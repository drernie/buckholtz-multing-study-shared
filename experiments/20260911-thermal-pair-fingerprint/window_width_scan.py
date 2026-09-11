"""window_width_scan.py -- resolves (as far as the current model allows)
the window-WIDTH question FINDING_power_analysis.md left open after the
Exact Pair Census (SS6).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

Two separate questions, kept distinct (feedback_verdict_attribution.md):

  Q_stat  -- does statistical power alone pick an optimal window width?
  Q_data  -- does the REAL cluster-pair separation distribution itself
             show anything special near s=45 Mpc, independent of any
             assumption about MULTING, or is 45 Mpc purely a MODEL-
             internal number with no real large-scale-structure
             signature at this separation?

Q_stat is answered by re-running the SAME one_trial() Monte Carlo
(power_analysis_mock_catalog.py) at a fine grid of window half-widths,
using the REAL N(width) from exact_pair_census.py's own pairwise-
separation array. Q_data is answered by comparing the REAL observed
pair count per separation bin against an ANALYTIC Poisson (unclustered)
expectation computed from the SAME real N=4390, real z-shell volume,
and real ACT-DR5 footprint (13211 deg^2, [VERIFIED-arXiv:2406.14754]) --
not a noisy empirical fit, since the unclustered expectation has a
closed form (the same volume-shell integral already used and verified
throughout this branch).
"""

from __future__ import annotations

import astropy.units as u
import numpy as np
from astropy.cosmology import Planck18 as cosmo
from exact_pair_census import (
    AREA_ACT_DR5_DEG2,
    Z_HIGH,
    Z_LOW,
    load_catalog,
    radec_z_to_cartesian_mpc,
)
from scipy.spatial import cKDTree

rng = np.random.default_rng(20260911)

CENTER_MPC = 45.0  # [VERIFIED] v82.md:58-59,318, d0, constant comoving at all z
S_MAX_QUERY = 300.0  # wider than exact_pair_census.py's 200, for a longer
# baseline arm in the Q_data check below

# same C1 constants as power_analysis_mock_catalog.py, reproduced here
# (not imported -- importing that module would re-run its own multi-minute
# Monte Carlo scan as a side effect of import; these are the same numbers,
# unchanged)
BETA1 = 1.433479e10
BETA2 = 7.806760e17
XI_MEAN_TRAJECTORY = 3.210416e-08
SIGMA_LN = 0.49
N_MC = 4000
DELTA_AIC_PROMOTE = 6.0
REL_NOISE = 3.0

FOOTPRINT_MID = 775.0  # Fork-2 mid target, matches the rest of this branch


def mock_xi_sample(n: int, mean_xi: float, sigma_ln: float) -> np.ndarray:
    mu_ln = np.log(mean_xi) - 0.5 * sigma_ln**2
    return rng.lognormal(mean=mu_ln, sigma=sigma_ln, size=n)


def s_m_pair(xi_a: np.ndarray, xi_b: np.ndarray) -> np.ndarray:
    return BETA1 * (xi_a + xi_b) - BETA2 * xi_a * xi_b


def one_trial(n_pairs: int, rel_noise: float, h_m_true: bool) -> tuple[float, float]:
    xi_a = mock_xi_sample(n_pairs, XI_MEAN_TRAJECTORY, SIGMA_LN)
    xi_b = mock_xi_sample(n_pairs, XI_MEAN_TRAJECTORY, SIGMA_LN)
    signal = s_m_pair(xi_a, xi_b)
    signal_rms = np.std(signal)
    noise_sigma = rel_noise * signal_rms
    y = (signal if h_m_true else 0.0) + rng.normal(0.0, noise_sigma, n_pairs)

    design = np.column_stack([np.ones(n_pairs), signal])
    coef, _, _, _ = np.linalg.lstsq(design, y, rcond=None)
    resid_full = y - design @ coef
    rss_full = float(np.sum(resid_full**2))
    lam = coef[1]
    sigma2_hat = rss_full / max(n_pairs - 2, 1)
    xtx_inv = np.linalg.inv(design.T @ design)
    lam_se = float(np.sqrt(sigma2_hat * xtx_inv[1, 1]))
    z_lambda = lam / lam_se if lam_se > 0 else 0.0

    rss_null = float(np.sum((y - np.mean(y)) ** 2))
    aic_null = n_pairs * np.log(rss_null / n_pairs + 1e-300) + 2 * 1
    aic_full = n_pairs * np.log(rss_full / n_pairs + 1e-300) + 2 * 2
    delta_aic = aic_null - aic_full
    return z_lambda, delta_aic


def power_at_n(n_pairs: int, rel_noise: float = REL_NOISE) -> float:
    n_pairs = max(int(round(n_pairs)), 2)
    promote_hm = sum(
        1
        for _ in range(N_MC)
        if (lambda z, d: abs(z) > 1.96 and d > DELTA_AIC_PROMOTE)(
            *one_trial(n_pairs, rel_noise, True)
        )
    )
    return promote_hm / N_MC


def main() -> None:
    print("=" * 78)
    print("Loading the real catalog, building the real pairwise separations")
    print("=" * 78)
    ra, dec, z = load_catalog()
    mask = (z >= Z_LOW) & (z <= Z_HIGH)
    n_used = int(mask.sum())
    xyz = radec_z_to_cartesian_mpc(ra[mask], dec[mask], z[mask])
    tree = cKDTree(xyz)
    sdm = tree.sparse_distance_matrix(tree, max_distance=S_MAX_QUERY, output_type="coo_matrix")
    upper = sdm.row < sdm.col
    seps = np.asarray(sdm.data[upper])
    print(f"  N clusters (z cut): {n_used}   N pairs <= {S_MAX_QUERY:.0f} Mpc: {len(seps)}")

    area_scale = FOOTPRINT_MID / AREA_ACT_DR5_DEG2

    print()
    print("=" * 78)
    print("Q_stat -- does power alone pick an optimal window width?")
    print("=" * 78)
    print(
        f"{'half-width':>10} {'[lo,hi] Mpc':>16} {'N (full)':>9} {'N (mid, scaled)':>16} {'power@3x':>10}"
    )
    half_widths = [2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 75.0]
    stat_results = []
    for hw in half_widths:
        lo, hi = CENTER_MPC - hw, CENTER_MPC + hw
        n_full = int(np.sum((seps >= lo) & (seps <= hi)))
        n_scaled = n_full * area_scale
        pw = power_at_n(n_scaled)
        stat_results.append((hw, n_full, n_scaled, pw))
        print(
            f"{hw:>10.1f} [{lo:>5.1f},{hi:>5.1f}] {n_full:>9d} {n_scaled:>16.1f} {pw * 100:>9.1f}%"
        )

    monotone = all(
        stat_results[i][3] <= stat_results[i + 1][3] + 1e-9 for i in range(len(stat_results) - 1)
    )
    print()
    print(
        f"  Monotonically non-decreasing in width: {monotone}. "
        + (
            "Confirms: under the CURRENT model (every simulated pair drawn from "
            "the SAME xi distribution regardless of its own separation s -- "
            "claim.md 3a's own flagged marginal HYPOTHESIS), power has NO "
            "interior optimum. Widening the window is trivially always "
            "better for power alone; width cannot be resolved by power-"
            "maximization under this model. A width choice needs a "
            "DIFFERENT justification (Q_data below, or a future model "
            "refinement that lets xi depend on each pair's own s -- a "
            "materially new assumption, not attempted here)."
            if monotone
            else "NOT monotonic -- an interior optimum exists under the "
            "current model. See the printed table for its location."
        )
    )

    print()
    print("=" * 78)
    print(
        "Q_data -- is s=45 Mpc itself special in the REAL pair-separation "
        "distribution, independent of any MULTING assumption?"
    )
    print("=" * 78)
    # Analytic Poisson (unclustered) expectation, using the REAL N=4390 and
    # REAL z-shell volume at the FULL ACT-DR5 footprint (13211 deg^2) --
    # the same volume-shell integral used throughout this branch, now with
    # the corrected (not all-z) density input.
    v_low = cosmo.comoving_volume(Z_LOW).to(u.Mpc**3).value * (AREA_ACT_DR5_DEG2 / 41253.0)
    v_high = cosmo.comoving_volume(Z_HIGH).to(u.Mpc**3).value * (AREA_ACT_DR5_DEG2 / 41253.0)
    v_shell = v_high - v_low
    n_density = n_used / v_shell  # Mpc^-3, REAL density in the REAL shell

    bin_edges = np.arange(0.0, S_MAX_QUERY + 10.0, 10.0)
    obs_hist, _ = np.histogram(seps, bins=bin_edges)
    print(
        f"{'bin [Mpc)':>16} {'observed':>9} {'poisson-expected':>17} {'1+xi(s) = obs/exp':>19} {'poisson z-score':>16}"
    )
    ratios = []
    for lo, hi, n_obs in zip(bin_edges[:-1], bin_edges[1:], obs_hist, strict=True):
        shell_vol = (4.0 / 3.0) * np.pi * (hi**3 - lo**3)
        n_exp = 0.5 * n_used * n_density * shell_vol
        ratio = n_obs / n_exp if n_exp > 0 else float("nan")
        z_score = (n_obs - n_exp) / np.sqrt(n_exp) if n_exp > 0 else float("nan")
        ratios.append((lo, hi, n_obs, n_exp, ratio, z_score))
        marker = "  <-- window center" if lo <= CENTER_MPC < hi else ""
        print(
            f"[{lo:>6.0f},{hi:>6.0f}) {n_obs:>9d} {n_exp:>17.2f} {ratio:>19.3f} {z_score:>16.2f}{marker}"
        )

    print()
    print(
        "  Reading: 1+xi(s) > 1 means REAL clusters are more clustered at "
        "that separation than a random (Poisson) field -- the standard "
        "two-point correlation excess. If this ratio peaks SPECIFICALLY "
        "near s=45 Mpc (not just monotonically declining with s, which is "
        "the generic LSS expectation at these scales), that would be a "
        "real, independent reason -- from the data itself, not from v82's "
        "text -- to treat 45 Mpc as a locally preferred separation. If it "
        "instead declines smoothly through s=45 with no local feature, "
        "45 Mpc has no such independent support: it remains solely a "
        "MODEL-internal number (v82's own frozen initial condition), not "
        "a scale singled out by real cluster clustering statistics."
    )


if __name__ == "__main__":
    main()
