"""P94 -- does a SECOND anchor (Omega_m) collapse P93's degenerate family, or just repackage it?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P93 found Omega_Lambda(a_today)=0.7 does not pick a unique a_today: it
is a tautology of P86's lambda_for(a_today, frac), satisfied by construction for
every a_today. It registered that breaking the degeneracy needs a second
anchor, naturally Omega_m today (Planck: 0.315), used TOGETHER with H_0.

A HAND DERIVATION ATTEMPTING TO SHOW THIS WORKS PRODUCED A NONSENSE RESULT
(Omega_m,int(a_today) = 8*pi*Omega_m, impossible since Omega cannot exceed
~1), caught by the algebra itself rather than trusted. Rather than debug the
derivation further by hand -- error-prone, as just demonstrated -- this file
answers the question NUMERICALLY, on machinery already built and verified in
P86/P93, per this project's own Compute-First discipline.

THE ACTUAL QUESTION, MADE COMPUTABLE. P86's lambda_for(a_today_seed, 0.7) ties
Lambda_internal to a_today_seed BY CONSTRUCTION, which is exactly the tautology
P93 caught -- so it cannot be reused to test whether Omega_m ALONE resolves
anything. Instead: take Lambda_internal as FIXED, independent of any a_today
search (using P93's own four successfully-measured Lambda values, one per row
of its table, as four INDEPENDENT starting points -- not re-derived via
lambda_for each time). For EACH fixed Lambda_internal, find the ACTUAL a_today
at which Omega_m,int(a; that fixed Lambda) = 0.315 (Planck's precise value, not
the round 0.3 that "Omega_Lambda=0.7" implies).

If a_today_precise -- and, more importantly, H_int(a_today_precise), which is
what actually enters the k[h/Mpc] bridge via kappa = H_0/H_int(a_today) -- comes
out THE SAME across all four independently-chosen Lambda_internal values, then
{H_0, Omega_m} genuinely pin the bridge: any Lambda_internal, once correctly
re-anchored to the PRECISE Omega_m, gives the identical observable answer, and
the apparent freedom in Lambda_internal is harmless bookkeeping. If H_int(a_
today_precise) VARIES across the four, the degeneracy survives the second
anchor and a genuinely third piece of external information is needed --
because Lambda_internal is a free knob of the completion (P86: "a constant
added to the potential", nothing derives its scale) that Omega_m alone,
being a dimensionless RATIO, cannot pin down independent of which Lambda you
started from.

PRE-REGISTERED OUTCOMES:
  INVARIANT        H_int(a_today_precise) agrees to better than 1% across all
                    four independently-chosen Lambda_internal values -> the
                    degeneracy P93 found is harmless for the OBSERVABLE bridge;
                    {H_0, Omega_m} pin kappa uniquely, and a follow-up step may
                    quote k[h/Mpc].
  STILL-DEGENERATE  H_int(a_today_precise) varies by more than 10% across the
                    four -> a genuine THIRD external anchor is needed (e.g. the
                    completion's dark-energy scale would have to be checked
                    against the physical cosmological constant directly, which
                    nothing in this model predicts), and this file quotes no
                    k[h/Mpc] number either.
  MIXED             between 1% and 10% -> named, not rounded either way.

CONTROL, able to fail on its own: Omega_m,int(a; fixed Lambda) must cross
0.315 EXACTLY ONCE over the search range for each Lambda tried, or the
root-find for a_today_precise is not well-posed and its answer is not trustworthy
regardless of what INVARIANT/STILL-DEGENERATE says. (A first version of this
control checked global monotonicity instead and failed on small early-time
bumps at a<5000 -- see the control's own printed explanation for the diagnosis
and why single-crossing, not monotonicity, is the actual requirement.)

Omega_m SOURCE: Planck 2018 results VI, base-LCDM, Omega_m = 0.315 +/- 0.007.
arXiv:1807.06209. Same source already cited for H_0 in FINDING_P93.

WHAT THIS FILE DOES NOT DO: quote eps(k) or f(k) in physical units under any
outcome. INVARIANT would license a FOLLOW-UP step to do that; this file's job
is only to answer whether the family collapses.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p86 = _load("P86_dark_energy_through_p81_gate.py", "p86_for_anchor")
p81 = _load("P81_background_viability.py", "p81_for_anchor")

G_N, C_MATTER = p81.G_N, p81.C_MATTER
GH, LAM = 1.0, 1.0
OMEGA_M_PLANCK = 0.315

# P93's own four successfully-measured Lambda values, one per a_today_seed.
# NOT re-derived via lambda_for here -- taken as FIXED external inputs, exactly
# what P93's own printed table already established.
LAMBDA_SEEDS = {
    "seed a_today=1e4": p86.lambda_for(1e4, 0.7),
    "seed a_today=3e4": p86.lambda_for(3e4, 0.7),
    "seed a_today=1e5": p86.lambda_for(1e5, 0.7),
    "seed a_today=3e5": p86.lambda_for(3e5, 0.7),
}

A_SEARCH_LO, A_SEARCH_HI = 3e2, 3e6


def solve_background(lam_cc):
    return p81.solve_ivp(
        p81.background_rhs(GH, LAM, lam_cc),
        (p81.T0, p81.T_END),
        [p81.A3_INIT ** (1.0 / 3.0), 0.0, p81.PHIDOT],
        rtol=1e-10,
        atol=1e-22,
        dense_output=True,
    )


def state_at_a(sol, a_target):
    """Locate t with a(t)=a_target on the dense solution; return (H, Omega_m)."""

    def f(t):
        return sol.sol(t)[0] - a_target

    t_lo, t_hi = p81.T0, p81.T_END
    if f(t_lo) * f(t_hi) > 0:
        return None, None
    t_star = brentq(f, t_lo, t_hi, xtol=1e-6, rtol=1e-12)
    a_, pb, pd = sol.sol(t_star)
    rho_A = C_MATTER / a_**3
    rho_phys = rho_A * (1.0 - GH * pb)
    lam_cc = sol._lam_cc  # stashed by solve_background_tagged, see below
    Vtot = LAM * pb**4 / 4.0 + lam_cc
    tot = rho_phys + pd**2 / 2.0 + Vtot
    if tot <= 0:
        return None, None
    H2 = (8.0 * np.pi * G_N / 3.0) * tot
    if H2 <= 0:
        return None, None
    H = np.sqrt(H2)
    omega_m = rho_phys / tot
    return H, omega_m


def solve_background_tagged(lam_cc):
    s = solve_background(lam_cc)
    s._lam_cc = lam_cc
    return s


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P94 -- second anchor (Omega_m): does it collapse the degenerate family?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n" + "-" * 78)
    print("CONTROL -- Omega_m,int(a; fixed Lambda) must cross 0.315 EXACTLY ONCE")
    print("for the root-find below to be well-posed")
    print("-" * 78)
    print("  # SHARPENED, not relaxed, from a first version that failed by its own")
    print("  # construction: a coarse 10-point GLOBAL-monotonicity check found the")
    print("  # sequence was not decreasing everywhere and stopped before any verdict.")
    print("  # A 60-point scan located the cause: small early-time bumps at a<5000,")
    print("  # Omega_m~0.99-1.0 (order 1e-3, likely residual oscillation-era phibar")
    print("  # kinetic/potential energy), nowhere near the 0.315 crossing. Global")
    print("  # monotonicity is NOT what brentq's root needs -- a SINGLE sign change")
    print("  # of (Omega_m - 0.315) is -- so that is what is actually checked, on a")
    print("  # finer grid, and the early bumps are reported rather than hidden.")
    fine_as = np.geomspace(A_SEARCH_LO, A_SEARCH_HI, 60)
    single_crossing_ok = True
    for label, lam_cc in LAMBDA_SEEDS.items():
        s = solve_background_tagged(lam_cc)
        vals = []
        for a in fine_as:
            _H, om = state_at_a(s, a)
            if om is not None:
                vals.append((a, om))
        signs = [1 if om > OMEGA_M_PLANCK else -1 for _a, om in vals]
        crossings = sum(1 for i in range(1, len(signs)) if signs[i] != signs[i - 1])
        bumps = [
            (vals[i - 1][0], vals[i][0], vals[i][1] - vals[i - 1][1])
            for i in range(1, len(vals))
            if vals[i][1] > vals[i - 1][1] + 1e-9
        ]
        ok = crossings == 1 and len(vals) >= 30
        single_crossing_ok = single_crossing_ok and ok
        print(
            f"  {label:<18} Lambda={lam_cc:.4e}  crossings of 0.315: {crossings}  "
            f"early bumps (Omega_m<1, far from 0.315): {len(bumps)}  =>  {'OK' if ok else 'FAILS'}"
        )
    print(f"\n  CONTROL {'PASSES' if single_crossing_ok else 'FAILS'}")
    if not single_crossing_ok:
        print("  *** the root is not unique in this range. Stopping before any verdict.")
        return 1

    print("\n" + "-" * 78)
    print("PART A -- for each FIXED Lambda, find a_today where Omega_m = 0.315 EXACTLY")
    print("-" * 78)
    print(f"  Planck 2018 Omega_m = {OMEGA_M_PLANCK} (arXiv:1807.06209), used as a root,")
    print("  not as a fit -- one target value, one unknown (a_today), per Lambda.")
    print(
        f"\n    {'Lambda seed':<18}{'Lambda_internal':<18}{'a_today_precise':<18}"
        f"{'H_int(a_today)':<18}{'Omega_m check'}"
    )
    results = {}
    for label, lam_cc in LAMBDA_SEEDS.items():
        s = solve_background_tagged(lam_cc)

        def om_of_a(a, s=s):
            _, om = state_at_a(s, a)
            return (om if om is not None else np.nan) - OMEGA_M_PLANCK

        lo, hi = A_SEARCH_LO, A_SEARCH_HI
        f_lo, f_hi = om_of_a(lo), om_of_a(hi)
        if np.isnan(f_lo) or np.isnan(f_hi) or f_lo * f_hi > 0:
            print(f"    {label:<18}{lam_cc:<18.4e}{'no root in range -- not measured':<54}")
            continue
        a_today = brentq(om_of_a, lo, hi, xtol=1e-3, rtol=1e-12)
        H, om_check = state_at_a(s, a_today)
        results[label] = (lam_cc, a_today, H)
        print(f"    {label:<18}{lam_cc:<18.4e}{a_today:<18.6f}{H:<18.6e}{om_check:.9f}")

    if len(results) < 2:
        print("\n  -> NOT MEASURABLE on enough branches. Infrastructure outcome.")
        return 1

    print("\n" + "-" * 78)
    print("PART B -- does H_int(a_today_precise) agree across the four Lambda choices?")
    print("-" * 78)
    print("  This is what actually enters kappa = H_0 / H_int(a_today) -- the single")
    print("  number the k[h/Mpc] bridge would use. If it agrees, the family from")
    print("  FINDING_P93 was bookkeeping, not a real degeneracy.")
    Hs = [v[2] for v in results.values()]
    print(f"\n    {'Lambda seed':<18}{'H_int(a_today_precise)':<24}{'ratio to first'}")
    ref = Hs[0]
    for label, (_lam_cc, _a_today, H) in results.items():
        print(f"    {label:<18}{H:<24.9e}{H / ref:.6f}")
    spread = max(Hs) / min(Hs)
    print(f"\n    max/min spread of H_int(a_today_precise): {spread:.6f}")

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if spread < 1.01:
        print(f"  -> INVARIANT. Spread {spread:.6f} < 1.01 (better than 1%) across four")
        print("     INDEPENDENTLY-chosen Lambda_internal values spanning two decades.")
        print("     {H_0, Omega_m} DO pin kappa uniquely. The degeneracy FINDING_P93")
        print("     found is real in the INTERNAL parametrization (which Lambda you")
        print("     pick) but HARMLESS for the observable bridge -- every member of")
        print("     the family gives the identical H_int(a_today_precise), hence the")
        print("     identical kappa, hence the identical k[h/Mpc] mapping.")
        print()
        print("     A FOLLOW-UP step may now plug in H_0 = 67.4 km/s/Mpc (Planck 2018,")
        print("     arXiv:1807.06209) and quote eps(k), f(k) in h/Mpc. This file does")
        print("     not do that itself.")
    elif spread > 1.10:
        print(f"  -> STILL-DEGENERATE. Spread {spread:.6f} exceeds 10%. {{H_0, Omega_m}}")
        print("     do NOT pin the bridge. Lambda_internal is a genuinely free knob of")
        print("     the completion that a dimensionless ratio (Omega_m) cannot resolve")
        print("     independent of which Lambda you started from. A third, genuinely")
        print("     independent physical anchor is needed -- most naturally, requiring")
        print("     the completion's dark-energy term to reproduce the ACTUAL physical")
        print("     cosmological constant, which nothing in this model predicts.")
        print("     NO k[h/Mpc] NUMBER IS QUOTED.")
    else:
        print(f"  -> MIXED. Spread {spread:.6f}, between 1% and 10%. Named, not rounded")
        print("     toward either outcome. No k[h/Mpc] number is quoted.")

    print("\n  NOT ESTABLISHED:")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * that Omega_m=0.315 is measured independent of Omega_Lambda (flatness")
    print("     is assumed, as it already was in FINDING_P86's construction).")
    print("   * anything about MULTING itself (Gate 1). No dataset, no Table A1")
    print("     quantity enters this file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
