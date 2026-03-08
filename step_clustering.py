from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import hdbscan
import numpy as np
from sentence_transformers import SentenceTransformer


@dataclass
class Cluster:
    """Container for one semantic cluster of normalized test steps."""

    cluster_id: int
    examples: List[str]


def _embed_steps(steps: List[str], model_name: str) -> np.ndarray:
    """Convert step text into dense sentence embeddings."""
    model = SentenceTransformer(model_name)
    embeddings = model.encode(steps, normalize_embeddings=True, convert_to_numpy=True)
    return embeddings


def _cluster_embeddings(
    embeddings: np.ndarray,
    min_cluster_size: int,
    min_samples: int | None,
) -> np.ndarray:
    """Run HDBSCAN on sentence embeddings and return one label per input step."""
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=min_samples,
        metric="euclidean",
        cluster_selection_method="eom",
    )
    return clusterer.fit_predict(embeddings)


def _to_cluster_objects(steps: List[str], labels: np.ndarray) -> List[Cluster]:
    """Group step strings by cluster label and convert to output objects."""
    grouped: Dict[int, List[str]] = {}

    # HDBSCAN uses -1 for noise. Keep noise items but assign deterministic IDs later.
    for step, label in zip(steps, labels):
        grouped.setdefault(int(label), []).append(step)

    clusters: List[Cluster] = []
    next_cluster_id = 1

    # Stable ordering: non-noise clusters first, then noise entries.
    ordered_labels = [label for label in sorted(grouped) if label != -1]
    if -1 in grouped:
        ordered_labels.append(-1)

    for label in ordered_labels:
        examples = grouped[label]
        if label == -1:
            # Split noise items into single-item clusters so each outlier remains explicit.
            for example in examples:
                clusters.append(Cluster(cluster_id=next_cluster_id, examples=[example]))
                next_cluster_id += 1
        else:
            clusters.append(Cluster(cluster_id=next_cluster_id, examples=examples))
            next_cluster_id += 1

    return clusters


def cluster_steps(
    steps: List[str],
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    min_cluster_size: int = 2,
    min_samples: int | None = 1,
) -> List[Cluster]:
    """Cluster normalized steps by semantic similarity.

    Pipeline:
    1. Validate and clean input steps.
    2. Encode each step using sentence embeddings.
    3. Cluster embeddings with HDBSCAN.
    4. Return semantic groups in `Cluster` objects.
    """
    cleaned_steps = [step.strip() for step in steps if step and step.strip()]
    if not cleaned_steps:
        return []

    if len(cleaned_steps) == 1:
        return [Cluster(cluster_id=1, examples=[cleaned_steps[0]])]

    embeddings = _embed_steps(cleaned_steps, model_name)
    labels = _cluster_embeddings(embeddings, min_cluster_size=min_cluster_size, min_samples=min_samples)
    return _to_cluster_objects(cleaned_steps, labels)


def clusters_to_dict(clusters: List[Cluster]) -> List[Dict[str, object]]:
    """Convert `Cluster` objects to the requested JSON-serializable format."""
    return [{"cluster_id": cluster.cluster_id, "examples": cluster.examples} for cluster in clusters]


if __name__ == "__main__":
    sample_steps = [
        "press dss key",
        "press emergency key",
        "press programmable key",
        "long press speaker key",
        "short press speaker key",
        "tap screen button",
    ]

    result = cluster_steps(sample_steps)
    # Print a JSON-like preview for quick manual verification.
    for cluster in clusters_to_dict(result):
        print(cluster)
