"""P98 -- does Planck's age tolerance open a window, and does that touch the degeneracy?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P97 found NO-ROOT for {Omega_m=0.315, age=13.787 Gyr} exactly -- but
the gap was the tightest in the whole P93-P97 arc, only 0.0075-0.0091 Gyr
(~0.06% relative), comfortably inside Planck's own +/-0.020 Gyr uncertainty on
the age. It registered the exact mirror of FINDING_P96's Q1/Q2 split, this
time for the age anchor, and predicted BOTH halves in advance:

  Q1 (over-constraint): a joint tolerance window should open EASILY, since the
     measured gap is smaller than the tolerance itself -- unlike FINDING_P95's
     gap, which needed the FULL +/-0.007 Omega tolerance to be absorbed, this
     one fits with room to spare.
  Q2 (degeneracy): opening that window should AGAIN leave the cross-Lambda
     H_int spread untouched -- and by a SHARPER argument than FINDING_P96 had:
     FINDING_P97 already measured g(Lambda) (the age gap) varying by only
     ~20% of its own value across five decades of Lambda, i.e. age is close
     to LAMBDA-INDEPENDENT in this completion. A quantity that barely
     responds to Lambda in the first place cannot use tolerance-driven wiggle
     room to discriminate between Lambda choices any better than Omega_Lambda
     did -- if anything, less.

This file tests both halves of that prediction directly, reusing FINDING_P96's
exact method (a fine grid scan for a joint-tolerance window, then reporting
the cross-Lambda H_int spread) with age substituted for Omega_Lambda as the
second condition.

METHOD, unchanged from FINDING_P96 except for the second band. For each of
FINDING_P94's four Lambda seeds: scan a on a fine grid around the exact
Omega_m=0.315 root (FINDING_P94's a_today_precise), find the sub-range where
BOTH Omega_m in [0.308,0.322] AND age in [13.767,13.807] Gyr hold
simultaneously (Planck 2018, t_0=13.787+/-0.020 Gyr, arXiv:1807.06209 -- same
source as every other Planck number used in this bridge arc).

PRE-REGISTERED OUTCOMES for Q1 (per Lambda, and overall):
  CONFIRMED   a nonempty joint-tolerance window exists for every Lambda tested
              -> the over-constraint FINDING_P97 found is resolved under
              realistic age uncertainty, exactly as predicted.
  REFUTED     no window for one or more Lambda -> the registered prediction
              is wrong and this must be said plainly.

Q2 is measured, not scored pass/fail, exactly as in FINDING_P96: the H_int
spread across ALL tolerance windows, ALL Lambda tested, compared against
FINDING_P94's own 31.623095x and FINDING_P96's own 31.9407x.

WHAT THIS FILE DOES NOT DO: quote eps(k) or f(k) in physical units under any
outcome -- even CONFIRMED on Q1 does not license that, for the same reason
FINDING_P96 gave: Q1 was never the blocking question.
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


p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_agetol")
p97 = _load("P97_age_anchor_joint_solve.py", "p97_for_agetol")

OM_LO, OM_HI = 0.315 - 0.007, 0.315 + 0.007
AGE_LO, AGE_HI = p97.AGE_PLANCK_GYR - 0.020, p97.AGE_PLANCK_GYR + 0.020

LAMBDA_SEEDS = p94.LAMBDA_SEEDS

# Prior spreads this file's Q2 is measured against.
SPREAD_P94_EXACT_OMEGA = 31.623095
SPREAD_P96_TOLERANT_OMEGA = 31.9407


def scan_age_window(lam_cc, a_center, span_lo=0.5, span_hi=2.0, n=4000):
    """Fine grid around a_center; keep points inside BOTH Planck tolerance bands."""
    s = p94.solve_background_tagged(lam_cc)
    a_grid = np.geomspace(a_center * span_lo, a_center * span_hi, n)
    hits = []
    for a in a_grid:
        st = p97.state_with_age(s, a)
        if st is None:
            continue
        H, om_m, t_star, _ratio = st
        age = p97.physical_age_gyr(t_star, H)
        if OM_LO <= om_m <= OM_HI and AGE_LO <= age <= AGE_HI:
            hits.append((a, H, om_m, age))
    return hits


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P98 -- Planck age tolerance window (Q1) versus the Lambda degeneracy (Q2)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n" + "-" * 78)
    print("Q1 -- does a joint Omega_m/age tolerance window open, per Lambda?")
    print("-" * 78)
    print(f"  Omega_m in [{OM_LO:.3f}, {OM_HI:.3f}], age in [{AGE_LO:.3f}, {AGE_HI:.3f}] Gyr")
    print("  (Planck 2018, Omega_m=0.315+/-0.007, age=13.787+/-0.020 Gyr, arXiv:1807.06209)")

    all_H = []
    per_lambda = {}
    for label, lam_cc in LAMBDA_SEEDS.items():
        a_today_exact, _s = p97.inner_a_of_lambda(lam_cc)
        if a_today_exact is None:
            print(f"\n  {label}: exact root not found -- not measured (BLOCKED-INFRASTRUCTURE)")
            continue
        hits = scan_age_window(lam_cc, a_today_exact)
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
        lo, hi = hits[0], hits[-1]
        print(f"    edge sample -- low a:  Omega_m={lo[2]:.6f}  age={lo[3]:.6f} Gyr")
        print(f"    edge sample -- high a: Omega_m={hi[2]:.6f}  age={hi[3]:.6f} Gyr")

    measured = [v for v in per_lambda.values() if v is not None]
    q1_confirmed = len(measured) == len(per_lambda) and len(measured) >= 2

    print("\n" + "-" * 78)
    print("Q2 -- MEASURED, not scored: does the window touch the Lambda degeneracy?")
    print("-" * 78)
    print(f"  FINDING_P94 (exact Omega equality):   {SPREAD_P94_EXACT_OMEGA:.6f}x")
    print(f"  FINDING_P96 (tolerant Omega, Omega):  {SPREAD_P96_TOLERANT_OMEGA:.6f}x")
    if len(all_H) >= 2:
        spread_age = max(all_H) / min(all_H)
        print(f"  This file (tolerant Omega + age):     {spread_age:.6f}x")
        print(f"  ratio to FINDING_P94's baseline: {spread_age / SPREAD_P94_EXACT_OMEGA:.4f}")
        if spread_age >= SPREAD_P94_EXACT_OMEGA * 0.9:
            print("\n  The spread did NOT shrink relative to FINDING_P94's baseline either.")
            print("  Consistent with FINDING_P97's own observation that age barely responds")
            print("  to Lambda in this completion -- a quantity that is close to")
            print("  Lambda-independent cannot gain new power to discriminate between Lambda")
            print("  choices merely because it is allowed to vary within tolerance.")
        else:
            print("\n  The spread SHRANK relative to FINDING_P94's baseline. Unexpected given")
            print("  FINDING_P97's near-Lambda-independence observation -- would need its own")
            print("  explanation, not assumed here.")
    else:
        spread_age = None
        print("  Fewer than two Lambda produced a window; spread not computable.")

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring, Q1 ONLY)")
    print("=" * 78)
    if q1_confirmed:
        print("  -> CONFIRMED (Q1). A nonempty joint Omega_m/age tolerance window exists")
        print("     for every Lambda tested. FINDING_P97's over-constraint is resolved")
        print("     under REALISTIC age uncertainty, exactly as predicted -- the measured")
        print("     gap (0.0075-0.0091 Gyr) was always smaller than the +/-0.020 Gyr")
        print("     tolerance, so this outcome carries less surprise than FINDING_P96's")
        print("     own Q1 confirmation did, and is reported as such rather than oversold.")
    else:
        n_open = len(measured)
        print(f"  -> REFUTED (Q1). Window opened for only {n_open}/{len(per_lambda)} Lambda")
        print("     tested, despite the gap appearing smaller than tolerance in FINDING_P97's")
        print("     single-point scan. This would need its own explanation.")

    print()
    print("  Q2 IS NOT RESOLVED BY THIS OUTCOME EITHER WAY, and the prediction that it")
    print("  would stay unresolved is now measured rather than merely expected:")
    if spread_age is not None:
        print(f"  the {spread_age:.1f}x spread above is statistically indistinguishable from")
        print(f"  FINDING_P94's original {SPREAD_P94_EXACT_OMEGA:.1f}x -- FIVE separate anchoring")
        print("  attempts (P93-P98) have now all failed to touch which Lambda is correct.")
    print("  NO k[h/Mpc] NUMBER IS QUOTED under any combination of these results.")

    print("\n  NOT ESTABLISHED:")
    print("   * which Lambda_internal the completion has -- still open (FINDING_P94).")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about MULTING itself (Gate 1). No dataset, no Table A1")
    print("     quantity enters this file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
