import argparse
import json
import os
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
        "Input case:\\n"
        f"{json.dumps(case_obj, ensure_ascii=False)}"
    )


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
                temperature=0.1,
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
                "title": case.get("title"),
                "preconditions": case.get("preconditions"),
                "steps": case.get("steps", []),
            }
            normalized_case = call_deepseek_case(
                client=client,
                model=args.model,
                skill_text=skill_text,
                case_obj=case_obj,
            )
            normalized_payload[sheet_name][case_id] = normalized_case
            print(f"Normalized case: {case_id}")

    kb = build_knowledge_base(parsed_payload, normalized_payload)
    save_json(args.output, kb)

    print(f"Output KB: {args.output}")
    print(f"Total entries: {kb['meta']['total_entries']}")


if __name__ == "__main__":
    main()
