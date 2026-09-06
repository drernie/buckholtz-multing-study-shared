"""Wire experiments/20260906-evidence-authority/E8_full_covariance_propagation.py
into pytest tests/ -q -- this is the hub module 4 other E-scripts (E8b, E8c,
E11, E12) import from, and it had zero pytest coverage (2026-09-06
boyko-project-radar finding). If P176 (which E8 imports) or E8 itself broke,
none of its 4 dependents' own bugs would be caught by the commit gate either.
"""

from __future__ import annotations

from unittest.mock import Mock

import numpy as np
import pytest
from E8_full_covariance_propagation import (
    TABLE_II,
    build_cov_cc,
    embed_33,
    fetch_mm20,
    hessian_small_eig_and_slope,
    make_chi2_cov,
    moresco_mask,
)
from E8_full_covariance_propagation import (
    test_positive_control_lcdm_diag as _e8_test_lcdm_diag,
)
from E8_full_covariance_propagation import (
    test_positive_control_table_ii_diag as _e8_test_table_ii_diag,
)
from E8_full_covariance_propagation import (
    test_positive_control_zero_components_reduces_to_diag as _e8_test_zero_components,
)


def test_positive_control_table_ii_diag():
    _e8_test_table_ii_diag()


def test_positive_control_lcdm_diag():
    # this is a generator (has `yield`) -- must be consumed for its asserts to run
    results = list(_e8_test_lcdm_diag())
    assert len(results) == 2  # "fixed" and "free" rows


def test_positive_control_zero_components_reduces_to_diag(mm20_real):
    _e8_test_zero_components(mm20_real)


def test_moresco_mask_count():
    """The script's own printed expectation ('expected 15') -- a real
    regression guard, not a new claim."""
    assert moresco_mask().sum() == 15


def test_fetch_mm20_parses_real_snapshot_format(monkeypatch, mm20_real_text):
    """Guards the same failure class as FINDING_E5 (a parser silently
    accepting/mis-reading upstream format) -- here for E8's own fetch."""
    resp = Mock()
    resp.text = mm20_real_text
    resp.raise_for_status = Mock(return_value=None)
    monkeypatch.setattr("requests.get", lambda *a, **k: resp)

    mm20 = fetch_mm20()

    assert len(mm20) == 29
    assert list(mm20.columns) == ["z", "imf", "stlib", "sps", "spsooo"]
    assert mm20["z"].min() == pytest.approx(0.075)
    assert mm20["z"].max() == pytest.approx(1.475)


def test_covariance_pipeline_runs_end_to_end(mm20_real):
    """Smoke test for build_cov_cc -> embed_33 -> make_chi2_cov with a real
    (frozen) modelling covariance -- the exact chain E8b/E8c/E11/E12 all
    reuse. Must not crash (Cholesky must succeed, per the module's own PC4)
    and must return a finite, non-negative chi2 at TJB's own fitted point."""
    C33 = embed_33(build_cov_cc(mm20_real, ["spsooo", "imf"], None))
    chi2_fn = make_chi2_cov(C33)
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    val = chi2_fn(h0a, b1, b2)
    assert np.isfinite(val)
    assert val >= 0.0


def test_hessian_small_eig_and_slope_runs(mm20_real):
    """Smoke test for the Hessian helper E11 also imports the pattern from --
    must not crash and must return a real (positive small eigenvalue) result."""
    C33 = embed_33(build_cov_cc(mm20_real, ["spsooo", "imf"], None))
    chi2_fn = make_chi2_cov(C33)
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    eig, slope = hessian_small_eig_and_slope(chi2_fn, h0a, b1, b2)
    assert eig[0] > 0.0
    assert np.isfinite(slope)
