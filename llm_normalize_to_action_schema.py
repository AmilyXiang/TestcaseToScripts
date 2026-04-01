from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, List

from openai import OpenAI


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_allowed_actions(path: Path) -> set[str]:
    return load_registry_section(path, "action", default_extra={"custom_action"})


def load_allowed_assertions(path: Path) -> set[str]:
    return load_registry_section(path, "assertion")


def load_registry_section(path: Path, section_key: str, default_extra: set[str] | None = None) -> set[str]:
    payload = load_json(path)
    if not isinstance(payload, dict):
        return set()

    root = payload.get(section_key)
    if not isinstance(root, dict):
        annotations_root = payload.get("annotations", {})
        root = annotations_root.get(section_key, {}) if isinstance(annotations_root, dict) else {}

    if not isinstance(root, dict):
        return set()

    items: set[str] = set()
    if default_extra:
        items.update(default_extra)

    for _, values in root.items():
        if isinstance(values, list):
            for item in values:
                if isinstance(item, str) and item.strip():
                    items.add(item.strip())
        elif isinstance(values, dict):
            for item in values.keys():
                if isinstance(item, str) and item.strip():
                    items.add(item.strip())
    return items


def load_synonym_resolver(path: Path | None) -> Dict[str, Any]:
    if not path or not path.exists():
        return {"phrase_to_action": {}, "phrase_to_assertion": {}}

    payload = load_json(path)
    if not isinstance(payload, dict):
        return {"phrase_to_action": {}, "phrase_to_assertion": {}}

    action_intents = payload.get("action_intents", {})
    assertion_intents = payload.get("assertion_intents", {})
    primitive_root = payload.get("intent_to_primitive", {})
    action_primitive_map = primitive_root.get("action", {}) if isinstance(primitive_root, dict) else {}
    assertion_primitive_map = primitive_root.get("assertion", {}) if isinstance(primitive_root, dict) else {}

    if not isinstance(action_intents, dict) or not isinstance(action_primitive_map, dict):
        action_intents = {}
        action_primitive_map = {}
    if not isinstance(assertion_intents, dict) or not isinstance(assertion_primitive_map, dict):
        assertion_intents = {}
        assertion_primitive_map = {}

    phrase_to_action: Dict[str, str] = {}
    for intent, phrases in action_intents.items():
        primitive = action_primitive_map.get(intent)
        if not isinstance(primitive, str) or "." not in primitive:
            continue
        action = primitive.split(".")[-1].strip()
        if not action:
            continue

        key_intent = str(intent).strip().lower()
        if key_intent:
            phrase_to_action[key_intent] = action

        if isinstance(phrases, list):
            for p in phrases:
                if isinstance(p, str) and p.strip():
                    phrase_to_action[p.strip().lower()] = action

    phrase_to_assertion: Dict[str, str] = {}
    for intent, phrases in assertion_intents.items():
        primitive = assertion_primitive_map.get(intent)
        if not isinstance(primitive, str) or "." not in primitive:
            continue
        assertion = primitive.split(".")[-1].strip()
        if not assertion:
            continue

        key_intent = str(intent).strip().lower()
        if key_intent:
            phrase_to_assertion[key_intent] = assertion

        if isinstance(phrases, list):
            for p in phrases:
                if isinstance(p, str) and p.strip():
                    phrase_to_assertion[p.strip().lower()] = assertion

    return {
        "phrase_to_action": phrase_to_action,
        "phrase_to_assertion": phrase_to_assertion,
    }


def first_n_case_ids(entries: List[Dict[str, Any]], limit: int) -> List[str]:
    ids: List[str] = []
    seen: set[str] = set()
    for e in entries:
        cid = e.get("case_id")
        if not isinstance(cid, str) or not cid.strip() or cid in seen:
            continue
        ids.append(cid)
        seen.add(cid)
        if len(ids) >= limit:
            break
    return ids


def build_prompt(
    skill_text: str,
    action_text: str,
    expected_text: str,
    allowed_actions: List[str],
    allowed_assertions: List[str],
) -> str:
    prompt = (
        skill_text.replace("{normalized_action}", action_text)
        .replace("{normalized_expected_result}", expected_text)
        .replace("{allowed_actions}", json.dumps(allowed_actions, ensure_ascii=False))
        .replace("{allowed_assertions}", json.dumps(allowed_assertions, ensure_ascii=False))
    )
    return prompt


def resolve_action_with_synonyms(
    action: str,
    action_text: str,
    resolver: Dict[str, Any],
    allowed_actions: set[str],
) -> tuple[str, str]:
    # Trust LLM when it picks a specific, non-generic allowed action
    if action in allowed_actions and action != "custom_action":
        return action, "llm_allowed"

    phrase_to_action = resolver.get("phrase_to_action", {}) if isinstance(resolver, dict) else {}
    if not isinstance(phrase_to_action, dict):
        phrase_to_action = {}

    # Try synonym lookup for both unrecognised actions AND custom_action outputs
    text = action_text.lower().strip()
    if text:
        for phrase, mapped_action in phrase_to_action.items():
            if phrase in text and mapped_action in allowed_actions and mapped_action != "custom_action":
                return mapped_action, f"synonym_match:{phrase}"

    return "custom_action", "no_allowed_or_synonym_match"


def extract_device_pair(text: str) -> tuple[str, str] | None:
    normalized = re.sub(r"\s+", " ", text.strip())
    patterns = [
        r"between\s+(.+?)\s+and\s+(.+?)(?:[\.;]|$)",
        r"(.+?)\s+and\s+(.+?)\s+are\s+(?:in\s+)?(?:communication|conversation|connected)(?:[\.;]|$)",
        r"communication\s+(?:is\s+)?(?:established|active)\s+with\s+(.+?)\s+and\s+(.+?)(?:[\.;]|$)",
    ]
    for p in patterns:
        m = re.search(p, normalized, flags=re.IGNORECASE)
        if not m:
            continue
        left = m.group(1).strip().rstrip(".")
        right = m.group(2).strip().rstrip(".")
        if left and right:
            return left, right
    return None


def resolve_expected_assertion(
    ex_action: str,
    ex_params: Dict[str, Any],
    expected_text: str,
    resolver: Dict[str, Any],
    allowed_assertions: set[str],
) -> tuple[str, Dict[str, Any], str]:
    if ex_action in allowed_assertions:
        return ex_action, ex_params, "llm_allowed"

    phrase_to_assertion = resolver.get("phrase_to_assertion", {}) if isinstance(resolver, dict) else {}
    if not isinstance(phrase_to_assertion, dict):
        phrase_to_assertion = {}

    text_candidates: List[str] = []
    for key in ("condition", "state", "content", "message", "tone"):
        v = ex_params.get(key)
        if isinstance(v, str) and v.strip():
            text_candidates.append(v.strip().lower())
    if expected_text.strip():
        text_candidates.append(expected_text.strip().lower())
    if ex_action.strip():
        text_candidates.append(ex_action.strip().lower())

    for text in text_candidates:
        for phrase, mapped_assertion in phrase_to_assertion.items():
            if phrase in text and mapped_assertion in allowed_assertions:
                return mapped_assertion, ex_params, f"synonym_match:{phrase}"

    merged_text = " ".join(text_candidates)
    has_conversation_signal = any(
        token in merged_text
        for token in [
            "communication",
            "conversation",
            "connected",
            "call established",
            "in comm",
        ]
    )
    if has_conversation_signal and "are_in_conversation" in allowed_assertions:
        pair = extract_device_pair(expected_text) or extract_device_pair(str(ex_params.get("condition", "")))
        if pair:
            return (
                "are_in_conversation",
                {"device_a": pair[0], "device_b": pair[1]},
                "semantic_conversation_pair",
            )

    return "custom_action", ex_params, "no_allowed_or_semantic_match"


def sanitize_schema(
    obj: Dict[str, Any],
    allowed_actions: set[str],
    allowed_assertions: set[str],
    action_text: str,
    expected_text: str,
    resolver: Dict[str, Any],
) -> Dict[str, Any]:
    raw_action = str(obj.get("action", "custom_action")).strip() or "custom_action"
    action, action_resolution = resolve_action_with_synonyms(raw_action, action_text, resolver, allowed_actions)

    params = obj.get("params", {})
    if not isinstance(params, dict):
        params = {}

    expected = obj.get("expected", [])
    cleaned_expected: List[Dict[str, Any]] = []
    if isinstance(expected, list):
        for item in expected:
            if not isinstance(item, dict):
                continue
            ex_action = str(item.get("action", "custom_action")).strip() or "custom_action"
            ex_params = item.get("params", {})
            if not isinstance(ex_params, dict):
                ex_params = {}

            ex_action, ex_params, _ = resolve_expected_assertion(
                ex_action=ex_action,
                ex_params=ex_params,
                expected_text=expected_text,
                resolver=resolver,
                allowed_assertions=allowed_assertions,
            )

            cleaned_expected.append({"action": ex_action, "params": ex_params})

    custom_reason = ""
    if action == "custom_action":
        if not action_text.strip() and expected_text.strip():
            custom_reason = "expected_only_step"
        elif not action_text.strip() and not expected_text.strip():
            custom_reason = "empty_action_and_expected"
        else:
            custom_reason = f"unmapped_action:{raw_action or 'empty'}"

    result = {
        "action": action,
        "params": params,
        "expected": cleaned_expected,
        "_meta": {
            "raw_action": raw_action,
            "resolution": action_resolution,
        },
    }
    if custom_reason:
        result["custom_reason"] = custom_reason
    return result


def call_llm_schema(
    client: OpenAI,
    model: str,
    prompt: str,
    max_retries: int = 3,
) -> Dict[str, Any]:
    for attempt in range(1, max_retries + 1):
        try:
            resp = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                temperature=0.0,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a strict JSON generator. Return JSON object only.",
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            content = resp.choices[0].message.content
            if not content:
                raise ValueError("Empty response from model")
            return json.loads(content)
        except Exception:
            if attempt >= max_retries:
                raise
            time.sleep(1.2 * attempt)

    raise RuntimeError("Unexpected retry loop state")


def run(
    input_path: Path,
    output_path: Path,
    skill_path: Path,
    capability_registry_path: Path,
    synonym_map_path: Path | None,
    case_limit: int,
    model: str,
    api_key: str,
    base_url: str,
) -> None:
    payload = load_json(input_path)
    entries = payload.get("entries", []) if isinstance(payload, dict) else []
    if not isinstance(entries, list):
        raise ValueError("Input file must contain entries array")

    skill_text = skill_path.read_text(encoding="utf-8")
    allowed_actions = load_allowed_actions(capability_registry_path)
    allowed_assertions = load_allowed_assertions(capability_registry_path)
    resolver = load_synonym_resolver(synonym_map_path)
    if not allowed_actions:
        raise ValueError("No allowed actions found in capability registry")
    allowed_actions_list = sorted(allowed_actions)
    allowed_assertions_list = sorted(allowed_assertions)

    selected_case_ids = set(first_n_case_ids(entries, case_limit))
    selected_entries = [e for e in entries if e.get("case_id") in selected_case_ids]

    client = OpenAI(api_key=api_key, base_url=base_url)

    output_rows: List[Dict[str, Any]] = []
    failed = 0
    empty_action_count = 0
    empty_expected_count = 0
    for e in selected_entries:
        case_id = e.get("case_id")
        step_no = e.get("step_no")
        sub_step_no = e.get("sub_step_no")
        action_text = str(e.get("normalized_action", "") or "")
        expected_text = str(e.get("normalized_expected_result", "") or "")
        has_action = bool(action_text.strip())
        has_expected = bool(expected_text.strip())

        if not has_action:
            empty_action_count += 1

        if not has_expected:
            empty_expected_count += 1

        if not has_action and not has_expected:
            output_rows.append(
                {
                    "case_id": case_id,
                    "step_no": step_no,
                    "sub_step_no": sub_step_no,
                    "normalized_action": action_text,
                    "normalized_expected_result": expected_text,
                    "skip_reason": "empty_normalized_action_and_expected_result",
                }
            )
            continue

        prompt = build_prompt(skill_text, action_text, expected_text, allowed_actions_list, allowed_assertions_list)

        try:
            raw = call_llm_schema(client, model, prompt)
            schema = sanitize_schema(raw, allowed_actions, allowed_assertions, action_text, expected_text, resolver)
            if not has_action:
                schema.pop("action", None)
                schema.pop("params", None)
                schema.pop("_meta", None)
                schema.pop("custom_reason", None)
            if not has_expected:
                # Keep action mapping but omit expected when normalized_expected_result is empty.
                schema.pop("expected", None)
        except Exception as ex:
            failed += 1
            schema = {
                "action": "custom_action",
                "params": {},
                "expected": [],
                "error": f"LLM mapping failed: {ex}",
            }

        output_rows.append(
            {
                "case_id": case_id,
                "step_no": step_no,
                "sub_step_no": sub_step_no,
                "normalized_action": action_text,
                "normalized_expected_result": expected_text,
                "action_schema": schema,
            }
        )

    result = {
        "meta": {
            "input_file": str(input_path),
            "skill_file": str(skill_path),
            "model": model,
            "selected_case_count": len(selected_case_ids),
            "selected_step_count": len(selected_entries),
            "failed_count": failed,
            "empty_action_count": empty_action_count,
            "empty_expected_result_count": empty_expected_count,
            "synonym_map": str(synonym_map_path) if synonym_map_path else None,
            "description": "Action schema generated from normalized steps via LLM.",
        },
        "rows": output_rows,
    }

    save_json(output_path, result)
    print(f"Selected cases: {len(selected_case_ids)}")
    print(f"Selected steps: {len(selected_entries)}")
    print(f"Empty-action steps: {empty_action_count}")
    print(f"Empty-expected steps: {empty_expected_count}")
    print(f"Failed mappings: {failed}")
    print(f"Output: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate action schema directly from normalized steps via LLM")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--skill", type=Path, default=Path("skills/normalize_to_action.md"))
    parser.add_argument("--capability-registry", type=Path, default=Path("resource/capability_registry.json"))
    parser.add_argument("--synonym-map", type=Path, default=Path("resource/synonym_map.json"))
    parser.add_argument("--case-limit", type=int, default=15)
    parser.add_argument("--model", type=str, default="deepseek-chat")
    parser.add_argument("--api-key", type=str, default=None)
    parser.add_argument("--base-url", type=str, default="https://api.deepseek.com")
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise EnvironmentError("Missing DeepSeek API key (use --api-key or DEEPSEEK_API_KEY)")

    run(
        input_path=args.input,
        output_path=args.output,
        skill_path=args.skill,
        capability_registry_path=args.capability_registry,
        synonym_map_path=args.synonym_map,
        case_limit=args.case_limit,
        model=args.model,
        api_key=api_key,
        base_url=args.base_url,
    )


if __name__ == "__main__":
    main()
