"""P109 -- Attractor analysis for initial conditions: does the ASYMPTOTIC, CONVERGED
G_infinity(k) established across FINDING_P107/P108's Lambda branches ALSO converge
across initial-condition variants, at a FIXED Lambda?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-DIRECTED PIVOT, AGREED BEFORE BUILDING. FINDING_P108 closed the Lambda-branch
question completely: G_infinity is Lambda-independent to well under 1% across the
whole tested Lambda range, at every tested k. The user's own next-step proposal:
now that Lambda-freedom is understood, is the SAME asymptotic G_infinity ALSO
robust to the completion's OTHER free choice -- initial conditions? If both
freedoms wash out at late times, that is attractor-like universality, a
materially stronger predictive-content result than Lambda-invariance alone. If
Lambda converges but IC does not, initial-condition selection becomes the
project's next real bottleneck.

WHAT IS ALREADY ESTABLISHED, AND WHY THIS IS A GENUINELY NEW QUESTION, NOT A
RE-TEST -- checked before building, not assumed. Two prior results touch IC
sensitivity, and NEITHER answers this file's question:
  (1) FINDING_P76's own Part E "LEVER GATE" tested G_growth's sensitivity to the
      SAME kind of IC variants (phibar_dot(1) x0.5/x2, psi0 x100, drA0 x10,
      dph0 x100) -- and found G_growth passes (<10% spread) at k=1, k=10. But
      that test was run at a SNAPSHOT window (P76's own A1=1235.6, A2=494114),
      with lam_cc=0 -- Lambda did not exist yet. FINDING_P107 itself proved that
      snapshot behavior and asymptotic behavior can be QUALITATIVELY different
      (eps looked reasonably behaved at a snapshot but was structurally the
      WRONG tool once the window reached the Lambda-dominated regime). P76's
      lever-gate pass is weak prior evidence, not a substitute for testing the
      CONVERGED quantity directly.
  (2) FINDING_P79 tested phibar_dot(1) in {0.1, 0.5, 1, 2} (x10 excluded as
      kination-dominated, not a legitimate IC variation -- the SAME exclusion
      applied here) on a DIFFERENT quantity: the SEPARATION between two
      different completions (D-SEP), at low k (1,2,3), non-asymptotic. Found
      that separation IS IC-sensitive there -- a 5.2x spread at k=1 and an
      outright SIGN CHANGE at k=3 under the phibar_dot(1) lever. This is a
      real, documented instance of an IC lever producing a dramatic effect on
      SOME quantity in this completion -- a concrete reason not to assume this
      file's answer in advance, in either direction.

RECONNAISSANCE FIRST, NOT ASSUMED. Before designing the sweep, checked whether
IC variation changes reachability the way Lambda variation did in FINDING_P107.
It does not: at Lambda=1e-15 (T_END=1e8), EVERY IC variant below reaches
a(T_END)/a_star = 5948.0 to 4 significant figures, matching the baseline
exactly -- IC perturbations of this size do not meaningfully shift WHEN Lambda
domination kicks in. No T_END widening is needed here, unlike FINDING_P108.

THE TEST. Lambda fixed at 1e-15 -- one of FINDING_P107's own full-reach,
already-converged branches, chosen so the Lambda question is held fixed and
already-answered while ONLY initial conditions vary. Seven IC variants
(baseline plus six perturbations), matching FINDING_P76's own lever-gate set
plus FINDING_P79's most informative point:
baseline, psi0 x100, drA0 x10, dph0 x100, phibar_dot(1) x0.1/x0.5/x2. For each,
sweep a_end = a_star*(2,5,10,20,50,100) with a1=a_star*0.2 fixed (unchanged from
P107/P108), T-convergence on G_growth (NOT eps -- FINDING_P107's own lesson,
not re-derived here), final step x=50->100, <2%, matching P76's own gate.

REGRESSION CONTROL, before trusting anything: the "baseline" IC variant, at
this same Lambda and x-grid, should reproduce FINDING_P107's own published
G_infinity values at Lambda=1e-15 exactly (same underlying computation, same
default IC).

PRE-REGISTERED OUTCOMES:
  ATTRACTOR-LIKE-UNIVERSALITY   all seven IC variants individually T-converge on
                                G_growth AND the converged G_infinity values
                                agree across variants (relative spread < 5%,
                                matching FINDING_P107/P108's own threshold) ->
                                late-time dimensionless growth is robust to
                                BOTH Lambda-freedom and IC-freedom. The
                                strongest possible predictive-content result
                                for this completion.
  IC-DOMINATED                  all seven variants individually T-converge, but
                                the converged VALUES differ by > 5% across
                                variants -> Lambda-freedom washes out but
                                IC-freedom does not; initial-condition
                                selection becomes the next real bottleneck,
                                exactly the outcome the user's own writeup
                                anticipated.
  NOT-CONVERGED                 at least one IC variant fails its own <2%
                                T-convergence check even at x=50->100 -> the
                                growth observable is not well-defined for that
                                IC choice at this reach, reported as found.

WHAT THIS FILE DOES NOT DO: vary Lambda jointly with IC (a combined 2D test is
a natural, larger follow-up if this reveals structure, not attempted here).
Extend T_END (not needed, per reconnaissance). Quote eps(k), G_growth, or f(k)
in physical units, or any k[h/Mpc] number. Touch MULTING itself (Gate 1).
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


p105 = _load("P105_growth_with_lambda_cc.py", "p105_for_a109")

G_growth = p105.G_growth
a_star = p105.a_star
G_HAT_FIXED, LAM_FIXED = p105.G_HAT_FIXED, p105.LAM_FIXED
PHIDOT_INIT = p105.PHIDOT_INIT

LAMBDA_FIXED = 1e-15  # one of FINDING_P107's own full-reach, already-converged branches
T_END = 1e8  # unchanged -- reconnaissance found no widening is needed for IC variation
X_LO = 0.2
X_ENDS = (2.0, 5.0, 10.0, 20.0, 50.0, 100.0)
KS = (0.1, 1.0, 10.0)

IC_VARIANTS = (
    ("baseline", {}),
    ("psi0 x100", {"psi0": 1e-3}),
    ("drA0 x10", {"drA0": 1e-4}),
    ("dph0 x100", {"dph0": 1e-4}),
    ("phidot x0.1", {"phidot0": 0.1 * PHIDOT_INIT}),
    ("phidot x0.5", {"phidot0": 0.5 * PHIDOT_INIT}),
    ("phidot x2", {"phidot0": 2.0 * PHIDOT_INIT}),
)

CONV_TOL = 0.02  # matches P76's own gate
CROSS_VARIANT_TOL = 0.05  # matches FINDING_P107/P108's own threshold

# FINDING_P107's own published G_infinity at Lambda=1e-15, for the regression
# control on the "baseline" IC variant.
P107_REGRESSION = {0.1: 1.002239, 1.0: 1.051074, 10.0: 1.095773}
REGRESSION_TOL = 1e-4


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P109 -- attractor analysis: does G_infinity(k) converge across initial")
    print("        conditions, at a FIXED, already-converged Lambda?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print(f"\n  Lambda fixed at {LAMBDA_FIXED:.1e} (FINDING_P107's own full-reach branch)")
    print(f"  IC variants: {[v[0] for v in IC_VARIANTS]}")

    a0 = a_star(LAMBDA_FIXED)
    a1 = a0 * X_LO

    # ==================================================================
    print("\n" + "-" * 78)
    print("REGRESSION CONTROL -- baseline IC must reproduce FINDING_P107's own")
    print(f"published G_infinity at Lambda={LAMBDA_FIXED:.1e}")
    print("-" * 78)
    reg_ok = True
    for kk, published in P107_REGRESSION.items():
        g = G_growth(G_HAT_FIXED, LAM_FIXED, kk, a1, a0 * 100.0, T_END, lam_cc=LAMBDA_FIXED)
        rel = abs(g / published - 1.0) if g is not None else float("inf")
        ok = rel < REGRESSION_TOL
        reg_ok = reg_ok and ok
        print(
            f"    k={kk}: P107={published:.6f}  this file={g:.6f}  rel={rel:.3e}  "
            f"{'OK' if ok else 'MISMATCH'}"
        )
    print(f"\n    REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** baseline IC does not reproduce FINDING_P107's own numbers. STOP.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(f"SWEEP -- {len(IC_VARIANTS)} IC variants, x={X_ENDS},")
    print("T-convergence on G_growth (final step x=50->100, <2%)")
    print("-" * 78)
    converged = {kk: {} for kk in KS}
    not_converged = {kk: [] for kk in KS}
    for label, kw in IC_VARIANTS:
        print(f"\n  IC={label}")
        for kk in KS:
            vals = [
                G_growth(G_HAT_FIXED, LAM_FIXED, kk, a1, a0 * x, T_END, lam_cc=LAMBDA_FIXED, **kw)
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
                converged[kk][label] = vals[-1]
            else:
                not_converged[kk].append(label)

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    for kk in KS:
        print(f"\n  k={kk}:")
        n_conv = len(converged[kk])
        print(f"    IC variants T-converged: {n_conv}/{len(IC_VARIANTS)}")
        if not_converged[kk]:
            print(f"    NOT converged: {not_converged[kk]}")
        if n_conv < len(IC_VARIANTS):
            print(f"    -> NOT-CONVERGED at k={kk}. At least one IC variant fails its own")
            print(f"       <{CONV_TOL:.0%} T-convergence check even at x=50->100.")
            continue
        items = list(converged[kk].items())
        vals = [v for _l, v in items]
        spread = (max(vals) - min(vals)) / abs(sum(vals) / len(vals))
        worst_lo = min(items, key=lambda kv: kv[1])
        worst_hi = max(items, key=lambda kv: kv[1])
        print(
            f"    converged G_infinity range: [{worst_lo[1]:.6f} ({worst_lo[0]}), "
            f"{worst_hi[1]:.6f} ({worst_hi[0]})]"
        )
        print(f"    relative spread across IC variants: {spread:.4e}")
        if spread < CROSS_VARIANT_TOL:
            print(f"    -> ATTRACTOR-LIKE-UNIVERSALITY at k={kk}. All {len(IC_VARIANTS)} IC")
            print("       variants individually T-converge, AND the converged values agree")
            print(f"       to within {CROSS_VARIANT_TOL:.0%} -- late-time dimensionless growth")
            print("       is robust to BOTH Lambda-freedom (FINDING_P107/P108) and")
            print("       IC-freedom, at this Lambda.")
        else:
            print(f"    -> IC-DOMINATED at k={kk}. Every IC variant individually T-converges,")
            print(f"       but the converged values differ by more than {CROSS_VARIANT_TOL:.0%}")
            print("       across variants -- Lambda-freedom washes out but IC-freedom does")
            print("       not. Initial-condition selection becomes the next bottleneck.")

    print("\n  NOT ESTABLISHED:")
    print(f"   * anything at Lambda values other than {LAMBDA_FIXED:.1e} -- a combined")
    print("     Lambda-and-IC test was not attempted here.")
    print("   * anything about phibar_dot(1) x10 (kination-dominated, excluded per")
    print("     FINDING_P77/P79's own precedent -- not a legitimate IC variation).")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
