from __future__ import annotations

import argparse
import json
from pathlib import Path

from step_clustering import cluster_steps, clusters_to_dict


def load_steps_from_kb(input_path: Path) -> list[str]:
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    entries = payload.get("entries", [])

    # Cluster normalized actions (non-empty) as the primary step semantics.
    steps = [
        item.get("normalized_action", "")
        for item in entries
        if isinstance(item, dict) and isinstance(item.get("normalized_action"), str)
    ]
    return [s.strip() for s in steps if s and s.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run embedding + HDBSCAN clustering from normalized KB file.")
    parser.add_argument("--input", type=Path, required=True, help="Input normalized KB JSON (contains entries[]).")
    parser.add_argument("--output", type=Path, required=True, help="Output clusters JSON path.")
    parser.add_argument("--model", type=str, default="sentence-transformers/all-mpnet-base-v2") ## "backup mode： all-MiniLM-L6-v2"
    parser.add_argument("--min-cluster-size", type=int, default=2)
    parser.add_argument("--min-samples", type=int, default=1)
    args = parser.parse_args()

    steps = load_steps_from_kb(args.input)
    clusters = cluster_steps(
        steps,
        model_name=args.model,
        min_cluster_size=args.min_cluster_size,
        min_samples=args.min_samples,
    )
    output = clusters_to_dict(clusters)

    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Input: {args.input}")
    print(f"Total normalized_action steps: {len(steps)}")
    print(f"Output: {args.output}")
    print(f"Total clusters: {len(output)}")


if __name__ == "__main__":
    main()
