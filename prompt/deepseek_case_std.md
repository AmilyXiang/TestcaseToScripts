你是一个测试用例标准化专家。请将下面提供的 TestRail 导出的 JSON 数据，转换为结构化的中间 JSON 格式。

要求如下：

1. 输入数据是一个 JSON 对象，包含一个 "cases" 数组，每个元素代表一个测试用例。你需要遍历每个用例。

2. 对每个用例，提取以下字段：
   - case_id: 原始用例的 "case_id" 字段（整数）。
   - title: 原始用例的 "title" 字段（字符串）。
   - description: 从 "custom_description" 中提取的完整描述文本。需要去除所有 HTML 标签（如 <h1>, <p>, <br /> 等），将 <br /> 转换为换行符，保留文本结构和列表项（以 "- " 开头的行）。同时清理 &nbsp; 等 HTML 实体。最终 description 是一个纯文本字符串，保持可读性。
   - preconditions: 如果原始 JSON 中存在 "custom_preconds" 且非 null，则将其 HTML 同样清理后作为字符串；否则保留 null。
   - steps: 从 "custom_steps_separated" 数组中提取。每个元素包含 "content" 和 "expected"。你需要将每个步骤作为一个对象，包含：
        * step_no: 序号（从 1 开始）。
        * action: 清理后的 "content" 文本（去除 HTML，<br/> 换行，&nbsp; 处理）。
        * expected_result: 清理后的 "expected" 文本。
        * 可选字段（如果你觉得该步骤的 action 或 expected 中可以明显拆分为多个独立的子步骤/子检查点，你可以增加 "action_substeps" 和 "expected_checkpoints" 数组，将主文本按句号、分号、换行或明显的列表项拆分。如果不拆分，则不要添加这两个字段。）

3. 特殊处理：
   - 某些用例的 "custom_steps_separated" 可能只有一个条目，但其中 "content" 包含多个句子或换行，表示多个动作。你不需要强制拆分，除非语义上明确是独立的子操作（例如以 "1."、"2." 开头，或每个句子以句号结束且动作顺序明显）。如果不拆分，保持单一 action 即可。
   - 如果 "custom_expected" 缺失或为空，则 expected_result 设为空字符串。
   - 保留原始文本中的所有重要信息（如电话号码、按键名称、菜单名称等），不要改写内容。

4. 输出格式：
   整个输出必须是一个 JSON 对象，结构如下：
   {
     "Worksheet": [
       {
         "case_id": ...,
         "title": "...",
         "description": "...",
         "preconditions": null 或 "...",
         "steps": [
           {
             "step_no": 1,
             "action": "...",
             "expected_result": "..."
           },
           ...
         ]
       },
       ...
     ],
     "meta": {
       "source": {
         "format": "testrail_auto_cases",
         "run_id": 原始数据中的 run_id（如果有）,
         "run_name": 原始数据中的 run_name,
         "auto_case_count": 原始数据中的 auto_case_count
       },
       "cleaning": {
         "touched_steps": 你实际处理的步骤总数,
         "cleaned_field_instances": 你执行清理操作的字段次数（例如对每个 description、action、expected 做清理算一次）
       }
     }
   }

5. 重要限制：
   - 不要添加任何解释文字或 markdown 代码块标记，只输出纯 JSON。
   - 确保 JSON 是有效的，不要有尾随逗号。
   - 所有的字符串中的换行符使用 \n 表示，双引号需要转义。

以下是输入的原始 JSON：

{在这里粘贴您的原始 JSON 数据}