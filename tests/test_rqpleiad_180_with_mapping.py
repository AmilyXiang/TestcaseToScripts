from __future__ import annotations

import pprint
import pytest

# Auto-generated from TestRail export.
# Update step_mapping.yaml to map natural-language steps into SSH commands.

CASES = [{'title': 'RQPLEIAD_180_01_Create_Emergency_Program_Key',
  'preconditions': 'OXE: \nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""',
             'intent': 'Create an emergency program key on the phone or addon',
             'suggested_commands': ['Press the empty program key (short or long press)',
                                    'Verify the key type choice screen is displayed'],
             'confidence': 0.95,
             'explanation': "The step involves interacting with the phone's programmable key and verifying the "
                            'expected screen. The intent is clear from the title and step description.',
             'tags': ['emergency', 'programmable_key', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'Press Emergency call',
             'expected': 'Display the create key screen',
             'intent': 'Create an emergency program key',
             'suggested_commands': ['Navigate to SIP device management',
                                    'Configure emergency number',
                                    'Press Emergency call button'],
             'confidence': 0.95,
             'explanation': 'The step involves creating an emergency program key by pressing the emergency call '
                            'button, which should display the create key screen. The preconditions suggest prior '
                            'configuration in the SIP device management.',
             'tags': ['emergency_call', 'key_creation', 'SIP_device'],
             'automation': 'automatable'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly  (the phone and addon side)',
             'intent': 'Create an emergency program key on the VoIP phone',
             'suggested_commands': ['Press the create key button on the screen', 'Press the OK key on the phone'],
             'confidence': 0.95,
             'explanation': 'The step involves creating a program key for emergency purposes, which can be done by '
                            "interacting with the phone's interface or buttons.",
             'tags': ['emergency', 'program_key', 'UI_interaction'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_02_Create_Guard_Program_Key',
  'preconditions': 'OXE: \nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""',
             'intent': 'Create a programmable guard key',
             'suggested_commands': ['Press and hold the empty program key',
                                    'Verify the key type choice screen is displayed'],
             'confidence': 0.95,
             'explanation': "The step involves interacting with the phone's program key to initiate the creation of a "
                            'guard key and verifying the expected UI response.',
             'tags': ['UI', 'Programmable Key', 'Guard Key'],
             'automation': 'automatable'},
            {'step': 'Press Guard call',
             'expected': 'Display the create key screen',
             'intent': 'Access guard call creation screen',
             'suggested_commands': ['Press the Guard call button', 'Verify the create key screen is displayed'],
             'confidence': 0.9,
             'explanation': 'The step tests the functionality of the Guard call button and its ability to navigate to '
                            'the create key screen.',
             'tags': ['UI', 'Guard Call', 'Navigation'],
             'automation': 'automatable'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly (phone and addon side)',
             'intent': 'Finalize guard key creation',
             'suggested_commands': ['Press the create key button on the screen',
                                    'Press the OK key on the phone',
                                    'Verify the program key is created successfully and displayed correctly'],
             'confidence': 0.92,
             'explanation': 'The step ensures the guard key is created and displayed correctly on both the phone and '
                            'addon, validating the final output of the process.',
             'tags': ['UI', 'Programmable Key', 'Validation'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_03_Create_Operator_Program_Key',
  'preconditions': 'OXE: \nmgr---SIP device management---DM profile---Operator number---xxxx',
  'steps': [{'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""',
             'intent': 'Create a programmable operator key',
             'suggested_commands': ['Press the empty program key', 'Select key type from the displayed options'],
             'confidence': 0.95,
             'explanation': 'The step involves interacting with the phone or addon to initiate the creation of a '
                            'programmable key by pressing an empty key.',
             'tags': ['UI Interaction', 'Programmable Key', 'Operator'],
             'automation': 'automatable'},
            {'step': 'Press Operator call',
             'expected': 'Display the create key screen',
             'intent': 'Initiate operator call key creation',
             'suggested_commands': ["Press the 'Operator call' button"],
             'confidence': 0.9,
             'explanation': "The step specifies pressing the 'Operator call' button to proceed with creating a key.",
             'tags': ['UI Interaction', 'Operator Call', 'Programmable Key'],
             'automation': 'automatable'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly (phone and addon side)',
             'intent': 'Finalize programmable key creation',
             'suggested_commands': ["Press the 'Create Key' button", "Press the 'OK' key on the phone"],
             'confidence': 0.92,
             'explanation': 'The step involves confirming the creation of the programmable key and verifying its '
                            'display on the phone and addon.',
             'tags': ['UI Interaction', 'Confirmation', 'Programmable Key'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_04_Emergency_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Emergency program key',
  'steps': [{'step': 'Press the Emergency program key of the phone or addon',
             'expected': 'title:  Outgoing call\n'
                         'Red background  \n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'Initiate an emergency outgoing call using the program key',
             'suggested_commands': ['Press Emergency program key', 'Verify call initiation and display elements'],
             'confidence': 0.95,
             'explanation': 'The step involves pressing the Emergency program key to initiate an outgoing call and '
                            'verifying the expected UI elements and behavior.',
             'tags': ['emergency_call', 'program_key', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title:  Conversation xx:xx\n'
                         'Red background  \n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify remote side answering the emergency call',
             'suggested_commands': ['Simulate remote side answering', 'Verify UI updates and button states'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of the phone when the remote side answers the emergency call, '
                            'including UI updates and button states.',
             'tags': ['emergency_call', 'remote_answer', 'UI_verification'],
             'automation': 'needs_context'},
            {'step': 'Press the emergency avatar',
             'expected': 'Display the emergency info',
             'intent': 'Access emergency information by pressing the emergency avatar',
             'suggested_commands': ['Press emergency avatar', 'Verify emergency info display'],
             'confidence': 0.92,
             'explanation': 'The step involves verifying that pressing the emergency avatar displays the emergency '
                            'information as expected.',
             'tags': ['emergency_call', 'avatar_interaction', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'Add a new call during an emergency call',
             'suggested_commands': ['Press new call button', 'Verify transition to add new call screen'],
             'confidence': 0.93,
             'explanation': 'The step tests the functionality of adding a new call during an emergency call by '
                            'pressing the new call button.',
             'tags': ['emergency_call', 'new_call', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'Verify hold functionality during an emergency call',
             'suggested_commands': ['Press hold key or button', 'Verify no action occurs'],
             'confidence': 0.88,
             'explanation': 'The step tests the behavior of the hold functionality during an emergency call, ensuring '
                            'no action occurs as expected.',
             'tags': ['emergency_call', 'hold_functionality', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'Switch audio to handset during emergency call',
             'suggested_commands': ['Pick up the handset'],
             'confidence': 0.95,
             'explanation': 'The step describes picking up the handset to switch the audio output to the handset '
                            'during an emergency call.',
             'tags': ['audio_switch', 'emergency_call', 'handset'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'Switch audio to handsfree during emergency call',
             'suggested_commands': ['Hang up the handset'],
             'confidence': 0.95,
             'explanation': 'The step describes hanging up the handset to switch the audio output to handsfree during '
                            'an emergency call.',
             'tags': ['audio_switch', 'emergency_call', 'handsfree'],
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'Attempt to release emergency call via release key',
             'suggested_commands': ['Press the release key or button'],
             'confidence': 0.9,
             'explanation': 'The step tests whether pressing the release key or button can terminate an emergency '
                            'call, which is expected to have no effect.',
             'tags': ['emergency_call', 'release_key', 'call_handling'],
             'automation': 'needs_context'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing arrow)\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify emergency call log details after call release',
             'suggested_commands': ['Check the call log for emergency call details'],
             'confidence': 0.9,
             'explanation': 'The step verifies that the emergency call log contains accurate details such as label, '
                            'avatar, name, number, and date after the call is released.',
             'tags': ['emergency_call', 'call_log', 'verification'],
             'automation': 'manual'}]},
 {'title': 'RQPLEIAD_180_05_Emergency_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Press the Emergency call log/ Emergency contact or dial the Emergency number',
             'expected': 'title: Outgoing call\n'
                         'Red background\n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'Verify emergency outgoing call behavior when initiated via call log, contact, or dial number.',
             'suggested_commands': ['Initiate emergency call via call log',
                                    'Verify UI elements during emergency call',
                                    'Press emergency avatar to view info screen',
                                    'Press release key to end call'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior of the phone when an emergency call is initiated '
                            'and ensuring the UI elements behave as expected.',
             'tags': ['emergency_call', 'UI_verification', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify UI and button behavior during an active emergency call when the remote side answers.',
             'suggested_commands': ['Answer emergency call on remote side',
                                    'Verify UI elements during active call',
                                    'Check button states (release, hold, new call)'],
             'confidence': 0.95,
             'explanation': 'The step focuses on verifying the UI and button states during an active emergency call '
                            'after the remote side answers.',
             'tags': ['emergency_call', 'UI_verification', 'button_behavior'],
             'automation': 'automatable'},
            {'step': 'Press the emergency avatar',
             'expected': 'Display the emergency info',
             'intent': 'Verify behavior when the emergency avatar is pressed during an emergency call.',
             'suggested_commands': ['Press emergency avatar during call', 'Verify emergency info screen is displayed'],
             'confidence': 0.9,
             'explanation': 'The step tests the functionality of the emergency avatar button and ensures it displays '
                            'the emergency info screen.',
             'tags': ['emergency_call', 'UI_verification', 'button_behavior'],
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'Verify behavior when the new call button is pressed during an emergency call.',
             'suggested_commands': ['Press new call button during emergency call',
                                    'Verify transition to add new call screen'],
             'confidence': 0.9,
             'explanation': 'The step ensures that pressing the new call button during an emergency call transitions '
                            'to the add new call screen.',
             'tags': ['emergency_call', 'UI_verification', 'button_behavior'],
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'Verify behavior when the hold key is pressed during an emergency call.',
             'suggested_commands': ['Press hold key during emergency call', 'Verify no action is performed'],
             'confidence': 0.9,
             'explanation': 'The step tests that the hold functionality is disabled during an emergency call and no '
                            'action is performed.',
             'tags': ['emergency_call', 'UI_verification', 'button_behavior'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'Switch audio to handset during emergency call',
             'suggested_commands': ['Pick up handset', 'Verify audio switches to handset'],
             'confidence': 0.95,
             'explanation': 'The step involves picking up the handset to ensure the audio switches correctly to the '
                            'handset during an emergency call.',
             'tags': ['audio', 'handset', 'emergency_call'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'Switch audio to handsfree during emergency call',
             'suggested_commands': ['Hang up handset', 'Verify audio switches to handsfree'],
             'confidence': 0.95,
             'explanation': 'The step involves hanging up the handset to ensure the audio switches correctly to '
                            'handsfree mode during an emergency call.',
             'tags': ['audio', 'handsfree', 'emergency_call'],
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'Prevent call release during emergency call',
             'suggested_commands': ['Press release key', 'Verify call cannot be released'],
             'confidence': 0.9,
             'explanation': 'The step tests that pressing the release key or button does not terminate the emergency '
                            'call, ensuring compliance with emergency call behavior.',
             'tags': ['call_release', 'emergency_call', 'validation'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing)\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify emergency call log details',
             'suggested_commands': ['Check call log after call release',
                                    'Verify emergency call details (label/avatar/name/number/date)'],
             'confidence': 0.9,
             'explanation': 'The step ensures that the emergency call log is correctly recorded and displays all '
                            'relevant details after the call is released.',
             'tags': ['call_log', 'emergency_call', 'verification'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_06_Emergency_Outgoing_Call_By_Dial_Hardcode_911/112',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Dial the 911 or 112',
             'expected': 'title: Outgoing call\n'
                         'Red background\n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'Verify emergency outgoing call behavior when dialing 911 or 112',
             'suggested_commands': ['Dial 911', 'Dial 112'],
             'confidence': 0.95,
             'explanation': "The step involves dialing emergency numbers and verifying the phone's behavior, such as "
                            'displaying a red background, emergency avatar, and release button functionality.',
             'tags': ['emergency_call', 'UI_verification', 'functional_test'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify behavior when the remote side answers an emergency call',
             'suggested_commands': ['Simulate remote side answering', 'Verify UI updates'],
             'confidence': 0.9,
             'explanation': "The step checks the phone's behavior when the remote side answers, including UI changes "
                            'such as red background and button states.',
             'tags': ['emergency_call', 'UI_verification', 'call_status'],
             'automation': 'automatable'},
            {'step': 'Press the emergency avatar',
             'expected': 'Display the  info: 911 or 112',
             'intent': 'Verify behavior when the emergency avatar is pressed',
             'suggested_commands': ['Press emergency avatar', 'Verify displayed information'],
             'confidence': 0.9,
             'explanation': 'The step involves pressing the emergency avatar and verifying that the correct '
                            'information (911 or 112) is displayed.',
             'tags': ['emergency_call', 'UI_interaction', 'functional_test'],
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'Verify behavior when the new call button is pressed during an emergency call',
             'suggested_commands': ['Press new call button', 'Verify transition to add new call screen'],
             'confidence': 0.85,
             'explanation': 'The step tests the functionality of the new call button during an emergency call and '
                            'ensures it transitions to the add new call screen.',
             'tags': ['emergency_call', 'UI_interaction', 'functional_test'],
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'Verify behavior when the hold button is pressed during an emergency call',
             'suggested_commands': ['Press hold button', 'Verify no action occurs'],
             'confidence': 0.9,
             'explanation': 'The step ensures that pressing the hold button during an emergency call does not perform '
                            'any action, as holding emergency calls is not allowed.',
             'tags': ['emergency_call', 'UI_interaction', 'negative_test'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'Switch voice to handset during emergency call',
             'suggested_commands': ['Pick up the handset to switch audio to handset mode'],
             'confidence': 0.95,
             'explanation': 'The step involves picking up the handset to change the audio output during an emergency '
                            'call.',
             'tags': ['audio', 'handset', 'emergency_call'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'Switch voice to handsfree during emergency call',
             'suggested_commands': ['Hang up the handset to switch audio to handsfree mode'],
             'confidence': 0.95,
             'explanation': 'The step involves hanging up the handset to change the audio output to handsfree mode '
                            'during an emergency call.',
             'tags': ['audio', 'handsfree', 'emergency_call'],
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'Attempt to release emergency call',
             'suggested_commands': ['Press the release key or physical button to attempt call release'],
             'confidence': 0.9,
             'explanation': 'The step tests whether pressing the release key or button can terminate an emergency '
                            'call, which is expected to fail.',
             'tags': ['call_release', 'emergency_call', 'button_action'],
             'automation': 'needs_context'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing )\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify emergency call log details',
             'suggested_commands': ['Check the call log for emergency call details after call release'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the emergency call log for correct details such as label, '
                            'avatar, name, number, and date.',
             'tags': ['call_log', 'emergency_call', 'verification'],
             'automation': 'manual'}]},
 {'title': 'RQPLEIAD_180_07_Emergency_Outgoing_Call_With_Second_Normal_Incoming_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify emergency outgoing call behavior',
             'suggested_commands': ['Make an emergency call',
                                    'Check UI for red background',
                                    'Verify emergency avatar is displayed',
                                    'Check button states'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior of the phone during an emergency call, including '
                            'UI elements and button states.',
             'tags': ['emergency_call', 'UI_verification', 'button_states'],
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the emergency call is  kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar  + Incoming call"+ switch button"',
             'intent': 'Verify behavior when receiving a normal incoming call during an emergency call',
             'suggested_commands': ['Receive a normal call during an emergency call',
                                    'Check if emergency call remains active',
                                    'Verify UI for new call details'],
             'confidence': 0.92,
             'explanation': 'The step tests the handling of a normal incoming call while an emergency call is active, '
                            'focusing on UI updates and call states.',
             'tags': ['incoming_call', 'emergency_call', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         'the emergency call is kept active\n'
                         'emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button',
             'intent': 'Verify behavior when switching between calls',
             'suggested_commands': ['Press the switch button',
                                    'Verify UI updates for call positions',
                                    'Check if emergency call remains active'],
             'confidence': 0.93,
             'explanation': 'The step involves testing the functionality of the switch button and ensuring the UI '
                            'reflects the correct call states.',
             'tags': ['call_switching', 'UI_verification', 'emergency_call'],
             'automation': 'automatable'},
            {'step': 'Answer the new call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and normal call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'Verify behavior when answering a new call during an emergency call',
             'suggested_commands': ['Answer the new call',
                                    'Verify conference call is established',
                                    'Check UI for conference details'],
             'confidence': 0.94,
             'explanation': "The step tests the phone's ability to handle a new call during an emergency call, "
                            'ensuring a conference call is created and UI updates correctly.',
             'tags': ['conference_call', 'UI_verification', 'emergency_call'],
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'Verify behavior when pressing the exit/release button during a call',
             'suggested_commands': ['Press the exit/release button', 'Verify no action occurs'],
             'confidence': 0.9,
             'explanation': 'The step ensures that pressing the exit/release button during a specific call state does '
                            'not trigger any unintended actions.',
             'tags': ['button_behavior', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Emergency call log and the normal incoming call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify call logs after conference call release',
             'suggested_commands': ['Check call log for conference call details',
                                    'Verify emergency call log details',
                                    'Check normal incoming call log details',
                                    'Ensure label/avatar/name/number/date are displayed correctly'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the presence and correctness of call logs for different types '
                            'of calls after a conference call is released. This includes emergency, normal incoming, '
                            'and conference call logs.',
             'tags': ['call_log_verification', 'conference_call', 'emergency_call', 'incoming_call'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_08_Emergency_Outgoing_Call_With_Second_Normal_Incoming_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify emergency outgoing call behavior',
             'suggested_commands': ['Initiate emergency call', 'Check UI elements during call'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior of the phone during an emergency call, including '
                            'UI elements and button states.',
             'tags': ['emergency_call', 'UI_verification', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the emergency call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'Verify behavior when a normal incoming call is received during an emergency call',
             'suggested_commands': ['Simulate incoming call during emergency call', 'Check UI for call details'],
             'confidence': 0.95,
             'explanation': 'The step tests how the phone handles a normal incoming call while an emergency call is '
                            'active, focusing on UI and call state.',
             'tags': ['incoming_call', 'emergency_call', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the emergency call is kept active\n'
                         'emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button',
             'intent': 'Verify switch functionality between calls',
             'suggested_commands': ['Press switch button', 'Verify call positions and UI updates'],
             'confidence': 0.9,
             'explanation': 'The step involves testing the switch button functionality and verifying the UI updates '
                            'for both calls.',
             'tags': ['call_switching', 'UI_verification', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'Press the silence button',
             'expected': 'Stop ringing',
             'intent': 'Verify silence button functionality during an incoming call',
             'suggested_commands': ['Press silence button', 'Verify ringing stops'],
             'confidence': 0.9,
             'explanation': 'The step tests the functionality of the silence button to ensure it stops the ringing of '
                            'an incoming call.',
             'tags': ['silence_button', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify reject/voicemail button functionality during an incoming call',
             'suggested_commands': ['Press reject/voicemail button',
                                    'Verify emergency call remains active and UI updates'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of the reject/voicemail button during an incoming call while '
                            'an emergency call is active, focusing on UI and call state.',
             'tags': ['reject_button', 'voicemail', 'emergency_call', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the not answered call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify call logs after an emergency outgoing call and a rejected incoming call.',
             'suggested_commands': ['Check emergency call log',
                                    'Check missed call log',
                                    'Verify label/avatar/name/number/date display'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the call logs and ensuring all relevant details are displayed '
                            'correctly after specific call scenarios.',
             'tags': ['call_log', 'emergency_call', 'missed_call', 'UI_verification'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_09_Emergency_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify emergency outgoing call behavior and UI during call establishment',
             'suggested_commands': ['Make an emergency call', 'Observe UI elements during the call'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior and UI elements when an emergency call is '
                            'established.',
             'tags': ['emergency_call', 'UI_verification', 'call_establishment'],
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
             'intent': 'Verify behavior and UI when making a normal outgoing call during an emergency call',
             'suggested_commands': ['Initiate a normal call during an emergency call',
                                    'Observe UI changes for both calls'],
             'confidence': 0.95,
             'explanation': 'The step involves checking the behavior and UI when a normal call is initiated during an '
                            'ongoing emergency call.',
             'tags': ['normal_call', 'emergency_call', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and normal call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'Verify conference call behavior and UI when remote side answers',
             'suggested_commands': ['Answer the call from the remote side', 'Verify conference call initiation and UI'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior and UI when a conference call is initiated after the remote '
                            'side answers.',
             'tags': ['conference_call', 'UI_verification', 'call_behavior'],
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'No anction',
             'intent': 'Verify behavior when pressing exit/release button during a conference call',
             'suggested_commands': ['Press the exit/release button during a conference call',
                                    'Observe system response'],
             'confidence': 0.85,
             'explanation': "The step checks the system's response when the exit/release button is pressed during a "
                            'conference call.',
             'tags': ['conference_call', 'button_behavior', 'UI_verification'],
             'automation': 'needs_context'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Emergency call loh and the normal outgoing call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify call log entries after a conference call is released',
             'suggested_commands': ['Release the conference call', 'Check call logs for all calls'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the call log entries for all calls after a conference call is '
                            'released.',
             'tags': ['call_logs', 'conference_call', 'UI_verification'],
             'automation': 'manual'}]},
 {'title': 'RQPLEIAD_180_10_Emergency_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify emergency outgoing call behavior and UI elements during the call.',
             'suggested_commands': ['Initiate emergency call',
                                    'Verify UI elements during the call',
                                    'Check button states'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior and UI elements of the phone during an emergency '
                            'call, including background color, avatar, and button states.',
             'tags': ['emergency_call', 'UI_verification', 'button_states'],
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
             'intent': 'Test behavior and UI elements when making a normal outgoing call during an emergency call.',
             'suggested_commands': ['Initiate normal outgoing call during emergency call',
                                    'Verify UI elements for both calls',
                                    'Check button states and call statuses'],
             'confidence': 0.95,
             'explanation': 'The step tests the behavior of the phone when a normal outgoing call is made during an '
                            'ongoing emergency call, focusing on UI elements and button states.',
             'tags': ['normal_call', 'emergency_call', 'UI_verification', 'call_status'],
             'automation': 'automatable'},
            {'step': 'Remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify behavior and UI elements when the remote side rejects the call.',
             'suggested_commands': ['Simulate remote side rejecting the call',
                                    'Verify UI elements after rejection',
                                    'Check button states post-rejection'],
             'confidence': 0.9,
             'explanation': "The step involves testing the phone's behavior and UI elements when the remote side "
                            'rejects the call, ensuring proper states and visuals.',
             'tags': ['call_rejection', 'UI_verification', 'button_states'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the unsuccessful call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify call log entries after emergency and unsuccessful calls.',
             'suggested_commands': ['Release the call',
                                    'Check call log for emergency and unsuccessful call entries',
                                    'Verify labels, avatars, and timestamps in call log'],
             'confidence': 0.9,
             'explanation': 'The step tests whether the call log correctly records both emergency and unsuccessful '
                            'calls, including proper display of labels, avatars, and timestamps.',
             'tags': ['call_log', 'emergency_call', 'unsuccessful_call', 'UI_verification'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_11_Guard_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Guard program key',
  'steps': [{'step': 'Press the Guard program key of the phone or addon',
             'expected': 'title: Outgoing call\n'
                         'Dark blue background\n'
                         'display Guard avatar and release button(led is on)\n'
                         'and press the Guard avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'Verify the behavior when the Guard program key is pressed during an outgoing call.',
             'suggested_commands': ['Press Guard program key',
                                    'Observe screen and LED behavior',
                                    'Interact with Guard avatar and release button'],
             'confidence': 0.95,
             'explanation': "The step involves verifying the phone's response to pressing the Guard program key, "
                            'including UI changes and button functionality.',
             'tags': ['UI', 'Functionality', 'Guard Key'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': "Verify the phone's behavior when the remote side answers the call.",
             'suggested_commands': ['Initiate call',
                                    'Wait for remote side to answer',
                                    'Observe screen and button states'],
             'confidence': 0.9,
             'explanation': "The step checks the phone's UI and button states after the remote side answers the call.",
             'tags': ['UI', 'Call Handling', 'Guard Key'],
             'automation': 'automatable'},
            {'step': 'Press the guard avatar',
             'expected': 'Display the guard info',
             'intent': 'Verify the behavior when the Guard avatar is pressed.',
             'suggested_commands': ['Press Guard avatar', 'Observe displayed information'],
             'confidence': 0.92,
             'explanation': "The step involves verifying the phone's response to pressing the Guard avatar, "
                            'specifically the display of guard information.',
             'tags': ['UI', 'Guard Key', 'Interaction'],
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'Verify the behavior when the new call button is pressed.',
             'suggested_commands': ['Press new call button', 'Observe transition to new call screen'],
             'confidence': 0.93,
             'explanation': "The step tests the phone's ability to transition to the add new call screen when the new "
                            'call button is pressed.',
             'tags': ['UI', 'Call Handling', 'New Call'],
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'Verify that the hold key does not perform any action during a Guard call.',
             'suggested_commands': ['Press hold key on screen',
                                    'Press physical hold button',
                                    'Verify no action occurs'],
             'confidence': 0.88,
             'explanation': 'The step ensures that the hold functionality is disabled during a Guard call, as '
                            'expected.',
             'tags': ['Functionality', 'Guard Key', 'Hold'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'Verify handset functionality during outgoing call with Guard program key',
             'suggested_commands': ['Pick up handset', 'Verify audio switches to handset'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the audio transition when the handset is picked up during a '
                            'call with Guard program key.',
             'tags': ['audio', 'handset', 'Guard program key'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'Verify handsfree functionality during outgoing call with Guard program key',
             'suggested_commands': ['Hang up handset', 'Verify audio switches to handsfree'],
             'confidence': 0.95,
             'explanation': 'The step checks if the audio transitions to handsfree mode when the handset is hung up '
                            'during a call with Guard program key.',
             'tags': ['audio', 'handsfree', 'Guard program key'],
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'Verify call cannot be released using release key during Guard program key usage',
             'suggested_commands': ['Press release key', 'Verify call remains active'],
             'confidence': 0.9,
             'explanation': 'The step ensures that the call cannot be released using the release key when the Guard '
                            'program key is active.',
             'tags': ['call control', 'release key', 'Guard program key'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log (outgoing)\nthe label /avatar /name /number/date display correctly',
             'intent': 'Verify call log details after releasing call with Guard program key',
             'suggested_commands': ['Release call', 'Check call log for Guard call details'],
             'confidence': 0.85,
             'explanation': 'The step verifies that the call log correctly displays details of the Guard outgoing call '
                            'after it has been released.',
             'tags': ['call log', 'Guard program key', 'UI verification'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_12_Guard_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Press the Guard call log/ Guard  contact or dial the Guard  number',
             'expected': 'title: Outgoing call\n'
                         'Dark blue background\n'
                         'display Guard avatar and release button(led is on)\n'
                         'and press the Guard avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'Verify outgoing call behavior when using Guard call log, contact, or dial number',
             'suggested_commands': ['Press Guard call log', 'Press Guard contact', 'Dial Guard number'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior of the phone when initiating an outgoing call '
                            'using specific Guard features.',
             'tags': ['outgoing_call', 'guard_feature', 'call_log', 'contact'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify call screen behavior when the remote side answers the call',
             'suggested_commands': ['Simulate remote side answering', 'Verify call screen updates'],
             'confidence': 0.9,
             'explanation': 'The step focuses on verifying the UI and button states when the remote side answers the '
                            'call.',
             'tags': ['call_screen', 'remote_answer', 'ui_verification'],
             'automation': 'automatable'},
            {'step': 'Press the guard avatar',
             'expected': 'Display the guard info',
             'intent': 'Verify behavior when pressing the Guard avatar',
             'suggested_commands': ['Press Guard avatar', 'Verify info screen display'],
             'confidence': 0.9,
             'explanation': 'The step tests the functionality of the Guard avatar button and its expected behavior.',
             'tags': ['guard_avatar', 'info_screen', 'ui_interaction'],
             'automation': 'automatable'},
            {'step': 'press the new call button',
             'expected': 'turn to the add new call screen',
             'intent': 'Verify behavior when pressing the new call button',
             'suggested_commands': ['Press new call button', 'Verify transition to add new call screen'],
             'confidence': 0.9,
             'explanation': 'The step checks the functionality of the new call button and its navigation behavior.',
             'tags': ['new_call', 'ui_navigation', 'button_functionality'],
             'automation': 'automatable'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call",
             'intent': 'Verify behavior when pressing the hold key during a Guard call',
             'suggested_commands': ['Press hold key on screen',
                                    'Press physical hold button',
                                    'Verify no action occurs'],
             'confidence': 0.85,
             'explanation': 'The step ensures that the hold functionality is disabled during a Guard call as expected.',
             'tags': ['hold_functionality', 'guard_call', 'button_verification'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'Switch audio to handset during a call',
             'suggested_commands': ['Lift handset', 'Verify audio switches to handset'],
             'confidence': 0.95,
             'explanation': 'The step involves picking up the handset to ensure the audio transitions from another '
                            'mode to the handset.',
             'tags': ['audio', 'handset', 'call'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset',
             'expected': 'the voice will switch to handsfree',
             'intent': 'Switch audio to handsfree during a call',
             'suggested_commands': ['Hang up handset', 'Verify audio switches to handsfree'],
             'confidence': 0.95,
             'explanation': 'The step involves hanging up the handset to ensure the audio transitions to handsfree '
                            'mode.',
             'tags': ['audio', 'handsfree', 'call'],
             'automation': 'automatable'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call",
             'intent': 'Prevent call release when using release key',
             'suggested_commands': ['Press release key', 'Verify call is not released'],
             'confidence': 0.9,
             'explanation': 'The step tests whether the release key is disabled for guarded calls, ensuring the call '
                            'cannot be released.',
             'tags': ['call release', 'guarded call', 'button'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log (outgoing)\nthe label /avatar /name /number/date display correctly',
             'intent': 'Verify call log details after releasing a call',
             'suggested_commands': ['Release call', 'Check call log for correct details'],
             'confidence': 0.9,
             'explanation': 'The step verifies that the call log accurately reflects the details of a released guarded '
                            'call.',
             'tags': ['call log', 'guarded call', 'verification'],
             'automation': 'manual'}]},
 {'title': 'RQPLEIAD_180_13_Guard_Ougoing_Call_With_Second_Normal_Incoming_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': "Verify the phone's behavior when establishing a call with the Guard.",
             'suggested_commands': ['Establish call with Guard', 'Verify UI elements (background, avatar, buttons)'],
             'confidence': 0.95,
             'explanation': 'The step describes initiating a call with the Guard and verifying the UI elements such as '
                            'background color, avatar, and button states.',
             'tags': ['call_establishment', 'UI_verification', 'Guard_call'],
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Guard call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': "Verify the phone's behavior when receiving a normal incoming call during an active Guard call.",
             'suggested_commands': ['Receive normal incoming call', 'Verify UI elements for both calls'],
             'confidence': 0.95,
             'explanation': 'The step describes receiving a normal incoming call while a Guard call is active and '
                            'verifying the UI elements for both calls.',
             'tags': ['incoming_call', 'UI_verification', 'Guard_call'],
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Guard call is kept active\n'
                         'Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button',
             'intent': "Verify the phone's behavior when switching between calls.",
             'suggested_commands': ['Press switch button', 'Verify UI updates for both calls'],
             'confidence': 0.95,
             'explanation': 'The step describes pressing the switch button to toggle between calls and verifying the '
                            'UI updates for both calls.',
             'tags': ['call_switching', 'UI_verification', 'Guard_call'],
             'automation': 'automatable'},
            {'step': 'Answer the new call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and normal call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': "Verify the phone's behavior when answering a new call during an active Guard call.",
             'suggested_commands': ['Answer new call',
                                    'Verify conference call initiation',
                                    'Verify UI elements for conference call'],
             'confidence': 0.95,
             'explanation': 'The step describes answering a new call during an active Guard call, which initiates a '
                            'conference call, and verifying the UI elements for the conference.',
             'tags': ['conference_call', 'UI_verification', 'Guard_call'],
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': "Verify the phone's behavior when pressing the exit/release button during a conference call.",
             'suggested_commands': ['Press exit/release button', 'Verify no action occurs'],
             'confidence': 0.9,
             'explanation': 'The step describes pressing the exit/release button during a conference call and '
                            'verifying that no action occurs.',
             'tags': ['button_action', 'conference_call', 'Guard_call'],
             'automation': 'automatable'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Guard call log and the normal incoming call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify call logs after a conference call with guard and normal incoming calls',
             'suggested_commands': ['Check call log for conference call details',
                                    'Verify guard call log details',
                                    'Check normal incoming call log details',
                                    'Validate label/avatar/name/number/date display'],
             'confidence': 0.95,
             'explanation': 'The test step involves verifying the presence and correctness of multiple call logs and '
                            'their associated details after a conference call is released.',
             'tags': ['call_log', 'conference_call', 'guard_call', 'incoming_call', 'UI_verification'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_14_Guard_Ougoing_Call_With_Second_Normal_Incoming_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify call establishment with Guard and UI behavior',
             'suggested_commands': ['Establish call with Guard', 'Verify UI elements'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the establishment of a call with the Guard and checking the '
                            'UI elements such as background color, avatar, and button states.',
             'tags': ['call_establishment', 'UI_verification', 'Guard_call'],
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Guard call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'Verify behavior when a normal incoming call is received during an active Guard call',
             'suggested_commands': ['Simulate incoming call', 'Verify active call state', 'Check UI for new call'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of the system when a normal incoming call is received during '
                            'an active Guard call, including verifying UI changes and call states.',
             'tags': ['incoming_call', 'call_handling', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Guard call is kept active\n'
                         'Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button',
             'intent': 'Verify call switch functionality and UI updates',
             'suggested_commands': ['Press switch button', 'Verify call positions', 'Check UI updates'],
             'confidence': 0.92,
             'explanation': 'This step tests the functionality of the switch button to toggle between calls and '
                            'verifies the corresponding UI updates.',
             'tags': ['call_switching', 'UI_verification', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'Press the silence button',
             'expected': 'Stop ringing',
             'intent': 'Verify silence button functionality during an incoming call',
             'suggested_commands': ['Press silence button', 'Verify ringing stops'],
             'confidence': 0.88,
             'explanation': 'The step tests the functionality of the silence button to ensure it stops the ringing of '
                            'an incoming call.',
             'tags': ['silence_button', 'incoming_call', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify reject button functionality and UI behavior',
             'suggested_commands': ['Press reject button', 'Verify call rejection', 'Check UI updates'],
             'confidence': 0.93,
             'explanation': 'This step tests the functionality of the reject button to ensure the incoming call is '
                            'rejected and verifies the corresponding UI updates.',
             'tags': ['call_rejection', 'UI_verification', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the not answered call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify call log details after handling outgoing and incoming calls',
             'suggested_commands': ['Check call log for Guard call entry',
                                    'Verify not answered call log entry',
                                    'Validate label/avatar/name/number/date display'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the call log entries and their details after specific call '
                            'scenarios. The expected result clearly outlines the elements to check.',
             'tags': ['call_log', 'verification', 'UI_elements'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_15_Guard_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify UI and functionality when a call is established with the Guard',
             'suggested_commands': ['Establish call with Guard', 'Verify UI elements', 'Check button states'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the UI and button states when a call is established with the '
                            'Guard.',
             'tags': ['UI', 'Call Handling', 'Guard'],
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
             'intent': 'Verify UI and functionality during a new outgoing call while Guard call is on hold',
             'suggested_commands': ['Initiate new outgoing call', 'Verify UI for both calls', 'Check button states'],
             'confidence': 0.95,
             'explanation': 'The step requires verifying the UI and button states for both the new outgoing call and '
                            'the Guard call on hold.',
             'tags': ['UI', 'Call Handling', 'Guard', 'Hold'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and normal call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'Verify conference call initiation and UI after remote side answers',
             'suggested_commands': ['Answer call on remote side',
                                    'Verify conference call initiation',
                                    'Check UI elements'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the transition to a conference call and the corresponding UI '
                            'changes when the remote side answers.',
             'tags': ['Conference Call', 'UI', 'Call Handling'],
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'Verify no action occurs when exit/release button is pressed during conference call',
             'suggested_commands': ['Press exit/release button', 'Verify no action occurs'],
             'confidence': 0.85,
             'explanation': 'The step tests the behavior of the exit/release button during a conference call, ensuring '
                            'no unintended actions occur.',
             'tags': ['Conference Call', 'Button Behavior'],
             'automation': 'automatable'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Guard call log and the normal outgoing call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify call logs after conference call is released',
             'suggested_commands': ['Release conference call', 'Check call logs', 'Verify log details'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the presence and correctness of call logs after the '
                            'conference call is released.',
             'tags': ['Call Logs', 'Conference Call'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_16_Guard_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify UI and functionality when a call is established with the Guard.',
             'suggested_commands': ['Initiate call to Guard',
                                    'Verify UI elements during call',
                                    'Check button states during call'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the UI and button states when a call is established with the '
                            'Guard. The expected behavior is clearly described.',
             'tags': ['UI', 'Call Handling', 'Guard Call'],
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
             'intent': 'Verify UI and functionality when making a new outgoing call while the Guard call is on hold.',
             'suggested_commands': ['Initiate new outgoing call',
                                    'Verify UI elements for both calls',
                                    'Check button states for both calls'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the UI and button states when a new outgoing call is made '
                            'while the Guard call is on hold. The expected behavior is detailed.',
             'tags': ['UI', 'Call Handling', 'Multiple Calls'],
             'automation': 'automatable'},
            {'step': 'Remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify UI and functionality when the remote side rejects the call.',
             'suggested_commands': ['Simulate remote side rejecting the call',
                                    'Verify UI elements after rejection',
                                    'Check button states after rejection'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the UI and button states when the remote side rejects the '
                            'call. The expected behavior is clearly outlined.',
             'tags': ['UI', 'Call Handling', 'Call Rejection'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the unsuccessful call log\n'
                         'the label /avatar /name /number/date display correctly',
             'intent': 'Verify call log entries after the call is released.',
             'suggested_commands': ['Release the call',
                                    'Check call log for Guard call',
                                    'Check call log for unsuccessful call'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the call log entries for both the Guard call and the '
                            'unsuccessful call after the call is released. The expected behavior is detailed.',
             'tags': ['Call Log', 'Post-Call Verification'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_17_Operator_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Operator program key',
  'steps': [{'step': 'Press the Operator program key of the phone or addon',
             'expected': 'title: Outgoing call\n'
                         'white background\n'
                         'display Operator avatar and release button(led is on)\n'
                         'and press the Operator avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'Initiate outgoing call using Operator program key',
             'suggested_commands': ['PressProgramKey', 'VerifyCallScreen'],
             'confidence': 0.95,
             'explanation': 'The step describes initiating an outgoing call using the Operator program key and '
                            'verifying the expected call screen behavior.',
             'tags': ['call', 'operator', 'program_key', 'outgoing'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Verify call screen after remote side answers',
             'suggested_commands': ['AnswerCallRemote', 'VerifyCallScreen'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the call screen after the remote side answers the call.',
             'tags': ['call', 'operator', 'remote_answer', 'screen_verification'],
             'automation': 'automatable'},
            {'step': 'Press the Operator avatar',
             'expected': 'Display the Operator info',
             'intent': 'Access Operator information',
             'suggested_commands': ['PressOperatorAvatar', 'VerifyInfoScreen'],
             'confidence': 0.85,
             'explanation': 'The step describes pressing the Operator avatar to access and verify the Operator '
                            'information screen.',
             'tags': ['operator', 'info_screen', 'avatar'],
             'automation': 'automatable'},
            {'step': 'Press the hold key of the screen or the hold physical key',
             'expected': 'will hold the call\n'
                         'title: On hold xx:xx\n'
                         'Blue background\n'
                         'display Operator avatar / hold / new call/ release button\n'
                         'the led of the hold is breath',
             'intent': 'Hold the call using hold key',
             'suggested_commands': ['PressHoldKey', 'VerifyHoldScreen'],
             'confidence': 0.9,
             'explanation': 'The step involves pressing the hold key to put the call on hold and verifying the hold '
                            'screen behavior.',
             'tags': ['call', 'hold', 'operator', 'screen_verification'],
             'automation': 'automatable'},
            {'step': 'Press the hold key of the screen or the hold physical key again',
             'expected': 'will retrieve the call\n'
                         'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Retrieve the call from hold',
             'suggested_commands': ['PressHoldKey', 'VerifyCallScreen'],
             'confidence': 0.9,
             'explanation': 'The step describes retrieving the call from hold by pressing the hold key again and '
                            'verifying the call screen behavior.',
             'tags': ['call', 'hold', 'retrieve', 'operator'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'Verify handset functionality during outgoing call',
             'suggested_commands': ['Lift handset', 'Verify voice switches to handset'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the transition of audio to the handset when it is picked up.',
             'tags': ['handset', 'audio', 'outgoing_call'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset or \npress the release key of the screen or the release physical button',
             'expected': 'will release the call',
             'intent': 'Verify call release functionality',
             'suggested_commands': ['Hang up handset', 'Press release key', 'Press release button'],
             'confidence': 0.9,
             'explanation': 'The step tests the ability to release a call using different methods.',
             'tags': ['call_release', 'release_key', 'handset'],
             'automation': 'automatable'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log (outgoing)\nthe label /avatar /name /number/date display correctly',
             'intent': 'Verify call log details for outgoing calls',
             'suggested_commands': ['Open call log', 'Verify details: label, avatar, name, number, date'],
             'confidence': 0.92,
             'explanation': 'The step ensures that the call log displays correct details for outgoing calls made by '
                            'the Operator program key.',
             'tags': ['call_log', 'outgoing_call', 'details_verification'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_18_Operator_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Press the Operator call log/ Operator contact or dial the Operator number',
             'expected': 'title: Outgoing call\n'
                         'white background\n'
                         'display Operator avatar and release button(led is on)\n'
                         'and press the Operator avatar will turn to the info screen\n'
                         'if press the release key will release the call',
             'intent': 'Initiate outgoing call via Operator log, contact, or dial number',
             'suggested_commands': ['Navigate to Operator call log', 'Select Operator contact', 'Dial Operator number'],
             'confidence': 0.95,
             'explanation': 'The step describes initiating an outgoing call using different methods (log, contact, or '
                            'direct dialing).',
             'tags': ['outgoing_call', 'operator', 'call_log', 'contact'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Verify call status and UI when remote side answers',
             'suggested_commands': ['Simulate remote side answering the call',
                                    'Check call status title',
                                    'Verify UI elements (background, avatar, buttons)'],
             'confidence': 0.9,
             'explanation': 'The step focuses on verifying the call status and UI changes when the remote side answers '
                            'the call.',
             'tags': ['call_status', 'ui_verification', 'operator', 'remote_answer'],
             'automation': 'automatable'},
            {'step': 'Press the Operator avatar',
             'expected': 'Display the Operator  info',
             'intent': 'Access Operator information screen',
             'suggested_commands': ['Press Operator avatar', 'Verify Operator info screen is displayed'],
             'confidence': 0.92,
             'explanation': "The step describes accessing the Operator's information by pressing the avatar.",
             'tags': ['operator_info', 'ui_interaction', 'avatar'],
             'automation': 'automatable'},
            {'step': 'Press the hold key of the screen or the hold physical key',
             'expected': 'will hold the call\n'
                         'title: On hold xx:xx\n'
                         'Blue background\n'
                         'display Operator avatar / hold / new call/ release button\n'
                         'the led of the hold is breath',
             'intent': 'Place call on hold',
             'suggested_commands': ['Press hold key on screen',
                                    'Press physical hold key',
                                    'Verify call is on hold',
                                    'Check UI elements (title, background, buttons, LED behavior)'],
             'confidence': 0.93,
             'explanation': 'The step involves placing the call on hold and verifying the corresponding UI and LED '
                            'behavior.',
             'tags': ['call_hold', 'ui_verification', 'led_behavior', 'operator'],
             'automation': 'automatable'},
            {'step': 'Press the hold key of the screen or the hold physical key again',
             'expected': 'will retrieve the call\n'
                         'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Retrieve call from hold',
             'suggested_commands': ['Press hold key on screen again',
                                    'Press physical hold key again',
                                    'Verify call is retrieved',
                                    'Check UI elements (title, background, buttons, LED behavior)'],
             'confidence': 0.93,
             'explanation': 'The step describes retrieving a call from hold and verifying the corresponding UI and LED '
                            'behavior.',
             'tags': ['call_retrieve', 'ui_verification', 'led_behavior', 'operator'],
             'automation': 'automatable'},
            {'step': 'pick up the handset',
             'expected': 'the voice will switch to handset',
             'intent': 'Switch voice to handset during a call',
             'suggested_commands': ['Lift the handset to switch audio output'],
             'confidence': 0.95,
             'explanation': 'The step involves picking up the handset, which is a straightforward action to switch the '
                            'audio output to the handset.',
             'tags': ['audio', 'handset', 'call'],
             'automation': 'automatable'},
            {'step': 'Hang on the handset or \npress the release key of the screen or the release physical button',
             'expected': 'will release the call',
             'intent': 'End a call using various methods',
             'suggested_commands': ['Hang up the handset',
                                    'Press the release key on the screen',
                                    'Press the physical release button'],
             'confidence': 0.9,
             'explanation': 'The step describes multiple ways to release a call, which can be automated depending on '
                            'the method used.',
             'tags': ['call', 'end_call', 'release'],
             'automation': 'automatable'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log (outgoing)\nthe label /avatar /name /number/date display correctly',
             'intent': 'Verify the operator call log details',
             'suggested_commands': ['Access the call log',
                                    'Verify the presence of outgoing call details',
                                    'Check label/avatar/name/number/date display'],
             'confidence': 0.85,
             'explanation': 'The step requires checking the call log for specific details, which may need manual '
                            'verification depending on the UI.',
             'tags': ['call_log', 'verification', 'UI_check'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_19_Operator_Outgoing_Call_With_Second_Normal_Imcoming_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Verify outgoing call establishment with operator',
             'suggested_commands': ['Place an outgoing call to the operator', 'Verify call interface elements'],
             'confidence': 0.95,
             'explanation': 'The step involves establishing a call with the operator and verifying the UI elements '
                            'displayed during the call.',
             'tags': ['call_establishment', 'UI_verification', 'operator'],
             'automation': 'automatable'},
            {'step': 'Phone receives the incoming call',
             'expected': 'the Operator call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'Verify incoming call handling during an active operator call',
             'suggested_commands': ['Receive an incoming call during an active operator call',
                                    'Verify UI elements for both calls'],
             'confidence': 0.92,
             'explanation': 'The step tests the behavior of the phone when an incoming call is received during an '
                            'active operator call, focusing on UI changes.',
             'tags': ['incoming_call', 'call_handling', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Operator call is kept active\n'
                         'Operator call in the lower part of the screen:\n'
                         'purple background +Guard avatar +switch button',
             'intent': 'Verify call switching functionality',
             'suggested_commands': ['Press the switch button', 'Verify the UI updates for both calls'],
             'confidence': 0.94,
             'explanation': 'The step tests the functionality of the switch button and the corresponding UI updates '
                            'for both calls.',
             'tags': ['call_switching', 'UI_verification', 'functionality_test'],
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
             'intent': 'Verify answering a new call while keeping the operator call on hold',
             'suggested_commands': ['Answer the new call', 'Verify the UI updates for both calls'],
             'confidence': 0.93,
             'explanation': 'The step tests the behavior of the phone when answering a new call while keeping the '
                            'operator call on hold, focusing on UI changes.',
             'tags': ['call_answering', 'call_hold', 'UI_verification'],
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
             'intent': 'Verify call switching and UI updates for two active calls',
             'suggested_commands': ['Press the switch button', 'Verify the UI updates for both calls'],
             'confidence': 0.94,
             'explanation': 'The step tests the functionality of the switch button and verifies the UI updates for two '
                            'active calls.',
             'tags': ['call_switching', 'UI_verification', 'functionality_test'],
             'automation': 'automatable'},
            {'step': 'Press the conference button',
             'expected': 'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Operator  and normal call avatar\n'
                         'display the exit and release button',
             'intent': "Verify conference call behavior and UI elements during an operator's outgoing call with a "
                       'second incoming call.',
             'suggested_commands': ['Press conference button',
                                    'Check for purple background',
                                    'Verify display of operator and normal call avatars',
                                    'Check for exit and release buttons'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior of the conference button and the corresponding '
                            'UI elements during a specific call scenario.',
             'tags': ['conference', 'UI', 'operator', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator / normal incoming / conference call log\n'
                         'the label /avatar /number display correctly',
             'intent': "Verify call log entries and UI elements after releasing a call during an operator's outgoing "
                       'call with a second incoming call.',
             'suggested_commands': ['Release the call',
                                    'Open call log',
                                    'Verify presence of operator, normal incoming, and conference call logs',
                                    'Check labels, avatars, and numbers for correctness'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the call log entries and their associated UI elements after '
                            'releasing a call in a specific scenario.',
             'tags': ['call_log', 'UI', 'operator', 'call_handling'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_20_Operator_Outgoing_Call_With_Second_Normal_Imcoming_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Verify outgoing call establishment with operator',
             'suggested_commands': ['Initiate call to operator', 'Verify UI elements during call'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the UI and call state when a call is established with the '
                            'operator.',
             'tags': ['call_establishment', 'UI_verification', 'operator'],
             'automation': 'automatable'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Operator call is kept active\n'
                         '\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"',
             'intent': 'Verify behavior when a normal incoming call is received during an active operator call',
             'suggested_commands': ['Simulate incoming call', 'Verify UI updates for new call'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of the phone when a new incoming call is received during an '
                            'active operator call.',
             'tags': ['incoming_call', 'UI_verification', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Operator call is kept active\n'
                         'Operator call in the lower part of the screen:\n'
                         'purple background +Guard avatar +switch button',
             'intent': 'Verify switch functionality between calls',
             'suggested_commands': ['Press switch button', 'Verify call positions and UI updates'],
             'confidence': 0.92,
             'explanation': 'The step involves testing the switch button functionality and verifying the UI updates '
                            'for active and held calls.',
             'tags': ['call_switching', 'UI_verification', 'multi_call_handling'],
             'automation': 'automatable'},
            {'step': 'Press the silence button',
             'expected': 'Stop ringing',
             'intent': 'Verify silence button functionality during an incoming call',
             'suggested_commands': ['Press silence button', 'Verify ringing stops'],
             'confidence': 0.88,
             'explanation': 'The step tests the functionality of the silence button to stop the ringing of an incoming '
                            'call.',
             'tags': ['silence_button', 'incoming_call', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Verify reject button functionality for an incoming call',
             'suggested_commands': ['Press reject button', 'Verify call is rejected or sent to voicemail'],
             'confidence': 0.93,
             'explanation': 'The step involves testing the reject button functionality to ensure the incoming call is '
                            'either rejected or sent to voicemail.',
             'tags': ['reject_button', 'incoming_call', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator / normal unanswered call log\nthe label /avatar /number display correctly',
             'intent': 'Verify call log behavior after rejecting a second incoming call',
             'suggested_commands': ['Release the active call',
                                    'Navigate to call log',
                                    'Verify presence of operator and normal unanswered call logs',
                                    'Check label, avatar, and number display'],
             'confidence': 0.95,
             'explanation': 'The test step involves verifying the call log after a specific sequence of actions, which '
                            'aligns with the intent to check call log behavior.',
             'tags': ['call_log', 'operator', 'incoming_call', 'call_rejection', 'UI_verification'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_21_Operator_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Verify UI and functionality during an outgoing call with an operator',
             'suggested_commands': ['Establish a call with the operator',
                                    'Verify UI elements such as background color, avatar, and buttons'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the UI and functional elements during an operator call, '
                            'including the display of specific UI components.',
             'tags': ['UI', 'Operator Call', 'Outgoing Call'],
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
             'intent': 'Verify UI and functionality during a second outgoing call while the operator call is on hold',
             'suggested_commands': ['Initiate a second outgoing call',
                                    'Verify UI elements for both calls, including background colors, avatars, and '
                                    'buttons'],
             'confidence': 0.95,
             'explanation': 'The step tests the behavior and UI when a second outgoing call is made while the operator '
                            'call is on hold.',
             'tags': ['UI', 'Operator Call', 'Outgoing Call', 'Call Hold'],
             'automation': 'automatable'},
            {'step': 'If press the transfer button',
             'expected': 'exit the two calls\n'
                         'Call log has the Operator call log and normal call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'Verify call termination and call log updates after pressing the transfer button',
             'suggested_commands': ['Press the transfer button',
                                    'Verify that both calls are terminated',
                                    'Check the call log for correct entries'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the behavior of the transfer button, ensuring both calls are '
                            'terminated and the call log is updated correctly.',
             'tags': ['Call Transfer', 'Call Log', 'UI'],
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
             'intent': 'Verify UI and functionality when transfer button is not pressed and remote side answers the '
                       'call',
             'suggested_commands': ['Do not press the transfer button',
                                    'Wait for the remote side to answer',
                                    'Verify UI elements for both calls, including background colors, avatars, and '
                                    'buttons'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior and UI when the transfer button is not pressed, and the '
                            'remote side answers the call.',
             'tags': ['UI', 'Operator Call', 'Outgoing Call', 'Call Hold'],
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
             'intent': 'Verify UI and functionality when switching between two calls',
             'suggested_commands': ['Press the switch button',
                                    'Verify UI elements for both calls, including background colors, avatars, and '
                                    'buttons'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior and UI when switching between two active calls.',
             'tags': ['UI', 'Call Switching', 'Operator Call', 'Outgoing Call'],
             'automation': 'automatable'},
            {'step': 'press the transfer key',
             'expected': 'exit the two calls',
             'intent': "Handle call transfer during an operator's outgoing call with a second normal outgoing call.",
             'suggested_commands': ['Transfer', 'End Call', 'Hold'],
             'confidence': 0.95,
             'explanation': 'The step involves pressing the transfer key to manage two calls, which is a common '
                            'telephony feature.',
             'tags': ['call_transfer', 'multi_call', 'operator'],
             'automation': 'automatable'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log and the normal outgoing call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'Verify call log details after handling multiple calls.',
             'suggested_commands': ['View Call Log', 'Check Call Details'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the call log for accuracy, which is a standard validation '
                            'process.',
             'tags': ['call_log', 'verification', 'operator'],
             'automation': 'manual'}]},
 {'title': 'RQPLEIAD_180_22_Operator_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Verify call establishment with Operator',
             'suggested_commands': ['Establish call with Operator', 'Check UI elements for call status'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the establishment of a call with the Operator and checking '
                            'the UI for specific elements.',
             'tags': ['call_establishment', 'UI_verification', 'Operator'],
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
             'intent': 'Verify new outgoing call while Operator call is on hold',
             'suggested_commands': ['Initiate new outgoing call', 'Verify UI for both calls', 'Check call hold status'],
             'confidence': 0.95,
             'explanation': 'The step involves initiating a new outgoing call, verifying the UI for both calls, and '
                            'ensuring the Operator call is on hold.',
             'tags': ['call_management', 'UI_verification', 'hold_functionality'],
             'automation': 'automatable'},
            {'step': 'remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Verify behavior when remote side rejects the call',
             'suggested_commands': ['Simulate remote side rejecting the call', 'Verify UI updates for call rejection'],
             'confidence': 0.9,
             'explanation': 'The step involves simulating a call rejection from the remote side and verifying the UI '
                            'updates accordingly.',
             'tags': ['call_rejection', 'UI_verification', 'Operator'],
             'automation': 'automatable'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator call log and the normal unsuccessful call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'Verify call logs after call release',
             'suggested_commands': ['Release the call', 'Check call logs for both Operator and unsuccessful call'],
             'confidence': 0.9,
             'explanation': 'The step involves releasing the call and verifying that the call logs for both the '
                            'Operator and the unsuccessful call are displayed correctly.',
             'tags': ['call_logs', 'UI_verification', 'call_release'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_23_Emergency_Call_With_Guard_Call',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile:\nEmergency  number----xxxx\nGuard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         '\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify emergency call establishment',
             'suggested_commands': ['Initiate emergency call', 'Check UI elements during call'],
             'confidence': 0.95,
             'explanation': "The step involves verifying the phone's behavior when an emergency call is established, "
                            'including UI elements and button states.',
             'tags': ['emergency_call', 'UI_verification', 'call_handling'],
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
             'intent': 'Verify outgoing call to Guard during emergency call',
             'suggested_commands': ['Initiate outgoing call to Guard',
                                    'Check UI elements for both calls',
                                    'Verify button states'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior when a new outgoing call is made to the Guard while an '
                            'emergency call is active, including UI and button state verification.',
             'tags': ['guard_call', 'emergency_call', 'UI_verification', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and Guard call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'Verify conference call initiation',
             'suggested_commands': ['Answer remote call',
                                    'Check conference call behavior',
                                    'Verify UI elements during conference'],
             'confidence': 0.92,
             'explanation': 'The step validates the automatic initiation of a conference call when the remote side '
                            'answers, including UI and button state verification.',
             'tags': ['conference_call', 'UI_verification', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'Verify exit/release button behavior during call',
             'suggested_commands': ['Press exit/release button during call', 'Check for any action or response'],
             'confidence': 0.88,
             'explanation': 'The step tests the behavior of the exit/release button during an active call to ensure no '
                            'unintended actions occur.',
             'tags': ['button_behavior', 'call_handling'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the Guard call log and the conference call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'Verify call log after call release',
             'suggested_commands': ['Release call', 'Check call log for entries', 'Verify labels and avatars'],
             'confidence': 0.93,
             'explanation': 'The step ensures that the call log correctly records the emergency call, Guard call, and '
                            'conference call, with accurate labels and avatars.',
             'tags': ['call_log', 'UI_verification', 'call_handling'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_24_Operator_Call_With_Emergency_Call',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile:\nEmergency number----xxxx\nOperator number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)',
             'intent': 'Establish a call with the operator',
             'suggested_commands': ['Dial operator number', 'Verify call connection'],
             'confidence': 0.95,
             'explanation': 'The step describes initiating a call with the operator and verifying the expected UI '
                            'elements.',
             'tags': ['call_establishment', 'UI_verification'],
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
             'intent': 'Make an outgoing emergency call while operator call is on hold',
             'suggested_commands': ['Dial emergency number', 'Verify UI changes for emergency call and operator call'],
             'confidence': 0.9,
             'explanation': 'The step involves making an emergency call and verifying the UI updates for both calls.',
             'tags': ['emergency_call', 'call_hold', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the operator and Emergency call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'Remote side answers the call and initiates conference',
             'suggested_commands': ['Answer call remotely', 'Verify conference call UI'],
             'confidence': 0.85,
             'explanation': 'The step describes the transition to a conference call upon remote answer and the '
                            'expected UI elements.',
             'tags': ['conference_call', 'UI_verification'],
             'automation': 'needs_context'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'Press exit/release button during conference call',
             'suggested_commands': ['Press exit/release button', 'Verify no action occurs'],
             'confidence': 0.8,
             'explanation': 'The step tests the behavior of the exit/release button during a conference call.',
             'tags': ['button_action', 'conference_call'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the Operator call log and the conference call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'Verify call logs after call release',
             'suggested_commands': ['Check call logs', 'Verify labels, avatars, and numbers'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the call logs for emergency, operator, and conference calls '
                            'after release.',
             'tags': ['call_logs', 'UI_verification'],
             'automation': 'manual'}]},
 {'title': 'RQPLEIAD_180_25_Guard_Call_With_Operator_Call',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile:\nOperator number----xxxx\nGuard number----xxxx',
  'steps': [{'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         '\n'
                         'The release/ hold button are grey (led is off)',
             'intent': 'Verify call establishment with Guard',
             'suggested_commands': ['Initiate call to Guard', 'Check call display UI'],
             'confidence': 0.95,
             'explanation': "The step involves verifying the phone's ability to establish a call with the Guard and "
                            'checking the UI elements for correctness.',
             'tags': ['call_establishment', 'UI_verification', 'Guard_call'],
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
             'intent': 'Verify outgoing call to Operator while Guard call is on hold',
             'suggested_commands': ['Initiate call to Operator',
                                    'Verify UI for Operator call',
                                    'Check Guard call status'],
             'confidence': 0.95,
             'explanation': "The step tests the phone's ability to make a new outgoing call to the Operator while "
                            'keeping the Guard call on hold, and verifies the UI behavior.',
             'tags': ['call_management', 'UI_verification', 'Operator_call', 'Guard_call'],
             'automation': 'automatable'},
            {'step': 'remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and operator call avatar\n'
                         'The exit and release button are grey (led is off)',
             'intent': 'Verify conference call creation',
             'suggested_commands': ['Answer call from remote side', 'Verify conference call UI'],
             'confidence': 0.9,
             'explanation': 'The step checks if a conference call is created directly when the remote side answers, '
                            'and verifies the UI elements for the conference call.',
             'tags': ['conference_call', 'UI_verification', 'call_answer'],
             'automation': 'automatable'},
            {'step': 'Press the exit /release button',
             'expected': 'no action',
             'intent': 'Verify exit/release button functionality during conference call',
             'suggested_commands': ['Press exit/release button', 'Verify no action occurs'],
             'confidence': 0.85,
             'explanation': 'The step tests the behavior of the exit/release button during a conference call, ensuring '
                            'no unintended actions occur.',
             'tags': ['button_functionality', 'conference_call', 'UI_verification'],
             'automation': 'automatable'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the Operator call log and the conference call log\n'
                         'the label /avatar /number display correctly',
             'intent': 'Verify call log after call release',
             'suggested_commands': ['Release call', 'Check call log entries', 'Verify labels and avatars'],
             'confidence': 0.9,
             'explanation': 'The step verifies the call log entries for the Guard call, Operator call, and conference '
                            'call, ensuring all details are displayed correctly.',
             'tags': ['call_log_verification', 'UI_verification', 'call_release'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_26_Light/Dark_Mode_Emergency/Guard/Operator_Call',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'settings---device---appearance---loght/dark mode',
             'expected': 'can modify  successfully',
             'intent': 'Verify ability to modify light/dark mode settings',
             'suggested_commands': ['Navigate to settings > device > appearance', 'Switch between light and dark mode'],
             'confidence': 0.95,
             'explanation': 'The step involves modifying the appearance settings of the device, specifically toggling '
                            'between light and dark mode.',
             'tags': ['UI', 'Appearance', 'Settings'],
             'automation': 'automatable'},
            {'step': 'check the Emergency outgoing call screen/ hold screen/ conversation screen',
             'expected': 'The background color at the very bottom of the screen:\nlight mode: white \ndark mode: black',
             'intent': 'Verify background color for Emergency call screens in light/dark mode',
             'suggested_commands': ['Place an emergency call',
                                    'Verify background color on outgoing call screen',
                                    'Verify background color on hold screen',
                                    'Verify background color on conversation screen'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the background color of various screens during an emergency '
                            'call in both light and dark modes.',
             'tags': ['UI', 'Emergency Call', 'Appearance'],
             'automation': 'needs_context'},
            {'step': 'check the Guard outgoing call screen/ hold screen/ conversation screen /conference screen',
             'expected': 'The background color at the very bottom of the screen:\nlight mode: white\ndark mode: black',
             'intent': 'Verify background color for Guard call screens in light/dark mode',
             'suggested_commands': ['Place a guard call',
                                    'Verify background color on outgoing call screen',
                                    'Verify background color on hold screen',
                                    'Verify background color on conversation screen',
                                    'Verify background color on conference screen'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the background color of various screens during a guard call '
                            'in both light and dark modes.',
             'tags': ['UI', 'Guard Call', 'Appearance'],
             'automation': 'needs_context'},
            {'step': 'check the Operator outgoing call screen/ hold screen/ conversation screen /conference screen',
             'expected': 'The background color at the very bottom of the screen:\nlight mode: white\ndark mode: black',
             'intent': 'Verify background color for Operator call screens in light/dark mode',
             'suggested_commands': ['Place an operator call',
                                    'Verify background color on outgoing call screen',
                                    'Verify background color on hold screen',
                                    'Verify background color on conversation screen',
                                    'Verify background color on conference screen'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the background color of various screens during an operator '
                            'call in both light and dark modes.',
             'tags': ['UI', 'Operator Call', 'Appearance'],
             'automation': 'needs_context'}]},
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
             'intent': 'Verify default hard key configuration after connecting to OXE',
             'suggested_commands': ['Check hard key menu options',
                                    'Verify default settings for hard keys',
                                    'Inspect reset to default icon state'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the default configuration of hard keys after connecting the '
                            'phone to OXE and accessing the hard keys menu.',
             'tags': ['hard_keys', 'default_settings', 'OXE_connection'],
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
             'intent': 'Verify hard key functionality upon long press',
             'suggested_commands': ['Perform long press on specified keys',
                                    'Verify displayed options for hard key configuration',
                                    'Check reset to default icon state'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of hard keys when long-pressed and verifies the options '
                            'displayed for configuration.',
             'tags': ['hard_keys', 'long_press', 'configuration'],
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F1 key',
             'expected': 'ALE-30/300/400/500:\nIf disable the lock: no action\nIf enable the lock: will lock the phone',
             'intent': 'Verify F1 key behavior in idle mode',
             'suggested_commands': ['Check LED state of F1/F2/F3 keys in idle mode',
                                    'Press F1 key and observe behavior',
                                    'Verify phone lock functionality'],
             'confidence': 0.85,
             'explanation': 'The step tests the behavior of the F1 key in idle mode and verifies the phone lock '
                            'functionality based on lock settings.',
             'tags': ['idle_mode', 'F1_key', 'lock_functionality'],
             'automation': 'needs_context'},
            {'step': 'Phone establish a normal call the led of the F1 is on\n'
                     'then press the F1 key\n'
                     'then press the F1 key again',
             'expected': 'ALE-30/300/400/500:\n'
                         'will hold the call, and led of the F1 key is breath\n'
                         'will retrieve the call. the led of the F1 key is on',
             'intent': 'Verify F1 key behavior during a call',
             'suggested_commands': ['Establish a normal call',
                                    'Press F1 key and observe call hold behavior',
                                    'Press F1 key again and verify call retrieval'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of the F1 key during a call, including holding and retrieving '
                            'the call, and verifies LED state changes.',
             'tags': ['call_handling', 'F1_key', 'LED_behavior'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1/F2/F3 is on\nthen press the F2 key',
             'expected': 'ALE-30/300/400/500:\nwill exit these two calls',
             'intent': 'Verify F2 key behavior during two active calls',
             'suggested_commands': ['Establish two normal calls',
                                    'Press F2 key and observe call exit behavior',
                                    'Verify LED state changes for F1/F2/F3 keys'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of the F2 key when two calls are active and verifies the exit '
                            'functionality.',
             'tags': ['multi_call_handling', 'F2_key', 'LED_behavior'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1/F2/F3 is on\nthen press the F3 key',
             'expected': 'ALE-300/400/500:will make the conference call,and led of the F3 key is breath',
             'intent': 'Test conference call functionality using hard keys',
             'suggested_commands': ['Establish two normal calls',
                                    'Verify LED status of F1/F2/F3 keys',
                                    'Press F3 key',
                                    'Check if conference call is initiated',
                                    'Verify F3 key LED is in breathing state'],
             'confidence': 0.95,
             'explanation': 'The test step involves verifying the behavior of the F3 key during a conference call '
                            'scenario, including LED status and call functionality.',
             'tags': ['conference_call', 'hard_key', 'LED_status', 'functionality_test'],
             'automation': 'automatable'},
            {'step': 'check the Triangle/Circle/Square on ALE500',
             'expected': 'The three keys name display correctly\n'
                         'and press the hard key:\n'
                         'Triangle : Will Return to the previous interface\n'
                         'Circle: will turn to the dashboard\n'
                         'Square :The screen brightness will decreased',
             'intent': 'Verify hard key functionality and labels on ALE500',
             'suggested_commands': ['Inspect Triangle/Circle/Square keys on ALE500',
                                    'Verify correct display of key names',
                                    'Press Triangle key and check if it returns to the previous interface',
                                    'Press Circle key and check if it navigates to the dashboard',
                                    'Press Square key and verify if screen brightness decreases'],
             'confidence': 0.9,
             'explanation': 'The test step focuses on validating the functionality and labeling of specific hard keys '
                            'on the ALE500 model.',
             'tags': ['hard_key', 'functionality_test', 'UI_verification', 'ALE500'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_28_Hard_Key_OXE_Define_Position_Label_Recognition',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'set the progkey 123:programmed with the phone A number on position 1\n'
                     'mnemo:  position1\n'
                     'Phone update the config file then check the file\n'
                     '（/config/dm/config.xxxxxxx.xml）',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,x" override="true"/>',
             'intent': 'Configure hard key with specific label and verify configuration file',
             'suggested_commands': ['Program key 123 with phone A number',
                                    'Verify configuration file at /config/dm/config.xxxxxxx.xml'],
             'confidence': 0.95,
             'explanation': 'The step describes programming a key with a specific label and verifying the '
                            'configuration file to ensure the changes are applied correctly.',
             'tags': ['configuration', 'hard_key', 'verification'],
             'automation': 'automatable'},
            {'step': 'press the hard key:\nALE-30/300/400: F1 key\nALE-500: Triangle Key',
             'expected': 'Will makes the outgoing call to the phone A',
             'intent': 'Test hard key functionality for making an outgoing call',
             'suggested_commands': ['Press F1 key on ALE-30/300/400',
                                    'Press Triangle Key on ALE-500',
                                    'Verify outgoing call to phone A'],
             'confidence': 0.9,
             'explanation': 'The step tests the functionality of specific hard keys to ensure they initiate an '
                            'outgoing call to phone A.',
             'tags': ['hard_key', 'call_functionality', 'testing'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 124:programmed with the phone B number on position 2\n'
                     'mnemo:  position_2\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position_2,30461,0,X" override="true"/>',
             'intent': 'Configure hard key with specific label and verify configuration file',
             'suggested_commands': ['Program key 124 with phone B number',
                                    'Verify configuration file at /config/dm/config.xxxxxxx.xml'],
             'confidence': 0.95,
             'explanation': 'The step describes programming a key with a specific label and verifying the '
                            'configuration file to ensure the changes are applied correctly.',
             'tags': ['configuration', 'hard_key', 'verification'],
             'automation': 'automatable'},
            {'step': 'press the hard key:\nALE-30/300/400: F2 key\nALE-500: Circle Key',
             'expected': 'Will makes the outgoing call to the phone B',
             'intent': 'Test hard key functionality for making an outgoing call',
             'suggested_commands': ['Press F2 key on ALE-30/300/400',
                                    'Press Circle Key on ALE-500',
                                    'Verify outgoing call to phone B'],
             'confidence': 0.9,
             'explanation': 'The step tests the functionality of specific hard keys to ensure they initiate an '
                            'outgoing call to phone B.',
             'tags': ['hard_key', 'call_functionality', 'testing'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 123:programmed with the phone C number on position 1\n'
                     'mnemo:  position 1\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position 1,xxx,0,x" override="true"/>',
             'intent': 'Configure hard key with specific label and verify configuration file',
             'suggested_commands': ['Program key 123 with phone C number',
                                    'Verify configuration file at /config/dm/config.xxxxxxx.xml'],
             'confidence': 0.95,
             'explanation': 'The step describes programming a key with a specific label and verifying the '
                            'configuration file to ensure the changes are applied correctly.',
             'tags': ['configuration', 'hard_key', 'verification'],
             'automation': 'automatable'},
            {'step': 'press the hard key:\nALE-30/300/400: F1 key\nALE-500: Triangle Key',
             'expected': 'Will makes the outgoing call to the phone C',
             'intent': 'Test hard key functionality for outgoing call',
             'suggested_commands': ['Press F1 key on ALE-30/300/400', 'Press Triangle Key on ALE-500'],
             'confidence': 0.95,
             'explanation': 'The step involves pressing a specific hard key to trigger an outgoing call to phone C.',
             'tags': ['hard_key', 'outgoing_call', 'phone_C'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 124:programmed with the phone D number on position 2\n'
                     'mnemo:  POSITION2\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,POSITION2,30461,0,X" override="true"/>',
             'intent': 'Configure program key and verify configuration file',
             'suggested_commands': ['Program key 124 with phone D number', 'Verify updated configuration file'],
             'confidence': 0.9,
             'explanation': 'The step describes programming a key with a specific phone number and verifying the '
                            'configuration file for correctness.',
             'tags': ['program_key', 'configuration_file', 'phone_D'],
             'automation': 'needs_context'},
            {'step': 'press the hard key:\nALE-30/300/400: F2 key\nALE-500: Circle Key',
             'expected': 'Will makes the outgoing call to the phone D',
             'intent': 'Test hard key functionality for outgoing call',
             'suggested_commands': ['Press F2 key on ALE-30/300/400', 'Press Circle Key on ALE-500'],
             'confidence': 0.95,
             'explanation': 'The step involves pressing a specific hard key to trigger an outgoing call to phone D.',
             'tags': ['hard_key', 'outgoing_call', 'phone_D'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 123 and 124\n'
                     'mnemo:  the string is different to one of the “position1”, “position2”, “position3”',
             'expected': '.If and their equivalent as described in the two above points, by default, the key 120 is '
                         'mapped to “position1” and 121 to “position2',
             'intent': 'Configure multiple program keys with custom mnemonics',
             'suggested_commands': ['Program keys 123 and 124 with custom mnemonics',
                                    'Verify default mapping for keys 120 and 121'],
             'confidence': 0.85,
             'explanation': 'The step involves programming multiple keys with custom mnemonics and verifying their '
                            'mappings.',
             'tags': ['program_key', 'mnemonics', 'key_mapping'],
             'automation': 'needs_context'},
            {'step': 'press the hard key:\nALE-30: F1/F2 key\nALE-300/400: F1/F2/F3 key\nALE-500: Triangle/Circle Key',
             'expected': 'The function is directly',
             'intent': 'Test multiple hard key functionalities',
             'suggested_commands': ['Press F1/F2 on ALE-30',
                                    'Press F1/F2/F3 on ALE-300/400',
                                    'Press Triangle/Circle Key on ALE-500'],
             'confidence': 0.9,
             'explanation': 'The step involves testing multiple hard keys across different phone models to verify '
                            'their functionality.',
             'tags': ['hard_key', 'multi_model', 'functionality_test'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_29_Hard_Key_OXE_Define_Key1_Lock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'Only set the progkey 123: programmed with phone A on position 1,and the lock parameter is '
                     'enabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,1" override="true"/>',
             'intent': 'Verify key programming and lock functionality',
             'suggested_commands': ['Program key with specified parameters',
                                    'Update configuration file',
                                    'Check configuration file for expected values'],
             'confidence': 0.95,
             'explanation': 'The step involves programming a key with specific parameters and verifying the '
                            'configuration file for correct updates.',
             'tags': ['key_programming', 'configuration_verification', 'lock_functionality'],
             'automation': 'automatable'},
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
             'intent': 'Verify hard keys menu display and options',
             'suggested_commands': ['Navigate to hard keys menu',
                                    'Verify menu title and icon states',
                                    'Check displayed options for different models'],
             'confidence': 0.9,
             'explanation': 'The step involves navigating to the hard keys menu and verifying the displayed options '
                            'and icons for different phone models.',
             'tags': ['menu_navigation', 'hard_keys', 'UI_verification'],
             'automation': 'needs_context'},
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
             'intent': 'Verify long press functionality for hard keys',
             'suggested_commands': ['Perform long press on specified keys',
                                    'Verify displayed options and icons for different models'],
             'confidence': 0.88,
             'explanation': 'The step involves testing the long press functionality for hard keys across different '
                            'phone models and verifying the displayed options.',
             'tags': ['long_press', 'hard_keys', 'functional_verification'],
             'automation': 'needs_context'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'Verify functionality of specific hard keys',
             'suggested_commands': ['Test F1, F2, and F3 keys on ALE-500', 'Verify expected functions for each key'],
             'confidence': 0.92,
             'explanation': 'The step involves verifying the specific functions of F1, F2, and F3 keys on the ALE-500 '
                            'model.',
             'tags': ['hard_keys', 'functionality_test', 'ALE_500'],
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
             'intent': 'Verify hard key names and functionality',
             'suggested_commands': ['Verify displayed hard key names',
                                    'Test functionality of Triangle, Circle, and Square keys'],
             'confidence': 0.93,
             'explanation': 'The step involves verifying the names and functionality of hard keys on different phone '
                            'models.',
             'tags': ['hard_keys', 'name_verification', 'functionality_test'],
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle key',
             'expected': 'Will makes the second outgoing call to phone A',
             'intent': 'Initiate second outgoing call during an active call',
             'suggested_commands': ['Establish call', 'Press Triangle key'],
             'confidence': 0.9,
             'explanation': 'The step describes initiating a second outgoing call by pressing the Triangle key while '
                            'already in an active call.',
             'tags': ['call_handling', 'multi_call', 'key_action'],
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nWill makes the outgoing call to phone A',
             'intent': 'Initiate outgoing call from idle mode using F1 key',
             'suggested_commands': ['Check idle mode', 'Press F1 key'],
             'confidence': 0.85,
             'explanation': 'The step describes initiating an outgoing call from idle mode by pressing the F1 key.',
             'tags': ['call_handling', 'idle_mode', 'key_action'],
             'automation': 'automatable'},
            {'step': 'Phone establish a call with phone B then press the F1',
             'expected': 'ALE-30/300/400:\nWill makes the second outgoing call to phone A',
             'intent': 'Initiate second outgoing call during an active call using F1 key',
             'suggested_commands': ['Establish call', 'Press F1 key'],
             'confidence': 0.9,
             'explanation': 'The step describes initiating a second outgoing call by pressing the F1 key while already '
                            'in an active call.',
             'tags': ['call_handling', 'multi_call', 'key_action'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1 is off, the led of the F2/F3 is on\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls',
             'intent': 'Exit two active calls using F2 key',
             'suggested_commands': ['Establish two calls', 'Press F2 key'],
             'confidence': 0.88,
             'explanation': 'The step describes exiting two active calls by pressing the F2 key.',
             'tags': ['call_handling', 'multi_call', 'key_action'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1 is off, the led of the F2/F3 is on\n'
                     'then press the F3 key',
             'expected': 'ALE-30/300/400:\nwill makes the conference call, and the led of the conference is breath',
             'intent': 'Initiate conference call using F3 key',
             'suggested_commands': ['Establish two calls', 'Press F3 key'],
             'confidence': 0.92,
             'explanation': 'The step describes initiating a conference call by pressing the F3 key when two calls are '
                            'active.',
             'tags': ['call_handling', 'conference_call', 'key_action'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>',
             'intent': 'Define and lock a programmable key on OXE',
             'suggested_commands': ['Access OXE user interface',
                                    'Navigate to programmable key settings',
                                    "Set progkey 124 to 'Not Assigned'"],
             'confidence': 0.95,
             'explanation': 'The step describes configuring a programmable key (progkey 124) on the OXE system and '
                            "setting it to 'Not Assigned'.",
             'tags': ['OXE', 'programmable_key', 'configuration'],
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
             'intent': 'Access and edit hard key settings on the phone',
             'suggested_commands': ['Enter hard keys menu via User/Device/Hard keys',
                                    'Long press F1, F2, F3, Triangle, Circle, or Square key',
                                    'Verify title and icon states',
                                    'Check available options for ALE-30, ALE-300/400, and ALE-500'],
             'confidence': 0.92,
             'explanation': 'The step involves accessing the hard keys menu on the phone, verifying the UI elements, '
                            'and checking the available options for different phone models.',
             'tags': ['hard_keys', 'menu_navigation', 'UI_verification'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_30_Hard_Key_OXE_Define_Key2_Unlock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'Only set the progkey 124: programmed with the Emergency function on position 2,and the lock '
                     'parameter is disabled\n'
                     'Phone update the config file then check the file![](index.php?/attachments/get/44225)',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position2,xxx,0,0" override="true"/>',
             'intent': 'Configure and verify key programming on OXE',
             'suggested_commands': ['Program key 124 with Emergency function',
                                    'Disable lock parameter',
                                    'Update phone configuration file',
                                    'Verify configuration file settings'],
             'confidence': 0.95,
             'explanation': 'The step involves programming a specific key with a function, updating the configuration, '
                            'and verifying the changes.',
             'tags': ['key_programming', 'configuration_verification', 'emergency_function'],
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
             'intent': 'Navigate to hard keys menu and verify UI elements',
             'suggested_commands': ['Enter hard keys menu',
                                    'Verify displayed title',
                                    'Check reset to default icon',
                                    'Verify radio button and key selection behavior',
                                    'Check options for different ALE models'],
             'confidence': 0.9,
             'explanation': 'The step focuses on navigating to the hard keys menu and verifying the UI elements and '
                            'options available for different models.',
             'tags': ['ui_verification', 'menu_navigation', 'model_specific_behavior'],
             'automation': 'needs_context'},
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
             'intent': 'Long press hard keys and verify UI elements',
             'suggested_commands': ['Long press F1/F2/F3/Triangle/Circle/Square key',
                                    'Verify displayed title',
                                    'Check reset to default icon',
                                    'Verify radio button and key selection behavior',
                                    'Check options for different ALE models'],
             'confidence': 0.9,
             'explanation': 'The step involves long pressing specific keys and verifying the UI elements and options '
                            'available for different models.',
             'tags': ['ui_verification', 'key_interaction', 'model_specific_behavior'],
             'automation': 'needs_context'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'Verify functionality of F1, F2, and F3 keys on ALE-500',
             'suggested_commands': ['Check F1 key functionality',
                                    'Check F2 key functionality',
                                    'Check F3 key functionality'],
             'confidence': 0.85,
             'explanation': 'The step involves verifying the specific functions assigned to the F1, F2, and F3 keys on '
                            'the ALE-500 model.',
             'tags': ['key_functionality', 'model_specific_behavior', 'function_verification'],
             'automation': 'manual'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will Return to the previous interface\n'
                         'Circle: Will makes the outgoing call to Emergency\n'
                         'Square :The screen brightness will decreased',
             'intent': 'Verify functionality and display of Triangle, Circle, and Square keys on ALE-500',
             'suggested_commands': ['Check Triangle key functionality and display',
                                    'Check Circle key functionality and display',
                                    'Check Square key functionality and display'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the display names and specific functions of the Triangle, '
                            'Circle, and Square keys on the ALE-500 model.',
             'tags': ['key_functionality', 'ui_verification', 'model_specific_behavior'],
             'automation': 'manual'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Circle key',
             'expected': 'Will makes the second outgoing call to Emergency',
             'intent': 'Make a second outgoing call to emergency during an active call',
             'suggested_commands': ['Establish call with phone B', 'Press Circle key'],
             'confidence': 0.95,
             'explanation': 'The step describes initiating a second outgoing call to emergency while an existing call '
                            'is active by pressing the Circle key.',
             'tags': ['call_handling', 'emergency_call', 'key_action'],
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F1 is on,the led of the F2/F3 is off',
             'intent': 'Make an outgoing emergency call from idle mode',
             'suggested_commands': ['Ensure phone is in idle mode', 'Press F2 key'],
             'confidence': 0.9,
             'explanation': 'The step describes making an emergency call from idle mode by pressing the F2 key, with '
                            'specific LED behavior and screen display expectations.',
             'tags': ['idle_mode', 'emergency_call', 'key_action', 'led_behavior'],
             'automation': 'automatable'},
            {'step': 'Phone establish a call. \nDuring the converstiaon then press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the new outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F2 is off,the led of the F1/F3 is oN',
             'intent': 'Make a new outgoing emergency call during an active call',
             'suggested_commands': ['Establish a call', 'Press F2 key during conversation'],
             'confidence': 0.92,
             'explanation': 'The step describes initiating a new emergency call during an active conversation by '
                            'pressing the F2 key, with specific LED and screen behavior.',
             'tags': ['call_handling', 'emergency_call', 'key_action', 'led_behavior'],
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath',
             'intent': 'Hold an active call using the F1 key',
             'suggested_commands': ['Establish a normal call', 'Press F1 key'],
             'confidence': 0.93,
             'explanation': 'The step describes holding an active call by pressing the F1 key, with specific LED '
                            'behavior indicating the hold state.',
             'tags': ['call_handling', 'hold_call', 'key_action', 'led_behavior'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1/F3 is on\nthen press the F3 key',
             'expected': 'ALE-300/400:\nwill make the conference call,and led of the F3 key is breath',
             'intent': 'Initiate a conference call using the F3 key',
             'suggested_commands': ['Establish two normal calls', 'Press F3 key'],
             'confidence': 0.94,
             'explanation': 'The step describes initiating a conference call by pressing the F3 key when two calls are '
                            'active, with specific LED behavior indicating the conference state.',
             'tags': ['call_handling', 'conference_call', 'key_action', 'led_behavior'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'Define and unlock a programmable key on OXE',
             'suggested_commands': ['program_key 124 Not_Assigned', 'set_key_state 124 inactive'],
             'confidence': 0.95,
             'explanation': 'The step involves programming a specific key (124) on the OXE system and setting it to '
                            "'Not Assigned'. This is a straightforward configuration task.",
             'tags': ['OXE', 'key_programming', 'configuration'],
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
             'intent': 'Access hard keys menu and verify options',
             'suggested_commands': ['navigate_to_menu Hard_Keys',
                                    'long_press_key F1',
                                    'long_press_key F2',
                                    'long_press_key F3',
                                    'long_press_key Triangle',
                                    'long_press_key Circle',
                                    'long_press_key Square'],
             'confidence': 0.9,
             'explanation': 'The step describes accessing the hard keys menu via navigation or long-pressing specific '
                            'keys, and verifying the available options for different phone models.',
             'tags': ['menu_navigation', 'hard_keys', 'verification'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_31_Hard_Key_OXE_Define_Key3_Unlock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'Only set the progkey 124: programmed with the Guard function on position 3,and the lock '
                     'parameter is disabled\n'
                     'Phone update the config file then check the file![](index.php?/attachments/get/44226)',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position3,xxx,0,0" override="true"/>',
             'intent': 'Configure and validate hard key settings',
             'suggested_commands': ['Set progkey 124 with Guard function',
                                    'Disable lock parameter',
                                    'Update config file',
                                    'Verify config file content'],
             'confidence': 0.9,
             'explanation': 'The step involves configuring a specific key with a Guard function, disabling a '
                            'parameter, and verifying the configuration file.',
             'tags': ['configuration', 'validation', 'hard_key', 'OXE'],
             'automation': 'automatable'},
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
             'intent': 'Navigate to hard keys menu and verify UI elements',
             'suggested_commands': ['Navigate to User/Device/Hard keys menu',
                                    "Verify title 'Edit maximum 2 keys'",
                                    'Check reset to default icon',
                                    'Verify radio buttons and key selection',
                                    'Validate options for ALE-30, ALE-300/400, and ALE-500',
                                    'Check info icon on ALE-300/400'],
             'confidence': 0.85,
             'explanation': 'The step describes navigating to the hard keys menu and verifying various UI elements and '
                            'options specific to different phone models.',
             'tags': ['navigation', 'UI_verification', 'hard_key', 'OXE'],
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
             'intent': 'Long press hard keys and verify UI elements',
             'suggested_commands': ['Long press F1/F2/F3/Triangle/Circle/Square key',
                                    "Verify title 'Edit maximum 2 keys'",
                                    'Check reset to default icon',
                                    'Verify radio buttons and key selection',
                                    'Validate options for ALE-30, ALE-300/400, and ALE-500',
                                    'Check info icon on ALE-300/400'],
             'confidence': 0.85,
             'explanation': 'The step involves long-pressing specific keys and verifying the UI elements and options '
                            'displayed for different phone models.',
             'tags': ['UI_verification', 'hard_key', 'long_press', 'OXE'],
             'automation': 'automatable'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'Verify F1/F2/F3 functions on ALE-500',
             'suggested_commands': ['Check F1 function: hold',
                                    'Check F2 function: transfer',
                                    'Check F3 function: conference'],
             'confidence': 0.9,
             'explanation': 'The step specifies verifying the functions assigned to F1, F2, and F3 keys on the ALE-500 '
                            'model.',
             'tags': ['function_verification', 'hard_key', 'ALE-500'],
             'automation': 'automatable'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly\n'
                         'and press the hard key:\n'
                         'Triangle : Will Return to the previous interface\n'
                         'Circle: will turn to the dashboard\n'
                         'Square :will makes the outgoing call to guard',
             'intent': 'Verify Triangle/Circle/Square keys on ALE-500',
             'suggested_commands': ['Check Triangle key: returns to previous interface',
                                    'Check Circle key: navigates to dashboard',
                                    'Check Square key: makes outgoing call to guard'],
             'confidence': 0.9,
             'explanation': 'The step involves verifying the names and functions of the Triangle, Circle, and Square '
                            'keys on the ALE-500 model.',
             'tags': ['function_verification', 'hard_key', 'ALE-500'],
             'automation': 'automatable'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Square  key',
             'expected': 'Will makes the second outgoing call to guard',
             'intent': 'Test the behavior of the Square key during an active call',
             'suggested_commands': ['Establish call with phone B', 'Press the Square key'],
             'confidence': 0.95,
             'explanation': 'The step describes a scenario where the Square key is pressed during an active call, and '
                            'the expected outcome is a second outgoing call to the guard.',
             'tags': ['call_handling', 'key_functionality', 'outgoing_call'],
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F3 key',
             'expected': 'ALE-300/400:\n'
                         'Makes the outgoing call to the guard\n'
                         'and the screen display correctly\n'
                         'Adn during the conversation, the led of the F1/F3 is on,the led of the F2 is off',
             'intent': 'Test the behavior of the F3 key in idle mode',
             'suggested_commands': ['Verify phone is in idle mode', 'Press the F3 key'],
             'confidence': 0.92,
             'explanation': 'The step tests the functionality of the F3 key when the phone is idle, ensuring it '
                            'initiates an outgoing call to the guard and updates the screen and LED indicators '
                            'correctly.',
             'tags': ['idle_mode', 'key_functionality', 'outgoing_call', 'led_behavior'],
             'automation': 'automatable'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F3',
             'expected': 'ALE-300/400:\n'
                         'Makes the new outgoing call to the guard\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F1 is on,the led of the F2/F3 is off',
             'intent': 'Test the behavior of the F3 key during an active call',
             'suggested_commands': ['Establish a call', 'Press the F3 key during the conversation'],
             'confidence': 0.93,
             'explanation': "The step evaluates the F3 key's functionality during an active call, ensuring it "
                            'initiates a new outgoing call to the guard and updates the screen and LED indicators '
                            'appropriately.',
             'tags': ['call_handling', 'key_functionality', 'outgoing_call', 'led_behavior'],
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath',
             'intent': 'Test the behavior of the F1 key during a normal call',
             'suggested_commands': ['Establish a normal call', 'Press the F1 key'],
             'confidence': 0.94,
             'explanation': "The step tests the F1 key's functionality during a normal call, ensuring it holds the "
                            'call and changes the LED behavior to breathing mode.',
             'tags': ['call_handling', 'key_functionality', 'led_behavior'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls the led of the F1/F2 is on, the led of the F3 is off\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls',
             'intent': 'Test the behavior of the F2 key during two active calls',
             'suggested_commands': ['Establish two normal calls', 'Press the F2 key'],
             'confidence': 0.91,
             'explanation': "The step evaluates the F2 key's functionality when two calls are active, ensuring it "
                            'exits both calls as expected.',
             'tags': ['call_handling', 'key_functionality', 'multi_call_management'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'Configure programmable key on OXE',
             'suggested_commands': ['Access OXE user interface',
                                    'Navigate to programmable key settings',
                                    "Set progkey 124 to 'Not Assigned'"],
             'confidence': 0.95,
             'explanation': "The step involves configuring a programmable key (progkey 124) on the OXE system to 'Not "
                            "Assigned'. This is a straightforward configuration task.",
             'tags': ['OXE', 'programmable_key', 'configuration'],
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
             'intent': 'Access hard keys menu and verify options',
             'suggested_commands': ['Enter hard keys menu via User/Device/Hard keys',
                                    'Long press F1/F2/F3/Triangle/Circle/Square key',
                                    'Verify displayed options and icons for each phone model'],
             'confidence': 0.9,
             'explanation': 'The step describes accessing the hard keys menu and verifying the options and icons '
                            'displayed for different phone models. This requires interaction with the phone and visual '
                            'verification.',
             'tags': ['hard_keys', 'menu_navigation', 'verification'],
             'automation': 'manual'}]},
 {'title': 'RQPLEIAD_180_32_Hard_Key_OXE_Define_Key 1&2_Lock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'set the progkey 123: programmed with the Emergency function on position 1\n'
                     'set the progkey 124: programmed with the Guard function on position 2\n'
                     'And the lock parameter are enabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,1" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,position2,xxx,0,1" override="true"/>',
             'intent': 'Program hard keys with specific functions and verify configuration file',
             'suggested_commands': ['Program key 123 with Emergency function',
                                    'Program key 124 with Guard function',
                                    'Enable lock parameter',
                                    'Update and verify configuration file'],
             'confidence': 0.95,
             'explanation': 'The step involves programming specific keys with predefined functions and verifying the '
                            'configuration file for correctness.',
             'tags': ['configuration', 'hard_keys', 'OXE', 'verification'],
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
             'intent': 'Access hard keys menu and verify key settings',
             'suggested_commands': ['Navigate to User/Device/Hard keys menu',
                                    'Verify admin-defined keys',
                                    'Check reset to default icon state',
                                    'Verify hard key options and icons for different models'],
             'confidence': 0.9,
             'explanation': 'The step involves accessing the hard keys menu and verifying the settings and options '
                            'displayed for different phone models.',
             'tags': ['menu_navigation', 'hard_keys', 'verification', 'UI'],
             'automation': 'needs_context'},
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
             'intent': 'Long press hard keys and verify settings',
             'suggested_commands': ['Long press F1/F2/F3 keys',
                                    'Verify admin-defined keys',
                                    'Check reset to default icon state',
                                    'Verify hard key options and icons for different models'],
             'confidence': 0.88,
             'explanation': 'The step involves testing the long press functionality of hard keys and verifying the '
                            'displayed settings for different phone models.',
             'tags': ['hard_keys', 'long_press', 'verification', 'UI'],
             'automation': 'needs_context'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\n'
                     'enable or disable the lock\n'
                     'then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation, the led of the F1/F2/F3 is off',
             'intent': 'Test lock functionality and emergency call behavior',
             'suggested_commands': ['Ensure phone is in idle mode',
                                    'Enable or disable lock',
                                    'Press F1 key',
                                    'Verify emergency call initiation and screen display'],
             'confidence': 0.92,
             'explanation': 'The step tests the lock functionality and verifies the behavior of the F1 key in '
                            'initiating an emergency call.',
             'tags': ['lock_functionality', 'emergency_call', 'idle_mode', 'verification'],
             'automation': 'needs_context'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Will makes the new outgoing call to the emergency\n'
                         'and the screen display correctly',
             'intent': 'Test emergency call initiation during an active call',
             'suggested_commands': ['Establish a call',
                                    'Press F1 key during conversation',
                                    'Verify new emergency call initiation and screen display'],
             'confidence': 0.93,
             'explanation': 'The step tests the behavior of the F1 key in initiating a new emergency call during an '
                            'active conversation.',
             'tags': ['emergency_call', 'active_call', 'verification'],
             'automation': 'needs_context'},
            {'step': 'Phone is idle then press the F2 Key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the guard\n'
                         'During the conversation, the led of the F1/F2/F3 is off',
             'intent': 'Test F2 key functionality during idle state',
             'suggested_commands': ['Press F2 key', 'Verify outgoing call to guard', 'Check LED status of F1/F2/F3'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the behavior of the F2 key when the phone is idle, including '
                            'making an outgoing call and checking LED status.',
             'tags': ['idle_state', 'F2_key', 'outgoing_call', 'LED_status'],
             'automation': 'automatable'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Will makes the new outgoing call to the guard\n'
                         'and the screen display correctly',
             'intent': 'Test F2 key functionality during an active call',
             'suggested_commands': ['Establish a call',
                                    'Press F2 key during conversation',
                                    'Verify new outgoing call to guard',
                                    'Check screen display'],
             'confidence': 0.95,
             'explanation': 'The step tests the behavior of the F2 key during an active call, ensuring it initiates a '
                            'new call and updates the screen correctly.',
             'tags': ['active_call', 'F2_key', 'outgoing_call', 'screen_display'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls,\n'
                     'the led of the F3 is on,the led of the F1/F2 is off\n'
                     'then press the F3 key',
             'expected': 'ALE-300/400:\nwill make the conference call,and led of the F3 key is breath',
             'intent': 'Test F3 key functionality for conference call',
             'suggested_commands': ['Establish two normal calls',
                                    'Verify LED status of F1/F2/F3',
                                    'Press F3 key',
                                    'Verify conference call initiation',
                                    'Check F3 LED breathing'],
             'confidence': 0.9,
             'explanation': 'The step verifies the functionality of the F3 key to initiate a conference call and '
                            'checks the LED behavior.',
             'tags': ['conference_call', 'F3_key', 'LED_status'],
             'automation': 'automatable'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will makes the outgoing call to emergency\n'
                         'Circle: Will makes the outgoing call to guard\n'
                         'Square :The screen brightness will decreased',
             'intent': 'Test Triangle/Circle/Square key functionality on ALE-500',
             'suggested_commands': ['Check Triangle/Circle/Square key names and colors',
                                    'Press Triangle key and verify emergency call',
                                    'Press Circle key and verify guard call',
                                    'Press Square key and verify screen brightness decrease'],
             'confidence': 0.9,
             'explanation': 'The step tests the functionality of the Triangle, Circle, and Square keys on the ALE-500, '
                            'including their labels, colors, and actions.',
             'tags': ['ALE-500', 'hard_keys', 'emergency_call', 'guard_call', 'screen_brightness'],
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Circle key',
             'expected': 'Will makes the second outgoing call to emergency/guard',
             'intent': 'Test Triangle/Circle key functionality during an active call on ALE-500',
             'suggested_commands': ['Establish a call with phone B',
                                    'Press Triangle key and verify emergency call',
                                    'Press Circle key and verify guard call'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of the Triangle and Circle keys on the ALE-500 during an '
                            'active call, ensuring they initiate the correct outgoing calls.',
             'tags': ['ALE-500', 'active_call', 'Triangle_key', 'Circle_key', 'outgoing_call'],
             'automation': 'automatable'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'Verify the functionality of F1/F2/F3 keys on ALE-500',
             'suggested_commands': ["Test F1 key for 'hold' function",
                                    "Test F2 key for 'transfer' function",
                                    "Test F3 key for 'conference' function"],
             'confidence': 0.95,
             'explanation': 'The step involves checking specific functions of the F1, F2, and F3 keys on the ALE-500 '
                            'device.',
             'tags': ['functionality', 'key testing', 'ALE-500'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': "Program keys 123 and 124 on OXE as 'Not Assigned'",
             'suggested_commands': ['Access OXE programming interface',
                                    "Set progkey 123 and 124 to 'Not Assigned'",
                                    'Verify settings match expected XML configuration'],
             'confidence': 0.92,
             'explanation': 'The step involves programming specific keys on OXE and verifying the configuration '
                            'matches the expected XML output.',
             'tags': ['OXE programming', 'key configuration', 'XML validation'],
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
             'intent': 'Access hard keys menu and verify options for ALE devices',
             'suggested_commands': ['Enter hard keys menu via User/Device/Hard keys',
                                    'Long press specific keys to access menu',
                                    'Verify displayed options for ALE-30, ALE-300/400, and ALE-500'],
             'confidence': 0.93,
             'explanation': 'The step involves accessing the hard keys menu and verifying the available options for '
                            'different ALE devices.',
             'tags': ['menu navigation', 'key options', 'device-specific testing'],
             'automation': 'manual'}]},
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
             'intent': 'Configure and validate hard key programming',
             'suggested_commands': ['Program key 123 with Emergency function',
                                    'Program key 124 with Guard function',
                                    'Update configuration file',
                                    'Verify configuration file settings'],
             'confidence': 0.95,
             'explanation': 'The step involves programming keys with specific functions, updating the configuration '
                            'file, and verifying the settings. This is a common configuration and validation task.',
             'tags': ['configuration', 'validation', 'hard_keys', 'OXE'],
             'automation': 'automatable'},
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
             'intent': 'Access and verify hard keys menu',
             'suggested_commands': ['Navigate to User/Device/Hard keys menu',
                                    'Verify menu title and icons',
                                    'Check radio button display',
                                    'Verify hard key names and selection states',
                                    'Check options for ALE-30, ALE-300/400, and ALE-500'],
             'confidence': 0.9,
             'explanation': 'The step involves accessing the hard keys menu and verifying the UI elements and options '
                            'for different device models. This is a UI validation task.',
             'tags': ['UI_validation', 'menu_navigation', 'hard_keys', 'OXE'],
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
             'intent': 'Long press hard key and verify options',
             'suggested_commands': ['Long press F1/F2/F3 key',
                                    'Verify menu title and icons',
                                    'Check radio button display',
                                    'Verify hard key names and selection states',
                                    'Check options for ALE-30, ALE-300/400, and ALE-500'],
             'confidence': 0.9,
             'explanation': 'The step involves performing a long press on specific keys and verifying the resulting UI '
                            'elements and options. This is a UI interaction and validation task.',
             'tags': ['UI_interaction', 'UI_validation', 'hard_keys', 'OXE'],
             'automation': 'automatable'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'Attempt to select more than allowed keys',
             'suggested_commands': ['Press a remaining key after selecting two keys',
                                    'Verify popup message for exceeding key limit'],
             'confidence': 0.85,
             'explanation': "The step tests the system's behavior when the user attempts to select more keys than "
                            'allowed. This is a boundary condition validation.',
             'tags': ['boundary_testing', 'error_handling', 'hard_keys', 'OXE'],
             'automation': 'automatable'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the Guard\n'
                         'and the screen display corectly\n'
                         'And during the conversation, thel ed of the F1 is on,the led of the F2/F3 is off',
             'intent': 'Initiate call using hard key and verify behavior',
             'suggested_commands': ['Ensure phone is in idle mode',
                                    'Press F2 key',
                                    'Verify outgoing call to Guard',
                                    'Check screen display during call',
                                    'Verify LED states during conversation'],
             'confidence': 0.9,
             'explanation': 'The step involves initiating a call using a hard key and verifying the call behavior, '
                            'screen display, and LED states. This is a functional and UI validation task.',
             'tags': ['functional_testing', 'UI_validation', 'hard_keys', 'OXE'],
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call then press the F2 key',
             'expected': 'ALE-30/300/400:\nMakes the new outgoing call to the Guard\nand the screen display corectly',
             'intent': 'Test F2 key functionality during an active call',
             'suggested_commands': ['Establish call',
                                    'Press F2 key',
                                    'Verify outgoing call to Guard',
                                    'Check screen display'],
             'confidence': 0.95,
             'explanation': 'The step describes pressing the F2 key during an active call and verifying the expected '
                            'behavior, which includes making an outgoing call to the Guard and correct screen display.',
             'tags': ['F2_key', 'call_handling', 'screen_display'],
             'automation': 'automatable'},
            {'step': 'Phone is idle then press the F3 key',
             'expected': 'ALE-300/400:\n'
                         'Makes the outgoing call to the Emergency\n'
                         'and the screen display corectly\n'
                         'During the conversation, the led of the F1 is on,the led of the F2/F3 is off',
             'intent': 'Test F3 key functionality when phone is idle',
             'suggested_commands': ['Ensure phone is idle',
                                    'Press F3 key',
                                    'Verify outgoing call to Emergency',
                                    'Check screen display',
                                    'Verify LED status of F1, F2, F3'],
             'confidence': 0.9,
             'explanation': 'The step involves pressing the F3 key when the phone is idle and verifying the outgoing '
                            'call to Emergency, screen display, and LED statuses.',
             'tags': ['F3_key', 'call_handling', 'LED_status', 'screen_display'],
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call then press the F3 key',
             'expected': 'ALE-300/400:\nMakes the new outgoing call to the Emergency\nand the screen display corectly',
             'intent': 'Test F3 key functionality during an active call',
             'suggested_commands': ['Establish call',
                                    'Press F3 key',
                                    'Verify outgoing call to Emergency',
                                    'Check screen display'],
             'confidence': 0.95,
             'explanation': 'The step describes pressing the F3 key during an active call and verifying the expected '
                            'behavior, which includes making an outgoing call to Emergency and correct screen display.',
             'tags': ['F3_key', 'call_handling', 'screen_display'],
             'automation': 'automatable'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath',
             'intent': 'Test F1 key functionality during an active call',
             'suggested_commands': ['Establish call',
                                    'Verify F1 LED is on',
                                    'Press F1 key',
                                    'Verify call is held',
                                    'Check F1 LED breathing'],
             'confidence': 0.9,
             'explanation': 'The step involves pressing the F1 key during an active call and verifying that the call '
                            'is held and the F1 LED changes to breathing mode.',
             'tags': ['F1_key', 'call_handling', 'LED_status'],
             'automation': 'automatable'},
            {'step': 'Phone establish two normal calls',
             'expected': 'the led of the F1 is on, the led of the F2/F3 is off',
             'intent': 'Verify LED statuses during two active calls',
             'suggested_commands': ['Establish two calls', 'Verify F1 LED is on', 'Verify F2 and F3 LEDs are off'],
             'confidence': 0.85,
             'explanation': 'The step involves establishing two active calls and verifying the LED statuses of F1, F2, '
                            'and F3 keys.',
             'tags': ['LED_status', 'call_handling', 'F1_key', 'F2_key', 'F3_key'],
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will Return to the previous interface\n'
                         'Circle: Will makes the outgoing call to guard\n'
                         'Square :Will makes the outgoing call to emergency',
             'intent': 'Verify hard key functionality and display',
             'suggested_commands': ['Check Triangle key functionality',
                                    'Check Circle key functionality',
                                    'Check Square key functionality'],
             'confidence': 0.95,
             'explanation': 'The step involves verifying the functionality and display of three specific hard keys on '
                            'the ALE-500 device.',
             'tags': ['hard_key', 'functionality', 'display', 'emergency'],
             'automation': 'automatable'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Circle key',
             'expected': 'Will makes the second outgoing call to guard/emergency',
             'intent': 'Verify hard key behavior during an active call',
             'suggested_commands': ['Establish call between two phones', 'Press Triangle key', 'Press Circle key'],
             'confidence': 0.9,
             'explanation': 'The step tests the behavior of Triangle and Circle keys during an active call on the '
                            'ALE-500 device.',
             'tags': ['hard_key', 'active_call', 'behavior'],
             'automation': 'needs_context'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'Verify F1, F2, F3 function keys',
             'suggested_commands': ['Test F1 key for hold functionality',
                                    'Test F2 key for transfer functionality',
                                    'Test F3 key for conference functionality'],
             'confidence': 0.92,
             'explanation': 'The step involves verifying the functionality of F1, F2, and F3 keys on the ALE-500 '
                            'device.',
             'tags': ['function_keys', 'hold', 'transfer', 'conference'],
             'automation': 'automatable'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'Program and verify unassigned keys',
             'suggested_commands': ['Program key 123 as unassigned',
                                    'Program key 124 as unassigned',
                                    'Verify key settings in configuration'],
             'confidence': 0.88,
             'explanation': 'The step involves programming specific keys as unassigned and verifying their '
                            'configuration settings.',
             'tags': ['program_keys', 'unassigned', 'configuration'],
             'automation': 'manual'},
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
             'intent': 'Verify hard keys menu and options',
             'suggested_commands': ['Enter hard keys menu',
                                    'Verify menu title and icons',
                                    'Verify options for different ALE models'],
             'confidence': 0.93,
             'explanation': 'The step tests the hard keys menu and available options for different ALE models.',
             'tags': ['hard_keys_menu', 'options', 'ALE_models'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_34_Hard_Key_OXE_Define_Key 1&3_Unlock',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\n'
                     'set the progkey 123: programmed with the Emergency function on position 1\n'
                     'set the progkey 124: programmed with the Guard function on position 3\n'
                     'And the lock parameter are all disabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,position3,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85517 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85517 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85517 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85517 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85517 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85517 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85517 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85517 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\n'
                     'enable or disable the lock\n'
                     'then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and screen display correctly\n'
                         'and during the conversation, the led of the F1/F2/F3 is off',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85517 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85517 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F3 key',
             'expected': 'ALE-300/400:\nMakes the outgoing call to the Guard\nand screen display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone establish one normal calls,the led of the F1/F2/F3 IS OFF\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nMakes the new outgoing call to the emergency\nand screen display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone establish one normal calls,the led of the F1/F2/F3 IS OFF\nthen press the F3 key',
             'expected': 'ALE-300/400:\nMakes the new outgoing call to the Guard\nand screen display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone establish two normal calls, the led of the F2 is on,the led of F1/F3 is off\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nCheck the Triangle Triangle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will makes the outgoing call to emergency\n'
                         'Circle: will turn to the homepage\n'
                         'Square :Will makes the outgoing call to guard',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Square key',
             'expected': 'Will makes the second outgoing call to emergency/guard',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F3 key',
             'expected': 'ALE-300/400:\nMakes the outgoing call to the Guard\nand screen display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone establish one normal calls,the led of the F1/F2/F3 IS OFF\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nMakes the new outgoing call to the emergency\nand screen display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone establish one normal calls,the led of the F1/F2/F3 IS OFF\nthen press the F3 key',
             'expected': 'ALE-300/400:\nMakes the new outgoing call to the Guard\nand screen display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone establish two normal calls, the led of the F2 is on,the led of F1/F3 is off\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nCheck the Triangle Triangle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will makes the outgoing call to emergency\n'
                         'Circle: will turn to the homepage\n'
                         'Square :Will makes the outgoing call to guard',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Square key',
             'expected': 'Will makes the second outgoing call to emergency/guard',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85399 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85399 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_35_Hard_Key_OXE_Define_Two_Lock_Hard_Key',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124, \nand Lock" parameter is enable"',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,1" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,1" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only the defined key displays the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only the defined key displays the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the function of the two keys',
             'expected': 'the function is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124, \nand Lock" parameter is enable"',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,1" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,1" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85335 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85335 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only the defined key displays the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85335 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85335 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only the defined key displays the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85335 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85335 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the function of the two keys',
             'expected': 'the function is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85335 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85335 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_36_Hard_Key_OXE_Define_One_Lock_Hard_Key_Update',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nonly define one of progkey 123 or 124\nand Lock" parameter is enabled"',
             'expected': '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the function of the defined key',
             'expected': 'the function is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     '\n'
                     'selectone undefined key then press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'And the reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Repeat steps 5-8',
             'expected': '',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\nonly define one of progkey 123 or 124\nand Lock" parameter is enabled"',
             'expected': '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the function of the defined key',
             'expected': 'the function is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     '\n'
                     'selectone undefined key then press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'And the reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Repeat steps 5-8',
             'expected': '',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85217 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85217 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_37_Hard_Key_OXE_Define_One_Lock_Hard_Key_One_Unlock_Hard_Key_Modify',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124,\none key is locked and one key is unlocked',
             'expected': 'lock key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>\n'
                         'unlocked key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     '\n'
                     'Select  the defined key which is unlocked and press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Repeat steps 4-7',
             'expected': '',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124,\none key is locked and one key is unlocked',
             'expected': 'lock key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>\n'
                         'unlocked key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     '\n'
                     'Select  the defined key which is unlocked and press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Repeat steps 4-7',
             'expected': '',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_38_Hard_Key_OXE_Define_One_Lock_Hard_Key_One_Unlock_Hard_Key_Reset_To_Default',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124,\none key is locked and one key is unlocked',
             'expected': 'lock key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>\n'
                         'unlocked key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the reset to default icon',
             'expected': 'The lock defined key: Not affected\nthe unlock defined key: return to the default',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124,\none key is locked and one key is unlocked',
             'expected': 'lock key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>\n'
                         'unlocked key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85097 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85097 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85097 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85097 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85097 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85097 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the reset to default icon',
             'expected': 'The lock defined key: Not affected\nthe unlock defined key: return to the default',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 85097 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 85097 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_39_Hard_Key_OXE_Define_Two_Unlock_Hard_Key_Modify',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124,\nthe lock paramter are all disabled',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     'press the edit button of the defined key which is unlocked',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Long press the unlocked hard key\nRepeat steps 4-7',
             'expected': '',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124,\nthe lock paramter are all disabled',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 55 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 55 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 55 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 55 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 55 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 55 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     'press the edit button of the defined key which is unlocked',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 55 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 55 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 55 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 55 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 55 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 55 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 55 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 55 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Long press the unlocked hard key\nRepeat steps 4-7',
             'expected': '',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 55 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 55 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_40_Hard_Key_OXE_Define_Two_Unlock_Hard_Key_Reset_To_Default',
  'preconditions': '',
  'steps': [{'step': 'OXE: user---program key\nset the progkey 123 and 124,\nthe lock paramter are all disabled',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124,\nthe lock paramter are all disabled',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,0" override="true"/>',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84916 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84916 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84916 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84916 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84916 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84916 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84916 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84916 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Define one key :\nSelect the undefined key and press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type then press the + button',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Repeat steps 2-4',
             'expected': 'These two keys are selected and the edit icon is displayed on the right\n'
                         'And the two hard key names are light',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400:\nPress the i icon',
             'expected': 'display the help screen: change the physical button',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'first defined hard key: is the key 123 on OXE side\n'
                         'second defined hard key: is the key 124 on OXE side\n'
                         'and parameter of the lock: disabled',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': "OXE: Doesn't configure the hard keys \n"
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Define one key :\nSelect the undefined key and press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type then press the + button',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Repeat steps 2-4',
             'expected': 'These two keys are selected and the edit icon is displayed on the right\n'
                         'And the two hard key names are light',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400:\nPress the i icon',
             'expected': 'display the help screen: change the physical button',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'first defined hard key: is the key 123 on OXE side\n'
                         'second defined hard key: is the key 124 on OXE side\n'
                         'and parameter of the lock: disabled',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'press one key whitch not defined then press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'he fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Repeat steps 2-4',
             'expected': 'These two keys are selected and the edit icon is displayed on the right\n'
                         'And the two hard key names are light',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400:\nPress the i icon',
             'expected': 'display the help screen: change the physical button',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'first defined hard key: is the key 123 on OXE side\n'
                         'second defined hard key: is the key 124 on OXE side\n'
                         'and parameter of the lock: disabled',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': "OXE: Doesn't configure the hard keys \n\nEnter the hard keys menu:\nUser/Device/Hard keys",
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84850 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84850 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'press one key whitch not defined then press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84850 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84850 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84850 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84850 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the hard key',
             'expected': 'he fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84850 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84850 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Repeat steps 2-4',
             'expected': 'These two keys are selected and the edit icon is displayed on the right\n'
                         'And the two hard key names are light',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84850 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84850 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84850 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84850 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'ALE-300/400:\nPress the i icon',
             'expected': 'display the help screen: change the physical button',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84850 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84850 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'first defined hard key: is the key 123 on OXE side\n'
                         'second defined hard key: is the key 124 on OXE side\n'
                         'and parameter of the lock: disabled',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84850 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84850 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Select the defined key\nDefine the two keys to another function',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'Phone sends the notify to the OXE\nthe progkey 123 and 124 of the OXE: the content is update',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone configure 2 hard keys  \nLong press the defined hard key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84791 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84791 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Select the defined key\nDefine the two keys to another function',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84791 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84791 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84791 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84791 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'Phone sends the notify to the OXE\nthe progkey 123 and 124 of the OXE: the content is update',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84791 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84791 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the function of the key to its default state',
             'expected': 'ALE-30:\n'
                         'F1/hold and F2/transfer\n'
                         'ALE-300/400:\n'
                         'F1/hold and F2/transfer and F3/conference\n'
                         'ALE-500:\n'
                         'Triangle/back and Circle/home and Square/low power',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'the program key 123 and 124 is not defined',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone configure 2 hard keys\nLong press the hard key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84734 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84734 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84734 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84734 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the function of the key to its default state',
             'expected': 'ALE-30:\n'
                         'F1/hold and F2/transfer\n'
                         'ALE-300/400:\n'
                         'F1/hold and F2/transfer and F3/conference\n'
                         'ALE-500:\n'
                         'Triangle/back and Circle/home and Square/low power',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84734 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84734 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'the program key 123 and 124 is not defined',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84734 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84734 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Select the defined key\nDefine the two keys to another function',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'Phone sends the notify to the OXE\nthe progkey 123 and 124 of the OXE: the content is update',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Select the defined key\nDefine the two keys to another function',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the new function of the key',
             'expected': 'the fucntion is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'Phone sends the notify to the OXE\nthe progkey 123 and 124 of the OXE: the content is update',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 50 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 50 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the function of the key to its default state',
             'expected': 'ALE-30:\n'
                         'two options: F1/hold and F2/transfer\n'
                         'ALE-300/400:\n'
                         'F1/hold and F2/transfer and F3/conference\n'
                         'ALE-500:\n'
                         'three options:Triangle/back and Circle/home and Square/low power',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'the program key 123 and 124 is not deffned',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84668 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84668 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the reset to default icon',
             'expected': 'all hard key display the default content',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84668 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84668 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Check the function of the key to its default state',
             'expected': 'ALE-30:\n'
                         'two options: F1/hold and F2/transfer\n'
                         'ALE-300/400:\n'
                         'F1/hold and F2/transfer and F3/conference\n'
                         'ALE-500:\n'
                         'three options:Triangle/back and Circle/home and Square/low power',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84668 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84668 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the two keys of the OXE',
             'expected': 'the program key 123 and 124 is not deffned',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84668 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84668 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Select the defined key\nDefine the two keys to default function',
             'expected': 'The two hard keys are selected and hard key name is light\n'
                         'cap icon:\n'
                         'ALE-30 :hold/transfer\n'
                         'ALE-300/400: hold/transfer/conference\n'
                         'ALE-500: Triangle/Circle/Square',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the hard key',
             'expected': 'The function is the default',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84610 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84610 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Select the defined key\nDefine the two keys to default function',
             'expected': 'The two hard keys are selected and hard key name is light\n'
                         'cap icon:\n'
                         'ALE-30 :hold/transfer\n'
                         'ALE-300/400: hold/transfer/conference\n'
                         'ALE-500: Triangle/Circle/Square',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84610 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84610 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the hard key',
             'expected': 'The function is the default',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84610 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84610 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Unselected the two defined keys',
             'expected': 'The two keys ard not selected and hard key name is grey',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the two hard keys',
             'expected': 'The function is the default',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Select the two leys again',
             'expected': 'The two keys ard selected and hard key name is light',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84552 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84552 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Unselected the two defined keys',
             'expected': 'The two keys ard not selected and hard key name is grey',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84552 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84552 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Press the two hard keys',
             'expected': 'The function is the default',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84552 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84552 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Select the two leys again',
             'expected': 'The two keys ard selected and hard key name is light',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84552 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84552 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
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
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Define the key to phone number/Immediate forward/Deactivate forward"Welcome '
                     'desk/Operator/Voicemail/"Redial/ Last caller/Cleaning mode/Meet me/Guard/Do not '
                     'disturb/Lock/Auto answer/Hunting group\n'
                     '\n'
                     'check the cap icon and function',
             'expected': 'ALE-30/300/400:F1/F2/abc cap icon\n'
                         'ALE-500: Triangle/Circle/Square Cap icon\n'
                         '\n'
                         'The function of the key is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Define the key to Hold/Transfer/Conference\ncheck the cap icon and function',
             'expected': 'ALE-30/300/400: Hold/Transfer/Conference cap icon\n'
                         'ALE-500:\n'
                         'Triangle/Circle/Square cap icon\n'
                         'Press the hard key:\n'
                         'the function of the key is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Define the key to Emergency\ncheck the cap icon and function',
             'expected': 'ALE-30/300/400: Red cap icon\n'
                         'ALE-500:\n'
                         'Triangle/Circle/Square cap icon, and the font color of the dashboard is red\n'
                         'Press the hard key:\n'
                         'Will makes the outgoing call to Emergency',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'When the hard key is not defined\ncheck the cap icon',
             'expected': 'ALE-30/300/400:\n'
                         'Hold cap icon\n'
                         'Transfer cap icon\n'
                         'Conference cap icon\n'
                         'ALE-500:\n'
                         'Triangle cap icon\n'
                         'Circle cap icon\n'
                         'Square cap icon',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Define the key to phone number/Immediate forward/Deactivate forward"Welcome '
                     'desk/Operator/Voicemail/"Redial/ Last caller/Cleaning mode/Meet me/Guard/Do not '
                     'disturb/Lock/Auto answer/Hunting group\n'
                     '\n'
                     'check the cap icon and function',
             'expected': 'ALE-30/300/400:F1/F2/abc cap icon\n'
                         'ALE-500: Triangle/Circle/Square Cap icon\n'
                         '\n'
                         'The function of the key is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Define the key to Hold/Transfer/Conference\ncheck the cap icon and function',
             'expected': 'ALE-30/300/400: Hold/Transfer/Conference cap icon\n'
                         'ALE-500:\n'
                         'Triangle/Circle/Square cap icon\n'
                         'Press the hard key:\n'
                         'the function of the key is correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Define the key to Emergency\ncheck the cap icon and function',
             'expected': 'ALE-30/300/400: Red cap icon\n'
                         'ALE-500:\n'
                         'Triangle/Circle/Square cap icon, and the font color of the dashboard is red\n'
                         'Press the hard key:\n'
                         'Will makes the outgoing call to Emergency',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please wait 49 seconds before "
                            "retrying.', 'details': 'Rate limit of 10 per 60s exceeded for UserByModelByMinute. Please "
                            "wait 49 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_50_Hard_Key_Reset',
  'preconditions': '',
  'steps': [{'step': 'There are 2 defined hard keys.\n'
                     '\n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Restart the phone \nthen\nShort/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'There are 2 defined hard keys.\n'
                     '\n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84485 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84485 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Restart the phone \nthen\nShort/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84485 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84485 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]},
 {'title': 'RQPLEIAD_180_51_Hard_Key_Reset_To_Factory',
  'preconditions': '',
  'steps': [{'step': 'There are 1 defined hard keys. \n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone reset flash, then the phone connects the OXE again\n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'These hard keys will not affected:\n'
                         '\n'
                         'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the undefined key',
             'expected': 'Still the default function',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': 'LLM unavailable; skipped enrichment',
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'There are 1 defined hard keys. \n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84428 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84428 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'Phone reset flash, then the phone connects the OXE again\n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'These hard keys will not affected:\n'
                         '\n'
                         'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84428 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84428 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'},
            {'step': 'check the undefined key',
             'expected': 'Still the default function',
             'intent': 'unknown',
             'suggested_commands': [],
             'confidence': 0.0,
             'explanation': "Enrichment failed: Error code: 429 - {'error': {'code': 'RateLimitReached', 'message': "
                            "'Rate limit of 100 per 86400s exceeded for UserByModelByDay. Please wait 84428 seconds "
                            "before retrying.', 'details': 'Rate limit of 100 per 86400s exceeded for "
                            "UserByModelByDay. Please wait 84428 seconds before retrying.'}}",
             'tags': ['llm_error', 'llm_unavailable'],
             'automation': 'needs_context'}]}]

@pytest.mark.generated
@pytest.mark.parametrize('case', CASES, ids=[c['title'] for c in CASES])
def test_rqpleiad_180_with_mapping(case, ssh_session, step_mapping_rules):
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
