"""Safety Tests for H_FLRW Provenance Recovery

Purpose: Ensure H_FLRW provenance mismatch is correctly classified,
         not as author error or validation/refutation claim.

Safety Labels:
- H_FLRW_PROVENANCE_MISMATCH
- NOT_AUTHOR_ERROR
- NOT_VALIDATION
- NOT_REFUTATION
"""

from pathlib import Path


def test_no_author_error_wording_in_reports():
    """Reports should not contain author-error wording"""
    report_files = [
        "docs/66_table_a1_recomputation_report.md",
        "docs/68_hflrw_provenance_recovery.md",
    ]

    # Check for phrases in POSITIVE context only
    # (negative like "NOT an author error" is safe)
    forbidden_positive_phrases = [
        "author made error",
        "Buckholtz error",
        "Buckholtz mistake",
        "Buckholtz made error",
        "table is wrong",
        "paper is wrong",
        "incorrect H_FLRW",
        "author's error",
        "author's mistake",
    ]

    for report_file in report_files:
        file_path = Path(__file__).parent.parent / report_file
        if not file_path.exists():
            continue  # Skip if file doesn't exist yet

        content = file_path.read_text(encoding="utf-8").lower()

        for phrase in forbidden_positive_phrases:
            assert phrase.lower() not in content, (
                f"Found forbidden phrase '{phrase}' in {report_file}"
            )


def test_provenance_mismatch_labels_present():
    """Reports should contain correct classification labels"""
    report_file = Path(__file__).parent.parent / "docs/66_table_a1_recomputation_report.md"

    if not report_file.exists():
        return  # Skip if file doesn't exist

    content = report_file.read_text(encoding="utf-8")

    required_labels = [
        "H_FLRW_PROVENANCE_MISMATCH",
        "NOT_AUTHOR_ERROR",
        "NOT_VALIDATION",
        "NOT_REFUTATION",
    ]

    for label in required_labels:
        assert label in content, f"Missing required label: {label}"


def test_explicit_not_author_error_statement():
    """Reports should explicitly state this is not an author error"""
    report_files = [
        "docs/66_table_a1_recomputation_report.md",
        "docs/68_hflrw_provenance_recovery.md",
    ]

    for report_file in report_files:
        file_path = Path(__file__).parent.parent / report_file
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8")

        # Should contain explicit negative statement
        assert (
            "NOT an author error" in content
            or "NOT an author-error" in content
            or "not an author error" in content
        ), f"Missing explicit 'NOT an author error' statement in {report_file}"


def test_no_validation_refutation_wording():
    """Reports should not contain validation/refutation language"""
    report_files = [
        "docs/66_table_a1_recomputation_report.md",
        "docs/68_hflrw_provenance_recovery.md",
    ]

    forbidden_phrases = [
        "validates MULTING",
        "refutes MULTING",
        "proves MULTING",
        "disproves MULTING",
        "confirms theory",
        "rejects theory",
        "MULTING is wrong",
        "MULTING is correct",
    ]

    for report_file in report_files:
        file_path = Path(__file__).parent.parent / report_file
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8").lower()

        for phrase in forbidden_phrases:
            assert phrase.lower() not in content, (
                f"Found forbidden validation/refutation phrase '{phrase}' in {report_file}"
            )


def test_diagnostic_script_has_safety_labels():
    """Diagnostic script should have safety labels in docstring"""
    script_path = Path(__file__).parent.parent / "scripts/diagnose_hflrw_parameter_candidates.py"

    if not script_path.exists():
        return

    content = script_path.read_text(encoding="utf-8")

    required_labels = [
        "INTERNAL_DIAGNOSTIC_ONLY",
        "NOT_SOURCE_CONFIRMED",
        "NOT_VALIDATION",
        "NOT_REFUTATION",
    ]

    for label in required_labels:
        assert label in content, f"Missing required safety label '{label}' in diagnostic script"


def test_mcmc_remains_blocked():
    """MCMC should still be blocked after H_FLRW provenance work"""
    # Check that we didn't accidentally enable MCMC
    # This would be detected by checking for MCMC implementation files
    # or MCMC-related code that shouldn't exist

    mcmc_files_that_should_not_exist = [
        "src/mcmc_hflrw_fit.py",
        "src/mcmc_multing_comparison.py",
        "scripts/run_mcmc_comparison.py",
    ]

    for forbidden_file in mcmc_files_that_should_not_exist:
        file_path = Path(__file__).parent.parent / forbidden_file
        assert not file_path.exists(), f"MCMC file should not exist: {forbidden_file}"


def test_prediction_remains_blocked():
    """Prediction should still be blocked after H_FLRW provenance work"""
    # Check that we didn't create prediction code

    prediction_files_that_should_not_exist = [
        "src/out_of_sample_prediction.py",
        "src/hflrw_prediction.py",
        "scripts/run_prediction.py",
    ]

    for forbidden_file in prediction_files_that_should_not_exist:
        file_path = Path(__file__).parent.parent / forbidden_file
        assert not file_path.exists(), f"Prediction file should not exist: {forbidden_file}"


def test_provenance_recovery_doc_exists():
    """H_FLRW provenance recovery document should exist"""
    doc_path = Path(__file__).parent.parent / "docs/68_hflrw_provenance_recovery.md"
    assert doc_path.exists(), "H_FLRW provenance recovery doc not found"


def test_candidate_sweep_csv_exists():
    """Candidate sweep results CSV should exist"""
    csv_path = Path(__file__).parent.parent / "docs/68_hflrw_candidate_sweep.csv"
    assert csv_path.exists(), "Candidate sweep CSV not found"


def test_power_law_best_fit_documented():
    """Power law best fit (p≈0.87) should be documented"""
    doc_path = Path(__file__).parent.parent / "docs/68_hflrw_provenance_recovery.md"

    if not doc_path.exists():
        return

    content = doc_path.read_text(encoding="utf-8")

    # Should mention power law fit and p≈0.87
    assert "power law" in content.lower() or "Power Law" in content
    assert "0.87" in content or "p = 0.87" in content or "p=0.87" in content


def test_meeting_safe_question_present():
    """Meeting-safe question for author should be documented"""
    doc_path = Path(__file__).parent.parent / "docs/68_hflrw_provenance_recovery.md"

    if not doc_path.exists():
        return

    content = doc_path.read_text(encoding="utf-8")

    # Should have meeting-safe question section
    assert "Meeting-Safe Question" in content or "meeting-safe question" in content


def test_no_email_sent_confirmation():
    """Confirm no email was sent during H_FLRW provenance work"""
    # Check email status document
    email_status_path = Path(__file__).parent.parent / "docs/26_email_status.md"

    if email_status_path.exists():
        content = email_status_path.read_text(encoding="utf-8")

        # Should NOT contain H_FLRW provenance email sent
        assert "H_FLRW provenance sent" not in content, "Email should not have been sent"


def test_assumptions_explicitly_tracked():
    """Assumptions should be explicitly tracked and labeled"""
    doc_path = Path(__file__).parent.parent / "docs/68_hflrw_provenance_recovery.md"

    if not doc_path.exists():
        return

    content = doc_path.read_text(encoding="utf-8")

    # Should have assumptions section
    assert "Assumption" in content or "assumption" in content

    # Should have evidence levels
    evidence_markers = [
        "ASSUMED_STANDARD",
        "INFERRED",
        "EXPLICIT",
        "NOT_STATED",
    ]

    has_evidence = any(marker in content for marker in evidence_markers)
    assert has_evidence, "Should have evidence level markers for assumptions"


def test_internal_diagnostic_only_label():
    """All provenance work should be labeled INTERNAL_DIAGNOSTIC_ONLY"""
    report_files = [
        "docs/66_table_a1_recomputation_report.md",
        "docs/68_hflrw_provenance_recovery.md",
    ]

    for report_file in report_files:
        file_path = Path(__file__).parent.parent / report_file
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8")

        assert "INTERNAL" in content and "DIAGNOSTIC" in content, (
            f"Missing INTERNAL_DIAGNOSTIC label in {report_file}"
        )
