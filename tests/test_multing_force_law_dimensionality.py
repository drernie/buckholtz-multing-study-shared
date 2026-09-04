"""Tests for MULTING force-law records — dimensional integrity checks."""

from src.multing_force_law_records import (
    CodePermission,
    ProvenanceStatus,
    UnitsStatus,
    get_all_closure_requirements,
    get_all_force_laws,
    get_all_length_scales,
    get_critical_blockers,
    get_force_law_status_summary,
    is_hz_modeling_allowed,
)


class TestForceLawRecords:
    """Test force-law record structure and status."""

    def test_all_force_laws_exist(self):
        """All 4 force-law records exist (monopole, dipole, quadrupole, total)."""
        force_laws = get_all_force_laws()

        assert len(force_laws) == 4, "Should have 4 force-law records"

        names = {fl.name for fl in force_laws}
        assert names == {"monopole", "dipole", "quadrupole", "total"}

    def test_each_force_law_has_required_fields(self):
        """Every force-law record has all required fields filled."""
        force_laws = get_all_force_laws()

        for fl in force_laws:
            assert fl.name, f"Force law {fl} missing name"
            assert fl.equation_latex, f"Force law {fl.name} missing equation_latex"
            assert fl.status, f"Force law {fl.name} missing status"
            assert fl.source_note, f"Force law {fl.name} missing source_note"
            assert fl.variables, f"Force law {fl.name} missing variables"
            assert fl.units_status, f"Force law {fl.name} missing units_status"
            assert fl.code_permission, f"Force law {fl.name} missing code_permission"
            assert fl.interpretation, f"Force law {fl.name} missing interpretation"

    def test_all_force_laws_are_source_candidate(self):
        """All force laws have status SOURCE_CANDIDATE (awaiting manual verification)."""
        force_laws = get_all_force_laws()

        for fl in force_laws:
            assert fl.status == ProvenanceStatus.SOURCE_CANDIDATE, (
                f"{fl.name} should be SOURCE_CANDIDATE until manually verified"
            )

    def test_all_force_laws_have_correct_units(self):
        """All force laws pass dimensional analysis (units status CORRECT)."""
        force_laws = get_all_force_laws()

        for fl in force_laws:
            assert fl.units_status == UnitsStatus.CORRECT, (
                f"{fl.name} dimensional analysis should be CORRECT"
            )

    def test_no_force_law_is_hz_ready(self):
        """No force law has code permission for H(z) modeling."""
        force_laws = get_all_force_laws()

        for fl in force_laws:
            assert fl.code_permission in (
                CodePermission.ALLOWED_FOR_DIMENSIONAL_CHECK,
                CodePermission.ALLOWED_FOR_RECORD_ONLY,
            ), f"{fl.name} should NOT have H(z) modeling permission"

            # Explicit check: NOT_ALLOWED_FOR_HZ_MODELING exists but not used for force laws
            # (force laws use DIMENSIONAL_CHECK or RECORD_ONLY, which also blocks H(z))


class TestLengthScaleRecords:
    """Test beta length-scale record structure."""

    def test_all_length_scales_exist(self):
        """All 3 beta length-scale records exist (r_dA, r_dP, r_qAB)."""
        scales = get_all_length_scales()

        assert len(scales) == 3, "Should have 3 length-scale records"

        names = {s.name for s in scales}
        assert names == {"r_dA", "r_dP", "r_qAB"}

    def test_each_length_scale_has_required_fields(self):
        """Every length-scale record has all required fields filled."""
        scales = get_all_length_scales()

        for s in scales:
            assert s.name, f"Length scale {s} missing name"
            assert s.definition_latex, f"Length scale {s.name} missing definition_latex"
            assert s.status, f"Length scale {s.name} missing status"
            assert s.source_note, f"Length scale {s.name} missing source_note"
            assert s.beta_parameter, f"Length scale {s.name} missing beta_parameter"
            assert s.characteristic_radius, f"Length scale {s.name} missing characteristic_radius"
            assert s.units, f"Length scale {s.name} missing units"
            assert s.code_permission, f"Length scale {s.name} missing code_permission"
            assert s.interpretation_unknown, f"Length scale {s.name} missing interpretation_unknown"

    def test_all_length_scales_record_only(self):
        """All length scales have code permission RECORD_ONLY (no computation allowed)."""
        scales = get_all_length_scales()

        for s in scales:
            assert s.code_permission == CodePermission.ALLOWED_FOR_RECORD_ONLY, (
                f"{s.name} should be RECORD_ONLY (no computation)"
            )


class TestClosureRequirements:
    """Test missing closure components that block H(z) modeling."""

    def test_all_closure_requirements_exist(self):
        """All 5 closure requirements documented."""
        requirements = get_all_closure_requirements()

        assert len(requirements) >= 5, "Should have ≥5 closure requirements"

        types = {req.requirement_type for req in requirements}
        expected_types = {
            "mean_field_approximation",
            "cosmological_averaging",
            "closure_relations",
            "friedmann_equation",
            "likelihood_function",
        }
        assert expected_types.issubset(types), (
            f"Missing closure requirements: {expected_types - types}"
        )

    def test_critical_blockers_exist(self):
        """At least 4 CRITICAL-severity blockers."""
        critical = get_critical_blockers()

        assert len(critical) >= 4, "Should have ≥4 CRITICAL blockers for H(z) modeling"

    def test_each_closure_requirement_has_required_fields(self):
        """Every closure requirement has all required fields filled."""
        requirements = get_all_closure_requirements()

        for req in requirements:
            assert req.requirement_type, f"Closure requirement {req} missing requirement_type"
            assert req.description, (
                f"Closure requirement {req.requirement_type} missing description"
            )
            assert req.blocker_severity, (
                f"Closure requirement {req.requirement_type} missing blocker_severity"
            )
            assert req.what_we_need, (
                f"Closure requirement {req.requirement_type} missing what_we_need"
            )
            assert req.example_from_lcdm, (
                f"Closure requirement {req.requirement_type} missing example_from_lcdm"
            )

    def test_hz_closure_explicitly_missing(self):
        """H(z) closure is documented as missing."""
        requirements = get_all_closure_requirements()

        # Check that Friedmann equation is among requirements
        friedmann_req = next(
            (req for req in requirements if req.requirement_type == "friedmann_equation"), None
        )

        assert friedmann_req is not None, "Friedmann equation requirement must exist"
        assert friedmann_req.blocker_severity == "CRITICAL", (
            "Friedmann equation blocker must be CRITICAL"
        )


class TestHzModelingBlocker:
    """Test that H(z) modeling is explicitly blocked."""

    def test_hz_modeling_not_allowed(self):
        """is_hz_modeling_allowed() returns False."""
        assert not is_hz_modeling_allowed(), "H(z) modeling should be blocked"

    def test_no_function_named_compute_hz_exists(self):
        """No function named compute_Hz, model_Hz, or Hz_forward exists in force_law_records.py."""
        import src.multing_force_law_records as module

        forbidden_names = ["compute_Hz", "model_Hz", "Hz_forward", "H_MULT", "solve_friedmann"]

        for name in forbidden_names:
            assert not hasattr(module, name), f"Function {name} should NOT exist (H(z) blocked)"

    def test_force_law_status_summary_documents_blocker(self):
        """get_force_law_status_summary() documents H(z) blocker."""
        summary = get_force_law_status_summary()

        assert "MISSING" in summary["cosmological_closure"], "Closure should be MISSING"
        assert "BLOCKED" in summary["mcmc_readiness"], "MCMC should be BLOCKED"
        assert "allowed_for_dimensional_check ONLY" in summary["code_permission"], (
            "Code permission should restrict to dimensional check only"
        )


class TestSourceVerificationStatus:
    """Test that source verification requirements are clear."""

    def test_all_records_awaiting_verification(self):
        """All force laws and length scales are SOURCE_CANDIDATE (not confirmed)."""
        force_laws = get_all_force_laws()
        scales = get_all_length_scales()

        for fl in force_laws:
            assert fl.status == ProvenanceStatus.SOURCE_CANDIDATE, (
                f"{fl.name} should await manual verification"
            )

        for s in scales:
            assert s.status == ProvenanceStatus.SOURCE_CANDIDATE, (
                f"{s.name} should await manual verification"
            )

    def test_source_notes_mention_manual_verification(self):
        """All source notes mention 'awaiting manual PDF verification'."""
        force_laws = get_all_force_laws()
        scales = get_all_length_scales()

        for fl in force_laws:
            assert "awaiting manual" in fl.source_note.lower(), (
                f"{fl.name} source note should mention manual verification"
            )

        for s in scales:
            assert "awaiting manual" in s.source_note.lower(), (
                f"{s.name} source note should mention manual verification"
            )


class TestSafeConclusion:
    """Test that safe wording is provided."""

    def test_status_summary_has_safe_conclusion(self):
        """get_force_law_status_summary() includes a safe conclusion."""
        summary = get_force_law_status_summary()

        assert "safe_conclusion" in summary, "Summary should include safe_conclusion field"

        conclusion = summary["safe_conclusion"]

        # Safe conclusion should NOT claim validation/refutation
        forbidden_words = ["validates", "refutes", "proves", "disproves", "ruled out", "excluded"]

        for word in forbidden_words:
            assert word not in conclusion.lower(), (
                f"Safe conclusion should NOT contain '{word}': {conclusion}"
            )

        # Safe conclusion SHOULD mention what is provided and what is missing
        assert "pairwise force law" in conclusion.lower(), "Should mention force law"
        assert "do not provide" in conclusion.lower() or "missing" in conclusion.lower(), (
            "Should mention what is missing"
        )
