# DSL to Action Schema Skill

## Reference Documents

Before generating, load and follow these two reference files as the authoritative source of truth:

- **`docs/operations_reference.md`** — canonical definition of every `operation` value; the **Press-Key Unified Rule** (`ui.press_key` + `element`); physical primitive descriptions; Terminology Glossary (DUT, SK1/SK2/SK3, Navigator Keys, Back Key, lock_device).
- **`docs/assertions_reference.md`** — canonical definition of every `assertions[].type` value; typical text patterns for each assertion; the `assert.none` rule for intermediate atomic steps; multi-actor chaining with `;` separator.

If any mapping rule in this skill conflicts with an entry in the reference docs, **the reference doc takes precedence**.

---

## Goal
Convert DSL rows into executable action schema rows with operation and assertion mapping.

## Input
- DSL JSON with shape:
  - meta
  - rows[]:
    - case_id
    - step_no
    - sub_step_no
    - dsl.action.intent
    - dsl.action.actor
    - dsl.action.target
    - dsl.action.text
    - dsl.expected.intent
    - dsl.expected.text
    - dsl.trace.title
    - dsl.trace.keywords

## Output
- Action Schema JSON with shape:
  - meta
  - rows[]:
    - case_id
    - step_no
    - sub_step_no
    - atomic_no          ← 1-based index within the sub_step (1 when not split)
    - action_schema:
      - operation          ← physical primitive (what you literally do)
      - semantic_intent    ← telephony/contacts/messaging/ui goal (why)
      - params: actor, target, element?, label?, text
      - assertions[]: type, text
      - meta: action_intent, expected_intent, title, keywords

> Three-layer atomization model:
> 1. `operation`       — fixed physical primitive vocabulary (what device action)
> 2. `semantic_intent` — business/telephony meaning (what feature is tested)
> 3. `atomic_no`       — position when one sub_step contains N sequential actions
>
> A sub_step with text "navigate to X and press SK1 Hold" becomes two rows:
> atomic_no=1: ui.navigate / navigate_ui
> atomic_no=2: ui.press_softkey / telephony.hold_call  (assertions kept here only)

## Mandatory Standards
1. Preserve case_id/step_no/sub_step_no exactly.
2. Deterministic mapping from intent to operation/assertion type.
3. Keep original text (atomic slice) in params.text; assertions[].text unchanged.
4. Never drop actions; output row_count >= input row_count (splits increase count).
5. If no mapping exists, use custom.execute and assert.custom.
6. If LLM is used for disambiguation, temperature must be 0.0.

## Atomic Splitting Rules
1. **Detect multi-verb steps**: count distinct action verbs in dsl.action.text
   (press, dial, navigate, select, open, check, move, send, answer, reject, hold, retrieve, etc.).
   If N > 1 verbs belong to N sequential physical actions, split into N atomic rows.
2. **Split text** by verb-introducing clause boundaries:
   connectors: `", then"`, `", and"`, `"; "`, `"before"`, `"after"`.
   Each clause becomes one atomic row's `params.text`.
3. **Assertions placement**: keep original assertions only on the **last** atomic row.
   All preceding atomic rows get `[{"type": "assert.none", "text": "(intermediate atomic step)"}]`.
4. **False-positive guard**: do NOT split when:
   - the second verb is a purpose/result clause ("press SK1 *to hold* the call")
   - the word is a UI label/softkey name ("'Reject'", "'Hold'")
   - there is only one physical interaction (e.g. "press and hold")
5. **atomic_no**: sequential integer starting at 1 within each (case_id, step_no, sub_step_no) group.
   Single-action steps always get atomic_no = 1.
6. Report `atomized_extra_rows` = total_rows − original_row_count in meta.

## Semantic Intent Mapping Baseline
(maps `meta.action_intent` from DSL row → `semantic_intent` value)
- initiate_outgoing_call -> telephony.make_call
- accept_call            -> telephony.answer_call
- reject_call            -> telephony.reject_call
- end_call               -> telephony.end_call
- hold_call              -> telephony.hold_call
- resume_call            -> telephony.resume_call
- open_directory         -> contacts.open_directory
- send_message           -> messaging.send_message
- navigate_ui            -> navigate_ui
- verify_display         -> verify_display
- custom_action          -> custom_action

## Physical Primitive Mapping
(maps `meta.action_intent` + text analysis → `operation` value)

Fixed vocabulary of physical primitives:
- `ui.dial_number`       — enter digits on dial pad
- **`ui.press_key`**     — press any physical key; `params.element` identifies which key (see `docs/operations_reference.md` → *Press-Key Family*)
  - `element: "call_key"`    → replaces `ui.press_call_key`
  - `element: "answer_key"`  → replaces `ui.press_answer_key`
  - `element: "release_key"` → replaces `ui.press_release_key`
  - `element: "any_key"`     → replaces `ui.press_any_key`
  - `element: "SK1/SK2/SK3"` → replaces `ui.press_softkey`; also set `params.label`
  - `element: "nav_up/nav_down/nav_left/nav_right/ok_key/back_key"` → replaces `ui.press_nav_key`
- `ui.navigate`          — menu navigation without a specific key press (swipe, scroll, abstract selection)
- `ui.check_display`     — observe/verify screen content
- `ui.open_app`          — open an application or feature from home screen
- `ui.send_message`      — compose and send a text/chat message
- `custom.execute`       — any action that cannot be mapped to a primitive above

Mapping rules:
| action_intent              | condition on text                              | operation       | element value                    |
|----------------------------|------------------------------------------------|-----------------|----------------------------------|
| initiate_outgoing_call     | text contains "dial"/"number"/"enter digit"    | ui.dial_number  | —                                |
| initiate_outgoing_call     | text contains "press call key"/"send key"      | ui.press_key    | `"call_key"`                     |
| initiate_outgoing_call     | text contains "SK1"/"SK2"/"SK3"/"softkey"      | ui.press_key    | `"SK1"` / `"SK2"` / `"SK3"`     |
| accept_call                | text contains "any key"                        | ui.press_key    | `"any_key"`                      |
| accept_call                | (default)                                      | ui.press_key    | `"answer_key"`                   |
| reject_call                | —                                              | ui.press_key    | `"SK"` + label `"Reject"`        |
| end_call                   | —                                              | ui.press_key    | `"release_key"`                  |
| hold_call                  | —                                              | ui.press_key    | `"SK"` + label `"Hold"`          |
| resume_call                | —                                              | ui.press_key    | `"SK"` + label `"Retrieve"`      |
| open_directory             | text contains "SK"/"softkey"                   | ui.press_key    | `"SK1"` / `"SK2"` / `"SK3"`     |
| open_directory             | text contains "open"/"launch"/"Call Log"       | ui.open_app     | —                                |
| send_message               | —                                              | ui.send_message | —                                |
| navigate_ui                | text contains "SK"/"softkey"                   | ui.press_key    | `"SK1"` / `"SK2"` / `"SK3"`     |
| navigate_ui                | text contains "nav key"/"navigation key"/"OK"  | ui.press_key    | `"nav_up/down/left/right"` / `"ok_key"` / `"back_key"` |
| navigate_ui                | (default — no key mentioned)                   | ui.navigate     | —                                |
| verify_display             | —                                              | ui.check_display| —                                |
| custom_action              | —                                              | custom.execute  | —                                |

For all `ui.press_key` rows, extract from text:
- `params.element`: key identifier (see element value column above; use exact values from `docs/operations_reference.md` Press-Key table)
- `params.label`:   display label in quotes, e.g. `"Hold"`, `"Retrieve"`, `"View"`, `"Reject"` — for softkeys only

## Assertion Mapping Baseline
- assert_call_established -> assert.call.established
- assert_call_released -> assert.call.released
- assert_ringing -> assert.call.ringing
- assert_displayed -> assert.ui.displayed
- assert_audio_quality -> assert.audio.quality
- assert_navigation_ok -> assert.ui.navigation_ok
- assert_message_sent -> assert.message.sent
- assert_generic -> assert.generic
- custom_expected -> assert.custom

## Quality Gates
1. row_count(output) >= row_count(input)  (splits increase count).
2. Every row has non-empty `operation` (physical primitive).
3. Every row has non-empty `semantic_intent`.
4. Every row has at least one assertion (may be assert.none for intermediate atomic steps).
5. Custom mapping ratios are reported:
   - `custom_operation_ratio`   — ratio of rows with `custom.execute`
   - `custom_assert_ratio`      — ratio of rows with `assert.custom`
   - `operation_specific_ratio` — ratio of rows using a specific primitive other than `ui.navigate`
   - `atomized_extra_rows`      — number of extra rows created by atomic splitting
6. All trace fields propagated to action_schema.meta.
7. For `ui.press_softkey` rows: `params.label` should be non-empty if a label keyword is present in text.
8. Within each (case_id, step_no, sub_step_no) group: only the highest atomic_no row has real assertions.

## Suggested Metadata
- description: Action schema (two-layer: physical operation + semantic intent) generated from DSL
- stage: dsl_to_action_schema
- generator: copilot-llm-direct
- schema_version: "2.0"

## Reusable Prompt
"Use dsl_to_action_schema_skill. Convert DSL rows to action schema with two-layer architecture: determine `semantic_intent` from DSL action_intent, then determine `operation` (physical primitive) from action_intent + text analysis. Extract `element` and `label` for softkey/nav rows. Preserve all traceability fields, keep row count stable, and report custom mapping and operation_specific ratios."