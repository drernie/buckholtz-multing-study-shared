"""
Anti-numerology scoring system.

Purpose: Detect and penalize arbitrary numerical relations that lack
         physical mechanism or use cosmological observations circularly.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CandidateRelation:
    """A candidate numerical relation to be evaluated."""

    name: str
    expression_text: str
    value: float
    target: float
    uses_constants: list[str]  # List of constant symbols used
    arbitrary_choices: int  # Count of arbitrary multipliers/divisors
    has_physical_mechanism: bool
    uses_cosmological_observations: bool
    notes: str = ""


def relative_error(value: float, target: float) -> float:
    """
    Calculate relative error between value and target.

    Args:
        value: Computed value
        target: Target value to match

    Returns:
        Absolute relative error: |value - target| / |target|
    """
    if target == 0:
        raise ValueError("Target cannot be zero for relative error calculation")
    return abs(value - target) / abs(target)


def complexity_penalty(arbitrary_choices: int) -> float:
    """
    Penalty for arbitrary choices in formula.

    Args:
        arbitrary_choices: Number of arbitrary multipliers like /32, *100, etc.

    Returns:
        Penalty score: 0 (no penalty) to 5 (severe penalty)
    """
    # Each arbitrary choice adds penalty
    # 0 choices: 0 penalty
    # 1 choice: 1 penalty
    # 2 choices: 2 penalty
    # 3+ choices: 5 penalty (formula is too flexible)
    if arbitrary_choices == 0:
        return 0.0
    elif arbitrary_choices == 1:
        return 1.0
    elif arbitrary_choices == 2:
        return 2.0
    else:
        return 5.0


def data_leakage_penalty(uses_cosmological_observations: bool) -> float:
    """
    Penalty for using cosmological observations to predict "fundamental" parameters.

    Args:
        uses_cosmological_observations: Whether formula uses H0, Omega_m, etc.

    Returns:
        Penalty score: 0 (no leakage) or 5 (severe leakage)
    """
    return 5.0 if uses_cosmological_observations else 0.0


def mechanism_bonus(has_physical_mechanism: bool) -> float:
    """
    Bonus for having a physical mechanism.

    Args:
        has_physical_mechanism: Whether a physical derivation exists

    Returns:
        Bonus score: 0 (no mechanism) or 3 (mechanism exists)
    """
    return 3.0 if has_physical_mechanism else 0.0


def penalized_score(candidate: CandidateRelation) -> float:
    """
    Calculate penalized quality score for a candidate relation.

    Scoring:
    - Start with 10 (perfect)
    - Subtract complexity penalty (0-5)
    - Subtract data leakage penalty (0 or 5)
    - Add mechanism bonus (0 or 3)
    - Cap at 10 max

    Interpretation:
    - 8-10: Strong relation with mechanism
    - 5-7: Structural relation, mechanism unclear
    - 3-4: Numerical coincidence, use caution
    - 0-2: Likely numerology, do not rely on

    Args:
        candidate: Candidate relation to score

    Returns:
        Penalized score (0-10 scale)
    """
    base_score = 10.0

    # Apply penalties
    score = base_score
    score -= complexity_penalty(candidate.arbitrary_choices)
    score -= data_leakage_penalty(candidate.uses_cosmological_observations)

    # Add bonus
    score += mechanism_bonus(candidate.has_physical_mechanism)

    # Cap at [0, 10]
    score = max(0.0, min(10.0, score))

    return score


def evaluate_relation(candidate: CandidateRelation) -> dict:
    """
    Full evaluation of a candidate relation.

    Args:
        candidate: Candidate to evaluate

    Returns:
        Dictionary with evaluation results
    """
    rel_error = relative_error(candidate.value, candidate.target)
    score = penalized_score(candidate)

    # Determine verdict
    if score >= 8 and rel_error < 0.01:
        verdict = "STRONG"
    elif score >= 5 and rel_error < 0.05:
        verdict = "PLAUSIBLE"
    elif score >= 3:
        verdict = "WEAK"
    else:
        verdict = "NUMEROLOGY"

    return {
        "name": candidate.name,
        "relative_error": rel_error,
        "penalized_score": score,
        "verdict": verdict,
        "warnings": _generate_warnings(candidate, score, rel_error),
    }


def _generate_warnings(candidate: CandidateRelation, score: float, rel_error: float) -> list[str]:
    """Generate warning messages based on evaluation."""
    warnings = []

    if candidate.arbitrary_choices > 0:
        warnings.append(
            f"Formula contains {candidate.arbitrary_choices} arbitrary choice(s). "
            f"Each choice increases search space and reduces uniqueness."
        )

    if candidate.uses_cosmological_observations:
        warnings.append(
            "Formula uses cosmological observations (H0, Omega, etc.). "
            "This creates circular reasoning risk: using fitted values "
            "to predict 'fundamental' parameters."
        )

    if not candidate.has_physical_mechanism:
        warnings.append(
            "No physical mechanism provided. "
            "Numerical agreement alone does not establish physics."
        )

    if rel_error < 0.01 and score < 5:
        warnings.append(
            "Beautiful numerical match (<1% error) but low quality score. "
            "This is a red flag for numerology: many formulas can achieve "
            "this precision with enough free parameters."
        )

    return warnings
