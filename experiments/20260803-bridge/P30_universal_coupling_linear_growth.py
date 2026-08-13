"""P30 -- derive the universal-coupling analogue of Archidiacono et al.'s
own linear-growth equations (P29's own quoted baryon growth equation is the
template), replacing their DM-only fifth-force topology with a genuinely
universal (source-democratic, mass-proportional-for-every-species) coupling
-- the reading P23 established for MULTING's own g.

User-specified target (2026-08-13, following the P22 4pi correction):
    delta_m'' + ... = 4*pi*G_eff*rho_m*delta_m,   G_eff = G_N + Delta_G

This is the honest equation needed BEFORE asking what CMB/lensing/growth-
rate bounds constrain Delta_G/G_N -- that numeric-bound search is the next,
separate step (not attempted here).

CORRECTED 2026-08-13, after context-blind skeptic review, same day. Two
real issues fixed, not just framing:
  (1) The original Step 2/3 called the SAME function with IDENTICAL
      arguments for both "S_chi" and "S_baryon", then "verified" they were
      equal -- a syntactic tautology (f(x)-f(x)==0), not a discovered fact.
      Rewritten below to make the DEFINITIONAL nature of "universal
      coupling" explicit (both species get the SAME G_eff BY CONSTRUCTION,
      stated plainly, not dressed as a derived check) and to add a genuinely
      non-trivial check instead: that Archidiacono's OWN DM-only model gives
      a DIFFERENT G_eff for the two species (a real asymmetry, matching
      P29's own established facts), contrasted with the universal case.
  (2) P29's own quoted baryon equation uses conformal time (primed
      derivatives, single-H-Hubble friction) -- the standard identity for
      that convention is (3/2)*Omega_m*(script_H)^2 = 4*pi*G_N*rho_m*a^2
      (WITH a scale-factor-squared term), not 4*pi*G_N*rho_m (which is the
      COSMIC-time identity). The original script conflated conformal and
      cosmic Hubble. Fixed below by keeping 'a' explicit throughout, so the
      identity used is dimensionally and conventionally consistent.
"""

import sympy as sp


def dm_only_effective_G(G_N, Delta_G, species):
    """Archidiacono's own DM-only topology (P29's own finding): chi gets an
    enhanced G_eff = G_N + Delta_G (their eq. 4.2's fifth-force term);
    baryons get ONLY G_N -- P29's own quoted baryon equation has no
    fifth-force/delta_s term at all. This is a genuine, checkable
    ASYMMETRY, not a definition."""
    if species == "chi":
        return G_N + Delta_G
    return G_N


def universal_effective_G(G_N, Delta_G, species):
    """The universal-coupling replacement (P23's reading of MULTING's g):
    BOTH species get the SAME enhanced G_eff. This is the DEFINITION of
    'universal' -- stated as such, not presented as a derived result."""
    return G_N + Delta_G


def source_term(G_eff, rho_m, a, f_chi, delta_chi, delta_b):
    """Standard conformal-time sub-horizon source term:
    (3/2)*Omega_m*(script_H)^2 = 4*pi*G_N*rho_m*a^2 (script_H = conformal
    Hubble = a*H_cosmic; the a^2 is required by this identity, corrected
    after skeptic review -- see module docstring). Sourced by the TOTAL
    matter combination f_chi*delta_chi + (1-f_chi)*delta_b, standard for
    gravity itself (both species fall in the same potential)."""
    return 4 * sp.pi * G_eff * rho_m * a**2 * (f_chi * delta_chi + (1 - f_chi) * delta_b)


def main():
    G_N, Delta_G, rho_m, f_chi, a = sp.symbols("G_N Delta_G rho_m f_chi a", positive=True)
    delta_chi, delta_b, delta_m = sp.symbols("delta_chi delta_b delta_m")

    print("=" * 78)
    print("P30 -- universal-coupling linear-growth equations (CORRECTED)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Archidiacono's own DM-only topology (P29): is G_eff genuinely")
    print("  DIFFERENT between species? A real, checkable asymmetry, not assumed.")
    g_eff_chi_dmonly = dm_only_effective_G(G_N, Delta_G, "chi")
    g_eff_b_dmonly = dm_only_effective_G(G_N, Delta_G, "b")
    print(f"  G_eff_chi (DM-only case) = {g_eff_chi_dmonly}")
    print(f"  G_eff_b   (DM-only case) = {g_eff_b_dmonly}")
    dmonly_diff = sp.simplify(g_eff_chi_dmonly - g_eff_b_dmonly)
    print(f"  G_eff_chi - G_eff_b = {dmonly_diff} (nonzero -- genuine asymmetry)")
    assert dmonly_diff == Delta_G

    print("\n[STEP 2] Universal-coupling replacement (P23's reading of MULTING's g):")
    print("  BOTH species get the SAME G_eff. This is the DEFINITION of 'universal',")
    print("  stated plainly -- NOT a result derived from anything below.")
    g_eff_chi_universal = universal_effective_G(G_N, Delta_G, "chi")
    g_eff_b_universal = universal_effective_G(G_N, Delta_G, "b")
    print(f"  G_eff_chi (universal case) = {g_eff_chi_universal}")
    print(f"  G_eff_b   (universal case) = {g_eff_b_universal}")

    print("\n[STEP 3] Source terms for each species (conformal-time convention,")
    print("  a^2 included -- see module docstring for the corrected identity):")
    source_chi_universal = source_term(g_eff_chi_universal, rho_m, a, f_chi, delta_chi, delta_b)
    source_b_universal = source_term(g_eff_b_universal, rho_m, a, f_chi, delta_chi, delta_b)
    print(f"  S_chi (universal) = {source_chi_universal}")
    print(f"  S_b   (universal) = {source_b_universal}")
    identical = sp.simplify(source_chi_universal - source_b_universal) == 0
    print("  S_chi - S_b == 0 (follows algebraically from Step 2's definition,")
    print(f"  not an independent discovery): {identical}")
    if not identical:
        print("  STOP -- construction error, sources should be equal by definition.")
        return 1

    print("\n[STEP 4] Consequence: given matched (adiabatic) initial conditions,")
    print("  delta_chi(t) = delta_b(t) for all time -- identical sources with")
    print("  identical initial data give identical solutions to identical linear")
    print("  ODEs. The SAME conclusion P28 reached follows here from encoding the")
    print("  SAME defining assumption (universal = identical G_eff for both")
    print("  species) in a different template (Archidiacono's own quoted baryon")
    print("  equation, via P29, rather than P28's earlier simplified toy) -- this")
    print("  is NOT an independent re-confirmation, since both derivations share")
    print("  the identical load-bearing assumption.")

    print("\n[STEP 5] Combined single-species equation for total matter delta_m")
    print("  := f_chi*delta_chi + (1-f_chi)*delta_b. Since delta_chi=delta_b=delta_m")
    print("  under universal coupling (Step 4), substitute directly:")
    G_eff = G_N + Delta_G
    delta_m_source = source_chi_universal.subs({delta_chi: delta_m, delta_b: delta_m})
    delta_m_source_simplified = sp.simplify(delta_m_source)
    print(f"  S_m = S_chi with delta_chi=delta_b=delta_m substituted: {delta_m_source}")
    print(f"  Simplified: {delta_m_source_simplified}")

    target = 4 * sp.pi * G_eff * rho_m * a**2 * delta_m
    matches_target = sp.simplify(delta_m_source_simplified - target) == 0
    print(f"\n  Target form (a^2 included): 4*pi*G_eff*rho_m*a^2*delta_m = {sp.expand(target)}")
    print(f"  S_m - target == 0 (symbolic check): {matches_target}")
    if not matches_target:
        print("  STOP -- does not reduce to the target single-species form.")
        return 1

    print("\n[STEP 6] Schematic growth equation (conformal-time convention,")
    print("  friction term NOT independently re-derived -- carried through by")
    print("  convention only, per this project's own honest-scope discipline):")
    print("  delta_m'' + script_H*delta_m' = 4*pi*G_eff*rho_m*a^2*delta_m")
    print("  G_eff = G_N + Delta_G, valid in the sub-Compton (r<<1/m_phi),")
    print("  scale-independent, time-independent-Delta_G regime only (see finding")
    print("  section 4 for the full list of regime restrictions).")

    print("\n" + "=" * 78)
    print("VERDICT -- CORRECTED after context-blind skeptic review, same day")
    print("=" * 78)
    print("(1) Archidiacono's own DM-only model gives a GENUINE, checked asymmetry")
    print("(G_eff_chi != G_eff_b). (2) A universal coupling makes G_eff equal BY")
    print("DEFINITION -- stated as such, not verified as a discovery. (3) Given")
    print("that definition, the source terms are equal (follows algebraically,")
    print("not independently). (4) The combined delta_m equation reduces to the")
    print("standard conformal-time growth form WITH the a^2 factor this project's")
    print("earlier version had dropped by conflating conformal and cosmic Hubble.")
    print("This is a SCHEMATIC target for a future literature search on Delta_G/")
    print("G_N bounds -- translating into the mu(a,k)/Sigma(a,k) parametrization")
    print("standard modified-gravity literature actually uses is real, non-trivial")
    print("work not attempted here, not a straightforward lookup.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
