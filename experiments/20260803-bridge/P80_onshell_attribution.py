"""P80 -- constraint-preserving attribution: which channel carries the effect?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THE EXISTING ATTRIBUTION IS NOT A MEASUREMENT.

FINDING_P77 split eps into a background-mediated part and a direct-force part by
DELETING the +g*rho_A*dphi term from the matter Euler equation. That takes the
system OFF-SHELL: FINDING_P73's first-class algebra breaks, the 0i constraint
residual reaches 6.8e-2, and -- decisively -- the direct share moves from 6.61%
to 16.39% depending only on when the probe is started. A factor 2.5 from an
arbitrary protocol choice is not a measurement.

THE FIX, AND IT IS NOT A PATCH.

Promote the coupling to TWO independent parameters:

    g_bg    appears in the BACKGROUND equations (a, phibar, rho_A)
    g_pert  appears in the PERTURBATION sector (the Euler exchange, the
            perturbed KG source, the perturbed matter density)

Then measure the direct contribution as a DERIVATIVE evaluated AT the physical
point g_pert = g_bg = g_hat:

    pert_sector := g_hat * d eps/d g_pert   |_(g_pert = g_bg = g_hat)

NAMING, AND IT IS NOT COSMETIC. This is NOT "the direct fifth force". g_pert
moves FOUR things at once: the dphi source, the scalar's stress perturbation,
the metric response through drho_phi, and the Euler force on matter. What the
derivative measures is the sensitivity of the whole PERTURBATION SECTOR. Calling
it "the fifth force" would attribute the number to one of the four.

A derivative at the on-shell point never leaves the constraint surface. A finite
deletion does. This is thermodynamic integration's trick -- integrate dH/dlambda
along the coupling rather than subtracting two states -- and it is the standard
answer to exactly this problem in computational physics.

WHY THIS MATTERS MORE AFTER FINDING_P79, NOT LESS.

P79 showed the P78 separation is initial-condition dependent by a factor 5. It
could NOT say through which channel: an IC-sensitive background history and an
IC-sensitive direct coupling look identical in eps. If the on-shell split works,
it says which -- and those are different diagnoses with different consequences.

PRE-REGISTERED OUTCOMES (before any number):
  A-OK    the derivative is well-defined (converges as the step shrinks) and
          the two channels sum to the total -> a SENSITIVITY DECOMPOSITION is
          established: the response along the physical line g_bg = g_pert = g is
          resolved into two coordinate components.
          *** NOT a causal decomposition. *** Part C's closure is the chain rule
          d eps(g,g)/dg = d/dg_bg + d/dg_pert, which EVERY smooth function
          obeys -- so closure tests the implementation, and cannot be evidence
          that the two coordinates name two physical mechanisms. Off-diagonal
          points g_bg != g_pert need not correspond to any action at all.
          Deeper, and worth stating because it may be the real answer: in the
          action ONE function M'(phi) governs both the sourcing of the scalar and
          the force back on matter. They are two faces of a single interaction
          term. If they cannot be varied independently without changing the
          theory, then "X% background vs Y% force" has NO unique physical answer,
          and only the total along the diagonal is defined.
  A-DEG   the derivative does not converge, or the channels do not sum ->
          attribution is impossible in principle in this formulation, which is
          itself a result and, combined with P79's W-FAIL, triggers the TZ stop
          rule.
  CONTROL   the split must not leak: with BOTH linear g_pert channels closed
            (background scalar off AND no dphi seed) the derivative must be
            exactly zero. If it is not, NEITHER outcome above may be read.
            The control as first written demanded zero at g_hat = 0 with the
            background scalar still running. That was false physics, it fired
            twice, and it is retracted in Part A -- see the note there.

WHAT THIS STEP CANNOT DO, STATED BEFORE THE NUMBERS.
Even A-OK leaves the response's dependence on the scalar's initial amplitude
unexplained: d eps/d g_pert is ODD in phibar_dot(1) to 3% but scales as
eta^0.30, not eta^1. Two candidate explanations were built and BOTH failed
(a point-sample amplitude -- invalid, the field oscillates and the samples
alternate in sign; and an RMS envelope over the growth window -- exponents
0.39 and 0.26, nowhere near 1). It is recorded as an open gap in Part E
rather than fitted until something matches.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location(
    "p76_ref", os.path.join(_HERE, "P76_growth_observable.py")
)
p76 = importlib.util.module_from_spec(_sp)
sys.modules["p76_ref"] = p76
_sp.loader.exec_module(p76)

G_N, C_MATTER = p76.G_N, p76.C_MATTER
A3_INIT, PHIDOT = p76.A3_INIT, p76.PHIDOT_INIT
T_END = 1e8


def bg_of(a, pb, pd, g_bg, lam):
    """The BACKGROUND sector. Sees only g_bg."""
    rho_A = C_MATTER / a**3
    rho_phys = rho_A * (1.0 - g_bg * pb)
    V = lam * pb**4 / 4.0
    H = np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
    return {
        "rho_A": rho_A,
        "rho_phys": rho_phys,
        "Vp": lam * pb**3,
        "Vpp": 3.0 * lam * pb**2,
        "H": H,
        "Hdot": -4.0 * np.pi * G_N * (rho_phys + pd**2),
    }


def make_system(g_bg, g_pert, lam, kk):
    """FINDING_P76's system with the coupling split in two.

    # WHY the split is exactly here: g_bg is the coupling as it enters the
    # BACKGROUND (Friedmann, the KG source, matter dilution); g_pert is the same
    # coupling as it enters the PERTURBED equations. At g_bg == g_pert this is
    # FINDING_P76's system verbatim -- asserted in Part A, not assumed.
    """

    def rhs(_t, y):
        a_, pb, pd, psi, psid, dph, dphd, drA, qm = y
        b = bg_of(a_, pb, pd, g_bg, lam)
        H, rho_A, rho_phys, Vp, Vpp = b["H"], b["rho_A"], b["rho_phys"], b["Vp"], b["Vpp"]
        pdd = g_bg * rho_A - 3.0 * H * pd - Vp
        dp_phi = pd * dphd - psi * pd**2 - Vp * dph
        psidd = 4 * np.pi * G_N * dp_phi - 4 * H * psid - (2 * b["Hdot"] + 3 * H**2) * psi
        dphdd = (
            g_pert * drA
            + 2 * psi * (g_pert * rho_A - Vp)
            + 4 * psid * pd
            - 3 * H * dphd
            - (kk**2 / a_**2 + Vpp) * dph
        )
        drAd = -3 * H * drA + 3 * psid * rho_A + (kk**2 / a_**2) * qm / (1 - g_bg * pb)
        qmd = -3 * H * qm - rho_phys * psi + g_pert * rho_A * dph
        return [a_ * H, pd, pdd, psid, psidd, dphd, dphdd, drAd, qmd]

    return rhs


def initial_data(g_bg, g_pert, lam, kk, psi0=1e-5, dph0=1e-6, dphd0=0.0, drA0=1e-5, phidot0=None):
    pd0 = PHIDOT if phidot0 is None else phidot0
    a0, pb0 = A3_INIT ** (1.0 / 3.0), 0.0
    b = bg_of(a0, pb0, pd0, g_bg, lam)
    H0 = b["H"]
    drho_phi0 = pd0 * dphd0 - psi0 * pd0**2 + b["Vp"] * dph0
    # the initial matter perturbation is DEFINED by the physical coupling,
    # so g_bg -- never the probe dial g_pert. See contrast().
    drho_m0 = drA0 * (1 - g_bg * pb0) - g_bg * b["rho_A"] * dph0
    psid0 = (-(kk**2 / a0**2) * psi0 - 4 * np.pi * G_N * (drho_phi0 + drho_m0)) / (
        3 * H0
    ) - H0 * psi0
    qm0 = -(psid0 + H0 * psi0) / (4 * np.pi * G_N) + pd0 * dph0
    return [a0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0, qm0]


_CACHE = {}


def run(g_bg, g_pert, lam, kk, rtol=1e-11, phidot0=None, dph0=1e-6):
    key = (g_bg, g_pert, lam, kk, rtol, phidot0, dph0)
    if key not in _CACHE:
        s = solve_ivp(
            make_system(g_bg, g_pert, lam, kk),
            (1.0, T_END),
            initial_data(g_bg, g_pert, lam, kk, dph0=dph0, phidot0=phidot0),
            rtol=rtol,
            atol=1e-20,
            dense_output=True,
        )
        assert s.success, f"integration failed: {key}"
        _CACHE[key] = s
    return _CACHE[key]


def contrast(sol, g_bg, _g_pert, lam, tv):
    """The observable's DEFINITION uses g_bg only, never g_pert.

    # THE BUG THIS FIXES was conceptual, not typographical. A first version
    # wrote `- g_pert * rho_A * dph` here. But Delta_m = drho_A*M +
    # rho_A*M'*dphi is the DEFINITION of the matter density perturbation, and
    # the M' in it belongs to the PHYSICAL coupling. g_pert is a dial on the
    # equations of motion, not on what matter IS. Letting it leak into the
    # definition made eps linear in g_pert with no dynamics at all, so
    # d eps/d g_pert did not vanish at g_hat=0 and control A2 failed --
    # correctly. The derivative would have mixed a dynamical response with a
    # definitional one, which attributes nothing.
    """
    a_, pb, pd, psi, _psid, dph, _dphd, drA, qm = sol.sol(tv)
    b = bg_of(a_, pb, pd, g_bg, lam)
    delta = drA * (1 - g_bg * pb) - g_bg * b["rho_A"] * dph - 3 * b["H"] * qm
    return delta / b["rho_phys"]


def t_of_a(sol, a_target):
    f = lambda tv: sol.sol(tv)[0] - a_target  # noqa: E731
    if f(1.0) * f(T_END) > 0:
        return None
    return brentq(f, 1.0, T_END, xtol=1e-8, rtol=1e-12)


def eps_of(g_bg, g_pert, lam, kk, a1, a2, rtol=1e-11, phidot0=None, dph0=1e-6):
    """eps against the FULLY uncoupled reference (0,0) at the same lambda."""
    out = []
    for gb, gp in ((g_bg, g_pert), (0.0, 0.0)):
        s = run(gb, gp, lam, kk, rtol=rtol, phidot0=phidot0, dph0=dph0)
        t1, t2 = t_of_a(s, a1), t_of_a(s, a2)
        if t1 is None or t2 is None:
            return None
        out.append(contrast(s, gb, gp, lam, t2) / contrast(s, gb, gp, lam, t1))
    return np.log(out[0] / out[1]) / np.log(a2 / a1)


def main() -> int:
    print("=" * 78)
    print("P80 -- constraint-preserving attribution via an ON-SHELL derivative")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    lam, GH = 1.0, 1.0
    KS = (3.0, 10.0, 30.0)
    s_ref = run(0.0, 0.0, lam, 1.0)
    A1, A2 = s_ref.sol(1e4)[0], s_ref.sol(8e7)[0]

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- CONTROLS")
    print("-" * 78)
    print("  A1 -- at g_bg == g_pert the split system must be FINDING_P76's")
    print("  system verbatim. Compare against P76's own code, not against numbers")
    print("  copied from a finding (which are rounded -- the error P78 made).")

    def eps_p76(kk):
        out = []
        for g in (GH, 0.0):
            s = p76.run(g, lam, kk, T_END, rtol=1e-11)
            t1, t2 = p76.t_of_a(s, A1, 1.0, T_END), p76.t_of_a(s, A2, 1.0, T_END)
            out.append(p76.contrast(s, g, lam, t2) / p76.contrast(s, g, lam, t1))
        return np.log(out[0] / out[1]) / np.log(A2 / A1)

    print(f"\n    {'k':<8}{'P80 (g_bg=g_pert)':<24}{'P76 original':<24}{'rel diff'}")
    worst = 0.0
    for kk in KS:
        a, b = eps_of(GH, GH, lam, kk, A1, A2), eps_p76(kk)
        d = abs(a - b) / abs(b)
        worst = max(worst, d)
        print(f"    {kk:<8}{a:<24.12f}{b:<24.12f}{d:.2e}")
    print(f"\n    => worst {worst:.2e}")
    if worst > 1e-10:
        print("    *** CONTROL FAILED: the split system is not P76's system.")
        return 1
    print("    PASSES -- the two-parameter system reduces exactly.")

    print("\n  A2 -- the leak control. THE ORIGINAL VERSION IS RETRACTED AS")
    print("  INVALID, not merely failed.")
    print()
    print("  # A2 first read: 'at g_hat = 0 the derivative must vanish, because")
    print("  # eps responds to g_pert only as source(h) x force(h) = O(h^2)'. It")
    print("  # returned 1.921e-04, then 1.924e-04, and I twice called it a bug.")
    print("  # The first diagnosis -- g_pert leaking into the observable's")
    print("  # definition -- was right on its own merits but moved A2 by 3e-07.")
    print("  # The control itself asserted FALSE PHYSICS:")
    print("  #")
    print("  #   at g_bg = 0 the BACKGROUND SCALAR IS STILL THERE (phibar_dot != 0),")
    print("  #   so  drho_A --h--> dphi --> drho_phi = phibar_dot*dphi_dot + V'*dphi")
    print("  #                          --> Psi --> delta_m")
    print("  #   is LINEAR in h. A nonzero derivative there is CORRECT.")
    print("  #")
    print("  # A second statement I was about to write here is ALSO false, and is")
    print("  # not being written: 'the pure Euler term is O(g_pert^2), so a first")
    print("  # derivative cannot see it.' True only if dphi is entirely")
    print("  # proportional to g_pert. initial_data seeds dph0 = 1e-6, so dphi has")
    print("  # a g_pert-INDEPENDENT part and g_pert*rho_A*dphi_HOM is LINEAR.")
    print("  # Measured: background scalar off -> d eps/d g_pert is exactly")
    print("  # proportional to dph0, ratio constant to 1.3e-05 across 8x in dph0.")
    print()
    print("  THE VALID CONTROL closes BOTH linear channels and demands zero:")
    print("  background scalar off (phibar_dot(1)=0 => phibar==0 => drho_phi==0)")
    print("  AND no dphi seed (dph0=0 => the Euler term is purely O(g_pert^2),")
    print("  which a central difference cancels identically).")
    h0 = 1e-3
    d_valid = (
        eps_of(0.0, h0, lam, 10.0, A1, A2, phidot0=0.0, dph0=0.0)
        - eps_of(0.0, -h0, lam, 10.0, A1, A2, phidot0=0.0, dph0=0.0)
    ) / (2 * h0)
    print(f"\n    both channels closed -> d eps/d g_pert = {d_valid:.6e}  (must be 0)")
    if abs(d_valid) > 1e-12:
        print("    *** CONTROL FAILED: a real implementation leak remains.")
        return 1
    print("    PASSES -- but read exactly what it licenses, see A2c.")
    print()
    print("  A2c -- WHAT A2 ALONE DOES *NOT* PROVE, added after review.")
    print("  A2's zero is a PARITY IDENTITY. With phibar==0 and dph0==0 the system")
    print("  is invariant under (g_pert, dphi, dphi_dot) -> (-g_pert, -dphi,")
    print("  -dphi_dot) -- verified: eps(+h) and eps(-h) agree BITWISE at h =")
    print("  1e-2, 5e-3, 2.5e-3. A central difference therefore vanishes for any")
    print("  eps that is EVEN in g_pert, so A2 can only catch a leak that is ODD.")
    print("  (The quadratic response underneath it is NOT characterised either:")
    print("  eps(h)-eps(0) reads 1.04e-08, 2.76e-11, -2.58e-09 across those h --")
    print("  sign-flipping, below the solver's floor for a quantity of size 0.046.)")
    print()
    print("  So the no-leak claim rests on this instead, which is parity-blind:")
    print("  the observable's DEFINITION must not depend on g_pert at all.")
    ic_a = initial_data(0.7, 0.0, lam, 10.0)
    ic_b = initial_data(0.7, 999.0, lam, 10.0)
    _s = run(0.7, 0.7, lam, 10.0)
    c_a = contrast(_s, 0.7, 0.0, lam, 1e5)
    c_b = contrast(_s, 0.7, 999.0, lam, 1e5)
    ic_same = all(x == y for x, y in zip(ic_a, ic_b, strict=True))
    print(f"\n    initial_data, g_pert 0.0 vs 999.0 -> bitwise identical: {ic_same}")
    print(f"    contrast,     g_pert 0.0 vs 999.0 -> bitwise identical: {c_a == c_b}")
    if not (ic_same and c_a == c_b):
        print("    *** g_pert HAS leaked into the observable's definition.")
        return 1
    print("    PASSES at every parity. NOTE this is trivially true of the source")
    print("    as written (neither function reads g_pert) -- its value is as a")
    print("    REGRESSION GUARD: it fires if anyone puts g_pert back in.")
    print()
    print("  A2b -- reopen the two channels one at a time; each must give a")
    print("  nonzero derivative, and their sizes say which one carries the effect.")
    d_seed = (
        eps_of(0.0, h0, lam, 10.0, A1, A2, phidot0=0.0)
        - eps_of(0.0, -h0, lam, 10.0, A1, A2, phidot0=0.0)
    ) / (2 * h0)
    d_bg = (eps_of(0.0, h0, lam, 10.0, A1, A2) - eps_of(0.0, -h0, lam, 10.0, A1, A2)) / (2 * h0)
    print(f"\n    + dphi seed only        -> {d_seed:.6e}  Euler force on dphi_HOM")
    print(f"    + background scalar too -> {d_bg:.6e}  adds the drho_phi channel")
    print(f"    ratio                   -> {abs(d_bg / d_seed):.0f}x")
    print("    => the scalar's own gravity dominates the g_pert response.")
    if not (abs(d_seed) > 1e-9 and abs(d_bg / d_seed) > 50):
        print("    *** A2b unexpected: the channel sizes do not match the diagnosis.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- is the derivative well-defined? (step convergence)")
    print("-" * 78)
    print("  A derivative is only a measurement if it converges as the step")
    print("  shrinks. Central differences at k=10, four step sizes:")
    print(f"\n    {'h':<12}{'d eps/d g_pert':<24}{'change vs previous'}")
    prev, conv = None, []
    for h in (1e-2, 5e-3, 2e-3, 1e-3):
        d = (eps_of(GH, GH + h, lam, 10.0, A1, A2) - eps_of(GH, GH - h, lam, 10.0, A1, A2)) / (
            2 * h
        )
        ch = "" if prev is None else f"{abs(d - prev) / abs(d):.2e}"
        if prev is not None:
            conv.append(abs(d - prev) / abs(d))
        print(f"    {h:<12.0e}{d:<24.9f}{ch}")
        prev = d
    B_OK = conv[-1] < 0.01
    print(
        f"\n    => final relative change {conv[-1]:.2e}; {'CONVERGED' if B_OK else 'NOT CONVERGED'}"
    )

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- the two channels, and whether they sum")
    print("-" * 78)
    print("  pert-sector := g_hat * d eps/d g_pert   |  on-shell")
    print("  background  := g_hat * d eps/d g_bg     |  on-shell")
    print()
    print("  The first is NOT 'the direct fifth force'. g_pert moves the dphi")
    print("  source, the scalar stress, the metric response through drho_phi AND")
    print("  the Euler force at once; the derivative sees their sum.")
    print("  Their sum is the total derivative along the physical line")
    print("  g_bg = g_pert = g_hat, so it must equal g_hat * d eps/d g_hat.")
    print("  That is a CHECK, not a definition -- if it fails, the split is not a")
    print("  decomposition of anything.")
    print()
    print("  AND THE CONVERSE IS NOT TRUE EITHER. Closure here IS the chain rule,")
    print("  which every smooth function obeys, so it can confirm the")
    print("  implementation and can NEVER establish that the two coordinates name")
    print("  two physical mechanisms. Read what follows as a SENSITIVITY split.")
    h = 1e-3
    print(f"\n    {'k':<7}{'pert-sector':<16}{'background':<16}{'sum':<16}{'total':<16}{'closure'}")
    C_OK, shares = True, {}
    for kk in KS:
        dp = (
            GH
            * (eps_of(GH, GH + h, lam, kk, A1, A2) - eps_of(GH, GH - h, lam, kk, A1, A2))
            / (2 * h)
        )
        db = (
            GH
            * (eps_of(GH + h, GH, lam, kk, A1, A2) - eps_of(GH - h, GH, lam, kk, A1, A2))
            / (2 * h)
        )
        tot = (
            GH
            * (eps_of(GH + h, GH + h, lam, kk, A1, A2) - eps_of(GH - h, GH - h, lam, kk, A1, A2))
            / (2 * h)
        )
        clo = abs(dp + db - tot) / abs(tot)
        C_OK = C_OK and clo < 0.01
        shares[kk] = dp / tot
        print(f"    {kk:<7}{dp:<16.6f}{db:<16.6f}{dp + db:<16.6f}{tot:<16.6f}{clo:.2e}")
    print(f"\n    => closure {'HOLDS' if C_OK else 'FAILS'} (threshold 1%)")
    print(f"\n    {'k':<7}{'perturbation-sector share of the derivative'}")
    for kk in KS:
        print(f"    {kk:<7}{shares[kk]:.2%}")
    print()
    print("    SCOPE: three k values, all inside the range P76/P77 showed the")
    print("    observable is well-behaved. k=1 (where P77 found the coupled")
    print("    contrast crosses zero ~160 times) and k>=100 are NOT measured here,")
    print("    so 'flat in k' means flat across 3..30 and nothing wider.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- comparison with FINDING_P77's off-shell probe")
    print("-" * 78)
    print("  P77's DELETION gave a 'direct' share of 6.61% (probe from t=1) or")
    print("  16.39% (probe from t=1e3) -- a factor 2.5 from an arbitrary choice.")
    print("  The on-shell derivative has no such choice to make.")
    print()
    print("  BUT READ THE COMPARISON CAREFULLY: THESE ARE DIFFERENT QUANTITIES.")
    print("  P77 REMOVED the Euler term entirely -- a finite, off-shell change.")
    print("  P80 measures an INFINITESIMAL sensitivity on the constraint surface.")
    print("  Nothing requires them to agree, and a gap between them is a fact")
    print("  about the two probes, not proof that either number is wrong.")
    print("  What the gap DOES kill is the claim that 6.61%..16.39% is")
    print("  protocol-independent, and with it the conclusion drawn from it --")
    print("  'this is a modified expansion history, not a force' -- which the")
    print("  constraint-preserving measure does not support.")
    print(f"\n    {'k':<7}{'on-shell pert-sector share':<28}{'P77 off-shell range'}")
    for kk in KS:
        rng = "6.61% .. 16.39%" if kk == 10.0 else "(measured at k=10 only)"
        print(f"    {kk:<7}{shares[kk]:<28.2%}{rng}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- the gap this step does NOT close, measured and left open")
    print("-" * 78)
    print("  d eps/d g_pert at g_bg = 0, as a function of eta = phibar_dot(1)")
    print("  scaled against its default. Two of three pre-registered signatures")
    print("  hold; the third fails and stays failed.")
    h0 = 1e-3
    vals = {}
    print(f"\n    {'eta':<8}{'d eps/d g_pert':<20}{'D/eta':<18}{'D(+eta)+D(-eta)'}")
    for eta in (-2.0, -1.0, -0.5, -0.25, 0.25, 0.5, 1.0, 2.0):
        pd0 = eta * PHIDOT
        vals[eta] = (
            eps_of(0.0, h0, lam, 10.0, A1, A2, phidot0=pd0)
            - eps_of(0.0, -h0, lam, 10.0, A1, A2, phidot0=pd0)
        ) / (2 * h0)
        odd = f"{vals[eta] + vals[-eta]:.3e}" if eta > 0 else ""
        print(f"    {eta:<8.2f}{vals[eta]:<20.6e}{vals[eta] / eta:<18.6e}{odd}")
    asym = max(abs(vals[e] + vals[-e]) / abs(vals[e]) for e in (0.25, 0.5, 1.0, 2.0))
    ratios = [abs(vals[e] / e) for e in vals]
    slope = np.polyfit(
        np.log([abs(e) for e in vals if e > 0]), np.log([vals[e] for e in vals if e > 0]), 1
    )[0]
    print(f"\n    ODD  -- worst |D(+)+D(-)|/|D(+)|      : {asym:.3f}   (holds)")
    print("    ZERO -- see A2/A2b above               : exact (holds)")
    print(f"    LINEAR -- D/eta spread across the sweep: {max(ratios) / min(ratios):.2f}x")
    print(f"              power law D ~ eta^{slope:.3f}          (FAILS)")
    print()
    print("  Two explanations were built for the sublinearity and BOTH failed:")
    print("    (1) 'the channel is linear in phibar_dot at the measurement epoch,")
    print("        the nonlinearity is in the seven-decade map from the IC' --")
    print("        INVALID TEST, not merely a negative one: it sampled")
    print("        phibar_dot at one instant, and by that epoch the field")
    print("        oscillates in V = lam*phi^4/4, so the four samples came back")
    print("        -4.6e-10 +8.1e-10 -8.6e-10 +9.2e-10, alternating in sign. A")
    print("        point sample measures PHASE; the claim was about AMPLITUDE.")
    print("    (2) the same claim with a matched estimator -- RMS envelope over")
    print("        the growth window in ln a. Exponents 0.390 (phibar_dot) and")
    print("        0.257 (including the V'*dphi half). Nowhere near 1.")
    print()
    print("  Recorded as an open gap. The oddness says the channel runs through")
    print("  phibar_dot, which is what A2b already established by a cleaner")
    print("  route; the amplitude scaling is not explained by anything tested.")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if B_OK and C_OK:
        print("  -> A-OK. The derivative converges and the two channels close on the")
        print("     total. The attribution is a MEASUREMENT, not a probe artifact,")
        print("     and it carries no protocol choice -- unlike FINDING_P77's, whose")
        print("     answer moved 2.5x with the probe's start time.")
        print("\n     What it says, in the only wording this test licenses: the")
        print("     PERTURBATION-SECTOR coordinate carries")
        print(
            f"     {min(shares.values()):.1%} to {max(shares.values()):.1%} of the "
            "response and the background coordinate the rest."
        )
        print("     What it does NOT say: that those are two physical mechanisms")
        print("     with those weights. Closure is the chain rule; a single M'(phi)")
        print("     drives both sourcing and force, and they may not be separable")
        print("     at all without changing the theory.")
        print()
        print("     AND IT DOES NOT CONTRADICT FINDING_P77's 6.61%..16.39%. The two")
        print("     cut the coupling in DIFFERENT PLACES. P77 deleted the Euler term")
        print("     ONLY. g_pert here sits in the perturbed KG SOURCE as well as the")
        print("     Euler term (lines 136-137 and 143), so this coordinate strictly")
        print("     CONTAINS P77's channel plus the dphi source and everything")
        print("     downstream of it. The move from ~7% to ~54% is the size of what")
        print("     P77's 'background' label was carrying that is not background")
        print("     history at all -- it is perturbation-sector physics its probe")
        print("     could not separate. P77's conclusion 'a modified expansion")
        print("     history, not a force' holds only under P77's own cut.")
    else:
        print("  -> A-DEG. The split does not behave as a decomposition:")
        if not B_OK:
            print("     the derivative does not converge with step size.")
        if not C_OK:
            print("     the two channels do not sum to the total.")
        print("     Attribution is impossible in principle in this formulation.")
        print("     Combined with FINDING_P79's W-FAIL this triggers the TZ stop")
        print("     rule -- write the null result, do not start P83.")

    print("\n  NOT ESTABLISHED:")
    print("   * that the split is unique. g_bg/g_pert is ONE way to cut the")
    print("     coupling; a different cut would attribute differently, and nothing")
    print("     here privileges this one beyond its being on-shell.")
    print("   * anything about which channel carries FINDING_P79's initial-")
    print("     condition dependence -- that needs the derivative measured under")
    print("     the lever, which is not done here.")
    print("   * anything observational. Internal units, NO_BRIDGE_FITTING in force.")
    print("   * anything about MULTING itself (Gate 1): the completion is OURS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
