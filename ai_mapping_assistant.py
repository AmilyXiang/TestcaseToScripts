"""
AI-assisted step-to-SSH mapping generator.

This module uses LLM (e.g., OpenAI GPT, Azure OpenAI, or compatible local models)
to analyze natural-language test steps and suggest SSH command mappings.

Output is always a *suggestion* that requires human review before adoption.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class StepAnalysis:
    """Analysis result for a single test step."""

    original_step: str
    intent: str  # e.g., "execute_command", "check_log", "check_config", "reboot_verify", "ui_action", "unknown"
    suggested_commands: list[str]
    confidence: float  # 0.0 ~ 1.0
    explanation: str


@dataclass
class MappingRule:
    """A suggested mapping rule (pattern -> commands)."""

    pattern: str  # regex pattern
    commands: list[str]
    description: str
    source_steps: list[str]  # original steps that led to this rule


# ---------------------------------------------------------------------------
# LLM client abstraction
# ---------------------------------------------------------------------------


class LLMClient:
    """Wrapper around OpenAI-compatible API (supports GitHub Models with Copilot license)."""

    # GitHub Models endpoint for Copilot users
    GITHUB_MODELS_URL = "https://models.inference.ai.azure.com"

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str = "gpt-4o-mini",
        use_github_models: bool | None = None,
    ):
        from openai import OpenAI

        # Auto-detect: if GITHUB_TOKEN is set, use GitHub Models
        github_token = os.environ.get("GITHUB_TOKEN")
        openai_key = os.environ.get("OPENAI_API_KEY")

        if use_github_models is None:
            use_github_models = bool(github_token) and not openai_key

        if use_github_models:
            # Use GitHub Models (for Copilot license holders)
            self.api_key = api_key or github_token
            self.base_url = base_url or self.GITHUB_MODELS_URL
            if not self.api_key:
                raise ValueError(
                    "No GitHub token provided. Set GITHUB_TOKEN env var.\n"
                    "Get your token at: https://github.com/settings/tokens\n"
                    "Required scope: (no special scope needed for GitHub Models)"
                )
            print(f"Using GitHub Models (Copilot license) at {self.base_url}")
        else:
            # Use OpenAI or compatible API
            self.api_key = api_key or openai_key
            self.base_url = base_url or os.environ.get("OPENAI_BASE_URL")
            if not self.api_key:
                raise ValueError(
                    "No API key provided.\n"
                    "Option 1: Set GITHUB_TOKEN for GitHub Models (Copilot license)\n"
                    "Option 2: Set OPENAI_API_KEY for OpenAI API"
                )

        self.model = model

        client_kwargs: dict[str, Any] = {"api_key": self.api_key}
        if self.base_url:
            client_kwargs["base_url"] = self.base_url

        self._client = OpenAI(**client_kwargs)

    def chat(self, system_prompt: str, user_prompt: str, temperature: float = 0.2, max_tokens: int | None = None) -> str:
        chat_params = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": temperature,
        }
        if max_tokens:
            chat_params["max_tokens"] = max_tokens
        response = self._client.chat.completions.create(**chat_params)
        content = response.choices[0].message.content or ""
        # Check if response was truncated
        if response.choices[0].finish_reason == "length":
            print(f"Warning: Response was truncated due to length limit. Consider increasing max_tokens.")
        return content


# ---------------------------------------------------------------------------
# AI Mapping Assistant
# ---------------------------------------------------------------------------

SYSTEM_PROMPT_ANALYZE = """\
You are an expert in Alcatel-Lucent (ALE) VoIP phone testing. You help convert manual test steps into automated SSH commands.

**Device Context:**
- This is an Alcatel-Lucent Enterprise VoIP phone (embedded Linux-based device)
- SSH provides direct shell access with standard Linux commands available

**Real Command Reference (USE THESE EXACT FORMATS):**

**Key Press Operations:**
- Short press: `aommgr shortpress 0 {{KEY}}`
- Long press: `aommgr longpress 0 {{KEY}}`
- Key values have KP_ prefix: KP_F1, KP_F2, KP_F3, KP_F4, KP_MENU, KP_PHONE, KP_HANGUP, KP_VOICEMAIL, etc.
- Example: `aommgr shortpress 0 KP_MENU`

**Audio/Voice Mode:**
- Set handset: `voicemode set handset`
- Set handsfree: `voicemode set handsfree`
- Set idle: `voicemode set idle`
- Mute: `mute`

**Screen/Display:**
- Get screen text: `screen_dump`
- Screenshot: `fbgrabjpg screen.jpg`
- Capture screen: `screen get`
- Check for icon on screen: `screen_dump | grep '{{ICON_NAME}}'`
- Common icons: icon_emergency, icon_guard, icon_operator, icon_call, icon_incoming_call, 
  icon_outgoing_call, icon_hold, icon_hangup, icon_conference, icon_transfer, icon_contacts,
  icon_call_log, icon_menu, icon_voicemail, icon_dnd, icon_handsfree, icon_headset_usb, etc.

**Log Files:**
- SIP module log: `/var/log/SIPModule.log`
- Upgrade log: `/data/log/upgrade.log`
- Reset log: `/data/log/Reset.log`
- Check logs: `cat /var/log/SIPModule.log | grep '{{KEYWORD}}'`

**Database (Call logs, Contacts, Program keys):**
- Query call logs: `sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from calllogs"`
- Delete call logs: `sqlite3 /data/ICTApplication/sipapp/db/database.db "delete from calllogs"`
- Query contacts: `sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from contacts"`
- Query program keys: `sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from progkeys"`

**System Info:**
- Memory: `cat /proc/meminfo | grep MemFree`
- Date: `date`
- Processes: `ps | grep {{PROCESS}}`

Given a test step written in natural language, analyze it and provide:

1. intent: The category of this step. Choose from:
   - "voip_keypress": Press phone keys/buttons → `aommgr shortpress/longpress 0 KP_{{KEY}}`
   - "voip_audio_mode": Change audio mode → `voicemode set handset/handsfree/idle`
   - "voip_mute": Mute/unmute → `mute`
   - "check_display": Verify phone display/screen → `screen_dump | grep '{{TEXT}}'`
   - "check_call_log": Check call logs → `sqlite3 .../database.db "select * from calllogs" | grep '{{INFO}}'`
   - "check_sip_log": Check SIP logs → `cat /var/log/SIPModule.log | grep '{{KEYWORD}}'`
   - "check_config": Verify configuration values
   - "check_process": Check if a process/service is running
   - "check_memory": Check memory usage → `cat /proc/meminfo | grep MemFree`
   - "file_operation": Create/copy/delete files
   - "reboot_verify": Reboot device and verify state after
   - "physical_action": Physical action (pick up handset, plug cable) - CANNOT be automated
   - "remote_action": Action on remote side (remote answers call) - handled by test framework
   - "unknown": Cannot determine

2. suggested_commands: A list of SSH commands that could automate this step.
   - Use EXACT command formats from the reference above
   - Map button names to KP_ keys (Emergency→KP_MENU or specific key, Menu→KP_MENU, etc.)
   - For "Press X button": use `aommgr shortpress 0 KP_{{KEY}}`
   - For "Long press X": use `aommgr longpress 0 KP_{{KEY}}`
   - For checking display: `screen_dump | grep '{{TEXT}}'`
   - For checking call log: `sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from calllogs" | grep '{{TYPE}}'`
   - If truly a physical action (handset), return empty list

3. confidence: A number from 0.0 to 1.0 indicating how confident you are.

4. explanation: Brief explanation of your reasoning.

Respond ONLY with valid JSON in this exact format:
{
  "intent": "...",
  "suggested_commands": ["cmd1", "cmd2"],
  "confidence": 0.8,
  "explanation": "..."
}
"""

SYSTEM_PROMPT_GENERATE_RULES = """\
You are an expert in test automation. Given a list of test steps and their analyses, 
generate reusable regex-based mapping rules.

Each rule should:
1. Have a regex pattern that matches similar steps
2. Have a list of SSH commands (with placeholders where appropriate)
3. Be general enough to match multiple similar steps but specific enough to be accurate

Respond ONLY with valid JSON in this format:
{
  "rules": [
    {
      "pattern": "regex pattern here",
      "commands": ["cmd1", "cmd2"],
      "description": "What this rule does"
    }
  ]
}
"""


class AIMappingAssistant:
    """AI-powered assistant for generating step-to-SSH mappings."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str = "gpt-4o-mini",
    ):
        self._client = LLMClient(api_key=api_key, base_url=base_url, model=model)
        self._history: list[StepAnalysis] = []

    def analyze_step(self, step_text: str, context: str = "") -> StepAnalysis:
        """Analyze a single test step and suggest SSH commands."""
        user_prompt = f"Test step: {step_text}"
        if context:
            user_prompt += f"\n\nAdditional context (preconditions/expected result): {context}"

        response = self._client.chat(SYSTEM_PROMPT_ANALYZE, user_prompt)

        # Parse JSON response
        try:
            # Extract JSON from response (in case there's extra text)
            json_match = re.search(r"\{[\s\S]*\}", response)
            if json_match:
                data = json.loads(json_match.group())
            else:
                data = {}
        except json.JSONDecodeError:
            data = {}

        analysis = StepAnalysis(
            original_step=step_text,
            intent=data.get("intent", "unknown"),
            suggested_commands=data.get("suggested_commands", []),
            confidence=float(data.get("confidence", 0.0)),
            explanation=data.get("explanation", "Failed to parse LLM response"),
        )

        self._history.append(analysis)
        return analysis

    def analyze_steps_batch(
        self, steps: list[dict[str, str]], show_progress: bool = True
    ) -> list[StepAnalysis]:
        """Analyze multiple steps. Each dict should have 'step' and optionally 'expected'."""
        results: list[StepAnalysis] = []
        total = len(steps)

        for i, s in enumerate(steps, 1):
            step_text = s.get("step", "")
            context = s.get("expected", "")

            if not step_text.strip():
                continue

            if show_progress:
                print(f"[{i}/{total}] Analyzing: {step_text[:60]}...")

            analysis = self.analyze_step(step_text, context)
            results.append(analysis)

        return results

    def generate_mapping_rules(
        self, analyses: list[StepAnalysis] | None = None
    ) -> list[MappingRule]:
        """Generate reusable mapping rules from analyzed steps."""
        if analyses is None:
            analyses = self._history

        if not analyses:
            return []

        # Prepare input for LLM
        steps_data = [
            {
                "step": a.original_step,
                "intent": a.intent,
                "suggested_commands": a.suggested_commands,
            }
            for a in analyses
            if a.intent != "ui_action" and a.suggested_commands
        ]

        if not steps_data:
            return []

        user_prompt = f"Generate mapping rules from these analyzed steps:\n{json.dumps(steps_data, indent=2, ensure_ascii=False)}"

        response = self._client.chat(SYSTEM_PROMPT_GENERATE_RULES, user_prompt)

        # Parse response
        try:
            json_match = re.search(r"\{[\s\S]*\}", response)
            if json_match:
                data = json.loads(json_match.group())
            else:
                data = {"rules": []}
        except json.JSONDecodeError:
            data = {"rules": []}

        rules: list[MappingRule] = []
        for r in data.get("rules", []):
            rules.append(
                MappingRule(
                    pattern=r.get("pattern", ""),
                    commands=r.get("commands", []),
                    description=r.get("description", ""),
                    source_steps=[],
                )
            )

        return rules

    def export_suggested_mapping(
        self, rules: list[MappingRule], output_path: str | Path
    ) -> None:
        """Export suggested mapping rules to a YAML file for human review."""
        output_path = Path(output_path)

        data = {
            "_note": "AI-generated suggestions. Review and edit before using.",
            "rules": [
                {
                    "pattern": r.pattern,
                    "commands": r.commands,
                    "description": r.description,
                }
                for r in rules
            ],
        }

        output_path.write_text(
            yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False),
            encoding="utf-8",
        )
        print(f"Exported {len(rules)} suggested rules to: {output_path}")

    def export_analysis_report(
        self, analyses: list[StepAnalysis], output_path: str | Path
    ) -> None:
        """Export detailed analysis report as JSON for review."""
        output_path = Path(output_path)

        data = [
            {
                "step": a.original_step,
                "intent": a.intent,
                "suggested_commands": a.suggested_commands,
                "confidence": a.confidence,
                "explanation": a.explanation,
            }
            for a in analyses
        ]

        output_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"Exported analysis report ({len(analyses)} steps) to: {output_path}")


# ---------------------------------------------------------------------------
# CLI interface
# ---------------------------------------------------------------------------


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="AI-assisted step-to-SSH mapping generator"
    )
    parser.add_argument(
        "--cases-json",
        required=True,
        help="Path to generated_cases.json from convert_testrail_xlsx.py",
    )
    parser.add_argument(
        "--output-mapping",
        default="ai_suggested_mapping.yaml",
        help="Output path for suggested mapping rules",
    )
    parser.add_argument(
        "--output-report",
        default="ai_analysis_report.json",
        help="Output path for detailed analysis report",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="LLM model to use (default: gpt-4o-mini)",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=0,
        help="Max steps to analyze (0 = all). Use for testing.",
    )
    args = parser.parse_args()

    # Load cases
    cases_path = Path(args.cases_json)
    if not cases_path.exists():
        print(f"Error: {cases_path} not found")
        return 1

    cases = json.loads(cases_path.read_text(encoding="utf-8"))

    # Collect all unique steps
    all_steps: list[dict[str, str]] = []
    seen: set[str] = set()

    for case in cases:
        for s in case.get("steps", []):
            step_text = (s.get("step") or "").strip()
            if step_text and step_text not in seen:
                seen.add(step_text)
                all_steps.append(
                    {"step": step_text, "expected": (s.get("expected") or "").strip()}
                )

    print(f"Found {len(all_steps)} unique steps to analyze")

    if args.max_steps > 0:
        all_steps = all_steps[: args.max_steps]
        print(f"Limiting to {args.max_steps} steps for this run")

    # Initialize assistant
    try:
        assistant = AIMappingAssistant(model=args.model)
    except ValueError as e:
        print(f"Error: {e}")
        print("Set OPENAI_API_KEY environment variable or use a compatible API.")
        return 1

    # Analyze steps
    print("\n=== Analyzing steps ===")
    analyses = assistant.analyze_steps_batch(all_steps)

    # Generate rules
    print("\n=== Generating mapping rules ===")
    rules = assistant.generate_mapping_rules(analyses)

    # Export results
    assistant.export_analysis_report(analyses, args.output_report)
    assistant.export_suggested_mapping(rules, args.output_mapping)

    # Summary
    print("\n=== Summary ===")
    intent_counts: dict[str, int] = {}
    for a in analyses:
        intent_counts[a.intent] = intent_counts.get(a.intent, 0) + 1

    for intent, count in sorted(intent_counts.items(), key=lambda x: -x[1]):
        print(f"  {intent}: {count}")

    automatable = sum(1 for a in analyses if a.intent != "ui_action" and a.suggested_commands)
    print(f"\nAutomatable steps: {automatable}/{len(analyses)}")
    print(f"Generated rules: {len(rules)}")
    print(f"\nNext: Review {args.output_mapping} and merge into step_mapping.yaml")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
