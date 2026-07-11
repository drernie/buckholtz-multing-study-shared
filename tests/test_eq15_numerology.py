"""
Test alternative formulas to assess Eq.15 uniqueness.

Purpose: Check whether Eq.15-style relation is unique or part of
         a large search space of similar numerical coincidences.
"""

from src.constants import (
    COULOMB_CONSTANT,
    ELECTRON_MASS,
    ELEMENTARY_CHARGE,
    GRAVITATIONAL_CONSTANT,
    MEV_TO_KG,
    MUON_MASS,
    TAU_MASS,
)
from src.numerology_penalty import CandidateRelation, evaluate_relation


def test_eq15_original():
    """Original Eq.15 as baseline."""
    mass_ratio = (TAU_MASS.value / ELECTRON_MASS.value) ** 2
    lhs = (4.0 / 3.0) * mass_ratio**6

    m_e_kg = ELECTRON_MASS.value * MEV_TO_KG.value
    numerator = COULOMB_CONSTANT.value * (ELEMENTARY_CHARGE.value**2)
    denominator = GRAVITATIONAL_CONSTANT.value * (m_e_kg**2)
    rhs = numerator / denominator

    candidate = CandidateRelation(
        name="Eq.15 (original)",
        expression_text="(4/3) * (m_tau^2 / m_e^2)^6",
        value=lhs,
        target=rhs,
        uses_constants=["m_tau", "m_e", "k_e", "e", "G"],
        arbitrary_choices=1,  # The 4/3 prefactor
        has_physical_mechanism=False,  # No mechanism provided yet
        uses_cosmological_observations=False,
        notes="Original relation from Buckholtz",
    )

    result = evaluate_relation(candidate)

    print("\n=== Eq.15 Original ===")
    print(f"Relative error: {result['relative_error'] * 100:.2f}%")
    print(f"Penalized score: {result['penalized_score']:.1f}/10")
    print(f"Verdict: {result['verdict']}")

    assert result["relative_error"] < 0.01  # Should reproduce


def test_alternative_exponent_11():
    """Try exponent 11 instead of 6 (i.e., 11th power of simple ratio)."""
    mass_ratio_simple = TAU_MASS.value / ELECTRON_MASS.value  # Not squared
    lhs = mass_ratio_simple**11

    m_e_kg = ELECTRON_MASS.value * MEV_TO_KG.value
    numerator = COULOMB_CONSTANT.value * (ELEMENTARY_CHARGE.value**2)
    denominator = GRAVITATIONAL_CONSTANT.value * (m_e_kg**2)
    rhs = numerator / denominator

    candidate = CandidateRelation(
        name="Alternative: (m_tau/m_e)^11",
        expression_text="(m_tau/m_e)^11",
        value=lhs,
        target=rhs,
        uses_constants=["m_tau", "m_e", "k_e", "e", "G"],
        arbitrary_choices=0,
        has_physical_mechanism=False,
        uses_cosmological_observations=False,
        notes="Testing different exponent",
    )

    result = evaluate_relation(candidate)

    print("\n=== Alternative: exponent 11 ===")
    print(f"Relative error: {result['relative_error'] * 100:.2f}%")
    print(f"Penalized score: {result['penalized_score']:.1f}/10")
    print(f"Verdict: {result['verdict']}")

    # Real check, not print-only: exponent 11 is dramatically worse than the
    # original (0.06% error) -- ~100% error, i.e. no numerical agreement at
    # all. This is what "not part of a broad numerology family" looks like.
    assert result["relative_error"] > 0.5, (
        f"exponent-11 alternative unexpectedly close to target "
        f"({result['relative_error'] * 100:.4f}% error) -- re-examine uniqueness claim"
    )


def test_alternative_exponent_13():
    """Try exponent 13."""
    mass_ratio_simple = TAU_MASS.value / ELECTRON_MASS.value
    lhs = mass_ratio_simple**13

    m_e_kg = ELECTRON_MASS.value * MEV_TO_KG.value
    numerator = COULOMB_CONSTANT.value * (ELEMENTARY_CHARGE.value**2)
    denominator = GRAVITATIONAL_CONSTANT.value * (m_e_kg**2)
    rhs = numerator / denominator

    candidate = CandidateRelation(
        name="Alternative: (m_tau/m_e)^13",
        expression_text="(m_tau/m_e)^13",
        value=lhs,
        target=rhs,
        uses_constants=["m_tau", "m_e", "k_e", "e", "G"],
        arbitrary_choices=0,
        has_physical_mechanism=False,
        uses_cosmological_observations=False,
        notes="Testing different exponent",
    )

    result = evaluate_relation(candidate)

    print("\n=== Alternative: exponent 13 ===")
    print(f"Relative error: {result['relative_error'] * 100:.2f}%")
    print(f"Penalized score: {result['penalized_score']:.1f}/10")
    print(f"Verdict: {result['verdict']}")

    # Real check: exponent 13 overshoots the target by ~2600x (relative
    # error >> 1), the opposite failure mode from exponent 11's undershoot.
    assert result["relative_error"] > 10.0, (
        f"exponent-13 alternative unexpectedly close to target "
        f"({result['relative_error'] * 100:.4f}% error) -- re-examine uniqueness claim"
    )


def test_alternative_muon_based():
    """Try muon instead of tau."""
    mass_ratio = (MUON_MASS.value / ELECTRON_MASS.value) ** 2
    lhs = (4.0 / 3.0) * mass_ratio**6

    m_e_kg = ELECTRON_MASS.value * MEV_TO_KG.value
    numerator = COULOMB_CONSTANT.value * (ELEMENTARY_CHARGE.value**2)
    denominator = GRAVITATIONAL_CONSTANT.value * (m_e_kg**2)
    rhs = numerator / denominator

    candidate = CandidateRelation(
        name="Alternative: muon-based",
        expression_text="(4/3) * (m_mu^2 / m_e^2)^6",
        value=lhs,
        target=rhs,
        uses_constants=["m_mu", "m_e", "k_e", "e", "G"],
        arbitrary_choices=1,
        has_physical_mechanism=False,
        uses_cosmological_observations=False,
        notes="Using muon instead of tau",
    )

    result = evaluate_relation(candidate)

    print("\n=== Alternative: muon-based ===")
    print(f"Relative error: {result['relative_error'] * 100:.2f}%")
    print(f"Penalized score: {result['penalized_score']:.1f}/10")
    print(f"Verdict: {result['verdict']}")

    # Real check: swapping in the muon gives essentially zero agreement
    # (relative error ~1, i.e. ~100% off) -- the relation is tau-specific,
    # not a generic "any charged lepton works" coincidence.
    assert result["relative_error"] > 0.9, (
        f"muon-based alternative unexpectedly close to target "
        f"({result['relative_error'] * 100:.4f}% error) -- re-examine tau-specificity claim"
    )


def test_alternative_different_prefactor():
    """Try different prefactor (e.g., 1 instead of 4/3)."""
    mass_ratio = (TAU_MASS.value / ELECTRON_MASS.value) ** 2
    lhs = 1.0 * mass_ratio**6  # No 4/3

    m_e_kg = ELECTRON_MASS.value * MEV_TO_KG.value
    numerator = COULOMB_CONSTANT.value * (ELEMENTARY_CHARGE.value**2)
    denominator = GRAVITATIONAL_CONSTANT.value * (m_e_kg**2)
    rhs = numerator / denominator

    candidate = CandidateRelation(
        name="Alternative: no prefactor",
        expression_text="(m_tau^2 / m_e^2)^6",
        value=lhs,
        target=rhs,
        uses_constants=["m_tau", "m_e", "k_e", "e", "G"],
        arbitrary_choices=0,
        has_physical_mechanism=False,
        uses_cosmological_observations=False,
        notes="Testing without 4/3 prefactor",
    )

    result = evaluate_relation(candidate)

    print("\n=== Alternative: no 4/3 prefactor ===")
    print(f"Relative error: {result['relative_error'] * 100:.2f}%")
    print(f"Penalized score: {result['penalized_score']:.1f}/10")
    print(f"Verdict: {result['verdict']}")

    # Real check: dropping the 4/3 prefactor gives ~25% error -- much worse
    # than the original's 0.06%, but not catastrophic like the other
    # alternatives above. The prefactor matters, but this is the closest
    # near-miss of the family and worth keeping visible as such.
    assert result["relative_error"] > 0.2, (
        f"no-prefactor alternative unexpectedly close to target "
        f"({result['relative_error'] * 100:.4f}% error) -- re-examine prefactor necessity claim"
    )


def test_summary_numerology_audit():
    """
    Summary: compare all alternatives.

    This test documents the search space exploration.
    If multiple formulas achieve similar precision, uniqueness is questionable.
    """
    print("\n" + "=" * 60)
    print("NUMEROLOGY AUDIT SUMMARY")
    print("=" * 60)
    print("\nThis test suite checks whether Eq.15 is unique or part of a")
    print("large family of numerically similar relations.")
    print("\nKEY QUESTIONS:")
    print("1. Do other exponents work equally well?")
    print("2. Does the 4/3 prefactor matter?")
    print("3. Does tau choice matter (vs muon)?")
    print("\nINTERPRETATION:")
    print("- If only original Eq.15 works → more unique")
    print("- If many alternatives work → numerology risk")
    print("=" * 60)

    # Real check tying the summary together: none of the four alternatives
    # tested above come within 20% of the target, while the original is
    # within 0.06%. This is what "the search space around Eq.15 is not
    # crowded with equally-good alternatives" looks like numerically -- not
    # a proof of uniqueness (only 4 alternatives were tried), but a real,
    # asserted fact about those 4, not just a printed narrative.
    m_e_kg = ELECTRON_MASS.value * MEV_TO_KG.value
    rhs = (COULOMB_CONSTANT.value * (ELEMENTARY_CHARGE.value**2)) / (
        GRAVITATIONAL_CONSTANT.value * (m_e_kg**2)
    )
    r_tau = TAU_MASS.value / ELECTRON_MASS.value
    r_mu = MUON_MASS.value / ELECTRON_MASS.value
    alt_errors = {
        "exp11": abs(r_tau**11 - rhs) / rhs,
        "exp13": abs(r_tau**13 - rhs) / rhs,
        "muon": abs((4.0 / 3.0) * (r_mu**2) ** 6 - rhs) / rhs,
        "no_prefactor": abs((r_tau**2) ** 6 - rhs) / rhs,
    }
    original_error = abs((4.0 / 3.0) * (r_tau**2) ** 6 - rhs) / rhs
    for name, err in alt_errors.items():
        assert err > 0.2, f"{name} alternative unexpectedly close to target ({err * 100:.4f}%)"
    assert original_error < 0.01
    assert all(err > 20 * original_error for err in alt_errors.values()), (
        "an alternative closed in on the original's precision -- re-examine uniqueness claim"
    )
