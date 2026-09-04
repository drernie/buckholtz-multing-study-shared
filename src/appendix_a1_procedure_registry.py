"""
Appendix A1 Procedure Registry — Programmatic Encoding of Steps 3–7

SOURCE: preprints202511.0598.v6.pdf, Appendix A.1, pages 31–38
DATE: 2026-05-29

This module encodes the procedural structure of Appendix A1 WITHOUT implementing H(z).
Purpose: Verification that no predictive H_MULT function exists in source material.
"""

from dataclasses import dataclass
from enum import Enum


class VariableProvenance(Enum):
    """Source of variable value."""

    DATA = "data"  # Observational data
    DERIVED = "derived"  # Calculated from data (e.g., z from Time)
    AI_ESTIMATED = "ai_estimated"  # AI service discretion
    FITTED_PHENOMENOLOGICAL = "fitted_phenomenological"  # β_d, β_q
    TABLE_REPORTED = "table_reported"  # Table A1 empirical values
    FORMULA_PROVIDED = "formula_provided"  # Explicit equation in source
    UNDER_SPECIFIED = "under_specified"  # Procedural only, no formula


class CodePermission(Enum):
    """What can be done with this variable in code."""

    CODE_READY = "code_ready"  # Can implement
    NOT_CODE_READY = "not_code_ready"  # Cannot implement (missing formula/data)
    ALLOWED_FOR_TABLE_REPRODUCTION_ONLY = "allowed_for_table_reproduction_only"
    BLOCKED = "blocked"  # Explicitly cannot implement


@dataclass
class Variable:
    """A variable in Appendix A1 procedure."""

    symbol: str
    meaning: str
    provenance: VariableProvenance
    code_permission: CodePermission
    notes: str
    step_introduced: int


@dataclass
class ProcedureStep:
    """A step in Appendix A1 procedure."""

    step_number: int
    title: str
    author_instruction: str  # Verbatim from source
    inputs: list[str]
    outputs: list[str]
    ai_discretion_allowed: bool
    code_ready: bool
    notes: str
    status: str  # SOURCE_CONFIRMED, UNDER_SPECIFIED, etc.


# ============================================================================
# Variable Provenance Table
# ============================================================================

VARIABLES = [
    Variable(
        symbol="Time",
        meaning="Time in billions of years after Big Bang",
        provenance=VariableProvenance.DATA,
        code_permission=CodePermission.CODE_READY,
        notes="Member of Set of Times (Step 3)",
        step_introduced=3,
    ),
    Variable(
        symbol="z",
        meaning="Redshift",
        provenance=VariableProvenance.DERIVED,
        code_permission=CodePermission.CODE_READY,
        notes="Derived from Time via cosmological relation",
        step_introduced=4,
    ),
    Variable(
        symbol="H-data",
        meaning="Observed H(z) with uncertainty",
        provenance=VariableProvenance.DATA,
        code_permission=CodePermission.CODE_READY,
        notes="From observations, NOT from FLRW models",
        step_introduced=4,
    ),
    Variable(
        symbol="m_A",
        meaning="Range of masses for object-A (galaxy cluster)",
        provenance=VariableProvenance.AI_ESTIMATED,
        code_permission=CodePermission.NOT_CODE_READY,
        notes="AI service 'chose or estimated' — no data source provided",
        step_introduced=4,
    ),
    Variable(
        symbol="r_A",
        meaning="Range of radii for object-A",
        provenance=VariableProvenance.AI_ESTIMATED,
        code_permission=CodePermission.NOT_CODE_READY,
        notes="AI service 'chose or estimated' — no data source provided",
        step_introduced=4,
    ),
    Variable(
        symbol="D_C:AB",
        meaning="Distances between centers of neighboring objects",
        provenance=VariableProvenance.AI_ESTIMATED,
        code_permission=CodePermission.NOT_CODE_READY,
        notes="AI service 'chose or estimated' — no data source provided",
        step_introduced=4,
    ),
    Variable(
        symbol="k_A/c²",
        meaning="Total kinetic energies of sub-objects (solar masses)",
        provenance=VariableProvenance.AI_ESTIMATED,
        code_permission=CodePermission.NOT_CODE_READY,
        notes="AI service 'chose or estimated' — no data source provided",
        step_introduced=4,
    ),
    Variable(
        symbol="β_d",
        meaning="Dipole scaling parameter",
        provenance=VariableProvenance.FITTED_PHENOMENOLOGICAL,
        code_permission=CodePermission.ALLOWED_FOR_TABLE_REPRODUCTION_ONLY,
        notes="Step 5: 'minimize standard-deviations away from observed H(z)'. Table A1: β_d = 4.5",
        step_introduced=5,
    ),
    Variable(
        symbol="β_q",
        meaning="Quadrupole scaling parameter",
        provenance=VariableProvenance.FITTED_PHENOMENOLOGICAL,
        code_permission=CodePermission.ALLOWED_FOR_TABLE_REPRODUCTION_ONLY,
        notes="Step 5: 'minimize standard-deviations away from observed H(z)'. Table A1: β_q = 18.0",
        step_introduced=5,
    ),
    Variable(
        symbol="H-MULT",
        meaning="Rate of expansion calculated by MULTING",
        provenance=VariableProvenance.UNDER_SPECIFIED,
        code_permission=CodePermission.BLOCKED,
        notes="Step 5: procedural instruction only, NO computational formula F_oP → H_MULT(z)",
        step_introduced=5,
    ),
    Variable(
        symbol="H-FLRW",
        meaning="Rate of expansion calculated by Lambda-CDM",
        provenance=VariableProvenance.FORMULA_PROVIDED,
        code_permission=CodePermission.CODE_READY,
        notes="Standard FLRW metric (comparison only)",
        step_introduced=5,
    ),
    Variable(
        symbol="σ_FLRW",
        meaning="Standard deviations of H-FLRW from H-data",
        provenance=VariableProvenance.DERIVED,
        code_permission=CodePermission.CODE_READY,
        notes="σ_FLRW = (H-FLRW - H-data) / σ_H-data",
        step_introduced=5,
    ),
    Variable(
        symbol="σ_MULT",
        meaning="Standard deviations of H-MULT from H-data",
        provenance=VariableProvenance.TABLE_REPORTED,
        code_permission=CodePermission.ALLOWED_FOR_TABLE_REPRODUCTION_ONLY,
        notes="Table A1 values only, NOT predictive (no H_MULT formula)",
        step_introduced=5,
    ),
    Variable(
        symbol="w_eff",
        meaning="Effective equation of state parameter",
        provenance=VariableProvenance.AI_ESTIMATED,
        code_permission=CodePermission.CODE_READY,
        notes="Step 7: fitted to H-data using FLRW (comparison)",
        step_introduced=7,
    ),
    Variable(
        symbol="H-w_eff",
        meaning="Rate calculated by FLRW with w_eff(z)",
        provenance=VariableProvenance.DERIVED,
        code_permission=CodePermission.CODE_READY,
        notes="Derived from w_eff via FLRW metric",
        step_introduced=7,
    ),
    Variable(
        symbol="σ_w_eff",
        meaning="Standard deviations of H-w_eff from H-data",
        provenance=VariableProvenance.DERIVED,
        code_permission=CodePermission.CODE_READY,
        notes="σ_w_eff = (H-w_eff - H-data) / σ_H-data",
        step_introduced=7,
    ),
]


# ============================================================================
# Procedure Steps
# ============================================================================

STEPS = [
    ProcedureStep(
        step_number=3,
        title="Time Range",
        author_instruction=(
            "Define a so-called 'Set of Times' as follows. "
            "Anticipate that 'Good Data' should not include information that relies on theoretical models. "
            "Let t_ROE,min denote the earliest time, in billions of years after the Big Bang, for which there is Good Data. "
            "Define a so-called 'Set of Times', which is set of times, in billions of years after the Big Bang, "
            "that has as members the number 13.5 and each integer that is less than or equal to 13 and greater than "
            "or equal to both t_ROE,min and 1."
        ),
        inputs=[],
        outputs=["t_ROE,min", "Set of Times"],
        ai_discretion_allowed=True,
        code_ready=True,
        notes="t_ROE,min is AUTHOR_PROMPT_INSTRUCTION — AI service must choose based on 'Good Data' constraint.",
        status="SOURCE_CONFIRMED",
    ),
    ProcedureStep(
        step_number=4,
        title="Galaxy Cluster Parameters",
        author_instruction=(
            "Provide a table, named 'Galaxy Cluster Parameters', for which there is one row for each member "
            "of the Set of Times and you ordered the rows so that times are in descending order and the columns "
            "provide the following data about galaxy clusters or protoclusters: "
            "Time, z, m_A, r_A, D_C:AB, k_A/c², H-data. "
            "Explain how you found, chose, or estimated the values in the table."
        ),
        inputs=["Set of Times"],
        outputs=["Time", "z", "m_A", "r_A", "D_C:AB", "k_A/c²", "H-data"],
        ai_discretion_allowed=True,
        code_ready=False,
        notes=(
            "m_A, r_A, D_C:AB, k_A are AI_ESTIMATED — no data sources provided. "
            "H-data is DATA but specific sources not cited in Appendix A1."
        ),
        status="AUTHOR_PROMPT_INSTRUCTION",
    ),
    ProcedureStep(
        step_number=5,
        title="Approximate Matches to Rate of Expansion Data",
        author_instruction=(
            "How well can you fit (by using my monopole, dipole, and quadrupole components of gravity) "
            "the data (in the Galaxy Cluster Parameters table) about the observed rate of expansion of the universe? "
            "In doing this work, use the formulas r_dA = β_d r_A, r_dP = β_d r_P, and |r_qAB|² = (β_q)² r_A r_P. "
            "Try to choose positive values for β_d and β_q that minimize the standard-deviations away from "
            "the nominal values of observed H(z). "
            "Provide a table, named 'Approximate Matches to Rate of Expansion Data', with columns: "
            "Time, z, H-data, H-FLRW, σ_FLRW, H-MULT, σ_MULT. "
            "Try to avoid using outputs from uses of the FLRW metric or other Lambda-CDM models."
        ),
        inputs=["Galaxy Cluster Parameters", "F_m", "F_d", "F_q", "F_oP"],
        outputs=["β_d", "β_q", "H-MULT", "σ_MULT"],
        ai_discretion_allowed=True,
        code_ready=False,
        notes=(
            "CRITICAL: β_d, β_q are FITTED to minimize σ from H-data. "
            "H_MULT formula is NOT provided — only procedural instruction 'fit by using monopole, dipole, quadrupole'. "
            "Table A1 reports β_d = 4.5, β_q = 18.0 (AI service output)."
        ),
        status="UNDER_SPECIFIED — bridge formula F_oP → H_MULT missing",
    ),
    ProcedureStep(
        step_number=6,
        title="Projections About the Future",
        author_instruction=(
            "Does the rate of expansion calculated by use of my monopole, dipole, and quadrupole components of gravity "
            "and your values for β_d and β_q project a future time at which the sum of monopole gravity plus quadrupole "
            "gravity would start to be larger than dipole gravity? If so, estimate and report a time range. "
            "Try to calculate (without using outputs from uses of the FLRW metric or other Lambda-CDM models) "
            "and report (for that time) an analog to H(z)."
        ),
        inputs=["β_d", "β_q", "H-MULT(z)"],
        outputs=["t_crossover", "H(t_crossover)"],
        ai_discretion_allowed=True,
        code_ready=False,
        notes="BLOCKED by Step 5 — H_MULT(z) formula missing, cannot compute future projection.",
        status="BLOCKED",
    ),
    ProcedureStep(
        step_number=7,
        title="A Possible Equation of State for Use with the FLRW Metric",
        author_instruction=(
            "I request that you try to suggest an equation of state for which use of the FLRW metric would be "
            "more accurate (regarding H-data data) than present Lambda-CDM uses. "
            "Compute a sample w_eff(z) curve from the H-data values (of H(z)) that you already used. "
            "Use FLRW techniques, but with an equation of state that features an adjustable (based on time) parameter w. "
            "Provide a table, named 'Comparison of matches to data, including via w_eff(z)', with columns: "
            "Time, z, H-data, H-FLRW, σ_FLRW, H-MULT, σ_MULT, w_eff, H-w_eff, σ_w_eff."
        ),
        inputs=["H-data", "H-FLRW", "H-MULT (from Step 5 table)"],
        outputs=["w_eff", "H-w_eff", "σ_w_eff"],
        ai_discretion_allowed=True,
        code_ready=True,
        notes=(
            "w_eff is AI_ESTIMATED (fitted to H-data using FLRW). "
            "PURPOSE: comparison to show MULTING vs improved-FLRW, NOT validation of MULTING. "
            "H-MULT values are copied from Step 5 table (NOT recalculated)."
        ),
        status="SOURCE_CONFIRMED — comparison only, no predictive MULTING claim",
    ),
]


# ============================================================================
# Table A1 Data
# ============================================================================


@dataclass
class TableA1Row:
    """One row of Table A1."""

    time: float  # Gyr after Big Bang
    z: float
    h_data: float  # km/s/Mpc
    sigma_h_data: float
    h_flrw: float
    sigma_flrw: float  # standard deviations from H-data
    # WHY optional: the z=0 anchor row genuinely reports no MULTING value
    # (see TABLE_A1 row 1 below) -- real source data, not a missing-value bug.
    h_mult: float | None
    sigma_mult: float | None
    w_eff: float
    h_w_eff: float
    sigma_w_eff: float


TABLE_A1 = [
    TableA1Row(13.5, 0, 73.0, 7.0, 67.4, -5.6, None, None, 1.30, 73, 0),
    TableA1Row(13, 0.06, 69.0, 3.0, 68.1, -0.3, 70.2, 0.4, -1.25, 69.3, 0.1),
    TableA1Row(12, 0.14, 74.0, 4.0, 69.3, -1.2, 73.5, -0.1, -1.20, 74.1, 0.03),
    TableA1Row(11, 0.25, 79.0, 4.5, 71.5, -1.7, 78.8, -0.04, -1.15, 79.2, 0.04),
    TableA1Row(10, 0.4, 82.0, 5.0, 75, -1.4, 83.1, 0.2, -1.10, 82.3, 0.1),
    TableA1Row(9, 0.65, 92.0, 7.0, 83, -1.3, 91.4, -0.1, -1.05, 92.4, 0.1),
    TableA1Row(8, 1, 105.0, 8.0, 95.7, -1.2, 104.2, -0.1, -1.01, 105.3, 0.04),
    TableA1Row(7, 1.5, 125.0, 15.0, 114.8, -0.7, 126.5, 0.1, -0.98, 125.6, 0.04),
    TableA1Row(6, 2.1, 150.0, 20.0, 140.3, -0.5, 151.8, 0.1, -0.96, 150.5, 0.03),
    TableA1Row(5, 3.2, 195.0, 30.0, 187.6, -0.2, 197.3, 0.1, -0.95, 195.2, 0.01),
    TableA1Row(4, 5, 270.0, 50.0, 265.2, -0.1, 271.5, 0.03, -0.97, 270.2, 0.004),
    TableA1Row(3, 8.5, 420.0, 90.0, 398.5, -0.2, 418.1, -0.02, -1.00, 420.1, 0.001),
]

# β_d and β_q reported by AI service
BETA_D_TABLE_A1 = 4.5
BETA_Q_TABLE_A1 = 18.0


# ============================================================================
# Bridge Status
# ============================================================================


@dataclass
class BridgeFinding:
    """Status of F_oP → H_MULT bridge."""

    question: str
    answer: str
    evidence: list[str]
    status: str


BRIDGE_FINDING = BridgeFinding(
    question="Does Appendix A1 explicitly define the bridge F_oP → H_MULT(z)?",
    answer="NO, formula missing",
    evidence=[
        "Force formulas provided: F_m, F_d, F_q, F_oP (Step 2)",
        "Scaling relations provided: r_dA = β_d × r_A, r_dP = β_d × r_P, |r_qAB|² = β_q² × r_A × r_P (Step 5)",
        "NO formula H_MULT = f(z, β_d, β_q, m_A, r_A, k_A, ...) provided",
        "Procedural instruction: 'How well can you fit (by using my monopole, dipole, and quadrupole components of gravity) the data...'",
        "AI discretion allowed: 'Feel free to use any or all the information in the Galaxy Cluster Parameters table.'",
    ],
    status="PARTIAL — procedural/heuristic bridge only, NOT computational formula",
)


# ============================================================================
# What Can Be Reproduced
# ============================================================================

ALLOWED_OPERATIONS = [
    "Table structure (Steps 3–7)",
    "Force formulas: F_m, F_d, F_q, F_oP",
    "Scaling relations: r_dA, r_dP, r_qAB",
    "β_d = 4.5, β_q = 18.0 as TABLE_REPORTED values (NOT predictive)",
    "Table A1 data as empirical table for comparison",
]

BLOCKED_OPERATIONS = [
    "H_MULT(z) computation — formula missing",
    "β_d, β_q fitting — objective function and method under-specified",
    "Future projections — requires H_MULT(z) formula",
    "MCMC parameter estimation — requires H_MULT(z) likelihood function",
    "Validation or falsification of MULTING — blocked by missing H_MULT(z)",
]


# ============================================================================
# Getters
# ============================================================================


def get_variable(symbol: str) -> Variable | None:
    """Get variable by symbol."""
    for var in VARIABLES:
        if var.symbol == symbol:
            return var
    return None


def get_step(step_number: int) -> ProcedureStep | None:
    """Get procedure step by number."""
    for step in STEPS:
        if step.step_number == step_number:
            return step
    return None


def get_beta_d_table_a1() -> float:
    """Get β_d value from Table A1."""
    return BETA_D_TABLE_A1


def get_beta_q_table_a1() -> float:
    """Get β_q value from Table A1."""
    return BETA_Q_TABLE_A1


def get_table_a1_data() -> list[TableA1Row]:
    """Get Table A1 empirical data."""
    return TABLE_A1


def get_bridge_finding() -> BridgeFinding:
    """Get F_oP → H_MULT bridge status."""
    return BRIDGE_FINDING


def is_operation_allowed(operation: str) -> bool:
    """Check if operation is allowed."""
    return operation in ALLOWED_OPERATIONS


def is_operation_blocked(operation: str) -> bool:
    """Check if operation is blocked."""
    return operation in BLOCKED_OPERATIONS
