"""Tests for H-MULT closure candidate status — enforce restrictions."""

from src.hmult_closure_candidates import (
    ClosureStatus,
    UsePermission,
    get_all_closure_candidates,
    get_closure_status_summary,
    get_critical_blockers,
    get_known_inputs,
    get_missing_inputs,
    is_mcmc_allowed,
    is_predictive_modeling_allowed,
    is_table_reproduction_candidate,
)


class TestClosureCandidateExists:
    """Test that closure candidate is documented."""

    def test_closure_candidate_exists(self):
        """At least one closure candidate exists."""
        candidates = get_all_closure_candidates()

        assert len(candidates) >= 1, "Should have at least one closure candidate"

    def test_phi_z_scaling_candidate_exists(self):
        """Phi(z) heuristic scaling candidate exists."""
        candidates = get_all_closure_candidates()

        phi_candidate = next((c for c in candidates if "Phi(z)" in c.name), None)

        assert phi_candidate is not None, "Phi(z) scaling candidate should exist"
        assert "H_MULT" in phi_candidate.formula_text, "Formula should mention H_MULT"
        assert "A_m(z)" in phi_candidate.formula_text, "Formula should mention monopole amplitude"
        assert "A_d(z)" in phi_candidate.formula_text, "Formula should mention dipole amplitude"
        assert "A_q(z)" in phi_candidate.formula_text, "Formula should mention quadrupole amplitude"


class TestClosureStatus:
    """Test that closure candidate has correct status."""

    def test_status_is_ai_transcript_or_phenomenological(self):
        """Closure candidate status is AI_TRANSCRIPT_REPORTED or FITTED_PHENOMENOLOGICAL."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            assert candidate.status in (
                ClosureStatus.AI_TRANSCRIPT_REPORTED,
                ClosureStatus.FITTED_PHENOMENOLOGICAL,
            ), f"{candidate.name} should be AI_TRANSCRIPT or PHENOMENOLOGICAL, not source-confirmed"

    def test_status_not_theoretically_derived(self):
        """Closure candidate is NOT marked as theoretically derived."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            assert candidate.status != ClosureStatus.THEORETICALLY_DERIVED, (
                f"{candidate.name} should NOT be marked theoretically derived (no rigorous derivation)"
            )


class TestUsePermissions:
    """Test that use permissions are correctly restricted."""

    def test_predictive_modeling_not_allowed(self):
        """Predictive modeling is explicitly blocked."""
        assert not is_predictive_modeling_allowed(), "Predictive modeling should be blocked"

    def test_mcmc_not_allowed(self):
        """MCMC parameter estimation is explicitly blocked."""
        assert not is_mcmc_allowed(), "MCMC should be blocked"

    def test_table_reproduction_is_candidate(self):
        """Table reproduction is a candidate (allowed IF cluster variables provided)."""
        assert is_table_reproduction_candidate(), (
            "Table reproduction should be candidate (not guaranteed)"
        )

    def test_use_permission_includes_not_allowed_for_prediction(self):
        """Use permission list includes NOT_ALLOWED_FOR_PREDICTION."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            assert UsePermission.NOT_ALLOWED_FOR_PREDICTION in candidate.use_permission, (
                f"{candidate.name} should have NOT_ALLOWED_FOR_PREDICTION"
            )

    def test_use_permission_includes_not_allowed_for_mcmc(self):
        """Use permission list includes NOT_ALLOWED_FOR_MCMC."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            assert UsePermission.NOT_ALLOWED_FOR_MCMC in candidate.use_permission, (
                f"{candidate.name} should have NOT_ALLOWED_FOR_MCMC"
            )


class TestRequiredInputs:
    """Test that required inputs are documented."""

    def test_formula_requires_cluster_variables(self):
        """Formula requires cluster variables (m_A, r_A, k_A)."""
        required = [inp.name for inp in get_missing_inputs()]

        assert "m_A(z)" in required, "Should require m_A(z)"
        assert "r_A(z)" in required, "Should require r_A(z)"
        assert "k_A(z)" in required, "Should require k_A(z)"

    def test_critical_blocker_is_cluster_table(self):
        """Critical blocker is cluster variable table."""
        blockers = get_critical_blockers()
        missing_inputs = get_missing_inputs()

        assert len(blockers) >= 1, "Should have at least one critical blocker"

        # Check that one of the MISSING inputs with CRITICAL blocker is cluster table
        critical_inputs = [inp for inp in missing_inputs if "CRITICAL" in inp.blocker]
        assert any(
            "cluster" in inp.name.lower() or "cluster" in inp.description.lower()
            for inp in critical_inputs
        ), "Critical blocker should be cluster variable table"

    def test_beta_d_and_beta_q_are_known(self):
        """Beta_d and beta_q are marked as KNOWN."""
        known = get_known_inputs()

        beta_d = next((inp for inp in known if "beta_d" in inp.name), None)
        beta_q = next((inp for inp in known if "beta_q" in inp.name), None)

        assert beta_d is not None, "beta_d should be in KNOWN inputs"
        assert beta_q is not None, "beta_q should be in KNOWN inputs"
        assert "4.5" in beta_d.source, "beta_d source should mention 4.5"
        assert "18.0" in beta_q.source, "beta_q source should mention 18.0"


class TestNoComputeHzFunction:
    """Test that no compute_Hz function exists (intentional)."""

    def test_no_function_named_compute_hz_exists(self):
        """No function named compute_Hz, model_Hz, or Hz_forward exists."""
        import src.hmult_closure_candidates as module

        forbidden_names = ["compute_Hz", "model_Hz", "Hz_forward", "H_MULT", "solve_friedmann"]

        for name in forbidden_names:
            assert not hasattr(module, name), (
                f"Function {name} should NOT exist (H(z) computation blocked)"
            )

    def test_only_record_function_exists(self):
        """Only record_hmult_closure_candidate function exists (no computation)."""
        import src.hmult_closure_candidates as module

        assert hasattr(module, "record_hmult_closure_candidate"), (
            "record_hmult_closure_candidate should exist"
        )

        # Check it returns a record, not a number
        result = module.record_hmult_closure_candidate()
        assert hasattr(result, "name"), "Should return ClosureCandidate record, not H(z) value"
        assert hasattr(result, "formula_text"), "Should return record with formula_text"


class TestMissingItems:
    """Test that missing items are documented."""

    def test_formula_has_missing_items_list(self):
        """Formula has non-empty missing_items list."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            assert len(candidate.missing_items) > 0, (
                f"{candidate.name} should have missing_items list"
            )

    def test_missing_items_include_formal_derivation(self):
        """Missing items include 'formal derivation'."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            missing_text = " ".join(candidate.missing_items).lower()
            assert "derivation" in missing_text or "field equations" in missing_text, (
                f"{candidate.name} should mention missing formal derivation"
            )

    def test_missing_items_include_uncertainty_estimates(self):
        """Missing items include uncertainty estimates (sigma_MULT)."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            missing_text = " ".join(candidate.missing_items).lower()
            assert "sigma" in missing_text or "uncertainty" in missing_text, (
                f"{candidate.name} should mention missing uncertainty estimates"
            )


class TestSafeWording:
    """Test that safe and unsafe wording are provided."""

    def test_safe_wording_exists(self):
        """Every closure candidate has safe_wording."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            assert len(candidate.safe_wording) > 0, f"{candidate.name} should have safe_wording"

    def test_safe_wording_does_not_claim_prediction(self):
        """Safe wording does NOT claim 'predicts cosmic expansion'."""
        candidates = get_all_closure_candidates()

        forbidden_phrases = ["predicts cosmic expansion", "predicts H(z)", "validates MULTING"]

        for candidate in candidates:
            safe_lower = candidate.safe_wording.lower()
            for phrase in forbidden_phrases:
                assert phrase not in safe_lower, (
                    f"{candidate.name} safe_wording should NOT contain '{phrase}'"
                )

    def test_safe_wording_mentions_phenomenological_or_heuristic(self):
        """Safe wording mentions 'phenomenological' or 'heuristic'."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            safe_lower = candidate.safe_wording.lower()
            assert "phenomenological" in safe_lower or "heuristic" in safe_lower, (
                f"{candidate.name} safe_wording should mention phenomenological or heuristic"
            )

    def test_unsafe_wording_contains_forbidden_phrases(self):
        """Unsafe wording contains forbidden phrases as examples of what NOT to say."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            unsafe_lower = candidate.unsafe_wording.lower()
            assert "do not say" in unsafe_lower or "not allowed" in unsafe_lower, (
                f"{candidate.name} unsafe_wording should contain 'do not say' examples"
            )


class TestStatusSummary:
    """Test closure status summary function."""

    def test_status_summary_has_required_keys(self):
        """Status summary contains all required keys."""
        summary = get_closure_status_summary()

        required_keys = [
            "closure_candidate",
            "status",
            "required_inputs",
            "critical_blockers",
            "predictive_modeling",
            "mcmc_readiness",
            "table_reproduction",
            "safe_conclusion",
        ]

        for key in required_keys:
            assert key in summary, f"Summary should contain key '{key}'"

    def test_summary_says_predictive_modeling_not_allowed(self):
        """Summary states predictive modeling is NOT ALLOWED."""
        summary = get_closure_status_summary()

        assert "NOT ALLOWED" in summary["predictive_modeling"], (
            "Summary should state predictive modeling NOT ALLOWED"
        )

    def test_summary_says_mcmc_blocked(self):
        """Summary states MCMC is BLOCKED."""
        summary = get_closure_status_summary()

        assert "BLOCKED" in summary["mcmc_readiness"], "Summary should state MCMC BLOCKED"

    def test_summary_says_table_reproduction_candidate(self):
        """Summary states table reproduction is CANDIDATE."""
        summary = get_closure_status_summary()

        assert (
            "CANDIDATE" in summary["table_reproduction"]
            or "possible" in summary["table_reproduction"].lower()
        ), "Summary should state table reproduction is CANDIDATE (not guaranteed)"


class TestFormulaNotMarkedSourceDerived:
    """Test that formula is NOT marked as source-derived or theoretically derived."""

    def test_formula_not_source_confirmed(self):
        """Formula is NOT marked SOURCE_CONFIRMED (AI transcript only)."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            assert candidate.status != ClosureStatus.SOURCE_CONFIRMED, (
                f"{candidate.name} should NOT be SOURCE_CONFIRMED (AI transcript)"
            )

    def test_formula_not_theoretically_derived(self):
        """Formula is NOT marked THEORETICALLY_DERIVED (no rigorous derivation)."""
        candidates = get_all_closure_candidates()

        for candidate in candidates:
            assert candidate.status != ClosureStatus.THEORETICALLY_DERIVED, (
                f"{candidate.name} should NOT be THEORETICALLY_DERIVED (heuristic scaling)"
            )
