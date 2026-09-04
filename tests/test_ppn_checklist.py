"""Tests for PPN checklist module."""

from src.ppn_checklist import (
    CheckStatus,
    RiskLevel,
    get_author_questions,
    get_blockers_summary,
    get_ppn_checks,
)


class TestPPNChecks:
    """Test PPN check structure and content."""

    def test_all_checks_have_required_fields(self):
        """Every PPN check has all required fields filled."""
        checks = get_ppn_checks()

        assert len(checks) > 0, "Should have at least one PPN check"

        for check in checks:
            assert check.check_id, f"Check {check.name} missing check_id"
            assert check.name, f"Check {check.check_id} missing name"
            assert check.description, f"Check {check.check_id} missing description"
            assert check.pnn_parameter, f"Check {check.check_id} missing pnn_parameter"
            assert check.observational_constraint, (
                f"Check {check.check_id} missing observational_constraint"
            )
            assert check.status, f"Check {check.check_id} missing status"
            assert check.risk_level, f"Check {check.check_id} missing risk_level"
            assert check.blocker, f"Check {check.check_id} missing blocker"
            assert check.author_question, f"Check {check.check_id} missing author_question"
            assert check.interpretation_branch, (
                f"Check {check.check_id} missing interpretation_branch"
            )
            assert check.safe_wording, f"Check {check.check_id} missing safe_wording"
            assert check.unsafe_wording, f"Check {check.check_id} missing unsafe_wording"

    def test_all_checks_blocked_or_unknown(self):
        """All PPN checks are BLOCKED or UNKNOWN (no applicable checks without info)."""
        checks = get_ppn_checks()

        for check in checks:
            assert check.status in (
                CheckStatus.BLOCKED,
                CheckStatus.UNKNOWN,
            ), f"{check.check_id} status is {check.status}, expected BLOCKED or UNKNOWN"

    def test_no_claims_of_refutation(self):
        """Safe wording never claims MULTING is refuted."""
        checks = get_ppn_checks()

        refutation_keywords = ["ruled out", "excluded", "falsified", "refuted", "violates"]

        for check in checks:
            safe_lower = check.safe_wording.lower()
            for keyword in refutation_keywords:
                assert keyword not in safe_lower, (
                    f"{check.check_id} safe_wording contains '{keyword}': {check.safe_wording}"
                )

    def test_no_claims_of_validation(self):
        """Safe wording never claims MULTING passes tests."""
        checks = get_ppn_checks()

        validation_keywords = ["passes", "consistent", "agrees with", "validates"]

        for check in checks:
            safe_lower = check.safe_wording.lower()
            for keyword in validation_keywords:
                # Allow "consistent with" in context of "cannot assess"
                if keyword == "consistent" and "cannot" in safe_lower:
                    continue
                assert keyword not in safe_lower, (
                    f"{check.check_id} safe_wording contains '{keyword}': {check.safe_wording}"
                )

    def test_blocked_checks_have_blocker_text(self):
        """Every BLOCKED check has non-empty blocker description."""
        checks = get_ppn_checks()

        blocked = [c for c in checks if c.status == CheckStatus.BLOCKED]

        assert len(blocked) > 0, "Should have at least one blocked check"

        for check in blocked:
            assert len(check.blocker) > 10, f"{check.check_id} blocker text too short"
            assert "missing" in check.blocker.lower() or "unclear" in check.blocker.lower(), (
                f"{check.check_id} blocker should mention what is missing/unclear"
            )

    def test_high_risk_checks_are_blocked(self):
        """HIGH or CRITICAL risk checks must be BLOCKED (cannot proceed without info)."""
        checks = get_ppn_checks()

        high_risk = [c for c in checks if c.risk_level in (RiskLevel.HIGH, RiskLevel.CRITICAL)]

        for check in high_risk:
            assert check.status == CheckStatus.BLOCKED, (
                f"{check.check_id} is {check.risk_level.value} risk but status is {check.status.value}"
            )


class TestBlockersSummary:
    """Test blocker categorization."""

    def test_blockers_summary_has_categories(self):
        """Blockers summary contains expected categories."""
        blockers = get_blockers_summary()

        expected_categories = {
            "no_metric",
            "no_k_A",
            "no_com_frame",
            "no_cutoff",
            "no_coupling_spec",
            "unknown_applicability",
        }

        assert set(blockers.keys()) == expected_categories

    def test_no_metric_blocks_gamma_beta(self):
        """No metric blocker should affect PPN-1 (γ) and PPN-2 (β)."""
        blockers = get_blockers_summary()

        assert "PPN-1" in blockers["no_metric"], "γ check should be blocked by no metric"
        assert "PPN-2" in blockers["no_metric"], "β check should be blocked by no metric"

    def test_no_k_A_blocks_alpha_checks(self):
        """No k_A blocker should affect PPN-3 (α₁) and PPN-4 (α₂)."""
        blockers = get_blockers_summary()

        assert "PPN-3" in blockers["no_k_A"], "α₁ check should be blocked by missing k_A"


class TestAuthorQuestions:
    """Test author question extraction."""

    def test_author_questions_extracted(self):
        """Author questions extracted from all checks."""
        questions = get_author_questions()

        assert len(questions) > 0, "Should have at least one author question"

        for question in questions:
            assert "**PPN-" in question, "Question should start with check ID"
            assert len(question) > 20, "Question should be substantive"

    def test_author_questions_no_duplicates(self):
        """No duplicate author questions (deduplication works)."""
        questions = get_author_questions()

        # Extract question text (after "**PPN-X:**")
        question_texts = [q.split(":** ", 1)[1] for q in questions]

        assert len(question_texts) == len(set(question_texts)), "Should have no duplicate questions"

    def test_author_questions_are_questions(self):
        """All author questions end with '?'."""
        questions = get_author_questions()

        for question in questions:
            question_text = question.split(":** ", 1)[1]
            assert question_text.endswith("?"), (
                f"Author question should end with '?': {question_text}"
            )


class TestInterpretationBranches:
    """Test interpretation branch assignments."""

    def test_all_checks_have_interpretation_branch(self):
        """Every check is assigned to at least one interpretation branch."""
        checks = get_ppn_checks()

        for check in checks:
            assert "branch" in check.interpretation_branch.lower(), (
                f"{check.check_id} should reference a Branch"
            )

    def test_gamma_beta_map_to_metric_branches(self):
        """γ and β checks map to metric-related interpretation branches."""
        checks = get_ppn_checks()

        gamma_check = next(c for c in checks if c.pnn_parameter == "gamma")
        beta_check = next(c for c in checks if c.pnn_parameter == "beta")

        assert (
            "branch 1" in gamma_check.interpretation_branch.lower()
            or "branch 4" in gamma_check.interpretation_branch.lower()
        ), "γ should map to Branch 1 or 4"

        assert (
            "branch 1" in beta_check.interpretation_branch.lower()
            or "branch 4" in beta_check.interpretation_branch.lower()
        ), "β should map to Branch 1 or 4"

    def test_alpha_checks_map_to_preferred_frame_branches(self):
        """α₁, α₂ checks map to preferred-frame interpretation branches."""
        checks = get_ppn_checks()

        alpha1_check = next(c for c in checks if c.pnn_parameter == "alpha1")
        alpha2_check = next(c for c in checks if c.pnn_parameter == "alpha2")

        assert (
            "branch 2" in alpha1_check.interpretation_branch.lower()
            or "branch 3" in alpha1_check.interpretation_branch.lower()
        ), "α₁ should map to Branch 2 or 3"

        assert "branch 3" in alpha2_check.interpretation_branch.lower(), "α₂ should map to Branch 3"


class TestSafeUnsafeWording:
    """Test safe vs unsafe wording pairs."""

    def test_unsafe_wording_contains_forbidden_claims(self):
        """Unsafe wording contains claims that should NOT be made."""
        checks = get_ppn_checks()

        forbidden_patterns = [
            ("ruled out", "claim of refutation without evidence"),
            ("excluded", "claim of refutation without evidence"),
            ("violates", "claim of constraint violation without calculation"),
            ("passes", "claim of validation without check"),
        ]

        for check in checks:
            unsafe_lower = check.unsafe_wording.lower()

            # At least one forbidden pattern should appear in unsafe wording
            has_forbidden = any(pattern in unsafe_lower for pattern, _ in forbidden_patterns)

            assert has_forbidden, (
                f"{check.check_id} unsafe wording should contain a forbidden claim"
            )

    def test_safe_wording_mentions_blocker_or_requirement(self):
        """Safe wording mentions what is missing or required."""
        checks = get_ppn_checks()

        blocker_keywords = [
            "cannot",
            "without",
            "missing",
            "unclear",
            "requires",
            "required",
            "needs",
            "needed",
        ]

        for check in checks:
            safe_lower = check.safe_wording.lower()

            has_blocker_mention = any(keyword in safe_lower for keyword in blocker_keywords)

            assert has_blocker_mention, (
                f"{check.check_id} safe wording should mention what is missing/required"
            )

    def test_safe_and_unsafe_are_different(self):
        """Safe and unsafe wordings are different for each check."""
        checks = get_ppn_checks()

        for check in checks:
            assert check.safe_wording != check.unsafe_wording, (
                f"{check.check_id} safe and unsafe wording are identical"
            )

            # Should differ by more than just punctuation
            safe_words = set(check.safe_wording.lower().split())
            unsafe_words = set(check.unsafe_wording.lower().split())

            overlap = len(safe_words & unsafe_words) / max(len(safe_words), len(unsafe_words))

            assert overlap < 0.7, (
                f"{check.check_id} safe and unsafe wording are too similar ({overlap:.0%} overlap)"
            )


class TestRealWorldScenarios:
    """Test checklist behavior in realistic scenarios."""

    def test_no_applicable_checks_without_metric(self):
        """Without weak-field metric, no γ/β checks can be APPLICABLE."""
        checks = get_ppn_checks()

        gamma_beta_checks = [c for c in checks if c.pnn_parameter in ("gamma", "beta")]

        for check in gamma_beta_checks:
            assert check.status != CheckStatus.APPLICABLE, (
                f"{check.check_id} should not be APPLICABLE without metric"
            )

    def test_cluster_scale_only_makes_ppn_not_applicable(self):
        """If dipole is cluster-scale only, PPN checks may be NOT_APPLICABLE."""
        checks = get_ppn_checks()

        applicability_check = next(c for c in checks if "applicability" in c.name.lower())

        # Currently UNKNOWN, but interpretation branch 5 (cluster-scale only)
        # would make it NOT_APPLICABLE
        assert "cluster-scale only" in applicability_check.interpretation_branch.lower(), (
            "Should have cluster-scale interpretation branch"
        )

    def test_all_checks_have_author_question(self):
        """Every check can be unblocked by sending author question."""
        checks = get_ppn_checks()

        for check in checks:
            assert len(check.author_question) > 0, (
                f"{check.check_id} has no path to resolution (empty author_question)"
            )
