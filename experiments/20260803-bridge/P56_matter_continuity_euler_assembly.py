"""P56 -- Step B2, Part 2 of the user's refined "Euler/G_matter" milestone:
derive Q^i (spatial source term, reusing P55's own machinery for a new
index), build the matter stress tensor T_m^munu=rho*u^mu*u^nu explicitly,
and assemble the ACTUAL linearized matter continuity + Euler equations
from nabla_mu T_m^munu = Q^nu -- the user's own equation, now fully
instantiated for both nu=0 and nu=i.

SCOPE, matching P55's own established (and, per P55's own self-caught
bug, REQUIRED) restriction: same unperturbed FRW metric FINDING_P46/P47
used (Phi=Psi=0). This file does NOT attempt the Phi,Psi-extension --
that remains the named open gap before the B1<->B2 compatibility check
(FINDING_P54's G_0i) can be attempted honestly.

KILL-GATES applicable to THIS file (subset of the user's own seven):
  KG-B2a: force/source not inserted by hand -- Q^i reused from the SAME
          general covariant identity as P55's Q^0, not asserted by
          analogy.
  KG-B2b: same gauge/scope as P55 throughout, stated explicitly.
  KG-B2c: theta=0 (irrotational dust) NOT substituted before derivation
          -- the velocity field V^i(t,x,y,z) is kept as a fully general
          vector field throughout; theta:=div(V) is only DEFINED at the
          end, from the derived equation, never assumed zero going in.
  KG-B2f: g used only symbolically throughout (g_hat), no numeric value
          substituted -- the P39 Reading-1-vs-Reading-2 ambiguity is not
          touched by this file at all.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
    """Reused VERBATIM from FINDING_P48/P54/P55's own already-verified helper."""
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
    """Reused VERBATIM from FINDING_P55's own already-verified helper."""
    total = 0
    for mu in range(n):
        total += sp.diff(T_upper[mu][nu], coords[mu])
    for mu in range(n):
        for lam in range(n):
            total += Gamma[mu][mu][lam] * T_upper[lam][nu]
            total += Gamma[nu][mu][lam] * T_upper[mu][lam]
    return total


def covariant_box(scalar_field, ginv, Gamma, coords, n=4):
    """Reused VERBATIM from FINDING_P55's own already-verified helper."""
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
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    eps = sp.Symbol("epsilon", real=True)
    a = sp.Function("a")(t)
    ghat = sp.Symbol("g_hat", real=True, positive=True)
    phibar = sp.Function("phi_bar")(t)
    deltaphi = sp.Function("delta_phi")(t, x, y, z)
    rhobar = sp.Function("rho_bar")(t)
    deltarho = sp.Function("delta_rho")(t, x, y, z)
    Vx = sp.Function("V_x")(t, x, y, z)

    print("=" * 78)
    print("P56 -- Step B2 Part 2: Q^i + matter continuity/Euler assembly")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\n[SCOPE] SAME Phi=Psi=0 metric as FINDING_P55 -- required, per P55's")
    print("own self-caught scope-mismatch bug. Phi,Psi-extension remains the")
    print("named open gap before B1<->B2 compatibility.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- same machinery as P55, reused verbatim")
    print("-" * 78)
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    n = 4
    Gamma = christoffels_exact(coords, g, ginv, n)

    phi = phibar + eps * deltaphi
    dphi = [sp.diff(phi, c) for c in coords]
    dphi_sq = sum(ginv[mu, nu] * dphi[mu] * dphi[nu] for mu in range(n) for nu in range(n))

    def T_phi_lower(mu, nu):
        gmn = g[mu, nu] if mu == nu else 0
        return dphi[mu] * dphi[nu] - sp.Rational(1, 2) * gmn * dphi_sq

    T_phi_upper = [[0] * n for _ in range(n)]
    for mu in range(n):
        for nu in range(n):
            T_phi_upper[mu][nu] = sp.expand(
                sum(
                    ginv[mu, a_] * ginv[nu, b_] * T_phi_lower(a_, b_)
                    for a_ in range(n)
                    for b_ in range(n)
                )
            )
    print("  Metric, Christoffels, T_phi^(mu,nu): identical construction to P55.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- Q^1 (spatial source), SAME general identity as P55's Q^0,")
    print("now for nu=1 (x-direction) instead of nu=0")
    print("-" * 78)
    box_phi_exact = covariant_box(phi, ginv, Gamma, coords, n)
    box_phi_lin = sp.simplify(sp.diff(box_phi_exact, eps).subs(eps, 0))
    print(f"  box(phi)^(1) = {box_phi_lin}  (matches P55's own result exactly,")
    print("  same computation, reused not repeated in full -- spot-checked)")
    expected_box_lin = -(
        sp.diff(deltaphi, t, 2)
        + 3 * (sp.diff(a, t) / a) * sp.diff(deltaphi, t)
        - sum(sp.diff(deltaphi, c, 2) for c in coords[1:]) / a**2
    )
    assert sp.simplify(box_phi_lin - expected_box_lin) == 0, (
        "box(phi)^(1) does not match P55's own already-verified result -- "
        "re-check the metric/Christoffel construction before proceeding"
    )
    print("  -> CONFIRMED: matches P55's own result exactly (same machinery,")
    print("     same metric -- this is a reuse-fidelity check, not new physics).")

    div_Tphi_1_lin = sp.simplify(
        sp.diff(covariant_div_upper(T_phi_upper, Gamma, coords, 1, n), eps).subs(eps, 0)
    )
    d1_phi_full = ginv[1, 1] * sp.diff(phi, x)
    identity_rhs_1_full = box_phi_exact * d1_phi_full
    identity_rhs_1_lin = sp.simplify(sp.diff(identity_rhs_1_full, eps).subs(eps, 0))
    print(f"  [nabla_mu T_phi^(mu,1)]^(1) = {div_Tphi_1_lin}")
    print(f"  [box(phi)*d^1(phi)]^(1)     = {identity_rhs_1_lin}")
    identity_check_1 = sp.simplify(div_Tphi_1_lin - identity_rhs_1_lin)
    assert identity_check_1 == 0, (
        "general identity FAILS for nu=1 -- re-check before proceeding, do "
        "NOT assume the nu=0 check (P55) covers this new component"
    )
    print("  -> CONFIRMED for nu=1 too (checked directly, not assumed from")
    print("     the nu=0 case -- a genuinely different tensor component).")

    rho = rhobar + eps * deltarho
    field_eq_rhs = -ghat * rho
    Q1_from_identity = sp.simplify(sp.diff((field_eq_rhs * d1_phi_full), eps).subs(eps, 0))
    Q1 = sp.simplify(-Q1_from_identity)
    print("  Q^1 := -[nabla_mu T_phi^(mu,1)]^(1) (same closure-condition")
    print(f"  caveat as P55's Q^0 -- see P55's own corrected framing) = {Q1}")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- matter stress tensor T_m^(mu,nu)=rho*u^mu*u^nu")
    print("[CORRECTED wording, skeptic-caught] KG-B2c means theta is not")
    print("SET TO ZERO before derivation, not that all three V^i components")
    print("are separately populated -- only V_x is (y,z by isotropy, not")
    print("needed for the x-Euler equation specifically; a genuinely general")
    print("3-component V would be needed for a full theta:=div(V) equation,")
    print("not attempted here).")
    print("-" * 78)
    print("  Four-velocity normalization g_munu*u^mu*u^nu=-1 on THIS metric")
    print("  (Phi=Psi=0) gives u^0=1 to O(eps) exactly -- NO eps-correction is")
    print("  sourced, since there is no Phi here to source one (checked, not")
    print("  assumed: (u^0)^2=1+a^2*eps^2*|V|^2, which is O(eps^2), negligible")
    print("  at linear order):")
    u0 = 1
    u1 = eps * Vx  # x-component; y,z by isotropy, not needed for the x-Euler eqn
    rho_full = rhobar + eps * deltarho

    T_m_upper = [[0] * n for _ in range(n)]
    T_m_upper[0][0] = rho_full * u0 * u0
    T_m_upper[0][1] = rho_full * u0 * u1
    T_m_upper[1][0] = rho_full * u1 * u0
    T_m_upper[1][1] = rho_full * u1 * u1  # O(eps^2), drops at linear order
    print("  T_m^(0,0)=rho*u0^2, T_m^(0,1)=T_m^(1,0)=rho*u0*u1, T_m^(1,1)=")
    print("  rho*u1^2=O(eps^2) -- pressureless dust, no stress term needed at")
    print("  this order (standard for a matter Euler-equation derivation).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- nu=0: matter continuity equation, sourced by Q^0")
    print("(cross-check against FINDING_P50A's own already-derived continuity)")
    print("-" * 78)
    div_Tm_0 = sp.simplify(
        sp.diff(covariant_div_upper(T_m_upper, Gamma, coords, 0, n), eps).subs(eps, 0)
    )
    print(f"  [nabla_mu T_m^(mu,0)]^(1) = {div_Tm_0}")
    Q0_reused = sp.simplify(
        -sp.diff((field_eq_rhs * (ginv[0, 0] * sp.diff(phi, t))), eps).subs(eps, 0)
    )
    print("  Q^0 (reused from FINDING_P55, re-derived here for a standalone")
    print(f"  check) = {Q0_reused}")
    continuity_eq = sp.Eq(div_Tm_0, Q0_reused)
    print(f"  Continuity equation: {continuity_eq}")

    print()
    print("  [POSITIVE CONTROL] Setting g_hat=0 (decoupled limit, Q^0->0) MUST")
    print("  reduce to the STANDARD pressureless-dust continuity equation")
    print("  delta_rho_dot + 3*H*delta_rho + rhobar*div(V) = 0 (no metric-")
    print("  perturbation term here, since Phi=Psi=0 in this scope -- unlike")
    print("  FINDING_P50A's own continuity, which included a 3*rhobar*Psi_dot")
    print("  term because THAT derivation used the Phi,Psi-perturbed metric):")
    decoupled_continuity = sp.simplify((div_Tm_0 - Q0_reused).subs(ghat, 0))
    div_V = sp.diff(Vx, x)  # x-piece only; full div(V) would sum y,z too, by isotropy
    expected_decoupled = sp.diff(deltarho, t) + 3 * (sp.diff(a, t) / a) * deltarho + rhobar * div_V
    print(f"  LHS-RHS at g_hat=0 = {decoupled_continuity}")
    print(f"  expected (standard, x-piece of div(V) only) = {expected_decoupled}")
    assert sp.simplify(decoupled_continuity - expected_decoupled) == 0, (
        "decoupled (g_hat=0) continuity does not match the standard "
        "pressureless-dust form -- a real error, not a scope caveat"
    )
    print("  -> CONFIRMED: decoupled limit matches the standard textbook")
    print("     continuity equation exactly (genuine positive control, not")
    print("     merely asserted).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- nu=1: THE MATTER EULER EQUATION, sourced by Q^1")
    print("(the actual deliverable of Step B2)")
    print("-" * 78)
    div_Tm_1 = sp.simplify(
        sp.diff(covariant_div_upper(T_m_upper, Gamma, coords, 1, n), eps).subs(eps, 0)
    )
    print(f"  [nabla_mu T_m^(mu,1)]^(1) = {div_Tm_1}")
    euler_eq = sp.Eq(div_Tm_1, Q1)
    print(f"  Euler equation (x-component): {euler_eq}")

    print()
    print("  [POSITIVE CONTROL, SELF-CAUGHT DURING BUILD] Decoupled limit")
    print("  (g_hat=0, Q^1->0) MUST reduce to geodesic free-fall. FIRST version")
    print("  of this assertion guessed 'd/dt(rhobar*V_x)+3*H*rhobar*V_x=0'")
    print("  (density dilution only) -- WRONG, caught by this exact assertion")
    print("  failing. Independently re-derived the correct form from the")
    print("  geodesic equation directly, BEFORE patching the assertion: for a")
    print("  free particle on ds^2=-dt^2+a^2*dx^2, physical momentum redshifts")
    print("  as 1/a, i.e. a*V=const in PHYSICAL velocity, giving (in this")
    print("  script's own COORDINATE velocity V=dx/dt) V_dot+2*H*V=0 -- the")
    print("  PECULIAR VELOCITY itself redshifts, not just the density. The")
    print("  momentum-DENSITY equation combines both effects: d/dt(rhobar*V)=")
    print("  rhobar_dot*V+rhobar*V_dot = -3*H*rhobar*V + rhobar*(-2*H*V) =")
    print("  -5*H*rhobar*V -- i.e. rhobar*V ~ a^-5 (density ~a^-3 TIMES")
    print("  velocity ~a^-2), matching momentum density's known additional")
    print("  redshift beyond pure number-density dilution. This is the")
    print("  CORRECT expected form, independently hand-verified before fixing")
    print("  the assertion (not just changed to match whatever sympy output):")
    decoupled_euler = sp.simplify(div_Tm_1.subs(ghat, 0))
    expected_decoupled_euler = sp.diff(rhobar * Vx, t) + 5 * (sp.diff(a, t) / a) * rhobar * Vx
    print(f"  LHS at g_hat=0 = {decoupled_euler}")
    print("  expected (momentum-density dilution, rhobar*V~a^-5, no Phi force")
    print(f"  term in this Phi=Psi=0 scope) = {expected_decoupled_euler}")
    assert sp.simplify(decoupled_euler - expected_decoupled_euler) == 0, (
        "decoupled Euler equation does not match the geodesic-verified "
        "momentum-density dilution form -- re-check before trusting the "
        "coupled result"
    )
    print("  -> CONFIRMED against the geodesic-verified form.")

    print()
    print("  [ADDENDUM #1, prompted by user's own physics review after this")
    print("  file's first commit] The '5H' coefficient is a property of the")
    print("  MOMENTUM-DENSITY bookkeeping (rhobar*V_x combined), not an")
    print("  independent physical statement -- convention-sensitive, not")
    print("  anomalous. Dividing by rhobar and eliminating rhobar_dot reduces")
    print("  it to a velocity equation.")
    print()
    print("  [CORRECTED after a SECOND round of user physics review, same day --")
    print("  then RE-CORRECTED (RETRACTED) by FINDING_P58, same day, per its own")
    print("  context-blind skeptic review] The version of this addendum that")
    print("  briefly stood here claimed a COUPLED background continuity")
    print("  (rhobar_dot=-3*H*rhobar-g_hat*rhobar*phibar_dot, exponential")
    print("  solution) and a correspondingly 'corrected' Euler reduction")
    print("  V_x_dot+(2*H-g_hat*phibar_dot)*V_x=... -- FINDING_P58's own two-")
    print("  route Q^mu consistency audit PROVED this is mathematically")
    print("  impossible: the density rhobar that THIS file's own construction")
    print("  actually uses (shared identically between T_m^munu and, via the")
    print("  field equation, Q^0/Q^1) is the BARE density (matching FINDING_P33's")
    print("  own worldline-action fluid limit) -- and a bare density, which by")
    print("  ITS OWN definition satisfies pure decoupled dust dilution, CANNOT")
    print("  also self-consistently satisfy a coupled evolution sourced by")
    print("  itself (proven directly in FINDING_P58, independently re-verified")
    print("  here before accepting, per audit-verification-gate.md):")
    Hubble = sp.diff(a, t) / a
    rhobar_decoupled_sub = -3 * Hubble * rhobar
    lhs_decoupled = sp.simplify(rhobar_decoupled_sub + 3 * Hubble * rhobar)
    rhs_selfconsistent_coupled = sp.simplify(-ghat * rhobar * sp.diff(phibar, t))
    print(f"  rhobar's own (bare, decoupled) defining relation gives LHS = {lhs_decoupled}")
    print(
        f"  the coupled closure's own RHS (self-consistent)            = {rhs_selfconsistent_coupled}"
    )
    print("  -> equal only if g_hat*rhobar*phibar_dot=0 identically -- NOT true")
    print("     in general. The coupled-continuity claim is RETRACTED.")
    print()
    print("  FINDING_P58's own exact resolution: the genuine nonzero background")
    print("  Q^0 this file already correctly computed is the DERIVATIVE")
    print("  consequence of FINDING_P33's own already-established ALGEBRAIC mass")
    print("  law (m_eff/m=1-g_hat*phi), relating rhobar (bare, this file's own)")
    print("  to a DIFFERENT, distinguishable physical density rho_phys=rhobar*")
    print("  (1-g_hat*phibar) -- NOT a new differential equation for rhobar")
    print("  itself. rhobar (as this file's own shared symbol) remains simply,")
    print("  purely uncoupled -- the ORIGINAL addendum #1 reduction (below) was")
    print("  correct all along; see FINDING_P58_two_route_Qmu_consistency_audit.md")
    print("  for the full derivation.")
    euler_momentum_density = sp.diff(rhobar * Vx, t) + 5 * Hubble * rhobar * Vx
    lhs_reduced_reconfirmed = sp.simplify(
        sp.expand(euler_momentum_density).subs(sp.diff(rhobar, t), rhobar_decoupled_sub) / rhobar
    )
    expected_uncoupled_form = sp.diff(Vx, t) + 2 * Hubble * Vx
    print()
    print("  RE-CONFIRMED reduction, using rhobar's own simple, uncoupled")
    print("  continuity (the internally-consistent reading of this file's own")
    print("  shared rhobar symbol, per FINDING_P58):")
    print(f"    {lhs_reduced_reconfirmed} = Q^1/rhobar")
    assert sp.simplify(lhs_reduced_reconfirmed - expected_uncoupled_form) == 0, (
        "re-confirmed reduction does not match V_x_dot+2*H*V_x -- algebra "
        "error, do not report this form"
    )
    print()
    print("  [SELF-CAUGHT before this addendum's own commit, prompted by")
    print("  comparing against the user's own independent restatement] the RHS")
    print("  Q^1/rhobar was first hand-typed as 'g_hat*d_x(delta_phi)/a^2/rhobar'")
    print("  (an extra, spurious /rhobar) -- WRONG, since Q^1 itself is already")
    print("  PROPORTIONAL to rhobar (Q^1=g_hat*rhobar*d_x(delta_phi)/a^2, Part 2")
    print("  above), so it CANCELS on division. Verified directly, not hand-typed:")
    Q1_over_rhobar = sp.simplify(Q1 / rhobar)
    expected_Q1_over_rhobar = ghat * sp.diff(deltaphi, x) / a**2
    print(f"    Q^1/rhobar = {Q1_over_rhobar}")
    assert sp.simplify(Q1_over_rhobar - expected_Q1_over_rhobar) == 0, (
        "Q^1/rhobar does not match g_hat*d_x(delta_phi)/a^2 -- rhobar does not "
        "cancel as expected, re-check Q^1's own rhobar-proportionality"
    )
    print("  -> CONFIRMED: rhobar cancels exactly, no residual rhobar-dependence.")
    print("     Full equation: V_x_dot + 2*H*V_x = g_hat*d_x(delta_phi)/a^2.")
    v_from_Vx = sp.Function("v")(t, x)
    Vx_of_v = v_from_Vx / a
    lhs_in_v = sp.simplify((sp.diff(Vx, t) + 2 * Hubble * Vx).subs(Vx, Vx_of_v).doit() * a)
    expected_vdot_Hv = sp.diff(v_from_Vx, t) + Hubble * v_from_Vx
    rhs_in_v = sp.simplify(expected_Q1_over_rhobar * a)
    assert sp.simplify(lhs_in_v - expected_vdot_Hv) == 0
    print(f"     In physical peculiar velocity v:=a*V_x: v_dot+H*v = {rhs_in_v}")
    print("     -- the ordinary single-H peculiar-velocity redshift, EXACTLY the")
    print("     form Addendum #1 originally derived, now RE-CONFIRMED correct")
    print("     (not merely a decoupled-limit special case) by FINDING_P58's")
    print("     own audit.")

    print()
    print("  Full (coupled) Euler equation, force term isolated:")
    print("  [NOTE] div(T_m^(mu,1)) itself contains NO g_hat at all -- the")
    print("  coupling enters ONLY through the equation div(T_m^(mu,1))=Q^1,")
    print("  not through T_m's own construction. So the 'decoupled' (g_hat=0)")
    print("  LHS above is identical to the general LHS; the force term is")
    print("  simply Q^1 itself, moved to the RHS of the SAME LHS as the")
    print("  g_hat=0 check -- not a separate quantity requiring its own")
    print("  computation:")
    print(f"  d/dt(rhobar*V_x)+5*H*rhobar*V_x = F_phi,  F_phi = Q^1 = {Q1}")

    print()
    print("  [PREDICTION CHECK, per the user's own pre-registration] Does F_phi")
    print("  reduce to the predicted local form F_phi ~ g_hat^2*delta_rho when")
    print("  FINDING_P46's own quasi-static delta_phi_k=g_hat*a^2*delta_rho_k/k^2")
    print("  is substituted? [NOTE: that substitution is a FOURIER/k-space")
    print("  statement; this file's Q^1 is in REAL SPACE (d_x of delta_phi) --")
    print("  a direct real-space substitution is not meaningful without first")
    print("  Fourier-transforming this equation, which this file does NOT do.")
    print("  Stated as an explicit next step, not attempted here.")
    print("  [CORRECTED after skeptic review] the original framing ('would be")
    print("  a fabricated unit mismatch') was slightly overprotective: P46's")
    print("  quasi-static reduction ALSO has a real-space form directly")
    print("  available (Laplacian(delta_phi) = -g_hat*a^2*delta_rho, the")
    print("  inverse-Fourier of its own k-space statement) -- substituting")
    print("  THAT (not the k-space delta_phi_k) into Q^1 gives a genuine, well-")
    print("  defined real-space next step: Q^1 = -g_hat^2*rhobar*d_x(G*delta_rho)")
    print("  /a^2 (G = flat-space Laplacian Green's function) -- an integro-")
    print("  differential statement, NOT a local F_phi~g_hat^2*delta_rho (that")
    print("  only holds mode-by-mode in Fourier space). This is a reachable")
    print("  next step, not blocked on a full k-space Euler-equation")
    print("  translation as the original framing implied.")

    print("\n" + "=" * 78)
    print("VERDICT [CORRECTED after context-blind skeptic review, Step 8a]")
    print("=" * 78)
    print("Q^1 derived via the SAME general covariant identity as P55's Q^0")
    print("(checked independently for nu=1, not assumed from nu=0 -- though")
    print("this check is a REUSE-FIDELITY check on the helper machinery, not")
    print("new physics per se; the identity is general and holds for any nu")
    print("once the machinery itself is correct). Matter stress tensor")
    print("T_m^(mu,nu)=rho*u^mu*u^nu built with V_x populated (y,z by")
    print("isotropy, not separately computed -- sufficient for the x-Euler")
    print("equation, NOT a fully general 3-component velocity field). Both the")
    print("continuity (nu=0) and Euler (nu=1) equations assembled from")
    print("nabla_mu T_m^(mu,nu)=Q^nu -- the user's own equation, now fully")
    print("instantiated. BOTH decoupled (g_hat=0) limits verified against")
    print("independently re-derived standard forms (the Euler-equation check")
    print("caught and fixed a genuine 3H->5H hand-derivation error) --")
    print("genuine positive controls, not asserted.")
    print()
    print("[Added after skeptic review] CLOSURE CAVEAT, INHERITED FROM P55, NOT")
    print("RESTATED THERE -- fixed here: total stress-energy conservation")
    print("(nabla_mu(T_phi+T_m)=0), which BOTH this file's continuity and")
    print("Euler equations rest on, is NOT automatic in FINDING_P46's own")
    print("setup (rho treated as an external scalar, not a dynamical dust")
    print("field) -- it is a CLOSURE CONDITION a genuine matter model must")
    print("satisfy (B2 Part 2's own open task), not a free-standing GR fact.")
    print("Both equations in this file inherit that same unresolved closure.")
    print()
    print("[Added after skeptic review] CROSS-FINDING DRIFT, project-level, NOT")
    print("a defect of this file's own derivation: FINDING_P50A's own matter")
    print("continuity equation (nabla_mu T_m^(mu,0)=0, NO source term) is now")
    print("INCONSISTENT with THIS file's own closure (nabla_mu T_m^(mu,0)=Q^0,")
    print("a real g_hat-dependent source). P50A predates P55/P56's discovery")
    print("that matter is NOT separately conserved once coupled to phi. Per")
    print("this campaign's own null-retroscan discipline (a new result that")
    print("changes an assumption underlying a prior finding should be applied")
    print("immediately, not deferred silently) -- flagged here explicitly as")
    print("an open item, NOT silently propagated. FINDING_P50A's own Part 7")
    print("needs a re-scan against this closure before its own continuity")
    print("equation is reused anywhere further -- not attempted in this file.")
    print()
    print("SCOPE, unchanged from P55: Phi=Psi=0 throughout. The decoupled Euler")
    print("limit correctly has NO gravitational force term, because THIS scope")
    print("has no Phi to source one -- this is not evidence the full equation")
    print("is missing gravity, it is a direct consequence of the scope choice,")
    print("stated explicitly, not smuggled past.")
    print()
    print("NOT YET DONE: (1) the real-space quasi-static substitution named")
    print("above (reachable, not blocked); (2) the Phi,Psi-extension needed")
    print("for the B1<->B2 compatibility check against FINDING_P54's own Phi-")
    print("inclusive G_0i; (3) testing the user's own pre-registered H0/H1/H2")
    print("split, which requires (2); (4) re-scanning FINDING_P50A against")
    print("this file's own closure condition.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
