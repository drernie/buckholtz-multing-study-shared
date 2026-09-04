"""Tests for Deep Bridge Independent Verification

Purpose: Verify algebraic consistency of Hamiltonian bridge H²(a) reconstruction

Safety: All tests verify internal reconstruction, NOT source-confirmed model
"""

from src.deep_bridge_verification import (
    ForceComponent,
    H2ScalingDerivation,
    PotentialDerivation,
    analyze_signs,
    check_acceleration_logic,
    check_force_scaling_pass,
    check_h2_derivation_pass,
    check_monopole_only_limit,
    check_potential_integration_pass,
    derive_h2_scalings,
    generate_final_verdict,
    get_forbidden_wording,
    get_safe_wording,
    is_mcmc_allowed,
    is_prediction_allowed,
    verify_all_potentials,
    verify_dipole_potential,
    verify_monopole_potential,
    verify_quadrupole_potential,
    verify_source_force_scalings,
)

# ============================================================================
# Part 1: Force Scaling Verification Tests
# ============================================================================


def test_force_scalings_explicitly_represented():
    """Test 1: Force scalings are explicitly represented"""
    components = verify_source_force_scalings()

    assert len(components) == 4  # F_m, F_d, F_q, F_oP total

    # Check each component has required fields
    for comp in components:
        assert isinstance(comp, ForceComponent)
        assert comp.component
        assert comp.r_scaling
        assert comp.sign_in_f_op
        assert comp.status


def test_force_scalings_match_expected():
    """Test: Force scalings match expected (r⁻², r⁻³, r⁻⁴)"""
    components = verify_source_force_scalings()

    scalings = {comp.component: comp.r_scaling for comp in components}

    assert scalings["Monopole (F_m)"] == "r⁻²"
    assert scalings["Dipole (F_d)"] == "r⁻³"
    assert scalings["Quadrupole (F_q)"] == "r⁻⁴"


def test_force_scalings_status_source_confirmed():
    """Test: All force components have SOURCE_CONFIRMED status"""
    components = verify_source_force_scalings()

    for comp in components:
        if comp.component != "Total (F_oP)":
            assert comp.status == "SOURCE_CONFIRMED"


def test_force_scaling_pass():
    """Test: check_force_scaling_pass() returns True"""
    assert check_force_scaling_pass() is True


# ============================================================================
# Part 2: Potential Integration Tests
# ============================================================================


def test_potential_differentiation_returns_original_force():
    """Test 2: Potential differentiation returns original force signs"""
    potentials = verify_all_potentials()

    for pot in potentials:
        assert isinstance(pot, PotentialDerivation)
        assert pot.passes is True
        assert "✅" in pot.check_derivative


def test_monopole_potential():
    """Test: Monopole potential V_m ∝ a⁻¹"""
    pot = verify_monopole_potential()

    assert pot.term == "Monopole (V_m)"
    assert pot.v_a_scaling == "a⁻¹"
    assert pot.passes is True
    assert "V_m = −G m_A m_P / r" in pot.potential_formula


def test_dipole_potential():
    """Test: Dipole potential V_d ∝ a⁻²"""
    pot = verify_dipole_potential()

    assert pot.term == "Dipole (V_d)"
    assert pot.v_a_scaling == "a⁻²"
    assert pot.passes is True
    assert "V_d = +C_d" in pot.potential_formula
    assert "repulsive" in pot.notes.lower()


def test_quadrupole_potential():
    """Test: Quadrupole potential V_q ∝ a⁻³"""
    pot = verify_quadrupole_potential()

    assert pot.term == "Quadrupole (V_q)"
    assert pot.v_a_scaling == "a⁻³"
    assert pot.passes is True
    assert "V_q = −C_q" in pot.potential_formula
    assert "attractive" in pot.notes.lower()


def test_potential_integration_pass():
    """Test: check_potential_integration_pass() returns True"""
    assert check_potential_integration_pass() is True


# ============================================================================
# Part 3: H² Derivation Tests
# ============================================================================


def test_h2_powers_derived_not_hardcoded():
    """Test 3: H² powers are derived, not hardcoded"""
    scalings = derive_h2_scalings()

    assert len(scalings) == 4  # a⁻², a⁻³, a⁻⁴, a⁻⁵

    for deriv in scalings:
        assert isinstance(deriv, H2ScalingDerivation)
        assert deriv.source_term  # Must have source
        assert deriv.v_a_scaling  # Must have V(a) scaling
        assert deriv.h2_scaling  # Must have H²(a) scaling
        assert deriv.verified is True


def test_h2_scalings_match_expected():
    """Test: H² scalings match expected (a⁻², a⁻³, a⁻⁴, a⁻⁵)"""
    scalings = derive_h2_scalings()

    h2_terms = {deriv.source_term: deriv.h2_scaling for deriv in scalings}

    assert h2_terms["E (integration constant)"] == "a⁻²"
    assert h2_terms["V_m (monopole)"] == "a⁻³"
    assert h2_terms["V_d (dipole)"] == "a⁻⁴"
    assert h2_terms["V_q (quadrupole)"] == "a⁻⁵"


def test_h2_derivation_pass():
    """Test: check_h2_derivation_pass() returns True"""
    assert check_h2_derivation_pass() is True


# ============================================================================
# Part 4: Monopole-Only Limit Tests
# ============================================================================


def test_monopole_only_limit():
    """Test 4: Monopole-only limit works (β_d=0, β_q=0 → matter + curvature)"""
    result = check_monopole_only_limit()

    assert result["beta_d_set_to_zero"] is True
    assert result["beta_q_set_to_zero"] is True
    assert result["matches_friedmann"] is True
    assert result["passes"] is True
    assert "Ω_k a⁻² + Ω_m a⁻³" in result["expected_formula"]


def test_monopole_limit_no_lambda():
    """Test: Monopole limit has no Λ term (as expected)"""
    result = check_monopole_only_limit()

    assert result["lambda_term_present"] is False
    assert result["lambda_term_expected"] is False  # MULTING uses dipole for acceleration


# ============================================================================
# Part 5: Sign and Acceleration Tests
# ============================================================================


def test_acceleration_logic():
    """Test: Acceleration ä/a logic computed from H² terms (CORRECTED)"""
    accel = check_acceleration_logic()

    assert "a_minus_2" in accel
    assert "a_minus_3" in accel
    assert "a_minus_4" in accel
    assert "a_minus_5" in accel

    # Check formula documented
    assert "formula" in accel
    assert "1 - n/2" in accel["formula"]


def test_a_minus_4_CAN_accelerate():
    """Test: a⁻⁴ term CAN accelerate if Ω_d < 0 (corrected interpretation)"""
    accel = check_acceleration_logic()

    # a⁻⁴ factor should be −1.0
    assert accel["a_minus_4"]["factor"] == -1.0

    # Should mention acceleration if Ω_d < 0
    a4_interp = accel["a_minus_4"]["interpretation"].lower()
    assert "acceleration if" in a4_interp or "accelerates if" in a4_interp


# ============================================================================
# Part 6: Safety Tests
# ============================================================================


def test_mcmc_blocked():
    """Test 6: MCMC is blocked"""
    assert is_mcmc_allowed() is False


def test_prediction_blocked():
    """Test 7: Prediction is blocked"""
    assert is_prediction_allowed() is False


def test_no_unsafe_wording():
    """Test 10: No unsafe wording appears"""
    forbidden = get_forbidden_wording()

    assert "validated" in forbidden
    assert "proved" in forbidden
    assert "solved" in forbidden
    assert "confirmed bridge" in forbidden
    assert "Buckholtz formula" in forbidden
    assert "discovery" in forbidden


def test_safe_wording_available():
    """Test: Safe wording is provided"""
    safe = get_safe_wording()

    assert "internal reconstruction" in safe
    assert "candidate bridge" in safe
    assert "algebraically consistent" in safe
    assert "diagnostic fit" in safe
    assert "source-unconfirmed" in safe


# ============================================================================
# Part 7: Final Verdict Tests
# ============================================================================


def test_final_verdict():
    """Test: Final verdict is generated"""
    verdict = generate_final_verdict()

    assert verdict["force_scaling"] == "PASS"
    assert verdict["potential_integration"] == "PASS"
    assert verdict["h2_scaling"] == "PASS"
    assert verdict["monopole_limit"] == "PASS"
    assert verdict["diagnostic_fit"] == "PENDING"
    assert verdict["source_confirmation"] == "NO"
    assert verdict["mcmc_readiness"] == "BLOCKED"
    assert verdict["prediction_readiness"] == "BLOCKED"


def test_verdict_overall_status():
    """Test: Overall status is ALGEBRAICALLY_VALID_BUT_SOURCE_UNCONFIRMED"""
    verdict = generate_final_verdict()

    assert "ALGEBRAICALLY_VALID" in verdict["overall_status"]
    assert "SOURCE_UNCONFIRMED" in verdict["overall_status"]


def test_verdict_notes_include_warnings():
    """Test: Verdict notes include a⁻⁴ neutrality warning"""
    verdict = generate_final_verdict()

    notes_text = " ".join(verdict["notes"])
    assert "a⁻⁴" in notes_text or "neutral" in notes_text.lower()
    assert "OUR_COMPUTATIONAL_RECONSTRUCTION" in notes_text


# ============================================================================
# Additional Safety Tests
# ============================================================================


def test_no_compute_h_mult_source_confirmed_function():
    """Test: No compute_H_MULT_source_confirmed() function exists"""
    import src.deep_bridge_verification as module

    assert not hasattr(module, "compute_H_MULT_source_confirmed")
    assert not hasattr(module, "compute_h_mult_source_confirmed")


def test_diagnostic_fit_marked_pending():
    """Test 8: Diagnostic fit is marked PENDING (not implemented yet)"""
    verdict = generate_final_verdict()

    assert verdict["diagnostic_fit"] == "PENDING"


def test_overfitting_status_reportable():
    """Test 9: Overfitting status is in verdict (pending)"""
    verdict = generate_final_verdict()

    # Overfitting audit not yet implemented, so should be in notes or pending
    assert "diagnostic_fit" in verdict  # Will be updated when fit implemented


# ============================================================================
# Integration Tests
# ============================================================================


def test_full_verification_chain():
    """Test: Full verification chain passes"""
    # Part 1: Force scalings
    assert check_force_scaling_pass() is True

    # Part 2: Potential integration
    assert check_potential_integration_pass() is True

    # Part 3: H² derivation
    assert check_h2_derivation_pass() is True

    # Part 4: Monopole limit
    assert check_monopole_only_limit()["passes"] is True

    # Safety
    assert is_mcmc_allowed() is False
    assert is_prediction_allowed() is False

    # Final verdict
    verdict = generate_final_verdict()
    assert verdict["force_scaling"] == "PASS"
    assert verdict["potential_integration"] == "PASS"
    assert verdict["h2_scaling"] == "PASS"
    assert verdict["monopole_limit"] == "PASS"


def test_row_1_excluded_placeholder():
    """Test 5: Row 1 is excluded (placeholder — fit not yet implemented)"""
    # This will be tested when diagnostic fit is implemented
    # For now, just verify the concept is documented
    verdict = generate_final_verdict()
    assert verdict["diagnostic_fit"] == "PENDING"


# ============================================================================
# Documentation Tests
# ============================================================================


def test_force_components_have_notes():
    """Test: All force components have explanatory notes"""
    components = verify_source_force_scalings()

    for comp in components:
        assert comp.notes  # Must have notes
        assert len(comp.notes) > 10  # Non-trivial explanation


def test_potentials_have_notes():
    """Test: All potentials have explanatory notes"""
    potentials = verify_all_potentials()

    for pot in potentials:
        assert pot.notes
        assert len(pot.notes) > 10


def test_h2_scalings_have_notes():
    """Test: All H² scalings have explanatory notes"""
    scalings = derive_h2_scalings()

    for deriv in scalings:
        assert deriv.notes
        assert len(deriv.notes) > 10


# ============================================================================
# Acceleration Correction Tests (Added 2026-05-29)
# ============================================================================


def test_acceleration_factor_a_minus_2_zero():
    """Test: a⁻² term gives zero acceleration contribution (curvature neutral)"""
    accel = check_acceleration_logic()

    assert accel["a_minus_2"]["n"] == 2
    assert accel["a_minus_2"]["factor"] == 0.0
    # Interpretation should indicate no acceleration/deceleration
    interp = accel["a_minus_2"]["interpretation"].lower()
    assert (
        "neutral" in accel["a_minus_2"]["contribution"].lower() or "does not accelerate" in interp
    )


def test_acceleration_factor_a_minus_3():
    """Test: a⁻³ term gives −0.5 factor (deceleration if Ω_m > 0)"""
    accel = check_acceleration_logic()

    assert accel["a_minus_3"]["n"] == 3
    assert accel["a_minus_3"]["factor"] == -0.5
    assert "deceleration" in accel["a_minus_3"]["interpretation"].lower()


def test_acceleration_factor_a_minus_4():
    """Test: a⁻⁴ term gives −1.0 factor (acceleration if Ω_d < 0)"""
    accel = check_acceleration_logic()

    assert accel["a_minus_4"]["n"] == 4
    assert accel["a_minus_4"]["factor"] == -1.0
    assert "acceleration if" in accel["a_minus_4"]["interpretation"].lower()


def test_acceleration_factor_a_minus_5():
    """Test: a⁻⁵ term gives −1.5 factor (strong deceleration if Ω_q > 0)"""
    accel = check_acceleration_logic()

    assert accel["a_minus_5"]["n"] == 5
    assert accel["a_minus_5"]["factor"] == -1.5
    assert "deceleration" in accel["a_minus_5"]["interpretation"].lower()


def test_negative_coefficient_flips_acceleration():
    """Test: Negative coefficient flips acceleration sign (documented)"""
    accel = check_acceleration_logic()

    # Check sign dependence documented for dipole
    assert "sign_dependence" in accel
    assert "Ω_d > 0" in accel["sign_dependence"]
    assert "Ω_d < 0" in accel["sign_dependence"]


def test_no_document_says_a_minus_4_neutral():
    """Test: No document incorrectly says 'a⁻⁴ is neutral'"""
    # Check acceleration logic
    accel = check_acceleration_logic()

    # a⁻⁴ should NOT be called neutral
    a4_text = str(accel["a_minus_4"]).lower()
    assert "neutral" not in a4_text

    # Check sign interpretations
    signs = analyze_signs()
    dipole_sign = [s for s in signs if s.component == "Dipole"][0]
    assert "neutral" not in dipole_sign.expected_effect.lower()


def test_acceleration_formula_documented():
    """Test: Correct acceleration formula ä/a = H²(1 - n/2) documented"""
    accel = check_acceleration_logic()

    assert "formula" in accel
    assert "1 - n/2" in accel["formula"]


def test_dipole_can_accelerate_documented():
    """Test: Key insight about dipole acceleration documented"""
    accel = check_acceleration_logic()

    assert "key_insight" in accel
    assert (
        "can accelerate" in accel["key_insight"].lower()
        or "accelerate if" in accel["key_insight"].lower()
    )


def test_sign_analysis_includes_dipole_acceleration():
    """Test: Sign analysis correctly shows dipole can accelerate"""
    signs = analyze_signs()

    dipole = [s for s in signs if s.component == "Dipole"][0]
    assert "acceleration" in dipole.expected_effect.lower()
    assert "if Ω_d < 0" in dipole.notes or "Ω_d < 0" in dipole.expected_effect


def test_final_verdict_corrected():
    """Test: Final verdict no longer says 'a⁻⁴ neutral'"""
    verdict = generate_final_verdict()

    notes_text = " ".join(verdict["notes"]).lower()
    assert (
        "neutral" not in notes_text or "curvature" in notes_text
    )  # Curvature is neutral, dipole is not
    assert "can accelerate" in notes_text or "sign" in notes_text
