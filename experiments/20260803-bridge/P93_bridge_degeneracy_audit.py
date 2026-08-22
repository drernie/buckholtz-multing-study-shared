"""P93 -- does the bridge for eps(k) actually need only ONE external number?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P84 established: eps and f are invariant under the campaign's full
scaling group, and k is not -- the bridge for eps(k) costs exactly ONE external
number, "the physical value of a*H at one reference epoch". FINDING_P85/P86
extended this: the t->z mapping is free, and the reference epoch can be defined
by adding a dark-energy term tuned so that Omega_Lambda = 0.7 there -- "a
DEFINITION of the reference epoch, never a value imported from data".

THIS FILE STARTED AS THE NUMERIC BRIDGE STEP -- plug in a real H_0 (Planck 2018,
67.4 km/s/Mpc, arXiv:1807.06209) and quote eps(k) in h/Mpc. Working the unit
algebra through by hand first (Structure-Bias Guard: reasoning in prose before
any code) surfaced something P86's own language had already half-admitted but
neither P84 nor P86 drew out: P86's lambda_for(a_today, frac=0.7) sets Lambda AS
A FUNCTION OF a_today so that Omega_Lambda(a_today) = 0.7 EXACTLY AT WHATEVER
a_today YOU HAND IT. That is not a condition that PICKS a_today -- it is
satisfied by construction for every a_today you could name. So "Omega_Lambda=0.7
today" does not, by itself, tell you WHICH internal epoch is "today". It fixes
Lambda relative to an already-chosen epoch; it does not choose the epoch.

WHY THIS MATTERS FOR THE COUNT OF EXTERNAL NUMBERS. If a_today is genuinely
free -- if the internal a*H value at "the Omega_Lambda=0.7 epoch" differs
substantially depending on which a_today you started from -- then P84's "one
external number" undercounts what plugging in a real H_0 requires: you would
ALSO need something that breaks this degeneracy (e.g. a real Omega_m at that
epoch, not just Omega_Lambda + Omega_m summing to something because a_today was
already picked). This is checked here rather than assumed, before any k -> h/Mpc
number is quoted, because an audit that misses a degeneracy in the reference
epoch would let ANY choice look like "the" bridge -- exactly the trap Gate 2
(Target Provenance) exists to catch: a fit dressed as a derivation.

PRE-REGISTERED OUTCOMES:
  A1  Omega_Lambda(a_today) = 0.7 to numerical precision, independent of which
      a_today is handed to lambda_for. This is EXPECTED given lambda_for's own
      algebra (rho_m*0.7/0.3, chosen so Omega_Lambda comes out to 0.7 BY
      CONSTRUCTION) -- checked as a control, not a discovery, because a check
      that always passes trivially by definition is not informative unless
      confirmed to actually hold in the running code, not just the formula.
  A2  DEGENERATE   the internal (a*H) at the Omega_Lambda=0.7 epoch VARIES
                    substantially (order-1 or more) across the tested a_today
                    range -> P84's external-number count undercounts what a real
                    H_0-based bridge needs; at least one more external anchor
                    (e.g. a physical Omega_m today) is required, and this file
                    STOPS without quoting any k[h/Mpc] number.
      NOT-DEGENERATE  (a*H) is nearly constant across a_today choices -> the
                    degeneracy is not physically consequential and P84's count
                    stands; a follow-up step may proceed to the numeric mapping.

WHAT THIS FILE DOES NOT DO: it does not quote eps(k) in h/Mpc. If A2 comes back
DEGENERATE, doing so would be fitting a free parameter (the epoch choice) to
whatever answer looks reasonable -- precisely NO_BRIDGE_FITTING under a
different name. Gate 2 (Target Provenance) requires knowing whether a claim is
a prediction, a fit, or an illustration BEFORE building it; this file exists to
answer that question for the epoch choice, not to route around it.

SOURCE FOR H_0, cited but NOT YET USED (kept here for the follow-up step this
file's verdict gates): Planck 2018 results VI, base-LCDM,
H_0 = 67.4 +/- 0.5 km/s/Mpc. arXiv:1807.06209.
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


p86 = _load("P86_dark_energy_through_p81_gate.py", "p86_for_bridge")
p81 = _load("P81_background_viability.py", "p81_for_bridge")

G_N, C_MATTER = p81.G_N, p81.C_MATTER
GH, LAM = 1.0, 1.0  # the campaign's standard working point, coupling on
A_TODAY_CANDIDATES = (1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6)


def omega_lambda_at(a_today, frac=0.7):
    """Omega_Lambda AT a_today, using P86's own lambda_for and P81's bg_quantities.

    # WHY recomputed here rather than trusted from lambda_for's docstring: the
    # docstring says what the formula is FOR, not that the running code hits it
    # exactly at every a_today tried. A1 exists to verify that, not assume it.
    """
    lam_cc = p86.lambda_for(a_today, frac)
    # background H^2 needs phibar and phibar_dot at a_today; obtained by running
    # the coupled background to a_today and reading them off, not assumed zero.
    s = p81.solve_ivp(
        p81.background_rhs(GH, LAM, lam_cc),
        (p81.T0, p81.T_END),
        [p81.A3_INIT ** (1.0 / 3.0), 0.0, p81.PHIDOT],
        rtol=1e-10,
        atol=1e-22,
        dense_output=True,
    )
    if not s.success:
        return None, None, None
    # locate t such that a(t) = a_today, by direct search on the dense solution
    from scipy.optimize import brentq

    def f(t):
        return s.sol(t)[0] - a_today

    t_lo, t_hi = p81.T0, p81.T_END
    if f(t_lo) * f(t_hi) > 0:
        return None, None, None
    t_star = brentq(f, t_lo, t_hi, xtol=1e-6, rtol=1e-12)
    a_, pb, pd = s.sol(t_star)
    rho_A = C_MATTER / a_**3
    rho_phys = rho_A * (1.0 - GH * pb)
    Vtot = LAM * pb**4 / 4.0 + lam_cc
    H2 = (8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + Vtot)
    if H2 <= 0:
        return None, None, None
    H = np.sqrt(H2)
    omega_lam = lam_cc / (rho_phys + pd**2 / 2.0 + Vtot)
    return omega_lam, H, a_ * H


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P93 -- degeneracy audit: does Omega_Lambda=0.7 pin down a_today?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n" + "-" * 78)
    print("A1 -- is Omega_Lambda(a_today) = 0.7 EXACTLY, for every a_today tried?")
    print("-" * 78)
    print("  Expected by construction (lambda_for chooses Lambda for this), but")
    print("  checked in the RUNNING CODE rather than trusted from the formula.")
    print(f"\n    {'a_today':<12}{'Lambda':<16}{'Omega_Lambda':<16}{'H (internal)':<16}{'a*H'}")
    rows = []
    for a_today in A_TODAY_CANDIDATES:
        om, H, aH = omega_lambda_at(a_today)
        if om is None:
            print(f"    {a_today:<12.4g}{'not measured (unresolved)':<48}")
            continue
        rows.append((a_today, om, H, aH))
        lam_cc = p86.lambda_for(a_today, 0.7)
        print(f"    {a_today:<12.4g}{lam_cc:<16.6e}{om:<16.9f}{H:<16.6e}{aH:.6e}")

    if not rows:
        print("\n  -> NOT MEASURABLE. Infrastructure outcome, not evidence either way.")
        return 1

    worst_om = max(abs(r[1] - 0.7) for r in rows)
    A1 = worst_om < 1e-6
    print(f"\n    worst |Omega_Lambda - 0.7| = {worst_om:.3e}  =>  A1 {'HOLDS' if A1 else 'FAILS'}")
    if not A1:
        print("    *** Omega_Lambda=0.7 is NOT exact at every a_today -- lambda_for")
        print("    *** does not do what its docstring claims. Stop here.")
        return 1

    print("\n" + "-" * 78)
    print("A2 -- does the internal (a*H) at that epoch VARY with the a_today choice?")
    print("-" * 78)
    print("  If Omega_Lambda=0.7 is satisfied identically at every a_today (A1),")
    print("  but a*H differs substantially across those a_today, then 'Omega_Lambda")
    print("  = 0.7 today' has NOT picked a unique epoch -- it is compatible with a")
    print("  whole FAMILY of epochs with different physical expansion rates, and")
    print("  quoting any ONE of them as 'today' would be an unstated choice.")
    aH_vals = [r[3] for r in rows]
    print(f"\n    {'a_today':<12}{'a*H (internal)':<18}{'ratio to a_today=1e5'}")
    ref = next((r[3] for r in rows if abs(r[0] - 1e5) < 1), aH_vals[len(aH_vals) // 2])
    for a_today, _om, _H, aH in rows:
        print(f"    {a_today:<12.4g}{aH:<18.6e}{aH / ref:.4g}")
    spread = max(aH_vals) / min(aH_vals)
    print(f"\n    max/min spread of a*H across the a_today ladder: {spread:.4g}x")
    print("    (order-1 or less would mean the choice barely matters; large means")
    print("     it matters a great deal -- this is the falsifiable question)")

    DEGENERATE = spread > 3.0

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if DEGENERATE:
        print(f"  -> DEGENERATE. a*H spans {spread:.3g}x across a_today choices that")
        print("     ALL satisfy Omega_Lambda=0.7 exactly. 'Omega_Lambda=0.7 today' by")
        print("     itself does NOT pick a unique reference epoch -- it fixes Lambda")
        print("     RELATIVE TO an already-chosen epoch, not the epoch itself.")
        print()
        print("     CONSEQUENCE: FINDING_P84's 'one external number' undercounts what")
        print("     a real H_0-based bridge needs. Breaking this degeneracy requires")
        print("     AT LEAST ONE MORE physical anchor -- e.g. a measured Omega_m today,")
        print("     used TOGETHER with H_0, not Omega_Lambda=0.7 alone. FINDING_P86's")
        print("     own language ('a DEFINITION of the reference epoch') already")
        print("     half-admitted this was a convention rather than a measurement; this")
        print("     file shows the convention does not even pin a UNIQUE epoch.")
        print()
        print("     NO k[h/Mpc] NUMBER IS QUOTED. Doing so now would mean choosing one")
        print("     a_today from the degenerate family and calling it 'the' bridge --")
        print("     a fit dressed as a derivation, exactly what Gate 2 exists to catch.")
    else:
        print(f"  -> NOT-DEGENERATE. a*H spread is only {spread:.3g}x across the ladder.")
        print("     The choice of a_today barely matters. FINDING_P84's count of ONE")
        print("     external number stands, and a follow-up step may plug in the real")
        print("     H_0 (Planck 2018, 67.4 km/s/Mpc, arXiv:1807.06209) to quote eps(k)")
        print("     in h/Mpc.")

    print("\n  NOT ESTABLISHED:")
    print("   * any numeric value of eps(k) in physical units -- gated on this verdict.")
    print("   * whether Omega_m=0.3 (or any specific value) is the right SECOND anchor")
    print("     if DEGENERATE -- only that one is needed.")
    print("   * anything about MULTING itself (Gate 1). Anything about NO_BRIDGE_FITTING")
    print("     beyond what is stated here -- no dataset and no Table A1 quantity enters")
    print("     this file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
