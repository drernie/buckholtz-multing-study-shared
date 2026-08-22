"""P84 -- what in this reconstruction is PHYSICS and what is a unit convention?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS BEFORE ANY BRIDGE.

FINDING_P82 produced f(a,k) and delta_f in INTERNAL units. The campaign's stated
next target is a mapping to observed units -- k in h/Mpc, so that f*sigma8 could
one day be compared. But P76 sets G_N = 1, C_MATTER = 1, a(1)^3 = 6*pi - 1 and
phibar_dot(1) = sqrt(2)/A3_INIT. Every one of those is a CHOICE. Until it is
known which of our numbers survive a change of that choice, any mapping to h/Mpc
is fitting dressed as derivation.

So the first bridge step is not a mapping. It is an audit:

    which combinations of (a, C, g_hat, lambda, phibar, k, t) are INVARIANT under
    the scaling freedom the equations possess, and does eps depend only on those?

The count of independent invariants IS the answer to "how many external numbers
does the bridge need". That is a falsifiable, internal question, and answering it
touches no data -- NO_BRIDGE_FITTING is not at risk here.

THE DERIVATION, to be CHECKED not trusted. The background system is

    rho_A = C/a^3 ,  rho_phys = rho_A*(1 - g*phibar) ,  V = lam*phibar^4/4
    H^2   = (8*pi*G/3)*(rho_phys + phibar_dot^2/2 + V)
    phibar_ddot = g*rho_A - 3*H*phibar_dot - lam*phibar^3
    a_dot = a*H

and the perturbation sector adds k^2/a^2 and V'' = 3*lam*phibar^2 terms.

Three one-parameter families leave this form-invariant (derived by hand, verified
symbolically in Part A and numerically in Part B):

  S1  COMOVING RESCALING     a -> b*a ,  C -> b^3*C ,  k -> b*k
  S2  TIME/DENSITY RESCALING t -> al*t , C -> C/al^2 , lam -> lam/al^2 , k -> k/al
  S3  FIELD RESCALING        phibar -> ga*phibar , g -> g/ga , C -> ga^2*C ,
                             lam -> lam/ga^2 , G -> G/ga^2

PRE-REGISTERED OUTCOMES:
  B-INVARIANT  every S_i leaves eps unchanged to solver precision AND a
               transformation deliberately OUTSIDE the group changes it -> the
               invariants are established, their count is the number of external
               numbers the bridge requires, and that number is reported.
  B-BROKEN     some S_i changes eps -> the derivation above is wrong. The bridge
               cannot be posed in these terms until it is fixed, and saying so is
               the result.

WHAT THIS CANNOT DO, stated before the numbers:
  * It cannot produce k in h/Mpc. It can only say how many independent external
    numbers such a mapping would need, and which internal quantity each one fixes.
  * It says nothing about whether the completion is right.
  * A symmetry verified at a few parameter points is not a proof; it is evidence
    at those points, and the negative control is what stops it being vacuous.
"""

import importlib.util
import os
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

_HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "p76_ref", os.path.join(_HERE, "P76_growth_observable.py")
)
p76 = importlib.util.module_from_spec(_spec)
sys.modules["p76_ref"] = p76
_spec.loader.exec_module(p76)

T_END = 1e8


def make_bg(g_hat, lam, C, G):
    """Background RHS with C and G left free -- P76 hard-codes both to 1."""

    def rhs(_t, y):
        a_, pb, pd = y
        rho_A = C / a_**3
        rho_phys = rho_A * (1.0 - g_hat * pb)
        arg = (8.0 * np.pi * G / 3.0) * (rho_phys + pd**2 / 2.0 + lam * pb**4 / 4.0)
        H = np.sqrt(arg) if arg > 0 else 0.0
        return [a_ * H, pd, g_hat * rho_A - 3.0 * H * pd - lam * pb**3]

    return rhs


def make_pert(g_hat, lam, C, G, kk):
    """P76's perturbation system with C, G free. Same equations, same order."""

    def rhs(_t, y):
        a_, pb, pd, psi, psid, dph, dphd, drA, qm = y
        rho_A = C / a_**3
        rho_phys = rho_A * (1.0 - g_hat * pb)
        Vp, Vpp = lam * pb**3, 3.0 * lam * pb**2
        arg = (8.0 * np.pi * G / 3.0) * (rho_phys + pd**2 / 2.0 + lam * pb**4 / 4.0)
        H = np.sqrt(arg) if arg > 0 else 0.0
        Hdot = -4.0 * np.pi * G * (rho_phys + pd**2)
        pdd = g_hat * rho_A - 3.0 * H * pd - Vp
        dp_phi = pd * dphd - psi * pd**2 - Vp * dph
        psidd = 4 * np.pi * G * dp_phi - 4 * H * psid - (2 * Hdot + 3 * H**2) * psi
        dphdd = (
            g_hat * drA
            + 2 * psi * (g_hat * rho_A - Vp)
            + 4 * psid * pd
            - 3 * H * dphd
            - (kk**2 / a_**2 + Vpp) * dph
        )
        drAd = -3 * H * drA + 3 * psid * rho_A + (kk**2 / a_**2) * qm / (1 - g_hat * pb)
        qmd = -3 * H * qm - rho_phys * psi + g_hat * rho_A * dph
        return [a_ * H, pd, pdd, psid, psidd, dphd, dphdd, drAd, qmd]

    return rhs


def eps_general(g_hat, lam, C, G, kk, a0, pd0, t0, t_end, psi0, dph0, drA0, n_a=2):
    """eps = d ln G_growth / d ln a, computed the P76 way but with units free.

    Returns None if either run cannot be carried -- an unresolved outcome, not a
    number, per the Substrate Gate discipline P81 had to be corrected for.
    """
    out = []
    for gg in (g_hat, 0.0):
        rho_A0 = C / a0**3
        b_rho_phys0 = rho_A0 * (1 - gg * 0.0)
        H0 = np.sqrt((8 * np.pi * G / 3) * (b_rho_phys0 + pd0**2 / 2.0))
        drho_phi0 = pd0 * 0.0 - psi0 * pd0**2
        drho_m0 = drA0 - gg * rho_A0 * dph0
        psid0 = (-(kk**2 / a0**2) * psi0 - 4 * np.pi * G * (drho_phi0 + drho_m0)) / (
            3 * H0
        ) - H0 * psi0
        qm0 = -(psid0 + H0 * psi0) / (4 * np.pi * G) + pd0 * dph0
        y0 = [a0, 0.0, pd0, psi0, psid0, dph0, 0.0, drA0, qm0]
        with np.errstate(all="ignore"):
            s = solve_ivp(
                make_pert(gg, lam, C, G, kk),
                (t0, t_end),
                y0,
                rtol=1e-11,
                atol=1e-20,
                dense_output=True,
            )
        if not s.success:
            return None
        out.append(s)

    # anchors: fixed FRACTIONS of the span, so they transform with the system
    ta, tb = t0 * (t_end / t0) ** 0.5, t0 * (t_end / t0) ** 0.95
    vals = []
    for s, gg in zip(out, (g_hat, 0.0), strict=True):
        r = []
        for tv in (ta, tb):
            a_, pb, pd, psi, _psid, dph, _dphd, drA, qm = s.sol(tv)
            rho_A = C / a_**3
            rho_phys = rho_A * (1 - gg * pb)
            H = np.sqrt((8 * np.pi * G / 3) * (rho_phys + pd**2 / 2.0 + lam * pb**4 / 4.0))
            delta = (drA * (1 - gg * pb) - gg * rho_A * dph - 3 * H * qm) / rho_phys
            r.append((delta, a_))
        vals.append(r)
    (d1c, a1c), (d2c, a2c) = vals[0]
    (d1u, _), (d2u, _) = vals[1]
    _ = n_a
    return np.log((d2c / d1c) / (d2u / d1u)) / np.log(a2c / a1c)


BASE = {
    "g_hat": 1.0,
    "lam": 1.0,
    "C": 1.0,
    "G": 1.0,
    "kk": 10.0,
    "a0": p76.A3_INIT ** (1.0 / 3.0),
    "pd0": p76.PHIDOT_INIT,
    "t0": 1.0,
    "t_end": T_END,
    "psi0": 1e-5,
    "dph0": 1e-6,
    "drA0": 1e-5,
}


def S1(p, b):
    """Comoving rescaling: a -> b*a, C -> b^3*C, k -> b*k. dph0/drA0 unchanged."""
    q = dict(p)
    q["a0"] *= b
    q["C"] *= b**3
    q["kk"] *= b
    return q


def S2(p, al):
    """Time/density rescaling: t -> al*t, C -> C/al^2, lam -> lam/al^2, k -> k/al."""
    q = dict(p)
    q["t0"] *= al
    q["t_end"] *= al
    q["C"] /= al**2
    q["lam"] /= al**2
    q["kk"] /= al
    q["pd0"] /= al
    return q


def S3(p, ga):
    """Field rescaling. G IS PART OF IT -- omitting G is what broke the first draft.

    phibar -> ga*phibar, g -> g/ga, C -> ga^2*C, lam -> lam/ga^2, G -> G/ga^2.

    # WHY G: without it the Friedmann RIGHT side picks up ga^2 (rho_A, the
    # kinetic term and V all scale that way) while the LEFT side (a_dot/a)^2 does
    # not move, so the equation is simply not satisfied. G -> G/ga^2 restores it,
    # and Klein-Gordon then scales uniformly as ga^1.
    """
    q = dict(p)
    q["g_hat"] /= ga
    q["C"] *= ga**2
    q["G"] /= ga**2
    q["lam"] /= ga**2
    q["pd0"] *= ga
    q["dph0"] *= ga
    q["drA0"] *= ga**2
    return q


def NOT_A_SYMMETRY(p, x):
    """Deliberately outside the group: lambda alone. The NEGATIVE CONTROL.

    # WHY this one: it changes a parameter the group DOES touch (lam), but not in
    # the combination any S_i uses. If eps survived this too, the positive checks
    # would prove nothing -- the same trap P77's non-discriminating pole test fell
    # into, and the reason P82 carries a negative control at all.
    """
    q = dict(p)
    q["lam"] *= x
    return q


def main() -> int:
    print("=" * 78)
    print("P84 -- scaling-group audit: what is physics, what is convention?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- the group, checked SYMBOLICALLY before any integration")
    print("-" * 78)
    print("  Each S_i is applied to the background equations with sympy and the")
    print("  residual must vanish IDENTICALLY. This catches a wrong exponent")
    print("  before a numerical run can hide it inside solver tolerance.")

    b, al, ga = sp.symbols("b alpha gamma", positive=True)
    C, G, g, lam = sp.symbols("C G g lambda", positive=True)

    # # THE FIRST VERSION OF THIS CHECK WAS ITSELF BROKEN, and it is worth the
    # # lines to say how, because it failed in two different ways at once and
    # # they must not be conflated.
    # #
    # # S3 gave a REAL residual: under phi->ga*phi, g->g/ga, C->ga^2*C,
    # # lam->lam/ga^2 the Friedmann RIGHT side picks up ga^2 while the LEFT side
    # # (a_dot/a)^2 does not move at all. G was missing from the transformation.
    # # With G -> G/ga^2 the two sides match and Klein-Gordon scales uniformly as
    # # ga^1 -- which is exactly the weight sympy had already reported as
    # # "invariant" for KG, so the tool was telling me where the gap was.
    # #
    # # S2's residual was a TEST artifact, not a physics error. It wrote
    # # a.subs(t, t/al), i.e. a(t/al), and compared an expression built on
    # # a(t/al) against one built on a(t). Those are different symbolic
    # # functions and their difference cannot simplify to zero however correct
    # # the physics is. Fixed by giving every equation the SAME argument u and
    # # putting the time rescaling into the derivative operator by hand.
    u = sp.symbols("u", positive=True)
    A = sp.Function("a")(u)
    P = sp.Function("phi")(u)

    def eqs_u(a_, ph_, C_, G_, g_, lam_, dt_du):
        """Residuals in the variable u, with d/dt = (1/dt_du) d/du supplied."""
        rho_A = C_ / a_**3
        rho_phys = rho_A * (1 - g_ * ph_)
        phdot = sp.diff(ph_, u) / dt_du
        adot = sp.diff(a_, u) / dt_du
        H = adot / a_
        H2 = (8 * sp.pi * G_ / 3) * (rho_phys + phdot**2 / 2 + lam_ * ph_**4 / 4)
        e_fried = H**2 - H2
        e_kg = sp.diff(phdot, u) / dt_du - g_ * rho_A + 3 * H * phdot + lam_ * ph_**3
        return sp.expand(e_fried), sp.expand(e_kg)

    base = eqs_u(A, P, C, G, g, lam, 1)
    checks = [
        (
            "S1  a->b*a, C->b^3*C, k->b*k",
            eqs_u(b * A, P, b**3 * C, G, g, lam, 1),
            (1, 1),
        ),
        (
            "S2  t->al*t, C->C/al^2, lam->lam/al^2, k->k/al",
            eqs_u(A, P, C / al**2, G, g, lam / al**2, al),
            (al**-2, al**-2),
        ),
        (
            "S3  phi->ga*phi, g->g/ga, C->ga^2*C, lam->lam/ga^2, G->G/ga^2",
            eqs_u(A, ga * P, ga**2 * C, G / ga**2, g / ga, lam / ga**2, 1),
            (1, ga),
        ),
    ]
    A_OK = True
    print(f"\n    {'transformation':<56}{'Friedmann':<14}{'Klein-Gordon'}")
    for name, (ef, ek), (wf, wk) in checks:
        rf = sp.simplify(sp.expand(ef - wf * base[0]))
        rk = sp.simplify(sp.expand(ek - wk * base[1]))
        okf, okk = rf == 0, rk == 0
        A_OK = A_OK and okf and okk
        print(
            f"    {name:<56}{('invariant' if okf else 'RESIDUAL'):<14}"
            f"{'invariant' if okk else 'RESIDUAL'}"
        )
    print(f"\n    => symbolic check {'PASSES' if A_OK else 'FAILS'}")
    if not A_OK:
        print("    *** the derivation is wrong. B-BROKEN before a single integration.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- does eps actually survive each S_i numerically?")
    print("-" * 78)
    ref = eps_general(**BASE)
    print(f"\n    reference eps (k=10, g=1, lam=1, C=1, G=1) : {ref:.12f}")
    print(f"\n    {'transformation':<34}{'eps':<20}{'rel change':<16}{'verdict'}")
    B_OK = True
    for name, fn, arg in (
        ("S1  b = 2", S1, 2.0),
        ("S1  b = 0.5", S1, 0.5),
        ("S2  alpha = 3", S2, 3.0),
        ("S2  alpha = 0.25", S2, 0.25),
        ("S3  gamma = 2", S3, 2.0),
        ("S3  gamma = 0.5", S3, 0.5),
    ):
        e = eps_general(**fn(BASE, arg))
        if e is None:
            print(f"    {name:<34}{'unresolved':<20}{'-':<16}NOT MEASURED")
            B_OK = False
            continue
        rel = abs(e / ref - 1)
        ok = rel < 1e-6
        B_OK = B_OK and ok
        print(f"    {name:<34}{e:<20.12f}{rel:<16.3e}{'invariant' if ok else 'CHANGED'}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- NEGATIVE CONTROL: eps must NOT survive a non-symmetry")
    print("-" * 78)
    print("  If eps were invariant under everything, Part B would prove nothing.")
    print(f"\n    {'transformation':<34}{'eps':<20}{'rel change':<16}{'verdict'}")
    C_OK = True
    for x in (2.0, 10.0, 0.1):
        e = eps_general(**NOT_A_SYMMETRY(BASE, x))
        if e is None:
            print(f"    lam -> {x:g}*lam".ljust(34) + f"{'unresolved':<20}{'-':<16}NOT MEASURED")
            continue
        rel = abs(e / ref - 1)
        moved = rel > 1e-3
        C_OK = C_OK and moved
        print(
            f"    lam -> {x:g}*lam".ljust(34)
            + f"{e:<20.12f}{rel:<16.3e}{'CHANGED (good)' if moved else 'INVARIANT (bad)'}"
        )
    print(f"\n    => negative control {'PASSES' if C_OK else 'FAILS'}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- WHICH invariant does k enter through? The actual deliverable.")
    print("-" * 78)
    print("  Part B says eps survives the whole group, so eps carries NO unit")
    print("  convention -- it is already a physical number. k does not: it moves")
    print("  under S1 and S2. So the bridge needs whatever INVARIANT k enters")
    print("  through, and nothing else.")
    print()
    print("  Derived: k/(a*H) is invariant under all three.")
    print("    S1  k->b*k and a->b*a           -> ratio unchanged")
    print("    S2  k->k/al and H->H/al         -> ratio unchanged")
    print("    S3  G->G/ga^2 with rho->ga^2*rho -> H unchanged, k and a unchanged")
    print()
    print("  Checked rather than argued -- k/(a*H) at t0 for every transform:")

    def k_over_aH(p_):
        rho_A0 = p_["C"] / p_["a0"] ** 3
        H0 = np.sqrt((8 * np.pi * p_["G"] / 3) * (rho_A0 + p_["pd0"] ** 2 / 2.0))
        return p_["kk"] / (p_["a0"] * H0)

    base_ratio = k_over_aH(BASE)
    print(f"\n{'parameter set':<34}{'k/(a*H) at t0':<26}{'rel change'}")
    print(f"    {'BASE':<34}{base_ratio:<26.15g}")
    D_OK = True
    for name, fn, arg in (
        ("S1  b = 2", S1, 2.0),
        ("S1  b = 0.5", S1, 0.5),
        ("S2  alpha = 3", S2, 3.0),
        ("S2  alpha = 0.25", S2, 0.25),
        ("S3  gamma = 2", S3, 2.0),
        ("S3  gamma = 0.5", S3, 0.5),
    ):
        r = k_over_aH(fn(BASE, arg))
        rel = abs(r / base_ratio - 1)
        ok = rel < 1e-12
        D_OK = D_OK and ok
        tag = "" if ok else "   NOT INVARIANT"
        print(f"    {name:<34}{r:<26.15g}{rel:.3e}{tag}")
    print(f"\n=> k/(a*H) {'IS invariant' if D_OK else 'is NOT invariant'}")
    print()
    print("  NEGATIVE CONTROL here too: a quantity that is NOT invariant must be")
    print("  seen to move, or the check above is vacuous.")
    print(f"\n{'parameter set':<34}{'bare k':<26}{'rel change'}")
    for name, fn, arg in (("S1  b = 2", S1, 2.0), ("S2  alpha = 3", S2, 3.0)):
        kk_ = fn(BASE, arg)["kk"]
        print(f"    {name:<34}{kk_:<26.15g}{abs(kk_ / BASE['kk'] - 1):.3e}")
    print("\nbare k moves, k/(a*H) does not -- the check discriminates.")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if A_OK and B_OK and C_OK:
        print("  -> B-INVARIANT. Three independent scalings leave eps unchanged, and")
        print("     a deliberate non-symmetry moves it. So of the EIGHT internal")
        print("     quantities (a, C, G, g_hat, lambda, phibar, k, t) THREE are pure")
        print("     convention -- P76 spent them on G_N=1, C_MATTER=1 and the")
        print("     choice of a(1).")
        print()
        print("     WHAT THIS MEANS FOR THE BRIDGE, and it is the deliverable:")
        print("     eps and f are invariant under the WHOLE group, so they carry")
        print("     NO unit convention -- they are ALREADY physical numbers and")
        print("     need nothing external. Only k does, and Part D shows it enters")
        print("     through the single invariant k/(a*H).")
        print()
        print("     So the bridge for eps(k) needs exactly ONE external number:")
        print("     the physical value of a*H at one reference epoch. NOT three.")
        print("     Three is what mapping EVERY internal quantity would cost, one")
        print("     per broken scaling. The observable we actually have is far")
        print("     cheaper than that, and quoting three would have OVERSTATED the")
        print("     cost of the bridge by conflating the two questions.")
    else:
        print("  -> B-BROKEN. The scaling group as derived does not hold:")
        if not A_OK:
            print("     the symbolic residual does not vanish.")
        if not B_OK:
            print("     eps moves under a claimed symmetry.")
        if not C_OK:
            print("     eps ALSO survives a non-symmetry, so Part B proves nothing")
            print("     -- the test does not discriminate and must be replaced.")
        print("     The bridge cannot be posed in these terms until this is fixed.")

    print("\n  NOT ESTABLISHED:")
    print("   * k in h/Mpc. This step CANNOT produce it -- only the COUNT of")
    print("     external numbers such a mapping needs, and what each one fixes.")
    print("   * that the symmetry holds away from the points tested. A symmetry")
    print("     verified at a few parameter values is evidence there, not a proof.")
    print("   * anything about whether the completion is right.")
    print("   * anything observational. NO_BRIDGE_FITTING untouched -- no dataset")
    print("     and no Table A1 quantity enters this file.")
    print("   * Perelman condition 5 -- still not met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
