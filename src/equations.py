"""
Equation records for IDM/MULTING.

This module contains RECORDS, not solvers.
Do not implement physics that is not clearly defined.
"""

from .epistemic_registry import EquationRecord, SourceRef

# Placeholder source for equations requiring verification
SOURCE_NEEDS_VERIFICATION = SourceRef(
    id="buckholtz_unverified",
    title="Buckholtz work (equation source requires verification)",
    location="TBD",
    note="Equation mentioned but full source not yet confirmed",
)


# Eq.15: The tau-electron mass ratio relation
EQ_15_CONSTANT_RELATION = EquationRecord(
    id="eq_15",
    label="Eq.15",
    expression_text=("(4/3) * (m_tau^2 / m_e^2)^6 ≈ k_e * e^2 / (G * m_e^2)"),
    symbols=["m_tau", "m_e", "k_e", "e", "G"],
    status="calculation",
    source=SourceRef(
        id="buckholtz_eq15",
        title="Buckholtz Eq.15 relation",
        location="Communications (to be verified in formal publication)",
        note="Numerical relation reproduced but physical mechanism unclear",
    ),
    dimensional_status="requires_clarification",
    notes=(
        "This equation can be reproduced numerically to ~1% precision. "
        "However: (1) Physical mechanism for exponent 6 is unclear. "
        "(2) Physical mechanism for prefactor 4/3 is unclear. "
        "(3) Dimensional analysis requires careful unit tracking. "
        "Status marked as 'calculation' because numerical reproduction succeeds, "
        "but underlying physics is not established."
    ),
)


# IDM: Six isomers claim
IDM_SIX_ISOMERS = EquationRecord(
    id="idm_six_isomers",
    label="IDM six-isomer structure",
    expression_text="N_isomers = 6 (5 dark + 1 ordinary matter)",
    symbols=["N_isomers"],
    status="hypothesis",
    source=SOURCE_NEEDS_VERIFICATION,
    dimensional_status="not_checked",
    notes=(
        "Claim: dark matter consists of 6 isomeric sectors. "
        "Requires verification of: (1) How isomers are defined. "
        "(2) What distinguishes them. (3) Observational implications."
    ),
)


# MULTING: Monopole term
MULTING_MONOPOLE = EquationRecord(
    id="multing_monopole",
    label="MULTING monopole term",
    expression_text="H(z) monopole component (exact form TBD)",
    symbols=["H", "z"],
    status="requires_source_verification",
    source=SOURCE_NEEDS_VERIFICATION,
    dimensional_status="not_checked",
    notes=(
        "MULTING includes a monopole modification to H(z). "
        "Full functional form requires source clarification."
    ),
)


# MULTING: Dipole term
MULTING_DIPOLE = EquationRecord(
    id="multing_dipole",
    label="MULTING dipole term",
    expression_text="H(z) dipole repulsion ~ beta_d (exact form TBD)",
    symbols=["H", "z", "beta_d"],
    status="requires_source_verification",
    source=SOURCE_NEEDS_VERIFICATION,
    dimensional_status="not_checked",
    notes=(
        "MULTING includes a dipole repulsion term scaled by beta_d. "
        "Full functional form, dimensional analysis, and beta_d definition "
        "require source clarification. "
        "Possible PPN/Solar System constraint implications require checking."
    ),
)


# MULTING: Quadrupole term
MULTING_QUADRUPOLE = EquationRecord(
    id="multing_quadrupole",
    label="MULTING quadrupole term",
    expression_text="H(z) quadrupole attraction ~ beta_q (exact form TBD)",
    symbols=["H", "z", "beta_q"],
    status="requires_source_verification",
    source=SOURCE_NEEDS_VERIFICATION,
    dimensional_status="not_checked",
    notes=(
        "MULTING includes a quadrupole attraction term scaled by beta_q. "
        "Full functional form, dimensional analysis, and beta_q definition "
        "require source clarification. "
        "Possible PPN/Solar System constraint implications require checking."
    ),
)


# Beta_d scale relation
BETA_D_SCALE_RELATION = EquationRecord(
    id="beta_d_scale",
    label="beta_d scale definition",
    expression_text="r_dA = beta_d * r_A (possible relation, TBD)",
    symbols=["r_dA", "beta_d", "r_A"],
    status="requires_source_verification",
    source=SOURCE_NEEDS_VERIFICATION,
    dimensional_status="not_checked",
    notes=(
        "Possible definition: beta_d relates dipole scale r_dA to some "
        "characteristic scale r_A. "
        "Requires clarification of: (1) What is r_A? "
        "(2) What is r_dA physically? (3) Dimensional consistency."
    ),
)


# Beta_q scale relation
BETA_Q_SCALE_RELATION = EquationRecord(
    id="beta_q_scale",
    label="beta_q scale definition",
    expression_text="L_q^2 = beta_q * L_ref^2 (possible relation, TBD)",
    symbols=["L_q", "beta_q", "L_ref"],
    status="requires_source_verification",
    source=SOURCE_NEEDS_VERIFICATION,
    dimensional_status="not_checked",
    notes=(
        "Possible definition: beta_q relates quadrupole scale L_q to some "
        "reference length L_ref. "
        "Requires clarification of: (1) What is L_ref? "
        "(2) What is L_q physically? (3) Dimensional consistency."
    ),
)


def get_all_equations() -> list[EquationRecord]:
    """
    Return all equation records.

    Returns:
        List of all registered equations.
    """
    return [
        EQ_15_CONSTANT_RELATION,
        IDM_SIX_ISOMERS,
        MULTING_MONOPOLE,
        MULTING_DIPOLE,
        MULTING_QUADRUPOLE,
        BETA_D_SCALE_RELATION,
        BETA_Q_SCALE_RELATION,
    ]


def get_verified_equations() -> list[EquationRecord]:
    """
    Return only equations with verified sources.

    Returns:
        Equations with status other than 'requires_source_verification'.
    """
    return [eq for eq in get_all_equations() if eq.status != "requires_source_verification"]


def get_unverified_equations() -> list[EquationRecord]:
    """
    Return equations requiring source verification.

    Returns:
        Equations with status 'requires_source_verification'.
    """
    return [eq for eq in get_all_equations() if eq.status == "requires_source_verification"]
