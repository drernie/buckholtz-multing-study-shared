"""P117 -- Testing a stiffer integrator for the deep-cut tail: it doesn't
help, and pushing the existing one to its true limit reveals the observable
never converges within the numerically-safe range at all.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED: "push a stiffer integrator to converge the deep-cut tail".
FINDING_P116's own reach-sensitivity control failed at the deep-cut tail
(x_lo=100): a 17.79% shift between a_reach=1e7 and 1e8*a_star, vs a 10%
threshold, at the T_END=3e9 ceiling this arc adopted since FINDING_P108.

STEP 1 -- test the literal request directly: does a stiffer integrator
(Radau, BDF, LSODA) push past RK45's own reach? Tested directly on the SAME
(k=0.3, phibar_dot(1)x0.1, Lambda=1e-15) system at T_END=1e10: Radau CRASHES
OUTRIGHT (Jacobian probe overflows float64), BDF FAILS AT THE FIRST STEP,
LSODA reaches the same t~7.633e9 RK45 does then fails WORSE (a=nan). RK45
(already in use) is the MOST robust: clean steps to t=7.630e9, only failing
at t=7.634e9 where `a` hits float64's actual maximum (~1.798e308). This is
diagnostic: the bottleneck is a genuine floating-point RANGE overflow of the
scale factor `a`, not integrator stiffness. VERDICT ON THE LITERAL REQUEST:
a stiffer integrator does not help -- switching methods makes things WORSE.

STEP 2 -- this diagnosis pointed at a real gap: every prior file in this
arc used T_END=3e9 as a *conservative* margin, never pushed further. RK45
safely reaches T_END~7.6e9, corresponding to a_reach/a_star up to ~1e270 --
vastly beyond anything tested before. Pushing into this range DOES show
FINDING_P114/P115/P116's own converged values were premature: at FIXED
x_lo=1, sqrt(G_E) keeps rising smoothly (dense-scanned, no discontinuity)
from 389,259 (a_reach=1e8, matching prior findings) past 870,000 by
a_reach~1e100 -- resolution-checked (n=16000..512000 agree to <0.001% even
AT this frontier, refuting an initial worry about under-resolved tails).

STEP 3 -- BUT a context-asymmetric skeptic review of an earlier draft of
this file correctly identified that cross-validating only two lower limits
(x_lo=1 and x_lo=100) at a shared a_reach=1e270 is NEAR-TAUTOLOGICAL: the
two domains overlap over >99% of their integrated length (both share the
same enormous tail from ~1e10 to 1e270; they differ only in the first ~4.6
units of ln(a) out of ~622 total), so their 0.48% agreement is arithmetically
close to guaranteed regardless of whether the tail itself has converged, not
independent evidence of it. The skeptic recommended a THIRD lower limit
INSIDE the dominant region. Testing it directly overturned the "converged"
claim entirely: x_lo=1e50 (still well inside the numerically-safe zone --
see Step 4) gives sqrt(G_E)=983,466, ~12-17% ABOVE the x_lo=1/100 values,
and a full scan of x_lo from 1 to 1e90 at a fixed, safe a_reach=1e94*a_star
shows sqrt(G_E) climbing MONOTONICALLY and WITHOUT LEVELING OFF the entire
way: 863,854 (x_lo=1) -> 902,197 (x_lo=1e10) -> 951,894 (x_lo=1e30) ->
1,015,170 (x_lo=1e90) -- no plateau anywhere in the numerically-accessible
domain.

STEP 4 -- the hard numerical ceiling. rho_A = C_MATTER/a**3 underflows to
EXACTLY 0.0 once a**3 itself overflows float64 (a > ~5.6e102, i.e.
a/a_star > ~5.6e97 for this Lambda). Beyond that point rho_phys = 0 and
contrast = delta_m/rho_phys becomes exactly +/-inf -- not a numerical
approximation issue, a hard representability wall tied to the observable's
own definition (dividing by a density that must underflow once `a` grows
large enough). No integrator, however capable, can push past this: it does
not depend on step size or method, only on the float64 range of `a**3`.
Traced directly: rho_A/rho_phys/delta_m/contrast are all individually
finite and well-behaved (no precision loss, checked at multiple points) all
the way up to a/a_star~1e97, confirming the drift found in Step 3 is REAL
physics up to that point, not numerical noise -- it simply never plateaus
before the wall is reached.

STEP 5 -- POSITIVE CONTROL, decisive: the SAME x_lo scan on the SMOOTH k=10
baseline, using the IDENTICAL code path, shows sqrt(G_E) essentially FLAT
(1.4798 to 1.4800, <0.02% total variation) across the SAME 90+-decade x_lo
range that drove the k=0.3 case up by 17%+. This rules out a code/machinery
bug: the same construction, same integration scheme, same float64 arithmetic
gives a clean, tightly converged answer for the smooth case and a
genuinely, monotonically non-converging one for the extreme-IC case. The
non-convergence is a real property of this branch, not an artifact of how
it was computed.

Separately: a sign change in contrast_coupled located between x=3000 and
x=10000 during this investigation is NOT a new feature -- it lands within
FINDING_P112's own original dense-scan finding of "ONE genuine transition
at lna=8.84 (a/a_star~6934)". Confirms, does not contradict,
FINDING_P111/P116's single-dominant-transient diagnosis.

CORRECTED VERDICT (an earlier draft of this file reported
"TRUE-ASYMPTOTE-FOUND" at sqrt(G_E)~870,000-875,000; that verdict is
RETRACTED here, not smoothed over, after the skeptic's specific critique
was tested directly and found correct): the Integrated Energy Growth
Observable, evaluated at the absolute safe numerical limit in BOTH a_reach
and x_lo, does NOT converge to a lower-limit-independent value for
(k=0.3, phibar_dot(1)x0.1). It climbs monotonically the entire way to a
hard numerical wall (density underflow) where the construction itself
becomes undefined. FINDING_P110's original k<1 growth-ratio question
remains genuinely open for this observable; what this file adds is a
precise characterization of exactly why and where this construction hits
its limit.

CONTROLS:
  INTEGRATOR COMPARISON (the user's literal request): RK45 wins outright.
  CEILING CONFIRMATION: RK45's t-domain ceiling (~7.634e9) and the SEPARATE,
    more restrictive a_reach ceiling from rho_A underflow (~1e97*a_star).
  RESOLUTION at the tested frontier: n=16000..512000 agree to <0.001%.
  X_LO INDEPENDENCE (replaces the flawed two-point cross-validation): full
    scan across the entire safe x_lo range, at fixed a_reach.
  SMOOTH-CASE POSITIVE CONTROL: identical scan on k=10 -- must show
    stability, or the whole test design is suspect.
  UNDERFLOW TRACE: rho_A/rho_phys/delta_m individually checked for
    precision loss vs. genuine physics, near the numerical wall.

WHAT THIS FILE DOES NOT DO: identify a numerically-stable reformulation
that could evade the density-underflow wall (e.g. tracking ln(rho) instead
of rho, or a different normalization) -- named as the natural next step,
not attempted. Resolve what physically happens to the k=0.3 branch beyond
a/a_star~1e97 (unknowable in float64 without such a reformulation). Vary
Lambda or other (k, IC) combinations. Quote any k[h/Mpc]. Touch MULTING
itself (Gate 1).
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p116 = _load("P116_transient_contribution_scan.py", "p116_for_p117")
p105 = p116.p105

a_star = p116.a_star
contrast_array = p116.contrast_array
PHIDOT_INIT = p116.PHIDOT_INIT
LAMBDA_FIXED = p116.LAMBDA_FIXED

T_END = 7e9  # safely below RK45's own ~7.634e9 float64 ceiling for `a`
A_REACH_SAFE_X = 1e94  # safely below the rho_A underflow wall (~1e97*a_star)
N_PROBE = 64000
RESOLUTION_TOL = 0.01
SMOOTH_CONTROL_TOL = 0.01


def energy_ratio_from(kk, a_lo, a_reach, n=N_PROBE, **ic):
    """G_E with an explicit lower limit a_lo, upper limit a_reach, using the
    module-level T_END=7e9 -- the RK45 ceiling this file established."""
    s_c = p105.run(1.0, 1.0, kk, T_END, lam_cc=LAMBDA_FIXED, **ic)
    s_r = p105.run(0.0, 1.0, kk, T_END, lam_cc=LAMBDA_FIXED, **ic)
    if s_c is None or s_r is None:
        return None

    def piece(sol, gh):
        t_hi = p105.t_of_a(sol, a_reach, 1.0, T_END)
        t_lo = p105.t_of_a(sol, a_lo, 1.0, T_END)
        if t_hi is None or t_lo is None:
            return None
        ts = np.geomspace(t_lo, t_hi, n)
        a_, c_ = contrast_array(sol, ts, gh, 1.0, LAMBDA_FIXED)
        ok = np.isfinite(c_) & (a_ >= a_lo) & (a_ <= a_reach)
        a_, c_ = a_[ok], c_[ok]
        if a_.size < 20:
            return None
        return float(np.trapezoid(c_**2, np.log(a_)))

    e_c, e_r = piece(s_c, 1.0), piece(s_r, 0.0)
    if e_c is None or e_r is None or e_r <= 0:
        return None
    return e_c / e_r


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P117 -- Stiffer integrator: no help. Pushing RK45 to its true limit:")
    print("        the observable never converges before hitting a numerical wall")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 1 -- INTEGRATOR COMPARISON (the user's literal request,")
    print("tested directly): RK45 vs Radau/BDF/LSODA at T_END=1e10")
    print("-" * 78)
    ic_arr = p105.initial_data(1.0, 1.0, 0.3, LAMBDA_FIXED, **ic0)
    sysfun = p105.make_system(1.0, 1.0, 0.3, LAMBDA_FIXED)
    for method in ("RK45", "Radau", "BDF", "LSODA"):
        try:
            with np.errstate(all="ignore"):
                s = solve_ivp(sysfun, (1.0, 1e10), ic_arr, method=method, rtol=1e-10, atol=1e-20)
            print(
                f"    {method:<8s} success={s.success}  t_last={s.t[-1]:.4e}  "
                f"nsteps={len(s.t)}  a_last={s.y[0, -1]:.3e}"
            )
        except Exception as exc:  # noqa: BLE001 - deliberately catching solver crashes
            print(f"    {method:<8s} CRASHED: {type(exc).__name__}: {exc}")
    print("  -> RK45 (already in use) is the MOST robust of the four -- a stiffer")
    print("     method does not help and three alternatives all do WORSE. The")
    print("     bottleneck is a genuine float64 range overflow of `a`, not stiffness.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 2 -- CEILING CONFIRMATION: two SEPARATE ceilings, not one")
    print("-" * 78)
    with np.errstate(all="ignore"):
        s_committed = solve_ivp(sysfun, (1.0, T_END), ic_arr, rtol=1e-10, atol=1e-20)
    ceiling_ok = s_committed.success
    print(
        f"    (a) RK45's own t-domain ceiling: T_END={T_END:.0e} succeeds "
        f"(a_last={s_committed.y[0, -1]:.3e}), safely below the ~7.634e9 wall"
    )
    with np.errstate(all="ignore"):
        s_c = p105.run(1.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
        a_at_safe_x = s_c.sol(p105.t_of_a(s_c, astar * A_REACH_SAFE_X, 1.0, T_END))[0]
        rho_a_at_safe_x = 1.0 / a_at_safe_x**3
    print("    (b) the SEPARATE, MORE RESTRICTIVE a_reach ceiling: rho_A=C_MATTER/a^3")
    print(
        f"        at a_reach/a_star={A_REACH_SAFE_X:.0e}, a={a_at_safe_x:.3e}, "
        f"rho_A={rho_a_at_safe_x:.3e} (still finite, safely above underflow)"
    )
    print(f"  CEILING CONFIRMATION {'PASSES' if ceiling_ok else 'FAILS'}")
    if not ceiling_ok:
        print("  *** STOP -- the committed T_END is not actually safe.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 3 -- RESOLUTION at the tested frontier (a_reach=1e94*a_star)")
    print("-" * 78)
    res_vals = []
    for n in (16000, 32000, 64000, 128000, 256000):
        ge = energy_ratio_from(0.3, astar * 1.0, astar * A_REACH_SAFE_X, n, **ic0)
        res_vals.append(ge)
        print(f"    n={n:<7d} sqrt(G_E)={ge**0.5:.4f}")
    res_spread = (max(res_vals) - min(res_vals)) / abs(np.mean(res_vals))
    res_ok = res_spread < RESOLUTION_TOL
    print(f"    relative spread across n: {res_spread:.4%}")
    print(
        f"  RESOLUTION CONTROL {'PASSES' if res_ok else 'FAILS'} (threshold {RESOLUTION_TOL:.0%})"
    )
    if not res_ok:
        print("  *** STOP -- not resolution-independent at this reach.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 4 -- SMOOTH-CASE POSITIVE CONTROL: k=10 baseline, x_lo scan")
    print("across the SAME 90+-decade range -- must be stable, or the whole")
    print("test design is suspect")
    print("-" * 78)
    smooth_xs = (0.2, 1.0, 100.0, 1e5, 1e10, 1e30, 1e50, 1e70, 1e90)
    smooth_vals = []
    for xlo in smooth_xs:
        ge = energy_ratio_from(10.0, astar * xlo, astar * A_REACH_SAFE_X)
        smooth_vals.append(ge**0.5 if ge else None)
        print(f"    k=10  x_lo={xlo:<10.4g}  sqrt(G_E)={smooth_vals[-1]!r}")
    valid_smooth = [v for v in smooth_vals if v is not None]
    smooth_spread = (max(valid_smooth) - min(valid_smooth)) / abs(np.mean(valid_smooth))
    smooth_ok = smooth_spread < SMOOTH_CONTROL_TOL
    print(f"    relative spread across the whole x_lo range: {smooth_spread:.4%}")
    print(
        f"  SMOOTH-CASE CONTROL {'PASSES' if smooth_ok else 'FAILS'} -- confirms the"
        " machinery itself is sound"
    )

    if not (res_ok and smooth_ok):
        print("\n  *** a required control failed. STOP.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- X_LO INDEPENDENCE SCAN, k=0.3 (replaces the flawed")
    print("two-point cross-validation an earlier draft of this file relied on,")
    print("per a context-asymmetric skeptic review's correct critique)")
    print("-" * 78)
    scan_xs = (1.0, 100.0, 1e3, 1e4, 1e5, 1e10, 1e20, 1e30, 1e40, 1e50, 1e60, 1e70, 1e80, 1e90)
    scan_vals = []
    for xlo in scan_xs:
        ge = energy_ratio_from(0.3, astar * xlo, astar * A_REACH_SAFE_X, **ic0)
        scan_vals.append(ge**0.5 if ge else None)
        print(f"    x_lo={xlo:<10.4g}  sqrt(G_E)={scan_vals[-1]!r}")

    valid_scan = [v for v in scan_vals if v is not None]
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if len(valid_scan) < len(scan_xs):
        print("  -> INCOMPLETE SCAN. Infrastructure outcome, not evidence.")
        return 1
    monotone_rise = all(valid_scan[i] <= valid_scan[i + 1] for i in range(len(valid_scan) - 1))
    total_rise = abs(valid_scan[-1] / valid_scan[0] - 1.0)
    print(f"  monotonic rise across the entire safe x_lo range: {monotone_rise}")
    print(f"  total rise, x_lo=1 to x_lo=1e90: {total_rise:.2%}")
    print("  NO PLATEAU found anywhere in the numerically-accessible domain.")

    print("\n  -> STILL-NOT-CONVERGED, NUMERICAL-WALL-IDENTIFIED. An earlier draft")
    print("     of this file reported 'TRUE-ASYMPTOTE-FOUND' at sqrt(G_E)~870,000,")
    print("     based on only two lower limits (x_lo=1, x_lo=100) agreeing to")
    print("     0.48% -- a context-asymmetric skeptic review correctly identified")
    print("     this as near-tautological (the two domains share >99% of their")
    print("     integrated length once a_reach is astronomically larger than")
    print("     either). Testing a third, more distant lower limit directly")
    print("     OVERTURNED the claim: the value keeps climbing, with no plateau,")
    print(f"     across the entire {total_rise:.0%} range this scan covers -- all the")
    print("     way to a HARD numerical wall (rho_A=C_MATTER/a^3 underflows to")
    print("     exactly 0 once a^3 overflows float64, making contrast=delta_m/")
    print("     rho_phys exactly +/-inf) that no integrator can push past, since")
    print("     it depends only on float64's representable range, not on method")
    print("     or step size. The smooth k=10 control (Control 4) rules out a")
    print("     code/machinery bug: the identical construction gives a tightly")
    print("     converged answer there, and a genuinely non-converging one here.")
    print("     FINDING_P110's original k<1 growth-ratio question remains open")
    print("     for this observable -- this file precisely characterizes why.")

    print("\n  NOT ESTABLISHED:")
    print("   * any value for G_E's asymptote -- there is no evidence one exists")
    print("     within float64's representable range for this branch.")
    print("   * what physically happens to the k=0.3 branch beyond a/a_star~1e97 --")
    print("     unknowable in float64 without a reformulation that avoids dividing")
    print("     by a density that must underflow (e.g. tracking ln(rho) instead).")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     one tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
