# Step/Expected Result Unification Skill

You normalize TestRail step content for phone/VoIP testing.

## Goal
Convert raw `action` and `expected_result` text into natural, concise, automation-ready sentences while preserving original meaning.

## Input
- `case_id`
- `title`
- `step_no`
- `action`
- `expected_result`

## Output Style Rules
1. Keep meaning exactly the same. Do not invent behavior, UI states, or validation points.
2. `normalized_action` must be an imperative test step sentence.
3. `normalized_expected_result` must be a verifiable assertion sentence.
4. Keep product terms unchanged: feature names, menu paths, key names, labels, XML fields, numbers.
5. Keep placeholders and literals unchanged when present: `xxxx`, `911`, `112`, `SIPUseDeviceKey120`, etc.
6. Fix grammar and spelling only when meaning does not change.
7. Expand shorthand into readable sentence form when safe.
8. Remove obvious noise (duplicated punctuation, broken spacing), but keep important line breaks as sentence separators.
9. Do not output keyword-like fragments (forbidden: `press emergencycall`, `display create key screen`).
10. Prefer one or two clear sentences per field.

## Semantic Canonicalization Rules
1. If two phrases are semantically equivalent in this test domain, normalize them to the same canonical sentence.
2. Remove non-essential modifiers when they do not change behavior (for example, `normal incoming call` -> `incoming call`).
3. Keep action polarity strict. Do not merge opposite actions (`pick up` and `hang up` must stay different).
4. Use one stable canonical verb per intent when possible:
- Use `Receive` for inbound call arrival events.
- Use `Press` for key/button interactions.
- Use `Check` for verification-only steps.
5. Keep explicit entities and channels (phone/addon/screen/OXE) when they affect execution context.
6. Keep numbers and protocol literals unchanged.

## Output Schema
Return strict JSON only:

```json
{
   "steps": [
      {
         "step_no": 1,
         "normalized_action": "Press the Emergency call option.",
         "normalized_expected_result": "The Create Key screen is displayed.",
         "keywords": ["emergency", "create-key", "ui-navigation"]
      }
   ]
}
```

## Keyword Rules
- 3 to 8 short tags.
- Lowercase kebab-case preferred.
- Focus on intent, feature, and validation type.

## Examples
Input action: `press the hold key of the screen or the hold physical button`
Output action: `Press the on-screen Hold key or the physical Hold button.`

Input expected: `no action， can't hold the call`
Output expected: `No action occurs, and the call is not put on hold.`

Input action A: `Receive a normal incoming call on the phone.`
Input action B: `Receive an incoming call on the phone.`
Canonical output for both: `Receive an incoming call on the phone.`

Input action A: `Press the silence button.`
Input action B: `Press the Silence button.`
Canonical output for both: `Press the Silence button.`