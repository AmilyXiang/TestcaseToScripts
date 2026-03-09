# Step/Expected Result Unification Skill

You normalize TestRail step content for phone/VoIP testing.

## Goal
Convert raw `action` and `expected_result` text into canonical, natural, automation-ready sentences, while preserving original meaning. Focus not only on linguistic normalization but also on semantic canonicalization: equivalent operations must map to the same canonical action.

## Priority Order (Must Follow)
1. Preserve original meaning and actor.  
2. Preserve domain literals/identifiers.  
3. Canonicalize equivalent semantics across surface variations.  
4. Improve readability and grammar.  
5. Optimize keywords.

## Input
- `case_id`  
- `title`  
- `preconditions`  
- `step_no`  
- `action`  
- `expected_result`  

## Output Style Rules
1. Keep meaning exactly the same. Do not invent behavior, UI states, or validation points.  
2. `normalized_action` must be an imperative test step sentence using **canonical verbs**.  
3. `normalized_expected_result` must be a verifiable assertion sentence.  
4. Keep product terms unchanged: feature names, menu paths, key names, labels, XML fields, numbers.  
5. Keep placeholders and literals unchanged (`xxxx`, `911`, `112`, `SIPUseDeviceKey120`).  
6. Fix grammar/spelling only when meaning does not change.  
7. Expand shorthand into readable sentence form when safe.  
8. Remove obvious noise (duplicated punctuation, broken spacing), but keep meaningful line breaks.  
9. Do not output keyword-like fragments (`press emergencycall`, `display create key screen`).  
10. Prefer one or two clear sentences per field.  
11. Use canonical casing style for output.  
12. Treat `\n` as meaningful line breaks and convert to readable sentence separators.  
13. Remove HTML/markup before semantic normalization.

## Canonical Action Mapping (Mandatory)
1. Equivalent surface forms must map to the **same canonical action sentence**.  
2. Remove non-essential UI/interaction noise when it does not affect operation.  
3. **Canonical verbs for common phone operations**:

| Surface verbs / phrases | Canonical verb / action |
|------------------------|------------------------|
| call / dial / make call / place call / initiate call | Dial |
| answer / pick up / take call | Answer call |
| hang up / end / terminate | End call |
| hold / press hold / tap hold | Put the call on hold |
| resume / unhold / release hold | Resume the call |
| switch / toggle / swap active call | Switch the active call |
| mute / silence | Mute the call |
| unmute / release silence | Unmute the call |
| transfer / forward | Transfer the call |
| conference / join conference | Join or start conference |

4. For **incoming events vs remote responses**, canonicalize strictly:

- `Phone receives an incoming call.`  
- `Remote side answers the call.`  
- `Remote side rejects the call.`

5. UI-only actions that do not change call state should be omitted unless essential.  
6. Remove adjectives/modifiers that do not affect behavior (`normal incoming call` → `incoming call`).  

## Text Cleaning & Normalization
1. Lowercase input for parsing, but output uses canonical casing.  
2. Remove punctuation noise.  
3. Remove filler words (`please`, `kindly`, `then`, `after that`).  
4. Remove non-semantic HTML/Markdown tags (`span`, `img`, markdown images).  
5. Decode HTML entities.  

## Precondition Parsing
1. Normalize `preconditions` per case.  
2. Inherit precondition to all steps in the case.  
3. Apply same cleanup rules as above.  
4. Preserve server/device semantics (`OXE`, `ALE-30`, etc.).  
5. Do not copy step actions into preconditions.  

## Numbered Sub-Step Decomposition
1. Split embedded numbered steps (`1. ... 2. ...`) into separate sub-steps.  
2. Align action and expected result by index.  
3. After decomposition, output as `step1`, `step2`, ...  
4. Never keep multiple numbered instructions in a single normalized action.

## Actor and Intent Constraints
1. Keep actor explicit when it matters (`Phone`, `Remote side`, `User`).  
2. Use stable templates:  
   - `Phone receives an incoming call.`  
   - `Remote side answers the call.`  
   - `Remote side rejects the call.`  
   - User interaction: start with `Press`, `Dial`, `Check`, `Open`, `Select`, `Configure`, `Reset`, `Repeat`.  
3. Do not mix event type and response type.  

## Semantic Canonicalization Rules
1. Map semantically equivalent phrases to the same canonical sentence.  
2. Keep action polarity strict (`pick up` ≠ `hang up`).  
3. Use canonical verb per intent wherever possible.  
4. Keep numbers, devices, and protocol literals unchanged.  
5. Remove UI-only steps if they do not affect call state.  

## Output Schema
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