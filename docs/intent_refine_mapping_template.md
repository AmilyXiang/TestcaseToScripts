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
- lock_device
- press_release_key
- press_sk_reject
- check_number_in_contact_or_not
- navigate_to_settings_menu
- navigate_to_language_menu

## Rule Table (R01-R33)

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
| R13 | take_call | phone B takes call from DUT A; the phone "B" takes the call from the DUT "A" | ringing only check | High |
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
| R26 | receive_message | distant device edits/sends text message to DUT; edit one or more text message(s) and sent it to DUT | DUT checks icon only | High |
| R27 | receive_message | choose fixed message and send to DUT | open message screen | High |
| R28 | check_incoming_message | check text message icon and number on DUT; check on DUT the text message icon presence (and message number) | send message action | High |
| R29 | navigate_message | open text message screen by any method; "By any method" (when followed by open message screen sub-step in same group) | check icon only | High |
| R30 | back_to_idle | go back homepage/idle; DUT returns in idle state; device returns to idle; return to idle state | Back key press only | High |
| R31 | initiate_outgoing_call | call between dectA and dectB; launch call; make a call between two devices | receive incoming call | High |
| R32 | navigate_calllog | launch call log app in menu screen | open central directory | High |
| R33 | lock_device | lock the DUT with handset MMI services (call server lock); activate handset lock; lock phone via MMI | check lock state; verify lock | High |
| R34 | *(repeat last step's intent)* | Redo step N; Repeat step N; Redo step N & M with different X; Repeat step N to M but: [explicit key follows in sub-steps] | new/different action verb | High |
| R35 | press_sk1_key | retrieve the call; unhold the call; resume the call; dect retrieve; when same case's hold action used SK1 | retrieve with different key | High |
| R36 | press_sk1_key | dectB hold dectA; hold remote party; put on hold (when same case uses SK1 for hold) | hold with different key | High |
| R37 | create_number_entry | select an entry and create a new contact or append an existing one with name and number from log; save as contact; append to contact | create top-level directory | High |
| R38 | initiate_outgoing_call_from_contact | launch call from newly created contact; call from contact; call using saved contact | generic outgoing call without contact | High |
| R39 | press_release_key | press the release key; press release key; release key pressed | reject softkey; press OK | High |
| R40 | press_sk_reject | press the right softkey "Reject"; press Reject softkey; press softkey Reject; reject incoming call via softkey | release key; press OK | High |
| R41 | check_number_in_contact_or_not | The number/name of phone X is not present in any contact list of DUT Y; number not in contact list; not present in any contact | check lock state; dial number | High |
| R42 | navigate_to_settings_menu | go to the application menu screen, select the Settings menu; go to Settings menu; open Settings menu; navigate to Settings | Central Directory; call log | High |
| R43 | navigate_to_language_menu | select and active the language menu; select language menu; open Language menu; navigate to Language settings | navigate to settings (without language) | High |

## Context-Statement Rows (NOT actions — keep needs_review)
Some action_text rows describe a background condition or precondition context rather than an executable action.
For these rows, `needs_review` is the correct output — do NOT force-map to a generic intent.

Recognition patterns:
- "[Device] is in [state]" constructs that describe observed state rather than what to do

> **NOTE**: The following patterns previously listed as context-statements now have canonical intents:
> - "The number/name of phone X is not present in any contact list of DUT Y" → `check_number_in_contact_or_not` (R41)
> - "DUT returns in idle state" → `back_to_idle` (R30)

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
