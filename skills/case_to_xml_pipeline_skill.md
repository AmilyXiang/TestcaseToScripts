# Case to XML Pipeline Skill

## Purpose
将 TestRail Auto cases details JSON（`output_copilot/*.details.json`）通过三步 pipeline 转换为可运行的 DECT XML 测试脚本。

**Pipeline 流程：**
```
[details.json] 
  → Step 1: 数据清洗 (deepseek_case_std.md)
  → Step 2: 原子化 (deepseek_std_to_atomic.md)
  → Step 3: 生成 XML (deepseek_atomic_to_xml.md)
  → [XML 脚本文件 + missing_profiles.json]
```

---

## 使用方式

**调用此 skill 时，向用户询问以下输入：**

| 参数 | 说明 | 示例 |
|------|------|------|
| `input_file` | TestRail auto cases details JSON 文件路径 | `output_copilot/testrail_run_38710_auto_cases.details.json` |
| `output_dir`（可选）| XML 输出目录，默认由 `run_id` 自动推断 | `testcase/run_38710` |

**测试输入（默认）：**
- `input_file`: `output_copilot/testrail_run_38710_auto_cases.details.json`
- `output_dir`: `testcase/run_38710`

---

## 固定资源文件

| 用途 | 路径 |
|------|------|
| Step 1 prompt | `prompt/deepseek_case_std.md` |
| Step 2 prompt | `prompt/deepseek_std_to_atomic.md` |
| Step 3 prompt | `prompt/deepseek_atomic_to_xml.md` |
| model profiles | `case2xml/model_profiles.json` |
| devices config | `case2xml/devices.json` |

---

## Step 1 — 数据清洗（Case Standardization）

### 目标
将 details JSON 的 `items[]` 转换为标准化 Worksheet JSON，清理 HTML 标签，结构化 steps。

### 输入准备

1. 读取用户指定的 details JSON 文件（即 `input_file`）。
2. 提取其中的 `items` 数组和 `run_id` 字段。
3. 将 `items` 数组包装为以下格式，供 prompt 使用：

```json
{
  "cases": [ /* items 数组内容 */ ]
}
```

> **字段说明**：details JSON 中每个 item 的字段名与 prompt 期望的字段名一致（`case_id`、`title`、`custom_description`、`custom_preconds`、`custom_steps_separated`），无需重命名字段。

### 执行规则

读取 `prompt/deepseek_case_std.md` 文件，按其全部规则处理准备好的 `{"cases": [...]}` 输入。

**关键规则摘要（以 prompt 文件为准）：**
- 提取 `case_id`、`title`、`description`（清理 HTML）、`preconditions`、`steps[]`
- 每个 step 包含 `step_no`、`action`（清理 HTML）、`expected_result`（清理 HTML）
- 保留所有重要信息，不改写内容
- 若 `custom_steps_separated` 某步骤有明显独立子操作，可添加 `action_substeps` 和 `expected_checkpoints`

### 输出

保存到：`tmp/pipeline_<run_id>_stage1_worksheet.json`

格式：
```json
{
  "Worksheet": [
    {
      "case_id": 10172156,
      "title": "US001-03_01_Outgoing_call_by_personal_directory_8262_SIP",
      "description": "...",
      "preconditions": null,
      "steps": [
        { "step_no": 1, "action": "...", "expected_result": "..." }
      ]
    }
  ],
  "meta": {
    "source": {
      "format": "testrail_auto_cases",
      "run_id": 38710,
      "run_name": null,
      "auto_case_count": 6
    },
    "cleaning": {
      "touched_steps": 12,
      "cleaned_field_instances": 30
    }
  }
}
```

---

## Step 2 — 原子化（Atomization）

### 目标
将 Worksheet 每个 case 的每个 step 拆解为原子动作序列（substeps），并为每个原子动作标注后续断言。

### 输入准备

1. 读取 `tmp/pipeline_<run_id>_stage1_worksheet.json`。
2. 提取 `Worksheet` 数组，统计用例数量 `{case_count}`。

### 执行规则

读取 `prompt/deepseek_std_to_atomic.md` 文件，按其全部规则处理 `Worksheet` 数组。

将文件中的 `{case_count}` 占位符替换为实际用例数量。

**关键规则摘要（以 prompt 文件为准）：**
- 每个原子动作只做一件事（press_key、navigate、enter_menu、make_call 等）
- 按句号、换行、顺序词拆分
- 无法映射的动作添加 `#TODO:` 前缀
- 保持原 `step_no`，新增 `substeps` 数组

### 输出

保存到：`tmp/pipeline_<run_id>_stage2_atomic.json`

格式：
```json
{
  "worksheet": [
    {
      "case_id": 10172156,
      "title": "...",
      "steps": [
        {
          "step_no": 1,
          "original_action": "...",
          "original_expected": "...",
          "substeps": [
            { "action": "press_key(\"offhook\")", "assertions": ["assert_display(\"Connected\")"] }
          ]
        }
      ]
    }
  ]
}
```

---

## Step 3 — XML 生成（XML Generation）

### 目标
将原子化 worksheet 转换为可运行的 DECT XML 测试脚本，并输出缺失配置清单。

### 输入准备

读取以下三个文件，分别对应 prompt 中的三个占位区块：

| prompt 区块 | 读取文件 |
|-------------|---------|
| `## MODEL_PROFILES_JSON` | `case2xml/model_profiles.json` |
| `## DEVICES_JSON` | `case2xml/devices.json` |
| `## ATOMIC_WORKSHEET_JSON` | `tmp/pipeline_<run_id>_stage2_atomic.json` |

### 执行规则

读取 `prompt/deepseek_atomic_to_xml.md` 文件，将文件末尾"十一、输入占位"的三个区块替换为以上三个文件的实际内容，然后按 prompt 全部规则执行。

**关键规则摘要（以 prompt 文件为准）：**
- 每个 case 生成独立 XML 文件，文件名格式：`TR_<case_id>__<title_slug>.xml`
- XML 严格遵守设备 init/close 模板、双端验证、参数化要求
- 无法映射的 action/assertion 记入 MISSING_PROFILES，并在 XML 中插入 `<!-- MISSING[...] -->` 注释
- 禁止将实际值（号码、姓名等）硬编码，优先用 `{device.N.*}` 占位符

### 输出

1. **XML 文件**：将 `## XMLS` 区块中每个 `### FILE: xxx.xml` 的内容保存到 `<output_dir>/` 目录：
   - 例如：`testcase/run_38710/TR_10172156__US001-03_01_Outgoing_call_by_personal_directory_8262_SIP.xml`

2. **缺失配置清单**：将 `## MISSING_PROFILES` 区块的 JSON 内容保存到：
   - `<output_dir>/missing_profiles.json`

---

## 中间文件汇总

| 阶段 | 文件 | 说明 |
|------|------|------|
| Step 1 输出 | `tmp/pipeline_<run_id>_stage1_worksheet.json` | 清洗后的 Worksheet |
| Step 2 输出 | `tmp/pipeline_<run_id>_stage2_atomic.json` | 原子化 worksheet |
| Step 3 XML 输出 | `<output_dir>/TR_<case_id>__<title_slug>.xml` | 可运行 XML 脚本 |
| Step 3 缺失清单 | `<output_dir>/missing_profiles.json` | 待人工补充项 |

> `<run_id>` 从 input_file 的顶层 `run_id` 字段读取（如 `38710`）。
> `<output_dir>` 默认为 `testcase/run_<run_id>`，用户可覆盖。

---

## 错误处理

| 情况 | 处理方式 |
|------|---------|
| `custom_steps_separated` 为空 | 保留 case，steps 为空数组，在 meta 中记录 |
| `items` 数组为空 | 终止并报告输入文件为空 |
| Step 1/2 无有效输出 | 终止并报告出错阶段 |
| Step 3 `MISSING_PROFILES` 非空 | 正常继续，将缺失清单保存，提示用户检查 |

---

## 完整执行检查清单

执行结束后，输出以下摘要报告（不需要保存为文件，直接回应用户即可）：

```
Pipeline 执行摘要
================
输入文件     : <input_file>
Run ID       : <run_id>
处理用例数   : <case_count>

Step 1 (清洗)
  - 输出文件 : tmp/pipeline_<run_id>_stage1_worksheet.json
  - 处理步骤数: <touched_steps>

Step 2 (原子化)
  - 输出文件 : tmp/pipeline_<run_id>_stage2_atomic.json
  - 总 substep: <total_substeps>
  - TODO 项数 : <todo_count>

Step 3 (XML 生成)
  - 输出目录  : <output_dir>
  - 生成 XML  : <xml_count> 个文件
  - 缺失配置  : <missing_count> 项（详见 missing_profiles.json）
```
