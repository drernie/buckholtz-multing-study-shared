"""Tests for H_MULT Algorithm Candidates Registry

Purpose: Verify integrity and safety of candidate algorithm registry
Context: Appendix A1 Step 5 provides scaling relations but NOT explicit formula

Test Coverage:
1. Registry structure and uniqueness
2. Safety rules enforcement (no false SOURCE_CONFIRMED, no premature MCMC)
3. Status consistency (MCMC ↔ SOURCE_CONFIRMED)
4. Overfitting risk classification
5. Dimensional checks
6. Code permission enforcement
"""

import pytest

from src.hmult_algorithm_candidates import (
    CANDIDATES,
    AlgorithmStatus,
    CodePermission,
    count_candidates_by_status,
    get_all_candidates,
    get_candidate_by_id,
    get_candidates_by_status,
    get_implementable_candidates,
    get_source_confirmed_candidates,
    validate_registry,
)

# ============================================================================
# Test 1: Registry Structure
# ============================================================================


def test_candidates_list_exists():
    """CANDIDATES list exists and is not empty"""
    assert CANDIDATES is not None
    assert len(CANDIDATES) > 0, "Candidate registry should not be empty"


def test_candidate_count():
    """Verify expected number of candidates (8 documented in docs/40)"""
    assert len(CANDIDATES) == 9, f"Expected 9 candidates, found {len(CANDIDATES)}"


def test_candidate_ids_unique():
    """All candidate IDs must be unique"""
    ids = [c.candidate_id for c in CANDIDATES]
    assert len(ids) == len(set(ids)), f"Duplicate IDs found: {ids}"


def test_all_candidates_have_required_fields():
    """Every candidate has non-empty required fields"""
    required_fields = [
        "candidate_id",
        "name",
        "formula_latex",
        "status",
        "code_permission",
        "required_inputs",
    ]
    for c in CANDIDATES:
        for field in required_fields:
            value = getattr(c, field)
            assert value is not None, f"Candidate {c.candidate_id} missing {field}"
            if isinstance(value, str):
                assert len(value) > 0, f"Candidate {c.candidate_id} has empty {field}"


# ============================================================================
# Test 2: Safety Rules — No False SOURCE_CONFIRMED
# ============================================================================


def test_no_source_confirmed_without_manuscript_citation():
    """SOURCE_CONFIRMED candidates MUST have manuscript PDF citation"""
    source_confirmed = get_source_confirmed_candidates()
    for c in source_confirmed:
        assert c.source_file is not None, (
            f"Candidate {c.candidate_id} marked SOURCE_CONFIRMED " f"but source_file is None"
        )
        assert "preprints202511.0598" in c.source_file, (
            f"Candidate {c.candidate_id} marked SOURCE_CONFIRMED "
            f"but source_file does not cite manuscript PDF"
        )


def test_default_no_source_confirmed():
    """By default, no candidates should be SOURCE_CONFIRMED (formula missing)"""
    source_confirmed = get_source_confirmed_candidates()
    assert len(source_confirmed) == 0, (
        f"Found {len(source_confirmed)} SOURCE_CONFIRMED candidates. "
        f"Formula missing in Appendix A1 — this should be 0 until manuscript provides formula."
    )


# ============================================================================
# Test 3: Safety Rules — MCMC Allowed Only If SOURCE_CONFIRMED
# ============================================================================


def test_mcmc_allowed_only_if_source_confirmed():
    """MCMC allowed ONLY for SOURCE_CONFIRMED candidates"""
    for c in CANDIDATES:
        if c.mcmc_allowed:
            assert c.status == AlgorithmStatus.SOURCE_CONFIRMED, (
                f"Candidate {c.candidate_id} allows MCMC but status is "
                f"{c.status.value}, not SOURCE_CONFIRMED"
            )


def test_default_no_mcmc_allowed():
    """By default, NO candidates should allow MCMC (formula not confirmed)"""
    mcmc_allowed_candidates = [c for c in CANDIDATES if c.mcmc_allowed]
    assert len(mcmc_allowed_candidates) == 0, (
        f"Found {len(mcmc_allowed_candidates)} candidates allowing MCMC. "
        f"Should be 0 until author confirms formula."
    )


# ============================================================================
# Test 4: Overfitting Risk Classification
# ============================================================================


def test_high_dof_marked_extreme_overfitting():
    """Candidates with DoF > 6 (for N_rows=12) must be marked EXTREME overfitting"""
    N_rows = 12  # Table A1 expected row count
    threshold = N_rows / 2  # 50% rule: DoF > N/2 → EXTREME
    for c in CANDIDATES:
        if c.degrees_of_freedom > threshold:
            assert c.overfitting_risk == "EXTREME", (
                f"Candidate {c.candidate_id} has DoF={c.degrees_of_freedom} "
                f"(>{threshold}) but overfitting_risk is {c.overfitting_risk}, "
                f"should be EXTREME"
            )


def test_low_dof_not_marked_extreme():
    """Candidates with DoF ≤ 3 should NOT be marked EXTREME"""
    for c in CANDIDATES:
        if c.degrees_of_freedom <= 3:
            assert c.overfitting_risk != "EXTREME", (
                f"Candidate {c.candidate_id} has DoF={c.degrees_of_freedom} "
                f"but overfitting_risk is EXTREME — should be LOW or NONE"
            )


def test_overfitting_risk_valid_values():
    """Overfitting risk must be one of: EXTREME, HIGH, MEDIUM, LOW, NONE"""
    valid_risks = {"EXTREME", "HIGH", "MEDIUM", "LOW", "NONE"}
    for c in CANDIDATES:
        assert c.overfitting_risk in valid_risks, (
            f"Candidate {c.candidate_id} has invalid overfitting_risk: " f"{c.overfitting_risk}"
        )


# ============================================================================
# Test 5: Dimensional Checks
# ============================================================================


def test_all_candidates_pass_dimensional_check():
    """All candidates must pass dimensional analysis"""
    for c in CANDIDATES:
        assert (
            c.dimensional_check_passes is True
        ), f"Candidate {c.candidate_id} fails dimensional check"


# ============================================================================
# Test 6: Code Permission Enforcement
# ============================================================================


def test_blocked_candidates_cannot_predict_new_z():
    """BLOCKED candidates cannot predict on new z"""
    blocked = [c for c in CANDIDATES if c.code_permission == CodePermission.BLOCKED]
    for c in blocked:
        assert c.can_predict_new_z in [
            "NO",
            "UNKNOWN",
            "PARTIAL",  # PARTIAL valid: means "IF missing inputs provided"
        ], f"Candidate {c.candidate_id} is BLOCKED but can_predict_new_z={c.can_predict_new_z}"


def test_phenomenological_cannot_predict_reliably():
    """PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY cannot predict new z reliably"""
    phenom = get_candidates_by_status(AlgorithmStatus.PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY)
    for c in phenom:
        assert c.can_predict_new_z in ["NO", "PARTIAL"], (
            f"Candidate {c.candidate_id} is PHENOMENOLOGICAL but "
            f"can_predict_new_z={c.can_predict_new_z} (should be NO or PARTIAL)"
        )


def test_post_hoc_diagnostic_not_forward_model():
    """POST_HOC_DIAGNOSTIC_ONLY cannot predict new z (not a forward model)"""
    post_hoc = get_candidates_by_status(AlgorithmStatus.POST_HOC_DIAGNOSTIC_ONLY)
    for c in post_hoc:
        assert c.can_predict_new_z == "NO", (
            f"Candidate {c.candidate_id} is POST_HOC_DIAGNOSTIC but "
            f"can_predict_new_z={c.can_predict_new_z} (should be NO)"
        )


# ============================================================================
# Test 7: Status Distribution
# ============================================================================


def test_status_distribution_reasonable():
    """Verify reasonable distribution of candidate statuses"""
    counts = count_candidates_by_status()

    # At least one AI_TRANSCRIPT_REPORTED (Phi(z) scaling found in docs/35)
    assert (
        counts.get(AlgorithmStatus.AI_TRANSCRIPT_REPORTED, 0) >= 1
    ), "Should have at least 1 AI_TRANSCRIPT_REPORTED candidate (Phi(z) scaling)"

    # At least one MVB_CANDIDATE (virial pressure route in docs/37)
    assert (
        counts.get(AlgorithmStatus.MVB_CANDIDATE, 0) >= 1
    ), "Should have at least 1 MVB_CANDIDATE (discrete lattice + virial pressure)"

    # At least one PHENOMENOLOGICAL (spline fit, polynomial fit)
    assert (
        counts.get(AlgorithmStatus.PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY, 0) >= 1
    ), "Should have at least 1 PHENOMENOLOGICAL candidate (table fit)"


# ============================================================================
# Test 8: Registry Access Functions
# ============================================================================


def test_get_all_candidates():
    """get_all_candidates() returns all candidates"""
    all_candidates = get_all_candidates()
    assert len(all_candidates) == len(CANDIDATES)


def test_get_candidate_by_id_exists():
    """get_candidate_by_id() returns correct candidate"""
    first_candidate = CANDIDATES[0]
    retrieved = get_candidate_by_id(first_candidate.candidate_id)
    assert retrieved is not None
    assert retrieved.candidate_id == first_candidate.candidate_id


def test_get_candidate_by_id_not_found():
    """get_candidate_by_id() returns None for nonexistent ID"""
    retrieved = get_candidate_by_id("nonexistent_id_xyz123")
    assert retrieved is None


def test_get_implementable_candidates():
    """get_implementable_candidates() excludes BLOCKED candidates"""
    implementable = get_implementable_candidates()
    for c in implementable:
        assert (
            c.code_permission != CodePermission.BLOCKED
        ), f"Candidate {c.candidate_id} is BLOCKED but returned as implementable"


# ============================================================================
# Test 9: Validation Function
# ============================================================================


def test_validate_registry_no_issues():
    """validate_registry() should return empty list (no issues)"""
    issues = validate_registry()
    assert isinstance(issues, list), "validate_registry() should return list"
    if issues:
        pytest.fail(
            f"Registry validation failed with {len(issues)} issues:\n"
            + "\n".join(f"  - {issue}" for issue in issues)
        )


# ============================================================================
# Test 10: Specific Candidate Checks
# ============================================================================


def test_phi_z_scaling_exists():
    """Phi(z) scaling candidate exists (most explicit formula found)"""
    phi_z = get_candidate_by_id("phi_z_scaling")
    assert phi_z is not None, "Phi(z) scaling candidate not found"
    assert phi_z.status == AlgorithmStatus.AI_TRANSCRIPT_REPORTED
    assert phi_z.source_file == "docs/35_ai_transcript_closure_candidate.md"


def test_mvb_virial_pressure_exists():
    """MVB virial pressure candidate exists (most physical)"""
    mvb = get_candidate_by_id("mvb_virial_pressure")
    assert mvb is not None, "MVB virial pressure candidate not found"
    assert mvb.status == AlgorithmStatus.MVB_CANDIDATE
    assert mvb.source_file == "docs/37_discrete_lattice_mvb_hypothesis.md"


def test_spline_fit_is_phenomenological():
    """Spline fit candidate is PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY"""
    spline = get_candidate_by_id("spline_table_fit")
    assert spline is not None
    assert spline.status == AlgorithmStatus.PHENOMENOLOGICAL_TABLE_REPRODUCTION_ONLY
    assert spline.can_reproduce_table_a1 == "YES"
    assert spline.can_predict_new_z == "NO"
    assert spline.mcmc_allowed is False


def test_w_eff_diagnostic_is_post_hoc():
    """w_eff diagnostic is POST_HOC_DIAGNOSTIC_ONLY"""
    w_eff = get_candidate_by_id("w_eff_diagnostic")
    assert w_eff is not None
    assert w_eff.status == AlgorithmStatus.POST_HOC_DIAGNOSTIC_ONLY
    assert w_eff.can_predict_new_z == "NO"
    assert w_eff.code_permission == CodePermission.DIAGNOSTIC_ONLY


# ============================================================================
# Test 11: Required Inputs Check
# ============================================================================


def test_all_candidates_have_required_inputs_list():
    """Every candidate has non-empty required_inputs list"""
    for c in CANDIDATES:
        assert isinstance(
            c.required_inputs, list
        ), f"Candidate {c.candidate_id} required_inputs is not a list"
        assert (
            len(c.required_inputs) > 0
        ), f"Candidate {c.candidate_id} has empty required_inputs list"


def test_phi_z_requires_amplitude_tables():
    """Phi(z) scaling requires A_m, A_d, A_q tables"""
    phi_z = get_candidate_by_id("phi_z_scaling")
    required = phi_z.required_inputs
    assert "A_m(z)" in required, "Phi(z) should require A_m(z)"
    assert "A_d(z)" in required, "Phi(z) should require A_d(z)"
    assert "A_q(z)" in required, "Phi(z) should require A_q(z)"
    assert "H_anchor" in required, "Phi(z) should require H_anchor"


def test_force_ratio_requires_cluster_variables():
    """Force ratio scaling requires cluster variables"""
    force_ratio = get_candidate_by_id("force_ratio_scaling")
    required = force_ratio.required_inputs
    assert "m_A(z)" in required, "Force ratio should require m_A(z)"
    assert "r_A(z)" in required, "Force ratio should require r_A(z)"
    assert "D_CAB(z)" in required, "Force ratio should require D_CAB(z)"
    assert "beta_d" in required, "Force ratio should require beta_d"
    assert "beta_q" in required, "Force ratio should require beta_q"


# ============================================================================
# Test 12: No Compute Hz Source Confirmed Function
# ============================================================================


def test_no_function_named_compute_hz_source_confirmed():
    """No function named compute_Hz_source_confirmed should exist"""
    import src.hmult_algorithm_candidates as module

    assert not hasattr(module, "compute_Hz_source_confirmed"), (
        "Module should NOT have function compute_Hz_source_confirmed — "
        "H_MULT formula not source-confirmed"
    )
    assert not hasattr(module, "compute_H_MULT_source_confirmed"), (
        "Module should NOT have function compute_H_MULT_source_confirmed — "
        "H_MULT formula not source-confirmed"
    )


# ============================================================================
# Test 13: Beta Values Remain Fitted
# ============================================================================


def test_beta_values_remain_fitted_not_derived():
    """Beta values (4.5, 18.0) should NOT appear as derived constants"""
    # This test ensures we don't accidentally treat beta_d, beta_q as
    # theoretical predictions rather than fitted parameters
    for c in CANDIDATES:
        if "beta_d" in str(c.formula_latex).lower():
            # If beta_d appears in formula, check notes mention "fitted"
            assert (
                "fitted" in c.notes.lower() or "table" in c.notes.lower()
            ), f"Candidate {c.candidate_id} uses beta_d but does not note it's fitted"


# ============================================================================
# Test 14: Candidate Summary Generation
# ============================================================================


def test_generate_candidate_summary():
    """generate_candidate_summary() produces non-empty markdown"""
    from src.hmult_algorithm_candidates import generate_candidate_summary

    summary = generate_candidate_summary()
    assert isinstance(summary, str)
    assert len(summary) > 0
    assert "# H_MULT Algorithm Candidates Summary" in summary
    assert f"**Total candidates:** {len(CANDIDATES)}" in summary


# ============================================================================
# Test 15: Edge Case — Empty Required Inputs
# ============================================================================


def test_no_candidate_has_zero_required_inputs():
    """No candidate should have zero required inputs (even diagnostics need H_MULT)"""
    for c in CANDIDATES:
        assert len(c.required_inputs) > 0, (
            f"Candidate {c.candidate_id} has zero required inputs — "
            f"all candidates need at least one input"
        )


# ============================================================================
# Summary Test
# ============================================================================


def test_registry_integrity_summary():
    """Master test: verify all safety rules in one place"""
    # Rule 1: No SOURCE_CONFIRMED without manuscript
    source_confirmed = get_source_confirmed_candidates()
    assert len(source_confirmed) == 0, "Should have 0 SOURCE_CONFIRMED (formula missing)"

    # Rule 2: No MCMC allowed
    mcmc_allowed = [c for c in CANDIDATES if c.mcmc_allowed]
    assert len(mcmc_allowed) == 0, "Should have 0 MCMC-allowed candidates"

    # Rule 3: All dimensional checks pass
    failed_dim = [c for c in CANDIDATES if not c.dimensional_check_passes]
    assert len(failed_dim) == 0, f"{len(failed_dim)} candidates fail dimensional check"

    # Rule 4: Validation passes
    issues = validate_registry()
    assert len(issues) == 0, f"Registry has {len(issues)} validation issues"

    # Rule 5: 9 candidates documented
    assert len(CANDIDATES) == 9, f"Expected 9 candidates, found {len(CANDIDATES)}"

    print("\n✅ All registry integrity checks passed")
    print(f"   - {len(CANDIDATES)} candidates registered")
    print(f"   - {len(source_confirmed)} SOURCE_CONFIRMED (correct: formula missing)")
    print(f"   - {len(mcmc_allowed)} MCMC-allowed (correct: awaiting author)")
    print(f"   - {len(get_implementable_candidates())} implementable (non-BLOCKED)")
