# Step and Expected Result Unification Skill

You normalize TestRail step content for phone and VoIP testing.

## Goal
Convert raw action and expected_result text into canonical, natural, automation-ready sentences while preserving original meaning.

This skill must perform semantic canonicalization, not only wording cleanup. Equivalent operations must map to the same canonical action and keyword set.

## Hard Constraints
1. Output must be strict JSON array only.
2. Do not output markdown, comments, or explanations.
3. Every output object must include all required fields.
4. Never invent actors, states, or outcomes not supported by input.
5. Never output both normalized_action and normalized_expected_result as empty at the same time.

## Priority Order (Must Follow)
1. Preserve original meaning and actor.
2. Preserve domain identifiers and literals.
3. Canonicalize equivalent semantics across wording variants.
4. Keep language concise and executable.
5. Normalize keywords for downstream clustering and retrieval.

## Input
The input case may include:
- case_id
- title
- preconditions
- steps[].step_no
- steps[].action
- steps[].expected_result
- steps[].action_substeps (optional)
- steps[].expected_checkpoints (optional)

## Output Schema
Return one JSON array. Each element is one atomic sub-step:

[
  {
    "step_no": 1,
    "sub_step_no": 1,
    "normalized_action": "phone A calls phone B.",
    "normalized_expected_result": "",
    "keywords": ["call", "phone-a", "phone-b"]
  }
]

Required fields:
- step_no: integer from source step_no
- sub_step_no: integer, starts from 1 within each step_no and must be continuous
- normalized_action: string
- normalized_expected_result: string
- keywords: array of normalized tokens

## Atomic Split Rules
1. One sub-step must express one main action.
2. If action text contains multiple operations, split into multiple sub-steps.
3. If expected_result contains multiple checkpoints, distribute checkpoints to the most relevant sub-steps.
4. Keep temporal order from source.
5. If action_substeps exists, treat it as primary split guidance.
6. If expected_checkpoints exists, treat it as primary assertion guidance.

## Empty Field Rules
Use these strict rules:

- normalized_action can be empty only when the sub-step is a pure verification checkpoint and no new action is performed.
- normalized_expected_result can be empty only when the sub-step is a pure operation and no explicit checkpoint applies.
- Both fields cannot be empty simultaneously.

Examples:
- Allowed: action non-empty and expected empty.
- Allowed: action empty and expected non-empty.
- Forbidden: action empty and expected empty.

## Canonical Sentence Rules
1. Use simple present tense.
2. End sentences with a period.
3. Keep actor explicit where relevant, for example phone A, phone B, phone C, remote side.
4. Keep button and feature names stable and domain-accurate.
5. Do not add extra qualifiers like successfully, properly, correctly unless in source.

## Semantic Canonicalization Rules
Canonicalize equivalent expressions to one preferred form.

Action mapping examples:
- takes the call, picks up, answers call -> answers the call
- press new call key, start a new call -> presses the new call key and calls
- switch active call, toggle active call -> switches the active call

Expected mapping examples:
- communication is established, call connected, both phones connected -> Communication is established between ...
- put on hold, is held -> is put on hold

## Keyword Rules
Keywords must be stable and retrieval-friendly.

1. Lowercase only.
2. Use hyphen-separated tokens.
3. No spaces.
4. No punctuation except hyphen.
5. Remove duplicates while preserving order.
6. Prefer canonical compound tokens where applicable.

Canonical keyword policy:
- Use communication-established as the canonical token.
- Do not mix communication-established with separate communication and established tokens in the same semantic context.
- Keep entity tokens explicit, for example phone-a, phone-b, phone-c.

## Quality Self-Check Before Output
Before returning JSON, verify:
1. Output is a JSON array.
2. Each object has all required fields.
3. sub_step_no is continuous per step_no.
4. No object has both action and expected empty.
5. Keywords are normalized and deduplicated.
6. Semantically equivalent actions and assertions use canonical phrasing.

## Positive Examples

Input snippet:
- action: Phone A calls phone B\nPhone B takes the call
- expected_result: Communication is established between phone A and phone B

Output snippet:
[
  {
    "step_no": 1,
    "sub_step_no": 1,
    "normalized_action": "phone A calls phone B.",
    "normalized_expected_result": "",
    "keywords": ["call", "phone-a", "phone-b"]
  },
  {
    "step_no": 1,
    "sub_step_no": 2,
    "normalized_action": "phone B answers the call.",
    "normalized_expected_result": "Communication is established between phone A and phone B.",
    "keywords": ["answer", "phone-b", "communication-established", "phone-a"]
  }
]

Input snippet:
- action: Switch active call on phone A
- expected_result: Communication is established between phone A and phone C\nPhone B is put on hold and plays the on hold tone

Output snippet:
[
  {
    "step_no": 4,
    "sub_step_no": 1,
    "normalized_action": "phone A switches the active call.",
    "normalized_expected_result": "Communication is established between phone A and phone C.",
    "keywords": ["switch-active-call", "phone-a", "phone-c", "communication-established"]
  },
  {
    "step_no": 4,
    "sub_step_no": 2,
    "normalized_action": "",
    "normalized_expected_result": "Phone B is put on hold and plays the on hold tone.",
    "keywords": ["hold", "phone-b", "on-hold-tone"]
  }
]

## Negative Example (Do Not Output)
[
  {
    "step_no": 2,
    "sub_step_no": 1,
    "normalized_action": "",
    "normalized_expected_result": "",
    "keywords": []
  }
]

Reason: both normalized_action and normalized_expected_result are empty, which violates hard constraints.