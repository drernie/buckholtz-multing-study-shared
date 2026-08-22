"""P89 -- the growth rate f, recomputed by P88's independent implementation.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

P88 met Perelman condition 5 for eps(k) and for NOTHING ELSE, and its own
finding named f as the cheapest next target: FINDING_P82's agreement with P77
is scoped weak-to-medium precisely because one implementation produced both
numbers. This file is the registered follow-up, and it is a real test of P88's
falsifiable prediction -- if a second implementation of f DISAGREES above 1e-4,
then P88's agreement was specific to eps and does not license treating the
shared solver as verified.

WHAT IS INDEPENDENT HERE, AND WHAT DELIBERATELY IS NOT.
  The SOLVER is P88's: N = ln a as the independent variable, a as the axis, H
  from the Friedmann constraint algebraically, 8 state variables, DOP853. It
  shares no computational code with P76 -- p88_independence_probe.py measured
  that rather than asserting it (0 mentions of P76 in the executable half, the
  fragment runs standalone and reproduces its number bitwise).
  The DERIVATIVE OPERATOR is new here and is also structurally different:

    P82                                  this file
    ---------------------------------    ---------------------------------
    central difference in ln t,          central difference in N = ln a
      then divide by d ln a                DIRECTLY -- f is the derivative
      measured over the same step          with respect to the integration
                                           variable, so no division and no
                                           second differenced quantity
    a(t) never inverted; points are      a IS the coordinate, so the
      matched at equal t                   evaluation point is exact

  So two things differ at once relative to P82 -- solver and difference scheme.
  That is deliberate: the question is whether the NUMBER survives a different
  route, not which of the two ingredients carries a discrepancy. If one appears,
  isolating it is a separate step, and this file says so rather than guessing.

THE DESIGN DECISION THAT DECIDES WHETHER THIS GATE MEASURES ANYTHING.
  f is about 1.04. Roughly 96 percent of it is the matter-domination growing
  mode delta ~ a, which BOTH implementations reproduce trivially -- P88's own
  L1 lock mass already showed the reconstruction gets f = 1 to 1.004e-06 with
  the coupling off. A relative comparison on f would therefore be dominated by
  the part that cannot fail, and would report a small number no matter what the
  coupling sector did. That is exactly the failure this campaign keeps
  catching: the gate measuring something other than what the claim asserts.

  So the PRE-REGISTERED criterion is on

      df := f(g_hat=1) - f(g_hat=0)

  where the coupling is the whole signal. df is about 0.04, so the same absolute
  error shows up roughly 25x larger in df than in f. Both are printed; only df
  is scored.

PRE-REGISTERED OUTCOMES (fixed before any number):
  F-CONFIRMED   relative agreement on df < 1e-4 at every (k, a) tested
                -> P88's prediction survives its first real test, and Perelman
                   condition 5 extends to f at the same rung and no higher.
  F-MARGINAL    between 1e-4 and 1e-2 -> survives, but the difference must be
                   named before f may be called reconstructed.
  F-DISCREPANT  worse than 1e-2 -> P88's agreement was specific to eps. The
                   shared solver is NOT verified, and the campaign's use of f
                   is in doubt until the cause is found.

CONTROLS, each able to fail:
  L1  external lock mass f -> 1 where Omega_phi is demonstrably small. P82's
      trap applies unchanged: our background is NOT pure matter domination, the
      scalar carries kinetic and potential energy, so an f below 1 could be
      CORRECT PHYSICS wearing the costume of a broken pipeline. Omega_phi is
      printed beside every f and the assertion is made only where it is small.
  L2  negative control on the QUANTITY -- the same pipeline run on the raw
      Delta_m instead of the contrast must land at f - 3, since
      Delta_m = delta * rho_phys ~ delta * a^-3. A gate that cannot tell the
      right quantity from the wrong one is not a gate.
  L3  negative control on the COMPARISON -- the Euler exchange term's sign is
      flipped in the reconstruction ONLY, and the agreement on df must collapse.

WHAT THIS CANNOT DO, STATED BEFORE THE NUMBERS:
  * Same person wrote both implementations. Different MODEL, blind replication,
    new physical experiment: all still absent. Strong, not Very strong.
  * A reconstruction tests the IMPLEMENTATION, never the SPECIFICATION. Two
    faithful solutions of the same wrong equations agree beautifully.
  * Nothing observational. NO_BRIDGE_FITTING untouched. Nothing about MULTING.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
T_END = 1e8
LAM = 1.0
KS = (3.0, 10.0, 30.0)
A_PROBE = (1e4, 1e5, 4e5)
H_STEP = 1e-4


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p88 = _load("P88_independent_reconstruction.py", "p88_for_f")
p76 = _load("P76_growth_observable.py", "p76_for_f")
p82 = _load("P82_growth_rate.py", "p82_for_f")


# ---------------------------------------------------------------------------
# THE RECONSTRUCTION SIDE. P88's solver, a derivative operator written here.
# ---------------------------------------------------------------------------


def solve_recon(g, lam, k, a_max, sign_euler=1.0, rtol=1e-11):
    return solve_ivp(
        p88.rhs_lnA(g, lam, k, sign_euler),
        (np.log(p88.A_0), np.log(a_max) + 0.05),
        p88.initial_state(g, lam, k),
        method="DOP853",
        rtol=rtol,
        atol=1e-22,
        dense_output=True,
    )


def f_recon(sol, a, g, lam, h=H_STEP):
    """f = d ln delta / d ln a, differenced in the INTEGRATION VARIABLE itself.

    # WHY this is not P82's scheme: P82 steps ln t and divides by the measured
    # d ln a, so two differenced quantities enter and a(t) sits in the
    # denominator. Here N = ln a IS the axis, so the same definition needs one
    # difference and no division.
    """
    d_p = p88.contrast_recon(a * np.exp(h), sol.sol(np.log(a) + h), g, lam)
    d_m = p88.contrast_recon(a * np.exp(-h), sol.sol(np.log(a) - h), g, lam)
    return np.log(d_p / d_m) / (2.0 * h)


def f_raw_recon(sol, a, g, lam, h=H_STEP):
    """L2's wrong quantity: the raw Delta_m = delta * rho_phys, not the contrast."""

    def raw(aa):
        y = sol.sol(np.log(aa))
        _, _, _, rho_phys = p88._H_and_Hdot(aa, y[0], y[1], g, lam)
        return p88.contrast_recon(aa, y, g, lam) * rho_phys

    return np.log(raw(a * np.exp(h)) / raw(a * np.exp(-h))) / (2.0 * h)


def dln_coupling_factor(sol, a, g, h=H_STEP):
    """d ln(1 - g*phibar) / d ln a -- the exact reason f_raw - f is not -3.

    # WHY this has to be MEASURED rather than dropped: at g_hat=0 it is
    # identically zero, so a control run only at g_hat=0 cannot tell "the code
    # handles the coupling factor correctly" from "the coupling factor never
    # appeared in the expression". Measuring it is what makes the g_hat=1 row a
    # test instead of a restatement.
    """

    def lf(aa):
        return np.log(1.0 - g * sol.sol(np.log(aa))[0])

    return (lf(a * np.exp(h)) - lf(a * np.exp(-h))) / (2.0 * h)


def omega_phi_recon(sol, a, g, lam):
    """The scalar's energy fraction, so L1 can be asserted only where it is small."""
    phi, u = sol.sol(np.log(a))[0], sol.sol(np.log(a))[1]
    rho_phi = u * u / 2.0 + lam * phi**4 / 4.0
    rho_phys = (p88.C_M / a**3) * (1.0 - g * phi)
    return rho_phi / (rho_phys + rho_phi)


# ---------------------------------------------------------------------------
# THE P82 SIDE, evaluated at MATCHED a rather than matched t.
# ---------------------------------------------------------------------------


def f_p82_at_a(g, lam, k, a):
    """P82's OWN growth_rate, at the t where P76's run reaches this a.

    # WHY matched a and not P82's own matched t: P76 built t_of_a precisely
    # because two runs with different couplings are at DIFFERENT a at the same
    # t, so comparing at equal t imports a background artifact into what is
    # supposed to be a perturbation comparison. P82 reported at equal t. If the
    # reconstruction were compared against that, a convention difference would
    # be indistinguishable from an implementation disagreement -- the exact
    # species of error FINDING_P78's A3 made. Part D measures how large that
    # convention difference actually is.
    """
    s = p76.run(g, lam, k, T_END)
    t = p76.t_of_a(s, a, 1.0, T_END)
    if t is None:
        return None
    return p82.growth_rate(s, g, lam, t)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P89 -- f through P88's independent implementation")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    a_max = max(A_PROBE)
    sols = {(g, k): solve_recon(g, LAM, k, a_max) for g in (1.0, 0.0) for k in KS}
    for (g, k), s in sols.items():
        if not s.success:
            print(f"  integration failed at g={g}, k={k} -- BLOCKED-INFRASTRUCTURE.")
            return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("L1 -- EXTERNAL lock mass, with P82's trap left in place")
    print("-" * 78)
    print("  In matter domination delta ~ a so f = 1. But our background is NOT")
    print("  pure matter domination -- the scalar carries kinetic and potential")
    print("  energy that feed H -- so an f below 1 could be CORRECT PHYSICS and")
    print("  would look identical to a broken pipeline. Omega_phi is printed")
    print("  beside every value and the assertion is made only where it is small.")
    print(f"\n    {'a':<12}{'Omega_phi':<16}{'f (g_hat=0)':<20}{'f - 1'}")
    worst_l1 = 0.0
    for a in A_PROBE:
        s = sols[(0.0, KS[0])]
        om = omega_phi_recon(s, a, 0.0, LAM)
        fv = f_recon(s, a, 0.0, LAM)
        if om < 1e-3:
            worst_l1 = max(worst_l1, abs(fv - 1.0))
        print(f"    {a:<12.4g}{om:<16.3e}{fv:<20.12f}{fv - 1:+.3e}")
    L1 = worst_l1 < 1e-3
    print(
        f"\n    worst |f-1| where Omega_phi < 1e-3: {worst_l1:.3e}  =>  L1 {'PASSES' if L1 else 'FAILS'}"
    )
    if not L1:
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("L2 -- NEGATIVE CONTROL on the QUANTITY: the raw Delta_m")
    print("-" * 78)
    print("  Delta_m = delta * rho_phys with rho_phys = (C/a^3)(1 - g*phibar), so")
    print("  EXACTLY  f_raw - f = -3 + d ln(1 - g*phibar) / d ln a.  The second")
    print("  term vanishes identically at g_hat=0 and is live at g_hat=1.")
    print()
    print("  P82 ran this control at g_hat=0 ONLY, which is why it reported")
    print("  exactly 3.000000 -- correct there, but the coupling factor was never")
    print("  exercised. The first version of THIS control inherited that target,")
    print("  applied it at g_hat=1 where it does not hold, and failed at 5.1e-03.")
    print("  The reconstruction was right and the control was wrong; the offsets")
    print("  match the second term to 1.8e-11.")
    print()
    print("  Two separate things the original conflated, now scored separately:")
    print("    L2a DISCRIMINATION -- the control's actual job. The wrong quantity")
    print("        must land far enough from f that L1 would have caught it.")
    print("    L2b IDENTITY -- consistency of rho_phys including the coupling")
    print("        factor. Sharper than P82's: the g_hat=1 row can fail.")
    print(
        f"\n    {'g_hat':<8}{'a':<10}{'f_raw - f':<19}{'-3 + dln(1-g phi)':<21}"
        f"{'deviation':<13}{'|separation|'}"
    )
    worst_id = 0.0
    min_sep = float("inf")
    for gv in (0.0, 1.0):
        sv = sols[(gv, 10.0)]
        for a in A_PROBE:
            fc = f_recon(sv, a, gv, LAM)
            fr = f_raw_recon(sv, a, gv, LAM)
            got = fr - fc
            want = -3.0 + dln_coupling_factor(sv, a, gv)
            worst_id = max(worst_id, abs(got - want))
            min_sep = min(min_sep, abs(got))
            print(
                f"    {gv:<8g}{a:<10.4g}{got:<19.12f}{want:<21.12f}"
                f"{got - want:<+13.3e}{abs(got):.4f}"
            )
    L2a = min_sep > 2.0
    L2b = worst_id < 1e-6
    print(f"\n    L2a smallest separation {min_sep:.4f} > 2  =>  {'PASSES' if L2a else 'FAILS'}")
    print(
        f"    L2b worst identity deviation {worst_id:.3e} < 1e-6  =>  {'PASSES' if L2b else 'FAILS'}"
    )
    if not (L2a and L2b):
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- reconstruction against P82, at MATCHED a")
    print("-" * 78)
    print("  f is scored on df := f(g_hat=1) - f(g_hat=0), NOT on f. About 96 %")
    print("  of f is the matter-domination mode both codes reproduce trivially;")
    print("  a comparison on f would be dominated by the part that cannot fail.")

    scored = {}
    for k in KS:
        print(f"\n  k = {k:g}")
        print(f"    {'a':<10}{'df recon':<18}{'df P82':<18}{'rel(df)':<12}{'rel(f) for scale'}")
        for a in A_PROBE:
            fr1 = f_recon(sols[(1.0, k)], a, 1.0, LAM)
            fr0 = f_recon(sols[(0.0, k)], a, 0.0, LAM)
            fp1 = f_p82_at_a(1.0, LAM, k, a)
            fp0 = f_p82_at_a(0.0, LAM, k, a)
            if fp1 is None or fp0 is None:
                print(f"    {a:<10.4g}{'a not reachable -- not measured':<48}")
                scored[(k, a)] = None
                continue
            dr, dp = fr1 - fr0, fp1 - fp0
            rel_df = abs(dr / dp - 1.0)
            rel_f = abs(fr1 / fp1 - 1.0)
            scored[(k, a)] = rel_df
            print(f"    {a:<10.4g}{dr:<18.12f}{dp:<18.12f}{rel_df:<12.3e}{rel_f:.3e}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("L3 -- NEGATIVE CONTROL on the COMPARISON")
    print("-" * 78)
    print("  The Euler exchange term's sign is flipped in the RECONSTRUCTION")
    print("  only. If the agreement survives a deliberate bug it means nothing.")
    k, a = 10.0, 4e5
    b1 = solve_recon(1.0, LAM, k, a_max, sign_euler=-1.0)
    b0 = solve_recon(0.0, LAM, k, a_max, sign_euler=-1.0)
    db = f_recon(b1, a, 1.0, LAM) - f_recon(b0, a, 0.0, LAM)
    dp = f_p82_at_a(1.0, LAM, k, a) - f_p82_at_a(0.0, LAM, k, a)
    rel_bad = abs(db / dp - 1.0)
    L3 = rel_bad > 1e-3
    print(f"\n    {'k':<7}{'df corrupted':<20}{'df P82':<20}{'relative diff'}")
    print(f"    {k:<7g}{db:<20.12f}{dp:<20.12f}{rel_bad:.3e}")
    print(f"\n    L3 {'PASSES' if L3 else 'FAILS'} -- the comparison discriminates.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- how much does the matched-t convention actually move df?")
    print("-" * 78)
    print("  P82 reported df at equal t. Everything above is at equal a. This is")
    print("  a measurement of the CONVENTION difference, not a defect claim --")
    print("  it exists so that any future quote of df has to say which one it is.")
    print(f"\n    {'k':<7}{'df @ matched a':<20}{'df @ matched t':<20}{'relative'}")
    for k in KS:
        s1, s0 = p76.run(1.0, LAM, k, T_END), p76.run(0.0, LAM, k, T_END)
        t_star = 8e7
        df_t = p82.growth_rate(s1, 1.0, LAM, t_star) - p82.growth_rate(s0, 0.0, LAM, t_star)
        a_star = s0.sol(t_star)[0]
        fa1, fa0 = f_p82_at_a(1.0, LAM, k, a_star), f_p82_at_a(0.0, LAM, k, a_star)
        df_a = fa1 - fa0
        print(f"    {k:<7g}{df_a:<20.12f}{df_t:<20.12f}{abs(df_t / df_a - 1.0):.3e}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    vals = [v for v in scored.values() if v is not None]
    if not vals or len(vals) < len(scored):
        print("  -> NOT MEASURABLE at one or more points. Infrastructure outcome,")
        print("     NOT evidence about the claim.")
    elif not L3:
        print("  -> INVALID. The negative control did not discriminate, so the")
        print("     agreement in Part B carries no information.")
    elif max(vals) < 1e-4:
        print(f"  -> F-CONFIRMED. Worst relative difference on df {max(vals):.3e} < 1e-4.")
        print("     P88's registered prediction SURVIVES its first real test: the")
        print("     agreement it demonstrated was not specific to eps(k).")
        print()
        print("     Perelman condition 5 now extends to f, at the SAME rung --")
        print("     'independently-written code' -- and no higher.")
    elif max(vals) < 1e-2:
        print(f"  -> F-MARGINAL. Worst relative difference on df {max(vals):.3e}.")
        print("     f survives but the difference must be NAMED. Note that TWO")
        print("     things differ from P82 here -- solver and difference scheme --")
        print("     so isolating which one carries it is a separate step.")
    else:
        print(f"  -> F-DISCREPANT. Worst relative difference on df {max(vals):.3e}.")
        print("     P88's agreement was SPECIFIC TO eps(k). The shared solver is")
        print("     NOT verified and the campaign's use of f is in doubt.")

    print("\n  NOT ESTABLISHED:")
    print("   * anything above the 'independently-written code' rung. Same person")
    print("     wrote both; different model, blind replication and new experiment")
    print("     all remain absent.")
    print("   * that the shared EQUATIONS are right. A reconstruction tests the")
    print("     implementation, never the specification.")
    print("   * mu_tot == 1, the viability boundary, the scaling group -- untouched.")
    print("   * anything observational. NO_BRIDGE_FITTING untouched. Gate 1 holds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
