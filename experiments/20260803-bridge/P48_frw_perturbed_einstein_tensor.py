"""P48 -- the deferred machinery-extension step flagged (but not started)
in P47's own module docstring: the general perturbed Einstein tensor on
FRW, extending FINDING_P38's own flat-Minkowski linearized-gravity
calculation to a background with H!=0.

METHOD (avoids the hand-derivation risk flagged in P47's scope note):
rather than hand-sorting which Christoffel-Christoffel products survive
at linear order (P38's own "drop all Gamma*Gamma" shortcut is valid ONLY
because its flat background has Gamma^(0)=0 identically -- FALSE on
FRW, where background Christoffels are O(H)), this script builds the
EXACT (unexpanded, nonlinear-in-epsilon) perturbed metric, computes the
EXACT Christoffel/Ricci/Einstein tensor via the standard formulas
(INCLUDING all Gamma*Gamma terms, not dropped), and extracts the O(eps)
piece via the SAME eps-linearization method already used reliably in
P44/P46/P47 (d/d(eps) at eps=0). This automatically and correctly
captures the background-Christoffel-times-perturbation-Christoffel
cross terms without any hand-derivation of a background covariant
derivative operator.

Metric convention, matching P38's own h_00=-2*Phi, h_ii=-2*Psi exactly
(extended from static Phi(x,y,z),Psi(x,y,z) to general Phi(t,x,y,z),
Psi(t,x,y,z), and from flat eta_ii=1 to a(t)^2):
  ds^2 = -(1+2*eps*Phi)*dt^2 + a(t)^2*(1-2*eps*Psi)*(dx^2+dy^2+dz^2)

THREE positive controls, all required before trusting the quasi-static
reduction in Part 5:
  (a) background (eps=0) Ricci tensor matches the STANDARD, independently
      citable textbook FRW result R_00=-3*addot/a, R_11=a*addot+2*adot^2
      (not self-referential to this project's own prior work).
  (b) static+flat (a=1, all time-derivatives of a/Phi/Psi ->0) limit of
      the linearized G_00 matches P38's own ALREADY-VERIFIED
      G_00=2*Laplacian(Psi) EXACTLY.
  (c) static+flat limit of the linearized off-diagonal G_12 matches
      P38's own trace-free structure (depends only on Phi-Psi, vanishing
      identically at Phi=Psi -- the same self-consistency property P38's
      own Step 4 checked).

Scope, learning directly from this session's own accumulated lessons:
  - Every "reduces to a known case" claim below is COMPUTED via a
    substitution with explicit, checkable order (P46's own lesson: a
    check that can't discriminate is not a check -- here the static+flat
    limit is checked against a SPECIFIC, already-published functional
    form (2*Laplacian(Psi)), not merely "does it look reasonable").
  - The quasi-static reduction (Part 5) reuses the SAME enslaved-
    response closure argument P46 already established and corrected,
    not re-invented and not silently assumed.
  - This step supplies the LHS (geometry) only. Combining with P46's
    delta_phi_k and P47's delta_T_munu to actually solve for Psi_k,
    Phi_k, gamma(a,k) is explicitly DEFERRED to a further, not-yet-
    started step -- kept out of scope here, matching this campaign's
    established granularity (cf. the P46/P47 split, for the same reason).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
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


def ricci_exact(coords, Gamma, mu, nu, n=4):
    """Full Ricci tensor formula, Gamma*Gamma terms INCLUDED (not dropped --
    this is the key extension beyond P38's flat-background shortcut)."""
    term1 = sum(sp.diff(Gamma[lam][mu][nu], coords[lam]) for lam in range(n))
    term2 = sum(sp.diff(Gamma[lam][mu][lam], coords[nu]) for lam in range(n))
    term3 = sum(Gamma[lam][lam][sig] * Gamma[sig][mu][nu] for lam in range(n) for sig in range(n))
    term4 = sum(Gamma[lam][nu][sig] * Gamma[sig][mu][lam] for lam in range(n) for sig in range(n))
    return term1 - term2 + term3 - term4


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    eps = sp.Symbol("epsilon", real=True)
    a = sp.Function("a")(t)
    Phi = sp.Function("Phi")(t, x, y, z)
    Psi = sp.Function("Psi")(t, x, y, z)

    print("=" * 78)
    print("P48 -- perturbed Einstein tensor on FRW (LHS machinery only)")
    print("Deferred extension of P38's own flat-Minkowski calculation, flagged")
    print("in P47's own scope note as too large to bundle with that step")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- exact perturbed FRW metric (P38's own h_00=-2*Phi,")
    print("h_ii=-2*Psi convention, extended to a(t)^2 and general t,x,y,z)")
    print("-" * 78)
    print("  ds^2 = -(1+2*eps*Phi)*dt^2 + a^2*(1-2*eps*Psi)*(dx^2+dy^2+dz^2)")
    g = sp.diag(
        -(1 + 2 * eps * Phi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
    )
    ginv = g.inv()
    n = 4
    print("  metric inverted exactly (not expanded in eps yet)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- exact Christoffels and Ricci tensor, Gamma*Gamma terms")
    print("INCLUDED (the extension P38's flat-background shortcut could skip)")
    print("-" * 78)
    Gamma = christoffels_exact(coords, g, ginv, n)
    R_components = {}
    for mu in range(4):
        for nu in range(mu, 4):
            R_components[(mu, nu)] = ricci_exact(coords, Gamma, mu, nu, n)
    Rscalar = sum(ginv[mu, mu] * R_components[(mu, mu)] for mu in range(4))
    print("  Christoffels, Ricci tensor (6 independent components), Ricci scalar")
    print("  all built from the EXACT (unexpanded) metric.")

    def G(mu, nu):
        Rmn = R_components[(mu, nu)] if mu <= nu else R_components[(nu, mu)]
        gmn = g[mu, nu] if mu == nu else 0
        return Rmn - sp.Rational(1, 2) * gmn * Rscalar

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- positive control 1: background (eps=0) Ricci vs the")
    print("STANDARD, independently citable textbook FRW result (not")
    print("self-referential to this project's own prior work)")
    print("-" * 78)
    R00_bg = sp.simplify(R_components[(0, 0)].subs(eps, 0))
    R11_bg = sp.simplify(R_components[(1, 1)].subs(eps, 0))
    a_dot = sp.diff(a, t)
    a_ddot = sp.diff(a, t, 2)
    standard_R00 = -3 * a_ddot / a
    standard_R11 = a * a_ddot + 2 * a_dot**2
    print(f"  R_00 (background) = {R00_bg}")
    print(f"  standard textbook R_00 = -3*addot/a = {standard_R00}")
    assert sp.simplify(R00_bg - standard_R00) == 0, (
        "background R_00 does not match standard FRW textbook result"
    )
    print(f"  R_11 (background) = {R11_bg}")
    print(f"  standard textbook R_11 = a*addot+2*adot^2 = {standard_R11}")
    assert sp.simplify(R11_bg - standard_R11) == 0, (
        "background R_11 does not match standard FRW textbook result"
    )
    print("  -> BOTH PASS. Metric convention and derivation confirmed correct")
    print("     against an external, independently-known result before any")
    print("     project-internal comparison is attempted.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- extract linearized G_00 and off-diagonal G_12 (general FRW,")
    print("not yet static or flat)")
    print("-" * 78)
    G00_lin = sp.simplify(sp.diff(G(0, 0), eps).subs(eps, 0))
    print(f"  G_00^(1) = {G00_lin}")
    G12_lin = sp.simplify(sp.diff(G(1, 2), eps).subs(eps, 0))
    print(f"  G_12^(1) = {G12_lin}")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- positive controls 2 and 3: static+flat limit vs P38's own")
    print("ALREADY-VERIFIED results")
    print("-" * 78)
    print("  Static+flat = a's derivatives->0, a->1, AND Phi/Psi time-derivatives")
    print("  ->0 (matching P38's own STATIC Phi(x,y,z),Psi(x,y,z) ansatz exactly --")
    print("  not just a->1, which alone would be insufficient, as an earlier")
    print("  intermediate check during this derivation itself caught):")

    def static_flat(expr):
        return sp.simplify(
            expr.subs(sp.diff(Psi, t, 2), 0)
            .subs(sp.diff(Phi, t), 0)
            .subs(sp.diff(Psi, t), 0)
            .subs(sp.diff(a, t, 2), 0)
            .subs(sp.diff(a, t), 0)
            .subs(a, 1)
        )

    G00_static = static_flat(G00_lin)
    laplacian_Psi = sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2) + sp.diff(Psi, z, 2)
    print(f"  G_00^(1) static+flat = {G00_static}")
    assert sp.simplify(G00_static - 2 * laplacian_Psi) == 0, (
        "static+flat G_00 does not match P38's own G_00=2*Laplacian(Psi)"
    )
    print("  -> MATCHES P38's own G_00=2*Laplacian(Psi) EXACTLY.")

    G12_static = static_flat(G12_lin)
    expected_G12 = -sp.diff(Phi - Psi, x, y)
    print(f"  G_12^(1) static+flat = {G12_static}")
    assert sp.simplify(G12_static - expected_G12) == 0, (
        "static+flat G_12 does not match the expected -d_x d_y(Phi-Psi) structure"
    )
    self_consistency = sp.simplify(G12_static.subs(Psi, Phi))
    assert self_consistency == 0, (
        "G_12 does not vanish at Phi=Psi -- fails P38's own self-consistency property"
    )
    print("  -> MATCHES P38's own trace-free structure -d_x*d_y(Phi-Psi), and")
    print("     vanishes identically at Phi=Psi -- the same self-consistency")
    print("     property P38's own Step 4 checked, now confirmed on FRW too.")
    print("  ALL THREE positive controls pass. The FRW extension is trustworthy.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 6 -- subhorizon quasi-static reduction (SAME enslaved-response")
    print("closure argument P46 already established and corrected, reused not")
    print("re-invented)")
    print("-" * 78)
    print("  General FRW G_00^(1) (Part 4), rewritten with H:=a_dot/a:")
    H = a_dot / a
    G00_general_form = 2 * (laplacian_Psi.subs(Psi, Psi) / a**2 - 3 * H * sp.diff(Psi, t))
    # verify this rewritten form matches the raw derivation exactly first
    assert sp.simplify(G00_general_form - G00_lin) == 0, (
        "rewritten G_00 form does not match the raw derivation"
    )
    print("    G_00^(1) = 2*[Laplacian(Psi)/a^2 - 3*H*Psi_dot]  (verified equal")
    print("    to the raw Part 4 result, not just visually similar)")
    print("  Fourier space (comoving k, laplacian -> -k^2), same convention P46")
    print("  used: G_00^(1)_k = 2*[-(k^2/a^2)*Psi_k - 3*H*Psi_dot_k]")
    print()
    print("  QUASI-STATIC APPROXIMATION, same regime and same closure argument as")
    print("  P46 (delta_phi enslaved to its source, source varies on a Hubble")
    print("  timescale, so time-derivative terms are suppressed by (k/(aH))^2")
    print("  relative to the (k/a)^2 term -- not re-derived from scratch, reused")
    print("  from P46's own corrected justification): drop the 3*H*Psi_dot_k term")
    print("  relative to (k^2/a^2)*Psi_k, valid for k/(aH)>>1:")
    print("    G_00^(1)_k  ~=  -2*(k^2/a^2)*Psi_k        (quasi-static)")
    print("  Off-diagonal, already static-limit-independent-of-a in Part 4/5 (no")
    print("  time-derivative terms appeared at all in G_12^(1) -- verify this")
    print("  explicitly, not assumed from the static+flat check alone):")
    dPsi_dt_terms_in_G12 = sp.diff(G12_lin, sp.diff(Psi, t))
    dPhi_dt_terms_in_G12 = sp.diff(G12_lin, sp.diff(Phi, t))
    print(f"    d(G_12^(1))/d(Psi_dot) = {dPsi_dt_terms_in_G12}")
    print(f"    d(G_12^(1))/d(Phi_dot) = {dPhi_dt_terms_in_G12}")
    assert dPsi_dt_terms_in_G12 == 0
    assert dPhi_dt_terms_in_G12 == 0
    print("  -> CONFIRMED: G_12^(1) has no time-derivative dependence on Phi or Psi")
    print("     at all -- the quasi-static approximation is NOT needed for the")
    print("     trace-free equation (it already has the algebraic, Poisson-type")
    print("     form): G_ij^(1)_tracefree,k = k_i*k_j-type structure ~ (Phi_k-Psi_k)")
    print("     in Fourier space (real-space -d_i*d_j(Phi-Psi) -> +k_i*k_j*(Phi_k-Psi_k)).")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Perturbed Einstein tensor on FRW derived via the EXACT metric +")
    print("eps-linearization method (Part 1-2), sidestepping the hand-derivation")
    print("risk flagged in P47's own scope note. THREE positive controls pass:")
    print("background Ricci matches an independent textbook result (Part 3);")
    print("static+flat G_00 and G_12 both match P38's own already-verified")
    print("results EXACTLY, including the Phi=Psi self-consistency property")
    print("(Part 5). Quasi-static reduction (Part 6) reuses P46's own corrected")
    print("closure argument for G_00 (drops the Psi_dot term for k/(aH)>>1);")
    print("G_12's trace-free equation needs NO quasi-static approximation at all")
    print("-- confirmed by direct differentiation, not assumed, that it has zero")
    print("time-derivative dependence structurally.")
    print("This finding supplies the LHS (geometry) only. Combining with P46's")
    print("delta_phi_k and P47's delta_T_munu to solve for Psi_k, Phi_k, and")
    print("assemble gamma(a,k) is explicitly DEFERRED to a further, not-yet-")
    print("started step -- kept out of scope here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
