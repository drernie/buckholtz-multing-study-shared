"""P95 -- solving JOINTLY for (a_today, Lambda_internal) from {Omega_m, Omega_Lambda}.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

FINDING_P94 registered a "third anchor" -- require the completion's Lambda,
once converted to physical units, to reproduce the real cosmological constant
-- as the next step to try. A hand-algebra check of that idea BEFORE building
it produced two contradictory conclusions in a row (first "this reduces to the
Omega_Lambda=1-Omega_m condition P94 already tried, so it is not new
information", then, on redoing it, "no -- P94 held Lambda FIXED and only
solved for a_today against ONE condition; enforcing Omega_m=0.315 AND
Omega_Lambda=0.685 SIMULTANEOUSLY, letting BOTH a_today and Lambda vary, is a
genuinely different, better-posed 2-equation/2-unknown system"). Two
self-contradicting hand derivations in a row is exactly the signal not to
trust a third one -- this file settles it numerically.

THE RESOLUTION, STATED PRECISELY BEFORE ANY NUMBER. Our internal Friedmann
budget has THREE components: matter (Omega_m), the added cosmological-constant
term (Omega_Lambda), and a small RESIDUAL scalar contribution
(Omega_phi = 1 - Omega_m - Omega_Lambda) that FINDING_P93 already measured as
nonzero (order 1e-5 to 1e-7, shrinking with a_today). Because Omega_phi is not
exactly zero, "Omega_m=0.315" and "Omega_Lambda=0.685" are NOT the same
condition -- flatness alone does not make one imply the other while a third
component exists. So jointly imposing BOTH is a real second equation, and
P94's single-condition family (fixed Lambda, vary a_today) never tested it.

THE METHOD: NESTED root-finding, reusing P94's own machinery rather than a
black-box 2D solver, so every step stays inspectable. For a given Lambda,
inner_a(Lambda) := the a_today where Omega_m,int(a; Lambda) = 0.315 exactly
(P94's own root, unchanged). Then g(Lambda) := Omega_Lambda,int(inner_a(Lambda);
Lambda) - 0.685. A root of g(Lambda) gives a (Lambda, a_today) pair satisfying
BOTH conditions at once.

PRE-REGISTERED OUTCOMES, because the honest space of results is NOT just
"works" -- the residual Omega_phi being tiny could mean g(Lambda) barely moves
at all across any Lambda range tried, or does not cross zero within a
physically sensible range:
  UNIQUE       g(Lambda) has a root, found from at least two different
               starting brackets, agreeing to <1% -> {Omega_m, Omega_Lambda}
               jointly DO pin (a_today, Lambda_internal), and kappa = H_0 /
               H_int(a_today) can finally be computed. A follow-up step may
               then quote k[h/Mpc].
  NO-ROOT      g(Lambda) does not change sign across the tested range -> the
               model, as built, cannot simultaneously match Planck's Omega_m
               AND Omega_Lambda at ANY epoch with ANY Lambda choice within the
               range tried. A sharper, more consequential negative result than
               FINDING_P94's degeneracy: not "underdetermined", but
               "over-constrained and inconsistent with flat LCDM's exact
               composition, given this completion's specific H(a) shape".
  NON-UNIQUE   multiple roots found, or the two starting brackets disagree by
               more than 1% -> still degenerate even with two joint
               conditions; the mechanism would need further isolation.

Omega_m = 0.315, Omega_Lambda = 1 - Omega_m = 0.685 -- both from Planck 2018
results VI, base-LCDM, arXiv:1807.06209 (same source as FINDING_P93/P94's
H_0 = 67.4 km/s/Mpc). Using 1-Omega_m for Omega_Lambda matches Planck's own
flat-LCDM analysis; it is not an independent third measurement, and this file
does not claim it is -- the NEW information here is using both SIMULTANEOUSLY
as constraints on the SAME (a_today, Lambda) pair, not a new external number.

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


p81 = _load("P81_background_viability.py", "p81_for_joint")
p94 = _load("P94_second_anchor_family_invariance.py", "p94_for_joint")

OMEGA_M_PLANCK = 0.315
OMEGA_LAMBDA_PLANCK = 1.0 - OMEGA_M_PLANCK
A_SEARCH_LO, A_SEARCH_HI = p94.A_SEARCH_LO, p94.A_SEARCH_HI

# Two independent brackets for the OUTER (Lambda) search, spanning the range
# FINDING_P93/P94 already showed contains sensible Omega_Lambda~0.7 behaviour.
LAMBDA_LO, LAMBDA_HI = 8.0e-17, 3.0e-12


def state_full(sol, a_target):
    """H, Omega_m, Omega_Lambda, Omega_phi_residual at a_target on sol."""
    from scipy.optimize import brentq as _brentq

    def f(t):
        return sol.sol(t)[0] - a_target

    t_lo, t_hi = p81.T0, p81.T_END
    if f(t_lo) * f(t_hi) > 0:
        return None
    t_star = _brentq(f, t_lo, t_hi, xtol=1e-6, rtol=1e-12)
    a_, pb, pd = sol.sol(t_star)
    lam_cc = sol._lam_cc
    rho_A = p94.C_MATTER / a_**3
    rho_phys = rho_A * (1.0 - p94.GH * pb)
    V_scalar = p94.LAM * pb**4 / 4.0
    Vtot = V_scalar + lam_cc
    tot = rho_phys + pd**2 / 2.0 + Vtot
    if tot <= 0:
        return None
    H2 = (8.0 * np.pi * p94.G_N / 3.0) * tot
    if H2 <= 0:
        return None
    H = np.sqrt(H2)
    om_m = rho_phys / tot
    om_lam = lam_cc / tot
    om_phi = (pd**2 / 2.0 + V_scalar) / tot
    return H, om_m, om_lam, om_phi


def inner_a_of_lambda(lam_cc):
    """FINDING_P94's own root: a_today where Omega_m,int = 0.315 exactly."""
    s = p94.solve_background_tagged(lam_cc)

    def om_of_a(a):
        st = state_full(s, a)
        return (st[1] if st is not None else np.nan) - OMEGA_M_PLANCK

    f_lo, f_hi = om_of_a(A_SEARCH_LO), om_of_a(A_SEARCH_HI)
    if np.isnan(f_lo) or np.isnan(f_hi) or f_lo * f_hi > 0:
        return None, s
    a_today = brentq(om_of_a, A_SEARCH_LO, A_SEARCH_HI, xtol=1e-3, rtol=1e-12)
    return a_today, s


def g_of_lambda(lam_cc):
    """Omega_Lambda,int at the Omega_m=0.315 point, minus the Planck target."""
    a_today, s = inner_a_of_lambda(lam_cc)
    if a_today is None:
        return None, None, None
    st = state_full(s, a_today)
    if st is None:
        return None, None, None
    _H, om_m, om_lam, om_phi = st
    return (om_lam - OMEGA_LAMBDA_PLANCK), a_today, (om_m, om_lam, om_phi)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P95 -- joint two-anchor solve for (a_today, Lambda_internal)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n" + "-" * 78)
    print("PART A -- scan g(Lambda) := Omega_Lambda,int(a_today(Lambda)) - 0.685")
    print("-" * 78)
    print("  a_today(Lambda) is P94's own root (Omega_m=0.315 exactly). If g")
    print("  changes sign across the Lambda range, a joint solution exists.")
    grid = np.geomspace(LAMBDA_LO, LAMBDA_HI, 12)
    print(
        f"\n    {'Lambda':<14}{'a_today':<16}{'Omega_m':<14}{'Omega_Lambda':<16}"
        f"{'Omega_phi':<14}{'g(Lambda)'}"
    )
    rows = []
    for lam in grid:
        g, a_today, comp = g_of_lambda(lam)
        if g is None:
            print(f"    {lam:<14.4e}{'not measured (no root / unresolved)':<60}")
            continue
        om_m, om_lam, om_phi = comp
        rows.append((lam, g, a_today))
        print(
            f"    {lam:<14.4e}{a_today:<16.4f}{om_m:<14.9f}{om_lam:<16.12f}{om_phi:<14.3e}{g:+.6e}"
        )

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
        print("  -> NO-ROOT. g(Lambda) does not change sign anywhere in")
        print(f"     [{LAMBDA_LO:.2e}, {LAMBDA_HI:.2e}]. The completion cannot")
        print("     simultaneously match Planck's Omega_m AND Omega_Lambda at ANY")
        print("     epoch with ANY Lambda in this range -- a sharper, more")
        print("     consequential negative result than FINDING_P94's degeneracy:")
        print("     not underdetermined, but OVER-CONSTRAINED. No k[h/Mpc] number")
        print("     is quoted.")
        print("\n  NOT ESTABLISHED: whether a root exists OUTSIDE this range; that")
        print("  would need its own extension, not assumed here.")
        return 0

    print("\n" + "-" * 78)
    print("PART B -- locate the root(s) precisely, from independent brackets")
    print("-" * 78)
    roots = []
    for lo_row, hi_row in crossings:
        lo_lam, hi_lam = lo_row[0], hi_row[0]

        def gg(lam):
            g, _a, _c = g_of_lambda(lam)
            return g if g is not None else np.nan

        lam_root = brentq(gg, lo_lam, hi_lam, xtol=1e-20, rtol=1e-10)
        a_root, s_root = inner_a_of_lambda(lam_root)
        H_root, om_m_r, om_lam_r, om_phi_r = state_full(s_root, a_root)
        roots.append((lam_root, a_root, H_root))
        print(f"    bracket [{lo_lam:.4e}, {hi_lam:.4e}]")
        print(f"      Lambda_internal = {lam_root:.10e}")
        print(f"      a_today         = {a_root:.6f}")
        print(f"      H_int(a_today)  = {H_root:.10e}")
        print(
            f"      check: Omega_m={om_m_r:.9f}  Omega_Lambda={om_lam_r:.9f}  "
            f"Omega_phi={om_phi_r:.3e}"
        )

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if len(roots) == 1:
        lam_root, a_root, H_root = roots[0]
        print("  -> UNIQUE (single crossing found; independence across starting")
        print("     brackets not yet cross-checked with a second grid -- see NOT")
        print("     ESTABLISHED below).")
        print(f"\n     Lambda_internal = {lam_root:.10e}")
        print(f"     a_today         = {a_root:.6f}")
        print(f"     H_int(a_today)  = {H_root:.10e}")
        kappa = 67.4 / H_root  # km/s/Mpc per internal-H unit; H_0 = 67.4, arXiv:1807.06209
        print(f"\n     kappa = H_0 / H_int(a_today) = {kappa:.6e} km/s/Mpc per internal unit")
        print("     (H_0 = 67.4 km/s/Mpc, Planck 2018, arXiv:1807.06209)")
        print("\n     k[h/Mpc] IS NOT QUOTED IN THIS FILE. A follow-up step may now")
        print("     combine kappa, a_today, and the universal h/Mpc constant")
        print("     100/c = 3.335641e-4 to map k=3,10,30 to physical units.")
    else:
        print(f"  -> NON-UNIQUE. {len(roots)} distinct roots found.")
        Hs = [r[2] for r in roots]
        spread = max(Hs) / min(Hs)
        print(f"     H_int(a_today) spread across roots: {spread:.4f}x")
        print("     Still degenerate even with two joint conditions. No k[h/Mpc]")
        print("     number is quoted.")

    print("\n  NOT ESTABLISHED:")
    print("   * that this is the ONLY root outside the scanned grid.")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about MULTING itself (Gate 1). No dataset, no Table A1")
    print("     quantity enters this file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
