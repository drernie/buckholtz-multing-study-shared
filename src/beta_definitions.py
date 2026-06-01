"""
Beta parameter definitions for IDM/MULTING.

CRITICAL: This module explicitly allows conflicting definitions.
          Do NOT assume one value is "correct".
          All candidate values are recorded with their sources and interpretations.

PROVENANCE NOTE (added 2026-06-01 after multi-AI supplementary review, docs/93):
    The candidate values below ({4.25, 0.78} for beta_d, {8.10, 0.19} for beta_q)
    are NOT different "versions" of Buckholtz's model. They are fitted outputs of
    different AI services that the author asked to choose beta values
    (source-confirmed from the supplementary materials):
        - Gemini : beta_d = 4.25, beta_q = 8.10
        - ChatGPT: beta_d = 0.78, beta_q = 0.19
        - Claude : beta_d = 4.5,  beta_q = 18.0  (Table A1 caption — see beta_provenance.py)
    The Claude pair (4.5 / 18.0) is the actual Table A1 caption value and lives in
    `beta_provenance.py`, which is the SINGLE SOURCE OF TRUTH for provenance and
    use-permission. This module is a legacy-but-active candidate registry kept for
    the numerical-relations analysis (test_beta_normalization_math.py); always
    consult `beta_provenance.py` before using any value for modeling.

    Earlier audit notes reconstructed some of these numbers from internal anchors
    (e.g. 4.25 ~ 17/4); that provenance is CONTESTED against the AI-service
    attribution above and is documented in docs/WHAT_THIS_REPRODUCES.md.
"""

from dataclasses import dataclass

from .epistemic_registry import SourceRef, Status


@dataclass(frozen=True)
class BetaDefinition:
    """
    Definition of a beta parameter (beta_d or beta_q).

    Multiple conflicting definitions may exist for the same parameter
    if they represent different normalizations, versions, or contexts.
    """

    name: str
    symbol: str
    value: float | None
    units: str
    source: SourceRef | None
    equation_ref: str | None  # Reference to equation that defines or uses it
    interpretation: str
    status: Status
    normalization_notes: str = ""
    # AI service that produced this fitted value (source-confirmed, docs/93).
    # Empty string = not attributed to a specific AI service.
    ai_service_source: str = ""


# Placeholder source for values requiring clarification
SOURCE_REQUIRES_CLARIFICATION = SourceRef(
    id="buckholtz_unclear",
    title="Buckholtz communications (requires clarification)",
    location="Multiple sources with conflicting values",
    note="Beta values appear in different contexts with different normalizations",
)


# Beta_d candidate definitions
BETA_D_CANDIDATE_1 = BetaDefinition(
    name="Beta_d (candidate value 4.25)",
    symbol="beta_d",
    value=4.25,
    units="dimensionless or length scale (unclear)",
    source=SOURCE_REQUIRES_CLARIFICATION,
    equation_ref="H(z) fit relation",
    interpretation="Dipole scale parameter (candidate 1)",
    status="unclear",
    normalization_notes=(
        "Source-confirmed (docs/93) as the Gemini AI-service fitted output, "
        "NOT a Buckholtz model version. Dimensionless scaling factor "
        "(r_dA = beta_d * r_A). Earlier audit reconstructed 4.25 ~ 17/4 from "
        "internal anchors; that provenance is contested vs the AI-service "
        "attribution (see docs/WHAT_THIS_REPRODUCES.md). Authoritative provenance "
        "record: beta_provenance.py (beta_d_1)."
    ),
    ai_service_source="Gemini",
)

BETA_D_CANDIDATE_2 = BetaDefinition(
    name="Beta_d (candidate value 0.78)",
    symbol="beta_d",
    value=0.78,
    units="dimensionless or length scale (unclear)",
    source=SOURCE_REQUIRES_CLARIFICATION,
    equation_ref=None,
    interpretation="Dipole scale parameter (candidate 2)",
    status="unclear",
    normalization_notes=(
        "Source-confirmed (docs/93) as the ChatGPT AI-service fitted output, "
        "NOT a Buckholtz model version. The 5.8x spread vs the Gemini value "
        "(4.25) reflects inter-service disagreement on the author's loose prompt, "
        "not different normalizations of one model. Authoritative provenance "
        "record: beta_provenance.py (beta_d_2)."
    ),
    ai_service_source="ChatGPT",
)

# Beta_q candidate definitions
BETA_Q_CANDIDATE_1 = BetaDefinition(
    name="Beta_q (candidate value 8.10)",
    symbol="beta_q",
    value=8.10,
    units="dimensionless or length² scale (unclear)",
    source=SOURCE_REQUIRES_CLARIFICATION,
    equation_ref="H(z) fit relation",
    interpretation="Quadrupole scale parameter (candidate 1)",
    status="unclear",
    normalization_notes=(
        "Source-confirmed (docs/93) as the Gemini AI-service fitted output, "
        "NOT a Buckholtz model version. Dimensionless scaling factor "
        "(|r_qAB|^2 = beta_q^2 * r_A * r_P). beta_q shows the largest "
        "inter-service spread (94.7x). Authoritative provenance record: "
        "beta_provenance.py (beta_q_1, currently source_missing)."
    ),
    ai_service_source="Gemini",
)

BETA_Q_CANDIDATE_2 = BetaDefinition(
    name="Beta_q (candidate value 0.19)",
    symbol="beta_q",
    value=0.19,
    units="dimensionless or length² scale (unclear)",
    source=SOURCE_REQUIRES_CLARIFICATION,
    equation_ref=None,
    interpretation="Quadrupole scale parameter (candidate 2)",
    status="unclear",
    normalization_notes=(
        "Source-confirmed (docs/93) as the ChatGPT AI-service fitted output, "
        "NOT a Buckholtz model version. The 94.7x spread vs the Gemini value "
        "(8.10) is the strongest signal that beta_q is unconstrained by the "
        "author's prompt. Authoritative provenance record: "
        "beta_provenance.py (beta_q_2)."
    ),
    ai_service_source="ChatGPT",
)


def get_all_beta_definitions() -> list[BetaDefinition]:
    """
    Return all beta parameter definitions.

    Returns:
        List of all beta definitions, including conflicting candidates.
    """
    return [
        BETA_D_CANDIDATE_1,
        BETA_D_CANDIDATE_2,
        BETA_Q_CANDIDATE_1,
        BETA_Q_CANDIDATE_2,
    ]


def get_beta_d_candidates() -> list[BetaDefinition]:
    """Return all beta_d candidate definitions."""
    return [BETA_D_CANDIDATE_1, BETA_D_CANDIDATE_2]


def get_beta_q_candidates() -> list[BetaDefinition]:
    """Return all beta_q candidate definitions."""
    return [BETA_Q_CANDIDATE_1, BETA_Q_CANDIDATE_2]
