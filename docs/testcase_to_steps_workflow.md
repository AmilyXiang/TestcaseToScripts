# Testcase 输入到 testcase_steps 输出的端到端流程

## 1. 目标与范围
本流程用于把 TestRail 原始测试用例数据，逐步转换为测试同学可直接阅读和执行的 steps JSON。

最终目标产物：简洁格式的 testcase_steps 文件（intent-first，precondition 在前，步骤按顺序）。

当前推荐终态文件示例：
- `testrail/testrail_run_36926_8234_Telephony_(RBH_with_8368_).testcase_steps.stepwise.copilot.v3.json`

---

## 2. 流程总览

```
TestRail Excel
     │
     │  main.py parse
     ▼
*.auto_cases.json                           [阶段 A：解析]
     │
     │  main.py clean  /  clean_testrail_json.py
     ▼
*.cleaned.stepwise.v3.json                 [阶段 B：清洗]
     │
     │  run_atomize_batched.py
     │  └─ prompt/prompt.atomize_to_actions.copilot.md
     │  └─ copilot-cli/generator_atomize_copilot.py
     │  └─ Copilot CLI (4 batches → tmp/atomize_batchN_output.json → merge)
     ▼
*.testcase_actions.stepwise.raw.v4.json    [阶段 C：Copilot LLM 原子化]
     │
     │  run_intent_refine_batched.py
     │  └─ prompt/prompt.intent_refine.copilot.md
     │  └─ copilot-cli/generator_intent_refine_copilot.py
     │  └─ docs/ 三个 intent 模板 + intent_refine_guide.md
     │  └─ Copilot CLI (4 batches → tmp/intent_batchN_output.json → merge)
     ▼
*.testcase_actions.stepwise.expected_refined.copilot.v3.json  [阶段 D：Intent Refine]
     │
     │  build_testcase_steps.py
     │  （或 Copilot CLI via prompt/prompt.actions_to_stepfile.copilot.md）
     ▼
*.testcase_steps.stepwise.copilot.v3.json  [阶段 E：Steps 生成]
```

---

## 3. 各阶段详细说明

### 阶段 A：解析（Excel → JSON）

| 项目 | 内容 |
|------|------|
| 入口 | `main.py parse` |
| 核心模块 | `testrail_parser.py` |
| 输入 | TestRail 导出的 Excel 文件（`.xlsx`） |
| 输出 | `testrail/<name>.auto_cases.json` |

命令：
```powershell
.venv\Scripts\python.exe main.py parse `
  --input "<excel_path>.xlsx" `
  --output "testrail/<name>.auto_cases.json"
```

---

### 阶段 B：清洗（JSON → Cleaned JSON）

| 项目 | 内容 |
|------|------|
| 入口 | `main.py clean` 或 `clean_testrail_json.py` |
| 核心模块 | `clean_testrail_json.py`、`data_cleaning.py` |
| 输入 | `*.auto_cases.json` |
| 输出 | `*.cleaned.stepwise.v3.json` |

清洗内容：
- 统一文本格式、去除标记
- 自动推导 `action_substeps` / `expected_checkpoints`（当文本可被结构化拆分时）

命令：
```powershell
.venv\Scripts\python.exe main.py clean `
  --input "testrail/<name>.auto_cases.json" `
  --output "testrail/<name>.cleaned.stepwise.v3.json"
```

---

### 阶段 C：原子化（Cleaned JSON → Raw Actions）

**核心变更（v4）**：原子化由 Python 正则替换为 Copilot LLM，原 `build_testcase_actions_local.py` 已删除。

| 项目 | 内容 |
|------|------|
| 入口 | `run_atomize_batched.py` |
| Prompt 模板 | `prompt/prompt.atomize_to_actions.copilot.md` |
| Generator | `copilot-cli/generator_atomize_copilot.py` |
| 执行方式 | Python 生成 batch prompt 文件 → 写 PS1 → `powershell.exe -File tmp/run_atomize.ps1` → Copilot CLI 逐 batch 处理 |
| 中间产物 | `tmp/atomize_batchN_prompt.md`、`tmp/atomize_batchN_output.json` |
| 输入 | `*.cleaned.stepwise.v3.json` |
| 输出 | `*.testcase_actions.stepwise.raw.v4.json` |

Batch 划分（当前 18 个 case 分 4 批）：
- Batch 1: 10172154, 10172156, 10172157, 10172158, 10172159
- Batch 2: 10172160, 10172161, 10172162, 10172163
命令：
```powershell
# 完整运行（自动分批，已完成的 batch 自动跳过）
.venv\Scripts\python.exe run_atomize_batched.py \
    --input  testrail/<prefix>.cleaned.stepwise.v3.json \
    --output testrail/<prefix>.testcase_actions.stepwise.raw.v4.json

# 自定义每批 case 数（默认 5）
.venv\Scripts\python.exe run_atomize_batched.py \
    --input testrail/<prefix>.cleaned.stepwise.v3.json \
    --output testrail/<prefix>.testcase_actions.stepwise.raw.v4.json \
    --batch-size 4

# 只生成 prompt 文件，不触发 Copilot
.venv\Scripts\python.exe run_atomize_batched.py --input ... --output ... --prepare-only

# 只合并已有 batch 输出
.venv\Scripts\python.exe run_atomize_batched.py --input ... --output ... --merge-only

# 单独跑某一个 batch
.venv\Scripts\python.exe run_atomize_batched.py --input ... --output ... --batch 2
```

原子化规则（`prompt.atomize_to_actions.copilot.md` 8 条规则，关键摘要）：
- **Rule 2**：`and` 连接两个不同交互目标的动词短语 → 拆分为独立行；连接名词/形容词/时间扩展 → 不拆
- **Rule 3**：`"By any method"`、`"In any of tab:"` 等 qualifier 行必须附加到下一个具体动作，不得独立成行
- **Rule 4**：语义配对检查点——导航/设置类**可执行祈使句**保留为 testcase 前部 action，禁止被折叠进 `precondition_text`
- **Rule 5**：`precondition_text` 仅保留**状态/上下文句**（如 `"When <state>"`、`"In idle"`、`"After hangup"`、`"During the conversation"`）；普通 action 禁止写入 `precondition_text`

---

### 阶段 D：Intent Refine（Raw Actions → Refined Actions）

| 项目 | 内容 |
|------|------|
| 入口 | `run_intent_refine_batched.py` |
| Prompt 模板 | `prompt/prompt.intent_refine.copilot.md` |
| Generator | `copilot-cli/generator_intent_refine_copilot.py` |
| 执行方式 | 同阶段 C（batch prompt → PS1 → Copilot CLI → merge） |
| 输入 | `*.testcase_actions.stepwise.raw.v4.json` |
| 输出 | `*.testcase_actions.stepwise.expected_refined.copilot.v3.json` |

> **注意**：两个 runner 的 batch 划分策略不同——atomize 按 case 数均分（4-5 个/批），intent refine 按行数均分（约 22-35 行/批）。两者的 case_id 分组因此不同，这是正常设计。

Intent refine 覆盖三类字段（单 pass 同时处理）：
- `action_intent`：使用 `docs/intent_refine_mapping_template.md` 作为权威映射
- `expected_intent`：使用 `docs/expected_intent_mapping_template.md`；同一 `expected_text` 必须统一为相同 `expected_intent`（多数票原则）
- `precondition_intent`：使用 `docs/precondition_intent_mapping_template.md`

必须内联读取的 docs 文件（共 4 个，缺一不可）：
- `docs/intent_refine_mapping_template.md`
- `docs/expected_intent_mapping_template.md`
- `docs/precondition_intent_mapping_template.md`
- `docs/intent_refine_guide.md`

命令：
```powershell
# 完整运行（自动按行数分批，约 30 行/批）
.venv\Scripts\python.exe run_intent_refine_batched.py \
    --input  testrail/<prefix>.testcase_actions.stepwise.raw.v4.json \
    --output testrail/<prefix>.testcase_actions.stepwise.expected_refined.copilot.v3.json

# 自定义每批目标行数（默认 30）
.venv\Scripts\python.exe run_intent_refine_batched.py \
    --input ... --output ... --batch-rows 25

# 只生成 prompt / 只合并
.venv\Scripts\python.exe run_intent_refine_batched.py --input ... --output ... --prepare-only
.venv\Scripts\python.exe run_intent_refine_batched.py --input ... --output ... --merge-only
```

---

### 阶段 E：Steps 生成（Refined Actions → testcase_steps）

| 项目 | 内容 |
|------|------|
| 入口 | `build_testcase_steps.py`（本地 Python，推荐） |
| 备选 | `prompt/prompt.actions_to_stepfile.copilot.md`（Copilot CLI 路径） |
| 输入 | `*.testcase_actions.stepwise.expected_refined.copilot.v3.json` |
| 输出 | `*.testcase_steps.stepwise.copilot.v3.json` |

两条关键压缩规则（`build_testcase_steps.py` 内置）：
- **Rule A**：多个连续行共享相同 `expected_intent` → `expected` 仅在最后一行展示，前面各行只有 `action`
- **Rule B**：多个连续行共享相同 `action_intent` → `action` 仅在第一行展示，后续各行只有 `expected`

命令：
```powershell
.venv\Scripts\python.exe build_testcase_steps.py `
  --input "testrail/<name>.testcase_actions.stepwise.expected_refined.copilot.v3.json" `
  --output "testrail/<name>.testcase_steps.stepwise.copilot.v3.json"
```

---

## 4. 相关代码与职责一览

### 4.1 核心脚本

| 文件 | 阶段 | 职责 |
|------|------|------|
| `main.py` | A / B | 入口：`parse`、`clean` 子命令 |
| `testrail_parser.py` | A | Excel → auto_cases JSON |
| `clean_testrail_json.py` | B | 清洗与结构化 |
| `data_cleaning.py` | B | 底层文本清洗工具 |
| `run_atomize_batched.py` | C | Copilot LLM 原子化批处理入口 |
| `run_intent_refine_batched.py` | D | Intent refine 批处理入口 |
| `build_testcase_steps.py` | E | Actions → Steps（本地 Python） |

### 4.2 Copilot CLI 相关

| 文件 | 职责 |
|------|------|
| `copilot-cli/generator_atomize_copilot.py` | 构建 batch 原子化 prompt 文件（阶段 C） |
| `copilot-cli/generator_intent_refine_copilot.py` | 构建 batch intent refine prompt 文件（阶段 D） |
| `copilot-cli/generator_copilot.py` | 通用 Copilot CLI 命令构建（旧流程兼容） |
| `copilot-cli/prompt_manager.py` | Prompt 文件路径注册表 |
| `copilot-cli/log_manager.py` | 日志工具 |
| `prompt/prompt.copilot_cli.md` | Copilot CLI `-p` 参数通用模板（被 generator_copilot.py 引用） |

### 4.3 Prompt 模板

| 文件 | 阶段 | 职责 |
|------|------|------|
| `prompt/prompt.atomize_to_actions.copilot.md` | C | 8 条原子化规则 |
| `prompt/prompt.intent_refine.copilot.md` | D | Intent refine 规则（三类 intent + 一致性约束） |
| `prompt/prompt.actions_to_stepfile.copilot.md` | E | Actions → Steps（Copilot 备选路径） |

### 4.4 Intent 模板（阶段 D 必须读取）

| 文件 | 用途 |
|------|------|
| `docs/intent_refine_mapping_template.md` | `action_intent` 权威映射规则 |
| `docs/expected_intent_mapping_template.md` | `expected_intent` 权威映射规则 |
| `docs/precondition_intent_mapping_template.md` | `precondition_intent` 权威映射规则 |
| `docs/intent_refine_guide.md` | 执行指南（Mode A 预览 → Mode B 写入，acceptance checklist） |

---

## 5. 文件命名规范

| 阶段产物 | 命名模式 |
|---------|---------|
| 解析 | `<name>.auto_cases.json` |
| 清洗 | `<name>.cleaned.stepwise.v3.json` |
| 原子化（Copilot LLM） | `<name>.testcase_actions.stepwise.raw.v4.json` |
| Intent Refine 输出 | `<name>.testcase_actions.stepwise.expected_refined.copilot.v3.json` |
| Steps 输出 | `<name>.testcase_steps.stepwise.copilot.v3.json` |
| Batch 中间产物 | `tmp/atomize_batchN_output.json`、`tmp/intent_batchN_output.json` |

> **版本策略**：源文件不可变，每次规则变化写新版本号。`v4` 后缀标识当前批次为 Copilot LLM 原子化产物。

---

## 6. 使用注意事项

1. **Copilot CLI 是必要条件**：阶段 C、D 均通过 `powershell.exe -File tmp/*.ps1` 调用 Copilot CLI，不得用 Python subprocess 直接调用（会触发 agentic 探索模式）。

2. **`--input` / `--output` 是必填参数**：两个 runner 均通过 `--input` 和 `--output` 指定路径，Batch 分组由脚本根据输入数据自动计算，无需手动维护。

3. **同 case 上下文优先**：intent 判定必须结合同 case 的相邻步骤，不能只看单行。

4. **expected_intent 一致性**：相同 `expected_text` 在 batch 内所有行必须使用相同 `expected_intent`（多数票）。此规则已内嵌进 `prompt.intent_refine.copilot.md`，无需额外脚本。

5. **precondition 位置固定**：生成 steps 时，每个 case 的 `precondition_intent` 必须在所有 steps 之前。

6. **DeepSeek 温度约束**：如使用 DeepSeek 做任何归一化，`temperature` 必须为 `0.0`。

7. **skip_case_ids 保护**：intent refine 时 `skip_case_ids` 内的 case 任何字段均不可修改。

---

## 7. 快速验收清单

执行后至少检查：
1. JSON 可解析，`status: "ok"`。
2. testcase 数量和 rows 数量符合预期。
3. 无幽灵 qualifier 行（`action_text` 不以 `"By any method"` 或 `"In any of tab:"` 开头）。
4. 每个 case 都有 `precondition_intent` 且在 steps 之前。
5. `action_intent` 和 `expected_intent` 均非空（允许 `needs_review` / `assert_generic`）。
6. 相同 `expected_text` 的行使用相同 `expected_intent`。
7. steps 顺序正确（`step_number` 按原顺序）。
8. spot check 关键 case（如 10172154、10172158、10172164）语义符合预期。

---

## 8. 常见问题

**Q: 某步只有 expected_intent，没有 action_intent？**
→ 命中 Rule B（同 action 多 expected）：action 已在前一步展示，这里是额外检查点。

**Q: 某步只有 action_intent，没有 expected_intent？**
→ 命中 Rule A（多 action 同 expected）：检查延后到组末统一展示。

**Q: Batch 卡住不动或输出文件未生成？**
→ 检查 `tmp/atomize_batchN_prompt.md` 中的 section 标签是否唯一（`## OUTPUT_PATH`、`## CASE_JSON_BEGIN`），避免 Copilot 解析歧义。

**Q: intent refine 后 expected_intent 不一致？**
→ `prompt.intent_refine.copilot.md` 中 `Same-text consistency` 规则已要求多数票统一，重跑 refine 或手动修正少数行。


## 1. 目标与范围
本流程用于把 TestRail 原始测试用例数据，逐步转换为测试同学可直接阅读和执行的 steps JSON。

最终目标产物是简洁格式的 testcase_steps 文件（intent-first，precondition 在前，步骤按顺序）。

当前推荐终态文件示例：
- testrail/testrail_run_36926_8234_Telephony_(RBH_with_8368_).testcase_steps.simple_intent_stepflow.v19.json

---

## 2. 流程总览

### 阶段 A：输入准备
1. 从 Excel 解析为结构化 JSON（可选）
2. 对 JSON 做清洗和标准化

### 阶段 B：生成 testcase_actions（分步执行）
1. 用本地脚本从 cleaned JSON 生成 testcase_actions rows
2. 输出 raw actions JSON

### 阶段 C：action 原子化门禁（新增，强制）
1. 在 raw actions 后立即执行原子化检测（atomicity gate）
2. 若检测到复合动作超阈值，流程立即失败并输出报告
3. 只有通过门禁的 actions 才允许进入后续 intent refine

### 阶段 D：intent 分步细化
1. 第一步：只优化 action_intent
2. 第二步：只优化 precondition_intent / precondition_required
3. 第三步：只优化 expected_intent

### 阶段 E：生成 testcase_steps
1. 使用分步优化后的 actions 生成 stepflow
2. 输出简洁 steps JSON（按 case 顺序、precondition 在前）

---

## 3. 相关代码与职责

### 3.1 入口与清洗
- main.py
  - 子命令：parse / build-kb / clean
  - clean 会调用 clean_testrail_json.py
- clean_testrail_json.py
  - 统一清洗文本
  - 自动补 action_substeps / expected_checkpoints（可推导时）

### 3.2 prompt 模板（强制，Copilot CLI 执行入口）

> **强制要求：** 以下三个 prompt 必须通过 Copilot CLI 执行，不得跳过。
> Copilot CLI 不可用时，整个流程应当停止，不得用本地脚本静默替代。

- prompt/prompt.case_to_action.copilot.md
  - 阶段 B：cleaned JSON -> testcase_actions JSON
  - 规则重点：语义对齐、原子化拆分、precondition 抽取
  - 必须内联读取 docs/intent_refine_mapping_template.md 中的 canonical list 作为 action_intent 参考
- prompt/prompt.intent_refine.copilot.md
  - 阶段 D：testcase_actions 的 action_intent / expected_intent / precondition_intent 精修
  - 规则重点：preserve-first、同 case 上下文判断、三模板治理
  - 必须内联读取全部 3 个 intent 模板 + intent_refine_guide.md（共 4 个 docs 文件）
- prompt/prompt.actions_to_stepfile.copilot.md
  - 阶段 E：testcase_actions -> testcase_steps（简洁 intent-first 结构）
  - 规则重点：
    - 多 action 同 expected：前置动作先做，检查只在最终执行步展示
    - 同 action 多 expected：动作只执行一次，后续检查步不重复 action

### 3.3 intent 模板与指南（强制，intent refine 时全部内联读取）

> **强制要求：** 以下 4 个文件在每次 intent refine 执行时都必须被完整读取并应用，缺一不可。
> 通过 Copilot CLI 时，generator 负责将全部内容内联到 prompt 中；不得仅引用文件路径。

- docs/intent_refine_mapping_template.md — action_intent 规则（R01-R32、E01-E03、B1/B2）
- docs/expected_intent_mapping_template.md — expected_intent 规则（18 个 canonical intents）
- docs/precondition_intent_mapping_template.md — precondition_intent 规则
- docs/intent_refine_guide.md — 执行指南（Mode A 预览 → Mode B 写入、acceptance checklist、common pitfalls）

### 3.4 本地脚本（仅作 Copilot CLI 不可用时的临时替代，不作为正式输出路径）

> **注意：** 以下脚本不应作为正式流程的默认入口。
> 本地脚本的 intent 逻辑是简化版（少量 heuristics），无法替代 Copilot CLI + 完整模板的语义质量。
> 本地脚本输出仅用于调试或环境验证，最终交付文件必须来自 Copilot CLI 路径。

- build_testcase_actions_local.py
  - 输入：cleaned JSON
  - 输出：testcase_actions JSON（临时）
  - 仅用于验证数据结构，不含完整语义映射

- build_testcase_steps.py
  - 输入：testcase_actions JSON
  - 输出：simple_stepflow_intent_first_clean JSON
  - 内置两条关键规则（本地执行可用）：
    - rule_a_multi_action_to_one_expected_hide_deferred
    - rule_b_one_action_to_multi_expected_hide_reused

### 3.5 Copilot CLI prompt 注册
- copilot-cli/prompt_manager.py
  - 已注册：prompt.actions_to_stepfile.copilot

---

## 4. 标准命令用法

## 4.1 环境准备
在项目根目录执行：
- Windows PowerShell
  - .venv/Scripts/Activate.ps1

安装依赖（首次）：
- .venv/Scripts/python.exe -m pip install -r requirements.txt

## 4.2 从 Excel 解析（可选）
- .venv/Scripts/python.exe main.py parse --input "<excel_path>" --output "testrail/<name>.parsed.json"

## 4.3 清洗
- .venv/Scripts/python.exe clean_testrail_json.py --input "testrail/<name>.parsed.json" --output "testrail/<name>.cleaned.json"

或：
- .venv/Scripts/python.exe main.py clean --input "testrail/<name>.parsed.json" --output "testrail/<name>.cleaned.json"

## 4.4 生成 testcase_actions（分步：第1步）— 强制走 Copilot CLI

使用 Copilot CLI 执行 prompt.case_to_action.copilot.md：
- copilot-cli/generator_copilot.py 负责将 cleaned JSON + prompt 内容内联后调用 Copilot CLI
- 输出：testrail/<name>.testcase_actions.copilot.vN.json

说明：
- Copilot CLI 是强制路径，必须可用。
- 若 copilot.cmd 不存在，请先确认 Copilot CLI 安装路径并配置 --copilot-cmd 参数。
- 本地脚本 build_testcase_actions_local.py 仅用于调试，不作为正式输出。

## 4.5 intent refine（分步：第2-4步）— 强制走 Copilot CLI

使用 Copilot CLI 执行 prompt.intent_refine.copilot.md：
- copilot-cli/generator_intent_refine_copilot.py 负责将以下内容全部内联到 prompt 后调用 Copilot CLI：
  - docs/intent_refine_mapping_template.md
  - docs/expected_intent_mapping_template.md
  - docs/precondition_intent_mapping_template.md
  - docs/intent_refine_guide.md
  - input JSON（当前 actions 文件）
- 执行顺序（三 pass 合一，或逐步输出均可）：
  - 第2步：只做 action_intent refine
  - 第3步：只做 precondition refine
  - 第4步：只做 expected_intent refine

强制要求：
- 每一步都独立输出版本文件
- 始终版本化输出（例如 raw -> action_refined -> precondition_refined -> expected_refined）
- 所有 4 个 docs 文件必须内联读取，不得以路径引用代替

## 4.5.1 原子化门禁（必须通过）
- 在 intent refine 前执行：检测 action_text 是否仍是复合句
- 默认阈值：`--max-composite-candidates 0`
- 报告文件：`--atomic-report-output`（未传时自动写到 `action_output.atomicity_report.json`）
- 门禁失败即停止，不进入后续 refine

## 4.5.2 expected_intent 一致性检查（Stage D 完成后强制执行）

Stage D（expected_intent refine）输出后，**必须立即运行一致性检查**，再进入 Stage E：

```bash
.venv/Scripts/python.exe check_expected_consistency.py
```

检查内容：
- 同一 `expected_text` → 不同 `expected_intent` 的所有冲突行
- 根本原因：LLM 逐行处理时对同一段文本给出不同 intent（非确定性问题）

修复原则：
1. **同 case 内**：相同 expected_text 必须使用相同 expected_intent（无例外）
2. **跨 case**：相同 expected_text 若语义相同，也应统一 intent
3. **合理例外**：极短 section header（如 `"On display:"`）因上下文完全不同可接受差异
4. 修复后再次运行 `check_expected_consistency.py`，确认 `Total conflicts: 0`（或仅剩合理例外）

验证通过后才可进入 Stage E（testcase_steps 生成）。

## 4.6 生成最终 testcase_steps（推荐脚本）
- .venv/Scripts/python.exe build_testcase_steps.py --input "testrail/xxx.v14.json" --output "testrail/xxx.testcase_steps.simple_intent_stepflow.v19.json"

## 4.7 一键分步流程（推荐）
- .venv/Scripts/python.exe run_testcase_pipeline_stepwise.py --input "testrail/<name>.auto_cases.json" --cleaned-output "testrail/<name>.cleaned.stepwise.vN.json" --action-output "testrail/<name>.testcase_actions.stepwise.raw.vN.json" --action-refined-output "testrail/<name>.testcase_actions.stepwise.action_refined.vN.json" --precondition-refined-output "testrail/<name>.testcase_actions.stepwise.precondition_refined.vN.json" --expected-refined-output "testrail/<name>.testcase_actions.stepwise.expected_refined.vN.json" --steps-output "testrail/<name>.testcase_steps.stepwise.vN.json" --atomic-report-output "testrail/<name>.testcase_actions.stepwise.atomicity_report.vN.json" --max-composite-candidates 0

输出结构：
- case_id
- precondition_intent（置顶）
- steps（顺序）
  - step_number
  - action_intent（仅当前执行时出现）
  - expected_intent（仅当前检查时出现）

---

## 5. 输出文件规范与版本建议

### 5.1 testcase_actions 命名
推荐：
- ...testcase_actions.copilot.regenerated_by_prompt.vN.json

### 5.2 testcase_steps 命名
推荐：
- ...testcase_steps.simple_intent_stepflow.vN.json

### 5.3 版本策略
- 源文件不可变
- 每次规则变化写新版本
- 在 meta 或文件名里体现本次 patch 目标

---

## 6. 使用注意事项（高优先）

1. 同 case 上下文优先
- intent 判定不能只看单句，必须看同 case 的相邻步骤与语义链。

2. precondition 位置固定
- 每个 case 的 precondition_intent 必须在最前面。

3. 两条关键压缩规则必须保留
- 多 action 同 expected：检查只在最后执行步呈现。
- 同 action 多 expected：动作只在首次执行步呈现。

4. 输出要“干净”
- 不输出 execute_after_* / reuse_from_* 等技术标记。
- 非当前执行项直接不展示。

5. preserve-first
- intent refine 时，高置信命中才改；不确定保持原值并审阅。

6. DeepSeek 温度约束
- 如果使用 DeepSeek 做相关映射或归一化，temperature 必须为 0.0。

7. 避免跨 case 合并
- 任何分组/压缩仅允许在同一个 case_id 内进行。

8. 跳过名单保护
- intent refine 时 skip_case_ids 必须严格不改任何字段。

---

## 7. 快速验收清单

执行后至少检查：
1. JSON 可解析。
2. testcase 数量符合预期。
3. 每个 case 都有 precondition_intent 且在 steps 之前。
4. steps 顺序正确（step_number 按原顺序）。
5. 无 execute_after_* / reuse_from_* 文本残留。
6. action/expected/precondition 均为 intent 字段。
7. spot check 关键 case（如 10172154、10172158、10172160）语义符合预期。

---

## 8. 常见问题与排查

1. 为什么某一步只有 expected_intent，没有 action_intent？
- 命中“同 action 多 expected”规则：动作已在前一步执行，这里是额外检查点。

2. 为什么某一步只有 action_intent，没有 expected_intent？
- 命中“多 action 同 expected”规则：该检查延后到组末统一执行。

3. 为什么 precondition 很长？
- 来自同 case 多行 precondition_intent 汇总；可后续按业务需要再分层展示。

4. 为什么出现 custom_action / assert_generic？
- 原始语义未命中更具体模板规则，建议回到 intent refine 做定向增强。

---

## 9. 推荐落地顺序（强制 Copilot CLI 路径）

> **前提条件：** 确认 `copilot.cmd`（或等效 Copilot CLI 命令）可在终端调用，否则流程不得开始。

1. **clean**：clean_testrail_json.py 清洗输入
2. **generate actions**：Copilot CLI 执行 prompt.case_to_action.copilot.md → testcase_actions JSON
3. **atomicity gate**：原子化门禁（未通过即停止，不进入 intent refine）
4. **intent refine（action pass）**：Copilot CLI 执行 prompt.intent_refine.copilot.md，内联全部 4 个 docs 文件，只改 action_intent
5. **intent refine（precondition pass）**：Copilot CLI，只改 precondition_intent
6. **intent refine（expected pass）**：Copilot CLI，只改 expected_intent
7. **generate steps**：Copilot CLI 执行 prompt.actions_to_stepfile.copilot.md → testcase_steps JSON

每步均须输出独立版本文件，可回溯。

### 9.1 Copilot CLI 不可用时的应急处理
- 停止流程，排查 copilot.cmd 路径配置
- 不得用本地脚本静默替代并当作正式输出
- 如需调试数据结构，可用本地脚本生成临时文件，但文件名须标注 `.debug.` 以示区分
