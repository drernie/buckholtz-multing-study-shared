"""P68 -- exponential mass law m(phi)=m0*exp(-g_hat*phi) as a SEPARATE completion.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

Motivation: FINDING_P67 established that x := g_hat*phibar grows logarithmically
without bound for any g_hat != 0, and that backreaction does NOT stop it at
O(g_hat). Under the LINEAR mass law m/m0 = 1 - x that is fatal at x=1, where
rho_phys = (1-x)*rho_A vanishes and then changes sign. The exponential law never
crosses zero, so the pathology would simply not exist.

But this file does NOT treat that as a free choice of a nicer function, because
it is not one. FINDING_P33 established the linear law is EXACT given the source's
own interaction term +g*m*phi (linear in phi); factoring -m*c + g*m*phi gives
m_eff/m = 1 - (g/c)*phi with no approximation. Adopting an exponential therefore
means ADDING phi^2, phi^3, ... worldline terms that are NOT in the source. That
is a DIFFERENT completion and is labelled as one throughout.

What this file establishes:
  A. provenance -- exactly what must be added to the action, term by term;
  B. the two laws agree to O(g_hat), so every P66/P67 result survives unchanged,
     and the first disagreement is located explicitly;
  C. the scalar EOM changes in a way that MATTERS: the source term becomes
     self-limiting, g_hat*rho_A*exp(-x) instead of g_hat*rho_A;
  D. consequence -- x no longer grows like ln t but like ln(ln t), verified
     numerically against the closed asymptotic ODE x'' + x' = k*exp(-x);
  E. no pathological surface exists at all;
  F. an HONEST Anti-Overfitting Gate scoring -- this does not pass 5/5.
"""

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

G_N = 1.0
C_MATTER = 1.0


def main() -> int:
    print("=" * 78)
    print("P68 -- exponential mass law as a SEPARATE completion")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    phi, g = sp.symbols("phi g_hat", real=True)

    # ==================================================================
    # PART A -- provenance: what exactly must be ADDED to the action?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- provenance. The linear law is NOT an assumption we may swap.")
    print("-" * 78)
    print("  FINDING_P33: source interaction is +g*m*phi per dtau, LINEAR in phi.")
    print("  S/dtau = -m*c + g*m*phi  =>  m_eff/m = 1 - (g/c)*phi   EXACTLY.")
    print("  (c=1 units below, so m_eff/m = 1 - g*phi = 1 - x.)")

    m_linear = 1 - g * phi
    m_exp = sp.exp(-g * phi)
    ser = sp.expand(sp.series(m_exp, g, 0, 5).removeO())
    print(f"\n  exponential law expanded:  m_exp/m0 = {ser} + ...")
    extra = sp.expand(ser - m_linear)
    print(f"  MINUS the linear law:      difference = {extra}")
    lowest_order = min(sum(mm) for mm in sp.Poly(extra, g).monoms())
    assert lowest_order == 2, f"first difference should be O(g^2), got {lowest_order}"
    print(f"\n  => first difference enters at O(g_hat^{lowest_order}).")
    print("  => adopting the exponential means ADDING worldline self-interaction")
    print("     terms  +(1/2)g^2*m*phi^2 - (1/6)g^3*m*phi^3 + ...  that are NOT")
    print("     present in the source. This is a DIFFERENT completion, not a")
    print("     reformulation of the same one. Labelled as such everywhere below.")

    # [SKEPTIC-CAUGHT, independently re-verified before adopting] The claim above
    # is NOT redefinition-proof on its own. A reviewer attacked it with
    # phi = (1/g)*(1 - exp(-g*chi)), which turns the LINEAR mass law into an
    # exponential one with NO added worldline terms. The attack lands on the
    # worldline term alone -- and is defeated only by the kinetic term.
    chi = sp.Symbol("chi", real=True)
    phi_of_chi = (1 - sp.exp(-g * chi)) / g
    mass_rewritten = sp.simplify(m_linear.subs(phi, phi_of_chi))
    assert sp.simplify(mass_rewritten - sp.exp(-g * chi)) == 0, "redefinition algebra wrong"
    print("\n  [SKEPTIC-CAUGHT] is this claim redefinition-proof? Attack:")
    print("    phi = (1/g)*(1 - exp(-g*chi))   =>   1 - g*phi = exp(-g*chi)")
    print(f"    LINEAR law rewritten in chi:  {mass_rewritten}   -- exponential!")
    print("    So on the WORLDLINE TERM ALONE the attack SUCCEEDS.")
    dphi_dchi = sp.simplify(sp.diff(phi_of_chi, chi))
    kinetic_new = sp.simplify(dphi_dchi**2 / 2)
    assert sp.simplify(kinetic_new - sp.Rational(1, 2)) != 0, "kinetic stayed canonical: claim DEAD"
    print(f"    BUT the kinetic term goes (1/2)(d phi)^2 -> {kinetic_new} * (d chi)^2")
    print("    -- NON-canonical. The theory with a CANONICAL kinetic term AND an")
    print("    exponential mass law is genuinely distinct from the one with a")
    print("    canonical kinetic term AND a linear mass law. The added phi^2,")
    print("    phi^3, ... terms are exactly what cannot be redefined away while")
    print("    keeping the kinetic term canonical.")
    print("    => the 'different completion' claim SURVIVES, but only under the")
    print("       CANONICAL (1/2)(d phi)^2 convention. Stating that convention is")
    print("       load-bearing, not decoration -- an earlier draft left it implicit.")

    # ==================================================================
    # PART B -- agreement to O(g_hat): do P66/P67 survive the substitution?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- do FINDING_P66/P67's results survive the substitution?")
    print("-" * 78)
    d_lin = sp.diff(m_linear, g).subs(g, 0)
    d_exp = sp.diff(m_exp, g).subs(g, 0)
    assert sp.simplify(d_lin - d_exp) == 0, "laws disagree at O(g) -- P66/P67 would NOT survive"
    print(f"  d/dg at g=0:  linear -> {d_lin},  exponential -> {d_exp}   IDENTICAL")
    print("  => the two laws are indistinguishable at first order in g_hat.")
    print("  => EVERY O(g_hat) result of FINDING_P66 and FINDING_P67 carries over")
    print("     unchanged, including delta(t)'s saturation constant c. P67's")
    print("     negative result about backreaction is NOT rescued by this swap --")
    print("     it applies verbatim here too. What changes is higher order.")

    # ==================================================================
    # PART C -- the scalar EOM, and why the change matters
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- the scalar EOM source term becomes SELF-LIMITING")
    print("-" * 78)
    print("  For a mass-varying scalar, the EOM source is -(d ln m/dphi)*rho_phys,")
    print("  with rho_phys = rho_A * m(phi)/m0.")
    rho_A = sp.Symbol("rho_A", positive=True)
    for name, m_of_phi in (("linear", m_linear), ("exponential", m_exp)):
        dlnm = sp.simplify(sp.diff(sp.log(m_of_phi), phi))
        source = sp.simplify(-dlnm * rho_A * m_of_phi)
        print(f"    {name:<12} d ln m/dphi = {dlnm}")
        print(f"    {name:<12} source      = {source}")
        if name == "linear":
            # POSITIVE CONTROL: must reproduce the g*rho_A used throughout P62-P67
            assert sp.simplify(source - g * rho_A) == 0, f"linear source != g*rho_A: {source}"
            print("      [positive control] reproduces g_hat*rho_A exactly, as used")
            print("      throughout P62-P67 -- machinery consistent with prior work.")
            # [SKEPTIC-CAUGHT gloss] the control passes via a 0/0-style
            # cancellation AT the pathological point: d ln m/dphi diverges at x=1
            # while rho_phys vanishes there, and only their PRODUCT is regular.
            print("      [caveat, skeptic-caught] this cancellation is 0/0-style at")
            print("      x=1: d ln m/dphi DIVERGES there while rho_phys VANISHES, and")
            print("      only the product is regular. Nothing downstream uses the")
            print("      factors separately, so no damage -- but any quantity that")
            print("      sees d ln m/dphi alone (e.g. a per-particle Yukawa force)")
            print("      would be singular at x=1 where the composite source is not.")
        else:
            assert sp.simplify(source - g * rho_A * sp.exp(-g * phi)) == 0, "exp source wrong"
            print("      => g_hat*rho_A*exp(-x): the source SUPPRESSES ITSELF as x grows.")
    print("\n  This is a genuinely different mechanism from the one P67 killed.")
    print("  P67 ruled out stabilisation via the EXPANSION (backreaction on a).")
    print("  This is stabilisation via the SOURCE, and it is not covered by P67.")

    # ==================================================================
    # PART D -- asymptotics: ln t becomes ln(ln t)
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- asymptotic growth law for x(t)")
    print("-" * 78)
    print("  Using a^3 -> 6*pi*t^2 (P62 background) and rho_A*a^3 = C:")
    print("    d/dt(a^3*phibar_dot) = g*C*exp(-x),  x_dot = g*(a^3*phibar_dot)/a^3")
    print("  Eliminating the momentum and setting s = ln t gives the closed form")
    print("    x'' + x' = k*exp(-x),     k := g_hat^2*C/(6*pi)     (' = d/ds)")

    s = sp.Symbol("s", positive=True)
    k = sp.Symbol("k", positive=True)
    x_ansatz = sp.log(k * s)
    resid = sp.simplify(sp.diff(x_ansatz, s, 2) + sp.diff(x_ansatz, s) - k * sp.exp(-x_ansatz))
    assert sp.simplify(resid * s**2) == -1, f"ansatz residual not O(1/s^2): {resid}"
    print(f"\n  ansatz x = ln(k*s):  residual of the ODE = {resid}, i.e. O(1/s^2).")
    print("  So x ~ ln(k*ln t): DOUBLE-logarithmic, versus ln t for the linear law.")
    print()
    print("  [SKEPTIC-CAUGHT, and this correction matters] An earlier draft went")
    print("  straight from 'ODE residual is 1/s^2' to an implied convergence rate.")
    print("  Those are DIFFERENT quantities. Linearising x = ln(k*s) + f(s) gives")
    print("    f'' + f' + f/s ~ 1/s^2,  solved at leading order by f = ln(s)/s.")
    print("  So the CORRECTION TO x decays as ln(s)/s -- far slower than 1/s^2.")

    def rhs_s(_s: float, y: np.ndarray, kk: float) -> list[float]:
        x_, xp = y
        return [xp, kk * np.exp(-x_) - xp]

    print("\n  Which decay law actually fits? Four decades, k=1 (decisive test):")
    print(f"    {'s':<10}{'diff = x - ln(k*s)':<22}{'diff/[ln(s)/s]':<18}{'diff/[1/s^2]'}")
    sol = solve_ivp(
        rhs_s, (1.0, 1e6), [0.0, 0.0], args=(1.0,), rtol=1e-12, atol=1e-14, dense_output=True
    )
    assert sol.success, "long integration failed"
    r_lns, r_s2 = [], []
    for sv in (1e3, 1e4, 1e5, 1e6):
        diff = float(sol.sol(sv)[0]) - np.log(sv)
        a_lns, a_s2 = diff / (np.log(sv) / sv), diff / (1.0 / sv**2)
        r_lns.append(a_lns)
        r_s2.append(a_s2)
        print(f"    {sv:<10.0e}{diff:<22.6e}{a_lns:<18.4f}{a_s2:.3e}")
    assert 0.8 < min(r_lns) and max(r_lns) < 1.2, f"ln(s)/s model fails: {r_lns}"
    assert max(r_s2) / min(r_s2) > 100, "1/s^2 model would be flat -- it is not"
    print("  => diff/[ln(s)/s] is FLAT near 1.0 across four decades; diff/[1/s^2]")
    print("     varies by four orders of magnitude. The correction IS ln(s)/s.")
    print("     Refined asymptote:  x = ln(k*ln t) + ln(ln t)/ln t + O(.)")

    # does subtracting the correction actually improve the fit? (skeptic's Test 2)
    print("\n  [refinement check] does subtracting ln(s)/s improve the residual?")
    for sv in (1e4, 1e5, 1e6):
        x_num = float(sol.sol(sv)[0])
        d1 = abs(x_num - np.log(sv))
        d2 = abs(x_num - np.log(sv) - np.log(sv) / sv)
        assert d2 < d1 / 10, f"ln(s)/s refinement did not help at s={sv}"
        print(f"    s={sv:<9.0e} |x-ln(ks)| = {d1:.3e} -> {d2:.3e}   {d1 / d2:.1f}x better")
    print("  => the ln(s)/s term is REAL, not a curve-fitting artifact.")

    # is the asymptote an attractor, or IC-dependent? (skeptic's Test 3)
    print("\n  [uniqueness check] is the asymptote independent of initial data?")
    vals = []
    for ic in ([0.0, 0.0], [0.5, 0.0], [0.0, 0.5], [-1.0, 0.0]):
        s3 = solve_ivp(
            rhs_s, (1.0, 1e4), ic, args=(1.0,), rtol=1e-12, atol=1e-14, dense_output=True
        )
        assert s3.success, f"IC {ic} failed"
        vals.append(float(s3.sol(1e4)[0]))
    spread = max(vals) - min(vals)
    print(f"    x(1e4) across 4 different ICs: spread = {spread:.3e}")
    assert spread < 1e-3, f"asymptote is IC-dependent, spread {spread}"
    print("  => IC-INDEPENDENT: the asymptote is an attractor, so treating it as")
    print("     THE late-time behaviour (not one of a family) is legitimate.")

    print("\n  smaller k, to confirm the k-dependence enters as ln(k):")
    print(f"    {'k':<9}{'s':<10}{'x numeric':<16}{'ln(k*s)':<16}{'diff'}")
    for kk in (0.1, 1.0):
        s4 = solve_ivp(
            rhs_s, (1.0, 1e4), [0.0, 0.0], args=(kk,), rtol=1e-12, atol=1e-14, dense_output=True
        )
        assert s4.success, f"integration failed for k={kk}"
        for sv in (1e3, 1e4):
            x_num = float(s4.sol(sv)[0])
            x_pred = float(np.log(kk * sv))
            print(f"    {kk:<9}{sv:<10.0e}{x_num:<16.8f}{x_pred:<16.8f}{x_num - x_pred:+.5f}")
        rel = abs(float(s4.sol(1e4)[0]) - np.log(kk * 1e4)) / abs(np.log(kk * 1e4))
        assert rel < 0.05, f"asymptote off by {rel:.3f} at k={kk}"
    print("  => NOTE s = ln t, so s=1e4 means t = e^10000. And because the")
    print("     correction decays only as ln(s)/s, the asymptotic form is")
    print("     approached even MORE slowly than ln(ln t) alone suggests. This is")
    print("     a statement about a LAW, emphatically not about a reachable epoch.")

    # NEGATIVE CONTROL: with the LINEAR source (no exp suppression) the same
    # machinery must give x growing like s itself, NOT like ln(s).
    print("\n  [negative control] same machinery, LINEAR source (no exp factor):")
    print("    x'' + x' = k  =>  x -> k*s asymptotically, i.e. x ~ k*ln t.")

    def rhs_lin(_s: float, y: np.ndarray, kk: float) -> list[float]:
        _x, xp = y
        return [xp, kk - xp]

    sol_lin = solve_ivp(
        rhs_lin, (1.0, 1e3), [0.0, 0.0], args=(1.0,), rtol=1e-10, atol=1e-12, dense_output=True
    )
    assert sol_lin.success, "linear-source control failed"
    x_lin_hi = float(sol_lin.sol(1e3)[0])
    rel_lin = abs(x_lin_hi - (1.0 * 1e3 - 1.0)) / (1.0 * 1e3)
    print(f"    x(1e3) = {x_lin_hi:.4f}  vs predicted k*s - k = {1e3 - 1:.4f}  rel {rel_lin:.2e}")
    assert rel_lin < 1e-3, f"linear-source control off: {rel_lin}"
    print("    => the machinery DOES reproduce linear-in-s growth when the")
    print("       suppression is removed. The ln(ln t) result is therefore a")
    print("       consequence of exp(-x), not an artifact of the solver.")

    # ==================================================================
    # PART E -- is the pathology actually gone?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- does the pathological surface still exist?")
    print("-" * 78)
    print(f"    {'x':<8}{'linear 1-x':<16}{'exponential e^-x':<20}{'linear status'}")
    for xv in (0.0, 0.5, 0.9, 1.0, 1.5, 5.0):
        lin = 1.0 - xv
        ex = float(np.exp(-xv))
        status = "OK" if lin > 0 else ("ZERO: rho_phys=0" if lin == 0 else "NEGATIVE mass")
        print(f"    {xv:<8}{lin:<16.6f}{ex:<20.6f}{status}")
        assert ex > 0, "exponential law went non-positive -- impossible"
    print("\n  => the exponential law is positive for ALL x: no zero, no sign flip.")
    print("     rho_phys = rho_A*exp(-x) decays but never vanishes at finite x.")
    print("     The x=1 surface that motivated P65-P67 does not exist here.")

    # ==================================================================
    # PART F -- Anti-Overfitting Gate, scored honestly
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART F -- Anti-Overfitting Gate (falsification-ladder.md), HONEST scoring")
    print("-" * 78)
    aog = [
        (
            "AOG-1 pre-registration",
            "PARTIAL",
            "d ln m/dphi = const is a standard mass-varying-DM form, so the "
            "FUNCTION was available beforehand -- but the MOTIVATION to adopt "
            "it here arrived only after P65/P67 produced the null.",
        ),
        ("AOG-2 specificity", "PASS", "one-parameter, same as the linear law; not a widening."),
        (
            "AOG-3 novel prediction",
            "PARTIAL",
            "[SKEPTIC-DOWNGRADED from a self-flattering PASS] the predictions "
            "(x ~ ln ln t; O(g^2) worldline terms) exist, but THIS SAME FILE "
            "concedes they sit at t = e^10000 and that no observational channel "
            "is proposed. Scoring a clean PASS while conceding unreachability in "
            "the same document is precisely the pattern AOG exists to catch.",
        ),
        (
            "AOG-4 non-triviality",
            "PARTIAL",
            "[SKEPTIC-DOWNGRADED] it does forbid the x=1 crossing, so it is not "
            "empty -- but the two laws agree at O(g) and differ only at O(g^2) "
            "with no channel attached. Falsifiable in principle only.",
        ),
        (
            "AOG-5 independent motivation",
            "FAIL",
            "the source's own term is LINEAR in phi (FINDING_P33, exact). The "
            "exponential requires ADDING phi^2, phi^3, ... with no independent "
            "basis in the source. Wanting to avoid x=1 is exactly the motivation "
            "AOG-5 exists to catch.",
        ),
    ]
    n_pass = sum(1 for _, v, _ in aog if v == "PASS")
    for name, verdict, why in aog:
        print(f"  {name:<28} {verdict}")
        print(f"      {why}")
    n_partial = sum(1 for _, v, _ in aog if v == "PARTIAL")
    n_fail = sum(1 for _, v, _ in aog if v == "FAIL")
    print(f"\n  SCORE: {n_pass} clear PASS, {n_partial} PARTIAL, {n_fail} FAIL out of 5.")
    assert n_pass == 1, f"expected 1 clear pass after the honest re-score, got {n_pass}"
    assert n_partial == 3 and n_fail == 1, "re-score tally wrong"
    print("  Rule: >=3 of 5 PASS permits promotion to weak_alive. NOT MET.")
    print("  => STATUS: `parked`, NOT `weak_alive`.")
    print()
    print("  [SELF-CORRECTION, recorded rather than quietly amended] An earlier")
    print("  draft scored this 3 PASS / 1 PARTIAL / 1 FAIL and claimed weak_alive")
    print("  eligibility while declining promotion anyway. The context-blind")
    print("  reviewer showed AOG-3 and AOG-4 were self-flattering, and the")
    print("  re-score was verified independently before acceptance. The FINAL")
    print("  decision (do not promote) is unchanged -- but the intermediate")
    print("  scoring was wrong, and a wrong score that happens to reach the right")
    print("  verdict is still a wrong score.")
    print()
    print("  => P68 is a [HYPOTHESIS]-tier ALTERNATIVE COMPLETION, parked,")
    print("     explicitly NOT a repair of the existing one, and NOT promoted")
    print("     above the linear law. Both stay live; they differ at O(g_hat^2).")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  ESTABLISHED:")
    print("   * the linear mass law is EXACT given the source's linear coupling,")
    print("     so the exponential is a DIFFERENT completion requiring added")
    print("     phi^2, phi^3, ... worldline terms -- not a reformulation;")
    print("   * the two agree exactly at O(g_hat), so P66/P67 survive verbatim,")
    print("     INCLUDING P67's negative result -- this swap does NOT rescue it;")
    print("   * the scalar source becomes self-limiting, g*rho_A*exp(-x), a")
    print("     DIFFERENT stabilisation mechanism from the one P67 ruled out;")
    print("   * consequently x ~ ln(k*ln t), double-logarithmic, not ln t --")
    print("     with the correction decaying only as ln(ln t)/ln t, verified")
    print("     over four decades, and the asymptote confirmed IC-independent")
    print("     (negative control: removing the suppression restores linear-in-s")
    print("     growth, so ln ln t is a consequence of exp(-x), not the solver);")
    print("   * no pathological surface exists: m/m0 = exp(-x) > 0 for all x.")
    print()
    print("  NOT ESTABLISHED:")
    print("   * that MULTING implies an exponential law. It does not -- the")
    print("     source is linear. This is OUR alternative, and AOG-5 FAILS.")
    print("   * the 'different completion' claim OUTSIDE the canonical kinetic-")
    print("     term convention. A field redefinition can move the mass law from")
    print("     linear to exponential, but only by making (d phi)^2 non-canonical")
    print("     (Part A). The claim is convention-relative, and the convention is")
    print("     stated rather than assumed.")
    print("   * that the exponential is preferable. It removes a pathology at the")
    print("     cost of terms with no independent justification; that trade is")
    print("     NOT resolved here and must not be presented as resolved.")
    print("   * anything about V(phibar) != 0 -- still untouched, a separate")
    print("     variant per the Minimal Relaxation Rule, deliberately NOT bundled.")
    print("   * that the asymptotic regime is reachable: s = ln t, so the check")
    print("     at s=1e4 sits at t = e^10000. A law, not an epoch.")
    print("   * anything about MULTING itself (Gate 1): this is our reconstruction.")
    print()
    print("  NET: the linear law's pathology is real and the exponential removes")
    print("  it, but at a cost the AOG makes explicit -- and on an honest re-score")
    print("  the AOG gives only 1 clean PASS, putting this at `parked`. Two live")
    print("  completions, differing at O(g_hat^2). Neither is promoted.")
    print()
    print("  The most useful result here is arguably the NEGATIVE one: because")
    print("  the two laws coincide exactly at O(g_hat), FINDING_P67's result is")
    print("  NOT escapable by this route. Any rescue of backreaction-driven")
    print("  stabilisation must come from O(g_hat^2) or from V(phibar) != 0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
