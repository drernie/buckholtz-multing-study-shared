"""Tests for minimum viable bridge (MVB) registry — enforce research hypothesis status."""

from src.minimum_viable_bridge_registry import (
    MVBCandidate,
    RequiredInput,
    RiskItem,
    get_minimum_author_question,
    get_mvb_candidate,
    get_mvb_status_summary,
    is_mcmc_allowed,
    is_mvb_source_supported,
    is_prediction_allowed,
)


class TestMVBCandidateExists:
    """Test that MVB candidate is documented."""

    def test_mvb_candidate_exists(self):
        """MVB candidate exists and is discrete lattice + virial route."""
        mvb = get_mvb_candidate()

        assert isinstance(mvb, MVBCandidate), "MVB should be MVBCandidate dataclass"
        assert "lattice" in mvb.name.lower(), "MVB name should mention lattice"
        assert "virial" in mvb.name.lower(), "MVB name should mention virial"

    def test_mvb_route_description(self):
        """MVB route description mentions key components."""
        mvb = get_mvb_candidate()

        route_lower = mvb.route_description.lower()
        assert "pairwise force" in route_lower or "f_op" in route_lower
        assert "lattice" in route_lower
        assert "virial" in route_lower
        assert "friedmann" in route_lower
        assert "h(z)" in route_lower


class TestMVBNotSourceSupported:
    """Test that MVB is not source-supported (critical constraint)."""

    def test_mvb_not_source_supported(self):
        """MVB is not source-supported."""
        assert not is_mvb_source_supported(), "MVB should NOT be source-supported"

    def test_mvb_status_is_research_hypothesis(self):
        """MVB status is RESEARCH_HYPOTHESIS."""
        mvb = get_mvb_candidate()

        assert mvb.status == "RESEARCH_HYPOTHESIS", "MVB status should be RESEARCH_HYPOTHESIS"

    def test_mvb_source_supported_field_false(self):
        """MVB source_supported field is False."""
        mvb = get_mvb_candidate()

        assert mvb.source_supported is False, "MVB source_supported should be False"


class TestMCMCBlocked:
    """Test that MCMC is blocked for MVB route."""

    def test_is_mcmc_allowed_returns_false(self):
        """is_mcmc_allowed() returns False."""
        assert not is_mcmc_allowed(), "MCMC should be blocked for MVB (not source-confirmed)"

    def test_mvb_mcmc_ready_false(self):
        """MVB mcmc_ready field is False."""
        mvb = get_mvb_candidate()

        assert mvb.mcmc_ready is False, "MVB mcmc_ready should be False"


class TestPredictionBlocked:
    """Test that prediction is blocked for MVB route."""

    def test_is_prediction_allowed_returns_false(self):
        """is_prediction_allowed() returns False."""
        assert not is_prediction_allowed(), "Prediction should be blocked for MVB"

    def test_mvb_prediction_allowed_false(self):
        """MVB prediction_allowed field is False."""
        mvb = get_mvb_candidate()

        assert mvb.prediction_allowed is False, "MVB prediction_allowed should be False"


class TestRequiredInputs:
    """Test that required inputs are documented."""

    def test_mvb_has_required_inputs(self):
        """MVB has required inputs list."""
        mvb = get_mvb_candidate()

        assert len(mvb.required_inputs) > 0, "MVB should have required inputs"
        assert all(isinstance(inp, RequiredInput) for inp in mvb.required_inputs), (
            "All inputs should be RequiredInput instances"
        )

    def test_critical_inputs_present(self):
        """Critical inputs are present."""
        mvb = get_mvb_candidate()
        input_names = [inp.input_name.lower() for inp in mvb.required_inputs]

        # Check for lattice geometry, neighbor count, cell volume, neighbor distance
        assert any("lattice" in name or "geometry" in name for name in input_names)
        assert any("neighbor" in name and "count" in name for name in input_names)
        assert any("volume" in name for name in input_names)
        assert any("distance" in name for name in input_names)

    def test_all_inputs_have_priority(self):
        """All required inputs have priority assigned."""
        mvb = get_mvb_candidate()

        for inp in mvb.required_inputs:
            assert inp.priority in [
                "CRITICAL",
                "HIGH",
                "MEDIUM",
                "LOW",
            ], f"Input {inp.input_id} should have valid priority"


class TestRisksDocumented:
    """Test that risks are documented."""

    def test_mvb_has_risks(self):
        """MVB has risks list."""
        mvb = get_mvb_candidate()

        assert len(mvb.risks) > 0, "MVB should have risks documented"
        assert all(isinstance(risk, RiskItem) for risk in mvb.risks), (
            "All risks should be RiskItem instances"
        )

    def test_critical_risk_present(self):
        """Critical risk about not being Buckholtz model is present."""
        mvb = get_mvb_candidate()
        risk_descriptions = [risk.risk_description.lower() for risk in mvb.risks]

        assert any("our model" in desc or "buckholtz" in desc for desc in risk_descriptions), (
            "Should document risk of MVB becoming 'our model' not Buckholtz's"
        )

    def test_all_risks_have_severity(self):
        """All risks have severity assigned."""
        mvb = get_mvb_candidate()

        for risk in mvb.risks:
            assert risk.severity in [
                "CRITICAL",
                "HIGH",
                "MEDIUM",
                "LOW",
            ], f"Risk {risk.risk_id} should have valid severity"

    def test_all_risks_have_mitigation(self):
        """All risks have mitigation strategy."""
        mvb = get_mvb_candidate()

        for risk in mvb.risks:
            assert len(risk.mitigation) > 0, f"Risk {risk.risk_id} should have mitigation strategy"


class TestAuthorClarification:
    """Test that author clarification question is documented."""

    def test_author_question_exists(self):
        """Author clarification question exists."""
        q_mvb = get_minimum_author_question()

        assert q_mvb.question_id == "Q_MVB", "Author question should have ID Q_MVB"
        assert q_mvb.priority == "CRITICAL", "Q_MVB should be CRITICAL priority"

    def test_author_question_mentions_mvb_components(self):
        """Author question mentions MVB components."""
        q_mvb = get_minimum_author_question()
        question_lower = q_mvb.question_text.lower()

        assert "lattice" in question_lower or "discrete" in question_lower
        assert "virial" in question_lower or "pressure" in question_lower
        assert "h(z)" in question_lower or "expansion" in question_lower

    def test_mvb_has_author_clarification_field(self):
        """MVB has author_clarification field."""
        mvb = get_mvb_candidate()

        assert mvb.author_clarification.question_id == "Q_MVB"


class TestSafeWording:
    """Test that safe/unsafe wording is documented."""

    def test_mvb_has_safe_wording(self):
        """MVB has safe wording documented."""
        mvb = get_mvb_candidate()

        assert len(mvb.safe_wording) > 0, "MVB should have safe wording examples"
        safe_lower = mvb.safe_wording.lower()
        assert "candidate" in safe_lower or "hypothesis" in safe_lower

    def test_mvb_has_unsafe_wording(self):
        """MVB has unsafe wording documented."""
        mvb = get_mvb_candidate()

        assert len(mvb.unsafe_wording) > 0, "MVB should have unsafe wording examples"
        unsafe_lower = mvb.unsafe_wording.lower()
        assert "unsafe" in unsafe_lower

    def test_no_unsafe_claims_in_route_description(self):
        """MVB route description does not use unsafe wording."""
        mvb = get_mvb_candidate()
        route_lower = mvb.route_description.lower()

        forbidden_words = ["proves", "validates", "solves", "only viable"]
        for word in forbidden_words:
            assert word not in route_lower, f"Route description should not contain '{word}'"


class TestNoForwardModelFunction:
    """Test that no forward model function exists (intentional)."""

    def test_no_forward_model_functions_exist(self):
        """No forward model functions exist in MVB registry."""
        import src.minimum_viable_bridge_registry as module

        forbidden_names = [
            "H_MVB",
            "forward_model_mvb",
            "build_virial_pressure",
            "compute_effective_fluid",
            "compute_H_MULTING",
        ]

        for name in forbidden_names:
            assert not hasattr(module, name), (
                f"Function {name} should NOT exist (MVB not source-confirmed)"
            )


class TestStatusSummary:
    """Test MVB status summary function."""

    def test_status_summary_has_required_keys(self):
        """Status summary contains required keys."""
        summary = get_mvb_status_summary()

        required_keys = [
            "route_name",
            "status",
            "source_supported",
            "mcmc_ready",
            "prediction_allowed",
            "required_inputs_count",
            "risks_count",
            "author_question",
            "critical_blocker",
            "safe_conclusion",
        ]

        for key in required_keys:
            assert key in summary, f"Summary should contain key '{key}'"

    def test_summary_says_not_source_supported(self):
        """Summary states MVB is not source-supported."""
        summary = get_mvb_status_summary()

        assert "NOT" in summary["source_supported"] or "False" in summary["source_supported"]

    def test_summary_says_mcmc_blocked(self):
        """Summary states MCMC is blocked."""
        summary = get_mvb_status_summary()

        assert "BLOCKED" in summary["mcmc_ready"] or "False" in summary["mcmc_ready"]

    def test_summary_mentions_q_mvb(self):
        """Summary mentions Q_MVB as author question."""
        summary = get_mvb_status_summary()

        assert summary["author_question"] == "Q_MVB"

    def test_summary_uses_safe_language(self):
        """Summary uses safe language (candidate, hypothesis, reconstruction)."""
        summary = get_mvb_status_summary()

        safe_conclusion = summary["safe_conclusion"].lower()
        critical_blocker = summary["critical_blocker"].lower()

        # Safe words should be present
        assert (
            "candidate" in safe_conclusion
            or "hypothesis" in critical_blocker
            or "reconstruction" in critical_blocker
        )

        # Unsafe words should be absent
        forbidden_words = ["proves", "validates", "solves", "only viable"]
        for word in forbidden_words:
            assert word not in safe_conclusion, f"Summary should not contain '{word}'"
            assert word not in critical_blocker, f"Blocker should not contain '{word}'"
