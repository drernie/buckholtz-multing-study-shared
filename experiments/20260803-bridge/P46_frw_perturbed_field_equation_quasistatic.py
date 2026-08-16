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

PART 5 -- does the QUASI-STATIC Fourier solution, in the static+flat
(a=1) limit, for a point-mass source, reduce via the ALREADY-ESTABLISHED
(P19, CONFIRMED-REAL) real-space Green's function 1/(4*pi*r) of the
Laplacian to P35's own real-space solution phi(r)=g_hat*M/(4*pi*r)?
[CORRECTED after context-blind skeptic review, 2026-08-16]: the ORIGINAL
version called this the "load-bearing" consistency check. Skeptic gave a
concrete adversarial counterexample: ANY solution of the form
delta_phi_k = g_hat*a^n*delta_rho_k/k^2, for ANY power n, reduces to the
SAME thing at a=1 -- so this check cannot distinguish the correct a^2
from a wrong a^17. Confirmed independently before accepting. The a=1
check is downgraded here to a basic sanity check only (does the a->1
limit fail to blow up); Part 2c below now supplies the check that
actually pins down the a-power, via a genuinely different derivation
path.

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

    print("\n  (c) [ADDED after skeptic review] Neither (a) nor (b) above actually")
    print("      pins down the SPECIFIC powers of a(t) in the general equation --")
    print("      skeptic showed (b) evaluated at a=1 cannot distinguish a^2 from")
    print("      ANY other power that equals 1 at a=1 (e.g. a^17). A genuinely")
    print("      independent check: re-derive the SAME equation via the standard")
    print("      covariant d'Alembertian formula box(phi)=(1/sqrt(-g))*d_mu(sqrt(-g)")
    print("      *g^{mu nu}*d_nu(phi)) -- a completely different method (metric")
    print("      determinant + inverse-metric contraction, NOT Lagrangian")
    print("      variation) that pins down BOTH the a^3 (volume) and 1/a^2")
    print("      (inverse spatial metric) powers independently of Part 1:")
    sqrtg = a**3
    time_flux = sqrtg * (-1) * phi_dot
    d_time_flux = sp.diff(time_flux, t)
    space_flux_div = sum(sp.diff(sqrtg * (1 / a**2) * sp.diff(phi, c), c) for c in coords)
    box_phi = sp.simplify((d_time_flux + space_flux_div) / sqrtg)
    print("      box(phi) = (1/a^3)*[d_t(-a^3*phi_dot) + sum_i d_i(a*d_i(phi))]")
    print(f"               = {box_phi}")
    assert sp.simplify(-box_phi - target_form.subs(rho, sp.Integer(0))) == 0, (
        "independent covariant box(phi) derivation does not match Part 1 (source-free part)"
    )
    print("      -> -box(phi) matches Part 1's source-free field equation EXACTLY,")
    print("         via a genuinely different derivation path. This directly")
    print("         refutes the skeptic's adversarial counterexample: a WRONG")
    print("         power of a on either term would NOT have matched this")
    print("         independently-built formula, regardless of what it gives at")
    print("         a=1 specifically.")

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
    print("     full field equation (no extra terms from expanding around phi_bar)")
    print("     -- a consequence of the SCALAR-FIELD equation being exactly linear")
    print("     in phi and rho (no V(phi) at this stage, same fact P44/P45 used).")
    print()
    print("  [CORRECTED, skeptic-caught] The ORIGINAL text overreached from this")
    print("  narrow fact to 'no perturbative approximation in this step' as a")
    print("  general claim. Precisely: delta_phi's RESPONSE to a PRESCRIBED")
    print("  delta_rho is exact -- true, and that is all this Part actually shows.")
    print("  It does NOT mean the whole perturbation setup is exact or complete:")
    print("  rho_bar(t) here is NOT required to satisfy the continuity equation")
    print("  (rho_bar_dot+3*H*rho_bar=0 for dust); a(t) is NOT required to satisfy")
    print("  the Friedmann constraint; and delta_rho itself has NO dynamical")
    print("  equation imposed (no continuity/Euler equation for the matter")
    print("  perturbation) -- it is left as a free external function throughout.")
    print("  This finding computes a RESPONSE FUNCTION for delta_phi given an")
    print("  arbitrary delta_rho, not a closed, self-consistent cosmological")
    print("  perturbation system (that needs the coupled scalar+matter+metric")
    print("  system, not attempted here).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- Fourier transform (exact) + subhorizon quasi-static")
    print("approximation (explicitly flagged, NOT exact)")
    print("-" * 78)
    print("  Fourier space (k := comoving wavenumber, laplacian -> -k^2), EXACT:")
    print("    delta_phi_k_ddot + 3*H*delta_phi_k_dot + (k^2/a^2)*delta_phi_k")
    print("    = g_hat*delta_rho_k")
    print()
    print("  SUBHORIZON QUASI-STATIC APPROXIMATION (validity: k/(a*H) >> 1):")
    print("  [CORRECTED, skeptic-caught] the ORIGINAL justification asserted")
    print("  'delta_phi_ddot ~ H^2*delta_phi' as if it were a general fact -- it")
    print("  is not; it is an assumption ABOUT THE SOLUTION's own time-dependence,")
    print("  not derived from anything above. The actual closure argument")
    print("  (standard in scalar-tensor QSA literature, stated explicitly here):")
    print("  delta_phi is taken to be ENSLAVED to delta_rho (source-dominated),")
    print("  and delta_rho evolves on a Hubble timescale (a fact about matter")
    print("  clustering, not derived in this finding either) -- so delta_phi")
    print("  inherits d/dt ~ H, giving delta_phi_ddot ~ H^2*delta_phi. The")
    print("  resulting solution below is self-consistent with this assumption:")
    print("  any time-dependence of delta_rho_k transfers directly to")
    print("  delta_phi_k with no extra derivative operators, matching the")
    print("  enslaved-response picture. Still an APPROXIMATION with a stated")
    print("  regime (k/(a*H)>>1), not an exact result:")
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
    print("PART 5 -- basic sanity check (NOT load-bearing -- see [CORRECTED] note):")
    print("does the a=1 limit fail to blow up, and connect notationally to P35?")
    print("-" * 78)
    print("  [CORRECTED, skeptic-caught] the ORIGINAL text called this the")
    print("  'load-bearing consistency check.' Skeptic gave a concrete adversarial")
    print("  counterexample: delta_phi_k=g_hat*a^n*delta_rho_k/k^2 reduces to the")
    print("  SAME thing at a=1 for ANY power n -- this check cannot distinguish")
    print("  a^2 (correct) from a^17 (wrong). Confirmed independently before")
    print("  accepting. Downgraded to a basic sanity check; Part 2c above is what")
    print("  actually verifies the a-power, via a genuinely different derivation.")
    print("  Static+flat limit of the quasi-static Fourier solution (a=1):")
    static_limit = deltaphi_k_solution.subs(a_sym, 1)
    print(f"    delta_phi_k|_(a=1) = {static_limit}  =  g_hat*delta_rho_k/k^2")
    print("  Matches the standard Fourier-space Green's function relation for")
    print("  -laplacian(phi)=g_hat*rho, and via the ALREADY-ESTABLISHED (P19,")
    print("  CONFIRMED-REAL) real-space Green's function laplacian[1/(4*pi*r)]=")
    print("  -delta^3(x), connects notationally to P35's own static solution")
    print("  g_hat*M/(4*pi*r) -- reused, not re-proven, but NOT independent")
    print("  verification of the a-power specifically (see correction above).")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("General FRW field equation derived via Euler-Lagrange (Part 1), passes")
    print("THREE positive controls: homogeneous->P34 (Part 2a), static+flat->P35")
    print("(Part 2b), and an independently-derived covariant box(phi) operator")
    print("(Part 2c, added after skeptic review -- the only one of the three that")
    print("actually pins down the a-power on EACH term separately, refuting a")
    print("skeptic-supplied adversarial counterexample the a=1 checks could not).")
    print("[CORRECTED] delta_phi's response to a PRESCRIBED delta_rho is exact")
    print("(Part 3) -- but this is a response function, NOT a closed cosmological")
    print("perturbation system: rho_bar has no continuity equation, a(t) has no")
    print("Friedmann constraint, delta_rho has no dynamics of its own, all left")
    print("as free external functions. [CORRECTED] the subhorizon quasi-static")
    print("solve (Part 4) rests on an explicit enslaved-response closure (delta_phi")
    print("tracks delta_rho's own Hubble-timescale evolution), not an unjustified")
    print("assertion, with its validity regime (k/(a*H)>>1) stated. [CORRECTED]")
    print("Part 5's a=1 reduction is a basic sanity check only, not independent")
    print("verification of the a-power (Part 2c supplies that). delta_phi_k =")
    print("g_hat*a^2*delta_rho_k/k^2 is the deliverable for the next step")
    print("(P47: perturbed Einstein equations -> gamma(a,k)) -- itself only a")
    print("response function until the matter sector's own dynamics are added.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
