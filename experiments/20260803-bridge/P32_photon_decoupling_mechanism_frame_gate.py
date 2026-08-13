"""P32 -- the first, cleanly-derivable step of the mechanism-frame gate
user-flagged on FINDING_P31: does MULTING's own worldline-coupled scalar
force (g*m_i*phi, per two_field_action_closure.py) produce a DIRECT
coupling to a massless particle (photon), the way it would need to if it
were to move lensing/ISW the same way Bean & Tangmatitham's metric-level Q
modification does?

This is deliberately a NARROWER question than the user's full P32 spec
(deriving mu(a,k), gamma(a,k)=Phi/Psi, Sigma(a,k), G_matter(a,k) from a
full covariant action with an Einstein-Hilbert term) -- that full
derivation is real, substantial GR work this project has never attempted
before, and rushing it risks introducing new errors. This finding answers
the single most decisive, cheaply-checkable sub-question first, and
explicitly flags what remains open for the fuller derivation.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def worldline_coupling_term(g, m, phi):
    """P1's own coupling term (two_field_action_closure.py, verified this
    session): g*m_i*phi(x_i), the monopole piece of the worldline action.
    Linear in the particle's rest mass m_i."""
    return g * m * phi


def main():
    g, phi, m = sp.symbols("g phi m", positive=False)

    print("=" * 78)
    print("P32 -- photon-decoupling check, mechanism-frame gate (partial)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] MULTING's own worldline coupling term (P1's action, verified")
    print("  this session by direct re-read of two_field_action_closure.py):")
    coupling = worldline_coupling_term(g, m, phi)
    print(f"  L_coupling = g * m_i * phi = {coupling}")
    print("  Linear in rest mass m_i -- this is the ENTIRE direct coupling of the")
    print("  monopole sector to matter; no other direct matter-phi term exists in")
    print("  the quoted action.")

    print("\n[STEP 2] Massless-particle limit (photon, m_i -> 0):")
    photon_coupling = coupling.subs(m, 0)
    print(f"  L_coupling(m=0) = {photon_coupling}")
    assert photon_coupling == 0
    print("  CONFIRMED: identically zero. A massless particle has ZERO direct")
    print("  coupling to phi via this term, for ANY value of g or phi -- this is")
    print("  forced by the coupling's own linear-in-mass structure, not assumed.")

    print("\n[STEP 3] Consequence for the direct-coupling channel:")
    print("  The SAME mechanism that produces the growth-equation modification")
    print("  (Delta_G, P30) -- a direct worldline force proportional to mass --")
    print("  produces EXACTLY ZERO direct force on photons. Photons do not")
    print("  directly feel g*m_i*phi, unlike the case in Bean & Tangmatitham's")
    print("  own (Q,R) framework, where Q modifies the METRIC Poisson equation")
    print("  itself -- a quantity BOTH matter and light are sourced by/move")
    print("  through equally, per standard GR geodesics.")

    print("\n[STEP 4] What this does NOT settle -- a SEPARATE, indirect channel:")
    print("  phi itself carries stress-energy (from its own kinetic term,")
    print("  (1/2)(d phi)^2 in the action) -- in ANY standard-GR completion of")
    print("  this action (implicit throughout this project, since no modified")
    print("  Einstein-Hilbert term has ever been written down here), phi's own")
    print("  stress-energy T_munu^(phi) SOURCES Einstein's equations, exactly")
    print("  like any other field's energy density. This is a genuinely SEPARATE,")
    print("  INDIRECT channel through which phi COULD still perturb the metric")
    print("  (and hence photons, via standard lensing) -- NOT ruled out by the")
    print("  direct-coupling-vanishes result above. Whether this backreaction")
    print("  channel produces a lensing signal comparable in size to the direct")
    print("  growth-equation Delta_G is NOT addressed here -- it requires the")
    print("  full covariant-action derivation (Einstein equations + scalar")
    print("  equation + matter equation simultaneously) the user's own P32 spec")
    print("  calls for, not attempted in this narrower first step.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("CONFIRMED (narrow, first step only): MULTING's own worldline coupling")
    print("g*m_i*phi gives photons EXACTLY ZERO direct coupling (massless limit),")
    print("a structural consequence of the coupling's own linear-in-mass form,")
    print("verified symbolically. This SUPPORTS, but does not fully PROVE, the")
    print("user-flagged concern that MULTING's own mechanism may leave lensing/ISW")
    print("unaffected while growth is modified -- a genuine divergence from Bean &")
    print("Tangmatitham's own (Q,R) phenomenology, IF the direct-coupling channel")
    print("is the whole story. NOT settled: phi's own gravitational backreaction")
    print("(indirect channel, via its stress-energy sourcing Einstein's equations)")
    print("could still produce SOME lensing signal -- unaddressed here, the")
    print("natural next, larger step for a future finding.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
