"""P29 -- direct verification (via Archidiacono et al.'s OWN quoted field
equations, arXiv:2204.08484, WebFetch-mediated, not general modified-gravity
literature) that their fifth-force model produces an ABSOLUTE growth
enhancement alongside the differential DM-baryon effect P22/P28 focused on
-- and a check on whether their DM-sourced/DM-received-only coupling
topology is the SAME functional structure as MULTING's own universal g
(P23's reading), or a genuinely different one.

This closes part of the gap FINDING_P28 (corrected) left open in its own
section 4 point 1 ("their actual constraint may derive from a more complete
analysis with additional channels... not checked here") -- now checked,
using the paper's own equations rather than general-literature plausibility
argument.
"""

import sympy as sp


def dm_only_poisson_source(G_N, beta, dlogm_ds, rho_chi_bar, delta_chi):
    """Archidiacono et al.'s own eq. (4.4), WebFetch-quoted:
    k^2 delta_s = -a^2 * 4*pi*G_N*beta*(dlogm/ds) * rho_chi_bar * delta_chi
    Schematic RHS (dropping k^2, a^2 -- irrelevant to the source-structure
    comparison below)."""
    return -4 * sp.pi * G_N * beta * dlogm_ds * rho_chi_bar * delta_chi


def universal_poisson_source(G_N, Delta_G, rho_tot, delta_tot):
    """A genuinely universal coupling (P23's reading of MULTING's g):
    sourced by the TOTAL matter perturbation, not DM alone."""
    return -4 * sp.pi * (G_N + Delta_G) * rho_tot * delta_tot


def baryon_growth_source_archidiacono(Omega_m, H, f_chi, delta_chi, delta_b):
    """Archidiacono et al.'s own quoted baryon equation (from eq. 4.16's
    system), WebFetch-quoted:
    delta_b'' + H*delta_b' - (3/2)*Omega_m*H^2*(f_chi*delta_chi + (1-f_chi)*delta_b) = 0
    Returns the source term only (RHS driving term)."""
    return sp.Rational(3, 2) * Omega_m * H**2 * (f_chi * delta_chi + (1 - f_chi) * delta_b)


def main():
    G_N, beta, dlogm_ds, rho_chi_bar, delta_chi, delta_b = sp.symbols(
        "G_N beta dlogm_ds rho_chi_bar delta_chi delta_b", positive=True
    )
    Delta_G, rho_tot, delta_tot = sp.symbols("Delta_G rho_tot delta_tot", positive=True)
    Omega_m, H, f_chi = sp.symbols("Omega_m H f_chi", positive=True)

    # --- Part 1: structural comparison, DM-only-sourced vs universal ---
    dm_only = dm_only_poisson_source(G_N, beta, dlogm_ds, rho_chi_bar, delta_chi)
    universal = universal_poisson_source(G_N, Delta_G, rho_tot, delta_tot)

    print("Archidiacono's own eq. 4.4 (schematic RHS):", dm_only)
    print("Universal-coupling Poisson source (schematic RHS):", universal)
    print()
    print("Does DM-only source contain a baryon (delta_b) term?", delta_b in dm_only.free_symbols)
    print(
        "Does universal source depend on delta_tot (= f_chi*delta_chi + (1-f_chi)*delta_b), "
        "i.e. does it structurally require a baryon contribution?",
        True,  # by construction: delta_tot is defined to include both species
    )
    assert delta_b not in dm_only.free_symbols
    print()
    print("CONSISTENT WITH WEBFETCH TRANSCRIPTION (not independent verification")
    print("of the source paper -- see FINDING_P29 section 1's correction): as")
    print("transcribed, Archidiacono's own eq. 4.4 has NO baryon term -- their")
    print("fifth force is sourced by dark matter density perturbations ONLY.")
    print("A universal coupling (P23's reading of g) is, by construction here,")
    print("sourced by the TOTAL matter perturbation -- if the transcription is")
    print("accurate, these are NOT the same functional form; one is not simply")
    print("a rescaled/relabeled version of the other. NOTE: 'universal' is a")
    print("hand-built comparison case, not itself fetched from any source.")

    # --- Part 2: does DM's enhanced growth feed into baryon growth via ---
    # --- ordinary gravity, even without a direct fifth-force term? ---
    baryon_source = baryon_growth_source_archidiacono(Omega_m, H, f_chi, delta_chi, delta_b)
    ddelta_chi = sp.diff(baryon_source, delta_chi)
    print()
    print("Baryon growth source (their own quoted eq., from the 4.16 system):", baryon_source)
    print("d(baryon source)/d(delta_chi) =", ddelta_chi)
    assert ddelta_chi != 0

    print()
    print("CONSISTENT WITH TRANSCRIPTION: baryons in Archidiacono's own model, as")
    print("quoted, respond to delta_chi via the STANDARD gravitational term, even")
    print("though they carry no direct fifth-force term of their own. This")
    print("derivative is trivially forced by the linear form as transcribed --")
    print("sympy confirms arithmetic, not the correctness of the transcription.")
    print("If the fifth force enhances delta_chi's own growth (via eq. 4.2's")
    print("Euler-equation term, not modeled here), that enhancement propagates to")
    print("baryons through ordinary gravity -- an absolute growth-of-structure")
    print("channel EXISTS in their own DM-only model (magnitude not addressed),")
    print("alongside the differential DM-baryon effect their abstract names as")
    print("the paper's primary novel signature. NOTE: this does NOT by itself say")
    print("anything about how a UNIVERSAL coupling would behave in their pipeline")
    print("-- see FINDING_P29 section 3's correction for why that link is a")
    print("non-sequitur, not a confirmation of FINDING_P28's retraction.")


if __name__ == "__main__":
    main()
