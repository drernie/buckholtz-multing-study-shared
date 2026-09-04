"""
H-MULT Closure Candidates — Heuristic Scaling Records

Purpose: Document candidate H(z) heuristic formulas from AI transcript/supplementary materials.

Status: AI_TRANSCRIPT_REPORTED — phenomenological table-reproduction candidate
NOT source-confirmed physical derivation, NOT MCMC-ready forward model.

See: docs/35_ai_transcript_closure_candidate.md
"""

from dataclasses import dataclass
from enum import Enum


class ClosureStatus(Enum):
    """Source and derivation status for closure formula."""

    AI_TRANSCRIPT_REPORTED = "ai_transcript_reported"  # From AI materials, not manuscript
    FITTED_PHENOMENOLOGICAL = "fitted_phenomenological"  # Fit to data, not derived
    SOURCE_CONFIRMED = "source_confirmed"  # Verified in manuscript equation
    THEORETICALLY_DERIVED = "theoretically_derived"  # Derived from field equations


class UsePermission(Enum):
    """What operations are allowed with this closure formula."""

    ALLOWED_FOR_TABLE_REPRODUCTION_CANDIDATE = (
        "allowed_for_table_reproduction_candidate"  # May attempt Table A1 reproduction
    )
    NOT_ALLOWED_FOR_PREDICTION = "not_allowed_for_prediction"  # Cannot predict on new redshifts
    NOT_ALLOWED_FOR_MCMC = "not_allowed_for_mcmc"  # Cannot use for parameter estimation


@dataclass
class RequiredInput:
    """Input variable required to evaluate closure formula."""

    name: str  # Variable name (m_A, r_A, k_A, etc.)
    description: str  # What this variable represents
    status: str  # "KNOWN", "MISSING", "COMPUTABLE"
    blocker: str  # If MISSING, what blocks it
    source: str  # Where this value comes from (Table A1, derived, etc.)


@dataclass
class ClosureCandidate:
    """Single closure formula candidate (heuristic or rigorous)."""

    name: str  # "Phi(z) scaling", "Mean-field H(z)", etc.
    formula_text: str  # Human-readable formula
    formula_latex: str  # LaTeX representation
    status: ClosureStatus  # AI_TRANSCRIPT_REPORTED, FITTED_PHENOMENOLOGICAL, etc.
    use_permission: list[UsePermission]  # What operations allowed
    required_inputs: list[RequiredInput]  # What inputs needed to evaluate
    missing_items: list[str]  # What prevents predictive use
    safe_wording: str  # How to describe this formula safely
    unsafe_wording: str  # What NOT to say about this formula


# ============================================================================
# H-MULT Heuristic Closure Candidate
# ============================================================================


PHI_Z_SCALING_CANDIDATE = ClosureCandidate(
    name="Phi(z) Heuristic Scaling",
    formula_text=(
        "Phi(z) = A_m(z) - A_d(z) + A_q(z)\nH_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)]"
    ),
    formula_latex=(
        r"\Phi(z) = A_m(z) - A_d(z) + A_q(z)\\"
        r"H_{\text{MULT}}^2(z) = H_{\text{anchor}}^2 \times \frac{\Phi(z)}{\Phi(z_{\text{anchor}})}"
    ),
    status=ClosureStatus.AI_TRANSCRIPT_REPORTED,
    use_permission=[
        UsePermission.ALLOWED_FOR_TABLE_REPRODUCTION_CANDIDATE,
        UsePermission.NOT_ALLOWED_FOR_PREDICTION,
        UsePermission.NOT_ALLOWED_FOR_MCMC,
    ],
    required_inputs=[
        RequiredInput(
            name="m_A(z)",
            description="Mass of cluster/object A at redshift z",
            status="MISSING",
            blocker="No evolution model provided in manuscript",
            source="REQUIRED (not provided)",
        ),
        RequiredInput(
            name="r_A(z)",
            description="Characteristic radius of A at redshift z",
            status="MISSING",
            blocker="No evolution model provided in manuscript",
            source="REQUIRED (not provided)",
        ),
        RequiredInput(
            name="k_A(z)",
            description="Kinetic energy scale of A at redshift z",
            status="MISSING",
            blocker="No evolution model provided in manuscript",
            source="REQUIRED (not provided)",
        ),
        RequiredInput(
            name="D_C:AB(z)",
            description="Comoving distance between objects A and B",
            status="COMPUTABLE",
            blocker="None (standard cosmology)",
            source="Standard cosmology, but which A/B?",
        ),
        RequiredInput(
            name="beta_d",
            description="Dipole strength parameter",
            status="KNOWN",
            blocker="None",
            source="Table A1, fitted value 4.5",
        ),
        RequiredInput(
            name="beta_q",
            description="Quadrupole strength parameter",
            status="KNOWN",
            blocker="None",
            source="Table A1, fitted value 18.0",
        ),
        RequiredInput(
            name="H_anchor",
            description="Reference Hubble parameter at anchor redshift",
            status="MISSING",
            blocker="Not specified (H(z=0)? H_FLRW? other?)",
            source="REQUIRED (not provided)",
        ),
        RequiredInput(
            name="z_anchor",
            description="Anchor redshift",
            status="MISSING",
            blocker="Not specified (z=0? z=0.5? other?)",
            source="REQUIRED (not provided)",
        ),
        RequiredInput(
            name="Cluster variable table",
            description="m_A(z_i), r_A(z_i), k_A(z_i) for all z_i in Table A1",
            status="MISSING",
            blocker="CRITICAL BLOCKER — cannot evaluate Phi(z) without this",
            source="REQUIRED (not provided)",
        ),
    ],
    missing_items=[
        "Formal derivation (Phi(z) → H(z) mapping from field equations)",
        "Dataset source (which clusters? which z range?)",
        "sigma_MULT definition (how are uncertainties computed?)",
        "Cluster variable table (m_A(z), r_A(z), k_A(z) for all z)",
        "Uncertainty propagation (σ(m_A) → σ(H_MULT) formula)",
        "Parameter count (how many free parameters total?)",
        "AIC/BIC comparison (MULTING vs ΛCDM model comparison)",
        "Out-of-sample test (train/test split, cross-validation)",
    ],
    safe_wording=(
        "A possible heuristic scaling H_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)] "
        "appears in AI transcript materials. This may reproduce the reported Table A1 H_MULT "
        "column IF cluster variables (m_A(z), r_A(z), k_A(z)) are provided for all tabulated "
        "redshifts. However, this is a phenomenological formula, not a rigorous derivation from "
        "field equations. It cannot predict H(z) on new redshifts without full cluster variable "
        "table. MCMC parameter estimation remains blocked pending formal closure."
    ),
    unsafe_wording=(
        "DO NOT say: 'This predicts cosmic expansion' (requires cluster table for all z). "
        "DO NOT say: 'This validates MULTING against H(z) observations' (phenomenological fit). "
        "DO NOT say: 'This is the Buckholtz H(z) equation' (AI transcript, not source-confirmed). "
        "DO NOT say: 'MCMC shows beta_d=4.5 and beta_q=18.0 are optimal' (fitted, not tested). "
        "DO NOT say: 'H_MULT outperforms ΛCDM' (no model comparison performed). "
        "DO NOT say: 'We can now compute H(z) from MULTING' (only for z where cluster variables known)."
    ),
)


# ============================================================================
# Registry Access Functions
# ============================================================================


def get_all_closure_candidates() -> list[ClosureCandidate]:
    """Return all H-MULT closure formula candidates."""
    return [PHI_Z_SCALING_CANDIDATE]


def get_required_inputs() -> list[RequiredInput]:
    """Return all required inputs for heuristic closure candidate."""
    return PHI_Z_SCALING_CANDIDATE.required_inputs


def get_missing_inputs() -> list[RequiredInput]:
    """Return only MISSING inputs (blockers)."""
    return [inp for inp in get_required_inputs() if inp.status == "MISSING"]


def get_known_inputs() -> list[RequiredInput]:
    """Return only KNOWN inputs (beta_d, beta_q)."""
    return [inp for inp in get_required_inputs() if inp.status == "KNOWN"]


def get_critical_blockers() -> list[str]:
    """Return critical blockers that prevent table reproduction."""
    missing = get_missing_inputs()
    return [inp.blocker for inp in missing if "CRITICAL" in inp.blocker]


# ============================================================================
# Use Permission Guards (ENFORCE RESTRICTIONS)
# ============================================================================


def is_predictive_modeling_allowed() -> bool:
    """Check if predictive modeling is allowed with current closure candidate.

    Returns:
        False — always False (NOT_ALLOWED_FOR_PREDICTION).
              Cannot predict H(z) on new redshifts without cluster table.
    """
    return False


def is_mcmc_allowed() -> bool:
    """Check if MCMC parameter estimation is allowed.

    Returns:
        False — always False (NOT_ALLOWED_FOR_MCMC).
              No forward model, no likelihood, no out-of-sample validation.
    """
    return False


def is_table_reproduction_candidate() -> bool:
    """Check if Table A1 reproduction is possible (with cluster variables).

    Returns:
        True — IF cluster variables provided, can attempt table reproduction.
              But this is a CANDIDATE attempt, not guaranteed to match.
    """
    return True


def record_hmult_closure_candidate() -> ClosureCandidate:
    """Record the heuristic closure candidate formula.

    This function does NOT compute H(z).
    It ONLY returns the candidate record for documentation.

    Returns:
        ClosureCandidate: Phi(z) scaling heuristic record
    """
    return PHI_Z_SCALING_CANDIDATE


def get_closure_status_summary() -> dict[str, str]:
    """Return summary of H-MULT closure candidate status."""
    missing_count = len(get_missing_inputs())
    known_count = len(get_known_inputs())
    critical_blocker_count = len(get_critical_blockers())

    return {
        "closure_candidate": "Phi(z) heuristic scaling (AI_TRANSCRIPT_REPORTED)",
        "status": "PHENOMENOLOGICAL (table-reproduction candidate, not predictive model)",
        "required_inputs": f"{len(get_required_inputs())} total ({known_count} known, {missing_count} missing)",
        "critical_blockers": f"{critical_blocker_count} (prevent table reproduction)",
        "predictive_modeling": "NOT ALLOWED (requires cluster table for all z)",
        "mcmc_readiness": "BLOCKED (no forward model, no likelihood)",
        "table_reproduction": "CANDIDATE (possible IF cluster variables provided)",
        "safe_conclusion": (
            "Heuristic closure candidate exists but requires cluster variable table "
            "(m_A(z), r_A(z), k_A(z)) for table reproduction. Cannot predict on new "
            "redshifts. MCMC remains blocked pending rigorous physical derivation."
        ),
    }


# ============================================================================
# NO compute_Hz FUNCTION (INTENTIONAL)
# ============================================================================

# This module does NOT implement:
# - compute_Hz(z, params)
# - model_Hz(z, beta_d, beta_q)
# - Hz_forward(z, params)
# - solve_friedmann(z, params)
# - H_MULT(z, beta_d, beta_q)

# Reason: Cluster variable table (m_A(z), r_A(z), k_A(z)) not provided.
# Cannot evaluate Phi(z) → cannot compute H_MULT(z).

# If cluster variables are provided in future, function would be named:
# - attempt_table_reproduction(z_array, cluster_variables, beta_d, beta_q, H_anchor, z_anchor)
# NOT:
# - predict_Hz(z_array, ...)  (no predictions allowed)
