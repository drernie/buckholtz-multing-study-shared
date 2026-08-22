"""P104 -- Predictive Quotient (background level): does the completion's DIMENSIONLESS
H(a) shape survive the Lambda_internal freedom P103 proved is undetermined?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

USER-PROPOSED PIVOT, ACKNOWLEDGED BEFORE BUILDING. After FINDING_P103 proved
Lambda_internal is structurally undetermined by the current completion (the
clock-hand-not-connected-to-anything picture), the user pointed out P103
established only:

    NOT-DERIVABLE-IN-THIS-COMPLETION,  not  NOT-DERIVABLE-IN-PRINCIPLE.

That distinction is correct and is adopted here explicitly -- P103's own
"Not established" section already said the same thing ("that NO extension
... could supply Step 2 -- only that the CURRENT one cannot"), and this file
treats that as the operative reading of P103's verdict, not a correction to
it.

The user's proposed next question is sharper than "try a tenth anchor":
Lambda sets an unknown ABSOLUTE scale, but does it also change the SHAPE of
predictions in a scale-INVARIANT sense? Two possible worlds:

    M1 -- SCALE DEGENERACY ONLY.  Lambda is just a ruler/clock offset.
          Dimensionless, properly-normalized observables computed from
          DIFFERENT Lambda branches AGREE with each other. The completion
          still has predictive content -- it just can't be dated.
    M2 -- DYNAMICAL DEGENERACY.    Different Lambda branches give genuinely
          different dimensionless histories. Lambda is a full free
          parameter of the PHYSICS, not just of the units. A much more
          serious predictiveness problem.

SCOPE CUT MADE BEFORE BUILDING, NOT DISCOVERED MID-BUILD (Compute First,
applied to planning, not just numerics). The user's own examples --
k_J/(aH), ratios of f(k1)-f(k2) growth differences, transfer-function shape
-- are PERTURBATION-level observables, computed by G_growth()/f_recon() (the
P76-P92 growth-channel machinery). Checked before writing any code: grep for
lam_cc across every P-file in this arc. It appears ONLY in P81/P86 and the
P93-P103 bridge files -- NEVER in P76's growth_a_matched/G_growth or P89's
f_recon. The growth/perturbation solver was built and has ALWAYS run at
lam_cc=0, with no hook to accept anything else. Testing the user's exact
proposal (Jeans-scale ratios, f(k) shape) would require FIRST extending that
solver to accept lam_cc -- itself a new completion, per the user's own
observation, needing its own action-to-observables pass. NOT done here.
This file tests the SAME question (M1 vs M2) at the layer that IS already
built: the BACKGROUND's dimensionless H(a) shape, reusing P94/P99-P103's
already-validated solve_background_safe/H_at_a pipeline unchanged. A
genuine perturbation-level version is named as the natural next step, not
attempted.

THE DESIGN, ANCHOR-FREE BY CONSTRUCTION. Comparing shape(a):=H(a)/H(a_ref)
at a FIXED numeric a_ref across branches would be unfair -- different
Lambda trivially give different absolute H at any fixed a, which just
restates that Lambda sets scale, telling us nothing about SHAPE. Instead,
each branch gets its OWN, Lambda-INTRINSIC reference point:

    a_star(Lambda) := (C_MATTER / Lambda) ** (1/3)

-- the epoch where rho_Lambda = rho_matter, i.e. where Lambda's own energy
density first becomes comparable to matter's. This is an ALGEBRAIC
definition from the potential's own structure (C_MATTER is fixed = 1
throughout this arc), needs no external anchor, and mirrors exactly the
"a-today-as-a-definition-not-a-measurement" logic FINDING_P86 already used
for Omega_Lambda=0.7. Then define the dimensionless shape

    shape_Lambda(x) := H(a_star(Lambda)*x) / H(a_star(Lambda))

and ask whether shape_Lambda(x), as a FUNCTION of x, is the SAME across
different Lambda branches. If it collapses onto one curve -> M1. If it does
not -> M2.

CONTROL, BEFORE TRUSTING THE COMPARISON. At x << 1 (deep inside matter/field
domination, far below each branch's OWN Lambda-crossing point), Lambda's
own contribution to H^2 is parametrically small BY CONSTRUCTION of a_star --
this holds for every branch identically, regardless of what value Lambda
actually has, because a_star was chosen precisely to put x=1 at the
crossing. So shape_Lambda(x) at small x should be branch-INDEPENDENT
already, as a NECESSARY (not sufficient) precondition for trusting anything
computed at larger x. This is a control that CAN fail -- if a_star's
formula or H_at_a has a bug, branches would disagree even here.

PRE-REGISTERED OUTCOMES, evaluated on the relative spread of shape_Lambda(x)
across branches at each x > x_control (the region where Lambda genuinely
matters):
  CONVERGES (M1)     relative spread < 5% at every tested x -> dimensionless
                     shape is branch-invariant within the tested range;
                     supports scale-degeneracy-only. The completion retains
                     real, undated predictive content.
  DIVERGES (M2)      relative spread > 20% at any tested x -> different
                     Lambda branches give genuinely different dimensionless
                     histories; Lambda is a real dynamical free parameter,
                     not just a clock offset. A materially worse
                     predictiveness result than M1.
  MIXED              neither threshold cleanly met -- reported per-x, not
                     rounded to either extreme.

WHAT THIS FILE DOES NOT DO: touch the growth/perturbation channel (G_growth,
f_recon) at all -- those never accepted lam_cc and are unmodified here. Does
not quote eps(k), f(k), or any k[h/Mpc] number. Does not touch MULTING
itself (Gate 1).
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


p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_a104")
p100 = _load("P100_shape_hardened_wide_scan.py", "p100_for_a104")

solve_background_safe = p100.solve_background_safe
H_at_a = p100.H_at_a
C_MATTER = p94.C_MATTER

G_HAT_FIXED, LAM_FIXED = 1.0, 1.0  # the same (g_hat, lam) point the whole arc has used

# Chosen WITHOUT reference to any external anchor -- log-spaced INSIDE the
# window FINDING_P100/P102 already validated as measurable for this exact
# solve_background_safe + H_at_a pipeline: [1.125e-17, 4.924e-12]. A first
# attempt at this file used (1e-17...1e-9), which reaches OUTSIDE that
# window on the high end -- solve_background_safe(1e-9) came back s._ok=False
# outright (individually verified before the range was corrected here, not
# discovered by a silent partial run). Note this is NOT the same measurable
# window FINDING_P103 found for the DIFFERENT P81.viability() pipeline
# (which tops out near 1e-13) -- the two solvers are not interchangeable.
LAMBDA_BRANCHES = (2e-17, 1e-16, 1e-15, 1e-14, 1e-13, 3e-12)

X_CONTROL = 0.02  # deep matter/field domination -- branches must already agree here
X_GRID = (0.05, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0)

CONVERGE_TOL = 0.05
DIVERGE_TOL = 0.20


def a_star(lam_cc):
    return (C_MATTER / lam_cc) ** (1.0 / 3.0)


def shape_curve(lam_cc, xs):
    """shape_Lambda(x) for every x in xs, or None at any x where H_at_a fails."""
    s = solve_background_safe(lam_cc)
    a0 = a_star(lam_cc)
    if s is None:
        return None
    H_ref = H_at_a(s, a0)
    if H_ref is None or H_ref <= 0:
        return None
    out = []
    for x in xs:
        Hx = H_at_a(s, a0 * x)
        out.append((Hx / H_ref) if Hx is not None else None)
    return out


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P104 -- Predictive Quotient (background level): does dimensionless")
    print("        H(a) shape survive the Lambda_internal freedom FINDING_P103 proved?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print(f"\n  Lambda branches (anchor-free, log-spaced): {LAMBDA_BRANCHES}")
    stars = {lc: a_star(lc) for lc in LAMBDA_BRANCHES}
    print("\n    Lambda           a_star = (C_MATTER/Lambda)^(1/3)")
    for lc, a0 in stars.items():
        print(f"    {lc:<16.4e}{a0:.4f}")

    # ==================================================================
    print("\n" + "-" * 78)
    print(f"CONTROL -- at x={X_CONTROL} (deep matter/field domination), shape_Lambda(x)")
    print("must already be branch-independent, BEFORE trusting anything at larger x")
    print("-" * 78)
    control_vals = {}
    for lc in LAMBDA_BRANCHES:
        v = shape_curve(lc, [X_CONTROL])
        control_vals[lc] = v[0] if v is not None else None
        print(f"    Lambda={lc:<12.4e} shape({X_CONTROL}) = {control_vals[lc]!r}")

    measured_control = [v for v in control_vals.values() if v is not None]
    if len(measured_control) < len(LAMBDA_BRANCHES):
        print(f"\n  *** {len(LAMBDA_BRANCHES) - len(measured_control)} branch(es) unmeasurable")
        print("  *** at the control point. Cannot trust the comparison. STOP.")
        return 1
    control_spread = (max(measured_control) - min(measured_control)) / np.mean(measured_control)
    control_ok = control_spread < CONVERGE_TOL
    print(f"\n    relative spread at control point: {control_spread:.4e}")
    print(f"    CONTROL {'PASSES' if control_ok else 'FAILS'} (threshold {CONVERGE_TOL:.0%})")
    if not control_ok:
        print("    *** branches disagree even in the matter-domination-adjacent regime,")
        print("    *** where Lambda should be negligible by construction of a_star.")
        print("    *** Something is wrong with a_star or H_at_a -- STOP, do not trust")
        print("    *** anything computed at larger x below.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(
        f"MAIN COMPARISON -- shape_Lambda(x) across {len(X_GRID)} x-values, "
        f"{len(LAMBDA_BRANCHES)} branches"
    )
    print("-" * 78)
    curves = {}
    for lc in LAMBDA_BRANCHES:
        curves[lc] = shape_curve(lc, X_GRID)

    print(
        f"\n    {'x':<8}"
        + "".join(f"Lam={lc:.1e}".ljust(16) for lc in LAMBDA_BRANCHES)
        + "rel.spread"
    )
    spreads = {}
    for i, x in enumerate(X_GRID):
        vals = [curves[lc][i] for lc in LAMBDA_BRANCHES]
        row = "".join((f"{v:<16.6f}" if v is not None else f"{'--':<16}") for v in vals)
        valid = [v for v in vals if v is not None]
        if len(valid) == len(LAMBDA_BRANCHES):
            spread = (max(valid) - min(valid)) / np.mean(valid)
            spreads[x] = spread
            print(f"    {x:<8g}{row}{spread:.4e}")
        else:
            print(f"    {x:<8g}{row}{'not measurable at all branches'}")

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if not spreads:
        print("  -> NOT MEASURABLE at any x beyond the control point. Infrastructure")
        print("     outcome, not evidence either way.")
        return 1

    worst_x, worst_spread = max(spreads.items(), key=lambda kv: kv[1])
    all_converge = all(s < CONVERGE_TOL for s in spreads.values())
    any_diverge = any(s > DIVERGE_TOL for s in spreads.values())
    print(f"  worst relative spread: {worst_spread:.4e} at x={worst_x}")
    print(f"  every x < {CONVERGE_TOL:.0%} threshold: {all_converge}")
    print(f"  any x > {DIVERGE_TOL:.0%} threshold: {any_diverge}")

    if all_converge:
        print("\n  -> CONVERGES (M1 -- scale degeneracy only).")
        print("     Dimensionless shape_Lambda(x) agrees across independently-chosen,")
        print("     unanchored Lambda branches to within 5% everywhere tested. Lambda")
        print("     behaves as a clock/ruler offset -- it sets WHERE the completion's")
        print("     history sits, not WHAT SHAPE that history has. The completion retains")
        print("     real, dateable-only-not-shapeable predictive content: the SAME")
        print("     structural freedom P103 proved for the absolute scale does not, on")
        print("     this test, propagate into the dimensionless dynamics.")
    elif any_diverge:
        print("\n  -> DIVERGES (M2 -- dynamical degeneracy).")
        print("     Dimensionless shape_Lambda(x) disagrees by more than 20% across")
        print("     branches at at least one tested x, despite passing the")
        print("     matter-domination-adjacent control. Lambda is not just a clock")
        print("     offset here -- different branches predict genuinely different")
        print("     dimensionless histories. This is a MATERIALLY WORSE predictiveness")
        print("     result than M1: the completion's underdetermination is not confined")
        print("     to normalization.")
    else:
        print("\n  -> MIXED. Neither threshold cleanly met across the full x range --")
        print("     reported per-x above, not rounded to either extreme.")

    print("\n  NOT ESTABLISHED:")
    print("   * anything at the PERTURBATION/growth level (f(k), Jeans scale, transfer")
    print("     function) -- G_growth/f_recon never accepted lam_cc; a genuine")
    print("     perturbation-level Predictive Quotient test requires extending that")
    print("     solver first, itself a new completion needing its own full pass.")
    print("   * that X_GRID's range [0.05,10] is wide enough -- collapse or divergence")
    print("     outside this range was not tested.")
    print(f"   * that {len(LAMBDA_BRANCHES)} log-spaced branches are representative of the FULL")
    print("     measurable Lambda range -- a denser branch scan was not attempted here.")
    print("   * any numeric value of eps(k), f(k), or k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
