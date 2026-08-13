"""P28 -- does Archidiacono et al.'s own constraint-generating observable
(relative DM-baryon density/velocity perturbations, arXiv:2204.08484 abstract,
re-verified this finding via direct WebFetch) register a universal
(composition-independent) fifth-force coupling, the way P25 established
equivalence-principle tests structurally cannot?

Toy model: standard sub-horizon linear growth equations for two matter
species (CDM density contrast delta_c, baryon density contrast delta_b),
sourced by a common Poisson-type term ~ 4*pi*G_eff*rho_tot (schematic --
this is the source-term structure common to Newtonian linear perturbation
theory, e.g. Dodelson "Modern Cosmology" ch.7, not a full relativistic
Boltzmann solve).

Claim under test: does a UNIVERSAL G_eff shift (same for both species)
survive in the EQUATION OF MOTION for the RELATIVE quantity delta_c-delta_b
-- the quantity Archidiacono's own abstract says their method constrains --
or does it cancel, leaving only a DM-only shift as detectable?
"""

import sympy as sp


def source_term(G_eff, rho_tot, pi):
    """Schematic linear-growth source term S = 4*pi*G_eff*rho_tot."""
    return 4 * pi * G_eff * rho_tot


def relative_source_difference(G_eff_c, G_eff_b, rho_tot, pi):
    """Source term for the RELATIVE growth equation (delta_c - delta_b)'' + ...
    = S_c - S_b. This is what Archidiacono's own DM-baryon relative
    perturbation observable is sourced by."""
    S_c = source_term(G_eff_c, rho_tot, pi)
    S_b = source_term(G_eff_b, rho_tot, pi)
    return sp.simplify(S_c - S_b)


def main():
    G, Delta_G_universal, Delta_G_dm_only, rho_tot, pi = sp.symbols(
        "G Delta_G_universal Delta_G_dm_only rho_tot pi", positive=True
    )

    # Case 1: universal (composition-independent) coupling -- P23's own
    # established reading of g -- SAME G_eff for CDM and baryons.
    G_eff_c_universal = G + Delta_G_universal
    G_eff_b_universal = G + Delta_G_universal
    diff_universal = relative_source_difference(G_eff_c_universal, G_eff_b_universal, rho_tot, pi)

    # Case 2: DM-only coupling -- Archidiacono et al.'s own actual model
    # (baryons unaffected by the extra interaction).
    G_eff_c_dmonly = G + Delta_G_dm_only
    G_eff_b_dmonly = G
    diff_dmonly = relative_source_difference(G_eff_c_dmonly, G_eff_b_dmonly, rho_tot, pi)

    print("Universal coupling -- source term for (delta_c - delta_b):", diff_universal)
    print("DM-only coupling   -- source term for (delta_c - delta_b):", diff_dmonly)
    print()
    print("Universal source term is identically zero:", diff_universal == 0)
    print("DM-only source term is nonzero:", diff_dmonly != 0)

    assert diff_universal == 0, "universal coupling must cancel from the relative equation"
    assert diff_dmonly != 0, "DM-only coupling must survive in the relative equation"
    assert sp.simplify(diff_dmonly - 4 * pi * rho_tot * Delta_G_dm_only) == 0

    print()
    print("CONFIRMED: a universal G_eff shift is invisible to the delta_c-delta_b")
    print("channel; only a species-DEPENDENT shift (Archidiacono's actual model)")
    print("sources it. Same structural blindness pattern as P25's EP-test result.")


if __name__ == "__main__":
    main()
