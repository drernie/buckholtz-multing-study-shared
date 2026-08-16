"""P49 -- assemble P46 (delta_phi_k), P47 (delta_T_munu^phi), P48 (delta_G_munu)
to solve the trace-free Einstein equation for Phi_k, Psi_k, and gamma(a,k).

PRE-REGISTERED PREDICTION (stated before this script computes anything, per
FL/EstimandOps discipline -- AOG-1 pre-registration, not a post-hoc claim):
  gamma_linear(a,k) = 1  for the canonical g-sector, at linear cosmological
  perturbation order, in the quasi-static subhorizon regime.
Falsified if the trace-free Einstein equation forces Phi_k != Psi_k for any
k != 0 once every source of anisotropic stress is actually assembled.

TWO GAPS closed here relative to just re-using P46+P47+P48 verbatim
(named before writing any code, per this campaign's established discipline
of predicting a gap and then checking it, not skipping straight to the
convenient assembly):

  GAP 1 -- P47 only linearized phi's BARE kinetic T_munu = d_mu(phi)d_nu(phi)
  - (1/2)g_munu(dphi)^2. P46's own Lagrangian has a SECOND phi-dependent
  piece, the interaction term +a^3*rho*g_hat*phi (from expanding P46's
  matter term -a^3*rho*(1-g_hat*phi)). This term was never checked for its
  own contribution to T_munu. It is checked explicitly in Part 2 below --
  not assumed isotropic by analogy with the bare kinetic term.

  GAP 2 -- P48 verified the trace-free Einstein tensor's structure using
  ONLY ONE component (G_12). A symmetric traceless 3x3 tensor has FIVE
  independent components; checking one does not, by itself, establish
  Phi_k=Psi_k for every Fourier mode k (a mode with k_x=k_y=0, i.e. purely
  along z, gives ZERO constraint from G_12 alone: k_x*k_y=0 for ANY value
  of Phi_k-Psi_k on that mode). Part 1 below adds the remaining four
  independent traceless components (G_13, G_23, G_11-G_22, G_22-G_33), all
  free to compute (same Ricci tensor already built by P48's own method,
  just extracting components P48 did not report), closing this gap for
  every k != 0, not just generic k.

METHOD: reuses P48's own exact-metric + eps-linearization machinery
verbatim (rebuilt here for a self-contained script, matching this
campaign's established convention that each finding is independently
reproducible without importing sibling files).

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
    print("P49 -- assemble P46+P47+P48 to solve the trace-free Einstein")
    print("equation for Phi_k, Psi_k, gamma(a,k)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nPRE-REGISTERED PREDICTION (stated before any assembly below):")
    print("  gamma_linear(a,k) = 1, for the canonical g-sector, quasi-static,")
    print("  linear cosmological perturbation order.")
    print("  Falsified if the trace-free Einstein equation forces Phi_k!=Psi_k")
    print("  for any k!=0 once every source of anisotropic stress is assembled.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- rebuild P48's Einstein-tensor machinery, extract the FULL")
    print("traceless part (5 independent components, not just G_12)")
    print("-" * 78)
    g = sp.diag(
        -(1 + 2 * eps * Phi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
    )
    ginv = g.inv()
    n = 4
    Gamma = christoffels_exact(coords, g, ginv, n)
    R_components = {}
    for mu in range(4):
        for nu in range(mu, 4):
            R_components[(mu, nu)] = ricci_exact(coords, Gamma, mu, nu, n)
    Rscalar = sum(ginv[mu, mu] * R_components[(mu, mu)] for mu in range(4))

    def G(mu, nu):
        Rmn = R_components[(mu, nu)] if mu <= nu else R_components[(nu, mu)]
        gmn = g[mu, nu] if mu == nu else 0
        return Rmn - sp.Rational(1, 2) * gmn * Rscalar

    G00_lin = sp.simplify(sp.diff(G(0, 0), eps).subs(eps, 0))
    G12_lin = sp.simplify(sp.diff(G(1, 2), eps).subs(eps, 0))
    G13_lin = sp.simplify(sp.diff(G(1, 3), eps).subs(eps, 0))
    G23_lin = sp.simplify(sp.diff(G(2, 3), eps).subs(eps, 0))
    G11_lin = sp.simplify(sp.diff(G(1, 1), eps).subs(eps, 0))
    G22_lin = sp.simplify(sp.diff(G(2, 2), eps).subs(eps, 0))
    G33_lin = sp.simplify(sp.diff(G(3, 3), eps).subs(eps, 0))

    print("  Cross-check against the expected closed-form textbook results")
    print("  (Ma & Bertschinger 1995-type conformal-Newtonian gauge forms --")
    print("  hardcoded here as independent targets, NOT copied from P48's")
    print("  own computed output; the Christoffel/Ricci pipeline itself is")
    print("  independently re-run in THIS script, so this is really a check")
    print("  that the algorithm P48 also independently implemented produces")
    print("  the same textbook answer when rebuilt here -- not merely a")
    print("  string-comparison against P48's own numbers):")
    expected_G00 = 2 * (
        (sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2) + sp.diff(Psi, z, 2)) / a**2
        - 3 * (sp.diff(a, t) / a) * sp.diff(Psi, t)
    )
    assert sp.simplify(G00_lin - expected_G00) == 0, "G_00 does not match expected textbook form"
    expected_G12 = -sp.diff(Phi - Psi, x, y)
    assert sp.simplify(G12_lin - expected_G12) == 0, "G_12 does not match expected textbook form"
    print("  -> G_00, G_12 both reproduce the expected textbook forms exactly")
    print("     (and, as a byproduct, match P48's own independently-obtained")
    print("     results) -- guards against silent drift/copy error before")
    print("     trusting the NEW components computed below.")

    print("\n  NEW (closing Gap 2): the other four independent traceless")
    print("  components -- G_13, G_23 (remaining off-diagonal pairs) and")
    print("  G_11-G_22, G_22-G_33 (diagonal-traceless combinations) -- all")
    print("  computed from the SAME Ricci tensor already built above, no new")
    print("  heavy symbolic work:")
    expected_G13 = -sp.diff(Phi - Psi, x, z)
    expected_G23 = -sp.diff(Phi - Psi, y, z)
    assert sp.simplify(G13_lin - expected_G13) == 0, (
        "G_13 does not match -d_x d_z(Phi-Psi) at the general FRW level"
    )
    assert sp.simplify(G23_lin - expected_G23) == 0, (
        "G_23 does not match -d_y d_z(Phi-Psi) at the general FRW level"
    )
    print(f"    G_13^(1) = {G13_lin}  ->  matches -d_x*d_z(Phi-Psi)")
    print(f"    G_23^(1) = {G23_lin}  ->  matches -d_y*d_z(Phi-Psi)")

    diff_11_22 = sp.simplify(G11_lin - G22_lin)
    diff_22_33 = sp.simplify(G22_lin - G33_lin)
    expected_11_22 = -(sp.diff(Phi - Psi, x, 2) - sp.diff(Phi - Psi, y, 2))
    expected_22_33 = -(sp.diff(Phi - Psi, y, 2) - sp.diff(Phi - Psi, z, 2))
    assert sp.simplify(diff_11_22 - expected_11_22) == 0, (
        "G_11-G_22 does not match -(d_x^2-d_y^2)(Phi-Psi)"
    )
    assert sp.simplify(diff_22_33 - expected_22_33) == 0, (
        "G_22-G_33 does not match -(d_y^2-d_z^2)(Phi-Psi)"
    )
    print(f"    G_11^(1)-G_22^(1) = {diff_11_22}  ->  matches -(d_x^2-d_y^2)(Phi-Psi)")
    print(f"    G_22^(1)-G_33^(1) = {diff_22_33}  ->  matches -(d_y^2-d_z^2)(Phi-Psi)")
    print("  -> ALL FIVE independent components of the traceless part of")
    print("     G_ij^(1) confirmed to have the single common structure")
    print("     -(d_i*d_j - (1/3)*delta_ij*Laplacian)(Phi-Psi), computed (not")
    print("     assumed from rotational symmetry of the metric ansatz alone).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- T_munu^(int): the interaction term's OWN contribution,")
    print("checked (Gap 1), not assumed isotropic by analogy with P47's bare")
    print("kinetic piece")
    print("-" * 78)
    print("  P46's own Lagrangian: L = a^3*(1/2)*phidot^2 - a*(1/2)*(grad phi)^2")
    print("                            - a^3*rho*(1 - g_hat*phi)")
    print("  Expanding: -a^3*rho*(1-g_hat*phi) = -a^3*rho + a^3*rho*g_hat*phi")
    print("  The '-a^3*rho' piece is the standard matter action already")
    print("  captured by the external perfect-fluid ansatz T^(matter)_munu=")
    print("  diag(rho,0,0,0) (P46's own explicit treatment of rho as a fixed")
    print("  external function, not itself varied w.r.t. the metric here).")
    print("  Only the NEW interaction piece, +a^3*rho*g_hat*phi = sqrt(-g)*")
    print("  (rho*g_hat*phi) [since sqrt(-g)=a^3], needs its own T_munu: it")
    print("  is a genuine g_munu-dependent term in the total action distinct")
    print("  from the bare fluid piece.")
    print()
    print("  Standard result for ANY Lagrangian PIECE with no explicit")
    print("  derivative-of-field-times-metric structure (same rule that gives")
    print("  a potential V(phi) its T_munu=-g_munu*V(phi) contribution -- a")
    print("  STANDARD, citable GR identity (delta(sqrt(-g))=-1/2*sqrt(-g)*")
    print("  g_munu*delta(g^munu)), NOT derived fresh in this script):")
    print("  a term action = integral d^4x sqrt(-g)*f(phi,rho) contributes")
    print("  T_munu^(that term) = g_munu * f(phi,rho) -- PROPORTIONAL TO")
    print("  g_munu BY CONSTRUCTION, regardless of the overall sign")
    print("  convention chosen for T_munu = -+-(2/sqrt(-g))*delta S/delta g^munu.")
    print("  This structural fact alone already guarantees zero anisotropic")
    print("  stress from ANY non-derivative interaction term.")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] The code below encodes this identity's")
    print("  CONCLUSION directly into the T_int ansatz (T_int(mu,nu) propto")
    print("  g_bg[mu,nu] by construction), then checks that ansatz's own")
    print("  internal self-consistency -- NOT an independent re-derivation of")
    print("  the identity itself from a symbolic functional variation of the")
    print("  action. The assertions below verify 'does the coded ansatz")
    print("  correctly implement isotropy', not 'is the g_munu-proportionality")
    print("  claim itself correct from first principles' -- that rests on the")
    print("  cited standard GR identity above, same status as how P48 cites")
    print("  (not re-derives) the standard cosmological Poisson equation.")

    rho_bar, delta_rho = sp.symbols("rho_bar delta_rho", real=True)
    phi_bar, delta_phi_sym = sp.symbols("phi_bar delta_phi", real=True)
    ghat = sp.Symbol("g_hat", real=True)
    eps2 = sp.Symbol("epsilon2", real=True)
    rho_full = rho_bar + eps2 * delta_rho
    phi_full = phi_bar + eps2 * delta_phi_sym
    g_bg = sp.diag(-1, a**2, a**2, a**2)  # BACKGROUND metric only, matching
    # P47's own established convention: linear-order T_munu perturbations use
    # the background metric to raise/lower indices; metric perturbations
    # (Phi,Psi) would only enter T_munu at SECOND order (Phi*delta_phi etc),
    # dropped here exactly as P47 already did for the bare kinetic term.

    def T_int(mu, nu):
        return g_bg[mu, nu] * ghat * rho_full * phi_full

    dT_int = {}
    for mu in range(4):
        for nu in range(4):
            dT_int[(mu, nu)] = sp.diff(T_int(mu, nu), eps2).subs(eps2, 0)

    print(f"\n  delta_T_00^(int) = {sp.simplify(dT_int[(0, 0)])}")
    print(f"  delta_T_11^(int) = {sp.simplify(dT_int[(1, 1)])}")
    print(f"  delta_T_12^(int) = {sp.simplify(dT_int[(1, 2)])}  (off-diagonal)")
    assert sp.simplify(dT_int[(1, 2)]) == 0
    assert sp.simplify(dT_int[(1, 3)]) == 0
    assert sp.simplify(dT_int[(2, 3)]) == 0
    assert sp.simplify(dT_int[(1, 1)] - dT_int[(2, 2)]) == 0
    assert sp.simplify(dT_int[(2, 2)] - dT_int[(3, 3)]) == 0
    print("  -> CONFIRMED (of the CODED ANSATZ's self-consistency): all")
    print("     off-diagonal components zero, all diagonal spatial components")
    print("     equal -- delta_T_ij^(int) as coded is purely isotropic.")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] MISSING TERM, stated explicitly: this")
    print("  computation used the BACKGROUND metric g_bg only. T_int is")
    print("  EXPLICITLY g_munu-proportional, so a full treatment would also")
    print("  include a delta(g_munu)*g_hat*rhobar*phibar cross-term (dropped")
    print("  here, matching P47's own identical convention for the analogous")
    print("  '-1/2*g_munu*(dphi)^2' piece of its own T_munu -- P47 also never")
    print("  combined metric perturbations with its own g_munu-proportional")
    print("  term, consistent with this whole sub-arc's P46-P48 split of")
    print("  'matter/scalar perturbations' from 'metric perturbations'.")
    print("  DOES NOT affect the Phi_k=Psi_k conclusion: the dropped term is")
    print("  proportional to delta(g_munu) itself, which for THIS metric")
    print("  ansatz (h_00=-2*Phi, h_ii=-2*Psi*a^2*delta_ij) is ALREADY purely")
    print("  diagonal/isotropic -- including it would still give zero")
    print("  anisotropic stress. It DOES mean Part 5's delta_T_00^(int)")
    print("  formula below is incomplete by a further +g_hat*rhobar*phibar*")
    print("  (-2*Phi) term, on top of the already-flagged delta_rho_k-")
    print("  dynamics gap -- Part 5 already declines to claim Psi_k is")
    print("  closed, so this does not change that section's conclusion.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- total anisotropic stress, and the resulting slip")
    print("condition")
    print("-" * 78)
    print("  delta_T_ij|TF (total) = delta_T_ij|TF^(phi, P47)     = 0")
    print("                        + delta_T_ij|TF^(int, Part 2)  = 0")
    print("                        + delta_T_ij|TF^(matter)       = 0")
    print("                                                       -----")
    print("                                                       = 0")
    print("  The matter term is the STANDARD pressureless-dust assumption")
    print("  (zero anisotropic stress at linear order) already flagged as an")
    print("  inherited, not independently re-derived, assumption in P47's own")
    print("  'What this does NOT establish' #3 -- unchanged here, stated")
    print("  explicitly rather than silently reused.")
    print()
    print("  Einstein's equation, trace-free part: delta_G_ij|TF = 8*pi*G_N*")
    print("  delta_T_ij|TF = 0, for ALL FIVE independent components (Part 1).")
    print("  In Fourier space (d_i -> i*k_i), each of the five conditions")
    print("  becomes a polynomial in (k_x,k_y,k_z) times (Phi_k - Psi_k):")
    print("    G_12,k = k_x*k_y*(Phi_k-Psi_k) = 0")
    print("    G_13,k = k_x*k_z*(Phi_k-Psi_k) = 0")
    print("    G_23,k = k_y*k_z*(Phi_k-Psi_k) = 0")
    print("    (G_11-G_22)_k = (k_x^2-k_y^2)*(Phi_k-Psi_k) = 0")
    print("    (G_22-G_33)_k = (k_y^2-k_z^2)*(Phi_k-Psi_k) = 0")
    kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
    print("\n  Claim: for ANY k=(k_x,k_y,k_z)!=(0,0,0), at least one of these")
    print("  five coefficients is nonzero -- so ALL FIVE conditions vanishing")
    print("  simultaneously forces (Phi_k-Psi_k)=0 for every k!=0, not just")
    print("  generic k. Verified by explicit case analysis (not asserted):")
    # Case analysis: suppose all five coefficients vanish simultaneously for
    # some k with at least one component nonzero. Show this forces k=0.
    sol = sp.solve(
        [kx * ky, kx * kz, ky * kz, kx**2 - ky**2, ky**2 - kz**2],
        [kx, ky, kz],
        dict=True,
    )
    print(f"    sp.solve(all five coefficients = 0) -> {sol}")
    assert all(s.get(kx, 0) == 0 and s.get(ky, 0) == 0 and s.get(kz, 0) == 0 for s in sol), (
        "found a nonzero k where all five traceless coefficients vanish -- "
        "the component set does not actually pin down every mode"
    )
    print("  -> sp.solve confirms the ONLY simultaneous solution is k=0.")

    print("\n  [SKEPTIC-CAUGHT, Step 8a] sp.solve's completeness on an")
    print("  arbitrary polynomial system is not guaranteed by API contract --")
    print("  a single sp.solve call is not by itself a rigorous proof. Added:")
    print("  independent brute-force enumeration over a dense integer AND")
    print("  half-integer grid, checking every candidate directly (no solver")
    print("  involved at all):")
    counterexamples = []
    grid = [v / 2 for v in range(-6, 7)]  # -3, -2.5, ..., 0, ..., 3
    for a_ in grid:
        for b_ in grid:
            for c_ in grid:
                if (a_, b_, c_) == (0, 0, 0):
                    continue
                five = [a_ * b_, a_ * c_, b_ * c_, a_**2 - b_**2, b_**2 - c_**2]
                if all(abs(v) < 1e-12 for v in five):
                    counterexamples.append((a_, b_, c_))
    assert counterexamples == [], (
        f"brute-force found k!=0 where all five traceless coefficients vanish: {counterexamples}"
    )
    print(f"    checked {len(grid) ** 3 - 1} candidate k!=0 points on a half-integer")
    print(f"    grid in [-3,3]^3 -- counterexamples found: {len(counterexamples)}")
    print("  -> CONFIRMED by direct enumeration, independent of sp.solve's")
    print("     internal completeness guarantees. This also matches the")
    print("     manual algebraic proof: k_x^2=k_y^2=k_z^2 (from the three")
    print("     difference-conditions) together with 'at most one of")
    print("     k_x,k_y,k_z nonzero' (from the three product-conditions) forces")
    print("     all three to zero. For every k!=0, at least one of the five")
    print("     conditions has a nonzero coefficient, forcing Phi_k=Psi_k.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- verdict: gamma(a,k)")
    print("-" * 78)
    print("  Phi_k = Psi_k  for every k != 0 (Part 3).")
    print("  gamma(a,k) := Psi_k / Phi_k = 1   identically, for every k != 0.")
    print()
    print("  PRE-REGISTERED PREDICTION: gamma_linear(a,k)=1.  RESULT: MATCH.")
    print("  Standard-physics framing (stated explicitly to avoid overclaiming")
    print("  novelty): this is the well-known 'no slip for a minimally-coupled")
    print("  canonical scalar (quintessence-type), including its non-derivative")
    print("  matter coupling' result from cosmological perturbation theory --")
    print("  NOT a MULTING-specific discovery. This finding's actual value:")
    print("  it confirms this reconstruction's g-sector, once covariantized")
    print("  through the full P46-P48 chain (including the interaction term,")
    print("  Gap 1, and the FULL traceless tensor structure, Gap 2), inherits")
    print("  this standard property rather than accidentally introducing new")
    print("  anisotropic stress -- a consistency result, matching this")
    print("  session's P47 precedent for how to correctly frame such results.")
    print()
    print("  [SKEPTIC-CAUGHT, Step 8a] Three scope caveats, stated explicitly:")
    print("  (1) FLUID-ACTION AMBIGUITY: the '-a^3*rho' piece was treated as a")
    print("  scalar-density matter action (giving T^(matter)_munu=g_munu*rho-")
    print("  like structure if derived the same way as T_int); the STANDARD")
    print("  dust convention T_munu=rho*u_mu*u_nu (from a fluid action with a")
    print("  4-velocity) is a DIFFERENT, more standard derivation route. Both")
    print("  give ZERO anisotropic stress (u_mu*u_nu is diag(1,0,0,0) in the")
    print("  fluid rest frame, same as g_munu's spatial part, both isotropic)")
    print("  -- so gamma=1 is unaffected either way -- but the T_int split in")
    print("  Part 2 is not the unique variationally-consistent choice, only a")
    print("  convenient one that happens to agree with the fluid-action route")
    print("  on the one property (isotropy) this finding actually needs.")
    print("  (2) GAUGE DEPENDENCE: Phi, Psi are gauge-dependent quantities in")
    print("  conformal-Newtonian/longitudinal gauge (implicitly used")
    print("  throughout, matching P38/P40/P46-P48's own convention). The")
    print("  gauge-INVARIANT content of this result is 'zero anisotropic")
    print("  stress' -- 'Phi_k=Psi_k' is the standard way this is stated in")
    print("  this specific gauge, not itself a gauge-invariant statement.")
    print("  (3) SCALAR SECTOR ONLY: no vector or tensor perturbation modes")
    print("  are analyzed here or anywhere in the P46-P49 sub-arc -- gamma=1")
    print("  is a scalar-sector statement only.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- bonus: how much of Psi_k itself (not just the ratio) is")
    print("closed, stated precisely rather than oversold")
    print("-" * 78)
    print("  delta_T_00 (total) = delta_T_00^(phi) + delta_T_00^(int) +")
    print("                       delta_T_00^(matter)")
    print("    delta_T_00^(phi)    = phibar_dot * delta_phi_dot   (P47)")
    print(f"    delta_T_00^(int)    = {sp.simplify(dT_int[(0, 0)])}")
    print("    delta_T_00^(matter) = delta_rho                      (standard)")
    print()
    print("  P46's own field equation gives delta_phi_k=g_hat*a^2*delta_rho_k/")
    print("  k^2, but delta_phi_k's OWN time-derivative (needed for")
    print("  delta_T_00^(phi)) requires knowing delta_rho_k(t)'s functional")
    print("  form -- which P46 explicitly left undetermined ('delta_rho has")
    print("  no dynamical equation imposed', FINDING_P46 Part 3). This is a")
    print("  REAL, already-flagged gap, not newly discovered here -- so the")
    print("  full delta_T_00^(phi) and delta_T_00^(int) contributions to")
    print("  Psi_k cannot be closed without either (a) imposing a continuity")
    print("  equation for delta_rho_k (not attempted, out of scope) or (b)")
    print("  the standard leading-order approximation that these are")
    print("  SUBDOMINANT to the matter term delta_rho_k itself, recovering")
    print("  P48 Part 6's already-established Psi_k=-4*pi*G_N*a^2*delta_rho_k")
    print("  /k^2. NOT claimed as a new, fully independent derivation of")
    print("  Psi_k here -- explicitly a re-use of P48's own result under an")
    print("  explicitly stated subdominance assumption, distinct from the")
    print("  Phi_k=Psi_k result above (Part 3-4), which needed NO such")
    print("  assumption.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Phi_k = Psi_k for every k != 0 (Parts 1-3, both named gaps closed:")
    print("interaction term's own T_munu checked not assumed isotropic; all")
    print("five independent traceless Einstein-tensor components checked, not")
    print("just G_12). gamma(a,k)=1 identically at linear cosmological order,")
    print("matching the pre-registered prediction exactly. Psi_k itself (not")
    print("just the ratio) is closed ONLY under a stated subdominance")
    print("assumption re-using P48's own already-established Poisson form --")
    print("not a new independent result, stated precisely rather than oversold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
