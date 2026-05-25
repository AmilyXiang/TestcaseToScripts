# KB to DSL Semantic Skill

## Goal
Convert KB rows into DSL rows with semantic intent mapping, while preserving traceability and stable structure.

## Input
- Preferred: KB JSON with shape:
  - meta
  - rows[] with fields:
    - case_id
    - title
    - step_no
    - sub_step_no
    - normalized_action
    - normalized_expected_result
    - keywords

## Output
- DSL JSON with shape:
  - meta
  - rows[]:
    - case_id
    - step_no
    - sub_step_no
    - dsl:
      - action: intent, actor, target, text
      - expected: intent, text
      - trace: title, keywords

## Mandatory Standards
1. Preserve case_id/step_no/sub_step_no exactly.
2. Do not mutate normalized_action and normalized_expected_result text.
3. Map action intent and expected intent using semantic rules, not delimiter heuristics.
4. Keep actor default as current_device unless source provides explicit actor.
5. Keep target as empty string unless source provides explicit target.
6. If no rule matches, fallback to custom_action/custom_expected.
7. Never output empty dsl.action.text when input action text exists.
8. If LLM is used for disambiguation, temperature must be 0.0.

## Action Intent Mapping Baseline
- initiate_outgoing_call: dial/make call/outgoing call
- accept_call: answer/pick up
- reject_call: reject/decline
- end_call: hang up/release/on-hook
- hold_call: hold
- resume_call: retrieve/resume
- open_directory: directory/contact/call log
- send_message: message/send text
- navigate_ui: press/select/open/enter/go to/launch
- verify_display: watch/check presentation
- custom_action: fallback

## Expected Intent Mapping Baseline
- assert_call_established: call established/connected/possible
- assert_call_released: call released/ended
- assert_ringing: ring/ringing
- assert_displayed: displayed/visible/icon/on display
- assert_audio_quality: audio quality/no perturbation
- assert_navigation_ok: navigation/scroll/options working
- assert_message_sent: message sent
- assert_generic: generic verification statement
- custom_expected: fallback

## Quality Gates
1. row_count(output) == row_count(input)
2. Required fields present in every row.
3. Intent fallback rate is reported:
  - action_custom_ratio
  - expected_custom_ratio
4. No missing trace title/keywords if present in KB.

## Suggested Metadata
- description: DSL generated from KB with semantic intent mapping
- stage: kb_to_dsl
- generator: copilot-llm-direct

## Reusable Prompt
"Use kb_to_dsl_semantic_skill. Convert KB rows to DSL with semantic intent mapping, preserve traceability fields, keep stable row count, and report fallback ratios. Do not split by delimiters."