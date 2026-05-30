# Precondition Intent Mapping Template

## Purpose
Provide a stable and auditable mapping standard for precondition_intent, similar to action_intent governance.

## Keep-As-Is (Approved)
- confirm_central_directory
- confirm_dut_is_in_contact_or_not
- hang_up
- confirm_text_message_screen_open

## Canonical Mapping Rules
- Before the end of the dialing. -> confirm_dialing_end
- During the ringing. -> confirm_ring_state
- During conversation. -> confirm_conversation_state
- During the conversation. -> confirm_conversation_state
- During the call setup. -> confirm_conversation_state
- When the local lock is active. -> confirm_lock_state

## Multi-State Conflict Rule
For a mixed precondition like:
- During the ringing phase.; During the conversation.

Use only one state intent (cannot be simultaneous).
Default choice:
- confirm_conversation_state

## Guardrails
- Preserve first: if a row already uses an approved intent and no explicit overwrite rule applies, keep original.
- Do not downgrade approved specialized intents to generic sequence_state.
- Do not mutate precondition_text unless explicitly requested; refine precondition_intent first.

## Suggested Metadata Block
Use a versioned patch block in output meta:
- precondition_intent_refine_vXX_patch
  - enabled
  - input
  - changed_rows
  - mode
  - guardrails
  - samples

## Review Checklist
- All sequence_state rows are either mapped or intentionally retained.
- confirm_dut_is_in_contact_or_not rows remain untouched unless a dedicated rule says otherwise.
- Mixed ringing/conversation rows use a single chosen intent.
- No unrelated case_id rows changed.
