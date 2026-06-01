"""Tests for Bridge Candidate Mathematical Audit

Safety enforcement:
- All candidates NOT_SOURCE_CONFIRMED
- MCMC blocked
- Prediction blocked
- Row 1 marked as outlier
"""

from src.bridge_candidate_math_audit import (
    BRIDGE_CANDIDATES,
    CANDIDATE_B,
    CANDIDATE_PHI,
    BridgeStatus,
    get_author_question_bridge_method,
    get_best_internal_candidate,
    get_row_1_status,
    is_mcmc_allowed,
    is_prediction_allowed,
    validate_registry,
)


def test_candidate_b_exists():
    """Candidate B (Discrete Lattice) exists"""
    assert "discrete_lattice_ode" in BRIDGE_CANDIDATES
    assert CANDIDATE_B.candidate_id == "discrete_lattice_ode"


def test_candidate_phi_exists():
    """Phi heuristic exists"""
    assert "phi_z_heuristic" in BRIDGE_CANDIDATES
    assert CANDIDATE_PHI.candidate_id == "phi_z_heuristic"


def test_candidate_b_dimensional_check_passes():
    """Candidate B passes dimensional check"""
    assert CANDIDATE_B.dimensional_check.passes is True
    assert "[T⁻²]" in CANDIDATE_B.dimensional_check.lhs_units
    assert "[T⁻²]" in CANDIDATE_B.dimensional_check.rhs_units


def test_candidate_b_sign_verified():
    """Candidate B sign convention verified"""
    assert CANDIDATE_B.sign_convention_verified is True


def test_candidate_b_has_required_inputs():
    """Candidate B lists all required inputs"""
    input_symbols = [inp.symbol for inp in CANDIDATE_B.required_inputs]
    assert "m_A(z)" in input_symbols
    assert "k_A(z)" in input_symbols
    assert "r_A(z)" in input_symbols
    assert "D_AB(z)" in input_symbols
    assert "N_eff" in input_symbols


def test_candidate_b_missing_inputs():
    """Candidate B has MISSING status for critical inputs"""
    missing = [inp for inp in CANDIDATE_B.required_inputs if inp.status == "MISSING"]
    assert len(missing) >= 6, "Expected ≥6 missing inputs"
    missing_symbols = [inp.symbol for inp in missing]
    assert "m_A(z)" in missing_symbols
    assert "D_AB(z)" in missing_symbols


def test_candidate_b_not_source_confirmed():
    """Candidate B is NOT_SOURCE_CONFIRMED"""
    assert BridgeStatus.NOT_SOURCE_CONFIRMED in CANDIDATE_B.status


def test_candidate_b_mcmc_blocked():
    """Candidate B MCMC blocked"""
    assert CANDIDATE_B.mcmc_allowed is False
    assert BridgeStatus.MCMC_BLOCKED in CANDIDATE_B.status


def test_candidate_b_prediction_blocked():
    """Candidate B prediction blocked"""
    assert CANDIDATE_B.prediction_allowed is False
    assert BridgeStatus.PREDICTION_BLOCKED in CANDIDATE_B.status


def test_phi_heuristic_not_physical_bridge():
    """Phi heuristic is TABLE_REPRODUCTION_HEURISTIC_ONLY"""
    assert (
        BridgeStatus.TABLE_REPRODUCTION_HEURISTIC_ONLY in CANDIDATE_PHI.status
    )
    assert (
        BridgeStatus.BEST_INTERNAL_CANDIDATE not in CANDIDATE_PHI.status
    )


def test_phi_heuristic_dimensional_issue():
    """Phi heuristic dimensional check fails (under-specified)"""
    assert CANDIDATE_PHI.dimensional_check.passes is False
    assert "under-specified" in CANDIDATE_PHI.dimensional_check.notes.lower()


def test_phi_heuristic_mcmc_blocked():
    """Phi heuristic MCMC blocked"""
    assert CANDIDATE_PHI.mcmc_allowed is False


def test_phi_heuristic_prediction_blocked():
    """Phi heuristic prediction blocked"""
    assert CANDIDATE_PHI.prediction_allowed is False


def test_no_mcmc_allowed_globally():
    """is_mcmc_allowed() returns False"""
    assert is_mcmc_allowed() is False


def test_no_prediction_allowed_globally():
    """is_prediction_allowed() returns False"""
    assert is_prediction_allowed() is False


def test_best_internal_candidate_is_b():
    """get_best_internal_candidate() returns Candidate B"""
    best = get_best_internal_candidate()
    assert best.candidate_id == "discrete_lattice_ode"


def test_row_1_status_is_outlier():
    """Row 1 marked as SOURCE_TABLE_OUTLIER"""
    status = get_row_1_status()
    assert status["classification"] == "SOURCE_TABLE_OUTLIER"
    assert status["sigma_mult_diff"] > 3.0
    assert status["exceed_factor"] > 20


def test_row_1_exclusion_recommendation():
    """Row 1 exclusion recommended"""
    status = get_row_1_status()
    assert "Exclude" in status["recommendation"]
    assert status["usable_rows"] == "Rows 2-12 (z=0.06 to 8.5)"


def test_author_question_exists():
    """Author clarification question Q15 exists"""
    question = get_author_question_bridge_method()
    assert len(question) > 0
    assert "F_oP" in question
    assert "D_AB" in question
    assert "ä/a" in question or "a/a" in question


def test_validate_registry_passes():
    """validate_registry() returns no issues"""
    issues = validate_registry()
    assert len(issues) == 0, f"Registry validation failed: {issues}"


def test_no_function_compute_H_MULT_source_confirmed():
    """No function compute_H_MULT_source_confirmed exists"""
    import src.bridge_candidate_math_audit as module

    assert not hasattr(module, "compute_H_MULT_source_confirmed"), (
        "Module should NOT have compute_H_MULT_source_confirmed — "
        "all candidates remain MCMC_BLOCKED"
    )
