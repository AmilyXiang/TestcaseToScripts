# TestRail Auto Cases Fetcher Prompt

## Quick Start (直接使用)

1. 复制下方 `Execution Prompt Template` 整段
2. 选择输入范围（`run_id` 或 `project_id`）
3. 将对应占位符替换为真实 ID
4. 直接粘贴到 Copilot Chat 执行

可选参数：

- `{{AUTO_VALUES}}` 默认 `"Auto"`
- `{{MAX_RETRY}}` 默认 `2`

## Role

你是 TestRail 数据提取助手。你的任务是通过 MCP 连接 TestRail，按输入范围（run 或 project）拉取测试/用例，并筛选 Auto cases。

## Objective

按以下顺序执行：

1. Connect to TestRail via MCP credentials
2. Pull data by scope (`run_id` 或 `project_id`)
3. Filter category Auto cases

## Inputs

- `run_id`: 要查询的 TestRail Run ID（可选，和 `project_id` 二选一）
- `project_id`: 要查询的 TestRail Project ID（可选，和 `run_id` 二选一）
- `scope`: 查询范围（可选，`"run"` 或 `"project"`；默认自动推断：有 `run_id` 则 run，否则 project）
- `auto_category_values`: 视为 Auto 的分类值（可选，默认：`["Auto"]`）
- `include_fields`: 需要返回的字段（可选，默认：`["case_id", "test_id", "title", "section_id", "priority_id", "type_id", "category"]`）
- `output_dir`: 输出目录（可选，默认：`output_copilot`）
- `output_prefix`: 输出文件名前缀（可选，默认自动生成：`testrail_<scope>_<id>_auto_cases`）
- `max_retry`: 单次工具调用失败时重试次数（可选，默认：`2`）

输入约束：

- `run_id` 与 `project_id` 不能同时为空。
- 若同时提供，优先使用 `run_id`，并在 `errors` 中附加提示：`both_run_id_and_project_id_provided_run_used`。

## Tool Usage Rules

- `scope=run`：优先使用 MCP 工具获取 run 下的 tests（例如 `get_tests`）。
- `scope=project`：优先使用分页能力拉取 project 下的 cases（例如 `get_cases` + `limit/offset` 直到结束）。
- 在筛选前，先读取 case 字段定义（如 `get_case_fields`），拿到 `custom_category` 的枚举映射（例如：`1 -> Manual`, `2 -> Auto`）。
- 如果主链路不可用，则使用可替代链路：
  - 先取 run 对应 case/test 列表（任何可用工具）；
  - 再补充 case 详情（如 `get_case`）以拿到分类字段；
  - 最后在本地筛选 Auto 类别。
- 不要臆造数据；没有查到就返回空数组。
- 工具调用失败时可重试（最多 `max_retry` 次），仍失败则在输出 JSON 中附加 `errors` 字段（数组）。

## Auto Category Mapping

仅当以下条件满足时，将该用例视为 Auto case：

- 若分类字段是字符串：`custom_category` / `category` 值等于 `Auto`（忽略大小写）。
- 若分类字段是数字/枚举 ID：先通过 `get_case_fields` 做 ID -> 文本映射，再判断映射值是否等于 `Auto`。

如果分类字段不存在，必须在输出中注明 `category_field_missing=true`。

如果映射接口不可用或映射缺失：

- `category` 原样返回（例如 `2`）。
- 同时在 `errors` 中记录 `category_mapping_unavailable` 或 `category_mapping_missing`，避免静默漏检。

### Why previously missed Auto cases

常见漏检原因：`custom_category` 在 TestRail 中是枚举 ID（如 `2`），而不是字符串 `"Auto"`。如果只按字符串比较，会把真实 Auto case 漏掉。

## Output Files Convention

必须产出两个 JSON 文件：

1. 统计文件（summary）
  - 文件名：`<output_prefix>.summary.json`
  - 示例：`testrail_project_5_auto_cases.summary.json`
2. 明细文件（details）
  - 文件名：`<output_prefix>.details.json`
  - 示例：`testrail_project_5_auto_cases.details.json`

推荐命名规则：

- `scope=run` 时：`output_prefix=testrail_run_<run_id>_auto_cases`
- `scope=project` 时：`output_prefix=testrail_project_<project_id>_auto_cases`

写入要求：

- 两个文件都必须写入 `output_dir`。
- `summary` 仅保留统计与元信息，不包含完整 steps 等大字段。
- `details` 包含完整 auto case 记录（用于追溯和后处理）。

## Output Format

仅输出 JSON（不要解释文字），格式如下：

```json
{
  "scope": "run",
  "project_id": 0,
  "run_id": 12345,
  "output_dir": "output_copilot",
  "output_prefix": "testrail_run_12345_auto_cases",
  "summary_file": "output_copilot/testrail_run_12345_auto_cases.summary.json",
  "details_file": "output_copilot/testrail_run_12345_auto_cases.details.json",
  "total_items": 0,
  "auto_items": 0,
  "category_field_missing": false,
  "errors": [],
  "items": [
    {
      "test_id": 0,
      "case_id": 0,
      "title": "",
      "section_id": 0,
      "priority_id": 0,
      "type_id": 0,
      "category": ""
    }
  ]
}
```

说明：

- 若执行全成功，`errors` 返回空数组 `[]`
- 若部分查询失败，`errors` 记录失败步骤和原因，但仍返回可得结果
- `summary_file` 与 `details_file` 必须是已写入到本地的真实文件路径

## Execution Prompt Template

将下面这段直接发给模型执行：

```text
Use TestRail MCP tools to fetch and filter Auto cases.

Input:
- scope: {{SCOPE}}
- run_id: {{RUN_ID_OR_EMPTY}}
- project_id: {{PROJECT_ID_OR_EMPTY}}
- auto_category_values: [{{AUTO_VALUES}}]
- output_dir: {{OUTPUT_DIR}}
- output_prefix: {{OUTPUT_PREFIX_OR_EMPTY}}
- max_retry: {{MAX_RETRY}}

Steps:
1) Connect to TestRail via MCP credentials.
2) Load category enum mapping from get_case_fields (custom_category id -> label).
3) Resolve scope:
  - if scope=run, pull all tests in run_id.
  - if scope=project, pull all cases in project_id with pagination.
4) Enrich case details if needed.
5) Filter items where category label equals Auto (case-insensitive), including enum-id mapping.
6) Write two files to output_dir:
  - <output_prefix>.summary.json
  - <output_prefix>.details.json
7) If a tool call fails, retry up to max_retry times and continue.

Return strict JSON only with fields:
scope, project_id, run_id, output_dir, output_prefix, summary_file, details_file, total_items, auto_items, category_field_missing, errors, items[].
If scope=run, each item includes: test_id, case_id, title, section_id, priority_id, type_id, category.
If scope=project, each item includes: case_id, title, section_id, priority_id, type_id, category.
If nothing matched, return items as [].
Do not include markdown.
```

## Example Call (run scope)

```text
Use TestRail MCP tools to fetch and filter Auto cases.

Input:
- scope: run
- run_id: 36926
- project_id:
- auto_category_values: ["Auto"]
- output_dir: output_copilot
- output_prefix: testrail_run_36926_auto_cases
- max_retry: 2

Steps:
1) Connect to TestRail via MCP credentials.
2) Load category enum mapping from get_case_fields (custom_category id -> label).
3) Resolve scope:
  - if scope=run, pull all tests in run_id.
  - if scope=project, pull all cases in project_id with pagination.
4) Enrich case details if needed.
5) Filter items where category label equals Auto (case-insensitive), including enum-id mapping.
6) Write two files to output_dir:
  - <output_prefix>.summary.json
  - <output_prefix>.details.json
7) If a tool call fails, retry up to max_retry times and continue.

Return strict JSON only with fields:
scope, project_id, run_id, output_dir, output_prefix, summary_file, details_file, total_items, auto_items, category_field_missing, errors, items[].
If scope=run, each item includes: test_id, case_id, title, section_id, priority_id, type_id, category.
If scope=project, each item includes: case_id, title, section_id, priority_id, type_id, category.
If nothing matched, return items as [].
Do not include markdown.
```

## Example Call (project scope)

```text
Use TestRail MCP tools to fetch and filter Auto cases.

Input:
- scope: project
- run_id:
- project_id: 5
- auto_category_values: ["Auto"]
- output_dir: output_copilot
- output_prefix: testrail_project_5_auto_cases
- max_retry: 2

Steps:
1) Connect to TestRail via MCP credentials.
2) Load category enum mapping from get_case_fields (custom_category id -> label).
3) Resolve scope:
  - if scope=run, pull all tests in run_id.
  - if scope=project, pull all cases in project_id with pagination.
4) Enrich case details if needed.
5) Filter items where category label equals Auto (case-insensitive), including enum-id mapping.
6) Write two files to output_dir:
  - <output_prefix>.summary.json
  - <output_prefix>.details.json
7) If a tool call fails, retry up to max_retry times and continue.

Return strict JSON only with fields:
scope, project_id, run_id, output_dir, output_prefix, summary_file, details_file, total_items, auto_items, category_field_missing, errors, items[].
If scope=run, each item includes: test_id, case_id, title, section_id, priority_id, type_id, category.
If scope=project, each item includes: case_id, title, section_id, priority_id, type_id, category.
If nothing matched, return items as [].
Do not include markdown.
```
