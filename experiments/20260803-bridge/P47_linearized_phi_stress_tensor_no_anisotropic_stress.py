"""P47 -- second of two steps toward the campaign's original P36 row
(PLAN_final_goal_20260814.md): "quasi-static cosmological reduction."
P46 solved the field-equation side (delta_phi_k). This step handles the
SOURCE side: linearize phi's own stress-energy tensor T_munu (P37's own
formula, extended to a covariant FRW form) around a homogeneous
background phi_bar(t) + small perturbation delta_phi(t,x), and check
whether it sources any anisotropic stress at LINEAR order -- the
quantity that gave P38/P40's static Phi!=Psi slip.

Deliberately scoped NARROWER than "derive the full perturbed Einstein
equations and solve for gamma(a,k)" (the original plan for this step),
after independent hand-checking (before writing any code) revealed the
Einstein-tensor side requires a genuinely much larger derivation (full
linearized-Einstein-tensor-ON-FRW, not the flat-Minkowski-background
version P38 already built) than anything attempted in this campaign so
far -- an appropriately-scoped single step in its own right, given this
whole area's demonstrated fragility (P36's own worst-correction history,
P46's own two rounds of correction), split off as a LATER step (not yet
started) rather than rushed.

RESULT PREVIEW (verified below, not assumed): unlike P38's STATIC,
point-source phi(r) -- where d_i(phi)*d_j(phi) ~ x_i*x_j/r^4 is genuinely
anisotropic (a real angular, l=2 structure) -- a HOMOGENEOUS background
phi_bar(t) has d_i(phi_bar)=0 identically. This means the anisotropic-
stress-generating term in T_ij (the d_i(phi)*d_j(phi) piece) is SECOND
order in delta_phi, not first -- it does not appear in LINEAR
cosmological perturbation theory at all. This is checked directly below,
not assumed by analogy to any textbook statement.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    eps = sp.Symbol("epsilon", real=True)
    coords = (x, y, z)

    print("=" * 78)
    print("P47 -- linearized T_munu of phi on FRW: does it source anisotropic")
    print("stress at linear order in delta_phi?")
    print("Second of two steps toward the campaign's real P36 (P46 solved the")
    print("field-equation side; this handles the source side)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- covariant T_munu = d_mu(phi)*d_nu(phi) - (1/2)*g_munu*(d phi)^2")
    print("on FRW (P37's own formula, extended from flat-eta to the FRW metric)")
    print("-" * 78)
    a = sp.Function("a")(t)
    phibar = sp.Function("phi_bar")(t)
    deltaphi = sp.Function("delta_phi")(t, x, y, z)
    phi = phibar + eps * deltaphi
    phi_dot = sp.diff(phi, t)
    grad_sq = sum(sp.diff(phi, c) ** 2 for c in coords)
    dphi_sq = -(phi_dot**2) + grad_sq / a**2  # g^{mu nu} d_mu(phi) d_nu(phi), g^00=-1, g^ii=1/a^2
    print("  (d phi)^2 = g^(mu nu)*d_mu(phi)*d_nu(phi) = -phi_dot^2 + (grad phi)^2/a^2")

    def T(mu, nu):
        d = [phi_dot, sp.diff(phi, x), sp.diff(phi, y), sp.diff(phi, z)]
        g_diag = [-1, a**2, a**2, a**2]
        g_munu = g_diag[mu] if mu == nu else 0
        return d[mu] * d[nu] - sp.Rational(1, 2) * g_munu * dphi_sq

    print("  T_munu(phi) = d_mu(phi)*d_nu(phi) - (1/2)*g_munu*(d phi)^2, g_00=-1,")
    print("  g_ii=a^2 (diagonal FRW, off-diagonal zero)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- positive control: background T_00 must match P34's own")
    print("rho_phi=phi_bar_dot^2/2 (canonical scalar, no potential)")
    print("-" * 78)
    T00_background = sp.simplify(T(0, 0).subs(eps, 0))
    print(f"  T_00 |_(eps=0, background) = {T00_background}")
    expected_background = sp.Rational(1, 2) * sp.diff(phibar, t) ** 2
    assert sp.simplify(T00_background - expected_background) == 0, (
        "background T_00 does not match P34's rho_phi=phi_bar_dot^2/2"
    )
    print("  -> MATCHES P34's own rho_phi=phi_bar_dot^2/2 exactly.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- linearize T_munu in epsilon (same eps-splitting method as")
    print("P44/P46, not assumed): delta_T_00, delta_T_ii (all three), delta_T_ij")
    print("(all three off-diagonal components)")
    print("-" * 78)
    dT00 = sp.simplify(sp.diff(T(0, 0), eps).subs(eps, 0))
    print(f"  delta_T_00 = {dT00}")
    phibar_dot = sp.diff(phibar, t)
    deltaphi_dot = sp.diff(deltaphi, t)
    expected_dT00 = phibar_dot * deltaphi_dot
    assert sp.simplify(dT00 - expected_dT00) == 0

    dT_diag = []
    for i in range(1, 4):
        dTii = sp.simplify(sp.diff(T(i, i), eps).subs(eps, 0))
        dT_diag.append(dTii)
        print(f"  delta_T_{i}{i} = {dTii}")

    print("\n  All three diagonal spatial components equal (isotropic)?")
    diag_equal = all(sp.simplify(dT_diag[0] - dT_diag[i]) == 0 for i in range(1, 3))
    print(f"    {diag_equal}")
    assert diag_equal, "diagonal spatial components of delta_T_ij are NOT equal"

    dT_offdiag = []
    pairs = [(1, 2), (1, 3), (2, 3)]
    labels = ["xy", "xz", "yz"]
    for (i, j), lab in zip(pairs, labels, strict=True):
        dTij = sp.simplify(sp.diff(T(i, j), eps).subs(eps, 0))
        dT_offdiag.append(dTij)
        print(f"  delta_T_{lab} (off-diagonal) = {dTij}")
        assert dTij == 0, f"off-diagonal delta_T_{lab} is not zero"

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- assemble the traceless (anisotropic-stress) part explicitly")
    print("-" * 78)
    dT_trace = sp.simplify(sum(dT_diag))
    print(f"  delta_T_ii (spatial trace) = {dT_trace}")
    tracefree_components = []
    for k in range(3):
        tf = sp.simplify(dT_diag[k] - sp.Rational(1, 3) * dT_trace)
        tracefree_components.append(tf)
        print(f"  [delta_T_ii]_tracefree, component {k} = {tf}")
        assert tf == 0, f"traceless diagonal component {k} is not zero"
    print("  All 3 traceless diagonal components AND all 3 off-diagonal")
    print("  components are IDENTICALLY ZERO at linear order.")
    print("  -> delta_T_ij = (a^2*phi_bar_dot*delta_phi_dot) * delta_ij EXACTLY --")
    print("     purely isotropic. phi's linearized stress-energy sources NO")
    print("     anisotropic stress at all, at linear cosmological perturbation")
    print("     order, for a homogeneous background phi_bar(t).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- why: structural reason, checked not assumed")
    print("-" * 78)
    print("  The anisotropic-stress-generating piece of T_ij is d_i(phi)*d_j(phi)")
    print("  (P38's static slip came from exactly this term, ~x_i*x_j/r^4, for a")
    print("  spatially-varying point-source profile). For phi=phi_bar(t)+eps*")
    print("  delta_phi(t,x): d_i(phi)=eps*d_i(delta_phi) (since d_i(phi_bar)=0,")
    print("  homogeneity) -- so d_i(phi)*d_j(phi) = eps^2*d_i(delta_phi)*")
    print("  d_j(delta_phi), SECOND order in eps. It contributes NOTHING at")
    print("  first order -- confirmed directly above, not by this structural")
    print("  argument alone.")
    di_phi = sp.diff(phi, x)
    di_phi_linear_coeff = sp.diff(di_phi, eps).subs(eps, 0)
    print(f"  d_x(phi) linear-in-eps coefficient = {sp.simplify(di_phi_linear_coeff)}")
    print("  (nonzero -- d_x(delta_phi) -- but the PRODUCT d_i(phi)*d_j(phi) is")
    print("  built from TWO such factors, hence O(eps^2), matching Part 3/4.)")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("phi's linearized stress-energy tensor, around a homogeneous FRW")
    print("background, sources ZERO anisotropic stress at linear order --")
    print("delta_T_ij = a^2*phi_bar_dot*delta_phi_dot*delta_ij exactly, verified")
    print("component-by-component (6 independent checks: 3 traceless-diagonal, 3")
    print("off-diagonal), not assumed from the static P38 result or from a")
    print("textbook citation. Structurally: the anisotropic-generating term")
    print("d_i(phi)*d_j(phi) is second-order in delta_phi for a homogeneous")
    print("background, unlike P38's static point-source case where the field")
    print("itself varies spatially at leading order. If the trace-free Einstein")
    print("equation (NOT derived in this step -- see module docstring) takes the")
    print("standard quasi-static form [k^2/a^2](Phi_k-Psi_k) ~ anisotropic-stress")
    print("source, phi's OWN contribution to that source vanishes at this order,")
    print("suggesting Phi_phi,k = Psi_phi,k (no slip) from phi at LINEAR")
    print("cosmological order -- structurally different from P38/P40's nonzero")
    print("STATIC two-body slip. This is a candidate real, useful null result in")
    print("the sense the campaign's own plan explicitly names as valid (P36 row:")
    print("'if quasi-static mu,gamma come out exactly Q=1,R=1 ... document and")
    print("stop this branch') -- NOT YET CONFIRMED as the full answer, since the")
    print("Einstein-equation side (and matter's own possible anisotropic stress)")
    print("is not derived here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
