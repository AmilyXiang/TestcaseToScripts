# Precondition Intent Mapping Template

## Purpose
Provide a stable and auditable mapping standard for precondition_intent.
**All precondition_intent values MUST come from the canonical list below. Do NOT invent new intent names.**

## Canonical Intent List (exhaustive)

| Intent | Meaning | Example precondition_text |
|--------|---------|--------------------------|
| `ui_context` | A specific screen/menu is already open | "In idle.", "Settings menu is open." |
| `condition_state` | Device/feature is in a specific state (locked, active, enabled) | "Auto answer is active.", "The feature is enabled." |
| `sequence_state` | A prior step has completed; DUT is back to idle | "After the previous step.", "DUT is back to idle." |
| `data_state` | A data object exists (contact, log, message) | "A contact entry exists in the directory." |
| `device_context` | Remote device has specific setup | "Phone B has CLIP activated.", "DUT A is registered." |
| `confirm_lock_state` | DUT or call server lock is active/inactive | "When the local lock is active.", "The DUT is locked." |
| `confirm_ring_state` | During ringing phase | "During the ringing phase." |
| `confirm_conversation_state` | During an active call / conversation state | "During the conversation.", "Call is established." |
| `confirm_dialing_end` | Before/during end of dialing phase | "Before the end of the dialing." |
| `confirm_central_directory` | Central directory is configured and accessible | "Central directory is configured." |
| `confirm_dut_is_in_contact_or_not` | Phone B's number is (not) in DUT contact list | "Phone B's number is not in any contact list of DUT A." |
| `hang_up` | Call has been released / DUT returned to idle after call | "After hangup.", "DUT returns to idle state." |
| `confirm_text_message_screen_open` | Text message screen is already open | "Text message screen is open." |
| `confirm_call_log_in_every_tab_or_not` | Call log state (empty or populated) | "Call log is empty on every tab." |
| `custom_precondition` | Does not match any above category | (catch-all) |

## Canonical Mapping Rules (text → intent)
- "Before the end of the dialing" → `confirm_dialing_end`
- "During the ringing" / "During the ringing phase" → `confirm_ring_state`
- "During conversation" / "During the conversation" / "During the call" → `confirm_conversation_state`
- "When the local lock is active" / "DUT is locked" / "call server lock" → `confirm_lock_state`
- "After hangup" / "DUT returns in idle" / "back to idle" → `hang_up`
- "In idle" / "idle screen" / "homepage" → `ui_context`
- "Phone B has CLIP activated" / "DUT A is registered" / device setup → `device_context`
- "number of phone B is not present in any contact" → `confirm_dut_is_in_contact_or_not`
- "central directory is configured" → `confirm_central_directory`
- "text message screen" / "message screen is open" → `confirm_text_message_screen_open`
- "Call log is empty" / "delete if not empty" → `confirm_call_log_in_every_tab_or_not`

## Multi-State Conflict Rule
For a mixed precondition like "During the ringing phase.; During the conversation.":
- Use only one state intent (cannot be simultaneous).
- Default choice: `confirm_conversation_state`

## Guardrails
- Preserve first: if a row already uses an approved intent and no explicit overwrite rule applies, keep original.
- Do not downgrade approved specialized intents to generic `sequence_state`.
- Do not mutate precondition_text unless explicitly requested; refine precondition_intent only.
- **NEVER use an intent value not in the canonical list above.**
- **Imperative-verb sentences are ACTIONS not preconditions** — do not assign any precondition_intent to them.

## Review Checklist
- All `sequence_state` rows are either mapped to a more specific intent or intentionally retained.
- `confirm_dut_is_in_contact_or_not` rows remain untouched unless a dedicated rule says otherwise.
- Mixed ringing/conversation rows use a single chosen intent.
- No unrelated case_id rows changed.
- No invented intent names in output.
