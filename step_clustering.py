from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, List, Literal, Optional

import hdbscan
import numpy as np
from sentence_transformers import SentenceTransformer


@dataclass
class Cluster:
    """Container for one semantic cluster of normalized test steps."""

    cluster_id: int
    examples: List[str]


def normalize_step_text(text: str) -> str:
    """
    Normalize a step string for more consistent embedding.
    - lowercases
    - strips leading/trailing whitespace
    - collapses multiple spaces
    - removes a trailing period (optional)
    """
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    # Remove a single trailing period if present (keeps internal decimals safe)
    if text.endswith("."):
        text = text[:-1].rstrip()
    return text


def _embed_steps(
    steps: List[str],
    model_name: str,
    normalize: bool = True,
    show_progress: bool = False,
) -> np.ndarray:
    """Convert step text into dense sentence embeddings, optionally normalized."""
    if normalize:
        steps = [normalize_step_text(step) for step in steps]

    model = SentenceTransformer(model_name)
    embeddings = model.encode(
        steps,
        normalize_embeddings=True,
        convert_to_numpy=True,
        show_progress_bar=show_progress,
    )
    return embeddings


def _cluster_embeddings(
    embeddings: np.ndarray,
    min_cluster_size: int,
    min_samples: Optional[int],
) -> np.ndarray:
    """Run HDBSCAN on sentence embeddings and return one label per input step."""
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster_size,
        min_samples=min_samples,
        metric="euclidean",
        cluster_selection_method="eom",
    )
    return clusterer.fit_predict(embeddings)


def _to_cluster_objects(
    steps: List[str],
    labels: np.ndarray,
    noise_strategy: Literal["single", "merge", "ignore"] = "single",
) -> List[Cluster]:
    """
    Group step strings by cluster label and convert to output objects.

    noise_strategy:
        - "single": each noise point becomes its own cluster (preserves all data)
        - "merge": all noise points are merged into one cluster
        - "ignore": noise points are discarded
    """
    grouped: Dict[int, List[str]] = {}

    for step, label in zip(steps, labels):
        grouped.setdefault(int(label), []).append(step)

    clusters: List[Cluster] = []
    next_cluster_id = 1

    # Process non‑noise clusters first (labels >= 0)
    for label in sorted(grouped):
        if label == -1:
            continue
        clusters.append(Cluster(cluster_id=next_cluster_id, examples=grouped[label]))
        next_cluster_id += 1

    # Handle noise (label == -1)
    if -1 in grouped:
        noise_examples = grouped[-1]
        if noise_strategy == "single":
            for ex in noise_examples:
                clusters.append(Cluster(cluster_id=next_cluster_id, examples=[ex]))
                next_cluster_id += 1
        elif noise_strategy == "merge":
            clusters.append(Cluster(cluster_id=next_cluster_id, examples=noise_examples))
            next_cluster_id += 1
        # "ignore" does nothing

    return clusters


def cluster_steps(
    steps: List[str],
    model_name: str = "sentence-transformers/all-mpnet-base-v2",
    min_cluster_size: int = 2,
    min_samples: Optional[int] = 1,
    noise_strategy: Literal["single", "merge", "ignore"] = "single",
    normalize_text: bool = True,
    show_progress: bool = False,
) -> List[Cluster]:
    """
    Cluster normalized steps by semantic similarity.

    Parameters
    ----------
    steps : list of str
        Input step sentences.
    model_name : str
        Name of a Sentence‑Transformers model.
    min_cluster_size : int
        Minimum size of a cluster (passed to HDBSCAN).
    min_samples : int or None
        Minimum samples parameter for HDBSCAN.
    noise_strategy : {"single", "merge", "ignore"}
        How to treat points labelled as noise (-1).
    normalize_text : bool
        Whether to apply basic text normalization before embedding.
    show_progress : bool
        Show a progress bar during embedding.

    Returns
    -------
    List[Cluster]
        Each Cluster contains a cluster_id and a list of example steps.
    """
    # Remove empty / whitespace‑only steps
    cleaned_steps = [step.strip() for step in steps if step and step.strip()]
    if not cleaned_steps:
        return []

    if len(cleaned_steps) == 1:
        return [Cluster(cluster_id=1, examples=[cleaned_steps[0]])]

    embeddings = _embed_steps(
        cleaned_steps,
        model_name=model_name,
        normalize=normalize_text,
        show_progress=show_progress,
    )
    labels = _cluster_embeddings(
        embeddings,
        min_cluster_size=min_cluster_size,
        min_samples=min_samples,
    )
    return _to_cluster_objects(cleaned_steps, labels, noise_strategy=noise_strategy)


def clusters_to_dict(clusters: List[Cluster]) -> List[Dict[str, object]]:
    """Convert `Cluster` objects to JSON‑serializable format."""
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

    result = cluster_steps(sample_steps, show_progress=True)
    for cluster in clusters_to_dict(result):
        print(cluster)