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


def extract_devices(text: str) -> List[str]:
    return re.findall(r"\bphone\s+[a-z0-9]+\b", text.lower())


def infer_action_intent(action_text: str, phrase_to_intent_action: Dict[str, str]) -> tuple[str, str]:
    text = action_text.strip().lower()
    if not text:
        return "no_action", "empty_action"

    for phrase, intent in phrase_to_intent_action.items():
        if phrase and phrase in text:
            return intent, f"phrase:{phrase}"

    # lightweight semantic fallback
    if "dial" in text or "call" in text:
        return "call by number", "semantic:dial_or_call"
    if "answer" in text or "take call" in text:
        return "answer incoming call", "semantic:answer"
    if "hang up" in text or "end" in text or "release" in text:
        return "end active call", "semantic:end_call"

    return "unknown_action", "no_phrase_or_semantic_match"


def infer_assertion_intent(expected_text: str, phrase_to_intent_assertion: Dict[str, str]) -> tuple[str, str]:
    text = expected_text.strip().lower()
    if not text:
        return "no_expected", "empty_expected"

    for phrase, intent in phrase_to_intent_assertion.items():
        if phrase and phrase in text:
            return intent, f"phrase:{phrase}"

    if any(k in text for k in ["in conversation", "communication is established", "connected"]):
        return "validate connected conversation", "semantic:conversation"
    if "rings" in text or "ringing" in text:
        return "validate ringing call setup", "semantic:ringing"
    if "idle" in text or "is idle" in text or "are idle" in text:
        return "validate idle state", "semantic:idle"

    return "unknown_assertion", "no_phrase_or_semantic_match"


def build_dsl_entry(entry: Dict[str, Any], phrase_to_intent_action: Dict[str, str], phrase_to_intent_assertion: Dict[str, str]) -> Dict[str, Any]:
    action_text = str(entry.get("normalized_action", "") or "")
    expected_text = str(entry.get("normalized_expected_result", "") or "")

    action_intent, action_evidence = infer_action_intent(action_text, phrase_to_intent_action)
    assertion_intent, assertion_evidence = infer_assertion_intent(expected_text, phrase_to_intent_assertion)

    devices = extract_devices(action_text)
    actor = devices[0] if devices else "current_device"
    target = devices[1] if len(devices) > 1 else ""

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
                "evidence": action_evidence,
            },
            "expected": {
                "intent": assertion_intent,
                "text": expected_text,
                "evidence": assertion_evidence,
            },
            "trace": {
                "title": entry.get("title"),
                "keywords": entry.get("keywords", []),
            },
        },
    }


def primitive_name(path: str | None) -> str:
    if not isinstance(path, str) or "." not in path:
        return ""
    return path.split(".")[-1].strip()


# Keyword → candidate keys pre-filter table (order matters: more specific first)
_ACTION_KEYWORD_GROUPS: List[Tuple[str, List[str]]] = [
    ("call back|callback|call-back|redial|redials|redial physical key|call back key",
     ["bis", "call_last_caller_from_call_log", "call_last_callee_from_call_log"]),
    ("answers the call|takes the call|pick up|answer incoming|answering the call",
     ["take_call", "take_call_by_soft_key", "take_second_call", "handsfree"]),
    ("does not answer the call|not answer the call|no answer",
     ["reject_call", "silence_call", "on_no_answer_by_key_to_number", "on_no_answer_by_key_to_voicemail"]),
    ("presses the new call|new call key|new call and calls",
     ["new_call"]),
    ("calls phone|calls the phone|dials|direct dial|off hook dial|handsfree dial",
     ["direct_dial", "handsfree_dial", "off_hook_dial", "new_call", "call_by_name",
      "handsfree_off_hook_dial", "off_hook_handsfree_dial"]),
    ("hang up|hangs up|end call|ends the call|releases the call|puts down",
     ["release_call", "end_call", "cancel_call"]),
    ("puts on hold|hold the call|holds the call",
     ["hold_call", "hold_call_by_softkey"]),
    ("retrieves the call|retrieve the call|unhold",
     ["retrieve_call", "retrieve_call_by_softkey"]),
    ("blind transfer",
     ["blind_transfer", "blind_transfer_by_softkey"]),
    ("transfers the call|transfer call|transfer softkey",
     ["transfer_call", "transfer_call_by_softkey", "blind_transfer", "blind_transfer_by_softkey", "transfer_conference"]),
    ("switches the active call|broker|switch between",
     ["broker"]),
    ("conference|start conference|3-way",
     ["start_conference", "start_conference_by_softkey", "end_conference", "transfer_conference"]),
    ("mute|unmute|mutes the call",
     ["mute", "unmute"]),
    ("forward|call forward|diverts",
     ["immediate_by_key_to_number", "immediate_by_key_to_voicemail", "deactivate_forward",
      "on_busy_by_key_to_number", "on_no_answer_by_key_to_number",
      "activate_do_not_disturb", "deactivate_do_not_disturb"]),
    ("voicemail|voice mail",
        ["immediate_by_key_to_voicemail", "create_voicemail_prog_key_by_menu", "message"]),
        ("text message|messages|send a text|read a text|read text message|tries to read",
        ["message", "send_to_create", "send_predefined", "to_complete_text_msg", "to_predefined_text_msg"]),
        ("password|lock prefix|change password|secret code|bad password",
        ["enter", "menu_key", "press_softkey", "ok"]),
    ("create contact|add contact|save contact",
     ["create_contact_basic_infos", "create_contact_full_infos"]),
    ("call contact|call by name|contact name",
     ["call_contact", "call_by_name"]),
    ("delete contact",
     ["delete_contact"]),
    ("call log",
     ["to_call_log", "to_incoming_call_log", "to_missed_call_log",
      "to_outgoing_call_log", "delete_call_log"]),
    ("settings|parameters|configuration",
     ["to_settings", "to_phone_settings", "to_audio_settings", "to_homepage_settings"]),
    ("progkeys|programmable key|prog key",
     ["to_progkeys", "create_prog_key", "del_prog_key_by_label", "use_progkey"]),
        (r"programming page|emplacement|already defined key|suppression button|update key|newly modified key|choose number|choose\s+\"?number\"?",
         ["to_progkeys", "create_prog_key_by_menu", "create_call_prog_key_by_menu", "modify_call_prog_key_by_menu",
            "del_prog_key_by_label", "use_progkey", "press_specific_progkey"]),
        ("call park|retrieve park|parked call|park using",
         ["hold_call", "retrieve_call", "retrieve_call_by_softkey", "use_progkey"]),
        ("search screen|search result|types the first|browse the menu|browses the menu",
         ["search", "search_and_press", "search_and_press_in_page", "menu_key", "directory"]),
        ("idle state|is idle|becomes idle|wait until.*idle",
         ["on_hook", "to_homepage", "hook"]),
        ("headset.*plugged|connected to a headset",
         ["switch_handsfree_to_headset", "handsfree"]),
        ("switches the audio mode|switch from handset|switch from handsfree|group-listening-mode",
         ["switch_handsfree_to_headset", "handsfree", "hook"]),
        ("volume level|volume up|volume down",
         ["volume_up", "volume_down", "set_ringing_volume"]),
    ("clean|reset|reboot|restart the phone|prepare",
     ["clean_device", "reset_phone", "prepare_device"]),
    ("silence|silent ringing",
     ["silence_call", "silence_second_call", "activate_silent_ringing"]),
    ("reject|refuses the call",
     ["reject_call", "reject_second_call"]),
    ("deflect|deflects to vm",
     ["deflect_call_to_VM", "deflect_second_call_to_VM"]),
    ("handsfree|speaker",
     ["handsfree", "handsfree_dial", "handsfree_off_hook_dial", "switch_handsfree_to_headset"]),
    ("interphony",
     ["interphony_on", "interphony_off", "deactivate_interphony"]),
]

_ASSERTION_KEYWORD_GROUPS: List[Tuple[str, List[str]]] = [
    ("in conversation|communication is established|connected|talking",
     ["are_in_conversation", "are_in_conversation_contact", "are_in_conversation_stress_tests"]),
    ("calling and receiving|setting up the call|ringing|is ringing|rings",
     ["are_calling_and_receiving", "are_calling_and_receiving_second_call", "is_ringing"]),
    ("on hold|put on hold|hold tone",
     ["is_on_hold"]),
    ("conference|3-way call",
     ["are_in_conference", "has_initiate_conference"]),
    ("mute led|mute indicator",
     ["is_mute_led_active", "is_mute_led_on_idle"]),
    ("handsfree|speaker mode",
     ["is_voicemode_handsfree"]),
    ("headset mode",
     ["is_voicemode_headset"]),
    ("handset mode",
     ["is_voicemode_handset"]),
    ("idle|no call",
     ["is_voicemode_idle"]),
    ("missed call|missed calls",
     ["has_missed_call", "has_missed_calls_or_messages"]),
    ("has called|outgoing call|has dialed",
     ["has_called", "has_dialed"]),
    ("has received|incoming call log",
     ["has_received_call"]),
    ("forward.*ok|forward is active|forward is set",
     ["forward_definition_OK"]),
    ("forward.*error|forward failed",
     ["forward_definition_error"]),
    ("display|screen shows|text displayed|shown on screen",
     ["is_text_on_screen", "text_displayed_on_sreen", "is_default_homepage_displayed"]),
    ("voice message|voicemail message",
     ["has_voice_messages"]),
    ("transferred|being transferred",
     ["are_being_transfered"]),
    ("interphony active",
     ["is_interphony_active"]),
    ("silent|no sound",
     ["is_silent"]),
    ("busy|line busy",
     ["distant_is_busy"]),
]


def _prefilter_candidates(
    text: str,
    allowed: set[str],
    groups: List[Tuple[str, List[str]]],
    top_n: int = 30,
) -> set[str]:
    """Return a smaller candidate set based on keyword matching."""
    text_lower = text.lower()
    candidates: set[str] = set()
    for keywords_raw, keys in groups:
        matched = False
        try:
            matched = re.search(keywords_raw, text_lower) is not None
        except re.error:
            matched = False
        if not matched:
            for kw in keywords_raw.split("|"):
                if kw.strip() and kw.strip() in text_lower:
                    matched = True
                    break
        if matched:
            candidates.update(k for k in keys if k in allowed)
    # If too few candidates, fall back to full list
    if len(candidates) < 3:
        return allowed
    return candidates


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
) -> str:
    if client is None or not action_text.strip():
        return "custom_action"

    # Step 1: pre-filter to manageable candidate set
    candidates = _prefilter_candidates(action_text, allowed_actions, _ACTION_KEYWORD_GROUPS)

    labels = action_labels or {}
    lines = [f"- {k}: {labels.get(k, k)}" for k in sorted(candidates) if k]
    choices = "\n".join(lines)

    system_msg = (
        "You are an expert at mapping IP phone test steps to capability function names.\n"
        "Rules:\n"
        "1. Return ONLY valid JSON {\"action\": \"chosen_key\"}.\n"
        "2. chosen_key MUST be one of the listed keys (exact match, case-sensitive).\n"
        "3. Use 'custom_action' ONLY if the step truly doesn't match any listed key.\n"
        "4. Ignore device names like 'phone A', 'phone B' — focus on the VERB/ACTION.\n"
        "5. Examples: 'calls phone B' → direct_dial; 'answers the call' → take_call; "
        "'puts on hold' → hold_call; 'switches active call' → broker."
    )
    user_msg = (
        f"Test step: {action_text}\n\n"
        f"Candidate capability keys (key: description):\n{choices}\n\n"
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
            return action
    except Exception:
        return "custom_action"
    return "custom_action"


def llm_pick_assertion(
    client: OpenAI | None,
    model: str,
    expected_text: str,
    allowed_assertions: set[str],
    assertion_labels: Dict[str, str] | None = None,
) -> str:
    if client is None or not expected_text.strip():
        return ""

    # Step 1: pre-filter to manageable candidate set
    candidates = _prefilter_candidates(expected_text, allowed_assertions, _ASSERTION_KEYWORD_GROUPS)

    labels = assertion_labels or {}
    lines = [f"- {k}: {labels.get(k, k)}" for k in sorted(candidates) if k]
    choices = "\n".join(lines)

    system_msg = (
        "You are an expert at mapping IP phone test expected results to assertion function names.\n"
        "Rules:\n"
        "1. Return ONLY valid JSON {\"assertion\": \"chosen_key\"}.\n"
        "2. chosen_key MUST be one of the listed keys (exact match, case-sensitive).\n"
        "3. Use empty string if nothing fits: {\"assertion\": \"\"}.\n"
        "4. Ignore device names — focus on the STATE being verified.\n"
        "5. Examples: 'communication is established' → are_in_conversation; "
        "'phone is ringing' → is_ringing; 'put on hold' → is_on_hold."
    )
    user_msg = (
        f"Expected result: {expected_text}\n\n"
        f"Candidate assertion keys (key: description):\n{choices}\n\n"
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
            return assertion
    except Exception:
        return ""
    return ""


def compile_dsl_to_schema(
    dsl_entry: Dict[str, Any],
    action_primitive_map: Dict[str, str],
    assertion_primitive_map: Dict[str, str],
    allowed_actions: set[str],
    allowed_assertions: set[str],
    client: OpenAI | None,
    model: str,
    action_labels: Dict[str, str] | None = None,
    assertion_labels: Dict[str, str] | None = None,
) -> Dict[str, Any]:
    dsl = dsl_entry.get("dsl", {})
    act_block = dsl.get("action", {}) if isinstance(dsl, dict) else {}
    exp_block = dsl.get("expected", {}) if isinstance(dsl, dict) else {}

    action_intent = str(act_block.get("intent", "") or "")
    action_text = str(act_block.get("text", "") or "")
    actor = str(act_block.get("actor", "") or "")
    target = str(act_block.get("target", "") or "")

    if client is not None and action_text.strip():
        # LLM-first: directly pick from full capability list with descriptions
        action = llm_pick_action(client, model, action_text, allowed_actions, action_labels)
        pick_path = "llm_direct"
    else:
        # Fallback: primitive map (synonym_map.json) when no LLM
        action = primitive_name(action_primitive_map.get(action_intent))
        if action not in allowed_actions or action == "":
            action = "custom_action"
        pick_path = "primitive_map"

    params = {}
    if actor:
        params["device"] = actor
    if target:
        params["target"] = target

    assertion_intent = str(exp_block.get("intent", "") or "")
    expected_text = str(exp_block.get("text", "") or "")
    expected_items: List[Dict[str, Any]] = []
    if expected_text:
        if client is not None:
            assertion = llm_pick_assertion(client, model, expected_text, allowed_assertions, assertion_labels)
        else:
            assertion = primitive_name(assertion_primitive_map.get(assertion_intent))
        if assertion and assertion in allowed_assertions:
            expected_items.append({"action": assertion, "params": {}})
        else:
            expected_items.append({"action": "custom_action", "params": {"text": expected_text}})

    # If action text is actually a state/precondition sentence, treat it as expected-state step.
    if action == "custom_action" and _looks_like_state_step(action_text):
        promoted_assertion = ""
        if client is not None:
            promoted_assertion = llm_pick_assertion(client, model, action_text, allowed_assertions, assertion_labels)
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
            "dsl_action_intent": action_intent,
            "dsl_expected_intent": assertion_intent,
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
    synonym_map_path: Path,
    capability_registry_path: Path,
    model: str,
    api_key: str | None,
    base_url: str,
) -> None:
    payload = load_json(input_path)
    entries = payload.get("entries", []) if isinstance(payload, dict) else []
    if not isinstance(entries, list):
        raise ValueError("Input must contain entries list")

    phrase_to_intent_action, phrase_to_intent_assertion, action_primitive_map, assertion_primitive_map = load_synonym_maps(synonym_map_path)
    allowed_actions = load_registry(capability_registry_path, "action", default_extra={"custom_action"})
    allowed_assertions = load_registry(capability_registry_path, "assertion")
    action_labels = load_capability_labels(capability_registry_path, "action")
    assertion_labels = load_capability_labels(capability_registry_path, "assertion")
    client = OpenAI(api_key=api_key, base_url=base_url) if api_key else None
    
    # Initialize DSL validator
    dsl_registry_path = capability_registry_path.parent / "dsl_registry.json"
    dsl_validator = DSLValidator(dsl_registry_path, capability_registry_path)
    print(f"DSL Validator: {dsl_validator.get_stats()}")

    dsl_rows = [build_dsl_entry(e, phrase_to_intent_action, phrase_to_intent_assertion) for e in entries]
    
    # Validate and auto-supplement DSL entries
    for i, row in enumerate(dsl_rows):
        dsl = row.get("dsl", {})
        action_intent = dsl.get("action", {}).get("intent", "")
        assertion_intent = dsl.get("expected", {}).get("intent", "")
        
        if action_intent:
            dsl_validator.get_or_create_dsl(action_intent, "action", "Custom", dsl.get("action", {}).get("text", ""))
        if assertion_intent:
            dsl_validator.get_or_create_dsl(assertion_intent, "assertion", "Custom", dsl.get("expected", {}).get("text", ""))
    
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
        return idx, compile_dsl_to_schema(
            r,
            action_primitive_map,
            assertion_primitive_map,
            allowed_actions,
            allowed_assertions,
            client,
            model,
            action_labels=action_labels,
            assertion_labels=assertion_labels,
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
    print(f"DSL Validator final: {dsl_validator.get_stats()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo pipeline: AAO -> DSL -> Action Schema (with DSL auto-validation)")
    parser.add_argument("--input", type=Path, required=True, help="Input normalized_kb JSON")
    parser.add_argument("--dsl-output", type=Path, required=True, help="Output DSL JSON")
    parser.add_argument("--action-output", type=Path, required=True, help="Output action schema JSON")
    parser.add_argument("--synonym-map", type=Path, default=Path("resource/synonym_map.json"))
    parser.add_argument("--capability-registry", type=Path, default=Path("resource/capability_registry.json"))
    parser.add_argument("--dsl-registry", type=Path, default=None, help="DSL registry path (auto-discovered if not specified)")
    parser.add_argument("--model", type=str, default="deepseek-chat")
    parser.add_argument("--api-key", type=str, default=None)
    parser.add_argument("--base-url", type=str, default="https://api.deepseek.com")
    args = parser.parse_args()

    run(
        input_path=args.input,
        dsl_output_path=args.dsl_output,
        action_output_path=args.action_output,
        synonym_map_path=args.synonym_map,
        capability_registry_path=args.capability_registry,
        model=args.model,
        api_key=args.api_key,
        base_url=args.base_url,
    )


if __name__ == "__main__":
    main()
