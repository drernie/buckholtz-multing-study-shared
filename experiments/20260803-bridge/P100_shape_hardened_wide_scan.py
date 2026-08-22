"""P100 -- P99 hardened against overflow, then re-scanned past both walls it hit.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P99 found NO JOINT FIT for the two-epoch H(a) shape match, but the
search hit two INFRASTRUCTURE walls rather than a proven absence of a root:
below Lambda~1.1e-16 the inner a_today root stopped resolving, and above
Lambda~4e-12 the integrator overflowed with an UNCAUGHT ValueError (a real
robustness gap in H_at_a and solve_background, neither of which guards
against non-finite states -- unlike P81's viability() and P86's background
solves, which both wrap solve_ivp in np.errstate and check s.success).

THIS FILE DOES TWO THINGS, IN ORDER, NOT ONE:

  (1) HARDEN. A local solve_background_safe() wraps P94's solve_background in
      np.errstate(all="ignore") and records s.success. A hardened H_at_a
      checks that flag, guards every sol.sol(t) evaluation for finiteness,
      and catches brentq's own ValueError on a NaN function value -- turning
      every failure mode into a clean None (BLOCKED-INFRASTRUCTURE) rather
      than a crash. This is the SAME Substrate Gate discipline this campaign
      has applied everywhere else; P99 simply had not needed it yet because
      its own pre-registered grid never reached the regions that trigger it.

  (2) REGRESSION CONTROL, before trusting any new number. The hardened path
      MUST reproduce FINDING_P99's own already-published values at the SAME
      Lambda it already tested -- if hardening silently changed the answer,
      that is a bug in the hardening, not a discovery. Checked at
      Lambda=2.084e-16 (P99's g=+2.905e-06) and Lambda=3.000e-12 (P99's
      g=+1.616e-05) before the wider scan is trusted at all.

  (3) THEN, and only then, re-scan a Lambda range extended well past BOTH
      walls P99 hit: down to 1e-19 (P99's floor was ~1.1e-16) and up to
      1e-9 (P99's ceiling was ~4e-12, where it crashed).

PRE-REGISTERED OUTCOMES:
  ROOT-FOUND        g(Lambda) crosses zero somewhere in the widened range ->
                    locate it precisely and finally run the out-of-sample
                    check at z=1.0/z=3.0 that FINDING_P99 never reached.
  STILL-NO-ROOT     the hardened, widened search still finds zero sign
                    changes -> report the NEW bounds honestly. Still not a
                    P95-style proof unless the endpoints themselves are
                    understood analytically (checked separately, not assumed).
  MIXED             the hardening changes FINDING_P99's own published numbers
                    at the regression-control Lambda values -> STOP. The
                    hardening introduced a bug; nothing past this point is
                    trustworthy until it is found.

WHAT THIS FILE DOES NOT DO: quote eps(k) or f(k) in physical units under any
outcome. ROOT-FOUND and a passing out-of-sample check would license a
follow-up step to do that; it is not done here.
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


p81 = _load("P81_background_viability.py", "p81_for_wide")
p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_wide")
p99 = _load("P99_shape_of_H_across_epochs.py", "p99_for_wide")

OMEGA_M, OMEGA_LAMBDA = p99.OMEGA_M, p99.OMEGA_LAMBDA
Z_FIT1, Z_FIT2, Z_CHECK = p99.Z_FIT1, p99.Z_FIT2, p99.Z_CHECK
shape_lcdm = p99.shape_lcdm

A_SEARCH_LO, A_SEARCH_HI = p94.A_SEARCH_LO, p94.A_SEARCH_HI

# Regression targets: FINDING_P99's own published numbers, not recomputed --
# quoted from the committed finding, to check the hardened path reproduces them.
REGRESSION = {
    2.084e-16: 2.905e-06,
    3.000e-12: 1.616e-05,
}
REGRESSION_TOL = 5e-3  # relative -- P99 printed 4 sig figs, not exact bit patterns

LAMBDA_LO_WIDE, LAMBDA_HI_WIDE = 1e-19, 1e-9


def solve_background_safe(lam_cc):
    """P94's solve_background, wrapped: errors suppressed, success recorded."""
    with np.errstate(all="ignore"):
        try:
            s = p94.solve_background(lam_cc)
        except Exception:  # noqa: BLE001 - any integrator failure is BLOCKED-INFRASTRUCTURE
            return None
    s._lam_cc = lam_cc
    s._ok = bool(s.success)
    return s


def H_at_a(sol, a_target):
    """Hardened: every failure mode returns None, none of them raise."""
    if sol is None or not getattr(sol, "_ok", False):
        return None
    with np.errstate(all="ignore"):
        try:
            a0 = sol.sol(sol.t[0])[0]
            a1 = sol.sol(sol.t[-1])[0]
        except Exception:  # noqa: BLE001
            return None
        if not (np.isfinite(a0) and np.isfinite(a1)):
            return None

        def f(t):
            try:
                av = sol.sol(t)[0]
            except Exception:  # noqa: BLE001
                return np.nan
            return av - a_target if np.isfinite(av) else np.nan

        t_lo, t_hi = p81.T0, p81.T_END
        f_lo, f_hi = f(t_lo), f(t_hi)
        if not (np.isfinite(f_lo) and np.isfinite(f_hi)) or f_lo * f_hi > 0:
            return None
        try:
            t_star = brentq(f, t_lo, t_hi, xtol=1e-6, rtol=1e-12)
        except (ValueError, RuntimeError):
            return None
        state = sol.sol(t_star)
        if not np.all(np.isfinite(state)):
            return None
        a_, pb, pd = state
        lam_cc = sol._lam_cc
        rho_A = p94.C_MATTER / a_**3
        rho_phys = rho_A * (1.0 - p94.GH * pb)
        Vtot = p94.LAM * pb**4 / 4.0 + lam_cc
        tot = rho_phys + pd**2 / 2.0 + Vtot
        if not np.isfinite(tot) or tot <= 0:
            return None
        H2 = (8.0 * np.pi * p94.G_N / 3.0) * tot
        if not np.isfinite(H2) or H2 <= 0:
            return None
        return float(np.sqrt(H2))


def shape_at(s, a_today, z):
    H_today = H_at_a(s, a_today)
    H_z = H_at_a(s, a_today / (1.0 + z))
    if H_today is None or H_z is None or H_today <= 0:
        return None
    return H_z / H_today


def inner_a_of_lambda(lam_cc, z_target=Z_FIT1):
    s = solve_background_safe(lam_cc)
    if s is None:
        return None, s

    def resid(a_today):
        sh = shape_at(s, a_today, z_target)
        return (sh - shape_lcdm(z_target)) if sh is not None else np.nan

    with np.errstate(all="ignore"):
        f_lo, f_hi = resid(A_SEARCH_LO), resid(A_SEARCH_HI)
        if not (np.isfinite(f_lo) and np.isfinite(f_hi)) or f_lo * f_hi > 0:
            return None, s
        try:
            a_today = brentq(resid, A_SEARCH_LO, A_SEARCH_HI, xtol=1e-3, rtol=1e-12)
        except (ValueError, RuntimeError):
            return None, s
    return a_today, s


def g_of_lambda(lam_cc):
    a_today, s = inner_a_of_lambda(lam_cc, Z_FIT1)
    if a_today is None:
        return None, None, None
    sh2 = shape_at(s, a_today, Z_FIT2)
    if sh2 is None:
        return None, None, None
    return (sh2 - shape_lcdm(Z_FIT2)), a_today, s


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P100 -- hardened H_at_a, then re-scan Lambda past both walls FINDING_P99 hit")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("STEP 1 -- REGRESSION CONTROL: hardened path must reproduce FINDING_P99's")
    print("own published numbers, or nothing past this point is trustworthy")
    print("-" * 78)
    print(f"\n    {'Lambda':<14}{'P99 published g':<20}{'this file g':<20}{'rel diff'}")
    reg_ok = True
    for lam, published in REGRESSION.items():
        g, _a, _s = g_of_lambda(lam)
        if g is None:
            print(f"    {lam:<14.4e}{published:<20.4e}{'not measured':<20}")
            reg_ok = False
            continue
        rel = abs(g / published - 1.0)
        ok = rel < REGRESSION_TOL
        reg_ok = reg_ok and ok
        print(
            f"    {lam:<14.4e}{published:<20.4e}{g:<20.6e}{rel:.3e}  {'OK' if ok else 'MISMATCH'}"
        )
    print(f"\n    REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** hardening changed FINDING_P99's own answers. STOP -- find the bug")
        print("  *** before trusting anything below.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(f"STEP 2 -- wide scan, Lambda in [{LAMBDA_LO_WIDE:.0e}, {LAMBDA_HI_WIDE:.0e}]")
    print("          (FINDING_P99's own range was [8.0e-17, 3.0e-12])")
    print("-" * 78)
    grid = np.geomspace(LAMBDA_LO_WIDE, LAMBDA_HI_WIDE, 40)
    print(f"\n    {'Lambda':<14}{'a_today':<16}{'g(Lambda)'}")
    rows = []
    for lam in grid:
        g, a_today, _s = g_of_lambda(lam)
        if g is None:
            print(f"    {lam:<14.4e}{'not measured (no root / unresolved)':<40}")
            continue
        rows.append((lam, g, a_today))
        print(f"    {lam:<14.4e}{a_today:<16.4f}{g:+.6e}")

    if len(rows) < 2:
        print("\n  -> NOT MEASURABLE across the widened range either. Infrastructure")
        print("     outcome, not evidence either way.")
        return 1

    signs = [1 if g > 0 else -1 for _l, g, _a in rows]
    crossings = [(rows[i - 1], rows[i]) for i in range(1, len(rows)) if signs[i] != signs[i - 1]]
    lam_measured = [r[0] for r in rows]
    print(f"\n    Lambda values that were MEASURABLE at all: {len(rows)}/{len(grid)}")
    print(f"    measurable range: [{min(lam_measured):.4e}, {max(lam_measured):.4e}]")
    print(f"    sign changes of g(Lambda): {len(crossings)}")

    if not crossings:
        best = min(rows, key=lambda r: abs(r[1]))
        print("\n" + "=" * 78)
        print("VERDICT (against the outcomes pre-registered in the docstring)")
        print("=" * 78)
        print("  -> STILL-NO-ROOT. Zero sign changes across the WIDENED, HARDENED scan.")
        print(f"     Closest approach: Lambda={best[0]:.4e}, g={best[1]:+.4e}.")
        print(f"     Measurable Lambda range: [{min(lam_measured):.4e}, {max(lam_measured):.4e}]")
        print("     -- compare FINDING_P99's own bounded range [8.0e-17, 3.0e-12], now")
        print(f"     extended by {min(lam_measured) / 8.0e-17:.3g}x downward and")
        print(f"     {max(lam_measured) / 3.0e-12:.3g}x upward before hitting the NEXT wall.")
        print("     NO k[h/Mpc] number is quoted.")
        return 0

    # ==================================================================
    print("\n" + "-" * 78)
    print("STEP 3 -- a root exists. Locate it, then run the out-of-sample check")
    print("          FINDING_P99 never reached.")
    print("-" * 78)
    fits = []
    for lo_row, hi_row in crossings:
        lo_lam, hi_lam = lo_row[0], hi_row[0]

        def gg(lam):
            g, _a, _s = g_of_lambda(lam)
            return g if g is not None else np.nan

        lam_fit = brentq(gg, lo_lam, hi_lam, xtol=1e-20, rtol=1e-10)
        a_fit, s_fit = inner_a_of_lambda(lam_fit, Z_FIT1)
        fits.append((lam_fit, a_fit, s_fit))
        print(
            f"    bracket [{lo_lam:.4e}, {hi_lam:.4e}]  ->  Lambda={lam_fit:.10e}, a_today={a_fit:.6f}"
        )

    worst_rel = {}
    for i, (_lam_fit, a_fit, s_fit) in enumerate(fits):
        print(f"\n  fit #{i + 1}: out-of-sample check at z={Z_CHECK}")
        worst = 0.0
        for z in Z_CHECK:
            sh = shape_at(s_fit, a_fit, z)
            target = shape_lcdm(z)
            if sh is None:
                print(f"    z={z:<6g} not measured")
                continue
            rel = abs(sh / target - 1.0)
            worst = max(worst, rel)
            print(f"    z={z:<6g} shape={sh:.9f}  LCDM={target:.9f}  rel={rel:.4e}")
        worst_rel[i] = worst

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    overall = max(worst_rel.values()) if worst_rel else float("nan")
    print(f"  -> ROOT-FOUND. Worst out-of-sample deviation: {overall:.4e}")
    if overall < 0.01:
        print("     SHAPE-MATCHES (per FINDING_P99's own criterion). First non-circular")
        print("     success in this bridge arc. NOT converted to k[h/Mpc] in this file.")
    elif overall > 0.10:
        print("     SHAPE-DIVERGES (per FINDING_P99's own criterion) even though a")
        print("     two-point fit exists -- the fit does not extrapolate.")
    else:
        print("     INTERMEDIATE. Named, not rounded toward either.")

    print("\n  NOT ESTABLISHED:")
    print("   * that the widened range is exhaustive -- Lambda outside")
    print(f"     [{LAMBDA_LO_WIDE:.0e}, {LAMBDA_HI_WIDE:.0e}] was not tried.")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
