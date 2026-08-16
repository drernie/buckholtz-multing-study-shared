"""P43 -- tenth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction, now authorized to
run this and two follow-on steps (P44, P45) in sequence ("го все по
очереди"). First of three symmetry/action-theoretic checks the user asked
for after reviewing background material on the principle of least action.

Three parts, each independently scoped:

PART A -- shift symmetry (phi -> phi+eps). Honestly scoped from the
START (not after a skeptic catches it): for THIS action (single field,
purely-kinetic quadratic term), the canonical Noether current J^mu=d^mu
phi trivially satisfies d_mu J^mu = box(phi), which IS phi's own field
equation (P35). This is NOT independent verification of P35 -- it is the
SAME "two routes share the same underlying premises, Noether's theorem
guarantees agreement" pattern already caught and corrected in P34's own
skeptic review. Presented here only as an explicit symmetry-breaking
reframing (WHY the field equation has this form), not as a fresh check.

PART B -- full 4D conservation d_mu T^mu_0 = 0 for the static field.
[CORRECTED after context-blind skeptic review, 2026-08-14]: the ORIGINAL
docstring/verdict called this "genuinely new coverage" beyond P37's
static-spatial d_i T_ij=0 check. Skeptic falsified that framing and it
was independently re-derived here (see the new explicit check just below
Part B's divergence computation): for ANY static field (d_t phi=0), T_i0
= d_i(phi)*d_0(phi) = d_i(phi)*0 = 0 IDENTICALLY, and T^0_0 has no
t-dependence, so d_mu(T^mu_0)=0 is a kinematic triviality of staticity
alone -- true for ANY T_munu of this two-derivative structural form,
regardless of whether phi solves its field equation. It exercises none
of T_munu's dynamical content, unlike P37's own d_i(T_ij)=0 check on the
SPATIAL components (which does require phi's on-shell field equation).
Kept as a worked-out negative example, not deleted, since the arithmetic
itself is correct and the reasoning for why it's empty is instructive.

PART C -- dilatation (scaling) weight analysis: does demanding the
action be scale-covariant under x->lambda*x, phi->lambda^Delta*phi force
a specific scaling weight for ghat, and does that weight favor either of
FINDING_P39's two candidate readings for [ghat] over the other?
[CORRECTED after context-blind skeptic review, 2026-08-14]: the ORIGINAL
verdict presented Delta_ghat=+1/2 as "a new independent constraint,
solved not guessed." Skeptic falsified the "constraint" framing (not the
arithmetic): the +1/2 depends on two unmotivated choices -- (a) rho's
scaling weight rho_w=-3 (mass-fixed density) is an input assumption, not
derived from this action, and other physically-plausible choices give
different Delta_ghat; (b) restricting the dilatation to SPATIAL-ONLY
coordinates on a static slice is a nonstandard notion of scale symmetry
for an action meant to be part of a Lorentz-covariant completion -- the
natural FULL 4D dilatation x^mu->lambda*x^mu gives a DIFFERENT phi
weight (Delta=-1, the standard canonical scaling dimension of a 4D
scalar field) and a different Delta_ghat. Both cross-checks now computed
explicitly below; Part C is downgraded from "new constraint" to
"SPECULATIVE, convention- and assumption-dependent, not established."

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    ghat = sp.Symbol("g_hat", positive=True)

    print("=" * 78)
    print("P43 -- Noether symmetry audit of MULTING's reconstructed action")
    print("(P34/P35's own S = S_EH + S_phi + S_matter)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART A -- shift symmetry phi -> phi+eps (honestly scoped up front)")
    print("-" * 78)
    print("P35's own Lagrangian (Sec.1, quoted): L = (1/2)phi_dot^2 -")
    print("(1/2)(grad phi)^2 - rho*(1-g_hat*phi)")
    rho = sp.Function("rho")(x, y, z)
    phi = sp.Function("phi")(t, x, y, z)
    phi_dot = sp.diff(phi, t)
    grad_phi_sq = sum(sp.diff(phi, c) ** 2 for c in (x, y, z))
    L = sp.Rational(1, 2) * phi_dot**2 - sp.Rational(1, 2) * grad_phi_sq - rho * (1 - ghat * phi)

    eps = sp.Symbol("epsilon")
    dL_deps = sp.diff(L.subs(phi, phi + eps), eps).subs(eps, 0)
    print(f"  dL/d(epsilon) at epsilon=0 (symmetry-breaking term) = {sp.simplify(dL_deps)}")
    assert sp.simplify(dL_deps) == ghat * rho, "breaking term does not match g_hat*rho"
    print("  -> Non-zero: shift symmetry is broken by exactly g_hat*rho, confirming")
    print("     (not discovering) that phi's coupling to matter is what sources it.")
    print("  Canonical current for the KINETIC part alone: J^mu = d^mu(phi).")
    print("  d_mu(J^mu) = box(phi) -- this EQUALS phi's field equation (P35), by")
    print("  construction of the canonical Noether procedure for a single scalar")
    print("  with a purely-kinetic quadratic term. NOT presented as independent")
    print("  verification of P35 -- same 'shared premises, Noether guarantees")
    print("  agreement' pattern P34's own skeptic review already caught once.")
    print("  What this DOES add: an explicit statement of WHICH symmetry is broken")
    print("  and by exactly what term -- a structural fact not stated plainly")
    print("  anywhere in P34/P35's own text.")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART B -- full 4D energy conservation (genuinely new -- P37 only")
    print("checked the STATIC spatial part)")
    print("-" * 78)
    print("Reuse P37's own T_munu = d_mu(phi)*d_nu(phi) - (1/2)*eta_munu*(d phi)^2")
    print("for the SAME static field phi(r)=g_hat*M/(4*pi*r) -- but here check the")
    print("FULL divergence d_mu(T^mu_0), not just the spatial d_i(T_ij) P37 checked:")
    ghat_sym, M = sp.symbols("g_hat M", positive=True)
    r = sp.sqrt(x**2 + y**2 + z**2)
    phi_static = ghat_sym * M / (4 * sp.pi * r)
    eta = [-1, 1, 1, 1]

    def T_component(mu, nu):
        d = [0, sp.diff(phi_static, x), sp.diff(phi_static, y), sp.diff(phi_static, z)]
        # phi_static has no time dependence: d_t(phi)=0, already reflected in d[0]=0
        grad_sq = sum(dd**2 for dd in d[1:])
        eta_munu = eta[mu] if mu == nu else 0
        return d[mu] * d[nu] - sp.Rational(1, 2) * eta_munu * grad_sq

    # d_mu(T^mu_0): raise the mu index with eta (diagonal), sum d_mu(eta^{mu mu}*T_{mu 0})
    coords4 = [t, x, y, z]
    div_T0 = 0
    for mu in range(4):
        T_mu0 = T_component(mu, 0)
        T_up_mu0 = eta[mu] * T_mu0  # raise mu index (diagonal eta, eta^{mu mu}=eta[mu])
        div_T0 += sp.diff(T_up_mu0, coords4[mu])
    div_T0 = sp.simplify(div_T0)
    print(f"  d_mu(T^mu_0) = {div_T0}  (for r>0, source-free region)")
    assert div_T0 == 0, "energy is NOT conserved for this static configuration"

    print("\n  [CORRECTED, skeptic-caught] Is this check content-free? Test directly")
    print("  whether T_i0 vanishes IDENTICALLY (a kinematic fact of staticity alone,")
    print("  independent of whether phi solves ANY field equation):")
    for i, coord_name in enumerate(("x", "y", "z"), start=1):
        T_i0 = sp.simplify(T_component(i, 0))
        print(f"    T_{coord_name}0 = {T_i0}")
        assert T_i0 == 0, f"T_{coord_name}0 should vanish identically for a static field"
    T_00_val = sp.simplify(T_component(0, 0))
    dt_T00 = sp.diff(T_00_val, t)
    print(f"    d_t(T_00) = {dt_T00}  (T_00 has no explicit t-dependence)")
    assert dt_T00 == 0
    print("  -> CONFIRMS the skeptic's point: T_i0=0 identically (needs only d_t(phi)=0,")
    print("     not phi's field equation), and T_00 is manifestly t-independent. So")
    print("     d_mu(T^mu_0)=0 holds for ANY T_munu of this structural form on ANY")
    print("     static configuration -- it is a triviality of staticity, NOT a check")
    print("     of this specific T_munu's dynamical content. Does NOT constitute new")
    print("     coverage beyond P37's own spatial d_i(T_ij)=0 check (which DOES use")
    print("     phi's on-shell field equation and is therefore non-trivial).")

    # ------------------------------------------------------------------
    print("\n" + "-" * 78)
    print("PART C -- dilatation weight analysis: does scale covariance force a")
    print("specific weight for g_hat, and does it favor either of P39's two")
    print("candidate readings?")
    print("-" * 78)
    print("Under x -> lambda*x (spatial only, static case), phi -> lambda^Delta*phi.")
    print("Kinetic term (1/2)(grad phi)^2 integrated over d^3x scales as:")
    Delta = sp.Symbol("Delta", real=True)  # NOT positive -- the physical answer is negative
    # (grad phi)^2 under x->lam*x, phi->lam^Delta*phi: each spatial derivative
    # brings a 1/lam, so (grad phi)^2 -> lam^(2*Delta-2) * (grad phi)^2 (evaluated
    # at rescaled argument); d^3x -> lam^3 d^3x
    print(
        f"  kinetic term scales as lambda^(3+2*Delta-2) = lambda^{sp.simplify(3 + 2 * Delta - 2)}"
    )
    Delta_solution = sp.solve(sp.Eq(3 + 2 * Delta - 2, 0), Delta)
    print(f"  invariance requires Delta = {Delta_solution}")
    assert len(Delta_solution) == 1
    Delta_val = Delta_solution[0]
    print(f"  -> phi's forced scaling weight: Delta = {Delta_val}")

    print("\n  Now the coupling term g_hat*rho*phi (matter density rho has its own")
    print("  scaling weight rho_w from rho~mass/length^3; under x->lam*x with a")
    print("  FIXED physical mass, rho -> lambda^-3 * rho). For int d^3x*g_hat*rho*phi")
    print("  to scale the SAME way as the kinetic term (both pieces of one action")
    print("  must scale together for the action to be scale-covariant as a whole):")
    rho_w = -3
    ghat_w = sp.Symbol("Delta_ghat")
    coupling_scaling_power = 3 + rho_w + ghat_w + Delta_val
    kinetic_scaling_power = 3 + 2 * Delta_val - 2
    ghat_solution = sp.solve(sp.Eq(coupling_scaling_power, kinetic_scaling_power), ghat_w)
    print(f"  solved: g_hat's forced scaling weight = {ghat_solution}")
    assert len(ghat_solution) == 1
    ghat_weight = ghat_solution[0]
    print("  g_hat scaling weight (length-dimension power, spatial rescaling only)")
    print(f"  = {ghat_weight}")

    print("\n  IMPORTANT CAVEAT before comparing to P39: this is a DILATATION weight")
    print("  (how a physical configuration's VALUE changes under an ACTIVE spatial")
    print("  rescaling, mass held fixed) -- NOT automatically the same kind of number")
    print("  as P39's own SI length-EXPONENT (a passive statement about units of")
    print("  measurement, independent of any dynamics). The two coincide for many")
    print("  simple engineering-dimension cases, but that coincidence is not proven")
    print("  here -- so a match or non-match below is informative as a NEW,")
    print("  independent data point, not as a direct arbiter of P39's own question:")
    print("  P39 reading 1: [g_hat] SI length exponent = -1")
    print("  P39 reading 2: [g_hat] SI length exponent = -2")
    print(f"  This analysis's own dilatation weight = {ghat_weight}")
    matches_r1 = ghat_weight == -1
    matches_r2 = ghat_weight == -2
    print(f"  Numerically coincides with reading 1?  {matches_r1}")
    print(f"  Numerically coincides with reading 2?  {matches_r2}")

    print("\n  [CORRECTED, skeptic-caught] Two cross-checks the ORIGINAL verdict")
    print("  skipped, both of which show Delta_ghat=+1/2 is not a robust constraint:")

    print("\n  (i) Sensitivity to the rho scaling-weight ASSUMPTION (rho_w=-3 was an")
    print("      unmotivated input, not derived from this action):")
    for rho_w_alt, label in (
        (0, "external prescribed source, mass NOT held fixed"),
        (-3, "mass-fixed density (this script's own choice)"),
        (-2, "point mass M~lambda^1, rho=M*delta3(r)"),
    ):
        ghat_w_alt = sp.Symbol("w")
        power_alt = 3 + rho_w_alt + ghat_w_alt + Delta_val
        sol_alt = sp.solve(sp.Eq(power_alt, kinetic_scaling_power), ghat_w_alt)
        print(f"      rho_w={rho_w_alt:>3} ({label}): Delta_ghat = {sol_alt}")
    print("      -> Delta_ghat ranges over -5/2, +1/2, -1/2 depending on a choice")
    print("         this script never derives. The headline +1/2 is one point in")
    print("         that range, not a unique result.")

    print("\n  (ii) Sensitivity to spatial-only vs FULL 4D dilatation (this action is")
    print("       meant to be part of a Lorentz-covariant completion, so the natural")
    print("       symmetry to check is x^mu -> lambda*x^mu, not spatial-only):")
    kin4d_power = 4 + 2 * Delta - 2
    Delta4d_sol = sp.solve(sp.Eq(kin4d_power, 0), Delta)
    assert len(Delta4d_sol) == 1
    Delta4d_val = Delta4d_sol[0]
    ghat4d_w = sp.Symbol("Delta_ghat_4d")
    coupling4d_power = 4 + rho_w + ghat4d_w + Delta4d_val
    ghat4d_sol = sp.solve(sp.Eq(coupling4d_power, kin4d_power.subs(Delta, Delta4d_val)), ghat4d_w)
    assert len(ghat4d_sol) == 1
    print(f"      full 4D: phi's weight Delta = {Delta4d_val} (standard canonical scaling")
    print("               dimension of a 4D scalar field -- NOT the -1/2 used above)")
    print(f"      full 4D: g_hat's weight Delta_ghat = {ghat4d_sol[0]} (vs +1/2 spatial-only)")
    print("      -> Two different, individually defensible notions of dilatation give")
    print("         two different numbers (+1/2 vs 0). Neither is privileged by")
    print("         anything in this script. The +1/2 headline is convention-")
    print("         dependent, not a derived fact about g_hat.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Part A: symmetry-breaking term identified explicitly (g_hat*rho), NOT")
    print("claimed as independent verification of P35 (same-premises pattern).")
    print("[CORRECTED] Part B: the d_mu(T^mu_0)=0 check is a KINEMATIC TRIVIALITY of")
    print("staticity alone (T_i0=0 identically, T_00 has no t-dependence) -- it holds")
    print("for ANY T_munu of this structural form and does NOT constitute new coverage")
    print("beyond P37's own (non-trivial, on-shell) spatial check.")
    print("[CORRECTED] Part C: Delta_ghat=+1/2 is NOT a robust, derived constraint --")
    print("it depends on an unmotivated rho-scaling assumption (alternatives give -5/2,")
    print("-1/2) AND on restricting to spatial-only rather than full-4D dilatation")
    print("(which gives 0, not +1/2). Downgraded to SPECULATIVE: convention- and")
    print("assumption-dependent, not comparable to P39's readings in any established way.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
