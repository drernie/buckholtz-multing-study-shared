"""Wire experiments/20260906-evidence-authority/independent_verification_rerun/
E18_all_rows_and_global_search.py into pytest tests/ -q -- added same
session, per this project's own established discipline.
"""

from __future__ import annotations

from E18_all_rows_and_global_search import (
    reoptimize_fixed_h0_anchor_rows,
    reproduce_all_rows,
)
from E18_all_rows_and_global_search import (
    test_negative_control_perturbed_om_changes_chi2_substantially as _test_nc1,
)
from E18_all_rows_and_global_search import (
    test_positive_control_reproduces_published_row as _test_pc1,
)


def test_positive_control_reproduces_published_row():
    _test_pc1()


def test_negative_control_perturbed_om_changes_chi2_substantially():
    _test_nc1()


def test_all_7_rows_forward_chi2_within_1pct():
    """Regression guard: all 7 Table II rows must reproduce chi2 to
    within 1% (this file's own pre-registered MCID)."""
    results = reproduce_all_rows()
    for name, r in results.items():
        assert r["rel_diff_pct"] < 1.0, (name, r)


def test_6_fixed_rows_reoptimize_within_1pct():
    """Regression guard: independent 2D re-optimization (no starting
    guess) for the 6 fixed-H0_anchor rows must recover chi2 within 1%
    of the published value. Reduced maxiter/popsize for CI speed -- the
    full, rigorous search (2000/40) is documented in FINDING_E18's own
    locked-in results, this only checks the machinery still lands in
    the right basin."""
    results = reoptimize_fixed_h0_anchor_rows(maxiter=200, popsize=15)
    for name, r in results.items():
        rel = 100.0 * abs(r["chi2_reopt"] - r["chi2_stated"]) / r["chi2_stated"]
        assert rel < 1.0, (name, r, rel)
