                ┌─────────────────┐
                │ 原始测试步骤数据 │
                └────────┬────────┘
                         │     - step-1: testrail_parser.py
                         |     - step-2: data_cleaning.py
                         ▼
                ┌─────────────────┐
                │ 文本标准化层     │
                │ normalize       │
                └────────┬────────┘
                         │    - step-3: build_step_result_kb.py：step_result_unify_skill.md
                         │    
                         ▼
                ┌─────────────────┐
                │ Step Pattern库  │
                │ (知识库核心)     │
                └────────┬────────┘
                         │     - step-4: step_clustering.py/run_step_clustering.py：pattern_extraction_skill.md
                         │     - step-5: cluster_action_schema_basic_call_no_oxo_generic_ids.py：        cluster_to_action_schema_skill.md
                ┌─────────────────┐
                │ Action Schema库 │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Vector检索库     │
                │ (相似步骤匹配)   │
                └─────────────────┘