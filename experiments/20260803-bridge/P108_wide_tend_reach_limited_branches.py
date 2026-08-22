"""P108 -- test the two reach-limited branches (Lambda=2e-17, 1e-16) with a wider
T_END, completing the full 6-branch asymptotic convergence picture FINDING_P107
could only give for 4 of 6.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHAT WAS LEFT OPEN. FINDING_P107's own reconnaissance found Lambda=2e-17 and
Lambda=1e-16 reach only 2.3x and 11.4x their own a_star before T_END=1e8 caps
them (0.36 and 1.06 decades) -- nowhere near the x=100 (2 decades) reach that
let the other four branches show clean G_growth convergence. P107 explicitly
did not extend T_END, citing overflow risk for the LARGE-Lambda branches
(1e-13, 3e-12), which were already at a(T_END)~1e42-1e229 by T_END=1e8. That
risk is SPECIFIC to those large-Lambda branches -- it says nothing about
whether extending T_END is safe for the two SMALL-Lambda branches, which were
UNDER-reaching, not over-reaching. This file tests exactly that, and touches
ONLY the two reach-limited branches -- the four already-converged branches
from FINDING_P107 are not re-run.

RECONNAISSANCE FIRST, NOT ASSUMED. Probed a(T_END) for both branches at
T_END in (1e8, 3e8, 1e9, 3e9, 1e10) before choosing anything:

    Lambda=2e-17:  T_END=1e8 -> ratio 2.3   | T_END=3e8 -> ratio 31   |
                   T_END=1e9 -> ratio 2.6e5 | T_END=1e10 -> ratio 1e59 (way overshoot)
    Lambda=1e-16:  T_END=1e8 -> ratio 11    | T_END=3e8 -> ratio 3719 |
                   T_END=1e9 -> ratio 2.3e12 (already way past what is needed)

Growth is exponential once Lambda dominates (de Sitter), so small increases in
T_END overshoot fast. Lambda=2e-17 is the binding constraint (slowest growth,
smallest Lambda). Narrowed empirically: T_END=4.5e8 gives Lambda=2e-17 a ratio
of ~213 (comfortably past x=100, with margin for the x=50->100 comparison) and
gives Lambda=1e-16 an even larger, equally comfortable margin. Chosen as the
SMALLEST T_END that safely clears x=100 for the harder branch, rather than the
much larger values that would overshoot without adding information -- no
reason to integrate further than needed, and unnecessary reach adds overflow
risk in later phases of the trajectory for no benefit here.

REGRESSION CONTROL, before trusting anything at the new T_END: FINDING_P107's
own G_growth values at (Lambda=2e-17, x=2.0) and (Lambda=1e-16, x=2.0/5.0/10.0)
were computed at T_END=1e8. The SAME points, re-evaluated at T_END=4.5e8,
should be IDENTICAL -- the trajectory from t=1 up to wherever a first reaches
a given target does not depend on where the integration eventually stops.
Checked live against P107's own published numbers before trusting the new,
wider-reach points.

THE TEST, mirroring FINDING_P107's own design exactly (same a1=a_star*0.2,
same x=(2,5,10,20,50,100) grid, same G_growth-not-eps diagnostic -- eps is the
wrong tool once Lambda dominates and growth freezes, established in P107, not
re-derived here). T-convergence on G_growth, final step x=50->100, <2%,
matching P76's own gate. If both branches converge, their G_infinity joins
FINDING_P107's own four converged values for the FIRST complete 6-branch
comparison in this arc.

PRE-REGISTERED OUTCOMES:
  REGRESSION-FAILS       the T_END=4.5e8 re-evaluation does not reproduce
                         FINDING_P107's own published values at the shared
                         points -> STOP, something is wrong with widening
                         T_END, nothing past this point is trustworthy.
  SIX-BRANCH-CONVERGES   both branches individually T-converge on G_growth AND
                         the full 6-branch G_infinity spread (this file's 2 +
                         FINDING_P107's own 4, re-quoted not recomputed)
                         stays under 5% -> the COMPLETE Lambda range tested in
                         this arc supports M1 (scale-degeneracy-only) with no
                         gaps left. The strongest possible form of this
                         result.
  PARTIAL-OR-DISAGREE    either branch fails to T-converge, or the full
                         6-branch spread exceeds 5% -> the picture is
                         genuinely incomplete or non-uniform; reported as
                         found, not rounded toward either extreme.

WHAT THIS FILE DOES NOT DO: touch the four already-converged branches from
FINDING_P107, or extend T_END for them. Quote eps(k), G_growth, or f(k) in
physical units, or any k[h/Mpc] number. Touch MULTING itself (Gate 1).
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p105 = _load("P105_growth_with_lambda_cc.py", "p105_for_a108")

G_growth = p105.G_growth
a_star = p105.a_star
G_HAT_FIXED, LAM_FIXED = p105.G_HAT_FIXED, p105.LAM_FIXED

T_END_OLD = 1e8  # FINDING_P107's own T_END, for the regression points only
T_END_NEW = 4.5e8  # chosen empirically -- smallest value that clears x=100 for Lambda=2e-17
X_LO = 0.2
X_ENDS = (2.0, 5.0, 10.0, 20.0, 50.0, 100.0)
KS = (0.1, 1.0, 10.0)

BRANCHES = (2e-17, 1e-16)

# FINDING_P107's own published values, re-quoted for regression -- both are
# at k=1.0 specifically (the value spot-checked live during this file's own
# design phase); the file below checks all three k for completeness.
P107_REGRESSION = {
    (2e-17, 1.0, 2.0): 1.046447,
    (1e-16, 1.0, 2.0): 1.046415,
    (1e-16, 1.0, 5.0): 1.050206,
    (1e-16, 1.0, 10.0): 1.050877,
}
REGRESSION_TOL = 1e-4

CONV_TOL = 0.02  # matches P76's own gate, and FINDING_P107's own choice

# FINDING_P107's own converged G_infinity at the four full-reach branches
# (Lambda order: 1e-15, 1e-14, 1e-13, 3e-12), re-quoted for the final
# 6-branch comparison, matching P107's own printed rows exactly -- not
# recomputed here.
P107_CONVERGED = {
    0.1: [1.002239, 1.000264, 1.000561, 0.996876],
    1.0: [1.051074, 1.050940, 1.050665, 1.050046],
    10.0: [1.095773, 1.095728, 1.095651, 1.095357],
}

CROSS_BRANCH_TOL = 0.05


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P108 -- widen T_END for the two reach-limited branches, complete the")
    print("        full 6-branch asymptotic convergence picture")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print(
        f"\n  T_END_OLD (FINDING_P107) = {T_END_OLD:.1e}, T_END_NEW (this file) = {T_END_NEW:.1e}"
    )
    print(f"  branches: {BRANCHES}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("REGRESSION CONTROL -- T_END=4.5e8 must reproduce FINDING_P107's own")
    print("published G_growth at the SAME (Lambda, k, x) points, T_END=1e8")
    print("-" * 78)
    reg_ok = True
    for (lc, kk, x), published in P107_REGRESSION.items():
        a0 = a_star(lc)
        g_new = G_growth(G_HAT_FIXED, LAM_FIXED, kk, a0 * X_LO, a0 * x, T_END_NEW, lam_cc=lc)
        rel = abs(g_new / published - 1.0) if g_new is not None else float("inf")
        ok = rel < REGRESSION_TOL
        reg_ok = reg_ok and ok
        print(
            f"    Lambda={lc:.1e} k={kk} x={x}: P107={published:.6f}  this file="
            f"{g_new:.6f}  rel={rel:.3e}  {'OK' if ok else 'MISMATCH'}"
        )
    print(f"\n    REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** widening T_END changed FINDING_P107's own answers at shared points.")
        print("  *** STOP -- find the bug before trusting anything below.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(f"SWEEP -- both reach-limited branches, x={X_ENDS}, T_END={T_END_NEW:.1e},")
    print("T-convergence on G_growth (final step x=50->100, <2%, matching P76's gate)")
    print("-" * 78)
    converged = {kk: {} for kk in KS}
    not_converged = {kk: [] for kk in KS}
    for lc in BRANCHES:
        a0 = a_star(lc)
        a1 = a0 * X_LO
        print(f"\n  Lambda={lc:.4e}, a_star={a0:.4f}")
        for kk in KS:
            vals = [
                G_growth(G_HAT_FIXED, LAM_FIXED, kk, a1, a0 * x, T_END_NEW, lam_cc=lc)
                for x in X_ENDS
            ]
            row = "".join(f"{v:<14.8f}" if v is not None else f"{'--':<14}" for v in vals)
            valid_last_two = vals[-2] is not None and vals[-1] is not None
            if valid_last_two:
                final_change = abs(vals[-1] / vals[-2] - 1.0) if vals[-2] != 0 else float("inf")
                conv_ok = final_change < CONV_TOL
            else:
                final_change = float("nan")
                conv_ok = False
            status = "CONVERGED" if conv_ok else "NOT-CONVERGED"
            print(f"    k={kk:<6} {row} final-step-change={final_change:.4%}  {status}")
            if conv_ok:
                converged[kk][lc] = vals[-1]
            else:
                not_converged[kk].append(lc)

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    for kk in KS:
        print(f"\n  k={kk}:")
        n_conv = len(converged[kk])
        print(f"    reach-limited branches T-converged: {n_conv}/{len(BRANCHES)}")
        if not_converged[kk]:
            print(f"    NOT converged: {not_converged[kk]}")
        if n_conv < len(BRANCHES):
            print("    -> PARTIAL. At least one reach-limited branch still fails T-convergence")
            print(f"       even at T_END={T_END_NEW:.1e}. Reported, not forced further.")
            continue
        new_vals = list(converged[kk].values())
        all_six = new_vals + P107_CONVERGED[kk]
        spread6 = (max(all_six) - min(all_six)) / abs(sum(all_six) / len(all_six))
        print(f"    this file's converged values: {[round(v, 6) for v in new_vals]}")
        print(
            f"    FINDING_P107's own 4 converged values: "
            f"{[round(v, 6) for v in P107_CONVERGED[kk]]}"
        )
        print(
            f"    FULL 6-branch range: [{min(all_six):.6f}, {max(all_six):.6f}], "
            f"relative spread {spread6:.4e}"
        )
        if spread6 < CROSS_BRANCH_TOL:
            print(f"    -> SIX-BRANCH-CONVERGES at k={kk}. Both reach-limited branches")
            print("       individually T-converge, and the FULL 6-branch G_infinity spread")
            print(f"       stays under {CROSS_BRANCH_TOL:.0%}. The complete Lambda range")
            print("       tested in this arc supports M1 with no gaps left.")
        else:
            print(f"    -> PARTIAL-OR-DISAGREE at k={kk}. Both branches converge, but the")
            print(f"       full 6-branch spread exceeds {CROSS_BRANCH_TOL:.0%}.")

    print("\n  NOT ESTABLISHED:")
    print("   * that T_END could not be pushed even further for these two branches --")
    print("     4.5e8 was chosen as the smallest value that safely clears x=100 for the")
    print("     harder branch, not tested beyond that.")
    print("   * anything about the four already-converged branches from FINDING_P107 --")
    print("     not re-run, re-quoted only.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
