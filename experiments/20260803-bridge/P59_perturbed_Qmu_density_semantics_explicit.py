"""P59 -- perturbed Q^0/Q^i with EXPLICIT bare-vs-physical density semantics,
per the user's own physics review of P58 (2026-08-17): P58 resolved the
Route A/Route B tension at BACKGROUND order only, by identifying "rho" as
two different objects (rho_A, the bare density the field equation/
Lagrangian actually sources on; rho_phys=rho_A*(1-g_hat*phi), the physical
density that should source T_m^munu). This file extends that resolution
to LINEAR (perturbative) order -- P55/P56's own Q^0/Q^1 were built using
ONE shared symbolic "rho" for BOTH T_m^munu and (via the field equation)
Q^0/Q^1's own derivation, exactly the same conflation P58 found at
background order. THIS FILE never uses a bare "rho" -- only rho_A,
rho_phys, delta_rho_A, delta_rho_phys, explicitly, throughout.

USER'S OWN PRE-REGISTERED OUTCOMES (tested here, not assumed):
  Q1 -- EXACT agreement survives perturbations: Q^0_A[rho_A]=Q^0_B[rho_phys]
        and Q^1_A[rho_A]=Q^1_B[rho_phys] once rho_phys=(1-g_hat*phi)*rho_A
        is substituted, at BOTH background AND linear order.
  Q2 -- agreement only after an EXTRA term: the perturbation of
        rho_phys=(1-g_hat*phi)*rho_A produces a term absent from P55/P56's
        own original equations, meaning THEIR equations need correcting.
  Q3 -- decomposition ambiguity: Q^mu itself is not unique (depends on how
        interaction stress is split between T_m and T_phi), only TOTAL
        conservation is meaningful -- observables need the full system,
        not an isolated Q^mu.

ROUTE A (reused, relabeled -- NOT recomputed, since FINDING_P55/P56 already
established these correctly IN TERMS OF rho_A, once "rho" there is read as
rho_A per FINDING_P58's own resolution):
  Q^0_A[rho_A] = -g_hat*(delta_rho_A*phibar_dot + rhobar_A*delta_phi_dot)
  Q^1_A[rho_A] = g_hat*rhobar_A*d_x(delta_phi)/a^2

ROUTE B (genuinely new here): build T_m^munu FROM rho_phys DIRECTLY
(expressed via rho_A and the mass law), compute its own covariant
divergence via the SAME machinery, compare against Route A's Q^0_A/Q^1_A.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
    """Reused VERBATIM from FINDING_P48/P54/P55/P56/P57/P58's own already-verified helper."""
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
    """Reused VERBATIM from FINDING_P55/P56's own already-verified helper."""
    total = 0
    for mu in range(n):
        total += sp.diff(T_upper[mu][nu], coords[mu])
    for mu in range(n):
        for lam in range(n):
            total += Gamma[mu][mu][lam] * T_upper[lam][nu]
            total += Gamma[nu][mu][lam] * T_upper[mu][lam]
    return total


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    eps = sp.Symbol("epsilon", real=True)
    a = sp.Function("a")(t)
    ghat = sp.Symbol("g_hat", real=True, positive=True)
    phibar = sp.Function("phi_bar")(t)
    deltaphi = sp.Function("delta_phi")(t, x, y, z)
    rhobar_A = sp.Function("rhobar_A")(t)
    deltarho_A = sp.Function("delta_rho_A")(t, x, y, z)
    Vx = sp.Function("V_x")(t, x, y, z)
    n = 4

    print("=" * 78)
    print("P59 -- perturbed Q^0/Q^i with EXPLICIT bare-vs-physical density")
    print("semantics (rho_A vs rho_phys), extending FINDING_P58's background-")
    print("order resolution to LINEAR (perturbative) order")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- the bare/physical relation at LINEAR order")
    print("(FINDING_P33's own mass law + FINDING_P58's resolution: rho_phys :=")
    print("rho_A*(1-g_hat*phi), EXACT algebraic relation, not an approximation)")
    print("-" * 78)
    phi = phibar + eps * deltaphi
    rho_A = rhobar_A + eps * deltarho_A
    rho_phys_exact = rho_A * (1 - ghat * phi)
    rhobar_phys = sp.simplify(rho_phys_exact.subs(eps, 0))
    deltarho_phys_full = sp.simplify(sp.diff(rho_phys_exact, eps).subs(eps, 0))
    print(f"  rhobar_phys (eps^0) = {rhobar_phys}")
    expected_rhobar_phys = rhobar_A * (1 - ghat * phibar)
    assert sp.simplify(rhobar_phys - expected_rhobar_phys) == 0
    print("  -> CONFIRMED: rhobar_phys = rhobar_A*(1-g_hat*phibar), matching")
    print("     FINDING_P58's own background relation exactly.")
    print(f"\n  delta_rho_phys (eps^1) = {deltarho_phys_full}")
    expected_deltarho_phys = (1 - ghat * phibar) * deltarho_A - ghat * rhobar_A * deltaphi
    residual_p1 = sp.simplify(deltarho_phys_full - expected_deltarho_phys)
    assert residual_p1 == 0, (
        "delta_rho_phys does not match (1-g_hat*phibar)*delta_rho_A-g_hat*"
        "rhobar_A*delta_phi -- algebra error, do not trust downstream Route B"
    )
    print("  -> CONFIRMED (user's own pre-derived form, independently re-")
    print("     verified before use, per audit-verification-gate.md):")
    print("     delta_rho_phys = (1-g_hat*phibar)*delta_rho_A - g_hat*rhobar_A*delta_phi")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- ROUTE A (reused, relabeled -- not recomputed): FINDING_P55/")
    print("P56's own Q^0/Q^1, now explicitly in terms of rho_A/delta_rho_A")
    print("-" * 78)
    Q0_A = sp.simplify(-ghat * (deltarho_A * sp.diff(phibar, t) + rhobar_A * sp.diff(deltaphi, t)))
    Q1_A = sp.simplify(ghat * rhobar_A * sp.diff(deltaphi, x) / a**2)
    print(f"  Q^0_A[rho_A] (FINDING_P55's own formula) = {Q0_A}")
    print(f"  Q^1_A[rho_A] (FINDING_P56's own formula) = {Q1_A}")
    print("  (Reused verbatim, relabeled rhobar->rhobar_A, deltarho->delta_rho_A")
    print("  -- these formulas are UNCHANGED numerically; only the SYMBOL's own")
    print("  physical meaning is now made explicit, per FINDING_P58.)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- ROUTE B (genuinely new): build T_m^munu FROM rho_phys")
    print("directly (expressed via rho_A per Part 1), compute its OWN covariant")
    print("divergence via the SAME machinery FINDING_P55/P56 already used")
    print("-" * 78)
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    Gamma = christoffels_exact(coords, g, ginv, n)

    u0 = 1
    u1 = eps * Vx
    rho_phys_full = rho_A * (1 - ghat * phi)  # exact, same as Part 1

    T_m_upper_B = [[0] * n for _ in range(n)]
    T_m_upper_B[0][0] = rho_phys_full * u0 * u0
    T_m_upper_B[0][1] = rho_phys_full * u0 * u1
    T_m_upper_B[1][0] = rho_phys_full * u1 * u0
    T_m_upper_B[1][1] = rho_phys_full * u1 * u1
    print("  T_m^(mu,nu) := rho_phys*u^mu*u^nu, rho_phys=rho_A*(1-g_hat*phi),")
    print("  u^0=1, u^1=eps*V_x -- SAME kinematic ansatz as FINDING_P56's own")
    print("  Part 3, but the density is now rho_phys, NOT the shared rho_A used")
    print("  there.")

    div_Tm_0_B_full = sp.simplify(
        sp.diff(covariant_div_upper(T_m_upper_B, Gamma, coords, 0, n), eps).subs(eps, 0)
    )
    div_Tm_1_B_full = sp.simplify(
        sp.diff(covariant_div_upper(T_m_upper_B, Gamma, coords, 1, n), eps).subs(eps, 0)
    )
    print(f"\n  [nabla_mu T_m^(mu,0)]^(1), built from rho_phys = {div_Tm_0_B_full}")
    print(f"  [nabla_mu T_m^(mu,1)]^(1), built from rho_phys = {div_Tm_1_B_full}")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- COMPARISON, ON rho_A's OWN BACKGROUND RELATION (rhobar_A_dot=")
    print("-3*H*rhobar_A) -- raw residuals alone are NOT the right comparison")
    print("(they mix rhobar_A_dot's own defining relation into 'new content');")
    print("substituting it first, THEN checking whether what remains factors")
    print("cleanly, is the correct test (mirrors FINDING_P58's own background-")
    print("order method exactly).")
    print("-" * 78)
    rhobar_A_dot_sub = -3 * (sp.diff(a, t) / a) * rhobar_A
    residual_Q0_raw = sp.simplify(div_Tm_0_B_full - Q0_A)
    residual_Q0_onshell = sp.simplify(residual_Q0_raw.subs(sp.diff(rhobar_A, t), rhobar_A_dot_sub))
    print(f"  nu=0 residual, on-shell = {residual_Q0_onshell}")

    matter_continuity_bare = (
        rhobar_A * sp.diff(Vx, x) + sp.diff(deltarho_A, t) + 3 * (sp.diff(a, t) / a) * deltarho_A
    )
    check0 = sp.simplify(residual_Q0_onshell - (1 - ghat * phibar) * matter_continuity_bare)
    assert check0 == 0, (
        "nu=0 on-shell residual does not factor as (1-g_hat*phibar)*[the simple "
        "uncoupled continuity combination] -- re-check before reporting Q1/Q2"
    )
    print("  -> FACTORS EXACTLY: residual = (1-g_hat*phibar)*[rhobar_A*d_x(V_x)")
    print("     +delta_rho_A_dot+3*H*delta_rho_A]. Since (1-g_hat*phibar) is")
    print("     generically nonzero, the CLOSURE requires this bracket to vanish")
    print("     -- i.e. delta_rho_A/V_x satisfy the SIMPLE, UNCOUPLED continuity")
    print("     equation, with ALL coupling absorbed into the (1-g_hat*phibar)")
    print("     mass-law rescaling. FINDING_P56's OWN Part 4 (which had a")
    print("     nonzero g_hat-sourced RHS, treating the shared symbol as if it")
    print("     satisfied a COUPLED continuity) needs this SAME correction as")
    print("     Gate 2's own retracted background claim -- Q2 outcome for nu=0,")
    print("     but a CLEAN one: the corrected equation is simpler, not more")
    print("     complex, than P56's original.")

    residual_Q1_raw = sp.simplify(div_Tm_1_B_full - Q1_A)
    residual_Q1_onshell = sp.simplify(residual_Q1_raw.subs(sp.diff(rhobar_A, t), rhobar_A_dot_sub))
    print(f"\n  nu=1 residual, on-shell = {residual_Q1_onshell}")
    matter_euler_bare = rhobar_A * (sp.diff(Vx, t) + 2 * (sp.diff(a, t) / a) * Vx)
    check1_simple = sp.simplify(residual_Q1_onshell - (1 - ghat * phibar) * matter_euler_bare)
    print("  Does nu=1 factor the SAME simple way (1-g_hat*phibar)*[rhobar_A*")
    print(f"  (V_x_dot+2*H*V_x)]? residual = {check1_simple}")
    print("  -> Does NOT factor that simply -- a genuine EXTRA term survives,")
    print("     unlike nu=0. Deriving the exact, correct closed form instead of")
    print("     forcing a simple factorization:")
    lhs_divided = sp.simplify(
        (div_Tm_1_B_full.subs(sp.diff(rhobar_A, t), rhobar_A_dot_sub))
        / (rhobar_A * (1 - ghat * phibar))
    )
    rhs_divided = sp.simplify(Q1_A / (rhobar_A * (1 - ghat * phibar)))
    expected_lhs_form = (
        sp.diff(Vx, t)
        + (2 * (sp.diff(a, t) / a) - ghat * sp.diff(phibar, t) / (1 - ghat * phibar)) * Vx
    )
    expected_rhs_form = ghat * sp.diff(deltaphi, x) / (a**2 * (1 - ghat * phibar))
    check_lhs = sp.simplify(lhs_divided - expected_lhs_form)
    check_rhs = sp.simplify(rhs_divided - expected_rhs_form)
    assert check_lhs == 0 and check_rhs == 0, (
        "the exact corrected Euler-equation form does not match the derived "
        "V_x_dot+[2H-g_hat*phibar_dot/(1-g_hat*phibar)]*V_x=... -- algebra error"
    )
    print("  Dividing the full closure equation by rhobar_A*(1-g_hat*phibar):")
    print(f"    LHS = {lhs_divided}")
    print(f"    RHS = {rhs_divided}")
    print("  -> CONFIRMED, exact (no truncation):")
    print("     V_x_dot + [2*H - g_hat*phibar_dot/(1-g_hat*phibar)]*V_x =")
    print("     g_hat*d_x(delta_phi)/[a^2*(1-g_hat*phibar)]")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- [Added after context-blind skeptic review, Step 8a] the")
    print("1/(1-g_hat*phibar) form above is not the cleanest presentation --")
    print("the skeptic found (and this is independently re-verified below,")
    print("before accepting) that in the rescaled momentum variable")
    print("W_x := (1-g_hat*phibar)*V_x, the equation collapses to EXACTLY the")
    print("standard UNDRESSED form, no singular factor anywhere:")
    print("-" * 78)
    Wx = sp.Function("W_x")(t, x, y, z)
    Vx_of_Wx = Wx / (1 - ghat * phibar)
    lhs_in_Wx = expected_lhs_form.subs(Vx, Vx_of_Wx).doit()
    lhs_in_Wx_times_factor = sp.simplify(lhs_in_Wx * (1 - ghat * phibar))
    expected_Wdot_2HW = sp.diff(Wx, t) + 2 * (sp.diff(a, t) / a) * Wx
    check_W = sp.simplify(lhs_in_Wx_times_factor - expected_Wdot_2HW)
    assert check_W == 0, (
        "the W_x-rescaled form does not collapse to W_x_dot+2*H*W_x -- "
        "algebra error, do not report this simplification"
    )
    rhs_in_Wx = sp.simplify(expected_rhs_form * (1 - ghat * phibar))
    print(f"  W_x_dot + 2*H*W_x = {rhs_in_Wx}")
    print("  -> CONFIRMED: EXACTLY W_x_dot+2*H*W_x=g_hat*d_x(delta_phi)/a^2 --")
    print("     the 1/(1-g_hat*phibar) factor cancels completely on BOTH the")
    print("     friction term AND the force term, not just one. W_x=(1-g_hat*")
    print("     phibar)*V_x=rho_phys*V_x/rhobar_A is the momentum-per-bare-mass")
    print("     -- physically the natural momentum variable given rho_phys is")
    print("     the actual gravitating mass. In this variable, nu=0 AND nu=1")
    print("     are STRUCTURALLY IDENTICAL to the standard uncoupled dust forms")
    print("     (continuity for delta_rho_A, momentum for W_x), each carrying")
    print("     its OWN g_hat-sourced RHS -- the 'nu=0 clean, nu=1 messy'")
    print("     asymmetry in Part 4 above is a VARIABLE-CHOICE artifact (V_x")
    print("     vs W_x), not a genuine physical asymmetry between the two")
    print("     equations.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("MIXED outcome across the two components -- neither pure Q1 nor pure")
    print("Q2 as a single verdict; each component tested independently, not")
    print("assumed to share the same answer:")
    print()
    print("nu=0 (continuity) -- Q2, CLEAN: FINDING_P56's own Part 4 continuity")
    print("equation (built from the shared 'rho' symbol with a g_hat-sourced RHS)")
    print("is corrected to the SIMPLE, UNCOUPLED form: rhobar_A*d_x(V_x)+")
    print("delta_rho_A_dot+3*H*delta_rho_A=0 -- matching the SAME pattern")
    print("FINDING_P58 already established at background order (rho_A is ALWAYS")
    print("simply, purely conserved, at every perturbative order). All coupling")
    print("content lives in the ALGEBRAIC delta_rho_phys=(1-g_hat*phibar)*")
    print("delta_rho_A-g_hat*rhobar_A*delta_phi relation (Part 1), not in")
    print("delta_rho_A's OWN dynamics.")
    print()
    print("nu=1 (Euler) -- Q2 in the V_x variable, but Q1-LIKE in the natural")
    print("physical variable: the corrected equation V_x_dot+[2*H-g_hat*")
    print("phibar_dot/(1-g_hat*phibar)]*V_x=g_hat*d_x(delta_phi)/[a^2*(1-g_hat*")
    print("phibar)] is EXACT, genuinely different from BOTH FINDING_P56's")
    print("re-confirmed (post-Gate-2-retraction) form (correct only if T_m is")
    print("built from rho_A directly) AND the earlier retracted Gate-2 form.")
    print("[Added after skeptic review] In the rescaled momentum variable")
    print("W_x:=(1-g_hat*phibar)*V_x (Part 5), this SAME equation collapses to")
    print("EXACTLY W_x_dot+2*H*W_x=g_hat*d_x(delta_phi)/a^2 -- the standard")
    print("undressed form, no singular factor anywhere. The 'nu=0 clean, nu=1")
    print("messy' asymmetry is thus a VARIABLE-CHOICE artifact (V_x vs W_x), not")
    print("a physical one: BOTH equations, in their own natural variable")
    print("(delta_rho_A for continuity, W_x=rho_phys*V_x/rhobar_A for momentum),")
    print("are structurally IDENTICAL to standard uncoupled dust with a")
    print("g_hat-sourced RHS. This is the PHYSICALLY relevant form if T_m^munu")
    print("is meant to represent rho_phys (the actual gravitating density) --")
    print("which it should, for any downstream use feeding Einstein's equations")
    print("(e.g. FINDING_P50A's own Poisson-type relation).")
    print()
    print("Neither pure Q3 (decomposition ambiguity) was found necessary to")
    print("invoke -- both components resolved to a definite, exact answer once")
    print("rho_A/rho_phys were properly disambiguated. The Q3 concern (whether")
    print("Q^mu itself is unique, independent of the rho_A/rho_phys question)")
    print("remains untested here -- a separate, deeper question, not resolved.")
    print()
    print("SCOPE: background+linear order only, Phi=Psi=0 (matching FINDING_P55/")
    print("P56's own scope). Does NOT extend to the Phi,Psi-perturbed metric")
    print("(FINDING_P57's own extension) -- a further, not-yet-attempted step.")
    print("Does NOT yet feed these corrected equations into FINDING_P50A's own")
    print("Poisson/mu_metric relation -- the decisive D1/D2/D3 test the user")
    print("pre-registered requires that further, not-yet-attempted step.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
