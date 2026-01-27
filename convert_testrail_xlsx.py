from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

from pytest_generator import load_step_mapping, render_pytest_module
from testrail_xlsx_parser import parse_testrail_xlsx


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert a TestRail XLSX export into pytest test modules.")
    parser.add_argument("--input", required=True, help="Path to TestRail XLSX export")
    parser.add_argument("--sheet", default=None, help="Optional sheet name; default: all sheets")
    parser.add_argument("--out-dir", default="tests", help="Output directory for generated pytest module")
    parser.add_argument("--module", default="testrail_generated", help="Base module name")
    parser.add_argument("--cases-json", default="generated_cases.json", help="Write normalized cases JSON to this file")
    parser.add_argument("--mapping", default="step_mapping.yaml", help="Step mapping YAML (natural language -> SSH commands)")
    parser.add_argument("--enrich", dest="enrich", action="store_true", help="Enrich steps with Copilot/OpenAI analysis")
    parser.add_argument("--no-enrich", dest="enrich", action="store_false", help="Disable step enrichment")
    parser.set_defaults(enrich=True)
    parser.add_argument("--enriched-json", default="enriched_cases.json", help="Write AI-enriched cases JSON to this file")
    parser.add_argument("--enrich-cache", default=".enrich_cache.json", help="Cache file for step enrichment")
    parser.add_argument("--enrich-model", default="deepseek-chat", help="LLM model name for enrichment")
    parser.add_argument("--enrich-base-url", default="https://api.deepseek.com", help="Override LLM base URL (optional)")
    parser.add_argument("--enrich-api-key", default="sk-025ea794c18e430d82852de4a700baac", help="Override API key (optional)")
    parser.add_argument("--enrich-batch-size", type=int, default=5, help="Batch size for enrichment calls")
    parser.add_argument("--enrich-max-steps", type=int, default=0, help="Limit number of steps to enrich (0 = all)")
    parser.add_argument("--enrich-retries", type=int, default=3, help="Retry count for failed enrichment calls")
    parser.add_argument("--enrich-temperature", type=float, default=0.2, help="LLM temperature for enrichment")
    args = parser.parse_args()

    xlsx_path = Path(args.input)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    cases = parse_testrail_xlsx(xlsx_path, sheet=args.sheet)

    cases_json_path = out_dir / args.cases_json
    cases_json_path.write_text(
        json.dumps(
            [
                {
                    "title": c.title,
                    "preconditions": c.preconditions,
                    "steps": [{"step": s.step, "expected": s.expected} for s in c.steps],
                }
                for c in cases
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Parsed cases: {len(cases)}")
    print(f"Wrote: {cases_json_path}")
    if args.enrich:
        enriched_path = out_dir / args.enriched_json
        cache_path = out_dir / args.enrich_cache
        _enrich_cases(
            cases=cases,
            enriched_path=enriched_path,
            cache_path=cache_path,
            model=args.enrich_model,
            base_url=args.enrich_base_url,
            api_key=args.enrich_api_key,
            batch_size=max(1, args.enrich_batch_size),
            max_steps=args.enrich_max_steps,
            retries=max(1, args.enrich_retries),
            temperature=args.enrich_temperature,
        )
        print(f"Wrote: {enriched_path}")
    mapping_rules = load_step_mapping(args.mapping)
    cases_payload = None
    if args.enrich:
        enriched_path = out_dir / args.enriched_json
        if enriched_path.exists():
            cases_payload = json.loads(enriched_path.read_text(encoding="utf-8"))
    module_code = render_pytest_module(
        module_name=args.module,
        cases=cases,
        mapping_rules=mapping_rules,
        cases_payload=cases_payload,
    )

    module_path = out_dir / f"test_{args.module}.py"
    module_path.write_text(module_code, encoding="utf-8")

    print(f"Wrote: {module_path}")
    print("Next: edit step_mapping.yaml to automate steps via SSH.")
    return 0


def _step_key(title: str, preconditions: str, step: str, expected: str) -> str:
    payload = f"{title}\n{preconditions}\n{step}\n{expected}".encode("utf-8")
    return hashlib.sha1(payload).hexdigest()


def _extract_json(text: str) -> str:
    # Remove markdown code blocks
    original_text = text
    if "```json" in text:
        text = text.split("```json", 1)[1]
        if "```" in text:
            text = text.split("```", 1)[0]
    elif "```" in text:
        parts = text.split("```")
        for part in parts:
            content = part.strip()
            if content and not content.startswith(('json', 'JSON')):
                if content.startswith("{") or content.startswith("["):
                    text = content
                    break
    
    text = text.strip()
    
    # Try to fix truncated JSON arrays
    if text.startswith("[") and not text.endswith("]"):
        # Find the last complete object within the array
        depth = 0
        last_complete_idx = -1
        in_string = False
        last_string_start = -1
        i = 0
        
        while i < len(text):
            char = text[i]
            
            if char == "\\" and i + 1 < len(text):
                # Skip escaped characters
                i += 2
                continue
            
            if char == '"':
                if in_string:
                    # String ends
                    in_string = False
                    last_string_start = -1
                else:
                    # String starts
                    in_string = True
                    last_string_start = i
            
            if not in_string:
                if char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                    # Mark as complete when object closes at depth 0
                    if depth == 0:
                        last_complete_idx = i
            
            i += 1
        
        # If we're still in a string at the end, it's truncated
        # Go back to before the last string started
        if in_string and last_string_start > 0:
            # Find the last complete object before this truncated string
            # Search backwards from last_string_start
            temp_depth = 0
            temp_in_string = False
            temp_last_complete = -1
            j = 0
            while j < last_string_start:
                c = text[j]
                if c == "\\" and j + 1 < last_string_start:
                    j += 2
                    continue
                if c == '"':
                    temp_in_string = not temp_in_string
                if not temp_in_string:
                    if c == "{":
                        temp_depth += 1
                    elif c == "}":
                        temp_depth -= 1
                        if temp_depth == 0:
                            temp_last_complete = j
                j += 1
            last_complete_idx = temp_last_complete
        
        if last_complete_idx > 0:
            text = text[:last_complete_idx + 1] + "\n]"
    
    return text


def _enrich_cases(
    *,
    cases,
    enriched_path: Path,
    cache_path: Path,
    model: str,
    base_url: str | None,
    api_key: str | None,
    batch_size: int,
    max_steps: int,
    retries: int,
    temperature: float,
) -> None:
    from ai_mapping_assistant import LLMClient

    cache: dict[str, dict] = {}
    if cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))

    system_prompt = """You are a test automation expert for Alcatel-Lucent VoIP phones via SSH.

**CRITICAL: Generate REAL executable SSH commands, NOT descriptions!**
**IMPORTANT: Keep commands concise - use loops or better alternatives instead of repeating the same command many times!**

**Device Models (IMPORTANT for command selection):**
- **ALE-500**: Pure touchscreen device - MUST use `key ts` commands, NO physical keys
- **ALE-400**: Hybrid device - Can use both `key ts` (touchscreen) AND `key sim` (physical keys)
- **ALE-300/ALE-30**: Physical keys only - MUST use `key sim` commands, NO touchscreen

**Available Commands:**

1. **Key Simulation - Physical Hardware Keys (key sim):**
   - Syntax: `key sim <KEY> [short|long]`
   - **Use for PHYSICAL HARDWARE buttons only!**
   - **Keyboard Keys**: 0-9, A-Z, BS, TAB, ENTER, SPACE, F8-F12, LEFTCTRL, LEFTSHIFT, RIGHTSHIFT, LEFTALT, etc.
   - **Keypad Keys**: KP_0 to KP_9, KP_*, KP_#, KP_F1-F4, KP_PHONE, KP_VOICEMAIL, KP_MENU, KP_HANGUP
   - **Softkeys**: SOFTK0 to SOFTK9
   - **Navigation (Picwheel)**: PW_UP, PW_DOWN, PW_LEFT, PW_RIGHT, PW_OK, PW_HOME, PW_AUDIO, PW_MUTE, PW_VOLUME_UP, PW_VOLUME_DOWN
   - **Android Keys**: ANDROID_BACK, ANDROID_HOMEPAGE, ANDROID_TASKMANAGER
   - **Handset/Hook**: HOOKON, HOOKOFF, BTH_HOOKON, BTH_HOOKOFF
   - **Headset**: USB0_HOOKON, USB0_HOOKOFF, USB0_MUTE, USB0_VOL_UP, USB0_VOL_DOWN, BTHEADSET_HOOKON, BTHEADSET_HOOKOFF
   - Examples:
     * Press physical menu button: `key sim KP_MENU`
     * Long press home button: `key sim PW_HOME long`
     * Dial with keypad: `key sim KP_1; key sim KP_2; key sim KP_3; key sim KP_PHONE`
     * Navigate with physical keys: `key sim PW_DOWN; key sim PW_DOWN; key sim PW_DOWN` (max 3-5 repetitions)
     * Pick up handset: `key sim HOOKOFF` or `key sim KP_PHONE`
     * Hang up: `key sim HOOKON` or `key sim KP_HANGUP`

2. **Touch Screen Click - On-Screen Buttons (key ts):**
   - Syntax: `key ts "<regex>" [<nth>]`
   - **Use for TOUCHSCREEN buttons, Program Keys, and on-screen elements!**
   - **NOT for physical hardware buttons!**
   - Examples:
     * Click on-screen "Contacts" button: `key ts "Contacts"`
     * Click program key: `key ts "Emergency"` or `key ts "Speed Dial 1"`
     * Click 2nd "Call" button: `key ts "Call" 2`
     * Click menu item: `key ts "Settings"`
   - **PREFER touch screen over many navigation key presses on touchscreen models!**

3. **Screen Verification:**
   - Syntax: `screen_dump [standard|raw|softkey|debug]`
   - Examples:
     * Check display: `screen_dump | grep "Emergency"`
     * Verify softkey: `screen_dump softkey | grep "OK"`

4. **Audio Control:**
   - `voicemode set handset|handsfree|idle`
   - `mute`

5. **Call Operations:**
   - **Manual Dialing (typing number):**
     * Dial digits: `key sim KP_1; key sim KP_2; key sim KP_3`
     * Then press OK to call: `key sim PW_OK` or `key sim KP_PHONE`
     * Full example: `key sim KP_1; key sim KP_2; key sim KP_3; key sim PW_OK`
   - **Program Key Speed Dial:**
     * Press Program Key directly (NO need to press OK): `key ts "Speed Dial 1"` or `key sim SOFTK0`
     * Program Key automatically initiates call
   - **Direct call command:** `call set <number>`
   - **Hang up:** `call drop` or `key sim KP_HANGUP` or `key sim HOOKON`
   - **Answer incoming call:** `call answer` or `key sim KP_PHONE` or `key sim HOOKOFF`

**CRITICAL RULES:**
- Keep suggested_commands array concise (1-5 commands max per step)
- If you need to navigate many times, use touch screen instead
- Don't repeat the same command more than 3-5 times
- Prefer direct navigation (touch screen, menu shortcuts) over repeated key presses

**Input Format:**
Each test step contains:
- `step`: The action to perform (e.g., "Press menu button")
- `expected`: The expected result to verify (e.g., "Display shows Settings menu")
- `title`, `preconditions`: Context about the test case

**IMPORTANT: Use BOTH 'step' and 'expected' fields together!**
- The `step` tells you WHAT to do → Generate action commands
- The `expected` tells you WHAT to verify → Generate verification commands (screen_dump, grep, etc.)
- ALWAYS consider the expected result when generating commands!

**Output Format:**
Return a JSON array with these fields for each step:
- `id`: (required) Original step identifier
- `intent`: (string) Action category (e.g., "press_key", "verify_display", "call_control")
- `suggested_commands`: (array of strings) **REAL SSH commands**, not descriptions! Keep concise!
- `confidence`: (0-1) How confident you are
- `explanation`: (string) Brief reasoning
- `automation`: "automatable" | "manual" | "needs_context"

**Examples:**
Input: {"step": "Press empty program key", "expected": "Display key type choice screen"}
Output: {"suggested_commands": ["key sim SOFTK0", "screen_dump | grep 'Choose your programmable key'"], "intent": "press_key", ...}

Input: {"step": "Long press the alarm button", "expected": "Phone enters emergency mode"}
Output: {"suggested_commands": ["key sim USB0_BIS long", "screen_dump | grep -i 'emergency'"], "intent": "press_key", ...}

Input: {"step": "Press Emergency call", "expected": "Display the create key screen"}
Output: {"suggested_commands": ["key ts \"Emergency\"", "screen_dump | grep 'Create'"], "intent": "press_key", ...}

Input: {"step": "Verify display shows Emergency", "expected": "Emergency text is visible"}
Output: {"suggested_commands": ["screen_dump | grep 'Emergency'"], "intent": "verify_display", ...}

**Return ONLY valid JSON array, no markdown, no explanations outside JSON.**"""

    client = LLMClient(api_key=api_key, base_url=base_url, model=model)

    enriched_cases: list[dict] = []
    total_steps = 0

    def write_cache() -> None:
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

    def call_batch(batch_items: list[dict]) -> list[dict]:
        user_prompt = (
            "Analyze the following items and return a JSON array with the same length/order. "
            "Each output must include the same id.\n\n" + json.dumps(batch_items, ensure_ascii=False)
        )
        last_err: Exception | None = None
        last_response = ""
        for attempt in range(1, retries + 1):
            try:
                response = client.chat(system_prompt, user_prompt, temperature=temperature, max_tokens=8000)
                last_response = response
                json_text = _extract_json(response)
                if not json_text:
                    raise ValueError(f"Empty response from LLM. Raw response length: {len(response)}")
                parsed = json.loads(json_text)
                if not isinstance(parsed, list):
                    raise ValueError("LLM response is not a JSON array")
                return parsed
            except Exception as exc:  # noqa: BLE001
                print(f"Attempt {attempt} failed: {exc}")
                print(f"Response length: {len(last_response)}")
                print(f"Response preview: {last_response[:800]}")
                print(f"Extracted JSON preview: {json_text[:500] if json_text else 'EMPTY'}")
                if attempt < retries:
                    print(f"Retrying in {0.5 * attempt} seconds...")
                last_err = exc
                time.sleep(0.5 * attempt)
        raise RuntimeError(f"Enrichment failed after {retries} attempts: {last_err}")

    for case in cases:
        steps_out: list[dict] = []
        batch: list[dict] = []

        for step in case.steps:
            if max_steps and total_steps >= max_steps:
                break

            total_steps += 1
            key = _step_key(case.title, case.preconditions, step.step, step.expected)
            cached = cache.get(key)
            if cached:
                steps_out.append(
                    {
                        "step": step.step,
                        "expected": step.expected,
                        **cached,
                    }
                )
                continue

            batch.append(
                {
                    "id": key,
                    "title": case.title,
                    "preconditions": case.preconditions,
                    "step": step.step,
                    "expected": step.expected,
                }
            )

            if len(batch) >= batch_size:
                results = call_batch(batch)
                result_map = {r.get("id"): r for r in results if isinstance(r, dict)}
                for item in batch:
                    rid = item["id"]
                    data = result_map.get(rid)
                    if not data:
                        data = {
                            "id": rid,
                            "intent": "unknown",
                            "suggested_commands": [],
                            "confidence": 0.0,
                            "explanation": "No valid response from LLM",
                            "automation": "needs_context",
                        }
                    cache[rid] = {
                        "intent": data.get("intent", "unknown"),
                        "suggested_commands": data.get("suggested_commands", []),
                        "confidence": data.get("confidence", 0.0),
                        "explanation": data.get("explanation", ""),
                        "automation": data.get("automation", "needs_context"),
                    }
                    steps_out.append(
                        {
                            "step": item["step"],
                            "expected": item["expected"],
                            **cache[rid],
                        }
                    )
                write_cache()
                batch = []

        if batch:
            results = call_batch(batch)
            result_map = {r.get("id"): r for r in results if isinstance(r, dict)}
            for item in batch:
                rid = item["id"]
                data = result_map.get(rid)
                if not data:
                    data = {
                        "id": rid,
                        "intent": "unknown",
                        "suggested_commands": [],
                        "confidence": 0.0,
                        "explanation": "No valid response from LLM",
                        "tags": ["llm_error"],
                        "automation": "needs_context",
                    }
                cache[rid] = {
                    "intent": data.get("intent", "unknown"),
                    "suggested_commands": data.get("suggested_commands", []),
                    "confidence": data.get("confidence", 0.0),
                    "explanation": data.get("explanation", ""),
                    "automation": data.get("automation", "needs_context"),
                }
                steps_out.append(
                    {
                        "step": item["step"],
                        "expected": item["expected"],
                        **cache[rid],
                    }
                )
            write_cache()

        enriched_cases.append(
            {
                "title": case.title,
                "preconditions": case.preconditions,
                "steps": steps_out,
            }
        )

        if max_steps and total_steps >= max_steps:
            break

    enriched_path.write_text(json.dumps(enriched_cases, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
