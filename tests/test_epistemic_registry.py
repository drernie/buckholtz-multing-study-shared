"""
Test epistemic registry invariants.

Purpose: Ensure claims, parameters, and equations follow status discipline.
"""

import pytest

from src.epistemic_registry import Claim, EquationRecord, Parameter, SourceRef


def test_claim_marked_fact_requires_source():
    """Claims marked as 'fact' must have a source."""
    source = SourceRef(id="test_source", title="Test Source", location="Test location")

    # Should succeed
    claim_with_source = Claim(
        id="test_claim_1",
        text="Test claim with source",
        status="fact",
        source=source,
        testable=True,
        failure_condition="Test failure",
    )
    assert claim_with_source.source is not None

    # Should fail
    with pytest.raises(ValueError, match="marked as 'fact' but has no source"):
        Claim(
            id="test_claim_2",
            text="Test claim without source",
            status="fact",
            source=None,  # Missing source!
            testable=True,
            failure_condition="Test failure",
        )


def test_claim_hypothesis_can_have_no_source():
    """Claims marked as 'hypothesis' may have no source."""
    claim = Claim(
        id="test_hypothesis",
        text="Test hypothesis",
        status="hypothesis",
        source=None,  # OK for hypothesis
        testable=True,
        failure_condition="Test failure",
    )
    assert claim.status == "hypothesis"


def test_parameter_marked_fact_with_value_requires_source():
    """Parameters marked as 'fact' with a value must have a source."""
    source = SourceRef(id="test_source", title="Test Source", location="Test location")

    # Should succeed
    param_with_source = Parameter(
        name="Test parameter",
        symbol="x",
        value=1.0,
        units="m",
        status="fact",
        source=source,
        interpretation="Test interpretation",
    )
    assert param_with_source.source is not None

    # Should fail
    with pytest.raises(ValueError, match="has a value and status 'fact'.*but no source"):
        Parameter(
            name="Test parameter 2",
            symbol="y",
            value=2.0,
            units="m",
            status="fact",
            source=None,  # Missing source!
            interpretation="Test interpretation",
        )


def test_parameter_fact_with_no_value_allowed():
    """Parameter marked 'fact' but value=None is allowed (definition exists, value TBD)."""
    param = Parameter(
        name="Test parameter no value",
        symbol="z",
        value=None,  # No value yet
        units="m",
        status="fact",
        source=None,  # OK when value is None
        interpretation="Defined but value not measured yet",
    )
    assert param.value is None


def test_equation_with_source_verification_status_allowed():
    """Equations can have 'requires_source_verification' status."""
    eq = EquationRecord(
        id="test_eq",
        label="Test Eq",
        expression_text="x = y + z",
        symbols=["x", "y", "z"],
        status="requires_source_verification",
        source=None,  # OK for this status
        dimensional_status="not_checked",
    )
    assert eq.status == "requires_source_verification"


def test_equation_with_other_status_requires_source():
    """Equations with status other than 'requires_source_verification' need source."""
    source = SourceRef(id="test_source", title="Test Source", location="Test location")

    # Should succeed
    eq_with_source = EquationRecord(
        id="test_eq_1",
        label="Test Eq 1",
        expression_text="a = b + c",
        symbols=["a", "b", "c"],
        status="calculation",
        source=source,
        dimensional_status="passed",
    )
    assert eq_with_source.source is not None

    # Should fail
    with pytest.raises(ValueError, match="has status.*but no source"):
        EquationRecord(
            id="test_eq_2",
            label="Test Eq 2",
            expression_text="d = e + f",
            symbols=["d", "e", "f"],
            status="calculation",  # Not a placeholder status
            source=None,  # Missing source!
            dimensional_status="not_checked",
        )


def test_source_ref_has_required_fields():
    """SourceRef must have id, title, and location."""
    source = SourceRef(id="test", title="Test Title", location="Test Location")
    assert source.id == "test"
    assert source.title == "Test Title"
    assert source.location == "Test Location"


def test_dimensional_status_values():
    """Test that dimensional_status has valid values."""
    valid_statuses = ["not_checked", "passed", "failed", "requires_clarification"]

    source = SourceRef(id="s", title="T", location="L")

    for status in valid_statuses:
        eq = EquationRecord(
            id=f"eq_{status}",
            label=f"Eq {status}",
            expression_text="test",
            symbols=[],
            status="calculation",
            source=source,
            dimensional_status=status,
        )
        assert eq.dimensional_status == status
