"""P46 -- first of two steps toward the campaign's original P36 row
(PLAN_final_goal_20260814.md): "quasi-static cosmological reduction,
subhorizon approximation." Explicitly flagged as the SAME CATEGORY of
step (local static result -> broader cosmological context) that produced
this campaign's single worst correction (P36, 5/6 skeptic issues
FALSIFIED, per the plan's own status log) -- built with maximal care as
a direct consequence: every equation below is re-derived from the action
via Euler-Lagrange, never pattern-matched from a prior static/homogeneous
result by analogy.

Split into two P-steps deliberately (this campaign's established
granularity, not one sprawling derivation):
  P46 (this file) -- derive the general (FRW, inhomogeneous) scalar field
    equation from the SAME Lagrangian P34/P35 already used, then solve it
    in the subhorizon quasi-static limit for delta(phi)_k(a).
  P47 (not yet built) -- derive the perturbed Einstein equations in the
    same limit (extending P38/P40's machinery to FRW) and assemble
    gamma(a,k).

PART 1 -- derive the general FRW field equation via Euler-Lagrange on the
FULL Lagrangian density (sqrt(-g)=a^3, g^{ij}=delta^{ij}/a^2), not by
hand and not by analogy.

PART 2 -- TWO positive controls, both required before trusting anything
new: (a) homogeneous limit (grad(phi)=0) must reduce EXACTLY to P34's own
phi_ddot+3H*phi_dot=g_hat*rho_0. (b) static+flat limit (a=1, i.e. H=0)
must reduce EXACTLY to P35's own phi_ddot-laplacian(phi)=g_hat*rho.

PART 3 -- because this equation is EXACTLY LINEAR in phi and rho (no
V(phi) term here -- P34's already-known stiff-fluid-era structure, same
fact P44/P45 already exploited), splitting phi=phi_bar(t)+delta_phi(t,x)
and rho=rho_bar(t)+delta_rho(t,x) gives a delta_phi equation of EXACTLY
the same functional form as the full equation -- no perturbative
expansion needed for this step, stated explicitly and verified, not
assumed.

PART 4 -- Fourier transform the linear delta_phi equation (exact, still
second-order in time), then apply the SUBHORIZON QUASI-STATIC
approximation (k/(aH) >> 1: drop delta_phi_ddot and 3*H*delta_phi_dot
relative to the (k/a)^2 term) -- flagged explicitly as an APPROXIMATION
with a stated validity regime, not an exact result. Solve the resulting
algebraic relation for delta_phi_k(a).

PART 5 -- third positive control: does the QUASI-STATIC Fourier solution,
in the static+flat (a=1) limit, for a point-mass source, reduce via the
ALREADY-ESTABLISHED (P19, CONFIRMED-REAL) real-space Green's function
1/(4*pi*r) of the Laplacian to EXACTLY P35's own real-space solution
phi(r)=g_hat*M/(4*pi*r)? This is the load-bearing consistency check that
the whole quasi-static machinery connects back to already-verified
ground, not just a plausible-sounding new construction.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    ghat = sp.Symbol("g_hat", positive=True)

    print("=" * 78)
    print("P46 -- FRW-perturbed field equation, subhorizon quasi-static solve")
    print("First of two steps toward the campaign's real P36 (quasi-static")
    print("cosmological reduction) -- same risk category as the campaign's")
    print("worst correction (P36), built with maximal explicit derivation.")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- FRW field equation via Euler-Lagrange (not by hand, not by")
    print("analogy to any prior static/homogeneous result)")
    print("-" * 78)
    a = sp.Function("a")(t)
    phi = sp.Function("phi")(t, x, y, z)
    rho = sp.Function("rho")(t, x, y, z)
    phi_dot = sp.diff(phi, t)
    grad_sq = sum(sp.diff(phi, c) ** 2 for c in (x, y, z))
    coords = (x, y, z)

    print("  Same Lagrangian density P34/P35 both used, restored to FRW:")
    print("  L = a^3*(1/2)*phi_dot^2 - a*(1/2)*(grad phi)^2 - a^3*rho*(1-g_hat*phi)")
    print("  (sqrt(-g)=a^3 for flat FRW; g^{ij}=delta^{ij}/a^2 raises the gradient)")
    L = (
        a**3 * sp.Rational(1, 2) * phi_dot**2
        - a * sp.Rational(1, 2) * grad_sq
        - a**3 * rho * (1 - ghat * phi)
    )
    dL_dphidot = sp.diff(L, phi_dot)
    eom_time = sp.diff(dL_dphidot, t)
    dL_dgrad = [sp.diff(L, sp.diff(phi, c)) for c in coords]
    eom_space = sum(sp.diff(dL_dgrad[i], coords[i]) for i in range(3))
    dL_dphi = sp.diff(L, phi)
    field_eq_raw = sp.simplify(eom_time + eom_space - dL_dphi)
    field_eq = sp.simplify(field_eq_raw / a**3)
    print(f"  (EL residual)/a^3 = {field_eq}")
    print("  Rearranged: phi_ddot + 3*H*phi_dot - laplacian(phi)/a^2 = g_hat*rho")
    print("  where H := a_dot/a (standard definition, substituted for readability")
    print("  only -- the assertion below checks the UNSUBSTITUTED sympy form).")

    a_dot = sp.diff(a, t)
    H = a_dot / a
    phi_ddot = sp.diff(phi, t, 2)
    laplacian = sum(sp.diff(phi, c, 2) for c in coords)
    target_form = phi_ddot + 3 * H * phi_dot - laplacian / a**2 - ghat * rho
    assert sp.simplify(field_eq - target_form) == 0, (
        "derived equation does not match the claimed FRW form"
    )

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- TWO positive controls, both required before trusting this")
    print("-" * 78)
    print("  (a) Homogeneous limit -- NOT checked by substituting into the")
    print("      already-derived field_eq (that would be tautological: comparing")
    print("      a freshly-written formula to an identically-written one proves")
    print("      nothing). Instead, INDEPENDENTLY re-derive from a genuinely")
    print("      homogeneous (t-only) candidate Lagrangian, same method as Part 1:")
    phibar = sp.Function("phi_bar")(t)
    rhobar = sp.Function("rho_bar")(t)
    phibar_dot = sp.diff(phibar, t)
    L_homog = a**3 * sp.Rational(1, 2) * phibar_dot**2 - a**3 * rhobar * (1 - ghat * phibar)
    dL_dphibardot = sp.diff(L_homog, phibar_dot)
    eom_time_homog = sp.diff(dL_dphibardot, t)
    dL_dphibar = sp.diff(L_homog, phibar)
    homog_eq_raw = sp.simplify(eom_time_homog - dL_dphibar)
    homog_eq = sp.simplify(homog_eq_raw / a**3)
    p34_eq = sp.diff(phibar, t, 2) + 3 * H * phibar_dot - ghat * rhobar
    assert sp.simplify(homog_eq - p34_eq) == 0, "homogeneous re-derivation does not match P34"
    print(f"      independently re-derived homogeneous equation = {homog_eq}")
    print("      -> MATCHES P34's phi_ddot+3*H*phi_dot=g_hat*rho_bar exactly.")
    print("      (Reuses the same underlying Lagrangian as Part 1's general")
    print("      derivation, so exact agreement is REQUIRED by construction, not")
    print("      surprising independent evidence -- same scoping discipline P43")
    print("      applied to its own Noether-current check; this still catches a")
    print("      real class of bug: a wrong a(t)-power or a sign slip in Part 1's")
    print("      general derivation, since that derivation was NOT reused here.)")

    print("\n  (b) Static + flat limit (a=1, so H=0 and 1/a^2=1) -- must match")
    print("      P35's own phi_ddot-laplacian(phi)=g_hat*rho EXACTLY:")
    static_flat_eq = field_eq.subs(a, sp.Integer(1))
    p35_eq = phi_ddot - laplacian - ghat * rho
    assert sp.simplify(static_flat_eq - p35_eq) == 0
    print(f"      static+flat limit = {sp.simplify(static_flat_eq)}")
    print("      -> MATCHES P35's phi_ddot-laplacian(phi)=g_hat*rho exactly.")
    print("  Both controls PASS -- the general FRW equation correctly contains")
    print("  both previously-established results as limiting cases.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- is 'perturbation theory' here exact or approximate? Check,")
    print("don't assume.")
    print("-" * 78)
    phibar = sp.Function("phi_bar")(t)
    deltaphi = sp.Function("delta_phi")(t, x, y, z)
    rhobar = sp.Function("rho_bar")(t)
    deltarho = sp.Function("delta_rho")(t, x, y, z)
    eps = sp.Symbol("epsilon", real=True)

    full_phi = phibar + eps * deltaphi
    full_rho = rhobar + eps * deltarho
    field_eq_split = target_form.subs(phi, full_phi).subs(rho, full_rho)
    field_eq_split = field_eq_split.doit()
    dEdeps = sp.diff(field_eq_split, eps)
    dEdeps_at0 = sp.simplify(dEdeps.subs(eps, 0))
    print(f"  d(field eq)/d(epsilon) |_(epsilon=0) = {dEdeps_at0}")
    expected_linear_eq = (
        sp.diff(deltaphi, t, 2)
        + 3 * H * sp.diff(deltaphi, t)
        - laplacian.subs(phi, deltaphi) / a**2
        - ghat * deltarho
    )
    assert sp.simplify(dEdeps_at0 - expected_linear_eq) == 0
    print("  -> CONFIRMED: delta_phi obeys EXACTLY the same functional form as the")
    print("     full field equation (no extra terms from expanding around phi_bar).")
    print("     This is a consequence of the field equation being exactly LINEAR")
    print("     in phi and rho -- no V(phi) term exists at this stage (same fact")
    print("     P44/P45 already used), so there is no perturbative approximation")
    print("     in THIS step -- delta_phi's equation is exact, not leading-order.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- Fourier transform (exact) + subhorizon quasi-static")
    print("approximation (explicitly flagged, NOT exact)")
    print("-" * 78)
    print("  Fourier space (k := comoving wavenumber, laplacian -> -k^2), EXACT:")
    print("    delta_phi_k_ddot + 3*H*delta_phi_k_dot + (k^2/a^2)*delta_phi_k")
    print("    = g_hat*delta_rho_k")
    print()
    print("  SUBHORIZON QUASI-STATIC APPROXIMATION (validity: k/(a*H) >> 1 --")
    print("  the (k/a)^2 term then dominates over delta_phi_ddot ~ H^2*delta_phi")
    print("  and 3*H*delta_phi_dot ~ H^2*delta_phi by an explicit factor of")
    print("  (k/(a*H))^2 >> 1 -- standard argument, flagged here as an")
    print("  APPROXIMATION with a stated regime, not asserted as exact):")
    k, a_sym, H_sym, ghat_sym = sp.symbols("k a H g_hat", positive=True)
    deltaphi_k, deltarho_k = sp.symbols("deltaphi_k deltarho_k")
    quasi_static_eq = sp.Eq((k**2 / a_sym**2) * deltaphi_k, ghat_sym * deltarho_k)
    solved = sp.solve(quasi_static_eq, deltaphi_k)
    assert len(solved) == 1
    deltaphi_k_solution = solved[0]
    print("    (k^2/a^2)*delta_phi_k = g_hat*delta_rho_k")
    print(f"    -> delta_phi_k = {deltaphi_k_solution}")
    print("    = g_hat * a^2 * delta_rho_k / k^2")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- load-bearing consistency check: does this reduce back to")
    print("P35's own real-space static solution?")
    print("-" * 78)
    print("  Static+flat limit of the quasi-static Fourier solution (a=1):")
    static_limit = deltaphi_k_solution.subs(a_sym, 1)
    print(f"    delta_phi_k|_(a=1) = {static_limit}  =  g_hat*delta_rho_k/k^2")
    print("  This is EXACTLY the standard Fourier-space Green's function relation")
    print("  for -laplacian(phi)=g_hat*rho (Fourier transform of -laplacian is")
    print("  +k^2, so 1/k^2 is its Green's function in k-space). Using the")
    print("  ALREADY-ESTABLISHED (P19, CONFIRMED-REAL) real-space Green's function")
    print("  laplacian[1/(4*pi*r)] = -delta^3(x), the real-space inverse transform")
    print("  of g_hat*M/k^2 (point mass, delta_rho_k=M in the standard convention)")
    print("  is EXACTLY g_hat*M/(4*pi*r) -- P35's own static solution, unchanged.")
    print("  This is not re-derived symbolically here (the 3D Fourier transform of")
    print("  1/k^2 -> 1/(4*pi*r) is the SAME already-cited P19 Green's function")
    print("  fact, just read in the other direction) -- flagged explicitly as")
    print("  reused, not re-proven, consistent with this project's own established")
    print("  practice of not re-deriving already-CONFIRMED-REAL building blocks.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("General FRW field equation derived via Euler-Lagrange (Part 1), passes")
    print("BOTH required positive controls exactly (Part 2: homogeneous->P34,")
    print("static+flat->P35). The linear perturbation delta_phi obeys the exact")
    print("same equation, not an approximation (Part 3) -- a genuine, checked")
    print("consequence of this action's own linearity, not assumed. The subhorizon")
    print("quasi-static solve (Part 4) is the ONLY approximation introduced,")
    print("explicitly flagged with its validity regime (k/(a*H)>>1). Its static")
    print("limit reproduces P35's own real-space solution exactly via the already-")
    print("established P19 Green's function (Part 5) -- the quasi-static machinery")
    print("connects back to already-verified ground, not a free-floating new")
    print("construction. delta_phi_k = g_hat*a^2*delta_rho_k/k^2 is the deliverable")
    print("for the next step (P47: perturbed Einstein equations -> gamma(a,k)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
