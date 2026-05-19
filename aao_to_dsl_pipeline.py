from __future__ import annotations

import argparse
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Tuple

from openai import OpenAI
from dsl_validator import DSLValidator


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_capability_labels(path: Path, section: str) -> Dict[str, str]:
    """Return flat dict {capability_key: '[Category] description'} from registry annotations."""
    payload = load_json(path)
    labels: Dict[str, str] = {}
    root = payload.get("annotations", {}).get(section, {})
    if not root:
        root = payload.get(section, {})
    for category, items in root.items():
        if isinstance(items, dict):
            for key, desc in items.items():
                labels[key] = f"[{category}] {desc}" if isinstance(desc, str) else key
    return labels


def load_registry(path: Path, section_key: str, default_extra: set[str] | None = None) -> set[str]:
    payload = load_json(path)
    items: set[str] = set(default_extra or set())

    if not isinstance(payload, dict):
        return items

    root = payload.get(section_key)
    if not isinstance(root, dict):
        annotations_root = payload.get("annotations", {})
        root = annotations_root.get(section_key, {}) if isinstance(annotations_root, dict) else {}

    if isinstance(root, dict):
        for values in root.values():
            if isinstance(values, list):
                for item in values:
                    if isinstance(item, str) and item.strip():
                        items.add(item.strip())
            elif isinstance(values, dict):
                for item in values.keys():
                    if isinstance(item, str) and item.strip():
                        items.add(item.strip())
    return items


def load_synonym_maps(path: Path) -> tuple[Dict[str, str], Dict[str, str], Dict[str, str], Dict[str, str]]:
    payload = load_json(path)
    action_intents = payload.get("action_intents", {}) if isinstance(payload, dict) else {}
    assertion_intents = payload.get("assertion_intents", {}) if isinstance(payload, dict) else {}
    primitive_root = payload.get("intent_to_primitive", {}) if isinstance(payload, dict) else {}

    action_primitive = primitive_root.get("action", {}) if isinstance(primitive_root, dict) else {}
    assertion_primitive = primitive_root.get("assertion", {}) if isinstance(primitive_root, dict) else {}

    phrase_to_intent_action: Dict[str, str] = {}
    phrase_to_intent_assertion: Dict[str, str] = {}

    for intent, phrases in action_intents.items():
        if not isinstance(intent, str):
            continue
        phrase_to_intent_action[intent.strip().lower()] = intent
        if isinstance(phrases, list):
            for p in phrases:
                if isinstance(p, str) and p.strip():
                    phrase_to_intent_action[p.strip().lower()] = intent

    for intent, phrases in assertion_intents.items():
        if not isinstance(intent, str):
            continue
        phrase_to_intent_assertion[intent.strip().lower()] = intent
        if isinstance(phrases, list):
            for p in phrases:
                if isinstance(p, str) and p.strip():
                    phrase_to_intent_assertion[p.strip().lower()] = intent

    return phrase_to_intent_action, phrase_to_intent_assertion, action_primitive, assertion_primitive


# Only match "phone <single-letter>" or "phone <digit>" identifiers (e.g. phone A, phone B, phone 1).
# This avoids false positives like "phone or", "phone and", "phone in".
_DEVICE_RE = re.compile(r"\bphone\s+([a-z]|[0-9])\b")


def extract_devices(text: str) -> List[str]:
    return [m.group(0) for m in _DEVICE_RE.finditer(text.lower())]


def build_dsl_entry(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Build DSL entry as a pure passthrough — no hardcoded intent inference.
    Intent resolution is fully delegated to the LLM in compile_dsl_to_schema."""
    action_text = str(entry.get("normalized_action", "") or "")
    expected_text = str(entry.get("normalized_expected_result", "") or "")

    devices = extract_devices(action_text)
    actor = devices[0] if devices else "current_device"
    target = devices[1] if len(devices) > 1 else ""

    action_intent = "no_action" if not action_text.strip() else "pending_llm"
    expected_intent = "no_expected" if not expected_text.strip() else "pending_llm"

    return {
        "case_id": entry.get("case_id"),
        "step_no": entry.get("step_no"),
        "sub_step_no": entry.get("sub_step_no"),
        "dsl": {
            "action": {
                "intent": action_intent,
                "actor": actor,
                "target": target,
                "text": action_text,
            },
            "expected": {
                "intent": expected_intent,
                "text": expected_text,
            },
            "trace": {
                "title": entry.get("title"),
                "keywords": entry.get("keywords", []),
            },
        },
    }


def _format_capability_list(keys: set[str], labels: Dict[str, str]) -> str:
    """Format capability keys grouped by category for a structured LLM prompt.
    Labels are expected in the form '[Category] description'."""
    from collections import defaultdict
    by_category: Dict[str, List[str]] = defaultdict(list)
    for k in sorted(keys):
        label = labels.get(k, k)
        if "]" in label:
            cat = label.split("]")[0].lstrip("[")
            desc = label.split("]", 1)[1].strip()
        else:
            cat = "Other"
            desc = label
        by_category[cat].append(f"  - {k}: {desc}")
    lines: List[str] = []
    for cat in sorted(by_category.keys()):
        lines.append(f"[{cat}]")
        lines.extend(by_category[cat])
    return "\n".join(lines)


def _looks_like_state_step(text: str) -> bool:
    text_lower = text.strip().lower()
    if not text_lower:
        return False
    imperative_hints = [
        "press", "dial", "enter", "choose", "switch", "send", "read", "connect",
        "modify", "initiate", "loop", "use", "create", "delete", "transfer", "hold",
    ]
    if any(v in text_lower for v in imperative_hints):
        return False
    return re.search(r"\b(is|are|becomes|become|rings|ringing|idle|busy|connected|in conversation)\b", text_lower) is not None


def llm_pick_action(
    client: OpenAI | None,
    model: str,
    action_text: str,
    allowed_actions: set[str],
    action_labels: Dict[str, str] | None = None,
    cache: Dict[str, str] | None = None,
) -> str:
    """Use LLM to map a normalized action text to the best matching capability key.
    No hardcoded keyword pre-filtering — the full capability registry is always used.
    cache: optional shared dict {action_text -> key} to avoid duplicate LLM calls."""
    if client is None or not action_text.strip():
        return "custom_action"

    if cache is not None and action_text in cache:
        return cache[action_text]

    choices = _format_capability_list(allowed_actions, action_labels or {})

    system_msg = (
        "You are an expert at mapping test step descriptions to automation capability function names.\n"
        "Rules:\n"
        "1. Return ONLY valid JSON {\"action\": \"chosen_key\"}.\n"
        "2. chosen_key MUST exactly match one of the listed keys (exact match, case-sensitive).\n"
        "3. Use 'custom_action' ONLY if no listed key is semantically appropriate.\n"
        "4. Focus on the VERB/ACTION being performed; ignore device names (e.g. 'phone A').\n"
        "5. Choose the most specific matching key available."
    )
    user_msg = (
        f"Test step: {action_text}\n\n"
        f"Available capability keys (grouped by category):\n{choices}\n\n"
        "Which key best matches the test step action? Return JSON."
    )

    try:
        resp = client.chat.completions.create(
            model=model,
            response_format={"type": "json_object"},
            temperature=0.0,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
        )
        content = resp.choices[0].message.content or "{}"
        obj = json.loads(content)
        action = str(obj.get("action", "custom_action") or "custom_action").strip()
        if action in allowed_actions:
            if cache is not None:
                cache[action_text] = action
            return action
    except Exception:
        if cache is not None:
            cache[action_text] = "custom_action"
        return "custom_action"
    if cache is not None:
        cache[action_text] = "custom_action"
    return "custom_action"


def llm_pick_assertion(
    client: OpenAI | None,
    model: str,
    expected_text: str,
    allowed_assertions: set[str],
    assertion_labels: Dict[str, str] | None = None,
    cache: Dict[str, str] | None = None,
) -> str:
    """Use LLM to map a normalized expected result to the best matching assertion key.
    No hardcoded keyword pre-filtering — the full assertion registry is always used.
    cache: optional shared dict {expected_text -> key} to avoid duplicate LLM calls."""
    if client is None or not expected_text.strip():
        return ""

    if cache is not None and expected_text in cache:
        return cache[expected_text]

    choices = _format_capability_list(allowed_assertions, assertion_labels or {})

    system_msg = (
        "You are an expert at mapping test expected results to assertion function names.\n"
        "Rules:\n"
        "1. Return ONLY valid JSON {\"assertion\": \"chosen_key\"}.\n"
        "2. chosen_key MUST exactly match one of the listed keys (exact match, case-sensitive).\n"
        "3. Return {\"assertion\": \"\"} if no key is semantically appropriate.\n"
        "4. Focus on the STATE being verified; ignore device names.\n"
        "5. Choose the most specific matching key available."
    )
    user_msg = (
        f"Expected result: {expected_text}\n\n"
        f"Available assertion keys (grouped by category):\n{choices}\n\n"
        "Which key best matches? Return JSON."
    )

    try:
        resp = client.chat.completions.create(
            model=model,
            response_format={"type": "json_object"},
            temperature=0.0,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
        )
        content = resp.choices[0].message.content or "{}"
        obj = json.loads(content)
        assertion = str(obj.get("assertion", "") or "").strip()
        if assertion in allowed_assertions:
            if cache is not None:
                cache[expected_text] = assertion
            return assertion
    except Exception:
        if cache is not None:
            cache[expected_text] = ""
        return ""
    if cache is not None:
        cache[expected_text] = ""
    return ""


def compile_dsl_to_schema(
    dsl_entry: Dict[str, Any],
    allowed_actions: set[str],
    allowed_assertions: set[str],
    client: OpenAI | None,
    model: str,
    action_labels: Dict[str, str] | None = None,
    assertion_labels: Dict[str, str] | None = None,
    action_cache: Dict[str, str] | None = None,
    assertion_cache: Dict[str, str] | None = None,
) -> Dict[str, Any]:
    dsl = dsl_entry.get("dsl", {})
    act_block = dsl.get("action", {}) if isinstance(dsl, dict) else {}
    exp_block = dsl.get("expected", {}) if isinstance(dsl, dict) else {}

    action_text = str(act_block.get("text", "") or "")
    actor = str(act_block.get("actor", "") or "")
    target = str(act_block.get("target", "") or "")

    if client is not None and action_text.strip():
        action = llm_pick_action(client, model, action_text, allowed_actions, action_labels, cache=action_cache)
        pick_path = "llm_direct"
    else:
        action = "custom_action" if action_text.strip() else ""
        pick_path = "no_llm_fallback"

    params = {}
    if actor:
        params["device"] = actor
    if target:
        params["target"] = target

    expected_text = str(exp_block.get("text", "") or "")
    expected_items: List[Dict[str, Any]] = []
    if expected_text:
        if client is not None:
            assertion = llm_pick_assertion(client, model, expected_text, allowed_assertions, assertion_labels, cache=assertion_cache)
        else:
            assertion = ""
        if assertion and assertion in allowed_assertions:
            expected_items.append({"action": assertion, "params": {}})
        else:
            expected_items.append({"action": "custom_action", "params": {"text": expected_text}})

    # If action text is actually a state/precondition sentence, treat it as expected-state step.
    if action == "custom_action" and _looks_like_state_step(action_text):
        promoted_assertion = ""
        if client is not None:
            promoted_assertion = llm_pick_assertion(client, model, action_text, allowed_assertions, assertion_labels, cache=assertion_cache)
        if promoted_assertion and promoted_assertion in allowed_assertions:
            expected_items.insert(0, {"action": promoted_assertion, "params": {}})
        elif not expected_items:
            expected_items.append({"action": "custom_action", "params": {"text": action_text}})
        action = ""
        params = {}

    schema = {
        "action": action,
        "params": params,
        "expected": expected_items,
        "_meta": {
            "path": pick_path,
        },
    }

    if not action_text.strip() and expected_text.strip():
        schema.pop("action", None)
        schema.pop("params", None)
        schema["custom_reason"] = "expected_only_step"
    elif not action_text.strip() and not expected_text.strip():
        schema.pop("action", None)
        schema.pop("params", None)
        schema["custom_reason"] = "empty_action_and_expected"
    elif action == "" and expected_items:
        schema.pop("action", None)
        schema.pop("params", None)
        schema["custom_reason"] = "state_step_promoted_to_expected"

    return {
        "case_id": dsl_entry.get("case_id"),
        "step_no": dsl_entry.get("step_no"),
        "sub_step_no": dsl_entry.get("sub_step_no"),
        "normalized_action": action_text,
        "normalized_expected_result": expected_text,
        "action_schema": schema,
    }


def run(
    input_path: Path,
    dsl_output_path: Path,
    action_output_path: Path,
    capability_registry_path: Path,
    model: str,
    api_key: str | None,
    base_url: str,
    synonym_map_path: Path | None = None,  # kept for CLI backward-compat, not used for routing
) -> None:
    payload = load_json(input_path)
    entries = payload.get("entries", []) if isinstance(payload, dict) else []
    if not isinstance(entries, list):
        raise ValueError("Input must contain entries list")

    allowed_actions = load_registry(capability_registry_path, "action", default_extra={"custom_action"})
    allowed_assertions = load_registry(capability_registry_path, "assertion")
    action_labels = load_capability_labels(capability_registry_path, "action")
    assertion_labels = load_capability_labels(capability_registry_path, "assertion")
    client = OpenAI(api_key=api_key, base_url=base_url) if api_key else None

    # Shared LLM result caches — keyed by normalized text, guarded by a lock for thread safety.
    # Any identical text across sub_steps hits the cache instead of calling the LLM again.
    import threading
    _cache_lock = threading.Lock()
    _action_cache: Dict[str, str] = {}
    _assertion_cache: Dict[str, str] = {}

    def _cached_action(text: str) -> str:
        with _cache_lock:
            if text in _action_cache:
                return _action_cache[text]
        result = llm_pick_action(client, model, text, allowed_actions, action_labels, cache=None)
        with _cache_lock:
            _action_cache[text] = result
        return result

    def _cached_assertion(text: str) -> str:
        with _cache_lock:
            if text in _assertion_cache:
                return _assertion_cache[text]
        result = llm_pick_assertion(client, model, text, allowed_assertions, assertion_labels, cache=None)
        with _cache_lock:
            _assertion_cache[text] = result
        return result

    # Initialize DSL validator
    dsl_registry_path = capability_registry_path.parent / "dsl_registry.json"
    dsl_validator = DSLValidator(dsl_registry_path, capability_registry_path)
    print(f"DSL Validator: {dsl_validator.get_stats()}")

    dsl_rows = [build_dsl_entry(e) for e in entries]

    dsl_payload = {
        "meta": {
            "source": str(input_path),
            "description": "AAO to DSL intermediate representation",
            "row_count": len(dsl_rows),
            "dsl_registry_stats": dsl_validator.get_stats(),
        },
        "rows": dsl_rows,
    }
    save_json(dsl_output_path, dsl_payload)

    # Parallel LLM calls: 16 threads to maximise throughput without hitting rate limits
    max_workers = 16 if client is not None else 1
    compiled_rows: List[Dict[str, Any]] = [None] * len(dsl_rows)  # type: ignore[list-item]

    def _compile_one(idx_row: Tuple[int, Dict[str, Any]]) -> Tuple[int, Dict[str, Any]]:
        idx, r = idx_row
        dsl = r.get("dsl", {})
        action_text = str(dsl.get("action", {}).get("text", "") or "")
        expected_text = str(dsl.get("expected", {}).get("text", "") or "")

        # Pre-populate cache entries via the thread-safe wrappers before calling compile.
        # compile_dsl_to_schema will read from the cache dicts directly (no lock needed
        # at that point because the value is already present).
        if client is not None and action_text.strip():
            _cached_action(action_text)
        if client is not None and expected_text.strip():
            _cached_assertion(expected_text)

        return idx, compile_dsl_to_schema(
            r,
            allowed_actions,
            allowed_assertions,
            client,
            model,
            action_labels=action_labels,
            assertion_labels=assertion_labels,
            action_cache=_action_cache,
            assertion_cache=_assertion_cache,
        )

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_compile_one, (i, r)): i for i, r in enumerate(dsl_rows)}
        done = 0
        for fut in as_completed(futures):
            idx, result = fut.result()
            compiled_rows[idx] = result
            done += 1
            if done % 50 == 0:
                print(f"  compiled {done}/{len(dsl_rows)} rows...")

    action_payload = {
        "meta": {
            "source_dsl": str(dsl_output_path),
            "description": "Action schema compiled from DSL",
            "row_count": len(compiled_rows),
        },
        "rows": compiled_rows,
    }
    save_json(action_output_path, action_payload)

    custom_count = sum(1 for r in compiled_rows if r.get("action_schema", {}).get("action") == "custom_action")
    print(f"DSL output: {dsl_output_path}")
    print(f"Action output: {action_output_path}")
    print(f"Rows: {len(compiled_rows)}")
    print(f"Custom action: {custom_count} ({(custom_count / len(compiled_rows) * 100 if compiled_rows else 0):.1f}%)")
    print(f"LLM cache: {len(_action_cache)} unique action texts, {len(_assertion_cache)} unique assertion texts")
    print(f"DSL Validator final: {dsl_validator.get_stats()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="AAO -> DSL -> Action Schema (fully LLM-driven, no hardcoded rules)")
    parser.add_argument("--input", type=Path, required=True, help="Input normalized_kb JSON")
    parser.add_argument("--dsl-output", type=Path, required=True, help="Output DSL JSON")
    parser.add_argument("--action-output", type=Path, required=True, help="Output action schema JSON")
    parser.add_argument("--synonym-map", type=Path, default=None, help="[deprecated, no longer used for routing]")
    parser.add_argument("--capability-registry", type=Path, default=Path("resource/capability_registry.json"))
    parser.add_argument("--model", type=str, default="deepseek-chat")
    parser.add_argument("--api-key", type=str, default=None)
    parser.add_argument("--base-url", type=str, default="https://api.deepseek.com")
    args = parser.parse_args()

    run(
        input_path=args.input,
        dsl_output_path=args.dsl_output,
        action_output_path=args.action_output,
        capability_registry_path=args.capability_registry,
        model=args.model,
        api_key=args.api_key,
        base_url=args.base_url,
    )


if __name__ == "__main__":
    main()
