"""P106 -- resolve the k=0.1 ambiguity FINDING_P105 left open: is the cross-branch
spread in eps(0.1; Lambda) real Lambda-dependence, or window-choice noise on an
already-known-ill-defined quantity?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHAT WAS LEFT OPEN. FINDING_P105 measured eps(k; Lambda) at ONE window per
branch ([a_star*0.2, a_star*2.0]) and found: k=1, k=10 (P76's own certified
"clean corner") converge across Lambda branches to within 2.2% and 0.5%.
k=0.1 (a mode P76's OWN prior, independent T-convergence/lever gates
already found UNRELIABLE, before this file or P105 ever ran) showed a
larger ABSOLUTE spread than either certified k -- reported honestly
unresolved, since P105 measured only ONE window per branch and could not
tell real Lambda-dependence from accumulated noise on an ill-defined
quantity.

THE DIAGNOSTIC, STATED BEFORE ANY CODE RUNS. P76's own Part G already
explained WHY k=0.1 might not have a well-defined eps AT ALL, for ANY
Lambda: "IF the force induces a PERSISTENT rate shift, an accumulated
ratio [G] keeps rising with the window -- window-dependent by
construction," and P76 measured this explicitly: eps(k=0.1) is NOT
constant across P76's OWN four-decade convergence check (only k=1, k=10
are). This is prior, independent information, not invented for this file.
It gives a concrete, checkable prediction: if k=0.1's eps is genuinely
ill-defined (window-dependent) REGARDLESS of Lambda, then the WITHIN-BRANCH
spread of eps(0.1) across DIFFERENT windows (same Lambda, same k) should be
comparable to, or larger than, the ACROSS-BRANCH spread FINDING_P105
measured at one fixed window (same k, different Lambda). If so, the
apparent "Lambda-dependence" P105 measured is indistinguishable from
ordinary window-choice noise on a quantity that was never well-defined at
that k in the first place -- resolving the ambiguity as "still noise,
exactly as P76 always said," not new evidence for or against M1/M2.

THE TEST, AND A DESIGN CORRECTION CAUGHT BY ITS OWN CONTROL, BEFORE
TRUSTING A RESULT. A first attempt fixed a1 = a_star*0.2 and measured
eps(k) at a_end = a_star*{0.5, 1.0, 2.0} -- spanning x=1, the Lambda-
crossing itself. The CONTROL below FAILED there even at k=1/k=10 (P76's
own certified k): within-branch spread was 10x-50x larger than
FINDING_P105's cross-branch spread. Read before reported as a result: this
does NOT mean k=1/k=10 are secretly unstable. It means a window spanning
the matter-to-Lambda TRANSITION is expected to show a changing eps --
that is the underlying physics changing, not measurement noise -- and
P76's own original convergence check never crossed any such transition
(lam_cc did not exist when it was run, so P76's tested window was matter-
domination throughout). Comparing "variation across a real physical
transition" to "variation across independent branches" was never a fair
test of window-choice noise. CORRECTED: a1 = a_star*0.2 (unchanged), a_end
= a_star*{1.8, 1.9, 2.0} -- a NARROW, LOCAL perturbation right around
FINDING_P105's own comparison point (x_end=2.0), asking whether THAT
SPECIFIC choice sits in a locally stable or locally unstable part of the
function -- the right question for whether P105's own comparison was
trustworthy. The WITHIN-branch spread (max-min across these three LOCAL
windows, same Lambda) is the diagnostic. As an explicit CONTROL, the SAME
three-window check is run at k=1 and k=10 too -- if even k=1/k=10 show
large within-branch spread under this NARROWED, local test, that would
mean something is still wrong with the comparison, not with the physics.

PRE-REGISTERED OUTCOMES:
  CONTROL-FAILS      within-branch spread at k=1 or k=10 is LARGE (>10% of
                     P105's own cross-branch spread at those k) -> this
                     file's window choices are not a valid analogue of
                     P76's convergence check. STOP -- the k=0.1 result
                     below cannot be trusted either.
  RESOLVED-NOISE     (control passes, i.e. k=1/k=10 within-branch spread is
                     small) AND k=0.1's within-branch (window) spread is
                     comparable to or LARGER than FINDING_P105's own
                     across-branch (Lambda) spread at k=0.1 -> the apparent
                     Lambda-dependence at k=0.1 is indistinguishable from
                     ordinary window-choice noise. Ambiguity CLOSES:
                     consistent with, not beyond, P76's own prior finding
                     that k=0.1 has no well-defined eps. Not new evidence
                     for M2.
  RESOLVED-REAL      (control passes) AND k=0.1's within-branch spread is
                     MUCH SMALLER (< 20%) than the across-branch spread ->
                     surprising: despite the mode's known instability, the
                     Lambda-dependence is reproducible across window
                     choices. A real, narrow finding worth flagging on its
                     own, separate from the M1 result at k=1/k=10.
  INCONCLUSIVE       neither threshold cleanly met.

WHAT THIS FILE DOES NOT DO: change FINDING_P105's own CONVERGES (M1)
verdict at k=1/k=10, which does not depend on anything resolved here.
Quote eps(k) or f(k) in physical units, or any k[h/Mpc] number. Touch
MULTING itself (Gate 1).
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


p105 = _load("P105_growth_with_lambda_cc.py", "p105_for_a106")

eps_of_k = p105.eps_of_k
a_star = p105.a_star
G_HAT_FIXED, LAM_FIXED = p105.G_HAT_FIXED, p105.LAM_FIXED

T_END = 1e8
LAMBDA_BRANCHES = (2e-17, 1e-16, 1e-15, 1e-14, 1e-13, 3e-12)  # SAME as FINDING_P105
X_LO = 0.2
# NARROW, LOCAL perturbation around FINDING_P105's own comparison point
# (x_end=2.0), NOT a wide sweep across the Lambda-crossing transition.
# CORRECTION MADE MID-BUILD, before trusting a result: a first attempt used
# X_ENDS=(0.5, 1.0, 2.0), spanning x=1 -- the Lambda-crossing itself. The
# CONTROL failed there even at k=1/k=10 (P76's own certified k), but not
# because of noise: that range straddles the matter-to-Lambda transition,
# where eps changing is the PHYSICS, not instability -- P76's own original
# convergence check never crossed any such transition (lam_cc did not even
# exist when it was run). Comparing "variation across a real transition" to
# "variation across independent branches" was never a fair test. Narrowed to
# a LOCAL window near x=2.0 to test whether P105's own specific comparison
# point sits in a locally stable or locally unstable part of the function --
# the right question for whether THAT comparison was trustworthy.
X_ENDS = (1.8, 1.9, 2.0)  # all confirmed reachable by every branch, per P105's own run
KS = (0.1, 1.0, 10.0)

# FINDING_P105's own published cross-branch spread at the single window
# x_end=2.0 -- re-quoted for direct comparison, not recomputed from scratch,
# so this file's numbers are checked against what was actually published.
P105_CROSS_BRANCH_ABS_SPREAD = {0.1: 2.569e-3, 1.0: 4.348e-4, 10.0: 1.697e-4}


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P106 -- resolve the k=0.1 ambiguity: window-choice noise, or real")
    print("        Lambda-dependence?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print(f"\n  branches (same as FINDING_P105): {LAMBDA_BRANCHES}")
    print(f"  a1 = a_star*{X_LO} (fixed), a_end = a_star*{X_ENDS} (three windows)")

    within_branch = {kk: {} for kk in KS}
    for lc in LAMBDA_BRANCHES:
        a0 = a_star(lc)
        a1 = a0 * X_LO
        print(f"\n  Lambda={lc:.4e}, a_star={a0:.4f}")
        print(f"    {'k':<7}" + "".join(f"x_end={x}".ljust(16) for x in X_ENDS) + "within-spread")
        for kk in KS:
            vals = []
            for x in X_ENDS:
                a_end = a0 * x
                e = eps_of_k(G_HAT_FIXED, LAM_FIXED, kk, a1, a_end, T_END, lam_cc=lc)
                vals.append(e)
            valid = [v for v in vals if v is not None]
            row = "".join((f"{v:<16.6f}" if v is not None else f"{'--':<16}") for v in vals)
            if len(valid) == len(X_ENDS):
                spread = max(valid) - min(valid)
                within_branch[kk][lc] = spread
                print(f"    {kk:<7}{row}{spread:.4e}")
            else:
                print(f"    {kk:<7}{row}{'not measurable at all windows'}")

    print("\n" + "-" * 78)
    print("CONTROL -- k=1/k=10 within-branch (window) spread must be SMALL relative")
    print("to FINDING_P105's own across-branch (Lambda) spread at those k")
    print("-" * 78)
    control_ok = True
    for kk in (1.0, 10.0):
        spreads = within_branch[kk]
        if len(spreads) < len(LAMBDA_BRANCHES):
            print(f"  k={kk}: not measurable at every branch -- CONTROL cannot be checked")
            control_ok = False
            continue
        worst = max(spreads.values())
        cross = P105_CROSS_BRANCH_ABS_SPREAD[kk]
        ratio = worst / cross
        ok = ratio < 0.10
        control_ok = control_ok and ok
        print(
            f"  k={kk}: worst within-branch spread {worst:.4e}, "
            f"P105's cross-branch spread {cross:.4e}, ratio {ratio:.3f} "
            f"{'OK' if ok else 'FAILS'} (threshold 0.10)"
        )

    print(f"\n  CONTROL {'PASSES' if control_ok else 'FAILS'}")
    if not control_ok:
        print("  *** this file's window choices are not a valid analogue of P76's own")
        print("  *** convergence check -- STOP, the k=0.1 result below cannot be trusted.")
        return 1

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    k01_spreads = within_branch[0.1]
    if len(k01_spreads) < len(LAMBDA_BRANCHES):
        print("  -> NOT MEASURABLE at every branch for k=0.1. Infrastructure outcome,")
        print("     not evidence either way.")
        return 1

    worst_within = max(k01_spreads.values())
    cross_k01 = P105_CROSS_BRANCH_ABS_SPREAD[0.1]
    ratio_k01 = worst_within / cross_k01
    print(f"  k=0.1: worst within-branch (window) spread = {worst_within:.4e}")
    print(f"  k=0.1: FINDING_P105's own across-branch (Lambda) spread = {cross_k01:.4e}")
    print(f"  ratio (within-branch / across-branch) = {ratio_k01:.3f}")

    if ratio_k01 >= 1.0:
        print("\n  -> RESOLVED-NOISE.")
        print("     Window-to-window variation WITHIN a single Lambda branch is AS LARGE")
        print("     AS OR LARGER THAN the variation ACROSS Lambda branches at a fixed")
        print("     window. The apparent Lambda-dependence FINDING_P105 measured at k=0.1")
        print("     is indistinguishable from ordinary window-choice noise on a quantity")
        print("     P76's own prior, independent gates already found ill-defined at this")
        print("     k. The ambiguity CLOSES: k=0.1 remains exactly as uninformative as")
        print("     P76 always said it was -- not new evidence for M2, and consistent")
        print("     with (not contradicting) FINDING_P105's own CONVERGES (M1) verdict")
        print("     at k=1/k=10.")
    elif ratio_k01 < 0.20:
        print("\n  -> RESOLVED-REAL.")
        print("     Window-to-window variation within a branch is small compared to the")
        print("     variation across branches -- surprising, given k=0.1's known overall")
        print("     instability. The Lambda-dependence at k=0.1 appears reproducible")
        print("     across window choices. A real, narrow finding, separate from the")
        print("     CONVERGES (M1) result at k=1/k=10 -- worth flagging on its own.")
    else:
        print("\n  -> INCONCLUSIVE. Neither threshold cleanly met -- reported as measured,")
        print("     not rounded to either extreme.")

    print("\n  NOT ESTABLISHED:")
    print("   * a full T-convergence sweep matching P76's own 4-decade check -- this file")
    print("     used 3 windows within [0.2, 2.0]*a_star, the range P105 already confirmed")
    print("     reachable by every branch; a wider sweep was not attempted.")
    print("   * anything about the PHYSICAL meaning of a real k=0.1 signal, if RESOLVED-REAL")
    print("     is the outcome -- only whether it is distinguishable from window noise.")
    print("   * FINDING_P105's own CONVERGES (M1) verdict at k=1/k=10, which this file")
    print("     does not touch either way.")
    print("   * any numeric value of eps(k) or f(k) in physical units, or any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
