#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator: Copilot-based testcase atomization.

Converts cleaned testcase JSON (cases with action_substeps / expected_checkpoints)
into atomic action rows (same schema as build_testcase_actions_local.py output).

Each prompt is fully self-contained: rules from prompt.atomize_to_actions.copilot.md
plus the case data for the batch, all inlined into a single temp prompt file.
Copilot writes the output JSON directly to the specified output path.
"""

import json
import os
from typing import Any, Dict, List

from generator_copilot import GeneratorCopilot
from log_manager import get_logger
from prompt_manager import PromptManager

logger = get_logger("atomize_generator_copilot")


class GeneratorAtomizeCopilot(GeneratorCopilot):
    """Build fully self-contained atomization prompts for Copilot CLI.

    The prompt template at ``prompt/prompt.atomize_to_actions.copilot.md``
    contains two placeholders::

        {output_path}   — absolute path where Copilot must write the output JSON
        {input_data}    — the inlined cleaned-case JSON for this batch
    """

    prompt_name = "prompt.atomize_to_actions.copilot"

    def __init__(
        self,
        temp_dir: str = "tmp",
        output_dir: str = "output_copilot",
        copilot_cmd: str = "copilot.cmd",
        project_root: str = "",
    ):
        super().__init__(
            temp_dir=temp_dir,
            output_dir=output_dir,
            copilot_cmd=copilot_cmd,
            target_name="atomize",
        )
        self.project_root = (
            project_root
            or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _read_prompt_template(self) -> str:
        """Load the base prompt template from prompt/prompt.atomize_to_actions.copilot.md."""
        rel = f"prompt/{self.prompt_name}.md"
        full_path = os.path.join(self.project_root, rel)
        try:
            with open(full_path, encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"[GeneratorAtomizeCopilot] Prompt template not found: {full_path}"
            )

    def _filter_cases(self, cleaned_data: dict, case_ids: List[str]) -> dict:
        """Return a copy of cleaned_data containing only the specified cases."""
        id_set = set(case_ids)
        worksheet = [
            c for c in cleaned_data.get("Worksheet", [])
            if str(c.get("case_id", "")) in id_set
        ]
        return {
            "meta": dict(cleaned_data.get("meta", {})),
            "Worksheet": worksheet,
        }

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def build_generate_prompt(
        self,
        cleaned_data: dict,
        case_ids: List[str],
        output_path: str,
    ) -> str:
        """Build a fully self-contained atomization prompt for the given cases.

        Parameters
        ----------
        cleaned_data : dict
            Full cleaned testcase JSON (all cases).
        case_ids : list[str]
            The subset of case IDs to include in this prompt.
        output_path : str
            Absolute path where Copilot must write the output JSON.
        """
        template = self._read_prompt_template()

        # Subset input data to only the requested cases
        subset = self._filter_cases(cleaned_data, case_ids)
        input_json_str = json.dumps(subset, ensure_ascii=False, indent=2)

        # Fill placeholders
        prompt = template.replace("{output_path}", self.normalize_prompt_path(output_path))
        prompt = prompt.replace("{input_data}", input_json_str)

        return prompt

    def write_prompt_file(
        self,
        cleaned_data: dict,
        case_ids: List[str],
        output_path: str,
        batch_label: str = "",
    ) -> str:
        """Write a self-contained prompt to a temp file and return its path.

        Parameters
        ----------
        cleaned_data : dict
            Full cleaned testcase JSON.
        case_ids : list[str]
            Case IDs for this batch.
        output_path : str
            Where Copilot should write the result JSON.
        batch_label : str
            Optional label used for naming the temp file.

        Returns
        -------
        str
            Absolute path of the written prompt file.
        """
        prompt_text = self.build_generate_prompt(cleaned_data, case_ids, output_path)
        label_slug = batch_label.replace(" ", "_").replace("/", "_") or "batch"
        prompt_file = os.path.join(self.temp_dir, f"atomize_{label_slug}_prompt.md")
        with open(prompt_file, "w", encoding="utf-8") as f:
            f.write(prompt_text)
        logger.info(
            "[GeneratorAtomizeCopilot] Prompt written: %s (%d chars)",
            prompt_file,
            len(prompt_text),
        )
        return prompt_file
