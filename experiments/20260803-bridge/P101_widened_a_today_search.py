"""P101 -- widen the a_today search bracket itself, the lever FINDING_P100 named but did not pull.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P100 hardened H_at_a and widened LAMBDA, confirming P99's crash was a
real wall, not a hidden root -- but explicitly left one question open: is the
inner root's a_today search bracket ([A_SEARCH_LO, A_SEARCH_HI] = [3e2, 3e6],
inherited unchanged from FINDING_P94) itself the binding constraint on the
measurable Lambda range [1.194e-16, 4.924e-12], or is something else? P100
named widening a_today as the next, DIFFERENT lever -- named but not pulled.
This file pulls it.

THE TEST, STATED BEFORE ANY CODE RUNS. If the a_today bracket is genuinely
the binding constraint, widening it should extend the MEASURABLE Lambda
range beyond P100's own [1.194e-16, 4.924e-12] -- more grid points resolve,
because a_today values outside [3e2, 3e6] become reachable by the search.
If the bracket is NOT the binding constraint, the measurable range should
stay the SAME (within numerical noise) even with a much wider bracket --
which would mean the true wall is somewhere else (the dynamics themselves,
or the Lambda range), and P100's own hypothesis about the next lever was
wrong. Both outcomes are informative; neither is assumed.

NEW BOUNDS, AND WHY -- INCLUDING A DESIGN BUG FOUND AND FIXED BEFORE ANY
RESULT WAS TRUSTED. FINDING_P100's own docstring named the two directions:
"down toward the trajectory's own starting point a(1)~2.61, and up toward
the full T_END=1e8 reach of the integration." A first attempt took that
literally -- A_TODAY_LO_NEW = a0*(1+1e-4) -- and it broke EVERY Lambda
value: shape(a_today) is not evaluated at a_today alone, it is evaluated at
a_today/(1+z) for the largest z this file uses. With a_today sitting right
at a0, a_today/(1+Z_FIT1=0.5) = a_today/1.5 falls BELOW a0 -- a point the
trajectory never reaches (a(t) >= a0 for all t in [T0, T_END]) -- so
resid() at that endpoint is NaN and inner_a_of_lambda_at rejects the
bracket before brentq ever runs. Every "not measured" row in that run was
this bug, not a physics result -- caught by reading the all-NaN output
rather than reporting it as STILL-NO-ROOT.
  A_TODAY_LO_NEW (corrected): a0 * (1 + max(Z_FIT1, Z_FIT2, *Z_CHECK)) *
    (1 + 1e-3) = a0 * 4.004 -- the smallest a_today for which a_today/(1+z)
    stays >= a0 for EVERY z this file ever evaluates, including the
    out-of-sample Z_CHECK=(1.0, 3.0) points reached only if Step 3 runs.
    Still ~75x lower than the old 3e2 floor, and now internally consistent
    rather than merely close to a0 in name.
  A_TODAY_HI_NEW: 1e8, matching T_END's own order of magnitude, exactly as
    P100 named it. This is NOT a computed maximum reachable a(T_END) for any
    particular Lambda (that is Lambda-dependent and was not probed) -- it is
    a round ceiling tied to the integration's own time-axis scale. If it is
    higher than what a given Lambda's trajectory actually reaches by
    T_END, resid() there returns NaN and that endpoint is cleanly
    unusable, exactly as every other unreachable point in this arc has
    been handled -- no correctness risk, only possibly wasted headroom.
    ~33x higher than the old 3e6 ceiling. This direction was NOT affected
    by the bug above (it only breaks the LOW side).

REGRESSION CONTROL FIRST, AS ALWAYS. Before trusting the widened bracket,
the SAME refactored code, run with the OLD bounds [3e2, 3e6], must reproduce
FINDING_P100's own already-published g values at FINDING_P100's own two
regression Lambda points -- if the refactor itself introduced a bug, nothing
past this point is trustworthy.

PRE-REGISTERED OUTCOMES, evaluated against P100's own measurable range and
sign-change count on the IDENTICAL Lambda grid geomspace(1e-19, 1e-9, 40):
  RANGE-EXTENDS       the widened bracket resolves MORE grid points than
                       P100's 19/40, and/or the measurable Lambda range
                       widens beyond [1.194e-16, 4.924e-12] -> the a_today
                       bracket WAS part of the binding constraint, as P100
                       hypothesized. Report the new range. If a sign change
                       now appears anywhere in the newly-measurable region,
                       that is ROOT-FOUND (see below) and takes priority.
  RANGE-UNCHANGED      the widened bracket resolves the SAME 19/40 points,
                       same range to within 1% -> the a_today bracket was
                       NOT the binding constraint after all; P100's own
                       named hypothesis for the next lever is refuted by
                       this test. The true wall is elsewhere (the dynamics
                       at those Lambda values, not search-bracket width).
  ROOT-FOUND           a sign change of g(Lambda) appears anywhere in the
                       (possibly widened) measurable range -> locate it,
                       run the out-of-sample check at z=1.0/z=3.0 that has
                       been pending since FINDING_P99. This is the first
                       chance in the whole P93-P101 bridge arc for that
                       check to actually execute.

WHAT THIS FILE DOES NOT DO: quote eps(k) or f(k) in physical units under any
outcome. ROOT-FOUND with a passing out-of-sample check would license a
follow-up step to do that; it is not done here.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p81 = _load("P81_background_viability.py", "p81_for_a101")
p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_a101")
p99 = _load("P99_shape_of_H_across_epochs.py", "p99_for_a101")
p100 = _load("P100_shape_hardened_wide_scan.py", "p100_for_a101")

shape_lcdm = p99.shape_lcdm
Z_FIT1, Z_FIT2, Z_CHECK = p99.Z_FIT1, p99.Z_FIT2, p99.Z_CHECK
solve_background_safe = p100.solve_background_safe
H_at_a = p100.H_at_a
shape_at = p100.shape_at

A_SEARCH_LO_OLD, A_SEARCH_HI_OLD = p94.A_SEARCH_LO, p94.A_SEARCH_HI

A0 = p81.A3_INIT ** (1.0 / 3.0)
# Floor must keep a_today/(1+z) >= A0 for every z this file evaluates,
# including out-of-sample Z_CHECK -- see docstring "design bug found and fixed".
_Z_MAX = max(Z_FIT1, Z_FIT2, *Z_CHECK)
A_TODAY_LO_NEW = A0 * (1.0 + _Z_MAX) * (1.0 + 1.0e-3)
A_TODAY_HI_NEW = 1.0e8

# P100's own regression targets, re-quoted -- the refactor (not the widened
# bounds yet) must reproduce these under the OLD bracket before anything else.
REGRESSION = {
    2.084e-16: 2.905e-06,
    3.000e-12: 1.616e-05,
}
REGRESSION_TOL = 5e-3

LAMBDA_LO_WIDE, LAMBDA_HI_WIDE = p100.LAMBDA_LO_WIDE, p100.LAMBDA_HI_WIDE

# P100's own published result, re-quoted for direct comparison.
P100_MEASURABLE_COUNT = 19
P100_MEASURABLE_RANGE = (1.194e-16, 4.924e-12)


def inner_a_of_lambda_at(lam_cc, z_target, a_lo, a_hi):
    """Same architecture as P99/P100's inner_a_of_lambda, but with EXPLICIT bounds."""
    s = solve_background_safe(lam_cc)
    if s is None:
        return None, s

    def resid(a_today):
        sh = shape_at(s, a_today, z_target)
        return (sh - shape_lcdm(z_target)) if sh is not None else np.nan

    with np.errstate(all="ignore"):
        f_lo, f_hi = resid(a_lo), resid(a_hi)
        if not (np.isfinite(f_lo) and np.isfinite(f_hi)) or f_lo * f_hi > 0:
            return None, s
        try:
            a_today = brentq(resid, a_lo, a_hi, xtol=1e-3, rtol=1e-12)
        except (ValueError, RuntimeError):
            return None, s
    return a_today, s


def g_of_lambda_at(lam_cc, a_lo, a_hi):
    a_today, s = inner_a_of_lambda_at(lam_cc, Z_FIT1, a_lo, a_hi)
    if a_today is None:
        return None, None, None
    sh2 = shape_at(s, a_today, Z_FIT2)
    if sh2 is None:
        return None, None, None
    return (sh2 - shape_lcdm(Z_FIT2)), a_today, s


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P101 -- widen the a_today search bracket itself (P100's named next lever)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print(f"\n  a0 (trajectory start, A3_INIT**(1/3)) = {A0!r}")
    print(f"  OLD bracket: [{A_SEARCH_LO_OLD:.4e}, {A_SEARCH_HI_OLD:.4e}]")
    print(f"  NEW bracket: [{A_TODAY_LO_NEW:.6e}, {A_TODAY_HI_NEW:.4e}]")
    print(
        f"    -> {A_SEARCH_LO_OLD / A_TODAY_LO_NEW:.3g}x lower floor, "
        f"{A_TODAY_HI_NEW / A_SEARCH_HI_OLD:.3g}x higher ceiling"
    )

    # ==================================================================
    print("\n" + "-" * 78)
    print("STEP 1 -- REGRESSION CONTROL: refactored code, OLD bounds, must reproduce")
    print("FINDING_P100's own published g values before the widened bounds are trusted")
    print("-" * 78)
    print(f"\n    {'Lambda':<14}{'P100 published g':<20}{'this file g':<20}{'rel diff'}")
    reg_ok = True
    for lam, published in REGRESSION.items():
        g, _a, _s = g_of_lambda_at(lam, A_SEARCH_LO_OLD, A_SEARCH_HI_OLD)
        if g is None:
            print(f"    {lam:<14.4e}{published:<20.4e}{'not measured':<20}")
            reg_ok = False
            continue
        rel = abs(g / published - 1.0)
        ok = rel < REGRESSION_TOL
        reg_ok = reg_ok and ok
        print(
            f"    {lam:<14.4e}{published:<20.4e}{g:<20.6e}{rel:.3e}  {'OK' if ok else 'MISMATCH'}"
        )
    print(f"\n    REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** the refactor changed FINDING_P100's own answers under the OLD bounds.")
        print("  *** STOP -- find the bug before trusting the widened bracket at all.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(
        f"STEP 2 -- SAME Lambda grid as FINDING_P100, geomspace({LAMBDA_LO_WIDE:.0e}, "
        f"{LAMBDA_HI_WIDE:.0e}, 40), NOW with the WIDENED a_today bracket"
    )
    print("-" * 78)
    grid = np.geomspace(LAMBDA_LO_WIDE, LAMBDA_HI_WIDE, 40)
    print(f"\n    {'Lambda':<14}{'a_today':<18}{'g(Lambda)'}")
    rows = []
    for lam in grid:
        g, a_today, _s = g_of_lambda_at(lam, A_TODAY_LO_NEW, A_TODAY_HI_NEW)
        if g is None:
            print(f"    {lam:<14.4e}{'not measured (no root / unresolved)':<40}")
            continue
        rows.append((lam, g, a_today))
        print(f"    {lam:<14.4e}{a_today:<18.6f}{g:+.6e}")

    if len(rows) < 2:
        print("\n  -> NOT MEASURABLE even with the widened bracket. Infrastructure")
        print("     outcome, not evidence either way.")
        return 1

    signs = [1 if g > 0 else -1 for _l, g, _a in rows]
    crossings = [(rows[i - 1], rows[i]) for i in range(1, len(rows)) if signs[i] != signs[i - 1]]
    lam_measured = [r[0] for r in rows]
    new_lo, new_hi = min(lam_measured), max(lam_measured)
    print(f"\n    Lambda values MEASURABLE with the widened bracket: {len(rows)}/{len(grid)}")
    print(f"    (FINDING_P100's own count, OLD bracket: {P100_MEASURABLE_COUNT}/40)")
    print(f"    measurable range: [{new_lo:.4e}, {new_hi:.4e}]")
    print(
        f"    (FINDING_P100's own range: [{P100_MEASURABLE_RANGE[0]:.4e}, "
        f"{P100_MEASURABLE_RANGE[1]:.4e}])"
    )
    print(f"    sign changes of g(Lambda): {len(crossings)}")

    range_extended = (
        len(rows) > P100_MEASURABLE_COUNT
        or new_lo < P100_MEASURABLE_RANGE[0] * 0.99
        or new_hi > P100_MEASURABLE_RANGE[1] * 1.01
    )

    if not crossings:
        best = min(rows, key=lambda r: abs(r[1]))
        print("\n" + "=" * 78)
        print("VERDICT (against the outcomes pre-registered in the docstring)")
        print("=" * 78)
        if range_extended:
            print("  -> RANGE-EXTENDS, but still zero sign changes.")
            print(
                f"     The a_today bracket WAS part of the binding constraint: measurable "
                f"count {len(rows)}/40 vs P100's {P100_MEASURABLE_COUNT}/40, range "
                f"[{new_lo:.4e}, {new_hi:.4e}] vs P100's "
                f"[{P100_MEASURABLE_RANGE[0]:.4e}, {P100_MEASURABLE_RANGE[1]:.4e}]."
            )
        else:
            print("  -> RANGE-UNCHANGED. Zero sign changes, and the measurable range is")
            print(
                f"     effectively identical to FINDING_P100's own "
                f"({len(rows)}/40 vs {P100_MEASURABLE_COUNT}/40, "
                f"[{new_lo:.4e}, {new_hi:.4e}] vs "
                f"[{P100_MEASURABLE_RANGE[0]:.4e}, {P100_MEASURABLE_RANGE[1]:.4e}]) "
                f"even with a {A_SEARCH_LO_OLD / A_TODAY_LO_NEW:.0f}x-lower floor and "
                f"{A_TODAY_HI_NEW / A_SEARCH_HI_OLD:.0f}x-higher ceiling."
            )
            print("     P100's own hypothesis -- that the a_today bracket was the binding")
            print("     constraint -- is REFUTED by this test. The true wall is elsewhere:")
            print("     the dynamics at those Lambda values themselves, not search-bracket")
            print("     width.")
        print(f"     Closest approach: Lambda={best[0]:.4e}, g={best[1]:+.4e}.")
        print("     NO k[h/Mpc] number is quoted.")
        return 0

    # ==================================================================
    print("\n" + "-" * 78)
    print("STEP 3 -- a root exists. Locate it, then run the out-of-sample check")
    print("          pending since FINDING_P99.")
    print("-" * 78)
    fits = []
    for lo_row, hi_row in crossings:
        lo_lam, hi_lam = lo_row[0], hi_row[0]

        def gg(lam):
            g, _a, _s = g_of_lambda_at(lam, A_TODAY_LO_NEW, A_TODAY_HI_NEW)
            return g if g is not None else np.nan

        lam_fit = brentq(gg, lo_lam, hi_lam, xtol=1e-20, rtol=1e-10)
        a_fit, s_fit = inner_a_of_lambda_at(lam_fit, Z_FIT1, A_TODAY_LO_NEW, A_TODAY_HI_NEW)
        fits.append((lam_fit, a_fit, s_fit))
        print(
            f"    bracket [{lo_lam:.4e}, {hi_lam:.4e}]  ->  Lambda={lam_fit:.10e}, "
            f"a_today={a_fit:.6f}"
        )

    worst_rel = {}
    for i, (_lam_fit, a_fit, s_fit) in enumerate(fits):
        print(f"\n  fit #{i + 1}: out-of-sample check at z={Z_CHECK}")
        worst = 0.0
        for z in Z_CHECK:
            sh = shape_at(s_fit, a_fit, z)
            target = shape_lcdm(z)
            if sh is None:
                print(f"    z={z:<6g} not measured")
                continue
            rel = abs(sh / target - 1.0)
            worst = max(worst, rel)
            print(f"    z={z:<6g} shape={sh:.9f}  LCDM={target:.9f}  rel={rel:.4e}")
        worst_rel[i] = worst

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    overall = max(worst_rel.values()) if worst_rel else float("nan")
    print(f"  -> ROOT-FOUND. Worst out-of-sample deviation: {overall:.4e}")
    if overall < 0.01:
        print("     SHAPE-MATCHES (per FINDING_P99's own criterion). First non-circular")
        print("     success in this bridge arc. NOT converted to k[h/Mpc] in this file.")
    elif overall > 0.10:
        print("     SHAPE-DIVERGES (per FINDING_P99's own criterion) even though a")
        print("     two-point fit exists -- the fit does not extrapolate.")
    else:
        print("     INTERMEDIATE. Named, not rounded toward either.")

    print("\n  NOT ESTABLISHED:")
    print(f"   * that A_TODAY_HI_NEW={A_TODAY_HI_NEW:.0e} is the true maximum reachable")
    print("     a(T_END) for any given Lambda -- it is a round ceiling, not a computed one.")
    print("   * that z_fit1=0.5, z_fit2=1.5 are the 'right' fit points.")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
