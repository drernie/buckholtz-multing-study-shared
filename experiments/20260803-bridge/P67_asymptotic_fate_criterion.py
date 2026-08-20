"""P67 -- asymptotic-fate criterion for the g_hat!=0 coupled background.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

Question (user-proposed, this session): FINDING_P65 found that x := g_hat*phibar
drifts logarithmically without bound on the uncoupled background. Does the FULL
coupled backreaction stop that drift -- i.e. can the expansion "freeze" the field
before it reaches the x=1 surface where rho_phys=(1-x)*rho_A vanishes?

The proposal reduced this to convergence of  I_inf = int^inf t/a^3(t) dt, with a
trichotomy for a ~ t^p:  p<2/3 power-divergence, p=2/3 log, p>2/3 convergence.

This file establishes four things:

  A. The criterion itself is EXACT -- it follows from FINDING_P66's exact first
     integral a^3*phibar_dot = sqrt(2)+g_hat*(t-1), no approximation.

  B. FINDING_P62's own background sits EXACTLY on the p=2/3 knife-edge
     (a0^3 = 6*pi*t^2 - 1 identically). So the fate is NOT decided by the leading
     power -- it is decided by the SUBLEADING behaviour of a^3, i.e. by exactly
     the O(g_hat) correction delta(t) that FINDING_P66 already computed.

  C. delta(t) SATURATES to a closed-form constant. Equivalently and more
     readably, c = -phibar0(inf)/3: the asymptotic scale-factor correction is the
     TOTAL accumulated zeroth-order field displacement, over 3. Therefore
     a^3 -> a0^3*(1+g_hat*c)^3 -- the power p is UNCHANGED, and only the
     coefficient of the log divergence moves, by 0.08% at |g_hat|=0.01 and 0.77%
     at |g_hat|=0.1. An ablation (true c vs c=0 vs -c) confirms the numerics
     actually RESOLVE this shift rather than merely tolerating it.

  D. SCOPE, established here rather than left implicit. TWO bounds limit the
     expansion, and the binding one is not the obvious one:
       Bound 1: x << 1, since x enters the Friedmann equation AT O(g_hat).
       Bound 2 (BINDS EARLIER): the phibar series needs |g*phibar1| << phibar0,
         but phibar0 -> a finite constant while phibar1 grows secularly as
         ln(t)/(6*pi). This fails at ln t ~ 1.44/g_hat -- three orders of
         magnitude in ln t before x would reach 1.
     This file therefore does NOT claim the crossing happens.

Verdict: at first order in g_hat, and inside the regime where that order is
valid, the hoped-for stabilisation mechanism gets NO support -- it is negligible,
and for g_hat>0 what little there is points the wrong way. Neither sign of g_hat
changes the divergence class. That is a real negative result about a specific
proposed mechanism -- not a claim about the ultimate fate of the model, which
remains undetermined.
"""

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp

# module-level physical convention, matching FINDING_P62/P66 (B=D=1, G_N=C=1)
G_N = 1.0
C_MATTER = 1.0


def build_delta_ode() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Symbol]:
    """Rebuild FINDING_P66's linear ODE for delta(t). Returns (Q_t, mu, a0_cubed, t).

    Only the fast symbolic part of P66 Part C is reproduced -- the slow final
    antiderivative is deliberately not attempted (P66 established it intractable).
    """
    t = sp.Symbol("t", positive=True)
    g = sp.Symbol("g_hat", real=True)

    # WHY: K tied to G_N, never a free symbol -- P66 self-caught bug #1, where an
    # untied K silently broke the background's own Friedmann positive control.
    a0_cubed = sp.expand(sp.Rational(9, 4) * (8 * sp.pi * sp.Integer(1) / 3) * t**2 - 1)
    a0_g1 = a0_cubed ** sp.Rational(1, 3)
    phibardot0_g1 = sp.sqrt(2) / a0_cubed

    a0_abs = sp.Function("a0")(t)
    phibar0_abs = sp.Function("phibar0")(t)
    phibar1_abs = sp.Function("phibar1")(t)
    delta_abs = sp.Function("delta")(t)
    C_a, G_N_a = sp.symbols("C G_N", real=True, positive=True)

    a_full = a0_abs * (1 + g * delta_abs)
    phibar_full = phibar0_abs + g * phibar1_abs
    fried = sp.expand(
        (sp.diff(a_full, t) / a_full) ** 2
        - (8 * sp.pi * G_N_a / 3)
        * (C_a / a_full**3 * (1 - g * phibar_full) + sp.diff(phibar_full, t) ** 2 / 2)
    )
    order1 = sp.simplify(sp.diff(fried, g).subs(g, 0))
    phibar1dot_exact = (t - 1) / a0_abs**3 - 3 * delta_abs * sp.diff(phibar0_abs, t)
    order1_closed = sp.simplify(order1.subs(sp.diff(phibar1_abs, t), phibar1dot_exact))
    assert not order1_closed.has(phibar1_abs), "phibar1 survived closure"

    poly = sp.Poly(sp.expand(order1_closed), sp.diff(delta_abs, t), delta_abs)
    A_c = poly.coeff_monomial(sp.diff(delta_abs, t))
    B_c = poly.coeff_monomial(delta_abs)
    D_c = poly.coeff_monomial(1)

    b_s, Tv = sp.Symbol("b", positive=True), sp.Symbol("Tv", positive=True)
    phibar0_of_t = (
        sp.integrate(sp.sqrt(2) / (b_s * t**2 - 1), (t, 1, Tv))
        .subs(Tv, t)
        .subs(b_s, sp.Rational(9, 4) * sp.Rational(8, 3) * sp.pi)
    )
    # WHY: sp.Integer(1), not the module-level float -- P66 self-caught bug #2,
    # where a float substitution polluted otherwise-exact rational coefficients.
    sb = {G_N_a: sp.Integer(1), C_a: sp.Integer(1)}
    A_n = sp.simplify(A_c.subs(sb).subs(a0_abs, a0_g1).doit())
    D_n = sp.simplify(
        D_c.subs(sb)
        .subs(a0_abs, a0_g1)
        .subs(sp.diff(phibar0_abs, t), phibardot0_g1)
        .subs(phibar0_abs, phibar0_of_t)
        .doit()
    )
    assert not (A_n.free_symbols - {t}), f"A(t) stray symbols: {A_n.free_symbols}"
    assert not (D_n.free_symbols - {t}), f"D(t) stray symbols: {D_n.free_symbols}"

    Q_t = sp.simplify(-D_n / A_n)

    # [SKEPTIC-ADDED] mu was previously hardcoded without deriving B, so a
    # miscopy could not be self-detected. Derive B and CHECK mu_dot/mu = B/A.
    B_n = sp.simplify(
        B_c.subs(sb).subs(a0_abs, a0_g1).subs(sp.diff(phibar0_abs, t), phibardot0_g1).doit()
    )
    assert not (B_n.free_symbols - {t}), f"B(t) stray symbols: {B_n.free_symbols}"
    mu = t - 1 / (6 * sp.pi * t)
    mu_check = sp.simplify(sp.diff(mu, t) / mu - B_n / A_n)
    assert mu_check == 0, f"mu is NOT the integrating factor for B/A: {mu_check}"
    return Q_t, mu, a0_cubed, t


def main() -> int:
    print("=" * 78)
    print("P67 -- asymptotic-fate criterion for the g_hat!=0 coupled background")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    t = sp.Symbol("t", positive=True)
    g = sp.Symbol("g_hat", real=True)

    # ==================================================================
    # PART A -- the criterion is EXACT, inherited from P66's first integral
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- the fate criterion follows EXACTLY from P66, no approximation")
    print("-" * 78)
    a_gen = sp.Function("a")(t)
    phibar_gen = sp.Function("phibar")(t)
    C_s = sp.Symbol("C", positive=True)

    # re-verify P66 Part A here rather than cite it: d/dt(a^3*phibar_dot) = g*C
    H_gen = sp.diff(a_gen, t) / a_gen
    phibar_ddot = g * (C_s / a_gen**3) - 3 * H_gen * sp.diff(phibar_gen, t)
    lhs = sp.diff(a_gen**3 * sp.diff(phibar_gen, t), t)
    resid = sp.simplify(lhs.subs(sp.diff(phibar_gen, t, 2), phibar_ddot) - g * C_s)
    assert resid == 0, f"P66 Part A does not reproduce: {resid}"
    print("  [re-verified, not cited] d/dt(a^3*phibar_dot) - g_hat*C = 0 for a")
    print("  GENERIC a(t). So a^3*phibar_dot = sqrt(2) + g_hat*(t-1) exactly.")

    # x := g*phibar  =>  x_dot = g*phibar_dot = g*(sqrt2+g*(t-1))/a^3
    x_dot = sp.simplify(g * (sp.sqrt(2) + g * (t - 1)) / a_gen**3)
    expected = (sp.sqrt(2) * g + g**2 * (t - 1)) / a_gen**3
    assert sp.simplify(x_dot - expected) == 0, "x_dot relation failed"
    print("  => x := g_hat*phibar obeys  x_dot = (sqrt2*g + g^2*(t-1)) / a^3.")
    print("  => at large t the g^2*(t-1) term dominates, and g^2 > 0 for EITHER")
    print("     sign of g_hat: the late-time drift of x is one-directional.")
    print("     [this is why FINDING_P64 found no sign asymmetry -- now explained]")
    print("  => fate hinges on convergence of  I_inf = int^inf t/a^3(t) dt.")

    # ==================================================================
    # PART B -- P62's background is EXACTLY the marginal case
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- FINDING_P62's background sits EXACTLY on the p=2/3 knife-edge")
    print("-" * 78)
    Q_t, mu, a0_cubed, t = build_delta_ode()
    print(f"  P62 background (B=D=1, G_N=1):  a0^3(t) = {a0_cubed}")

    lead = sp.limit(a0_cubed / t**2, t, sp.oo)
    assert lead == 6 * sp.pi, f"a0^3/t^2 -> {lead}, expected 6*pi"
    print(f"  a0^3 / t^2  ->  {lead}   as t->oo   =>  a0 ~ t^(2/3) EXACTLY")

    integrand_x_t = sp.limit(t * (t / a0_cubed), t, sp.oo)
    assert integrand_x_t == 1 / (6 * sp.pi), f"marginality failed: {integrand_x_t}"
    print(f"  t * (t/a0^3) -> {integrand_x_t}  =>  integrand ~ 1/(6*pi*t)")
    print("  => I(T) diverges LOGARITHMICALLY. This is the knife-edge, not one")
    print("     of three generic outcomes: the leading power decides NOTHING,")
    print("     and the subleading behaviour of a^3 decides everything.")

    # ==================================================================
    # PART C -- POSITIVE + NEGATIVE CONTROLS on the criterion machinery
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- controls: can the criterion actually DISCRIMINATE?")
    print("-" * 78)
    print("  A criterion that reports 'diverges' for every input is useless.")
    print("  Four backgrounds with analytically KNOWN answers:")
    cases: list[tuple[str, sp.Expr, str]] = [
        ("p=1/3  (a^3 = t)", t, "power-diverges"),
        ("p=2/3  (a^3 = t^2)", t**2, "log-diverges"),
        ("p=1    (a^3 = t^3)", t**3, "CONVERGES"),
        ("de Sitter (a^3 = e^3t)", sp.exp(3 * t), "CONVERGES"),
    ]
    for label, a3, expected_word in cases:
        Ival = sp.integrate(t / a3, (t, 1, sp.oo))
        converged = Ival.is_finite is True
        got = "CONVERGES" if converged else "diverges"
        ok = ("CONVERGES" in expected_word) == converged
        assert ok, f"control FAILED for {label}: expected {expected_word}, got {got}"
        print(f"    {label:<26} I_inf = {str(Ival):<12} -> {got:<10} [expected {expected_word}]")
    print("  => CONTROLS PASS: the criterion separates convergent from divergent,")
    print("     and places p=2/3 on the boundary. It is not a rubber stamp.")

    # ==================================================================
    # PART D -- delta(t) saturates to a CLOSED-FORM constant
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- delta(t) asymptote, in closed form")
    print("-" * 78)
    print("  Analytic argument: Q(t) ~ c/t and mu(t) ~ t  =>  mu*Q ~ c")
    print("  =>  int mu*Q ~ c*t  =>  delta = (1/mu)*int(mu*Q) ~ c.  So delta")
    print("  saturates, and delta_inf = lim t*Q(t) -- a closed-form constant.")

    c_sym = sp.simplify(sp.limit(t * Q_t, t, sp.oo))
    c_val = float(sp.N(c_sym, 30))
    print(f"\n  c = lim t*Q(t) = {c_sym}")
    print(f"  c (numeric)    = {c_val:.10f}")
    assert c_val < 0, f"c expected negative, got {c_val}"

    # [SKEPTIC-ADDED, independently re-verified before adopting] The reviewer
    # re-derived c by hand in a far more readable closed form:
    #     c = -phibar0(inf)/3,   phibar0(inf) = int_1^inf sqrt2/(6*pi*t^2-1) dt
    # Adopted here because it is not merely tidier -- it says what c MEANS:
    # delta_inf is set by the TOTAL accumulated displacement of the zeroth-order
    # field, divided by 3. Asserted equal to the sympy limit, not assumed.
    phibar0_inf = sp.simplify(sp.integrate(sp.sqrt(2) / (6 * sp.pi * t**2 - 1), (t, 1, sp.oo)))
    c_readable = -phibar0_inf / 3
    assert abs(float(sp.N(c_readable - c_sym, 30))) < 1e-20, (
        f"readable closed form disagrees with lim t*Q(t): {c_readable} vs {c_sym}"
    )
    print(f"\n  [equivalent, readable]  c = -phibar0(inf)/3, phibar0(inf) = {phibar0_inf}")
    print(
        f"  phibar0(inf) = {float(sp.N(phibar0_inf, 20)):.10f}  =>  c = {float(sp.N(c_readable, 20)):.10f}"
    )
    print("  => the two closed forms agree to <1e-20. Physical reading: delta_inf")
    print("     is the TOTAL accumulated zeroth-order field displacement, over 3.")

    mu_f = sp.lambdify(t, mu, "numpy")
    Q_f = sp.lambdify(t, Q_t, "numpy")

    def delta_of(T: float) -> float:
        """delta(T) with delta(1)=0, integrating factor + numeric quadrature."""
        val, _ = quad(lambda s: mu_f(s) * Q_f(s), 1.0 + 1e-9, T, limit=800)
        return float(val / mu_f(T))

    print("\n  numeric delta(T), five decades (independent of the limit above):")
    for T in [1e3, 1e4, 1e5, 1e6, 1e7]:
        print(f"    delta({T:>8.0e}) = {delta_of(T): .10f}")
    d_far = delta_of(1e7)
    rel = abs(d_far - c_val) / abs(c_val)
    print(f"\n  |delta(1e7) - c|/|c| = {rel:.3e}")
    assert rel < 1e-3, f"delta does not converge to lim t*Q(t): {d_far} vs {c_val}"
    print("  => CONFIRMED: delta SATURATES at the closed-form constant. It does")
    print("     NOT grow -- so it cannot change the leading power of a^3.")

    # ==================================================================
    # PART E -- consequence: power unchanged, coefficient rescaled the WRONG way
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- consequence for I(T)")
    print("-" * 78)
    print("  a^3 = a0^3*(1+g*delta)^3 -> a0^3*(1+g*c)^3: a CONSTANT rescaling.")
    print("  a0^3 ~ 6*pi*t^2, so a^3 ~ [6*pi*(1+g*c)^3]*t^2 -- still exactly t^2.")
    print("  => the O(g_hat) backreaction does NOT change p=2/3.")
    print("  => I(T) ~ [1/(6*pi*(1+g*c)^3)] * ln T  ->  still divergent.\n")
    # [SKEPTIC-ADDED] both signs of g_hat tabulated. An earlier version showed
    # only g>0 and asserted a bare "wrong sign" -- incomplete, since c<0 means
    # the shift REVERSES for g<0 (verified independently before adopting).
    print(f"    {'g_hat':<9}{'(1+g*c)^-3':<15}{'vs g_hat=0':<14}{'direction':<10}{'note'}")
    for gv in (-1.0, -0.1, -0.01, 0.01, 0.1, 1.0):
        fac = 1.0 / (1.0 + gv * c_val) ** 3
        direction = "faster" if fac > 1 else "slower"
        note = "formal only" if abs(gv) == 1.0 else "cross-checked" if gv > 0 else ""
        print(f"    {gv:<9}{fac:<15.6f}{(fac - 1) * 100:<+14.2f}{direction:<10}{note}")
    print("\n  Reading this HONESTLY, magnitude first:")
    print("   * the shift is TINY: 0.08% at |g|=0.01, 0.77% at |g|=0.1. The")
    print("     dominant fact is that backreaction is NEGLIGIBLE at this order.")
    print("   * its DIRECTION depends on sign(g_hat): for g>0 the drift is")
    print("     marginally faster, for g<0 marginally slower.")
    print("   * but the g^2 numerator of x_dot is sign-blind, so NEITHER sign")
    print("     changes the divergence CLASS. Negative g_hat slows a divergent")
    print("     drift; it does not stop one.")
    print("   * the |g_hat|=1 rows are a FORMAL evaluation of the small-g")
    print("     expansion -- they are NOT covered by the cross-check below,")
    print("     which stops at |g_hat|=0.1.")
    print("\n  => the proposed rescue is absent because it is negligible, and")
    print("     for g>0 what little there is points the wrong way. The correct")
    print("     summary is 'negligible, and not helpful' -- NOT 'a large effect")
    print("     in the wrong direction'.")
    # ==================================================================
    # PART F -- SCOPE: where does the O(g_hat) expansion actually hold?
    # ==================================================================
    print("\n" + "-" * 78)
    print("PART F -- [SCOPE, self-imposed] where is any of this valid?")
    print("-" * 78)
    print("  BOUND 1 (stated in the first version): x enters the Friedmann")
    print("  equation AT O(g_hat) -- the term K*rho_A*(1 - g_hat*phibar) has")
    print("  g_hat*phibar = x as its O(g_hat) piece. So the expansion needs")
    print("  x << 1 -- the same x whose approach to 1 is the question.")
    print()
    print("  BOUND 2 [SKEPTIC-CAUGHT, independently re-derived, and it BINDS")
    print("  EARLIER]: the phibar series itself is phibar = phibar0 + g*phibar1,")
    print("  needing |g*phibar1| << phibar0. But phibar0 -> phibar0(inf), a")
    print("  FINITE constant, while phibar1_dot ~ 1/(6*pi*t) makes phibar1 grow")
    print("  SECULARLY as ln(t)/(6*pi). The ratio g*ln(t)/(6*pi*phibar0(inf))")
    print("  reaches 1 at ln t ~ 1.44/g -- far EARLIER than x reaches 1.")
    phib_inf = float(sp.N(phibar0_inf, 20))
    print(f"\n    {'g_hat':<9}{'ln t: series breaks':<24}{'ln t: x->1':<18}{'which first'}")
    for gv in (0.01, 0.1, 1.0):
        lnt_series = 6 * np.pi * phib_inf / gv
        coef = gv**2 / (6.0 * np.pi * (1.0 + gv * c_val) ** 3)
        lnt_x1 = 1.0 / coef
        assert lnt_series < lnt_x1, f"series bound not the binding one at g={gv}"
        print(f"    {gv:<9}{lnt_series:<24.4g}{lnt_x1:<18.4g}{'SERIES'}")
    print("\n  => the perturbative description dies THREE ORDERS OF MAGNITUDE in")
    print("     ln t before the x=1 pathology would be reached. This does not")
    print("     weaken the O(g_hat) negative result (which lives in the valid")
    print("     window); it STRENGTHENS the refusal to say anything about x=1.")

    # leading-log estimate of x(t), then the crossing time it implies.
    # WHY log10: exp(0.1/coef) overflows to inf for small g_hat and prints as
    # an uninformative "inf" -- report the exponent instead.
    print("\n  Leading-log estimate  x(t) ~ [g^2/(6*pi*(1+g*c)^3)]*ln t  (x0=0):")
    print(f"    {'g_hat':<8}{'log10(t) at x=0.1':<24}{'log10(t) at x=1':<20}")
    for gv in (0.01, 0.1, 1.0):
        coef = gv**2 / (6.0 * np.pi * (1.0 + gv * c_val) ** 3)
        lg_01 = 0.1 / coef / np.log(10.0)
        lg_1 = 1.0 / coef / np.log(10.0)
        print(f"    {gv:<8}{lg_01:<24.4g}{lg_1:<20.4g}")
    print("\n  *** The x=1 crossing lies FAR outside the x<<1 window in every")
    print("  case. This file therefore does NOT claim the crossing occurs. ***")
    print("  What it does establish is narrower and still real: the specific")
    print("  proposed rescue -- backreaction-driven freezing -- is absent at")
    print("  the only order where we can currently compute.")

    # ---- cross-check vs the FULL nonlinear system (P64 machinery) ----
    # [SELF-CAUGHT BUG, kept visible per this campaign's discipline] The first
    # version of this check compared full x(t) against the ASYMPTOTIC log-rate
    # g^2/(6*pi*(1+g*c)^3) over t=50..200 and asserted 25% agreement. It FAILED
    # at g_hat=0.01 (rel.diff 1.52). The physics was right; the TEST was wrong.
    # x_dot has two terms, sqrt2*g/a^3 and g^2*(t-1)/a^3, crossing over at
    # t ~ 1 + sqrt2/g:  g=0.01 -> t~142, g=0.1 -> t~15, g=1.0 -> t~2.4. At
    # t=50 with g=0.01 the DROPPED transient still dominates the RETAINED
    # asymptotic term, so the comparison was against the wrong quantity.
    # Fixed by (i) comparing to the FULL O(g) prediction in the near window,
    # and (ii) testing the asymptotic rate only far PAST the crossover.
    print("\n  Cross-check vs the FULL nonlinear system (P64 machinery).")
    print("  x_dot has two terms, crossing over at t ~ 1 + sqrt2/g_hat:")
    for gv in (0.01, 0.1, 1.0):
        print(f"    g_hat={gv:<6} transient dominates until t ~ {1 + np.sqrt(2) / gv:.1f}")

    def rhs(time: float, y: np.ndarray, ghat: float) -> list[float]:
        a, phibar, phibardot = y
        rho_A = C_MATTER / a**3
        rho_phys = rho_A * (1.0 - ghat * phibar)
        arg = (8.0 * np.pi * G_N / 3.0) * (rho_phys + phibardot**2 / 2.0)
        H = np.sqrt(max(arg, 0.0))
        return [a * H, phibardot, ghat * rho_A - 3.0 * H * phibardot]

    a1 = float((6.0 * np.pi - 1.0) ** (1.0 / 3.0))
    phibardot1 = np.sqrt(2.0) / (6.0 * np.pi - 1.0)
    # positive control on the initial data: P62's own closed-form H(1)
    H1 = np.sqrt((8 * np.pi * G_N / 3) * (1.0 / a1**3 + phibardot1**2 / 2))
    H1_expected = (2.0 / 3.0) * (12 * np.pi) / (2 * (6 * np.pi - 1))
    assert abs(H1 - H1_expected) < 1e-12, f"initial Friedmann fails: {H1} vs {H1_expected}"
    print(f"\n  [positive control] H(1) from the state vector = {H1:.12f}")
    print(f"  [positive control] H(1) from P62 closed form   = {H1_expected:.12f}  MATCH")

    a0c_f = sp.lambdify(t, a0_cubed, "numpy")

    def x_semianalytic(T: float, ghat: float) -> float:
        """O(g) prediction for x(T) itself, with x(1)=0.

        WHY no extra factor of ghat at the call site: the integrand below IS
        x_dot = (sqrt2*g + g^2*(t-1))/a^3 -- the coupling is already inside it.
        [SELF-CAUGHT BUG #2, kept visible] The first version multiplied the
        result by ghat AGAIN at the call site, giving x_pred exactly 1/ghat too
        small; the tell was x_full/x_pred = 100.000 at ghat=0.01, a suspiciously
        round number equal to 1/ghat rather than anything physical.
        """

        def integrand(s: float) -> float:
            a3 = a0c_f(s) * (1.0 + ghat * delta_of(s)) ** 3
            return (np.sqrt(2.0) * ghat + ghat**2 * (s - 1.0)) / a3

        val, _ = quad(integrand, 1.0, T, limit=200)
        return float(val)

    print("\n  (i) near window -- full nonlinear x(T) vs the FULL O(g) prediction:")
    print(f"    {'g_hat':<8}{'T':<8}{'x_full':<15}{'x_O(g)':<15}{'rel.diff'}")
    for gv in (0.01, 0.1):
        y0 = [a1, 0.0, phibardot1]
        sol = solve_ivp(
            rhs, (1.0, 200.0), y0, args=(gv,), rtol=1e-11, atol=1e-13, dense_output=True
        )
        assert sol.success, f"integration failed for g_hat={gv}"
        for T in (50.0, 200.0):
            x_full = gv * float(sol.sol(T)[1])
            x_pred = x_semianalytic(T, gv)  # already includes g_hat -- see docstring
            rel = abs(x_full - x_pred) / abs(x_full)
            print(f"    {gv:<8}{T:<8.0f}{x_full:<15.6e}{x_pred:<15.6e}{rel:<10.2e}")
            assert rel < 0.02, f"O(g) prediction off by {rel:.3f} at g={gv}, T={T}"
    print("  => agrees to better than 2%: the perturbative machinery tracks the")
    print("     full nonlinear system in the window where it is supposed to.")

    print("\n  (ii) far window -- asymptotic log-rate, tested PAST the crossover:")
    print(f"    {'g_hat':<8}{'window':<14}{'dx/dlnt full':<16}{'predicted':<16}{'rel.diff'}")
    for gv in (0.01, 0.1):
        y0 = [a1, 0.0, phibardot1]
        sol = solve_ivp(rhs, (1.0, 1e6), y0, args=(gv,), rtol=1e-10, atol=1e-14, dense_output=True)
        assert sol.success, f"far integration failed for g_hat={gv}"
        t_lo, t_hi = 1e5, 1e6
        x_lo, x_hi = gv * float(sol.sol(t_lo)[1]), gv * float(sol.sol(t_hi)[1])
        rate_full = (x_hi - x_lo) / np.log(t_hi / t_lo)
        coef = gv**2 / (6.0 * np.pi * (1.0 + gv * c_val) ** 3)
        rel_rate = abs(rate_full - coef) / abs(coef)
        print(f"    {gv:<8}{'1e5..1e6':<14}{rate_full:<16.6e}{coef:<16.6e}{rel_rate:<10.4f}")
        assert rel_rate < 0.05, f"asymptotic rate mismatch g={gv}: {rel_rate}"
        # confirm we stayed IN SCOPE out there, i.e. x is still small
        assert abs(x_hi) < 0.1, f"x left the small-x window at g={gv}: x={x_hi}"
    print("  => the full nonlinear growth rate matches the predicted asymptotic")
    print("     log-coefficient to better than 5%, with x still < 0.1 (in scope).")

    # ---- [SKEPTIC-DEMANDED] does the cross-check RESOLVE c, or merely tolerate it? ----
    # The reviewer's sharpest point: Part C's four controls test the INTEGRAL
    # classifier, not the delta calculation. A sign error in Q, a missing term in
    # B, or a wrong c would sail straight through them. Two ablations fix that:
    # if the measured rate agrees best with the TRUE c, and strictly worse with
    # c=0 and with c flipped, then the check genuinely resolves the c-correction.
    print("\n  (iii) [ABLATION] does the far-window check actually RESOLVE c,")
    print("  or is it just loose enough to tolerate any c? Compare the SAME")
    print("  measured rate against three predictions: true c, c=0, and -c.")
    print(
        f"\n    {'g_hat':<8}{'rel.diff true c':<18}{'rel.diff c=0':<16}{'rel.diff -c':<14}{'best'}"
    )
    for gv in (0.01, 0.1):
        y0 = [a1, 0.0, phibardot1]
        sol = solve_ivp(rhs, (1.0, 1e6), y0, args=(gv,), rtol=1e-10, atol=1e-14, dense_output=True)
        assert sol.success, f"ablation integration failed for g_hat={gv}"
        x_lo, x_hi = gv * float(sol.sol(1e5)[1]), gv * float(sol.sol(1e6)[1])
        rate_full = (x_hi - x_lo) / np.log(10.0)
        variants = {
            "true c": c_val,
            "c=0": 0.0,
            "-c": -c_val,
        }
        rels: dict[str, float] = {}
        for name, cc in variants.items():
            pred = gv**2 / (6.0 * np.pi * (1.0 + gv * cc) ** 3)
            rels[name] = abs(rate_full - pred) / abs(pred)
        best = min(rels, key=lambda k: rels[k])
        print(f"    {gv:<8}{rels['true c']:<18.5f}{rels['c=0']:<16.5f}{rels['-c']:<14.5f}{best}")
        assert best == "true c", f"ablation FAILED at g={gv}: best fit was {best}, not true c"
        assert rels["c=0"] > rels["true c"], f"c=0 not worse at g={gv}"
        assert rels["-c"] > rels["c=0"], f"flipped c not worst at g={gv}"
    print("  => ABLATION PASSES: the true c fits strictly best, c=0 is worse, and")
    print("     a sign-flipped c is worst. The check RESOLVES the c-correction --")
    print("     it is not a loose tolerance accepting anything. Combined with the")
    print("     0.0006 agreement, this makes the sign of c an empirical result")
    print("     here, not only a symbolic one.")
    print("\n  HONEST NAMING [skeptic-corrected]: both sides solve the SAME")
    print("  Friedmann+KG equations, so this validates the DERIVATION (it caught")
    print("  both bugs above), NOT the physics choices -- the Lagrangian, the")
    print("  coupling form, and the initial data are shared and therefore")
    print("  untested by it. 'Self-consistency against numerical integration of")
    print("  the same equations' is the accurate label, not 'independent check'.")

    # ==================================================================
    # PART G -- verdict
    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  ESTABLISHED (exact, no approximation):")
    print("   * the fate criterion I_inf = int^inf t/a^3 dt follows from P66's")
    print("     exact first integral -- it is not a modelling choice;")
    print("   * P62's background is EXACTLY marginal (a0^3 = 6*pi*t^2 - 1), so")
    print("     the leading power decides nothing and the subleading term decides")
    print("     everything -- this is a knife-edge, not a generic case;")
    print("   * the criterion machinery discriminates (4 controls, Part C).")
    print()
    print("  ESTABLISHED (first order in g_hat):")
    print(f"   * delta(t) SATURATES at c = {c_val:.8f} < 0, in closed form;")
    print("   * therefore a^3 keeps the SAME power t^2 -- backreaction cannot")
    print("     change convergence class at this order;")
    print("   * the log coefficient is rescaled by (1+g*c)^-3, and the ABLATION")
    print("     shows the data resolve this: true c fits strictly better than")
    print("     c=0 or -c. Magnitude first, honestly: the shift is 0.08% at")
    print("     |g|=0.01 and 0.77% at |g|=0.1. The dominant fact is that the")
    print("     backreaction is NEGLIGIBLE here; its direction (faster for g>0,")
    print("     slower for g<0) is a secondary detail on a tiny effect.")
    print("   * NEITHER sign changes the divergence CLASS -- the g^2 numerator")
    print("     of x_dot is sign-blind. So no choice of sign(g_hat) rescues it.")
    print()
    print("  NOT ESTABLISHED -- and this file must not be read as claiming it:")
    print("   * that x actually reaches 1. TWO bounds fail before then, and the")
    print("     binding one is NOT the obvious one: the phibar series breaks at")
    print("     ln t ~ 1.44/g_hat, three orders of magnitude in ln t EARLIER")
    print("     than x would reach 1 (Part F, Bound 2).")
    print("   * anything at O(g_hat^2), which is where a genuine change of power")
    print("     would have to come from if it comes at all;")
    print("   * anything with V(phibar) != 0 -- a potential is precisely the kind")
    print("     of term that CAN change the late-time power p, and P66/P67 both")
    print("     assume V=0;")
    print("   * generality of rhobar_A*a^3 = C, inherited from FINDING_P58.")
    print()
    print("  NET: a specific proposed rescue mechanism is ruled out at the order")
    print("  where it was proposed. The ultimate fate of the completion remains")
    print("  open, and the live candidates are now V!=0 and a nonlinear m(phi).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
