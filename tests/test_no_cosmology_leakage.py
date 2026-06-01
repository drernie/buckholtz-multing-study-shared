"""
Test that beta candidate formulas do not use cosmological observations.

Purpose: Prevent circular reasoning where H0, Omega_m, etc. are used
         to derive "fundamental" beta parameters.
"""


from src.beta_definitions import get_all_beta_definitions
from src.data_anchoring import get_high_leakage_risk


def test_beta_definitions_exist():
    """Verify beta definitions are registered."""
    all_betas = get_all_beta_definitions()
    assert len(all_betas) > 0, "No beta definitions found"

    beta_d_found = any("beta_d" in b.symbol for b in all_betas)
    beta_q_found = any("beta_q" in b.symbol for b in all_betas)

    assert beta_d_found, "No beta_d definitions found"
    assert beta_q_found, "No beta_q definitions found"


def test_beta_definitions_have_status():
    """Every beta definition must have a status."""
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        assert beta.status is not None, f"Beta {beta.name} has no status"
        assert beta.status in [
            "fact",
            "calculation",
            "hypothesis",
            "inference",
            "assumption",
            "fitted",
            "derived",
            "unknown",
            "unclear",
            "requires_source_verification",
        ], f"Beta {beta.name} has invalid status: {beta.status}"


def test_beta_definitions_have_units():
    """Every beta definition must specify units (even if unclear)."""
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        assert beta.units is not None, f"Beta {beta.name} has no units field"
        assert len(beta.units) > 0, f"Beta {beta.name} has empty units"


def test_beta_definitions_have_interpretation():
    """Every beta definition must have interpretation text."""
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        assert beta.interpretation is not None, f"Beta {beta.name} has no interpretation"
        assert len(beta.interpretation) > 0, f"Beta {beta.name} has empty interpretation"


def test_no_cosmology_leakage_in_beta_notes():
    """
    Check that beta definition notes do not reference cosmological observations.

    This is a heuristic check: search for keywords that suggest data leakage.
    """
    # Keywords that suggest cosmological observation usage
    leakage_keywords = [
        "H0",
        "H_0",
        "Hubble constant fitted",
        "Omega_m fitted",
        "Omega_Lambda fitted",
        "Pantheon fit",
        "Planck fit",
        "fitted to SNIa",
        "fitted to CMB",
        "cosmic chronometer fit",
    ]

    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        notes_lower = beta.normalization_notes.lower()

        for keyword in leakage_keywords:
            if keyword.lower() in notes_lower:
                # If keyword found, beta must be marked with leakage warning
                assert "leakage" in notes_lower or "circular" in notes_lower, (
                    f"Beta {beta.name} mentions '{keyword}' but does not "
                    f"warn about data leakage or circular reasoning risk."
                )


def test_high_leakage_datasets_are_documented():
    """Verify high-leakage datasets are in the registry."""
    high_risk = get_high_leakage_risk()

    # Should include at least these
    names = {anchor.name for anchor in high_risk}

    assert "Planck CMB" in names, "Planck CMB should be marked as high leakage risk"
    assert "Cosmic chronometers H(z)" in names or any(
        "H(z)" in n for n in names
    ), "H(z) measurements should be marked as high leakage risk"


def test_candidate_beta_formulas_marked_if_using_observations():
    """
    If a beta candidate formula uses cosmological observations,
    it must be explicitly marked.

    This test is a placeholder: when candidate formulas are added,
    ensure they include a flag like:

        uses_cosmological_observations = True/False

    For now, we check that the concept exists in the numerology module.
    """
    from src.numerology_penalty import CandidateRelation

    # Example: a hypothetical bad formula
    bad_formula = CandidateRelation(
        name="Bad example: beta_d = H0 / 100",
        expression_text="beta_d = H0 / 100",
        value=0.7,
        target=0.7,
        uses_constants=["H0"],
        arbitrary_choices=1,
        has_physical_mechanism=False,
        uses_cosmological_observations=True,  # Must be True!
        notes="Circular reasoning: deriving beta from H0",
    )

    assert (
        bad_formula.uses_cosmological_observations is True
    ), "Example formula using H0 must be flagged"

    # Penalized score should be low due to leakage
    from src.numerology_penalty import penalized_score

    score = penalized_score(bad_formula)

    assert score <= 5, (
        f"Formula using cosmological observations should score ≤5, got {score}. "
        f"Data leakage penalty should reduce score significantly."
    )
