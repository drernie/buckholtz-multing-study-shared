"""H_MULT Algorithm Candidates Registry

Purpose: Programmatic encoding of candidate H_MULT(z) algorithms
Context: Appendix A1 Step 5 provides scaling relations but NOT explicit formula
Status: CANDIDATE_REGISTRY — none are SOURCE_CONFIRMED

CRITICAL SAFETY RULES:
1. NO candidate is SOURCE_CONFIRMED unless manuscript PDF citation provided
2. ALL candidates marked with appropriate status label
3. NO candidate allows MCMC by default
4. NO candidate allows prediction without AUTHOR_CONFIRMATION_REQUIRED
5. beta_d=4.5, beta_q=18.0 remain FITTED_PHENOMENOLOGICAL, NOT derived

"""

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum


class AlgorithmStatus(Enum):
    """Status classification for H_MULT algorithm candidates"""

    SOURCE_CONFIRMED = "source_confirmed"
    """Explicit in manuscript PDF, page number cited"""

    AI_TRANSCRIPT_REPORTED = "ai_transcript_reported"
    """From AI transcript materials, not manuscript"""

    PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY = "phenomenological_table_reproduction_only"
    """Can fit Table A1, NOT predictive on new z"""

    COMPUTATIONAL_RECONSTRUCTION_CANDIDATE = "computational_reconstruction_candidate"
    """Audit team reconstruction from first principles"""

    MVB_CANDIDATE = "mvb_candidate"
    """Discrete lattice + virial pressure route (audit hypothesis)"""

    TOY_EFFECTIVE_MODEL = "toy_effective_model"
    """Simplified physics toy model, order-of-magnitude only"""

    POST_HOC_DIAGNOSTIC_ONLY = "post_hoc_diagnostic_only"
    """Diagnostic tool, NOT forward model"""

    RESEARCH_HYPOTHESIS = "research_hypothesis"
    """Research reconstruction, awaiting author confirmation"""


class CodePermission(Enum):
    """Permission status for implementing candidate"""

    BLOCKED = "blocked"
    """Implementation blocked — missing inputs or author confirmation"""

    DIAGNOSTIC_ONLY = "diagnostic_only"
    """Can implement for diagnostic plots, NOT predictions"""

    TABLE_REPRODUCTION_ONLY = "table_reproduction_only"
    """Can reproduce Table A1 IF inputs provided, NOT new z"""

    AUTHOR_CONFIRMATION_REQUIRED = "author_confirmation_required"
    """Awaiting author confirmation before full implementation"""


@dataclass
class AlgorithmCandidate:
    """One H_MULT(z) algorithm candidate

    Attributes:
        candidate_id: Unique identifier (e.g., "phi_z_scaling")
        name: Human-readable name
        formula_latex: LaTeX formula representation
        status: AlgorithmStatus classification
        code_permission: CodePermission for implementation
        source_file: Where this candidate was found/documented
        required_inputs: List of required input variables
        dimensional_check_passes: Whether dimensional analysis passes
        can_reproduce_table_a1: Whether can reproduce Table A1
        can_predict_new_z: Whether can predict on new redshifts
        mcmc_allowed: Whether MCMC parameter estimation allowed
        degrees_of_freedom: Number of free parameters
        overfitting_risk: HIGH/MEDIUM/LOW/NONE
        notes: Additional context
        implementation: Optional Python callable
    """

    candidate_id: str
    name: str
    formula_latex: str
    status: AlgorithmStatus
    code_permission: CodePermission
    source_file: str | None
    required_inputs: list[str]
    dimensional_check_passes: bool
    can_reproduce_table_a1: str  # YES/NO/UNKNOWN
    can_predict_new_z: str  # YES/NO/PARTIAL/UNKNOWN
    mcmc_allowed: bool
    degrees_of_freedom: int
    overfitting_risk: str  # HIGH/MEDIUM/LOW/NONE
    notes: str
    implementation: Callable | None = None


# ============================================================================
# Candidate Registry
# ============================================================================

CANDIDATES = [
    # ------------------------------------------------------------------------
    # Candidate 1: Spline Interpolation
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="spline_table_fit",
        name="Spline-Fit Table-Reproduction Candidate",
        formula_latex=r"H_{\text{MULT}}(z) = \text{spline}(z_{\text{table}}, H_{\text{MULT,table}})",
        status=AlgorithmStatus.PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY,
        code_permission=CodePermission.TABLE_REPRODUCTION_ONLY,
        source_file=None,
        required_inputs=["z_table", "H_MULT_table"],
        dimensional_check_passes=True,
        can_reproduce_table_a1="YES",
        can_predict_new_z="NO",
        mcmc_allowed=False,
        degrees_of_freedom=12,  # N_rows in Table A1
        overfitting_risk="EXTREME",
        notes=(
            "Pure interpolation. Zero physical content. "
            "Can only reproduce Table A1 by construction. "
            "Extrapolation beyond table range not allowed."
        ),
    ),
    # ------------------------------------------------------------------------
    # Candidate 2: Phi(z) Phenomenological Scaling
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="phi_z_scaling",
        name="AI Transcript Phi(z) Phenomenological Scaling",
        formula_latex=(
            r"\Phi(z) = A_m(z) - A_d(z) + A_q(z), \quad "
            r"H_{\text{MULT}}^2(z) = H_{\text{anchor}}^2 \times "
            r"\frac{\Phi(z)}{\Phi(z_{\text{anchor}})}"
        ),
        status=AlgorithmStatus.AI_TRANSCRIPT_REPORTED,
        code_permission=CodePermission.BLOCKED,
        source_file="docs/35_ai_transcript_closure_candidate.md",
        required_inputs=["A_m(z)", "A_d(z)", "A_q(z)", "H_anchor", "z_anchor"],
        dimensional_check_passes=True,
        can_reproduce_table_a1="YES",  # IF A_m, A_d, A_q tables provided
        can_predict_new_z="PARTIAL",  # Requires A_m, A_d, A_q for new z
        mcmc_allowed=False,
        degrees_of_freedom=36,  # 3 tables × 12 rows
        overfitting_risk="EXTREME",
        notes=(
            "Most explicit formula found in project files. "
            "Heuristic analogy to force-law sign structure. "
            "NOT source-confirmed physical derivation. "
            "BLOCKED: A_m, A_d, A_q definitions unknown, tables missing."
        ),
    ),
    # ------------------------------------------------------------------------
    # Candidate 3: Net Force Ratio Scaling
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="force_ratio_scaling",
        name="Dimensionless Force Ratio Scaling Candidate",
        formula_latex=(
            r"\text{Net}(z) = \frac{F_{\text{oP}}}{F_m} = "
            r"1 - \frac{F_d}{F_m} + \frac{F_q}{F_m}, \quad "
            r"H_{\text{MULT}}^2(z) = H_{\text{FLRW}}^2(z) \times \text{Net}(z)"
        ),
        status=AlgorithmStatus.COMPUTATIONAL_RECONSTRUCTION_CANDIDATE,
        code_permission=CodePermission.BLOCKED,
        source_file="docs/40_hmult_algorithm_recovery_and_brainstorm.md",
        required_inputs=["m_A(z)", "r_A(z)", "k_A(z)", "D_CAB(z)", "beta_d", "beta_q"],
        dimensional_check_passes=True,
        can_reproduce_table_a1="UNKNOWN",
        can_predict_new_z="UNKNOWN",
        mcmc_allowed=False,
        degrees_of_freedom=36,  # Cluster vars × 12 rows
        overfitting_risk="EXTREME",
        notes=(
            "Physically motivated: force ratios → expansion modulation. "
            "Audit reconstruction, NOT manuscript-confirmed. "
            "BLOCKED: Cluster variable table missing. "
            "Physical mechanism H² ~ Net(z) not derived."
        ),
    ),
    # ------------------------------------------------------------------------
    # Candidate 4: Acceleration-Over-Length Scaling
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="accel_over_length",
        name="Pairwise Acceleration / Length Scale Bridge",
        formula_latex=(
            r"a_{\text{MULT}}(z) = \frac{F_{\text{oP}}(z)}{m_P}, \quad "
            r"H_{\text{MULT}}^2(z) \sim \frac{a_{\text{MULT}}(z)}{L(z)}"
        ),
        status=AlgorithmStatus.TOY_EFFECTIVE_MODEL,
        code_permission=CodePermission.BLOCKED,
        source_file="docs/40_hmult_algorithm_recovery_and_brainstorm.md",
        required_inputs=["F_oP(z)", "m_P", "L(z)"],
        dimensional_check_passes=True,
        can_reproduce_table_a1="UNKNOWN",
        can_predict_new_z="NO",
        mcmc_allowed=False,
        degrees_of_freedom=0,  # Undefined L(z) choice
        overfitting_risk="NONE",
        notes=(
            "Dimensionally correct but ambiguous. "
            "Multiple L(z) candidates (D_CAB, c/H, horizon). "
            "No rigorous derivation why H² ~ a/L. "
            "Order-of-magnitude check only."
        ),
    ),
    # ------------------------------------------------------------------------
    # Candidate 5: Virial Pressure / Effective Fluid (MVB)
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="mvb_virial_pressure",
        name="Discrete Lattice + Virial Pressure Route (MVB Candidate)",
        formula_latex=(
            r"P_{\text{virial}}(z) = -\frac{\langle \vec{r} \cdot \vec{F}_{\text{oP}} \rangle}{3 V_{\text{cell}}(z)}, \quad "
            r"\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}\left(\rho_{\text{eff}} + \frac{3 P_{\text{eff}}}{c^2}\right)"
        ),
        status=AlgorithmStatus.MVB_CANDIDATE,
        code_permission=CodePermission.AUTHOR_CONFIRMATION_REQUIRED,
        source_file="docs/37_discrete_lattice_mvb_hypothesis.md",
        required_inputs=[
            "F_oP(r,z)",
            "V_cell(z)",
            "lattice_geometry",
            "rho_eff(z)",
            "initial_conditions",
        ],
        dimensional_check_passes=True,
        can_reproduce_table_a1="UNKNOWN",
        can_predict_new_z="UNKNOWN",
        mcmc_allowed=False,
        degrees_of_freedom=5,  # Lattice params + ICs
        overfitting_risk="LOW",
        notes=(
            "Most physically rigorous candidate. "
            "Uses standard statistical mechanics (virial theorem). "
            "Audit reconstruction — NOT Buckholtz's stated approach. "
            "Requires ODE solver + lattice geometry specification."
        ),
    ),
    # ------------------------------------------------------------------------
    # Candidate 6: Discrete Lattice Neighbor Dynamics
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="discrete_ode",
        name="Nearest-Neighbor Cluster ODE Route",
        formula_latex=(
            r"D_{\text{CAB}}(t) = a(t) \times D_0, \quad "
            r"\ddot{D}_{\text{CAB}} = \frac{F_{\text{oP}}}{\mu}, \quad "
            r"\frac{\ddot{a}}{a} = \frac{\ddot{D}_{\text{CAB}}}{D_{\text{CAB}}}"
        ),
        status=AlgorithmStatus.MVB_CANDIDATE,
        code_permission=CodePermission.AUTHOR_CONFIRMATION_REQUIRED,
        source_file="docs/37_discrete_lattice_mvb_hypothesis.md",
        required_inputs=["F_oP(D_CAB, z)", "mu", "D0", "a(t0)", "a_dot(t0)"],
        dimensional_check_passes=True,
        can_reproduce_table_a1="UNKNOWN",
        can_predict_new_z="UNKNOWN",
        mcmc_allowed=False,
        degrees_of_freedom=3,  # ICs + D0
        overfitting_risk="LOW",
        notes=(
            "Simplest discrete dynamics candidate. "
            "Analytically tractable in principle. "
            "Risk: ä/a = D̈/D assumes all clusters have same dynamics. "
            "Needs careful re-derivation to avoid circular logic. "
            "ODE D-closure priority: KILLED_EARLY (2026-06-06) — see k_a_independent_closure."
        ),
    ),
    # ------------------------------------------------------------------------
    # Candidate 7: Effective w(z) Reconstruction (Post-Hoc)
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="w_eff_diagnostic",
        name="Equation-of-State Reconstruction from H_MULT",
        formula_latex=(
            r"w_{\text{eff}}(z) = -1 - \frac{2}{3} \times \frac{1}{1+z} \times "
            r"\frac{d \ln H_{\text{MULT}}}{dz}"
        ),
        status=AlgorithmStatus.POST_HOC_DIAGNOSTIC_ONLY,
        code_permission=CodePermission.DIAGNOSTIC_ONLY,
        source_file="docs/40_hmult_algorithm_recovery_and_brainstorm.md",
        required_inputs=["z", "H_MULT(z)"],
        dimensional_check_passes=True,
        can_reproduce_table_a1="N/A",  # Uses Table A1 as input
        can_predict_new_z="NO",
        mcmc_allowed=False,
        degrees_of_freedom=0,  # Post-hoc diagnostic
        overfitting_risk="NONE",
        notes=(
            "Diagnostic tool only — NOT forward model. "
            "Requires H_MULT(z) as input. "
            "Useful for checking if w_eff correlates with "
            "monopole/dipole/quadrupole dominance."
        ),
    ),
    # ------------------------------------------------------------------------
    # Candidate 8: ΛCDM + Phenomenological Correction
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="lcdm_plus_polynomial",
        name="ΛCDM + Polynomial Correction",
        formula_latex=(
            r"H_{\text{MULT}}(z) = H_{\text{FLRW}}(z) \times " r"[1 + c_1 z + c_2 z^2 + c_3 z^3]"
        ),
        status=AlgorithmStatus.PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY,
        code_permission=CodePermission.DIAGNOSTIC_ONLY,
        source_file="docs/40_hmult_algorithm_recovery_and_brainstorm.md",
        required_inputs=["H_FLRW(z)", "c1", "c2", "c3"],
        dimensional_check_passes=True,
        can_reproduce_table_a1="YES",
        can_predict_new_z="PARTIAL",  # Extrapolation only
        mcmc_allowed=False,
        degrees_of_freedom=3,  # c1, c2, c3
        overfitting_risk="LOW",
        notes=(
            "Simplest smooth interpolation with few parameters. "
            "Zero physical content. "
            "Useful for testing if MULTING ~ ΛCDM + small correction. "
            "AIC/BIC penalty: 3 extra parameters vs ΛCDM (2 parameters)."
        ),
    ),
    # ------------------------------------------------------------------------
    # Candidate 9: k_A Independent Closure
    # ------------------------------------------------------------------------
    AlgorithmCandidate(
        candidate_id="k_a_independent_closure",
        name="k_A Independent Closure (Press-Schechter + Virial)",
        formula_latex=(
            r"k_A(z) = \alpha \cdot \frac{3}{2} M_{\mathrm{halo}} \sigma_v^2 / c^2, "
            r"\quad D(z) = D_0 (1+z)^{-\gamma_{\mathrm{req}}}"
        ),
        status=AlgorithmStatus.COMPUTATIONAL_RECONSTRUCTION_CANDIDATE,
        code_permission=CodePermission.DIAGNOSTIC_ONLY,
        source_file="src/k_a_closure_test.py",
        required_inputs=["m_A(z)", "r_A(z)", "D(z)", "beta_d", "beta_q", "alpha@z=0"],
        dimensional_check_passes=True,
        can_reproduce_table_a1="PARTIAL",
        can_predict_new_z="NO",
        mcmc_allowed=False,
        degrees_of_freedom=0,
        overfitting_risk="NONE",
        notes=(
            "k_A closure test: independent k_A(z) vs CSV-inferred at fixed beta=4.5/18.0. "
            "Double-inversion diagnostic (isolines + gamma/alpha grid) in "
            "src/double_inversion_isoline.py, src/double_inversion_grid.py. "
            "NOT_VALIDATION — beta fitted to H_obs. "
            "ODE D-closure route (d_closure_ode): KILLED_EARLY — gamma_req is fit not force-derived. "
            "See docs/99_k_a_closure_report.md, docs/DOUBLE_INVERSION_DIAGNOSTIC.md."
        ),
    ),
]


# ============================================================================
# Registry Access Functions
# ============================================================================


def get_all_candidates() -> list[AlgorithmCandidate]:
    """Return all H_MULT algorithm candidates"""
    return CANDIDATES


def get_candidate_by_id(candidate_id: str) -> AlgorithmCandidate | None:
    """Get candidate by ID, return None if not found"""
    for candidate in CANDIDATES:
        if candidate.candidate_id == candidate_id:
            return candidate
    return None


def get_candidates_by_status(status: AlgorithmStatus) -> list[AlgorithmCandidate]:
    """Get all candidates with given status"""
    return [c for c in CANDIDATES if c.status == status]


def get_source_confirmed_candidates() -> list[AlgorithmCandidate]:
    """Get only SOURCE_CONFIRMED candidates (should be empty unless manuscript cited)"""
    return get_candidates_by_status(AlgorithmStatus.SOURCE_CONFIRMED)


def get_implementable_candidates() -> list[AlgorithmCandidate]:
    """Get candidates with non-BLOCKED code permission"""
    return [c for c in CANDIDATES if c.code_permission != CodePermission.BLOCKED]


def count_candidates_by_status() -> dict:
    """Count candidates by status"""
    from collections import Counter

    return dict(Counter(c.status for c in CANDIDATES))


# ============================================================================
# Validation Functions
# ============================================================================


def validate_registry() -> list[str]:
    """Validate registry integrity, return list of issues"""
    issues = []

    # Check 1: No SOURCE_CONFIRMED without explicit source
    source_confirmed = get_source_confirmed_candidates()
    if source_confirmed:
        for c in source_confirmed:
            if not c.source_file or "preprints202511.0598" not in c.source_file:
                issues.append(
                    f"Candidate {c.candidate_id} marked SOURCE_CONFIRMED "
                    f"but no manuscript PDF citation provided"
                )

    # Check 2: MCMC allowed only if SOURCE_CONFIRMED
    for c in CANDIDATES:
        if c.mcmc_allowed and c.status != AlgorithmStatus.SOURCE_CONFIRMED:
            issues.append(
                f"Candidate {c.candidate_id} allows MCMC but status is "
                f"{c.status.value}, not SOURCE_CONFIRMED"
            )

    # Check 3: High DoF candidates marked as HIGH overfitting risk
    for c in CANDIDATES:
        if c.degrees_of_freedom > 6 and c.overfitting_risk != "EXTREME":
            issues.append(
                f"Candidate {c.candidate_id} has DoF={c.degrees_of_freedom} "
                f"but overfitting_risk is {c.overfitting_risk}, should be EXTREME"
            )

    # Check 4: All candidates have unique IDs
    ids = [c.candidate_id for c in CANDIDATES]
    if len(ids) != len(set(ids)):
        issues.append("Duplicate candidate IDs found")

    # Check 5: Dimensional check passes for all
    failed_dim_check = [c for c in CANDIDATES if not c.dimensional_check_passes]
    if failed_dim_check:
        issues.append(
            f"{len(failed_dim_check)} candidates fail dimensional check: "
            f"{[c.candidate_id for c in failed_dim_check]}"
        )

    return issues


# ============================================================================
# Report Generation
# ============================================================================


def generate_candidate_summary() -> str:
    """Generate markdown summary of all candidates"""
    lines = ["# H_MULT Algorithm Candidates Summary\n"]
    lines.append(f"**Total candidates:** {len(CANDIDATES)}\n")

    # Count by status
    status_counts = count_candidates_by_status()
    lines.append("## Status Distribution\n")
    for status, count in status_counts.items():
        lines.append(f"- {status.value}: {count}")
    lines.append("")

    # List candidates
    lines.append("## Candidate List\n")
    for i, c in enumerate(CANDIDATES, 1):
        lines.append(f"### {i}. {c.name}\n")
        lines.append(f"- **ID:** `{c.candidate_id}`")
        lines.append(f"- **Status:** {c.status.value}")
        lines.append(f"- **Code Permission:** {c.code_permission.value}")
        lines.append(f"- **Can Reproduce Table A1:** {c.can_reproduce_table_a1}")
        lines.append(f"- **Can Predict New z:** {c.can_predict_new_z}")
        lines.append(f"- **MCMC Allowed:** {c.mcmc_allowed}")
        lines.append(f"- **DoF:** {c.degrees_of_freedom}")
        lines.append(f"- **Overfitting Risk:** {c.overfitting_risk}")
        lines.append("")

    # Validation results
    issues = validate_registry()
    if issues:
        lines.append("## ⚠️ Registry Issues\n")
        for issue in issues:
            lines.append(f"- {issue}")
    else:
        lines.append("## ✅ Registry Validation Passed\n")

    return "\n".join(lines)


# ============================================================================
# Module-level validation on import
# ============================================================================

_VALIDATION_ISSUES = validate_registry()
if _VALIDATION_ISSUES:
    import warnings

    warnings.warn(
        f"H_MULT candidate registry has {len(_VALIDATION_ISSUES)} issues:\n"
        + "\n".join(f"  - {issue}" for issue in _VALIDATION_ISSUES),
        stacklevel=2,
    )
