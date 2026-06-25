import os


class PromptManager:
	"""集中管理和生成 prompt 的类"""

	def __init__(self, prompt_folder: str = "prompt"):
		self.prompt_folder = prompt_folder
		self.prompts = {
			"prompt.reset_context": "prompt.reset_context.md",
			"prompt.copilot_cli": "prompt.copilot_cli.md",
			"prompt.pdf_markdown": "prompt.pdf_markdown.md",
			"prompt.image_markdown": "prompt.image_markdown.md",
			"prompt.filter_chapter": "prompt.filter_chapter.md",
			"prompt.feature.copilot": "prompt.feature.copilot.md",
			"prompt.sub_feature.copilot": "prompt.sub_feature.copilot.md",
			"prompt.case_to_action.copilot": "prompt.case_to_action.copilot.md",
			"prompt.actions_to_stepfile.copilot": "prompt.actions_to_stepfile.copilot.md",
			"prompt.intent_refine.copilot": "prompt.intent_refine.copilot.md",
			"prompt.testrail_auto_cases_fetcher": "prompt.testrail_auto_cases_fetcher.md",
			"prompt.user_story.copilot": "prompt.user_story.copilot.md",
			"prompt.test_case.copilot": "prompt.test_case.copilot.md",
		}

	def add_prompt(self, name: str, template: str):
		"""添加一个 prompt 模板"""
		self.prompts[name] = template

	def get_prompt(self, name: str, **kwargs) -> str:
		"""根据名称和参数获取格式化后的 prompt"""
		template_file_name = self.prompts.get(name)
		if not template_file_name:
			raise ValueError(f"Prompt '{name}' not found.")
		template_file_path = os.path.join(self.prompt_folder, template_file_name)
		# 从文件中读取模板内容
		try:
			with open(template_file_path, 'r', encoding='utf-8') as f:
				template = f.read()
		except FileNotFoundError:
			raise ValueError(f"Prompt file '{template_file_path}' not found.")
		if not template:
			raise ValueError(f"Prompt '{name}' not found.")

		# 只替换已提供的占位符，避免 JSON 示例中的花括号被 str.format 误解析
		result = template
		for key, value in kwargs.items():
			result = result.replace(f"{{{key}}}", str(value))
		return result

	def list_prompts(self):
		"""列出所有已注册的 prompt 名称"""
		return list(self.prompts.keys())


if __name__ == "__main__":
	pm = PromptManager()
	print(pm.list_prompts())
	test_case_prompt = pm.get_prompt(
		"prompt.test_case.copilot", 
		document_path_list="./document/HLA_deskphones_communication.md\n./document/HLA_deskphones_Appendix.md",
		user_story_name="Incoming call screen display",
		user_story_content="As an user, I want the ALE-500 to display an animated blue circle and a clear incoming call screen when a call rings so that I can easily notice and identify incoming calls.",
		user_story_id="TS_001",
		product="ALE-500",
		scenario="NORMAL",
		output_file_path="output_copilot/test_case.json")
	print(test_case_prompt)

	os.makedirs("tmp", exist_ok=True)
	prompt_file = "tmp/prompt.md"
	with open(prompt_file, "w", encoding="utf-8") as f:
		f.write(test_case_prompt)
	print(f"Prompt saved to: {prompt_file}")
	