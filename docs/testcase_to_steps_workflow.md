# Testcase 输入到 testcase_steps 输出的端到端流程

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

### 阶段 B：生成 testcase_actions
1. 用 case-to-action prompt 将步骤原文转成 action rows
2. 输出 testcase_actions JSON（含 action_text/expected_text/intents/precondition）

### 阶段 C：intent 细化
1. 用 intent refine prompt + mapping template 精修 action/expected/precondition intent
2. 版本化输出（vN -> vN+1）

### 阶段 D：生成 testcase_steps
1. 用 actions_to_stepfile prompt（规则说明）或本地脚本
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

### 3.2 prompt 模板
- prompt/prompt.case_to_action.copilot.md
  - cleaned JSON -> testcase_actions JSON
  - 规则重点：语义对齐、原子化拆分、precondition 抽取
- prompt/prompt.intent_refine.copilot.md
  - testcase_actions 的 action_intent / expected_intent / precondition_intent 精修
  - 规则重点：preserve-first、同 case 上下文判断、三模板治理
- prompt/prompt.actions_to_stepfile.copilot.md
  - testcase_actions -> testcase_steps（简洁 intent-first 结构）
  - 规则重点：
    - 多 action 同 expected：前置动作先做，检查只在最终执行步展示
    - 同 action 多 expected：动作只执行一次，后续检查步不重复 action

### 3.3 intent 模板与指南
- docs/intent_refine_mapping_template.md
- docs/expected_intent_mapping_template.md
- docs/precondition_intent_mapping_template.md
- docs/intent_refine_guide.md

### 3.4 新增可复用脚本（推荐用于最后一步）
- build_testcase_steps.py
  - 输入：testcase_actions JSON
  - 输出：simple_stepflow_intent_first_clean JSON
  - 内置两条关键规则：
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

## 4.4 生成 testcase_actions（Copilot prompt）
使用：
- prompt/prompt.case_to_action.copilot.md

输入参数：
- case_input_path
- cleaned_output_path
- action_output_path

输出：
- testrail/<name>.testcase_actions...json

## 4.5 intent refine（Copilot prompt）
使用：
- prompt/prompt.intent_refine.copilot.md

输入参数：
- input_action_file
- output_action_file
- skip_case_ids

建议：
- 先做只读预览，再写盘
- 始终版本化输出（例如 v12 -> v13 -> v14）

## 4.6 生成最终 testcase_steps（推荐脚本）
- .venv/Scripts/python.exe build_testcase_steps.py --input "testrail/xxx.v14.json" --output "testrail/xxx.testcase_steps.simple_intent_stepflow.v19.json"

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

## 9. 推荐落地顺序（最短路径）

1. clean_testrail_json.py 清洗输入
2. prompt.case_to_action.copilot 生成 testcase_actions
3. prompt.intent_refine.copilot 做 intent 精修（版本化）
4. build_testcase_steps.py 生成最终简洁 testcase_steps

这条路径最稳定，也最容易审计回溯。