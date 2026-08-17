"""P57 -- the Phi,Psi-extension of FINDING_P46's own field equation, the gap
named as open since FINDING_P54's own closing note and repeated in P55/P56:
"the Phi,Psi-extension of FINDING_P46's own field equation is a newly-named,
real, open gap" -- needed for BOTH the B1<->B2 compatibility check (against
FINDING_P54's own Phi-inclusive G_0i) AND the FINDING_P50A re-scan the
user's own physics review (2026-08-17) flagged as the highest-value next
step after P56 ("re-derive P50A under nabla_mu T_m^munu=Q^nu").

SCOPE DECISION, stated explicitly: this file does ONLY the field-equation
extension (deliberately, per this campaign's own "one step at a time"
granularity -- P46/P47/P48 were split the same way rather than combined).
The extended Q^0 (needed for the actual P50A re-scan) and the P50A
correction itself are NOT attempted here -- named as the explicit next
step. This single result unblocks BOTH downstream tasks at once (Cheapest
Differentiating Test Protocol: one calculation, two open gaps closed).

METHOD -- SAME single perturbation parameter used throughout this whole
campaign (P48, P54, P55, P56), NOT a nonstandard two-epsilon device: since
box(phi) is LINEAR in phi, and FINDING_P46's own covariant-box cross-check
(Part 2c) already established box(phi)=-g_hat*rho as the field equation via
a GENERALLY COVARIANT operator (built from Christoffel symbols, which
transform correctly under ANY metric) -- reusing that exact operator on
FINDING_P48/P54's own Phi,Psi-perturbed metric, with phi=phibar(t)+
eps*delta_phi(t,x,y,z) and rho=rhobar(t)+eps*delta_rho(t,x,y,z) at the SAME
order eps as the metric's own eps*Phi, eps*Psi terms (P48/P54's own
convention), gives the standard single first-order cosmological-perturbation
calculation -- not an ad hoc extension.

KILL-GATES applicable to THIS file:
  - the eps^0 (background) piece MUST reduce EXACTLY to P34's own
    phibar_ddot+3*H*phibar_dot=g_hat*rhobar (trivial, since Phi=Psi=0 at
    eps^0 by construction, but checked, not assumed).
  - the eps^1 piece, with Phi and Psi set to IDENTICALLY ZERO (not eps->0,
    but the FUNCTIONS Phi,Psi set to 0), MUST reduce EXACTLY to
    FINDING_P46's own delta_phi equation (Part 3's own result) -- the
    genuine positive control this whole file exists to satisfy.
  - the NEW terms proportional to Phi and/or Psi are extracted explicitly
    and reported, not buried in an unexamined combined expression.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def christoffels_exact(coords, g, ginv, n=4):
    """Reused VERBATIM from FINDING_P48/P54/P55/P56's own already-verified helper."""
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


def covariant_box(scalar_field, ginv, Gamma, coords, n=4):
    """Reused VERBATIM from FINDING_P55/P56's own already-verified helper."""
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
    Phi = sp.Function("Phi")(t, x, y, z)
    Psi = sp.Function("Psi")(t, x, y, z)
    ghat = sp.Symbol("g_hat", real=True, positive=True)
    phibar = sp.Function("phi_bar")(t)
    deltaphi = sp.Function("delta_phi")(t, x, y, z)
    rhobar = sp.Function("rho_bar")(t)
    deltarho = sp.Function("delta_rho")(t, x, y, z)
    n = 4

    print("=" * 78)
    print("P57 -- Phi,Psi-extension of FINDING_P46's own field equation")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print("\nScope decision: field-equation extension ONLY -- the extended Q^0")
    print("(for the P50A re-scan itself) is a separate, not-yet-started next step.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 1 -- SAME exact perturbed metric as FINDING_P48/P54, reused")
    print("verbatim (not reinvented)")
    print("-" * 78)
    print("  ds^2 = -(1+2*eps*Phi)*dt^2 + a^2*(1-2*eps*Psi)*(dx^2+dy^2+dz^2)")
    g = sp.diag(
        -(1 + 2 * eps * Phi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
        a**2 * (1 - 2 * eps * Psi),
    )
    ginv = g.inv()
    Gamma = christoffels_exact(coords, g, ginv, n)
    print("  Christoffels: identical construction to FINDING_P48/P54.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 2 -- field split at the SAME order eps as the metric's own")
    print("eps*Phi, eps*Psi terms (standard single first-order cosmological")
    print("perturbation theory, not a nonstandard second bookkeeping device)")
    print("-" * 78)
    phi = phibar + eps * deltaphi
    rho = rhobar + eps * deltarho
    print("  phi = phi_bar(t) + eps*delta_phi(t,x,y,z)")
    print("  rho = rho_bar(t) + eps*delta_rho(t,x,y,z)")

    box_phi_exact = covariant_box(phi, ginv, Gamma, coords, n)
    print("\n  Field equation (general covariance, matching FINDING_P46's own")
    print("  Part 2c cross-check): box(phi) + g_hat*rho = 0, exact in eps.")
    print("  [SELF-CAUGHT, fixed before any skeptic review] the FIRST version")
    print("  of this file compared box(phi)+g_hat*rho directly against P34/P46's")
    print("  own 'forward' sign convention (phi_ddot+3*H*phi_dot-...-g_hat*rho)")
    print("  termwise and got a spurious assertion failure -- box(phi) itself")
    print("  carries an OVERALL MINUS SIGN relative to that convention (verified")
    print("  directly: covariant_box(phibar) on the unperturbed metric gives")
    print("  -(phibar_ddot+3*H*phibar_dot), matching P46's own hand-rolled")
    print("  box_phi exactly, per P55's own already-established sign check).")
    print("  FIXED by flipping sign once here, matching P34/P46's own forward")
    print("  convention directly instead of comparing up to an unstated sign:")
    field_eq_exact = sp.simplify(-(box_phi_exact + ghat * rho))

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 3 -- eps^0 (background) piece: KILL-GATE, must match P34 exactly")
    print("-" * 78)
    field_eq_0 = sp.simplify(field_eq_exact.subs(eps, 0))
    a_dot = sp.diff(a, t)
    H = a_dot / a
    p34_eq = sp.diff(phibar, t, 2) + 3 * H * sp.diff(phibar, t) - ghat * rhobar
    print(f"  eps^0 field equation = {field_eq_0}")
    check_bg = sp.simplify(field_eq_0 - p34_eq)
    assert check_bg == 0, (
        "background (eps^0) piece does not match P34's phibar_ddot+3*H*"
        "phibar_dot=g_hat*rhobar -- re-check metric/field construction"
    )
    print("  -> CONFIRMED: matches P34 exactly (trivial at Phi=Psi=0, but")
    print("     checked directly, not assumed).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 4 -- eps^1 piece: the actual deliverable, split into the")
    print("known (Phi=Psi=0) part and the NEW Phi,Psi-sourced terms")
    print("-" * 78)
    field_eq_1 = sp.simplify(sp.diff(field_eq_exact, eps).subs(eps, 0))
    print(f"  Full eps^1 field equation = {field_eq_1}")

    print("\n  [KILL-GATE, THE genuine positive control] setting Phi and Psi to")
    print("  IDENTICALLY ZERO (the functions, not eps->0 -- eps^1 is already")
    print("  taken) must reduce EXACTLY to FINDING_P46's own Part 3 result:")
    known_part = sp.simplify(field_eq_1.subs([(Phi, 0), (Psi, 0)]))
    laplacian_deltaphi = sum(sp.diff(deltaphi, c, 2) for c in coords[1:])
    p46_part3_eq = (
        sp.diff(deltaphi, t, 2)
        + 3 * H * sp.diff(deltaphi, t)
        - laplacian_deltaphi / a**2
        - ghat * deltarho
    )
    check_p46 = sp.simplify(known_part - p46_part3_eq)
    print(f"  eps^1 field eq at Phi=Psi=0 = {known_part}")
    assert check_p46 == 0, (
        "eps^1 field equation at Phi=Psi=0 does not match FINDING_P46's own "
        "Part 3 delta_phi equation exactly -- the extension is built wrong"
    )
    print("  -> CONFIRMED: matches FINDING_P46's own Part 3 equation exactly")
    print("     (genuine positive control, not merely asserted).")

    print("\n  NEW terms sourced by Phi, Psi -- the actual new physics:")
    new_terms = sp.simplify(field_eq_1 - known_part)
    print(f"  (full eps^1 eq) - (Phi=Psi=0 part) = {new_terms}")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART 5 -- sanity checks on the NEW terms (not load-bearing for the")
    print("headline, but worth stating explicitly)")
    print("-" * 78)
    only_phi = sp.simplify(new_terms.subs(Psi, 0))
    only_psi = sp.simplify(new_terms.subs(Phi, 0))
    print(f"  Setting Psi=0 (Phi-only piece)  = {only_phi}")
    print(f"  Setting Phi=0 (Psi-only piece)  = {only_psi}")
    print("  Both pieces are generically nonzero for phi_bar_dot!=0 -- i.e.")
    print("  BOTH the lapse perturbation Phi and the spatial-curvature")
    print("  perturbation Psi directly source delta_phi's own equation of")
    print("  motion once phi_bar is time-evolving, independent of any g_hat")
    print("  coupling to matter (this is standard scalar-field-in-an-FRW-")
    print("  perturbation physics, not MULTING-specific -- phi_bar_dot")
    print("  appearing is exactly the well-known gravitational-redshift/")
    print("  time-dilation source term for any rolling scalar field).")

    print("\n  Simplification, ON THE BACKGROUND EQUATION OF MOTION (P34's own")
    print("  phibar_ddot+3*H*phibar_dot=g_hat*rhobar, i.e. p34_eq:=phibar_ddot+")
    print("  3*H*phibar_dot-g_hat*rhobar=0) -- NOT an unconditional algebraic")
    print("  identity off-shell, checked explicitly as such, not overclaimed:")
    only_phi_bg_substituted = sp.simplify(
        -2 * Phi * ghat * rhobar - sp.diff(Phi, t) * sp.diff(phibar, t)
    )
    residual_check = sp.simplify(only_phi - only_phi_bg_substituted)
    p34_residual_form = sp.simplify(-2 * Phi * p34_eq)
    print("  candidate simplified form = -2*Phi*g_hat*rhobar - Phi_dot*phibar_dot")
    print(f"  residual (original - candidate) = {residual_check}")
    onshell_check = sp.simplify(residual_check - p34_residual_form)
    assert onshell_check == 0, (
        "residual is not exactly -2*Phi*p34_eq -- the on-shell simplification "
        "claim is wrong, do not report it"
    )
    print("  -> CONFIRMED: residual = -2*Phi*p34_eq exactly (p34_eq being P34's")
    print("     own background field equation) -- i.e. the simplified form")
    print("     -2*Phi*g_hat*rhobar-Phi_dot*phibar_dot is EXACT ON-SHELL (once")
    print("     the background equation of motion holds), not an unconditional")
    print("     algebraic identity off the background solution.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("The Phi,Psi-extended field equation for delta_phi is:")
    print(f"  {field_eq_1} = 0")
    print()
    print("Passes its one genuine positive control: setting Phi=Psi=0 reduces")
    print("EXACTLY to FINDING_P46's own Part 3 equation, not merely similar --")
    print("checked via direct symbolic subtraction, zero residual. The eps^0")
    print("(background) piece independently matches P34 exactly.")
    print()
    print("NEW terms proportional to Phi and/or Psi, sourced by phi_bar_dot,")
    print("are extracted explicitly above -- standard rolling-scalar-in-FRW")
    print("physics (gravitational time-dilation sourcing), present regardless")
    print("of g_hat. On P34's own background equation of motion (on-shell,")
    print("not an unconditional identity), the Phi-only piece simplifies to")
    print("-2*Phi*g_hat*rhobar-Phi_dot*phibar_dot.")
    print()
    print("SCOPE, stated explicitly per this file's own scope decision: this")
    print("gives the EXTENDED FIELD EQUATION for delta_phi only. It does NOT")
    print("yet give the extended Q^0/Q^1 source terms (FINDING_P55/P56's own")
    print("deliverable, now needing the SAME Phi,Psi-extension applied to")
    print("T_phi^munu's own divergence -- a separate, not-yet-started step),")
    print("and it does NOT yet correct FINDING_P50A's own Part 7 continuity")
    print("equation (needs the extended Q^0, not built here). Both remain")
    print("explicit open next steps -- this file unblocks them, does not")
    print("complete them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
