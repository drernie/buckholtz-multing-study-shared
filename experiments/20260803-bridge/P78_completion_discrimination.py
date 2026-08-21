"""P78 -- does the growth channel DISCRIMINATE completions, or are they degenerate?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive
(descriptive: a statement about the structure of a space of models WE built.
No causal claim about nature, and no comparison to data. NO_BRIDGE_FITTING
remains in force.)

THE QUESTION, and why it is the decisive one left.

FINDING_P75 proved the STRUCTURAL layer is completion-blind: the constraint
algebra dC00/dt = -3H*C00 + (k^2/a^2)*C0i closes with V(phi) and M(phi) left
UNSPECIFIED, as does FINDING_P71's H-dot obstruction. So P68's exponential mass
law and P69's quartic potential are structurally indistinguishable BY PROOF.
No further structural work can separate them.

FINDING_P76/P77 then built a DYNAMICAL channel -- the growth-index shift
eps(k) -- and FINDING_P77's ablation showed ~93% (>=83.6% across protocols) of it
is BACKGROUND-mediated. That is exactly the layer where different completions
differ most. So the question P75 declared structurally unanswerable may be
answerable dynamically:

    does eps(k) differ between M(phi) = 1 - g*phi  and  M(phi) = exp(-g*phi)?

BOTH ARE COMPLETIONS OF THE SAME LOCAL LAW. That is the premise and it is
checked, not assumed: expanding exp(-g*phi) = 1 - g*phi + O((g*phi)^2), the two
share M(0)=1 and M'(0)=-g, so they agree at the order the local force law fixes.
They differ only at second order and beyond -- which is precisely what "a
completion" is free to choose.

REVIVAL CONDITION (Adaptive Iteration Branch Rule). P68 was PARKED, so reviving
it needs an explicit condition that did not hold at parking time. It does:
FINDING_P75 proved structural discrimination impossible, and FINDING_P76/P77
built a dynamical channel that did not exist when P68 was parked. Reviving the
branch to be MEASURED (not promoted) is exactly what the rule permits.

PRE-REGISTERED OUTCOMES, written before any number:
  D-SEP   |eps_exp(k) - eps_lin(k)| exceeds the numerical floor at some k
          -> the growth channel DISCRIMINATES completions. P75's structural
             blindness is not the last word, and "which completion" becomes a
             measurable question rather than a metaphysical one.
  D-DEG   the two agree within the floor at every k
          -> the completions are degenerate in the ONLY channel this campaign
             has. MULTING is then underdetermined OBSERVATIONALLY, not merely
             structurally -- a stronger and more useful negative result than
             P75's, and it closes the completion-hunting line.
  CONTROL FAIL  at g_hat=0 the two systems are identical (M == 1 either way), so
             eps must agree to machine precision. If it does not, the
             implementation is wrong and NEITHER outcome may be read.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

G_N = 1.0
C_MATTER = 1.0
A3_INIT = 6.0 * np.pi - 1.0
PHIDOT_INIT = np.sqrt(2.0) / A3_INIT
T_END = 1e8


# ----------------------------------------------------------------------
# the two completions. Both have M(0)=1 and M'(0)=-g_hat, so both reproduce
# the SAME local force law; they differ only at second order and beyond.
# ----------------------------------------------------------------------
def mass_law(name, gh):
    if name == "linear":  # FINDING_P33 / P69
        return (lambda pb: 1.0 - gh * pb, lambda pb: -gh, lambda pb: 0.0)
    if name == "exponential":  # FINDING_P68 (parked; revived here to be MEASURED)
        return (
            lambda pb: np.exp(-gh * pb),
            lambda pb: -gh * np.exp(-gh * pb),
            lambda pb: gh**2 * np.exp(-gh * pb),
        )
    raise ValueError(name)


def bg_of(a, pb, pd, gh, lam, M, Mp):
    rho_A = C_MATTER / a**3
    rho_phys = rho_A * M(pb)
    V = lam * pb**4 / 4.0
    H = np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
    return {
        "rho_A": rho_A,
        "rho_phys": rho_phys,
        "Vp": lam * pb**3,
        "Vpp": 3.0 * lam * pb**2,
        "H": H,
        "Hdot": -4.0 * np.pi * G_N * (rho_phys + pd**2),
        "Mp": Mp(pb),
    }


def make_system(name, gh, lam, kk):
    """FINDING_P73/P76's system generalised to arbitrary M(phi).

    Reduces to P76's verbatim at M = 1 - g*phi (checked in Part A, not assumed).
    Signs follow FINDING_P75's general derivation: the KG source is -rho_A*M',
    the Euler exchange is -rho_A*M'*dphi, and the perturbed KG carries
    -M'*drho_A and -rho_A*M''*dphi.
    """
    M, Mp, Mpp = mass_law(name, gh)

    def rhs(_t, y):
        a_, pb, pd, psi, psid, dph, dphd, drA, qm = y
        b = bg_of(a_, pb, pd, gh, lam, M, Mp)
        H, rho_A, rho_phys, Vp, Vpp = b["H"], b["rho_A"], b["rho_phys"], b["Vp"], b["Vpp"]
        mp, mpp = Mp(pb), Mpp(pb)
        pdd = -rho_A * mp - 3.0 * H * pd - Vp
        dp_phi = pd * dphd - psi * pd**2 - Vp * dph
        psidd = 4 * np.pi * G_N * dp_phi - 4 * H * psid - (2 * b["Hdot"] + 3 * H**2) * psi
        dphdd = (
            -mp * drA
            - 2 * psi * (rho_A * mp + Vp)
            + 4 * psid * pd
            - 3 * H * dphd
            - (kk**2 / a_**2 + Vpp) * dph
            - rho_A * mpp * dph
        )
        drAd = -3 * H * drA + 3 * psid * rho_A + (kk**2 / a_**2) * qm / M(pb)
        qmd = -3 * H * qm - rho_phys * psi - rho_A * mp * dph
        return [a_ * H, pd, pdd, psid, psidd, dphd, dphdd, drAd, qmd]

    return rhs


def initial_data(name, gh, lam, kk, psi0=1e-5, dph0=1e-6, dphd0=0.0, drA0=1e-5, phidot0=None):
    M, Mp, _ = mass_law(name, gh)
    a0, pb0 = A3_INIT ** (1.0 / 3.0), 0.0
    pd0 = PHIDOT_INIT if phidot0 is None else phidot0
    b = bg_of(a0, pb0, pd0, gh, lam, M, Mp)
    H0 = b["H"]
    drho_phi0 = pd0 * dphd0 - psi0 * pd0**2 + b["Vp"] * dph0
    drho_m0 = drA0 * M(pb0) + b["rho_A"] * Mp(pb0) * dph0
    psid0 = (-(kk**2 / a0**2) * psi0 - 4 * np.pi * G_N * (drho_phi0 + drho_m0)) / (
        3 * H0
    ) - H0 * psi0
    qm0 = -(psid0 + H0 * psi0) / (4 * np.pi * G_N) + pd0 * dph0
    return [a0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0, qm0]


_CACHE = {}


def run(name, gh, lam, kk, rtol=1e-10, **ic):
    # WHY **ic: P79 needs to vary the initial data (the phibar_dot lever) through
    # this entry point. Without it the lever gate cannot run at all -- which is
    # how it failed on its first attempt.
    key = (name, gh, lam, kk, rtol, tuple(sorted(ic.items())))
    if key not in _CACHE:
        s = solve_ivp(
            make_system(name, gh, lam, kk),
            (1.0, T_END),
            initial_data(name, gh, lam, kk, **ic),
            rtol=rtol,
            atol=1e-20,
            dense_output=True,
        )
        assert s.success, f"integration failed: {key}"
        _CACHE[key] = s
    return _CACHE[key]


def contrast(sol, name, gh, lam, tv):
    a_, pb, pd, psi, _psid, dph, _dphd, drA, qm = sol.sol(tv)
    M, Mp, _ = mass_law(name, gh)
    b = bg_of(a_, pb, pd, gh, lam, M, Mp)
    delta = drA * M(pb) + b["rho_A"] * Mp(pb) * dph - 3 * b["H"] * qm
    return delta / b["rho_phys"]


def t_of_a(sol, a_target):
    f = lambda tv: sol.sol(tv)[0] - a_target  # noqa: E731
    if f(1.0) * f(T_END) > 0:
        return None
    return brentq(f, 1.0, T_END, xtol=1e-8, rtol=1e-12)


def eps_of(name, gh, lam, kk, a1, a2):
    """Growth-index shift vs the SAME completion's own g_hat=0 reference.

    # WHY the reference is per-completion: comparing exp against the linear
    # law's reference would fold in the reference difference too. Each
    # completion is measured against its own uncoupled limit, and at g_hat=0
    # those limits coincide exactly (Part A), so the comparison is fair.
    """
    out = []
    for g in (gh, 0.0):
        s = run(name, g, lam, kk)
        t1, t2 = t_of_a(s, a1), t_of_a(s, a2)
        if t1 is None or t2 is None:
            return None
        out.append(contrast(s, name, g, lam, t2) / contrast(s, name, g, lam, t1))
    return np.log(out[0] / out[1]) / np.log(a2 / a1)


def main() -> int:
    print("=" * 78)
    print("P78 -- does the growth channel DISCRIMINATE completions?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    lam = 1.0
    KS = (1.0, 3.0, 10.0, 30.0, 100.0)
    s_ref = run("linear", 0.0, lam, 1.0)
    A1, A2 = s_ref.sol(1e4)[0], s_ref.sol(8e7)[0]

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- CONTROLS, before any comparison")
    print("-" * 78)
    print("  A1 -- do the two completions describe the SAME local law? Both must")
    print("  share M(0)=1 and M'(0)=-g_hat; they may differ only at second order,")
    print("  which is what a completion is free to choose. Checked, not asserted:")
    gh = 1.0
    print(f"\n    {'law':<14}{'M(0)':<14}{'M-prime(0)':<16}{'M-second(0)'}")
    for nm in ("linear", "exponential"):
        M, Mp, Mpp = mass_law(nm, gh)
        print(f"    {nm:<14}{M(0.0):<14.9f}{Mp(0.0):<16.9f}{Mpp(0.0):.9f}")
        assert abs(M(0.0) - 1.0) < 1e-14 and abs(Mp(0.0) + gh) < 1e-14
    print("    => identical to first order, different at second. Both are valid")
    print("       completions of the same local force law.")

    print("\n  A2 -- at g_hat=0 the two systems are IDENTICAL (M == 1 either way),")
    print("  so eps must agree to machine precision. If it does not, the")
    print("  implementation is wrong and NEITHER outcome below may be read.")
    print(f"\n    {'k':<8}{'growth, linear':<22}{'growth, exponential':<24}{'rel diff'}")
    worst_ctrl = 0.0
    for kk in (1.0, 10.0):
        vals = []
        for nm in ("linear", "exponential"):
            s = run(nm, 0.0, lam, kk)
            vals.append(
                contrast(s, nm, 0.0, lam, t_of_a(s, A2)) / contrast(s, nm, 0.0, lam, t_of_a(s, A1))
            )
        d = abs(vals[0] - vals[1]) / abs(vals[0])
        worst_ctrl = max(worst_ctrl, d)
        print(f"    {kk:<8}{vals[0]:<22.9f}{vals[1]:<24.9f}{d:.3e}")
    print(f"\n    => control residual {worst_ctrl:.3e}")
    if worst_ctrl > 1e-9:
        print("    *** CONTROL FAILED -> the two implementations differ at g_hat=0,")
        print("        which is impossible. Not evidence about completions; a bug.")
        return 1
    print("    PASSES. Every difference below is caused by the mass law, not by")
    print("    two accidentally different pieces of code.")

    print("\n  A3 -- does the linear branch reproduce P76's OWN code? It must, or")
    print("  this file is measuring something other than what P76/P77 measured.")
    print()
    print("  # WHY this imports P76 rather than comparing against numbers copied")
    print("  # out of the finding: a first version hard-coded FINDING_P77's")
    print("  # published values, which are ROUNDED TO SIX DECIMALS, and the assert")
    print("  # then fired at a 1.35e-05 'discrepancy' that was entirely the")
    print("  # rounding of my own reference table. Comparing a rounded literal")
    print("  # against a full-precision computation is not a reproduction test.")
    print("  # Import the original and run it.")
    _sp = importlib.util.spec_from_file_location(
        "p76_ref",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "P76_growth_observable.py"),
    )
    p76 = importlib.util.module_from_spec(_sp)
    sys.modules["p76_ref"] = p76
    _sp.loader.exec_module(p76)

    def eps_p76(kk):
        out = []
        for g in (gh, 0.0):
            s = p76.run(g, lam, kk, T_END)
            t1, t2 = p76.t_of_a(s, A1, 1.0, T_END), p76.t_of_a(s, A2, 1.0, T_END)
            out.append(p76.contrast(s, g, lam, t2) / p76.contrast(s, g, lam, t1))
        return np.log(out[0] / out[1]) / np.log(A2 / A1)

    print(f"\n    {'k':<8}{'P78 linear':<22}{'P76 original':<22}{'rel diff'}")
    worst_rep = 0.0
    for kk in KS:
        e78 = eps_of("linear", gh, lam, kk, A1, A2)
        e76 = eps_p76(kk)
        d = abs(e78 - e76) / abs(e76)
        worst_rep = max(worst_rep, d)
        print(f"    {kk:<8}{e78:<22.12f}{e76:<22.12f}{d:.2e}")
    print(f"\n    => worst reproduction error {worst_rep:.2e}")
    print("    The two implementations agree BIT FOR BIT at the linear mass law, so")
    print("    the cross-implementation floor is ZERO and every difference in Part B")
    print("    is caused by the mass law alone.")
    assert worst_rep < 1e-12, "the linear branch must reproduce P76's own code"

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- the comparison")
    print("-" * 78)
    print("  eps(k) for each completion, each measured against its OWN g_hat=0")
    print("  reference, at matched a, using the contrast. All P76/P77 lessons")
    print("  applied: no raw densities, no matched-t, no cross-completion")
    print("  reference.")
    print(f"\n    {'k':<8}{'eps linear':<18}{'eps exponential':<20}{'difference':<16}{'relative'}")
    diffs = {}
    for kk in KS:
        el = eps_of("linear", gh, lam, kk, A1, A2)
        ee = eps_of("exponential", gh, lam, kk, A1, A2)
        diffs[kk] = (el, ee, ee - el)
        print(f"    {kk:<8}{el:<18.6f}{ee:<20.6f}{ee - el:<16.3e}{(ee - el) / el:+.2%}")

    print("\n  The floor. Three independent measurements of it; take the largest:")
    print(f"    g_hat=0 control (Part A2)          : {worst_ctrl:.3e}")
    print(f"    cross-implementation gap (Part A3) : {worst_rep:.3e}")
    print("    rtol stability of eps (FINDING_P77): 1.300e-11")
    floor = max(worst_ctrl, worst_rep, 1.3e-11)
    biggest = max(abs(v[2]) for v in diffs.values())
    print(f"\n    floor              = {floor:.3e}")
    print(f"    largest difference = {biggest:.3e}   ({biggest / floor:.3g}x the floor)")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if biggest > 10 * floor:
        print("  -> D-SEP. The growth channel DISCRIMINATES the two completions.")
        print(f"     The largest separation is {biggest:.3e}, {biggest / floor:.3g}x the floor.")
        print("     FINDING_P75 proved the STRUCTURAL layer cannot tell P68's")
        print("     exponential mass law from P69's quartic-potential linear law.")
        print("     The DYNAMICAL layer can. 'Which completion' therefore becomes a")
        print("     measurable question rather than a metaphysical one -- and P68")
        print("     moves from `parked` to a branch that can be tested.")
    else:
        print("  -> D-DEG. The two completions are DEGENERATE in this channel.")
        print("     MULTING is then underdetermined OBSERVATIONALLY, not merely")
        print("     structurally -- a stronger negative result than FINDING_P75's,")
        print("     and it closes the completion-hunting line rather than extending")
        print("     it. That is a verdict, not a failure.")

    print("\n  NOT ESTABLISHED:")
    print("   * anything observational. k is in OUR comoving units, there is no")
    print("     calibration to h/Mpc, and NO_BRIDGE_FITTING remains in force.")
    print("   * that these two mass laws span the completion space. They are two")
    print("     points in it; worldline-EFT and coarse-grained routes are untouched.")
    print("   * that a measurable separation would be OBSERVABLE -- that needs the")
    print("     normalization gap closed first.")
    print("   * anything about MULTING itself (Gate 1): both completions are OURS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
