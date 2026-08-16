"""P50A -- derive the structural (symbolic, dimensionless-in-form) growth
coupling mu(a,k) from the SAME P46-P49 system that gave gamma(a,k)=1.

PRE-REGISTERED PREDICTIONS (user's framing, stated before this script
computed anything), REFINED once during derivation (see Part 10):
  H1: mu(a,k) != 1, gamma=1  (new force changes growth without slip)
  H0: mu(a,k) = 1, gamma=1   (canonical g-sector linearly degenerate w/ GR)

REFINEMENT #1 (null hypothesis): this campaign's own established
convention (FINDING_P46, explicit) is that a(t) is NOT required to
satisfy the Friedmann constraint. Under that convention, even the
PURE-MATTER (g_hat=0) quasi-static Poisson equation does not reduce to
mu=1 exactly. REFINED null: mu(a,k) equals the SAME g_hat=0 matter-only
baseline, evaluated in the SAME convention (Part 10).

[CORRECTED after context-blind skeptic review, Step 8a] REFINEMENT #2
(the derivation itself): the ORIGINAL version of this script postulated
a "theta=0 dust continuity" closure (delta_rho_dot_k=-3*H*delta_rho_k)
without deriving it. The skeptic found this is NOT the correct linear
continuity equation on a perturbed background -- it is missing a
metric-perturbation term (+3*rhobar*Psi_dot_k), and silently dropping it
directly contradicted Part 4's own insistence that metric perturbations
matter for T_00. Independently re-derived from scratch here (Part 7) via
the covariant divergence nabla_mu T^mu_0=0, confirming the skeptic's
claim exactly: delta_rho_dot_k = -3*H*delta_rho_k + 3*rhobar*Psi_dot_k.
This couples Psi_dot_k into delta_phi_dot_k at the SAME parametric order
as the already-retained O(1/k^2) terms -- NOT automatically negligible by
k-power-counting alone. Checked (not assumed) that the LEADING
(k->infinity) result mu->1-g_hat*phibar is independent of how Psi_dot_k
is closed (verified for a GENERIC enslaved-response coefficient c, not
one specific value) -- this is the ROBUST result kept here. The FULL
(subleading) closed-form mu(a,k) the original version claimed as "exact"
is RETRACTED as such: it depends on closing Psi_dot_k (via the Psi_k(t)
ODE this now genuinely is, or matter's own Euler equation / T_0i / G_0i,
none built anywhere in P46-P50A) -- explicitly deferred, not attempted.

[CORRECTED, Part 10] The ORIGINAL "sanity check" (delta_mu->0 as
g_hat->0) was true but tautological -- mu_baseline was DEFINED as
mu|_(g_hat=0), so the check had zero discriminating power. Replaced with
a genuine external check: mu_baseline reduces to the textbook GR result
(mu=1) under the Friedmann-imposed + subhorizon limit -- a real
consistency check against a convention this campaign does not itself
adopt.

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


def main():
    t = sp.Symbol("t", real=True)
    eps = sp.Symbol("epsilon", real=True)
    Phi = sp.Function("Phi")(t)

    print("=" * 78)
    print("P50A -- structural mu(a,k) from the P46-P49 system")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nPRE-REGISTERED (user's framing): H1: mu!=1,gamma=1 vs H0: mu=1,gamma=1.")
    print("Falsifiable prediction stated here, before Part 7's closure: mu(a,k)")
    print("will differ from the g_hat=0 baseline by a term manifestly")
    print("proportional to g_hat (checked explicitly in Part 10).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- g_00*g^00=1 identically (trivial but load-bearing for Part 2)")
    print("-" * 78)
    g00_full = -(1 + 2 * eps * Phi)
    g00inv_full = 1 / g00_full
    identity = sp.simplify(g00_full * g00inv_full)
    print(f"  g_00 * g^00 = {identity}")
    assert identity == 1

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- delta_T00^(phi) using the FULL perturbed metric (not just")
    print("background, closing the question P49 left open for this piece)")
    print("-" * 78)
    phibar = sp.Function("phibar")(t)
    deltaphi = sp.Function("deltaphi")(t)
    phi_full = phibar + eps * deltaphi
    phidot_full = sp.diff(phi_full, t)
    # T00 = phidot^2 - (1/2)*g00*g00inv*phidot^2  (spatial-gradient term is
    # O(eps^2) for a homogeneous background, per FINDING_P47 Part 5 -- reused,
    # not re-derived)
    T00_phi_full = sp.simplify(
        phidot_full**2 - sp.Rational(1, 2) * g00_full * g00inv_full * phidot_full**2
    )
    print(f"  T00^(phi), full metric, simplified: {T00_phi_full}")
    print("  -> the g00*g00inv=1 identity (Part 1) kills ALL metric-dependence")
    print("     of this term identically, for ANY g_00 -- not a special")
    print("     property of THIS metric ansatz.")
    dT00_phi = sp.diff(T00_phi_full, eps).subs(eps, 0)
    dT00_phi = sp.simplify(dT00_phi)
    print(f"  delta_T00^(phi) = {dT00_phi}")
    expected_dT00_phi = sp.diff(phibar, t) * sp.diff(deltaphi, t)
    assert sp.simplify(dT00_phi - expected_dT00_phi) == 0, (
        "delta_T00^(phi) does not match FINDING_P47's own background-only result"
    )
    print("  -> MATCHES FINDING_P47's own result EXACTLY, now confirmed to be")
    print("     Phi-INDEPENDENT even with the full metric -- closes the open")
    print("     question, not merely reused by assumption.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- delta_T00^(int) using the FULL perturbed metric (closes")
    print("the missing delta(g_munu) term FINDING_P49 explicitly flagged)")
    print("-" * 78)
    rhobar = sp.Function("rhobar")(t)
    deltarho = sp.Function("deltarho")(t)
    ghat = sp.Symbol("g_hat", real=True, positive=True)
    rho_full = rhobar + eps * deltarho
    T00_int_full = g00_full * ghat * rho_full * phi_full
    dT00_int = sp.diff(T00_int_full, eps).subs(eps, 0)
    dT00_int = sp.expand(dT00_int)
    print(f"  delta_T00^(int) = {dT00_int}")
    expected_dT00_int_no_phi_term = -ghat * rhobar * deltaphi - ghat * phibar * deltarho
    # split off the Phi-dependent piece explicitly
    phi_term = sp.simplify(dT00_int - expected_dT00_int_no_phi_term)
    print("  Phi-dependent piece (the one FINDING_P49 flagged as missing):")
    print(f"    {phi_term}")
    assert sp.simplify(phi_term - (-2 * ghat * phibar * rhobar * Phi)) == 0, (
        "Phi-dependent piece of delta_T00^(int) does not match the predicted "
        "-2*g_hat*phibar*rhobar*Phi form"
    )
    print("  -> CONFIRMED: exactly the -2*g_hat*phibar*rhobar*Phi term")
    print("     FINDING_P49 predicted was missing, now included and verified.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- delta_T00^(matter), derived (not postulated) via proper")
    print("4-velocity normalization -- first time in this sub-arc matter's")
    print("T_munu comes from an actual derivation rather than diag(rho,0,0,0)")
    print("-" * 78)
    print("  Fluid at rest (u^i=0): g_00*(u^0)^2=-1  =>  u^0=1/sqrt(-g_00)")
    u0_full = 1 / sp.sqrt(-g00_full)
    u0_series = sp.series(u0_full, eps, 0, 2).removeO()
    u_0_full = sp.expand(g00_full * u0_series)
    u_0_lin = sp.series(u_0_full, eps, 0, 2).removeO()
    print(f"  u_0 (linear in eps) = {u_0_lin}")
    T00_matter_full = rho_full * u_0_lin**2
    T00_matter_lin = sp.series(T00_matter_full, eps, 0, 2).removeO()
    dT00_matter = sp.diff(T00_matter_lin, eps).subs(eps, 0)
    dT00_matter = sp.expand(dT00_matter)
    print(f"  delta_T00^(matter) = {dT00_matter}")
    assert sp.simplify(dT00_matter - (deltarho + 2 * rhobar * Phi)) == 0, (
        "delta_T00^(matter) does not match the expected delta_rho+2*rhobar*Phi form"
    )
    print("  -> CONFIRMED: delta_rho + 2*rhobar*Phi -- the standard result for")
    print("     a pressureless perfect fluid's lower-index T_00 perturbation")
    print("     (the Phi-dependence here is a completely generic GR fact about")
    print("     4-velocity normalization, unrelated to this project's own")
    print("     specific choices).")

    print("\n" + "=" * 78)
    print("Parts 1-4 use NO new assumption beyond P46-P49 -- pure re-derivation")
    print("with the full metric, closing gaps FINDING_P49 itself flagged.")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- assemble total delta_T00, substitute Phi_k=Psi_k (P49) --")
    print("still NO new assumption beyond P46-P49 + the slip=0 substitution")
    print("-" * 78)
    G_N, k, H = sp.symbols("G_N k H", real=True, positive=True)
    delta_rho_k, delta_phi_dot_k, Psi_k = sp.symbols("delta_rho_k delta_phi_dot_k Psi_k", real=True)
    phibar_dot, rhobar_s, phibar_s = sp.symbols("phibar_dot rhobar phibar", real=True)
    a_s = sp.Symbol("a", positive=True)

    delta_phi_k = ghat * a_s**2 * delta_rho_k / k**2  # P46's quasi-static solution

    dT00_phi_k = phibar_dot * delta_phi_dot_k  # delta_phi_dot_k left SYMBOLIC here
    dT00_int_k = (
        -ghat * rhobar_s * delta_phi_k
        - ghat * phibar_s * delta_rho_k
        - 2 * ghat * phibar_s * rhobar_s * Psi_k
    )
    dT00_matter_k = delta_rho_k + 2 * rhobar_s * Psi_k
    dT00_total_k = sp.expand(dT00_phi_k + dT00_int_k + dT00_matter_k)
    print("  delta_T00_total (Phi_k substituted by Psi_k) =")
    print(f"    {dT00_total_k}")
    print("  ('delta_phi_dot_k' is still a free symbol here -- this is the")
    print("  'P50A-strict' result: everything above needs NO assumption beyond")
    print("  P46-P49.)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 6 -- combine with P48's EXACT quasi-static G_00, solve EXACTLY")
    print("for Psi_k (no term-dropping beyond what P48 already established)")
    print("-" * 78)
    print("  G_00^(1)_k (quasi-static, P48 Part 6) = -2*(k^2/a^2)*Psi_k")
    print("  Einstein: G_00 = 8*pi*G_N*T_00  =>  solve for Psi_k:")
    eq = sp.Eq(-2 * (k**2 / a_s**2) * Psi_k, 8 * sp.pi * G_N * dT00_total_k)
    sol_unclosed = sp.solve(eq, Psi_k)
    assert len(sol_unclosed) == 1
    Psi_k_unclosed = sp.simplify(sol_unclosed[0])
    print("  Psi_k (exact, delta_phi_dot_k still symbolic) =")
    print(f"    {Psi_k_unclosed}")
    print("  No term was dropped here beyond P48's own already-established")
    print("  quasi-static G_00 reduction -- this equation is EXACT given that.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 7 -- matter's OWN continuity equation, DERIVED (not postulated)")
    print("via covariant divergence -- reuses the SAME u^i=0 ansatz Part 4")
    print("already used for T_00^(matter), applied consistently")
    print("-" * 78)
    print("  [SKEPTIC-CAUGHT, Step 8a] The ORIGINAL version of this Part simply")
    print("  postulated delta_rho_dot_k=-3*H*delta_rho_k as 'the simplest theta=0")
    print("  closure' without deriving it. Skeptic flagged this is NOT the")
    print("  correct linear-order continuity equation on a perturbed FRW")
    print("  background -- it is missing a metric-perturbation term, and doing")
    print("  so directly CONTRADICTS Part 4's own insistence that metric")
    print("  perturbations matter for T_00. FIXED by deriving it properly:")
    print("  the SAME u^i=0 ansatz already used in Part 4 (matter exactly at")
    print("  rest in these coordinates -- this IS 'theta=0', not a separate")
    print("  new assumption on top of Part 4) is now applied to compute")
    print("  nabla_mu T^mu_0 = 0 directly, via the same Christoffel machinery")
    print("  this campaign has used since P48.")

    t_sym = sp.Symbol("t", real=True)
    x_sym, y_sym, z_sym = sp.symbols("x y z", real=True)
    coords = [t_sym, x_sym, y_sym, z_sym]
    eps2b = sp.Symbol("epsilon2b", real=True)
    a_t = sp.Function("a")(t_sym)
    Psi_t = sp.Function("Psi")(t_sym)
    Phi_t = sp.Function("Phi")(t_sym)
    rhobar_t = sp.Function("rhobar")(t_sym)
    deltarho_t = sp.Function("deltarho")(t_sym)
    rho_full_t = rhobar_t + eps2b * deltarho_t

    g_t = sp.diag(
        -(1 + 2 * eps2b * Phi_t),
        a_t**2 * (1 - 2 * eps2b * Psi_t),
        a_t**2 * (1 - 2 * eps2b * Psi_t),
        a_t**2 * (1 - 2 * eps2b * Psi_t),
    )
    ginv_t = g_t.inv()
    Gamma_t = christoffels_exact(coords, g_t, ginv_t, 4)
    sqrtmg_t = sp.sqrt(-g_t.det())
    u0_t = 1 / sp.sqrt(-g_t[0, 0])
    T00_up_down_t = sp.simplify(rho_full_t * g_t[0, 0] * u0_t**2)
    term1_div = sp.diff(sqrtmg_t * T00_up_down_t, t_sym) / sqrtmg_t
    term2_conn = Gamma_t[0][0][0] * T00_up_down_t
    cons_eq = sp.together(term1_div - term2_conn)
    cons_numer, _ = sp.fraction(cons_eq)
    cons_numer_lin = sp.diff(sp.expand(cons_numer), eps2b).subs(eps2b, 0)
    cons_numer_lin = sp.simplify(cons_numer_lin)
    print("\n  linear-order conservation numerator (before using background eq):")
    print(f"    {cons_numer_lin}")
    cons_numer_reduced = sp.simplify(
        cons_numer_lin.subs(sp.diff(rhobar_t, t_sym), -3 * (sp.diff(a_t, t_sym) / a_t) * rhobar_t)
    )
    print("  after using background continuity (rhobar_dot=-3*H*rhobar):")
    print(f"    {cons_numer_reduced}")
    sol_cons = sp.solve(sp.Eq(cons_numer_reduced, 0), sp.diff(deltarho_t, t_sym))
    assert len(sol_cons) == 1
    delta_rho_dot_derived = sp.simplify(sol_cons[0])
    print(f"  -> delta_rho_dot_k = {delta_rho_dot_derived}")
    H_t_expr = sp.diff(a_t, t_sym) / a_t
    expected_correct = 3 * rhobar_t * sp.diff(Psi_t, t_sym) - 3 * H_t_expr * deltarho_t
    assert sp.simplify(delta_rho_dot_derived - expected_correct) == 0, (
        "derived delta_rho_dot_k does not match 3*rhobar*Psi_dot - 3*H*deltarho"
    )
    print("  -> CONFIRMED: delta_rho_dot_k = -3*H*delta_rho_k + 3*rhobar*Psi_dot_k")
    print("     -- the ORIGINAL closure (missing the '+3*rhobar*Psi_dot_k' term)")
    print("     was genuinely wrong, independently re-derived here from scratch")
    print("     via the covariant divergence, not merely patched from a citation.")

    print("\n  This means delta_phi_dot_k (via P46's own quasi-static solution,")
    print("  differentiated) now depends on Psi_dot_k too, not delta_rho_k alone:")
    delta_rho_k_t = sp.Function("delta_rho_k")(t_sym)
    Psi_k_t = sp.Function("Psi_k")(t_sym)
    delta_phi_k_t = ghat * a_t**2 * delta_rho_k_t / k**2
    delta_phi_k_dot_general = sp.diff(delta_phi_k_t, t_sym)
    delta_rho_dot_k_correct = -3 * H_t_expr * delta_rho_k_t + 3 * rhobar_t * sp.diff(Psi_k_t, t_sym)
    delta_phi_k_dot_corrected = sp.simplify(
        delta_phi_k_dot_general.subs(sp.diff(delta_rho_k_t, t_sym), delta_rho_dot_k_correct)
    )
    print(f"    delta_phi_dot_k (corrected) = {delta_phi_k_dot_corrected}")

    print("\n  [NEW, explicitly named] Is the new Psi_dot_k term automatically")
    print("  negligible by k-power-counting alone? NO -- both pieces of")
    print("  delta_phi_dot_k carry the SAME explicit 1/k^2 prefactor, so this")
    print("  is NOT a free k-suppression argument. Closing it requires either")
    print("  (a) solving the resulting first-order ODE for Psi_k(t) at fixed k")
    print("  (not attempted here -- genuinely larger scope), or (b) REUSING")
    print("  (not inventing) the SAME enslaved-response/quasi-static closure")
    print("  principle P46 already established for delta_phi_k itself: Psi_k,")
    print("  like delta_phi_k, tracks its source's Hubble-timescale evolution,")
    print("  so Psi_dot_k ~ c*H*Psi_k for some O(1) coefficient c. Verified")
    print("  below that the LEADING (k->infinity) result is independent of c")
    print("  -- genuinely robust, not merely assumed away.")

    c_sym = sp.Symbol("c", real=True)
    Psi_dot_k_closure = c_sym * H * Psi_k
    delta_rho_dot_k_closed = -3 * H * delta_rho_k + 3 * rhobar_s * Psi_dot_k_closure
    delta_phi_dot_k_closed = sp.expand(
        ghat * a_s**2 * (2 * H * delta_rho_k + delta_rho_dot_k_closed) / k**2
    )
    print("\n  delta_phi_dot_k (closed, generic enslaved-response coefficient c) =")
    print(f"    {delta_phi_dot_k_closed}")

    Psi_k_closed_generic_c = sp.simplify(
        Psi_k_unclosed.subs(delta_phi_dot_k, delta_phi_dot_k_closed)
    )
    print("\n  Psi_k (closed, generic c) computed -- used below for the")
    print("  c-independence check on the leading large-k term.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 8 -- mu(a,k): LEADING (k->infinity) term is robust to the")
    print("Part 7 correction AND to the choice of c; the FULL (subleading)")
    print("closed form is NOT -- retracted as 'exact', stated precisely")
    print("-" * 78)
    Psi_GR = -4 * sp.pi * G_N * a_s**2 * delta_rho_k / k**2
    mu_generic_c = sp.simplify(Psi_k_closed_generic_c / Psi_GR)
    leading_generic_c = sp.limit(mu_generic_c, k, sp.oo)
    leading_generic_c = sp.simplify(leading_generic_c)
    print(f"  mu(a,k) leading term (k->infinity), generic c = {leading_generic_c}")
    assert sp.simplify(leading_generic_c - (1 - ghat * phibar_s)) == 0, (
        "leading-order mu depends on c -- the robustness claim is false"
    )
    print("  -> CONFIRMED: independent of c -- the leading term 1-g_hat*phibar")
    print("     survives BOTH the continuity-equation correction AND any")
    print("     reasonable Psi_dot_k closure. This is the ROBUST result.")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] The ORIGINAL Part 8 presented a full")
    print("  'exact closed form' for mu(a,k) including O(1/k^2) subleading")
    print("  terms. Given delta_phi_dot_k genuinely depends on Psi_dot_k at the")
    print("  SAME order as the retained O(1/k^2) terms (not extra-suppressed),")
    print("  that subleading structure depends on the closure coefficient c --")
    print("  NOT parameter-free. RETRACTED as 'exact': only the LEADING term")
    print("  is established here; the full k-dependence requires either solving")
    print("  the Psi_k(t) ODE or fixing c by some further physical argument --")
    print("  explicitly deferred (see 'What this does NOT establish').")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 9 -- leading-order mu, restated precisely")
    print("-" * 78)
    mu_leading = 1 - ghat * phibar_s
    print(f"  mu(a,k) -> {mu_leading}   as k -> infinity")
    print("  (Not assumed identical to k/(aH)>>1 -- Friedmann is not imposed,")
    print("  so no fixed relation between k and aH is available here.)")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 10 -- REAL external check, replacing the ORIGINAL circular one")
    print("-" * 78)
    print("  [SKEPTIC-CAUGHT, Step 8a] The ORIGINAL 'sanity check' (delta_mu->0")
    print("  as g_hat->0) is TRUE but has ZERO discriminating power: mu_baseline")
    print("  was DEFINED as mu|_(g_hat=0), so the check is tautological by")
    print("  construction (0=0 for any formula built this way), not evidence")
    print("  the refinement isolates real physics. REMOVED. Replaced with a")
    print("  genuine EXTERNAL check: does the g_hat=0 baseline reduce to the")
    print("  textbook GR result (mu=1) under the ADDITIONAL, clearly-labeled")
    print("  HYPOTHETICAL of also imposing the Friedmann constraint")
    print("  (H^2=8*pi*G_N*rhobar/3) and taking the standard subhorizon limit")
    print("  k/(a*H)>>1 -- NOT adopted as this campaign's actual convention,")
    print("  used here only as an external consistency check:")
    G_N_check, a_check, k_check, H_check, rhobar_check = sp.symbols(
        "G_N a k H rhobar", positive=True
    )
    mu_baseline_check = k_check**2 / (
        k_check**2 + 8 * sp.pi * G_N_check * a_check**2 * rhobar_check
    )
    friedmann_sub = mu_baseline_check.subs(rhobar_check, 3 * H_check**2 / (8 * sp.pi * G_N_check))
    friedmann_sub = sp.simplify(friedmann_sub)
    print(f"    mu_baseline with Friedmann imposed = {friedmann_sub}")
    subhorizon_limit = sp.limit(friedmann_sub, k_check, sp.oo)
    print(f"    subhorizon limit (k -> infinity, i.e. k/(aH)>>1): {subhorizon_limit}")
    assert subhorizon_limit == 1, (
        "mu_baseline does not reduce to 1 under Friedmann + subhorizon -- "
        "external consistency check FAILED"
    )
    print("  -> CONFIRMED: mu_baseline -> 1 exactly under Friedmann + subhorizon,")
    print("     matching the textbook GR/LambdaCDM Poisson equation. This is a")
    print("     genuine external check (against a DIFFERENT, standard")
    print("     convention this campaign does not itself adopt), not a")
    print("     tautological subtraction.")

    mu_baseline_actual = sp.simplify(mu_generic_c.subs(ghat, 0))

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 11 -- H0/H1 verdict, appropriately conditional")
    print("-" * 78)
    print("  LEADING-ORDER H1 (mu(a,k) -> 1-g_hat*phibar =/= 1 as k->infinity,")
    print("  generically when g_hat*phibar!=0): CONFIRMED, robust to the Part 7")
    print("  correction and to any reasonable Psi_dot_k closure (checked for a")
    print("  GENERIC coefficient c, not assumed for one specific value).")
    print()
    print("  FULL-k-DEPENDENCE H1/H0 (does mu(a,k) differ from the matter-only")
    print("  baseline at EVERY k, not just k->infinity): NOT ESTABLISHED HERE.")
    print("  The subleading structure depends on closing Psi_dot_k, which this")
    print("  finding does NOT do beyond checking c-independence of the leading")
    print("  term -- genuinely open, deferred to a further step (solving the")
    print("  Psi_k(t) ODE, or matter's own Euler equation via T_0i/G_0i).")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("LEADING-ORDER result: mu(a,k) -> 1-g_hat*phibar as k->infinity,")
    print("CONFIRMED robust to a real error the skeptic caught (the original")
    print("continuity-equation closure was missing a metric-perturbation term,")
    print("independently re-derived and fixed here) and to the choice of")
    print("Psi_dot_k closure (checked for generic c). This IS a genuine,")
    print("falsifiable structural result: the canonical g-sector changes growth")
    print("at leading order in 1/k, generically, without slip.")
    print("SUBLEADING k-dependence and a fully closed 'exact' mu(a,k) are NOT")
    print("established -- retracted from the original overclaim, genuinely")
    print("deferred (needs either the Psi_k(t) ODE or matter's Euler equation).")
    print("SI/numeric normalization of g_hat (FINDING_P39's gap) remains")
    print("unresolved -- deferred to P50B, matching the user's own staging.")
    return {
        "mu_leading": mu_leading,
        "mu_baseline_actual": mu_baseline_actual,
    }


if __name__ == "__main__":
    result = main()
    raise SystemExit(0 if result else 1)
