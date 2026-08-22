"""P96 -- does Planck's own uncertainty open a window, and does that touch the degeneracy?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P95 proved Omega_m=0.315 and Omega_Lambda=0.685 cannot be matched
EXACTLY, for any Lambda -- Omega_phi >= 0 identically forces Omega_Lambda <=
0.685 always. It registered a specific, narrow follow-up: since the measured
shortfall (Omega_phi ~ 1e-7 to 1e-4) is one to three orders BELOW Planck's own
+/-0.007 uncertainty on Omega_m/Omega_Lambda, relaxing exact equality to that
real measurement tolerance should open a viable window.

TWO DIFFERENT QUESTIONS, AND THIS FILE ANSWERS ONLY THE FIRST -- CONFLATING
THEM WOULD BE THE OVERCLAIM THIS FILE EXISTS TO PREVENT.

  Q1 (FINDING_P95's question, over-constraint): for a GIVEN Lambda, does SOME
     a_today put BOTH Omega_m and Omega_Lambda inside Planck's tolerance band
     simultaneously? Since Omega_phi is tiny compared to +/-0.007, this should
     hold for essentially any Lambda already known to give sensible Omega~0.7
     behaviour -- the shortfall that blocked EXACT equality is small enough to
     fit inside the measurement uncertainty.

  Q2 (FINDING_P94's question, degeneracy): WHICH Lambda is correct? Nothing
     about relaxing a tolerance on Omega_m/Omega_Lambda touches this. If exact
     equality was achievable for a wide range of DIFFERENT Lambda (P94's
     31.6x H_int spread), a LOOSER tolerance admits an equal-or-WIDER range of
     Lambda choices, each with its own small window -- the degeneracy across
     Lambda cannot be narrowed by loosening a constraint that already had
     multiple solutions before loosening.

So this file (a) tests Q1 as P95 registered it, and (b) explicitly measures
whether the H_int spread ACROSS different Lambda choices, even restricted to
each one's own tolerance window, stays as wide as FINDING_P94 found -- to
state plainly, with a number, that opening the window (if it opens) does
NOTHING for the degeneracy. A finding that only answered Q1 and stayed silent
on Q2 would let a reader conclude "the bridge is fixed"; it is not.

METHOD. For each of P94/P95's four Lambda seeds: scan a on a grid around the
EXACT Omega_m=0.315 root already located (FINDING_P94's a_today_precise), find
the sub-range where BOTH Omega_m in [0.308, 0.322] AND Omega_Lambda in
[0.678, 0.692] hold simultaneously (Planck 2018, Omega_m=0.315+/-0.007,
arXiv:1807.06209 -- same source used throughout this bridge arc). Record the
window's existence, its width in a, and the H_int range spanned within it.

PRE-REGISTERED OUTCOMES for Q1 (per Lambda, and overall):
  CONFIRMED   a nonempty joint-tolerance window exists for every Lambda tested
              -> FINDING_P95's over-constraint is resolved under realistic
              measurement uncertainty, exactly as predicted.
  REFUTED     no window exists for one or more Lambda -> the over-constraint
              is more severe than the small Omega_phi values suggested; the
              registered prediction is wrong and this must be said plainly.

Q2 is not scored pass/fail -- it is MEASURED and reported: the spread of
H_int across the four windows (min over any window's low end to max over any
window's high end), compared directly against FINDING_P94's own 31.623x.

WHAT THIS FILE DOES NOT DO: quote eps(k) or f(k) in physical units under any
outcome -- even CONFIRMED on Q1 does not license that, because Q2 (which
Lambda) remains open regardless, and this file says so explicitly rather than
letting a narrow Q1 win read as the whole bridge being resolved.
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


p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_tol")
p95 = _load("P95_joint_two_anchor_solve.py", "p95_for_tol")

OM_LO, OM_HI = 0.315 - 0.007, 0.315 + 0.007
OL_LO, OL_HI = 0.685 - 0.007, 0.685 + 0.007

# Same four Lambda seeds used throughout this bridge arc (P93/P94/P95), so the
# comparison to FINDING_P94's 31.623x is apples-to-apples, not a new sample.
LAMBDA_SEEDS = p94.LAMBDA_SEEDS


def scan_window(lam_cc, a_center, span_lo=0.5, span_hi=2.0, n=4000):
    """Fine grid around a_center; return rows inside BOTH Planck tolerance bands."""
    s = p94.solve_background_tagged(lam_cc)
    a_grid = np.geomspace(a_center * span_lo, a_center * span_hi, n)
    hits = []
    for a in a_grid:
        st = p95.state_full(s, a)
        if st is None:
            continue
        H, om_m, om_lam, _om_phi = st
        if OM_LO <= om_m <= OM_HI and OL_LO <= om_lam <= OL_HI:
            hits.append((a, H, om_m, om_lam))
    return hits


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P96 -- Planck tolerance window (Q1) versus the Lambda degeneracy (Q2)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n" + "-" * 78)
    print("Q1 -- does a joint Omega_m/Omega_Lambda tolerance window open, per Lambda?")
    print("-" * 78)
    print(f"  Omega_m in [{OM_LO:.3f}, {OM_HI:.3f}], Omega_Lambda in [{OL_LO:.3f}, {OL_HI:.3f}]")
    print("  (Planck 2018, Omega_m=0.315+/-0.007, arXiv:1807.06209)")

    all_H = []
    per_lambda = {}
    for label, lam_cc in LAMBDA_SEEDS.items():
        a_today_exact, _s = p95.inner_a_of_lambda(lam_cc)
        if a_today_exact is None:
            print(f"\n  {label}: exact root not found -- not measured (BLOCKED-INFRASTRUCTURE)")
            continue
        hits = scan_window(lam_cc, a_today_exact)
        print(f"\n  {label}  (Lambda={lam_cc:.4e}, exact-equality a_today={a_today_exact:.3f})")
        if not hits:
            print("    NO WINDOW -- zero grid points inside both tolerance bands")
            per_lambda[label] = None
            continue
        a_vals = [h[0] for h in hits]
        H_vals = [h[1] for h in hits]
        per_lambda[label] = (min(a_vals), max(a_vals), min(H_vals), max(H_vals))
        all_H.extend(H_vals)
        print(f"    window: {len(hits)} grid points, a in [{min(a_vals):.3f}, {max(a_vals):.3f}]")
        print(f"    H_int range within window: [{min(H_vals):.6e}, {max(H_vals):.6e}]")
        lo = hits[0]
        hi = hits[-1]
        print(f"    edge sample -- low a: Omega_m={lo[2]:.6f} Omega_Lambda={lo[3]:.6f}")
        print(f"    edge sample -- high a: Omega_m={hi[2]:.6f} Omega_Lambda={hi[3]:.6f}")

    measured = [v for v in per_lambda.values() if v is not None]
    q1_confirmed = len(measured) == len(per_lambda) and len(measured) >= 2

    print("\n" + "-" * 78)
    print("Q2 -- MEASURED, not scored: does the window touch the Lambda degeneracy?")
    print("-" * 78)
    print("  FINDING_P94's own spread (exact-equality H_int across four Lambda): 31.623095x")
    if len(all_H) >= 2:
        spread_tol = max(all_H) / min(all_H)
        print(f"  H_int spread across ALL tolerance windows, ALL Lambda tested: {spread_tol:.4f}x")
        print(
            f"  ratio of the two spreads (tolerance / exact-equality): {spread_tol / 31.623095:.4f}"
        )
        if spread_tol >= 31.623095 * 0.9:
            print("\n  The spread did NOT shrink. Loosening the constraint did not narrow")
            print("  which Lambda is right -- it only gave each Lambda more room to fit,")
            print("  which is what a genuine degeneracy across a FREE parameter looks like")
            print("  when the constraint on it is loosened rather than removed.")
        else:
            print("\n  The spread SHRANK relative to FINDING_P94's exact-equality figure.")
            print("  Unexpected -- would need its own explanation, not assumed here.")
    else:
        spread_tol = None
        print("  Fewer than two Lambda produced a window; spread not computable.")

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring, Q1 ONLY)")
    print("=" * 78)
    if q1_confirmed:
        print("  -> CONFIRMED (Q1). A nonempty joint-tolerance window exists for every")
        print("     Lambda tested. FINDING_P95's over-constraint is resolved under")
        print("     REALISTIC measurement uncertainty, as its own registered prediction")
        print("     said it should be.")
    else:
        n_open = len(measured)
        print(f"  -> REFUTED (Q1). Window opened for only {n_open}/{len(per_lambda)} Lambda")
        print("     tested. FINDING_P95's registered prediction does not hold as stated.")

    print()
    print("  Q2 IS NOT RESOLVED BY THIS OUTCOME EITHER WAY. Whether or not a per-Lambda")
    print("  window opens, WHICH Lambda the completion actually has is untouched --")
    if spread_tol is not None:
        print(f"  the {spread_tol:.1f}x spread above is the same free-parameter degeneracy")
        print("  FINDING_P94 found, now measured under tolerance instead of exact equality.")
    print("  NO k[h/Mpc] NUMBER IS QUOTED under any combination of these results.")

    print("\n  NOT ESTABLISHED:")
    print("   * which Lambda_internal the completion has -- still open (FINDING_P94).")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about MULTING itself (Gate 1). No dataset, no Table A1")
    print("     quantity enters this file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
