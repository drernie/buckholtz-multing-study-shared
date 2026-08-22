"""P107 -- close the gap FINDING_P106 found: does the completion's growth observable
reach a CONVERGED asymptotic value at P76-comparable reach, and does the converged
value still agree across Lambda branches?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHAT WAS LEFT OPEN. FINDING_P106 found that eps(k;Lambda) at FINDING_P105's own
comparison window ([0.2, 2.0]*a_star) is STILL window-length-dependent even at
P76's own "certified" k -- P105's CONVERGES (M1) verdict measured a SNAPSHOT, not
a confirmed asymptotically converged rate. P76's OWN original convergence check
reached ~2.6 decades past its reference point before trusting a number.
P104-P106 never got close to that reach. This file does -- and finds that the
RIGHT quantity to test convergence on, in the regime this file reaches, is not
the one P105/P106 used.

RECONNAISSANCE FIRST, NOT ASSUMED. Before designing the sweep, probed how far
EACH of P105's 6 branches can actually integrate before T_END=1e8 caps them.
Genuinely asymmetric, not uniform:

    Lambda        a_star      a(T_END)/a_star (decades past crossing)
    2e-17         368403      2.3x     (0.36 decades)  -- barely past its own crossing
    1e-16         215443      11.4x    (1.06 decades)
    1e-15         100000      5948x    (3.77 decades)
    1e-14          46416      2.3e12x  (12.4 decades)
    1e-13          21544      3.5e42x  (39.6 decades) -- already overflow-adjacent
    3e-12           6934      3.3e229x (217 decades) -- deep float64 overflow territory

Larger Lambda means faster de Sitter expansion once Lambda dominates -- a(T_END)
grows explosively for larger Lambda, not because more physics happens but because
de Sitter growth is exponential in Lambda's own rate. The two smallest Lambda
values genuinely cannot be pushed far past their own crossing within T_END=1e8 --
a real infrastructure limit, confirmed empirically before the sweep was designed:
x=(2,5,10,20,50,100) resolves cleanly through x=100 for FOUR of six branches
(1e-15, 1e-14, 1e-13, 3e-12); Lambda=1e-16 resolves only through x=10; Lambda=2e-17
resolves ONLY at x=2, the same point FINDING_P105/P106 already used.

A DESIGN CORRECTION FOUND MID-BUILD, BEFORE TRUSTING THE FIRST RESULT. The first
version of this file swept eps(k;Lambda) = ln(G)/ln(a2/a1) exactly as P105/P106
did, just over the much wider x-grid above. Every branch, every k, came back
"NOT-CONVERGED" -- eps declined smoothly and almost IDENTICALLY (~11% per step)
across every k and every Lambda, all the way to x=100. That near-universal,
k-and-Lambda-independent decay pattern was the tell that something structural, not
physical, was being measured -- checked before writing any verdict, not after.
Diagnosis: G_growth itself was queried directly at the SAME points, and it
SATURATES cleanly (e.g. Lambda=1e-15, k=1: G=1.04638 -> 1.05016 -> 1.05083 ->
1.05101 -> 1.05107 -> 1.05107, final-step change 0.0008%). Once Lambda dominates,
matter perturbation growth FREEZES (matter dilutes away, nothing left to grow),
so the coupled-vs-uncoupled ratio G_growth stops accumulating and settles to a
constant G_infinity. But eps := ln(G)/ln(a2/a1) has a BOUNDED numerator
(ln(G_infinity)) divided by an UNBOUNDED, ever-growing denominator (ln(a2/a1)) --
it is MATHEMATICALLY GUARANTEED to decay toward zero once G saturates, regardless
of any Lambda-dependence question. This is not a new finding about this
completion; it is the exact condition FINDING_P76's own Part G already named for
when eps is the wrong tool: "IF the force induces a PERSISTENT rate shift, [G]
keeps rising with the window" -- eps was built for that regime (pure matter
domination, no Lambda, where P76 originally tested it and G never stopped
growing). Once Lambda dominates and growth freezes, that condition fails, and G
itself -- not eps -- is the well-defined, convergent quantity. Corrected: this
file's T-convergence check and cross-branch comparison use G_growth, with eps
reported alongside and its necessary decay explained, not treated as evidence.

THE TEST. For the four full-reach branches, sweep a_end = a_star*(2, 5, 10, 20,
50, 100) with a1 = a_star*0.2 fixed (unchanged from P105/P106). PER-BRANCH
T-CONVERGENCE on G_growth, mirroring P76's own gate: the LAST TWO points
(x=50 -> x=100) must differ by < 2% before a branch's G is trusted as converged.
Only THEN is the converged G_infinity used for the CROSS-BRANCH comparison this
arc has been trying to reach honestly.

PRE-REGISTERED OUTCOMES, per k, evaluated on G_growth for the four full-reach
branches:
  CONVERGES-CONFIRMED    all four branches individually T-converge (<2% over the
                         final step) AND the converged G_infinity values agree
                         across branches (relative spread < 5%) -> the
                         completion's growth observable, evaluated at a genuine
                         P76-comparable asymptotic reach, is Lambda-independent.
                         Strongest form of M1 this arc has produced -- including,
                         for the first time, a clean answer at k=0.1.
  STILL-NOT-CONVERGED    at least one full-reach branch fails its own <2%
                         T-convergence check on G_growth itself -> the growth
                         observable is not well-defined at that k even in this
                         much wider reach, regardless of Lambda.
  CONVERGES-BUT-DISAGREE all four branches individually T-converge, but the
                         converged G_infinity values differ by > 5% across
                         branches -> genuine M2 evidence in a properly converged
                         quantity, not window noise.

WHAT THIS FILE DOES NOT DO: extend T_END past 1e8, or work around the two
reach-limited branches' (2e-17, 1e-16) infrastructure boundary. Quote eps(k) or
f(k) in physical units, or any k[h/Mpc] number. Touch MULTING itself (Gate 1).
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


p105 = _load("P105_growth_with_lambda_cc.py", "p105_for_a107")

G_growth = p105.G_growth
eps_of_k = p105.eps_of_k
a_star = p105.a_star
G_HAT_FIXED, LAM_FIXED = p105.G_HAT_FIXED, p105.LAM_FIXED

T_END = 1e8
X_LO = 0.2
X_ENDS = (2.0, 5.0, 10.0, 20.0, 50.0, 100.0)
KS = (0.1, 1.0, 10.0)

FULL_REACH = (1e-15, 1e-14, 1e-13, 3e-12)
LIMITED_REACH = (2e-17, 1e-16)
LIMITED_REACH_MAX_X = {2e-17: 2.0, 1e-16: 10.0}

CONV_TOL = 0.02  # matches P76's own T-convergence gate exactly
CROSS_BRANCH_TOL = 0.05  # tighter than P105's snapshot 5%/10%, since these ARE converged


def sweep_branch(lc, kk, xs):
    a0 = a_star(lc)
    a1 = a0 * X_LO
    g_out, e_out = [], []
    for x in xs:
        g_out.append(G_growth(G_HAT_FIXED, LAM_FIXED, kk, a1, a0 * x, T_END, lam_cc=lc))
        e_out.append(eps_of_k(G_HAT_FIXED, LAM_FIXED, kk, a1, a0 * x, T_END, lam_cc=lc))
    return g_out, e_out


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P107 -- asymptotic convergence test: does G_growth(k;Lambda) reach a")
    print("        CONVERGED value at P76-comparable reach, and does it agree")
    print("        across branches?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print(f"\n  full-reach branches (x up to 100 confirmed): {FULL_REACH}")
    print(f"  limited-reach branches (reported, excluded from converged compare): {LIMITED_REACH}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("LIMITED-REACH BRANCHES -- reported honestly, whatever they have")
    print("-" * 78)
    for lc in LIMITED_REACH:
        max_x = LIMITED_REACH_MAX_X[lc]
        xs_here = [x for x in X_ENDS if x <= max_x]
        print(f"\n  Lambda={lc:.4e} (max safe x={max_x}):")
        for kk in KS:
            g_vals, _e_vals = sweep_branch(lc, kk, xs_here)
            row = "".join(
                f"x={x}:{v:.6f}  " if v is not None else f"x={x}:--  "
                for x, v in zip(xs_here, g_vals, strict=True)
            )
            print(f"    k={kk:<6} G={row}")
    print("\n  These two branches cannot be tested for asymptotic convergence within")
    print("  T_END=1e8 -- a real infrastructure boundary (small Lambda means slow de")
    print("  Sitter growth means little reach past their own crossing), not fixed")
    print("  here. Excluded from the converged comparison below.")

    # ==================================================================
    print("\n" + "-" * 78)
    print(f"FULL-REACH BRANCHES -- sweep x={X_ENDS}, T-convergence on G_growth,")
    print("final step (x=50 -> x=100), matching P76's OWN <2% gate exactly")
    print("-" * 78)
    converged = {kk: {} for kk in KS}
    not_converged = {kk: [] for kk in KS}
    for lc in FULL_REACH:
        print(f"\n  Lambda={lc:.4e}, a_star={a_star(lc):.4f}")
        for kk in KS:
            g_vals, e_vals = sweep_branch(lc, kk, X_ENDS)
            g_row = "".join(f"{v:<12.6f}" if v is not None else f"{'--':<12}" for v in g_vals)
            e_row = "".join(f"{v:<12.6f}" if v is not None else f"{'--':<12}" for v in e_vals)
            valid_last_two = g_vals[-2] is not None and g_vals[-1] is not None
            if valid_last_two:
                final_change = (
                    abs(g_vals[-1] / g_vals[-2] - 1.0) if g_vals[-2] != 0 else float("inf")
                )
                conv_ok = final_change < CONV_TOL
            else:
                final_change = float("nan")
                conv_ok = False
            status = "CONVERGED" if conv_ok else "NOT-CONVERGED"
            print(f"    k={kk:<6} G={g_row} final-step-change={final_change:.4%}  {status}")
            print(
                f"    {'':<7} eps={e_row}(reported, not the convergence criterion -- see docstring)"
            )
            if conv_ok:
                converged[kk][lc] = g_vals[-1]
            else:
                not_converged[kk].append(lc)

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    for kk in KS:
        print(f"\n  k={kk}:")
        n_conv = len(converged[kk])
        print(f"    branches T-converged on G_growth: {n_conv}/{len(FULL_REACH)}")
        if not_converged[kk]:
            print(f"    NOT converged: {not_converged[kk]}")
        if n_conv < len(FULL_REACH):
            print(f"    -> STILL-NOT-CONVERGED at k={kk}. At least one full-reach branch")
            print(f"       fails its own <{CONV_TOL:.0%} T-convergence check on G_growth")
            print("       itself, even at x=50->100.")
            continue
        vals = list(converged[kk].values())
        spread = (max(vals) - min(vals)) / abs(sum(vals) / len(vals))
        print(
            f"    converged G_infinity range: [{min(vals):.6f}, {max(vals):.6f}], "
            f"relative spread {spread:.4e}"
        )
        if spread < CROSS_BRANCH_TOL:
            print(f"    -> CONVERGES-CONFIRMED at k={kk}. All {len(FULL_REACH)} full-reach")
            print("       branches individually T-converge on G_growth, AND the converged")
            print(f"       G_infinity values agree to within {CROSS_BRANCH_TOL:.0%} across")
            print("       branches. The completion's growth observable, at a genuine")
            print("       P76-comparable asymptotic reach, is Lambda-independent here.")
        else:
            print(f"    -> CONVERGES-BUT-DISAGREE at k={kk}. Every branch individually")
            print("       T-converges, but the converged G_infinity values differ by more")
            print(f"       than {CROSS_BRANCH_TOL:.0%} across branches -- genuine M2 evidence")
            print("       in a properly converged quantity.")

    print("\n  ON eps (reported, not scored): eps := ln(G)/ln(a2/a1) declines toward")
    print("  zero across this whole sweep, at nearly the SAME rate regardless of k or")
    print("  Lambda -- a mathematical consequence of G saturating while the window")
    print("  keeps growing, not a physics finding. Comparing eps at this reach would")
    print("  have wrongly read as STILL-NOT-CONVERGED for everything; G_growth is the")
    print("  quantity that is actually well-defined once Lambda dominates.")

    print("\n  NOT ESTABLISHED:")
    print("   * anything about the two limited-reach branches (2e-17, 1e-16) beyond")
    print("     what was reported for them -- not pushed further within T_END=1e8.")
    print("   * that extending T_END past 1e8 would not change the picture for the")
    print("     limited-reach branches -- not attempted, given the overflow risk for")
    print("     the LARGE-Lambda branches already near float64 limits.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
