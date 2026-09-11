"""power_analysis_s_dependent.py -- mock-catalog power analysis for the
s-dependent Endpoint/Summary Measure `estimand.md` was amended to use
after `null_results/INDEX.md` NR-025 rejected the fixed-window design.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

Named as the concrete next artifact in `estimand.md`'s own MCID section
(4th-pass amendment) and Status section: "a new mock-catalog power
analysis for THIS design -- required before any code touches real
kSZ/tSZ data ... Not built in this amendment." This script is that
artifact -- still entirely mock/synthetic (no kSZ/tSZ map touched, per
`estimand.md`'s own Pre-Data Requirement), same as
`power_analysis_mock_catalog.py` was for the old window design.

Reuses, does not re-derive:
  - Q(z), the real trajectory table from the CLOSED branch
    `experiments/20260907-icm-expansion-correlation/
    stage4_is_dflip_reachable.py` -- imported live, not re-typed.
  - Real (RA, Dec, z) cluster positions from `exact_pair_census.py`
    (ACT-DR5 MCMF, arXiv:2406.14754) -- the mock realizations below draw
    their (z, s) covariates from the REAL empirical joint distribution
    of real pair separations and redshifts (bootstrap resampling), not
    an invented synthetic distribution.
  - BETA1, BETA2, XI_CROSSING, SIGMA_LN, the broad [20,160] Mpc
    population window, and the AIC/z-test Monte Carlo machinery, all
    from `power_analysis_mock_catalog.py`, unchanged.

xi_pred(z, s) derivation (see `estimand.md` Endpoint section for the
full algebra): Q(z) = (beta2/beta1) * K(z)R(z) / (M(z) c^2 d_of(z)),
where d_of(z) = d0/(1+z) is v82's own PHYSICAL trajectory separation.
For a REAL pair with its own COMOVING separation s_comoving, converting
to physical (s_comoving/(1+z)) and substituting cancels the (1+z)
factors exactly:

    xi_pred(z, s_comoving) = (beta1/beta2) * Q(z) * (d0 / s_comoving)

d0=45 (the CONSTANT comoving trajectory separation), not d_of(z) --
this is not a re-derivation, it is the same cancellation already spelled
out in estimand.md's own Endpoint section.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from exact_pair_census import Z_HIGH, Z_LOW, load_catalog, radec_z_to_cartesian_mpc
from scipy.spatial import cKDTree

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "20260907-icm-expansion-correlation"))
from stage4_is_dflip_reachable import Q_of_z  # noqa: E402  [VERIFIED-run, reused live]

rng = np.random.default_rng(20260911)

# ---- frozen constants, same values as power_analysis_mock_catalog.py ----
BETA1 = 1.433479e10
BETA2 = 7.806760e17
XI_CROSSING = 3.668913e-08
SIGMA_LN = 0.49
D0_MPC = 45.0  # [VERIFIED] v82.md:58-59,318, constant comoving at every z

S_MIN_MPC, S_MAX_MPC = 20.0, 160.0  # same broad population window as the
# old design (kSZ-literature convention) -- carried forward as a
# documented, NOT independently re-verified, stand-in for "the source
# paper's own validated scale range" (estimand.md's own Population
# criterion still names that as the real requirement, not yet read off
# the paper's methods section)
S_MIN_VALID = 10.0  # [ADDED] excludes the small-s contamination band
# FINDING_window_width_resolution.md flagged (near-duplicate/deblending
# artifacts, not real close pairs) -- a documented choice, not a silent one

N_MC = 4000
DELTA_AIC_PROMOTE = 6.0
Z_CRIT = 1.96


def xi_pred(z: np.ndarray, s_comoving: np.ndarray) -> np.ndarray:
    q = np.array([Q_of_z(zi, b1=BETA1, b2=BETA2) for zi in np.atleast_1d(z)])
    return (BETA1 / BETA2) * q * (D0_MPC / np.atleast_1d(s_comoving))


def build_real_pair_pool() -> tuple[np.ndarray, np.ndarray]:
    """Real (z_pair, s_pair) for every real ACT-DR5 MCMF pair in the
    broad population window, s in [S_MIN_VALID, S_MAX_MPC] Mpc comoving."""
    ra, dec, z = load_catalog()
    mask = (z >= Z_LOW) & (z <= Z_HIGH)
    z_used = z[mask]
    xyz = radec_z_to_cartesian_mpc(ra[mask], dec[mask], z_used)
    tree = cKDTree(xyz)
    sdm = tree.sparse_distance_matrix(tree, max_distance=S_MAX_MPC, output_type="coo_matrix")
    upper = sdm.row < sdm.col
    row, col, seps = sdm.row[upper], sdm.col[upper], np.asarray(sdm.data[upper])
    in_range = (seps >= S_MIN_VALID) & (seps <= S_MAX_MPC)
    row, col, seps = row[in_range], col[in_range], seps[in_range]
    z_pair = 0.5 * (z_used[row] + z_used[col])
    return z_pair, seps


def s_m_pair(xi_a: np.ndarray, xi_b: np.ndarray) -> np.ndarray:
    return BETA1 * (xi_a + xi_b) - BETA2 * xi_a * xi_b


def _aic(rss: float, n: int, k: int) -> float:
    return n * np.log(rss / n + 1e-300) + 2 * k


def one_trial(z_i: np.ndarray, s_i: np.ndarray, rel_noise: float, h_m_true: bool) -> dict:
    n = len(z_i)
    xi_center = xi_pred(z_i, s_i)
    xi_a = rng.lognormal(mean=np.log(xi_center) - 0.5 * SIGMA_LN**2, sigma=SIGMA_LN)
    xi_b = rng.lognormal(mean=np.log(xi_center) - 0.5 * SIGMA_LN**2, sigma=SIGMA_LN)
    signal = s_m_pair(xi_a, xi_b)  # Model 1's own regressor, S_M(z,s)
    free_reg = xi_center  # Model 2's own regressor, xi_pred(z,s) -- the
    # DETERMINISTIC center, not the noisy draw, matching estimand.md's
    # own Model 2 definition (y = c + mu*xi_pred(z,s))

    signal_rms = np.std(signal)
    noise_sigma = rel_noise * signal_rms
    y = (signal if h_m_true else 0.0) + rng.normal(0.0, noise_sigma, n)

    # Model 0: y = c
    rss0 = float(np.sum((y - np.mean(y)) ** 2))
    aic0 = _aic(rss0, n, 1)

    # Model 1: y = c + lambda*signal
    d1 = np.column_stack([np.ones(n), signal])
    coef1, _, _, _ = np.linalg.lstsq(d1, y, rcond=None)
    resid1 = y - d1 @ coef1
    rss1 = float(np.sum(resid1**2))
    aic1 = _aic(rss1, n, 2)
    sigma2_1 = rss1 / max(n - 2, 1)
    xtx_inv1 = np.linalg.inv(d1.T @ d1)
    lam_se = float(np.sqrt(sigma2_1 * xtx_inv1[1, 1]))
    z_lambda = coef1[1] / lam_se if lam_se > 0 else 0.0

    # Model 2: y = c + mu*xi_pred(z,s)
    d2 = np.column_stack([np.ones(n), free_reg])
    coef2, _, _, _ = np.linalg.lstsq(d2, y, rcond=None)
    resid2 = y - d2 @ coef2
    rss2 = float(np.sum(resid2**2))
    aic2 = _aic(rss2, n, 2)

    return {
        "z_lambda": z_lambda,
        "d_aic_01": aic0 - aic1,  # Model1 beats Model0
        "d_aic_21": aic2 - aic1,  # Model1 beats Model2
    }


def promote(trial: dict) -> bool:
    """Matches estimand.md's own two-part PROMOTE bar: Model 1 beats
    BOTH Model 0 and Model 2 by the pre-registered margin (the sign-near-
    crossing sub-check is NOT implemented here -- named, not silently
    added; see the script's own closing note)."""
    return (
        abs(trial["z_lambda"]) > Z_CRIT
        and trial["d_aic_01"] > DELTA_AIC_PROMOTE
        and trial["d_aic_21"] > DELTA_AIC_PROMOTE
    )


def power_at_n(
    n_target: int, z_pool: np.ndarray, s_pool: np.ndarray, rel_noise: float
) -> tuple[float, float]:
    pool_n = len(z_pool)
    promote_hm = promote_h0 = 0
    for _ in range(N_MC):
        idx = rng.integers(0, pool_n, size=n_target)
        z_i, s_i = z_pool[idx], s_pool[idx]
        if promote(one_trial(z_i, s_i, rel_noise, True)):
            promote_hm += 1
        if promote(one_trial(z_i, s_i, rel_noise, False)):
            promote_h0 += 1
    return promote_hm / N_MC, promote_h0 / N_MC


def main() -> None:
    print("=" * 78)
    print("STEP 1 -- real (z,s) pair pool, broad population window")
    print("=" * 78)
    z_pool, s_pool = build_real_pair_pool()
    print(
        f"  N real pairs, s in [{S_MIN_VALID:.0f},{S_MAX_MPC:.0f}] Mpc comoving, "
        f"z in [{Z_LOW},{Z_HIGH}]: {len(z_pool)}"
    )
    print(f"  z_pair range: {z_pool.min():.3f} - {z_pool.max():.3f}")
    print(f"  s_pair range: {s_pool.min():.2f} - {s_pool.max():.2f} Mpc")

    print()
    print("=" * 78)
    print(
        "STEP 2 -- Positivity check (estimand.md's own named cheapest "
        "check): do any REAL pairs already approach/cross xi_crossing, "
        "with NO scatter assumption?"
    )
    print("=" * 78)
    xi_all = xi_pred(z_pool, s_pool)
    print(
        f"  xi_pred(z,s) over the real pool: min={xi_all.min():.4e}  "
        f"median={np.median(xi_all):.4e}  max={xi_all.max():.4e}"
    )
    print(f"  xi_crossing = {XI_CROSSING:.4e}")
    frac_above = np.mean(xi_all > XI_CROSSING)
    print(
        f"  fraction of REAL pairs with xi_pred > xi_crossing (deterministic, "
        f"no scatter): {frac_above * 100:.3f}%"
    )
    closest = np.argsort(-xi_all)[:5]
    print("  5 closest-to/over-crossing real pairs:")
    for i in closest:
        print(
            f"    z={z_pool[i]:.3f}  s={s_pool[i]:.2f} Mpc  xi_pred={xi_all[i]:.4e}"
            f"  ({'ABOVE' if xi_all[i] > XI_CROSSING else 'below'} crossing)"
        )

    print()
    print("=" * 78)
    print(f"STEP 3 -- Monte Carlo power (N_MC={N_MC} per cell), s-dependent design")
    print("=" * 78)
    n_scan = [10, 20, 30, 50, 75, 100, 150, 200, 300, 449, 500, 1000, 2000]
    noise_scan = [1.0, 3.0, 10.0]
    print(f"{'N_pairs':>8} {'rel_noise':>10} {'power':>8} {'false-promote':>15}")
    results = []
    for n_target in n_scan:
        for rel_noise in noise_scan:
            p_power, p_false = power_at_n(n_target, z_pool, s_pool, rel_noise)
            results.append((n_target, rel_noise, p_power, p_false))
            print(
                f"{n_target:>8} {rel_noise:>10.1f} {p_power * 100:>7.1f}% {p_false * 100:>14.1f}%"
            )

    print()
    print("=" * 78)
    print("STEP 4 -- comparison to the OLD (window-based, superseded) design")
    print("=" * 78)
    print(
        "  Old design (power_analysis_mock_catalog.py, window-based, REJECTED\n"
        "  test design per NR-025) at the SAME footprint-scaled broad-window N:\n"
        "    N=449 (mid footprint): 100.0% power @3x noise\n"
        "  New design (this script), same N=449, real (z,s), 2-model bar:"
    )
    row_449 = [r for r in results if r[0] == 449 and r[1] == 3.0]
    if row_449:
        print(
            f"    N=449: {row_449[0][2] * 100:.1f}% power @3x noise, "
            f"{row_449[0][3] * 100:.1f}% false-promote"
        )
    print(
        "  Reading: the new design's TWO-PART bar (beat null AND beat the\n"
        "  free-linear alternative) is intentionally stricter than the old\n"
        "  design's one-part bar (beat null only) -- a lower power number at\n"
        "  the same N is not evidence the new design is worse, it is evidence\n"
        "  the new design is testing a SHARPER, more specific claim, matching\n"
        "  estimand.md's own PROMOTE region wording."
    )

    print()
    print("=" * 78)
    print("What this does NOT establish")
    print("=" * 78)
    print(
        "  1. The sign-near-crossing sub-check in estimand.md's own PROMOTE\n"
        "     region ('the highest-xi stratum shows sign consistent with the\n"
        "     predicted crossing') is NOT implemented in the promote() function\n"
        "     above -- only the two ChiSq/AIC comparisons are. Named, not\n"
        "     silently added.\n"
        "  2. The [20,160] Mpc population window is carried forward from the\n"
        "     old design, NOT independently re-verified against the source kSZ\n"
        "     paper's own methods section (estimand.md's own Population\n"
        "     criterion still names that as unresolved).\n"
        "  3. The small-s Consistency(d) instrumental threat (CMB-beam\n"
        "     blending) is handled here only by a blanket S_MIN_VALID=10 Mpc\n"
        "     cut, not the real angular-separation-vs-beam-size check\n"
        "     estimand.md itself says is still needed.\n"
        "  4. Real power will be lower than every number above -- these are\n"
        "     best-case, confounder-free upper bounds; the synthetic four-world\n"
        "     identifiability battery (estimand.md's own hard gate) has not run."
    )


if __name__ == "__main__":
    main()
