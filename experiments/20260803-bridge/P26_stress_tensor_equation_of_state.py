"""P26_stress_tensor_equation_of_state.py -- the "Level 3" step this
project's own 2026-08-03 finding (FINDING_effective_fluid_energy_scale.md)
named as "the only surviving route": derive the k-sector's stress-energy
tensor T_mu_nu directly from the action's own canonical kinetic term, and
extract rho_phi, p_phi -- NOT the old manual force-to-H(z) bridge.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive

CONTEXT CHAIN (all previously established in this project, cited not
re-derived):
  1. FINDING_effective_fluid_energy_scale.md (2026-08-03): the naive
     statistical-mechanics "pair-fluid" bridge (MULTING potential ->
     Layzer-Irvine energy -> rho_pair -> H(z)) fails by 4-5 orders of
     magnitude. Concludes: "the covariant-action route of level 3 ... [is]
     the only surviving route."
  2. two_field_action_closure.py / FINDING_P1 Sec 4.3 (2026-08-10): the
     FORCE on a test particle from an isotropic/randomly-oriented shell of
     dipoles averages to EXACTLY ZERO (a "double layer", proven in
     FINDING_dipole_shell_is_a_double_layer.md) -- a narrower, FIRST-MOMENT
     result, about forces, not energy density.
  3. FINDING_P13a (2026-08-12), corrected: explicitly flags that a zero
     mean FORCE (first moment, <delta>=0) does NOT imply zero ENERGY
     DENSITY or power spectrum (second moment, P(k)=0) -- names this the
     genuinely open next calculation.
  4. FINDING_P14 (2026-08-12): computes the self-energy channel, but its
     own corrected Sec 1 flags a real, UNRESOLVED tension -- does the
     self-energy channel survive ensemble averaging, or does it exactly
     cancel against cross-terms the way P9's idealized CONTINUOUS shell
     does?
  5. FINDING_P15/P16 (2026-08-12): RESOLVE that tension for realistic,
     DISCRETE (not idealized-continuous) populations -- self-energy is
     real and DOMINANT over cross-terms (by ~4e-5 to 1.4e-4) at realistic
     cluster separations. The continuum cancellation P9 found does not
     extend to the physically realistic discrete case.

Given (5) resolves (4)'s tension in favor of "self-energy survives," this
script does what was flagged as open since (3): compute T_mu_nu for the
scalar field's own gradient energy directly, extract rho_phi=T_00 and the
effective pressure from T_ij, and derive the equation of state w=p/rho --
the piece needed to know whether this channel is even STRUCTURALLY capable
of behaving like dark energy (w<-1/3, accelerates expansion) as opposed to
matter (w=0) or curvature (w=-1/3, no net effect on acceleration).

METHOD: canonical stress tensor T_mu_nu = d_mu(phi) d_nu(phi) -
eta_mu_nu*(1/2)(d phi)^2 for the action's own (1/2)(d phi)^2 kinetic term
(two_field_action_closure.py line 111), static limit (consistent with
every finding P9-P25). First prove the GENERAL identity
Trace(T_ij) = -T_00 (3D, ANY static profile -- not special to the dipole),
then apply to the P19-normalized dipole field, cross-check the volume
integral of T_00 against P14's own already-verified E_self formula as a
positive control.
"""

from __future__ import annotations

import sympy as sp

r, theta, p, r_min = sp.symbols("r theta p r_min", positive=True)


def general_trace_identity() -> bool:
    """Prove Trace(T_ij) = -T_00 for an ARBITRARY static scalar profile
    f(r,theta) -- not just the dipole -- confirming this is a structural
    fact about the canonical stress tensor in 3D, not a coincidence of the
    dipole's specific angular form."""
    f = sp.Function("f")(r, theta)
    dfr = sp.diff(f, r)
    dftheta_over_r = sp.diff(f, theta) / r
    g2 = dfr**2 + dftheta_over_r**2
    t00 = sp.Rational(1, 2) * g2
    t_rr = dfr**2 - sp.Rational(1, 2) * g2
    t_thth = dftheta_over_r**2 - sp.Rational(1, 2) * g2
    t_phph = -sp.Rational(1, 2) * g2
    trace = sp.simplify(t_rr + t_thth + t_phph)
    return sp.simplify(trace - (-t00)) == 0


def dipole_stress_tensor():
    """T_00, T_rr, T_thth, T_phph for P19's normalized dipole potential
    phi = p*cos(theta)/(4*pi*r^2)."""
    phi = p * sp.cos(theta) / (4 * sp.pi * r**2)
    dphidr = sp.diff(phi, r)
    dphidtheta_over_r = sp.diff(phi, theta) / r
    grad2 = sp.simplify(dphidr**2 + dphidtheta_over_r**2)
    t00 = sp.Rational(1, 2) * grad2
    t_rr = sp.simplify(dphidr**2 - sp.Rational(1, 2) * grad2)
    t_thth = sp.simplify(dphidtheta_over_r**2 - sp.Rational(1, 2) * grad2)
    t_phph = sp.simplify(0 - sp.Rational(1, 2) * grad2)
    return t00, t_rr, t_thth, t_phph


def volume_integrate_t00(t00_expr) -> sp.Expr:
    """Integrate T_00 over r>=r_min, all solid angle -- gives the
    canonically-normalized field self-energy (rho_phi contribution)."""
    integrand = t00_expr * r**2 * sp.sin(theta)
    inner = sp.simplify(sp.integrate(integrand, (theta, 0, sp.pi)))
    return sp.simplify(sp.integrate(inner, (r, r_min, sp.oo)) * 2 * sp.pi)


def main() -> int:
    print("=" * 78)
    print("P26 -- stress tensor T_mu_nu, rho_phi, p_phi, equation of state w")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] GENERAL identity: Trace(T_ij) = -T_00 for ANY static")
    print("  scalar profile in 3D (not special to the dipole) -- this is what")
    print("  makes w=-1/3 a STRUCTURAL fact, robust under any subsequent")
    print("  averaging, not a fragile feature of one specific field shape.")
    identity_holds = general_trace_identity()
    print(f"  Trace(T_ij) = -T_00 verified for generic f(r,theta): {identity_holds}")
    if not identity_holds:
        print("  STOP -- the general identity does not hold, w is not -1/3.")
        return 1

    print("\n[STEP 2] Apply to P19-normalized dipole field phi=p*cos(theta)/(4*pi*r^2)")
    t00, t_rr, t_thth, t_phph = dipole_stress_tensor()
    print(f"  T_00     = {t00}")
    print(f"  T_rr     = {t_rr}")
    print(f"  T_thth   = {t_thth}")
    print(f"  T_phph   = {t_phph}")
    trace = sp.simplify(t_rr + t_thth + t_phph)
    print(f"  Trace(T_ij) = {trace}")
    w_pointwise = sp.simplify(sp.Rational(1, 3) * trace / t00)
    print(f"  w = (1/3)*Trace(T_ij)/T_00 = {w_pointwise}  (POINTWISE, angle-independent)")
    if w_pointwise != sp.Rational(-1, 3):
        print("  STOP -- w is not exactly -1/3, re-check the algebra.")
        return 1

    print("\n[STEP 3] Positive control -- cross-check against P14's OWN already")
    print("  skeptic-verified E_self formula, using P14's OWN (pre-P19,")
    print("  un-normalized) convention phi=p*cos(theta)/r^2, WITHOUT the 1/2")
    print("  canonical-energy factor (matching how P14 itself computed it,")
    print("  per its own Sec.1 text: 'the total field energy ... d^3x', no 1/2).")
    phi_old = p * sp.cos(theta) / r**2
    dphidr_old = sp.diff(phi_old, r)
    dphidtheta_old = sp.diff(phi_old, theta) / r
    grad2_old = sp.simplify(dphidr_old**2 + dphidtheta_old**2)
    bare_integrand = grad2_old * r**2 * sp.sin(theta)
    bare_inner = sp.simplify(sp.integrate(bare_integrand, (theta, 0, sp.pi)))
    e_self_bare = sp.simplify(sp.integrate(bare_inner, (r, r_min, sp.oo)) * 2 * sp.pi)
    p14_formula = sp.Rational(8, 3) * sp.pi * p**2 / r_min**3
    print(f"  integral of bare |grad(phi)|^2 dV (no 1/2, old convention) = {e_self_bare}")
    print(f"  P14's own formula (8*pi/3)*p^2/r_min^3                     = {p14_formula}")
    control_match = sp.simplify(e_self_bare - p14_formula) == 0
    print(f"  Match: {control_match}")
    if not control_match:
        print("  STOP -- positive control fails, methodology does not reproduce")
        print("  P14's own already-verified result.")
        return 1

    print("\n[STEP 4] CORRECTED E_self -- canonical (1/2 factor) AND P19-normalized")
    print("  (1/(4*pi) in phi) together. NOT computed identically anywhere before.")
    e_self_correct = volume_integrate_t00(t00)
    print(f"  E_self (canonical + P19-normalized) = {e_self_correct}")
    ratio_to_p14 = sp.simplify(e_self_correct / p14_formula)
    print(f"  Ratio to P14's original bare, un-normalized formula: {ratio_to_p14}")
    print("  -> combines P19's already-known 1/(4*pi)^2 geometric correction")
    print("     WITH a previously-unflagged factor of 1/2 from the canonical")
    print("     (1/2)(grad phi)^2 energy density vs. the bare |grad phi|^2 this")
    print("     project's E_self calculations (P14-P20) have used throughout.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("CONFIRMED (structural, sympy-verified, general + specific): the")
    print("k-sector's own field-gradient stress-energy has w = p/rho = -1/3")
    print("EXACTLY, pointwise, for ANY static profile -- hence for the")
    print("volume-integrated rho_phi=n*E_self too (the pointwise relation")
    print("P(x)=-(1/3)*rho(x) survives any linear averaging/integration).")
    print("This is the CURVATURE equation of state (rho+3p=0 identically --")
    print("ZERO net contribution to the Friedmann ACCELERATION equation),")
    print("NOT dark-energy-like (would need w<-1/3). rho_phi is REAL and")
    print("nonzero (P15/P16 already resolved P14's own tension in its favor),")
    print("genuinely derived from T_mu_nu this time, not the old force-based")
    print("or statistical-mechanics bridges -- but it behaves like curvature,")
    print("not dark energy.")
    print()
    print("Also found (Step 3-4): a previously-unflagged factor-of-2 in P14's")
    print("own E_self convention (bare |grad phi|^2, not the canonical (1/2)")
    print("factor) -- on top of P19's already-known 1/(4*pi) normalization gap.")
    print("Corrected E_self = p^2/(12*pi*r_min^3), a factor 32*pi^2 smaller than")
    print("P14's original printed number. Does not change any qualitative")
    print("conclusion (Omega_phi's ABSOLUTE scale was already blocked by A,")
    print("kappa being individually unknown, per P17/P21/P22) -- this is one")
    print("more, now-identified, order-unity factor to fold in whenever that")
    print("gap is eventually resolved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
