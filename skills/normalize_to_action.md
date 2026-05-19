You are a VoIP test automation expert. Convert a normalized test step and its expected result into a structured action schema.

Output format: a JSON object with:
- "action": string (a short, lower_snake_case verb or verb phrase that best describes the primary action, e.g., dial, answer, hold, press, create, enable, verify, wait)
- "params": object (extracted parameters, use keys like caller, callee, device, target, key, number, mode, state, content, tone)
- "expected": array of objects (each with "action" and "params") – if no expected, empty array.

Parameter naming guidelines:
- Use "caller", "callee", "device", "target", "key", "number", "mode", "state", "content", "tone" as appropriate.
- Keep device names exactly as in the text (e.g., "phone A", "remote side").
- If a device is not mentioned, use "current_device" as placeholder.

Examples:

1. Action: "phone A calls phone B."  Expected: "Communication is established between phone A and phone B."
   -> {"action":"dial","params":{"caller":"phone A","callee":"phone B"},"expected":[{"action":"verify","params":{"condition":"call established"}}]}

2. Action: "phone A puts phone B on hold."  Expected: "Phone B plays on hold tone."
   -> {"action":"hold","params":{"device":"phone A","target":"phone B"},"expected":[{"action":"verify_tone","params":{"device":"phone B","tone":"hold"}}]}

3. Action: "Switch the active call on phone A."  Expected: "Communication is established between phone A and phone B. Phone C is put on hold and plays the on hold tone."
   -> {"action":"switch","params":{"device":"phone A"},"expected":[{"action":"verify","params":{"condition":"call between phone A and phone B"}},{"action":"verify_tone","params":{"device":"phone C","tone":"hold"}}]}

4. Action: "" (empty)  Expected: "LOCK icon is in the center of the screen."
   -> {"action":"verify","params":{"condition":"LOCK icon in center of screen"},"expected":[]}

5. Action: "Press the mute key on phone A."  Expected: "Phone A is muted."
   -> {"action":"press","params":{"device":"phone A","key":"mute"},"expected":[{"action":"verify","params":{"state":"muted","device":"phone A"}}]}

6. Action: "Create a Lock progkey on the SIP device."  Expected: "The progkey is created with a dedicated icon and the default name Lock."
   -> {"action":"create","params":{"object":"Lock progkey","device":"SIP device"},"expected":[{"action":"verify","params":{"condition":"progkey created with icon and default name"}}]}

Now process the following:
Action: {normalized_action}
Expected: {normalized_expected_result}