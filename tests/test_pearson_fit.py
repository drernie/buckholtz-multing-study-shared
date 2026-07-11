"""Tests for src/pearson_fit.py — the README headline Pearson r=0.62 claim.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION (same status as the module
under test). Before this file existed, no test imported pearson_fit.py at all,
so the headline r=0.62 (MCXC, n=443) had zero regression protection and zero
check that it isn't a trivial artifact of both H_MULTING(z) and H_CC(z) being
monotonically increasing in z (found by 2026-07-11 code audit).

These tests do three things:
  1. Pin the current numeric output (regression protection).
  2. Run a genuine null test: shuffle which cluster's (mass, thermal energy,
     radius) triple is paired with which redshift, keep the true z (so the
     H_CC(z) target and D=D0/(1+z) scale are untouched), and confirm the same
     grid-search procedure cannot find a comparably good fit on the shuffled
     data. If it could, r=0.62 would say nothing beyond "both curves rise
     with z" -- it does not: see test_grid_search_beats_shuffled_physics_null.
  3. Pin a second, separate finding surfaced while writing (2): a beta_d=0,
     beta_q=0 baseline -- i.e. the monopole/Newtonian mass/D^2 term ALONE,
     with no MULTING-specific dipole or quadrupole contribution whatsoever --
     gives r=0.7334, HIGHER than both TJB's own reported beta_d=4.5, beta_q=18
     (r=0.6234) and grid_search_pearson's own "best" fit (r=0.6235). The grid
     search cannot find this itself: beta_d_log_range/beta_q_log_range default
     to logspace(2,8), i.e. beta in [100, 1e8], which never includes near-zero
     values. See test_zero_beta_baseline_beats_reported_and_optimized_fit.
     NOT_VALIDATION/NOT_REFUTATION applies here too: this says the dipole and
     quadrupole terms, AT THESE SPECIFIC beta VALUES, do not improve the fit
     over pure mass/D^2 scaling -- it is not a statement about whether some
     other (beta_d, beta_q) inside [100, 1e8] the grid search also missed
     would do better, nor about MULTING/IDM as a framework.
"""

from __future__ import annotations

import numpy as np
import pytest

from src.pearson_fit import grid_search_pearson, load_data, single_pearson

DATA_MISSING = pytest.mark.skipif(
    not __import__("pathlib").Path("data/clusters_clean.csv").exists()
    or not __import__("pathlib").Path("data/hz_cc.csv").exists(),
    reason="data/clusters_clean.csv or data/hz_cc.csv not present",
)


@pytest.fixture(scope="module")
def real_data():
    clusters, hz_cc = load_data()
    df = clusters[clusters["Ethermal_c2_Msun"].notna()].sort_values("z").reset_index(drop=True)
    return df, hz_cc


@DATA_MISSING
def test_load_data_has_expected_shape():
    clusters, hz_cc = load_data()
    assert len(clusters) > 0
    assert len(hz_cc) > 0
    assert {"z", "M500c_Msun", "Ethermal_c2_Msun", "R500c_Mpc"}.issubset(clusters.columns)
    assert {"z", "Hz_km_s_Mpc"}.issubset(hz_cc.columns)


@DATA_MISSING
def test_single_pearson_tjb_beta_matches_readme(real_data):
    """Regression pin for the README headline: TJB's own beta_d=4.5, beta_q=18.0
    at D0=100 Mpc gives r about 0.62 on n=443 pairs. If this drifts, either the
    data files changed or single_pearson() broke -- both worth knowing about."""
    df, hz_cc = real_data
    res = single_pearson(df, hz_cc, beta_d=4.5, beta_q=18.0, D0_Mpc=100.0)
    assert res["n"] == 443, f"pair count drifted: {res['n']} (was 443)"
    assert abs(res["r"] - 0.6234) < 0.01, f"r drifted: {res['r']:.4f} (was ~0.6234)"
    assert res["p"] < 1e-10


@DATA_MISSING
def test_grid_search_pearson_returns_well_formed_result(real_data):
    df, hz_cc = real_data
    res = grid_search_pearson(df, hz_cc, D0_Mpc=100.0, n_pts=20, label="smoke")
    assert -1.0 <= res["r"] <= 1.0
    assert res["n"] >= 5
    assert np.isfinite(res["beta_d"])
    assert np.isfinite(res["beta_q"])


@DATA_MISSING
def test_grid_search_beats_shuffled_physics_null(real_data):
    """The core anti-artifact check flagged by the 2026-07-11 audit.

    Shuffle WHICH cluster's (M500c, Ethermal, R500c) triple is attached to
    which z, leaving z itself (and therefore D=D0/(1+z) and the H_CC(z)
    lookup target) untouched. If the real r=0.62 were merely "two curves
    that both rise with z," a shuffled dataset would let the wide 50x50-style
    grid search find a comparably good (beta_d, beta_q) fit almost every time,
    since D(z) and H_CC(z) are unaffected by the shuffle. It does not: the
    real fit beats every shuffled trial by a wide margin (real ~0.62 vs
    shuffled max ~0.36 over 10 trials, empirically 0/10). This does not
    validate the MULTING model -- it only shows the correlation is not the
    z-monotonicity artifact the audit worried it might be.
    """
    df, hz_cc = real_data
    real = grid_search_pearson(df, hz_cc, D0_Mpc=100.0, n_pts=20, label="real")
    assert np.isfinite(real["r"])

    rng = np.random.default_rng(42)
    n_trials = 10
    null_rs = []
    for trial in range(n_trials):
        shuffled = df.copy()
        perm = rng.permutation(len(df))
        for col in ("M500c_Msun", "Ethermal_c2_Msun", "R500c_Mpc"):
            shuffled[col] = df[col].to_numpy()[perm]
        res = grid_search_pearson(shuffled, hz_cc, D0_Mpc=100.0, n_pts=20, label=f"null{trial}")
        if np.isfinite(res["r"]):
            null_rs.append(res["r"])

    assert len(null_rs) >= n_trials - 2, "too many shuffled trials failed to produce a finite r"
    null_max = max(null_rs)
    assert real["r"] > null_max + 0.15, (
        f"real r={real['r']:.4f} does not clearly beat the shuffled-physics null "
        f"(null max={null_max:.4f} over {len(null_rs)} trials) -- the correlation "
        "may be a trivial artifact of shared z-monotonicity, not physical content"
    )


@DATA_MISSING
def test_zero_beta_baseline_beats_reported_and_optimized_fit(real_data):
    """Surfaced 2026-07-11 while writing the null test above (not hypothesized
    in advance -- found by mutation-probing the formula and noticing the
    dipole/quadrupole terms were numerically negligible at beta_d=4.5).

    A zero-parameter monopole-only baseline (beta_d=0, beta_q=0, i.e. plain
    H ~ sqrt(mass/D^2), no MULTING-specific structure at all) scores HIGHER
    than both TJB's own reported beta_d=4.5, beta_q=18.0 AND
    grid_search_pearson's own reported "best" fit. The grid search's default
    beta_d_log_range/beta_q_log_range=(2.0, 8.0) means beta in [100, 1e8] --
    it structurally cannot find this baseline itself, since 0 is outside that
    range. This test exists so that gap is visible in the test suite instead
    of only discoverable by hand.
    """
    df, hz_cc = real_data
    baseline = single_pearson(df, hz_cc, beta_d=0.0, beta_q=0.0, D0_Mpc=100.0)
    reported = single_pearson(df, hz_cc, beta_d=4.5, beta_q=18.0, D0_Mpc=100.0)
    optimized = grid_search_pearson(df, hz_cc, D0_Mpc=100.0, n_pts=20, label="optimized")

    assert baseline["n"] == reported["n"] == optimized["n"], (
        "sample sizes differ between baseline/reported/optimized -- comparison invalid"
    )
    assert baseline["r"] > reported["r"], (
        f"baseline r={baseline['r']:.4f} no longer beats TJB-reported r={reported['r']:.4f} "
        "-- this finding may have changed, re-verify before updating this pin"
    )
    assert baseline["r"] > optimized["r"], (
        f"baseline r={baseline['r']:.4f} no longer beats grid-search-optimal "
        f"r={optimized['r']:.4f} -- re-verify before updating this pin"
    )
    assert abs(baseline["r"] - 0.7334) < 0.01, f"baseline r drifted: {baseline['r']:.4f}"


@DATA_MISSING
def test_grid_search_silent_sample_size_is_reported(real_data):
    """The audit flagged that NaN/positivity filtering inside grid_search_pearson
    can silently shrink n below the input cluster count with no warning. This
    test does not forbid that (positivity filtering is legitimate physics: phi
    must stay positive under the sqrt), it only pins that n is reported and is
    a real subset of the input, so a future silent-collapse regression (e.g.
    n dropping to single digits) is visible in the test output."""
    df, hz_cc = real_data
    res = grid_search_pearson(df, hz_cc, D0_Mpc=100.0, n_pts=20, label="n-check")
    assert 5 <= res["n"] <= len(df), (
        f"reported n={res['n']} is outside the physically possible range "
        f"[5, {len(df)}] for this input"
    )
