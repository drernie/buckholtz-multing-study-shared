"""
Test beta provenance registry — source verification enforcement.

CRITICAL: These tests enforce the provenance audit finding:
ZERO beta values have confirmed sources. ALL are either audit_reconstruction
or source_missing. H(z) modeling is BLOCKED.
"""

from src.beta_provenance import (
    BETA_PROVENANCE_REGISTRY,
    count_by_provenance_status,
    count_by_use_permission,
    get_all_beta_names,
    get_audit_reconstruction_betas,
    get_beta_provenance,
    get_blocking_summary,
    get_manuscript_reported_fitted_betas,
    get_pending_verification_betas,
    get_source_confirmed_betas,
    get_source_missing_betas,
    h_z_modeling_blocked,
    is_allowed_for_modeling,
)


def test_all_six_beta_candidates_exist():
    """Registry must contain all 6 beta candidates (4 original + 2 NotebookLM)."""
    expected_names = {"beta_d_1", "beta_d_2", "beta_q_1", "beta_q_2", "beta_d_A1", "beta_q_A1"}
    actual_names = set(get_all_beta_names())

    assert actual_names == expected_names, f"Missing or extra beta candidates: {actual_names}"


def test_beta_d_1_provenance():
    """Beta_d_1 = 4.25 is audit reconstruction (17/4 from Eq.20)."""
    prov = get_beta_provenance("beta_d_1")

    assert prov.value == 4.25
    assert prov.provenance_status == "audit_reconstruction", (
        "17/4 is OUR reconstruction, not Buckholtz's statement"
    )
    assert prov.use_permission_status == "do_not_use_for_modeling"
    assert "17/4" in prov.first_known_appearance
    assert "7 alternative formulas" in prov.evidence_trail  # Uniqueness warning


def test_beta_d_2_provenance():
    """Beta_d_2 = 0.78 is audit reconstruction (7/9 from Eq.20) with HIGH numerology risk."""
    prov = get_beta_provenance("beta_d_2")

    assert prov.value == 0.78
    assert prov.provenance_status == "audit_reconstruction"
    assert prov.use_permission_status == "do_not_use_for_modeling"
    assert "7/9" in prov.first_known_appearance
    assert "20 alternative formulas" in prov.evidence_trail, "Must warn about structured numerology"


def test_beta_q_1_provenance():
    """Beta_q_1 = 8.10 is source_missing (cannot reconstruct from known anchors)."""
    prov = get_beta_provenance("beta_q_1")

    assert prov.value == 8.10
    assert prov.provenance_status == "source_missing", "8.10 has NO source and NO reconstruction"
    assert prov.use_permission_status == "do_not_use_for_modeling"
    assert "Unknown" in prov.first_known_appearance
    assert "HIGHEST PRIORITY" in prov.recommended_action  # Blocker flag


def test_beta_q_2_provenance():
    """Beta_q_2 = 0.19 is audit reconstruction (complexity-2 formula)."""
    prov = get_beta_provenance("beta_q_2")

    assert prov.value == 0.19
    assert prov.provenance_status == "audit_reconstruction"
    assert prov.use_permission_status == "do_not_use_for_modeling"
    assert "(1×4)/(3×7)" in prov.first_known_appearance
    assert "complexity-2" in prov.evidence_trail  # Warn about complex formula


def test_zero_source_confirmed_betas():
    """
    CRITICAL: ZERO beta values have confirmed sources.

    This is the PRIMARY BLOCKER for H(z) implementation.
    """
    source_confirmed = get_source_confirmed_betas()

    assert len(source_confirmed) == 0, (
        "PROVENANCE AUDIT FINDING: No beta values have confirmed sources. "
        "If this test fails, audit was incorrect OR Buckholtz provided clarification."
    )


def test_h_z_modeling_blocked():
    """H(z) modeling must be blocked until beta provenance confirmed."""
    assert h_z_modeling_blocked() is True, "H(z) MUST be blocked — no source-confirmed betas"


def test_no_beta_allowed_for_modeling():
    """
    Meta-test: is_allowed_for_modeling() must return False for ALL beta candidates.

    If this fails → either registry was updated (good) or test is wrong (bad).
    """
    for beta_name in get_all_beta_names():
        assert is_allowed_for_modeling(beta_name) is False, (
            f"{beta_name} marked as allowed for modeling, but provenance audit says NO"
        )


def test_audit_reconstruction_count():
    """3 out of 4 beta values are audit reconstructions."""
    audit_recon = get_audit_reconstruction_betas()

    # Expected: beta_d_1, beta_d_2, beta_q_2
    assert len(audit_recon) == 3, f"Expected 3 audit reconstructions, got {len(audit_recon)}"
    assert "beta_d_1" in audit_recon
    assert "beta_d_2" in audit_recon
    assert "beta_q_2" in audit_recon


def test_source_missing_count():
    """1 out of 4 beta values is source_missing (beta_q_1)."""
    source_missing = get_source_missing_betas()

    assert len(source_missing) == 1, f"Expected 1 source_missing, got {len(source_missing)}"
    assert "beta_q_1" in source_missing


def test_provenance_status_counts():
    """Count provenance statuses — must match audit findings + manually verified candidates."""
    counts = count_by_provenance_status()

    assert counts.get("audit_reconstruction", 0) == 3, "3 audit reconstructions"
    assert counts.get("source_missing", 0) == 1, "1 source missing"
    assert counts.get("manuscript_reported_fitted", 0) == 2, (
        "2 manually verified fitted values (beta_d_A1=4.5, beta_q_A1=18.0)"
    )
    assert counts.get("source_confirmed", 0) == 0, "ZERO source confirmed (fitted ≠ confirmed)"
    assert counts.get("buckholtz_stated", 0) == 0, (
        "ZERO buckholtz_stated (no emails/drafts available)"
    )


def test_use_permission_counts():
    """4 beta values blocked, 2 allowed for fit reproduction only."""
    counts = count_by_use_permission()

    assert counts.get("do_not_use_for_modeling", 0) == 4, (
        "4 beta values BLOCKED (audit/source_missing)"
    )
    assert counts.get("allowed_for_fit_reproduction_only", 0) == 2, (
        "2 allowed for fit reproduction (beta_d_A1, beta_q_A1)"
    )
    assert counts.get("source_confirmed", 0) == 0, "ZERO allowed for predictive modeling"


def test_blocking_summary_contains_key_info():
    """Blocking summary must mention primary issues."""
    summary = get_blocking_summary()

    assert "BLOCKED" in summary, "Must state H(z) is blocked"
    assert "0/6" in summary or "Source confirmed: 0" in summary, (
        "Must show 0 source-confirmed betas out of 6 total"
    )
    assert "Audit reconstruction" in summary or "audit_recon" in summary.lower()
    assert "beta_q_1" in summary, "Must mention beta_q_1 (source_missing, highest priority)"
    assert "Pending verification" in summary or "NotebookLM" in summary, (
        "Must mention NotebookLM candidates"
    )


def test_no_phantom_beta_values():
    """Registry must contain exactly 6 beta candidates (4 original + 2 NotebookLM)."""
    assert len(BETA_PROVENANCE_REGISTRY) == 6, "Must have exactly 6 beta candidates"


def test_all_betas_have_recommended_action():
    """Every beta must have explicit recommended_action (not empty)."""
    for beta_name in get_all_beta_names():
        prov = get_beta_provenance(beta_name)
        assert prov.recommended_action.strip() != "", f"{beta_name} missing recommended_action"


def test_audit_reconstructions_marked_as_our_inference():
    """
    Audit reconstructions must clearly state they are OUR derivation, not Buckholtz's.

    This prevents circular reasoning: using our inference as if it were his claim.
    """
    audit_recon = get_audit_reconstruction_betas()

    for beta_name in audit_recon:
        prov = get_beta_provenance(beta_name)
        evidence_lower = prov.evidence_trail.lower()

        # Must mention "audit" or "we derived" or "our reconstruction"
        assert any(
            phrase in evidence_lower
            for phrase in ["audit reconstruction", "we derived", "our reconstruction"]
        ), f"{beta_name}: audit reconstruction not clearly marked as OUR inference"


def test_beta_d_2_numerology_warning():
    """
    Beta_d_2 has 20 alternatives (HIGH structured numerology risk).

    Must be flagged explicitly to prevent false uniqueness claims.
    """
    prov = get_beta_provenance("beta_d_2")

    assert "20 alternative" in prov.evidence_trail, "Must warn about 20 alternatives"
    assert (
        "structured numerology" in prov.evidence_trail.lower() or "HIGH" in prov.evidence_trail
    ), "Must flag HIGH numerology risk"


def test_beta_q_1_highest_priority_flag():
    """
    Beta_q_1 is source_missing AND cannot be reconstructed.

    Must be flagged as HIGHEST PRIORITY for clarification.
    """
    prov = get_beta_provenance("beta_q_1")

    assert "HIGHEST PRIORITY" in prov.recommended_action.upper(), (
        "beta_q_1 (source_missing, no reconstruction) must be highest priority"
    )


# NEW TESTS: NotebookLM candidates


def test_beta_d_A1_provenance():
    """Beta_d_A1 = 4.5 is manually verified manuscript-reported fitted value."""
    prov = get_beta_provenance("beta_d_A1")

    assert prov.value == 4.5
    assert prov.provenance_status == "manuscript_reported_fitted", (
        "Manually verified from preprints202511.0598.v6.pdf, Appendix A.3, Table A1"
    )
    assert prov.use_permission_status == "allowed_for_fit_reproduction_only"
    assert "MANUALLY VERIFIED" in prov.evidence_trail
    assert "Table A1" in prov.evidence_trail or "Appendix" in prov.evidence_trail
    assert "FIT REPRODUCTION ONLY" in prov.recommended_action
    assert prov.manual_verification_status == "manually_verified"
    assert prov.derivation_status == "fitted_not_derived"
    assert prov.manuscript_identifier == "preprints202511.0598.v6.pdf"


def test_beta_q_A1_provenance():
    """Beta_q_A1 = 18.0 is manually verified manuscript-reported fitted value."""
    prov = get_beta_provenance("beta_q_A1")

    assert prov.value == 18.0
    assert prov.provenance_status == "manuscript_reported_fitted", (
        "Manually verified from preprints202511.0598.v6.pdf, Appendix A.3, Table A1"
    )
    assert prov.use_permission_status == "allowed_for_fit_reproduction_only"
    assert "MANUALLY VERIFIED" in prov.evidence_trail
    assert "Table A1" in prov.evidence_trail or "Appendix" in prov.evidence_trail
    assert "FIT REPRODUCTION ONLY" in prov.recommended_action
    assert prov.manual_verification_status == "manually_verified"
    assert prov.derivation_status == "fitted_not_derived"
    assert prov.manuscript_identifier == "preprints202511.0598.v6.pdf"


def test_pending_verification_count():
    """0 NotebookLM candidates pending verification (both manually verified)."""
    pending = get_pending_verification_betas()

    assert len(pending) == 0, (
        f"Expected 0 pending verification after manual check, got {len(pending)}. "
        "Beta_d_A1 and beta_q_A1 are now manuscript_reported_fitted."
    )


def test_manuscript_reported_fitted_count():
    """2 manuscript-reported fitted values (NotebookLM candidates manually verified)."""
    fitted = get_manuscript_reported_fitted_betas()

    assert len(fitted) == 2, (
        f"Expected 2 manuscript_reported_fitted after manual verification, got {len(fitted)}. "
        "Beta_d_A1=4.5 and beta_q_A1=18.0 verified from preprints202511.0598.v6.pdf."
    )
    assert "beta_d_A1" in fitted
    assert "beta_q_A1" in fitted


def test_notebooklm_candidates_ai_warning():
    """Manually verified candidates must state AI-assisted fitting context."""
    for beta_name in ["beta_d_A1", "beta_q_A1"]:
        prov = get_beta_provenance(beta_name)
        evidence_lower = prov.evidence_trail.lower()

        assert (
            "ai-assisted thought experiment" in evidence_lower
            or "llm was instructed" in evidence_lower
        ), f"{beta_name}: must document AI-assisted fitting context from manuscript"


def test_notebooklm_candidates_fitted_context():
    """Manually verified candidates must explicitly state fitted (not derived) status."""
    for beta_name in ["beta_d_A1", "beta_q_A1"]:
        prov = get_beta_provenance(beta_name)
        evidence_lower = prov.evidence_trail.lower()

        assert (
            "fitted phenomenological parameters" in evidence_lower
            and "not derived" in evidence_lower
        ), f"{beta_name}: must explicitly state fitted (NOT derived) status"

        assert prov.derivation_status == "fitted_not_derived", (
            f"{beta_name}: derivation_status must be 'fitted_not_derived'"
        )


def test_h_z_modeling_still_blocked_with_notebooklm():
    """H(z) modeling REMAINS blocked even with manually verified fitted values (circular reasoning)."""
    assert h_z_modeling_blocked() is True, (
        "H(z) MUST remain blocked — beta_d_A1 and beta_q_A1 are manuscript_reported_fitted "
        "(fitted to H(z) data), NOT source_confirmed. Using fitted values for H(z) predictions = circular reasoning."
    )
