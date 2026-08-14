"""P32 -- the mechanism-frame gate user-flagged on FINDING_P31: does
MULTING's own worldline-coupled scalar force (g*m_i*phi, per
two_field_action_closure.py) produce a DIRECT coupling to a massless
particle (photon), the way it would need to if it were to move
lensing/ISW the same way Bean & Tangmatitham's metric-level Q modification
does?

This is deliberately a NARROWER question than the user's full P32 spec
(deriving mu(a,k), gamma(a,k)=Phi/Psi, Sigma(a,k), G_matter(a,k) from a
full covariant action with an Einstein-Hilbert term) -- that full
derivation is real, substantial GR work this project has never attempted
before, and rushing it risks introducing new errors. This finding checks
two complementary, cheap arguments and explicitly flags what remains open
for the fuller derivation.

CORRECTED 2026-08-14, after context-blind skeptic review, same day. FOUR
real issues fixed, not just framing:
  (1) THE OVERCLAIM -- the original script's Step 1 said "no other direct
      matter-phi term exists in the quoted action." This is false: the
      action's own text (two_field_action_closure.py line 113) reads
      "sum_i int dtau [ g m_i + p_i . grad ] phi(x_i), p_i = kappa k_i
      r_i/c^2" -- a SECOND, dipole/k-charge coupling term, not
      proportional to mass, exists in the SAME quoted action. Fixed below:
      explicitly acknowledged, and scoped -- this finding is about the
      MONOPOLE (g) sector specifically, since that is the ONLY sector
      implicated in the ΔG/growth-equation story (P21's A*g^2=4*pi*ΔG;
      P30's growth equation) that Bean & Tangmatitham's Q addresses. The
      dipole/kappa sector is a genuinely SEPARATE mechanism (P18-P20's own
      analysis), not at stake in the Bean-Q-mapping question this finding
      investigates -- but whether photons carry zero k-charge too is
      flagged explicitly as an OPEN, UNVERIFIED assumption, not asserted.
  (2) DERIVATION RIGOR -- naively substituting m=0 into a term written as
      an integral over PROPER TIME (dtau) is not rigorous: proper time is
      degenerate (dtau=0) along a null (photon) worldline, so "dtau [g*m]"
      is a 0*(anything) form in that parametrization, not a well-defined
      limit. Fixed below: the rigorous argument uses an affine parameter
      instead of proper time (standard for massless-particle actions,
      e.g. via an einbein formulation) -- for a coupling LINEAR in m at
      FIXED particle energy E, the term scales as m^2*c^2/E (via
      m*dtau -> (m^2*c^2/E)*dlambda), which vanishes as m->0 at any fixed
      E. Same conclusion, rigorous route, not a naive substitution.
  (3) A CHEAPER, MORE DECISIVE ARGUMENT WAS MISSED -- Bean & Tangmatitham's
      own phi (their eq. 6) is a METRIC potential (a Newtonian-gauge
      perturbation to the metric itself, paired with a second potential
      psi via their own eq. 7 slip relation R) -- it carries NO independent
      kinetic term of its own; it is part of the geometry, not a separate
      matter-sector field. MULTING's own phi (two_field_action_closure.py)
      is a CANONICAL SCALAR FIELD with its own kinetic term (1/2)(d phi)^2,
      appearing as an ADDITIONAL matter-sector degree of freedom coupled to
      matter's worldline -- structurally a different KIND of object. This
      definitional mismatch is checkable by inspection of what each
      framework's own "phi" symbol denotes, requires no assumption about
      which particles carry which MULTING charges, and is arguably CHEAPER
      and MORE decisive than the photon-coupling argument -- added below as
      an independent, complementary check.
  (4) LOGICAL OVERCLAIM in the original VERDICT -- "supports (does not
      fully prove)" implied the direct-channel-zero result shifts the
      probability of the ultimate lensing question. But with the
      backreaction channel (Step 4 below) completely unbounded, 0 (direct)
      + unknown (backreaction) = unknown (total) -- the direct result alone
      does not license "supports." Corrected below to "is consistent with"
      /"is a necessary but not sufficient condition for."
"""

import sympy as sp


def worldline_coupling_term(g, m, phi):
    """P1's own MONOPOLE coupling term (two_field_action_closure.py,
    verified this session): g*m_i*phi(x_i). Scoped explicitly to the
    monopole sector -- the action's own text also contains a SEPARATE
    dipole/k-charge term (p_i . grad phi, p_i = kappa*k_i*r_i/c^2), not
    analyzed here (see module docstring point 1)."""
    return g * m * phi


def einbein_scaling_term(m, c, E):
    """Rigorous massless-particle limit via an affine-parameter (einbein)
    argument, replacing the naive m->0 substitution into a proper-time
    integral (proper time is degenerate for null worldlines). For a
    coupling linear in m, m*dtau ~ (m^2*c^2/E)*dlambda at fixed particle
    energy E (dtau = dlambda/gamma, gamma = E/(m*c^2) for m>0) -- this
    scaling, not the bare coupling, is what must vanish as m -> 0."""
    return (m**2 * c**2) / E


def main():
    g, phi, m, c, E = sp.symbols("g phi m c E", positive=True)

    print("=" * 78)
    print("P32 -- photon-decoupling + definitional-mismatch check (CORRECTED)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[PART A -- Step 1] MULTING's own MONOPOLE coupling term (P1's action,")
    print("  re-verified this session). NOTE: the action's own text also has a")
    print("  SEPARATE dipole/k-charge term (p_i . grad phi) -- NOT analyzed here,")
    print("  scoped out because it is a genuinely different mechanism, unrelated")
    print("  to the Delta_G/growth-equation story Bean & Tangmatitham's Q addresses:")
    coupling = worldline_coupling_term(g, m, phi)
    print(f"  L_monopole = g * m_i * phi = {coupling}")
    print("  Linear in rest mass m_i. Whether photons carry zero k-charge (the")
    print("  SEPARATE dipole coupling) is an OPEN, UNVERIFIED assumption, not")
    print("  asserted here -- flagged explicitly, not silently ignored.")

    print("\n[PART A -- Step 2] Rigorous massless limit via affine parameter (NOT a")
    print("  naive m->0 substitution into the proper-time integral, which is")
    print("  ill-defined for a null worldline -- dtau=0 identically for a photon):")
    scaling = einbein_scaling_term(m, c, E)
    print("  m*dtau -> (m^2*c^2/E)*dlambda  (fixed particle energy E)")
    print(f"  scaling term = {scaling}")
    limit_at_m0 = sp.limit(scaling, m, 0)
    print(f"  limit as m -> 0 (fixed E): {limit_at_m0}")
    assert limit_at_m0 == 0
    print("  CONFIRMED via the rigorous route: the coupling's contribution to the")
    print("  action vanishes as m->0 at fixed E -- same conclusion as the naive")
    print("  substitution, reached without relying on an ill-defined limit.")

    print("\n[PART A -- Step 3] Consequence for the direct-coupling channel:")
    print("  The MONOPOLE mechanism that produces the growth-equation modification")
    print("  (Delta_G, P30) gives photons ZERO direct force, via the rigorous")
    print("  affine-parameter argument above -- IF photons carry zero k-charge")
    print("  (unverified, Part A Step 1). Bean & Tangmatitham's own Q, by")
    print("  contrast, modifies a METRIC potential that both matter and light")
    print("  move through equally by construction (see Part B).")

    print("\n[PART B] A cheaper, independent, definitional-mismatch check:")
    print("  Bean & Tangmatitham's own phi (their eq. 6, per FINDING_P31) is a")
    print("  METRIC potential -- part of the perturbed spacetime geometry itself,")
    print("  paired with a second potential via their own eq. 7 slip relation R,")
    print("  carrying NO independent kinetic term of its own.")
    print("  MULTING's own phi (two_field_action_closure.py) is a CANONICAL SCALAR")
    print("  FIELD with its own kinetic term (1/2)(d phi)^2 -- an ADDITIONAL")
    print("  matter-sector degree of freedom, not part of the metric.")
    print("  These are DIFFERENT KINDS of object under the same symbol name --")
    print("  this mismatch requires no assumption about photon/k-charge coupling")
    print("  at all, and is a cheaper, independent reason the direct Q<->A*g^2")
    print("  identification (P22, P31) needs the mechanism-frame caveat already")
    print("  recorded there.")

    print("\n[STEP 4] What Part A+B do NOT settle -- a SEPARATE, indirect channel:")
    print("  phi itself carries stress-energy (from its own kinetic term) -- in")
    print("  ANY standard-GR completion of this action (implicit throughout this")
    print("  project, no modified Einstein-Hilbert term ever written down here),")
    print("  phi's own stress-energy T_munu^(phi) SOURCES Einstein's equations,")
    print("  exactly like any other field's energy density -- a genuinely SEPARATE,")
    print("  INDIRECT, UNBOUNDED channel through which phi could still perturb the")
    print("  metric (hence photons, via standard lensing). NOT addressed here.")

    print("\n" + "=" * 78)
    print("VERDICT -- CORRECTED after context-blind skeptic review, same day")
    print("=" * 78)
    print("Part A (rigorous, conditional on photons carrying zero k-charge,")
    print("unverified) and Part B (definitional mismatch, unconditional, cheaper)")
    print("are two INDEPENDENT reasons Bean & Tangmatitham's Q cannot simply be")
    print("identified with MULTING's own A*g^2 without further work. NEITHER")
    print("'supports' the lensing-unaffected conclusion in a probability-shifting")
    print("sense -- with Step 4's backreaction channel completely UNBOUNDED,")
    print("0 (direct) + unknown (backreaction) = unknown (total). Correct verb:")
    print("Part A/B are each CONSISTENT WITH, and a NECESSARY but NOT SUFFICIENT")
    print("condition for, MULTING's mechanism leaving lensing/ISW unaffected --")
    print("not evidence that shifts the probability either way. FINDING_P31's")
    print("status (phenomenological soft ceiling) remains unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
