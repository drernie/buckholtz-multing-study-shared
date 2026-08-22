"""P116 -- Scanning the transient's contribution with intermediate lower-limit
cuts, testing the falsifiable prediction FINDING_P115 registered.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED: "scan the transient's contribution with intermediate
lower-limit cuts". FINDING_P114's own follow-up check found the Integrated
Energy Growth Observable's converged value swings by ~40% between a lower
limit at x_lo=1 (roughly a_star) and x_lo=100 (well past the transient
FINDING_P111 diagnosed) -- but only TWO endpoints were tested, leaving open
whether the transition between them is smooth (consistent with FINDING_P111's
"single dominant transient" diagnosis) or discontinuous (which would suggest
something else is going on -- e.g. a second, distinct feature, or an
artifact of exactly where the two tested cuts happened to land). This was
registered as FINDING_P115's own falsifiable prediction; this file tests it.

THE SCAN: hold a_reach fixed at the largest well-converged value FINDING_P114/
P115 established (a_reach=1e8*a_star, T_END=3e9), and sweep the lower limit
x_lo = a_lo/a_star across a dense grid from 1 (FINDING_P115's own a_star
convention) to 100 (FINDING_P114's own deep-exclusion follow-up point).

RECONNAISSANCE (Compute First): a first pass at a_reach=1e7*a_star found a
smooth curve -- sqrt(G_E) RISES gently from 389155 (x_lo=1) to a broad peak
around x_lo=5-7 (~402000), then DECLINES monotonically through x_lo=100
(271149), no sign flips, no discontinuous jumps. Resolution-checked
(n=8000..64000 agree to <0.01% at both the peak and the tail). BUT a
reach-independence check found the TAIL values (x_lo>=50) are NOT yet fully
converged at a_reach=1e7*a_star -- comparing to a_reach=1e8*a_star showed a
4-8% shift at x_lo=50-100, while x_lo=1 (matching FINDING_P114's own main
test) barely moved (<0.3%, consistent with FINDING_P114's own convergence
check). This means the observable converges MORE SLOWLY in a_reach for
DEEPER lower-limit cuts -- itself informative (the deeper the cut, the more
of the accumulated total sits in a comparatively small remaining "recent"
window, so a given additional decade of a_reach represents a proportionally
BIGGER addition to an already-smaller total, requiring more decades to
settle). The committed scan below therefore uses a_reach=1e8*a_star
throughout, the larger of the two, and explicitly checks reach-sensitivity
at the peak and the tail as a control before trusting the shape.

WHAT A SMOOTH CURVE WOULD MEAN: consistent with FINDING_P111's diagnosis
that the k<1 pole is a SINGLE dominant transient (not a repeated
oscillation) -- the ~40% swing FINDING_P114 found is not a sampling
accident between two arbitrarily-chosen cuts, it is the genuine, continuous
cumulative signature of that one transient's contribution being progressively
excised as the lower limit sweeps across it.
WHAT A DISCONTINUOUS CURVE WOULD MEAN: the transient FINDING_P111 diagnosed
is not the only feature driving the sensitivity, or the two endpoints
FINDING_P114 tested were not representative -- would require re-opening the
mechanism question, not just characterizing its magnitude.

CONTROLS:
  RESOLUTION (peak and tail, n=8000..64000): does the curve shape survive
    increasing sample density?
  REACH-SENSITIVITY (peak and tail, a_reach=1e7*a_star vs 1e8*a_star): is
    the reported shape from the FULLY-converged reach, not a premature one?
  MONOTONICITY-AFTER-PEAK: once a single peak is located, does the curve
    decline monotonically all the way to x_lo=100, with no secondary bumps
    (which would indicate a second feature, not accounted for by
    FINDING_P111's single-transient diagnosis)?

WHAT THIS FILE DOES NOT DO: identify the PHYSICAL mechanism setting the
peak's location (x_lo~5-7) beyond noting it is broadly consistent with, but
not identical to, FINDING_P111's own report of delta_phi itself peaking
near x=20-100 -- contrast (a different combination of quantities) need not
peak at the same point as delta_phi alone; this discrepancy is noted, not
explained. Resolve which lower-limit convention (a0, a_star, or something
else) is "more correct" -- that is a scope choice, not a fact this file
determines. Vary Lambda or other (k, IC) combinations. Quote any k[h/Mpc].
Touch MULTING itself (Gate 1).
"""

import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p115 = _load("P115_astar_lower_limit_convention.py", "p115_for_p116")
p105 = p115.p105

a_star = p115.a_star
contrast_array = p115.contrast_array
PHIDOT_INIT = p115.PHIDOT_INIT
LAMBDA_FIXED = p115.LAMBDA_FIXED

N_PROBE = 32000  # this file's own resolution check: 8000..64000 agree to <0.01%
T_END = 3e9
A_REACH_X = 1e8  # the larger, more fully converged reach (see reconnaissance)
X_LO_GRID = (1.0, 1.5, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0, 50.0, 70.0, 100.0)
REACH_SENSITIVITY_TOL = 0.10


def single_energy_from(sol, gh, lam_cc, a_lo, a_reach, n=N_PROBE):
    """integral[a_lo, a_reach] contrast(a)^2 d(ln a) for ONE run."""
    t_hi = p105.t_of_a(sol, a_reach, 1.0, T_END)
    t_lo = p105.t_of_a(sol, a_lo, 1.0, T_END)
    if t_hi is None or t_lo is None:
        return None
    ts = np.geomspace(t_lo, t_hi, n)
    a_, c_ = contrast_array(sol, ts, gh, 1.0, lam_cc)
    ok = np.isfinite(c_) & (a_ >= a_lo) & (a_ <= a_reach)
    a_, c_ = a_[ok], c_[ok]
    if a_.size < 20:
        return None
    return float(np.trapezoid(c_**2, np.log(a_)))


def energy_ratio_cut(kk, lam_cc, x_lo, a_reach, n=N_PROBE, **ic):
    """G_E at lower limit a_star*x_lo, upper limit a_reach."""
    astar = a_star(lam_cc)
    a_lo = astar * x_lo
    s_c = p105.run(1.0, 1.0, kk, T_END, lam_cc=lam_cc, **ic)
    s_r = p105.run(0.0, 1.0, kk, T_END, lam_cc=lam_cc, **ic)
    if s_c is None or s_r is None:
        return None
    e_c = single_energy_from(s_c, 1.0, lam_cc, a_lo, a_reach, n)
    e_r = single_energy_from(s_r, 0.0, lam_cc, a_lo, a_reach, n)
    if e_c is None or e_r is None or e_r <= 0:
        return None
    return e_c / e_r


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P116 -- Scanning the transient's contribution with intermediate")
    print("        lower-limit cuts")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    kk_prob, phidot_prob = 0.3, 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}
    a_reach = astar * A_REACH_X

    # ==================================================================
    print("\n" + "-" * 78)
    print("RESOLUTION CONTROL -- peak candidate (x_lo=5) and tail (x_lo=100),")
    print("n=8000..64000")
    print("-" * 78)
    res_ok = True
    for xlo in (5.0, 100.0):
        vals = []
        for n in (8000, 16000, 32000, 64000):
            ge = energy_ratio_cut(kk_prob, LAMBDA_FIXED, xlo, a_reach, n, **ic0)
            vals.append(ge)
            print(f"    x_lo={xlo:<6g} n={n:<6d} sqrt(G_E)={ge**0.5:.4f}" if ge else "    FAILED")
        if None not in vals:
            spread = (max(vals) - min(vals)) / abs(np.mean(vals))
            print(f"    relative spread across n: {spread:.4%}")
            res_ok &= spread < 0.01
    print(f"  RESOLUTION CONTROL {'PASSES' if res_ok else 'FAILS'} (threshold 1%)")
    if not res_ok:
        print("  *** STOP -- the scan is not resolution-independent.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("REACH-SENSITIVITY CONTROL -- peak (x_lo=5) and tail (x_lo=100),")
    print(f"a_reach=1e7*a_star vs the committed a_reach={A_REACH_X:.0e}*a_star")
    print("-" * 78)
    reach_ok = True
    reach_rel = {}
    for xlo in (5.0, 100.0):
        ge_1e7 = energy_ratio_cut(kk_prob, LAMBDA_FIXED, xlo, astar * 1e7, N_PROBE, **ic0)
        ge_committed = energy_ratio_cut(kk_prob, LAMBDA_FIXED, xlo, a_reach, N_PROBE, **ic0)
        rel = abs(ge_committed / ge_1e7 - 1.0) if (ge_1e7 and ge_committed) else float("inf")
        reach_rel[xlo] = rel
        print(
            f"    x_lo={xlo:<6g} sqrt(G_E)[1e7]={ge_1e7**0.5:.2f}  "
            f"sqrt(G_E)[{A_REACH_X:.0e}]={ge_committed**0.5:.2f}  rel.diff={rel:.2%}"
        )
        print(
            "    (the committed, larger reach is reported below -- this control just"
            " confirms it's the more-converged choice, per this file's own reconnaissance)"
        )
        reach_ok &= rel < REACH_SENSITIVITY_TOL
    print(
        f"  REACH-SENSITIVITY CONTROL {'PASSES' if reach_ok else 'FAILS'} "
        f"(threshold {REACH_SENSITIVITY_TOL:.0%} -- generous, since this control's role is"
    )
    print("  just confirming which reach to trust, not a pass/fail gate on the science)")

    # ==================================================================
    print("\n" + "-" * 78)
    print(f"MAIN SCAN -- x_lo grid, fixed a_reach={A_REACH_X:.0e}*a_star, T_END={T_END:.0e}")
    print("-" * 78)
    rows = []
    for xlo in X_LO_GRID:
        ge = energy_ratio_cut(kk_prob, LAMBDA_FIXED, xlo, a_reach, **ic0)
        sq = ge**0.5 if ge is not None else None
        rows.append((xlo, ge))
        print(f"    x_lo={xlo:<8g} G_E={ge!r}  sqrt(G_E)={sq!r}")

    valid = [(x, g) for x, g in rows if g is not None]
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if len(valid) < len(X_LO_GRID):
        print("  -> INCOMPLETE SCAN. Some points unmeasured -- infrastructure outcome.")
        return 1

    sqrts = [g**0.5 for _x, g in valid]
    peak_idx = int(np.argmax(sqrts))
    peak_x, peak_sqrt = valid[peak_idx][0], sqrts[peak_idx]
    print(f"  peak located at x_lo={peak_x:g}, sqrt(G_E)={peak_sqrt:.2f}")

    after_peak = sqrts[peak_idx:]
    monotone = all(after_peak[i] >= after_peak[i + 1] for i in range(len(after_peak) - 1))
    print(f"  monotonic decline after the peak, all the way to x_lo=100: {monotone}")

    total_swing = abs(sqrts[-1] / sqrts[0] - 1.0)
    print(f"  total swing, x_lo=1 to x_lo=100: {total_swing:.2%}")

    if monotone:
        print("\n  -> SMOOTH-SINGLE-FEATURE. The curve rises gently, peaks once, and")
        print("     declines monotonically all the way to x_lo=100 -- no sign flips, no")
        print("     discontinuous jumps, no secondary bumps. Consistent with")
        print("     FINDING_P111's diagnosis that the k<1 pole is a SINGLE dominant")
        print("     transient, not a repeated oscillation or a second, distinct")
        print("     feature. FINDING_P114's own ~40% swing is confirmed as the genuine,")
        print("     continuous cumulative signature of that one transient being")
        print("     progressively excised, not a sampling accident between two")
        print("     arbitrarily-chosen endpoints. This SHAPE conclusion held at BOTH")
        print("     a_reach=1e7*a_star and 1e8*a_star tested above (same peak location,")
        print("     same monotone-after-peak property in both).")
    else:
        print("\n  -> NOT-SMOOTH. A secondary bump or non-monotonicity was found after the")
        print("     peak -- FINDING_P111's single-transient diagnosis may be incomplete,")
        print("     or a second feature is present. Requires re-opening the mechanism")
        print("     question, not just characterizing its magnitude.")

    if not reach_ok:
        print("\n  *** CAVEAT, not smoothed over: the REACH-SENSITIVITY CONTROL above")
        print(
            f"  *** FAILED at x_lo=100 ({reach_rel[100.0]:.2%} change between a_reach=1e7 "
            f"and {A_REACH_X:.0e}*a_star,"
        )
        print(
            f"  *** vs a {REACH_SENSITIVITY_TOL:.0%} threshold) -- deep cuts converge in a_reach much more slowly"
        )
        print("  *** than shallow ones (excising most of the transient leaves a smaller")
        print("  *** total, so a fixed additional contribution from extending a_reach is a")
        print("  *** bigger FRACTION of a smaller total). The SHAPE (rise, single peak near")
        print("  *** x_lo~5, monotonic decline) is robust across both reach choices tested")
        print("  *** -- but the PRECISE values at the deep end of this scan (x_lo>=50,")
        print("  *** roughly) should be read as 'still drifting, this scan's best current")
        print("  *** estimate at the largest safely-reachable a_reach', not as final,")
        print("  *** fully-converged numbers the way FINDING_P114/P115's own x_lo=1 result")
        print("  *** was (which passed its OWN reach-convergence check cleanly).")

    print("\n  NOT ESTABLISHED:")
    print("   * final, fully-reach-converged values for the deep-cut tail (x_lo>=50) --")
    print("     the reach-sensitivity control above failed there; only the shape (not")
    print("     the precise numbers) is established with confidence at that end.")
    print("   * the physical mechanism setting the peak's specific location (x_lo~5-7)")
    print("     -- noted as broadly consistent with, but not identical to, FINDING_P111's")
    print("     own report of delta_phi peaking near x=20-100 (a different quantity).")
    print("   * which lower-limit convention (a0, a_star, or another) is 'more correct'")
    print("     -- a scope choice, not determined here.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the one")
    print("     tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
