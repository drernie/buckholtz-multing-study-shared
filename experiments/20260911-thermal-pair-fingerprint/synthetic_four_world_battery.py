"""synthetic_four_world_battery.py -- estimand.md's own Pre-Data
Requirement: a synthetic identifiability battery (four mock worlds),
the hard gate before any code may touch real kSZ/tSZ data.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

Per `falsification-ladder.md` Step 2b (Oracle Adequacy Gate), applied
here exactly as `estimand.md` names it: before trusting the pipeline's
verdict on real data, check it can actually tell the states it claims
to distinguish. Four worlds, matched in sample size to the real target:

  1. World MULTING              -- the frozen (beta1,beta2) force law
     actually sources the dynamics. Pipeline SHOULD promote.
  2. World optical-depth-confounded -- no MULTING effect; a real-but-
     wrong-shaped association exists. Pipeline should NOT promote.
  3. World merger-confounded    -- no MULTING effect; a DIFFERENT
     real-but-wrong-shaped association exists (distinguishable from
     world 2). Pipeline should NOT promote.
  4. World null                 -- no association at all (pure noise).
     Pipeline should NOT promote.

Reuses, does not re-derive: the entire fitting/promote() pipeline from
`power_analysis_s_dependent.py` (SUTVA-corrected 2026-09-11), via
`fit_and_check()`, so the battery tests the EXACT SAME pipeline the
power analysis reports numbers for -- not a separate, possibly-drifted
copy.

Operationalizing worlds 2/3 -- an honest, stated limitation: this mock
has no explicit per-cluster K/G/Dyn variables (only the deterministic
z-trajectory-based xi_pred(z,s), per this whole branch's own C1
"fingerprint" scope). The two confounded worlds are therefore
operationalized as the two MOST DIRECTLY TESTABLE proxies available
inside the existing regressor set, not as a literal G->tau or Dyn
simulation:

  World 2 (optical-depth-confounded) -> a LINEAR-in-xi_pred signal
    (exactly Model 2's own regressor) -- "some real xi_pred-correlated
    channel exists, but not the specific S_M-quadratic-reversal shape."
  World 3 (merger-confounded) -> a signal driven by 1/s ALONE, with NO
    z-dependence (unlike real xi_pred, which is Q(z)*(45/s) -- entangles
    z and s together) -- "a real separation-driven channel exists,
    structurally distinct from xi_pred's own z-entangled form."

Both are matched in amplitude to World 1's own signal RMS (same
relative-noise convention as power_analysis_s_dependent.py, FINDING_
P191-P194 precedent) -- a fair, non-strawman alternative, not a
signal too weak to ever be mistaken for the real thing.
"""

from __future__ import annotations

import numpy as np
import power_analysis_s_dependent as pad

rng = np.random.default_rng(20260911)

N_MC = 4000
REL_NOISE = 3.0  # the same headline noise level used throughout this branch
N_SCAN = [100, 449, 1000]  # a modest scan, not the full 13-point grid --
# this battery answers "does the pipeline discriminate," not "what is
# the power curve" (power_analysis_s_dependent.py already answers that)


def world_multing(z_i: np.ndarray, s_i: np.ndarray, rel_noise: float) -> dict:
    """World 1: reuses pad.one_trial() directly -- the real generator,
    unchanged."""
    return pad.one_trial(z_i, s_i, rel_noise, h_m_true=True)


def world_null(z_i: np.ndarray, s_i: np.ndarray, rel_noise: float) -> dict:
    """World 4: reuses pad.one_trial() directly -- pure noise, no signal."""
    return pad.one_trial(z_i, s_i, rel_noise, h_m_true=False)


def world_optical_depth_confounded(z_i: np.ndarray, s_i: np.ndarray, rel_noise: float) -> dict:
    """World 2: y is LINEAR in xi_pred(z,s) -- Model 2's own regressor,
    not Model 1's S_M quadratic-reversal shape. Amplitude matched to
    World 1's own signal RMS at the same (z,s) sample, via a real
    reference computation (not an arbitrary constant)."""
    n = len(z_i)
    xi_center = pad.xi_pred(z_i, s_i)
    xi_a = rng.lognormal(mean=np.log(xi_center) - 0.5 * pad.SIGMA_LN**2, sigma=pad.SIGMA_LN)
    xi_b = rng.lognormal(mean=np.log(xi_center) - 0.5 * pad.SIGMA_LN**2, sigma=pad.SIGMA_LN)
    signal = pad.s_m_pair(xi_a, xi_b)  # still needed: Model 1's own regressor
    reference_rms = np.std(signal)  # World 1's own signal scale, for a fair amplitude match

    linear_confound = xi_center - np.mean(xi_center)
    gamma = reference_rms / (np.std(linear_confound) + 1e-300)
    confound_signal = gamma * linear_confound

    noise_sigma = rel_noise * reference_rms
    y = confound_signal + rng.normal(0.0, noise_sigma, n)
    return pad.fit_and_check(xi_center, signal, y)


def world_merger_confounded(z_i: np.ndarray, s_i: np.ndarray, rel_noise: float) -> dict:
    """World 3: y depends on 1/s ALONE, with no z-dependence -- unlike
    real xi_pred(z,s), which entangles z (via Q(z)) and s together.
    A structurally distinct confound from World 2, not a relabeling of
    the same one."""
    n = len(z_i)
    xi_center = pad.xi_pred(z_i, s_i)
    xi_a = rng.lognormal(mean=np.log(xi_center) - 0.5 * pad.SIGMA_LN**2, sigma=pad.SIGMA_LN)
    xi_b = rng.lognormal(mean=np.log(xi_center) - 0.5 * pad.SIGMA_LN**2, sigma=pad.SIGMA_LN)
    signal = pad.s_m_pair(xi_a, xi_b)
    reference_rms = np.std(signal)

    inv_s = 1.0 / s_i
    merger_confound = inv_s - np.mean(inv_s)
    delta = reference_rms / (np.std(merger_confound) + 1e-300)
    confound_signal = delta * merger_confound

    noise_sigma = rel_noise * reference_rms
    y = confound_signal + rng.normal(0.0, noise_sigma, n)
    return pad.fit_and_check(xi_center, signal, y)


WORLDS = {
    "1_MULTING": (world_multing, "SHOULD promote"),
    "2_optical_depth_confounded": (world_optical_depth_confounded, "should NOT promote"),
    "3_merger_confounded": (world_merger_confounded, "should NOT promote"),
    "4_null": (world_null, "should NOT promote"),
}


def run_world(
    world_fn, n_target: int, z_disjoint: np.ndarray, s_disjoint: np.ndarray, rel_noise: float
) -> float:
    """Same SUTVA-compliant sampling as power_analysis_s_dependent.py's
    own power_at_n_disjoint(): without-replacement draws from a real
    cluster-disjoint matching, not the combinatorial pool."""
    pool_n = len(z_disjoint)
    promoted = 0
    for _ in range(N_MC):
        idx = rng.choice(pool_n, size=n_target, replace=False)
        z_i, s_i = z_disjoint[idx], s_disjoint[idx]
        trial = world_fn(z_i, s_i, rel_noise)
        if pad.promote(trial):
            promoted += 1
    return promoted / N_MC


def main() -> None:
    print("=" * 78)
    print("STEP 1 -- real cluster-disjoint matching (SUTVA-compliant, same as")
    print("          power_analysis_s_dependent.py's own corrected design)")
    print("=" * 78)
    z_pool, s_pool, row, col, n_clusters = pad.build_real_pair_pool()
    order_random = np.random.default_rng(20260911).permutation(len(s_pool))
    matched = pad.build_disjoint_matching(row, col, order_random, n_clusters)
    z_disjoint, s_disjoint = z_pool[matched], s_pool[matched]
    print(f"  Real disjoint matching: {len(matched)} pairs (ceiling for N_SCAN below)")

    n_scan_feasible = [n for n in N_SCAN if n <= len(matched)]
    dropped = [n for n in N_SCAN if n > len(matched)]
    if dropped:
        print(f"  Dropped (exceed the disjoint ceiling): {dropped}")

    print()
    print("=" * 78)
    print(f"STEP 2 -- four-world battery, N_MC={N_MC} per (world, N) cell, rel_noise={REL_NOISE}x")
    print("=" * 78)
    print(f"{'world':>30} {'N_pairs':>8} {'promote rate':>13}  expectation")
    results = {}
    for world_name, (world_fn, expectation) in WORLDS.items():
        results[world_name] = {}
        for n_target in n_scan_feasible:
            rate = run_world(world_fn, n_target, z_disjoint, s_disjoint, REL_NOISE)
            results[world_name][n_target] = rate
            print(f"{world_name:>30} {n_target:>8} {rate * 100:>12.1f}%  {expectation}")

    print()
    print("=" * 78)
    print("VERDICT -- Oracle Adequacy Gate (falsification-ladder.md Step 2b)")
    print("=" * 78)
    hm_rates = results["1_MULTING"]
    confound_worlds = ["2_optical_depth_confounded", "3_merger_confounded", "4_null"]
    max_confound_rate = max(results[w][n] for w in confound_worlds for n in n_scan_feasible)
    min_multing_rate = min(hm_rates[n] for n in n_scan_feasible)
    print(f"  Min World-1 (MULTING) promote rate across the scan: {min_multing_rate * 100:.1f}%")
    print(f"  Max confound/null promote rate across worlds 2/3/4: {max_confound_rate * 100:.1f}%")
    if max_confound_rate <= 0.05 and min_multing_rate > max_confound_rate:
        print(
            "  ADEQUATE: the pipeline separates World 1 from worlds 2/3/4 at every "
            "scanned N -- not ORACLE_INADEQUATE on this battery."
        )
    else:
        print(
            "  ORACLE_INADEQUATE risk: a confounded/null world promotes at a rate "
            "not clearly below World 1's own rate, or above a 5% nominal bound -- "
            "per falsification-ladder.md Step 2b, this must be fixed before any "
            "verdict on real data counts as evidence."
        )

    print()
    print("=" * 78)
    print("What this does NOT establish")
    print("=" * 78)
    print(
        "  1. Worlds 2/3 are OPERATIONALIZED proxies (linear-in-xi_pred; pure\n"
        "     1/s with no z-dependence) for 'optical-depth-confounded' and\n"
        "     'merger-confounded' -- this mock has no explicit per-cluster\n"
        "     K/G/Dyn variables to simulate the real DAG paths literally. A\n"
        "     more faithful simulation would need those variables built first.\n"
        "  2. This is still entirely synthetic -- passing this battery clears\n"
        "     estimand.md's own hard pre-data gate, it does not touch real\n"
        "     kSZ/tSZ data or validate anything about MULTING itself.\n"
        "  3. Only rel_noise=3x is scanned here, not the full 1x/3x/10x grid\n"
        "     power_analysis_s_dependent.py already covers for World 1 alone.\n"
        "  4. Not a claim about MULTING (NO_AUTHOR_ERROR) -- entirely about\n"
        "     whether this project's own pipeline can tell these four\n"
        "     specific synthetic worlds apart."
    )


if __name__ == "__main__":
    main()
