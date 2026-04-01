from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List

from openai import OpenAI


def load_allowed_actions_from_capability_registry(path: Path | None) -> set[str]:
    if not path or not path.exists():
        return set()

    payload = load_json(path)
    if not isinstance(payload, dict):
        return set()

    action_root = payload.get("action")
    if not isinstance(action_root, dict):
        annotations_root = payload.get("annotations", {})
        action_root = annotations_root.get("action", {}) if isinstance(annotations_root, dict) else {}

    if not isinstance(action_root, dict):
        return set()

    actions: set[str] = set()
    for _, values in action_root.items():
        if isinstance(values, list):
            for item in values:
                if isinstance(item, str) and item.strip():
                    actions.add(item.strip())
        elif isinstance(values, dict):
            for item in values.keys():
                if isinstance(item, str) and item.strip():
                    actions.add(item.strip())
    return actions


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sanitize_result(obj: Dict[str, Any], cluster_id: int, allowed_actions: set[str]) -> Dict[str, Any]:
    action = str(obj.get("standard_action", "generic_action")).strip()
    if action not in allowed_actions:
        action = "generic_action"

    params = obj.get("parameters", [])
    clean_params: List[Dict[str, Any]] = []
    if isinstance(params, list):
        for p in params:
            if not isinstance(p, dict):
                continue
            clean_params.append(
                {
                    "name": str(p.get("name", "")).strip(),
                    "type": str(p.get("type", "string")).strip() or "string",
                    "description": str(p.get("description", "")).strip(),
                    "example": str(p.get("example", "")).strip(),
                }
            )

    out: Dict[str, Any] = {
        "cluster_id": cluster_id,
        "standard_action": action,
        "parameters": clean_params,
        "representative_sentence": str(obj.get("representative_sentence", "")).strip(),
    }

    notes = obj.get("notes")
    if isinstance(notes, str) and notes.strip():
        out["notes"] = notes.strip()

    return out


def call_llm_for_cluster(
    client: OpenAI,
    model: str,
    skill_text: str,
    cluster_obj: Dict[str, Any],
    allowed_actions: List[str],
    max_retries: int = 3,
) -> Dict[str, Any]:
    payload = {
        "cluster_id": cluster_obj.get("cluster_id"),
        "examples": cluster_obj.get("examples", []),
        "allowed_standard_actions": allowed_actions,
    }

    prompt = (
        "Follow the skill exactly and return strict JSON for one cluster.\n\n"
        f"Skill:\n{skill_text}\n\n"
        f"Input:\n{json.dumps(payload, ensure_ascii=False)}"
    )

    for attempt in range(1, max_retries + 1):
        try:
            resp = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                temperature=0.0,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a strict JSON generator for VoIP action schema mapping.",
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            content = resp.choices[0].message.content
            if not content:
                raise ValueError("Empty LLM response")
            return json.loads(content)
        except Exception as ex:
            if attempt >= max_retries:
                raise
            time.sleep(1.2 * attempt)

    raise RuntimeError("Unexpected retry loop state")


def run(
    input_path: Path,
    output_path: Path,
    skill_path: Path,
    capability_registry_path: Path,
    api_key: str,
    model: str,
    base_url: str,
) -> None:
    clusters = load_json(input_path)
    if not isinstance(clusters, list):
        raise ValueError("Input clusters JSON must be a list")

    skill_text = skill_path.read_text(encoding="utf-8")
    allowed_actions = load_allowed_actions_from_capability_registry(capability_registry_path)
    if not allowed_actions:
        raise ValueError("No action primitives found in capability registry: cannot determine allowed actions.")
    allowed_actions.add("generic_action")
    allowed_actions_list = sorted(allowed_actions)
    client = OpenAI(api_key=api_key, base_url=base_url)

    results: List[Dict[str, Any]] = []
    failed: List[int] = []

    for item in clusters:
        if not isinstance(item, dict):
            continue
        cluster_id = int(item.get("cluster_id", -1))
        try:
            raw = call_llm_for_cluster(client, model, skill_text, item, allowed_actions=allowed_actions_list)
            final = sanitize_result(raw, cluster_id, allowed_actions)
            results.append(final)
            print(f"Mapped cluster: {cluster_id}")
        except Exception as ex:
            failed.append(cluster_id)
            results.append(
                {
                    "cluster_id": cluster_id,
                    "standard_action": "generic_action",
                    "parameters": [],
                    "representative_sentence": "",
                    "notes": f"LLM mapping failed: {ex}",
                }
            )
            print(f"Failed cluster: {cluster_id} -> {ex}")

    save_json(output_path, results)
    print(f"Input clusters: {len(clusters)}")
    print(f"Output mappings: {len(results)}")
    print(f"Failed mappings: {len(failed)}")
    if failed:
        print(f"Failed cluster ids: {failed}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Map clustered VoIP steps to standard action schema using LLM.")
    parser.add_argument("--input", type=Path, required=True, help="Cluster JSON input file")
    parser.add_argument("--output", type=Path, required=True, help="Mapped action schema output file")
    parser.add_argument("--skill", type=Path, default=Path("skills/cluster_action_schema_skill.md"))
    parser.add_argument("--capability-registry", type=Path, default=Path("resource/capability_registry.json"))
    parser.add_argument("--model", type=str, default="deepseek-chat")
    parser.add_argument("--api-key", type=str, default=None)
    parser.add_argument("--base-url", type=str, default="https://api.deepseek.com")
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise EnvironmentError("Missing DeepSeek API key (use --api-key or DEEPSEEK_API_KEY)")

    run(
        input_path=args.input,
        output_path=args.output,
        skill_path=args.skill,
        capability_registry_path=args.capability_registry,
        api_key=api_key,
        model=args.model,
        base_url=args.base_url,
    )


if __name__ == "__main__":
    main()
