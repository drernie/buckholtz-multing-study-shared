"""P90 -- mu_tot and mu_m through P88's independent implementation.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

THE PREDICTION THIS TESTS IS PARTLY MY OWN MIS-SPECIFICATION, AND THAT IS SAID
FIRST RATHER THAN QUIETLY REPAIRED. FINDING_P89 registered:

    "mu_tot, being an algebraic identity among background and perturbation
     variables at a single point, should reproduce at ROUNDTRIP PRECISION
     (1e-12 or better) with no step-refinement ladder needed at all"

That was written before looking at mu_tot's definition, and half of it is
VACUOUS. mu_tot is

    mu_tot = -(k^2/a^2) * psi / (4 pi G (Delta_m + Delta_phi))

which is the perturbed Einstein (00) constraint rearranged. It is not a number
that a code computes and might get wrong -- it is 1 BY CONSTRUCTION in any code
that solves the constraint, P76's and P88's alike. So "the two implementations
agree on mu_tot to 1e-12" would measure only that both satisfy a constraint they
were each built to satisfy. Reporting that as cross-implementation agreement
would be the ninth instance of this campaign's recurring failure: the gate
measuring something other than what the claim asserts.

WHAT IS ACTUALLY TESTABLE, and what this file does instead:

  (1) THE IDENTITY IS A PROPERTY OF THE EQUATIONS, NOT OF P76'S DISCRETIZATION.
      P88's solver imposes the BACKGROUND Friedmann constraint algebraically but
      EVOLVES the perturbations -- nothing in it forces the perturbed (00)
      constraint to stay satisfied. So |mu_tot - 1| along an independently
      discretized solution is a genuine constraint-preservation measurement
      against an EXTERNAL target (the Einstein equations), owing nothing to P76.
      FINDING_P74 measured 9.07e-11 for its own solver; the threshold here is
      its own stated 1e-8.

  (2) mu_m IS THE NON-TRIVIAL NUMBER AND IS WHERE A REAL COMPARISON LIVES.
      mu_m = -(k^2/a^2) * psi / (4 pi G Delta_m) uses the MATTER comoving
      density alone, so it is not pinned to anything and genuinely differs from
      1. That is the reconstructable claim, and it is compared against P74's own
      mu_of at MATCHED a (P89's lesson: equal-t comparison imports a background
      artifact).

  (3) THE HALF OF THE PREDICTION THAT SURVIVES is "no step-refinement ladder
      needed". Unlike eps and f, mu involves NO differencing at all -- it is
      pointwise in the state vector. The only knob is solver rtol. That is
      checked rather than asserted.

THE NEGATIVE CONTROLS ARE THE POINT OF THIS FILE, because FINDING_P74 itself
documented that its lock mass was BLIND to a fabricated term: adding
+7*g_hat*rho_A*dphi to the matter branch changed nothing, and P74 honestly
WEAKENED its own Part B over it. The reason is now visible: P74 evaluated that
control at g_hat=0, where the term is identically zero. That is the SECOND
control in this campaign found to have been run at g_hat=0 where the interesting
term vanishes -- P89 found the same shape in P82's negative control yesterday.
It is a pattern, not a coincidence, and it gets tested here rather than noted.

  N1  P74's own fabricated term, evaluated at BOTH couplings.
      PRE-REGISTERED, both directions, each able to fail:
        at g_hat=0 the residual must be IDENTICAL to the clean one (reproducing
          P74's documented blindness -- if it differs, P74's G2 was wrong);
        at g_hat=1 the residual must be LARGE (the repair -- if it is not, the
          identity really cannot see this term and the blindness is intrinsic
          rather than an artifact of where P74 looked).

  N2  WHAT THE IDENTITY CANNOT SEE, BY CONSTRUCTION. A term added to Delta_m and
      SUBTRACTED from Delta_phi cancels in the total. mu_tot must be blind to it
      and mu_m must detect it. This is characterisation, not a pass/fail dressed
      up: it states precisely what a mu_tot check certifies and what it does not.

PRE-REGISTERED OUTCOMES:
  M-VACUOUS     N1 at g_hat=1 does NOT discriminate -> the identity check cannot
                distinguish a correct total from a corrupted one, and NOTHING
                else in this file carries information regardless of its numbers.
                Checked FIRST, before any agreement is reported.
  M-CONFIRMED   identity |mu_tot - 1| < 1e-8 in the reconstruction AND mu_m
                agrees with P74 to < 1e-4 relative.
  M-MARGINAL    identity holds but mu_m agrees only between 1e-4 and 1e-2.
  M-DISCREPANT  identity fails, or mu_m disagrees by more than 1e-2.

WHAT THIS CANNOT DO:
  * Same person wrote both implementations. Different MODEL, blind replication,
    new physical experiment: all still absent. Strong, not Very strong.
  * A reconstruction tests the IMPLEMENTATION, never the SPECIFICATION.
  * Nothing observational. NO_BRIDGE_FITTING untouched. Gate 1 holds.
"""

import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T_END = 1e7
LAM = 1.0
KS = (0.1, 1.0, 10.0)  # P74's own k grid, far wider than P88/P89 used
A_PROBE = (1e3, 1e4, 5e4)


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p88 = _load("P88_independent_reconstruction.py", "p88_for_mu")
p74 = _load("P74_gauge_correct_mu.py", "p74_for_mu")
p76 = _load("P76_growth_observable.py", "p76_for_mu")


# ---------------------------------------------------------------------------
# THE RECONSTRUCTION SIDE. P88's solver; the mu formulae transcribed from the
# specification (they ARE the claim), the code that evaluates them written here.
# ---------------------------------------------------------------------------


def split_recon(sol, a, g, lam):
    """Matter/scalar split of the COMOVING density perturbation Delta = drho - 3H dq."""
    phi, u, psi, _psid, dph, dphd, dra, qm = sol.sol(np.log(a))
    H, _, rho_A, _ = p88._H_and_Hdot(a, phi, u, g, lam)
    Vp = lam * phi**3
    drho_phi = u * dphd - psi * u * u + Vp * dph
    drho_m = dra * (1.0 - g * phi) - g * rho_A * dph
    return {
        "psi": psi,
        "dph": dph,
        "rho_A": rho_A,
        "Delta_m": drho_m - 3.0 * H * qm,
        "Delta_phi": drho_phi - 3.0 * H * (-u * dph),
    }


def mu_recon(sol, a, g, lam, k, total=True, fabricate=0.0, shuffle=0.0):
    """mu with the chosen denominator, plus the two deliberate corruptions.

    # WHY the corruptions live in the SAME function as the clean value rather
    # than in a copy: a copy can drift from the original and then the negative
    # control is testing a different expression than the one it is meant to
    # protect. fabricate replays P74's +7*g*rho_A*dphi; shuffle moves weight
    # from the scalar branch into the matter branch, which CANCELS in the total.
    """
    d = split_recon(sol, a, g, lam)
    bogus = fabricate * 7.0 * g * d["rho_A"] * d["dph"]
    dm = d["Delta_m"] + bogus + shuffle
    dp = d["Delta_phi"] - shuffle
    den = (dm + dp) if total else dm
    return -(k**2 / a**2) * d["psi"] / (4.0 * np.pi * p88.G_N * den)


# ---------------------------------------------------------------------------
# THE P74 SIDE, at matched a.
# ---------------------------------------------------------------------------


def mu_m_p74_at_a(g, lam, k, a):
    s = p74.run(g, lam, k, T_END)
    t = p76.t_of_a(s, a, 1.0, T_END)
    if t is None:
        return None
    return p74.mu_of(s.sol(t), g, lam, k)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P90 -- mu_tot and mu_m through P88's independent implementation")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    a_max = max(A_PROBE)
    sols = {}
    for g in (1.0, 0.0):
        for k in KS:
            sols[(g, k)] = _solve(g, k, a_max)
    for (g, k), s in sols.items():
        if not s.success:
            print(f"  integration failed at g={g}, k={k} -- BLOCKED-INFRASTRUCTURE.")
            return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("N1 -- THE DISCRIMINATION CHECK, RUN FIRST")
    print("-" * 78)
    print("  FINDING_P74 documented that its lock mass was BLIND to a fabricated")
    print("  +7*g_hat*rho_A*dphi term and honestly WEAKENED its own Part B over")
    print("  it. The reason is now visible: it evaluated that control at g_hat=0,")
    print("  where the term is IDENTICALLY ZERO. Both directions are predicted:")
    print("    at g_hat=0 the residual must be UNCHANGED (P74's finding reproduced)")
    print("    at g_hat=1 it must be LARGE (the repair)")
    print(
        f"\n    {'g_hat':<8}{'k':<8}{'clean |mu_tot-1|':<22}{'fabricated |mu_tot-1|':<24}{'ratio'}"
    )
    blind_ok, repair_ratio = True, float("inf")
    for g in (0.0, 1.0):
        for k in KS:
            a = A_PROBE[-1]
            clean = abs(mu_recon(sols[(g, k)], a, g, LAM, k) - 1.0)
            fab = abs(mu_recon(sols[(g, k)], a, g, LAM, k, fabricate=1.0) - 1.0)
            ratio = fab / clean if clean > 0 else float("inf")
            if g == 0.0:
                blind_ok = blind_ok and abs(ratio - 1.0) < 1e-6
            else:
                repair_ratio = min(repair_ratio, ratio)
            print(f"    {g:<8g}{k:<8g}{clean:<22.6e}{fab:<24.6e}{ratio:.6g}")
    N1_blind = blind_ok
    N1_repair = repair_ratio > 1e3
    print(f"\n    g_hat=0 residual unchanged (P74's blindness reproduced): {N1_blind}")
    print(f"    g_hat=1 smallest amplification {repair_ratio:.3g} > 1e3       : {N1_repair}")
    if not N1_repair:
        print("\n    -> M-VACUOUS. The identity check cannot tell a correct total")
        print("       from a corrupted one, so nothing below carries information.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("N2 -- WHAT THE IDENTITY CANNOT SEE, BY CONSTRUCTION")
    print("-" * 78)
    print("  A term added to Delta_m and SUBTRACTED from Delta_phi cancels in the")
    print("  total. mu_tot must be blind to it; mu_m must detect it. This states")
    print("  what a mu_tot check certifies and what it does not.")
    a, g = A_PROBE[-1], 1.0
    print(f"\n    {'k':<8}{'mu_tot shift':<22}{'mu_m shift'}")
    tot_blind, m_sees = True, True
    for k in KS:
        d = split_recon(sols[(g, k)], a, g, LAM)
        eps_shift = 0.1 * abs(d["Delta_m"])
        t0 = mu_recon(sols[(g, k)], a, g, LAM, k)
        t1 = mu_recon(sols[(g, k)], a, g, LAM, k, shuffle=eps_shift)
        m0 = mu_recon(sols[(g, k)], a, g, LAM, k, total=False)
        m1 = mu_recon(sols[(g, k)], a, g, LAM, k, total=False, shuffle=eps_shift)
        rt, rm = abs(t1 / t0 - 1.0), abs(m1 / m0 - 1.0)
        tot_blind = tot_blind and rt < 1e-12
        m_sees = m_sees and rm > 1e-3
        print(f"    {k:<8g}{rt:<22.3e}{rm:.3e}")
    print(f"\n    mu_tot blind to it (expected, by construction) : {tot_blind}")
    print(f"    mu_m detects it (expected)                     : {m_sees}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- the IDENTITY under an independent discretization")
    print("-" * 78)
    print("  P88's solver imposes the BACKGROUND Friedmann constraint but EVOLVES")
    print("  the perturbations; nothing forces the perturbed (00) constraint to")
    print("  stay satisfied. The target 1 is EXTERNAL -- the Einstein equations --")
    print("  and owes nothing to P76. FINDING_P74 got 9.07e-11 for its own solver.")
    print(f"\n    {'k':<8}{'a':<10}{'mu_tot':<24}{'|mu_tot - 1|'}")
    worst_id = 0.0
    for k in KS:
        for a in A_PROBE:
            v = mu_recon(sols[(1.0, k)], a, 1.0, LAM, k)
            worst_id = max(worst_id, abs(v - 1.0))
            print(f"    {k:<8g}{a:<10.4g}{v:<24.15f}{abs(v - 1.0):.4e}")
    IDENT = worst_id < 1e-8
    print(f"\n    worst |mu_tot - 1| = {worst_id:.4e} < 1e-8  =>  {'HOLDS' if IDENT else 'FAILS'}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- mu_m, the NON-TRIVIAL number, against P74 at matched a")
    print("-" * 78)
    print("  mu_tot is pinned to 1 in BOTH codes by construction, so a")
    print("  cross-implementation ratio on it would be vacuous and is not")
    print("  reported as agreement. mu_m is not pinned to anything.")
    print(f"\n    {'k':<8}{'a':<10}{'mu_m recon':<24}{'mu_m P74':<24}{'relative'}")
    rels = {}
    for k in KS:
        for a in A_PROBE:
            mr = mu_recon(sols[(1.0, k)], a, 1.0, LAM, k, total=False)
            mp = mu_m_p74_at_a(1.0, LAM, k, a)
            if mp is None:
                print(f"    {k:<8g}{a:<10.4g}{'a not reachable -- not measured':<48}")
                rels[(k, a)] = None
                continue
            rels[(k, a)] = abs(mr / mp - 1.0)
            print(f"    {k:<8g}{a:<10.4g}{mr:<24.15f}{mp:<24.15f}{rels[(k, a)]:.3e}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- the surviving half of P89's prediction: NO LADDER NEEDED")
    print("-" * 78)
    print("  eps and f both needed a differencing step and both showed a")
    print("  refinement ladder. mu has NO difference operator at all -- it is")
    print("  pointwise in the state vector -- so the only knob is solver rtol,")
    print("  and the agreement should already be at its floor without refining.")
    print(f"\n    {'recon rtol':<14}{'mu_m recon':<24}{'relative vs P74'}")
    k, a = 1.0, A_PROBE[-1]
    mp = mu_m_p74_at_a(1.0, LAM, k, a)
    ladder = []
    for rt in (1e-8, 1e-10, 1e-12):
        s = _solve(1.0, k, a_max, rtol=rt)
        mr = mu_recon(s, a, 1.0, LAM, k, total=False)
        ladder.append(abs(mr / mp - 1.0))
        print(f"    {rt:<14.0e}{mr:<24.15f}{ladder[-1]:.3e}")
    spread = max(ladder) / max(min(ladder), 1e-300)
    print(f"\n    spread across four orders of rtol: {spread:.3g}x")
    print("    (a differencing ladder would move by ~1e4 here; this one should not)")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    vals = [v for v in rels.values() if v is not None]
    if not vals or len(vals) < len(rels):
        print("  -> NOT MEASURABLE at one or more points. Infrastructure outcome,")
        print("     NOT evidence about the claim.")
    elif not IDENT:
        print(f"  -> M-DISCREPANT. The identity fails at {worst_id:.3e} under an")
        print("     independent discretization, so mu_tot == 1 is a property of")
        print("     P76's solver rather than of the equations.")
    elif max(vals) < 1e-4:
        print(f"  -> M-CONFIRMED. Identity {worst_id:.3e} < 1e-8 under an independent")
        print(f"     discretization, and mu_m agrees with P74 to {max(vals):.3e} < 1e-4.")
        print("     Perelman condition 5 now covers eps(k), f, and mu -- all three")
        print("     at the 'independently-written code' rung and no higher.")
    elif max(vals) < 1e-2:
        print(f"  -> M-MARGINAL. Identity holds; mu_m agrees only to {max(vals):.3e}.")
    else:
        print(f"  -> M-DISCREPANT. mu_m disagrees by {max(vals):.3e}.")

    print("\n  WHAT THE IDENTITY DOES NOT CERTIFY (N2, measured not assumed):")
    print("   * any error that cancels between the matter and scalar branches.")
    print("     mu_tot is blind to it BY CONSTRUCTION -- only mu_m sees it.")
    print("\n  NOT ESTABLISHED:")
    print("   * anything above the 'independently-written code' rung.")
    print("   * that the shared EQUATIONS are right.")
    print("   * the viability boundary and the scaling group -- untouched.")
    print("   * anything observational. Gate 1 holds.")
    return 0


def _solve(g, k, a_max, rtol=1e-11):
    from scipy.integrate import solve_ivp

    return solve_ivp(
        p88.rhs_lnA(g, LAM, k),
        (np.log(p88.A_0), np.log(a_max) + 0.05),
        p88.initial_state(g, LAM, k),
        method="DOP853",
        rtol=rtol,
        atol=1e-22,
        dense_output=True,
    )


if __name__ == "__main__":
    raise SystemExit(main())
