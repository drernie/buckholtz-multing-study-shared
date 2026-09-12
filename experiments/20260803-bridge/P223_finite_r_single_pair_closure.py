"""P223_finite_r_single_pair_closure.py -- symbolic check of CLAIM_P223's
H1/H2/H3. Reuses v82's own primary-source equations (Eqs 1-9, read
directly this session from `data/source_material/buckholtz_202608.0943v1.
v82.md` lines 226-320) and `docs/127`'s own S-S background-closure method
(`G_eff = G * lim_{r->inf}[f(r) - r f'(r)]`, `phi(r) = -(G/r) f(r)`).

H1 -- does v82's own single-pair bridge (Eqs 1-4, 7, 8) keep
     k_A(z)-dependent terms in a_ddot/a, with no algebraic cancellation?
H2 -- does the SAME F^(1)/F^(2) power laws (1/s^3, 1/s^4), run through
     docs/127's own population-averaged S-S closure method, reproduce
     G_alpha_beta = 0 exactly (must match docs/127's own published
     result bit-for-bit, or this script's own re-implementation is
     wrong)?
H3 -- synthesis, printed only (not a separate symbolic step): H1+H2
     together show v82's bridge and docs/127's closure answer different
     mathematical questions about the same force law -- one pair's own
     finite s(z) trajectory (never taken to infinity) vs. the
     r-> infinity behavior of the S-S convolution's OWN integration
     variable (a population coordinate, unrelated to v82's s(z)).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR
"""

from __future__ import annotations

import sympy as sp

# ---- symbols, matching v82's own notation (Eqs 1-4) ------------------------
G, c, s, r = sp.symbols("G c s r", positive=True)
m_A, m_P, k_A, k_P, r_A, r_P = sp.symbols("m_A m_P k_A k_P r_A r_P", positive=True)
beta_1, beta_2 = sp.symbols("beta_1 beta_2", positive=True)
mu_reduced = sp.symbols("mu_reduced", positive=True)


def v82_force_terms() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Eqs (1)-(4), verbatim from the primary source."""
    F0 = -G * m_A * m_P / s**2
    F1 = -G * beta_1 * c**-2 * (k_A * m_P * r_A + m_A * k_P * r_P) / s**3
    F2 = -G * beta_2 * c**-4 * (k_A * k_P * r_A * r_P) / s**4
    F_P = F0 - F1 + F2  # Eq (1)
    return F0, F1, F2, F_P


def h1_check_no_cancellation() -> None:
    """H1: a_ddot/a = s_ddot(z)/s(z) [Eq 8], with mu_reduced*s_ddot = F_P
    [Eq 7, accretion-correction bracket set to 0 -- the Eq (5) special
    case, u_P=u_A=v_P=v_A -- since the accretion term is additive and
    does not depend on k_A/k_P, it cannot be the source of any
    cancellation of the multipole terms and is set aside to isolate the
    force-law question this claim is actually about].
    """
    print("=" * 78)
    print("H1 -- does v82's own bridge keep k_A(z)-dependence in a_ddot/a?")
    print("=" * 78)
    F0, F1, F2, F_P = v82_force_terms()
    print(f"\nF^(0) = {F0}")
    print(f"F^(1) = -({-F1})  [Eq 3, note Eq(1)'s own minus sign already applied]")
    print(f"F^(2) = {F2}")
    print(f"F_P = F^(0) - F^(1) + F^(2) = {sp.simplify(F_P)}")

    s_ddot = F_P / mu_reduced  # Eq (7), accretion=0
    a_ddot_over_a = s_ddot / s  # Eq (8)
    a_ddot_over_a = sp.simplify(a_ddot_over_a)
    print(f"\na_ddot/a = F_P / (mu_reduced * s) = {a_ddot_over_a}")

    # Isolate each term's own s-power and physical-parameter dependence
    terms = sp.Add.make_args(sp.expand(a_ddot_over_a))
    print(f"\nExpanded into {len(terms)} additive terms (distinct s-powers):")
    for t in terms:
        _, power = t.as_coeff_exponent(s)
        depends_on_k = t.has(k_A) or t.has(k_P)
        print(f"  s^{int(power):+d} term, k_A/k_P-dependent={depends_on_k}: {t}")

    # The actual H1 claim: setting k_A=k_P=0 must NOT reproduce the full
    # expression (i.e. the k-dependent terms are not already absorbed
    # into / cancelled by the monopole term).
    monopole_only = a_ddot_over_a.subs({k_A: 0, k_P: 0})
    full_minus_monopole = sp.simplify(a_ddot_over_a - monopole_only)
    survives = full_minus_monopole != 0
    print(f"\nmonopole-only (k_A=k_P=0):        {monopole_only}")
    print(f"full - monopole-only (k-terms):   {full_minus_monopole}")
    print(f"H1 VERDICT: k-dependent terms {'SURVIVE (nonzero)' if survives else 'CANCEL (zero)'}")
    print(
        "  -- matches FINDING_P156's own Table IIIa reading (k-tiers dominate\n"
        "     96-99.65% of v82's own published force budget) if SURVIVE."
    )
    assert survives, "H1 FALSIFIED: k-dependent terms cancel -- contradicts Table IIIa"


def g_alpha_beta(f_of_r: sp.Expr) -> sp.Expr:
    """docs/127's own method: phi(r) = -(G/r) f(r); G_eff contribution
    = G * lim_{r->inf} [f(r) - r * f'(r)]."""
    return G * sp.limit(f_of_r - r * sp.diff(f_of_r, r), r, sp.oo)


def h2_reproduce_docs127() -> None:
    """H2: map each v82 force power-law F(s) ~ 1/s^n onto docs/127's own
    f(r) convention (phi ~ 1/s^(n-1), f(r) ~ 1/r^(n-2)) and recompute
    G_alpha_beta for n=2,3,4 -- must reproduce docs/127's own table
    (monopole: G, dipole: 0, quadrupole: 0) exactly."""
    print("\n" + "=" * 78)
    print("H2 -- re-derive docs/127's G_alpha_beta for v82's own n=2,3,4 power laws")
    print("=" * 78)
    results = {}
    for n, label in [
        (2, "monopole F^(0) ~ 1/s^2"),
        (3, "dipole F^(1) ~ 1/s^3"),
        (4, "quadrupole F^(2) ~ 1/s^4"),
    ]:
        f_of_r = r ** (-(n - 2)) if n > 2 else sp.Integer(1)
        g_ab = g_alpha_beta(f_of_r)
        results[n] = g_ab
        print(f"  {label}: f(r) = {f_of_r}  ->  G_alpha_beta = {g_ab}")

    print("\ndocs/127's own published table (for comparison, not re-derived here):")
    print("  monopole: G   | dipole: 0   | quadrupole: 0")
    match = results[2] == G and results[3] == 0 and results[4] == 0
    print(
        f"\nH2 VERDICT: {'REPRODUCED exactly' if match else 'MISMATCH -- investigate before trusting anything downstream'}"
    )
    assert match, "H2 FALSIFIED: does not reproduce docs/127's own published G_alpha_beta table"


def h3_synthesis() -> None:
    print("\n" + "=" * 78)
    print("H3 -- synthesis (interpretive, not a separate symbolic derivation)")
    print("=" * 78)
    print(
        "H1 confirmed: v82's OWN s(z) -- one specific pair's own separation,\n"
        "  staying finite (~tens of Mpc) throughout cosmic history, NEVER taken\n"
        "  to infinity anywhere in Eqs (1)-(9) -- keeps k_A(z)-dependent force\n"
        "  terms with no cancellation mechanism.\n"
        "H2 confirmed: docs/127's r->infinity limit is over a DIFFERENT variable\n"
        "  entirely -- the S-S convolution's own integration coordinate (a\n"
        "  population coordinate: how far a background source sits from a test\n"
        "  point), asking how much a population of DISTANT sources contributes\n"
        "  to the mean background field. It is not a statement about how large\n"
        "  v82's own pair separation s(z) can be.\n"
        "H3: H1 and H2 are therefore not in contradiction -- they answer two\n"
        "  distinct mathematical questions about the same microscopic force law:\n"
        "  (a) one pair's own deterministic trajectory (v82, H1) vs.\n"
        "  (b) the r->infinity tail-contribution of an isotropic population's\n"
        "      convolution integral (docs/127's S-S closure, H2).\n"
        "docs/153 SS0's causal-compatibility question answered: CATEGORICALLY\n"
        "  SEPARATE -- docs/127's G_eff=0 result does not constrain v82's bridge\n"
        "  construction one way or the other, not because the comparison is\n"
        "  unfinished, but because the two routes are different questions about\n"
        "  the same underlying force law's own multipole structure."
    )


def main() -> None:
    h1_check_no_cancellation()
    h2_reproduce_docs127()
    h3_synthesis()


if __name__ == "__main__":
    main()
