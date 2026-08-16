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

[CORRECTED after context-blind skeptic review, 2026-08-16]: three
framing issues found, ZERO math errors -- the skeptic independently
re-derived every assertion and confirmed all of them. (1) The ORIGINAL
"positive control" (Part 2) compared this script's T_00 against P34's
own rho_phi -- both are derivations of the SAME textbook quantity (a
canonical scalar's homogeneous energy density) from the same physical
setup, not an independent check; relabeled a self-consistency check.
(2) The ORIGINAL "6 independent checks" claim (Part 3/4) overstated
what was tested: independently re-verified (new check added below) that
the linear-order delta_T_ij result is IDENTICAL whether delta_phi
depends on space at all or is purely delta_phi(t) -- the six assertions
are one algebraic fact (phi_bar's homogeneity kills every term
involving a spatial derivative of delta_phi at linear order) in six
syntactic locations, not six facts about delta_phi's spatial structure.
(3) The ORIGINAL "candidate real null result" framing invited reading
this as a MULTING-specific discovery; the skeptic correctly identified
this as a STANDARD, textbook property of any canonical minimally-
coupled scalar on FRW (inherited from the choice of kinetic term, not
from anything MULTING-specific) -- relabeled accordingly. All three
fixes are framing/calibration, not retractions of the computed result.

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
    print("PART 2 -- self-consistency check (NOT an independent positive control --")
    print("see [CORRECTED] note): background T_00 vs P34's own rho_phi")
    print("-" * 78)
    print("  [CORRECTED, skeptic-caught] the ORIGINAL text called this a 'positive")
    print("  control.' Both this T_00 and P34's rho_phi=phi_bar_dot^2/2 are")
    print("  derivations of the SAME textbook quantity (a canonical scalar's")
    print("  homogeneous energy density) from the same physical setup -- a")
    print("  consistent sign/factor error would spoil both symmetrically, so this")
    print("  is a self-consistency check (catches gross algebra slips), not an")
    print("  independent verification against external ground truth:")
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

    print("\n  [CORRECTED, skeptic-caught] The ORIGINAL text called the above '6")
    print("  independent checks.' Skeptic showed this overstates what was tested:")
    print("  does the result actually depend on delta_phi's SPATIAL structure, or")
    print("  would a purely time-dependent delta_phi(t) (no x,y,z dependence at")
    print("  all) give the identical answer? Computed directly, not asserted:")
    deltaphi_tonly = sp.Function("delta_phi")(t)
    phi_tonly = phibar + eps * deltaphi_tonly
    phi_dot_tonly = sp.diff(phi_tonly, t)
    grad_sq_tonly = sum(sp.diff(phi_tonly, c) ** 2 for c in coords)
    dphi_sq_tonly = -(phi_dot_tonly**2) + grad_sq_tonly / a**2

    def T_tonly(mu, nu):
        d = [phi_dot_tonly, sp.diff(phi_tonly, x), sp.diff(phi_tonly, y), sp.diff(phi_tonly, z)]
        g_diag = [-1, a**2, a**2, a**2]
        g_munu = g_diag[mu] if mu == nu else 0
        return d[mu] * d[nu] - sp.Rational(1, 2) * g_munu * dphi_sq_tonly

    dT11_tonly = sp.simplify(sp.diff(T_tonly(1, 1), eps).subs(eps, 0))
    print(f"  delta_T_11 with a purely t-dependent delta_phi(t): {dT11_tonly}")
    # deltaphi (4-arg) and deltaphi_tonly (1-arg) are DIFFERENT sympy Function
    # objects despite sharing a name -- can't diff them directly. Compare each
    # against its own hand-built target of the SAME shape instead.
    target_shape = a**2 * phibar_dot * sp.diff(deltaphi_tonly, t)
    assert sp.simplify(dT11_tonly - target_shape) == 0
    assert sp.simplify(dT_diag[0] - a**2 * phibar_dot * deltaphi_dot) == 0
    print("  -> Same functional SHAPE as the general-delta_phi(t,x,y,z) result")
    print("     above (a^2*phi_bar_dot*d_t(delta_phi), verified for each case")
    print("     against its own hand-built target of that shape). Confirms:")
    print("     the six assertions above are not six facts about delta_phi's")
    print("     spatial structure -- they are ONE algebraic fact (phi_bar's")
    print("     homogeneity kills every term involving a spatial derivative of")
    print("     delta_phi at linear order) appearing in six syntactic locations.")
    print("     Downgraded from '6 independent checks' accordingly.")

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
    print("directly (not assumed from the static P38 result).")
    print("[CORRECTED] this is a STANDARD, textbook property of any canonical")
    print("minimally-coupled scalar on FRW (the quintessence literature routinely")
    print("relies on exactly this), inherited from the choice of kinetic term --")
    print("NOT a MULTING-specific discovery. This finding's actual value: it")
    print("confirms this reconstruction's phi-sector, having a canonical kinetic")
    print("term, has NOT accidentally introduced a non-canonical piece that would")
    print("break the standard behavior -- a consistency check, not a discovery.")
    print("[CORRECTED] the six per-component assertions are ONE algebraic fact")
    print("(phi_bar's homogeneity kills every spatial-derivative-of-delta_phi term")
    print("at linear order) in six syntactic locations, not six independent facts")
    print("-- confirmed above by showing the result is unchanged for a purely")
    print("t-dependent delta_phi. Structurally: the anisotropic-generating term")
    print("d_i(phi)*d_j(phi) is second-order in delta_phi for a homogeneous")
    print("background, unlike P38's static point-source case where the field")
    print("itself varies spatially at leading order. If the trace-free Einstein")
    print("equation (NOT derived in this step -- see module docstring) takes the")
    print("standard quasi-static form [k^2/a^2](Phi_k-Psi_k) ~ anisotropic-stress")
    print("source, phi's OWN contribution to that source vanishes at this order,")
    print("suggesting Phi_phi,k = Psi_phi,k (no slip) from phi at LINEAR")
    print("cosmological order -- structurally different from P38/P40's nonzero")
    print("STATIC two-body slip (a genuinely different regime, not a tension).")
    print("NOT YET CONFIRMED as the full answer: the Einstein-equation side (and")
    print("matter's own possible anisotropic stress) is not derived here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
