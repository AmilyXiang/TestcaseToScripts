import argparse
import html
import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, List

from openai import OpenAI


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_prompt(skill_text: str, case_obj: Dict[str, Any]) -> str:
    return (
        "Follow the skill below and normalize each step item.\\n"
        "Important: output natural, automation-ready sentences, not compressed tokens.\\n\\n"
        "Skill:\\n"
        f"{skill_text}\\n\\n"
        "Return strict JSON with this schema:\\n"
        "{\"steps\": [{\"step_no\": int, \"normalized_action\": str, \"normalized_expected_result\": str, \"keywords\": [str]}]}\\n\\n"
        "Hard constraints:\\n"
        "- Keep same number of steps as input.\\n"
        "- Keep each step_no unchanged.\\n"
        "- Preserve domain literals and product terms.\\n"
        "- Use imperative sentence for normalized_action.\\n"
        "- Use verifiable assertion sentence for normalized_expected_result.\\n"
        "- Never output keyword-only fragments.\\n\\n"
        "Canonicalization requirement:\\n"
        "- Semantically equivalent phrasings must be normalized to the same sentence.\\n"
        "- Example: 'Receive a normal incoming call on the phone.' and 'Receive an incoming call on the phone.' must map to 'Phone receives an incoming call.'.\\n"
        "- Keep actor explicit and correct: Phone / Remote side / User.\\n"
        "- 'Remote side answers the call' must not be rewritten as 'Phone receives an answer'.\\n"
        "- Keep ALE model identifiers exact and distinct: ALE-20, ALE-20h, ALE-30, ALE-30h, ALE-300, ALE-400, ALE-500.\\n"
        "- OXE is server-side context; statements after OXE must remain server-side configure/check actions.\\n"
        "- Do not merge opposite actions (e.g., pick up vs hang up).\\n\\n"
        "Input case:\\n"
        f"{json.dumps(case_obj, ensure_ascii=False)}"
    )


def cleanup_markup_text(text: Any) -> Any:
    """Remove HTML/markdown artifacts while preserving meaningful sentence content."""
    if not isinstance(text, str):
        return text

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = html.unescape(normalized)

    # Remove markdown image tokens.
    normalized = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", normalized)

    # Convert paragraph and line-break tags to line boundaries.
    normalized = re.sub(r"<\s*br\s*/?\s*>", "\n", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"<\s*/\s*p\s*>\s*<\s*p\s*>", "\n", normalized, flags=re.IGNORECASE)

    # Remove non-semantic HTML tags but keep content.
    normalized = re.sub(r"<\s*img[^>]*>", "", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"<[^>]+>", "", normalized)

    # Normalize whitespace and blank lines.
    normalized = re.sub(r"[ \t]+", " ", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    normalized = "\n".join(line.strip() for line in normalized.split("\n")).strip()

    return normalized


def canonicalize_action_text(text: Any) -> Any:
    if not isinstance(text, str):
        return text

    normalized = cleanup_markup_text(text)
    normalized = re.sub(r"\s+", " ", normalized.strip())

    # Canonicalize equivalent incoming-call phrasings with explicit actor.
    normalized = re.sub(
        r"^(Receive a normal incoming call on the phone|Receive an incoming call on the phone|Phone receives a normal incoming call(?: on the phone)?)\.?$",
        "Phone receives an incoming call.",
        normalized,
        flags=re.IGNORECASE,
    )

    # Canonicalize remote-side answer/reject events.
    normalized = re.sub(
        r"^(Answer the call from the remote side|Have the remote side answer the call|Receive an answer from the remote side|Receive an answer to the call from the remote side|Receive an answer from the remote side for the call)\.?$",
        "Remote side answers the call.",
        normalized,
        flags=re.IGNORECASE,
    )
    normalized = re.sub(
        r"^(Have the remote side reject the call|Remote side reject the call|Receive a reject from the remote side)\.?$",
        "Remote side rejects the call.",
        normalized,
        flags=re.IGNORECASE,
    )

    # Repair common actor drift from model generations.
    if re.search(r"remote side", normalized, flags=re.IGNORECASE) and re.search(r"incoming call", normalized, flags=re.IGNORECASE):
        normalized = "Phone receives an incoming call."

    # Normalize capitalization variants for common button names.
    normalized = re.sub(r"\bPress the silence button\.?$", "Press the Silence button.", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bPress the switch button\.?$", "Press the Switch button.", normalized, flags=re.IGNORECASE)

    # Canonical casing for common domain terms and labels.
    normalized = re.sub(r"\boxe\b", "OXE", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20h\b", "ALE-20h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30h\b", "ALE-30h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20\b", "ALE-20", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30\b", "ALE-30", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*300\b", "ALE-300", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*400\b", "ALE-400", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*500\b", "ALE-500", normalized, flags=re.IGNORECASE)

    normalized = re.sub(r"\btransfer\b", "Transfer", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bsilence\b", "Silence", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bswitch\b", "Switch", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bhold\b", "Hold", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\brelease\b", "Release", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bconference\b", "Conference", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bemergency\b", "Emergency", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bguard\b", "Guard", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\boperator\b", "Operator", normalized, flags=re.IGNORECASE)

    normalized = re.sub(r"\bphone\b", "phone", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bremote side\b", "Remote side", normalized, flags=re.IGNORECASE)

    # Ensure final sentence punctuation.
    if normalized and not re.search(r"[.!?]$", normalized):
        normalized += "."

    return normalized


def canonicalize_expected_text(text: Any) -> Any:
    if not isinstance(text, str):
        return text
    normalized = cleanup_markup_text(text)
    normalized = re.sub(r"\s+", " ", normalized.strip())
    normalized = re.sub(r"\boxe\b", "OXE", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20h\b", "ALE-20h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30h\b", "ALE-30h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20\b", "ALE-20", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30\b", "ALE-30", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*300\b", "ALE-300", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*400\b", "ALE-400", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*500\b", "ALE-500", normalized, flags=re.IGNORECASE)
    return normalized


def canonicalize_precondition_text(text: Any) -> Any:
    if text is None:
        return None
    if not isinstance(text, str):
        return text

    normalized = cleanup_markup_text(text)
    normalized = re.sub(r"\s+", " ", normalized.strip())
    normalized = re.sub(r"\boxe\b", "OXE", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20h\b", "ALE-20h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30h\b", "ALE-30h", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*20\b", "ALE-20", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*30\b", "ALE-30", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*300\b", "ALE-300", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*400\b", "ALE-400", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bale-?\s*500\b", "ALE-500", normalized, flags=re.IGNORECASE)
    return normalized or None


def canonicalize_keywords(values: Any) -> List[str]:
    if not isinstance(values, list):
        return []

    normalized: List[str] = []
    seen = set()
    for item in values:
        if not isinstance(item, str):
            continue
        token = item.strip().lower()
        token = re.sub(r"\s+", "-", token)
        token = re.sub(r"[^a-z0-9\-_/]", "", token)
        if not token or token in seen:
            continue
        seen.add(token)
        normalized.append(token)
    return normalized


def call_deepseek_case(
    client: OpenAI,
    model: str,
    skill_text: str,
    case_obj: Dict[str, Any],
    max_retries: int = 3,
) -> Dict[str, Any]:
    prompt = build_prompt(skill_text, case_obj)

    for attempt in range(1, max_retries + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                temperature=0.0,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a senior QA test normalization assistant. "
                            "You produce strict JSON only. "
                            "Your output must be natural, clear, and directly usable in automation scripts."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            content = response.choices[0].message.content
            if not content:
                raise ValueError("Empty response from model")
            parsed = json.loads(content)
            if "steps" not in parsed or not isinstance(parsed["steps"], list):
                raise ValueError("Model output missing 'steps' array")
            return parsed
        except Exception:
            if attempt >= max_retries:
                raise
            time.sleep(1.5 * attempt)

    raise RuntimeError("Unexpected retry loop state")


def build_knowledge_base(
    parsed_payload: Dict[str, Any],
    normalized_payload: Dict[str, Any],
) -> Dict[str, Any]:
    kb_entries: List[Dict[str, Any]] = []

    for sheet_name, cases in parsed_payload.items():
        for case in cases:
            case_id = case.get("case_id")
            title = case.get("title")
            precondition_raw = case.get("preconditions")
            precondition_normalized = canonicalize_precondition_text(precondition_raw)
            steps_by_no = {
                int(item.get("step_no")): item
                for item in normalized_payload[sheet_name][case_id]["steps"]
            }

            for step in case.get("steps", []):
                step_no = int(step.get("step_no"))
                normalized = steps_by_no.get(step_no, {})
                kb_entries.append(
                    {
                        "sheet": sheet_name,
                        "case_id": case_id,
                        "title": title,
                        "precondition_raw": precondition_raw,
                        "normalized_precondition": precondition_normalized,
                        "step_no": step_no,
                        "raw_action": step.get("action"),
                        "raw_expected_result": step.get("expected_result"),
                        "normalized_action": normalized.get("normalized_action"),
                        "normalized_expected_result": normalized.get("normalized_expected_result"),
                        "keywords": normalized.get("keywords", []),
                    }
                )

    return {
        "meta": {
            "total_entries": len(kb_entries),
            "description": "Knowledge base entries for normalized test steps and expected results.",
        },
        "entries": kb_entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build normalized step/expected-result knowledge base from parsed TestRail JSON using DeepSeek API."
    )
    parser.add_argument("--input", type=Path, default=Path("parsed_testrail.json"))
    parser.add_argument("--skill", type=Path, default=Path("skills/step_result_unify_skill.md"))
    parser.add_argument("--output", type=Path, default=Path("normalized_kb.json"))
    parser.add_argument("--model", type=str, default="deepseek-chat")
    parser.add_argument("--api-key", type=str, default=None, help="DeepSeek API key (optional, otherwise use DEEPSEEK_API_KEY env var).")
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise EnvironmentError("Missing DEEPSEEK_API_KEY environment variable")

    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    client = OpenAI(api_key=api_key, base_url=base_url)

    parsed_payload = load_json(args.input)
    skill_text = args.skill.read_text(encoding="utf-8")

    normalized_payload: Dict[str, Dict[str, Any]] = {}

    for sheet_name, cases in parsed_payload.items():
        normalized_payload[sheet_name] = {}
        for case in cases:
            case_id = case.get("case_id")
            case_obj = {
                "case_id": case_id,
                "title": cleanup_markup_text(case.get("title")),
                "description": cleanup_markup_text(case.get("description")),
                "preconditions": cleanup_markup_text(case.get("preconditions")),
                "steps": [
                    {
                        "step_no": item.get("step_no"),
                        "action": cleanup_markup_text(item.get("action")),
                        "expected_result": cleanup_markup_text(item.get("expected_result")),
                    }
                    for item in case.get("steps", [])
                ],
            }
            normalized_case = call_deepseek_case(
                client=client,
                model=args.model,
                skill_text=skill_text,
                case_obj=case_obj,
            )

            for item in normalized_case.get("steps", []):
                item["normalized_action"] = canonicalize_action_text(item.get("normalized_action"))
                item["normalized_expected_result"] = canonicalize_expected_text(item.get("normalized_expected_result"))
                item["keywords"] = canonicalize_keywords(item.get("keywords", []))

            normalized_payload[sheet_name][case_id] = normalized_case
            print(f"Normalized case: {case_id}")

    kb = build_knowledge_base(parsed_payload, normalized_payload)
    save_json(args.output, kb)

    print(f"Output KB: {args.output}")
    print(f"Total entries: {kb['meta']['total_entries']}")


if __name__ == "__main__":
    main()
