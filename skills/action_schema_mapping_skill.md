# Action Schema Mapping Skill (VoIP Test Steps)

## Objective
Design a Step Pattern to Action Schema extraction module for VoIP phone test cases.

Each test step is a natural language instruction.

Example input:
`phone A takes the second incoming call by switching it to the top of the screen and pressing the take call key.`

Example output:
```json
{
  "action": "answer_call",
  "params": {
    "device": "phone A",
    "call_index": 2
  }
}
```

## Required Pipeline
pattern
-> regex match (high precision)
-> embedding similarity fallback
-> generic

## Supported Actions
- dial_call
- answer_call
- hangup_call
- hold_call
- resume_call
- transfer_call
- conference_start
- conference_join
- mute_call
- unmute_call
- generic_action

## Extraction Rules
1. Rule-based action typing first.
2. Parameter extraction from the source step text:
   - device / from_device / to_device
   - call_index (first/second/third...)
   - key_name
   - prefix
   - participants
3. If no rule-based action can be determined, use embedding similarity against action prototypes.
4. If embedding confidence is below threshold, return `generic_action`.

## Output Contract
Per step output must contain:
- `action_schema.action`
- `action_schema.params`
- `action_schema_method` (`rule`, `pattern_mapping`, `embedding`, `generic`)
