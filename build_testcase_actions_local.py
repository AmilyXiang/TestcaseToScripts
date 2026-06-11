from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def _split_action(step: dict[str, Any]) -> list[str]:
    subs = step.get("action_substeps")
    if isinstance(subs, list) and subs:
        out = [str(s).strip() for s in subs if str(s).strip()]
        if out:
            return out

    action = str(step.get("action") or "").strip()
    if not action:
        return [""]

    lines = [x.strip() for x in action.splitlines() if x.strip()]
    if not lines:
        return [action]

    out: list[str] = []
    for line in lines:
        out.extend(_atomize_action_line(line))
    return out or [action]


_ACTION_VERB_FOLLOW = (
    r"press|enter|select|open|go|set|input|dial|make|unlock|lock|reboot|"
    r"activate|deactivate|navigate|long\s+press|return|choose|switch|answer|reject"
)


def _atomize_action_line(text: str) -> list[str]:
    s = (text or "").strip()
    if not s:
        return []

    # Only split when the right side starts with an executable verb phrase.
    s = re.sub(r"(?i)\band\s+then\b", " ; ", s)
    s = re.sub(r"(?i)\bthen\b(?=\s+(?:" + _ACTION_VERB_FOLLOW + r")\b)", " ; ", s)
    s = re.sub(r"(?i)\band\b(?=\s+(?:" + _ACTION_VERB_FOLLOW + r")\b)", " ; ", s)
    s = re.sub(r"(?i),(?=\s*(?:" + _ACTION_VERB_FOLLOW + r")\b)", " ;", s)

    parts = [p.strip(" -\t") for p in re.split(r"\s*;\s*", s) if p.strip(" -\t")]
    return parts or [text]


def _split_expected(step: dict[str, Any]) -> list[str]:
    cps = step.get("expected_checkpoints")
    if isinstance(cps, list) and cps:
        out = [str(s).strip() for s in cps if str(s).strip()]
        if out:
            return out

    expected = str(step.get("expected_result") or "").strip()
    if not expected:
        return [""]

    lines = [x.strip() for x in expected.splitlines() if x.strip()]
    return lines or [expected]


def _action_intent(text: str) -> str:
    t = text.lower()
    if ("check" in t or "verify" in t) and "incoming call" in t:
        return "check_call_presentation"
    if "press any key" in t:
        return "press_any_key"
    if "sk1" in t:
        return "press_sk1_key"
    if "sk2" in t:
        return "press_sk2_key"
    if "sk3" in t:
        return "press_sk3_key"
    if "ok key" in t or "press ok" in t:
        return "press_ok_key"
    # Match "back key" with or without surrounding quotes (e.g. press the "Back" key)
    if "back key" in t or '"back"' in t or "\u201cback\u201d" in t:
        return "press_back_key"
    # dial_number must be checked before navigator, so "Dial … and … navigator keys" → dial_number
    if "dial" in t and "number" in t:
        return "dial_number"
    if "outgoing" in t or "dial" in t or "make a call" in t or "call to" in t:
        return "initiate_outgoing_call"
    if "navigator right" in t or "right navigation" in t:
        return "press_navigator_right_key"
    if "navigator" in t or "nav key" in t:
        return "press_navigator_key"
    if "incoming call" in t or ("ring" in t and "call" in t):
        return "receive_incoming_call"
    if "answer" in t or "take call" in t:
        return "take_call"
    if "missed call" in t:
        return "confirm_missed_call"
    if "call log" in t or "calllog" in t:
        return "navigate_calllog"
    if "central directory" in t:
        return "navigate_to_central_directory"
    if "message" in t and ("open" in t or "navigate" in t or "screen" in t):
        return "navigate_message"
    if "message" in t and ("send" in t or "receive" in t):
        return "receive_message"
    if "lock" in t and ("check" in t or "verify" in t):
        return "check_lock_state"
    if "back to idle" in t or "homepage" in t or "go back" in t:
        return "back_to_idle"
    return "needs_review"


def _expected_intent(text: str) -> str:
    t = text.lower()
    # "Answering is possible AND transfer is also possible" is a multi-capability assertion -> assert_generic
    if (
        "call is established" in t
        or "conversation" in t
        or ("can answer" in t and "transfer" not in t)
        or ("answer this incoming call" in t and "transfer" not in t)
    ):
        return "assert_call_established"
    if "incoming call" in t and ("display" in t or "present" in t):
        return "assert_displayed_incoming_call"
    if "missed call" in t:
        return "assert_displayed_missed_call"
    if "call menu" in t or "all calls menu" in t:
        return "assert_displayed_call_menu"
    if "message sent" in t:
        return "assert_message_sent"
    if "lock" in t and ("state" in t or "locked" in t):
        return "assert_lock_state"
    if "name" in t and "display" in t:
        return "assert_displayed_name_of_phone"
    if "number" in t and "display" in t:
        return "assert_displayed_number_of_phone"
    return "assert_generic"


def _extract_actor(text: str) -> str:
    """Infer the primary actor label from action_text.

    Returns an uppercase letter ("A", "B", …) for named devices,
    "DUT" for single-device actions, or "" when text is empty.

    Priority (first match wins):
      1. Sentence-initial subject: "The phone/handset X" / "Phone/Handset X"
      2. Device the tester operates: "On the DUT/phone/handset X"
      3. Originator in a call: "from the phone/handset X"
      4. Any labeled device anywhere in the sentence
      5. Default: "DUT"
    """
    t = (text or "").strip()
    if not t:
        return ""

    _DEVICE_WORDS = r"(?:DUT|phone|handset|device)"
    # Allow optional whitespace between opening quote and label letter,
    # e.g. both `"A"` and `" A "` (TestRail export inserts spaces around quotes).
    _LABEL = r'["\u201c\u201d]?\s*([A-Z])\s*["\u201c\u201d]?'

    # Pattern 1 — "The phone X …" / "Handset X …" at start of sentence
    m = re.match(
        rf'^(?:the\s+)?{_DEVICE_WORDS}\s*{_LABEL}\b',
        t, flags=re.IGNORECASE,
    )
    if m:
        return m.group(1).upper()

    # Pattern 2 — "On the DUT X" / "On the phone X"
    m = re.search(
        rf'\bon\s+the\s+{_DEVICE_WORDS}\s*{_LABEL}\b',
        t, flags=re.IGNORECASE,
    )
    if m:
        return m.group(1).upper()

    # Pattern 3 — "from the phone/handset X" (caller / originator)
    m = re.search(
        rf'\bfrom\s+(?:the\s+|a\s+(?:distant\s+)?)?{_DEVICE_WORDS}\s*{_LABEL}\b',
        t, flags=re.IGNORECASE,
    )
    if m:
        return m.group(1).upper()

    # Pattern 4 — any labeled device (first occurrence)
    m = re.search(
        rf'\b{_DEVICE_WORDS}\s*{_LABEL}\b',
        t, flags=re.IGNORECASE,
    )
    if m:
        return m.group(1).upper()

    # Default: DUT is always the device under test = A (primary device in all test cases)
    return "A"


def _is_observation_action(text: str) -> bool:
    t = (text or "").lower().strip()
    return t.startswith(("check", "verify", "observe", "watch", "confirm"))


def _is_eventful_action(text: str) -> bool:
    t = (text or "").lower()
    if _is_observation_action(text):
        return True
    return any(
        token in t
        for token in (
            "incoming call",
            "make a call",
            "call to",
            "dial",
            "answer",
            "reject",
            "press ",
            "receive message",
            "send message",
        )
    )


def _is_setup_action(text: str) -> bool:
    t = (text or "").lower()
    if not t or _is_eventful_action(text):
        return False
    return any(
        token in t
        for token in (
            "menu",
            "screen",
            "settings",
            "language",
            "select ",
            "go to",
            "navigate",
            "open ",
            "activate",
            "deactivate",
        )
    )


def _fold_leading_setup_actions(actions: list[str], expects: list[str]) -> tuple[list[str], list[str]]:
    if len(actions) <= 1:
        return [], actions

    trigger_index = None
    for idx, action in enumerate(actions):
        if _is_eventful_action(action):
            trigger_index = idx
            break

    if trigger_index is None or trigger_index == 0:
        return [], actions

    leading_actions = actions[:trigger_index]
    remaining_actions = actions[trigger_index:]
    if not leading_actions or not all(_is_setup_action(action) for action in leading_actions):
        return [], actions

    if len(expects) < len(remaining_actions):
        return [], actions

    return leading_actions, remaining_actions


def _merge_preconditions(base_pre: str, inline_pre: str) -> str:
    base_pre = (base_pre or "").strip()
    inline_pre = (inline_pre or "").strip()
    if base_pre and inline_pre:
        return f"{base_pre} ; {inline_pre}"
    return base_pre or inline_pre


# State indicators used to identify embedded "when <condition>" clauses.
_EMBEDDED_WHEN_STATE_WORDS = (
    "is active", "is enabled", "is configured", "is locked", "is unlocked",
    "is present", "is available", "is set", "is inactive", "is off",
    "is on", "are active", "are enabled", "has been", "have been",
    "lock is", "mode is", "state is", "status is",
)


def _extract_inline_precondition(action_text: str) -> tuple[str, str]:
    text = (action_text or "").strip()
    if not text:
        return "", ""

    lower = text.lower()

    # 1. Condition-led clauses at the start of the sentence.
    if lower.startswith(("when ", "while ", "if ", "once ", "after ")):
        m = re.match(r"^(when|while|if|once|after)\b\s*(.+?)\s*[,;:]\s*(.+)$", text, flags=re.IGNORECASE)
        if m:
            pre = f"{m.group(1)} {m.group(2)}".strip()
            return pre, m.group(3).strip()
        return text, ""

    # 2. "In idle, <action>" — very common in DECT test cases.
    if lower.startswith("in idle"):
        m = re.match(r"^in idle\s*[,;:]\s*(.+)$", text, flags=re.IGNORECASE)
        if m:
            return "In idle", m.group(1).strip()
        return "In idle", ""

    # 3. Lock-state prefix (no following action — pure state row).
    if lower.startswith(("in keylock status", "in locked status", "in lock status")):
        return text, ""

    # 4. Embedded trailing "when <state-condition>" clause.
    # e.g. "Make an incoming call on DUT when the local lock is active."
    # Only extract when the when-clause clearly describes a device/system state.
    m = re.match(r"^(.+?)\s+when\s+(.+?)\.*$", text, flags=re.IGNORECASE)
    if m:
        main_part = m.group(1).strip()
        when_part = m.group(2).strip().rstrip(".")
        when_lower = when_part.lower()
        if any(indicator in when_lower for indicator in _EMBEDDED_WHEN_STATE_WORDS):
            return f"when {when_part}", main_part

    return "", text


def _precondition_intent(text: str) -> str:
    """Classify precondition_intent using Stage-D canonical types.

    Canonical types (from prompt.case_to_action.copilot.md):
      device_context | ui_context | sequence_state |
      condition_state | data_state | custom_precondition
    """
    t = (text or "").lower()
    # ui_context: UI/screen state (idle screen, specific menu, etc.)
    if "idle" in t or any(w in t for w in ("menu", "screen", "tab", "homepage")):
        return "ui_context"
    # condition_state: device or feature configuration/lock state
    if any(w in t for w in ("keylock", "lock", "active", "enabled", "configured",
                             "disabled", "inactive", "unlocked", "is set")):
        return "condition_state"
    # sequence_state: something that happened just before (after hangup, after call, etc.)
    if any(w in t for w in ("after ", "hangup", "hang up", "previous step", "already")):
        return "sequence_state"
    # data_state: data must exist (contact, directory entry, etc.)
    if any(w in t for w in ("contact", "directory", "entry", "number", "name", "registered")):
        return "data_state"
    return "custom_precondition"


def build_rows(cleaned: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for case in cleaned.get("Worksheet", []):
        case_id = str(case.get("case_id") or "").strip()
        title = str(case.get("title") or "")
        pre = str(case.get("preconditions") or "").strip()
        if not case_id:
            continue

        for step in case.get("steps", []):
            step_no = int(step.get("step_no") or 0)
            if step_no <= 0:
                continue

            actions = _split_action(step)
            expects = _split_expected(step)
            carried_setup_pre, actions = _fold_leading_setup_actions(actions, expects)
            n = max(len(actions), len(expects), 1)

            for i in range(n):
                a = actions[i] if i < len(actions) else actions[-1]
                e = expects[i] if i < len(expects) else expects[-1]

                inline_pre, normalized_action = _extract_inline_precondition(a)
                effective_action = normalized_action if normalized_action else a
                step_setup_pre = " ; ".join(carried_setup_pre) if i == 0 and carried_setup_pre else ""
                merged_inline_pre = _merge_preconditions(step_setup_pre, inline_pre)
                pre_text = _merge_preconditions(pre, merged_inline_pre)
                pre_required = bool(merged_inline_pre)
                pre_intent = _precondition_intent(merged_inline_pre) if merged_inline_pre else ""

                rows.append(
                    {
                        "case_id": case_id,
                        "title": title,
                        "step_no": step_no,
                        "sub_step_no": i + 1,
                        "action_actor": _extract_actor(effective_action),
                        "action_text": effective_action,
                        "action_intent": _action_intent(effective_action),
                        "expected_actor": _extract_actor(e),
                        "expected_text": e,
                        "expected_intent": _expected_intent(e),
                        "precondition_actor": _extract_actor(pre_text) if pre_text else "A",
                        "precondition_text": pre_text,
                        "precondition_intent": pre_intent,
                        "precondition_required": pre_required,
                    }
                )

    rows.sort(key=lambda x: (x["case_id"], x["step_no"], x["sub_step_no"], x["action_text"]))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Build testcase_actions from cleaned JSON.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    cleaned = json.loads(args.input.read_text(encoding="utf-8"))
    rows = build_rows(cleaned)
    out = {
        "status": "ok",
        "meta": {
            "input": str(args.input).replace("\\", "/"),
            "mode": "local_stable",
            "rows": len(rows),
        },
        "rows": rows,
    }
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote actions: {args.output}")
    print(f"Rows: {len(rows)}")


if __name__ == "__main__":
    main()
