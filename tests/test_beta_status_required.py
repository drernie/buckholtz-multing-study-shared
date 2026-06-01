"""
Test that all beta definitions have required fields.

Purpose: Ensure epistemic registry discipline is maintained.
"""


from src.beta_definitions import get_all_beta_definitions


def test_all_betas_have_symbol():
    """Every beta must have a symbol."""
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        assert beta.symbol is not None
        assert len(beta.symbol) > 0


def test_all_betas_have_units():
    """Every beta must specify units (even if 'unclear')."""
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        assert beta.units is not None
        assert len(beta.units) > 0


def test_all_betas_have_status():
    """Every beta must have an explicit status."""
    all_betas = get_all_beta_definitions()

    valid_statuses = [
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
    ]

    for beta in all_betas:
        assert beta.status is not None, f"{beta.name} has no status"
        assert beta.status in valid_statuses, f"{beta.name} has invalid status: {beta.status}"


def test_all_betas_have_source_or_placeholder():
    """Every beta must have a source or source placeholder."""
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        assert beta.source is not None, (
            f"{beta.name} has no source. Use placeholder if source is unclear."
        )


def test_all_betas_have_interpretation():
    """Every beta must have interpretation text."""
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        assert beta.interpretation is not None
        assert len(beta.interpretation) > 10, f"{beta.name} has trivial or missing interpretation"


def test_fact_status_requires_value_and_source():
    """
    If a beta is marked as 'fact', it must have:
    - a value
    - a source (not just placeholder)
    """
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        if beta.status == "fact":
            assert beta.value is not None, f"{beta.name} marked 'fact' but has no value"
            assert beta.source is not None, f"{beta.name} marked 'fact' but has no source"
            assert "requires clarification" not in beta.source.title.lower(), (
                f"{beta.name} marked 'fact' but source is placeholder"
            )


def test_unclear_status_has_notes():
    """If status is 'unclear', notes should explain why."""
    all_betas = get_all_beta_definitions()

    for beta in all_betas:
        if beta.status == "unclear":
            assert len(beta.normalization_notes) > 20, (
                f"{beta.name} is 'unclear' but has no explanation in normalization_notes"
            )


def test_multiple_candidates_allowed():
    """
    Test that multiple conflicting beta values are allowed.

    This is a design feature: we explicitly allow conflicting definitions
    to represent different normalizations or versions.
    """
    all_betas = get_all_beta_definitions()

    beta_d_count = sum(1 for b in all_betas if "beta_d" in b.symbol)
    beta_q_count = sum(1 for b in all_betas if "beta_q" in b.symbol)

    # Should have at least 2 candidates for each (per TS requirement)
    assert beta_d_count >= 2, "Should have multiple beta_d candidates (different normalizations)"
    assert beta_q_count >= 2, "Should have multiple beta_q candidates (different normalizations)"


def test_conflicting_values_are_documented():
    """
    When multiple values exist for same parameter,
    normalization_notes should explain the conflict.
    """
    all_betas = get_all_beta_definitions()

    # Get all beta_d values
    beta_d_betas = [b for b in all_betas if "beta_d" in b.symbol]
    beta_d_values = [b.value for b in beta_d_betas if b.value is not None]

    # If multiple values exist, check that they're different
    if len(beta_d_values) > 1:
        unique_values = set(beta_d_values)
        assert len(unique_values) > 1, (
            "Multiple beta_d entries but all have same value - should consolidate"
        )

        # Check that at least one has normalization notes
        has_normalization_explanation = any(len(b.normalization_notes) > 20 for b in beta_d_betas)
        assert has_normalization_explanation, (
            "Conflicting beta_d values exist but no normalization notes explain why"
        )


def test_every_candidate_has_source_attribution():
    """Every candidate must name its origin — NOT just carry a vague 'unclear' tag.

    Non-tautological guard (replaces the weak len>20 check): a new candidate
    cannot be added without stating which AI service produced it AND pointing to
    the authoritative provenance registry. This is the C8 anti-drift discipline:
    no untracked beta value may enter the candidate registry.
    """
    for beta in get_all_beta_definitions():
        assert beta.ai_service_source, (
            f"{beta.name} has no ai_service_source. Every candidate value must be "
            f"attributed to its origin (e.g. 'Gemini', 'ChatGPT') per docs/93."
        )
        assert "beta_provenance" in beta.normalization_notes, (
            f"{beta.name} normalization_notes must reference beta_provenance.py "
            f"(the single source of truth) so the two registries cannot drift."
        )


def test_no_candidate_framed_as_buckholtz_version():
    """Candidates must NOT be framed as Buckholtz model versions.

    Guards against re-introducing the misleading 'different version' wording that
    obscured these are AI-service outputs (skeptic finding H1).
    """
    for beta in get_all_beta_definitions():
        assert "NOT a Buckholtz model version" in beta.normalization_notes, (
            f"{beta.name} must explicitly state it is NOT a Buckholtz model version."
        )
