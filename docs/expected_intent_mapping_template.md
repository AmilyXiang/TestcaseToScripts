# Expected Intent Mapping Template

## Purpose
Provide a stable and auditable mapping standard for expected_intent, aligned with action_intent and precondition_intent governance.

## Canonical Expected Intents
- assert_number_changed
- assert_contact_valid
- assert_emergency_call_established
- assert_search_function
- assert_navigate_capability
- assert_displayed_incoming_call
- assert_dialing_screen_disappear
- assert_displayed_number_of_phone
- assert_displayed_name_of_phone
- assert_call_established
- assert_lock_state
- assert_displayed_missed_call
- assert_displayed_call_menu
- assert_message_sent
- assert_displayed_alu_message
- assert_displayed_alu_message_disappear
- assert_displayed_hold_call
- assert_generic

## Core Mapping Principle
Map by validation target, not by isolated keywords.
Choose the dominant checkpoint semantics expressed by expected_text.

## Canonical Mapping Rules
- "The character before the cursor is deleted..." -> assert_number_changed
- "Each contact can be scrolled and validated" -> assert_contact_valid
- "Entered contacts are listed at local contacts app opening" -> assert_contact_valid
- "It's possible to make an emergency call" -> assert_emergency_call_established
- "Check that the search in the system directory is done correctly" -> assert_search_function
- "The navigation in the list is correctly working" -> assert_navigate_capability
- "Verify that the incoming call is presented on the DUT" -> assert_displayed_incoming_call
- "The current dialing will be ended" -> assert_dialing_screen_disappear
- "Number of the phone B is displayed on the DUT A" -> assert_displayed_number_of_phone
- "(OXE internal call: B's Display name is seen on DUT)" -> assert_displayed_name_of_phone
- "Call is established" / "call is possible" / "call is OK" / "conversation established" -> assert_call_established
- "The DUT can answer the incoming call with any keys" -> assert_call_established
- "The incoming call can be auto answered with handset voice mode" -> assert_call_established
- "user can answer this incoming call by pressing answer keys" -> assert_call_established
- "Check that the call can be established correctly" / "Establish the call" -> assert_call_established
- "DUT returns back in lock state" -> assert_lock_state
- "A missed call message icon is displayed on the top bar" -> assert_displayed_missed_call
- "All calls menu display" -> assert_displayed_call_menu
- "Check the missed call is right, the missed call icon disappear on top bar" -> assert_displayed_missed_call
- "Message sent" -> assert_message_sent
- "Only ALU message icon is displayed without number of unread messages" -> assert_displayed_alu_message
- "Alu message icon dissapears" -> assert_displayed_alu_message_disappear
- "dectB is hold. Screen display on A and B are correct" -> assert_displayed_hold_call
- "Contact can be created or appended with name ... and nb from selected call log" -> assert_contact_valid
- Fallback when no strong semantic hit exists -> assert_generic

## Conflict Resolution
- If one expected_text contains multiple checks, choose the dominant observable validation target.
- Prefer assert_call_established over assert_generic for successful call outcome wording.
- Prefer display-specific intents (for example assert_displayed_number_of_phone / assert_displayed_incoming_call) over generic display labels.
- If legacy label assert_call_state appears, normalize to assert_call_established.

## Guardrails
- Preserve first: if no high-confidence mapping applies, keep existing expected_intent unchanged.
- Do not downgrade an existing specific expected_intent to assert_generic without explicit reason.
- Do not invent new expected_intent values outside the canonical list.

## Suggested Metadata Block
Use a versioned patch block in output meta:
- expected_intent_refine_vXX_patch
  - enabled
  - input
  - changed_rows
  - mode
  - guardrails
  - samples

## Review Checklist
- assert_generic is used only when no stronger validation target is justified.
- Display-oriented expectations are separated into explicit display subtypes when wording is clear.
- Call success expectations map to assert_call_established consistently.
- No unrelated action_intent or precondition_intent fields changed.
