"""Wire experiments/20260906-evidence-authority/E8c_drop_non_moresco_points.py
into pytest tests/ -q. E8c had no test_* functions of its own.
"""

from __future__ import annotations

import numpy as np
from E8_full_covariance_propagation import H_cc, moresco_mask, s_cc, z_cc
from E8c_drop_non_moresco_points import cov_subset, run, with_anchors


def test_moresco_mask_count():
    assert moresco_mask().sum() == 15


def test_reference_33pt_diag_matches_e8b_baseline():
    """The REF row must reproduce E8b's own reported diagonal dchi2 (+0.561)
    -- a real cross-file regression guard, not a new claim."""
    d_ref = run("REF", *with_anchors(z_cc, H_cc, np.diag(s_cc**2)))
    assert abs(d_ref - 0.561) < 0.01, d_ref


def test_drop_and_zero_variants_run_end_to_end(mm20_real):
    """Smoke test for the DROP/ZERO covariance-subset pipeline (cov_subset ->
    with_anchors -> run) -- must not crash and must return a finite dchi2."""
    mask = moresco_mask()
    z15, H15, s15 = z_cc[mask], H_cc[mask], s_cc[mask]

    d_drop = run(
        "DROP 15+2, Moresco default",
        *with_anchors(z15, H15, cov_subset(z15, H15, s15, mm20_real, ["spsooo", "imf"])),
    )
    assert np.isfinite(d_drop)

    d_zero = run(
        "ZERO 33 pts, cov on his 15 only",
        *with_anchors(z_cc, H_cc, cov_subset(z_cc, H_cc, s_cc, mm20_real, ["spsooo", "imf"], mask)),
    )
    assert np.isfinite(d_zero)
