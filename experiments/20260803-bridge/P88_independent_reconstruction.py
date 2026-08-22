"""P88 -- Perelman condition 5: an INDEPENDENTLY WRITTEN reconstruction of eps(k).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS IS THE LAST THING THE CAMPAIGN CAN DO FOR ITSELF.

Every finding from P73 onward ends with "Perelman condition 5 -- still not met."
Condition 5 is EXTERNAL RECONSTRUCTION, and the reason it has never been met is
structural: every single step imports P76_growth_observable.py. P80, P81, P82,
P84, P87 all call the same run(), the same contrast(), the same integrator. When
FINDING_P82 found that its delta_f reproduced P77's anchor-free slope to 1.15e-04
it had to scope that agreement as "weak-to-medium" on the Independent
Verification Strength Ladder -- same model, isolated context -- precisely because
the two numbers came out of one implementation.

This file is a SECOND IMPLEMENTATION of eps(k), sharing no computational code
with the first.

WHAT "INDEPENDENT" MEANS HERE, CONCRETELY. Not "written again in different
words". The formulation itself differs:

    P76                                  this file
    ---------------------------------    ---------------------------------
    independent variable t               independent variable N = ln a
    a is a STATE VARIABLE, dot a = a*H   a IS the variable; H from the
                                         Friedmann constraint algebraically
    9 state variables                    8 state variables
    matching at equal a needs brentq     matching is free -- a is the axis
    RK45                                 DOP853

The Friedmann constraint is therefore satisfied EXACTLY BY CONSTRUCTION here,
rather than approximately by integrating a alongside it, and an entire
root-finding layer disappears. Those are different sources of error, which is
the point of a reconstruction.

WHAT IS SHARED, AND MUST BE. The EQUATIONS and the INITIAL DATA are the claim's
specification, not its implementation -- a reconstruction that solved different
equations would be measuring something else. So the physics is transcribed from
the findings; the code to solve it is not.

THE TRAP THIS AVOIDS. FINDING_P78's control A3 failed falsely because it compared
against P77's published values ROUNDED TO SIX DECIMALS. So this file does NOT
compare against the published 0.045688. It picks its own anchors and runs P76's
machinery at THOSE SAME anchors, so the comparison is like-for-like at full
precision and cannot be measuring a rounding artifact.

PRE-REGISTERED OUTCOMES (thresholds fixed before any number):
  R-CONFIRMED   relative agreement < 1e-4 at every k tested -> Perelman
                condition 5 is met AT THE "independently-written code" RUNG for
                this one claim, and for no other claim in the campaign.
  R-MARGINAL    agreement between 1e-4 and 1e-2 -> the number survives but the
                difference needs naming before it can be quoted as reconstructed.
  R-DISCREPANT  worse than 1e-2 -> one of the two implementations is wrong, and
                the campaign's central number is in doubt until it is resolved.

WHAT THIS CANNOT DO, STATED BEFORE THE NUMBERS AND NOT NEGOTIABLE AFTERWARDS:
  * The higher rungs stay unmet. A different MODEL, a blind replication by
    another group, and a new physical experiment are all still absent, and the
    same person wrote both implementations. Meeting one rung is not meeting
    condition 5 in the sense Perelman's own case required.
  * It reconstructs eps(k) ONLY. mu_tot == 1, the viability boundary, the growth
    rate f, the scaling group -- none of those are touched, and each would need
    its own reconstruction.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

# ---------------------------------------------------------------------------
# THE RECONSTRUCTION. Nothing above this line imports anything from the
# campaign; the constants below are transcribed from the findings' STATED
# specification, which is the claim, not the code that solves it.
# ---------------------------------------------------------------------------

G_N = 1.0
C_M = 1.0
A3_0 = 6.0 * np.pi - 1.0  # a(t=1)^3
A_0 = A3_0 ** (1.0 / 3.0)
U_0 = np.sqrt(2.0) / A3_0  # phibar_dot(t=1)
PSI_0, DPH_0, DPHD_0, DRA_0 = 1e-5, 1e-6, 0.0, 1e-5


def _H_and_Hdot(a, phi, u, g, lam, sign_euler=1.0):
    """H from the Friedmann CONSTRAINT -- not integrated, solved."""
    rho_A = C_M / a**3
    rho_phys = rho_A * (1.0 - g * phi)
    V = lam * phi**4 / 4.0
    H2 = (8.0 * np.pi * G_N / 3.0) * (rho_phys + u * u / 2.0 + V)
    H = np.sqrt(H2) if H2 > 0 else 0.0
    Hdot = -4.0 * np.pi * G_N * (rho_phys + u * u)
    _ = sign_euler
    return H, Hdot, rho_A, rho_phys


def rhs_lnA(g, lam, k, sign_euler=1.0):
    """d/dN of the 8-vector, N = ln a. Every dot-derivative divided by H."""

    def f(N, y):
        a = np.exp(N)
        phi, u, psi, psid, dph, dphd, dra, qm = y
        H, Hdot, rho_A, rho_phys = _H_and_Hdot(a, phi, u, g, lam)
        if H <= 0.0:
            return np.zeros(8)
        Vp = lam * phi**3
        Vpp = 3.0 * lam * phi**2
        k2a2 = (k / a) ** 2

        du = g * rho_A - 3.0 * H * u - Vp
        dp_phi = u * dphd - psi * u * u - Vp * dph
        dpsid = 4.0 * np.pi * G_N * dp_phi - 4.0 * H * psid - (2.0 * Hdot + 3.0 * H * H) * psi
        ddphd = (
            g * dra
            + 2.0 * psi * (g * rho_A - Vp)
            + 4.0 * psid * u
            - 3.0 * H * dphd
            - (k2a2 + Vpp) * dph
        )
        ddra = -3.0 * H * dra + 3.0 * psid * rho_A + k2a2 * qm / (1.0 - g * phi)
        dqm = -3.0 * H * qm - rho_phys * psi + sign_euler * g * rho_A * dph
        return np.array([u, du, psid, dpsid, dphd, ddphd, ddra, dqm]) / H

    return f


def initial_state(g, lam, k):
    """Constraint-consistent initial data, from the specification."""
    a = A_0
    rho_A = C_M / a**3
    rho_phys = rho_A  # phibar(t=1) = 0
    H = np.sqrt((8.0 * np.pi * G_N / 3.0) * (rho_phys + U_0 * U_0 / 2.0))
    drho_phi = U_0 * DPHD_0 - PSI_0 * U_0 * U_0  # V'(0) = 0
    drho_m = DRA_0 - g * rho_A * DPH_0
    psid = (-((k / a) ** 2) * PSI_0 - 4.0 * np.pi * G_N * (drho_phi + drho_m)) / (
        3.0 * H
    ) - H * PSI_0
    qm = -(psid + H * PSI_0) / (4.0 * np.pi * G_N) + U_0 * DPH_0
    _ = lam
    return np.array([0.0, U_0, PSI_0, psid, DPH_0, DPHD_0, DRA_0, qm])


def contrast_recon(a, y, g, lam):
    phi, u, _psi, _psid, dph, _dphd, dra, qm = y
    H, _, rho_A, rho_phys = _H_and_Hdot(a, phi, u, g, lam)
    return (dra * (1.0 - g * phi) - g * rho_A * dph - 3.0 * H * qm) / rho_phys


def eps_recon(g, lam, k, a1, a2, sign_euler=1.0, rtol=1e-11):
    """eps against the (0, lam) reference, both solved in N = ln a with DOP853."""
    out = []
    for gg in (g, 0.0):
        s = solve_ivp(
            rhs_lnA(gg, lam, k, sign_euler),
            (np.log(A_0), np.log(a2) + 0.05),
            initial_state(gg, lam, k),
            method="DOP853",
            rtol=rtol,
            atol=1e-22,
            dense_output=True,
        )
        if not s.success:
            return None
        d1 = contrast_recon(a1, s.sol(np.log(a1)), gg, lam)
        d2 = contrast_recon(a2, s.sol(np.log(a2)), gg, lam)
        out.append(d2 / d1)
    return np.log(out[0] / out[1]) / np.log(a2 / a1)


# ---------------------------------------------------------------------------
# Everything BELOW this line may touch the campaign's code -- the comparison
# obviously needs both numbers. The reconstruction above does not.
# ---------------------------------------------------------------------------

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location(
    "p76_cmp", os.path.join(_HERE, "P76_growth_observable.py")
)
p76 = importlib.util.module_from_spec(_sp)
sys.modules["p76_cmp"] = p76
_sp.loader.exec_module(p76)

T_END_P76 = 1e8
A1, A2 = 1000.0, 400000.0  # MY anchors, round numbers, chosen here, not inherited


def eps_p76(g, lam, k, a1, a2):
    """P76's OWN PUBLIC ENTRY POINT, evaluated at the SAME anchors.

    # WHY G_growth rather than re-assembling run/t_of_a/contrast by hand here:
    # what is being compared against is P76 AS IT IS, not my transcription of
    # its internals -- a transcription could import my own reading of it and
    # quietly stop being the other implementation. eps = ln(G)/ln(a2/a1) is
    # P76's own Part F formula, unchanged.
    # An unreachable anchor raises inside G_growth. That is an INFRASTRUCTURE
    # outcome (Substrate Gate), not a disagreement, so it returns None and the
    # verdict branch reports "not measured" instead of scoring it against the
    # claim.
    """
    try:
        gr = p76.G_growth(g, lam, k, a1, a2, T_END_P76)
    except AssertionError:
        return None
    return np.log(gr) / np.log(a2 / a1)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P88 -- Perelman condition 5: independent reconstruction of eps(k)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- CONTROLS ON THE RECONSTRUCTION ITSELF")
    print("-" * 78)

    print("\n  L1 -- EXTERNAL lock mass, before any comparison. In matter")
    print("  domination the growing mode is delta ~ a, so d ln delta / d ln a")
    print("  must be 1. Textbook, and owed to nothing in this project. A")
    print("  reconstruction that cannot reproduce it is not a reconstruction.")
    s0 = solve_ivp(
        rhs_lnA(0.0, 0.0, 10.0),
        (np.log(A_0), np.log(A2) + 0.05),
        initial_state(0.0, 0.0, 10.0),
        method="DOP853",
        rtol=1e-11,
        atol=1e-22,
        dense_output=True,
    )
    print(f"\n    {'a':<14}{'d ln delta / d ln a':<26}{'deviation from 1'}")
    worst = 0.0
    for a in (1e3, 1e4, 1e5, 4e5):
        h = 1e-4
        d_p = contrast_recon(a * np.exp(h), s0.sol(np.log(a) + h), 0.0, 0.0)
        d_m = contrast_recon(a * np.exp(-h), s0.sol(np.log(a) - h), 0.0, 0.0)
        fN = np.log(d_p / d_m) / (2 * h)
        worst = max(worst, abs(fN - 1.0))
        print(f"    {a:<14.4g}{fN:<26.12f}{fN - 1:+.3e}")
    L1 = worst < 1e-3
    print(f"\n    worst deviation {worst:.3e}  =>  L1 {'PASSES' if L1 else 'FAILS'}")
    if not L1:
        print("    *** the reconstruction does not reproduce the textbook value.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- the reconstruction against P76, at IDENTICAL anchors")
    print("-" * 78)
    print(f"  anchors a1 = {A1:g}, a2 = {A2:g} -- chosen HERE, not inherited, and")
    print("  P76 is evaluated at the same two so the comparison cannot be")
    print("  measuring a published rounding (the error FINDING_P78's A3 made).")
    print(f"\n    {'k':<7}{'reconstruction':<20}{'P76':<20}{'relative diff'}")
    diffs = {}
    for k in (3.0, 10.0, 30.0):
        er = eps_recon(1.0, 1.0, k, A1, A2)
        ep = eps_p76(1.0, 1.0, k, A1, A2)
        if er is None or ep is None:
            print(f"    {k:<7g}{'unresolved -- not measured':<40}")
            diffs[k] = None
            continue
        rel = abs(er / ep - 1.0)
        diffs[k] = rel
        print(f"    {k:<7g}{er:<20.12f}{ep:<20.12f}{rel:.3e}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- NEGATIVE CONTROL: a corrupted reconstruction must DISAGREE")
    print("-" * 78)
    print("  If the comparison passes even with a deliberate bug, it proves")
    print("  nothing. The Euler exchange term's sign is flipped in the")
    print("  reconstruction ONLY, and the agreement must collapse.")
    print(f"\n    {'k':<7}{'corrupted recon':<20}{'P76':<20}{'relative diff'}")
    C_OK = True
    for k in (10.0,):
        eb = eps_recon(1.0, 1.0, k, A1, A2, sign_euler=-1.0)
        ep = eps_p76(1.0, 1.0, k, A1, A2)
        if eb is None or ep is None:
            print(f"    {k:<7g}{'unresolved':<40}")
            C_OK = False
            continue
        rel = abs(eb / ep - 1.0)
        C_OK = C_OK and rel > 1e-3
        print(f"    {k:<7g}{eb:<20.12f}{ep:<20.12f}{rel:.3e}")
    print(
        f"\n    negative control {'PASSES' if C_OK else 'FAILS'} -- the comparison discriminates."
    )

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    vals = [v for v in diffs.values() if v is not None]
    if not vals or len(vals) < len(diffs):
        print("  -> NOT MEASURABLE at one or more k. Infrastructure outcome, NOT")
        print("     evidence about the claim.")
    elif not C_OK:
        print("  -> INVALID. The negative control did not discriminate, so the")
        print("     agreement in Part B carries no information.")
    elif max(vals) < 1e-4:
        print(f"  -> R-CONFIRMED. Worst relative difference {max(vals):.3e} < 1e-4.")
        print("     Two implementations sharing NO computational code -- different")
        print("     independent variable, different state vector, different")
        print("     integrator, Friedmann exact by construction versus integrated")
        print("     -- agree on eps(k).")
        print()
        print("     PERELMAN CONDITION 5 IS MET AT THE 'independently-written")
        print("     code' RUNG, FOR eps(k) ONLY.")
        print()
        print("     AND NOT ABOVE IT. The same person wrote both implementations.")
        print("     A different MODEL, a blind replication by another group, and a")
        print("     new physical experiment all remain absent. On the campaign's")
        print("     own Independent Verification Strength Ladder this is 'Strong',")
        print("     not 'Very strong' and not 'Strongest'. Every other claim in")
        print("     the campaign -- mu_tot == 1, the viability boundary, f, the")
        print("     scaling group -- is UNTOUCHED and still unmet.")
    elif max(vals) < 1e-2:
        print(f"  -> R-MARGINAL. Worst relative difference {max(vals):.3e}. The")
        print("     number survives but the difference must be NAMED before eps")
        print("     may be called reconstructed.")
    else:
        print(f"  -> R-DISCREPANT. Worst relative difference {max(vals):.3e}. One")
        print("     of the two implementations is wrong, and the campaign's")
        print("     central number is in doubt until that is resolved.")

    print("\n  NOT ESTABLISHED:")
    print("   * any claim other than eps(k) at (g_hat, lambda) = (1, 1).")
    print("   * that the shared EQUATIONS are right. A reconstruction tests the")
    print("     implementation, never the specification -- if both files solve")
    print("     the same wrong equations they will agree beautifully.")
    print("   * anything observational. NO_BRIDGE_FITTING untouched.")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
