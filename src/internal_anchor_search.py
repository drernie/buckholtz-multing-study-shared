"""
Internal Anchor Search — Structured Numerology Detection

Check whether beta candidate values can be reconstructed from Buckholtz
internal anchors (Eq.20 mass ratios, N' formalism).

CRITICAL: This is a numerology risk check, not a validation.
If many alternative formulas work equally well → structured numerology risk.

All results marked as candidate_relation or structured_numerology.
"""

import itertools
from dataclasses import dataclass
from typing import Literal

# Buckholtz internal anchors from Eq.20 and N' formalism
ANCHORS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,  # From m_W² : m_Z² : m_H² :: 7 : 9 : 17
    "nine": 9,  # From m_W² : m_Z² : m_H² :: 7 : 9 : 17
    "ten": 10,  # From ΣN' = 10
    "seventeen": 17,  # From m_W² : m_Z² : m_H² :: 7 : 9 : 17
    "N_Z": 3,  # N' value for Z boson
    "N_max": 4,  # Maximum N' value
}


@dataclass(frozen=True)
class CandidateFormula:
    """
    A candidate formula generated from internal anchors.

    Status taxonomy:
    - verified_arithmetic: Matches target within 0.1%
    - candidate_relation: Matches target within 1%
    - structured_numerology: Matches target within 5% (numerology risk)
    - rejected: Error > 5%
    - requires_author_clarification: Plausible but needs verification
    """

    expression: str  # Human-readable formula (e.g., "17/4")
    value: float  # Numerical result
    target_name: str  # Which beta candidate (e.g., "beta_d_1")
    target_value: float  # Expected value
    error: float  # Relative error
    complexity: float  # Complexity score (lower is simpler)
    status: Literal[
        "verified_arithmetic",
        "candidate_relation",
        "structured_numerology",
        "rejected",
        "requires_author_clarification",
    ]
    anchor_names: tuple[str, ...]  # Which anchors were used


def generate_simple_ratios() -> list[tuple]:
    """
    Generate simple a/b ratios from anchor pairs.

    Complexity = 1 (simplest possible formula).

    Returns raw (expression, value, complexity, anchor_names) tuples, same
    convention as generate_simple_products/generate_simple_sums/
    generate_ratio_of_products below -- callers build the real
    CandidateFormula objects (WHY: the return type here previously said
    `list[CandidateFormula]`, which was wrong and made mypy's type
    inference in search_anchor_formulas' tuple-unpacking loop cascade
    into 10 unrelated-looking errors; the function's actual behavior
    never changed, only this stale annotation).
    """
    formulas = []
    anchor_items = list(ANCHORS.items())

    for (name_a, val_a), (name_b, val_b) in itertools.combinations(anchor_items, 2):
        if val_b == 0:
            continue

        # a / b
        value = val_a / val_b
        formulas.append(
            (
                f"{name_a}/{name_b}",
                value,
                1.0,  # complexity
                (name_a, name_b),
            )
        )

        # b / a
        if val_a != 0:
            value = val_b / val_a
            formulas.append(
                (
                    f"{name_b}/{name_a}",
                    value,
                    1.0,  # complexity
                    (name_b, name_a),
                )
            )

    return formulas


def generate_simple_products() -> list[tuple]:
    """
    Generate simple a*b products from anchor pairs.

    Complexity = 1.5 (slightly more complex than ratios).
    """
    formulas = []
    anchor_items = list(ANCHORS.items())

    for (name_a, val_a), (name_b, val_b) in itertools.combinations(anchor_items, 2):
        # a * b
        value = val_a * val_b
        formulas.append(
            (
                f"{name_a}*{name_b}",
                value,
                1.5,  # complexity
                (name_a, name_b),
            )
        )

    return formulas


def generate_ratio_of_products() -> list[tuple]:
    """
    Generate (a*b)/(c*d) formulas from anchor quadruples.

    Complexity = 2.0 (two operations).

    WARNING: Combinatorial explosion — limit to selected pairs.
    """
    formulas = []
    anchor_items = list(ANCHORS.items())

    # Only use meaningful pairs to avoid explosion
    # Limit to first 8 anchors (avoid N_Z, N_max for this level)
    meaningful_anchors = anchor_items[:8]

    for (n1, v1), (n2, v2) in itertools.combinations(meaningful_anchors, 2):
        for (n3, v3), (n4, v4) in itertools.combinations(meaningful_anchors, 2):
            if v3 * v4 == 0:
                continue

            # (a*b) / (c*d)
            value = (v1 * v2) / (v3 * v4)
            formulas.append(
                (
                    f"({n1}*{n2})/({n3}*{n4})",
                    value,
                    2.0,  # complexity
                    (n1, n2, n3, n4),
                )
            )

    return formulas


def generate_simple_sums() -> list[tuple]:
    """
    Generate a+b and a-b from anchor pairs.

    Complexity = 2.0 (sums are less natural for dimensionless ratios).
    """
    formulas = []
    anchor_items = list(ANCHORS.items())

    for (name_a, val_a), (name_b, val_b) in itertools.combinations(anchor_items, 2):
        # a + b
        value = val_a + val_b
        formulas.append(
            (
                f"{name_a}+{name_b}",
                value,
                2.0,  # complexity
                (name_a, name_b),
            )
        )

        # a - b
        if val_a > val_b:
            value = val_a - val_b
            formulas.append(
                (
                    f"{name_a}-{name_b}",
                    value,
                    2.0,  # complexity
                    (name_a, name_b),
                )
            )

    return formulas


def classify_match(
    error: float,
) -> Literal[
    "verified_arithmetic",
    "candidate_relation",
    "structured_numerology",
    "rejected",
]:
    """
    Classify formula based on relative error.

    Thresholds:
    - < 0.1%: verified_arithmetic (exact match)
    - < 1%: candidate_relation (very close)
    - < 5%: structured_numerology (suspiciously close)
    - >= 5%: rejected
    """
    if error < 0.001:
        return "verified_arithmetic"
    elif error < 0.01:
        return "candidate_relation"
    elif error < 0.05:
        return "structured_numerology"
    else:
        return "rejected"


def search_anchors_for_target(
    target_name: str, target_value: float, max_complexity: float = 2.0
) -> list[CandidateFormula]:
    """
    Search for anchor-based formulas matching target value.

    Parameters:
    - target_name: e.g., "beta_d_1"
    - target_value: e.g., 4.25
    - max_complexity: Maximum complexity score to consider

    Returns:
    - List of CandidateFormula sorted by error then complexity
    """
    all_formulas = []

    # Generate candidates by complexity level
    all_formulas.extend(generate_simple_ratios())
    all_formulas.extend(generate_simple_products())
    all_formulas.extend(generate_simple_sums())

    if max_complexity >= 2.0:
        # Only include ratio_of_products if allowed
        # WARNING: This can generate thousands of candidates
        ratio_products = generate_ratio_of_products()
        # Limit to first 1000 to avoid memory issues
        all_formulas.extend(ratio_products[:1000])

    # Evaluate matches
    candidates = []
    for expr, value, complexity, anchor_names in all_formulas:
        if complexity > max_complexity:
            continue

        error = abs(value - target_value) / target_value if target_value != 0 else float("inf")
        status = classify_match(error)

        candidates.append(
            CandidateFormula(
                expression=expr,
                value=value,
                target_name=target_name,
                target_value=target_value,
                error=error,
                complexity=complexity,
                status=status,
                anchor_names=anchor_names,
            )
        )

    # Sort by error first, then complexity
    candidates.sort(key=lambda c: (c.error, c.complexity))

    return candidates


def get_top_matches(
    target_name: str,
    target_value: float,
    top_n: int = 10,
    max_complexity: float = 2.0,
) -> list[CandidateFormula]:
    """
    Get top N best matches for a target value.

    Returns only candidates with status != 'rejected'.
    """
    all_candidates = search_anchors_for_target(target_name, target_value, max_complexity)

    # Filter out rejected
    non_rejected = [c for c in all_candidates if c.status != "rejected"]

    return non_rejected[:top_n]


def analyze_beta_candidates(max_complexity: float = 2.0) -> dict[str, list[CandidateFormula]]:
    """
    Analyze all known beta candidate values.

    Returns:
    - Dictionary mapping beta_name → list of matching formulas
    """
    targets = {
        "beta_d_1": 4.25,
        "beta_d_2": 0.78,
        "beta_q_1": 8.10,
        "beta_q_2": 0.19,
    }

    results = {}
    for name, value in targets.items():
        results[name] = get_top_matches(name, value, top_n=20, max_complexity=max_complexity)

    return results


def compute_uniqueness_score(candidates: list[CandidateFormula]) -> dict:
    """
    Compute uniqueness score for a set of candidate formulas.

    Returns:
    - uniqueness_score: float (0 = many alternatives, 1 = unique)
    - alternative_count: int (number of formulas with error < 5%)
    - verified_count: int (number with error < 0.1%)
    - verdict: str (unique / plausible / structured_numerology)
    """
    verified = [c for c in candidates if c.status == "verified_arithmetic"]
    candidate_rel = [c for c in candidates if c.status == "candidate_relation"]
    structured_num = [c for c in candidates if c.status == "structured_numerology"]

    total_matches = len(verified) + len(candidate_rel) + len(structured_num)

    if total_matches == 0:
        uniqueness_score = 0.0
        verdict = "no_match"
    elif len(verified) == 1 and total_matches == 1:
        uniqueness_score = 1.0
        verdict = "unique"
    elif total_matches <= 3:
        uniqueness_score = 0.7
        verdict = "plausible"
    elif total_matches <= 10:
        uniqueness_score = 0.4
        verdict = "multiple_candidates"
    else:
        uniqueness_score = 0.1
        verdict = "structured_numerology"

    return {
        "uniqueness_score": uniqueness_score,
        "alternative_count": total_matches,
        "verified_count": len(verified),
        "candidate_count": len(candidate_rel),
        "structured_numerology_count": len(structured_num),
        "verdict": verdict,
    }
