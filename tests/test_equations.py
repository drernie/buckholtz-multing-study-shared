"""Smoke / characterization tests for the equation registry (was 0% covered).

Locks the key invariant: verified + unverified is a complete, disjoint partition
of all equations, keyed off the source-verification status.
"""

from src.equations import (
    get_all_equations,
    get_unverified_equations,
    get_verified_equations,
)


def test_all_equations_present():
    eqs = get_all_equations()
    assert len(eqs) >= 5  # currently 7 records; guards against accidental emptying


def test_verified_unverified_form_complete_disjoint_partition():
    all_eqs = get_all_equations()
    verified = get_verified_equations()
    unverified = get_unverified_equations()

    # Complete partition: every equation lands in exactly one bucket.
    assert len(verified) + len(unverified) == len(all_eqs)
    assert all(eq.status != "requires_source_verification" for eq in verified)
    assert all(eq.status == "requires_source_verification" for eq in unverified)


def test_every_equation_has_status():
    for eq in get_all_equations():
        assert eq.status, "every equation must carry an explicit epistemic status"
