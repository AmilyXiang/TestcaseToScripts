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

## Supported Actions (VoIP Phone Test)

### Basic Call Control
- offhook                         // Go off-hook (get dial tone)
- onhook                          // Go on-hook (end call)
- dial                            // Dial a number
- answer                          // Answer an incoming call
- reject                          // Reject an incoming call
- redial                          // Redial last number
- speed_dial                      // Speed dial (predefined number)

### Call Supplementary Services
- hold                            // Place a call on hold
- resume                          // Resume a held call
- transfer_attended               // Attended transfer (consult then transfer)
- transfer_blind                  // Blind transfer (direct transfer)
- conference_start                // Start a conference call
- conference_join                 // Join a conference
- conference_split                // Split a conference
- park_call                       // Park a call
- retrieve_parked                 // Retrieve a parked call
- call_pickup                     // Pick up a call ringing elsewhere
- call_waiting                    // Call waiting (accept second call)
- call_forward_unconditional      // Set unconditional call forward
- call_forward_busy               // Set call forward on busy
- call_forward_noanswer           // Set call forward on no answer
- do_not_disturb_enable           // Enable Do Not Disturb
- do_not_disturb_disable          // Disable Do Not Disturb

### Advanced Call Features
- mute                            // Mute microphone
- unmute                          // Unmute microphone
- switch_call                     // Switch between active calls
- auto_answer                     // Enable/disable auto-answer
- call_completion                 // Call completion (callback on busy/no answer)
- call_intrusion                  // Intrude into a call
- executive_override              // Executive override (barge in)
- malicious_call_trace            // Trace a malicious call
- anonymous_call                  // Make an anonymous call
- call_recording_start            // Start call recording
- call_recording_stop             // Stop call recording

### Status & Control
- check_call_state                // Check current call state
- check_voicemail                 // Check voicemail
- message_waiting_indication      // Message waiting indicator (MWI)
- set_dnd                         // Set Do Not Disturb
- set_forward                     // Set call forwarding
- register                        // Register with SIP server
- deregister                      // Deregister from SIP server
- reboot                          // Reboot the phone

### Configuration & Maintenance
- configure_network               // Configure network settings
- configure_sip_account           // Configure SIP account
- set_date_time                   // Set date and time
- set_language                    // Set display language
- set_ringtone                    // Set ringtone
- adjust_volume                   // Adjust volume (handset/speaker/ringer)
- reset_to_factory                // Factory reset
- firmware_upgrade                // Upgrade firmware

### Service Codes & DTMF
- send_dtmf                       // Send DTMF tones
- test_call                       // Make a test call (e.g., #123)
- echo_test                       // Echo test (e.g., #124)
- dtmf_test                       // DTMF test (e.g., #125)
- queue_login                     // Log into a call queue
- queue_logout                    // Log out of a call queue
- agent_join_queue                // Agent joins queue
- agent_leave_queue               // Agent leaves queue
- voicemail_access                // Access voicemail

### Special Scenarios
- interoperability_test           // Interoperability test with other vendors
- load_test                       // Load test (high call rate)
- long_call                       // Long duration call (e.g., 24h)
- abnormal_termination            // Abort call (reboot/power loss)
- concurrent_calls                // Test multiple concurrent calls

### Generic / Low‑Level
- generic_action                  // Fallback for unmapped actions
- key_press                       // Simulate key press
- wait                            // Wait for specified time
- verify_screen                   // Verify screen content
- verify_tone                     // Verify tone (dial/ringback/busy)

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
