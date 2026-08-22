"""P99 -- does the completion's H(a) SHAPE match flat-LCDM's, across multiple epochs?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P98 closed the P93-P98 sub-arc: six anchoring attempts, all matching a
single number at or through ONE epoch, converged on the same conclusion -- a
ratio or integral observable fixes composition, never the absolute scale of
Lambda_internal. It named what would differ in KIND, not just which number is
matched: an observable sensitive to the SHAPE of H(a) across multiple epochs
at once. This file is that different kind of test.

THE KEY STRUCTURAL DIFFERENCE FROM P93-P98, STATED BEFORE ANY CODE. Define the
SHAPE ratio

    shape(a) := H_internal(a) / H_internal(a_today)

kappa (the internal-to-physical H conversion) multiplies BOTH numerator and
denominator and CANCELS EXACTLY. So shape(a) needs no external calibration at
all -- it is a purely internal, dimensionless function of (Lambda_internal,
a_today) and the epoch a. Compare it against flat-LCDM's own shape,

    shape_LCDM(z) := H_LCDM(z)/H_0 = sqrt(Omega_m*(1+z)^3 + Omega_Lambda)

(Omega_m=0.315, Omega_Lambda=0.685, Planck 2018, arXiv:1807.06209 -- the same
values used throughout this bridge arc, and shape_LCDM(0)=1 by construction).

The completion has exactly TWO free numbers left after this arc:
Lambda_internal and a_today (kappa, the third, is calibration and drops out of
a shape comparison entirely). Matching shape(a) to shape_LCDM(z) at TWO
epochs is therefore a WELL-POSED 2-equation/2-unknown system -- unlike every
P93-P98 step, which either under-determined (1 equation, 2 unknowns, P94) or
over-determined (2+ equations forced onto 1 remaining unknown after kappa
dropped out at a single epoch, P95/P97) the SAME two unknowns. Fitting at two
epochs and CHECKING at additional, out-of-sample epochs is genuinely
falsifiable in a way P93-P98 could not be: nothing forces agreement beyond the
two fitted points.

METHOD: the same nested root-finding architecture as P95/P97. For a trial
Lambda, inner_a(Lambda) is chosen so shape(a) matches shape_LCDM at z_fit1
EXACTLY. Then g(Lambda) := shape(a_at_z_fit2; Lambda, inner_a(Lambda)) -
shape_LCDM(z_fit2). A root of g(Lambda) gives a (Lambda, a_today) pair matching
BOTH fit points. That pair is then evaluated -- not fitted -- at z_check
points the solve never saw.

z_fit1 = 0.5, z_fit2 = 1.5 (a reasonably separated pair inside the redshift
range BAO/SNe surveys actually probe). z_check = 1.0 (between the fit points,
interpolation) and z_check = 3.0 (beyond them, extrapolation) -- both
OUT-OF-SAMPLE, evaluated only after the fit is fixed.

CONTROL BEFORE ANY SOLVE: shape(a_today)=1 and shape_LCDM(0)=1 by construction
-- checked in the running code, not trusted from the formulas, exactly as
every joint-anchor step in this arc has insisted on.

PRE-REGISTERED OUTCOMES, on the OUT-OF-SAMPLE residuals only (the fit points
cannot fail by construction and are not scored):
  SHAPE-MATCHES    both out-of-sample residuals < 1% -> the completion's
                   H(a) shape genuinely resembles flat-LCDM once calibrated at
                   two points. This is the first NON-CIRCULAR success this
                   arc could report, and licenses a follow-up step to fix
                   kappa via this same (Lambda, a_today) and finally quote
                   k[h/Mpc].
  SHAPE-DIVERGES   either out-of-sample residual > 10% -> no calibration of
                   this completion reproduces flat-LCDM's expansion-history
                   shape over an observationally relevant redshift range --
                   a more fundamental statement than P93-P98's degeneracy:
                   not "which Lambda", but "no Lambda makes this look like
                   standard cosmology's H(a)".
  INTERMEDIATE     between 1% and 10% -> named, not rounded toward either.

WHAT THIS FILE DOES NOT DO: quote eps(k) or f(k) in physical units under any
outcome. SHAPE-MATCHES would license a follow-up step to do that; it does not
do it here.
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


p81 = _load("P81_background_viability.py", "p81_for_shape")
p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_shape")

OMEGA_M = 0.315
OMEGA_LAMBDA = 1.0 - OMEGA_M

Z_FIT1, Z_FIT2 = 0.5, 1.5
Z_CHECK = (1.0, 3.0)

A_SEARCH_LO, A_SEARCH_HI = p94.A_SEARCH_LO, p94.A_SEARCH_HI
LAMBDA_LO, LAMBDA_HI = 8.0e-17, 3.0e-12


def shape_lcdm(z):
    return np.sqrt(OMEGA_M * (1.0 + z) ** 3 + OMEGA_LAMBDA)


def H_at_a(sol, a_target):
    """Internal H at a_target, via the SAME brentq-on-dense-solution pattern used throughout."""

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
    return np.sqrt(H2)


def inner_a_of_lambda(lam_cc, z_target=Z_FIT1):
    """a_today such that shape(a_at_z_target)/shape(a_today) matches shape_LCDM(z_target).

    # WHY solved by varying a_today rather than a_at_z_target directly: a_today
    # is the free unknown throughout this arc; a_at_z_target = a_today/(1+z) is
    # DERIVED from it, keeping the redshift-to-scale-factor relation fixed
    # exactly the way FINDING_P85 established (1+z = a_ref/a, no extra freedom).
    """
    s = p94.solve_background_tagged(lam_cc)

    def resid(a_today):
        H_today = H_at_a(s, a_today)
        H_z = H_at_a(s, a_today / (1.0 + z_target))
        if H_today is None or H_z is None or H_today <= 0:
            return np.nan
        return (H_z / H_today) - shape_lcdm(z_target)

    f_lo, f_hi = resid(A_SEARCH_LO), resid(A_SEARCH_HI)
    if np.isnan(f_lo) or np.isnan(f_hi) or f_lo * f_hi > 0:
        return None, s
    a_today = brentq(resid, A_SEARCH_LO, A_SEARCH_HI, xtol=1e-3, rtol=1e-12)
    return a_today, s


def shape_at(s, a_today, z):
    H_today = H_at_a(s, a_today)
    H_z = H_at_a(s, a_today / (1.0 + z))
    if H_today is None or H_z is None or H_today <= 0:
        return None
    return H_z / H_today


def g_of_lambda(lam_cc):
    """shape at z_fit2 (given the z_fit1-fixed a_today), minus the LCDM target."""
    a_today, s = inner_a_of_lambda(lam_cc, Z_FIT1)
    if a_today is None:
        return None, None, None
    sh2 = shape_at(s, a_today, Z_FIT2)
    if sh2 is None:
        return None, None, None
    return (sh2 - shape_lcdm(Z_FIT2)), a_today, s


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P99 -- H(a) SHAPE across multiple epochs, versus flat-LCDM")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL -- shape(a_today)=1 and shape_LCDM(0)=1, checked not assumed")
    print("-" * 78)
    lam_probe = 6.5e-14
    s_probe = p94.solve_background_tagged(lam_probe)
    a_probe = 30000.0
    sh_self = shape_at(s_probe, a_probe, 0.0)
    lcdm_self = shape_lcdm(0.0)
    print(f"  shape(a_today; z=0)   = {sh_self!r}")
    print(f"  shape_LCDM(z=0)       = {lcdm_self!r}")
    control_ok = sh_self is not None and abs(sh_self - 1.0) < 1e-9 and abs(lcdm_self - 1.0) < 1e-12
    print(f"  CONTROL {'PASSES' if control_ok else 'FAILS'}")
    if not control_ok:
        print("  *** normalization is broken. Stopping before any joint solve.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(
        f"PART A -- scan g(Lambda) := shape(z={Z_FIT2}) - shape_LCDM({Z_FIT2}), z_fit1={Z_FIT1} fixes a_today"
    )
    print("-" * 78)
    grid = np.geomspace(LAMBDA_LO, LAMBDA_HI, 12)
    print(f"\n    {'Lambda':<14}{'a_today':<16}{'shape(z_fit2)':<16}{'g(Lambda)'}")
    rows = []
    for lam in grid:
        g, a_today, _s = g_of_lambda(lam)
        if g is None:
            print(f"    {lam:<14.4e}{'not measured (no root / unresolved)':<46}")
            continue
        rows.append((lam, g, a_today))
        print(f"    {lam:<14.4e}{a_today:<16.4f}{g + shape_lcdm(Z_FIT2):<16.9f}{g:+.6e}")

    if len(rows) < 2:
        print("\n  -> NOT MEASURABLE. Infrastructure outcome, not evidence either way.")
        return 1

    signs = [1 if g > 0 else -1 for _l, g, _a in rows]
    crossings = [(rows[i - 1], rows[i]) for i in range(1, len(rows)) if signs[i] != signs[i - 1]]
    print(f"\n    sign changes of g(Lambda) across the grid: {len(crossings)}")

    if not crossings:
        best = min(rows, key=lambda r: abs(r[1]))
        print("\n" + "=" * 78)
        print("VERDICT")
        print("=" * 78)
        print(
            f"  -> NO JOINT FIT. g(Lambda) never crosses zero in [{LAMBDA_LO:.2e}, {LAMBDA_HI:.2e}]."
        )
        print(f"     Closest approach: Lambda={best[0]:.4e}, g={best[1]:+.4e}.")
        print("     No (Lambda, a_today) pair reproduces shape_LCDM at BOTH fit points at")
        print("     all -- the shape test cannot even be attempted at the check points.")
        print("     NO k[h/Mpc] number is quoted.")
        return 0

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- locate the two-point fit, from independent brackets")
    print("-" * 78)
    fits = []
    for lo_row, hi_row in crossings:
        lo_lam, hi_lam = lo_row[0], hi_row[0]

        def gg(lam):
            g, _a, _s = g_of_lambda(lam)
            return g if g is not None else np.nan

        lam_fit = brentq(gg, lo_lam, hi_lam, xtol=1e-20, rtol=1e-10)
        a_fit, s_fit = inner_a_of_lambda(lam_fit, Z_FIT1)
        sh1 = shape_at(s_fit, a_fit, Z_FIT1)
        sh2 = shape_at(s_fit, a_fit, Z_FIT2)
        fits.append((lam_fit, a_fit, s_fit))
        print(f"    bracket [{lo_lam:.4e}, {hi_lam:.4e}]")
        print(f"      Lambda_internal = {lam_fit:.10e}")
        print(f"      a_today         = {a_fit:.6f}")
        print(f"      fit check: shape(z={Z_FIT1})={sh1:.9f} vs LCDM {shape_lcdm(Z_FIT1):.9f}")
        print(f"                 shape(z={Z_FIT2})={sh2:.9f} vs LCDM {shape_lcdm(Z_FIT2):.9f}")

    print("\n" + "-" * 78)
    print(f"PART C -- OUT-OF-SAMPLE CHECK at z={Z_CHECK}, never used in the fit")
    print("-" * 78)
    worst_rel = {}
    for i, (lam_fit, a_fit, s_fit) in enumerate(fits):
        print(f"\n  fit #{i + 1}: Lambda={lam_fit:.4e}, a_today={a_fit:.4f}")
        print(f"    {'z_check':<10}{'shape (completion)':<22}{'shape_LCDM':<16}{'relative diff'}")
        worst = 0.0
        for z in Z_CHECK:
            sh = shape_at(s_fit, a_fit, z)
            target = shape_lcdm(z)
            if sh is None:
                print(f"    {z:<10g}{'not measured':<22}")
                continue
            rel = abs(sh / target - 1.0)
            worst = max(worst, rel)
            print(f"    {z:<10g}{sh:<22.9f}{target:<16.9f}{rel:.4e}")
        worst_rel[i] = worst

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    overall_worst = max(worst_rel.values()) if worst_rel else float("nan")
    print(f"  worst out-of-sample relative deviation across all fits: {overall_worst:.4e}")
    if overall_worst < 0.01:
        print("  -> SHAPE-MATCHES. Both out-of-sample checks agree with flat-LCDM to < 1%.")
        print("     The completion's H(a) shape genuinely resembles flat-LCDM once calibrated")
        print("     at two points -- the first NON-CIRCULAR success in this bridge arc.")
        print("     A follow-up step may now fix kappa via this SAME (Lambda, a_today) and")
        print("     quote k[h/Mpc]. Not done in this file.")
    elif overall_worst > 0.10:
        print("  -> SHAPE-DIVERGES. Out-of-sample deviation exceeds 10%. No calibration of")
        print("     this completion reproduces flat-LCDM's expansion-history SHAPE over this")
        print("     redshift range. A more fundamental statement than FINDING_P93-P98's")
        print("     degeneracy: not 'which Lambda', but 'no Lambda makes this completion's")
        print(
            "     H(a) look like standard cosmology's' over z in "
            f"[{Z_FIT1}, {max(Z_FIT2, *Z_CHECK)}]."
        )
        print("     NO k[h/Mpc] number is quoted.")
    else:
        print("  -> INTERMEDIATE. Named, not rounded toward either outcome.")
        print("     NO k[h/Mpc] number is quoted.")

    print("\n  NOT ESTABLISHED:")
    print("   * that z_fit1=0.5, z_fit2=1.5 are the 'right' fit points -- a different pair")
    print("     could give a different verdict; not tested here.")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about MULTING itself (Gate 1). No dataset, no Table A1")
    print("     quantity enters this file -- shape_LCDM is a textbook formula, not a fit")
    print("     to any specific survey's H(z) data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
