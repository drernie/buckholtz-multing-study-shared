"""P35 -- second step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md): does P21's own founding relation
(A*g^2=4*pi*Delta_G, DEFINED there by dimensional matching to
Archidiacono's phenomenology, never derived from a field equation)
actually fall out of MULTING's own matter+scalar action, once P34's
explicit gravitational-sector choice (standard, unmodified Einstein-
Hilbert gravity) is taken seriously and the static, weak-field, point-
source limit is worked out?

METHOD. Re-uses TWO already-established, already-skeptic-confirmed
building blocks rather than re-deriving them (Using Wheels First):
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
    print("P35 -- static weak-field limit closes the loop on P21's Delta_G")
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
    print("  (attractive for like-sign g_hat, matching two_field_action_closure.py's")
    print("   own docstring point 2: 'its m-m exchange renormalises G, attractive')")

    print("\n[STEP 5] Combine with the STANDARD (P34: S_EH unmodified) Newtonian")
    print("  potential energy U_N(r) = -G_N*m*M/r, and extract G_eff:")
    U_N = -G_N * m * M / r
    U_total = sp.together(U_N + U_5th)
    print(f"  U_total(r) = {U_total}")
    G_eff_expr = sp.simplify(-U_total * r / (m * M))
    print(f"  => G_eff := -U_total*r/(m*M) = {G_eff_expr}")
    delta_G = sp.simplify(G_eff_expr - G_N)
    print(f"  => Delta_G := G_eff - G_N = {delta_G}")

    print("\n[STEP 6] Compare to P21's OWN founding relation, A*g_hat^2=4*pi*Delta_G")
    print("  (defined there by dimensional matching, NEVER previously derived from")
    print("  a field equation -- this is the load-bearing check of this finding):")
    A = sp.Symbol("A", positive=True)  # P21's own normalization constant
    p21_relation_delta_G = sp.simplify(A * ghat**2 / (4 * sp.pi))
    print(f"  P21's Delta_G (A left general) = {p21_relation_delta_G}")
    print(f"  This derivation's Delta_G      = {delta_G}")
    match_with_A1 = sp.simplify(p21_relation_delta_G.subs(A, 1) - delta_G)
    print(f"  Difference, setting A=1: {match_with_A1}")
    assert match_with_A1 == 0, "Does NOT match P21's relation even with A=1 -- STOP"

    print("\n[STEP 7] Qualitative slip observation (cheap, same structure, no new")
    print("  derivation needed): dust has zero anisotropic stress; phi is a")
    print("  CANONICAL, minimally-coupled scalar with no direct R-coupling (P34's")
    print("  own explicit choice) -- its own anisotropic-stress contribution at")
    print("  linear order is second-order-small (grad(phi) x grad(phi), phi itself")
    print("  already first-order). Standard, well-known consequence for this class")
    print("  of theory (canonical quintessence-type scalars): NO slip, gamma=1")
    print("  (Phi=Psi) exactly at this order -- qualitative only, not computed here.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("The static, weak-field, point-source limit of MULTING's own matter+scalar")
    print("action (P34's gravitational-sector choice, P19's already-confirmed Green's")
    print("function, P33's m_eff(phi) coupling) reproduces P21's OWN founding relation")
    print("A*g^2=4*pi*Delta_G EXACTLY, with A=1 in the canonical-kinetic-term")
    print("convention used throughout P34-P35. P21's relation was DEFINED by")
    print("dimensional matching at the start of this arc; it is now DERIVED from a")
    print("genuine field-theoretic calculation for the first time. Every finding")
    print("built on P21's Delta_G (P22, P28-P31) inherits this closure.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
