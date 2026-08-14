"""P35 -- second step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md): a flat-background Yukawa-exchange
calculation, using MULTING's own matter+scalar action, reproduces the
FUNCTIONAL FORM of P21's phenomenological Delta_G formula under one
specific, already-flagged-as-conventional normalization choice.

CORRECTED 2026-08-14, after context-blind skeptic review, same day.
FOUR real issues, the most consequential ones NOT just framing:
  (1) "Derives (not merely restates) P21's founding relation" OVERCLAIMED
      in the strongest way found this session. Independently re-checked
      by re-reading FINDING_P21_shared_phi_normalization_constraint.md
      directly (not from memory) before accepting the skeptic's
      correction: P21's OWN text (already corrected by its own skeptic
      review) explicitly states the missing normalization constant A's
      PLACEMENT is "a convention, not a forced discovery: the identical
      physics results from placing an equivalent factor in the kinetic
      term instead." P21 never claimed A=1 as a physical prediction --
      only that SOME factor with G's units must exist. This script
      independently CHOSE the canonical-kinetic-term convention (the
      same one P21 flagged as equally valid but arbitrary), which makes
      A=1 TRUE BY CONSTRUCTION, not by physical content. Matching A=1 to
      P21's formula is therefore substantially CIRCULAR -- not
      independent confirmation of P21's specific coefficient, only of
      the FUNCTIONAL FORM (Delta_G proportional to coupling^2/(4*pi),
      the generic shape of any canonically-normalized massless-scalar
      Yukawa exchange). Retitled and downgraded throughout.
  (2) U_N=-G_N*m*M/r (the standard Newtonian potential energy) is
      IMPORTED, never derived from S_EH anywhere in this script --
      combining a genuinely derived quantity (U_5th) with an imported
      one (U_N) and calling the SUM "G_eff, derived" overclaimed. Fixed:
      only the ADDITIVE Delta_G (Yukawa) piece is claimed as derived;
      G_N/U_N is explicitly flagged as the imported, unmodified
      baseline.
  (3) THE MOST CONSEQUENTIAL, A REAL PHYSICS GAP, NOT FRAMING: Section
      5's "qualitative slip" argument ("phi's own anisotropic-stress
      contribution is second-order-small") was WRONG, not just
      unproven. It conflated two DIFFERENT perturbation expansions: in
      COSMOLOGICAL perturbation theory, a small perturbation delta-phi
      makes (grad delta-phi)^2 genuinely second-order-small. But THIS
      script's phi(r)=g_hat*M/(4*pi*r) is the FULL static field sourced
      by M, not a small cosmological perturbation -- its own
      |grad(phi)|^2 is O(g_hat^2), the EXACT SAME parametric order as
      the claimed Delta_G correction itself. Phi's own stress-energy
      (hence its own contribution to the metric, hence any slip Phi!=Psi)
      is UNCOMPUTED at the order where it would matter, not
      "second-order-small" -- withdrawn to "not computed, genuinely
      open question," not re-asserted at any confidence.
  (4) Related to (2)-(3): the scalar's own stress-energy sources gravity
      (via Einstein's equations) at the SAME O(g_hat^2) order as the
      claimed Delta_G. This script computes U_5th on a flat background
      (no metric response to phi) and combines it with an UNPERTURBED
      U_N (also no metric response to phi) -- a linear superposition of
      two DECOUPLED leading-order pieces, not the fully self-consistent
      coupled Einstein+scalar+matter solution a genuine G_eff derivation
      would need. This O(g_hat^2) gap is neither computed nor bounded
      here.
  Also fixed (small, concrete): "attractive for like-sign g_hat" was
  MEANINGLESS/WRONG -- U_5th=-g_hat^2*m*M/(4*pi*r) is attractive for
  ANY real g_hat, since g_hat enters squared (via m_eff applied to both
  the source and the test particle). Removed the "like-sign" qualifier.

METHOD (unchanged). Re-uses TWO already-established, already-skeptic-
confirmed building blocks rather than re-deriving them (Using Wheels
First):
  (1) P34's own general (here: static-limited) scalar field equation,
      derived via direct Euler-Lagrange variation of the SAME action
      P34 used, now WITHOUT the homogeneous-FRW restriction (i.e. this
      is the genuinely NEW piece of this finding -- P34 only ever
      derived the spatially-homogeneous case).
  (2) P19's own already-skeptic-confirmed 3D Green's function result
      (Laplacian(1/(4*pi*r)) = -delta^3(x), CONFIRMED-REAL,
      FINDING_P19_greens_function_normalization_derived.md) -- cited,
      NOT re-derived from scratch.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def general_scalar_field_equation(t, x, y, z, phi, rho, ghat):
    """Direct Euler-Lagrange variation of the SAME matter+scalar
    Lagrangian density P34 used (L = (1/2)phi_dot^2 - (1/2)(grad phi)^2
    - rho*(1-ghat*phi)), now kept fully general in space AND time (no
    homogeneous-FRW restriction) -- this is the genuinely new derivation
    step in this finding. Returns the field-equation residual; the
    correctly-signed EOM is phi_tt - Laplacian(phi) = ghat*rho."""
    L = (
        sp.Rational(1, 2) * sp.diff(phi, t) ** 2
        - sp.Rational(1, 2) * (sp.diff(phi, x) ** 2 + sp.diff(phi, y) ** 2 + sp.diff(phi, z) ** 2)
        - rho * (1 - ghat * phi)
    )
    dL_dphi_t = sp.diff(L, sp.diff(phi, t))
    dL_dphi_x = sp.diff(L, sp.diff(phi, x))
    dL_dphi_y = sp.diff(L, sp.diff(phi, y))
    dL_dphi_z = sp.diff(L, sp.diff(phi, z))
    dL_dphi = sp.diff(L, phi)
    eom = (
        sp.diff(dL_dphi_t, t)
        + sp.diff(dL_dphi_x, x)
        + sp.diff(dL_dphi_y, y)
        + sp.diff(dL_dphi_z, z)
        - dL_dphi
    )
    return sp.expand(eom)


def green_function_point_source_potential(ghat, M, r):
    """phi(r) = ghat*M/(4*pi*r) -- built directly from P19's own already-
    confirmed Green's function (Laplacian(1/(4*pi*r))=-delta^3(x)), NOT
    re-derived here. Verification below checks this satisfies the
    STATIC LIMIT of the field equation derived above away from the
    origin (Laplace's equation, source-free region)."""
    return ghat * M / (4 * sp.pi * r)


def main():
    t, x, y, z, r = sp.symbols("t x y z r", real=True)
    ghat = sp.Symbol("g_hat", positive=True)
    M, m, G_N = sp.symbols("M m G_N", positive=True)
    phi = sp.Function("phi")

    print("=" * 78)
    print("P35 -- flat-background Yukawa exchange (CORRECTED, narrowed scope)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] General (non-homogeneous) scalar field equation --")
    print("  genuinely new: P34 only derived the spatially-homogeneous FRW case.")
    print("  Same action, same Lagrangian density, kept fully x,y,z,t-dependent:")
    phi_general = phi(t, x, y, z)
    rho_general = sp.Function("rho")(x, y, z)  # static source density
    eom_general = general_scalar_field_equation(t, x, y, z, phi_general, rho_general, ghat)
    print(f"  raw Euler-Lagrange residual: {eom_general}")
    print("  => phi_tt - Laplacian(phi) = g_hat*rho   (rearranged)")

    print("\n[STEP 2] Static limit (phi_tt=0, point source rho=M*delta^3(x)):")
    print("  Laplacian(phi) = -g_hat*M*delta^3(x)")
    print("  Using P19's own already-confirmed Green's function")
    print("  (Laplacian(1/(4*pi*r)) = -delta^3(x), CONFIRMED-REAL, cited not re-derived):")
    phi_point = green_function_point_source_potential(ghat, M, r)
    print(f"  phi(r) = {phi_point}")

    print("\n[STEP 3] Verify this solves the STATIC field equation away from the")
    print("  origin (r>0, source-free region -- Laplace's equation, spherical):")
    lap_phi_away = sp.simplify(
        sp.diff(r**2 * sp.diff(phi_point, r), r) / r**2
    )  # radial Laplacian in spherical symmetry
    print(f"  Laplacian(phi) for r>0 (should be 0): {lap_phi_away}")
    assert lap_phi_away == 0, "phi(r)=ghat*M/(4*pi*r) does NOT solve Laplace's eq away from origin"

    print("\n[STEP 4] Fifth-force potential energy on a test mass m, FROM THE SAME")
    print("  matter-action interaction term used throughout P33-P35")
    print("  (S_matter = -int dtau*m*(1-g_hat*phi)  =>  U_5th = -m*g_hat*phi(r)):")
    U_5th = sp.simplify(-m * ghat * phi_point)
    print(f"  U_5th(r) = {U_5th}")
    print("  CORRECTED: attractive for ANY real g_hat, not 'like-sign' -- g_hat")
    print("  enters SQUARED (m_eff applied to both source and test particle), so")
    print("  the sign of g_hat itself is irrelevant to attraction/repulsion here.")

    print("\n[STEP 5] Combine with the IMPORTED (not derived from S_EH here) Newtonian")
    print("  potential energy U_N(r) = -G_N*m*M/r. CORRECTED: only the ADDITIVE")
    print("  Delta_G (Yukawa) piece below is genuinely derived in this script; U_N")
    print("  itself is a textbook import, not re-derived from S_EH -- combining a")
    print("  derived quantity with an imported one and calling the SUM 'G_eff,")
    print("  derived' would overclaim (skeptic-flagged, fixed here):")
    U_N = -G_N * m * M / r
    U_total = sp.together(U_N + U_5th)
    print(f"  U_total(r) = {U_total}   [U_N imported, U_5th derived]")
    G_eff_expr = sp.simplify(-U_total * r / (m * M))
    delta_G = sp.simplify(G_eff_expr - G_N)
    print(f"  => Delta_G (the genuinely derived, additive piece) := {delta_G}")

    print("\n[STEP 6] Compare to P21's OWN formula, A*g_hat^2=4*pi*Delta_G. CORRECTED")
    print("  after re-reading FINDING_P21 directly: P21's own (already skeptic-")
    print("  corrected) text states A's PLACEMENT is 'a convention, not a forced")
    print("  discovery' -- P21 never claimed a specific numeric value for A. This")
    print("  script's canonical-kinetic-term choice makes A=1 TRUE BY CONSTRUCTION,")
    print("  not by independent physical content -- the match below confirms the")
    print("  FUNCTIONAL FORM only (Delta_G proportional to coupling^2/(4*pi)), NOT")
    print("  an independent numeric confirmation of P21's specific coefficient:")
    A = sp.Symbol("A", positive=True)  # P21's own normalization constant
    p21_relation_delta_G = sp.simplify(A * ghat**2 / (4 * sp.pi))
    print(f"  P21's Delta_G (A left general) = {p21_relation_delta_G}")
    print(f"  This derivation's Delta_G      = {delta_G}")
    match_with_A1 = sp.simplify(p21_relation_delta_G.subs(A, 1) - delta_G)
    print(f"  Difference, setting A=1 (a CHOSEN convention, not a result): {match_with_A1}")
    assert match_with_A1 == 0, "Does NOT match P21's relation even with A=1 -- STOP"

    print("\n[STEP 7] CORRECTED -- Section 5's original 'qualitative slip' claim was")
    print("  WRONG, not just unproven: it conflated cosmological-perturbation-theory")
    print("  'small delta-phi' reasoning with THIS static, full-field phi(r), whose")
    print("  own |grad(phi)|^2 is O(g_hat^2) -- the SAME order as Delta_G itself, not")
    print("  second-order-small. Phi's own stress-energy (hence any metric slip)")
    print("  is UNCOMPUTED at the order that would matter. Status: genuinely OPEN,")
    print("  not asserted at any confidence level, qualitative claim withdrawn.")

    print("\n" + "=" * 78)
    print("VERDICT (CORRECTED after skeptic review, same day -- narrowed)")
    print("=" * 78)
    print("A flat-background Yukawa-exchange calculation, using MULTING's own")
    print("matter+scalar action, gives U_5th=-g_hat^2*m*M/(4*pi*r) -- genuinely")
    print("derived, correctly signed and dimensioned. Combined (by linear")
    print("superposition, NOT a self-consistent coupled solution) with the IMPORTED")
    print("standard Newtonian U_N, this gives an additive Delta_G=g_hat^2/(4*pi).")
    print("This reproduces the FUNCTIONAL FORM of P21's own formula under ONE")
    print("specific, already-flagged-as-conventional normalization choice -- NOT an")
    print("independent numeric confirmation, since P21's own text already states")
    print("A's value is convention-dependent, not a physical prediction. WITHDRAWN:")
    print("the 'qualitative slip, gamma=1' claim -- phi's own O(g_hat^2) stress-")
    print("energy and its metric backreaction are UNCOMPUTED, genuinely open,")
    print("at exactly the order this finding's own Delta_G lives at.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
