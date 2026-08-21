"""P82 -- the growth rate f(a,k) = d ln delta_m / d ln a (TZ bridge 7)

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS AND NOT MORE eps.

FINDING_P76's eps is a SHIFT -- a ratio of one run's growth to another's. It is
internal by construction: it needs a reference run, and no observation gives you
one. The quantity the literature actually measures is the growth rate

    f(a,k) = d ln delta_m / d ln a

whose product with sigma8 is what redshift-space distortions constrain. f needs
no reference run. It is the first quantity in this whole arc that has the SHAPE
of an observable, even though nothing here is compared to data.

THE LOCK MASS IS EXTERNAL, WHICH IS THE POINT.

In matter domination the growing mode is delta ~ a, so f = 1. That is textbook
and owes nothing to this project -- unlike FINDING_P74's lock mass, whose target
was internal and through which a deliberately fabricated term sailed unnoticed.
P76 already used this lock mass for delta ~ a; P82 uses its LOGARITHMIC
DERIVATIVE, which is a strictly sharper test: a growth that is off by a constant
factor still passes 'delta ~ a' by eye but fails f = 1 immediately.

THE TRAP THIS FILE IS BUILT TO AVOID.

Our background is NOT pure matter domination. The scalar carries kinetic energy
and, at lambda != 0, potential energy, and both feed H. If f comes out below 1
because the scalar contributes to the expansion, that is CORRECT PHYSICS and not
a failure of the machinery -- but it would look identical to a broken pipeline.
So Omega_phi is reported alongside f at every point, and the lock mass is only
asserted where Omega_phi is demonstrably small. FINDING_P78's A3 failed falsely
for exactly this species of reason: a gate compared against the wrong thing.

PRE-REGISTERED OUTCOMES:
  F-OK    the lock mass passes where Omega_phi is small, AND f converges under
          both the solver tolerance and the differencing step -> the standard
          observable exists in our units, ready for the day bridge 5 closes.
  F-FAIL  either fails -> say so plainly; eps remains the only channel and this
          route is closed.

WHAT THIS FILE WILL NOT DO, stated before the numbers: compare f, or f*sigma8,
to any dataset. Producing f in internal units is the entire deliverable.
Comparison is bridge 10 and is blocked -- NO_BRIDGE_FITTING remains in force.
"""

import importlib.util
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location(
    "p76_ref", os.path.join(_HERE, "P76_growth_observable.py")
)
p76 = importlib.util.module_from_spec(_sp)
sys.modules["p76_ref"] = p76
_sp.loader.exec_module(p76)

G_N = p76.G_N
LAM = 1.0
T_END = 1e8  # same span P76 integrates to


def state_at(sol, g_hat, lam, t):
    """delta_m (the CONTRAST), a, and the scalar's energy fraction, at one time."""
    a_, pb, pd = sol.sol(t)[0], sol.sol(t)[1], sol.sol(t)[2]
    b = p76.bg_quantities(a_, pb, pd, g_hat, lam)
    rho_phi = pd**2 / 2.0 + lam * pb**4 / 4.0
    omega_phi = rho_phi / (b["rho_phys"] + rho_phi)
    return {
        "a": a_,
        "delta": p76.contrast(sol, g_hat, lam, t),
        "omega_phi": omega_phi,
    }


def growth_rate(sol, g_hat, lam, t, dlnt=1e-3):
    """f = d ln delta / d ln a by a central difference in ln t.

    # WHY in ln t and not ln a: t is the integration variable, so stepping it is
    # exact, while stepping a would need a(t) inverted twice per evaluation and
    # would put the root-finder's tolerance inside the derivative.
    """
    tm, tp = t * np.exp(-dlnt), t * np.exp(dlnt)
    sm, sp = state_at(sol, g_hat, lam, tm), state_at(sol, g_hat, lam, tp)
    dln_delta = np.log(sp["delta"] / sm["delta"])
    dln_a = np.log(sp["a"] / sm["a"])
    return dln_delta / dln_a


def raw_growth_rate(sol, g_hat, lam, t, dlnt=1e-3):
    """Same, but on the RAW Delta_m instead of the contrast -- the negative control.

    Delta_m = delta * rho_phys ~ delta * a^-3, so this must come out near f-3.
    If it does NOT, the lock mass cannot tell the right quantity from the wrong
    one and is not a test.
    """

    def raw(tv):
        a_, pb, pd = sol.sol(tv)[0], sol.sol(tv)[1], sol.sol(tv)[2]
        b = p76.bg_quantities(a_, pb, pd, g_hat, lam)
        return p76.contrast(sol, g_hat, lam, tv) * b["rho_phys"], a_

    tm, tp = t * np.exp(-dlnt), t * np.exp(dlnt)
    dm, am = raw(tm)
    dp, ap = raw(tp)
    return np.log(dp / dm) / np.log(ap / am)


def main() -> int:
    print("=" * 78)
    print("P82 -- the growth rate f(a,k) = d ln delta_m / d ln a")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    KS = [3.0, 10.0, 30.0]
    TS = [1e4, 1e5, 1e6, 1e7, 8e7]

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- LOCK MASS (external): f -> 1 in matter domination at g_hat=0")
    print("-" * 78)
    print("  Textbook, not generated by this project. Reported WITH Omega_phi,")
    print("  because our background is not pure matter domination and f below 1")
    print("  where the scalar still carries energy is correct physics, not a")
    print("  broken pipeline. The lock mass is asserted only where Omega_phi is")
    print("  demonstrably small.")

    s0 = p76.run(0.0, LAM, 10.0, T_END)
    print(f"\n    {'t':<12}{'a':<16}{'Omega_phi':<16}{'f':<14}{'f-1'}")
    lock_pts = []
    for t in TS:
        st = state_at(s0, 0.0, LAM, t)
        f = growth_rate(s0, 0.0, LAM, t)
        lock_pts.append((st["omega_phi"], f))
        print(f"    {t:<12.1e}{st['a']:<16.6g}{st['omega_phi']:<16.3e}{f:<14.9f}{f - 1:+.3e}")

    small = [(o, f) for o, f in lock_pts if o < 1e-3]
    print(f"\n    points with Omega_phi < 1e-3 : {len(small)} of {len(lock_pts)}")
    if not small:
        print("    *** cannot assert the lock mass -- the scalar never becomes")
        print("    negligible on this span, so f=1 is not the right expectation.")
        return 1
    worst = max(abs(f - 1.0) for _, f in small)
    print(f"    worst |f-1| among those      : {worst:.3e}")
    L1 = worst < 1e-3
    print(f"    LOCK MASS {'PASSES' if L1 else 'FAILS'} (threshold 1e-3)")
    if not L1:
        print("    -> F-FAIL. The machinery does not reproduce the textbook value.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- NEGATIVE CONTROL: the lock mass must be able to FAIL")
    print("-" * 78)
    print("  Same pipeline on the RAW Delta_m instead of the contrast. Since")
    print("  Delta_m = delta*rho_phys ~ delta*a^-3, this must land near f-3 = -2.")
    print("  A lock mass that passes on both quantities is not a test -- the")
    print("  lesson of P76's hardcoded column and of P77's non-discriminating")
    print("  pole test.")
    print(f"\n    {'t':<12}{'f (contrast)':<18}{'f (raw Delta_m)':<20}{'difference'}")
    diffs = []
    for t in TS:
        fc = growth_rate(s0, 0.0, LAM, t)
        fr = raw_growth_rate(s0, 0.0, LAM, t)
        diffs.append(fc - fr)
        print(f"    {t:<12.1e}{fc:<18.9f}{fr:<20.9f}{fc - fr:+.6f}")
    near3 = all(abs(d - 3.0) < 1e-2 for d in diffs)
    print(f"\n    difference is 3.00 at every point: {near3}")
    print(
        f"    NEGATIVE CONTROL {'PASSES' if near3 else 'FAILS'}"
        " -- the gate distinguishes the two quantities."
    )
    if not near3:
        print("    *** the lock mass cannot tell the right quantity from the wrong")
        print("    one, so its PASS above carries no information. F-FAIL.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- CONVERGENCE in both knobs that could fake a value")
    print("-" * 78)
    print("  C1 -- the differencing step. f is a finite difference, so it must")
    print("  stop moving as the step shrinks.")
    print(f"\n    {'dlnt':<12}{'f at t=1e6, k=10':<24}{'change vs previous'}")
    prev, c1_last = None, None
    for d in (1e-2, 3e-3, 1e-3, 3e-4, 1e-4):
        f = growth_rate(s0, 0.0, LAM, 1e6, dlnt=d)
        ch = "" if prev is None else f"{abs(f - prev):.3e}"
        print(f"    {d:<12.1e}{f:<24.12f}{ch}")
        if prev is not None:
            c1_last = abs(f - prev)
        prev = f
    C1 = c1_last is not None and c1_last < 1e-6
    print(f"\n    C1 {'CONVERGED' if C1 else 'NOT CONVERGED'} (last change < 1e-6)")

    print("\n  C2 -- the solver tolerance. If f tracks rtol it belongs to the")
    print("  integrator, not to the model.")
    print(f"\n    {'rtol':<12}{'f at t=1e6, k=10':<24}{'shift vs rtol=1e-11'}")
    ref = None
    c2_worst = 0.0
    for rt in (1e-8, 1e-9, 1e-10, 1e-11, 1e-12):
        s = p76.run(0.0, LAM, 10.0, T_END, rtol=rt)
        f = growth_rate(s, 0.0, LAM, 1e6)
        if rt == 1e-11:
            ref = f
        print(f"    {rt:<12.0e}{f:<24.12f}" + ("" if ref is None else f"{f - ref:+.3e}"))
    for rt in (1e-8, 1e-9, 1e-10, 1e-12):
        s = p76.run(0.0, LAM, 10.0, T_END, rtol=rt)
        c2_worst = max(c2_worst, abs(growth_rate(s, 0.0, LAM, 1e6) - ref))
    C2 = c2_worst < 1e-6
    print(f"\n    worst shift across four decades of rtol: {c2_worst:.3e}")
    print(
        f"    C2 {'PASSES' if C2 else 'FAILS'} -- f {'does not' if C2 else 'DOES'}"
        " track the solver."
    )

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- the deliverable: f(a,k) with the coupling on")
    print("-" * 78)
    print("  This is the number bridge 7 asks for. It is in INTERNAL UNITS and")
    print("  is compared to nothing -- comparison is bridge 10 and is blocked.")
    for kk in KS:
        sc = p76.run(1.0, LAM, kk, T_END)
        print(f"\n    k = {kk:g}")
        print(f"      {'t':<12}{'a':<14}{'Omega_phi':<14}{'f (g=1)':<14}{'f (g=0)':<14}{'delta f'}")
        for t in TS:
            st = state_at(sc, 1.0, LAM, t)
            f1 = growth_rate(sc, 1.0, LAM, t)
            f0 = growth_rate(p76.run(0.0, LAM, kk, T_END), 0.0, LAM, t)
            print(
                f"      {t:<12.1e}{st['a']:<14.6g}{st['omega_phi']:<14.3e}"
                f"{f1:<14.9f}{f0:<14.9f}{f1 - f0:+.6e}"
            )

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if L1 and near3 and C1 and C2:
        print("  -> F-OK. The external lock mass passes where the scalar is")
        print("     negligible, the negative control shows the gate can fail, and")
        print("     f converges in both the differencing step and the solver")
        print("     tolerance. The standard growth observable exists in our units.")
    else:
        print("  -> F-FAIL. Details above. eps remains the only channel.")

    print("\n  NOT ESTABLISHED:")
    print("   * anything observational. f is in INTERNAL units and is compared")
    print("     to no dataset. NO_BRIDGE_FITTING in force; bridge 10 is blocked.")
    print("   * that f is the RIGHT observable for this completion -- only that")
    print("     it is computable and well-behaved in it.")
    print("   * anything about MULTING itself (Gate 1): the completion is OURS.")
    print("   * Perelman condition 5 (external reconstruction) -- still not met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
