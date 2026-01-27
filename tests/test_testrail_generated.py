from __future__ import annotations

import pprint
import pytest

# Auto-generated from TestRail export.
# Update step_mapping.yaml to map natural-language steps into SSH commands.

CASES = [{'title': 'RQPLEIAD_180_01_Create_Emergency_Program_Key',
  'preconditions': 'OXE: \r\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing an empty program key. SOFTK0 is the first programmable '
                            'softkey, which is typically empty by default and used for creating emergency program '
                            'keys.',
             'automation': 'automatable'},
            {'step': 'Press Emergency call',
             'expected': 'Display the create key screen',
             'intent': 'press_key',
             'suggested_commands': ['key ts "Emergency"'],
             'confidence': 0.9,
             'explanation': "The step 'Press Emergency call' likely refers to a softkey or on-screen button labeled "
                            "'Emergency' or 'Emergency call'. Using touch screen is the most direct method.",
             'automation': 'automatable'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly  (the phone and addon side)',
             'intent': 'press_key',
             'suggested_commands': ['key ts "create key"', 'key sim OK'],
             'confidence': 0.9,
             'explanation': "Step instructs to press either a 'create key' button on the screen or the OK key. The "
                            "touch screen command is attempted first as it's more direct. The OK key command is "
                            'provided as a fallback.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_02_Create_Guard_Program_Key',
  'preconditions': 'OXE: \r\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing an empty program key. The primary method is to simulate '
                            'pressing a softkey, with SOFTK0 being a typical default for the first empty programmable '
                            'key.',
             'automation': 'automatable'},
            {'step': 'Press Guard call',
             'expected': 'Display the create key screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': "Assuming 'Guard call' is assigned to the first programmable softkey (SOFTK0) based on "
                            'typical phone configuration patterns.',
             'automation': 'automatable'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly (phone and addon side)',
             'intent': 'press_key',
             'suggested_commands': ['key ts "create"', 'key sim OK'],
             'confidence': 0.9,
             'explanation': "Step instructs to press either the on-screen 'create' button or the physical OK key. "
                            'Providing both commands covers both possibilities efficiently.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_03_Create_Operator_Program_Key',
  'preconditions': 'OXE: \r\nmgr---SIP device management---DM profile---Operator number---xxxx',
  'steps': [{'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press an empty program key. The primary method for a programmable '
                            'key is the SOFTK0 key, which corresponds to the first empty program key on the phone.',
             'automation': 'automatable'},
            {'step': 'Press Operator call',
             'expected': 'Display the create key screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': "Assuming 'Operator call' is the label for the first programmable softkey (SOFTK0).",
             'automation': 'automatable'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly (phone and addon side)',
             'intent': 'press_key',
             'suggested_commands': ['key ts "create key"', 'key sim OK'],
             'confidence': 0.9,
             'explanation': "Two alternative methods to press the create key: touch screen click for 'create key' text "
                            'or pressing the OK key on the phone.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_04_Emergency_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Emergency program key',
  'steps': [{'step': 'Press the Emergency program key of the phone or addon',
             'expected': 'title:  Outgoing call\n'
                         'Red background  \n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press the Emergency program key. The primary method is to simulate '
                            "a softkey press. The exact softkey number (e.g., SOFTK0) is assumed as the 'Emergency "
                            "program key' is typically mapped to a programmable softkey.",
             'tags': ['emergency', 'program_key', 'outgoing_call'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title:  Conversation xx:xx\n'
                         'Red background  \n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep 'Conversation'",
                                    "screen_dump | grep 'emergency avatar'",
                                    "screen_dump | grep 'new call button'"],
             'confidence': 0.8,
             'explanation': 'The step describes a remote action (answer) and expects a specific screen state. '
                            'Automation requires verifying the display shows the expected title, avatar, and button. '
                            'The remote answer itself cannot be automated via phone SSH commands, but the resulting '
                            'screen can be verified.',
             'tags': ['emergency', 'call_answered', 'screen_verification'],
             'automation': 'needs_context'},
            {'step': 'Press the emergency avatar',
             'expected': 'Display the emergency info',
             'intent': 'touch_screen',
             'suggested_commands': ['key ts "emergency avatar"'],
             'confidence': 0.85,
             'explanation': "The step instructs to press the 'emergency avatar' on the screen. This is best performed "
                            'using a touch screen click command with a regex matching the displayed text.',
             'tags': ['emergency', 'avatar', 'touch_screen'],
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'touch_screen',
             'suggested_commands': ['key ts "new call button"'],
             'confidence': 0.85,
             'explanation': "The step instructs to press the 'new call button' on the screen. This is best performed "
                            'using a touch screen click command with a regex matching the displayed text.',
             'tags': ['emergency', 'new_call', 'touch_screen'],
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'press_key',
             'suggested_commands': ['key ts "hold"', 'key sim BIS'],
             'confidence': 0.7,
             'explanation': 'The step instructs to press the hold key, either on-screen or the physical button. The '
                            "BIS key is commonly the physical 'Hold' button. The on-screen button can be clicked via "
                            "touch. The expected result is 'no action', so the command is issued but the verification "
                            'of no state change would be a separate step.',
             'tags': ['emergency', 'hold', 'negative_test'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handset'],
             'confidence': 1.0,
             'explanation': "The step 'pick up the handset' means to switch the audio mode to handset, which is "
                            'directly executable via the voicemode command.',
             'tags': ['audio', 'handset', 'precondition'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handsfree'],
             'confidence': 1.0,
             'explanation': "The step 'Hang on the handset' (meaning hang up or switch to handsfree) is interpreted as "
                            'setting the voice mode to handsfree, which is directly executable.',
             'tags': ['audio', 'handsfree', 'hangup'],
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'press_key',
             'suggested_commands': ['key sim RELEASE'],
             'confidence': 0.9,
             'explanation': "The step 'press the release key of the screen or the release physical button' maps to the "
                            "RELEASE key simulation. It's a direct key press action.",
             'tags': ['key_press', 'release', 'emergency_call'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing arrow)\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Emergency|outgoing'"],
             'confidence': 0.8,
             'explanation': "The step 'check the call log' requires verifying the display for emergency call log "
                            'details. The screen_dump command with grep can check for relevant text, but specific log '
                            'navigation may need additional context.',
             'tags': ['verification', 'call_log', 'emergency'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_05_Emergency_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Press the Emergency call log/ Emergency contact or dial the Emergency number',
             'expected': 'title: Outgoing call\n'
                         'Red background\n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'call_control',
             'suggested_commands': ['key sim 1; key sim 2; key sim 3; key sim 4; key sim DIAL',
                                    "screen_dump | grep -E 'Outgoing call|Emergency'"],
             'confidence': 0.8,
             'explanation': 'Step requires initiating an emergency call via dialing. Using a placeholder emergency '
                            "number '1234' as per preconditions. Then verifying the outgoing call screen.",
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Conversation|Emergency'",
                                    "screen_dump raw | grep -E 'Red background|release.*grey|hold.*grey'"],
             'confidence': 0.8,
             'explanation': 'The step requires verifying the call screen after the remote side answers. The expected '
                            "result includes specific text and UI states. The commands check for the 'Conversation' "
                            "title and 'Emergency' indicator, and the raw dump is used to check for background color "
                            'and button states which may not be in standard text output.',
             'automation': 'automatable'},
            {'step': 'Press the emergency avatar',
             'expected': 'Display the emergency info',
             'intent': 'touch_screen_click',
             'suggested_commands': ['key ts "emergency"'],
             'confidence': 0.8,
             'explanation': 'The step asks to press an emergency avatar, which is likely a touch screen element. Using '
                            "regex 'emergency' (case-insensitive) to click the emergency avatar/icon.",
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim DIAL'],
             'confidence': 0.9,
             'explanation': "The 'new call button' typically corresponds to the DIAL key on VoIP phones, which "
                            'initiates a new call/dialing screen.',
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'press_key',
             'suggested_commands': ['key ts "Hold"', 'key sim HOLD'],
             'confidence': 0.9,
             'explanation': 'Attempting to press Hold button via touch screen first, then physical key as fallback. '
                            'The HOLD key is a standard key on Alcatel-Lucent phones.',
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handset'],
             'confidence': 1.0,
             'explanation': 'Command directly sets voice mode to handset, simulating picking up the handset.',
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'call_control',
             'suggested_commands': ['call drop', 'voicemode set idle'],
             'confidence': 0.9,
             'explanation': 'Hanging up the handset requires dropping the call and setting voice mode to idle',
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'call_control',
             'suggested_commands': ['key sim RELEASE'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press the release key, which maps directly to the RELEASE key '
                            'simulation command.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing)\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call log"',
                                    'screen_dump | grep -E "(Emergency|emergency|EMERGENCY)"',
                                    'screen_dump | grep -E "(label|avatar|name|number|date)"'],
             'confidence': 0.8,
             'explanation': 'Navigate to call log from home screen using touch screen, then verify emergency call log '
                            'details are displayed correctly.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_06_Emergency_Outgoing_Call_By_Dial_Hardcode_911/112',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Dial the 911 or 112',
             'expected': 'title: Outgoing call\n'
                         'Red background\n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'call_control',
             'suggested_commands': ['key sim 9; key sim 1; key sim 1; key sim DIAL',
                                    "screen_dump | grep -E 'Outgoing call|Emergency'"],
             'confidence': 0.9,
             'explanation': "Dial 911 using key simulation and verify the call screen shows 'Outgoing call' or "
                            "'Emergency'.",
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 0.9,
             'explanation': 'Answer the incoming emergency call from remote side',
             'automation': 'automatable'},
            {'step': 'Press the emergency avatar',
             'expected': 'Display the  info: 911 or 112',
             'intent': 'press_key',
             'suggested_commands': ['key ts "911"', 'key ts "112"'],
             'confidence': 0.9,
             'explanation': "The emergency avatar likely displays '911' or '112' on screen. Using touch screen to "
                            'click the displayed emergency number is more direct than navigation keys.',
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim DIAL'],
             'confidence': 0.9,
             'explanation': "The 'new call button' is the DIAL key, which initiates a new call or brings up the dial "
                            'screen.',
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'press_key',
             'suggested_commands': ['key ts "Hold"', 'key sim HOLD'],
             'confidence': 0.8,
             'explanation': 'The step instructs to press the hold key, which could be a softkey on the screen or a '
                            "physical button. The first command attempts a touch screen click on 'Hold'. The second "
                            'command simulates a physical HOLD key press, assuming it exists as a standard key. If '
                            "'HOLD' is not a valid key, the test may need to use a different key name or rely on the "
                            'touch screen.',
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handset'],
             'confidence': 1.0,
             'explanation': 'Picking up the handset requires switching voice mode to handset',
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'call_control',
             'suggested_commands': ['voicemode set idle'],
             'confidence': 0.9,
             'explanation': "The step 'Hang on the handset' means to end the call and place the handset back on-hook, "
                            'which is equivalent to setting the voice mode to idle.',
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'press_key',
             'suggested_commands': ['key sim RELEASE'],
             'confidence': 0.9,
             'explanation': 'Press the release key as specified in the step. This simulates pressing the physical '
                            'release button.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing )\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Call Log"',
                                    'screen_dump | grep -E "911|112|Emergency"',
                                    'screen_dump | grep -E "Label|Avatar|Name|Number|Date"'],
             'confidence': 0.9,
             'explanation': 'Navigate to call log menu and verify emergency call entry with correct fields',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_07_Emergency_Outgoing_Call_With_Second_Normal_Incoming_Call_Answer',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx'],
             'confidence': 0.9,
             'explanation': "The step requires establishing a call to the emergency number 'xxxx' configured in the "
                            "preconditions. The 'call set' command is the direct method to initiate a call via SSH.",
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the emergency call is  kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar  + Incoming call"+ switch button"',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Incoming call|switch'",
                                    "screen_dump raw | grep -E 'white background|normal avatar'"],
             'confidence': 0.8,
             'explanation': 'Verify the screen shows the new incoming call with the described elements (white '
                            "background, normal avatar, 'Incoming call' text, switch button) while the emergency call "
                            'remains active.',
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         'the emergency call is kept active\n'
                         'emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button',
             'intent': 'press_key',
             'suggested_commands': ['key sim CONF0'],
             'confidence': 0.9,
             'explanation': "The 'switch button' in a multi-call context typically corresponds to the conference/swap "
                            'key (CONF0).',
             'automation': 'automatable'},
            {'step': 'Answer the new call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and normal call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 0.9,
             'explanation': "The step requires answering an incoming call while another call is active. The 'call "
                            "answer' command is the direct SSH command to answer an incoming call on Alcatel-Lucent "
                            'VoIP phones.',
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'press_key',
             'suggested_commands': ['key sim EXIT'],
             'confidence': 0.9,
             'explanation': "The step asks to press exit/release button. 'EXIT' is the correct key for exit function, "
                            "and 'RELEASE' is for call release/hangup. Since the test context involves emergency "
                            'outgoing call with incoming call, pressing EXIT is appropriate for navigating away from '
                            'current screen without hanging up.',
             'automation': 'automatable'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Emergency call log and the normal incoming call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call Log"',
                                    "screen_dump | grep -E 'Conference|Emergency'"],
             'confidence': 0.8,
             'explanation': 'Navigate to call log via home and touch screen, then verify presence of conference and '
                            'emergency call entries.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_08_Emergency_Outgoing_Call_With_Second_Normal_Incoming_Call_Reject',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx'],
             'confidence': 0.9,
             'explanation': 'The step requires establishing a call to the emergency number configured in the DM '
                            "profile. The 'call set' command is the direct method to initiate an outgoing call via "
                            'SSH.',
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the emergency call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Incoming call|switch'",
                                    "screen_dump raw | grep -A2 -B2 'Incoming'"],
             'confidence': 0.8,
             'explanation': 'Verifying that incoming call UI appears with expected elements while emergency call '
                            'remains active',
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the emergency call is kept active\n'
                         'emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button',
             'intent': 'press_key',
             'suggested_commands': ['key sim CONF0'],
             'confidence': 0.9,
             'explanation': "The 'switch button' in a multi-call context (emergency + incoming) typically corresponds "
                            'to the conference/swap key, which is CONF0 on Alcatel-Lucent phones.',
             'automation': 'automatable'},
            {'step': 'Press the silence button',
             'expected': 'Stop ringing',
             'intent': 'call_control',
             'suggested_commands': ['key sim MUTE'],
             'confidence': 0.9,
             'explanation': "The 'silence button' typically refers to the MUTE key which stops ringing during an "
                            'incoming call',
             'automation': 'automatable'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['key ts "Reject"', 'key ts "Voicemail"'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing a button to reject an incoming call or send it to voicemail. '
                            "The exact label may vary (e.g., 'Reject', 'Decline', 'Send to Voicemail'). Using touch "
                            'screen commands to click the most likely on-screen buttons is the most direct method.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the not answered call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim MENU',
                                    "key ts 'Call Log'",
                                    "screen_dump | grep -E '(Emergency|Not Answered|Missed)'",
                                    "screen_dump | grep -E '(Label|Avatar|Name|Number|Date)'"],
             'confidence': 0.8,
             'explanation': 'Navigate to the call log menu via the main menu and touch screen, then verify the '
                            'presence and correct display of the emergency and missed call logs.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_09_Emergency_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['key sim 1; key sim 2; key sim 3; key sim DIAL',
                                    "screen_dump | grep -E 'Conversation|Emergency'"],
             'confidence': 0.7,
             'explanation': 'Step requires establishing an emergency call. Using a generic emergency number (123) and '
                            "dialing. Then verifying the call screen with 'Conversation' or 'Emergency' text.",
             'automation': 'automatable'},
            {'step': 'Phone makes the new normal outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the emergency call is on hold\n'
                         'The emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect",
             'intent': 'call_control',
             'suggested_commands': ['call set 1234567890',
                                    "screen_dump | grep -E 'Outgoing call|white background|normal avatar|release "
                                    "button'",
                                    "screen_dump | grep -E 'Red background|emergency avatar|switch button'",
                                    "screen_dump softkey | grep 'transfer'"],
             'confidence': 0.8,
             'explanation': 'Step requires making a new normal outgoing call while an emergency call is active. The '
                            "'call set' command initiates the call. The screen verification commands check for the "
                            'expected UI elements for both calls as described in the expected result.',
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and normal call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Conference|Emergency'",
                                    "screen_dump softkey | grep -E 'EXIT|RELEASE'"],
             'confidence': 0.8,
             'explanation': 'Step is to verify UI state after remote side answers. Need to check for conference label, '
                            'emergency indication, and softkey/button states (grey/off).',
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'No anction',
             'intent': 'press_key',
             'suggested_commands': ['key sim EXIT'],
             'confidence': 1.0,
             'explanation': 'The step is to press the exit/release button, which directly maps to the EXIT key '
                            'simulation command.',
             'automation': 'automatable'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Emergency call loh and the normal outgoing call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call Log"',
                                    "screen_dump | grep -E 'Conference|Emergency'"],
             'confidence': 0.8,
             'explanation': 'Navigate to call log from home screen and verify presence of conference and emergency '
                            'call entries.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_10_Emergency_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx',
                                    "screen_dump | grep -E 'Conversation|Red background|emergency avatar|new call "
                                    "button'"],
             'confidence': 0.8,
             'explanation': "The step requires establishing an emergency call. The 'call set' command initiates the "
                            "call to the emergency number 'xxxx' as defined in the preconditions. A screen dump is "
                            'then used to verify the expected display elements (title, red background, emergency '
                            'avatar, new call button).',
             'automation': 'automatable'},
            {'step': 'Phone makes the new normal outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the emergency call is on hold\n'
                         'The emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect",
             'intent': 'call_control',
             'suggested_commands': ['call set 1234567890'],
             'confidence': 0.7,
             'explanation': "Step requires making a new normal outgoing call. The 'call set' command initiates a call, "
                            'but the specific number is not provided in the step. Using a placeholder number.',
             'automation': 'automatable'},
            {'step': 'Remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Conversation [0-9]{2}:[0-9]{2}'",
                                    "screen_dump | grep -E 'emergency|Emergency'",
                                    "screen_dump | grep -E 'new call|New Call'",
                                    "screen_dump | grep -E 'release|Release|hold|Hold'"],
             'confidence': 0.7,
             'explanation': 'The step describes a remote side rejection scenario. The expected result is a specific '
                            'screen state (Conversation timer, red background, emergency avatar, new call button with '
                            'LED on, and greyed release/hold buttons). The verification requires checking the screen '
                            "dump for these elements. The 'red background' and LED states may not be directly "
                            'verifiable via SSH text dump, but the presence of key text labels can be confirmed.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the unsuccessful call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Call Log"',
                                    "screen_dump | grep -E 'Emergency|Unsuccessful'",
                                    "screen_dump | grep -E 'label|avatar|name|number|date'"],
             'confidence': 0.8,
             'explanation': 'Navigate to call log menu and verify emergency and unsuccessful call logs with correct '
                            'labels.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_11_Guard_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Guard program key',
  'steps': [{'step': 'Press the Guard program key of the phone or addon',
             'expected': 'title: Outgoing call\n'
                         'Dark blue background\n'
                         'display Guard avatar and release button(led is on)\n'
                         'and press the Guard avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press the Guard program key. On Alcatel-Lucent VoIP phones, program '
                            'keys are typically mapped to SOFTK0-SOFTK9. Assuming Guard is the first program key, '
                            'SOFTK0 is used.',
             'tags': ['program_key', 'guard', 'outgoing_call'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 0.7,
             'explanation': 'The step describes the remote side answering the call. To simulate this in automation, we '
                            'can answer the call on the phone under test, assuming it is the receiving end. However, '
                            "context is needed to confirm which device is remote. The command 'call answer' is used to "
                            'answer an incoming call on the phone.',
             'tags': ['call_answer', 'remote_side'],
             'automation': 'needs_context'},
            {'step': 'Press the guard avatar',
             'expected': 'Display the guard info',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.8,
             'explanation': "Assuming 'guard avatar' is mapped to a programmable softkey (SOFTK0). If not, touch "
                            'screen click might be needed but requires screen context.',
             'tags': ['guard', 'program_key', 'softkey'],
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim DIAL'],
             'confidence': 0.9,
             'explanation': "'new call button' typically corresponds to the DIAL key on the phone keypad.",
             'tags': ['dial', 'new_call'],
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'press_key',
             'suggested_commands': ['key ts "Hold"', 'key sim HOLD'],
             'confidence': 0.8,
             'explanation': "The step asks to press the hold key, which could be a touchscreen element labeled 'Hold' "
                            'or a physical HOLD button. The command set includes a touchscreen click for a softkey and '
                            "a key simulation for a physical button. The exact key name 'HOLD' is assumed based on "
                            'common phone layouts.',
             'tags': ['hold', 'guard', 'program_key', 'call_control'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handset'],
             'confidence': 1.0,
             'explanation': "Picking up the handset directly corresponds to switching the voice mode to 'handset' "
                            'using the voicemode command.',
             'tags': ['handset', 'guard', 'audio', 'mode_switch'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handset'],
             'confidence': 0.9,
             'explanation': "The step 'Hang on the handset' means to place the handset on-hook, which sets the voice "
                            'mode to handset (idle). The expected result about switching to handsfree is likely a '
                            'subsequent verification step not covered by this command.',
             'tags': ['handset', 'hook', 'voicemode'],
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'press_key',
             'suggested_commands': ['key sim RELEASE'],
             'confidence': 0.8,
             'explanation': 'The step instructs to press the release key, which corresponds to the RELEASE key '
                            "simulation. The expected result 'no action' is a verification that needs to be checked "
                            'separately after the key press.',
             'tags': ['release', 'call_control'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log (outgoing)\nthe label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME', 'key ts "Call Log"', 'screen_dump | grep -i "Guard"'],
             'confidence': 0.8,
             'explanation': 'Navigate to call log and verify Guard call log entries are present with correct details',
             'tags': ['call_log', 'guard', 'verification'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_12_Guard_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Press the Guard call log/ Guard  contact or dial the Guard  number',
             'expected': 'title: Outgoing call\n'
                         'Dark blue background\n'
                         'display Guard avatar and release button(led is on)\n'
                         'and press the Guard avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'call_control',
             'suggested_commands': ["screen_dump | grep -E 'Guard|Call log|Contact'",
                                    "key ts 'Guard'",
                                    "key ts 'Call log' 2",
                                    'call set xxxx',
                                    "screen_dump | grep -E 'Outgoing call|Dark blue|Guard avatar|release button'"],
             'confidence': 0.7,
             'explanation': 'Step requires initiating a Guard call via log/contact or dialing. First verify screen for '
                            "Guard options, then attempt to click 'Guard' or 'Call log'. If not found, dial the number "
                            'directly. Finally verify outgoing call screen with expected elements.',
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 0.9,
             'explanation': "The step instructs the remote side to answer the call. The 'call answer' SSH command "
                            'simulates answering an incoming call on the phone.',
             'automation': 'automatable'},
            {'step': 'Press the guard avatar',
             'expected': 'Display the guard info',
             'intent': 'press_key',
             'suggested_commands': ['key ts "guard"'],
             'confidence': 0.8,
             'explanation': "The step 'Press the guard avatar' suggests a touch screen interaction with an on-screen "
                            "element labeled 'guard' or containing that text. Using 'key ts' with a regex is the most "
                            'direct method.',
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim DIAL'],
             'confidence': 0.9,
             'explanation': "The 'new call button' typically corresponds to the DIAL key on VoIP phones, which "
                            'initiates a new call/dialing screen.',
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'press_key',
             'suggested_commands': ['key ts "Hold"', 'key sim HOLD'],
             'confidence': 0.9,
             'explanation': 'Attempting to press Hold via touch screen first (most direct), then physical HOLD key '
                            'simulation as fallback. Note: HOLD key may not be standard - using best guess based on '
                            'typical phone layouts.',
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handset'],
             'confidence': 1.0,
             'explanation': 'Command directly switches voice mode to handset as required',
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'call_control',
             'suggested_commands': ['call drop'],
             'confidence': 0.9,
             'explanation': "The step 'Hang on the handset' means to end the call, which is performed by the 'call "
                            "drop' command.",
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'press_key',
             'suggested_commands': ['key sim RELEASE'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press the release key, which maps directly to the RELEASE key '
                            'simulation command.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log (outgoing)\nthe label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME', 'key ts "Call log"', "screen_dump | grep -E 'Guard|xxxx'"],
             'confidence': 0.8,
             'explanation': 'Navigate to home, open call log, and verify the guard call log entry is present with '
                            'correct details.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_13_Guard_Ougoing_Call_With_Second_Normal_Incoming_Call_Answer',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx'],
             'confidence': 0.9,
             'explanation': 'Establishing a call with the Guard number configured in DM profile',
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Guard call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Incoming call|switch'",
                                    "screen_dump raw | grep -E 'white.*background|normal.*avatar'"],
             'confidence': 0.8,
             'explanation': 'Step verifies screen shows new incoming call while guard call is active. Commands check '
                            "for 'Incoming call' text and visual cues like white background/avatar.",
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Guard call is kept active\n'
                         'Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button',
             'intent': 'press_key',
             'suggested_commands': ['key sim CONF0'],
             'confidence': 0.9,
             'explanation': "The 'switch button' during a guard call with incoming call typically corresponds to the "
                            'conference/transfer key (CONF0) which handles call switching functionality.',
             'automation': 'automatable'},
            {'step': 'Answer the new call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and normal call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 0.95,
             'explanation': "The step requires answering an incoming call while another call is active. The 'call "
                            "answer' command directly answers incoming calls on SIP phones.",
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'press_key',
             'suggested_commands': ['key sim EXIT'],
             'confidence': 0.9,
             'explanation': 'The step explicitly requests pressing the exit/release button, which maps directly to the '
                            'EXIT key simulation command.',
             'automation': 'automatable'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Guard call log and the normal incoming call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call Log" || key ts "History"',
                                    "screen_dump | grep -E '(Conference|Guard|Incoming)'"],
             'confidence': 0.7,
             'explanation': 'Navigate to call log from home screen using touch, then verify logs for conference, '
                            'guard, and normal incoming calls.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_14_Guard_Ougoing_Call_With_Second_Normal_Incoming_Call_Reject',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx'],
             'confidence': 0.9,
             'explanation': "The step requires establishing a call with the Guard number. The 'call set' command is "
                            'the direct method to initiate an outgoing call via SSH.',
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Guard call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Incoming call|switch'",
                                    "screen_dump softkey | grep -E 'Answer|Reject'"],
             'confidence': 0.8,
             'explanation': 'Verify the screen shows the new incoming call with the expected elements (white '
                            "background, avatar, 'Incoming call' text, switch button) while the guard call remains "
                            'active.',
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Guard call is kept active\n'
                         'Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button',
             'intent': 'press_key',
             'suggested_commands': ['key sim CONF0'],
             'confidence': 0.9,
             'explanation': "The 'switch button' in a multi-call context typically corresponds to the conference/swap "
                            'key (CONF0).',
             'automation': 'automatable'},
            {'step': 'Press the silence button',
             'expected': 'Stop ringing',
             'intent': 'call_control',
             'suggested_commands': ['key sim MUTE'],
             'confidence': 0.9,
             'explanation': "The 'silence button' typically refers to the MUTE key which stops ringing during an "
                            'incoming call',
             'automation': 'automatable'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['key ts "Reject"', 'key ts "Voicemail"'],
             'confidence': 0.8,
             'explanation': "The step requires pressing either 'reject' or 'turn to voicemail' button during an "
                            'incoming call scenario. Using touch screen commands to click these buttons is the most '
                            'direct method.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the not answered call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call Log"',
                                    "screen_dump | grep -E 'Guard|xxxx'",
                                    "screen_dump | grep -E 'label|avatar|name|number|date'"],
             'confidence': 0.8,
             'explanation': 'Navigate to call log via home and touch screen, then verify guard call and unanswered '
                            'call logs with correct details.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_15_Guard_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx'],
             'confidence': 0.9,
             'explanation': "The step requires establishing a call with the Guard number. The 'call set' command is "
                            'the direct method to initiate an outgoing call via SSH.',
             'automation': 'automatable'},
            {'step': 'Phone makes the new normal outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the Guard call is on hold\n'
                         'The Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect",
             'intent': 'call_control',
             'suggested_commands': ['call set 1234567890',
                                    "screen_dump | grep -E 'Outgoing call|white background|normal avatar|release "
                                    "button'"],
             'confidence': 0.8,
             'explanation': "Step requires making a new outgoing call. Using 'call set' with a placeholder number. "
                            'Then verifying the screen shows the expected elements for the new call.',
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and normal call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 1.0,
             'explanation': "The step instructs to answer an incoming call from the remote side. The 'call answer' SSH "
                            'command directly simulates answering the call on the phone.',
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'press_key',
             'suggested_commands': ['key sim EXIT'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing the exit/release button, which maps directly to the EXIT key '
                            'simulation command.',
             'automation': 'automatable'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Guard call log and the normal outgoing call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Call Log"',
                                    'screen_dump | grep -E "(Conference|Guard|Outgoing)"'],
             'confidence': 0.8,
             'explanation': 'Navigate to call log menu and verify presence of conference, guard, and normal outgoing '
                            'call entries with correct labels.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_16_Guard_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx', "screen_dump | grep -E 'Conversation|Guard'"],
             'confidence': 0.9,
             'explanation': 'Establish call with Guard number and verify call screen',
             'automation': 'automatable'},
            {'step': 'Phone makes the new normal outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the Guard call is on hold\n'
                         'The Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect",
             'intent': 'call_control',
             'suggested_commands': ['call set 1234567890'],
             'confidence': 0.8,
             'explanation': "Step requires initiating a new outgoing call. Using 'call set' with a placeholder number "
                            'is the standard SSH command to make a call. The specific number is not provided in the '
                            'step, so a placeholder is used.',
             'automation': 'automatable'},
            {'step': 'Remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Conversation|Guard'",
                                    "screen_dump raw | grep -E 'Dark blue|grey'"],
             'confidence': 0.7,
             'explanation': 'Verifying display shows conversation screen with Guard avatar and correct button states '
                            'after remote rejection',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the unsuccessful call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call log" || key ts "Call History" || key ts "History"',
                                    "screen_dump | grep -E '(Guard|unsuccessful|Failed|Missed)'",
                                    "screen_dump | grep -E '(label|avatar|name|number|date)'"],
             'confidence': 0.8,
             'explanation': 'Navigate to call log and verify both Guard call and unsuccessful call entries with '
                            'correct display fields',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_17_Operator_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Operator program key',
  'steps': [{'step': 'Press the Operator program key of the phone or addon',
             'expected': 'title: Outgoing call\n'
                         'white background\n'
                         'display Operator avatar and release button(led is on)\n'
                         'and press the Operator avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.8,
             'explanation': "The step instructs to press the Operator program key. The 'SOFTK0' key is the typical "
                            'default mapping for the first programmable softkey, which is commonly used for operator '
                            "functions. However, the exact softkey number (SOFTK0-9) may vary depending on the phone's "
                            'configuration. The command simulates a short press.',
             'tags': ['program_key', 'operator', 'outgoing_call'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 0.9,
             'explanation': "The step 'Remote side answer the call' implies the remote party (another phone) should "
                            'answer an incoming call. Since we are controlling the test phone via SSH, we simulate the '
                            "remote side answering by using the 'call answer' command on the test phone, assuming it "
                            'is in a ringing state from an outgoing call initiated via the Operator program key.',
             'tags': ['call', 'answer', 'operator', 'program_key'],
             'automation': 'automatable'},
            {'step': 'Press the Operator avatar',
             'expected': 'Display the Operator info',
             'intent': 'press_key',
             'suggested_commands': ['key ts "Operator"'],
             'confidence': 0.9,
             'explanation': "The step 'Press the Operator avatar' suggests clicking a touchscreen element labeled "
                            "'Operator' (likely an avatar/icon). Using touchscreen click is appropriate for UI "
                            'elements.',
             'tags': ['operator', 'program_key', 'touchscreen', 'ui_interaction'],
             'automation': 'automatable'},
            {'step': 'Press the hold key of the screen or the hold physical key',
             'expected': 'will hold the call\n'
                         'title: On hold xx:xx\n'
                         'Blue background\n'
                         'display Operator avatar / hold / new call/ release button\n'
                         'the led of the hold is breath',
             'intent': 'press_key',
             'suggested_commands': ['key sim HOLD'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press the hold key, which is a standard key on the phone. The '
                            "command 'key sim HOLD' simulates pressing the hold key.",
             'tags': ['hold', 'call_control', 'program_key'],
             'automation': 'automatable'},
            {'step': 'Press the hold key of the screen or the hold physical key again',
             'expected': 'will retrieve the call\n'
                         'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['key ts "Hold"', 'key sim HOLD'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing the hold key to retrieve a call. Both touch screen and '
                            "physical key options are provided since the step mentions 'screen or physical key'.",
             'tags': ['hold', 'call_retrieval', 'operator_key'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handset'],
             'confidence': 1.0,
             'explanation': "The step 'pick up the handset' corresponds to switching the voice mode to handset using "
                            'the SSH command.',
             'tags': ['handset', 'audio', 'precondition'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset or \npress the release key of the screen or the release physical button',
             'expected': 'will release the call',
             'intent': 'call_control',
             'suggested_commands': ['key sim RELEASE'],
             'confidence': 0.9,
             'explanation': "The step instructs to hang up the call by pressing the release key. The 'key sim RELEASE' "
                            'command simulates pressing the release key, which is the primary method to end a call.',
             'tags': ['hang_up', 'release_key', 'call_termination'],
             'automation': 'automatable'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log (outgoing)\nthe label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Call Log"',
                                    "screen_dump | grep -E 'Operator|\\+?[0-9]+'",
                                    "screen_dump | grep -E 'Label|Avatar|Name|Number|Date'"],
             'confidence': 0.8,
             'explanation': 'The step requires checking the call log for an Operator outgoing call entry and verifying '
                            'that label, avatar, name, number, and date display correctly. This involves navigating to '
                            'the call log menu (typically via MENU -> Call Log) and then using screen_dump to verify '
                            'the displayed information. The exact navigation path may vary by phone model or menu '
                            "structure, but 'Call Log' is a common menu item. The grep commands check for the Operator "
                            'entry and the required fields.',
             'tags': ['call_log', 'verification', 'operator', 'program_key'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_18_Operator_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Press the Operator call log/ Operator contact or dial the Operator number',
             'expected': 'title: Outgoing call\n'
                         'white background\n'
                         'display Operator avatar and release button(led is on)\n'
                         'and press the Operator avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx',
                                    "screen_dump | grep -E 'Outgoing call|Operator'",
                                    "screen_dump | grep 'release'"],
             'confidence': 0.8,
             'explanation': 'Step instructs to initiate an outgoing call to the Operator via dialing, call log, or '
                            "contact. The most direct and automatable action is to dial the Operator number 'xxxx' "
                            "using the call set command. Screen verification can check for the 'Outgoing call' title "
                            'and release button.',
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 1.0,
             'explanation': "The step instructs the remote side to answer the call. The 'call answer' SSH command "
                            'simulates answering an incoming call on the phone.',
             'automation': 'automatable'},
            {'step': 'Press the Operator avatar',
             'expected': 'Display the Operator  info',
             'intent': 'press_key',
             'suggested_commands': ['key ts "Operator"'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing the Operator avatar, which is likely a touchscreen element '
                            "labeled 'Operator'. Using touch screen click is the most direct method.",
             'automation': 'automatable'},
            {'step': 'Press the hold key of the screen or the hold physical key',
             'expected': 'will hold the call\n'
                         'title: On hold xx:xx\n'
                         'Blue background\n'
                         'display Operator avatar / hold / new call/ release button\n'
                         'the led of the hold is breath',
             'intent': 'press_key',
             'suggested_commands': ['key ts "Hold"', 'key sim HOLD'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing the hold key. The touch screen command \'key ts "Hold"\' is '
                            "the primary method to press an on-screen hold button. The physical key command 'key sim "
                            "HOLD' is also provided as an alternative, as the step mentions 'hold physical key'.",
             'automation': 'automatable'},
            {'step': 'Press the hold key of the screen or the hold physical key again',
             'expected': 'will retrieve the call\n'
                         'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['key ts "Hold"', "screen_dump | grep 'Conversation'"],
             'confidence': 0.8,
             'explanation': "Step instructs to press the hold key to retrieve a call. The touch screen command 'key ts "
                            '"Hold"\' is the primary method. A screen dump is added to verify the call was retrieved '
                            "and the 'Conversation' title appears as expected.",
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'audio_control',
             'suggested_commands': ['voicemode set handset'],
             'confidence': 1.0,
             'explanation': 'Picking up the handset corresponds to switching voice mode to handset',
             'automation': 'automatable'},
            {'step': 'Hang on the handset or \npress the release key of the screen or the release physical button',
             'expected': 'will release the call',
             'intent': 'call_control',
             'suggested_commands': ['call drop'],
             'confidence': 0.9,
             'explanation': "The step requires hanging up a call, which can be done directly with the 'call drop' "
                            'command instead of simulating physical button presses.',
             'automation': 'automatable'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log (outgoing)\nthe label /avatar /name /number/date display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim MENU', "key ts 'Call log'", "screen_dump | grep -E 'Operator|xxxx'"],
             'confidence': 0.8,
             'explanation': "Navigate to the Call log menu and verify the Operator's outgoing call entry is present "
                            'with correct details.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_19_Operator_Outgoing_Call_With_Second_Normal_Imcoming_Call_Answer',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['key sim DIAL', "screen_dump | grep -E 'Conversation|Operator'"],
             'confidence': 0.8,
             'explanation': 'Assuming operator number is preconfigured and phone is idle, pressing DIAL should call '
                            'operator. Then verify display shows conversation screen with operator info.',
             'automation': 'automatable'},
            {'step': 'Phone receives the incoming call',
             'expected': 'the Operator call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Incoming call|switch'", 'screen_dump softkey'],
             'confidence': 0.8,
             'explanation': 'The step describes a verification of the screen state when a second call arrives. The '
                            'primary action is to check the display for the described elements (white background, '
                            "normal avatar, 'Incoming call' text, and a switch button). The softkey dump can also be "
                            'checked for any relevant call handling options.',
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Operator call is kept active\n'
                         'Operator call in the lower part of the screen:\n'
                         'purple background +Guard avatar +switch button',
             'intent': 'call_control',
             'suggested_commands': ['key sim CONF0'],
             'confidence': 0.9,
             'explanation': "The 'switch button' in a multi-call context typically corresponds to the conference/swap "
                            'key (CONF0).',
             'automation': 'automatable'},
            {'step': 'Answer the new call',
             'expected': 'The new call in the upper part of the screen:\n'
                         'purple background+ normal avatar\n'
                         '\n'
                         'the Operator call will on hold\n'
                         'Operator  call in the lower part of the screen:\n'
                         'Blue background +Operator avatar + switch button\n'
                         '\n'
                         'The middle part: display the conference and transfer button',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 0.9,
             'explanation': "The step 'Answer the new call' directly maps to the SSH command for answering an incoming "
                            'call.',
             'automation': 'automatable'},
            {'step': 'Press the switch button then check the two call screen',
             'expected': 'The Operator  call in the upper part of the screen:\n'
                         'Purple background +Operator  avatar\n'
                         '\n'
                         'the new call will on hold\n'
                         'The new call in the lower part of the screen:\n'
                         'blue background+ normal avatar +switch button\n'
                         '\n'
                         'The middle part: display the conference and transfer button',
             'intent': 'call_control',
             'suggested_commands': ['key ts "switch"', 'screen_dump'],
             'confidence': 0.8,
             'explanation': 'Press the switch button using touch screen and then check the display to verify the two '
                            'call screen layout',
             'automation': 'automatable'},
            {'step': 'Press the conference button',
             'expected': 'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Operator  and normal call avatar\n'
                         'display the exit and release button',
             'intent': 'press_key',
             'suggested_commands': ['key sim CONF0'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing the conference button. The primary method is to simulate the '
                            "CONF0 key press, as it's the standard conference key on Alcatel-Lucent VoIP phones.",
             'automation': 'automatable'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator / normal incoming / conference call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'call_control_and_verification',
             'suggested_commands': ['call drop',
                                    'key sim HOME',
                                    'key ts "Call Log"',
                                    "screen_dump | grep -E 'Operator|conference'"],
             'confidence': 0.8,
             'explanation': 'Hang up the call, navigate to the home screen, open the call log, and verify the presence '
                            'of the expected call log entries.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_20_Operator_Outgoing_Call_With_Second_Normal_Imcoming_Call_Reject',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['key sim DIAL', "screen_dump | grep -E 'Conversation|Operator'"],
             'confidence': 0.7,
             'explanation': 'Step requires establishing a call with the Operator. The precondition mentions an '
                            "'Operator number' configured. The most direct action is to press the DIAL key, which "
                            'should initiate a call to the pre-configured Operator number. A screen dump is then used '
                            "to verify the call is active and shows the expected 'Conversation' title and 'Operator' "
                            'reference.',
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Operator call is kept active\n'
                         '\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Incoming call|switch'",
                                    "screen_dump raw | grep -E 'white background|normal avatar'"],
             'confidence': 0.8,
             'explanation': 'Verifying that the incoming call UI appears with the described elements while the '
                            'operator call remains active.',
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Operator call is kept active\n'
                         'Operator call in the lower part of the screen:\n'
                         'purple background +Guard avatar +switch button',
             'intent': 'press_key',
             'suggested_commands': ['key sim CONF0'],
             'confidence': 0.9,
             'explanation': "The 'switch button' in call handling context typically refers to the conference/transfer "
                            'button (CONF0) used to switch between calls.',
             'automation': 'automatable'},
            {'step': 'Press the silence button',
             'expected': 'Stop ringing',
             'intent': 'press_key',
             'suggested_commands': ['key sim MUTE'],
             'confidence': 0.9,
             'explanation': "The 'silence button' on an Alcatel-Lucent VoIP phone is typically the MUTE key, which is "
                            'used to silence the ringer for an incoming call.',
             'automation': 'automatable'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'press_key',
             'suggested_commands': ['key sim RELEASE'],
             'confidence': 0.9,
             'explanation': "The step 'press the reject button' corresponds to the RELEASE key, which is the standard "
                            'key to reject an incoming call.',
             'automation': 'automatable'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator / normal unanswered call log\nthe label /avatar /number display correctly',
             'intent': 'call_control_and_verification',
             'suggested_commands': ['call drop',
                                    'key sim HOME',
                                    'key ts "Call Log"',
                                    "screen_dump | grep -E 'Operator|xxxx'",
                                    "screen_dump | grep -E 'label|avatar|number'"],
             'confidence': 0.8,
             'explanation': 'Step requires hanging up the active call, navigating to the call log, and verifying the '
                            "presence and correct display of the operator/unanswered call entry. Using 'call drop' to "
                            'release, then navigating via HOME and touch screen to Call Log. Screen verification '
                            'checks for the operator number and correct label/avatar/number display.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_21_Operator_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['key sim DIAL', "screen_dump | grep -E 'Conversation|Operator'"],
             'confidence': 0.7,
             'explanation': 'Step requires establishing a call with the Operator. The precondition suggests the '
                            'Operator number is configured (e.g., as a speed dial or softkey). The most direct action '
                            'is to press the DIAL key, which typically initiates a call to the pre-configured Operator '
                            'number. A screen dump is then used to verify the call screen with the expected title and '
                            'background.',
             'automation': 'automatable'},
            {'step': 'Phone makes the new outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the Operatorcall is on hold\n'
                         'The Operator call in the lower part of the screen:\n'
                         'blue background +Guard avatar +switch button\n'
                         '\n'
                         'and display the transfer button',
             'intent': 'call_control',
             'suggested_commands': ['call set 1234567890'],
             'confidence': 0.7,
             'explanation': "Step requires making a new outgoing call. The 'call set' command initiates a call to a "
                            'specified number. The exact number is not provided in the step, so a placeholder is used.',
             'automation': 'automatable'},
            {'step': 'If press the transfer button',
             'expected': 'exit the two calls\n'
                         'Call log has the Operator call log and normal call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'call_control',
             'suggested_commands': ['key sim CONF0'],
             'confidence': 0.9,
             'explanation': "The 'transfer button' on Alcatel-Lucent VoIP phones is typically the CONF0 key (first "
                            'conference/transfer key). Pressing it during two active calls should initiate a transfer '
                            'action.',
             'automation': 'automatable'},
            {'step': "If don't press the transfer button\nand remote side answer the call",
             'expected': 'The new call in the upper part of the screen:\n'
                         'purple background+ normal avatar \n'
                         '\n'
                         'the Operator  call will on hold\n'
                         'Operator call in the lower part of the screen:\n'
                         'blue background + Operator avatar + switch button\n'
                         '\n'
                         'The middle part: display the conference and transfer button',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'purple background|normal avatar'",
                                    "screen_dump | grep -E 'blue background|Operator avatar|switch button'",
                                    "screen_dump | grep -E 'conference|transfer button'"],
             'confidence': 0.8,
             'explanation': 'Verifying screen display elements as described in expected results: upper call with '
                            'purple background, lower operator call with blue background, and conference/transfer '
                            'buttons in middle.',
             'automation': 'automatable'},
            {'step': 'Press the switch button then check the two call screen',
             'expected': 'The Operator call in the upper part of the screen:\n'
                         'Purple background +Operator avatar\n'
                         '\n'
                         'the new call will on hold\n'
                         'The new call in the lower part of the screen:\n'
                         'blue background+ normal avatar  + switch button\n'
                         '\n'
                         'The middle part: display the conference and transfer button',
             'intent': 'press_key_and_verify_display',
             'suggested_commands': ['key sim CONF0', "screen_dump | grep -E 'Operator|conference|transfer'"],
             'confidence': 0.8,
             'explanation': "The 'switch button' likely refers to the conference key (CONF0) to toggle between calls. "
                            'Then verify the screen shows the described layout with Operator call, held call, and '
                            'conference/transfer buttons.',
             'automation': 'automatable'},
            {'step': 'press the transfer key',
             'expected': 'exit the two calls',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'No valid response from LLM',
             'automation': 'needs_context'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log and the normal outgoing call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Call Log"',
                                    'screen_dump | grep -E "Operator|Call Log"',
                                    'screen_dump | grep -E "[0-9]{3,}"'],
             'confidence': 0.8,
             'explanation': 'Navigate to call log menu and verify both operator and normal outgoing call entries with '
                            'correct labels/numbers',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_22_Operator_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['key sim DIAL', "screen_dump | grep -E 'Conversation|Operator'"],
             'confidence': 0.7,
             'explanation': 'Step requires establishing a call with the Operator. The precondition suggests the '
                            'Operator number is configured. The simplest action is to press the DIAL key, which should '
                            'initiate a call to the pre-configured Operator number. A screen dump is then used to '
                            'verify the call screen.',
             'automation': 'automatable'},
            {'step': 'Phone makes the new outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the Operatorcall is on hold\n'
                         'The Operator call in the lower part of the screen:\n'
                         'blue background +Guard avatar +switch button\n'
                         '\n'
                         'and display the transfer button',
             'intent': 'call_control',
             'suggested_commands': ['call set 1234567890'],
             'confidence': 0.8,
             'explanation': "The step requires making a new outgoing call. The 'call set' command initiates a call to "
                            'a specified number. The exact number is not provided in the step, so a placeholder '
                            '(1234567890) is used. The test precondition mentions an operator number (xxxx), but the '
                            'step is for a new outgoing call, not necessarily to the operator.',
             'automation': 'automatable'},
            {'step': 'remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['call drop'],
             'confidence': 0.9,
             'explanation': 'The remote side rejecting the call means the phone should hang up the outgoing call '
                            "attempt. The 'call drop' command simulates ending/rejecting the call from the phone side.",
             'automation': 'automatable'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator call log and the normal unsuccessful call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'call_control_and_verification',
             'suggested_commands': ['call drop',
                                    'key sim HOME',
                                    'key ts "Call Log"',
                                    "screen_dump | grep -E 'Operator|unsuccessful'",
                                    "screen_dump | grep -E 'label|avatar|number'"],
             'confidence': 0.9,
             'explanation': 'First hang up the call, then navigate to call log via home menu and touch screen. Verify '
                            'both operator and unsuccessful call logs exist, and check label/avatar/number display.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_23_Emergency_Call_With_Guard_Call',
  'preconditions': 'OXE:\r\n'
                   'mgr---SIP device management---DM profile:\r\n'
                   'Emergency  number----xxxx\r\n'
                   'Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         '\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx', "screen_dump | grep -E 'Conversation|Emergency'"],
             'confidence': 0.8,
             'explanation': 'Establish emergency call using configured emergency number and verify display shows '
                            'conversation screen with emergency indicators',
             'automation': 'automatable'},
            {'step': 'Phone makes the new outgoing call to Guard',
             'expected': 'The Guard call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'Dark blue background+ Guard avatar + release button\n'
                         '\n'
                         'the emergency call is on hold\n'
                         'The emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar + switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect",
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Outgoing call|Guard'",
                                    "screen_dump | grep -E 'emergency|Emergency'",
                                    "screen_dump | grep 'transfer'"],
             'confidence': 0.8,
             'explanation': 'Verifying screen shows Guard call as outgoing with emergency call on hold and transfer '
                            'button disabled',
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and Guard call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Conference|Emergency|Guard'",
                                    "screen_dump softkey | grep -E 'EXIT|RELEASE'"],
             'confidence': 0.8,
             'explanation': 'Verify conference call is established with Emergency and Guard avatars, and check softkey '
                            'states for exit/release buttons',
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'press_key',
             'suggested_commands': ['key sim EXIT'],
             'confidence': 0.9,
             'explanation': "The step instructs to press the exit/release button. The 'EXIT' key is the standard key "
                            'for this action.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the Guard call log and the conference call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call Log" || key ts "History" || key ts "Recent Calls"',
                                    "screen_dump | grep -E '(Emergency|Guard|Conference|Call Log)'"],
             'confidence': 0.8,
             'explanation': 'Navigate to call log and verify emergency, guard, and conference call entries are present '
                            'with correct labels',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_24_Operator_Call_With_Emergency_Call',
  'preconditions': 'OXE:\r\n'
                   'mgr---SIP device management---DM profile:\r\n'
                   'Emergency number----xxxx\r\n'
                   'Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx', "screen_dump | grep -E 'Conversation|Operator'"],
             'confidence': 0.8,
             'explanation': 'Using call set with operator number from preconditions to establish call, then verifying '
                            'display shows conversation screen',
             'automation': 'automatable'},
            {'step': 'Phone makes the new outgoing call to Emergency',
             'expected': 'The Emergency call in the upper part of the screen:\n'
                         '"Emergency call"\n'
                         'Red background+ Emergency avatar + release button\n'
                         '\n'
                         'the Operator call is on hold\n'
                         'The Operator call in the lower part of the screen:\n'
                         'blue background +Operator avatar + switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect",
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx', "screen_dump | grep -E 'Emergency call|Emergency avatar'"],
             'confidence': 0.8,
             'explanation': "The step requires initiating an emergency call. The 'call set' command is used to dial "
                            'the emergency number (xxxx as placeholder). A screen dump is then used to verify the '
                            'emergency call UI elements as described.',
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the operator and Emergency call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Conference|Purple background|operator|Emergency call "
                                    "avatar'",
                                    "screen_dump softkey | grep -E 'exit|release'"],
             'confidence': 0.8,
             'explanation': 'The expected result describes the screen content after the remote side answers, including '
                            'conference info, background color, avatars, and softkey states. The commands verify the '
                            'display and softkey area for these elements.',
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'press_key',
             'suggested_commands': ['key sim EXIT'],
             'confidence': 0.9,
             'explanation': 'The step asks to press the exit/release button, which corresponds to the EXIT key. Since '
                            'no action is expected, a simple key press is sufficient.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the Operator call log and the conference call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call Log"',
                                    'screen_dump | grep -E "Emergency|Operator|Conference"'],
             'confidence': 0.8,
             'explanation': 'Navigate to call log from home screen and verify emergency, operator, and conference call '
                            'logs are present with correct labels.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_25_Guard_Call_With_Operator_Call',
  'preconditions': 'OXE:\r\n'
                   'mgr---SIP device management---DM profile:\r\n'
                   'Operator number----xxxx\r\n'
                   'Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         '\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx', "screen_dump | grep -E 'Conversation|Guard'"],
             'confidence': 0.8,
             'explanation': "Step requires establishing a call to the Guard number. The 'call set' command initiates "
                            "the call. A screen dump is then used to verify the expected 'Conversation' title and "
                            'Guard-related display.',
             'automation': 'automatable'},
            {'step': 'Phone makes the new outgoing call to Operator',
             'expected': 'The Operator call in the upper part of the screen:\n'
                         '"Operator call"\n'
                         'Purple background+ Operator avatar + release button\n'
                         '\n'
                         'the Guard call is on hold\n'
                         'The Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar + switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect",
             'intent': 'call_control',
             'suggested_commands': ['call set xxxx'],
             'confidence': 0.9,
             'explanation': 'Makes a new outgoing call to the Operator number configured in the DM profile.',
             'automation': 'automatable'},
            {'step': 'remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and operator call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'call_control',
             'suggested_commands': ['call answer'],
             'confidence': 0.9,
             'explanation': "The step 'remote side answer the call' instructs the phone under test to answer an "
                            "incoming call. The 'call answer' SSH command is the direct method to answer a ringing "
                            'call.',
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'press_key',
             'suggested_commands': ['key sim EXIT'],
             'confidence': 0.9,
             'explanation': 'The step asks to press the exit/release button, which corresponds to the EXIT key. This '
                            'is a straightforward key press operation.',
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the Operator call log and the conference call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'verify_display',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Call Log"',
                                    'screen_dump | grep -E "Guard|Operator|Conference"'],
             'confidence': 0.8,
             'explanation': 'Navigate to call log from home screen and verify presence of Guard, Operator, and '
                            'Conference entries',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_26_Light/Dark_Mode_Emergency/Guard/Operator_Call',
  'preconditions': 'OXE:\r\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'settings---device---appearance---light/dark mode',
             'expected': 'can modify  successfully',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim HOME',
                                    'key ts "Settings"',
                                    'key ts "Device"',
                                    'key ts "Appearance"',
                                    'key ts "Light/Dark Mode"'],
             'confidence': 0.9,
             'explanation': 'Navigate through Settings menu to reach Light/Dark Mode option using touch screen for '
                            'direct selection',
             'automation': 'automatable'},
            {'step': 'check the Emergency outgoing call screen/ hold screen/ conversation screen',
             'expected': 'The background color at the very bottom of the screen:\nlight mode: white \ndark mode: black',
             'intent': 'verify_display',
             'suggested_commands': ['call set 911', 'screen_dump raw', 'call drop'],
             'confidence': 0.8,
             'explanation': 'Make emergency call to trigger emergency screens, capture raw screen dump to check bottom '
                            'background color, then hang up. Need to verify emergency number configured on phone.',
             'automation': 'automatable'},
            {'step': 'check the Guard outgoing call screen/ hold screen/ conversation screen /conference screen',
             'expected': 'The background color at the very bottom of the screen:\nlight mode: white\ndark mode: black',
             'intent': 'verify_display',
             'suggested_commands': ['call set xxxx', 'screen_dump raw', 'call drop'],
             'confidence': 0.7,
             'explanation': 'The step requires checking the Guard outgoing call screen. The most direct way is to '
                            'place a call to the emergency/guard number (xxxx as per preconditions) and capture the '
                            'screen dump in raw mode to analyze the background color at the bottom. The call is then '
                            'dropped to clean up.',
             'automation': 'automatable'},
            {'step': 'check the Operator outgoing call screen/ hold screen/ conversation screen /conference screen',
             'expected': 'The background color at the very bottom of the screen:\nlight mode: white\ndark mode: black',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Operator|Call|Hold|Conference'",
                                    'screen_dump raw | head -20 | tail -5'],
             'confidence': 0.8,
             'explanation': 'Checking screen content for operator call/hold/conference screens and examining bottom '
                            'area for background color',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_27_Hard_Key_Default',
  'preconditions': '',
  'steps': [{'step': "OXE:  Doesn't configure the hard keys on the phone\n"
                     'Phone is out of box then connects the OXE\n'
                     '\n'
                     ' Enter the hard keys menu:\n'
                     'User/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device/Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the hard keys menu by opening the main menu and selecting the specified menu '
                            'item via touch screen.',
             'tags': ['menu', 'hard_keys', 'configuration'],
             'automation': 'automatable'},
            {'step': 'Long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long',
                                    'key sim SOFTK1 long',
                                    'key sim SOFTK2 long',
                                    'key sim BIS long',
                                    'key sim MESSAGE long',
                                    'key sim HOME long'],
             'confidence': 0.9,
             'explanation': 'The step requires long pressing multiple programmable soft keys (F1/F2/F3) and special '
                            'keys (Triangle/Circle/Square). SOFTK0-2 correspond to F1-F3 softkeys. BIS is the '
                            'alarm/triangle key, MESSAGE is the envelope/circle key, and HOME is the home/square key '
                            'on many models.',
             'tags': ['hard_key', 'long_press', 'programmable_key', 'softkey'],
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F1 key',
             'expected': 'ALE-30/300/400/500:\nIf disable the lock: no action\nIf enable the lock: will lock the phone',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The F1 key corresponds to the first softkey (SOFTK0) on Alcatel-Lucent phones. The step '
                            'requires pressing F1 while the phone is idle.',
             'tags': ['hard_key', 'softkey', 'idle'],
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call the led of the F1 is on\n'
                     'then press the F1 key\n'
                     'then press the F1 key again',
             'expected': 'ALE-30/300/400/500:\n'
                         'will hold the call, and led of the F1 key is breath\n'
                         'will retrieve the call. the led of the F1 key is on',
             'intent': 'call_control',
             'suggested_commands': ['call set 12345', 'key sim F1', 'key sim F1'],
             'confidence': 0.8,
             'explanation': "The step requires establishing a call, then pressing the F1 key twice. 'call set' "
                            'initiates a call. The F1 key is likely a programmable softkey (SOFTK0) or a conference '
                            "key. The first press should hold, the second should retrieve. Exact key mapping for 'F1' "
                            'is uncertain; assuming SOFTK0.',
             'tags': ['call', 'hold', 'retrieve', 'led', 'softkey'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1/F2/F3 is on\nthen press the F2 key',
             'expected': 'ALE-30/300/400/500:\nwill exit these two calls',
             'intent': 'call_control',
             'suggested_commands': ['call set 12345', 'call answer', 'call set 67890', 'call answer', 'key sim F2'],
             'confidence': 0.7,
             'explanation': 'The step requires establishing two calls and pressing the F2 key. The commands simulate '
                            'making and answering two calls (using placeholder numbers) and then pressing the F2 key. '
                            "The exact mapping of 'F2' to a key name (e.g., CONF1, ADDON1) is uncertain without "
                            "specific phone model context, so 'F2' is used directly as a best guess.",
             'tags': ['call', 'hard_key', 'led'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1/F2/F3 is on\nthen press the F3 key',
             'expected': 'ALE-300/400/500:will make the conference call,and led of the F3 key is breath',
             'intent': 'call_control',
             'suggested_commands': ['call set 1234567890',
                                    'call answer',
                                    'call set 0987654321',
                                    'call answer',
                                    'key sim CONF0'],
             'confidence': 0.7,
             'explanation': 'First, establish two calls. The commands simulate dialing and answering two numbers. Then '
                            'press the F3 key, which is mapped to CONF0 (Conference key 0) to initiate the conference. '
                            'The LED behavior cannot be verified via SSH.',
             'tags': ['conference', 'hardkey', 'call'],
             'automation': 'automatable'},
            {'step': 'check the Triangle/Circle/Square on ALE500',
             'expected': 'The three keys name display correctly\n'
                         'and press the hard key:\n'
                         'Triangle : Will Return to the previous interface\n'
                         'Circle: will turn to the dashboard\n'
                         'Square :The screen brightness will decreased',
             'intent': 'verify_display_and_test_keys',
             'suggested_commands': ["screen_dump | grep -E 'Triangle|Circle|Square'",
                                    'key sim HOME',
                                    "screen_dump | grep -E 'Dashboard|Home'",
                                    'key sim EXIT',
                                    "screen_dump | grep -E 'previous|back'",
                                    'key sim BIS',
                                    "screen_dump | grep -E 'brightness|dim'"],
             'confidence': 0.8,
             'explanation': 'First verify the three key names are displayed, then test each hard key function: HOME '
                            'for dashboard (circle), EXIT for previous interface (triangle), BIS for brightness '
                            'decrease (square).',
             'tags': ['hard_keys', 'display_verification', 'key_functionality'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_28_Hard_Key_OXE_Define_Position_Label_Recognition',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'set the progkey 123:programmed with the phone A number on position 1\n'
                     'mnemo:  position1\n'
                     'Phone update the config file then check the file\n'
                     '（/config/dm/config.xxxxxxx.xml）',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,x" override="true"/>',
             'intent': 'verify_configuration',
             'suggested_commands': ["grep 'SIPUseDeviceKey120' /config/dm/config.*.xml"],
             'confidence': 0.9,
             'explanation': 'The test requires checking the configuration file for the specific XML entry after '
                            'programming a key. The grep command will search for the expected setting in the config '
                            'file.',
             'tags': ['configuration', 'xml', 'program_key', 'verification'],
             'automation': 'automatable'},
            {'step': 'press the hard key:\nALE-30/300/400: F1 key\nALE-500: Triangle Key',
             'expected': 'Will makes the outgoing call to the phone A',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'SOFTK0 corresponds to the F1 key position on Alcatel-Lucent phones. For ALE-500 models, '
                            'the Triangle Key is typically mapped to the same physical position as F1/softkey 0.',
             'tags': ['hard_key', 'softkey', 'call_initiation'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 124:programmed with the phone B number on position 2\n'
                     'mnemo:  position_2\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position_2,30461,0,X" override="true"/>',
             'intent': 'verify_configuration',
             'suggested_commands': ["cat /etc/phone/profile.xml | grep 'SIPUseDeviceKey121'"],
             'confidence': 0.9,
             'explanation': "The step requires checking the phone's configuration file for a specific XML entry after "
                            'programming a key. The command reads the profile file and filters for the relevant '
                            'setting.',
             'tags': ['configuration', 'file_check', 'program_key'],
             'automation': 'automatable'},
            {'step': 'press the hard key:\nALE-30/300/400: F2 key\nALE-500: Circle Key',
             'expected': 'Will makes the outgoing call to the phone B',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK2'],
             'confidence': 0.9,
             'explanation': 'The F2 key on ALE-30/300/400 phones corresponds to the second programmable softkey '
                            "(SOFTK2). The 'Circle Key' on ALE-500 is likely the OK key, but the step specifies "
                            'different keys for different models. The primary instruction is for ALE-30/300/400, so '
                            'SOFTK2 is used.',
             'tags': ['hard_key', 'F2', 'SOFTK2', 'outgoing_call'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 123:programmed with the phone C number on position 1\n'
                     'mnemo:  position 1\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position 1,xxx,0,x" override="true"/>',
             'intent': 'program_key_configuration',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Settings"',
                                    'key ts "Programmable keys"',
                                    'key ts "Key 1"',
                                    'key ts "Label"',
                                    'key sim 1; key sim 2; key sim 3; key sim DIAL',
                                    'key ts "Save"',
                                    "screen_dump | grep -i 'position 1'"],
             'confidence': 0.7,
             'explanation': "Navigate to programmable key settings, program key 1 with label 'position 1' and phone C "
                            'number 123, then verify display shows the label. Actual config file check requires SSH '
                            "access to file system which isn't specified in available commands.",
             'tags': ['programmable_key', 'configuration', 'label', 'verification'],
             'automation': 'automatable'},
            {'step': 'press the hard key:\nALE-30/300/400: F1 key\nALE-500: Triangle Key',
             'expected': 'Will makes the outgoing call to the phone C',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press a hard key labeled F1 (ALE-30/300/400) or Triangle (ALE-500). '
                            'On Alcatel-Lucent VoIP phones, the F1 function key is typically mapped to the first '
                            "softkey (SOFTK0). The 'Triangle Key' is likely a softkey icon, also corresponding to "
                            'SOFTK0.',
             'tags': ['hard_key', 'softkey', 'function_key'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 124:programmed with the phone D number on position 2\n'
                     'mnemo:  POSITION2\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,POSITION2,30461,0,X" override="true"/>',
             'intent': 'verify_configuration',
             'suggested_commands': ["grep -i 'SIPUseDeviceKey121' /etc/phone/config.xml",
                                    "screen_dump | grep -i 'POSITION2'"],
             'confidence': 0.7,
             'explanation': 'The step requires checking the config file for a specific XML entry and verifying the '
                            'phone displays the mnemo. First command checks config, second verifies display.',
             'tags': ['configuration', 'program_key', 'verification'],
             'automation': 'automatable'},
            {'step': 'press the hard key:\nALE-30/300/400: F2 key\nALE-500: Circle Key',
             'expected': 'Will makes the outgoing call to the phone D',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK2'],
             'confidence': 0.9,
             'explanation': 'F2 key corresponds to SOFTK2 (second softkey position). Circle key on ALE-500 is '
                            'typically the navigation/OK key, but since the test specifies different models, SOFTK2 is '
                            'the most likely mapping for F2 key functionality.',
             'tags': ['hard_key', 'softkey', 'model_specific'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 123 and 124\n'
                     'mnemo:  the string is different to one of the “position1”, “position2”, “position3”',
             'expected': '.If and their equivalent as described in the two above points, by default, the key 120 is '
                         'mapped to “position1” and 121 to “position2',
             'intent': 'program_key_configuration',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Settings"',
                                    'key ts "Programmable keys"',
                                    'key ts "Key 123"',
                                    'key ts "Label"',
                                    'key ts "Clear"',
                                    'key ts "A"',
                                    'key ts "B"',
                                    'key ts "C"',
                                    'key ts "Save"',
                                    'key ts "Key 124"',
                                    'key ts "Label"',
                                    'key ts "Clear"',
                                    'key ts "D"',
                                    'key ts "E"',
                                    'key ts "F"',
                                    'key ts "Save"',
                                    'key sim HOME'],
             'confidence': 0.7,
             'explanation': 'The step requires setting program keys 123 and 124 with mnemonics different from '
                            "'position1', 'position2', 'position3'. The exact UI path and label entry method are "
                            'model-dependent. This sequence navigates to the programmable keys menu, selects each key, '
                            "clears any existing label, enters a distinct label (e.g., 'ABC' for key 123, 'DEF' for "
                            'key 124), saves, and returns home.',
             'tags': ['programmable_key', 'configuration', 'label', 'mnemonic'],
             'automation': 'automatable'},
            {'step': 'press the hard key:\nALE-30: F1/F2 key\nALE-300/400: F1/F2/F3 key\nALE-500: Triangle/Circle Key',
             'expected': 'The function is directly',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0', 'key sim SOFTK1', 'key sim SOFTK2'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing a hard function key (F1/F2/F3 or Triangle/Circle). On '
                            'Alcatel-Lucent VoIP phones, these are typically mapped to the softkey buttons (SOFTK0, '
                            'SOFTK1, SOFTK2). The command list covers all possible keys mentioned for different ALE '
                            'models.',
             'tags': ['hard_key', 'function_key', 'softkey'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_29_Hard_Key_OXE_Define_Key1_Lock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'Only set the progkey 123: programmed with phone A on position 1,and the lock parameter is '
                     'enabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,1" override="true"/>',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'program'", "screen_dump | grep -i 'key'"],
             'confidence': 0.3,
             'explanation': 'Step is about OXE programming a key with lock parameter, but the test step is vague. Need '
                            'to first verify the phone is on a programming screen or menu to proceed. Commands check '
                            'for program/key related text.',
             'tags': ['program_key', 'configuration', 'verification'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button,\n'
                         'Only F1 hard key is selected, all hard key names display grey\n'
                         'ALE-30:\n'
                         'two options: F1 cap icon/Phone A and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: F1 cap icon/Phone A and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Phone A and Circle cap icon/Home and Square cap icon/Low '
                         'power\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the Hard keys menu via the main menu path User/Device/Hard keys using touch '
                            'screen clicks for direct access.',
             'tags': ['navigation', 'menu', 'hard_keys'],
             'automation': 'automatable'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button,\n'
                         'Only F1 hard key is selected, all hard key names display grey\n'
                         'ALE-30:\n'
                         'two options: F1 cap icon/Phone A and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: F1 cap icon/Phone A and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Phone A and Circle cap icon/Home and Square cap icon/Low '
                         'power\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long', "screen_dump | grep -i 'Edit maximum 2 keys'"],
             'confidence': 0.9,
             'explanation': "The step requires a long press of the first programmable softkey (F1). The command 'key "
                            "sim SOFTK0 long' simulates this action. A screen dump is added to verify the expected "
                            'title appears, confirming the key press was successful and the correct menu is displayed.',
             'tags': ['hard_key', 'long_press', 'softkey', 'configuration'],
             'automation': 'automatable'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'F1.*hold|hold.*F1'",
                                    "screen_dump | grep -E 'F2.*transfer|transfer.*F2'",
                                    "screen_dump | grep -E 'F3.*conference|conference.*F3'"],
             'confidence': 0.8,
             'explanation': 'Verifying F1/F2/F3 function labels on display. Using grep patterns to check for expected '
                            'text near function keys.',
             'tags': ['display_verification', 'function_keys', 'label_check'],
             'automation': 'automatable'},
            {'step': 'Title "Edit maximum 2 keys"\n'
                     'The reset to default icon is grey\n'
                     'The left of the options all display the radio button,\n'
                     'Only F1 hard key is selected, all hard key names display grey\n'
                     'ALE-30:\n'
                     'two options: F1 cap icon/Phone A and transfer cap icon/Transfer\n'
                     'ALE-300/400:\n'
                     'three options: F1 cap icon/Phone A and transfer cap icon/Transfer and conference cap '
                     'icon/Conference\n'
                     'ALE-500:\n'
                     'three options: Triangle cap icon/Phone A and Circle cap icon/Home and Square cap icon/Low power\n'
                     '\n'
                     'ALE-300/400: The i icon display at the upper right corner of the screen',
             'expected': 'The three keys name display correctly\n'
                         'and press the hard key:\n'
                         'Triangle :Will makes the outgoing call to Phone A\n'
                         'Circle: will turn to the dashboard\n'
                         'Square :The screen brightness will decreased',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Edit maximum 2 keys|reset to default|F1|Phone "
                                    "A|Transfer|Conference|Triangle|Circle|Square|dashboard|brightness'",
                                    "screen_dump softkey | grep -E 'OK|EXIT|HELP'"],
             'confidence': 0.9,
             'explanation': 'Verify the screen displays the correct title, greyed reset icon, radio buttons, greyed '
                            'hard key names, and the correct options (F1/Phone A, Transfer, Conference for '
                            'ALE-300/400; Triangle/Phone A, Circle/Home, Square/Low power for ALE-500). Also check for '
                            "the 'i' icon on ALE-300/400.",
             'tags': ['display_verification', 'hard_key_config', 'ui_check'],
             'automation': 'automatable'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle key',
             'expected': 'Will makes the second outgoing call to phone A',
             'intent': 'call_control',
             'suggested_commands': ['call set <phone_B_number>', 'sleep 2', 'key sim CONF0'],
             'confidence': 0.9,
             'explanation': 'First establish call to phone B, then press Triangle key (CONF0) to initiate second '
                            'outgoing call',
             'tags': ['call', 'conference', 'hard_key'],
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nWill makes the outgoing call to phone A',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The F1 key corresponds to the first softkey (SOFTK0). The phone is idle, so pressing it '
                            'should initiate the pre-programmed action (outgoing call).',
             'tags': ['hard_key', 'softkey', 'call_initiation'],
             'automation': 'automatable'},
            {'step': 'Phone establish a call with phone B then press the F1',
             'expected': 'ALE-30/300/400:\nWill makes the second outgoing call to phone A',
             'intent': 'call_control',
             'suggested_commands': ['call set <phone_B_number>', 'key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'First establish call to phone B, then press F1 (SOFTK0) to initiate second outgoing call '
                            'to phone A as expected.',
             'tags': ['call', 'softkey', 'conference'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1 is off, the led of the F2/F3 is on\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls',
             'intent': 'call_control',
             'suggested_commands': ['call set 12345', 'call drop', 'call set 67890', 'call answer', 'key sim CONF1'],
             'confidence': 0.7,
             'explanation': 'First establish two calls: make first call, hang up, make second call, answer it, then '
                            'press CONF1 (assuming F2 maps to CONF1). Need to verify actual key mapping for F2.',
             'tags': ['call', 'conference', 'hard_key'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1 is off, the led of the F2/F3 is on\n'
                     'then press the F3 key',
             'expected': 'ALE-30/300/400:\nwill makes the conference call, and the led of the conference is breath',
             'intent': 'call_control',
             'suggested_commands': ['call set 12345', 'call answer', 'call set 67890', 'call answer', 'key sim CONF0'],
             'confidence': 0.7,
             'explanation': 'Step requires establishing two calls and pressing the F3 key (assumed to be CONF0). '
                            'Commands simulate making and answering two calls, then pressing the conference key. '
                            'Preconditions about LED states are not directly verifiable via SSH.',
             'tags': ['conference', 'hard_key', 'call'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>',
             'intent': 'program_key_configuration',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Settings"',
                                    'key ts "Programmable keys"',
                                    'key ts "Key 1"',
                                    'screen_dump | grep -E "Not Assigned|124"'],
             'confidence': 0.7,
             'explanation': "Navigate to programmable key settings to configure Key 1 as 'Not Assigned' (124). Exact "
                            'menu path may vary by phone model.',
             'tags': ['program_key', 'configuration', 'oxe'],
             'automation': 'automatable'},
            {'step': 'Phone Enter the hard keys menu:\n'
                     'User/Device/Hard keys\n'
                     'or long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to Hard keys menu via MENU key and touch screen to avoid repeated key presses.',
             'tags': ['menu_navigation', 'hard_keys', 'configuration'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_30_Hard_Key_OXE_Define_Key2_Unlock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'Only set the progkey 124: programmed with the Emergency function on position 2,and the lock '
                     'parameter is disabled\n'
                     'Phone update the config file then check the file![](index.php?/attachments/get/44225)',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position2,xxx,0,0" override="true"/>',
             'intent': 'verify_configuration',
             'suggested_commands': ["screen_dump | grep -i 'emergency'",
                                    "key ts 'Emergency'",
                                    "screen_dump | grep -i 'lock'",
                                    'key sim EXIT'],
             'confidence': 0.7,
             'explanation': 'The step requires verifying that a program key is configured with Emergency function on '
                            'position 2 with lock disabled. First check if Emergency is visible, then navigate to '
                            'verify lock status.',
             'tags': ['program_key', 'emergency', 'configuration', 'lock'],
             'automation': 'automatable'},
            {'step': 'Phone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button,\n'
                         'F2 hard key name is light the other key is grey\n'
                         'Only F2 hard key is selected and the edit icon is displayed on the right\n'
                         'ALE-30:\n'
                         'two options: hold icon button/On hold and Red cap icon/Emergency\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and Red cap icon/Emergency and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/On hold and Circle cap icon/Emergency and Square cap '
                         'icon/Low power\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the hard keys menu via the main menu, then touch screen selections for '
                            "'User/Device' and 'Hard keys'.",
             'tags': ['navigation', 'menu', 'hard_keys'],
             'automation': 'automatable'},
            {'step': 'Long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button,\n'
                         'F2 hard key name is light the other key is grey\n'
                         'Only F2 hard key is selected and the edit icon is displayed on the right\n'
                         'ALE-30:\n'
                         'two options: hold icon button/On hold and Red cap icon/Emergency\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and Red cap icon/Emergency and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/On hold and Circle cap icon/Emergency and Square cap '
                         'icon/Low power\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long'],
             'confidence': 0.9,
             'explanation': "The step 'Long press the F1/F2/F3/Triangle/Circle/Square key' refers to a programmable "
                            'softkey. On Alcatel-Lucent phones, F1 is typically SOFTK0. A long press is required.',
             'tags': ['hard_key', 'long_press', 'softkey', 'programmable_key'],
             'automation': 'automatable'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump softkey | grep -E 'F1.*hold|hold.*F1'",
                                    "screen_dump softkey | grep -E 'F2.*transfer|transfer.*F2'",
                                    "screen_dump softkey | grep -E 'F3.*conference|conference.*F3'"],
             'confidence': 0.8,
             'explanation': 'Verifying softkey labels for F1/F2/F3 functions on ALE-500 display. Using softkey screen '
                            'dump to check for expected labels.',
             'tags': ['softkey', 'verification', 'ALE-500'],
             'automation': 'automatable'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will Return to the previous interface\n'
                         'Circle: Will makes the outgoing call to Emergency\n'
                         'Square :The screen brightness will decreased',
             'intent': 'verify_display_and_key_function',
             'suggested_commands': ["screen_dump | grep -E 'Triangle|Circle|Square|emergency'",
                                    'key sim ADDON0',
                                    'screen_dump',
                                    'key sim ADDON1',
                                    'call drop'],
             'confidence': 0.8,
             'explanation': 'First, verify the key labels and emergency color via screen dump. Then test Triangle '
                            '(ADDON0) for navigation back, Circle (ADDON1) for emergency call (requires immediate '
                            'hangup), and Square (ADDON2) for brightness decrease. Using ADDON keys as standard '
                            'mapping for triangle/circle/square programmable keys.',
             'automation': 'automatable'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Circle key',
             'expected': 'Will makes the second outgoing call to Emergency',
             'intent': 'call_control',
             'suggested_commands': ['call set <phone_B_number>', 'key sim OK'],
             'confidence': 0.8,
             'explanation': "Assuming 'Circle key' refers to the OK/Select key (often circular). First establish a "
                            'call to phone B, then press the OK key to initiate a second call, presumably to Emergency '
                            'as per expected result. The exact Emergency number or dialing method is not specified in '
                            'the step.',
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F1 is on,the led of the F2/F3 is off',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK1'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press the F2 key while the phone is idle. On Alcatel-Lucent phones, '
                            'the F1/F2/F3 keys are typically mapped to the programmable softkeys SOFTK0, SOFTK1, '
                            "SOFTK2. Pressing F2 corresponds to 'key sim SOFTK1'.",
             'automation': 'automatable'},
            {'step': 'Phone establish a call. \nDuring the converstiaon then press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the new outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F2 is off,the led of the F1/F3 is oN',
             'intent': 'call_control_and_key_press',
             'suggested_commands': ['call set 911', 'sleep 2', 'key sim SOFTK2'],
             'confidence': 0.9,
             'explanation': 'First establish a call to emergency number (911), then press F2 key (SOFTK2) during '
                            'conversation',
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath',
             'intent': 'call_control',
             'suggested_commands': ['call set 123', 'key sim ADDON0'],
             'confidence': 0.8,
             'explanation': "First establish a call, then press the F1 key (ADDON0) to hold it. The number '123' is a "
                            'placeholder.',
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1/F3 is on\nthen press the F3 key',
             'expected': 'ALE-300/400:\nwill make the conference call,and led of the F3 key is breath',
             'intent': 'call_control',
             'suggested_commands': ['call set 12345', 'call drop', 'call set 67890', 'call drop', 'key sim CONF0'],
             'confidence': 0.7,
             'explanation': 'First establish two calls (using placeholder numbers), then press the conference key (F3 '
                            'is CONF0). Need to verify LED status via screen dump.',
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'program_key_configuration',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Settings"',
                                    'key ts "Programmable keys"',
                                    'key ts "Key 124"',
                                    'key ts "Not Assigned"'],
             'confidence': 0.7,
             'explanation': "Navigating through menu to set programmable key 124 to 'Not Assigned'. Exact menu "
                            'structure may vary by phone model/firmware.',
             'automation': 'automatable'},
            {'step': 'Phone Enter the hard keys menu:\n'
                     'User/Device/Hard keys\n'
                     'or long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device/Hard keys"'],
             'confidence': 0.9,
             'explanation': "The step requires entering the hard keys menu via the UI path 'User/Device/Hard keys'. "
                            'The first command opens the main menu, and the second uses touch screen to directly '
                            'select the target menu item, which is more efficient than multiple key presses.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_31_Hard_Key_OXE_Define_Key3_Unlock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'Only set the progkey 124: programmed with the Guard function on position 3,and the lock '
                     'parameter is disabled\n'
                     'Phone update the config file then check the file![](index.php?/attachments/get/44226)',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position3,xxx,0,0" override="true"/>',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'program'", "screen_dump | grep -i 'key'"],
             'confidence': 0.3,
             'explanation': 'Step is ambiguous; it mentions OXE user programming a key with Guard function, but the '
                            'phone-side action is unclear. Initial verification of program key menu is needed.',
             'automation': 'needs_context'},
            {'step': 'Phone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button,\n'
                         'F3 hard key name is light the other key is grey\n'
                         'Only F3 hard key is selected and the edit icon is displayed on the right\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and abc cap icon/Guard\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Guard\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the hard keys menu via the main menu and touch screen selections.',
             'automation': 'automatable'},
            {'step': 'Long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button,\n'
                         'F3 hard key name is light the other key is grey\n'
                         'Only F3 hard key is selected and the edit icon is displayed on the right\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and abc cap icon/Guard\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Guard\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long'],
             'confidence': 0.9,
             'explanation': "The step 'Long press the F1/F2/F3/Triangle/Circle/Square key' is ambiguous but typically "
                            'maps to a softkey. F1/F2/F3 often correspond to SOFTK0, SOFTK1, SOFTK2. Assuming the '
                            'first softkey (F1) is the target for a long press.',
             'automation': 'automatable'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'F1.*hold|hold.*F1'",
                                    "screen_dump | grep -E 'F2.*transfer|transfer.*F2'",
                                    "screen_dump | grep -E 'F3.*conference|conference.*F3'"],
             'confidence': 0.8,
             'explanation': 'The step requires checking the displayed function labels for F1, F2, and F3 keys. Using '
                            'screen_dump with grep is the most direct way to verify the text on the screen matches the '
                            'expected labels (hold, transfer, conference).',
             'automation': 'automatable'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly\n'
                         'and press the hard key:\n'
                         'Triangle : Will Return to the previous interface\n'
                         'Circle: will turn to the dashboard\n'
                         'Square :will makes the outgoing call to guard',
             'intent': 'verify_display_and_test_keys',
             'suggested_commands': ["screen_dump | grep -E 'Triangle|Circle|Square'",
                                    'key sim ADDON0',
                                    "screen_dump | grep -E 'previous|dashboard|guard'",
                                    'key sim ADDON1',
                                    "screen_dump | grep -E 'previous|dashboard|guard'",
                                    'key sim ADDON2',
                                    "screen_dump | grep -E 'previous|dashboard|guard'"],
             'confidence': 0.9,
             'explanation': 'First verify the three keys are displayed correctly, then test each ADDON key '
                            '(Triangle=ADDON0, Circle=ADDON1, Square=ADDON2) and verify the expected behavior after '
                            'each press.',
             'automation': 'automatable'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Square  key',
             'expected': 'Will makes the second outgoing call to guard',
             'intent': 'call_control',
             'suggested_commands': ['call set <phone_B_number>', 'key sim CONF0'],
             'confidence': 0.9,
             'explanation': 'First establish call to phone B, then press CONF0 (Square key) to initiate second '
                            'outgoing call',
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F3 key',
             'expected': 'ALE-300/400:\n'
                         'Makes the outgoing call to the guard\n'
                         'and the screen display correctly\n'
                         'Adn during the conversation, the led of the F1/F3 is on,the led of the F2 is off',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK2'],
             'confidence': 0.9,
             'explanation': 'Press the F3 key (SOFTK2) while phone is idle.',
             'automation': 'automatable'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F3',
             'expected': 'ALE-300/400:\n'
                         'Makes the new outgoing call to the guard\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F1 is on,the led of the F2/F3 is off',
             'intent': 'call_control',
             'suggested_commands': ['call set 123', 'key sim SOFTK2'],
             'confidence': 0.8,
             'explanation': 'Step requires establishing a call and pressing F3 (SOFTK2) during conversation. The call '
                            'number is unspecified, so using a placeholder (123).',
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath',
             'intent': 'call_control',
             'suggested_commands': ['call set 123',
                                    "screen_dump | grep -i 'connected' || screen_dump | grep -i 'call'",
                                    'key sim ADDON0'],
             'confidence': 0.8,
             'explanation': 'Step requires establishing a call and pressing the F1 key (ADDON0). The call setup is '
                            'straightforward, but verifying the LED state (breathing) is not directly possible via '
                            'SSH; we can only check call state via screen.',
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1/F2 is on, the led of the F3 is off\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls',
             'intent': 'call_control',
             'suggested_commands': ['call set 12345', 'call answer', 'call set 67890', 'call answer', 'key sim SOFTK2'],
             'confidence': 0.8,
             'explanation': 'Establish two calls (assuming numbers 12345 and 67890) and press F2 (SOFTK2) to exit '
                            'calls',
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'program'",
                                    "screen_dump | grep -i 'key'",
                                    "screen_dump | grep -i '124'",
                                    "screen_dump | grep -i 'not assigned'"],
             'confidence': 0.7,
             'explanation': 'The step describes an OXE configuration action to set a program key. This is a '
                            'provisioning/configuration step, not a direct phone UI interaction. The most relevant '
                            "automation is to verify the phone's display shows the programming interface or the key "
                            'status, but the exact UI path is not specified. The commands check for common programming '
                            'menu text.',
             'automation': 'needs_context'},
            {'step': 'Phone Enter the hard keys menu:\n'
                     'User/Device/Hard keys\n'
                     'or long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'navigate_to_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device/Hard keys"'],
             'confidence': 0.9,
             'explanation': 'First press MENU key to open main menu, then use touch screen to directly select '
                            "'User/Device/Hard keys' menu item if visible. This is more efficient than navigating with "
                            'arrow keys.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_32_Hard_Key_OXE_Define_Key 1&2_Lock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'set the progkey 123: programmed with the Emergency function on position 1\n'
                     'set the progkey 124: programmed with the Guard function on position 2\n'
                     'And the lock parameter are enabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,1" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,position2,xxx,0,1" override="true"/>',
             'intent': 'verify_configuration',
             'suggested_commands': ["grep -E 'SIPUseDeviceKey120|SIPUseDeviceKey121' /etc/phone/config.xml"],
             'confidence': 0.8,
             'explanation': "The step requires checking the phone's configuration file for specific XML entries after "
                            'programming keys via OXE. The SSH command directly searches for the expected lines in the '
                            'config file.',
             'automation': 'automatable'},
            {'step': 'Phone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only F1 and F2 hard key display the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'ALE-30:\n'
                         'two options: Red cap icon/Emergency and F2 cap icon/Guard\n'
                         'ALE-300/400:\n'
                         'three options: Red cap icon/ Emergency and F2 cap icon/ Guard and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/ Emergency and Circle cap icon/ Guard and Square cap icon/ '
                         'Conference\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the hard keys menu via the main menu, then touch screen selections for '
                            "'User/Device' and 'Hard keys'.",
             'automation': 'automatable'},
            {'step': 'Long press the F1/F2/F3 key',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only F1 and F2 hard key display the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'ALE-30:\n'
                         'two options: Red cap icon/Emergency and F2 cap icon/Guard\n'
                         'ALE-300/400:\n'
                         'three options: Red cap icon/ Emergency and F2 cap icon/ Guard and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/ Emergency and Circle cap icon/ Guard and Square cap icon/ '
                         'Conference\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long', 'key sim SOFTK1 long', 'key sim SOFTK2 long'],
             'confidence': 0.9,
             'explanation': 'F1/F2/F3 keys correspond to SOFTK0/SOFTK1/SOFTK2. Long press each to trigger admin key '
                            'definition mode.',
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\n'
                     'enable or disable the lock\n'
                     'then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation, the led of the F1/F2/F3 is off',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -v 'Emergency'", "screen_dump | grep -i 'idle'"],
             'confidence': 0.8,
             'explanation': 'Final verification that phone returns to idle mode and F1/F2/F3 LED status is off '
                            '(indirectly verified via screen)',
             'automation': 'automatable'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Will makes the new outgoing call to the emergency\n'
                         'and the screen display correctly',
             'intent': 'call_control',
             'suggested_commands': ['call set 123', 'sleep 2', 'key sim SOFTK0'],
             'confidence': 0.8,
             'explanation': 'First establish a call using a test number, then press F1 (SOFTK0) during the '
                            'conversation',
             'automation': 'automatable'},
            {'step': 'Phone is idle then press the F2 Key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the guard\n'
                         'During the conversation, the led of the F1/F2/F3 is off',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK1'],
             'confidence': 0.9,
             'explanation': 'F2 key corresponds to SOFTK1 (softkey 1) on Alcatel-Lucent VoIP phones',
             'automation': 'automatable'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Will makes the new outgoing call to the guard\n'
                         'and the screen display correctly',
             'intent': 'call_control',
             'suggested_commands': ['call set 123', 'key sim SOFTK2'],
             'confidence': 0.8,
             'explanation': 'First establish a call using a dummy number, then press the F2 key (SOFTK2) during the '
                            'conversation.',
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls,\n'
                     'the led of the F3 is on,the led of the F1/F2 is off\n'
                     'then press the F3 key',
             'expected': 'ALE-300/400:\nwill make the conference call,and led of the F3 key is breath',
             'intent': 'call_control',
             'suggested_commands': ['call set 1001', 'call answer', 'call set 1002', 'call answer', 'key sim CONF0'],
             'confidence': 0.8,
             'explanation': 'Establish two calls and press conference key (F3). Using CONF0 for conference key as '
                            'typical mapping.',
             'automation': 'automatable'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will makes the outgoing call to emergency\n'
                         'Circle: Will makes the outgoing call to guard\n'
                         'Square :The screen brightness will decreased',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'call'", "screen_dump | grep -i 'brightness'"],
             'confidence': 0.7,
             'explanation': 'After pressing each key, verify the expected actions: outgoing call screens for '
                            'Triangle/Circle, and brightness change indication for Square (though brightness change '
                            'may not be directly verifiable via SSH).',
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Circle key',
             'expected': 'Will makes the second outgoing call to emergency/guard',
             'intent': 'call_control',
             'suggested_commands': ['call set <phone_B_number>', 'key sim ADDON0'],
             'confidence': 0.8,
             'explanation': 'The step requires establishing a call and then pressing the Triangle/Circle key. The '
                            "'ADDON0' key is the typical mapping for the first programmable addon key, which often has "
                            'a triangle/circle icon. The phone B number is a placeholder.',
             'automation': 'automatable'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'F1.*hold|hold.*F1'",
                                    "screen_dump | grep -E 'F2.*transfer|transfer.*F2'",
                                    "screen_dump | grep -E 'F3.*conference|conference.*F3'"],
             'confidence': 0.8,
             'explanation': 'The step requires checking the displayed function labels for F1, F2, and F3 keys. Using '
                            'screen_dump with grep is the most direct way to verify the text on the display matches '
                            'the expected labels (hold, transfer, conference).',
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Not Assigned|Unassigned|Empty'"],
             'confidence': 0.7,
             'explanation': "The step describes verifying that program keys 123 and 124 are set to 'Not Assigned'. The "
                            "most direct verification is to check the phone's display for the 'Not Assigned' status, "
                            'likely in a menu or settings screen.',
             'automation': 'automatable'},
            {'step': 'Phone Enter the hard keys menu:\n'
                     'User/Device/Hard keys\n'
                     'or long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'navigate_to_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device/Hard keys"'],
             'confidence': 0.9,
             'explanation': 'First press MENU to open main menu, then use touch screen to directly select '
                            "'User/Device/Hard keys' menu item if visible. This is more efficient than navigating "
                            'through multiple key presses.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_33_Hard_Key_OXE_Define_Key 2_Lock_Key 3_Unlock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'set the progkey 123: programmed with the Emergency function on position 3,the lock parameter is '
                     'disabled\n'
                     'set the progkey 124: programmed with the Guard function on position 2,the lock paramter is '
                     'enabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position3,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,position2,xxx,0,1" override="true"/>',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Emergency|Guard|program|key'"],
             'confidence': 0.3,
             'explanation': 'Step describes OXE configuration and checking a config file, not direct phone UI '
                            'interaction. The only automatable part is verifying the phone display shows relevant '
                            'status after update, but the step is primarily a backend configuration check.',
             'automation': 'needs_context'},
            {'step': 'Phone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button,\n'
                         'F2&F3 hard key name is light the F1 key name is grey\n'
                         'F2 and F3 hard keys are selected but only F3: the edit icon is displayed on the right\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and F2 cap icon/Guard\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and F2 cap icon/ Guard and Red cap icon/Emergency\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/ On hold and Circle cap icon/ Guard and Square cap icon/ '
                         'Emergency\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the hard keys menu via the main menu, then touch screen selections for '
                            "'User/Device' and 'Hard keys'.",
             'automation': 'automatable'},
            {'step': 'Long press the F1/F2/F3 key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button,\n'
                         'F2&F3 hard key name is light the F1 key name is grey\n'
                         'F2 and F3 hard keys are selected but only F3: the edit icon is displayed on the right\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and F2 cap icon/Guard\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and F2 cap icon/ Guard and Red cap icon/Emergency\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/ On hold and Circle cap icon/ Guard and Square cap icon/ '
                         'Emergency\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long'],
             'confidence': 0.9,
             'explanation': 'The F1 key is typically mapped to the first softkey (SOFTK0). The instruction is to long '
                            'press it.',
             'automation': 'automatable'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK2'],
             'confidence': 0.9,
             'explanation': "The step mentions pressing 'the remaining key' which likely refers to a third softkey "
                            'after two keys have already been selected/locked. SOFTK2 is the third softkey (0-indexed: '
                            'SOFTK0, SOFTK1, SOFTK2).',
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the Guard\n'
                         'and the screen display corectly\n'
                         'And during the conversation, thel ed of the F1 is on,the led of the F2/F3 is off',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK1'],
             'confidence': 0.9,
             'explanation': 'The step requires pressing the F2 key while the phone is idle. On Alcatel-Lucent VoIP '
                            'phones, the F1/F2/F3 keys typically correspond to programmable softkeys SOFTK0, SOFTK1, '
                            "SOFTK2. Pressing F2 is simulated with 'key sim SOFTK1'.",
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call then press the F2 key',
             'expected': 'ALE-30/300/400:\nMakes the new outgoing call to the Guard\nand the screen display corectly',
             'intent': 'call_control',
             'suggested_commands': ['call set 123', 'key sim SOFTK1'],
             'confidence': 0.8,
             'explanation': "First establish a call using 'call set' with a placeholder number, then press the F2 key "
                            'which is SOFTK1.',
             'automation': 'automatable'},
            {'step': 'Phone is idle then press the F3 key',
             'expected': 'ALE-300/400:\n'
                         'Makes the outgoing call to the Emergency\n'
                         'and the screen display corectly\n'
                         'During the conversation, the led of the F1 is on,the led of the F2/F3 is off',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK2'],
             'confidence': 0.9,
             'explanation': 'The step instructs to press the F3 key while the phone is idle. On Alcatel-Lucent VoIP '
                            'phones, programmable function keys F1-F3 are typically mapped to SOFTK0-SOFTK2. F3 '
                            'corresponds to SOFTK2.',
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call then press the F3 key',
             'expected': 'ALE-300/400:\nMakes the new outgoing call to the Emergency\nand the screen display corectly',
             'intent': 'call_control',
             'suggested_commands': ['call set 123', 'key sim SOFTK2'],
             'confidence': 0.8,
             'explanation': "Step requires establishing a call then pressing F3 (SOFTK2). Using a dummy number '123' "
                            'for the call. The expected result mentions an Emergency call, suggesting the F3 key may '
                            'be programmed for emergency dialing, but the step instruction is followed directly.',
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath',
             'intent': 'call_control',
             'suggested_commands': ['call set 123', 'sleep 2', 'key sim ADDON0'],
             'confidence': 0.8,
             'explanation': "Step requires establishing a call and pressing the F1 key (ADDON0). The '123' is a "
                            'placeholder number for the call. A short sleep ensures the call is active before pressing '
                            'the key.',
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls',
             'expected': 'the led of the F1 is on, the led of the F2/F3 is off',
             'intent': 'call_control',
             'suggested_commands': ['call set 1234', 'call answer', 'call set 5678', 'call answer'],
             'confidence': 0.7,
             'explanation': "Step requires establishing two normal calls. Commands make a call to '1234', answer it "
                            "(assuming another phone calls back), make a second call to '5678', and answer it. This "
                            'simulates two active calls. Specific numbers may need adjustment.',
             'automation': 'automatable'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will Return to the previous interface\n'
                         'Circle: Will makes the outgoing call to guard\n'
                         'Square :Will makes the outgoing call to emergency',
             'intent': 'verify_display_and_functionality',
             'suggested_commands': ["screen_dump | grep -E 'Triangle|Circle|Square|emergency'",
                                    'key sim ADDON0',
                                    'screen_dump',
                                    'key sim ADDON1',
                                    'call drop'],
             'confidence': 0.8,
             'explanation': 'First verify the display shows the three key names with emergency in red. Then test each '
                            'hard key: ADDON0 (Triangle) should return to previous interface, ADDON1 (Circle) should '
                            'call guard, ADDON2 (Square) should call emergency. Need to hang up after test calls.',
             'automation': 'automatable'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Circle key',
             'expected': 'Will makes the second outgoing call to guard/emergency',
             'intent': 'call_control',
             'suggested_commands': ['call set <phone_B_number>', 'key sim ADDON0'],
             'confidence': 0.8,
             'explanation': 'The step requires establishing a call with phone B, then pressing the Triangle/Circle '
                            "key. The 'call set' command initiates the call. The Triangle/Circle key is typically "
                            'mapped to an ADDON key (ADDON0-3). Assuming the first programmable key is used, ADDON0 is '
                            'the most common default for such a function.',
             'automation': 'automatable'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump softkey | grep -E 'hold|Hold'",
                                    "screen_dump softkey | grep -E 'transfer|Transfer'",
                                    "screen_dump softkey | grep -E 'conference|Conference'"],
             'confidence': 0.8,
             'explanation': 'Checking softkey labels for F1/F2/F3 functions. Using softkey screen dump to verify the '
                            'labels match expected functions.',
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Program Key|Not Assigned|123|124'"],
             'confidence': 0.7,
             'explanation': "Step requires verifying the display shows the program key menu or 'Not Assigned' status "
                            'for keys 123 and 124. Using screen_dump to check the current screen content.',
             'automation': 'automatable'},
            {'step': 'Phone Enter the hard keys menu:\n'
                     'User/Device/Hard keys\n'
                     'or long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigates to the Hard keys menu via the main menu and touch screen selections as '
                            'described in the step.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_34_Hard_Key_OXE_Define_Key 1&3_Unlock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'set the progkey 123: programmed with the Emergency function on position 1\n'
                     'set the progkey 124: programmed with the Guard function on position 3\n'
                     'And the lock parameter are all disabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,position3,xxx,0,0" override="true"/>',
             'intent': 'verify_configuration',
             'suggested_commands': ["grep -E 'SIPUseDeviceKey120|SIPUseDeviceKey121' /etc/phone/config.xml"],
             'confidence': 0.8,
             'explanation': "The step requires checking the phone's configuration file for specific XML entries after "
                            'programming keys. The grep command is the most direct way to verify the presence and '
                            'content of the expected settings.',
             'automation': 'automatable'},
            {'step': 'Phone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button,\n'
                         'F1 and F3 hard key names are light the F2 key name is grey\n'
                         'F1 and F3 hard keys are selected and the edit icon is displayed on the right\n'
                         'ALE-30:\n'
                         'two options: Red cap icon/Emergency and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: Red cap icon/ Emergency and transfer cap icon/Transfer and abc cap '
                         'icon/Guard\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/ Emergency and Circle cap icon/Home and Square cap '
                         'icon/Guard\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the hard keys menu via the main menu and touch screen selections.',
             'automation': 'automatable'},
            {'step': 'Long press the F1/F2/F3 key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button,\n'
                         'F1 and F3 hard key names are light the F2 key name is grey\n'
                         'F1 and F3 hard keys are selected and the edit icon is displayed on the right\n'
                         'ALE-30:\n'
                         'two options: Red cap icon/Emergency and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: Red cap icon/ Emergency and transfer cap icon/Transfer and abc cap '
                         'icon/Guard\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/ Emergency and Circle cap icon/Home and Square cap '
                         'icon/Guard\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long'],
             'confidence': 0.9,
             'explanation': "The step 'Long press the F1/F2/F3 key' refers to the programmable softkeys. F1 is SOFTK0, "
                            "F2 is SOFTK1, F3 is SOFTK2. The test title mentions 'Define_Key 1&3', so the action "
                            'likely starts with F1 (SOFTK0). A long press is required.',
             'automation': 'automatable'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK2'],
             'confidence': 0.8,
             'explanation': "Assuming the 'remaining key' is the third programmable softkey (SOFTK2) after keys 1 and "
                            '3 are already defined. This is a typical scenario for defining keys on Alcatel-Lucent '
                            'phones.',
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\n'
                     'enable or disable the lock\n'
                     'then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and screen display correctly\n'
                         'and during the conversation, the led of the F1/F2/F3 is off',
             'intent': 'verify_display_and_call',
             'suggested_commands': ["screen_dump | grep -E 'Idle|Home'",
                                    'call set 911',
                                    "screen_dump | grep -E 'Emergency|Calling|Dialing'",
                                    "screen_dump softkey | grep -E 'F1|F2|F3'"],
             'confidence': 0.8,
             'explanation': 'Step requires verifying idle mode, making an emergency call, checking display, and '
                            "verifying F1/F2/F3 LED status via softkey dump. The 'enable or disable the lock' "
                            'precondition is ambiguous but likely refers to a phone lock state; assuming phone is '
                            'unlocked for emergency call. F1 key press is simulated via call to emergency number '
                            '(e.g., 911).',
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F3 key',
             'expected': 'ALE-300/400:\nMakes the outgoing call to the Guard\nand screen display correctly',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK2'],
             'confidence': 0.9,
             'explanation': 'F3 key corresponds to SOFTK2 (softkey 2) on Alcatel-Lucent phones. Phone is in idle mode '
                            'as precondition.',
             'automation': 'automatable'},
            {'step': 'Phone establish one normal calls,the led of the F1/F2/F3 IS OFF\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nMakes the new outgoing call to the emergency\nand screen display correctly',
             'intent': 'call_control',
             'suggested_commands': ['call set 911', "screen_dump | grep -i 'emergency\\|calling\\|dialing'"],
             'confidence': 0.8,
             'explanation': 'First establish a normal call to emergency number (911), then verify screen shows '
                            'emergency/calling/dialing text. F1 key is likely SOFTK0 (first programmable key).',
             'automation': 'automatable'},
            {'step': 'Phone establish one normal calls,the led of the F1/F2/F3 IS OFF\nthen press the F3 key',
             'expected': 'ALE-300/400:\nMakes the new outgoing call to the Guard\nand screen display correctly',
             'intent': 'call_control_and_key_press',
             'suggested_commands': ['call set 123', 'sleep 2', 'key sim SOFTK2'],
             'confidence': 0.8,
             'explanation': 'First establish a call using a test number, then press F3 key (SOFTK2). Need to verify '
                            'LED status is OFF first, but that requires context about current state.',
             'automation': 'needs_context'},
            {'step': 'Phone establish two normal calls, the led of the F2 is on,the led of F1/F3 is off\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls',
             'intent': 'call_control',
             'suggested_commands': ['call set 1234567890',
                                    'call drop',
                                    'call set 0987654321',
                                    'call answer',
                                    'key sim CONF0'],
             'confidence': 0.7,
             'explanation': 'First call setup, hangup, second call setup, answer, then press F2 (CONF0) to exit both '
                            'calls. Need actual numbers for calls.',
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nCheck the Triangle Triangle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will makes the outgoing call to emergency\n'
                         'Circle: will turn to the homepage\n'
                         'Square :Will makes the outgoing call to guard',
             'intent': 'press_key',
             'suggested_commands': ['key sim ADDON2', 'call drop'],
             'confidence': 0.7,
             'explanation': 'Assuming Square is ADDON2. Press to make guard call, then hang up.',
             'automation': 'automatable'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Square key',
             'expected': 'Will makes the second outgoing call to emergency/guard',
             'intent': 'press_key',
             'suggested_commands': ['call set <phone_B_number>', 'key sim ADDON0'],
             'confidence': 0.8,
             'explanation': 'Establish a call to phone B, then press the first addon key (ADDON0) which is likely the '
                            'Triangle/Square key. The exact addon key mapping (0-3) for Triangle/Square needs '
                            'verification.',
             'automation': 'automatable'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump softkey | grep -E 'F1.*hold|hold.*F1'",
                                    "screen_dump softkey | grep -E 'F2.*transfer|transfer.*F2'",
                                    "screen_dump softkey | grep -E 'F3.*conference|conference.*F3'"],
             'confidence': 0.8,
             'explanation': 'The step requires checking the softkey labels (F1/F2/F3) on the ALE-500 phone display. '
                            "Using 'screen_dump softkey' will output the current softkey labels, and grepping for the "
                            'expected functions verifies them.',
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Program|Key|Assign|Not Assigned'"],
             'confidence': 0.3,
             'explanation': "Step describes an OXE configuration action (setting program keys 123 and 124 to 'Not "
                            "Assigned'), which is a provisioning/configuration task, not a direct phone UI interaction "
                            'via SSH. The expected result is an XML configuration snippet, not a screen state. The '
                            "best possible automation is to check if the phone's display is in a programming or "
                            'settings menu, but this is a weak match.',
             'automation': 'needs_context'},
            {'step': 'Phone Enter the hard keys menu:\n'
                     'User/Device/Hard keys\n'
                     'or long press the F1/F2/F3/Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.8,
             'explanation': 'Step instructs to navigate to the Hard keys menu via User/Device/Hard keys. Using the '
                            'MENU key and touch screen clicks is the most direct and reliable method.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_35_Hard_Key_OXE_Define_Two_Lock_Hard_Key',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124, \nand Lock" parameter is enable"',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,1" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,1" override="true"/>',
             'intent': 'program_key_configuration',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Settings"',
                                    'key ts "Programmable Keys"',
                                    'key ts "Key 123"',
                                    'key ts "Lock"'],
             'confidence': 0.7,
             'explanation': 'Step describes programming keys 123 and 124 with Lock enabled. Commands navigate to '
                            'programmable key settings via menu. Exact menu labels may vary, requiring screen '
                            'verification.',
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only the defined key displays the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the hard keys menu via the main menu and touch screen selections.',
             'automation': 'automatable'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only the defined key displays the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long', 'key sim SOFTK1 long', 'key sim SOFTK2 long'],
             'confidence': 0.9,
             'explanation': 'The step requires long-pressing programmable softkeys (F1/F2/F3). SOFTK0-2 correspond to '
                            'these keys. For ALE-500, the shape keys (Triangle/Circle/Square) are also programmable '
                            'softkeys, typically mapped to the same SOFTK0-2. Executing all three covers the device '
                            'variants.',
             'automation': 'automatable'},
            {'step': 'check the function of the two keys',
             'expected': 'the function is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Lock|Key'"],
             'confidence': 0.7,
             'explanation': "The step is vague but likely requires verifying the phone's display or menu shows the "
                            'correct function/label for the two lock hard keys. Using screen_dump to check for '
                            'relevant text is the best automated approach.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_36_Hard_Key_OXE_Define_One_Lock_Hard_Key_Update',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nonly define one of progkey 123 or 124\nand Lock" parameter is enabled"',
             'expected': '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>',
             'intent': 'configuration_verification',
             'suggested_commands': ["screen_dump | grep -E 'progkey|123|124|Lock'",
                                    "screen_dump softkey | grep -E 'OK|Save|Confirm'"],
             'confidence': 0.3,
             'explanation': 'Step describes OXE configuration via user programming to define a locked hard key. This '
                            'is a network/configuration action, not directly executable via phone SSH key simulation. '
                            'Commands check if the phone display shows relevant programming/key lock status.',
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate through menu hierarchy using touch screen for direct selection',
             'automation': 'automatable'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long', 'key sim SOFTK1 long', 'key sim SOFTK2 long'],
             'confidence': 0.9,
             'explanation': 'The step requires long pressing F1/F2/F3 softkeys. SOFTK0-2 correspond to F1-F3. Multiple '
                            'commands cover different phone models.',
             'automation': 'automatable'},
            {'step': 'check the function of the defined key',
             'expected': 'the function is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Lock|Key|Function'"],
             'confidence': 0.7,
             'explanation': 'The step is to check the function of a defined hard key. Since the exact key and expected '
                            'function are not specified, the safest approach is to verify the display shows relevant '
                            "status (e.g., 'Lock', 'Key', 'Function') after pressing the key, assuming it triggers an "
                            'on-screen confirmation.',
             'automation': 'automatable'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     '\n'
                     'selectone undefined key then press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'navigate_and_select',
             'suggested_commands': ['key sim MENU',
                                    'key ts "User" || key ts "Device"',
                                    'key ts "Hard keys"',
                                    'screen_dump | grep -E "undefined|empty|program"',
                                    'key ts "undefined" || key ts "empty" || key ts "program"',
                                    'key ts "\\+" || key ts "add" || key ts "Add"'],
             'confidence': 0.8,
             'explanation': 'Navigate to Hard Keys menu via MENU > User/Device > Hard keys, find undefined key, press '
                            '+ button. Using regex patterns for flexibility.',
             'automation': 'automatable'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'And the reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'navigate_and_verify',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Hard Keys"',
                                    "screen_dump | grep -E 'Hard Keys|Key Type'",
                                    'key ts "Key Type"',
                                    "screen_dump | grep -E 'selected|default|icon'"],
             'confidence': 0.8,
             'explanation': 'Step requires navigating to hard keys menu, selecting a key type, and verifying display '
                            'elements. Commands open menu, navigate via touch, and verify screen content.',
             'automation': 'automatable'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'No valid response from LLM',
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'lock.*unlocked|unlocked.*lock'",
                                    "screen_dump | grep -E 'key.*defined|defined.*key'"],
             'confidence': 0.7,
             'explanation': 'Step requires checking if a defined key (likely a programmable softkey) shows correct '
                            'content and its lock parameter is unlocked. Using screen_dump with grep to verify the '
                            'display text.',
             'automation': 'automatable'},
            {'step': 'Repeat steps 5-8',
             'expected': '',
             'intent': 'needs_context',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "The step 'Repeat steps 5-8' is a meta-instruction that refers to other steps not provided "
                            'in this context. Without knowing what steps 5-8 are, no specific SSH commands can be '
                            'generated.',
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_37_Hard_Key_OXE_Define_One_Lock_Hard_Key_One_Unlock_Hard_Key_Modify',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124,\none key is locked and one key is unlocked',
             'expected': 'lock key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>\n'
                         'unlocked key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'configure_program_key',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'This step describes a configuration action on the OXE (OmniPCX Enterprise) system to set '
                            'program keys 123 and 124 with lock/unlock statuses. This is a server-side provisioning '
                            'task, not a direct phone UI interaction via SSH. It cannot be automated using the '
                            'provided SSH commands for the phone.',
             'automation': 'manual'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the Hard Keys menu via the main menu and touch screen selections.',
             'automation': 'automatable'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['screen_dump', 'key sim SOFTK0 long', 'key sim SOFTK1 long', 'key sim SOFTK2 long'],
             'confidence': 0.8,
             'explanation': 'Step requires long press of programmable keys (F1/F2/F3 or Triangle/Circle/Square). '
                            'SOFTK0-2 map to these keys. Screen dump first to confirm context.',
             'automation': 'automatable'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     '\n'
                     'Select  the defined key which is unlocked and press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.8,
             'explanation': 'Navigating through menu structure to reach Hard keys menu as described in first method',
             'automation': 'automatable'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU',
                                    "screen_dump | grep -i 'hard.*key' || screen_dump | grep -i 'program'",
                                    'key ts "Hard Key" || key ts "Program"'],
             'confidence': 0.8,
             'explanation': 'First access the main menu, then search for hard key/program menu entry and select it via '
                            'touch screen.',
             'automation': 'automatable'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'lock'",
                                    "screen_dump | grep -i 'unlock'",
                                    "screen_dump | grep -i 'function'"],
             'confidence': 0.7,
             'explanation': 'Step is to check the new function of a hard key. Since the specific hard key is not '
                            "defined, the most direct verification is to check the phone's display for any text "
                            "related to 'lock', 'unlock', or 'function' after pressing the key. This assumes the "
                            "function's status or label is shown on screen.",
             'automation': 'automatable'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'lock'",
                                    "screen_dump | grep -i 'unlock'",
                                    "screen_dump | grep -i 'key'"],
             'confidence': 0.7,
             'explanation': 'Need to verify OXE key definition and lock parameter status on display. Using grep for '
                            'lock/unlock/key terms to check content.',
             'automation': 'automatable'},
            {'step': 'Repeat steps 4-7',
             'expected': '',
             'intent': 'repeat_previous_steps',
             'suggested_commands': [],
             'confidence': 0.1,
             'explanation': 'Step instructs to repeat previous steps 4-7, but those steps are not provided in the '
                            'context. Cannot generate specific SSH commands without knowing what steps 4-7 are.',
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_38_Hard_Key_OXE_Define_One_Lock_Hard_Key_One_Unlock_Hard_Key_Reset_To_Default',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124,\none key is locked and one key is unlocked',
             'expected': 'lock key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>\n'
                         'unlocked key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'program_key_setup',
             'suggested_commands': ['key sim MENU',
                                    "key ts 'Settings'",
                                    "key ts 'Programmable keys'",
                                    "key ts 'Key 123'",
                                    "key ts 'Lock'",
                                    "key ts 'Key 124'",
                                    "key ts 'Unlock'"],
             'confidence': 0.7,
             'explanation': 'Navigating to programmable key settings via menu to set key 123 as locked and key 124 as '
                            'unlocked. Exact menu labels may vary.',
             'automation': 'automatable'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate through menu hierarchy to reach Hard keys configuration menu',
             'automation': 'automatable'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long', 'key sim SOFTK1 long', 'key sim SOFTK2 long'],
             'confidence': 0.9,
             'explanation': 'Step instructs to long press F1/F2/F3 keys. On Alcatel-Lucent phones, these are typically '
                            'the programmable softkeys (SOFTK0, SOFTK1, SOFTK2). The command covers all models by '
                            'simulating long presses on the first three softkeys.',
             'automation': 'automatable'},
            {'step': 'Press the reset to default icon',
             'expected': 'The lock defined key: Not affected\nthe unlock defined key: return to the default',
             'intent': 'press_key',
             'suggested_commands': ['key sim HOME long'],
             'confidence': 0.7,
             'explanation': "The 'reset to default' function is often accessed via a long press of the HOME key, which "
                            'typically opens a settings or reset menu. Using touch screen is not specified.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_39_Hard_Key_OXE_Define_Two_Unlock_Hard_Key_Modify',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124,\nthe lock paramter are all disabled',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'program_key_setup',
             'suggested_commands': ['key sim MENU',
                                    "key ts 'Settings'",
                                    "key ts 'Programmable Keys'",
                                    "key ts 'Key 123'",
                                    "key ts 'Lock'",
                                    "key ts 'Disabled'",
                                    'key sim OK',
                                    'key sim EXIT',
                                    "key ts 'Key 124'",
                                    "key ts 'Lock'",
                                    "key ts 'Disabled'",
                                    'key sim OK',
                                    'key sim EXIT',
                                    'key sim EXIT'],
             'confidence': 0.7,
             'explanation': 'The step requires navigating to the programmable keys menu to set keys 123 and 124 with '
                            'lock parameters disabled. The exact menu path may vary by phone model and configuration, '
                            'but this sequence uses common menu navigation via touch screen where possible.',
             'automation': 'automatable'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the hard keys menu via the main menu and touch screen selections.',
             'automation': 'automatable'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long', 'key sim SOFTK1 long', 'key sim SOFTK2 long'],
             'confidence': 0.8,
             'explanation': 'The step instructs to long press F1/F2/F3 or Triangle/Circle/Square keys. On '
                            'Alcatel-Lucent phones, F1/F2/F3 are typically softkeys (SOFTK0, SOFTK1, SOFTK2). The '
                            'ALE-500 shape keys (Triangle, Circle, Square) are not standard SSH key names; they likely '
                            'map to ADDON keys or other programmable keys, but SOFTK commands are the safest generic '
                            "interpretation for F1/F2/F3. Since the exact model (ALE-30/300/400/500) isn't specified "
                            'in the command context, I provide commands for all three softkeys to cover the '
                            'ALE-300/400 case. The user must select the correct one based on their phone model.',
             'automation': 'automatable'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     'press the edit button of the defined key which is unlocked',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"', 'key ts "Edit" 1'],
             'confidence': 0.8,
             'explanation': 'Navigates to the hard keys menu via the main menu and selects the first edit button for '
                            'an unlocked key.',
             'automation': 'automatable'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'navigate_and_verify',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Hard Keys"',
                                    'screen_dump | grep -E "(Hard Keys|Key Type|Unlock)"'],
             'confidence': 0.8,
             'explanation': 'Navigate to Hard Keys menu and verify display shows relevant options for key type '
                            'selection',
             'automation': 'automatable'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'function'"],
             'confidence': 0.7,
             'explanation': "The step is vague but likely requires verifying the hard key's function via the display. "
                            'Using screen_dump to check for function-related text is a general approach.',
             'automation': 'automatable'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'OXE|Unlock|Unlocked'",
                                    "screen_dump softkey | grep -E 'Define|Modify'"],
             'confidence': 0.7,
             'explanation': 'Step requires checking if a key is defined and its content/lock parameter. Using '
                            'screen_dump to verify display text related to OXE, unlock status, and key '
                            'definition/modify options.',
             'automation': 'automatable'},
            {'step': 'Long press the unlocked hard key\nRepeat steps 4-7',
             'expected': '',
             'intent': 'press_key',
             'suggested_commands': ['key sim ADDON0 long'],
             'confidence': 0.8,
             'explanation': "Assuming 'unlocked hard key' refers to an addon key (ADDON0-3) since it's a hard key that "
                            'can be programmed. Using ADDON0 as default.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_40_Hard_Key_OXE_Define_Two_Unlock_Hard_Key_Reset_To_Default',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124,\nthe lock paramter are all disabled',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'configure_program_keys',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Settings"',
                                    'key ts "Programmable keys"',
                                    'key ts "Key 123"',
                                    'key ts "Lock"',
                                    'key ts "Disabled"',
                                    'key sim OK',
                                    'key sim EXIT',
                                    'key ts "Key 124"',
                                    'key ts "Lock"',
                                    'key ts "Disabled"',
                                    'key sim OK',
                                    'key sim EXIT',
                                    'key sim EXIT'],
             'confidence': 0.7,
             'explanation': 'The step requires navigating to the programmable keys menu to set keys 123 and 124 with '
                            'lock parameters disabled. The exact menu path may vary by phone model, but this sequence '
                            'uses common menu navigation via touch screen where possible.',
             'automation': 'automatable'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User"', 'key ts "Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the Hard keys menu via the main menu and touch screen selections.',
             'automation': 'automatable'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 long', 'key sim SOFTK1 long', 'key sim SOFTK2 long'],
             'confidence': 0.8,
             'explanation': 'The step requires long pressing programmable softkeys (F1/F2/F3 or '
                            "Triangle/Circle/Square). The SSH command 'key sim SOFTK0 long' corresponds to long press "
                            'of the first programmable key. Issuing commands for SOFTK0, SOFTK1, and SOFTK2 covers all '
                            'mentioned keys across the ALE models.',
             'automation': 'automatable'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'press_key',
             'suggested_commands': ['key ts "reset to default"'],
             'confidence': 0.9,
             'explanation': "Using touch screen to directly click the 'reset to default' icon is the most efficient "
                            'method',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_41_Hard_Key_Phone_Define_By_Hard_Key',
  'preconditions': '',
  'steps': [{'step': "OXE: Doesn't configure the hard keys \n"
                     '\n'
                     'ALE-30: long press the F1/F2\n'
                     'ALE-300/400: long press the F1/F2/F3\n'
                     'ALE-500: Long press the Triangle/Circle/Square key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Edit maximum 2 keys|reset to default.*grey|hold cap "
                                    'icon|On hold and transfer|Transfer|conference cap icon|Conference|Triangle cap '
                                    "icon|Back|Circle cap icon|Home|Square cap icon|Low power'"],
             'confidence': 0.8,
             'explanation': 'The step describes verifying specific UI elements after long-pressing hard keys. Since '
                            "the exact phone model isn't specified, the verification command searches for all possible "
                            'expected text patterns mentioned in the expected results.',
             'automation': 'automatable'},
            {'step': 'Define one key :\nSelect the undefined key and press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'press_key',
             'suggested_commands': ['key ts "\\+\\s*button"', "screen_dump | grep -E 'key type|choice'"],
             'confidence': 0.8,
             'explanation': "The step requires selecting an undefined key and pressing a '+' button. Using touch "
                            "screen to click a '+' button is the most direct method. A screen dump is then used to "
                            'verify the key type choice screen appears with correct choices.',
             'automation': 'automatable'},
            {'step': 'select one key type then press the + button',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'menu_navigation_and_verification',
             'suggested_commands': ['key ts "\\+\\s*button"',
                                    "screen_dump | grep -E 'selected|define'",
                                    "screen_dump | grep 'reset to default'",
                                    "screen_dump | grep -E 'icon|hard key name'"],
             'confidence': 0.7,
             'explanation': "Step requires selecting a key type and pressing a '+' button, then verifying UI elements. "
                            "Using touch screen to click the '+' button is most direct. Screen verification commands "
                            "check for key selection, correct display, and the 'reset to default' icon. The 'long "
                            "press' verification is deferred as it requires context on which specific hard key to "
                            'press.',
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'function'", "screen_dump softkey | grep -i 'define'"],
             'confidence': 0.3,
             'explanation': "Step is too vague - 'check the new function of the hard key' needs more context about "
                            'which hard key and what to verify. Generic screen checks for function-related text.',
             'automation': 'needs_context'},
            {'step': 'Repeat steps 2-4',
             'expected': 'These two keys are selected and the edit icon is displayed on the right\n'
                         'And the two hard key names are light',
             'intent': 'needs_context',
             'suggested_commands': [],
             'confidence': 0.1,
             'explanation': "The step 'Repeat steps 2-4' is a procedural instruction that depends entirely on the "
                            'context of steps 2-4, which are not provided. No specific SSH command can be generated '
                            'without knowing the actions of those steps.',
             'automation': 'needs_context'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'press_key',
             'suggested_commands': ['key sim ADDON0'],
             'confidence': 0.8,
             'explanation': 'The test involves pressing a remaining key (likely ADDON0) after two keys are already '
                            'defined, expecting an error message about exceeding the limit.',
             'automation': 'automatable'},
            {'step': 'ALE-300/400:\nPress the i icon',
             'expected': 'display the help screen: change the physical button',
             'intent': 'press_key',
             'suggested_commands': ['key sim HELP'],
             'confidence': 0.9,
             'explanation': "The 'i icon' is the standard help key on Alcatel-Lucent phones, mapped to the HELP hard "
                            'key.',
             'automation': 'automatable'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'first defined hard key: is the key 123 on OXE side\n'
                         'second defined hard key: is the key 124 on OXE side\n'
                         'and parameter of the lock: disabled',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E '123|124'", "screen_dump | grep -i 'lock.*disabled'"],
             'confidence': 0.4,
             'explanation': "The step requires checking the phone's display for OXE-defined hard key assignments (123, "
                            '124) and lock parameter status. However, the exact menu location or display format is '
                            'unknown. The commands attempt to grep for the key numbers and lock status from the screen '
                            'dump, but success depends on the current screen context.',
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_42_Hard_Key_Phone_Define_By_Menu',
  'preconditions': '',
  'steps': [{'step': "OXE: Doesn't configure the hard keys \n\nEnter the hard keys menu:\nUser/Device/Hard keys",
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low power',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', "key ts 'User'", "key ts 'Device'", "key ts 'Hard keys'"],
             'confidence': 0.9,
             'explanation': "Navigate to the Hard Keys menu via the phone's menu structure (User -> Device -> Hard "
                            'keys).',
             'automation': 'automatable'},
            {'step': 'press one key whitch not defined then press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0', 'key sim ADDON0'],
             'confidence': 0.7,
             'explanation': "Press an undefined softkey (SOFTK0) or addon key (ADDON0), then press the '+' button "
                            '(ADDON0). Using two different undefined keys provides better test coverage.',
             'automation': 'automatable'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'menu_navigation_and_verification',
             'suggested_commands': ['key sim MENU',
                                    "screen_dump | grep -E 'Hard.*Key|Key.*Type'",
                                    "key ts 'Hard Key' || key ts 'Key Type'",
                                    "screen_dump | grep -E 'selected|default'"],
             'confidence': 0.8,
             'explanation': 'Navigate to Hard Key menu via MENU, verify display, select a key type, and check for '
                            'selection and reset icon.',
             'automation': 'automatable'},
            {'step': 'check the new function of the hard key',
             'expected': 'he fucntion is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'function'"],
             'confidence': 0.3,
             'explanation': "Step is vague. 'Check the new function of the hard key' likely requires verifying a menu "
                            "or screen. Using screen_dump to search for 'function' is a generic starting point.",
             'automation': 'needs_context'},
            {'step': 'Repeat steps 2-4',
             'expected': 'These two keys are selected and the edit icon is displayed on the right\n'
                         'And the two hard key names are light',
             'intent': 'needs_context',
             'suggested_commands': [],
             'confidence': 0.1,
             'explanation': 'Step references previous steps (2-4) which are not provided. Cannot generate specific SSH '
                            'commands without knowing the exact actions for selecting keys and verifying the edit icon '
                            'and key name highlights.',
             'automation': 'needs_context'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0',
                                    'key sim SOFTK1',
                                    'key sim SOFTK2',
                                    'key sim SOFTK3',
                                    'key sim SOFTK4'],
             'confidence': 0.7,
             'explanation': "The step mentions pressing 'the remaining key' in a context about defining hard keys by "
                            'menu. This likely refers to pressing one of the programmable softkeys (SOFTK0-4) after '
                            'others are already assigned. Testing multiple softkeys covers different scenarios.',
             'automation': 'automatable'},
            {'step': 'ALE-300/400:\nPress the i icon',
             'expected': 'display the help screen: change the physical button',
             'intent': 'press_key',
             'suggested_commands': ['key sim HELP'],
             'confidence': 0.9,
             'explanation': "The 'i icon' is the standard help key on Alcatel-Lucent phones, mapped to the HELP hard "
                            'key.',
             'automation': 'automatable'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'first defined hard key: is the key 123 on OXE side\n'
                         'second defined hard key: is the key 124 on OXE side\n'
                         'and parameter of the lock: disabled',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E '123|124'", "screen_dump | grep -i 'lock.*disabled'"],
             'confidence': 0.6,
             'explanation': "The step requires checking the phone's display for defined hard keys (123, 124) and lock "
                            'parameter status. Using screen_dump with grep is the best way to verify this information '
                            "on the phone's UI, though the exact menu location is not specified.",
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_43_Hard_Key_Phone_Define_Update_By_Long_Press_Hard_Key',
  'preconditions': '',
  'steps': [{'step': 'Phone configure 2 hard keys  \nLong press the defined hard key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim ADDON0 long'],
             'confidence': 0.7,
             'explanation': 'Step requires long press of a defined hard key. Assuming the first programmable hard key '
                            '(ADDON0) is one of the two configured keys. Exact key mapping (ADDON0-3) depends on '
                            'physical phone model and configuration.',
             'automation': 'automatable'},
            {'step': 'Select the defined key\nDefine the two keys to another function',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'hard_key_configuration',
             'suggested_commands': ['key sim MENU',
                                    "screen_dump | grep -i 'hard key\\|programmable\\|function'",
                                    "key ts 'Hard Key' || key ts 'Programmable Key' || key ts 'Function Key'",
                                    "screen_dump | grep -E 'Key [0-9]|SOFTK[0-9]|ADDON[0-3]'",
                                    "for i in $(seq 0 2); do key ts 'Key $i' && sleep 1 && key sim MENU && sleep 1; "
                                    'done'],
             'confidence': 0.7,
             'explanation': 'Navigate to hard key menu, verify display, select keys, and test long press '
                            'functionality. Using loops to test multiple keys efficiently.',
             'automation': 'automatable'},
            {'step': 'check the new function of the key',
             'expected': 'the fucntion is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'function'"],
             'confidence': 0.4,
             'explanation': "Step is vague; 'check the new function' likely requires verifying the screen shows the "
                            'correct function name or status after a long press. Using screen_dump to search for '
                            "'function' is a generic check.",
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'Phone sends the notify to the OXE\nthe progkey 123 and 124 of the OXE: the content is update',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E '123|124'", "screen_dump softkey | grep -E '123|124'"],
             'confidence': 0.4,
             'explanation': "Step is ambiguous. 'Check the two keys of the OXE' likely means verifying the phone's "
                            'display or softkey labels for program keys 123 and 124 have updated after a notification. '
                            'Using screen_dump to search for those numbers is the best automated check.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_44_Hard_Key_Phone_Define_Reset_To_Default_By_Long_Press_Hard_Key',
  'preconditions': '',
  'steps': [{'step': 'Phone configure 2 hard keys\nLong press the hard key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim ADDON0 long'],
             'confidence': 0.7,
             'explanation': "The step requires a long press on a configured hard key. The 'ADDON0' command simulates "
                            'pressing the first programmable hard key (e.g., a side key). The exact key (ADDON0-3) '
                            'depends on phone model and configuration context, but ADDON0 is the most common default '
                            'for the first hard key.',
             'automation': 'automatable'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'press_key',
             'suggested_commands': ['key sim HOME long'],
             'confidence': 0.8,
             'explanation': "The 'reset to default icon' is typically accessed via a long press of the HOME key on "
                            'many Alcatel-Lucent VoIP phones to reset programmable keys to default.',
             'automation': 'automatable'},
            {'step': 'Check the function of the key to its default state',
             'expected': 'ALE-30:\n'
                         'F1/hold and F2/transfer\n'
                         'ALE-300/400:\n'
                         'F1/hold and F2/transfer and F3/conference\n'
                         'ALE-500:\n'
                         'Triangle/back and Circle/home and Square/low power',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'F1.*hold.*F2.*transfer'",
                                    "screen_dump | grep -E 'Triangle.*back.*Circle.*home.*Square.*low power'"],
             'confidence': 0.7,
             'explanation': 'The step requires checking the default state of programmable keys. The expected result '
                            'lists configurations for different phone models (ALE-30, ALE-300/400, ALE-500). Since the '
                            'specific phone model under test is not provided, the commands verify the display for key '
                            'labels matching the described default states. This is an approximation; the exact '
                            'verification may depend on the phone model and screen context.',
             'automation': 'automatable'},
            {'step': 'check the two keys of the OXE',
             'expected': 'the program key 123 and 124 is not defined',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Program Key 123|Program Key 124'"],
             'confidence': 0.7,
             'explanation': 'The step requires checking if program keys 123 and 124 are not defined. The most direct '
                            "method is to verify the phone's display for any labels or indicators showing these keys "
                            'are defined. Using screen_dump with grep checks for their presence.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_45_Hard_Key_Phone_Define_Update_By_Menu',
  'preconditions': '',
  'steps': [{'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to hard keys menu via menu button and touch screen selections',
             'automation': 'automatable'},
            {'step': 'Select the defined key\nDefine the two keys to another function',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'hard_key_configuration',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Settings"',
                                    'key ts "Hard Keys"',
                                    'key ts "Key.*" 1',
                                    'key ts "Define"'],
             'confidence': 0.8,
             'explanation': 'Navigate to hard key settings menu and select first key for redefinition',
             'automation': 'automatable'},
            {'step': 'check the new function of the key',
             'expected': 'the fucntion is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'function'"],
             'confidence': 0.3,
             'explanation': "Step is vague. 'Check the new function of the key' likely means verifying the key's "
                            'assigned function is displayed or active. A screen dump to look for related text is a '
                            'generic starting point.',
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'Phone sends the notify to the OXE\nthe progkey 123 and 124 of the OXE: the content is update',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E '123|124'", "screen_dump softkey | grep -E '123|124'"],
             'confidence': 0.4,
             'explanation': "The step is ambiguous. 'Check the two keys of the OXE' likely means verifying the phone's "
                            'display shows updated program key labels (123 and 124) after a notify. Using screen_dump '
                            'to search for these numbers is the best automated check.',
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_46_Hard_Key_Phone_Define_Reset_To_Default_By_Menu',
  'preconditions': '',
  'steps': [{'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to Hard keys menu via menu key and touch screen for direct selection',
             'automation': 'automatable'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'press_key',
             'suggested_commands': ['key ts "Reset to default"'],
             'confidence': 0.9,
             'explanation': "The step requires pressing a 'reset to default icon' which is best accessed via touch "
                            'screen using pattern matching for the label.',
             'automation': 'automatable'},
            {'step': 'Check the function of the key to its default state',
             'expected': 'ALE-30:\n'
                         'two options: F1/hold and F2/transfer\n'
                         'ALE-300/400:\n'
                         'F1/hold and F2/transfer and F3/conference\n'
                         'ALE-500:\n'
                         'three options:Triangle/back and Circle/home and Square/low power',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'F1.*hold.*F2.*transfer'",
                                    "screen_dump | grep -E 'F3.*conference'",
                                    "screen_dump | grep -E 'Triangle.*back.*Circle.*home.*Square.*low power'"],
             'confidence': 0.8,
             'explanation': 'The step requires checking the default state of programmable keys. The expected result '
                            'lists different configurations for ALE-30, ALE-300/400, and ALE-500 models. The commands '
                            'verify the presence of the described labels on the screen. Since the exact model is not '
                            'specified, multiple checks are provided.',
             'automation': 'automatable'},
            {'step': 'check the two keys of the OXE',
             'expected': 'the program key 123 and 124 is not deffned',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E '123|124'", "screen_dump softkey | grep -E '123|124'"],
             'confidence': 0.7,
             'explanation': 'Checking if program keys 123 and 124 are displayed on screen or softkey area to verify '
                            'they are not defined',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_47_Hard_Key_Defined_Default_Funtcion',
  'preconditions': '',
  'steps': [{'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_to_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the Hard keys menu via the main menu and touch screen selections.',
             'automation': 'automatable'},
            {'step': 'Select the defined key\nDefine the two keys to default function',
             'expected': 'The two hard keys are selected and hard key name is light\n'
                         'cap icon:\n'
                         'ALE-30 :hold/transfer\n'
                         'ALE-300/400: hold/transfer/conference\n'
                         'ALE-500: Triangle/Circle/Square',
             'intent': 'hard_key_configuration',
             'suggested_commands': ['key sim MENU',
                                    'key ts "Settings"',
                                    'key ts "Hard Keys"',
                                    'screen_dump | grep -E "hold/transfer|conference|Triangle|Circle|Square"'],
             'confidence': 0.8,
             'explanation': 'Navigate to hard key settings menu to verify default function assignments. The exact menu '
                            'path may vary by model, but Settings → Hard Keys is typical. Screen verification checks '
                            'for expected function names.',
             'automation': 'automatable'},
            {'step': 'Press the hard key',
             'expected': 'The function is the default',
             'intent': 'press_key',
             'suggested_commands': ['key sim HOME'],
             'confidence': 0.3,
             'explanation': "The step 'Press the hard key' is ambiguous; 'HOME' is a common hard key for default "
                            'functions, but context is missing.',
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_48_Hard_Key_Defined_Unselected',
  'preconditions': '',
  'steps': [{'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'navigate_menu',
             'suggested_commands': ['key sim MENU', 'key ts "User/Device"', 'key ts "Hard keys"'],
             'confidence': 0.9,
             'explanation': 'Navigate to the Hard keys menu via the main menu and touch screen selections.',
             'automation': 'automatable'},
            {'step': 'Unselected the two defined keys',
             'expected': 'The two keys ard not selected and hard key name is grey',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0', 'key sim SOFTK1'],
             'confidence': 0.8,
             'explanation': 'Assuming the two defined keys are softkeys (SOFTK0 and SOFTK1), pressing them toggles '
                            'selection. Pressing each once should unselect them if they were previously selected.',
             'automation': 'automatable'},
            {'step': 'Press the two hard keys',
             'expected': 'The function is the default',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0; key sim SOFTK1'],
             'confidence': 0.9,
             'explanation': "The test title 'Hard_Key_Defined_Unselected' and step 'Press the two hard keys' refer to "
                            'the two programmable softkeys (SOFTK0 and SOFTK1) on the phone. The command simulates '
                            'pressing both.',
             'automation': 'automatable'},
            {'step': 'Select the two leys again',
             'expected': 'The two keys ard selected and hard key name is light',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0; key sim SOFTK1'],
             'confidence': 0.7,
             'explanation': "Assuming 'two leys' refers to two softkeys (SOFTK0 and SOFTK1) based on the test case "
                            'title mentioning hard keys and selection state. The command presses both softkeys to '
                            'select them.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_49_Hard_Key_Defined_Cap_Icon_Function',
  'preconditions': '',
  'steps': [{'step': 'When the hard key is not defined\ncheck the cap icon',
             'expected': 'ALE-30/300/400:\n'
                         'Hold cap icon\n'
                         'Transfer cap icon\n'
                         'Conference cap icon\n'
                         'ALE-500:\n'
                         'Triangle cap icon\n'
                         'Circle cap icon\n'
                         'Square cap icon',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Hold|Transfer|Conference|Triangle|Circle|Square'"],
             'confidence': 0.7,
             'explanation': 'The step requires checking the display for specific cap icons. The expected result lists '
                            'icons for different phone models. The command uses grep to search for any of the '
                            'mentioned icon names on the screen.',
             'automation': 'automatable'},
            {'step': 'Define the key to phone number/Immediate forward/Deactivate forward"Welcome '
                     'desk/Operator/Voicemail/"Redial/ Last caller/Cleaning mode/Meet me/Guard/Do not '
                     'disturb/Lock/Auto answer/Hunting group\n'
                     '\n'
                     'check the cap icon and function',
             'expected': 'ALE-30/300/400:F1/F2/abc cap icon\n'
                         'ALE-500: Triangle/Circle/Square Cap icon\n'
                         '\n'
                         'The function of the key is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'F1|F2|abc|Triangle|Circle|Square'"],
             'confidence': 0.7,
             'explanation': 'Step requires checking the cap icon (F1/F2/abc for ALE-30/300/400 or '
                            "Triangle/Circle/Square for ALE-500) and verifying the key's function is correct. The "
                            'screen dump command can capture the display to check for these icons.',
             'automation': 'automatable'},
            {'step': 'Define the key to Hold/Transfer/Conference\ncheck the cap icon and function',
             'expected': 'ALE-30/300/400: Hold/Transfer/Conference cap icon\n'
                         'ALE-500:\n'
                         'Triangle/Circle/Square cap icon\n'
                         'Press the hard key:\n'
                         'the function of the key is correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -E 'Hold|Transfer|Conference|Call'"],
             'confidence': 0.6,
             'explanation': 'After pressing the key, need to verify the function executed correctly (e.g., call held, '
                            'transfer initiated, conference started). A screen dump check for related UI text is the '
                            'best automated verification.',
             'automation': 'automatable'},
            {'step': 'Define the key to Emergency\ncheck the cap icon and function',
             'expected': 'ALE-30/300/400: Red cap icon\n'
                         'ALE-500:\n'
                         'Triangle/Circle/Square cap icon, and the font color of the dashboard is red\n'
                         'Press the hard key:\n'
                         'Will makes the outgoing call to Emergency',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'No valid response from LLM',
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_50_Hard_Key_Reset',
  'preconditions': '',
  'steps': [{'step': 'There are 2 defined hard keys.\n'
                     '\n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'press_key_and_verify',
             'suggested_commands': ['key sim SOFTK0',
                                    "screen_dump | grep -E 'Menu|Function'",
                                    'key sim EXIT',
                                    'key sim SOFTK0 long',
                                    "screen_dump | grep -E 'Menu|Function'"],
             'confidence': 0.8,
             'explanation': 'Assumes first defined hard key is SOFTK0. Short press, verify menu/function, exit, then '
                            'long press and verify again.',
             'automation': 'automatable'},
            {'step': 'Restart the phone \nthen\nShort/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'hard_key_test',
             'suggested_commands': ['key sim HOME',
                                    'key sim HOME long',
                                    "screen_dump | grep -E 'Menu|Settings|Options'"],
             'confidence': 0.7,
             'explanation': 'The step requires restarting the phone (assumed done), then testing a hard key with short '
                            'and long press, and verifying the menu display. Since the specific hard key is not '
                            'defined, HOME is used as a common example. A short press simulates normal function, a '
                            'long press should enter a menu, and screen_dump verifies the menu is displayed correctly.',
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_51_Hard_Key_Reset_To_Factory',
  'preconditions': '',
  'steps': [{'step': 'There are 1 defined hard keys. \n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'press_key_and_verify',
             'suggested_commands': ['key sim SOFTK0',
                                    "screen_dump | grep -E 'Menu|Function'",
                                    'key sim SOFTK0 long',
                                    "screen_dump | grep -E 'Menu|Function'"],
             'confidence': 0.7,
             'explanation': "Assuming the 'defined hard key' is a programmable softkey (SOFTK0). Short press, verify "
                            'normal function via screen. Long press, verify menu display.',
             'automation': 'automatable'},
            {'step': 'Phone reset flash, then the phone connects the OXE again\n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'These hard keys will not affected:\n'
                         '\n'
                         'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'verify_display',
             'suggested_commands': ["screen_dump | grep -i 'menu'", "screen_dump softkey | grep -i 'OK'"],
             'confidence': 0.7,
             'explanation': "Step requires checking the hard key menu display after a reset. The 'screen_dump' "
                            'commands verify if a menu is present and if softkeys are correctly labeled, which aligns '
                            'with verifying the menu display and function.',
             'automation': 'automatable'},
            {'step': 'check the undefined key',
             'expected': 'Still the default function',
             'intent': 'verify_display',
             'suggested_commands': ['screen_dump'],
             'confidence': 0.3,
             'explanation': "Step is ambiguous ('check the undefined key'). The safest generic action is to capture "
                            "the current screen state to verify the phone's display and softkey labels, which may show "
                            'the default function of a key.',
             'automation': 'needs_context'}]}]

@pytest.mark.generated
@pytest.mark.parametrize('case', CASES, ids=[c['title'] for c in CASES])
def test_testrail_generated(case, ssh_session, step_mapping_rules):
    """Execute a TestRail test case against DUT via SSH when mappings exist."""
    title = case['title']
    pre = case.get('preconditions') or ''
    steps = case.get('steps') or []

    if pre:
        # Preconditions are usually informational; you can map them into setup actions if needed.
        pass

    any_automated = False
    for i, s in enumerate(steps, 1):
        step_text = (s.get('step') or '').strip()
        exp_text = (s.get('expected') or '').strip()
        cmds = []
        ai_cmds = s.get('suggested_commands') or []
        if isinstance(ai_cmds, str):
            ai_cmds = [ai_cmds]
        cmds.extend([c for c in ai_cmds if c])

        if not cmds:
            for rule in step_mapping_rules:
                pattern = rule.get('pattern')
                if pattern and __import__('re').search(pattern, step_text, flags=__import__('re').IGNORECASE):
                    rule_cmds = rule.get('commands', [])
                    if isinstance(rule_cmds, str):
                        rule_cmds = [rule_cmds]
                    cmds.extend([c for c in rule_cmds if c])

        if cmds:
            any_automated = True
            for cmd in cmds:
                result = ssh_session.exec(cmd)
                assert result.exit_code == 0, f'[{title}] step {i} failed: {cmd}\n{result.stdout}\n{result.stderr}'
        else:
            # No mapping: keep the step visible in output and mark as xfail (not silently passing).
            pytest.xfail(f'No SSH mapping for step {i}: {step_text} | expected: {exp_text}')

    if not any_automated:
        pytest.xfail(f'No steps automated for case: {title}')
