"""P34 -- first step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md): explicitly add a gravitational sector
(flagged as an assumption -- standard, unmodified Einstein-Hilbert
gravity, chosen as the simplest possible closure, per P33's own
corrected lesson never to assume this silently) to MULTING's own
reconstructed matter+scalar action, reduce to the homogeneous FRW
background, and derive the background equations via TWO independent
routes -- Bianchi/energy-conservation vs direct Euler-Lagrange variation
of the reduced (minisuperspace) action -- as a genuine, non-tautological
cross-check (the two routes start from structurally different equations;
agreement is real information, not guaranteed by construction).

UNITS NOTE (found by re-reading two_field_action_closure.py directly
before starting, not from memory): the project's own stated action,
"S = int d^4x (1/2)(d phi)^2 + sum_i int dtau [g m_i + ...] phi(x_i)",
has never been dimensionally fixed end-to-end anywhere in this project --
it appears only as a print statement (lines 111-116 of that file), never
symbolically encoded or unit-checked. This finding does NOT inherit a
units convention from the source (none was ever fixed); it FIXES one
explicitly here (c=1 units for the derivation, i.e. time and length
measured in the same units, standard practice in this literature), flags
it as a new, explicit choice, and defines g_hat := g/c as a single
symbol throughout to sidestep re-litigating the source's own unfixed
c-bookkeeping. Restoring explicit c-factors to match P21-P33's own SI-like
convention is deferred, flagged as future work.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def route_a_bianchi(t, a, phi, rho0, ghat, H):
    """Route A: assume the STANDARD (unmodified) Friedmann + total energy
    conservation law rho_dot_total = -3H(rho_total+p_total) -- this is
    forced by the Bianchi identity for ANY matter content once gravity
    itself (S_EH) is standard, unmodified GR -- and solve it for the
    scalar's own source term. This uses ONLY: (1) bare mass conservation
    rho0_dot=-3H*rho0 (particle number conservation, unmodified by phi),
    (2) the definitions rho_m_eff=rho0*(1-ghat*phi), rho_phi=phi_dot^2/2,
    p_phi=phi_dot^2/2 (standard canonical scalar, no potential), p_m=0
    (dust). It does NOT use the matter+scalar action directly."""
    rho_m_eff = rho0 * (1 - ghat * phi)
    rho_phi = sp.Rational(1, 2) * sp.diff(phi, t) ** 2
    p_total = rho_phi
    rho_total = rho_m_eff + rho_phi

    rho0_dot = sp.diff(rho0, t)
    # bare mass conservation is an INPUT here, not derived -- substitute it in
    rho0_dot_law = -3 * H * rho0

    lhs = sp.diff(rho_total, t).subs(rho0_dot, rho0_dot_law)
    rhs = -3 * H * (rho_total + p_total)
    # solve lhs - rhs = 0 for phi_ddot (the only second-time-derivative present)
    residual = sp.expand(lhs - rhs)
    return residual


def route_b_euler_lagrange(t, a, phi, rho0_const_times_a3, ghat):
    """Route B: reduce the matter+scalar action to a 1D (minisuperspace)
    Lagrangian for phi(t) alone, treating a(t) and the comoving bare mass
    M=rho0*a^3 (constant, particle-number conservation) as external
    background functions -- standard, valid procedure for a homogeneous
    test-scalar sourced by homogeneous dust. Derive phi's own equation of
    motion via the actual Euler-Lagrange equation -- a DIFFERENT starting
    point from Route A (direct field-theoretic variation, not energy
    bookkeeping)."""
    L_phi = a**3 * sp.Rational(1, 2) * sp.diff(phi, t) ** 2
    L_matter = -rho0_const_times_a3 * (1 - ghat * phi)
    L = L_phi + L_matter

    dL_dphidot = sp.diff(L, sp.diff(phi, t))
    eom = sp.diff(dL_dphidot, t) - sp.diff(L, phi)
    return sp.expand(eom)


def main():
    t = sp.Symbol("t", positive=True)
    a = sp.Function("a", positive=True)(t)
    phi = sp.Function("phi")(t)
    rho0 = sp.Function("rho0", positive=True)(t)
    ghat = sp.Symbol("g_hat")  # := g/c, dimensionless-in-these-units coupling
    H = sp.diff(a, t) / a
    M = sp.Symbol("M", positive=True)  # comoving bare mass, M = rho0*a^3 = const

    print("=" * 78)
    print("P34 -- FRW background, two independent derivation routes")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[SETUP] Single-metric action (gravitational sector EXPLICITLY added,")
    print("  flagged as an assumption -- standard unmodified Einstein-Hilbert):")
    print("  S = S_EH[g] + S_phi[phi,g] + S_matter[worldlines,phi;g]")
    print("  S_EH  = standard, unmodified -- Friedmann eq. is the ordinary one,")
    print("          H^2=(8*pi*G_N/3)*rho_total, NOT independently re-derived here")
    print("          (textbook GR result, unaffected by matter's phi-dependence,")
    print("          which enters only through rho_total's own definition below).")
    print("  S_phi = int d^4x sqrt(-g) * phi_dot^2/2   (canonical, c=1 units, flagged)")
    print("  S_matter = -sum_i int dtau_i * m_i*(1-g_hat*phi(x_i)),  g_hat := g/c")
    print("             (P33's own m_eff(phi)/m=1-(g/c)phi, re-used unchanged --")
    print("              that identification was NOT weakened by P33's correction)")

    print("\n[ROUTE A] Bianchi identity / total energy conservation")
    print("  (uses ONLY: bare mass conservation + standard rho,p definitions --")
    print("   does NOT touch the matter+scalar action directly)")
    residual_a = route_a_bianchi(t, a, phi, rho0, ghat, H)
    # residual_a should be linear in phi_ddot; solve for phi_ddot + 3H phi_dot - ghat*rho0
    phi_dd = sp.diff(phi, t, 2)
    coeff_check = sp.diff(residual_a, phi_dd)
    print(f"  coefficient of phi'' in the residual (sanity: should be phi_dot): {coeff_check}")
    solved_a = sp.solve(sp.Eq(residual_a, 0), phi_dd)
    print(f"  => phi'' solved from Route A: {sp.simplify(solved_a[0]) if solved_a else 'FAILED'}")
    eom_a = sp.simplify(phi_dd - 3 * H * sp.diff(phi, t) + ghat * rho0)
    print(f"  Route A EOM claim  phi''+3H*phi' = g_hat*rho0  <=> this expr is 0: {eom_a}")
    check_a = sp.simplify(residual_a.subs(phi_dd, 3 * H * sp.diff(phi, t) * -1 + ghat * rho0))
    print(f"  Substituting the CLAIMED solution into the Route-A residual (should be 0): {check_a}")

    print("\n[ROUTE B] Direct Euler-Lagrange on the reduced matter+scalar action")
    print("  (uses ONLY: the actual action's own kinetic + interaction terms --")
    print("   does NOT touch energy conservation / Bianchi identity)")
    eom_b_expr = route_b_euler_lagrange(t, a, phi, M, ghat)
    print(f"  raw Euler-Lagrange residual: {eom_b_expr}")
    eom_b_normalized = sp.simplify(eom_b_expr / a**3)
    print(f"  divided by a^3: {eom_b_normalized}")
    claimed_b = sp.simplify(
        a**3 * (phi_dd + 3 * H * sp.diff(phi, t) - ghat * M / a**3) - eom_b_expr
    )
    print(
        f"  Route B EOM claim  phi''+3H*phi' = g_hat*rho0 (rho0=M/a^3) <=> this is 0: "
        f"{sp.simplify(claimed_b)}"
    )

    print("\n[CROSS-CHECK] Do Route A and Route B agree? (genuine, non-tautological --")
    print("  the two routes started from DIFFERENT equations: energy conservation")
    print("  vs. direct field variation)")
    agree = (check_a == 0) and (sp.simplify(claimed_b) == 0)
    print("  Route A gives:  phi'' + 3H phi' = g_hat * rho0")
    print("  Route B gives:  phi'' + 3H phi' = g_hat * rho0   (rho0 = M/a^3)")
    print(f"  Both residuals vanish identically: {agree}")
    assert agree, "Route A and Route B disagree -- STOP, do not proceed to P35"

    print("\n[STRUCTURAL OBSERVATION] Where does 'G_eff = G_N + Delta G' actually live?")
    print("  The BACKGROUND Friedmann equation above uses the UNMODIFIED G_N --")
    print("  S_EH was never touched. The only background-level deviation from LCDM")
    print("  is through rho_total's own content (rho_phi, and rho_m,eff's g_hat*phi")
    print("  correction), BOTH of which are second-order-small if g_hat*phi<<1 --")
    print("  consistent with P22/P31's own bound (epsilon_g <~ 8.39e-12). This is")
    print("  CONSISTENT WITH, and structurally explains, P1's own already-stated")
    print("  background result ('MULTING q-blind on background, = LCDM@73',")
    print("  two_field_action_closure.py line 128) -- not previously derived from")
    print("  a full action, only asserted. The P21-22 'Delta G' (fifth-force")
    print("  correction to Newton's constant) is a LINEAR-PERTURBATION / two-body")
    print("  potential effect (phi mediates a Yukawa-like force between mass")
    print("  overdensities), NOT a background-level G_N replacement -- this")
    print("  distinction was never made explicit anywhere in P21-P33.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Two structurally independent derivation routes (Bianchi/energy-conservation")
    print("vs. direct Euler-Lagrange variation) agree EXACTLY on the background scalar")
    print("equation of motion: phi''+3H*phi' = (g/c)*rho0. This is a genuine positive")
    print("control -- the routes share no common derivation step, so agreement is real")
    print("information, not a tautology. The background Friedmann equation itself is")
    print("the STANDARD, unmodified GR result (G_N untouched); MULTING's own")
    print("deviation from LCDM enters entirely through the SOURCE content, matching")
    print("and explaining P1's own prior (asserted, not derived) background-blindness")
    print("claim. Explicit new finding: 'Delta G' (P21-22) is a linear-perturbation")
    print("effect, not a background-level G_N modification -- this had never been")
    print("stated explicitly before this derivation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
