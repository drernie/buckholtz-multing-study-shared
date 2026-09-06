"""E18 -- extends the fresh, outside-party rerun of TJB's own
independently-implemented verification script (`multing_fit_rerun.py`,
itself a path-fixed-only copy of the archive's own
`independent_verification/multing_fit.py`) to close two gaps named in
CLAIM_E18: (1) only 1 of 7 Table II rows was checked so far, (2) only a
local, nearby-start re-optimization existed anywhere in this project
(FINDING_P176's own "does NOT establish" #5), never a genuinely wide
global search.

Reuses `multing_fit_rerun.py`'s own independently-implemented physics
functions (H_of_z_vec, chi2_of) unchanged -- this file adds only the
7-row loop and the global-optimizer check, no new physics.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
import yaml
from multing_fit_rerun import _HERE, H0_planck_kms, chi2_of
from multing_fit_rerun import Om_planck as _OM_PLANCK_ORIGINAL

ASSUMPTIONS_PATH = f"{_HERE}/assumptions.yaml"
with open(ASSUMPTIONS_PATH) as f:
    _A = yaml.safe_load(f)

TABLE_II = _A["fitted_configurations"]


def reproduce_all_rows():
    """Positive control: chi2 at each of TJB's own 7 published
    (beta1, beta2, H0_anchor) triples, compared to his own stated chi2."""
    results = {}
    for name, row in TABLE_II.items():
        chi2, _Hmod = chi2_of(row["beta_1"], row["beta_2"], row["H0_anchor_kms"])
        results[name] = {
            "chi2_reproduced": chi2,
            "chi2_stated": row["chi2_33"],
            "rel_diff_pct": 100.0 * abs(chi2 - row["chi2_33"]) / row["chi2_33"],
        }
    return results


def reoptimize_fixed_h0_anchor_rows(seed=20260906, maxiter=2000, popsize=40):
    """Closes a real gap: reproduce_all_rows() above only evaluates chi2
    AT TJB's own already-reported (beta1,beta2) for the 6 fixed-H0_anchor
    rows -- that only confirms the forward chi2 FUNCTION matches, not
    that an independent optimizer recovers those same beta values from
    scratch. This function independently re-optimizes beta1,beta2 ONLY
    (H0_anchor held fixed at each row's own stated value) via
    differential_evolution, for all 6 non-free rows, from no starting
    guess at all (a global 2D search, not a local one).

    maxiter/popsize default to the full, FINDING-documented rigorous
    search (2000/40, ~1.6e5 evaluations/row); pytest's own regression
    test passes a much smaller budget for CI speed -- the full-rigor
    numbers are locked into FINDING_E18's own results, this is a
    lighter-weight sanity check that the machinery still works and
    lands in the right basin, not a re-run of the full search."""
    from scipy.optimize import differential_evolution

    results = {}
    for name, row in TABLE_II.items():
        if name == "unconstrained_spotlighted":
            continue  # already globally re-optimized in Part B (3 free params)
        h0a_fixed = row["H0_anchor_kms"]

        def objective(p, h0a=h0a_fixed):
            b1, b2 = p
            if b1 <= 0 or b2 <= 0:
                return 1e12
            val, _ = chi2_of(b1, b2, h0a)
            return val if np.isfinite(val) else 1e12

        bounds = [(1.0e9, 1.0e11), (1.0e16, 1.0e19)]  # 2 / 3 orders of magnitude
        res = differential_evolution(
            objective, bounds, seed=seed, maxiter=maxiter, popsize=popsize, tol=1e-12, polish=True
        )
        results[name] = {
            "beta_1_reopt": res.x[0],
            "beta_2_reopt": res.x[1],
            "chi2_reopt": res.fun,
            "beta_1_stated": row["beta_1"],
            "beta_2_stated": row["beta_2"],
            "chi2_stated": row["chi2_33"],
        }
    return results


GLOBAL_BOUNDS = [
    (1.0e9, 1.0e11),
    (1.0e16, 1.0e19),
    (55.0, 90.0),
]  # 2/3 orders of magnitude on beta1/beta2
GLOBAL_SEEDS = (20260906, 1, 2)  # multi-seed robustness, per Step 8a skeptic point 2


def global_search_unconstrained_row(seed=20260906, bounds=None):
    """A genuinely different, population-based global optimizer
    (differential_evolution, not Nelder-Mead from a nearby guess) over a
    bound spanning 2-3 orders of magnitude in beta1/beta2 (not just a
    single decade around the known answer), to check for a missed global
    minimum or an undiscovered degenerate solution TJB's own local
    search did not report. Bounds/seed reported explicitly, not just
    asserted "wide" -- per Step 8a skeptic point 2."""
    from scipy.optimize import differential_evolution

    def objective(p):
        b1, b2, h0a = p
        if b1 <= 0 or b2 <= 0 or h0a <= 0:
            return 1e12
        val, _ = chi2_of(b1, b2, h0a)
        return val if np.isfinite(val) else 1e12

    result = differential_evolution(
        objective,
        bounds or GLOBAL_BOUNDS,
        seed=seed,
        maxiter=2000,
        popsize=40,
        tol=1e-12,
        mutation=(0.5, 1.5),
        recombination=0.7,
        polish=True,
    )
    return result


def test_positive_control_reproduces_published_row():
    """The archive's own already-published unconstrained_spotlighted row
    must reproduce to <1% -- this is TJB's own reported value, an
    external, falsifiable check."""
    row = TABLE_II["unconstrained_spotlighted"]
    chi2, _ = chi2_of(row["beta_1"], row["beta_2"], row["H0_anchor_kms"])
    rel = 100.0 * abs(chi2 - row["chi2_33"]) / row["chi2_33"]
    assert rel < 1.0, (chi2, row["chi2_33"], rel)


def test_negative_control_perturbed_om_changes_chi2_substantially():
    """Perturbing Om_planck by a large, obviously-wrong amount must
    change chi2 substantially -- confirms the reproduction is sensitive
    to inputs, not silently returning a cached/hardcoded number."""
    import multing_fit_rerun as m

    row = TABLE_II["unconstrained_spotlighted"]
    chi2_normal, _ = chi2_of(row["beta_1"], row["beta_2"], row["H0_anchor_kms"])
    original = m.Om_planck
    try:
        m.Om_planck = 0.05  # obviously wrong, far from Planck's 0.315
        chi2_perturbed, _ = chi2_of(row["beta_1"], row["beta_2"], row["H0_anchor_kms"])
    finally:
        m.Om_planck = original
    rel_shift = abs(chi2_perturbed - chi2_normal) / chi2_normal
    assert rel_shift > 0.5, (chi2_normal, chi2_perturbed, rel_shift)


if __name__ == "__main__":
    test_positive_control_reproduces_published_row()
    print("PC1 unconstrained_spotlighted row reproduces to <1%: PASS")

    test_negative_control_perturbed_om_changes_chi2_substantially()
    print("NC1 perturbed Om_planck changes chi2 by >50% (sensitivity confirmed): PASS\n")

    print("=" * 100)
    print("PART A -- chi2 reproduction across ALL 7 Table II rows (own published triples)")
    print(
        f"(Confirmed: Om_planck={_OM_PLANCK_ORIGINAL}, H0_planck_kms={H0_planck_kms} -- unchanged)"
    )
    print("=" * 100)
    row_results = reproduce_all_rows()
    print(f"{'row':<28} {'chi2 (ours)':>13} {'chi2 (stated)':>14} {'rel diff':>10}")
    max_rel_diff = 0.0
    for name, r in row_results.items():
        if "chi2_33" not in TABLE_II[name]:
            continue
        max_rel_diff = max(max_rel_diff, r["rel_diff_pct"])
        print(
            f"{name:<28} {r['chi2_reproduced']:13.4f} {r['chi2_stated']:14.4f} "
            f"{r['rel_diff_pct']:9.3f}%"
        )
    print(f"\n  Max relative difference across all 7 rows: {max_rel_diff:.3f}%")
    print(
        f"  MCID (>1%): {'MATERIAL DISCREPANCY' if max_rel_diff > 1.0 else 'all 7 rows reproduce -- no discrepancy'}"
    )

    print("\n" + "=" * 100)
    print("PART A2 -- independent 2D re-optimization (beta1,beta2) for the 6 FIXED-H0_anchor rows")
    print(
        "(closes the forward-evaluation-only gap in Part A: global search from NO starting guess)"
    )
    print("=" * 100)
    reopt_results = reoptimize_fixed_h0_anchor_rows()
    print(
        f"{'row':<24} {'chi2 reopt':>11} {'chi2 stated':>12} {'diff':>9} {'b1 shift%':>10} {'b2 shift%':>10}"
    )
    max_reopt_diff = 0.0
    for name, r in reopt_results.items():
        chi2_diff_pct = 100.0 * abs(r["chi2_reopt"] - r["chi2_stated"]) / r["chi2_stated"]
        b1_shift = 100.0 * abs(r["beta_1_reopt"] - r["beta_1_stated"]) / r["beta_1_stated"]
        b2_shift = 100.0 * abs(r["beta_2_reopt"] - r["beta_2_stated"]) / r["beta_2_stated"]
        max_reopt_diff = max(max_reopt_diff, chi2_diff_pct)
        print(
            f"{name:<24} {r['chi2_reopt']:11.4f} {r['chi2_stated']:12.4f} "
            f"{chi2_diff_pct:8.3f}% {b1_shift:9.3f}% {b2_shift:9.3f}%"
        )
    print(
        f"\n  Max chi2 relative difference across all 6 independently-reoptimized rows: {max_reopt_diff:.3f}%"
    )
    print(
        f"  MCID (>1%): {'MATERIAL DISCREPANCY' if max_reopt_diff > 1.0 else 'all 6 rows independently re-optimize to published values -- no discrepancy'}"
    )

    print("\n" + "=" * 100)
    print("PART B -- global search (differential_evolution, not local Nelder-Mead), MULTI-SEED")
    print(
        f"bounds (2-3 orders of magnitude, EXPLICIT, per Step 8a skeptic point 2): "
        f"beta_1 in {GLOBAL_BOUNDS[0]}, beta_2 in {GLOBAL_BOUNDS[1]}, H0_anchor in {GLOBAL_BOUNDS[2]}"
    )
    print(f"seeds: {GLOBAL_SEEDS}")
    print("=" * 100)
    row = TABLE_II["unconstrained_spotlighted"]
    seed_results = []
    for s in GLOBAL_SEEDS:
        res = global_search_unconstrained_row(seed=s)
        seed_results.append((s, res.x[0], res.x[1], res.x[2], res.fun))
        print(
            f"  seed={s:>10}: beta_1={res.x[0]:.6e}  beta_2={res.x[1]:.6e}  "
            f"H0_anchor={res.x[2]:.4f}  chi2={res.fun:.4f}"
        )
    chi2_values = [r[4] for r in seed_results]
    best_seed_result = min(seed_results, key=lambda r: r[4])
    b1_g, b2_g, h0a_g, chi2_g = (
        best_seed_result[1],
        best_seed_result[2],
        best_seed_result[3],
        best_seed_result[4],
    )
    print(
        f"\n  chi2 spread across {len(GLOBAL_SEEDS)} seeds: min={min(chi2_values):.4f}  max={max(chi2_values):.4f}"
    )
    print(
        f"  best-of-seeds: beta_1={b1_g:.6e}, beta_2={b2_g:.6e}, H0_anchor={h0a_g:.4f}, chi2={chi2_g:.4f}"
    )
    print(f"  published chi2 = {row['chi2_33']:.4f}")
    delta = chi2_g - row["chi2_33"]
    print(f"  delta = {delta:+.4f}")
    print(
        f"  MCID (global chi2 more than 1 unit BELOW published): "
        f"{'MATERIAL -- a better fit exists that TJB did not report' if delta < -1.0 else 'not material -- no better fit found in the wide, multi-seed search'}"
    )
    # Distinct-solution check: is the global optimum near the published point?
    b1_shift_pct = 100.0 * abs(b1_g - row["beta_1"]) / row["beta_1"]
    b2_shift_pct = 100.0 * abs(b2_g - row["beta_2"]) / row["beta_2"]
    print(
        f"\n  Global-optimum (beta_1,beta_2) vs published: "
        f"{b1_shift_pct:.2f}% / {b2_shift_pct:.2f}% away"
    )
    print("  (a large % shift here with chi2 still close to published would flag a genuinely")
    print("   DISTINCT degenerate solution -- consistent with the beta1-beta2 near-degeneracy")
    print("   FINDING_P176 already established, not a red flag by itself.)")
