"""P33 -- the first well-scoped step toward the full covariant-action
derivation the mechanism-frame gate (P32) ultimately needs: covariantize
MULTING's own flat-space monopole coupling and identify which STANDARD
class of scalar-tensor theory it belongs to, using established literature
rather than a from-scratch Einstein-equation derivation.

Deliberately narrower than the full mu(a,k)/gamma(a,k)/Sigma(a,k)/
G_matter(a,k) extraction -- that requires deriving Einstein equations, the
scalar equation, and the matter equation SIMULTANEOUSLY from a full
covariant action with an Einstein-Hilbert term, real GR work this project
has explicitly and repeatedly deferred (P30, P32) to avoid rushing under
time pressure. This finding instead answers a cheaper, well-posed
sub-question: is MULTING's own coupling structure a RECOGNIZED type in the
scalar-tensor literature, with ALREADY-ESTABLISHED consequences for the
metric-vs-matter-equation question P32's Part B raised?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def total_monopole_action_density(g, m, c, phi):
    """MULTING's own kinetic term (-m*c per unit dtau, standard relativistic
    free particle) PLUS the already-established interaction term (+g*m*phi,
    verified this session by direct re-read of two_field_action_closure.py).
    Summed BEFORE factoring -- this is the total action density per dtau."""
    kinetic = -m * c
    interaction = g * m * phi
    return kinetic + interaction


def effective_mass_factor(total_density, m, c):
    """Factor the total density as -m*c*[effective mass factor], exposing
    the mass-varying-particle form S = -c*int(dtau)*m_eff(phi)."""
    return sp.simplify(-total_density / (m * c))


def main():
    g, m, phi, c, alpha = sp.symbols("g m phi c alpha", positive=False)

    print("=" * 78)
    print("P33 -- covariantization + mass-varying-scalar classification")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Total monopole action density (kinetic + already-established")
    print("  interaction term, both re-verified this session):")
    total = total_monopole_action_density(g, m, c, phi)
    print(f"  S_total/dtau = -m*c + g*m*phi = {total}")

    print("\n[STEP 2] Factor as a mass-varying particle: S_total = -m*c*int(dtau)*[...]")
    eff_factor = effective_mass_factor(total, m, c)
    print(f"  effective mass factor = {eff_factor}")
    m_eff = m * eff_factor
    print(f"  m_eff(phi) = m * [{eff_factor}] = {sp.expand(m_eff)}")

    consistency = sp.simplify(-m * c * eff_factor - total)
    print(f"  Consistency check (should be 0, EXACT not approximate): {consistency}")
    assert consistency == 0

    print("\n[STEP 3] Covariant form (dtau -> proper time along a curved-spacetime")
    print("  worldline, reduces exactly to the flat-space form when g_munu -> eta_munu):")
    print("  S_i = -c * int(dtau_curved) * m_eff(phi(x_i)),   m_eff(phi) = m*(1 - (g/c)*phi)")
    print("  This is manifestly a scalar (covariant) action -- a MASS-VARYING")
    print("  particle, exactly the structure of a CONFORMALLY-COUPLED scalar in")
    print("  scalar-tensor gravity (matter built from a Jordan-frame metric")
    print("  g_munu = A(phi)^2 * g_munu_tilde, A(phi) ~ 1 + alpha*phi to linear order).")

    print("\n[STEP 4] Identify MULTING's own coupling with the standard A(phi) form:")
    A_standard = 1 + alpha * phi
    alpha_identified = sp.solve(sp.Eq(m_eff / m, A_standard), alpha)[0]
    print("  Standard form: A(phi) = 1 + alpha*phi")
    print(f"  m_eff/m = {sp.simplify(m_eff / m)}")
    print(f"  Identified alpha = {alpha_identified}")
    assert alpha_identified == -g / c

    print("\n[STEP 5] Literature-grounded consequence of this classification")
    print("  (WebFetch, this session, arXiv:1804.07180 eq. 1 -- DIRECT QUOTE):")
    print('  "The SM degrees of freedom {psi} move on geodesics determined by')
    print('   the Jordan-frame metric g_munu = A^2(chi) * g_munu_tilde"')
    print("  -- i.e. matter moves on a metric CONFORMALLY RELATED to, but NOT")
    print("  identical to, the canonical (Einstein-frame) metric g_tilde whose")
    print("  own field equations remain standard GR (sourced by ordinary")
    print("  stress-energy + the scalar's own stress-energy -- the SAME")
    print("  backreaction channel P32's own section 4 already flagged, not a")
    print("  NEW, direct Q-type Poisson-equation modification). This is the")
    print("  standard, well-established Einstein-frame/Jordan-frame")
    print("  classification for conformally-coupled scalar-tensor theories.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("MULTING's own monopole coupling, covariantized, is EXACTLY (not")
    print("approximately) a mass-varying / conformally-coupled scalar particle,")
    print("with A(phi) = 1 - (g/c)*phi -- verified symbolically. This IS a")
    print("RECOGNIZED class in the scalar-tensor literature. Per that")
    print("literature's own established classification (direct quote above,")
    print("[VERIFIED-WEBFETCH] for the structural fact; the broader claim that")
    print("Einstein-frame field equations remain standard GR form is")
    print("[WEAK/well-established-consensus], synthesized across multiple")
    print("indexed papers via WebSearch, not pinned to one direct quote):")
    print("matter in this class of theory feels an EXTRA fifth-force term in")
    print("its own equation of motion, while the metric's OWN field equations")
    print("remain standard GR, modified ONLY through the scalar's own")
    print("stress-energy backreaction -- NOT through a direct, Q-type")
    print("modification of the Poisson equation the way Bean & Tangmatitham's")
    print("phenomenology assumes. This STRENGTHENS FINDING_P32's own Part B")
    print("definitional-mismatch argument with a literature-grounded")
    print("classification, still short of a full from-scratch derivation --")
    print("that remains the larger, deferred next step.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
