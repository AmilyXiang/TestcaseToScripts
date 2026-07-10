#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_pipeline_copilot.py

通过 Copilot CLI 执行四步 pipeline，从 TestRail 拉取 Auto cases 并转换为 DECT XML 测试脚本。

  Step 1: TestRail 拉取          (prompt/prompt.testrail_auto_cases_fetcher.md)
  Step 2: Case standardization   (prompt/deepseek_case_std.md)
  Step 3: Atomization            (prompt/deepseek_std_to_atomic.md)
  Step 4: XML generation         (prompt/deepseek_atomic_to_xml.md)

用法:
  python run_pipeline_copilot.py --run-id 38710                           # 完整执行（Step 1-4）
  python run_pipeline_copilot.py --input output_copilot/xxx.details.json  # 从 Step 2 开始
  python run_pipeline_copilot.py --run-id 38710 --step 1                  # 只执行 Step 1
  python run_pipeline_copilot.py --run-id 38710 --step 2                  # 只执行 Step 2
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime

# 将 copilot-cli 加入 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "copilot-cli"))
from generator_copilot import GeneratorCopilot
from prompt_manager import PromptManager

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Prompt 路径
# ---------------------------------------------------------------------------
PROMPT_CASE_STD     = os.path.join(PROJECT_ROOT, "prompt", "deepseek_case_std.md")
PROMPT_ATOMIC       = os.path.join(PROJECT_ROOT, "prompt", "deepseek_std_to_atomic.md")
PROMPT_XML              = os.path.join(PROJECT_ROOT, "prompt", "deepseek_atomic_to_xml.md")
PROMPT_TESTRAIL_FETCHER = os.path.join(PROJECT_ROOT, "prompt", "prompt.testrail_auto_cases_fetcher.md")
MODEL_PROFILES_JSON     = os.path.join(PROJECT_ROOT, "case2xml", "model_profiles.json")
DEVICES_JSON        = os.path.join(PROJECT_ROOT, "case2xml", "devices.json")

# Step 3 分批阈值：prompt 超过此字节数时自动按 STEP3_BATCH_SIZE 分批处理
STEP3_SIZE_THRESHOLD = 30 * 1024   # 30 KB
STEP3_BATCH_SIZE     = 2           # 每批处理的 case 数

# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def strip_code_fences(text: str) -> str:
    """去除 LLM 可能输出的 markdown 代码块围栏（```json ... ``` 等）。"""
    text = re.sub(r"^```[a-zA-Z]*\s*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n```\s*$", "", text, flags=re.MULTILINE)
    return text.strip()


def extract_json_from_text(text: str) -> str:
    """从文本中提取第一个完整的顶层 JSON 对象或数组。"""
    text = strip_code_fences(text)

    for start_char in ("{", "["):
        idx = text.find(start_char)
        if idx == -1:
            continue
        depth = 0
        in_string = False
        escape = False
        for i, ch in enumerate(text[idx:]):
            if escape:
                escape = False
                continue
            if ch == "\\" and in_string:
                escape = True
                continue
            if ch == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            if ch in "{[":
                depth += 1
            elif ch in "}]":
                depth -= 1
                if depth == 0:
                    candidate = text[idx : idx + i + 1]
                    try:
                        json.loads(candidate)
                        return candidate
                    except json.JSONDecodeError:
                        break
    return ""


def parse_xml_output(text: str) -> dict:
    """从 Copilot 输出中解析 ## XMLS 区块，返回 {filename: xml_content}。"""
    files = {}
    xmls_match = re.search(r"## XMLS\s*\n(.*?)(?=## MISSING_PROFILES|$)", text, re.DOTALL)
    if not xmls_match:
        return files

    xmls_section = xmls_match.group(1)
    file_pattern = re.compile(r"### FILE:\s*(\S+\.xml)\s*\n(.*?)(?=### FILE:|$)", re.DOTALL)
    for m in file_pattern.finditer(xmls_section):
        filename = m.group(1).strip()
        # 去除 XML 前后的 markdown 代码块围栏
        content = strip_code_fences(m.group(2))
        files[filename] = content
    return files


def parse_missing_profiles(text: str) -> str:
    """从 Copilot 输出中解析 ## MISSING_PROFILES 区块，返回 JSON 字符串。"""
    match = re.search(r"## MISSING_PROFILES\s*\n(.*)", text, re.DOTALL)
    if match:
        result = extract_json_from_text(match.group(1))
        if result:
            return result
    return '{"missing_items":[]}'


# ---------------------------------------------------------------------------
# Pipeline 主类
# ---------------------------------------------------------------------------

class PipelineCopilot:
    def __init__(self, input_file: str | None = None, output_dir: str | None = None,
                 run_id: int | str | None = None):
        self.tmp_dir = os.path.join(PROJECT_ROOT, "tmp")
        os.makedirs(self.tmp_dir, exist_ok=True)

        if input_file:
            # 从已有 details.json 启动（跳过 Step 1）
            self.input_file = os.path.abspath(input_file)
            with open(self.input_file, "r", encoding="utf-8") as f:
                self.input_data = json.load(f)
            self.run_id = self.input_data.get("run_id", "unknown")
        elif run_id is not None:
            # 从 run_id 启动，Step 1 负责 fetch
            self.run_id     = run_id
            self.input_file = None
            self.input_data = {}
        else:
            raise ValueError("必须提供 input_file 或 run_id 之一")

        self.output_dir = output_dir or os.path.join(PROJECT_ROOT, "testcase", f"run_{self.run_id}")
        os.makedirs(self.output_dir, exist_ok=True)

        # Step 1 输出：TestRail details.json
        _prefix          = f"testrail_run_{self.run_id}_auto_cases"
        self.stage0_path = os.path.join(PROJECT_ROOT, "output_copilot", f"{_prefix}.details.json")

        # 中间文件路径
        self.stage1_path = os.path.join(self.tmp_dir, f"pipeline_{self.run_id}_stage1_worksheet.json")
        self.stage2_path = os.path.join(self.tmp_dir, f"pipeline_{self.run_id}_stage2_atomic.json")

        # Copilot CLI runner
        self._runner = GeneratorCopilot(
            prompt_manager=PromptManager(prompt_folder=os.path.join(PROJECT_ROOT, "prompt")),
            temp_dir=self.tmp_dir,
            output_dir=self.output_dir,
            project_root=PROJECT_ROOT,
            target_name=f"pipeline_{self.run_id}",
        )

    # ------------------------------------------------------------------
    # 内部方法
    # ------------------------------------------------------------------

    def _write_temp_prompt(self, step_name: str, content: str) -> str:
        """将 prompt 内容写入临时文件，返回文件路径（绝对路径）。"""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = f"prompt_pipeline_{self.run_id}_{step_name}_{ts}.md"
        path = os.path.join(self.tmp_dir, name)
        write_file(path, content)
        return path

    def _run_copilot(self, step_name: str, prompt_content: str) -> str:
        """写临时 prompt 文件，通过 Copilot CLI 执行，返回 stdout 字符串。"""
        temp_path = self._write_temp_prompt(step_name, prompt_content)
        print(f"  Prompt file : {temp_path}")

        result = self._runner.run_copilot_cli(temp_path)

        print(f"  Return code : {result['return_code']}")
        if result["stderr"]:
            preview = result["stderr"][:300].replace("\n", " ")
            print(f"  STDERR      : {preview}")

        # 将原始输出保存供调试
        raw_path = os.path.join(self.tmp_dir, f"pipeline_{self.run_id}_{step_name}_raw.txt")
        write_file(raw_path, result["stdout"])
        print(f"  Raw output  : {raw_path}")

        return result["stdout"]

    # ------------------------------------------------------------------
    # Step 1
    # ------------------------------------------------------------------

    def run_step1(self) -> bool:
        """Step 1: TestRail 拉取 — 通过 MCP 获取指定 run_id 的 Auto cases。"""
        print("\n=== Step 1: TestRail Fetch ===")

        fetcher_md = read_file(PROMPT_TESTRAIL_FETCHER)
        # 提取最后一个 ```text ... ``` 执行模板块
        template_blocks = re.findall(r"```text\n(.*?)```", fetcher_md, re.DOTALL)
        if not template_blocks:
            print("  ERROR: 无法从 fetcher prompt 中提取执行模板")
            return False
        template = template_blocks[-1]

        output_prefix = f"testrail_run_{self.run_id}_auto_cases"
        prompt = (
            template
            .replace("{{SCOPE}}", "run")
            .replace("{{RUN_ID_OR_EMPTY}}", str(self.run_id))
            .replace("{{PROJECT_ID_OR_EMPTY}}", "")
            .replace("{{AUTO_VALUES}}", '"Auto"')
            .replace("{{OUTPUT_DIR}}", "output_copilot")
            .replace("{{OUTPUT_PREFIX_OR_EMPTY}}", output_prefix)
            .replace("{{MAX_RETRY}}", "2")
        )

        output = self._run_copilot("step1_testrail_fetch", prompt)

        # 若 Copilot 已写入文件，直接使用；否则从 stdout 解析并写入
        if not os.path.exists(self.stage0_path):
            json_str = extract_json_from_text(output)
            if not json_str:
                print("  ERROR: 无法从 Step 1 输出中提取 JSON，也未找到输出文件")
                print(f"  输出预览: {output[:500]}")
                return False
            write_file(self.stage0_path, json_str)

        # 更新 input_file 与 input_data 供后续步骤使用
        self.input_file = self.stage0_path
        with open(self.input_file, "r", encoding="utf-8") as f:
            self.input_data = json.load(f)

        auto_count = self.input_data.get("auto_items", len(self.input_data.get("items", [])))
        print(f"  完成: {auto_count} Auto cases → {self.stage0_path}")
        return auto_count > 0

    # ------------------------------------------------------------------
    # Step 2
    # ------------------------------------------------------------------

    def run_step2(self) -> bool:
        """Step 2: 数据清洗 — 按 deepseek_case_std.md 规则处理 items[]。"""
        print("\n=== Step 2: Data Cleaning ===")

        # 若 input_data 未加载（--run-id + --step 2 场景），从 stage0_path 读取
        if not self.input_data:
            if not os.path.exists(self.stage0_path):
                print(f"  ERROR: 未找到 Step 1 输出文件: {self.stage0_path}")
                return False
            self.input_file = self.stage0_path
            with open(self.input_file, "r", encoding="utf-8") as f:
                self.input_data = json.load(f)

        items       = self.input_data.get("items", [])
        cases_input = json.dumps({"cases": items}, ensure_ascii=False, indent=2)

        prompt_template = read_file(PROMPT_CASE_STD)
        prompt = prompt_template.replace("{在这里粘贴您的原始 JSON 数据}", cases_input)

        output = self._run_copilot("step1_case_std", prompt)

        json_str = extract_json_from_text(output)
        if not json_str:
            print("  ERROR: 无法从 Step 1 输出中提取 JSON")
            print(f"  输出预览: {output[:500]}")
            return False

        write_file(self.stage1_path, json_str)

        data         = json.loads(json_str)
        case_count   = len(data.get("Worksheet", []))
        touched_steps = data.get("meta", {}).get("cleaning", {}).get("touched_steps", "?")
        print(f"  完成: {case_count} cases，{touched_steps} steps → {self.stage1_path}")
        return True

    # ------------------------------------------------------------------
    # Step 3
    # ------------------------------------------------------------------

    def run_step3(self) -> bool:
        """Step 3: 原子化 — 按 deepseek_std_to_atomic.md 规则处理 Worksheet[]。"""
        print("\n=== Step 3: Atomization ===")

        with open(self.stage1_path, "r", encoding="utf-8") as f:
            stage1_data = json.load(f)

        worksheet      = stage1_data.get("Worksheet", [])
        case_count     = len(worksheet)
        worksheet_json = json.dumps(worksheet, ensure_ascii=False, indent=2)

        prompt_template = read_file(PROMPT_ATOMIC)
        prompt = prompt_template.replace("{case_count}", str(case_count))
        prompt = prompt.replace("{在此粘贴您的完整 Worksheet JSON}", worksheet_json)

        output = self._run_copilot("step2_atomic", prompt)

        json_str = extract_json_from_text(output)
        if not json_str:
            print("  ERROR: 无法从 Step 2 输出中提取 JSON")
            print(f"  输出预览: {output[:500]}")
            return False

        write_file(self.stage2_path, json_str)

        data = json.loads(json_str)
        total_substeps = sum(
            len(step.get("substeps", []))
            for case in data.get("worksheet", [])
            for step in case.get("steps", [])
        )
        todo_count = sum(
            1
            for case in data.get("worksheet", [])
            for step in case.get("steps", [])
            for sub in step.get("substeps", [])
            if str(sub.get("action", "")).startswith("#TODO")
        )
        print(f"  完成: {case_count} cases，{total_substeps} substeps，{todo_count} TODOs → {self.stage2_path}")
        return True

    # ------------------------------------------------------------------
    # Step 4 — 内部辅助
    # ------------------------------------------------------------------

    def _build_step4_prompt(self, prompt_template: str, model_profiles: str,
                            devices: str, worksheet_cases: list) -> str:
        """将三个占位区块替换为实际内容，返回完整 prompt 字符串。"""
        worksheet_json = json.dumps({"worksheet": worksheet_cases}, ensure_ascii=False, indent=2)
        prompt = re.sub(
            r"(## MODEL_PROFILES_JSON\s*\n)\{在此粘贴 case2xml/model_profiles\.json 的完整内容\}",
            r"\g<1>" + model_profiles, prompt_template,
        )
        prompt = re.sub(
            r"(## DEVICES_JSON\s*\n)\{在此粘贴 case2xml/devices\.json 的完整内容\}",
            r"\g<1>" + devices, prompt,
        )
        prompt = re.sub(
            r"(## ATOMIC_WORKSHEET_JSON\s*\n)\{在此粘贴 atomic worksheet JSON\}",
            r"\g<1>" + worksheet_json, prompt,
        )
        return prompt

    def _execute_step4_prompt(self, prompt_template: str, model_profiles: str,
                              devices: str, worksheet_cases: list, label: str):
        """执行一次 Step 4 Copilot CLI 调用，返回 (xml_files_dict, missing_items_list)。"""
        prompt        = self._build_step4_prompt(prompt_template, model_profiles, devices, worksheet_cases)
        output        = self._run_copilot(label, prompt)
        xml_files     = parse_xml_output(output)
        missing_items = json.loads(parse_missing_profiles(output)).get("missing_items", [])
        if not xml_files:
            print(f"  WARNING [{label}]: 未解析到 XML 文件，请检查对应 raw.txt")
        return xml_files, missing_items

    # ------------------------------------------------------------------
    # Step 4 — 主逻辑（自动分批）
    # ------------------------------------------------------------------

    def run_step4(self) -> bool:
        """Step 4: XML 生成。
        - 若全量 prompt 体积 <= STEP3_SIZE_THRESHOLD，单次调用。
        - 否则按 STEP3_BATCH_SIZE 拆批依次调用，最终合并结果。
        """
        print("\n=== Step 4: XML Generation ===")

        model_profiles  = read_file(MODEL_PROFILES_JSON)
        devices         = read_file(DEVICES_JSON)
        prompt_template = read_file(PROMPT_XML)

        with open(self.stage2_path, "r", encoding="utf-8") as f:
            atomic_data = json.load(f)
        worksheet_cases = atomic_data.get("worksheet", [])
        total_cases     = len(worksheet_cases)

        # 估算全量 prompt 体积
        full_prompt  = self._build_step4_prompt(prompt_template, model_profiles, devices, worksheet_cases)
        prompt_bytes = len(full_prompt.encode("utf-8"))
        print(f"  全量 prompt 体积: {prompt_bytes // 1024} KB ({total_cases} cases)")

        all_xml_files     = {}
        all_missing_items = []

        if prompt_bytes <= STEP3_SIZE_THRESHOLD or total_cases <= 1:
            # 单次执行
            print("  模式: 单次执行")
            xml_files, missing_items = self._execute_step4_prompt(
                prompt_template, model_profiles, devices, worksheet_cases, "step4_xml"
            )
            all_xml_files.update(xml_files)
            all_missing_items.extend(missing_items)
        else:
            # 分批执行
            batches     = [worksheet_cases[i:i + STEP3_BATCH_SIZE]
                           for i in range(0, total_cases, STEP3_BATCH_SIZE)]
            batch_count = len(batches)
            print(f"  超过阈值 {STEP3_SIZE_THRESHOLD // 1024} KB，"
                  f"分 {batch_count} 批（每批 {STEP3_BATCH_SIZE} cases）")

            for idx, batch in enumerate(batches, start=1):
                case_ids  = [c.get("case_id", "?") for c in batch]
                batch_kb  = len(self._build_step4_prompt(
                    prompt_template, model_profiles, devices, batch
                ).encode("utf-8")) // 1024
                print(f"\n  -- Batch {idx}/{batch_count}: cases={case_ids}  {batch_kb} KB --")
                xml_files, missing_items = self._execute_step4_prompt(
                    prompt_template, model_profiles, devices, batch, f"step4_xml_batch{idx}"
                )
                all_xml_files.update(xml_files)
                all_missing_items.extend(missing_items)

        # 写入输出文件
        xml_count = 0
        for filename, xml_content in all_xml_files.items():
            out_path = os.path.join(self.output_dir, filename)
            write_file(out_path, xml_content)
            print(f"  XML: {out_path}")
            xml_count += 1

        missing_path = os.path.join(self.output_dir, "missing_profiles.json")
        write_file(missing_path, json.dumps(
            {"missing_items": all_missing_items}, ensure_ascii=False, indent=2
        ))
        print(f"  缺失配置: {len(all_missing_items)} 项 → {missing_path}")
        print(f"  完成: {xml_count} 个 XML 文件")
        return xml_count > 0

    # ------------------------------------------------------------------
    # 完整执行
    # ------------------------------------------------------------------

    def run(self) -> bool:
        print("\nPipeline 开始")
        print(f"  Run ID     : {self.run_id}")
        print(f"  输出目录   : {self.output_dir}")

        if not self.run_step1():
            print("\nPipeline 在 Step 1 失败")
            return False

        if not self.run_step2():
            print("\nPipeline 在 Step 2 失败")
            return False

        if not self.run_step3():
            print("\nPipeline 在 Step 3 失败")
            return False

        if not self.run_step4():
            print("\nPipeline 在 Step 4 失败")
            return False

        print("\nPipeline 完成")
        return True


# ---------------------------------------------------------------------------
# 入口
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="通过 Copilot CLI 执行 Case→XML 四步 pipeline")
    parser.add_argument("--input",     help="已有 TestRail auto cases details JSON（跳过 Step 1）")
    parser.add_argument("--run-id",    type=int, help="TestRail Run ID（从 Step 1 开始完整执行）")
    parser.add_argument("--output-dir", help="XML 输出目录（默认 testcase/run_<run_id>）")
    parser.add_argument(
        "--step", type=int, choices=[1, 2, 3, 4],
        help="只执行指定步骤（需要前置步骤的输出文件已存在）",
    )
    args = parser.parse_args()

    if not args.input and not args.run_id:
        parser.error("必须提供 --input 或 --run-id 之一")

    pipeline = PipelineCopilot(input_file=args.input, output_dir=args.output_dir, run_id=args.run_id)

    if args.step == 1:
        success = pipeline.run_step1()
    elif args.step == 2:
        success = pipeline.run_step2()
    elif args.step == 3:
        success = pipeline.run_step3()
    elif args.step == 4:
        success = pipeline.run_step4()
    else:
        success = pipeline.run()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
