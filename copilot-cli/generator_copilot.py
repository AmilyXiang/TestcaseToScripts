#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
from datetime import datetime
from typing import Any, Dict, List

from prompt_manager import PromptManager


class GeneratorCopilot:
	"""Base class for copilot generators. Only provides shared helper methods."""
	copilot_cli_prompt_name = "prompt.copilot_cli"

	def __init__(
		self,
		prompt_manager: PromptManager | None = None,
		temp_dir: str = "tmp",
		output_dir: str = "output_copilot",
		copilot_cmd: str = "copilot.cmd",
		target_name: str = "",
	):
		self.prompt_manager = prompt_manager or PromptManager()
		self.temp_dir = temp_dir
		# Keep tmp_dir alias for backward-compatible subclasses.
		self.tmp_dir = temp_dir
		self.output_dir = output_dir
		self.copilot_cmd = copilot_cmd
		self.target_name = target_name

		os.makedirs(self.temp_dir, exist_ok=True)
		os.makedirs(self.output_dir, exist_ok=True)

	@staticmethod
	def normalize_prompt_path(path: str) -> str:
		"""Normalize path format for prompts to avoid slash/backslash mixing."""
		return path.replace("\\", "/")

	@staticmethod
	def decode_subprocess_output(raw: bytes | None) -> str:
		"""Decode subprocess output robustly across different Windows code pages."""
		if not raw:
			return ""

		for encoding in ("utf-8", "gbk"):
			try:
				return raw.decode(encoding)
			except UnicodeDecodeError:
				continue

		return raw.decode("utf-8", errors="replace")

	def build_document_path_list(self, documents: List[str] | str) -> str:
		"""Convert documents input into prompt bullet list text."""
		if isinstance(documents, str):
			return documents
		return "\n".join([f"- {self.normalize_prompt_path(path)}" for path in documents])

	def build_copilot_cli_cmd(self, prompt_file_path: str) -> List[str]:
		"""Build Copilot CLI command using prompt.copilot_cli template."""
		cli_prompt = self.prompt_manager.get_prompt(
			self.copilot_cli_prompt_name,
			prompt_file_path=self.normalize_prompt_path(prompt_file_path),
		)
		return [self.copilot_cmd, "-p", cli_prompt, "--allow-all"]

	def run_copilot_cli(self, prompt_file_path: str) -> Dict[str, Any]:
		"""Run copilot cli with prompt file and return decoded command results."""
		cmd = self.build_copilot_cli_cmd(prompt_file_path)
		proc = subprocess.run(cmd, capture_output=True, text=False, cwd=os.path.dirname(__file__))

		return {
			"command": " ".join(cmd),
			"return_code": proc.returncode,
			"stdout": self.decode_subprocess_output(proc.stdout),
			"stderr": self.decode_subprocess_output(proc.stderr),
		}

	def build_output_file_path(self, timestamp: str) -> str:
		"""Build output file path using target_name and provided timestamp."""
		use_target_name = self.target_name.strip()
		if not use_target_name:
			raise ValueError("target_name is empty. Please set target_name when initializing GeneratorCopilot.")

		output_file_name = f"{use_target_name}_{timestamp}.json"
		return self.normalize_prompt_path(os.path.join(self.output_dir, output_file_name))

	def build_temp_prompt_file(self, timestamp: str, generate_prompt: str) -> str:
		"""Build temp prompt file path and write prompt content using target_name and timestamp."""
		use_target_name = self.target_name.strip()
		if not use_target_name:
			raise ValueError("target_name is empty. Please set target_name when initializing GeneratorCopilot.")

		temp_prompt_file_name = f"prompt_{use_target_name}_copilot_{timestamp}.md"
		temp_prompt_file_path = self.normalize_prompt_path(os.path.join(self.temp_dir, temp_prompt_file_name))

		with open(temp_prompt_file_path, "w", encoding="utf-8") as file:
			file.write(generate_prompt)

		return temp_prompt_file_path
