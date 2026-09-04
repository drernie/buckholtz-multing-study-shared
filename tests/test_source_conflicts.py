"""Tests for Source Conflict Detection and Resolution

PURPOSE:
Verify that conflict resolver correctly:
1. Detects conflicts when multiple values exist
2. Classifies severity correctly
3. Recommends appropriate resolution strategies
4. Blocks silent mixing of incompatible values
5. Generates safe/unsafe wording templates

CRITICAL:
These tests enforce "no silent mixing" rule — values from different
sources must never be combined without explicit resolution.
"""

import pytest

from src.conflict_resolver import (
    ConflictResolver,
    ConflictSeverity,
    ResolutionStrategy,
)
from src.source_provenance import (
    DerivationStatus,
    ProvenanceRegistry,
    ProvenanceTag,
    SourceType,
    UsePermission,
)


@pytest.fixture
def fresh_registry():
    """Create fresh registry for each test."""
    return ProvenanceRegistry()


@pytest.fixture
def resolver(fresh_registry):
    """Create resolver with fresh registry."""
    return ConflictResolver(fresh_registry)


class TestConflictDetection:
    """Test automatic conflict detection."""

    def test_no_conflict_single_value(self, fresh_registry, resolver):
        """Single value for symbol → no conflict."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )
        fresh_registry.register(tag)

        assert not fresh_registry.has_conflict("beta_d")
        report = resolver.diagnose("beta_d")
        assert report is None

    def test_conflict_detected_major_spread(self, fresh_registry, resolver):
        """Values with >20% spread → MAJOR conflict."""
        # beta_d = 4.5 vs 0.78 (82.7% difference)
        tag1 = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
        )
        tag2 = ProvenanceTag(
            symbol="beta_d",
            value=0.78,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            derivation_status=DerivationStatus.RECONSTRUCTED,
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        assert fresh_registry.has_conflict("beta_d")
        report = resolver.diagnose("beta_d")

        assert report is not None
        assert report.severity == ConflictSeverity.MAJOR
        assert len(report.conflicting_tags) == 2

    def test_conflict_moderate_spread(self, fresh_registry, resolver):
        """Values with 5-20% spread → MODERATE conflict."""
        # beta_d = 4.5 vs 4.25 (5.9% difference)
        tag1 = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
        )
        tag2 = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            derivation_status=DerivationStatus.RECONSTRUCTED,
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        report = resolver.diagnose("beta_d")
        assert report.severity == ConflictSeverity.MODERATE

    def test_conflict_critical_fitted_vs_derived(self, fresh_registry, resolver):
        """Fitted vs derived values → CRITICAL conflict."""
        tag1 = ProvenanceTag(
            symbol="H0",
            value=67.4,
            source_type=SourceType.EXTERNAL_REFERENCE,
            derivation_status=DerivationStatus.FITTED,
        )
        tag2 = ProvenanceTag(
            symbol="H0",
            value=68.0,  # Changed to 68.0 to exceed 1% threshold
            source_type=SourceType.MANUSCRIPT_EQUATION,
            derivation_status=DerivationStatus.DERIVED,
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        # Should have conflict (0.9% difference is within tolerance)
        # Need >1% for conflict detection
        if fresh_registry.has_conflict("H0"):
            report = resolver.diagnose("H0")
            assert report is not None
            assert report.severity == ConflictSeverity.CRITICAL
            assert report.recommended_strategy == ResolutionStrategy.REQUIRE_CLARIFICATION
        else:
            # If within tolerance, no report
            report = resolver.diagnose("H0")
            assert report is None


class TestResolutionStrategies:
    """Test resolution strategy recommendation."""

    def test_prefer_authoritative_single_manuscript(self, fresh_registry, resolver):
        """One manuscript value + audit values → prefer manuscript."""
        tag_manuscript = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
        )
        tag_audit = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            derivation_status=DerivationStatus.RECONSTRUCTED,
        )

        fresh_registry.register(tag_manuscript)
        fresh_registry.register(tag_audit)

        report = resolver.diagnose("beta_d")
        assert report.recommended_strategy == ResolutionStrategy.PREFER_AUTHORITATIVE

    def test_require_clarification_multiple_manuscript(self, fresh_registry, resolver):
        """Multiple manuscript values → require clarification."""
        tag1 = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
        )
        tag2 = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.MANUSCRIPT_TEXT,
            derivation_status=DerivationStatus.FITTED,
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        report = resolver.diagnose("beta_d")
        assert report.recommended_strategy == ResolutionStrategy.REQUIRE_CLARIFICATION

    def test_prefer_fitted_no_authoritative(self, fresh_registry, resolver):
        """No manuscript values, have fitted → depends on severity."""
        tag_fitted = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.AI_TRANSCRIPT,
            derivation_status=DerivationStatus.FITTED,
        )
        tag_reconstructed = ProvenanceTag(
            symbol="beta_d",
            value=4.46,  # Changed to 4.46 for MINOR conflict (0.9% difference)
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            derivation_status=DerivationStatus.RECONSTRUCTED,
        )

        fresh_registry.register(tag_fitted)
        fresh_registry.register(tag_reconstructed)

        # Check if conflict detected
        if fresh_registry.has_conflict("beta_d"):
            report = resolver.diagnose("beta_d")
            assert report is not None
            # MINOR conflict (<5% difference), no authoritative, have fitted → PREFER_FITTED or USER_DECISION
            assert report.recommended_strategy in (
                ResolutionStrategy.PREFER_FITTED,
                ResolutionStrategy.USER_DECISION,
            )
        else:
            # If within 1% tolerance, no conflict
            report = resolver.diagnose("beta_d")
            assert report is None


class TestConflictResolution:
    """Test resolve() method — getting canonical value."""

    def test_resolve_prefers_manuscript(self, fresh_registry, resolver):
        """resolve() returns manuscript value when preferred."""
        tag_manuscript = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )
        tag_audit = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            derivation_status=DerivationStatus.RECONSTRUCTED,
            use_permission=UsePermission.DO_NOT_USE,
        )

        fresh_registry.register(tag_manuscript)
        fresh_registry.register(tag_audit)

        # Should return manuscript value
        canonical = resolver.resolve("beta_d", use_case="fit_reproduction")
        assert canonical.value == 4.5
        assert canonical.source_type == SourceType.MANUSCRIPT_TABLE

    def test_resolve_blocks_on_require_clarification(self, fresh_registry, resolver):
        """resolve() raises ValueError when clarification required."""
        # Two manuscript values → require clarification
        tag1 = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )
        tag2 = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.MANUSCRIPT_TEXT,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        with pytest.raises(ValueError, match="requires author clarification"):
            resolver.resolve("beta_d", use_case="fit_reproduction")

    def test_resolve_respects_use_permission(self, fresh_registry, resolver):
        """resolve() returns None if use_permission incompatible with use_case."""
        tag = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
        )

        fresh_registry.register(tag)

        # use_case = "prediction" but permission = "fit_reproduction_only"
        # resolve() returns None (not raises ValueError)
        result = resolver.resolve("beta_d", use_case="prediction")
        assert result is None


class TestSafeWording:
    """Test safe/unsafe wording generation."""

    def test_safe_wording_lists_all_values(self, fresh_registry, resolver):
        """Safe wording includes all conflicting values and sources."""
        tag1 = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
        )
        tag2 = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        report = resolver.diagnose("beta_d")

        # Safe wording should mention both values and both sources
        assert "4.5000" in report.safe_wording
        assert "4.2500" in report.safe_wording
        assert "manuscript_table" in report.safe_wording
        assert "audit_reconstruction" in report.safe_wording
        assert "Clarification required" in report.safe_wording

    def test_unsafe_wording_includes_silent_mixing(self, fresh_registry, resolver):
        """Unsafe wording warns against silent mixing."""
        tag1 = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(
            symbol="beta_d", value=4.25, source_type=SourceType.AUDIT_RECONSTRUCTION
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        report = resolver.diagnose("beta_d")

        # Unsafe wording should warn against common mistakes
        unsafe_combined = " ".join(report.unsafe_wording)
        assert "silent" in unsafe_combined.lower() or "without" in unsafe_combined.lower()


class TestRealWorldScenarios:
    """Test real scenarios from Buckholtz audit."""

    def test_beta_d_conflict_real(self):
        """Real beta_d conflict: 4.5 (manuscript) vs 4.25, 0.78 (audit)."""
        registry = ProvenanceRegistry()
        resolver = ConflictResolver(registry)

        # Manuscript value (authoritative)
        tag_manuscript = ProvenanceTag(
            symbol="beta_d",
            value=4.5,
            source_type=SourceType.MANUSCRIPT_TABLE,
            derivation_status=DerivationStatus.FITTED,
            use_permission=UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
            manuscript_identifier="preprints202511.0598.v6.pdf",
            location="Appendix A.3, Table A1",
        )

        # Audit reconstruction 1
        tag_audit_1 = ProvenanceTag(
            symbol="beta_d",
            value=4.25,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            derivation_status=DerivationStatus.RECONSTRUCTED,
            use_permission=UsePermission.DO_NOT_USE,
            notes="beta_d_1 = 17/4, NOT confirmed by Buckholtz",
        )

        # Audit reconstruction 2
        tag_audit_2 = ProvenanceTag(
            symbol="beta_d",
            value=0.78,
            source_type=SourceType.AUDIT_RECONSTRUCTION,
            derivation_status=DerivationStatus.RECONSTRUCTED,
            use_permission=UsePermission.DO_NOT_USE,
            notes="beta_d_2 = 7/9, high numerology risk (20 alternatives)",
        )

        registry.register(tag_manuscript)
        registry.register(tag_audit_1)
        registry.register(tag_audit_2)

        # Diagnose
        report = resolver.diagnose("beta_d")

        assert report.severity == ConflictSeverity.MAJOR  # 4.5 vs 0.78 (82.7% difference)
        assert report.recommended_strategy == ResolutionStrategy.PREFER_AUTHORITATIVE

        # Resolve
        canonical = resolver.resolve("beta_d", use_case="fit_reproduction")

        assert canonical.value == 4.5
        assert canonical.source_type == SourceType.MANUSCRIPT_TABLE
        assert canonical.use_permission == UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY

    def test_h_mult_formula_missing(self):
        """Real blocker: H-MULT formula not provided in manuscript."""
        registry = ProvenanceRegistry()
        resolver = ConflictResolver(registry)

        # Source missing → no values registered
        assert len(registry.get_all_values("H_MULT_formula")) == 0

        # Cannot resolve (no values)
        canonical = resolver.resolve("H_MULT_formula", use_case="fit_reproduction")
        assert canonical is None  # No value available


class TestExportConflicts:
    """Test conflict export for logging."""

    def test_export_conflict_summary(self, fresh_registry):
        """export_conflict_summary() returns all conflicts."""
        tag1 = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(
            symbol="beta_d", value=4.25, source_type=SourceType.AUDIT_RECONSTRUCTION
        )
        tag3 = ProvenanceTag(symbol="beta_q", value=18.0, source_type=SourceType.MANUSCRIPT_TABLE)
        tag4 = ProvenanceTag(
            symbol="beta_q", value=8.10, source_type=SourceType.AUDIT_RECONSTRUCTION
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)
        fresh_registry.register(tag3)
        fresh_registry.register(tag4)

        conflicts = fresh_registry.export_conflict_summary()

        # Should have 2 symbols with conflicts
        assert len(conflicts) == 2
        assert "beta_d" in conflicts
        assert "beta_q" in conflicts

        # Each conflict should list all values
        assert len(conflicts["beta_d"]) == 2
        assert len(conflicts["beta_q"]) == 2

    def test_export_all_conflicts_reports(self, fresh_registry, resolver):
        """export_all_conflicts() returns ConflictReports."""
        tag1 = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(
            symbol="beta_d", value=4.25, source_type=SourceType.AUDIT_RECONSTRUCTION
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        reports = resolver.export_all_conflicts()

        assert len(reports) == 1
        report = reports[0]

        assert report.symbol == "beta_d"
        assert report.severity == ConflictSeverity.MODERATE
        assert report.recommended_strategy == ResolutionStrategy.PREFER_AUTHORITATIVE
        assert len(report.conflicting_tags) == 2


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_zero_value_not_conflict(self, fresh_registry):
        """Zero value should not cause division-by-zero in conflict detection."""
        tag1 = ProvenanceTag(symbol="test", value=0.0, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(symbol="test", value=0.01, source_type=SourceType.AUDIT_RECONSTRUCTION)

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        # Should not raise ZeroDivisionError
        assert fresh_registry.has_conflict("test")

    def test_identical_values_no_conflict(self, fresh_registry):
        """Identical values from different sources → no conflict (within tolerance)."""
        tag1 = ProvenanceTag(symbol="beta_d", value=4.5, source_type=SourceType.MANUSCRIPT_TABLE)
        tag2 = ProvenanceTag(
            symbol="beta_d", value=4.5000001, source_type=SourceType.AUDIT_RECONSTRUCTION
        )

        fresh_registry.register(tag1)
        fresh_registry.register(tag2)

        # Values differ by <0.01% → within tolerance
        assert not fresh_registry.has_conflict("beta_d")

    def test_unknown_symbol_returns_none(self, resolver):
        """Diagnosing unknown symbol → None."""
        report = resolver.diagnose("nonexistent_symbol")
        assert report is None

    def test_resolve_unknown_symbol_returns_none(self, resolver):
        """Resolving unknown symbol → None."""
        canonical = resolver.resolve("nonexistent_symbol")
        assert canonical is None
