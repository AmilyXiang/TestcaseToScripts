# Intent Refine Mapping Template (Telephony)

## Purpose
This template standardizes action intent refinement so that different wording with the same meaning maps to the same `action_intent`.

## Stable Mapping Contract
- Output must use approved canonical intents only.
- Match by meaning first, then wording.
- Use fixed priority order (high -> low).
- If no confident match, mark as `needs_review` (do not guess).
- For conflicting rules, the higher priority rule wins.
- Preserve-first: if no high-confidence match, keep existing action_intent unchanged.
- No downgrade: do not replace a specific existing intent with a more generic one.

## Canonical Intent List (current)
- dial_number
- press_navigator_key
- press_back_key
- create_personal_directory
- create_number_entry
- initiate_outgoing_call_from_contact
- init_emergency_call
- navigate_to_central_directory
- receive_incoming_call
- check_call_presentation
- take_call
- assign_name
- auto_answer_active
- select_any_key
- press_ok_key
- press_any_key
- auto_answer_deactive
- check_lock_state
- dont_take_call
- confirm_missed_call
- press_sk3_key
- press_navigator_right_key
- receive_message
- check_incoming_message
- navigate_message
- back_to_idle
- initiate_outgoing_call
- navigate_calllog
- press_sk1_key
- press_sk2_key

## Rule Table (R01-R32)

| Rule ID | Canonical action_intent | Meaning-first trigger examples | Negative examples (must NOT hit) | Priority |
|---|---|---|---|---|
| R01 | dial_number | Dial a complete number | make outgoing call to B | High |
| R02 | press_navigator_key | move cursor with left/right navigator keys | press right navigation to missed call menu | High |
| R03 | press_back_key | press Back key | go back homepage | High |
| R04 | create_personal_directory | create a personal directory | append existing contact only | High |
| R05 | create_number_entry | create entries with internal/external numbers | create top-level directory | High |
| R06 | initiate_outgoing_call_from_contact | outgoing call using personal directory/contact name | generic dial | High |
| R07 | init_emergency_call | dial emergency destination number | regular outgoing call | High |
| R08 | navigate_to_central_directory | enter/open/go to Central Directory menu | call log menu | High |
| R09 | initiate_outgoing_call_from_contact | send call with selected name/contact | reject call | High |
| R10 | receive_incoming_call | initiate incoming call to DUT from distant phone | outgoing call from DUT | High |
| R11 | check_call_presentation | watch/check call presentation on DUT screen | take/answer call | High |
| R12 | take_call | DUT takes incoming call | reject/decline incoming | High |
| R13 | take_call | phone B takes call from DUT A | ringing only check | High |
| R14 | assign_name | give handset/DUT a name | display name check | High |
| R15 | auto_answer_active | activate auto answer feature in local MMI | deactivate auto answer | High |
| R16 | select_any_key | select "Any key" option | press any key to answer | High |
| R17 | press_ok_key | validate/confirm with OK key | press SK3 | High |
| R18 | press_any_key | press any key to answer incoming call | select "Any key" setting | High |
| R19 | auto_answer_deactive | deactivate auto answer feature in local MMI | activate auto answer | High |
| R20 | check_lock_state | verify lock state immediately after | set lock state action | High |
| R21 | receive_incoming_call | distant phone calls your phone | missed call post-condition | High |
| R22 | dont_take_call | do not take the call | reject with key action | High |
| R23 | confirm_missed_call | this is missed / not answered call | active reject action | High |
| R24 | press_sk3_key | press SK3 to enter call log app | press SK2 View | High |
| R25 | press_navigator_right_key | press right navigation to missed call menu | generic navigator up/down | High |
| R26 | receive_message | distant device edits/sends text message to DUT | DUT checks icon only | High |
| R27 | receive_message | choose fixed message and send to DUT | open message screen | High |
| R28 | check_incoming_message | check text message icon and number on DUT | send message action | High |
| R29 | navigate_message | open text message screen by any method | check icon only | High |
| R30 | back_to_idle | go back homepage/idle | Back key press only | High |
| R31 | initiate_outgoing_call | call between dectA and dectB | receive incoming call | High |
| R32 | navigate_calllog | launch call log app in menu screen | open central directory | High |

## Extended Consistency Rules
These are optional but recommended for stable naming in call-log flows.

| Rule ID | Canonical action_intent | Trigger examples | Priority |
|---|---|---|---|
| E01 | press_sk1_key | Try SK1 Call key | Medium |
| E02 | press_sk2_key | Press SK2 View key | Medium |
| E03 | press_sk3_key | Press SK3 More key; Press SK3 More key or OK key | Medium |

## Scheme B Contextual Specialization
When existing intent is generic but context is explicit, refine to specific intent.

### B1: navigate_ui specialization
- Principle: specialize only when BOTH conditions are satisfied:
	1) explicit navigation action verb exists (for example: enter/open/go to/launch/navigate/select/switch to), and
	2) target screen/menu/tab is inferable with high confidence.
- Examples (valid specialization):
	- "Enter the menu \"Central Directory\"" -> `navigate_to_central_directory`
	- "Launch Call log app" / "Open CallLog" -> `navigate_to_calllog`
	- "Switch to All calls tab" -> `navigate_to_calllog_all_calls`
	- "Go to Dialed tab" -> `navigate_to_calllog_dialed`
	- "Go to Settings menu" -> `navigate_to_settings_menu`
	- "Open Language menu" -> `navigate_to_language_menu`
- Examples (must NOT specialize):
	- text contains only target noun without navigation action (for example: "Settings menu", "CallLog", "Language menu").
	- text is status/assertion-like and not an operation (for example: "On settings menu", "in call log").
- If either condition is missing, keep original `navigate_ui`.

### B2: press_key specialization
- Principle: `press_key` should become `press_<key>_key` where `<key>` is resolved from action_text.
- Examples:
	- SK1 -> `press_sk1_key`
	- SK2 -> `press_sk2_key`
	- SK3 -> `press_sk3_key`
	- OK -> `press_ok_key`
	- Back -> `press_back_key`
	- Release -> `press_release_key`
	- Right navigator -> `press_navigator_right_key`
- If key cannot be resolved with high confidence, keep original `press_key`.

## Conflict Resolution
Use first-match-wins with strict order:
1. R19 before R15 (deactive must win before active)
2. R18 before R16 when phrase contains "answer incoming call"
3. R25 before generic navigator rules
4. R24/E03 before generic press_key rules

## Fallback Policy
If no rule matches confidently:
- Keep original action_intent unchanged
- Mark row as needs_review in the report
- Log row id + text into review report
- Do not auto-invent a new intent

## Review Log Format
- case_id
- step_no
- sub_step_no
- action_text
- previous_action_intent
- suggested_action_intent
- matched_rule_id
- confidence (high/medium/low)
