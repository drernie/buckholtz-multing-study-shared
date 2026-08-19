"""P63 -- g_hat!=0 coupled background closure: derive all four typed
background equations (E_00, E_ii, E_phi, E_rho) and test whether they are
MUTUALLY CONSISTENT under general covariance (a background-level Bianchi
closure check), before attempting to solve for a(t)/phibar(t) or return
to the perturbation sector at all.

DIRECT RESPONSE to the user's own detailed review of FINDING_P62 and
explicit design for this file:
  "background system непосредственно из action, с жёсткой типизацией:
   rho_A, rho_phys, phibar, a. ... проверить, что background equations
   взаимно совместимы: E_00=0, E_ii=0, E_phi=0, E_rho=0. Критический тест:
   d/dt(E_00) =? combination of E_ii, E_phi, E_rho."
Four pre-registered outcomes, verbatim from the user's own message:
  C1 -- system closes and admits regular solutions.
  C2 -- closes, but requires free invariants/normalizations (dynamics
        determined, predictive calibration not yet fixed).
  C3 -- closure requires a NEW arbitrary function/prescription (genuine
        structural underdetermination).
  C4 -- equations fail consistency/Bianchi closure themselves (internal
        inconsistency in the completion).
Also required, mirroring FINDING_P62's own skeptic-demanded Part M
discipline: positive control (full closure) PLUS one-equation-broken
negative controls for E_rho, E_phi, E_ii separately, "as far as
constructively possible."

WHY THIS ORDER MATTERS (the user's own framing, also verbatim):
FINDING_P62 showed the previous bottleneck was never really Psi_k -- it
was one level BELOW that, in the background's own internal consistency.
This reorders the whole program from
    free a(t) -> perturbations -> mu
to
    S -> background EOM -> on-shell FRW -> perturbation system -> mu,gamma
This file is the "S -> background EOM -> on-shell FRW" step, g_hat!=0,
attempted for the first time in this campaign.

FACTS REUSED VERBATIM from prior findings (grounded via direct citation,
not memory -- see FINDING_P63's own finding.md for the extraction):
  FINDING_P34/P46 -- background scalar KG: phibar_ddot+3*H*phibar_dot
                     = g_hat*rhobar_A   (matches two independent Lagrangian
                     routes AND a covariant d'Alembertian cross-check)
  FINDING_P58     -- rhobar_A's own continuity is UNCONDITIONALLY
                     uncoupled: rhobar_A_dot+3*H*rhobar_A=0, regardless of
                     g_hat (proven: rhobar_A tracks conserved particle
                     number times a FIXED reference mass m_0)
  FINDING_P58     -- rho_phys := rhobar_A*(1-g_hat*phibar), exact algebraic
                     relation (matches FINDING_P33's own mass law)
  FINDING_P48     -- christoffels_exact, ricci_exact (full Gamma*Gamma
                     Ricci tensor) helpers, ALREADY verified against the
                     standard textbook FRW result (R_00=-3*addot/a,
                     R_11=a*addot+2*adot^2) -- reused verbatim below, only
                     at BACKGROUND order (no eps/Psi/Phi needed at all,
                     since this file never touches perturbations)
  FINDING_P39     -- the SI-normalization gap between g_hat and G_N is
                     STILL OPEN (no established relation) -- G_N and g_hat
                     are kept as independent free symbols throughout, per
                     this campaign's own standing convention; this file
                     does NOT attempt to close that gap

NEW in this file: G_00^bg, G_ii^bg derived from Christoffels/Ricci (not
textbook-quoted, though P48's own textbook cross-check IS reused as a
positive control); T_00/T_ii for BOTH sectors at background order,
derived (not assumed) from the same canonical/perfect-fluid stress
tensors used throughout this campaign; the four-equation closure test
itself, with three one-equation-relaxed negative controls.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
    """Reused VERBATIM from FINDING_P48's own already-verified helper."""
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
    """Reused VERBATIM from FINDING_P48's own already-verified helper
    (full Ricci tensor, Gamma*Gamma terms included)."""
    term1 = sum(sp.diff(Gamma[lam][mu][nu], coords[lam]) for lam in range(n))
    term2 = sum(sp.diff(Gamma[lam][mu][lam], coords[nu]) for lam in range(n))
    term3 = sum(Gamma[lam][lam][sig] * Gamma[sig][mu][nu] for lam in range(n) for sig in range(n))
    term4 = sum(Gamma[lam][nu][sig] * Gamma[sig][mu][lam] for lam in range(n) for sig in range(n))
    return term1 - term2 + term3 - term4


def main():
    print("=" * 78)
    print("P63 -- g_hat!=0 coupled background closure: E_00, E_ii, E_phi,")
    print("E_rho typed, and tested for mutual consistency (Bianchi closure)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    # PART A -- pure FRW background metric, Christoffels, Ricci (no
    # perturbations at all -- reuses FINDING_P48's own helpers, already
    # verified against the standard textbook FRW result)
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- pure FRW background metric, Ricci tensor via")
    print("Christoffels (FINDING_P48's own verified helpers, reused")
    print("verbatim), re-confirmed against the standard textbook result")
    print("-" * 78)
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    a = sp.Function("a")(t)
    n = 4
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    Gamma = christoffels_exact(coords, g, ginv, n)

    R00 = sp.simplify(ricci_exact(coords, Gamma, 0, 0, n))
    R11 = sp.simplify(ricci_exact(coords, Gamma, 1, 1, n))
    a_dot = sp.diff(a, t)
    a_ddot = sp.diff(a, t, 2)
    standard_R00 = -3 * a_ddot / a
    standard_R11 = a * a_ddot + 2 * a_dot**2
    assert sp.simplify(R00 - standard_R00) == 0, "R_00 does not match standard FRW textbook result"
    assert sp.simplify(R11 - standard_R11) == 0, "R_11 does not match standard FRW textbook result"
    print("  R_00 = -3*addot/a, R_11 = a*addot+2*adot^2 -- CONFIRMED against")
    print("  the standard textbook result (same check as FINDING_P48 Part 3,")
    print("  re-run here at pure background order, no eps needed).")

    Rscalar = ginv[0, 0] * R00 + 3 * ginv[1, 1] * R11
    G00 = sp.simplify(R00 - sp.Rational(1, 2) * g[0, 0] * Rscalar)
    G11 = sp.simplify(R11 - sp.Rational(1, 2) * g[1, 1] * Rscalar)
    H = a_dot / a
    G00_expected = 3 * H**2
    G11_over_a2_expected = -2 * a_ddot / a - H**2
    assert sp.simplify(G00 - G00_expected) == 0, "G_00 does not reduce to 3*H^2"
    assert sp.simplify(sp.simplify(G11 / a**2) - G11_over_a2_expected) == 0, (
        "G_11/a^2 does not reduce to -2*addot/a-H^2"
    )
    print("  G_00 = 3*H^2, G_11/a^2 = -2*addot/a-H^2 -- CONFIRMED, the")
    print("  standard closed forms (second one is the acceleration/")
    print("  Raychaudhuri-type equation, not previously derived anywhere")
    print("  in this campaign -- genuinely new to this file).")

    # ==================================================================
    # PART B -- stress-energy content, BOTH sectors, background order,
    # DERIVED (not assumed) from the same canonical constructions used
    # throughout this campaign
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- T_00, T_ii for scalar (canonical, V=0) and matter")
    print("(dust, rho_phys per FINDING_P58) sectors, background order")
    print("-" * 78)
    ghat = sp.Symbol("g_hat", real=True, positive=True)
    G_N = sp.Symbol("G_N", real=True, positive=True)
    phibar = sp.Function("phi_bar")(t)
    rhobar_A = sp.Function("rhobar_A")(t)
    phibar_dot = sp.diff(phibar, t)

    print("  Scalar sector (canonical T_munu=d_mu*phi*d_nu*phi-(1/2)*g_munu*")
    print("  (d*phi)^2, background: phibar=phibar(t) only, V=0):")
    dphibar = [phibar_dot, 0, 0, 0]
    dphibar_sq = sum(ginv[mu, mu] * dphibar[mu] ** 2 for mu in range(n))
    T_phi_00 = sp.simplify(dphibar[0] * dphibar[0] - sp.Rational(1, 2) * g[0, 0] * dphibar_sq)
    T_phi_11 = sp.simplify(dphibar[1] * dphibar[1] - sp.Rational(1, 2) * g[1, 1] * dphibar_sq)
    assert sp.simplify(T_phi_00 - phibar_dot**2 / 2) == 0, "T_phi_00 != phibar_dot^2/2"
    assert sp.simplify(T_phi_11 / a**2 - phibar_dot**2 / 2) == 0, (
        "T_phi_11/a^2 != phibar_dot^2/2 -- V=0 stiff-fluid p=rho expected"
    )
    print("  -> CONFIRMED: T_00^phi = phibar_dot^2/2, T_ii^phi/a^2 =")
    print("     phibar_dot^2/2 -- the V=0 stiff-fluid p=rho result, DERIVED")
    print("     here (not assumed), same as used in FINDING_P62's own")
    print("     background construction.")

    print("\n  Matter sector (dust, T_munu=rho_phys*u_mu*u_nu, background:")
    print("  comoving observer u^i=0 EXACTLY, not just to O(eps^2)):")
    rho_phys = rhobar_A * (1 - ghat * phibar)
    u0_lower = g[0, 0] * 1  # u^0=1 exactly for a comoving background observer
    T_m_00 = sp.simplify(rho_phys * u0_lower * u0_lower)
    T_m_11 = 0  # u^1=0 exactly at background order -- no eps needed to see this
    assert sp.simplify(T_m_00 - rho_phys) == 0, "T_m_00 != rho_phys"
    print(f"  -> CONFIRMED: T_00^matter = rho_phys = {rho_phys}, T_ii^matter = 0")
    print("     EXACTLY (comoving dust has no pressure at background order,")
    print("     regardless of g_hat -- the field-dependent mass enters only")
    print("     through rho_phys itself, not through a new pressure term,")
    print("     confirming FINDING_P34's own p_m=0 assumption was safe to")
    print("     make, for THIS point-particle-dust construction specifically).")

    T00_total = sp.expand(T_phi_00 + T_m_00)
    T11_over_a2_total = sp.expand(T_phi_11 / a**2 + T_m_11)

    # ==================================================================
    # PART C -- the four typed background equations
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- the four typed background equations (user's own")
    print("naming): E_00, E_ii, E_phi, E_rho")
    print("-" * 78)
    E00 = sp.expand(G00 - 8 * sp.pi * G_N * T00_total)
    Eii = sp.expand(G11 / a**2 - 8 * sp.pi * G_N * T11_over_a2_total)
    Ephi = sp.expand(sp.diff(phibar, t, 2) + 3 * H * phibar_dot - ghat * rhobar_A)
    Erho = sp.expand(sp.diff(rhobar_A, t) + 3 * H * rhobar_A)
    print("  E_00  = G_00 - 8*pi*G_N*T_00^total")
    print(f"        = {E00}")
    print("  E_ii  = G_ii/a^2 - 8*pi*G_N*T_ii^total/a^2")
    print(f"        = {Eii}")
    print("  E_phi = phibar_ddot+3*H*phibar_dot-g_hat*rhobar_A")
    print("        (FINDING_P34/P46, reused verbatim, two independent")
    print("        Lagrangian routes + covariant d'Alembertian cross-check)")
    print("  E_rho = rhobar_A_dot+3*H*rhobar_A")
    print("        (FINDING_P58, proven UNCONDITIONAL regardless of g_hat)")
    print("\n  [SCOPE NOTE, FINDING_P39] G_N and g_hat are kept as independent")
    print("  free symbols throughout -- the SI-normalization relation between")
    print("  them is still an open gap, not assumed or closed here.")

    # ==================================================================
    # PART D -- THE critical test (user's own boxed equation): does
    # d/dt(E_00) reduce to a combination of E_ii, E_phi, E_rho? Checked
    # as a SINGLE, fully general, OFF-SHELL algebraic identity -- no
    # equation is assumed to vanish. This simultaneously gives the full
    # positive control (all four on-shell -> trivial 0=0) AND every
    # one-equation-relaxed negative control (each term's own coefficient
    # IS the exact answer to "how much does violating this equation
    # contribute"), in one check.
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- THE CRITICAL TEST: d/dt(E_00) as a general (off-shell)")
    print("combination of E_00, E_ii, E_rho, E_phi. Hand-derived candidate")
    print("identity (verified below, not trusted blind):")
    print("  dE_00/dt = -3*H*(E_00+E_ii) - 8*pi*G_N*(1-g_hat*phibar)*E_rho")
    print("             - 8*pi*G_N*phibar_dot*E_phi")
    print("-" * 78)

    dE00_dt_raw = sp.diff(E00, t)
    candidate_rhs = (
        -3 * H * (E00 + Eii)
        - 8 * sp.pi * G_N * (1 - ghat * phibar) * Erho
        - 8 * sp.pi * G_N * phibar_dot * Ephi
    )
    closure_residual = sp.simplify(dE00_dt_raw - candidate_rhs)
    print(f"\n  dE_00/dt - candidate_RHS = {closure_residual}")
    is_closed = closure_residual == 0
    print(f"  Identically zero (fully general, no substitutions)? {is_closed}")
    assert is_closed, (
        "the candidate closure identity does NOT hold as a general "
        "off-shell identity -- report the actual nonzero residual, do "
        "not force-fit a different coefficient without showing the work"
    )
    print("  -> CONFIRMED, off-shell, no assumptions: this is a PURE")
    print("     ALGEBRAIC IDENTITY among the four typed background")
    print("     equations, holding for ANY a(t), phibar(t), rhobar_A(t)")
    print("     whatsoever -- not just on-shell solutions.")

    print("\n  What this identity gives for free:")
    print("  [POSITIVE CONTROL] If E_00=E_ii=E_rho=E_phi=0 all hold, the RHS")
    print("  is trivially 0 -- d/dt(E_00) vanishes too: full closure. C1-or-C2")
    print("  territory (existence of solutions is a SEPARATE question from")
    print("  closure, not addressed by this identity alone).")
    print()
    print("  [NEGATIVE CONTROL, E_rho] Coefficient of E_rho in the identity is")
    print("  -8*pi*G_N*(1-g_hat*phibar) -- generically NONZERO (only vanishes")
    print("  at the single special point phibar=1/g_hat). Breaking E_rho ALONE")
    print("  (all else on-shell) makes d/dt(E_00) pick up EXACTLY this multiple")
    print("  of the violation -- E_rho is genuinely load-bearing, not vacuous.")
    print()
    print("  [NEGATIVE CONTROL, E_phi] Coefficient of E_phi is")
    print("  -8*pi*G_N*phibar_dot -- generically nonzero (only vanishes if")
    print("  phibar is exactly constant, the SAME degenerate case FINDING_P61's")
    print("  own skeptic review flagged as diagnostically weak). E_phi is")
    print("  genuinely load-bearing for any genuinely time-varying phibar.")
    print()
    print("  [NEGATIVE CONTROL, E_ii] Coefficient of E_ii is -3*H -- nonzero")
    print("  for any expanding/contracting background (H!=0). E_ii is")
    print("  genuinely load-bearing, not a redundant relation trivially")
    print("  implied without being invoked.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("The four typed background equations (E_00, E_ii, E_phi, E_rho) are")
    print("MUTUALLY CONSISTENT under general covariance: d/dt(E_00) equals an")
    print("EXACT, fully general linear combination of all three others, with")
    print("no free/undetermined coefficients and no substitution required to")
    print("see it. This is the background-level analogue of the standard GR")
    print("fact that only 2 of the 3 single-fluid FRW equations are")
    print("independent -- here extended, correctly, to the full FOUR-equation")
    print("coupled matter+scalar system, and VERIFIED rather than assumed.")
    print()
    print("This directly answers the user's own critical test and rules out")
    print("C4 (internal inconsistency) for this specific completion: the")
    print("closure genuinely holds, not just for lucky special cases.")
    print()
    print("Does NOT yet distinguish C1 from C2 from C3 -- closure (consistency")
    print("of the EQUATIONS) is a different question from whether they ADMIT")
    print("REGULAR SOLUTIONS (C1), require a free normalization/invariant to")
    print("calibrate (C2, most likely given FINDING_P39's own still-open")
    print("G_N-vs-g_hat gap), or need a genuinely new arbitrary function (C3).")
    print("Attempting an actual solution (even a special-case one, as")
    print("FINDING_P62 did for g_hat=0) is the natural next step to")
    print("distinguish these -- NOT attempted in this file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
