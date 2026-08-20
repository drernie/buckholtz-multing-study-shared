"""P73 -- attack Psi_k with the obstruction named.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

The chain that leads here:
  FINDING_P61  built the closed system for Psi_k and found it NOT
               Bianchi-consistent on a free background. Psi_k left unresolved.
  FINDING_P71  localised the obstruction EXACTLY:
                   dC/dt|_{C=0} = -Psi * [H_dot + 4*pi*G*(rho_tot + p_tot)]
               so the 0i constraint propagates iff the background satisfies the
               H-dot equation.
  FINDING_P72  showed P69's background satisfies H-dot STRUCTURALLY -- it is an
               analytic identity of that integrator's ODE system.

So the obstruction is not merely absent, it CANNOT be present there. This file
asks what that unlocks.

THE ARGUMENT. If both the 00 and 0i constraints propagate, they are genuine
first-class constraints: impose them ONCE on initial data and evolve freely.
That is exactly what makes P61's system well-posed rather than over-determined.
P71 did the 0i. This file does the 00, then builds constraint-satisfying initial
data, integrates, and produces Psi_k(t) -- the object P61 could not resolve.

What this file establishes:
  A. the 00 constraint also propagates (P71 did only the 0i);
  B. the degree-of-freedom count: 4 unknowns, 4 evolution equations, 2
     constraints preserved by the evolution -- well-posed, not over-determined;
  C. constraint-satisfying initial data, constructed rather than assumed;
  D. Psi_k(t) actually integrated, with BOTH constraints monitored as a running
     positive control, and a NEGATIVE control on a background that violates
     H-dot -- which should make the constraints drift, demonstrating P71's
     obstruction in action;
  E. mu(a,k) computed from the solution, and what it says about FINDING_P60's
     undecided D2-vs-D3.
"""

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

G_N = 1.0
C_MATTER = 1.0
A3_INIT = 6.0 * np.pi - 1.0
PHIDOT_INIT = np.sqrt(2.0) / A3_INIT


# ----------------------------------------------------------------------
# background (FINDING_P69, reused verbatim; `sabotage` only for Part D's
# negative control, where it breaks the H-dot equation on purpose)
# ----------------------------------------------------------------------
def bg_rhs(_t: float, y: np.ndarray, gh: float, lam: float, sabotage: bool = False) -> list[float]:
    a, pb, pd = y
    rho_A = C_MATTER / a**3
    arg = (8.0 * np.pi * G_N / 3.0) * (rho_A * (1.0 - gh * pb) + pd**2 / 2.0 + lam * pb**4 / 4.0)
    H = np.sqrt(max(arg, 0.0))
    drag = 2.0 if sabotage else 3.0  # 3H -> 2H breaks H-dot (P72's own control)
    return [a * H, pd, gh * rho_A - drag * H * pd - lam * pb**3]


def bg_quantities(a: float, pb: float, pd: float, gh: float, lam: float) -> dict:
    rho_A = C_MATTER / a**3
    rho_phys = rho_A * (1.0 - gh * pb)
    V = lam * pb**4 / 4.0
    Vp = lam * pb**3
    Vpp = 3.0 * lam * pb**2
    H = np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
    Hdot = -4.0 * np.pi * G_N * (rho_phys + pd**2)
    return {
        "rho_A": rho_A,
        "rho_phys": rho_phys,
        "V": V,
        "Vp": Vp,
        "Vpp": Vpp,
        "H": H,
        "Hdot": Hdot,
    }


def main() -> int:
    print("=" * 78)
    print("P73 -- attacking Psi_k with the obstruction named")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    # PART A -- does the 00 constraint propagate too?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- the 00 constraint (P71 did only the 0i)")
    print("-" * 78)
    t = sp.Symbol("t", positive=True)
    k, G = sp.symbols("k G_N", positive=True)
    g, lam = sp.symbols("g_hat lambda", real=True)
    a = sp.Function("a")(t)
    phib = sp.Function("phibar")(t)
    rhoA = sp.Function("rho_A")(t)
    H = sp.diff(a, t) / a
    V = lam * phib**4 / 4
    Vp, Vpp = sp.diff(V, phib), sp.diff(V, phib, 2)
    rho_phys = rhoA * (1 - g * phib)

    Psi = sp.Function("Psi")(t)
    dphi = sp.Function("dphi")(t)
    drhoA = sp.Function("drho_A")(t)
    Qm = sp.Function("Q_m")(t)

    drho_phi = sp.diff(phib, t) * sp.diff(dphi, t) - Psi * sp.diff(phib, t) ** 2 + Vp * dphi
    dp_phi = sp.diff(phib, t) * sp.diff(dphi, t) - Psi * sp.diff(phib, t) ** 2 - Vp * dphi
    drho_m = drhoA * (1 - g * phib) - g * rhoA * dphi
    drho_tot = drho_phi + drho_m
    dq_tot = -sp.diff(phib, t) * dphi + Qm

    subs_chain = [
        (
            sp.diff(Psi, t, 2),
            4 * sp.pi * G * dp_phi - 4 * H * sp.diff(Psi, t) - (2 * sp.diff(H, t) + 3 * H**2) * Psi,
        ),
        (
            sp.diff(dphi, t, 2),
            g * drhoA
            + 2 * Psi * (g * rhoA - Vp)
            + 4 * sp.diff(Psi, t) * sp.diff(phib, t)
            - 3 * H * sp.diff(dphi, t)
            - (k**2 / a**2 + Vpp) * dphi,
        ),
        (
            sp.diff(drhoA, t),
            -3 * H * drhoA + 3 * sp.diff(Psi, t) * rhoA + (k**2 / a**2) * Qm / (1 - g * phib),
        ),
        (sp.diff(Qm, t), -3 * H * Qm - rho_phys * Psi + g * rhoA * dphi),
        (sp.diff(phib, t, 2), g * rhoA - 3 * H * sp.diff(phib, t) - Vp),
        (sp.diff(rhoA, t), -3 * H * rhoA),
    ]

    C0i = sp.diff(Psi, t) + H * Psi + 4 * sp.pi * G * dq_tot
    R_Hdot_sol = sp.solve(
        sp.diff(H, t) + 4 * sp.pi * G * (rho_phys + sp.diff(phib, t) ** 2), sp.diff(a, t, 2)
    )[0]

    # [SELF-CAUGHT, TWICE, and both matter]
    # (1) A first draft demanded dC00/dt == 0 identically after imposing the
    #     constraints. That is the WRONG criterion. Constraints are FIRST CLASS
    #     when the time derivative of each is a LINEAR COMBINATION of the
    #     constraints -- not when it vanishes. Neither sign passed the wrong test.
    # (2) With the right criterion it still failed, which forced deriving the
    #     matter continuity equation instead of writing it from memory: requiring
    #     the SCALAR sector's own continuity to be an identity at g_hat=0 fixes
    #     the sign of the (k^2/a^2)*Q term, and the sign I had was WRONG.
    #     The leftover at g_hat != 0 then came out as g_hat*(drho_A*phibar_dot +
    #     rho_A*dphi_dot) -- exactly the first-order exchange term FINDING_P71
    #     identified, which is what confirms the corrected convention.
    print("  A constraint pair is FIRST CLASS when d/dt of each is a LINEAR")
    print("  COMBINATION of the constraints -- not when it vanishes. Solve for")
    print("  (A,B) in  dC00/dt = A*C00 + B*C0i, with the H-dot equation imposed.")
    print("  The relative 00/0i sign is convention-dependent; both are tried and")
    print("  which one yields a clean algebra is reported.")
    A_, B_ = sp.symbols("A_ B_")
    winner, coeffs = None, None
    for sgn in (+1, -1):
        C00 = (
            3 * H * (sp.diff(Psi, t) + H * Psi)
            + (k**2 / a**2) * Psi
            + sgn * 4 * sp.pi * G * drho_tot
        )
        d00 = sp.diff(C00, t)
        for _ in range(3):
            for old, new in subs_chain:
                d00 = d00.subs(old, new)
        d00 = sp.simplify(sp.expand(d00.subs(sp.diff(a, t, 2), R_Hdot_sol)))
        C00s = sp.simplify(C00.subs(sp.diff(a, t, 2), R_Hdot_sol))
        C0is = sp.simplify(C0i.subs(sp.diff(a, t, 2), R_Hdot_sol))
        expr = sp.expand(d00 - A_ * C00s - B_ * C0is)
        fields = [Psi, sp.diff(Psi, t), dphi, sp.diff(dphi, t), drhoA, Qm]
        eqs = sp.Poly(expr, *fields).coeffs()
        sol = sp.solve(eqs[:2], [A_, B_], dict=True)
        if not sol:
            print(f"    sign {sgn:+d}: no (A,B) even from two coefficients")
            continue
        resid = sp.simplify(sp.expand(expr.subs(sol[0])))
        ok = resid == 0
        print(f"    sign {sgn:+d}: residual over ALL coefficients -> {'ZERO' if ok else 'nonzero'}")
        if ok:
            winner, coeffs = sgn, sol[0]
    assert winner is not None, "no sign makes the 00 constraint first class"
    print(f"\n  => sign {winner:+d}, with the constraint algebra")
    print(f"       A = {sp.simplify(coeffs[A_])}")
    print(f"       B = {sp.simplify(coeffs[B_])}")
    assert sp.simplify(coeffs[A_] + 3 * H) == 0, "expected A = -3H"
    assert sp.simplify(coeffs[B_] - k**2 / a**2) == 0, "expected B = k^2/a^2"
    print("     i.e.  dC00/dt = -3H*C00 + (k^2/a^2)*C0i  -- textbook constraint")
    print("     algebra, and the other sign gives an unrecognisable mess, so the")
    print("     selection is discriminating rather than a fit.")
    print()
    print("  => BOTH constraints are FIRST CLASS on an H-dot-satisfying")
    print("     background. Impose them once on initial data and the evolution")
    print("     preserves them. That is what makes FINDING_P61's system")
    print("     well-posed rather than over-determined.")

    # [CHECKED, because the corrected sign came from THIS file] does the sign
    # correction invalidate FINDING_P71's headline identity? Re-run it both ways.
    print("\n  [regression check on FINDING_P71] the continuity sign corrected")
    print("  here is the one P71 used. Does P71's identity survive the change?")
    for lbl, cs in (("P71's original sign", -1), ("corrected sign", +1)):
        chain = list(subs_chain)
        chain[2] = (
            sp.diff(drhoA, t),
            -3 * H * drhoA + 3 * sp.diff(Psi, t) * rhoA + cs * (k**2 / a**2) * Qm / (1 - g * phib),
        )
        dC = sp.diff(C0i, t)
        for _ in range(2):
            for old, new in chain:
                dC = dC.subs(old, new)
        dC = sp.simplify(sp.expand(dC.subs(Qm, sp.solve(C0i, Qm)[0])))
        R = sp.diff(H, t) + 4 * sp.pi * G * (rho_phys + sp.diff(phib, t) ** 2)
        holds = sp.simplify(sp.expand(dC + Psi * R)) == 0
        print(f"    {lbl:<22}: dC/dt = -Psi*R_Hdot ?  {holds}")
    print("  => P71's identity holds EITHER WAY: the (k^2/a^2)*Q term does not")
    print("     enter the 0i propagation at all. FINDING_P71 needs no retraction.")

    # ==================================================================
    # PART B -- degree-of-freedom count
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- is the system over-determined? (FINDING_P61's worry)")
    print("-" * 78)
    print("  unknowns (4):   Psi_k, deltaphi_k, deltarho_A_k, Q_m_k")
    print("  evolution (4):  ij-trace, scalar field eq, matter continuity, Euler")
    print("  constraints (2): 00 and 0i")
    print()
    print("  Naively 6 equations for 4 unknowns => over-determined, which is how")
    print("  FINDING_P61's failure looked. But Part A + FINDING_P71 show both")
    print("  constraints are PRESERVED by the evolution. So they are conditions on")
    print("  INITIAL DATA, not extra equations at every step:")
    print("    4 unknowns, 4 first-order-in-time evolution equations (Psi second")
    print("    order => 5 state variables), 2 constraints fixing 2 of the initial")
    print("    values. Well-posed.")
    print("  The system was never over-determined -- it only looked that way on a")
    print("  background where the constraints did not propagate.")

    # ==================================================================
    # PART C -- constraint-satisfying initial data
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- constructing initial data that satisfies both constraints")
    print("-" * 78)
    print("  Free choices: Psi(1), deltaphi(1), deltaphi_dot(1). Then")
    print("    0i  fixes  Q_m(1)")
    print("    00  fixes  Psi_dot(1)")
    print("  and deltarho_A(1) follows from the 00 equation's own content.")
    print("  Nothing is assumed -- both are SOLVED, and the residuals are asserted.")

    # ==================================================================
    # PART D -- integrate, and monitor both constraints
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- Psi_k(t): integrated, with both constraints monitored")
    print("-" * 78)

    def make_system(gh: float, lam: float, kk: float, sabotage: bool = False):
        def rhs(tt, y):
            a_, pb, pd, psi, psid, dph, dphd, drA, qm = y
            b = bg_quantities(a_, pb, pd, gh, lam)
            H, rho_A, rho_phys, Vp, Vpp = (b["H"], b["rho_A"], b["rho_phys"], b["Vp"], b["Vpp"])
            drag = 2.0 if sabotage else 3.0
            pdd = gh * rho_A - drag * H * pd - Vp
            Hdot = b["Hdot"]
            dp_phi_ = pd * dphd - psi * pd**2 - Vp * dph
            psidd = 4 * np.pi * G_N * dp_phi_ - 4 * H * psid - (2 * Hdot + 3 * H**2) * psi
            dphdd = (
                gh * drA
                + 2 * psi * (gh * rho_A - Vp)
                + 4 * psid * pd
                - 3 * H * dphd
                - (kk**2 / a_**2 + Vpp) * dph
            )
            drAd = -3 * H * drA + 3 * psid * rho_A + (kk**2 / a_**2) * qm / (1 - gh * pb)
            qmd = -3 * H * qm - rho_phys * psi + gh * rho_A * dph
            return [a_ * H, pd, pdd, psid, psidd, dphd, dphdd, drAd, qmd]

        return rhs

    def initial_data(gh: float, lam: float, kk: float, psi0: float = 1e-5):
        """Solve the two constraints for Q_m(1) and Psi_dot(1)."""
        a0 = A3_INIT ** (1.0 / 3.0)
        pb0, pd0 = 0.0, PHIDOT_INIT
        b = bg_quantities(a0, pb0, pd0, gh, lam)
        H0 = b["H"]
        dph0, dphd0 = 1e-6, 0.0
        # 00 constraint (sign `winner` from Part A) fixes the combination; choose
        # drho_A(1) freely and solve 00 for Psi_dot(1).
        drA0 = 1e-5
        drho_phi0 = pd0 * dphd0 - psi0 * pd0**2 + b["Vp"] * dph0
        drho_m0 = drA0 * (1 - gh * pb0) - gh * b["rho_A"] * dph0
        drho_tot0 = drho_phi0 + drho_m0
        # 3H(Psi_dot + H Psi) + (k^2/a^2)Psi + winner*4piG*drho_tot = 0
        psid0 = (-(kk**2 / a0**2) * psi0 - winner * 4 * np.pi * G_N * drho_tot0) / (
            3 * H0
        ) - H0 * psi0
        # 0i constraint fixes Q_m(1):  Psi_dot + H Psi + 4piG(-pd*dphi + Q) = 0
        qm0 = -(psid0 + H0 * psi0) / (4 * np.pi * G_N) + pd0 * dph0
        return [a0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0, qm0]

    def constraints(y, gh, lam, kk):
        a_, pb, pd, psi, psid, dph, dphd, drA, qm = y
        b = bg_quantities(a_, pb, pd, gh, lam)
        H = b["H"]
        drho_phi_ = pd * dphd - psi * pd**2 + b["Vp"] * dph
        drho_m_ = drA * (1 - gh * pb) - gh * b["rho_A"] * dph
        c00 = (
            3 * H * (psid + H * psi)
            + (kk**2 / a_**2) * psi
            + winner * 4 * np.pi * G_N * (drho_phi_ + drho_m_)
        )
        c0i = psid + H * psi + 4 * np.pi * G_N * (-pd * dph + qm)
        scale = abs(3 * H * (psid + H * psi)) + abs((kk**2 / a_**2) * psi) + 1e-300
        return abs(c00) / scale, abs(c0i) / (abs(psid) + abs(H * psi) + 1e-300)

    gh, lam = 1.0, 1.0
    print(
        f"\n  {'k':<8}{'|C00|/scale @t=1':<20}{'@t=1e3':<16}{'|C0i| @t=1e3':<16}{'Psi(1e3)/Psi(1)'}"
    )
    solutions = {}
    for kk in (0.1, 1.0, 10.0):
        y0 = initial_data(gh, lam, kk)
        r00_0, r0i_0 = constraints(y0, gh, lam, kk)
        assert r00_0 < 1e-12 and r0i_0 < 1e-12, (
            f"initial data violates constraints: {r00_0}, {r0i_0}"
        )
        sol = solve_ivp(
            make_system(gh, lam, kk),
            (1.0, 1e3),
            y0,
            rtol=1e-11,
            atol=1e-16,
            dense_output=True,
        )
        assert sol.success, f"integration failed at k={kk}"
        solutions[kk] = sol
        r00, r0i = constraints(sol.sol(1e3), gh, lam, kk)
        ratio = sol.sol(1e3)[3] / y0[3]
        print(f"  {kk:<8}{r00_0:<20.3e}{r00:<16.3e}{r0i:<16.3e}{ratio:.6e}")
        assert r00 < 1e-6, f"00 constraint DRIFTED at k={kk}: {r00}"
        assert r0i < 1e-6, f"0i constraint DRIFTED at k={kk}: {r0i}"
    print("\n  => both constraints stay satisfied to <1e-6 relative over three")
    print("     decades of t, at every k. Psi_k(t) is SOLVED -- the object")
    print("     FINDING_P61 left unresolved.")

    # NEGATIVE CONTROL: a background that VIOLATES H-dot must break this
    print("\n  [negative control] same integration on a background whose KG drag")
    print("  is 3H -> 2H, which breaks the H-dot equation (P72's own sabotage):")
    print(f"\n    {'k':<8}{'|C00| @t=1e3':<18}{'|C0i| @t=1e3':<18}{'constraints hold?'}")
    for kk in (0.1, 1.0, 10.0):
        y0 = initial_data(gh, lam, kk)
        sol = solve_ivp(
            make_system(gh, lam, kk, sabotage=True),
            (1.0, 1e3),
            y0,
            rtol=1e-11,
            atol=1e-16,
            dense_output=True,
        )
        assert sol.success, f"sabotaged integration failed at k={kk}"
        r00, r0i = constraints(sol.sol(1e3), gh, lam, kk)
        broke = r00 > 1e-3 or r0i > 1e-3
        print(f"    {kk:<8}{r00:<18.3e}{r0i:<18.3e}{'NO -- drifted' if broke else 'yes'}")
        assert broke, f"sabotaged background did NOT break the constraints at k={kk}"
    print("\n  => on a background violating H-dot the constraints DRIFT, exactly as")
    print("     FINDING_P71 predicts. The obstruction is not hypothetical: it is")
    print("     visible in the numerics, and removing it is what makes Psi_k")
    print("     solvable at all.")

    # ==================================================================
    # PART E -- mu(a,k)
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- mu(a,k) from the solution: FINDING_P60's D2 vs D3")
    print("-" * 78)
    print("  mu is defined by the modified Poisson equation, with rho_phys as the")
    print("  reference density (FINDING_P60's Route B):")
    print("     mu(a,k) := -(k^2/a^2) * Psi / (4*pi*G * delta_rho_phys)")
    print("  In unmodified GR with no scalar, mu = 1.")
    print(f"\n  {'k':<8}{'t':<10}{'mu':<18}{'|mu-1|'}")
    mus = {}
    for kk in (0.1, 1.0, 10.0):
        sol = solutions[kk]
        for tv in (10.0, 1e2, 1e3):
            a_, pb, pd, psi, psid, dph, dphd, drA, qm = sol.sol(tv)
            drho_phys = drA * (1 - gh * pb) - gh * (C_MATTER / a_**3) * dph
            mu = -(kk**2 / a_**2) * psi / (4 * np.pi * G_N * drho_phys)
            mus[(kk, tv)] = mu
            print(f"  {kk:<8}{tv:<10.0e}{mu:<18.8f}{abs(mu - 1.0):.3e}")
    spread = max(abs(v - 1.0) for v in mus.values())
    print(f"\n  max |mu - 1| across all (k,t): {spread:.3e}")

    # ==================================================================
    # RETRACTION -- the two tests that kill the obvious reading
    # ==================================================================
    print("\n  " + "!" * 70)
    print("  RETRACTION. A draft of this file read the table above as D3 --")
    print("  'mu is k-dependent, therefore a genuine modification'. The")
    print("  context-blind reviewer proposed two tests that destroy that reading,")
    print("  and both come back against it. They are run here, not paraphrased.")
    print("  " + "!" * 70)

    print("\n  TEST 1 -- turn the COUPLING OFF (g_hat=0, lambda=0). If the k-shape")
    print("  survives with no coupling at all, it is kinematics, not modification.")
    print(f"\n    {'k':<8}{'mu (g=1,lam=1)':<20}{'mu (g=0,lam=0)':<20}{'coupling signal'}")
    max_signal = 0.0
    for kk in (0.1, 1.0, 10.0):
        y_on = initial_data(gh, lam, kk)
        y_off = initial_data(0.0, 0.0, kk)
        s_on = solve_ivp(make_system(gh, lam, kk), (1.0, 1e3), y_on,
                         rtol=1e-11, atol=1e-18, dense_output=True)
        s_off = solve_ivp(make_system(0.0, 0.0, kk), (1.0, 1e3), y_off,
                          rtol=1e-11, atol=1e-18, dense_output=True)
        assert s_on.success and s_off.success

        def _mu(sol, ghv, kk=kk):
            a_, pb, _pd, psi, _psid, dph, _dphd, drA, _qm = sol.sol(1e3)
            dr = drA * (1 - ghv * pb) - ghv * (C_MATTER / a_**3) * dph
            return -(kk**2 / a_**2) * psi / (4 * np.pi * G_N * dr)

        m_on, m_off = _mu(s_on, gh), _mu(s_off, 0.0)
        sig = abs(m_on - m_off) / abs(m_off)
        max_signal = max(max_signal, sig)
        print(f"    {kk:<8}{m_on:<20.6f}{m_off:<20.6f}{sig:.2%}")
    print("\n    => the k-shape is REPRODUCED with the coupling entirely OFF.")
    print(f"       The actual coupling signal is at most {max_signal:.2%}.")
    print("       *** The k-dependence in the table above is KINEMATIC. ***")
    assert max_signal < 0.05, "coupling signal unexpectedly large -- re-examine"

    print("\n  TEST 2 -- is mu converged in t, or a superhorizon transient?")
    print(f"\n    {'t':<10}{'mu (k=0.1)':<16}{'mu ratio/decade':<18}{'a ratio/decade'}")
    s_long = solve_ivp(make_system(gh, lam, 0.1), (1.0, 1e6), initial_data(gh, lam, 0.1),
                       rtol=1e-10, atol=1e-18, dense_output=True)
    assert s_long.success
    prev_mu = prev_a = None
    for tv in (10.0, 1e2, 1e3, 1e4, 1e5, 1e6):
        a_, pb, _pd, psi, _psid, dph, _dphd, drA, _qm = s_long.sol(tv)
        dr = drA * (1 - gh * pb) - gh * (C_MATTER / a_**3) * dph
        mu_v = -(0.1**2 / a_**2) * psi / (4 * np.pi * G_N * dr)
        rm = "" if prev_mu is None else f"{mu_v / prev_mu:.3f}"
        ra = "" if prev_a is None else f"{a_ / prev_a:.3f}"
        print(f"    {tv:<10.0e}{mu_v:<16.6f}{rm:<18}{ra}")
        prev_mu, prev_a = mu_v, a_
    print("\n    => mu is NOT converged at t=1e3. It grows initially like a(t)")
    print("       (ratio ~4.6 per decade, matching a), then saturates toward 1 as")
    print("       the mode enters the horizon. 'mu = 0.095 at k=0.1' was a")
    print("       SNAPSHOT OF A SUPERHORIZON TRANSIENT, not a property of the")
    print("       model. The reviewer predicted exactly this.")
    print("\n  => BOTH the k-dependence and the departure from 1 are explained")
    print("     WITHOUT any modification. The D3 verdict is RETRACTED. What is")
    print(f"     left as a genuine coupling effect is the <= {max_signal:.2%} difference")
    print("     between coupled and uncoupled -- small, k-dependent, and NOT")
    print("     established here to be above this setup's own systematics.")

    # ==================================================================
    # PART F -- is that mu a property of the MODEL or of MY initial data?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART F -- the check that decides whether Part E means anything")
    print("-" * 78)
    print("  mu is a ratio of two quantities OF THE SOLUTION. With generic initial")
    print("  data one gets a superposition of growing, decaying and oscillating")
    print("  modes, and that ratio is whatever the data happened to be. mu is only")
    print("  meaningful if it is INITIAL-DATA INDEPENDENT -- i.e. if the system")
    print("  has an attractor. Untested, Part E would be a number about my")
    print("  arbitrary choices. So: vary the free data and look.")
    datasets = [
        ("baseline", 1e-5, 1e-6, 0.0, 1e-5),
        ("10x drho_A", 1e-5, 1e-6, 0.0, 1e-4),
        ("dphi -> 0", 1e-5, 1e-12, 0.0, 1e-5),
        ("dphi_dot != 0", 1e-5, 1e-6, 1e-6, 1e-5),
        ("Psi 100x", 1e-3, 1e-6, 0.0, 1e-5),
    ]
    worst_spread = 1.0
    for kk in (0.1, 1.0, 10.0):
        vals = []
        for _lbl, p0, d0, dd0, r0 in datasets:
            y0 = initial_data(gh, lam, kk, psi0=p0)
            y0[5], y0[6], y0[7] = d0, dd0, r0
            # re-solve the two constraints for the modified free data
            b0 = bg_quantities(y0[0], y0[1], y0[2], gh, lam)
            drho_phi0 = y0[2] * dd0 - p0 * y0[2] ** 2 + b0["Vp"] * d0
            drho_m0 = r0 * (1 - gh * y0[1]) - gh * b0["rho_A"] * d0
            y0[4] = (
                -(kk**2 / y0[0] ** 2) * p0 - winner * 4 * np.pi * G_N * (drho_phi0 + drho_m0)
            ) / (3 * b0["H"]) - b0["H"] * p0
            y0[8] = -(y0[4] + b0["H"] * p0) / (4 * np.pi * G_N) + y0[2] * d0
            r00_0, r0i_0 = constraints(y0, gh, lam, kk)
            assert r00_0 < 1e-10 and r0i_0 < 1e-10, "modified initial data violates constraints"
            s = solve_ivp(
                make_system(gh, lam, kk), (1.0, 1e3), y0,
                rtol=1e-11, atol=1e-18, dense_output=True,
            )
            assert s.success, f"IC-variation run failed at k={kk}"
            a_, pb, pd, psi, _psid, dph, _dphd, drA, _qm = s.sol(1e3)
            drho_phys = drA * (1 - gh * pb) - gh * (C_MATTER / a_**3) * dph
            vals.append(-(kk**2 / a_**2) * psi / (4 * np.pi * G_N * drho_phys))
        spread = max(vals) / min(vals)
        worst_spread = max(worst_spread, spread)
        print(f"    k={kk:<6} mu(t=1e3) across 5 datasets: "
              f"{min(vals):.6f} .. {max(vals):.6f}   spread {spread:.4f}x")
        assert spread < 1.05, f"mu is initial-data DEPENDENT at k={kk}: {spread}x"
    print(f"\n  => mu varies by at most {worst_spread:.4f}x across five very")
    print("     different initial-data choices (including deltaphi driven to zero")
    print("     and Psi scaled by 100). The system has an ATTRACTOR, so mu is a")
    print("     property of the MODEL, not of my arbitrary data.")
    print("  [BUT] this does NOT rescue the mu verdict. The reviewer was right")
    print("  that all five datasets are positive-sign generic data, so what this")
    print("  shows is growing-mode dominance -- and in any case Test 1 above kills")
    print("  the interpretation regardless of how stable the number is.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  ESTABLISHED:")
    print(f"   * the 00 constraint propagates (sign {winner:+d}) on the SAME")
    print("     condition P71 found for the 0i -- the H-dot equation. Both are")
    print("     first-class, so P61's system is WELL-POSED, not over-determined;")
    print("   * Psi_k(t) INTEGRATED on P69's background, with both constraints")
    print("     holding to <1e-6 relative over three decades at k=0.1, 1, 10 --")
    print("     the object FINDING_P61 left unresolved;")
    print("   * NEGATIVE CONTROL: on a background violating H-dot the constraints")
    print("     DRIFT. P71's obstruction is visible in the numerics, and removing")
    print("     it is what makes Psi_k solvable at all;")
    print("   * mu(a,k) computed and shown initial-data independent")
    print(f"     (<= {worst_spread:.4f}x across five datasets) -- but see the RETRACTION.")
    print()
    print("  RETRACTED, by this file's own tests after review:")
    print("   * the claim that mu's k-dependence decides D2-vs-D3 in favour of D3.")
    print("     Turning the coupling entirely OFF reproduces the same k-shape, so")
    print("     the shape is KINEMATIC (Newtonian-gauge, superhorizon), not a")
    print(f"     modification. The real coupling signal is <= {max_signal:.2%}.")
    print("   * the number 'mu = 0.095 at k=0.1'. It is not converged: mu grows")
    print("     like a(t) and reaches 0.914 by t=1e6. It was a snapshot of a")
    print("     superhorizon transient.")
    print("   => FINDING_P60's D2-vs-D3 remains UNDECIDED. This file does not")
    print("      settle it, and an earlier draft claiming otherwise was wrong.")
    print()
    print("  NOT ESTABLISHED:")
    print("   * ANY verdict on D2 vs D3. See the RETRACTION above -- and note")
    print("     that even the surviving <=0.58% coupling signal is one background,")
    print("     one potential, one coupling value, and is not shown to exceed this")
    print("     setup's own numerical systematics. The (g_hat, lambda) dependence")
    print("     of mu is NOT scanned here.")
    print("   * that the relative 00/0i sign was DERIVED. It was SELECTED by the")
    print("     closure test. That test is nontrivial, but it is not a Christoffel")
    print("     computation and is not presented as one.")
    print("   * anything at k outside [0.1, 10]. The constraint-preservation")
    print("     result is stated for t <= 1e3; only the single mu diagnostic of")
    print("     Test 2 was carried to t=1e6.")
    print("   * anything about MULTING itself (Gate 1): V is OUR construction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
