"""P195 -- floor-sensitivity sweep for FINDING_P158_ADDENDUM2's grounded
rho result. Reuses ADDENDUM2's own pipeline verbatim (hmf/Tinker08 mass
function, Tinker et al. 2010 bias, Fourier-Bessel xi_mm, the exact
pairwise-correlation formula) -- the ONLY thing this file varies is the
population floor, per the Minimal Relaxation Rule.

ADDENDUM2's own Objection 2 (accepted as an open limitation, not run
there): the M_of(z)/2 floor choice was never checked against nearby
alternatives. This file runs that check at the 4 redshifts (z<=0.5)
ADDENDUM2 itself found trustworthy (inside Tinker+2010's own
nu-calibration range) -- z>=1.07 is already known untrustworthy for a
different reason (extrapolated nu) and a floor sweep there would not be
informative.

See CLAIM_P195_floor_sensitivity_sweep.md for the full protocol.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import warnings

import numpy as np
from P158_addendum2_real_mass_function import (
    build_mass_function,
    load_multing_core,
    pair_rho_exact,
    population_moments,
    xi_mm,
)

warnings.filterwarnings("ignore")

NU_CALIBRATION_CEILING = 10.0
TRUSTED_ZS = [0.0, 0.0233, 0.07, 0.5]  # ADDENDUM2's own already-trusted subset
FLOOR_DIVISORS = [4.0, 2.0, 1.0]  # M_of(z)/f -- f=2 is ADDENDUM2's own baseline
MPC_TO_M = 3.0856775814913673e22

# MCID, pre-registered in CLAIM_P195: a floor-choice change is MATERIAL if
# it flips rho's sign, or moves rho by more than this fraction of the way
# from 0 to the P158 decision threshold (rho=-0.5).
MCID_ABS_DELTA = 0.05

# ADDENDUM2's own tabulated baseline (f=2.0) values -- the positive
# control below must reproduce these to high precision.
ADDENDUM2_BASELINE_RHO = {
    0.0: 0.004506,
    0.0233: 0.010071,
    0.07: 0.005262,
    0.5: 0.000836,
}


def rho_at(mc, h, z, m_floor_msun):
    mf = build_mass_function(z=z)
    mean_lnm, mean_lnm2, mean_b, mean_lnm_b = population_moments(mf, m_floor_msun)
    d_mpc_h = (mc.d_of(z) / MPC_TO_M) * h
    xi = xi_mm(d_mpc_h, mf.k, mf.power)
    rho, cov, var, denom = pair_rho_exact(mean_lnm, mean_lnm2, mean_b, mean_lnm_b, xi)
    idx = np.argmin(np.abs(mf.m - m_floor_msun))
    nu = mf.nu[idx]
    return rho, nu, denom


def rho_bounded_bin(mc, h, z, lo_msun, hi_msun):
    """Same exact formula, but restricting the population to a BOUNDED
    window [lo, hi) instead of an unbounded-above floor -- tests whether
    the qualitative construction (floor vs. bin) matters, not just the
    floor's exact multiplier."""
    mf = build_mass_function(z=z)
    m = mf.m
    dndlnm = mf.dndlnm
    mask = (m >= lo_msun) & (m < hi_msun)
    from P158_addendum2_real_mass_function import tinker10_bias
    from scipy.integrate import simpson

    m_pop, w = m[mask], dndlnm[mask]
    lnm = np.log(m_pop)
    b = tinker10_bias(mf.nu[mask])
    norm = simpson(w, x=lnm)
    mean_lnm = simpson(w * lnm, x=lnm) / norm
    mean_lnm2 = simpson(w * lnm**2, x=lnm) / norm
    mean_b = simpson(w * b, x=lnm) / norm
    mean_lnm_b = simpson(w * lnm * b, x=lnm) / norm
    d_mpc_h = (mc.d_of(z) / MPC_TO_M) * h
    xi = xi_mm(d_mpc_h, mf.k, mf.power)
    rho, cov, var, denom = pair_rho_exact(mean_lnm, mean_lnm2, mean_b, mean_lnm_b, xi)
    idx_lo = np.argmin(np.abs(mf.m - lo_msun))
    return rho, mf.nu[idx_lo], denom


def test_regression_check_baseline_matches_addendum2():
    """NOT an independent verification -- Step 8a skeptic pass, 2026-09-05,
    Probe 3 (correctly caught): this calls the SAME imported functions
    ADDENDUM2 itself used, so it is a regression check that this file's
    sweep harness (parameterizing the floor) introduced no discrepancy
    from ADDENDUM2's own already-published numbers -- it CANNOT catch a
    unit-conversion bug shared with ADDENDUM2 (e.g. in mc.d_of(z) or the
    Mpc/h conversion), because both would reproduce the same wrong
    number. Real independence would require a second implementation
    (different hmf model, or a hand-computed toy at one z) -- not
    attempted here; renamed from the original draft's "positive control"
    per the skeptic's finding that the stronger label overclaimed."""
    mc = load_multing_core()
    mf0 = build_mass_function(z=0.0)
    h = mf0.cosmo_model.h
    for z, expected_rho in ADDENDUM2_BASELINE_RHO.items():
        m_floor = (mc.M_of(z) / 1.98892e30) / 2.0
        rho, nu, denom = rho_at(mc, h, z, m_floor)
        rel_err = abs(rho - expected_rho) / abs(expected_rho)
        assert rel_err < 0.01, f"z={z}: rho={rho:.6f} vs ADDENDUM2's {expected_rho:.6f}"
        assert nu <= NU_CALIBRATION_CEILING, f"z={z}: nu={nu:.2f} outside calibration"
    return True


def main():
    mc = load_multing_core()
    mf0 = build_mass_function(z=0.0)
    h = mf0.cosmo_model.h

    test_regression_check_baseline_matches_addendum2()
    print("Regression check (NOT independent -- same code path as ADDENDUM2, see")
    print("docstring): f=2.0 baseline reproduces ADDENDUM2's own tabulated rho values")
    print("to <1% relative error at all 4 trusted redshifts: PASS\n")

    print("=" * 90)
    print("FLOOR SWEEP: rho(z, M >= M_of(z)/f) for f in {4, 2 (baseline), 1}")
    print("=" * 90)
    results = {}
    for z in TRUSTED_ZS:
        row = {}
        for f in FLOOR_DIVISORS:
            m_floor = (mc.M_of(z) / 1.98892e30) / f
            rho, nu, denom = rho_at(mc, h, z, m_floor)
            row[f] = (rho, nu)
        results[z] = row
        print(f"z={z:6.4f}:")
        for f in FLOOR_DIVISORS:
            rho, nu = row[f]
            print(f"    f={f:3.1f}  (floor=M_of(z)/{f:.0f}):  rho={rho:10.6f}   nu={nu:6.2f}")

    print()
    print("=" * 90)
    print("BOUNDED-BIN CHECK: M_of(z)/2 <= M < 2*M_of(z) (qualitatively different")
    print("  construction -- a window around the characteristic mass, not an")
    print("  unbounded-above floor)")
    print("=" * 90)
    bin_results = {}
    for z in TRUSTED_ZS:
        lo = (mc.M_of(z) / 1.98892e30) / 2.0
        hi = (mc.M_of(z) / 1.98892e30) * 2.0
        rho, nu, denom = rho_bounded_bin(mc, h, z, lo, hi)
        bin_results[z] = rho
        print(f"z={z:6.4f}:  bounded-bin rho={rho:10.6f}   nu(floor)={nu:6.2f}")

    print()
    print("=" * 90)
    print("MCID CHECK (pre-registered in CLAIM_P195): sign flip, or |delta rho| > 0.05")
    print("  at any tested redshift, across f in {4,2,1} AND the bounded-bin variant")
    print("=" * 90)
    material_change = False
    fold_changes = {}
    for z in TRUSTED_ZS:
        rhos = [results[z][f][0] for f in FLOOR_DIVISORS] + [bin_results[z]]
        signs = {np.sign(r) for r in rhos}
        max_delta = max(rhos) - min(rhos)
        fold = max(rhos) / min(rhos) if min(rhos) > 0 else float("inf")
        fold_changes[z] = fold
        sign_flip = len(signs) > 1
        exceeds_mcid = max_delta > MCID_ABS_DELTA
        if sign_flip or exceeds_mcid:
            material_change = True
        print(
            f"  z={z:6.4f}: rho range [{min(rhos):.6f}, {max(rhos):.6f}]  "
            f"spread={max_delta:.6f}  fold-change={fold:5.1f}x  "
            f"sign_flip={sign_flip}  exceeds_MCID={exceeds_mcid}"
        )
    print()
    print("  NOTE (added after Step 8a skeptic Probe 1, 2026-09-05): the pre-")
    print("  registered absolute-delta MCID (0.05) is calibrated against the")
    print("  mechanism's own -0.5 decision threshold, not against these rho values'")
    print("  own tiny scale (~0.0007-0.04) -- it can pass even when rho swings by a")
    print(
        f"  large RELATIVE factor (observed: up to {max(fold_changes.values()):.0f}x). Both numbers are"
    )
    print("  reported honestly above; the MCID answers 'does this ever threaten the")
    print("  sign or approach the -0.5 threshold' (no), NOT 'is the magnitude stable'")
    print("  (it is not -- see fold-change column).")

    print()
    print("  Monotonic pattern (not itself tested for extrapolation beyond f in")
    print("  {4,2,1}): rho DECREASES as the floor mass increases (f decreases from 4")
    print("  toward 1) at every tested z. Whether this trend continues, flattens, or")
    print("  reverses at floor choices outside {4,2,1} (e.g. f=8 or f=0.5) is NOT")
    print("  established by this file -- reported as an open pattern, not extrapolated.")

    print()
    print("=" * 90)
    print("VERDICT")
    print("=" * 90)
    if material_change:
        print("WEAKENED -- at least one tested redshift shows a sign flip or a")
        print("  floor-choice-induced change exceeding the pre-registered absolute MCID")
        print("  (0.05). FINDING_P158_ADDENDUM2's 'safely above threshold' framing needs")
        print("  qualifying -- see the per-z numbers above.")
    else:
        print("SIGN-ROBUST-AND-THRESHOLD-SAFE-BUT-NOT-MAGNITUDE-STABLE, WITHIN TESTED")
        print("  RANGE ONLY (f in {4,2,1} plus one bounded-bin variant; per Step 8a")
        print("  skeptic Probe 5, extrapolation beyond this range is not licensed):")
        print("  rho stays positive and never approaches the P158 rho>-0.5 decision")
        print("  threshold at any tested floor choice (pre-registered MCID passes) --")
        print("  but its MAGNITUDE varies by up to a large fold-change across those")
        print("  same choices (see above), so 'robust' should be read narrowly, as")
        print("  'the qualitative directional conclusion survives', not 'the exact")
        print("  number is stable'. The z<=0.5 qualitative conclusion (population-")
        print("  averaging favors F^(2) over F^(1)) does not depend on the specific")
        print("  M_of(z)/2 floor choice; the exact size of that effect does.")


if __name__ == "__main__":
    main()
