from __future__ import annotations

import pprint
import pytest

# Auto-generated from TestRail export.
# Update step_mapping.yaml to map natural-language steps into SSH commands.

CASES = [{'title': 'RQPLEIAD_180_01_Create_Emergency_Program_Key',
  'preconditions': 'OXE: \nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': ({'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""'},
            {'step': 'Press Emergency call', 'expected': 'Display the create key screen'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly  (the phone and addon side)'})},
 {'title': 'RQPLEIAD_180_02_Create_Guard_Program_Key',
  'preconditions': 'OXE: \nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': ({'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""'},
            {'step': 'Press Guard call', 'expected': 'Display the create key screen'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly (phone and addon side)'})},
 {'title': 'RQPLEIAD_180_03_Create_Operator_Program_Key',
  'preconditions': 'OXE: \nmgr---SIP device management---DM profile---Operator number---xxxx',
  'steps': ({'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""'},
            {'step': 'Press Operator call', 'expected': 'Display the create key screen'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly (phone and addon side)'})},
 {'title': 'RQPLEIAD_180_04_Emergency_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Emergency program key',
  'steps': ({'step': 'Press the Emergency program key of the phone or addon',
             'expected': 'title:  Outgoing call\n'
                         'Red background  \n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call'},
            {'step': 'Remote side answer the call',
             'expected': 'title:  Conversation xx:xx\n'
                         'Red background  \n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Press the emergency avatar', 'expected': 'Display the emergency info'},
            {'step': 'press the new call button', 'expected': 'turn to the add new call screen'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call"},
            {'step': 'pick up the handset', 'expected': 'the voice will switch to handset'},
            {'step': 'Hang on the handset', 'expected': 'the voice will switch to handsfree'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call"},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing arrow)\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_05_Emergency_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': ({'step': 'Press the Emergency call log/ Emergency contact or dial the Emergency number',
             'expected': 'title: Outgoing call\n'
                         'Red background\n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Press the emergency avatar', 'expected': 'Display the emergency info'},
            {'step': 'press the new call button', 'expected': 'turn to the add new call screen'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call"},
            {'step': 'pick up the handset', 'expected': 'the voice will switch to handset'},
            {'step': 'Hang on the handset', 'expected': 'the voice will switch to handsfree'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call"},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing)\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_06_Emergency_Outgoing_Call_By_Dial_Hardcode_911/112',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': ({'step': 'Dial the 911 or 112',
             'expected': 'title: Outgoing call\n'
                         'Red background\n'
                         'display emergency avatar and release button(led is on)\n'
                         'and press the emergency avatar will turn to the info screen\n'
                         'if press the release key will release the call'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Press the emergency avatar', 'expected': 'Display the  info: 911 or 112'},
            {'step': 'press the new call button', 'expected': 'turn to the add new call screen'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call"},
            {'step': 'pick up the handset', 'expected': 'the voice will switch to handset'},
            {'step': 'Hang on the handset', 'expected': 'the voice will switch to handsfree'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call"},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log (outgoing )\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_07_Emergency_Outgoing_Call_With_Second_Normal_Incoming_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the emergency call is  kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar  + Incoming call"+ switch button"'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         'the emergency call is kept active\n'
                         'emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button'},
            {'step': 'Answer the new call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and normal call avatar\n'
                         'The exit and release button are grey (led is off)'},
            {'step': 'Press the exit /release button', 'expected': 'no action'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Emergency call log and the normal incoming call log\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_08_Emergency_Outgoing_Call_With_Second_Normal_Incoming_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the emergency call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the emergency call is kept active\n'
                         'emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button'},
            {'step': 'Press the silence button', 'expected': 'Stop ringing'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the not answered call log\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_09_Emergency_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone makes the new normal outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the emergency call is on hold\n'
                         'The emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect"},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and normal call avatar\n'
                         'The exit and release button are grey (led is off)'},
            {'step': 'Press the exit /release button', 'expected': 'No anction'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Emergency call loh and the normal outgoing call log\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_10_Emergency_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone makes the new normal outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the emergency call is on hold\n'
                         'The emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar +switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect"},
            {'step': 'Remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the unsuccessful call log\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_11_Guard_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Guard program key',
  'steps': ({'step': 'Press the Guard program key of the phone or addon',
             'expected': 'title: Outgoing call\n'
                         'Dark blue background\n'
                         'display Guard avatar and release button(led is on)\n'
                         'and press the Guard avatar will turn to the info screen\n'
                         'if press the release key will release the call'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Press the guard avatar', 'expected': 'Display the guard info'},
            {'step': 'press the new call button', 'expected': 'turn to the add new call screen'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call"},
            {'step': 'pick up the handset', 'expected': 'the voice will switch to handset'},
            {'step': 'Hang on the handset', 'expected': 'the voice will switch to handsfree'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call"},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log (outgoing)\nthe label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_12_Guard_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': ({'step': 'Press the Guard call log/ Guard  contact or dial the Guard  number',
             'expected': 'title: Outgoing call\n'
                         'Dark blue background\n'
                         'display Guard avatar and release button(led is on)\n'
                         'and press the Guard avatar will turn to the info screen\n'
                         'if press the release key will release the call'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Press the guard avatar', 'expected': 'Display the guard info'},
            {'step': 'press the new call button', 'expected': 'turn to the add new call screen'},
            {'step': 'press the hold key of the screen or the hold physical button',
             'expected': "no action， can't hold the call"},
            {'step': 'pick up the handset', 'expected': 'the voice will switch to handset'},
            {'step': 'Hang on the handset', 'expected': 'the voice will switch to handsfree'},
            {'step': 'press the release key of the screen or the release physical button',
             'expected': "no action， can't release the call"},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log (outgoing)\nthe label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_13_Guard_Ougoing_Call_With_Second_Normal_Incoming_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Guard call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Guard call is kept active\n'
                         'Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button'},
            {'step': 'Answer the new call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and normal call avatar\n'
                         'The exit and release button are grey (led is off)'},
            {'step': 'Press the exit /release button', 'expected': 'no action'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Guard call log and the normal incoming call log\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_14_Guard_Ougoing_Call_With_Second_Normal_Incoming_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Guard call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Guard call is kept active\n'
                         'Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button'},
            {'step': 'Press the silence button', 'expected': 'Stop ringing'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the not answered call log\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_15_Guard_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone makes the new normal outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the Guard call is on hold\n'
                         'The Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect"},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and normal call avatar\n'
                         'The exit and release button are grey (led is off)'},
            {'step': 'Press the exit /release button', 'expected': 'no action'},
            {'step': 'After the conference call is released, check the call log',
             'expected': 'Has the conference call log and the Guard call log and the normal outgoing call log\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_16_Guard_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone makes the new normal outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the Guard call is on hold\n'
                         'The Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar +switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect"},
            {'step': 'Remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the unsuccessful call log\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_17_Operator_Outgoing_Call_By_Program_Key',
  'preconditions': 'Phone has the Operator program key',
  'steps': ({'step': 'Press the Operator program key of the phone or addon',
             'expected': 'title: Outgoing call\n'
                         'white background\n'
                         'display Operator avatar and release button(led is on)\n'
                         'and press the Operator avatar will turn to the info screen\n'
                         'if press the release key will release the call'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Press the Operator avatar', 'expected': 'Display the Operator info'},
            {'step': 'Press the hold key of the screen or the hold physical key',
             'expected': 'will hold the call\n'
                         'title: On hold xx:xx\n'
                         'Blue background\n'
                         'display Operator avatar / hold / new call/ release button\n'
                         'the led of the hold is breath'},
            {'step': 'Press the hold key of the screen or the hold physical key again',
             'expected': 'will retrieve the call\n'
                         'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'pick up the handset', 'expected': 'the voice will switch to handset'},
            {'step': 'Hang on the handset or \npress the release key of the screen or the release physical button',
             'expected': 'will release the call'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log (outgoing)\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_18_Operator_Outgoing_Call_By_Dial_Number/Call log/Contact',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': ({'step': 'Press the Operator call log/ Operator contact or dial the Operator number',
             'expected': 'title: Outgoing call\n'
                         'white background\n'
                         'display Operator avatar and release button(led is on)\n'
                         'and press the Operator avatar will turn to the info screen\n'
                         'if press the release key will release the call'},
            {'step': 'Remote side answer the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Press the Operator avatar', 'expected': 'Display the Operator  info'},
            {'step': 'Press the hold key of the screen or the hold physical key',
             'expected': 'will hold the call\n'
                         'title: On hold xx:xx\n'
                         'Blue background\n'
                         'display Operator avatar / hold / new call/ release button\n'
                         'the led of the hold is breath'},
            {'step': 'Press the hold key of the screen or the hold physical key again',
             'expected': 'will retrieve the call\n'
                         'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'pick up the handset', 'expected': 'the voice will switch to handset'},
            {'step': 'Hang on the handset or \npress the release key of the screen or the release physical button',
             'expected': 'will release the call'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log (outgoing)\n'
                         'the label /avatar /name /number/date display correctly'})},
 {'title': 'RQPLEIAD_180_19_Operator_Outgoing_Call_With_Second_Normal_Imcoming_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Phone receives the incoming call',
             'expected': 'the Operator call is kept active\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Operator call is kept active\n'
                         'Operator call in the lower part of the screen:\n'
                         'purple background +Guard avatar +switch button'},
            {'step': 'Answer the new call',
             'expected': 'The new call in the upper part of the screen:\n'
                         'purple background+ normal avatar\n'
                         '\n'
                         'the Operator call will on hold\n'
                         'Operator  call in the lower part of the screen:\n'
                         'Blue background +Operator avatar + switch button\n'
                         '\n'
                         'The middle part: display the conference and transfer button'},
            {'step': 'Press the switch button then check the two call screen',
             'expected': 'The Operator  call in the upper part of the screen:\n'
                         'Purple background +Operator  avatar\n'
                         '\n'
                         'the new call will on hold\n'
                         'The new call in the lower part of the screen:\n'
                         'blue background+ normal avatar +switch button\n'
                         '\n'
                         'The middle part: display the conference and transfer button'},
            {'step': 'Press the conference button',
             'expected': 'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Operator  and normal call avatar\n'
                         'display the exit and release button'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator / normal incoming / conference call log\n'
                         'the label /avatar /number display correctly'})},
 {'title': 'RQPLEIAD_180_20_Operator_Outgoing_Call_With_Second_Normal_Imcoming_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Phone receives the normal incoming call',
             'expected': 'the Operator call is kept active\n'
                         '\n'
                         'The new call in the lower part of the screen:\n'
                         'white background+ normal avatar + Incoming call"+ switch button"'},
            {'step': 'press the switch button',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Incoming call"\n'
                         'white background+ normal avatar + answer / silence button\n'
                         '\n'
                         'the Operator call is kept active\n'
                         'Operator call in the lower part of the screen:\n'
                         'purple background +Guard avatar +switch button'},
            {'step': 'Press the silence button', 'expected': 'Stop ringing'},
            {'step': 'press the reject button / turn to voicemail button',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator / normal unanswered call log\n'
                         'the label /avatar /number display correctly'})},
 {'title': 'RQPLEIAD_180_21_Operator_Outgoing_Call_With_Second_Normal_Outgoing_Call_Answer',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Phone makes the new outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the Operatorcall is on hold\n'
                         'The Operator call in the lower part of the screen:\n'
                         'blue background +Guard avatar +switch button\n'
                         '\n'
                         'and display the transfer button'},
            {'step': 'If press the transfer button',
             'expected': 'exit the two calls\n'
                         'Call log has the Operator call log and normal call log\n'
                         'the label /avatar /number display correctly'},
            {'step': "If don't press the transfer button\nand remote side answer the call",
             'expected': 'The new call in the upper part of the screen:\n'
                         'purple background+ normal avatar \n'
                         '\n'
                         'the Operator  call will on hold\n'
                         'Operator call in the lower part of the screen:\n'
                         'blue background + Operator avatar + switch button\n'
                         '\n'
                         'The middle part: display the conference and transfer button'},
            {'step': 'Press the switch button then check the two call screen',
             'expected': 'The Operator call in the upper part of the screen:\n'
                         'Purple background +Operator avatar\n'
                         '\n'
                         'the new call will on hold\n'
                         'The new call in the lower part of the screen:\n'
                         'blue background+ normal avatar  + switch button\n'
                         '\n'
                         'The middle part: display the conference and transfer button'},
            {'step': 'press the transfer key', 'expected': 'exit the two calls'},
            {'step': 'check the call log',
             'expected': 'Has the Operator call log and the normal outgoing call log\n'
                         'the label /avatar /number display correctly'})},
 {'title': 'RQPLEIAD_180_22_Operator_Outgoing_Call_With_Second_Normal_Outgoing_Call_Reject',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Operator number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Phone makes the new outgoing call',
             'expected': 'The new call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'white background+ normal avatar + release button\n'
                         '\n'
                         'the Operatorcall is on hold\n'
                         'The Operator call in the lower part of the screen:\n'
                         'blue background +Guard avatar +switch button\n'
                         '\n'
                         'and display the transfer button'},
            {'step': 'remote side reject the call',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Release the call then check the call log',
             'expected': 'Has the Operator call log and the normal unsuccessful call log\n'
                         'the label /avatar /number display correctly'})},
 {'title': 'RQPLEIAD_180_23_Emergency_Call_With_Guard_Call',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile:\nEmergency  number----xxxx\nGuard number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Emergency',
             'expected': 'title: Conversation xx:xx\n'
                         'Red background\n'
                         'display emergency avatar / new call button(led is on)\n'
                         '\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone makes the new outgoing call to Guard',
             'expected': 'The Guard call in the upper part of the screen:\n'
                         '"Outgoing call"\n'
                         'Dark blue background+ Guard avatar + release button\n'
                         '\n'
                         'the emergency call is on hold\n'
                         'The emergency call in the lower part of the screen:\n'
                         'Red background +emergency avatar + switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect"},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Emergency and Guard call avatar\n'
                         'The exit and release button are grey (led is off)'},
            {'step': 'Press the exit /release button', 'expected': 'no action'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the Guard call log and the conference call log\n'
                         'the label /avatar /number display correctly'})},
 {'title': 'RQPLEIAD_180_24_Operator_Call_With_Emergency_Call',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile:\nEmergency number----xxxx\nOperator number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Operator',
             'expected': 'title: Conversation xx:xx\n'
                         'purple background\n'
                         'display Operator avatar / hold / new call/ release button(led is on)'},
            {'step': 'Phone makes the new outgoing call to Emergency',
             'expected': 'The Emergency call in the upper part of the screen:\n'
                         '"Emergency call"\n'
                         'Red background+ Emergency avatar + release button\n'
                         '\n'
                         'the Operator call is on hold\n'
                         'The Operator call in the lower part of the screen:\n'
                         'blue background +Operator avatar + switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect"},
            {'step': 'Remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the operator and Emergency call avatar\n'
                         'The exit and release button are grey (led is off)'},
            {'step': 'Press the exit /release button', 'expected': 'no action'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the emergency call log and the Operator call log and the conference call log\n'
                         'the label /avatar /number display correctly'})},
 {'title': 'RQPLEIAD_180_25_Guard_Call_With_Operator_Call',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile:\nOperator number----xxxx\nGuard number----xxxx',
  'steps': ({'step': 'Phone establish a call with the Guard',
             'expected': 'title: Conversation xx:xx\n'
                         'Dark blue background\n'
                         'display Guard avatar / new call button(led is on)\n'
                         '\n'
                         'The release/ hold button are grey (led is off)'},
            {'step': 'Phone makes the new outgoing call to Operator',
             'expected': 'The Operator call in the upper part of the screen:\n'
                         '"Operator call"\n'
                         'Purple background+ Operator avatar + release button\n'
                         '\n'
                         'the Guard call is on hold\n'
                         'The Guard call in the lower part of the screen:\n'
                         'Dark blue background +Guard avatar + switch button\n'
                         '\n'
                         "the transfer button is grey, and press the transfer physical key can't take effect"},
            {'step': 'remote side answer the call',
             'expected': 'Will make the conference call directly\n'
                         '\n'
                         'Conference xx:xx\n'
                         'Purple background\n'
                         'display the Guard and operator call avatar\n'
                         'The exit and release button are grey (led is off)'},
            {'step': 'Press the exit /release button', 'expected': 'no action'},
            {'step': 'After the call is released, check the call log',
             'expected': 'Has the Guard call log and the Operator call log and the conference call log\n'
                         'the label /avatar /number display correctly'})},
 {'title': 'RQPLEIAD_180_26_Light/Dark_Mode_Emergency/Guard/Operator_Call',
  'preconditions': 'OXE:\nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': ({'step': 'settings---device---appearance---loght/dark mode', 'expected': 'can modify  successfully'},
            {'step': 'check the Emergency outgoing call screen/ hold screen/ conversation screen',
             'expected': 'The background color at the very bottom of the screen:\n'
                         'light mode: white \n'
                         'dark mode: black'},
            {'step': 'check the Guard outgoing call screen/ hold screen/ conversation screen /conference screen',
             'expected': 'The background color at the very bottom of the screen:\nlight mode: white\ndark mode: black'},
            {'step': 'check the Operator outgoing call screen/ hold screen/ conversation screen /conference screen',
             'expected': 'The background color at the very bottom of the screen:\n'
                         'light mode: white\n'
                         'dark mode: black'})},
 {'title': 'RQPLEIAD_180_27_Hard_Key_Default',
  'preconditions': '',
  'steps': ({'step': "OXE:  Doesn't configure the hard keys on the phone\n"
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'},
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F1 key',
             'expected': 'ALE-30/300/400/500:\n'
                         'If disable the lock: no action\n'
                         'If enable the lock: will lock the phone'},
            {'step': 'Phone establish a normal call the led of the F1 is on\n'
                     'then press the F1 key\n'
                     'then press the F1 key again',
             'expected': 'ALE-30/300/400/500:\n'
                         'will hold the call, and led of the F1 key is breath\n'
                         'will retrieve the call. the led of the F1 key is on'},
            {'step': 'Phone establish two normal calls the led of the F1/F2/F3 is on\nthen press the F2 key',
             'expected': 'ALE-30/300/400/500:\nwill exit these two calls'},
            {'step': 'Phone establish two normal calls the led of the F1/F2/F3 is on\nthen press the F3 key',
             'expected': 'ALE-300/400/500:will make the conference call,and led of the F3 key is breath'},
            {'step': 'check the Triangle/Circle/Square on ALE500',
             'expected': 'The three keys name display correctly\n'
                         'and press the hard key:\n'
                         'Triangle : Will Return to the previous interface\n'
                         'Circle: will turn to the dashboard\n'
                         'Square :The screen brightness will decreased'})},
 {'title': 'RQPLEIAD_180_28_Hard_Key_OXE_Define_Position_Label_Recognition',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\n'
                     'set the progkey 123:programmed with the phone A number on position 1\n'
                     'mnemo:  position1\n'
                     'Phone update the config file then check the file\n'
                     '（/config/dm/config.xxxxxxx.xml）',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,x" override="true"/>'},
            {'step': 'press the hard key:\nALE-30/300/400: F1 key\nALE-500: Triangle Key',
             'expected': 'Will makes the outgoing call to the phone A'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 124:programmed with the phone B number on position 2\n'
                     'mnemo:  position_2\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position_2,30461,0,X" override="true"/>'},
            {'step': 'press the hard key:\nALE-30/300/400: F2 key\nALE-500: Circle Key',
             'expected': 'Will makes the outgoing call to the phone B'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 123:programmed with the phone C number on position 1\n'
                     'mnemo:  position 1\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position 1,xxx,0,x" override="true"/>'},
            {'step': 'press the hard key:\nALE-30/300/400: F1 key\nALE-500: Triangle Key',
             'expected': 'Will makes the outgoing call to the phone C'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 124:programmed with the phone D number on position 2\n'
                     'mnemo:  POSITION2\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,POSITION2,30461,0,X" override="true"/>'},
            {'step': 'press the hard key:\nALE-30/300/400: F2 key\nALE-500: Circle Key',
             'expected': 'Will makes the outgoing call to the phone D'},
            {'step': 'OXE: user---program key\n'
                     'set the progkey 123 and 124\n'
                     'mnemo:  the string is different to one of the “position1”, “position2”, “position3”',
             'expected': '.If and their equivalent as described in the two above points, by default, the key 120 is '
                         'mapped to “position1” and 121 to “position2'},
            {'step': 'press the hard key:\nALE-30: F1/F2 key\nALE-300/400: F1/F2/F3 key\nALE-500: Triangle/Circle Key',
             'expected': 'The function is directly'})},
 {'title': 'RQPLEIAD_180_29_Hard_Key_OXE_Define_Key1_Lock',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\n'
                     'Only set the progkey 123: programmed with phone A on position 1,and the lock parameter is '
                     'enabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,1" override="true"/>'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference'},
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
                         'Square :The screen brightness will decreased'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle key',
             'expected': 'Will makes the second outgoing call to phone A'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nWill makes the outgoing call to phone A'},
            {'step': 'Phone establish a call with phone B then press the F1',
             'expected': 'ALE-30/300/400:\nWill makes the second outgoing call to phone A'},
            {'step': 'Phone establish two normal calls the led of the F1 is off, the led of the F2/F3 is on\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls'},
            {'step': 'Phone establish two normal calls the led of the F1 is off, the led of the F2/F3 is on\n'
                     'then press the F3 key',
             'expected': 'ALE-30/300/400:\nwill makes the conference call, and the led of the conference is breath'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>'},
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'})},
 {'title': 'RQPLEIAD_180_30_Hard_Key_OXE_Define_Key2_Unlock',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\n'
                     'Only set the progkey 124: programmed with the Emergency function on position 2,and the lock '
                     'parameter is disabled\n'
                     'Phone update the config file then check the file![](index.php?/attachments/get/44225)',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position2,xxx,0,0" override="true"/>'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will Return to the previous interface\n'
                         'Circle: Will makes the outgoing call to Emergency\n'
                         'Square :The screen brightness will decreased'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Circle key',
             'expected': 'Will makes the second outgoing call to Emergency'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F1 is on,the led of the F2/F3 is off'},
            {'step': 'Phone establish a call. \nDuring the converstiaon then press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the new outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F2 is off,the led of the F1/F3 is oN'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath'},
            {'step': 'Phone establish two normal calls the led of the F1/F3 is on\nthen press the F3 key',
             'expected': 'ALE-300/400:\nwill make the conference call,and led of the F3 key is breath'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>'},
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'})},
 {'title': 'RQPLEIAD_180_31_Hard_Key_OXE_Define_Key3_Unlock',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\n'
                     'Only set the progkey 124: programmed with the Guard function on position 3,and the lock '
                     'parameter is disabled\n'
                     'Phone update the config file then check the file![](index.php?/attachments/get/44226)',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,1,position3,xxx,0,0" override="true"/>'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly\n'
                         'and press the hard key:\n'
                         'Triangle : Will Return to the previous interface\n'
                         'Circle: will turn to the dashboard\n'
                         'Square :will makes the outgoing call to guard'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Square  key',
             'expected': 'Will makes the second outgoing call to guard'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F3 key',
             'expected': 'ALE-300/400:\n'
                         'Makes the outgoing call to the guard\n'
                         'and the screen display correctly\n'
                         'Adn during the conversation, the led of the F1/F3 is on,the led of the F2 is off'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F3',
             'expected': 'ALE-300/400:\n'
                         'Makes the new outgoing call to the guard\n'
                         'and the screen display correctly\n'
                         'and during the conversation,the led of the F1 is on,the led of the F2/F3 is off'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath'},
            {'step': 'Phone establish two normal calls the led of the F1/F2 is on, the led of the F3 is off\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls'},
            {'step': 'OXE: user---program key\nset the progkey 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>'},
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'})},
 {'title': 'RQPLEIAD_180_32_Hard_Key_OXE_Define_Key 1&2_Lock',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\n'
                     'set the progkey 123: programmed with the Emergency function on position 1\n'
                     'set the progkey 124: programmed with the Guard function on position 2\n'
                     'And the lock parameter are enabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,1" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,position2,xxx,0,1" override="true"/>'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\n'
                     'enable or disable the lock\n'
                     'then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and the screen display correctly\n'
                         'and during the conversation, the led of the F1/F2/F3 is off'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Will makes the new outgoing call to the emergency\n'
                         'and the screen display correctly'},
            {'step': 'Phone is idle then press the F2 Key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the guard\n'
                         'During the conversation, the led of the F1/F2/F3 is off'},
            {'step': 'Phone establish a call.\nDuring the converstiaon then press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Will makes the new outgoing call to the guard\n'
                         'and the screen display correctly'},
            {'step': 'Phone establish two normal calls,\n'
                     'the led of the F3 is on,the led of the F1/F2 is off\n'
                     'then press the F3 key',
             'expected': 'ALE-300/400:\nwill make the conference call,and led of the F3 key is breath'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will makes the outgoing call to emergency\n'
                         'Circle: Will makes the outgoing call to guard\n'
                         'Square :The screen brightness will decreased'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Circle key',
             'expected': 'Will makes the second outgoing call to emergency/guard'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>'},
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'})},
 {'title': 'RQPLEIAD_180_33_Hard_Key_OXE_Define_Key 2_Lock_Key 3_Unlock',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\n'
                     'set the progkey 123: programmed with the Emergency function on position 3,the lock parameter is '
                     'disabled\n'
                     'set the progkey 124: programmed with the Guard function on position 2,the lock paramter is '
                     'enabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position3,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,position2,xxx,0,1" override="true"/>'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F2 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the Guard\n'
                         'and the screen display corectly\n'
                         'And during the conversation, thel ed of the F1 is on,the led of the F2/F3 is off'},
            {'step': 'Phone establish a normal call then press the F2 key',
             'expected': 'ALE-30/300/400:\nMakes the new outgoing call to the Guard\nand the screen display corectly'},
            {'step': 'Phone is idle then press the F3 key',
             'expected': 'ALE-300/400:\n'
                         'Makes the outgoing call to the Emergency\n'
                         'and the screen display corectly\n'
                         'During the conversation, the led of the F1 is on,the led of the F2/F3 is off'},
            {'step': 'Phone establish a normal call then press the F3 key',
             'expected': 'ALE-300/400:\nMakes the new outgoing call to the Emergency\nand the screen display corectly'},
            {'step': 'Phone establish a normal call the led of the F1 is on\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nwill hold the call, and led of the F1 key is breath'},
            {'step': 'Phone establish two normal calls',
             'expected': 'the led of the F1 is on, the led of the F2/F3 is off'},
            {'step': 'ALE-500:\nCheck the Triangle /Circle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will Return to the previous interface\n'
                         'Circle: Will makes the outgoing call to guard\n'
                         'Square :Will makes the outgoing call to emergency'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Circle key',
             'expected': 'Will makes the second outgoing call to guard/emergency'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>'},
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'})},
 {'title': 'RQPLEIAD_180_34_Hard_Key_OXE_Define_Key 1&3_Unlock',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\n'
                     'set the progkey 123: programmed with the Emergency function on position 1\n'
                     'set the progkey 124: programmed with the Guard function on position 3\n'
                     'And the lock parameter are all disabled\n'
                     'Phone update the config file then check the file',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,position1,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,position3,xxx,0,0" override="true"/>'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
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
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\n'
                     'enable or disable the lock\n'
                     'then press the F1 key',
             'expected': 'ALE-30/300/400:\n'
                         'Makes the outgoing call to the emergency\n'
                         'and screen display correctly\n'
                         'and during the conversation, the led of the F1/F2/F3 is off'},
            {'step': 'Phone is idle mode the led of the F1/F2/F3 is off\nthen press the F3 key',
             'expected': 'ALE-300/400:\nMakes the outgoing call to the Guard\nand screen display correctly'},
            {'step': 'Phone establish one normal calls,the led of the F1/F2/F3 IS OFF\nthen press the F1 key',
             'expected': 'ALE-30/300/400:\nMakes the new outgoing call to the emergency\nand screen display correctly'},
            {'step': 'Phone establish one normal calls,the led of the F1/F2/F3 IS OFF\nthen press the F3 key',
             'expected': 'ALE-300/400:\nMakes the new outgoing call to the Guard\nand screen display correctly'},
            {'step': 'Phone establish two normal calls, the led of the F2 is on,the led of F1/F3 is off\n'
                     'then press the F2 key',
             'expected': 'ALE-30/300/400:\nwill exit these two calls'},
            {'step': 'ALE-500:\nCheck the Triangle Triangle/Square key',
             'expected': 'The three keys name display correctly(emergency is red color)\n'
                         'and press the hard key:\n'
                         'Triangle :Will makes the outgoing call to emergency\n'
                         'Circle: will turn to the homepage\n'
                         'Square :Will makes the outgoing call to guard'},
            {'step': 'ALE-500:\nPhone establish a call with phone B then press the Triangle/Square key',
             'expected': 'Will makes the second outgoing call to emergency/guard'},
            {'step': 'check the f1/f2/f3 function of the ALE-500',
             'expected': 'F1: hold\nF2: transfer\nF3: conference'},
            {'step': 'OXE: user---program key\nset the progkey 123 and 124 :Not Assigned',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,0,,,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,0,,,0,0" override="true"/>'},
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'})},
 {'title': 'RQPLEIAD_180_35_Hard_Key_OXE_Define_Two_Lock_Hard_Key',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\nset the progkey 123 and 124, \nand Lock" parameter is enable"',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,1" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,1" override="true"/>'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only the defined key displays the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "All keys defined by Admin"\n'
                         'The reset to default icon is grey\n'
                         'Only the defined key displays the radio button and selected,\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'check the function of the two keys', 'expected': 'the function is correctly'})},
 {'title': 'RQPLEIAD_180_36_Hard_Key_OXE_Define_One_Lock_Hard_Key_Update',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\nonly define one of progkey 123 or 124\nand Lock" parameter is enabled"',
             'expected': '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'hard key names are all grey\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'check the function of the defined key', 'expected': 'the function is correctly'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     '\n'
                     'selectone undefined key then press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'And the reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly'},
            {'step': 'check the new function of the hard key', 'expected': 'the fucntion is correctly'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked'},
            {'step': 'Repeat steps 5-8', 'expected': ''})},
 {'title': 'RQPLEIAD_180_37_Hard_Key_OXE_Define_One_Lock_Hard_Key_One_Unlock_Hard_Key_Modify',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\nset the progkey 123 and 124,\none key is locked and one key is unlocked',
             'expected': 'lock key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>\n'
                         'unlocked key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,0" override="true"/>'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     '\n'
                     'Select  the defined key which is unlocked and press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly'},
            {'step': 'check the new function of the hard key', 'expected': 'the fucntion is correctly'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked'},
            {'step': 'Repeat steps 4-7', 'expected': ''})},
 {'title': 'RQPLEIAD_180_38_Hard_Key_OXE_Define_One_Lock_Hard_Key_One_Unlock_Hard_Key_Reset_To_Default',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\nset the progkey 123 and 124,\none key is locked and one key is unlocked',
             'expected': 'lock key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,1" override="true"/>\n'
                         'unlocked key:\n'
                         '<setting id="SIPUseDeviceKey12x" value="0,12x,1,positionx,xxx,0,0" override="true"/>'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected\n'
                         'Undefined key and lock key are grey, the unlock defined key name is light\n'
                         'And the cap icon/hard key name display correctly\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Press the reset to default icon',
             'expected': 'The lock defined key: Not affected\nthe unlock defined key: return to the default'})},
 {'title': 'RQPLEIAD_180_39_Hard_Key_OXE_Define_Two_Unlock_Hard_Key_Modify',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\nset the progkey 123 and 124,\nthe lock paramter are all disabled',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,0" override="true"/>'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Enter the hard keys menu: User/Device/Hard keys\n'
                     'or long press the hard key\n'
                     'press the edit button of the defined key which is unlocked',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly'},
            {'step': 'check the new function of the hard key', 'expected': 'the fucntion is correctly'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'This key is defined and content display correctly\n\nlock paramter is unlocked'},
            {'step': 'Long press the unlocked hard key\nRepeat steps 4-7', 'expected': ''})},
 {'title': 'RQPLEIAD_180_40_Hard_Key_OXE_Define_Two_Unlock_Hard_Key_Reset_To_Default',
  'preconditions': '',
  'steps': ({'step': 'OXE: user---program key\nset the progkey 123 and 124,\nthe lock paramter are all disabled',
             'expected': '<setting id="SIPUseDeviceKey120" value="0,120,1,positionx,xxx,0,0" override="true"/>\n'
                         '<setting id="SIPUseDeviceKey121" value="0,121,1,positionx,xxx,0,0" override="true"/>'},
            {'step': 'Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'ALE-30: Long press the F1/F2\n'
                     'ALE-300/400: Long press the F1/F2/F3\n'
                     'ALE-500:Long press Triangle/Circle/Square',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only defined hard key is selected '
                         'and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the unlock defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Press the reset to default icon', 'expected': 'all hard key display the default content'})},
 {'title': 'RQPLEIAD_180_41_Hard_Key_Phone_Define_By_Hard_Key',
  'preconditions': '',
  'steps': ({'step': "OXE: Doesn't configure the hard keys \n"
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
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'},
            {'step': 'Define one key :\nSelect the undefined key and press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly'},
            {'step': 'select one key type then press the + button',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly'},
            {'step': 'check the new function of the hard key', 'expected': 'the fucntion is correctly'},
            {'step': 'Repeat steps 2-4',
             'expected': 'These two keys are selected and the edit icon is displayed on the right\n'
                         'And the two hard key names are light'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"'},
            {'step': 'ALE-300/400:\nPress the i icon',
             'expected': 'display the help screen: change the physical button'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'first defined hard key: is the key 123 on OXE side\n'
                         'second defined hard key: is the key 124 on OXE side\n'
                         'and parameter of the lock: disabled'})},
 {'title': 'RQPLEIAD_180_42_Hard_Key_Phone_Define_By_Menu',
  'preconditions': '',
  'steps': ({'step': "OXE: Doesn't configure the hard keys \n\nEnter the hard keys menu:\nUser/Device/Hard keys",
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon is grey\n'
                         'radio button + default cap icon + grey hard key name\n'
                         'ALE-30:\n'
                         'two options: hold cap icon/On hold and transfer cap icon/Transfer\n'
                         'ALE-300/400:\n'
                         'three options: hold cap icon/On hold and transfer cap icon/Transfer and conference cap '
                         'icon/Conference\n'
                         'ALE-500:\n'
                         'three options: Triangle cap icon/Back and Circle cap icon/Home and Square cap icon/Low '
                         'power'},
            {'step': 'press one key whitch not defined then press the + button',
             'expected': 'will display the key type choine screen\n\nand the choices all display correctly'},
            {'step': 'select one key type',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly'},
            {'step': 'check the new function of the hard key', 'expected': 'he fucntion is correctly'},
            {'step': 'Repeat steps 2-4',
             'expected': 'These two keys are selected and the edit icon is displayed on the right\n'
                         'And the two hard key names are light'},
            {'step': 'ALE-300/400/500:\npress the remaining key',
             'expected': 'will popup"only 2 keys allowed,deselect one key first"'},
            {'step': 'ALE-300/400:\nPress the i icon',
             'expected': 'display the help screen: change the physical button'},
            {'step': 'Check the defined key of the OXE',
             'expected': 'first defined hard key: is the key 123 on OXE side\n'
                         'second defined hard key: is the key 124 on OXE side\n'
                         'and parameter of the lock: disabled'})},
 {'title': 'RQPLEIAD_180_43_Hard_Key_Phone_Define_Update_By_Long_Press_Hard_Key',
  'preconditions': '',
  'steps': ({'step': 'Phone configure 2 hard keys  \nLong press the defined hard key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Select the defined key\nDefine the two keys to another function',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly'},
            {'step': 'check the new function of the key', 'expected': 'the fucntion is correctly'},
            {'step': 'check the two keys of the OXE',
             'expected': 'Phone sends the notify to the OXE\n'
                         'the progkey 123 and 124 of the OXE: the content is update'})},
 {'title': 'RQPLEIAD_180_44_Hard_Key_Phone_Define_Reset_To_Default_By_Long_Press_Hard_Key',
  'preconditions': '',
  'steps': ({'step': 'Phone configure 2 hard keys\nLong press the hard key',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Press the reset to default icon', 'expected': 'all hard key display the default content'},
            {'step': 'Check the function of the key to its default state',
             'expected': 'ALE-30:\n'
                         'F1/hold and F2/transfer\n'
                         'ALE-300/400:\n'
                         'F1/hold and F2/transfer and F3/conference\n'
                         'ALE-500:\n'
                         'Triangle/back and Circle/home and Square/low power'},
            {'step': 'check the two keys of the OXE', 'expected': 'the program key 123 and 124 is not defined'})},
 {'title': 'RQPLEIAD_180_45_Hard_Key_Phone_Define_Update_By_Menu',
  'preconditions': '',
  'steps': ({'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Select the defined key\nDefine the two keys to another function',
             'expected': 'Can define the key successfully, and the key is selected.\n'
                         'display correctly(icon /hard key name)\n'
                         '\n'
                         'and enter hard keys menu :display correctly\n'
                         'long press the hard key :display correctly'},
            {'step': 'check the new function of the key', 'expected': 'the fucntion is correctly'},
            {'step': 'check the two keys of the OXE',
             'expected': 'Phone sends the notify to the OXE\n'
                         'the progkey 123 and 124 of the OXE: the content is update'})},
 {'title': 'RQPLEIAD_180_46_Hard_Key_Phone_Define_Reset_To_Default_By_Menu',
  'preconditions': '',
  'steps': ({'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Press the reset to default icon', 'expected': 'all hard key display the default content'},
            {'step': 'Check the function of the key to its default state',
             'expected': 'ALE-30:\n'
                         'two options: F1/hold and F2/transfer\n'
                         'ALE-300/400:\n'
                         'F1/hold and F2/transfer and F3/conference\n'
                         'ALE-500:\n'
                         'three options:Triangle/back and Circle/home and Square/low power'},
            {'step': 'check the two keys of the OXE', 'expected': 'the program key 123 and 124 is not deffned'})},
 {'title': 'RQPLEIAD_180_47_Hard_Key_Defined_Default_Funtcion',
  'preconditions': '',
  'steps': ({'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Select the defined key\nDefine the two keys to default function',
             'expected': 'The two hard keys are selected and hard key name is light\n'
                         'cap icon:\n'
                         'ALE-30 :hold/transfer\n'
                         'ALE-300/400: hold/transfer/conference\n'
                         'ALE-500: Triangle/Circle/Square'},
            {'step': 'Press the hard key', 'expected': 'The function is the default'})},
 {'title': 'RQPLEIAD_180_48_Hard_Key_Defined_Unselected',
  'preconditions': '',
  'steps': ({'step': 'Phone configure two hard keys\nPhone Enter the hard keys menu:\nUser/Device/Hard keys',
             'expected': 'Title "Edit maximum 2 keys"\n'
                         'The reset to default icon display at the upper left corner of the screen\n'
                         'The left of the options all display the radio button, but only two defined hard key is '
                         'selected and the edit icon is displayed on the right\n'
                         'Undefined key is grey, the defined key name is light\n'
                         '\n'
                         'ALE-300/400: The i icon display at the upper right corner of the screen'},
            {'step': 'Unselected the two defined keys',
             'expected': 'The two keys ard not selected and hard key name is grey'},
            {'step': 'Press the two hard keys', 'expected': 'The function is the default'},
            {'step': 'Select the two leys again', 'expected': 'The two keys ard selected and hard key name is light'})},
 {'title': 'RQPLEIAD_180_49_Hard_Key_Defined_Cap_Icon_Function',
  'preconditions': '',
  'steps': ({'step': 'When the hard key is not defined\ncheck the cap icon',
             'expected': 'ALE-30/300/400:\n'
                         'Hold cap icon\n'
                         'Transfer cap icon\n'
                         'Conference cap icon\n'
                         'ALE-500:\n'
                         'Triangle cap icon\n'
                         'Circle cap icon\n'
                         'Square cap icon'},
            {'step': 'Define the key to phone number/Immediate forward/Deactivate forward"Welcome '
                     'desk/Operator/Voicemail/"Redial/ Last caller/Cleaning mode/Meet me/Guard/Do not '
                     'disturb/Lock/Auto answer/Hunting group\n'
                     '\n'
                     'check the cap icon and function',
             'expected': 'ALE-30/300/400:F1/F2/abc cap icon\n'
                         'ALE-500: Triangle/Circle/Square Cap icon\n'
                         '\n'
                         'The function of the key is correctly'},
            {'step': 'Define the key to Hold/Transfer/Conference\ncheck the cap icon and function',
             'expected': 'ALE-30/300/400: Hold/Transfer/Conference cap icon\n'
                         'ALE-500:\n'
                         'Triangle/Circle/Square cap icon\n'
                         'Press the hard key:\n'
                         'the function of the key is correctly'},
            {'step': 'Define the key to Emergency\ncheck the cap icon and function',
             'expected': 'ALE-30/300/400: Red cap icon\n'
                         'ALE-500:\n'
                         'Triangle/Circle/Square cap icon, and the font color of the dashboard is red\n'
                         'Press the hard key:\n'
                         'Will makes the outgoing call to Emergency'})},
 {'title': 'RQPLEIAD_180_50_Hard_Key_Reset',
  'preconditions': '',
  'steps': ({'step': 'There are 2 defined hard keys.\n'
                     '\n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly'},
            {'step': 'Restart the phone \nthen\nShort/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly'})},
 {'title': 'RQPLEIAD_180_51_Hard_Key_Reset_To_Factory',
  'preconditions': '',
  'steps': ({'step': 'There are 1 defined hard keys. \n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly'},
            {'step': 'Phone reset flash, then the phone connects the OXE again\n'
                     'Short/long press the defined hard key and check the hard key menu',
             'expected': 'These hard keys will not affected:\n'
                         '\n'
                         'short press: the function works normaly\n'
                         'long press/enter the hard key menu: The function is display correctly'},
            {'step': 'check the undefined key', 'expected': 'Still the default function'})}]

@pytest.mark.generated
@pytest.mark.parametrize('case', CASES, ids=[c['title'] for c in CASES])
def test_rqpleiad_180(case, ssh_session, step_mapping_rules):
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
