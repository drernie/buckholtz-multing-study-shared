"""P61 -- close Psi_k(t) self-consistently: assemble the closed dynamical
system (00 Einstein, 0i momentum constraint, Phi=Psi, Phi/Psi-extended
scalar field equation, and matter continuity+Euler with GENERAL V_x, all
sourced by rho_phys per FINDING_P60's Route-B logic), then run the user's
own proposed decisive experiment -- constraint route vs evolution route --
to determine D2/D3/D4/D5.

SCOPE GATE (user's own, explicit, load-bearing): strictly V=0 truncation.
NO ad hoc closure ansatz (Psi_dot=c*H*Psi) anywhere -- FINDING_P48's own
EXACT (non-quasi-static) G_00=2[laplacian(Psi)/a^2-3*H*Psi_dot] already
supplies Psi's own evolution equation directly, with no extra assumption.

UNKNOWNS (functions of t, at fixed k): Psi_k, delta_phi_k, delta_rho_A_k,
V_x_k (or W_k:=(1-g_hat*phibar)*V_x_k). Background a(t),H(t),phibar(t),
rhobar_A(t) treated as given coefficients (matching FINDING_P46's own
"Friedmann not imposed" convention -- until Part F/G below, which
DIRECTLY TESTS the consequences of that choice).

COMPONENTS REUSED (verbatim formulas, NOT recomputed from Christoffels
except where marked NEW):
  FINDING_P48 -- exact G_00
  FINDING_P54 -- exact G_0i (Phi substituted by Psi)
  FINDING_P49 -- Phi=Psi (no anisotropic stress)
  FINDING_P57 -- Phi,Psi-extended scalar field equation (verified against
                 directly in Part A)
  FINDING_P59 -- Psi=0 special case of the NEW continuity+Euler below
  FINDING_P50A -- theta=0 special case of the NEW continuity below
  FINDING_P60 -- rho_phys Route-B logic (T_int+T_matter[rho_A] combines
                 into T_matter[rho_phys] alone)

NEW in this file (not previously derived anywhere in the campaign):
  - Q^0, Q^1 on the Psi-perturbed metric (Phi=Psi substituted) -- extends
    FINDING_P55/P56's own flat-metric Q^nu, explicitly named as a
    not-yet-started step in FINDING_P57's own scope list.
  - T_0i for both the scalar (phi) and matter[rho_phys] sectors.
  - Matter continuity + Euler equations with GENERAL V_x (not theta=0) on
    the Psi-perturbed metric, sourced by the above Q^0/Q^1 -- the
    Phi,Psi-extension of FINDING_P59's own construction, named as an open
    item in FINDING_P59/P60's own "what this does NOT establish" lists.
  - The decisive constraint-propagation test (Part F/G): does the 0i
    momentum constraint remain consistent under evolution via the 00
    equation + continuity + Euler + scalar field equation (the standard
    GR Bianchi-identity guarantee)? Tested directly, not assumed.

USER'S OWN PRE-REGISTERED OUTCOMES (D2/D3/D4/D5 -- tested here):
  D2 -- mu_phys(a,k)=1 identically after full closure (pure artifact).
  D3 -- mu_phys(k->infinity)=1, but mu_phys(a,k)!=1 at finite k (real,
        scale-dependent physics).
  D4 -- no unique algebraic mu(a,k) exists; the system is a genuinely
        history-dependent (kernel/ODE) response, not reducible to a
        single coefficient.
  D5 -- the current completion is structurally insufficient for a unique
        linear observable (missing background functions/matter terms) --
        a structural endpoint, not a reason to add a function by hand.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
    """Reused VERBATIM from FINDING_P48/.../P60's own already-verified helper."""
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
    """Reused VERBATIM from FINDING_P55/.../P60's own already-verified helper."""
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
    print("P61 -- closed dynamical system for Psi_k(t): assemble, then run")
    print("the decisive constraint-propagation test (D2/D3/D4/D5)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nSCOPE GATE: strictly V=0. NO ad hoc Psi_dot=c*H*Psi closure --")
    print("FINDING_P48's own EXACT G_00 supplies Psi's evolution directly.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART A -- real-space setup: Phi=Psi substituted (FINDING_P49),")
    print("Christoffels reused via the same machinery as P48/P54/P55-P60")
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

    print("  [POSITIVE CONTROL] box(phi)^(1) on this metric must match")
    print("  FINDING_P57's own already-verified geometric terms exactly")
    print("  (excluding the -g_hat*delta_rho source, which is P46's field")
    print("  equation RHS, not part of the pure geometric box operator):")
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
    assert check_p57 == 0, (
        "box(phi)^(1) on the Psi-perturbed metric does not match "
        "FINDING_P57's own already-verified geometric terms -- STOP, "
        "do not proceed with a broken Christoffel/box machinery"
    )
    print("  -> CONFIRMED exactly. Machinery matches FINDING_P57's own")
    print("     independently-skeptic-reviewed result.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART B -- Q^0, Q^1 on the Psi-perturbed metric (NEW -- extends")
    print("FINDING_P55/P56's own flat-metric Q^nu, named as a not-yet-")
    print("started step in FINDING_P57's own scope list)")
    print("-" * 78)
    dphi = [sp.diff(phi, c) for c in coords]
    d0_phi_full = ginv[0, 0] * dphi[0]
    d1_phi_full = ginv[1, 1] * dphi[1]
    field_eq_rhs = -ghat * rho_A  # box(phi)=-g_hat*rho_A on-shell (P46/P57's own relation)

    Q0 = sp.simplify(-sp.diff((field_eq_rhs * d0_phi_full), eps).subs(eps, 0))
    Q1 = sp.simplify(-sp.diff((field_eq_rhs * d1_phi_full), eps).subs(eps, 0))
    print(f"  Q^0 (Psi-extended) = {Q0}")
    print(f"  Q^1 (Psi-extended) = {Q1}")

    print("\n  [POSITIVE CONTROL] Psi->0 (function) must reduce EXACTLY to")
    print("  FINDING_P55/P56's own already-verified Q^0/Q^1:")
    Q0_flat = sp.simplify(Q0.subs(Psi, 0))
    Q1_flat = sp.simplify(Q1.subs(Psi, 0))
    expected_Q0_flat = -ghat * (deltarho_A * sp.diff(phibar, t) + rhobar_A * sp.diff(deltaphi, t))
    expected_Q1_flat = ghat * rhobar_A * sp.diff(deltaphi, x) / a**2
    assert sp.simplify(Q0_flat - expected_Q0_flat) == 0, "Q^0 does not reduce to P55's own result"
    assert sp.simplify(Q1_flat - expected_Q1_flat) == 0, "Q^1 does not reduce to P56's own result"
    print("  -> CONFIRMED: both reduce exactly, zero residual.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART C -- T_0i (NEW): phi kinetic piece + matter[rho_phys] piece,")
    print("T_00 (rho_phys, per FINDING_P60's own Route-B logic)")
    print("-" * 78)
    dphi_sq = sum(ginv[mu, nu] * dphi[mu] * dphi[nu] for mu in range(n) for nu in range(n))

    def T_phi_lower(mu, nu):
        gmn = g[mu, nu] if mu == nu else 0
        return dphi[mu] * dphi[nu] - sp.Rational(1, 2) * gmn * dphi_sq

    T_phi_01_lin = sp.simplify(sp.diff(sp.expand(T_phi_lower(0, 1)), eps).subs(eps, 0))
    T_phi_00_lin = sp.simplify(sp.diff(sp.expand(T_phi_lower(0, 0)), eps).subs(eps, 0))

    u0_upper_series = sp.series(1 / sp.sqrt(-g[0, 0]), eps, 0, 2).removeO()
    u1_upper_full = eps * Vx
    rho_phys_full = rho_A * (1 - ghat * phi)  # exact, matches FINDING_P59 Part 1

    u_0_lower = sp.expand(g[0, 0] * u0_upper_series)
    u_1_lower = sp.expand(g[1, 1] * u1_upper_full)
    T_matter_00_lin = sp.simplify(
        sp.diff(sp.expand(rho_phys_full * u_0_lower * u_0_lower), eps).subs(eps, 0)
    )
    T_matter_01_lin = sp.simplify(
        sp.diff(sp.expand(rho_phys_full * u_0_lower * u_1_lower), eps).subs(eps, 0)
    )

    print("  [POSITIVE CONTROL] T_01^(phi) must match the standard")
    print("  phibar_dot*d_x(delta_phi) form, and T_01^(int) must vanish")
    print("  identically (g_01=0 in this gauge, per FINDING_P49's own")
    print("  structural argument for any g_munu-proportional term):")
    assert sp.simplify(T_phi_01_lin - sp.diff(phibar, t) * sp.diff(deltaphi, x)) == 0
    T_int_01 = g[0, 1] * ghat * rho_A * phi
    assert T_int_01 == 0
    print("  -> CONFIRMED, both.")

    T_00_total = sp.expand(T_phi_00_lin + T_matter_00_lin)
    T_01_total = sp.expand(T_phi_01_lin + T_matter_01_lin)
    print(f"\n  T_00^total (rho_phys) = {T_00_total}")
    print(f"  T_01^total (rho_phys) = {T_01_total}")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART D -- matter continuity (nu=0) and Euler (nu=1), GENERAL")
    print("V_x, on the Psi-perturbed metric, sourced by Q^0/Q^1 (NEW --")
    print("the Phi,Psi-extension of FINDING_P59's own construction)")
    print("-" * 78)
    T_m_upper = [[0] * n for _ in range(n)]
    T_m_upper[0][0] = rho_phys_full * u0_upper_series * u0_upper_series
    T_m_upper[0][1] = rho_phys_full * u0_upper_series * u1_upper_full
    T_m_upper[1][0] = T_m_upper[0][1]
    T_m_upper[1][1] = 0  # O(eps^2)

    div_Tm_0 = sp.simplify(
        sp.diff(covariant_div_upper(T_m_upper, Gamma, coords, 0, n), eps).subs(eps, 0)
    )
    div_Tm_1 = sp.simplify(
        sp.diff(covariant_div_upper(T_m_upper, Gamma, coords, 1, n), eps).subs(eps, 0)
    )

    continuity_eq = sp.simplify(div_Tm_0 - Q0)
    euler_eq = sp.simplify(div_Tm_1 - Q1)

    rhobar_A_dot_sub = -3 * H * rhobar_A  # rho_A's own uncoupled background relation (P58)
    continuity_onshell = sp.simplify(continuity_eq.subs(sp.diff(rhobar_A, t), rhobar_A_dot_sub))
    euler_onshell = sp.simplify(euler_eq.subs(sp.diff(rhobar_A, t), rhobar_A_dot_sub))

    print("  [POSITIVE CONTROL] Psi->0 (function), on-shell, must reduce")
    print("  EXACTLY to FINDING_P59's own already-verified nu=0 result")
    print("  (M*[the simple uncoupled continuity bracket]):")
    matter_continuity_bare = rhobar_A * sp.diff(Vx, x) + sp.diff(deltarho_A, t) + 3 * H * deltarho_A
    cont_psi0_check = sp.simplify(continuity_onshell.subs(Psi, 0) - M * matter_continuity_bare)
    assert cont_psi0_check == 0, "continuity does not reduce to FINDING_P59's own Psi=0 result"
    print("  -> CONFIRMED, zero residual.")

    print("\n  Factoring the full (Psi != 0) continuity equation:")
    continuity_extra = sp.simplify(continuity_onshell - M * matter_continuity_bare)
    print(f"  continuity_onshell - M*[bare bracket] = {continuity_extra}")
    expected_extra = -3 * M * rhobar_A * sp.diff(Psi, t)
    assert sp.simplify(continuity_extra - expected_extra) == 0
    print("  -> CONFIRMED: factors exactly as -3*M*rhobar_A*Psi_dot. The")
    print("     closed continuity equation (continuity_onshell=0, M generically")
    print("     nonzero) is therefore:")
    print("     delta_rho_A_dot = -3*H*delta_rho_A - rhobar_A*d_x(V_x) + 3*rhobar_A*Psi_dot")
    print("     -- the STANDARD Newtonian-gauge continuity equation (Ma &")
    print("     Bertschinger form), now with the general velocity-divergence")
    print("     term FINDING_P50A's own theta=0 case did not have.")

    print("\n  Euler equation, W_x:=(1-g_hat*phibar)*V_x substitution (the")
    print("  SAME rescaling that collapsed FINDING_P59's own Euler equation):")
    Wx = sp.Function("W_x")(t, x, y, z)
    Vx_of_Wx = Wx / M
    euler_in_Wx = sp.simplify(euler_onshell.subs(Vx, Vx_of_Wx).doit())
    euler_in_Wx_cleared = sp.simplify(sp.expand(euler_in_Wx * a**2 / rhobar_A))
    expected_euler_Wx_times_a2 = (
        a**2 * (sp.diff(Wx, t) + 2 * H * Wx) + M * sp.diff(Psi, x) - ghat * sp.diff(deltaphi, x)
    )
    check_euler_Wx = sp.simplify(euler_in_Wx_cleared - expected_euler_Wx_times_a2)
    assert check_euler_Wx == 0, "Euler equation in W_x does not match the expected clean form"
    print("  -> CONFIRMED: the closed Euler equation is EXACTLY")
    print("     W_x_dot + 2*H*W_x = g_hat*d_x(delta_phi)/a^2 - M*d_x(Psi)/a^2")
    print("     -- FINDING_P59's own Psi=0 result, PLUS the standard")
    print("     Newtonian gravitational-force term (-d_x(Psi)/a^2), rescaled")
    print("     by the SAME M factor as the density conversion.")

    print("\n" + "=" * 78)
    print("PARTS A-D ESTABLISH THE CLOSED SYSTEM (real space). Parts E-G run")
    print("the decisive constraint-propagation test in k-space (real-space")
    print("integrals over x are not tractable symbolically for general")
    print("field profiles -- switching to an explicit single Fourier mode,")
    print("matching this campaign's own established k-space convention;")
    print("d_x->I*k, laplacian->-k^2, applied to the ALREADY-VERIFIED real-")
    print("space formulas above, not re-derived from scratch).")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART E -- k-space equations (00, 0i), and the four closed")
    print("evolution relations, all reused directly from Parts A-D")
    print("-" * 78)
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

    # 00 equation, solved for Psi_dot (k-space form of Part C's T_00_total)
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
    print("  Psi_dot (from the 00 equation) built.")

    # continuity (Part D, k-space), Psi_dot substituted
    cont_sub = (-3 * HH * DRHO_k - RHOBAR_A * Ik * VX_k + 3 * RHOBAR_A * sp.diff(PSI_k, T)).subs(
        sp.diff(PSI_k, T), Psidot_00
    )
    # scalar field eq (Part A/P57, k-space), Psi_dot substituted
    dphi_ddot_sub = (
        -3 * HH * sp.diff(DPHI_k, T)
        - (k**2) * DPHI_k / A**2
        + ghat * DRHO_k
        + 2 * PSI_k * sp.diff(PHIBAR, T, 2)
        + 6 * HH * PSI_k * sp.diff(PHIBAR, T)
        + 4 * sp.diff(PSI_k, T) * sp.diff(PHIBAR, T)
    ).subs(sp.diff(PSI_k, T), Psidot_00)
    print("  continuity + scalar-field-eq (Psi_dot substituted) built.")

    Psiddot_raw = sp.diff(Psidot_00, T)
    Psiddot_sub = Psiddot_raw.subs(sp.diff(PSI_k, T), Psidot_00)
    Psiddot_sub = Psiddot_sub.subs(sp.diff(DRHO_k, T), cont_sub)
    Psiddot_sub = Psiddot_sub.subs(sp.diff(DPHI_k, T, 2), dphi_ddot_sub)
    print("  Psi_ddot (fully substituted) built.")

    # 0i RAW constraint (unsolved -- affine in V_x, no division, cheap to
    # differentiate): C := 2*(Psi_dot+H*Psi)*I*k - 8*pi*G_N*T01_total_k
    C_raw = 2 * (sp.diff(PSI_k, T) + HH * PSI_k) * Ik - 8 * sp.pi * G_N * (
        -MM * A**2 * RHOBAR_A * VX_k + sp.diff(PHIBAR, T) * Ik * DPHI_k
    )
    C_sub = C_raw.subs(sp.diff(PSI_k, T), Psidot_00)
    C_poly = sp.Poly(sp.expand(C_sub), VX_k)
    P_coef = C_poly.coeff_monomial(VX_k)
    Q_coef = C_poly.coeff_monomial(1)
    print("  0i constraint C = P*V_x + Q extracted (affine, no division).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART F -- DECISIVE TEST: constraint route vs evolution route.")
    print("d/dt(0i constraint), fully substituted via the 00/continuity/")
    print("scalar/Euler equations, must vanish GIVEN the constraint itself")
    print("holds (standard GR Bianchi-identity guarantee) -- checked via")
    print("cross-multiplication (A*Q-B*P=0), not division, to stay tractable")
    print("-" * 78)
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
    print("  dC/dt = A*V_x + B extracted (all evolution equations substituted).")

    cross = sp.expand(A_coef * Q_coef - B_coef * P_coef)
    print("\n  [SANITY CONTROL, g_hat=0, FREE background -- this campaign's")
    print("  own established convention since FINDING_P46, a(t) NOT required")
    print("  to satisfy Friedmann] cross-multiplication residual:")
    cross_ghat0_free = sp.simplify(cross.subs(ghat, 0))
    is_zero_free = cross_ghat0_free == 0
    assert not is_zero_free, (
        "the free-background residual is now ZERO -- this would mean the "
        "D5 hypothesis is WRONG, or the machinery changed since this was "
        "last verified; report exactly this, do not force the D5 narrative"
    )
    print(f"  Identically zero? {is_zero_free}")
    print("  (If True: even the free-background convention is Bianchi-")
    print("  consistent at g_hat=0, and the D5 hypothesis below would need")
    print("  revisiting. If False, as independently found in this file's")
    print("  own development scratch work: the free-background convention")
    print("  breaks Bianchi consistency, structurally, before any MULTING-")
    print("  specific coupling is even switched on.)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART G -- decisive control: the SAME check, with an EXPLICIT")
    print("Friedmann-satisfying background (matter-dominated a=t^(2/3),")
    print("phibar=const, g_hat=0) -- must vanish if standard GR Bianchi")
    print("consistency is genuinely restored once Friedmann is imposed")
    print("-" * 78)
    a_fried = T ** sp.Rational(2, 3)
    rhobar_fried = sp.Rational(1, 6) / (sp.pi * G_N) / T**2  # chosen: 3H^2=8*pi*G_N*rhobar exactly
    friedmann_check = sp.simplify(
        3 * (sp.diff(a_fried, T) / a_fried) ** 2 - 8 * sp.pi * G_N * rhobar_fried
    )
    assert friedmann_check == 0, "chosen background does not actually satisfy Friedmann -- fix it"
    print("  Friedmann satisfied by construction (verified): 3H^2=8*pi*G_N*rhobar_A.")

    cross_ghat0_fried = sp.simplify(
        cross.subs(ghat, 0).subs(PHIBAR, 0).subs(A, a_fried).subs(RHOBAR_A, rhobar_fried).doit()
    )
    print(f"\n  cross-multiplication residual, Friedmann background: {cross_ghat0_fried}")
    is_zero_fried = cross_ghat0_fried == 0
    assert is_zero_fried, (
        "the phibar=const Friedmann-background residual is now NONZERO -- "
        "this contradicts the narrow Part G result, report exactly this"
    )
    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART H -- [SKEPTIC-CAUGHT ISOLATION TEST, Step 8a] Part G used")
    print("phibar=CONST (phibar_dot=0), which trivially satisfies its own")
    print("background Klein-Gordon equation but ALSO kills every term that")
    print("could couple the scalar sector into constraint propagation. Does")
    print("the SAME matter-only-Friedmann background restore consistency")
    print("with a GENUINE, NONZERO phibar_dot? This is the test that")
    print("actually isolates 'Friedmann is the fix' from 'phibar=0 is a")
    print("mask' -- run BEFORE trusting Part G's causal claim.")
    print("-" * 78)
    phibar_iso = -1 / T
    phibar_kg_check = sp.simplify(
        sp.diff(phibar_iso, T, 2) + 3 * (sp.diff(a_fried, T) / a_fried) * sp.diff(phibar_iso, T)
    )
    assert phibar_kg_check == 0, "phibar_iso does not satisfy its own background KG equation"
    print("  phibar=-1/t chosen: nonzero, AND independently verified to satisfy")
    print("  its own background KG eq (phibar_ddot+3H*phibar_dot=0 at g_hat=0).")

    cross_ghat0_iso1 = sp.simplify(
        cross.subs(ghat, 0)
        .subs(PHIBAR, phibar_iso)
        .subs(A, a_fried)
        .subs(RHOBAR_A, rhobar_fried)
        .doit()
    )
    print("\n  cross-multiplication residual, matter-only-Friedmann + nonzero,")
    print(f"  KG-consistent phibar = {cross_ghat0_iso1}")
    is_zero_iso1 = cross_ghat0_iso1 == 0
    print(f"  Identically zero? {is_zero_iso1}")
    assert not is_zero_iso1, (
        "matter-only Friedmann + nonzero KG-consistent phibar is now "
        "CONSISTENT -- this would overturn the corrected Part H finding, "
        "report exactly this, do not force the narrative"
    )

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART I -- does the SAME test pass if Friedmann is imposed for the")
    print("TOTAL (matter+scalar) background energy, 3H^2=8*pi*G_N*(rhobar_A+")
    print("phibar_dot^2/2), rather than matter alone -- even though this")
    print("choice of rhobar_A(t) then does NOT separately satisfy matter's")
    print("own continuity (rhobar_A~a^-3)? A deliberate, isolating diagnostic,")
    print("not a claim that this rhobar_A is physical.")
    print("-" * 78)
    phibar_dot_sq_half = sp.diff(phibar_iso, T) ** 2 / 2
    rhobar_total_fried = sp.simplify(
        3 * (sp.diff(a_fried, T) / a_fried) ** 2 / (8 * sp.pi * G_N) - phibar_dot_sq_half
    )
    total_friedmann_check = sp.simplify(
        3 * (sp.diff(a_fried, T) / a_fried) ** 2
        - 8 * sp.pi * G_N * (rhobar_total_fried + phibar_dot_sq_half)
    )
    assert total_friedmann_check == 0, "rhobar_total_fried does not satisfy TOTAL Friedmann"
    print(f"  rhobar_A(t) chosen for TOTAL Friedmann = {rhobar_total_fried}")
    print("  (note: does NOT purely scale as t^-2 -- does not separately")
    print("  satisfy matter's own background continuity; deliberate, isolating")
    print("  whether TOTAL-energy Friedmann alone is the missing piece.)")

    cross_ghat0_iso2 = sp.simplify(
        cross.subs(ghat, 0)
        .subs(PHIBAR, phibar_iso)
        .subs(A, a_fried)
        .subs(RHOBAR_A, rhobar_total_fried)
        .doit()
    )
    print("\n  cross-multiplication residual, TOTAL Friedmann + nonzero phibar")
    print(f"  = {cross_ghat0_iso2}")
    is_zero_iso2 = cross_ghat0_iso2 == 0
    print(f"  Identically zero? {is_zero_iso2}")
    assert not is_zero_iso2, (
        "TOTAL Friedmann (without separate matter continuity) + nonzero "
        "phibar is now CONSISTENT -- this would overturn the corrected "
        "Part I finding, report exactly this, do not force the narrative"
    )

    print("\n" + "=" * 78)
    print("VERDICT [CORRECTED after context-blind skeptic review, Step 8a --")
    print("the original verdict below OVERCLAIMED: 'Friedmann is precisely")
    print("the missing ingredient' was true only for the degenerate")
    print("phibar=const special case (Part G), not demonstrated in general.")
    print("Parts H-I show it is NOT sufficient once a genuine, self-consistent")
    print("nonzero scalar background is present -- fixed with real computation,")
    print("not softened language.]")
    print("=" * 78)
    print("D5 CONFIRMED, more narrowly and more honestly than originally")
    print("claimed: the closed dynamical system built in Parts A-D is NOT")
    print("Bianchi-consistent under this campaign's own free-background")
    print("convention (robust across every background tested, Parts F, H, I).")
    print()
    print("What Part G alone established (still valid, doubly-verified after")
    print("the skeptic-caught bug fixes): in the DEGENERATE special case where")
    print("the scalar background is entirely absent (phibar=const, no scalar")
    print("contribution to source anything), matter-only Friedmann (for a and")
    print("rhobar_A alone) DOES restore full consistency -- a real, clean,")
    print("narrow result: standard GR+dust (no scalar sector at all) is")
    print("internally consistent once its own background solves its own")
    print("Einstein equation, exactly as expected.")
    print()
    print("What Parts H-I show, SKEPTIC-CAUGHT: this does NOT generalize.")
    print("With a GENUINE, nonzero, background-KG-equation-satisfying phibar,")
    print("NEITHER matter-only Friedmann (Part H) NOR total-energy Friedmann")
    print("without separate matter continuity (Part I) restores consistency.")
    print("The most likely explanation: full Bianchi consistency requires the")
    print("ENTIRE background (a, phibar, rhobar_A) to be a genuine, MUTUALLY")
    print("self-consistent joint solution of Friedmann + matter's own")
    print("continuity + the scalar's own KG equation, ALL SIMULTANEOUSLY --")
    print("not 'add one extra relation on top of an otherwise free choice.'")
    print("Constructing such a solution (a coupled matter+scalar-field FRW")
    print("cosmology) is a genuinely larger task, NOT attempted here.")
    print()
    print("This is STILL the user's own pre-registered D5 -- if anything, a")
    print("DEEPER version of it: 'if closing the system requires background")
    print("functions or matter terms not yet supplied, this is a structural")
    print("endpoint, not a reason to introduce a new function by hand.' What")
    print("is missing is not one relation (Friedmann) but a genuinely")
    print("self-consistent background solution this campaign has never")
    print("constructed -- tied to the same long-open FINDING_P39 SI-")
    print("normalization gap (binding g_hat to G_N), now shown to be even")
    print("more load-bearing than the original Part G result suggested.")
    print()
    print("NOT YET DONE: constructing a genuinely self-consistent (a, phibar,")
    print("rhobar_A) coupled background solution and re-testing; the g_hat!=0")
    print("(coupled) case entirely; whether Friedmann should use rhobar_phys")
    print("rather than rhobar_A.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
