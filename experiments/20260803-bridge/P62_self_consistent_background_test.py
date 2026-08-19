"""P62 -- construct a genuinely, mutually self-consistent (a, phibar,
rhobar_A) background (Friedmann + matter continuity + scalar background
Klein-Gordon equation, ALL SIMULTANEOUSLY, at g_hat=0) and re-run
FINDING_P61's own decisive constraint-propagation test against it.

DIRECT CONTINUATION OF FINDING_P61 (2026-08-19), which explicitly named
this as the un-attempted next step after its own skeptic-caught
correction: Parts H/I there showed neither matter-only Friedmann nor
total-energy Friedmann (each imposed ON TOP OF an otherwise free choice)
restores Bianchi consistency once phibar is genuinely nonzero. The
remaining open question, stated verbatim in FINDING_P61's own "NOT YET
DONE" list: does full consistency require the ENTIRE background to be a
mutually self-consistent JOINT solution of all three background
equations at once, rather than one relation added to a free choice?

SCOPE: g_hat=0 (uncoupled/free background) ONLY -- the coupled g_hat!=0
case remains untested, exactly as flagged as an open item in P61.

PARTS A-F below are REPRODUCED VERBATIM from FINDING_P61's own script
(same file, same variable names) up through building `cross`, the fully
substituted 0i-constraint-propagation residual at g_hat=0. This is
deliberate duplication, matching this campaign's own established practice
of keeping each Pxx file self-contained and independently reproducible
rather than importing from a prior file's monolithic main().

NEW in this file:
  - Part J: the exact two-fluid (pressureless matter + free massless
    scalar / "stiff fluid") FRW background solution. This is a known,
    standard solvable system (V=0 means the scalar behaves exactly as a
    stiff fluid, rho_phi=phibar_dot^2/2 propto a^-6); solved here from
    scratch via direct integration of the Friedmann constraint, then
    independently verified (assert) to satisfy Friedmann, matter
    continuity, and the scalar background KG equation, ALL THREE
    SIMULTANEOUSLY and EXACTLY -- the joint self-consistency FINDING_P61
    Parts H/I did NOT have.
  - Part K: substitutes this genuinely self-consistent background into
    FINDING_P61's own `cross` expression (g_hat=0) and checks whether the
    0i constraint now stays consistent under evolution.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
    """Reused VERBATIM from FINDING_P48/.../P61's own already-verified helper."""
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for lam in range(n):
        for mu in range(n):
            for nu in range(n):
                term = sum(
                    ginv[lam, sig]
                    * (
                        sp.diff(g[sig, mu], coords[nu])
                        + sp.diff(g[sig, nu], coords[mu])
                        - sp.diff(g[mu, nu], coords[sig])
                    )
                    for sig in range(n)
                )
                Gamma[lam][mu][nu] = sp.Rational(1, 2) * term
    return Gamma


def covariant_div_upper(T_upper, Gamma, coords, nu, n=4):
    """Reused VERBATIM from FINDING_P55/.../P61's own already-verified helper."""
    total = 0
    for mu in range(n):
        total += sp.diff(T_upper[mu][nu], coords[mu])
    for mu in range(n):
        for lam in range(n):
            total += Gamma[mu][mu][lam] * T_upper[lam][nu]
            total += Gamma[nu][mu][lam] * T_upper[mu][lam]
    return total


def covariant_box(scalar_field, ginv, Gamma, coords, n=4):
    """Reused VERBATIM from FINDING_P55/.../P59's own already-verified helper."""
    dphi_local = [sp.diff(scalar_field, c) for c in coords]
    result = 0
    for mu in range(n):
        for nu in range(n):
            hessian_munu = sp.diff(scalar_field, coords[mu], coords[nu]) - sum(
                Gamma[lam][mu][nu] * dphi_local[lam] for lam in range(n)
            )
            result += ginv[mu, nu] * hessian_munu
    return result


def main():
    print("=" * 78)
    print("P62 -- genuinely self-consistent (a,phibar,rhobar_A) background,")
    print("re-testing FINDING_P61's decisive constraint-propagation test")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    # PARTS A-F: reproduced VERBATIM from FINDING_P61, building `cross`
    # ==================================================================
    print("\n" + "-" * 78)
    print("PARTS A-F -- reproduced verbatim from FINDING_P61 (same file,")
    print("same variable names), building the closed system and `cross`,")
    print("the fully-substituted 0i-constraint-propagation residual.")
    print("-" * 78)

    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    eps = sp.Symbol("epsilon", real=True)
    a = sp.Function("a")(t)
    ghat = sp.Symbol("g_hat", real=True, positive=True)
    phibar = sp.Function("phi_bar")(t)
    deltaphi = sp.Function("delta_phi")(t, x, y, z)
    rhobar_A = sp.Function("rhobar_A")(t)
    deltarho_A = sp.Function("delta_rho_A")(t, x, y, z)
    Psi = sp.Function("Psi")(t, x, y, z)
    Vx = sp.Function("V_x")(t, x, y, z)
    n = 4
    H = sp.diff(a, t) / a

    g = sp.diag(
        -(1 + 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
    )
    ginv = g.inv()
    Gamma = christoffels_exact(coords, g, ginv, n)
    phi = phibar + eps * deltaphi
    rho_A = rhobar_A + eps * deltarho_A
    M = 1 - ghat * phibar

    box_phi_exact = covariant_box(phi, ginv, Gamma, coords, n)
    box_phi_lin = sp.simplify(sp.diff(box_phi_exact, eps).subs(eps, 0))
    p57_geometric_part = (
        sp.diff(deltaphi, t, 2)
        + 3 * H * sp.diff(deltaphi, t)
        - sum(sp.diff(deltaphi, c, 2) for c in coords[1:]) / a**2
        - 2 * Psi * sp.diff(phibar, t, 2)
        - 6 * H * Psi * sp.diff(phibar, t)
        - sp.diff(Psi, t) * sp.diff(phibar, t)
        - 3 * sp.diff(Psi, t) * sp.diff(phibar, t)
    )
    check_p57 = sp.simplify(box_phi_lin - (-p57_geometric_part))
    assert check_p57 == 0, "Part A machinery check failed -- STOP"
    print("  Part A (machinery vs FINDING_P57): CONFIRMED.")

    dphi = [sp.diff(phi, c) for c in coords]
    d0_phi_full = ginv[0, 0] * dphi[0]
    d1_phi_full = ginv[1, 1] * dphi[1]
    field_eq_rhs = -ghat * rho_A

    Q0 = sp.simplify(-sp.diff((field_eq_rhs * d0_phi_full), eps).subs(eps, 0))
    Q1 = sp.simplify(-sp.diff((field_eq_rhs * d1_phi_full), eps).subs(eps, 0))
    Q0_flat = sp.simplify(Q0.subs(Psi, 0))
    Q1_flat = sp.simplify(Q1.subs(Psi, 0))
    expected_Q0_flat = -ghat * (deltarho_A * sp.diff(phibar, t) + rhobar_A * sp.diff(deltaphi, t))
    expected_Q1_flat = ghat * rhobar_A * sp.diff(deltaphi, x) / a**2
    assert sp.simplify(Q0_flat - expected_Q0_flat) == 0
    assert sp.simplify(Q1_flat - expected_Q1_flat) == 0
    print("  Part B (Q^0,Q^1 vs FINDING_P55/P56): CONFIRMED.")

    dphi_sq = sum(ginv[mu, nu] * dphi[mu] * dphi[nu] for mu in range(n) for nu in range(n))

    def T_phi_lower(mu, nu):
        gmn = g[mu, nu] if mu == nu else 0
        return dphi[mu] * dphi[nu] - sp.Rational(1, 2) * gmn * dphi_sq

    T_phi_01_lin = sp.simplify(sp.diff(sp.expand(T_phi_lower(0, 1)), eps).subs(eps, 0))

    u0_upper_series = sp.series(1 / sp.sqrt(-g[0, 0]), eps, 0, 2).removeO()
    u1_upper_full = eps * Vx
    rho_phys_full = rho_A * (1 - ghat * phi)

    assert sp.simplify(T_phi_01_lin - sp.diff(phibar, t) * sp.diff(deltaphi, x)) == 0
    T_int_01 = g[0, 1] * ghat * rho_A * phi
    assert T_int_01 == 0
    print("  Part C (T_0i sectors vs structural argument): CONFIRMED.")

    T_m_upper = [[0] * n for _ in range(n)]
    T_m_upper[0][0] = rho_phys_full * u0_upper_series * u0_upper_series
    T_m_upper[0][1] = rho_phys_full * u0_upper_series * u1_upper_full
    T_m_upper[1][0] = T_m_upper[0][1]
    T_m_upper[1][1] = 0

    div_Tm_0 = sp.simplify(
        sp.diff(covariant_div_upper(T_m_upper, Gamma, coords, 0, n), eps).subs(eps, 0)
    )
    div_Tm_1 = sp.simplify(
        sp.diff(covariant_div_upper(T_m_upper, Gamma, coords, 1, n), eps).subs(eps, 0)
    )
    continuity_eq = sp.simplify(div_Tm_0 - Q0)
    euler_eq = sp.simplify(div_Tm_1 - Q1)
    rhobar_A_dot_sub = -3 * H * rhobar_A
    continuity_onshell = sp.simplify(continuity_eq.subs(sp.diff(rhobar_A, t), rhobar_A_dot_sub))
    euler_onshell = sp.simplify(euler_eq.subs(sp.diff(rhobar_A, t), rhobar_A_dot_sub))

    matter_continuity_bare = rhobar_A * sp.diff(Vx, x) + sp.diff(deltarho_A, t) + 3 * H * deltarho_A
    cont_psi0_check = sp.simplify(continuity_onshell.subs(Psi, 0) - M * matter_continuity_bare)
    assert cont_psi0_check == 0
    continuity_extra = sp.simplify(continuity_onshell - M * matter_continuity_bare)
    expected_extra = -3 * M * rhobar_A * sp.diff(Psi, t)
    assert sp.simplify(continuity_extra - expected_extra) == 0

    Wx = sp.Function("W_x")(t, x, y, z)
    Vx_of_Wx = Wx / M
    euler_in_Wx = sp.simplify(euler_onshell.subs(Vx, Vx_of_Wx).doit())
    euler_in_Wx_cleared = sp.simplify(sp.expand(euler_in_Wx * a**2 / rhobar_A))
    expected_euler_Wx_times_a2 = (
        a**2 * (sp.diff(Wx, t) + 2 * H * Wx) + M * sp.diff(Psi, x) - ghat * sp.diff(deltaphi, x)
    )
    check_euler_Wx = sp.simplify(euler_in_Wx_cleared - expected_euler_Wx_times_a2)
    assert check_euler_Wx == 0
    print("  Part D (continuity+Euler vs FINDING_P59/P50A): CONFIRMED.")

    T = sp.Symbol("t", real=True)
    A = sp.Function("a")(T)
    HH = sp.diff(A, T) / A
    PHIBAR = sp.Function("phi_bar")(T)
    RHOBAR_A = sp.Function("rhobar_A")(T)
    G_N, k = sp.symbols("G_N k", real=True, positive=True)
    Ik = sp.I * k
    MM = 1 - ghat * PHIBAR
    MMdot = sp.diff(MM, T)

    PSI_k = sp.Function("Psi_k")(T)
    DPHI_k = sp.Function("delta_phi_k")(T)
    DRHO_k = sp.Function("delta_rho_A_k")(T)
    VX_k = sp.Function("V_x_k")(T)

    T00_k = (
        -2 * ghat * PSI_k * PHIBAR * RHOBAR_A
        - ghat * DPHI_k * RHOBAR_A
        - ghat * DRHO_k * PHIBAR
        + 2 * PSI_k * RHOBAR_A
        + DRHO_k
        + sp.diff(PHIBAR, T) * sp.diff(DPHI_k, T)
    )
    Psidot_00 = sp.solve(
        sp.Eq(2 * (-(k**2) * PSI_k / A**2 - 3 * HH * sp.diff(PSI_k, T)), 8 * sp.pi * G_N * T00_k),
        sp.diff(PSI_k, T),
    )[0]

    cont_sub = (-3 * HH * DRHO_k - RHOBAR_A * Ik * VX_k + 3 * RHOBAR_A * sp.diff(PSI_k, T)).subs(
        sp.diff(PSI_k, T), Psidot_00
    )
    dphi_ddot_sub = (
        -3 * HH * sp.diff(DPHI_k, T)
        - (k**2) * DPHI_k / A**2
        + ghat * DRHO_k
        + 2 * PSI_k * sp.diff(PHIBAR, T, 2)
        + 6 * HH * PSI_k * sp.diff(PHIBAR, T)
        + 4 * sp.diff(PSI_k, T) * sp.diff(PHIBAR, T)
    ).subs(sp.diff(PSI_k, T), Psidot_00)

    Psiddot_raw = sp.diff(Psidot_00, T)
    Psiddot_sub = Psiddot_raw.subs(sp.diff(PSI_k, T), Psidot_00)
    Psiddot_sub = Psiddot_sub.subs(sp.diff(DRHO_k, T), cont_sub)
    Psiddot_sub = Psiddot_sub.subs(sp.diff(DPHI_k, T, 2), dphi_ddot_sub)

    C_raw = 2 * (sp.diff(PSI_k, T) + HH * PSI_k) * Ik - 8 * sp.pi * G_N * (
        -MM * A**2 * RHOBAR_A * VX_k + sp.diff(PHIBAR, T) * Ik * DPHI_k
    )
    C_sub = C_raw.subs(sp.diff(PSI_k, T), Psidot_00)
    C_poly = sp.Poly(sp.expand(C_sub), VX_k)
    P_coef = C_poly.coeff_monomial(VX_k)
    Q_coef = C_poly.coeff_monomial(1)

    dCdt_raw = sp.diff(C_sub, T)
    dCdt_sub = dCdt_raw.subs(sp.diff(PSI_k, T), Psidot_00)
    dCdt_sub = dCdt_sub.subs(sp.diff(DRHO_k, T), cont_sub)
    dCdt_sub = dCdt_sub.subs(sp.diff(DPHI_k, T, 2), dphi_ddot_sub)
    dCdt_sub = dCdt_sub.subs(sp.diff(PSI_k, T, 2), Psiddot_sub)
    Wdot_euler = -2 * HH * (MM * VX_k) + ghat * Ik * DPHI_k / A**2 - MM * Ik * PSI_k / A**2
    Vxdot_euler = (Wdot_euler - MMdot * VX_k) / MM
    dCdt_sub = dCdt_sub.subs(sp.diff(VX_k, T), Vxdot_euler)
    dC_poly = sp.Poly(sp.expand(sp.together(dCdt_sub) * MM), VX_k)
    A_coef = dC_poly.coeff_monomial(VX_k)
    B_coef = dC_poly.coeff_monomial(1)

    cross = sp.expand(A_coef * Q_coef - B_coef * P_coef)
    cross_ghat0 = sp.simplify(cross.subs(ghat, 0))
    is_zero_free = cross_ghat0 == 0
    assert not is_zero_free, "free-background residual is now ZERO -- report exactly this"
    print("  Part F (`cross` reproduced, g_hat=0, free background): nonzero,")
    print("  exactly matching FINDING_P61's own result. Machinery confirmed")
    print("  reproduced correctly before proceeding to the new background test.")

    # ==================================================================
    # PART J -- NEW: the exact two-fluid (dust + free massless scalar)
    # FRW background, solved from scratch, verified self-consistent
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART J -- NEW: exact two-fluid background. V=0 means the scalar")
    print("behaves exactly as a 'stiff fluid' (rho_phi=phibar_dot^2/2,")
    print("propto a^-6); mixed with dust (rhobar_A propto a^-3), the")
    print("Friedmann constraint integrates in closed form:")
    print("  a(t)^3 = (9K/4)*t^2 - D/B,  K:=8*pi*G_N/3")
    print("(derived by hand first via separation of variables on")
    print("(a^3)_dot^2=9K(B*a^3+D); B,D>0 are the matter/scalar integration")
    print("constants. Specific choice B=D=1 below, matching this campaign's")
    print("established style of picking one concrete instance rather than a")
    print("fully free symbolic family, per FINDING_P61 Part G's own")
    print("precedent (rhobar_fried was likewise a specific chosen form).")
    print("-" * 78)

    K = 8 * sp.pi * G_N / 3
    a_cubed = sp.Rational(9, 4) * K * T**2 - 1  # B=D=1
    A_bg = a_cubed ** sp.Rational(1, 3)
    H_bg = sp.simplify(sp.diff(a_cubed, T) / (3 * a_cubed))
    RHOBAR_A_bg = 1 / a_cubed
    phibar_dot_bg = sp.sqrt(2) / a_cubed
    phibar_ddot_bg = sp.diff(phibar_dot_bg, T)

    print(f"  a(t)^3 = {a_cubed}")
    print(f"  H(t)   = {H_bg}   [rational in t -- no cube roots; only bare")
    print("             A^2/A^-2 factors elsewhere will carry the 1/3 power]")
    print(f"  rhobar_A(t) = {RHOBAR_A_bg}")
    print(f"  phibar_dot(t) = {phibar_dot_bg}")

    print("\n  [POSITIVE CONTROL 1/3] Friedmann: 3*H^2=8*pi*G_N*(rhobar_A+")
    print("  phibar_dot^2/2), exactly, symbolically:")
    friedmann_residual = sp.simplify(
        3 * H_bg**2 - 8 * sp.pi * G_N * (RHOBAR_A_bg + phibar_dot_bg**2 / 2)
    )
    assert friedmann_residual == 0, f"Friedmann NOT satisfied: residual={friedmann_residual}"
    print(f"  -> residual = {friedmann_residual}. CONFIRMED.")

    print("\n  [POSITIVE CONTROL 2/3] matter continuity: rhobar_A_dot+3*H*")
    print("  rhobar_A=0, exactly, symbolically:")
    continuity_residual = sp.simplify(sp.diff(RHOBAR_A_bg, T) + 3 * H_bg * RHOBAR_A_bg)
    assert continuity_residual == 0, f"continuity NOT satisfied: residual={continuity_residual}"
    print(f"  -> residual = {continuity_residual}. CONFIRMED.")

    print("\n  [POSITIVE CONTROL 3/3] scalar background KG: phibar_ddot+3*H*")
    print("  phibar_dot=0, exactly, symbolically:")
    kg_residual = sp.simplify(phibar_ddot_bg + 3 * H_bg * phibar_dot_bg)
    assert kg_residual == 0, f"scalar KG NOT satisfied: residual={kg_residual}"
    print(f"  -> residual = {kg_residual}. CONFIRMED.")

    print("\n  ALL THREE background equations satisfied SIMULTANEOUSLY and")
    print("  EXACTLY -- this is the genuinely self-consistent joint solution")
    print("  FINDING_P61 Parts H/I did not have (there, Friedmann was")
    print("  imposed while phibar was chosen independently of it, or")
    print("  matter's own continuity was sacrificed to impose total-energy")
    print("  Friedmann instead). Physical domain: t^2 > 4/(9*K) (a^3>0),")
    print("  i.e. the late-time branch of this cosmology -- a standard,")
    print("  explicitly stated domain restriction for an exact FRW solution,")
    print("  not a defect of the algebra.")

    # ==================================================================
    # PART K -- NEW: substitute the Part J background into `cross`
    # (g_hat=0) and test whether the 0i constraint stays consistent
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART K -- DECISIVE TEST: does `cross` (FINDING_P61's own fully-")
    print("substituted 0i-constraint-propagation residual, g_hat=0) vanish")
    print("against this genuinely self-consistent background? PHIBAR itself")
    print("(undifferentiated) is checked to be absent from cross_ghat0 first")
    print("-- if confirmed, only phibar_dot/phibar_ddot need to be supplied,")
    print("avoiding this background's own closed-form phibar(t) (an inverse")
    print("hyperbolic function of t, not needed if never referenced bare).")
    print("-" * 78)

    print("  [SELF-CAUGHT BUG] `cross_ghat0.has(PHIBAR)` is NOT the right test:")
    print("  sympy's .has() also matches PHIBAR inside Derivative(PHIBAR(T),T)")
    print("  sub-trees, so it can NOT distinguish 'contains phibar_dot' from")
    print("  'contains bare, undifferentiated phibar'. The correct test is")
    print("  termwise: does a term still reference PHIBAR after phibar_dot AND")
    print("  phibar_ddot are zeroed out?")
    cross_ghat0_terms = sp.Add.make_args(sp.expand(cross_ghat0))
    bare_terms = [
        term
        for term in cross_ghat0_terms
        if term.subs(sp.diff(PHIBAR, T, 2), 0).subs(sp.diff(PHIBAR, T), 0).has(PHIBAR)
    ]
    has_bare_phibar = len(bare_terms) > 0
    print(f"  total additive terms in cross_ghat0: {len(cross_ghat0_terms)}")
    print(f"  terms carrying genuinely BARE (undifferentiated) PHIBAR: {len(bare_terms)}")
    assert not has_bare_phibar, (
        "cross_ghat0 DOES reference bare, undifferentiated PHIBAR in at least "
        f"one term -- {bare_terms[:3]} -- the derivative-only substitution "
        "below is invalid; phibar(t)'s own closed form would be required "
        "instead. Report exactly this, do not silently substitute 0 for it."
    )
    print("  -> CONFIRMED absent (0 terms). Substituting phibar_dot/phibar_ddot")
    print("     only is valid -- phibar(t)'s own closed form is never needed.")

    cross_bg = cross_ghat0.subs(sp.diff(PHIBAR, T, 2), phibar_ddot_bg)
    cross_bg = cross_bg.subs(sp.diff(PHIBAR, T), phibar_dot_bg)
    cross_bg = cross_bg.subs(A, A_bg)
    cross_bg = cross_bg.subs(RHOBAR_A, RHOBAR_A_bg)
    cross_bg = sp.simplify(cross_bg.doit())

    print(f"\n  cross, self-consistent background, g_hat=0 = {cross_bg}")
    is_zero_selfconsistent = cross_bg == 0
    print(f"  Identically zero? {is_zero_selfconsistent}")

    # ==================================================================
    # PART L -- NEW: robustness check -- a SECOND, different (B,D) pair,
    # to rule out the Part K zero being a coincidence of B=D=1 specifically
    # (Spot-Check Rule, integrity.md) -- reuses the already-built
    # cross_ghat0, no need to redo Parts A-F
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART L -- ROBUSTNESS CHECK: same construction, DIFFERENT (B,D)")
    print("integration constants (B=2, D=3, not B=D=1) -- rules out Part K's")
    print("zero being a coincidence specific to that one numeric choice.")
    print("-" * 78)

    B2, D2 = sp.Integer(2), sp.Integer(3)
    a_cubed_2 = sp.Rational(9, 4) * K * B2 * T**2 - D2 / B2
    H_bg_2 = sp.simplify(sp.diff(a_cubed_2, T) / (3 * a_cubed_2))
    RHOBAR_A_bg_2 = B2 / a_cubed_2
    phibar_dot_bg_2 = sp.sqrt(2 * D2) / a_cubed_2
    phibar_ddot_bg_2 = sp.diff(phibar_dot_bg_2, T)

    print(f"  a(t)^3 = {a_cubed_2}")
    friedmann_residual_2 = sp.simplify(
        3 * H_bg_2**2 - 8 * sp.pi * G_N * (RHOBAR_A_bg_2 + phibar_dot_bg_2**2 / 2)
    )
    assert friedmann_residual_2 == 0, f"Friedmann (B=2,D=3) NOT satisfied: {friedmann_residual_2}"
    continuity_residual_2 = sp.simplify(sp.diff(RHOBAR_A_bg_2, T) + 3 * H_bg_2 * RHOBAR_A_bg_2)
    assert continuity_residual_2 == 0, (
        f"continuity (B=2,D=3) NOT satisfied: {continuity_residual_2}"
    )
    kg_residual_2 = sp.simplify(phibar_ddot_bg_2 + 3 * H_bg_2 * phibar_dot_bg_2)
    assert kg_residual_2 == 0, f"scalar KG (B=2,D=3) NOT satisfied: {kg_residual_2}"
    print("  Friedmann + continuity + scalar KG all independently confirmed")
    print("  for this DIFFERENT (B,D) pair too.")

    cross_bg_2 = cross_ghat0.subs(sp.diff(PHIBAR, T, 2), phibar_ddot_bg_2)
    cross_bg_2 = cross_bg_2.subs(sp.diff(PHIBAR, T), phibar_dot_bg_2)
    cross_bg_2 = cross_bg_2.subs(A, a_cubed_2 ** sp.Rational(1, 3))
    cross_bg_2 = cross_bg_2.subs(RHOBAR_A, RHOBAR_A_bg_2)
    cross_bg_2 = sp.simplify(cross_bg_2.doit())
    is_zero_selfconsistent_2 = cross_bg_2 == 0
    print(f"\n  cross, self-consistent background (B=2,D=3), g_hat=0 = {cross_bg_2}")
    print(f"  Identically zero? {is_zero_selfconsistent_2}")
    assert is_zero_selfconsistent_2, (
        "B=2,D=3 background gives a NONZERO residual -- this means the Part K "
        "zero WAS a coincidence specific to B=D=1, report exactly this, do "
        "not claim a general result"
    )
    print("  -> CONFIRMED: zero for this DIFFERENT (B,D) pair too.")
    print("  [SKEPTIC-CAUGHT, Step 8a] NOTE: (B,D)=(1,1) and (B,D)=(2,3) are")
    print("  NOT independent tests of the underlying claim -- both sit in the")
    print("  SAME one-parameter on-shell solution family, and the standard GR")
    print("  Bianchi identity guarantees cross=0 at EVERY point in that family")
    print("  if the Parts A-D algebra is correct, regardless of (B,D). A second")
    print("  point cannot detect an algebra bug that manifests only off-shell.")
    print("  This second (B,D) checks sp.simplify's own numerical/algebraic")
    print("  robustness across a different concrete expression, not independent")
    print("  physical evidence. See Part M below for a test that actually")
    print("  discriminates on-shell from off-shell.")

    # ==================================================================
    # PART M -- NEW [SKEPTIC-DEMANDED, Step 8a]: a genuinely discriminating
    # test. Break Friedmann ONLY (Minimal Relaxation Rule: one assumption
    # changed), keeping matter continuity and scalar KG intact, using the
    # SAME substitution code path. If `cross` is sensitive to genuine
    # self-consistency (not just "background of this algebraic shape"),
    # this MUST be nonzero.
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART M -- [SKEPTIC-DEMANDED, Step 8a] DISCRIMINATING TEST: does")
    print("`cross` actually detect broken self-consistency, or does the same")
    print("algebraic SHAPE of background always give zero regardless? Break")
    print("ONLY Friedmann (rhobar_A normalized by a DIFFERENT B than the one")
    print("that built a(t)), keeping matter continuity and scalar KG intact")
    print("-- same a(t), same phibar_dot(t), same code path as Part K.")
    print("-" * 78)

    B_wrong = sp.Integer(5)  # != B=1 used to build a_cubed
    RHOBAR_A_offshell = B_wrong / a_cubed  # still propto a^-3: continuity intact
    friedmann_offshell = sp.simplify(
        3 * H_bg**2 - 8 * sp.pi * G_N * (RHOBAR_A_offshell + phibar_dot_bg**2 / 2)
    )
    print("  Friedmann residual (rhobar_A mismatched to B=5, a(t) built from B=1):")
    print(f"  {friedmann_offshell}")
    assert friedmann_offshell != 0, (
        "the mismatched-B background accidentally still satisfies Friedmann -- "
        "pick a different B_wrong, this test is not actually off-shell"
    )
    continuity_offshell = sp.simplify(sp.diff(RHOBAR_A_offshell, T) + 3 * H_bg * RHOBAR_A_offshell)
    assert continuity_offshell == 0, "matter continuity broken too -- not a clean one-EOM test"
    kg_offshell = sp.simplify(phibar_ddot_bg + 3 * H_bg * phibar_dot_bg)
    assert kg_offshell == 0, "scalar KG broken too -- not a clean one-EOM test"
    print("  -> CONFIRMED: Friedmann broken (nonzero residual above), matter")
    print("     continuity intact, scalar KG intact. Exactly one EOM violated.")

    cross_bg_offshell = cross_ghat0.subs(sp.diff(PHIBAR, T, 2), phibar_ddot_bg)
    cross_bg_offshell = cross_bg_offshell.subs(sp.diff(PHIBAR, T), phibar_dot_bg)
    cross_bg_offshell = cross_bg_offshell.subs(A, A_bg)
    cross_bg_offshell = cross_bg_offshell.subs(RHOBAR_A, RHOBAR_A_offshell)
    cross_bg_offshell = sp.simplify(cross_bg_offshell.doit())
    is_zero_offshell = cross_bg_offshell == 0
    print(f"\n  cross, OFF-SHELL (Friedmann broken) background, g_hat=0 = {cross_bg_offshell}")
    print(f"  Identically zero? {is_zero_offshell}")
    assert not is_zero_offshell, (
        "the OFF-SHELL background (Friedmann deliberately broken) gives ZERO -- "
        "this means `cross` is NOT actually sensitive to background "
        "self-consistency, and Part K's zero is vacuous, not evidence of "
        "anything. Report exactly this, it would overturn the whole finding."
    )
    print("  -> CONFIRMED NONZERO: `cross` genuinely discriminates on-shell")
    print("     from off-shell. Part K's zero is not a vacuous artifact of the")
    print("     algebraic SHAPE of the background -- it required Friedmann to")
    print("     ACTUALLY hold, not just continuity+KG.")

    print("\n" + "-" * 78)
    print("PART N -- [SKEPTIC-DEMANDED, Step 8a] NUMERIC cross-check,")
    print("independent of sp.simplify's own internal correctness: evaluate")
    print("the RAW (unsimplified) substituted expression at concrete numeric")
    print("(t, G_N, k) inside the physical domain, to high precision, as an")
    print("orthogonal check against a hypothetical simplify() false-positive")
    print("(a nonzero expression incorrectly reduced to exactly 0 -- a rare")
    print("but documented sympy risk with fractional-power/branch-cut terms).")
    print("-" * 78)

    cross_bg_raw = cross_ghat0.subs(sp.diff(PHIBAR, T, 2), phibar_ddot_bg)
    cross_bg_raw = cross_bg_raw.subs(sp.diff(PHIBAR, T), phibar_dot_bg)
    cross_bg_raw = cross_bg_raw.subs(A, A_bg)
    cross_bg_raw = cross_bg_raw.subs(RHOBAR_A, RHOBAR_A_bg)
    cross_bg_raw = cross_bg_raw.doit()  # NOTE: no sp.simplify() -- raw substituted form

    print("  [FIXED after first attempt] `cross_bg_raw` still contains PSI_k(T),")
    print("  DRHO_k(T), diff(DPHI_k,T) -- these are the UNKNOWNS of the closed")
    print("  perturbed system, not background quantities; `cross=0` is claimed")
    print("  as an IDENTITY in these free functions (every coefficient of each")
    print("  vanishes independently), so they must be replaced by fixed generic")
    print("  numeric constants FIRST -- BEFORE substituting T -- else T-first")
    print("  substitution turns e.g. Psi_k(T) into Psi_k(3), which no longer")
    print("  matches a substitution keyed on the generic Psi_k(T) object.")
    cross_bg_funcvals = cross_bg_raw.subs(
        {
            PSI_k: sp.Rational(3, 7),
            DRHO_k: sp.Rational(-2, 5),
            sp.diff(DPHI_k, T): sp.Rational(1, 11),
        }
    )

    for t_val, gn_val, k_val in [
        (sp.Integer(3), sp.Integer(1), sp.Integer(2)),
        (sp.Rational(7, 2), sp.Rational(1, 3), sp.Integer(5)),
    ]:
        numeric_val = cross_bg_funcvals.subs({T: t_val, G_N: gn_val, k: k_val}).evalf(50)
        print(f"  t={t_val}, G_N={gn_val}, k={k_val}: cross (raw, unsimplified) = {numeric_val}")
        assert abs(numeric_val) < sp.Float("1e-40"), (
            f"numeric evaluation at t={t_val},G_N={gn_val},k={k_val} is NOT ~0 "
            f"({numeric_val}) -- this would mean sp.simplify's symbolic '0' "
            "result in Part K was a FALSE POSITIVE. Report exactly this."
        )
    print("  -> CONFIRMED: raw (unsimplified) substituted expression evaluates")
    print("     to ~0 to 50-digit precision at two independent (t,G_N,k) points")
    print("     (fixed generic values for the free perturbation functions),")
    print("     via a computational path that does NOT depend on sp.simplify's")
    print("     own correctness. The symbolic zero in Part K is not a")
    print("     simplify() false positive.")

    print("\n" + "=" * 78)
    print("VERDICT [reworded after context-blind skeptic review, Step 8a --")
    print("the original wording below OVERCLAIMED 'confirmed for two")
    print("independent choices' when both points share the same Bianchi-")
    print("guaranteed on-shell family; fixed by adding Parts M-N, which are")
    print("the tests that actually discriminate, and by downgrading the")
    print("claim to what those tests actually establish.]")
    print("=" * 78)
    if is_zero_selfconsistent and not is_zero_offshell:
        print("RESULT: `cross` genuinely discriminates on-shell from off-shell")
        print("(Part M) and the on-shell zero is not a simplify() artifact")
        print("(Part N, independent numeric check). Within this scope (V=0,")
        print("g_hat=0, dust+stiff-fluid family, late-time branch), the 0i")
        print("constraint DOES stay consistent once the background genuinely,")
        print("jointly solves Friedmann+continuity+KG -- as GR's own Bianchi")
        print("identity mandates whenever the linearized algebra is correct.")
        print("This is best read as a REGRESSION/PLATFORM-VALIDATION result for")
        print("FINDING_P61's own Parts A-D closed system, not as new physics:")
        print("Bianchi guarantees this outcome for ANY correct algebra once the")
        print("background is genuinely on-shell. What it does NOT do: prove")
        print("Parts A-D contain no algebra error that happens to be dressed")
        print("by a factor proportional to a background EOM residual --such an")
        print("error would be invisible to this on-shell test by construction.")
    else:
        print("RESULT: the discriminating tests (Parts M/N) did NOT both pass")
        print("as expected -- see the specific assertion failure above. Do NOT")
        print("report the Part K zero as meaningful without resolving this.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
