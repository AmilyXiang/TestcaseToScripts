# DSL to Action Schema Skill

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
    - action_schema:
      - operation
      - params: actor, target, text
      - assertions[]: type, text
      - meta: action_intent, expected_intent, title, keywords

## Mandatory Standards
1. Preserve case_id/step_no/sub_step_no exactly.
2. Deterministic mapping from intent to operation/assertion type.
3. Keep original text in params.text and assertions[].text.
4. Never drop rows; output row_count must equal input row_count.
5. If no mapping exists, use custom.execute and assert.custom.
6. If LLM is used for disambiguation, temperature must be 0.0.

## Operation Mapping Baseline
- initiate_outgoing_call -> telephony.make_call
- accept_call -> telephony.answer_call
- reject_call -> telephony.reject_call
- end_call -> telephony.end_call
- hold_call -> telephony.hold_call
- resume_call -> telephony.resume_call
- open_directory -> contacts.open_directory
- send_message -> messaging.send_message
- navigate_ui -> ui.navigate
- verify_display -> ui.check_display
- custom_action -> custom.execute

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
1. row_count(output) == row_count(input)
2. Every row has non-empty operation.
3. Every row has at least one assertion.
4. Custom mapping ratios are reported:
  - custom_operation_ratio
  - custom_assert_ratio
5. All trace fields propagated to action_schema.meta.

## Suggested Metadata
- description: Action schema generated from DSL
- stage: dsl_to_action_schema
- generator: copilot-llm-direct

## Reusable Prompt
"Use dsl_to_action_schema_skill. Convert DSL rows to action schema with deterministic intent mappings, preserve all traceability fields, keep row count stable, and report custom mapping ratios."