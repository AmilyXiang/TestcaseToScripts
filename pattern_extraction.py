from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import asdict, dataclass
from itertools import zip_longest
from pathlib import Path
from typing import Dict, List, Sequence

from openai import OpenAI


TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_\-/]+|[^\w\s]")


@dataclass
class PatternObject:
    pattern: str
    regex: str
    parameters: List[str]


def tokenize(sentence: str) -> List[str]:
    """Split a sentence into word-like tokens and punctuation tokens."""
    return TOKEN_PATTERN.findall(sentence)


def infer_parameter_name(prev_token: str | None, next_token: str | None, index: int) -> str:
    """Infer a readable placeholder name from neighboring static tokens."""
    prev_l = (prev_token or "").lower()
    next_l = (next_token or "").lower()

    if next_l == "key":
        return "key_name"
    if next_l == "button":
        return "button_name"
    if prev_l == "steps":
        return "step_index"
    if next_l in {"call", "number"}:
        return "target"

    return f"param_{index}"


def untokenize(tokens: Sequence[str]) -> str:
    """Join tokens into readable text while avoiding spaces before punctuation."""
    if not tokens:
        return ""

    no_space_before = {".", ",", ";", ":", "!", "?", ")", "]", "}"}
    no_space_after = {"(", "[", "{"}

    out = [tokens[0]]
    for token in tokens[1:]:
        if token in no_space_before:
            out.append(token)
        elif out[-1] in no_space_after:
            out.append(token)
        else:
            out.append(" " + token)
    return "".join(out)


def extract_pattern(examples: List[str]) -> PatternObject:
    """Extract one generalized pattern from multiple normalized step examples."""
    cleaned = [item.strip() for item in examples if item and item.strip()]
    if not cleaned:
        return PatternObject(pattern="", regex="", parameters=[])

    if len(cleaned) == 1:
        literal = cleaned[0]
        return PatternObject(pattern=literal, regex=re.escape(literal), parameters=[])

    tokenized = [tokenize(sentence) for sentence in cleaned]
    columns = list(zip_longest(*tokenized, fillvalue=None))

    pattern_tokens: List[str] = []
    regex_tokens: List[str] = []
    parameters: List[str] = []
    param_index = 1

    for col_index, column_values in enumerate(columns):
        unique_values = sorted({value for value in column_values if value is not None})

        # Static column: all rows share the same token.
        if len(unique_values) == 1 and None not in column_values:
            token = unique_values[0]
            pattern_tokens.append(token)
            regex_tokens.append(re.escape(token))
            continue

        prev_token = pattern_tokens[-1] if pattern_tokens else None
        next_token = None
        for look_ahead in range(col_index + 1, len(columns)):
            future_values = [v for v in columns[look_ahead] if v is not None]
            if not future_values:
                continue
            if len(set(future_values)) == 1:
                next_token = future_values[0]
                break

        name = infer_parameter_name(prev_token, next_token, param_index)
        if name in parameters:
            name = f"{name}_{param_index}"

        parameters.append(name)
        pattern_tokens.append("{" + name + "}")
        regex_tokens.append("(.*)")
        param_index += 1

    pattern_text = untokenize(pattern_tokens)
    regex_text = untokenize(regex_tokens)

    return PatternObject(pattern=pattern_text, regex=regex_text, parameters=parameters)


def extract_patterns_from_clusters(clusters: List[Dict[str, object]]) -> List[Dict[str, object]]:
    """Extract a generalized pattern for each cluster object."""
    outputs: List[Dict[str, object]] = []

    for cluster in clusters:
        cluster_id = cluster.get("cluster_id")
        examples = cluster.get("examples", [])
        pattern_obj = extract_pattern(examples if isinstance(examples, list) else [])
        outputs.append(
            {
                "cluster_id": cluster_id,
                "examples": examples,
                "pattern": asdict(pattern_obj),
            }
        )

    return outputs


def optimize_pattern_with_llm(
    client: OpenAI,
    model: str,
    examples: List[str],
    initial_pattern: PatternObject,
) -> PatternObject:
    """Use LLM to refine pattern text/regex while preserving examples coverage."""
    prompt = {
        "task": "Refine pattern extraction output",
        "rules": [
            "Keep semantics of examples.",
            "Pattern must stay automation-friendly.",
            "Regex must match all examples.",
            "Do not create extra parameters unless needed.",
            "Return strict JSON only.",
        ],
        "schema": {
            "pattern": "string",
            "regex": "string",
            "parameters": ["string"],
        },
        "examples": examples,
        "initial": asdict(initial_pattern),
    }

    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        temperature=0.0,
        messages=[
            {"role": "system", "content": "You are a QA pattern engineer. Output strict JSON only."},
            {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)},
        ],
    )

    content = response.choices[0].message.content
    if not content:
        return initial_pattern

    try:
        data = json.loads(content)
        pattern = str(data.get("pattern", "")).strip()
        regex = str(data.get("regex", "")).strip()
        parameters = data.get("parameters", [])
        if not isinstance(parameters, list):
            parameters = []
        if not pattern or not regex:
            return initial_pattern
        return PatternObject(pattern=pattern, regex=regex, parameters=[str(p) for p in parameters])
    except Exception:
        return initial_pattern


def optimize_patterns_with_llm(
    patterns: List[Dict[str, object]],
    api_key: str,
    model: str = "deepseek-chat",
    base_url: str = "https://api.deepseek.com",
) -> List[Dict[str, object]]:
    """Refine algorithmic patterns with an LLM as a final optimization pass."""
    client = OpenAI(api_key=api_key, base_url=base_url)

    optimized: List[Dict[str, object]] = []
    for item in patterns:
        examples = item.get("examples", [])
        pattern_dict = item.get("pattern", {})

        initial = PatternObject(
            pattern=str(pattern_dict.get("pattern", "")),
            regex=str(pattern_dict.get("regex", "")),
            parameters=[str(p) for p in pattern_dict.get("parameters", [])],
        )

        better = optimize_pattern_with_llm(
            client=client,
            model=model,
            examples=examples if isinstance(examples, list) else [],
            initial_pattern=initial,
        )

        optimized.append(
            {
                "cluster_id": item.get("cluster_id"),
                "examples": item.get("examples"),
                "pattern": asdict(better),
            }
        )

    return optimized


def build_patterns_file(
    input_path: Path,
    output_path: Path,
    optimize_with_llm: bool = False,
    api_key: str | None = None,
    model: str = "deepseek-chat",
    base_url: str = "https://api.deepseek.com",
) -> None:
    clusters = json.loads(input_path.read_text(encoding="utf-8"))
    patterns = extract_patterns_from_clusters(clusters)

    if optimize_with_llm:
        resolved_api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        if not resolved_api_key:
            raise EnvironmentError("Missing DEEPSEEK_API_KEY for LLM optimization")
        patterns = optimize_patterns_with_llm(
            patterns=patterns,
            api_key=resolved_api_key,
            model=model,
            base_url=base_url,
        )

    output_path.write_text(json.dumps(patterns, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract generalized patterns from clustered steps.")
    parser.add_argument("--input", type=Path, default=Path("step_clusters_from_kb_v3.json"))
    parser.add_argument("--output", type=Path, default=Path("step_patterns_from_kb_v3.json"))
    parser.add_argument("--optimize-with-llm", action="store_true")
    parser.add_argument("--api-key", type=str, default=None)
    parser.add_argument("--model", type=str, default="deepseek-chat")
    parser.add_argument("--base-url", type=str, default="https://api.deepseek.com")
    args = parser.parse_args()

    build_patterns_file(
        input_path=args.input,
        output_path=args.output,
        optimize_with_llm=args.optimize_with_llm,
        api_key=args.api_key,
        model=args.model,
        base_url=args.base_url,
    )
    print(f"Output pattern file: {args.output}")
