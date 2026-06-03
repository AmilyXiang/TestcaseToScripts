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
    if "back key" in t:
        return "press_back_key"
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
    if "outgoing" in t or "dial" in t or "make a call" in t or "call to" in t:
        return "initiate_outgoing_call"
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
    if "call is established" in t or "conversation" in t:
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
    if "idle" in t:
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
            n = max(len(actions), len(expects), 1)

            for i in range(n):
                a = actions[i] if i < len(actions) else actions[-1]
                e = expects[i] if i < len(expects) else expects[-1]

                inline_pre, normalized_action = _extract_inline_precondition(a)
                effective_action = normalized_action if normalized_action else a
                pre_text = _merge_preconditions(pre, inline_pre)
                pre_required = bool(inline_pre)
                pre_intent = _precondition_intent(inline_pre) if inline_pre else ""

                rows.append(
                    {
                        "case_id": case_id,
                        "title": title,
                        "step_no": step_no,
                        "sub_step_no": i + 1,
                        "action_text": effective_action,
                        "expected_text": e,
                        "action_intent": _action_intent(effective_action),
                        "expected_intent": _expected_intent(e),
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
