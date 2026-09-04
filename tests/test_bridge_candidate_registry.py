"""Tests for bridge candidate registry — enforce zero source-supported bridges."""

from src.bridge_candidate_registry import (
    BridgeStatus,
    CodePermission,
    get_all_bridge_candidates,
    get_bridge_status_summary,
    get_computational_reconstructions,
    get_dead_end_routes,
    get_mcmc_ready_bridges,
    get_priority_zero_question,
    get_source_supported_bridges,
    get_speculative_toy_models,
    is_mcmc_allowed,
    is_predictive_modeling_allowed,
)


class TestBridgeCandidatesExist:
    """Test that bridge candidates are documented."""

    def test_all_bridge_candidates_exist(self):
        """Six bridge routes evaluated (A, B, C, D, E, F)."""
        candidates = get_all_bridge_candidates()

        assert len(candidates) == 6, "Should have 6 bridge routes (A-F)"

    def test_route_names_correct(self):
        """All route names present."""
        candidates = get_all_bridge_candidates()
        route_names = [c.name for c in candidates]

        expected_routes = [
            "Route A: Newtonian Dust + Extra Forces",
            "Route B: Effective Stress-Energy Tensor",
            "Route C: Parametrized Friedmann (MGCAMB-style)",
            "Route D: Scalar Field / Dark Energy Map",
            "Route E: N-body → Fluid Backreaction",
            "Route F: PPN Extrapolation to Cosmology",
        ]

        for expected in expected_routes:
            assert expected in route_names, f"{expected} should be in bridge candidates"


class TestZeroSourceSupportedBridges:
    """Test that zero source-supported bridges found (critical blocker)."""

    def test_zero_source_supported(self):
        """No source-supported bridge routes found."""
        source_supported = get_source_supported_bridges()

        assert len(source_supported) == 0, (
            "Should have ZERO source-supported bridges (critical blocker)"
        )

    def test_all_non_source_supported_have_reason(self):
        """All non-source-supported bridges document why."""
        candidates = get_all_bridge_candidates()

        for candidate in candidates:
            if candidate.status != BridgeStatus.SOURCE_SUPPORTED:
                assert len(candidate.why_not_source_supported) > 0, (
                    f"{candidate.name} should document why not source-supported"
                )


class TestBridgeStatusClassification:
    """Test that bridge routes correctly classified."""

    def test_routes_a_and_c_are_computational_reconstructions(self):
        """Routes A and C are computational reconstructions."""
        reconstructions = get_computational_reconstructions()
        reconstruction_names = [r.name for r in reconstructions]

        assert len(reconstructions) == 2, "Should have 2 computational reconstructions"
        assert "Route A: Newtonian Dust + Extra Forces" in reconstruction_names
        assert "Route C: Parametrized Friedmann (MGCAMB-style)" in reconstruction_names

    def test_routes_b_d_e_are_speculative_toy_models(self):
        """Routes B, D, E are speculative toy models."""
        toy_models = get_speculative_toy_models()
        toy_model_names = [t.name for t in toy_models]

        assert len(toy_models) == 3, "Should have 3 speculative toy models"
        assert "Route B: Effective Stress-Energy Tensor" in toy_model_names
        assert "Route D: Scalar Field / Dark Energy Map" in toy_model_names
        assert "Route E: N-body → Fluid Backreaction" in toy_model_names

    def test_route_f_is_dead_end(self):
        """Route F (PPN extrapolation) is dead end."""
        dead_ends = get_dead_end_routes()

        assert len(dead_ends) == 1, "Should have 1 dead end route"
        assert dead_ends[0].name == "Route F: PPN Extrapolation to Cosmology"
        assert dead_ends[0].code_permission == CodePermission.NOT_ALLOWED


class TestMCMCBlocked:
    """Test that MCMC is blocked (zero MCMC-ready bridges)."""

    def test_zero_mcmc_ready_bridges(self):
        """No MCMC-ready bridge routes."""
        mcmc_ready = get_mcmc_ready_bridges()

        assert len(mcmc_ready) == 0, "Should have ZERO MCMC-ready bridges"

    def test_is_mcmc_allowed_returns_false(self):
        """is_mcmc_allowed() returns False."""
        assert not is_mcmc_allowed(), "MCMC should be blocked (no source-supported routes)"

    def test_all_bridges_have_mcmc_ready_false(self):
        """All bridge candidates have mcmc_ready = False."""
        candidates = get_all_bridge_candidates()

        for candidate in candidates:
            assert not candidate.mcmc_ready, (
                f"{candidate.name} should have mcmc_ready=False (no source support)"
            )


class TestPredictiveModelingBlocked:
    """Test that predictive modeling is blocked."""

    def test_is_predictive_modeling_allowed_returns_false(self):
        """is_predictive_modeling_allowed() returns False."""
        assert not is_predictive_modeling_allowed(), "Predictive modeling should be blocked"

    def test_all_bridges_have_predictive_use_false(self):
        """All bridge candidates have predictive_use_allowed = False."""
        candidates = get_all_bridge_candidates()

        for candidate in candidates:
            assert not candidate.predictive_use_allowed, (
                f"{candidate.name} should have predictive_use_allowed=False"
            )


class TestPriorityZeroQuestion:
    """Test that Priority 0 question (Q0) exists."""

    def test_priority_zero_question_exists(self):
        """Q0 exists and is about F_oP → H(z) mapping."""
        q0 = get_priority_zero_question()

        assert q0.question_id == "Q0", "Priority 0 question should have ID Q0"
        assert "F_oP" in q0.question_text, "Q0 should mention F_oP (pairwise force)"
        assert "H(z)" in q0.question_text, "Q0 should mention H(z) (expansion rate)"
        assert q0.priority == "CRITICAL", "Q0 should be CRITICAL priority"

    def test_all_non_dead_end_bridges_need_q0(self):
        """All non-dead-end bridges require Q0 clarification."""
        candidates = get_all_bridge_candidates()

        for candidate in candidates:
            if candidate.status != BridgeStatus.DEAD_END:
                author_questions = [q.question_id for q in candidate.author_clarification_needed]
                assert "Q0" in author_questions, f"{candidate.name} should require Q0 clarification"


class TestCodePermissions:
    """Test that code permissions are correctly assigned."""

    def test_route_a_toy_model_only(self):
        """Route A (Newtonian dust) is toy model only."""
        route_a = next((c for c in get_all_bridge_candidates() if "Newtonian Dust" in c.name), None)

        assert route_a is not None
        assert route_a.code_permission == CodePermission.ALLOWED_FOR_TOY_MODEL_ONLY

    def test_route_c_fit_reproduction_only(self):
        """Route C (parametrized Friedmann) is fit reproduction only."""
        route_c = next(
            (c for c in get_all_bridge_candidates() if "Parametrized Friedmann" in c.name), None
        )

        assert route_c is not None
        assert route_c.code_permission == CodePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY

    def test_routes_b_d_speculative_exploration(self):
        """Routes B and D allow speculative exploration."""
        route_b = next((c for c in get_all_bridge_candidates() if "Stress-Energy" in c.name), None)
        route_d = next((c for c in get_all_bridge_candidates() if "Scalar Field" in c.name), None)

        assert route_b is not None
        assert route_b.code_permission == CodePermission.ALLOWED_FOR_SPECULATIVE_EXPLORATION

        assert route_d is not None
        assert route_d.code_permission == CodePermission.ALLOWED_FOR_SPECULATIVE_EXPLORATION

    def test_route_e_computational_research(self):
        """Route E (N-body backreaction) is computational research."""
        route_e = next((c for c in get_all_bridge_candidates() if "N-body" in c.name), None)

        assert route_e is not None
        assert route_e.code_permission == CodePermission.ALLOWED_FOR_COMPUTATIONAL_RESEARCH

    def test_route_f_not_allowed(self):
        """Route F (PPN extrapolation) is not allowed."""
        route_f = next(
            (c for c in get_all_bridge_candidates() if "PPN Extrapolation" in c.name), None
        )

        assert route_f is not None
        assert route_f.code_permission == CodePermission.NOT_ALLOWED


class TestCriticalNuances:
    """Test that critical nuances are documented."""

    def test_route_a_has_averaging_nuance(self):
        """Route A documents standard averaging limitation."""
        route_a = next((c for c in get_all_bridge_candidates() if "Newtonian Dust" in c.name), None)

        assert route_a is not None
        nuance_lower = route_a.critical_nuance.lower()
        assert "averaging" in nuance_lower, "Route A should mention averaging"
        assert "not a refutation" in nuance_lower or "not refut" in nuance_lower, (
            "Route A should clarify this is NOT a refutation"
        )

    def test_route_f_has_regime_nuance(self):
        """Route F documents wrong regime issue."""
        route_f = next(
            (c for c in get_all_bridge_candidates() if "PPN Extrapolation" in c.name), None
        )

        assert route_f is not None
        nuance_lower = route_f.critical_nuance.lower()
        assert "weak-field" in nuance_lower or "regime" in nuance_lower
        assert "cosmology" in nuance_lower or "cosmological" in nuance_lower


class TestNoForwardModelFunction:
    """Test that no forward model function exists (intentional)."""

    def test_no_function_named_forward_model_exists(self):
        """No function named H_MULT, forward_model, or compute_expansion_rate exists."""
        import src.bridge_candidate_registry as module

        forbidden_names = [
            "H_MULT",
            "forward_model",
            "build_friedmann_equation",
            "compute_expansion_rate",
        ]

        for name in forbidden_names:
            assert not hasattr(module, name), (
                f"Function {name} should NOT exist (no source-supported bridge)"
            )


class TestStatusSummary:
    """Test bridge status summary function."""

    def test_status_summary_has_required_keys(self):
        """Status summary contains all required keys."""
        summary = get_bridge_status_summary()

        required_keys = [
            "total_routes",
            "source_supported",
            "computational_reconstructions",
            "speculative_toy_models",
            "dead_ends",
            "mcmc_ready",
            "priority_zero_question",
            "critical_blocker",
            "safe_conclusion",
        ]

        for key in required_keys:
            assert key in summary, f"Summary should contain key '{key}'"

    def test_summary_says_zero_source_supported(self):
        """Summary states zero source-supported bridges."""
        summary = get_bridge_status_summary()

        assert "0 found" in summary["source_supported"], "Summary should state 0 source-supported"

    def test_summary_says_mcmc_blocked(self):
        """Summary states MCMC is blocked."""
        summary = get_bridge_status_summary()

        assert "0 routes" in summary["mcmc_ready"] or "BLOCKED" in summary["mcmc_ready"], (
            "Summary should state MCMC blocked"
        )

    def test_summary_mentions_q0(self):
        """Summary mentions Q0 as priority zero question."""
        summary = get_bridge_status_summary()

        assert summary["priority_zero_question"] == "Q0", "Summary should reference Q0"


class TestSafeWording:
    """Test that safe wording is used (no refutation claims)."""

    def test_no_bridge_uses_refute_language(self):
        """No bridge candidate uses 'refute', 'refuted', 'wrong', 'impossible'."""
        candidates = get_all_bridge_candidates()

        forbidden_words = ["refute", "refuted", "wrong", "impossible", "disprove", "kill"]

        for candidate in candidates:
            combined_text = (
                candidate.critical_nuance
                + " "
                + candidate.why_not_source_supported
                + " "
                + " ".join(candidate.assumptions)
            ).lower()

            for word in forbidden_words:
                assert word not in combined_text or "not a refutation" in combined_text, (
                    f"{candidate.name} should avoid '{word}' or clarify 'not a refutation'"
                )

    def test_summary_uses_safe_language(self):
        """Summary uses safe language (clarification, blocker, not refutation)."""
        summary = get_bridge_status_summary()

        safe_conclusion = summary["safe_conclusion"].lower()
        critical_blocker = summary["critical_blocker"].lower()

        # Safe words should be present
        assert "clarification" in critical_blocker or "interpretation" in safe_conclusion

        # Unsafe words should be absent
        forbidden_words = ["refute", "wrong", "impossible", "disprove"]
        for word in forbidden_words:
            assert word not in safe_conclusion, f"Summary should not contain '{word}'"
            assert word not in critical_blocker, f"Blocker text should not contain '{word}'"
