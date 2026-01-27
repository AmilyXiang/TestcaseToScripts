from __future__ import annotations

import pprint
import pytest

# Auto-generated from TestRail export.
# Update step_mapping.yaml to map natural-language steps into SSH commands.

CASES = [{'title': 'RQPLEIAD_180_01_Create_Emergency_Program_Key',
  'preconditions': 'OXE: \nmgr---SIP device management---DM profile---Emergency number----xxxx',
  'steps': [{'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 short', 'key sim SOFTK0 long'],
             'confidence': 0.9,
             'explanation': 'The command simulates pressing the empty program key, which can be done either as a short '
                            'or long press.',
             'tags': ['key_simulation', 'program_key'],
             'automation': 'automatable'},
            {'step': 'Press Emergency call',
             'expected': 'Display the create key screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The action involves pressing a specific program key for emergency calls.',
             'tags': ['emergency', 'key_press'],
             'automation': 'automatable'},
            {'step': 'Press the create key button of the screen or the ok key of the phone',
             'expected': 'The progarm key created successfully and display correctly  (the phone and addon side)',
             'intent': 'press_key',
             'suggested_commands': ["key ts 'Create'"],
             'confidence': 0.8,
             'explanation': "The command simulates a touch screen click on the 'Create' button.",
             'tags': ['key_simulation', 'touch_screen'],
             'automation': 'automatable'}]},
 {'title': 'RQPLEIAD_180_02_Create_Guard_Program_Key',
  'preconditions': 'OXE: \nmgr---SIP device management---DM profile---Guard number----xxxx',
  'steps': [{'step': 'Short or long press the empty program key of the phone or addon',
             'expected': 'Display the key type choice screen\ntitleChoose your programmable key""',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0 short', 'key sim SOFTK0 long'],
             'confidence': 0.9,
             'explanation': 'The command simulates pressing the empty program key, either short or long as specified.',
             'tags': ['key_simulation', 'program_key'],
             'automation': 'automatable'},
            {'step': 'Press Guard call',
             'expected': 'Display the create key screen',
             'intent': 'press_key',
             'suggested_commands': ['key sim SOFTK0'],
             'confidence': 0.9,
             'explanation': 'The action involves pressing a soft key to create a guard program.',
             'tags': ['key_simulation', 'guard_program'],
             'automation': 'automatable'}]}]

@pytest.mark.generated
@pytest.mark.parametrize('case', CASES, ids=[c['title'] for c in CASES])
def test_rqpleiad_180_test(case, ssh_session, step_mapping_rules):
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
