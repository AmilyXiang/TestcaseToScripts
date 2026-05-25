#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from typing import Any, Dict, List

from generator_copilot import GeneratorCopilot
from log_manager import get_logger
from prompt_manager import PromptManager


logger = get_logger("sub_feature_generator_copilot")


class GeneratorSubFeatureCopilot(GeneratorCopilot):
	"""Generate sub-features by building prompt from PromptManager and invoking copilot cli."""
	prompt_name = "prompt.sub_feature.copilot"

	def __init__(
		self,
		prompt_manager: PromptManager | None = None,
		temp_dir: str = "tmp",
		output_dir: str = "output_copilot",
		copilot_cmd: str = "copilot.cmd",
		documents: List[str] | None = None,
		feature_name: str = "",
	):
		super().__init__(
			prompt_manager=prompt_manager,
			temp_dir=temp_dir,
			output_dir=output_dir,
			copilot_cmd=copilot_cmd,
			target_name="sub_features",
		)
		self.documents = documents or []
		self.feature_name = feature_name
		self.output_file_path = ""

	def build_generate_prompt(self, output_file_path: str, feature_name: str | None = None) -> str:
		"""Build prompt from PromptManager using prompt.sub_feature.copilot template."""
		if not self.documents:
			raise ValueError("documents is empty. Please provide at least one document path.")

		use_feature_name = (feature_name if feature_name is not None else self.feature_name).strip()
		if not use_feature_name:
			raise ValueError("feature_name is empty. Please provide feature_name.")

		document_list_text = self.build_document_path_list(self.documents)
		return self.prompt_manager.get_prompt(
			self.prompt_name,
			document_path_list=document_list_text,
			feature_name=use_feature_name,
			output_file_path=self.normalize_prompt_path(output_file_path),
		)

	def generate(self) -> Dict[str, Any]:
		"""
		1) Build generate prompt
		2) Build output file name with timestamp
		3) Save generate prompt into temp prompt file
		4) Build Copilot CLI prompt with temp generate prompt file path
		5) Invoke copilot cli command to generate sub-features and save into output_dir with output_file_name
		"""
		logger.info("[GeneratorSubFeatureCopilot] generate start")
		try:
			logger.info("[GeneratorSubFeatureCopilot] step1 build output file path")
			timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
			self.output_file_path = self.build_output_file_path(timestamp)

			logger.info("[GeneratorSubFeatureCopilot] step2 build generation prompt")
			generate_prompt = self.build_generate_prompt(
				output_file_path=self.output_file_path,
				feature_name=self.feature_name,
			)

			logger.info("[GeneratorSubFeatureCopilot] step3 build temp prompt file")
			temp_prompt_file = self.build_temp_prompt_file(timestamp, generate_prompt)

			logger.info("[GeneratorSubFeatureCopilot] step4 run copilot command")
			copilot_result = self.run_copilot_cli(temp_prompt_file)
			logger.info("[GeneratorSubFeatureCopilot] command=%s", copilot_result["command"])
			logger.info("[GeneratorSubFeatureCopilot] command finished return_code=%s", copilot_result["return_code"])

			logger.info("[GeneratorSubFeatureCopilot] step6 check output file")
			output_exists = os.path.exists(self.output_file_path)
			output_status = "OK" if output_exists else "NOK"

			result = {
				"prompt_file": temp_prompt_file,
				"output_file_path": self.output_file_path,
				"command": copilot_result["command"],
				"return_code": copilot_result["return_code"],
				"stdout": copilot_result["stdout"],
				"stderr": copilot_result["stderr"],
				"output_exists": output_exists,
				"output_status": output_status,
			}
			logger.info(
				"[GeneratorSubFeatureCopilot] generate done output_exists=%s output_status=%s",
				output_exists,
				output_status,
			)
			return result
		except Exception:
			logger.exception("[GeneratorSubFeatureCopilot] generate failed")
			raise


if __name__ == "__main__":
	generator = GeneratorSubFeatureCopilot(
		temp_dir="./tmp",
		output_dir="./tmp",
		copilot_cmd="copilot.cmd",
		documents=[
			"./resource/PLEIADES_HLA.docx.toc.md",
		],
		feature_name="Call Management",
	)

	result = generator.generate()

	print("\n=== Copilot Generation Summary ===")
	print(f"Prompt file: {result['prompt_file']}")
	print(f"Output file target: {result['output_file_path']}")
	print(f"Return code: {result['return_code']}")
	print(f"Output exists: {result['output_exists']}")
	print(f"Output status: {result['output_status']}")
	print("\n=== Copilot CLI Output ===")
	print("STDOUT:")
	print(result["stdout"])
	print("STDERR:")
	print(result["stderr"])
