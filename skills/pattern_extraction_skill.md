# Clustering to Pattern Extraction Skill

You extract generalized step patterns from clusters of normalized test steps.

## Goal
Given one cluster of semantically similar step sentences, generate:
- A generalized pattern string with placeholders
- A regex that can match the same pattern
- A parameter list in placeholder order

## Input
A cluster object:

```json
{
  "cluster_id": 10,
  "examples": [
    "press dss key",
    "press emergency key",
    "press line key"
  ]
}
```

## Mandatory End-to-End Pipeline
This skill MUST be executed in the following strict order:

1. `clustering`
2. `token alignment`
3. `algorithm pattern extraction`
4. `LLM optimization pattern`

If a run skips any stage, the output is considered incomplete.

## Stage Details
### Stage 1: Clustering
Input must come from clustered normalized steps (for example `step_clusters_from_kb_v3.json`).

### Stage 2: Token Alignment
1. Tokenize each sentence into words.
2. Align tokens by column.

### Stage 3: Algorithm Pattern Extraction
1. Detect columns where tokens differ.
2. Replace differing columns with parameter placeholders.
3. Build generalized pattern string.
4. Build regex from the same template.

### Stage 4: LLM Optimization Pattern
1. Use LLM to improve readability and parameter naming.
2. Keep semantics unchanged.
3. Keep regex compatible with all examples in the cluster.
4. Do not remove required placeholders.

## Output Schema
```json
{
  "cluster_id": 10,
  "pattern": "press {key_name} key",
  "regex": "^press (.+?) key$",
  "parameters": ["key_name"]
}
```

## Rules
1. Keep shared tokens unchanged.
2. Use lowercase placeholders in snake_case.
3. Prefer semantically meaningful placeholder names (for example `key_name`, `button_name`, `device_name`).
4. If there are multiple varying columns, create multiple placeholders in left-to-right order.
5. Escape regex special characters for fixed tokens.
6. Regex should be anchored with `^` and `$`.
7. Use non-greedy capture groups `(.+?)` for placeholders.
8. If examples have different lengths and cannot be aligned safely, return a fallback pattern with one placeholder:
- `pattern`: `{free_text}`
- `regex`: `^(.+?)$`
- `parameters`: `["free_text"]`
9. LLM optimization may refine wording and placeholder names, but must preserve the same matching coverage.
10. For every cluster output, include the final optimized pattern, not only the algorithmic draft.

## Example
Input examples:
- `press dss key`
- `press emergency key`
- `press line key`

Output:
```json
{
  "pattern": "press {key_name} key",
  "regex": "^press (.+?) key$",
  "parameters": ["key_name"]
}
```
