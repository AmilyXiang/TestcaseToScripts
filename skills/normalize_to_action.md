You are a VoIP test automation expert. Convert a normalized test step and its expected result into a structured action schema.

Allowed action intents:
The primary action must be selected from the provided "Allowed Action List" (see below).
If the action is not found in the list, use "custom_action".

Allowed assertion intents:
The expected result validation must use assertions from the provided "Allowed Assertion List" (see below).
If multiple checks are needed, add multiple entries in the "expected" array.

Output format: a JSON object with:
- "action": string (primary intent)
- "params": object (extracted parameters)
- "expected": array of objects (each with "action" and "params") – if no expected, empty array.

Parameter naming guidelines:
- Use "caller", "callee", "device", "target", "key", "number", "mode", "state", "content", "tone" as appropriate.
- Keep device names exactly as in the text (e.g., "phone A", "remote side").
- If a device is not mentioned, use "current_device" as placeholder.

Examples:

1. Action: "phone A calls phone B."  Expected: "Communication is established between phone A and phone B."
   -> {"action":"direct_dial","params":{"caller":"phone A","callee":"phone B"},"expected":[{"action":"are_in_conversation","params":{"device_a":"phone A","device_b":"phone B"}}]}

2. Action: "phone A puts phone B on hold."  Expected: "Phone B plays on hold tone."
   -> {"action":"hold_call","params":{"device":"phone A","target":"phone B"},"expected":[{"action":"is_on_hold","params":{"device":"phone B"}}]}

3. Action: "Switch the active call on phone A."  Expected: "Communication is established between phone A and phone B. Phone C is put on hold and plays the on hold tone."
   -> {"action":"broker","params":{"device":"phone A"},"expected":[{"action":"are_in_conversation","params":{"device_a":"phone A","device_b":"phone B"}},{"action":"is_on_hold","params":{"device":"phone C"}}]}

4. Action: "Press the mute key on phone A."  Expected: "Phone A is muted."
   -> {"action":"mute","params":{"device":"phone A"},"expected":[{"action":"is_mute_led_active","params":{"device":"phone A"}}]}

Now process the following:
Action: {normalized_action}
Expected: {normalized_expected_result}

Allowed Action List:
{allowed_actions}

Allowed Assertion List:
{allowed_assertions}
