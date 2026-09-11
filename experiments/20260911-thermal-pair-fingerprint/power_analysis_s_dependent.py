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

[AMENDED 2026-09-11, same day, after the beam-blending check] promote()
now also implements the sign-near-crossing sub-check estimand.md's own
PROMOTE region names ("the highest-xi stratum shows sign consistent
with the predicted crossing") -- operationalized as a sign-near-
REVERSAL check at XI_PEAK=BETA1/BETA2 (see that constant's own docstring
for why XI_PEAK, not XI_CROSSING itself, is the stratification point).
This is a real, load-bearing addition to promote(), not a comment --
every power number in this run supersedes the earlier 2-condition run.

[CORRECTED 2026-09-11, same day, real bug -- caught by an external
review of the published shared repo, independently verified before
applying, per method_verify_pasted_ai_reports.md] power_at_n()'s own
`rng.integers(0, pool_n, size=n_target)` sampled WITH REPLACEMENT from
the full 7693-pair COMBINATORIAL pool -- i.e. from every candidate pair
among 4390 clusters, not a set of cluster-disjoint pairs. Verified
directly, not taken on the critique's word: at N=449, 43.2% of sampled
pairs in a single trial shared a real cluster with another sampled pair
in that SAME trial (mean 3.93 candidate pairs per cluster, max 18).
This violates estimand.md's own Population/SUTVA exclusion rule ("a
cluster appearing in more than one candidate pair is assigned to at
most one pair... the same physical object cannot licitly appear as an
independent unit twice"). Every power number in the PRIOR run of this
script (the 59.9%-at-N=449 headline) is WITHDRAWN, not merely footnoted
-- it is the power of an easier, SUTVA-violating "pair-i.i.d. surrogate
design", not of the design estimand.md actually specifies. Fixed below
by sampling WITHOUT replacement from a real cluster-disjoint matching
(build_disjoint_matching()), not from the raw combinatorial pool.
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

# [ADDED, sign-near-crossing sub-check] S_M(xi) = 2*BETA1*xi - BETA2*xi^2
# is a downward parabola in xi -- it RISES for xi < XI_PEAK and FALLS for
# xi > XI_PEAK, where XI_PEAK = BETA1/BETA2 is where dS_M/dxi = 0.
# XI_PEAK != XI_CROSSING: XI_CROSSING solves S_M(xi)=1 (where the TOTAL
# force -1+S_M changes sign, claim.md Sec4's own root), XI_PEAK solves
# dS_M/dxi=0 (where the CORRECTION TERM's own slope changes sign). They
# are close (XI_PEAK=1.836e-8 vs XI_CROSSING=3.669e-8) because S_M's peak
# value (~263) is so far above 1 that both roots of S_M=1 sit close to
# S_M's own zero-crossings -- but they are NOT the same point, and this
# script stratifies at XI_PEAK, not XI_CROSSING, because REAL pairs above
# XI_CROSSING are rare (306/7693=3.98% of the pool) while REAL pairs
# above XI_PEAK are common (1457/7693=18.9%) -- [VERIFIED] via the real
# pool itself, not assumed -- making a per-trial stratified slope fit
# statistically usable at realistic N. This operationalizes estimand.md's
# "sign consistent with the predicted crossing" as "sign consistent with
# the predicted REVERSAL" (the same qualitative non-monotonic feature
# that produces the eventual crossing), stated as a deliberate, honest
# choice, not a literal match to the word "crossing".
XI_PEAK = BETA1 / BETA2
MIN_STRATUM_N = 5  # sub-check auto-fails below this -- too few points to
# trust a fitted sign

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


def build_real_pair_pool() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int]:
    """Every real ACT-DR5 MCMF CANDIDATE pair in the broad population
    window, s in [S_MIN_VALID, S_MAX_MPC] Mpc comoving -- the full
    COMBINATORIAL set (one cluster can appear in many candidate pairs).
    Returns (z_pair, s_pair, row, col, n_clusters) -- row/col are the
    cluster indices behind each pair, needed by build_disjoint_matching()
    to enforce estimand.md's own SUTVA exclusion rule."""
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
    return z_pair, seps, row, col, len(z_used)


def build_disjoint_matching(
    row: np.ndarray, col: np.ndarray, order: np.ndarray, n_clusters: int
) -> np.ndarray:
    """Greedy cluster-disjoint matching: walk candidate pairs in the
    given `order`, accept a pair only if NEITHER of its two clusters has
    already been used by an earlier-accepted pair. Returns the indices
    (into row/col/seps) of the accepted, mutually cluster-disjoint pairs
    -- this is estimand.md's own Population/SUTVA rule ("a cluster
    appearing in more than one candidate pair is assigned to at most one
    pair"), made concrete. `order` is passed in, not fixed here, because
    the tie-break rule matters and should be chosen (and reported)
    explicitly by the caller -- see main()'s own random-vs-closest-s
    comparison."""
    used = np.zeros(n_clusters, dtype=bool)
    accepted = []
    for i in order:
        a, b = row[i], col[i]
        if not used[a] and not used[b]:
            used[a] = True
            used[b] = True
            accepted.append(i)
    return np.array(accepted, dtype=int)


def s_m_pair(xi_a: np.ndarray, xi_b: np.ndarray) -> np.ndarray:
    return BETA1 * (xi_a + xi_b) - BETA2 * xi_a * xi_b


def _aic(rss: float, n: int, k: int) -> float:
    return n * np.log(rss / n + 1e-300) + 2 * k


def fit_and_check(xi_center: np.ndarray, signal: np.ndarray, y: np.ndarray) -> dict:
    """[EXTRACTED 2026-09-11, for reuse by the synthetic four-world
    battery -- same fitting/sign-check logic one_trial() already used,
    factored out so a WORLD-SPECIFIC y-generator (this script's own
    MULTING-true/null, or the four-world battery's optical-depth-
    confounded/merger-confounded generators) can share ONE fitting
    implementation, not a second copy that could silently drift.
    `xi_center`/`signal` are still needed (not just `y`) because the
    sign-near-crossing stratification and Model 1's own regressor both
    depend on them, not only on the observed outcome."""
    n = len(y)
    free_reg = xi_center  # Model 2's own regressor, xi_pred(z,s) -- the
    # DETERMINISTIC center, not a noisy draw, matching estimand.md's own
    # Model 2 definition (y = c + mu*xi_pred(z,s))

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

    # sign-near-crossing (sign-near-reversal) sub-check: fit y vs xi_center
    # SEPARATELY within the low-xi (<=XI_PEAK) and high-xi (>XI_PEAK)
    # strata of THIS SAME trial's pairs. MULTING predicts +1 (rising)
    # below the peak and -1 (falling) above it -- a genuine non-monotonic
    # reversal a purely monotonic alternative cannot produce by
    # construction, distinct from the AIC/z-test comparisons above.
    low_mask = xi_center <= XI_PEAK
    high_mask = ~low_mask
    sign_low = _stratum_slope_sign(xi_center[low_mask], y[low_mask])
    sign_high = _stratum_slope_sign(xi_center[high_mask], y[high_mask])

    return {
        "z_lambda": z_lambda,
        "d_aic_01": aic0 - aic1,  # Model1 beats Model0
        "d_aic_21": aic2 - aic1,  # Model1 beats Model2
        "sign_low": sign_low,  # None if stratum too small to fit
        "sign_high": sign_high,
    }


def one_trial(z_i: np.ndarray, s_i: np.ndarray, rel_noise: float, h_m_true: bool) -> dict:
    n = len(z_i)
    xi_center = xi_pred(z_i, s_i)
    xi_a = rng.lognormal(mean=np.log(xi_center) - 0.5 * SIGMA_LN**2, sigma=SIGMA_LN)
    xi_b = rng.lognormal(mean=np.log(xi_center) - 0.5 * SIGMA_LN**2, sigma=SIGMA_LN)
    signal = s_m_pair(xi_a, xi_b)  # Model 1's own regressor, S_M(z,s)

    signal_rms = np.std(signal)
    noise_sigma = rel_noise * signal_rms
    y = (signal if h_m_true else 0.0) + rng.normal(0.0, noise_sigma, n)

    return fit_and_check(xi_center, signal, y)


def _stratum_slope_sign(xi_stratum: np.ndarray, y_stratum: np.ndarray) -> int | None:
    """Sign of the OLS slope of y on xi within one stratum, or None if
    there are fewer than MIN_STRATUM_N points to trust a fitted sign."""
    n = len(xi_stratum)
    if n < MIN_STRATUM_N:
        return None
    d = np.column_stack([np.ones(n), xi_stratum])
    coef, _, _, _ = np.linalg.lstsq(d, y_stratum, rcond=None)
    slope = coef[1]
    if slope == 0.0:
        return 0
    return 1 if slope > 0 else -1


def promote(trial: dict) -> bool:
    """Matches estimand.md's own two-part PROMOTE bar (Model 1 beats
    BOTH Model 0 and Model 2 by the pre-registered margin) PLUS the
    sign-near-crossing (operationalized as sign-near-reversal, see
    XI_PEAK's own docstring above) sub-check: the low-xi stratum's
    fitted slope must be positive AND the high-xi stratum's fitted slope
    must be negative -- a DIRECTION-matched reversal, not merely "the
    two strata disagree". Auto-fails if either stratum has too few
    points to fit (sign is None) -- a missing check is not a passed one."""
    return (
        abs(trial["z_lambda"]) > Z_CRIT
        and trial["d_aic_01"] > DELTA_AIC_PROMOTE
        and trial["d_aic_21"] > DELTA_AIC_PROMOTE
        and trial["sign_low"] == 1
        and trial["sign_high"] == -1
    )


def power_at_n(
    n_target: int, z_pool: np.ndarray, s_pool: np.ndarray, rel_noise: float
) -> tuple[float, float]:
    """[WITHDRAWN DESIGN, kept only for the honest old-vs-new comparison
    printed in main() -- do not use this for a real power claim.] Samples
    WITH REPLACEMENT from a combinatorial (non-disjoint) pool -- violates
    estimand.md's own SUTVA exclusion rule, see the module docstring's
    2026-09-11 correction note. Superseded by power_at_n_disjoint()."""
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


def power_at_n_disjoint(
    n_target: int, z_disjoint: np.ndarray, s_disjoint: np.ndarray, rel_noise: float
) -> tuple[float, float]:
    """CORRECTED design: z_disjoint/s_disjoint already come from a real
    cluster-disjoint matching (build_disjoint_matching()) -- every pair
    in this pool shares no cluster with any other pair in the SAME pool.
    Each Monte Carlo trial draws n_target of them WITHOUT replacement
    (`replace=False`), so within one trial no cluster and no pair repeats
    either -- the actual estimand.md-compliant unit of analysis."""
    pool_n = len(z_disjoint)
    if n_target > pool_n:
        raise ValueError(
            f"n_target={n_target} exceeds the real disjoint-pair ceiling ({pool_n}) -- "
            "not a feasible SUTVA-compliant sample size"
        )
    promote_hm = promote_h0 = 0
    for _ in range(N_MC):
        idx = rng.choice(pool_n, size=n_target, replace=False)
        z_i, s_i = z_disjoint[idx], s_disjoint[idx]
        if promote(one_trial(z_i, s_i, rel_noise, True)):
            promote_hm += 1
        if promote(one_trial(z_i, s_i, rel_noise, False)):
            promote_h0 += 1
    return promote_hm / N_MC, promote_h0 / N_MC


def main() -> None:
    print("=" * 78)
    print("STEP 1 -- real (z,s) COMBINATORIAL pair pool, broad population window")
    print("=" * 78)
    z_pool, s_pool, row, col, n_clusters = build_real_pair_pool()
    print(
        f"  N real candidate pairs, s in [{S_MIN_VALID:.0f},{S_MAX_MPC:.0f}] Mpc comoving, "
        f"z in [{Z_LOW},{Z_HIGH}]: {len(z_pool)}   (N clusters: {n_clusters})"
    )
    print(f"  z_pair range: {z_pool.min():.3f} - {z_pool.max():.3f}")
    print(f"  s_pair range: {s_pool.min():.2f} - {s_pool.max():.2f} Mpc")
    print(
        "  NOTE: this pool is COMBINATORIAL -- one cluster can appear in many\n"
        "  candidate pairs (mean 3.93, max 18). It is NOT the unit of analysis\n"
        "  estimand.md specifies; STEP 1b below builds the real, cluster-\n"
        "  disjoint matching that is."
    )

    print()
    print("=" * 78)
    print(
        "STEP 1b -- [ADDED, SUTVA correction] real cluster-disjoint matching, "
        "estimand.md's own Population/SUTVA exclusion rule made concrete"
    )
    print("=" * 78)
    # Two tie-break orders, both reported: RANDOM is the primary, honest
    # construction (no preference for small s, which would otherwise bias
    # the matched set toward exactly the high-xi_pred regime this branch's
    # own headline results live in); SMALLEST-S-FIRST is a named upper-
    # bound/sensitivity check, not the primary result.
    rng_match = np.random.default_rng(20260911)
    order_random = rng_match.permutation(len(s_pool))
    order_smallest_s = np.argsort(s_pool)

    matched_random = build_disjoint_matching(row, col, order_random, n_clusters)
    matched_smalls = build_disjoint_matching(row, col, order_smallest_s, n_clusters)

    z_disjoint = z_pool[matched_random]
    s_disjoint = s_pool[matched_random]
    xi_disjoint = xi_pred(z_disjoint, s_disjoint)
    frac_disjoint = np.mean(xi_disjoint > XI_CROSSING)

    z_disjoint_s = z_pool[matched_smalls]
    s_disjoint_s = s_pool[matched_smalls]
    xi_disjoint_s = xi_pred(z_disjoint_s, s_disjoint_s)
    frac_disjoint_s = np.mean(xi_disjoint_s > XI_CROSSING)

    print(
        f"  RANDOM-order matching (primary):      {len(matched_random)} disjoint pairs, "
        f"Positivity fraction {frac_disjoint * 100:.3f}%"
    )
    print(
        f"  smallest-s-first matching (sensitivity): {len(matched_smalls)} disjoint pairs, "
        f"Positivity fraction {frac_disjoint_s * 100:.3f}%"
    )
    print(
        "  Reading: if these fractions differ substantially, the SUTVA-\n"
        "  compliant Positivity result is sensitive to the (unspecified in\n"
        "  estimand.md) matching tie-break rule -- named explicitly, not\n"
        "  smoothed over. The RANDOM-order number is what STEP 3 below uses."
    )

    print()
    print("=" * 78)
    print(
        "STEP 2 -- Positivity check on the COMBINATORIAL pool (original, kept "
        "for continuity -- see STEP 1b above for the SUTVA-correct version)"
    )
    print("=" * 78)
    xi_all = xi_pred(z_pool, s_pool)
    print(
        f"  xi_pred(z,s) over the COMBINATORIAL pool: min={xi_all.min():.4e}  "
        f"median={np.median(xi_all):.4e}  max={xi_all.max():.4e}"
    )
    print(f"  xi_crossing = {XI_CROSSING:.4e}")
    frac_above = np.mean(xi_all > XI_CROSSING)
    print(
        f"  fraction of REAL candidate pairs with xi_pred > xi_crossing (deterministic, "
        f"no scatter, COMBINATORIAL pool): {frac_above * 100:.3f}%"
    )
    closest = np.argsort(-xi_all)[:5]
    print("  5 closest-to/over-crossing real pairs (combinatorial pool):")
    for i in closest:
        print(
            f"    z={z_pool[i]:.3f}  s={s_pool[i]:.2f} Mpc  xi_pred={xi_all[i]:.4e}"
            f"  ({'ABOVE' if xi_all[i] > XI_CROSSING else 'below'} crossing)"
        )

    print()
    print("=" * 78)
    print(
        f"STEP 3 -- Monte Carlo power (N_MC={N_MC} per cell), CORRECTED "
        "SUTVA-compliant design (sampling WITHOUT replacement from the "
        "random-order disjoint matching)"
    )
    print("=" * 78)
    ceiling = len(matched_random)
    n_scan_full = [10, 20, 30, 50, 75, 100, 150, 200, 300, 449, 500, 1000, 2000]
    n_scan = [n for n in n_scan_full if n <= ceiling]
    dropped = [n for n in n_scan_full if n > ceiling]
    if dropped:
        print(f"  Dropped from the scan (exceed the real disjoint ceiling of {ceiling}): {dropped}")
    noise_scan = [1.0, 3.0, 10.0]
    print(f"{'N_pairs':>8} {'rel_noise':>10} {'power':>8} {'false-promote':>15}")
    results = []
    for n_target in n_scan:
        for rel_noise in noise_scan:
            p_power, p_false = power_at_n_disjoint(n_target, z_disjoint, s_disjoint, rel_noise)
            results.append((n_target, rel_noise, p_power, p_false))
            print(
                f"{n_target:>8} {rel_noise:>10.1f} {p_power * 100:>7.1f}% {p_false * 100:>14.1f}%"
            )

    print()
    print("=" * 78)
    print("STEP 4 -- three-way comparison: window-based / WITHDRAWN s-dependent / CORRECTED")
    print("=" * 78)
    print(
        "  (a) Old window-based design (power_analysis_mock_catalog.py, REJECTED\n"
        "      per NR-025), N=449 (Fork-2 mid footprint): 100.0% power @3x noise\n"
        "  (b) WITHDRAWN: this script's own PRIOR run, N=449, with-replacement\n"
        "      sampling from the combinatorial pool (SUTVA-violating, see the\n"
        "      module docstring's 2026-09-11 correction note): 59.9% power @3x\n"
        "      noise, 0.1% false-promote -- do not cite this number going forward.\n"
        "  (c) CORRECTED: this run, sampling WITHOUT replacement from the real\n"
        "      cluster-disjoint matching, same three-part bar:"
    )
    match_449 = [r for r in results if r[0] == 449 and r[1] == 3.0]
    if match_449:
        print(
            f"      N=449: {match_449[0][2] * 100:.1f}% power @3x noise, "
            f"{match_449[0][3] * 100:.1f}% false-promote"
        )
    else:
        print(f"      N=449 not reachable (real disjoint ceiling: {ceiling} pairs)")
    print(
        "  Reading: the new design's THREE-part bar (beat null AND beat the\n"
        "  free-linear alternative AND show the direction-matched sign\n"
        "  reversal at XI_PEAK) is intentionally, substantially stricter than\n"
        "  the old design's one-part bar (beat null only) -- a lower power\n"
        "  number at the same N is not evidence the new design is worse, it is\n"
        "  the real, quantified cost of testing a SHARPER, more specific claim,\n"
        "  matching estimand.md's own PROMOTE region wording as closely as this\n"
        "  script operationalizes it."
    )

    print()
    print("=" * 78)
    print("What this does NOT establish")
    print("=" * 78)
    print(
        "  1. [AMENDED] The sign-near-crossing sub-check IS now implemented --\n"
        "     but as a sign-near-REVERSAL check at XI_PEAK=beta1/beta2, not\n"
        "     literally at XI_CROSSING (see that constant's own docstring for\n"
        "     why). This is a documented, honest operationalization choice,\n"
        "     not a literal match to estimand.md's exact wording.\n"
        "  2. The [20,160] Mpc population window is carried forward from the\n"
        "     old design, NOT independently re-verified against the source kSZ\n"
        "     paper's own methods section (estimand.md's own Population\n"
        "     criterion still names that as unresolved).\n"
        "  3. [RESOLVED, see FINDING_beam_blending_check.md] The small-s\n"
        "     Consistency(d) instrumental threat (CMB-beam blending) was\n"
        "     checked directly for all 306 real Positivity pairs -- only 5/306\n"
        "     (1.6%) at real risk, a small quantified correction, not open.\n"
        "  4. Real power will be lower than every number above -- these are\n"
        "     best-case, confounder-free upper bounds; the synthetic four-world\n"
        "     identifiability battery (estimand.md's own hard gate) has not run.\n"
        "  5. [ADDED, SUTVA correction] The greedy disjoint matching's tie-break\n"
        "     rule (random order, primary) is one defensible choice among several\n"
        "     -- estimand.md's own text names 'closest match on the matching\n"
        "     variables' (M, z, Env, Dyn), none of which are in this mock. STEP\n"
        "     1b's own random-vs-smallest-s comparison is the honesty check for\n"
        "     this, not a full sensitivity sweep over tie-break rules."
    )


if __name__ == "__main__":
    main()
