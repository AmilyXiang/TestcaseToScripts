from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, List

from openai import OpenAI


ALLOWED_ACTIONS = {
    "dial_call",
    "answer_call",
    "hangup_call",
    "hold_call",
    "resume_call",
    "switch_call",
    "mute_call",
    "unmute_call",
    "transfer_call",
    "conference_start",
    "conference_join",
    "key_press",
    "configure_settings",
    "check_display",
    "wait",
    "power_cycle",
    "lock_device",
    "unlock_device",
    "enter_pin",
    "verify",
    "generic_action",
}


def parse_allowed_actions_from_skill(skill_text: str) -> set[str]:
    """Extract allowed actions from the "Allowed Standard Actions" section in skill markdown."""
    marker = "## Allowed Standard Actions"
    idx = skill_text.find(marker)
    if idx < 0:
        return set(ALLOWED_ACTIONS)

    tail = skill_text[idx + len(marker) :]
    # Stop at next markdown heading to avoid parsing unrelated bullet lists.
    next_heading = tail.find("\n## ")
    section = tail if next_heading < 0 else tail[:next_heading]

    actions: set[str] = set()
    for line in section.splitlines():
        m = re.match(r"\s*-\s*`([^`]+)`\s*$", line)
        if m:
            actions.add(m.group(1).strip())

    return actions or set(ALLOWED_ACTIONS)


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
    max_retries: int = 3,
) -> Dict[str, Any]:
    payload = {
        "cluster_id": cluster_obj.get("cluster_id"),
        "examples": cluster_obj.get("examples", []),
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
    api_key: str,
    model: str,
    base_url: str,
) -> None:
    clusters = load_json(input_path)
    if not isinstance(clusters, list):
        raise ValueError("Input clusters JSON must be a list")

    skill_text = skill_path.read_text(encoding="utf-8")
    allowed_actions = parse_allowed_actions_from_skill(skill_text)
    client = OpenAI(api_key=api_key, base_url=base_url)

    results: List[Dict[str, Any]] = []
    failed: List[int] = []

    for item in clusters:
        if not isinstance(item, dict):
            continue
        cluster_id = int(item.get("cluster_id", -1))
        try:
            raw = call_llm_for_cluster(client, model, skill_text, item)
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
        api_key=api_key,
        model=args.model,
        base_url=args.base_url,
    )


if __name__ == "__main__":
    main()
