#!/usr/bin/env python3
"""
Generate action_schema from normalized knowledge base using DeepSeek API.

Usage:
    python generate_action_schema.py --input normalized_kb.json --output action_schema.json --api-key YOUR_KEY
"""

import json
import os
import time
import argparse
import logging
from typing import Dict, Any, List, Optional
from openai import OpenAI

# 配置日志
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# 优化后的 Prompt 模板（使用 {action} 和 {expected} 占位符）
PROMPT_TEMPLATE = """You are a VoIP test automation expert. Convert a normalized test step and its expected result into a structured action schema.

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
Action: {action}
Expected: {expected}
"""

def load_kb(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_results(results: List[Dict[str, Any]], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

def call_deepseek(client: OpenAI, action_text: str, expected_text: str, model: str = "deepseek-chat", max_retries: int = 3) -> Optional[Dict[str, Any]]:
    """调用 DeepSeek API 生成 action_schema"""
    prompt = PROMPT_TEMPLATE.format(action=action_text, expected=expected_text)
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that outputs valid JSON only."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
                response_format={"type": "json_object"}
            )
            content = response.choices[0].message.content
            if not content:
                raise ValueError("Empty response from API")
            schema = json.loads(content)
            # 确保必要字段存在
            if "action" not in schema:
                schema["action"] = "generic_action"
            if "params" not in schema:
                schema["params"] = {}
            if "expected" not in schema:
                schema["expected"] = []
            return schema
        except Exception as e:
            logger.warning(f"Attempt {attempt+1}/{max_retries} failed: {e}")
            if attempt == max_retries - 1:
                logger.error(f"Failed to process action: {action_text[:100]}...")
                return None
            time.sleep(1.5 * (attempt + 1))
    return None

def main():
    parser = argparse.ArgumentParser(description="Generate action_schema from normalized knowledge base")
    parser.add_argument("--input", required=True, help="Path to normalized_kb.json")
    parser.add_argument("--output", required=True, help="Output path for action_schema.json")
    parser.add_argument("--api-key", default=None, help="DeepSeek API key (or set DEEPSEEK_API_KEY env var)")
    parser.add_argument("--model", default="deepseek-chat", help="Model name")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between API calls (seconds)")
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise EnvironmentError("Missing DeepSeek API key. Provide --api-key or set DEEPSEEK_API_KEY environment variable.")

    client = OpenAI(api_key=api_key, base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))

    # 加载知识库
    kb = load_kb(args.input)
    entries = kb.get("entries", [])
    logger.info(f"Loaded {len(entries)} entries from {args.input}")

    results = []
    for idx, entry in enumerate(entries):
        action_text = entry.get("normalized_action", "")
        expected_text = entry.get("normalized_expected_result", "")
        # 如果两者都为空，跳过（但理论上不应发生）
        if not action_text and not expected_text:
            logger.warning(f"Skipping entry {idx} (case {entry.get('case_id')} step {entry.get('step_no')}) because both action and expected are empty.")
            continue

        logger.info(f"Processing {idx+1}/{len(entries)}: case {entry.get('case_id')} step {entry.get('step_no')}.{entry.get('sub_step_no')}")
        schema = call_deepseek(client, action_text, expected_text, model=args.model)
        if schema is None:
            schema = {"action": "generic_action", "params": {}, "expected": []}

        result_entry = {
            "sheet": entry.get("sheet"),
            "case_id": entry.get("case_id"),
            "title": entry.get("title"),
            "step_no": entry.get("step_no"),
            "sub_step_no": entry.get("sub_step_no"),
            "normalized_action": action_text,
            "normalized_expected_result": expected_text,
            "action_schema": schema
        }
        results.append(result_entry)

        # 避免 API 限流
        time.sleep(args.delay)

    save_results(results, args.output)
    logger.info(f"Saved {len(results)} entries to {args.output}")

if __name__ == "__main__":
    main()