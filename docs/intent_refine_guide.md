# Guide: How to Use Intent Refine Mapping

## What this guide solves
Inputs can have many wording variants, but the same meaning should produce the same `action_intent` or `precondition_intent`.

This guide ensures stable, repeatable outputs using the mapping templates.

Related template:
- `docs/intent_refine_mapping_template.md`
- `docs/expected_intent_mapping_template.md`
- `docs/precondition_intent_mapping_template.md`

## When to use this guide
Use this process in the following cases:
1. Before any new intent-refine batch run.
2. When new wording appears for existing meaning.
3. When regression is suspected after rule updates.
4. During acceptance review before writing output files.

## Operating Modes

### Mode A: Read-only preview (recommended first)
- Do not modify any JSON files.
- Produce a preview report:
  - matched rows by rule id
  - changed rows count
  - `needs_review` rows
  - conflicts encountered

### Mode B: Write output
- Run only after approval of Mode A report.
- Apply mappings to output version file (for example vN -> vN+1).
- Keep source file immutable.

## Standard Workflow
1. Normalize text
- lowercase for matching
- normalize punctuation/quotes/spaces
- keep original source text unchanged

2. Apply priority rules
- use strict first-match-wins order
- follow conflict resolution in template

3. Assign canonical intent
- output only from approved canonical list
- never invent ad-hoc intent names
- if unmatched or low confidence, keep existing intent unchanged

4. Handle unmatched rows
- keep existing intent unchanged
- assign `needs_review` in report
- add to review report

5. Validate
- no forbidden/new intent values
- deterministic rerun check (same input -> same output)
- compare against golden cases

## Acceptance Checklist
A run is accepted only if all are true:
- 100% rows have valid canonical intents from allowed list or `needs_review`
- 0 unintended changes in non-target rows
- conflict rules applied in correct order
- regression checks pass on golden dataset
- summary report generated

## Suggested Report Format
- input_file
- output_file
- total_rows
- changed_rows
- unchanged_rows
- matched_by_rule (R01-R32 counts)
- unmatched_rows_count
- unmatched_samples (top N)
- conflict_hits
- canonical_intent_distribution

## How to maintain stability over time
1. Add new synonym expressions under existing rule ids first.
2. Create a new rule id only if semantics are truly new.
3. Update conflict resolution whenever overlap appears.
4. Re-run regression after every template change.
5. Keep versioned outputs for traceability.

## Example decision pattern
- Text: "Press the release key."
- Candidate meanings: `press_key`, `reject_call`
- Context: incoming call ringing and release action
- Final mapping: `reject_call` (meaning-first rule)

## Common pitfalls
- Matching only keywords without semantics
- Letting generic rules run before specific rules
- Mixing setting-selection with runtime action (example: select any key vs press any key to answer)
- Silent introduction of new intent labels
- Missing `actor` field when action_text names a specific device (e.g. "dectA", "handset B", "DUT A") — always add `"actor": "A"/"B"` after `action_intent` in those rows; omitting it loses multi-device execution context

## Practical recommendation
Always run Mode A (read-only) first, review, then run Mode B (write output). This is the safest path for stable intent refinement.