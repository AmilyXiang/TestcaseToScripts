import argparse
import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List

from openai import OpenAI

# 假设这些函数已在 data_cleaning 模块中定义
from data_cleaning import (
    canonicalize_action_text,
    canonicalize_expected_text,
    canonicalize_keywords,
    canonicalize_precondition_text,
    clean_step_text,
    cleanup_markup_text,
)


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_prompt(skill_text: str, case_obj: Dict[str, Any]) -> str:
    # 注意：这里将 \n 写为换行符，而不是 "\\n"
    return (
        "Follow the skill below and normalize each step item.\n"
        "Important: output natural, automation-ready sentences, not compressed tokens.\n\n"
        "Skill:\n"
        f"{skill_text}\n\n"
        "Input case:\n"
        f"{json.dumps(case_obj, ensure_ascii=False)}"
    )


def call_deepseek_case(
    client: OpenAI,
    model: str,
    skill_text: str,
    case_obj: Dict[str, Any],
    max_retries: int = 3,
) -> List[Dict[str, Any]]:
    prompt = build_prompt(skill_text, case_obj)

    for attempt in range(1, max_retries + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                temperature=0.0,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a senior QA test normalization assistant. "
                            "You produce strict JSON only. "
                            "Your output must be natural, clear, and directly usable in automation scripts."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            content = response.choices[0].message.content
            if not content:
                raise ValueError("Empty response from model")
            parsed = json.loads(content)
            # 根据 prompt，输出可能是一个对象包含 steps 数组，也可能直接是数组
            if isinstance(parsed, dict) and "steps" in parsed:
                steps = parsed["steps"]
            elif isinstance(parsed, list):
                steps = parsed
            else:
                raise ValueError("Unexpected JSON structure from model")
            # 确保每个步骤都有 step_no 和 sub_step_no（如果是子步骤）
            for step in steps:
                if "step_no" not in step:
                    raise ValueError("Missing step_no in model output")
                if "sub_step_no" not in step:
                    # 如果不是子步骤，可以添加默认 sub_step_no=1
                    step["sub_step_no"] = 1
            return steps
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt >= max_retries:
                raise
            time.sleep(1.5 * attempt)

    raise RuntimeError("Unexpected retry loop state")


def build_knowledge_base(
    parsed_payload: Dict[str, Any],
    normalized_payload: Dict[str, List[Dict[str, Any]]],  # now normalized_payload maps case_id to list of sub-steps
) -> Dict[str, Any]:
    kb_entries: List[Dict[str, Any]] = []

    for sheet_name, cases in parsed_payload.items():
        for case in cases:
            case_id = case.get("case_id")
            title = case.get("title")
            precondition_raw = case.get("preconditions")
            precondition_normalized = canonicalize_precondition_text(precondition_raw)

            # 获取该用例的所有子步骤列表
            sub_steps = normalized_payload.get(sheet_name, {}).get(case_id, [])
            if not sub_steps:
                # 如果没有标准化结果，可能该用例未被处理，跳过或警告
                print(f"Warning: No normalized data for case {case_id}")
                continue

            # 建立从 step_no 到该步骤子步骤列表的映射
            step_to_substeps = {}
            for sub in sub_steps:
                sn = sub.get("step_no")
                step_to_substeps.setdefault(sn, []).append(sub)

            # 遍历原始步骤
            for step in case.get("steps", []):
                step_no = step.get("step_no")
                if step_no is None:
                    print(f"Warning: Missing step_no in raw case {case_id}")
                    continue
                # 获取该步骤对应的子步骤
                substeps = step_to_substeps.get(step_no, [])
                if substeps:
                    for sub in substeps:
                        kb_entries.append({
                            "sheet": sheet_name,
                            "case_id": case_id,
                            "title": title,
                            "precondition_raw": precondition_raw,
                            "normalized_precondition": precondition_normalized,
                            "step_no": step_no,
                            "sub_step_no": sub.get("sub_step_no"),
                            "raw_action": step.get("action"),
                            "raw_expected_result": step.get("expected_result"),
                            "normalized_action": sub.get("normalized_action"),
                            "normalized_expected_result": sub.get("normalized_expected_result"),
                            "keywords": sub.get("keywords", []),
                        })
                else:
                    # 如果没有子步骤，则使用原步骤的标准化结果（兼容旧格式）
                    # 这种情况应该不会发生，因为如果 substeps 为空，说明模型可能没有输出该步骤的子步骤
                    # 作为 fallback，我们仍然尝试用旧逻辑？但为了简单，我们跳过或警告
                    print(f"Warning: No substeps found for step {step_no} in case {case_id}")

    return {
        "meta": {
            "total_entries": len(kb_entries),
            "description": "Knowledge base entries for normalized test steps and expected results.",
        },
        "entries": kb_entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build normalized step/expected-result knowledge base from parsed TestRail JSON using DeepSeek API."
    )
    parser.add_argument("--input", type=Path, default=Path("parsed_testrail.json"))
    parser.add_argument("--skill", type=Path, default=Path("skills/step_result_unify_skill.md"))
    parser.add_argument("--output", type=Path, default=Path("normalized_kb.json"))
    parser.add_argument("--model", type=str, default="deepseek-chat")
    parser.add_argument("--api-key", type=str, default=None, help="DeepSeek API key (optional, otherwise use DEEPSEEK_API_KEY env var).")
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise EnvironmentError("Missing DEEPSEEK_API_KEY environment variable")

    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    client = OpenAI(api_key=api_key, base_url=base_url)

    parsed_payload = load_json(args.input)
    skill_text = args.skill.read_text(encoding="utf-8")

    normalized_payload: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}

    for sheet_name, cases in parsed_payload.items():
        normalized_payload[sheet_name] = {}
        for case in cases:
            case_id = case.get("case_id")
            # 构造发送给模型的 case 对象，包括可能的 action_substeps 和 expected_checkpoints
            case_obj = {
                "case_id": case_id,
                "title": cleanup_markup_text(case.get("title")),
                "description": cleanup_markup_text(case.get("description")),
                "preconditions": cleanup_markup_text(case.get("preconditions")),
                "steps": [],
            }
            for step in case.get("steps", []):
                step_obj = {
                    "step_no": step.get("step_no"),
                    "action": clean_step_text(step.get("action")),
                    "expected_result": clean_step_text(step.get("expected_result")),
                }
                # 如果存在子步骤，添加
                if "action_substeps" in step:
                    step_obj["action_substeps"] = step["action_substeps"]
                if "expected_checkpoints" in step:
                    step_obj["expected_checkpoints"] = step["expected_checkpoints"]
                case_obj["steps"].append(step_obj)

            try:
                normalized_substeps = call_deepseek_case(
                    client=client,
                    model=args.model,
                    skill_text=skill_text,
                    case_obj=case_obj,
                )
            except Exception as e:
                print(f"Failed to normalize case {case_id}: {e}")
                continue

            # 应用 canonicalize 函数到每个子步骤
            for sub in normalized_substeps:
                sub["normalized_action"] = canonicalize_action_text(sub.get("normalized_action"))
                sub["normalized_expected_result"] = canonicalize_expected_text(sub.get("normalized_expected_result"))
                sub["keywords"] = canonicalize_keywords(sub.get("keywords", []))

            normalized_payload[sheet_name][case_id] = normalized_substeps
            print(f"Normalized case: {case_id}")

    kb = build_knowledge_base(parsed_payload, normalized_payload)
    save_json(args.output, kb)

    print(f"Output KB: {args.output}")
    print(f"Total entries: {kb['meta']['total_entries']}")


if __name__ == "__main__":
    main()