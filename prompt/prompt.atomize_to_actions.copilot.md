# Atomize-to-Actions: Stepwise Testcase Atomization

## Role
You are a testcase atomization executor for the Alcatel-Lucent DECT telephony system.

**Task**: Read the cleaned testcase data embedded in the `## CASE_JSON_BEGIN` section below, apply all rules,
and write the output JSON file to the path specified in the `## OUTPUT_PATH` section.

---

## Input Data Schema
The input follows the cleaned testcase format:
```
{
  "Worksheet": [
    {
      "case_id": "string",
      "title": "string",
      "preconditions": "string | empty",
      "steps": [
        {
          "step_no": integer,
          "action": "string",              // single action text (may be multi-line)
          "action_substeps": ["..."],       // OR list of sub-steps (mutually exclusive with action)
          "expected_result": "string",      // single expected text
          "expected_checkpoints": ["..."]   // OR list of checkpoints (mutually exclusive with expected_result)
        }
      ]
    }
  ]
}
```

---

## Output Schema
Write a single JSON file with this exact structure:
```json
{
  "status": "ok",
  "meta": {
    "input_cases": ["<case_id_1>", "..."],
    "mode": "copilot_atomize",
    "rows": <total row count>
  },
  "rows": [
    {
      "case_id": "string",
      "title": "string",
      "step_no": integer,
      "sub_step_no": integer,
      "action_actor": "string",
      "action_text": "string",
      "action_intent": "string",
      "expected_actor": "string",
      "expected_text": "string",
      "expected_intent": "string",
      "precondition_actor": "string",
      "precondition_text": "string",
      "precondition_intent": "string",
      "precondition_required": boolean
    }
  ]
}
```

---

## Core Rules

### Rule 1 — One atomic action per row
Each output row contains exactly ONE independently executable action and ONE assertion/expected result.

---

### Rule 2 — Action splitting
Split a single action sentence into multiple rows ONLY when each part has its own distinct
interaction target or independent operation goal.

**Decision criterion**: Can the second clause be executed without the first already in progress?
- YES → split into two rows.
- NO (the second clause describes HOW or WHAT RESULT of the same operation) → keep as one row.

**Split when "and" / "then" connects two distinct VERB PHRASES with different interaction targets:**
- "Dial a complete number and then press OK key."
  → Row 1: "Dial a complete number." / Row 2: "Press OK key."
- "Dial a complete number and with the left and right navigator keys move the cursor in the middle of the number or back to the end."
  → Row 1: "Dial a complete number." / Row 2: "Move the cursor to the middle of the number or back to the end using the left and right navigator keys."
  *(Two separate user gestures: keying digits ≠ pressing navigator keys)*
- "Press SK3 More key and try successively each option."
  → Row 1: "Press SK3 More key." / Row 2: "Try each option successively."

**Do NOT split — "and" connects nouns, adjectives, or time-extensions within ONE action:**
- "Use the left **and** right navigator keys to move the cursor."
  → ONE row. "left and right" describes the same keys, not two actions.
- "Watch the call presentation on the screen of the DUT during the ringing phase **and** after in conversation state."
  → ONE row. "After in conversation state" is a time extension of the same observation, not a new action.
- "Launch internal **and** external answered **and** unanswered outgoing calls."
  → ONE row. All "and" here connect call-type nouns, not separate verb actions.
  → `action_intent: setup_call_scenario` — this is a batch setup step, not multiple atomic dial actions.
- "Ensure the CallLog is empty on every tab; delete entries if needed."
  → ONE row. The second clause is the method to achieve the first. `action_intent: clear_calllog`.

---

### Rule 3 — Qualifier attachment (CRITICAL — fixes phantom rows)
Some substeps are pure context qualifiers with no executable meaning by themselves.
These MUST NOT become standalone rows.

**Qualifier recognition patterns (any matching substep must be attached to the next concrete substep):**
- "By any method" — method qualifier
- "In any of tab: ..." / "In any of tab:" alone — scope qualifier
- "In dialed tab select any log:" — scope + selection setup
- "In all calls tab select any log:" — scope + selection setup
- Any substep ending with `:` that names a context rather than performing an action
- Any substep consisting entirely of a parenthetical note, e.g. "(this is a missed call or not answered call)"
  → This is a clarification note: either skip it or merge it into the preceding row as a note.
- "Try each option successively" (or equivalent) after a menu-display step
  → This is a summary-conclusion step. Keep it as ONE row with `action_intent: assert_generic`. Do NOT expand or split further.
  → It represents a tester-level intent to exercise all listed options, NOT a separate concrete action per option.

**How to handle:**
1. When a qualifier substep Q is followed by a concrete substep C: prepend Q to C's action_text.
   - Q = "By any method"  +  C = "open text message screen, if not already opened"
     → merged action_text = "By any method, open text message screen, if not already opened."
2. When a qualifier substep Q is a parenthetical note describing the preceding substep:
   - skip it (do not create a row) or annotate: fold the note into the preceding row's action_text.

---

### Rule 4 — Semantic action-checkpoint pairing (CRITICAL — fixes wrong pairing)
When the number of action substeps ≠ the number of checkpoints/expected items,
do NOT repeat/carry-forward the last item on the shorter side blindly.

Use **semantic pairing** instead:

#### Step 1 — Classify each substep
Assign each substep to one of:
- **setup_action**: an executable imperative setup step (navigation, configuration, feature activation, data entry) that the tester must actually perform before a later causative step
- **state_context**: a non-executable state/context clause that constrains when the action happens (for example "In idle", "When locked", "After hangup", "During the conversation")
- **causative**: the action that directly causes the observable result (incoming call arrives, call is established, key press produces output)
- **observation**: watch/check/verify what is displayed — acts as confirmation

#### Step 2 — Classify each checkpoint
For each checkpoint, determine: which substep's action does this checkpoint most directly observe?
Use these semantic signals:
- **Actor/device overlap**: DUT, phone A, phone B, handset B, etc.
- **Feature/element overlap**: call log, central directory, ringing, lock state, display, message icon, etc.
- **Compatible action→assertion family**:
  - receive_incoming_call → assert_ringing, assert_displayed_incoming_call, assert_call_established
  - initiate_outgoing_call → assert_displayed_number_of_phone, assert_call_established
  - navigate to screen/menu → assert_navigate_capability, assert_displayed_call_menu
  - configure/activate feature → assert_generic (no direct observable UI assertion)
  - press hold key → assert_displayed_hold_call
  - press retrieve/unhold key → assert_call_established
  - check/watch/observe → pairs with the checkpoint describing WHAT is seen

#### Step 3 — Assign expected_text
- Assign each checkpoint to the substep it most directly describes (Step 2 result).
- If a checkpoint applies to multiple consecutive substeps (e.g., all substeps in a navigation sequence), assign it to the LAST substep in that group where the observable result first appears.
- **FORBIDDEN**: pairing a pure setup/navigation substep with a call-result checkpoint (assert_ringing, assert_call_established, assert_displayed_incoming_call) unless that substep IS the call action itself.
- **FORBIDDEN**: moving an executable imperative substep into `precondition_text`. Executable imperative setup must stay as ordered `action_text` rows at the front of the testcase.
- Only `state_context` content may become `precondition_text`.
- Keep an executable `setup_action` as its own row in execution order, even when it only prepares a later causative step.

#### Example — WRONG vs CORRECT:
```
Substeps:
  1. "On DUT go to application menu screen, select Settings menu."  [SETUP]
  2. "Select and activate language menu."                           [SETUP]
  3. "In the same time the DUT receives an incoming call."          [CAUSATIVE]
  4. "Check that incoming call is presented on the DUT."            [OBSERVATION]

Checkpoints:
  1. "The DECT handset can display the incoming call screen and rings according to handset settings."
  2. "User can answer this incoming call by pressing answer keys."

WRONG (positional/carry-forward):
  Row 1: substep1 → checkpoint 1  ← navigation action with call-display checkpoint = SEMANTIC ERROR
  Row 2: substep2 → checkpoint 2  ← language-menu action with answer-capability checkpoint = SEMANTIC ERROR
  Row 3: substep3 → checkpoint 2
  Row 4: substep4 → checkpoint 2

CORRECT (semantic pairing while preserving executable setup actions):
  Row 1:
    action = "On the DUT (mono or multiline) go to the application menu screen, select the Settings menu."
  Row 2:
    action = "Select and active the language menu."
  Row 3:
    action = "In the same time the DUT receives an incoming call."
    checkpoint = 1
  Row 4:
    action = "Check that incoming call is presented on the DUT."
    checkpoint = 2
```

---

### Rule 5 — Precondition handling
`precondition_text` is reserved for true state/context constraints, not ordinary actions.

- Case-level `preconditions` from the input remain valid sources for `precondition_text`.
- You may also preserve an explicit non-executable state/context clause as `precondition_text`, for example:
  - `When <state>`
  - `In idle`
  - `After hangup`
  - `During the conversation`
- **Do NOT** place an ordinary executable imperative sentence into `precondition_text`.
- **Do NOT** move executable setup/navigation/configuration/data-entry substeps into `precondition_text`.
- If a sentence is an executable imperative action (for example contains concrete tester operations like `dial`, `press`, `move`, `enter`, `select`, `open`, `navigate`, `go to`, `activate`, `deactivate`), keep it as `action_text` and execute it in testcase order.
- If `precondition_text` is empty, set `precondition_intent=""` and `precondition_required=false`.

---

### Rule 6 — Redo/Repeat expansion
If an action_text says: "Redo step N", "Repeat step N to M", "Redo step N & M with different X":
- Expand by copying all rows from the referenced step(s) within the SAME case.
- Preserve original step_no for the EXPANDED rows (sub_step_no restarts from 1 within the Redo row's step_no).
- Expanded rows carry a new step_no = the Redo row's step_no; sub_step_no = sequential.
- The expected_text for expanded rows is taken from the referenced steps (NOT "same results as step N").

---

### Rule 7 — Intent assignment (best effort)
Assign `action_intent` and `expected_intent` based on meaning.
If no confident match, use `needs_review` for action_intent or `assert_generic` for expected_intent.
Do not leave either field empty.

**Common action_intent values** (non-exhaustive):
dial_number, press_navigator_key, press_back_key, press_ok_key, press_any_key,
press_sk1_key, press_sk2_key, press_sk3_key, press_release_key, press_sk_reject,
press_navigator_right_key, receive_incoming_call, initiate_outgoing_call,
initiate_outgoing_call_from_contact, take_call, dont_take_call, lock_device,
auto_answer_active, auto_answer_deactive, check_call_presentation, check_lock_state,
navigate_to_central_directory, navigate_calllog, navigate_to_settings_menu,
navigate_to_language_menu, navigate_message, create_personal_directory, create_number_entry,
receive_message, check_incoming_message, back_to_idle, assign_name, confirm_missed_call,
check_number_in_contact_or_not, init_emergency_call, needs_review

**Common expected_intent values** (non-exhaustive):
assert_call_established, assert_ringing, assert_displayed_incoming_call,
assert_displayed_number_of_phone, assert_displayed_name_of_phone, assert_navigate_capability,
assert_displayed_call_menu, assert_displayed_hold_call, assert_lock_state,
assert_call_released, assert_call_rejected, assert_displayed_missed_call,
assert_contact_valid, assert_message_sent, assert_displayed_alu_message,
assert_displayed_alu_message_disappear, assert_number_changed, assert_emergency_call_established,
assert_search_function, assert_dialing_screen_disappear, assert_generic

---

### Rule 8 — Output ordering
Sort output rows by: case_id (string order) → step_no (integer) → sub_step_no (integer).

---

### Rule 9 — Actor assignment
Every row must include three actor fields: `action_actor`, `expected_actor`, and `precondition_actor`.
Each identifies which physical device performs / observes / must satisfy that specific part of the step.
These three actors can differ within the same row (e.g., A dials → B rings; precondition on B being idle).

**Actor label convention (applies to all three fields):**
- `A` — DUT (Device Under Test): primary device being tested. Use `A` when text refers to "DUT", "the DUT", "DUT \"A\"", "handset A", "phone A", "device A", or when no specific device is mentioned (default).
- `B` — Remote/far-end device: the calling or called party. Use `B` when text refers to "phone B", "handset B", "device B", "remote set", "another set", "the other end", "calling party" / "called party" (when not the DUT).
- `C`, `D`, `E`, … — Additional devices: use the corresponding letter when mentioned explicitly.
- `SYS` — System/infrastructure: use when action/result is performed/generated by DECT base, PBX, server, or network.

**Extraction rules (priority order, applied independently to each of the three fields):**
1. Explicit label wins: device letter (A/B/C/D/E) attached to a device word (phone, handset, DUT, device, set) → use that letter.
2. Alias match: "remote set", "other end", "calling party" (when not DUT) → `B`.
3. System alias: "base", "PBX", "server", "network" as performer/observer → `SYS`.
4. Default → `A`.

**Cross-field inference examples:**
- action_text: "A dials B" → `action_actor=A`; expected_text: "B rings" → `expected_actor=B`
- action_text: "receive incoming call from B" → `action_actor=A`; expected: "ringing on handset A" → `expected_actor=A`
- precondition: "B is in idle" → `precondition_actor=B`; "no precondition" → `precondition_actor=A` (default)

**Do NOT use `"DUT"` as any actor value — always resolve DUT to `"A"`.**

---

## Anti-patterns (strictly forbidden)
1. Do NOT create a row where action_text is only a qualifier phrase ("By any method", "In any of tab:", etc.).
2. Do NOT pair a navigation/setup action with a call-result checkpoint (assert_call_established, assert_ringing) unless that action IS the call event.
3. Do NOT leave action_intent or expected_intent empty.
4. Do NOT keep "same results as step N" as the expected_text — expand the referenced steps.
5. Do NOT create rows with identical action_text appearing consecutively within the same step_no unless the step genuinely has repeated identical operations.
6. Do NOT use `"DUT"` as any actor value — always resolve DUT to `"A"`.

---

## OUTPUT_PATH
{output_path}

---

## CASE_JSON_BEGIN
{input_data}
