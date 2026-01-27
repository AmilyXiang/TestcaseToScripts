import json

text = '''```json
[
    {
        "id": "64b3d8d5f81a79fcd1eb55ccd5401393e5577111",
        "intent": "verify_display",
        "suggested_commands": [
            "key sim HOME",
            "key ts \"Call Log\"",
            "screen_dump | grep -E \"Guard|label|avatar|name|number|date\""
        ],
        "confidence": 0.8,
        "explanation": "Navigate to call log and verify Guard call log details are displayed correctly",
        "tags": ["call_log", "verification", "guard_key"],
        "automati'''

# 模拟 _extract_json 函数
if "```json" in text:
    text = text.split("```json", 1)[1]
    if "```" in text:
        text = text.split("```", 1)[0]

text = text.strip()

# Try to fix truncated JSON arrays
if text.startswith("[") and not text.endswith("]"):
    depth = 0
    last_complete_idx = -1
    in_string = False
    escape_next = False
    bracket_depth = 0
    
    for i, char in enumerate(text):
        if escape_next:
            escape_next = False
            continue
        if char == "\\":
            escape_next = True
            continue
        if char == '"':
            in_string = not in_string
        if not in_string:
            if char == "[":
                bracket_depth += 1
            elif char == "]":
                bracket_depth -= 1
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0 and bracket_depth == 1:
                    last_complete_idx = i
    
    if last_complete_idx > 0:
        text = text[:last_complete_idx + 1] + "\n]"

try:
    parsed = json.loads(text)
    print("修复成功！")
    print(f"解析结果: {len(parsed)} 个对象")
    print(json.dumps(parsed, indent=2, ensure_ascii=False))
except Exception as e:
    print(f"修复失败: {e}")
    print(f"文本长度: {len(text)}")
    print(f"文本预览: {text[:500]}")
