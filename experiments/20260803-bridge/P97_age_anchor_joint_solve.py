"""P97 -- does the AGE of the universe, a structurally different anchor, resolve the degeneracy?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P96 confirmed that relaxing Omega_m/Omega_Lambda to Planck's own
tolerance opens a per-Lambda window (Q1) but leaves the cross-Lambda spread in
H_int completely unchanged (Q2, 31.6x -> 31.9x, 1% wider not narrower). It
registered why: a ratio-type anchor at a SINGLE epoch fixes composition, never
the absolute scale of Lambda_internal. The registered next candidate was the
age of the universe -- an INTEGRAL over the full expansion history, sensitive
to Lambda's influence across the ENTIRE trajectory rather than at one instant.

THE PHYSICAL QUANTITY, DERIVED CAREFULLY BEFORE ANY CODE. H = d(ln a)/dt, and
ln(a) is the SAME dimensionless quantity in internal or physical description
(additive rescaling of a drops out of the derivative) -- only t's own unit
convention differs (FINDING_P84's S2: t -> alpha*t). So if physical time =
tau * internal time for a single constant tau, then H_physical = H_internal /
tau, i.e. tau = H_internal(a_today) / H_0_physical. The AGE at a_today is then

    physical_age [Gyr] = t_internal(a_today) * H_internal(a_today) * HubbleTimeGyr(H_0)

where HubbleTimeGyr(H_0) = 977.79 / H_0[km/s/Mpc] is a PURE UNIT CONVERSION
(Mpc-to-km and Gyr-to-seconds, both exact, not measured cosmological data --
verified via WebSearch this session: 3.0857e19 km/Mpc, 3.156e16 s/Gyr, giving
977.79/100 = 9.778 Gyr at H_0=100, the standard textbook figure). t_internal
is READ DIRECTLY off the already-solved trajectory -- P94/P95's own
background solve already computes it internally via brentq to locate a_today;
this file is the first to actually KEEP that value rather than discard it.

t_0 = 13.787 +/- 0.020 Gyr, Planck 2018 results VI, base-LCDM, arXiv:1807.06209
(same source as H_0=67.4, Omega_m=0.315 used throughout this bridge arc,
verified via WebSearch this session, not trusted from memory).

CONTROL BEFORE ANY JOINT SOLVE: in DEEP matter domination (Lambda and the
scalar both negligible), the age-Hubble-time ratio t*H has the EXACT textbook
value 2/3 (age = 2/(3H) for pure matter, a well-known analytic EdS result,
external to this project and to anything already used in this campaign). This
is checked at small a, BEFORE trusting the ratio's more complex behaviour near
a_today, exactly as FINDING_P85's own w_eff control checked EdS at small a
before trusting the coupled trajectory.

METHOD: the SAME nested root-finding architecture as FINDING_P95, with the
inner root UNCHANGED (Omega_m,int(a;Lambda)=0.315, FINDING_P94's own root) and
the OUTER target replaced: g(Lambda) := physical_age(inner_a(Lambda); Lambda)
- 13.787. A root of g(Lambda) gives a (Lambda, a_today) pair matching BOTH
Omega_m AND the real age simultaneously -- a genuinely different combination
of constraints than P95's (Omega_m, Omega_Lambda) pair, since age integrates
information Omega_Lambda at one instant does not carry.

PRE-REGISTERED OUTCOMES:
  UNIQUE       g(Lambda) has a root, and the (a_today, Lambda, H_int) found
               agrees to <1% regardless of which of P94's four seeds bounds
               the search -> age + Omega_m jointly pin the bridge. A
               follow-up step may finally compute kappa and quote k[h/Mpc].
  NO-ROOT      g(Lambda) does not change sign across a physically reasonable
               Lambda range -> the completion cannot reproduce both Omega_m
               AND the real age at any epoch with any Lambda in range -- an
               over-constraint analogous to FINDING_P95's, but on a
               genuinely different pair of observables.
  NON-UNIQUE   multiple roots, or seed-dependent answers differing by >1% ->
               age does not resolve the degeneracy either; the mechanism
               would need still further isolation.

WHAT THIS FILE DOES NOT DO: quote eps(k) or f(k) in physical units under any
outcome. UNIQUE would license a follow-up step to do that.
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


p81 = _load("P81_background_viability.py", "p81_for_age")
p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_age")

OMEGA_M_PLANCK = 0.315
AGE_PLANCK_GYR = 13.787  # Planck 2018 VI, arXiv:1807.06209
H0_PLANCK = 67.4  # km/s/Mpc, same source
HUBBLE_TIME_GYR_AT_H0 = 977.79 / H0_PLANCK  # pure unit conversion, verified this session

A_SEARCH_LO, A_SEARCH_HI = p94.A_SEARCH_LO, p94.A_SEARCH_HI
LAMBDA_LO, LAMBDA_HI = 8.0e-17, 3.0e-12


def state_with_age(sol, a_target):
    """H, Omega_m, t_internal(a_target), age_ratio := t*H -- all from ONE brentq root."""

    def f(t):
        return sol.sol(t)[0] - a_target

    t_lo, t_hi = p81.T0, p81.T_END
    if f(t_lo) * f(t_hi) > 0:
        return None
    t_star = brentq(f, t_lo, t_hi, xtol=1e-6, rtol=1e-12)
    a_, pb, pd = sol.sol(t_star)
    lam_cc = sol._lam_cc
    rho_A = p94.C_MATTER / a_**3
    rho_phys = rho_A * (1.0 - p94.GH * pb)
    Vtot = p94.LAM * pb**4 / 4.0 + lam_cc
    tot = rho_phys + pd**2 / 2.0 + Vtot
    if tot <= 0:
        return None
    H2 = (8.0 * np.pi * p94.G_N / 3.0) * tot
    if H2 <= 0:
        return None
    H = np.sqrt(H2)
    om_m = rho_phys / tot
    return H, om_m, t_star, t_star * H


def physical_age_gyr(t_star, H_int):
    return t_star * H_int * HUBBLE_TIME_GYR_AT_H0


def inner_a_of_lambda(lam_cc):
    """Unchanged from FINDING_P94/P95: a_today where Omega_m,int = 0.315 exactly."""
    s = p94.solve_background_tagged(lam_cc)

    def om_of_a(a):
        st = state_with_age(s, a)
        return (st[1] if st is not None else np.nan) - OMEGA_M_PLANCK

    f_lo, f_hi = om_of_a(A_SEARCH_LO), om_of_a(A_SEARCH_HI)
    if np.isnan(f_lo) or np.isnan(f_hi) or f_lo * f_hi > 0:
        return None, s
    a_today = brentq(om_of_a, A_SEARCH_LO, A_SEARCH_HI, xtol=1e-3, rtol=1e-12)
    return a_today, s


def g_of_lambda(lam_cc):
    """physical_age at the Omega_m=0.315 point, minus the Planck target."""
    a_today, s = inner_a_of_lambda(lam_cc)
    if a_today is None:
        return None, None, None
    st = state_with_age(s, a_today)
    if st is None:
        return None, None, None
    H, om_m, t_star, ratio = st
    age = physical_age_gyr(t_star, H)
    return (age - AGE_PLANCK_GYR), a_today, (H, om_m, t_star, ratio, age)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P97 -- age of the universe as a joint anchor with Omega_m")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL -- deep matter domination: age-Hubble ratio t*H must -> 2/3")
    print("-" * 78)
    print("  Textbook EdS result (age = 2/(3H) for pure matter), external to this")
    print("  project. Checked at SMALL a, before trusting the coupled trajectory.")
    lam_small = 8.0e-17  # smallest seed; Lambda's effect is weakest here
    s0 = p94.solve_background_tagged(lam_small)
    print(f"\n    {'a':<12}{'t*H (age ratio)':<20}{'deviation from 2/3'}")
    worst = 0.0
    n_ok = 0
    for a in (5.0, 15.0, 50.0, 150.0, 500.0):
        st = state_with_age(s0, a)
        if st is None:
            print(f"    {a:<12g}{'not measured':<20}")
            continue
        _H, _om, _t, ratio = st
        dev = abs(ratio - 2.0 / 3.0)
        worst = max(worst, dev)
        n_ok += 1
        print(f"    {a:<12g}{ratio:<20.6f}{dev:.3e}")
    control_ok = n_ok >= 3 and worst < 0.05
    print(f"\n    worst deviation: {worst:.3e}  =>  CONTROL {'PASSES' if control_ok else 'FAILS'}")
    if not control_ok:
        print("  *** the age extraction does not reproduce a textbook result.")
        print("  *** Stopping before any joint solve -- the machinery is not trustworthy yet.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- scan g(Lambda) := physical_age(a_today(Lambda)) - 13.787 Gyr")
    print("-" * 78)
    print(f"  Target age {AGE_PLANCK_GYR} Gyr (Planck 2018, arXiv:1807.06209).")
    print(f"  Hubble time at H_0={H0_PLANCK}: {HUBBLE_TIME_GYR_AT_H0:.6f} Gyr (unit conversion).")
    grid = np.geomspace(LAMBDA_LO, LAMBDA_HI, 12)
    print(f"\n    {'Lambda':<14}{'a_today':<16}{'Omega_m':<12}{'age (Gyr)':<14}{'g(Lambda)'}")
    rows = []
    for lam in grid:
        g, a_today, comp = g_of_lambda(lam)
        if g is None:
            print(f"    {lam:<14.4e}{'not measured (no root / unresolved)':<50}")
            continue
        _H, om_m, _t, _ratio, age = comp
        rows.append((lam, g, a_today))
        print(f"    {lam:<14.4e}{a_today:<16.4f}{om_m:<12.9f}{age:<14.6f}{g:+.6f}")

    if len(rows) < 2:
        print("\n  -> NOT MEASURABLE. Infrastructure outcome, not evidence either way.")
        return 1

    signs = [1 if g > 0 else -1 for _l, g, _a in rows]
    crossings = [(rows[i - 1], rows[i]) for i in range(1, len(rows)) if signs[i] != signs[i - 1]]
    print(f"\n    sign changes of g(Lambda) across the grid: {len(crossings)}")

    if not crossings:
        print("\n" + "=" * 78)
        print("VERDICT (against the outcomes pre-registered in the docstring)")
        print("=" * 78)
        lo_g = min(rows, key=lambda r: abs(r[1]))
        print(
            f"  -> NO-ROOT. g(Lambda) does not change sign in [{LAMBDA_LO:.2e}, {LAMBDA_HI:.2e}]."
        )
        print(f"     Closest approach: Lambda={lo_g[0]:.4e}, |g|={abs(lo_g[1]):.4f} Gyr.")
        print("     The completion cannot match BOTH Omega_m AND the real age at any")
        print("     epoch with any Lambda in this range. NO k[h/Mpc] number is quoted.")
        return 0

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- locate the root(s), from independent brackets")
    print("-" * 78)
    roots = []
    for lo_row, hi_row in crossings:
        lo_lam, hi_lam = lo_row[0], hi_row[0]

        def gg(lam):
            g, _a, _c = g_of_lambda(lam)
            return g if g is not None else np.nan

        lam_root = brentq(gg, lo_lam, hi_lam, xtol=1e-20, rtol=1e-10)
        a_root, s_root = inner_a_of_lambda(lam_root)
        H_root, om_m_r, t_root, ratio_r = state_with_age(s_root, a_root)
        age_r = physical_age_gyr(t_root, H_root)
        roots.append((lam_root, a_root, H_root))
        print(f"    bracket [{lo_lam:.4e}, {hi_lam:.4e}]")
        print(f"      Lambda_internal = {lam_root:.10e}")
        print(f"      a_today         = {a_root:.6f}")
        print(f"      H_int(a_today)  = {H_root:.10e}")
        print(f"      check: Omega_m={om_m_r:.9f}  age={age_r:.6f} Gyr")

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if len(roots) == 1:
        lam_root, a_root, H_root = roots[0]
        print("  -> UNIQUE (single crossing found in this scan).")
        print(f"\n     Lambda_internal = {lam_root:.10e}")
        print(f"     a_today         = {a_root:.6f}")
        print(f"     H_int(a_today)  = {H_root:.10e}")
        kappa = H0_PLANCK / H_root
        print(f"\n     kappa = H_0 / H_int(a_today) = {kappa:.6e} km/s/Mpc per internal unit")
        print("\n     COMPARISON TO FINDING_P95's (Omega_m, Omega_Lambda) joint result, if any")
        print("     -- both use the SAME inner Omega_m=0.315 root, so a match would show")
        print("     the two INDEPENDENT second constraints (Omega_Lambda vs age) agree.")
        print("\n     k[h/Mpc] IS NOT QUOTED IN THIS FILE. A follow-up step may now combine")
        print("     kappa, a_today, and the universal h/Mpc constant 100/c=3.335641e-4 to")
        print("     map k=3,10,30 to physical units.")
    else:
        Hs = [r[2] for r in roots]
        spread = max(Hs) / min(Hs)
        print(f"  -> NON-UNIQUE. {len(roots)} distinct roots found.")
        print(f"     H_int(a_today) spread across roots: {spread:.4f}x")
        print("     Age does not resolve the degeneracy either. No k[h/Mpc] number quoted.")

    print("\n  NOT ESTABLISHED:")
    print("   * that this is the only root outside the scanned Lambda range.")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about MULTING itself (Gate 1). No dataset, no Table A1")
    print("     quantity enters this file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
