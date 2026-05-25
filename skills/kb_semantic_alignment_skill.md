# KB Semantic Alignment Skill

## Goal
Generate KB from cleaned or auto_cases input using semantic understanding, not delimiter-based splitting.

## Input
- Preferred: testrail/*auto_cases.json
- Optional: testrail/*.cleaned.json

## Output
- KB file with rows:
  - case_id
  - title
  - step_no
  - sub_step_no
  - normalized_action
  - normalized_expected_result
  - keywords

## Mandatory Standards
1. Never split action/expected by newline, bullet, or punctuation only.
2. Always do semantic clause extraction first.
3. Keep execution order monotonic inside each step.
4. Align expected clauses to actions by semantic compatibility, with local position bias.
5. Drop context-only clauses from action rows (notes, reminders, disclaimers).
6. Keep one row per actionable atomic clause.
7. If expected is fewer than actions, reuse nearest semantic expected; do not leave empty expected unless source is empty.
8. If expected is more than actions, merge related expected clauses into the nearest action (separator: " ; ").
9. Preserve traceability fields: case_id, title, step_no, sub_step_no.
10. For LLM calls (if any), use temperature=0.0.

## Semantic Procedure
### 1) Normalize
- Strip HTML tags while preserving structural boundaries:
  - <br>, </p>, </li> -> sentence boundary
  - <li> -> bullet prefix
- Normalize spaces and escaped characters.

### 2) Semantic Clause Extraction
- Segment by sentence intent, not symbols.
- Keep connector-aware boundaries:
  - then, after, before, while, when, note
- Merge tiny dependent fragments back to parent clause.

### 3) Clause Classification
Action clause classes:
- action: perform an operation (press/select/open/dial/send/read...)
- observation: explicit verification action (check/verify/watch)
- context: notes/disclaimers/non-executable fragments (filtered out)

Expected clause classes:
- call_state
- ringing
- ui_display
- navigation
- messaging
- generic

### 4) Semantic Alignment (Core)
For each action clause A_i:
- Compute baseline expected index by relative order.
- Search only in local window around baseline (monotonic constraint).
- Score candidates by:
  - domain compatibility (telephony/directory/messaging/observation)
  - lexical overlap bonus
  - distance penalty from baseline
- Pick best candidate as aligned expected for A_i.

### 5) Post Processing
- Deduplicate exact adjacent duplicates only when both action domain and expected text are identical.
- Generate keywords from title + action + expected semantic terms.

## Quality Gates (Must Pass)
1. No empty normalized_action rows.
2. step_no and sub_step_no strictly increasing within each case/step.
3. No context-only rows.
4. Random sample check:
  - telephony cases: action aligns to call/ringing/display assertions.
  - messaging cases: action aligns to message/display assertions.
5. Row count should be stable against semantic decomposition (not symbol explosion).

## Suggested Metadata
- description: KB generated with monotonic semantic alignment
- alignment_strategy: monotonic-semantic
- generator: copilot-llm-direct

## Reusable Prompt
"Use kb_semantic_alignment_skill. Read auto_cases or cleaned data, generate KB with semantic clause understanding and monotonic semantic alignment. Do not split by delimiters only. Keep traceability fields and output quality gates."
