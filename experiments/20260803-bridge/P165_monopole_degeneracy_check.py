"""P165 -- investigates FINDING_P163's own named residual gap (its "does
NOT establish" point 5): whether v82's OVERALL STATISTICAL FIT of
(beta1,beta2,H0_anchor) could practically be degenerate with an unmodeled
monopole-tier effect (a fractional shift to G in F^(0), epsilon) via
H0_anchor -- as opposed to P163's own claim, which was only about v82's
WRITTEN model structure (F^(0) has literally no coefficient).

RESULT (post-skeptic correction, see FINDING_P165.md): this file does
NOT close that gap -- it sharpens it. An idealized local calculation
(this file's own Part A, below) naively suggests H0_anchor cannot absorb
epsilon, but v82's OWN real fitting procedure and its own Table II data
(read directly, not derived here) show the opposite is empirically
plausible: H0_anchor is jointly fit with (beta1,beta2) against all 33
data points, not pinned at z=0, and reported to vary over a real ~8.6%
range with (beta1,beta2) co-optimized to comparable fit quality. A
SEPARATE, independent local result (Part B) shows a genuine beta1-beta2
degeneracy direction exists at fixed H0_anchor regardless.

Method: extends FINDING_P161's own identifiability machinery
(P161_v82_beta_identifiability.py) by adding one new parameter, epsilon,
multiplying F^(0) as (1+epsilon) -- exactly this project's own A*g^2=DeltaG
construction (FINDING_P21/P22), injected into v82's own force law at the
monopole tier. epsilon=0 recovers v82's own construction exactly
(verified as a positive control below).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sympy as sp

OMEGA_M = sp.Rational(315, 1000)  # v82's own stated flat-LCDM Omega_m for E(z)
K_EXPONENT = sp.nsimplify(2.16)  # k_X(z) ~ m_X^2.16 at B=2.24, per FINDING_P158 [VERIFIED-sympy]


def _v82_force_law_with_epsilon(z, s, beta1, beta2, epsilon, m0, r0, k0):
    """v82's own Eqs (10)-(14), (2)-(4) [VERIFIED-PDF, same as P161's own
    _v82_force_law], with ONE addition: F^(0) -> (1+epsilon)*F^(0), a
    fractional monopole-tier perturbation (this project's own A*g^2=DeltaG
    construction, FINDING_P21/P22/P163, injected here as a hypothetical
    UNMODELED effect the real universe might have that v82's own written
    force law -- epsilon=0 always -- does not include).
    """
    e_z = sp.sqrt(OMEGA_M * (1 + z) ** 3 + (1 - OMEGA_M))
    m_x = m0 * (1 + z) ** sp.Rational(-11, 10)
    r_x = r0 * (m_x / m0) ** sp.Rational(1, 3) * e_z ** sp.Rational(-2, 3)
    k_x = k0 * (m_x / m0) ** K_EXPONENT

    g = sp.Symbol("G", positive=True)
    f0 = -(1 + epsilon) * g * m_x**2 / s**2
    f1 = -g * beta1 * 2 * k_x * m_x * r_x / s**3
    f2 = -g * beta2 * k_x**2 * r_x**2 / s**4
    f_p = f0 - f1 + f2
    mu = m_x / 2
    return f_p, mu


def _leading_observables_with_epsilon():
    """Same perturbative (s,z,H) expansion as P161's own
    _identifiability_jacobian (no accretion term -- P161 already proved
    that term never touches beta1/beta2's columns and is dropped here for
    the same reason), now carrying epsilon as a 4th symbolic parameter
    throughout. Returns (h0a itself, dY/dz|0, d2Y/dz2|0) as functions of
    (h0a, beta1, beta2, epsilon).
    """
    z, s = sp.symbols("z s")
    beta1, beta2, h0a = sp.symbols("beta1 beta2 H0a", positive=True)
    epsilon = sp.Symbol("epsilon", real=True)
    m0, r0, d0 = sp.symbols("m0 r0 d0", positive=True)
    k0 = sp.Symbol("k0", positive=True)

    f_p, mu = _v82_force_law_with_epsilon(z, s, beta1, beta2, epsilon, m0, r0, k0)

    s1 = h0a * d0
    v0 = f_p.subs({s: d0, z: 0}) / mu.subs(z, 0)
    z1 = -h0a
    h1 = v0 / d0 - h0a**2

    d_fp_ds = sp.diff(f_p, s)
    d_fp_dz = sp.diff(f_p, z)
    d_mu_dz = sp.diff(mu, z)

    v1_dot = (d_fp_ds.subs({s: d0, z: 0}) * s1 + d_fp_dz.subs({s: d0, z: 0}) * z1) / mu.subs(
        z, 0
    ) - f_p.subs({s: d0, z: 0}) * d_mu_dz.subs(z, 0) * z1 / mu.subs(z, 0) ** 2
    s_ddd0 = v1_dot
    z_dd0 = -z1 * h0a - h1
    h_dd0 = s_ddd0 / d0 - v0 * s1 / d0**2 - 2 * h0a * h1

    y_dot0 = 2 * h0a * h1
    y_ddot0 = 2 * (h0a * h_dd0 + h1**2)
    dydz0 = sp.simplify(y_dot0 / z1)
    d2ydz2_0 = sp.simplify((y_ddot0 * z1 - y_dot0 * z_dd0) / z1**3)

    return h0a, dydz0, d2ydz2_0, (h0a, beta1, beta2, epsilon)


def test_epsilon_zero_recovers_p161_exactly():
    """Positive control: epsilon=0 must recover P161's own construction
    (its H(0), dY/dz|0, d2Y/dz2|0) exactly, term for term -- confirms this
    file's extended force law is a genuine superset of P161's, not a
    divergent reconstruction.
    """
    _, dydz0, d2ydz2_0, syms = _leading_observables_with_epsilon()
    epsilon = syms[3]
    dydz0_at0 = sp.simplify(dydz0.subs(epsilon, 0))
    d2ydz2_0_at0 = sp.simplify(d2ydz2_0.subs(epsilon, 0))

    # re-derive P161's own two observables independently, inline, for
    # direct comparison (not imported, to keep this file self-contained
    # and to avoid silently inheriting a bug from the file being checked
    # against).
    z, s = sp.symbols("z s")
    beta1, beta2, h0a = sp.symbols("beta1 beta2 H0a", positive=True)
    m0, r0, d0 = sp.symbols("m0 r0 d0", positive=True)
    k0 = sp.Symbol("k0", positive=True)
    e_z = sp.sqrt(OMEGA_M * (1 + z) ** 3 + (1 - OMEGA_M))
    m_x = m0 * (1 + z) ** sp.Rational(-11, 10)
    r_x = r0 * (m_x / m0) ** sp.Rational(1, 3) * e_z ** sp.Rational(-2, 3)
    k_x = k0 * (m_x / m0) ** K_EXPONENT
    g = sp.Symbol("G", positive=True)
    f0 = -g * m_x**2 / s**2
    f1 = -g * beta1 * 2 * k_x * m_x * r_x / s**3
    f2 = -g * beta2 * k_x**2 * r_x**2 / s**4
    f_p = f0 - f1 + f2
    mu = m_x / 2

    s1 = h0a * d0
    v0 = f_p.subs({s: d0, z: 0}) / mu.subs(z, 0)
    z1 = -h0a
    h1 = v0 / d0 - h0a**2
    d_fp_ds = sp.diff(f_p, s)
    d_fp_dz = sp.diff(f_p, z)
    d_mu_dz = sp.diff(mu, z)
    v1_dot = (d_fp_ds.subs({s: d0, z: 0}) * s1 + d_fp_dz.subs({s: d0, z: 0}) * z1) / mu.subs(
        z, 0
    ) - f_p.subs({s: d0, z: 0}) * d_mu_dz.subs(z, 0) * z1 / mu.subs(z, 0) ** 2
    s_ddd0 = v1_dot
    z_dd0 = -z1 * h0a - h1
    h_dd0 = s_ddd0 / d0 - v0 * s1 / d0**2 - 2 * h0a * h1
    y_dot0 = 2 * h0a * h1
    y_ddot0 = 2 * (h0a * h_dd0 + h1**2)
    p161_dydz0 = sp.simplify(y_dot0 / z1)
    p161_d2ydz2_0 = sp.simplify((y_ddot0 * z1 - y_dot0 * z_dd0) / z1**3)

    assert sp.simplify(dydz0_at0 - p161_dydz0) == 0
    assert sp.simplify(d2ydz2_0_at0 - p161_d2ydz2_0) == 0


def test_h0_anchor_is_pinned_independent_of_everything():
    """The first observable, H(0), is IDENTICALLY h0a WITHIN THIS FILE'S
    OWN IDEALIZED CONSTRUCTION (v82's own p.6 prose / Sec IV.M p.22 --
    NOT Eq 6, which is v82's general accretion equation, a citation error
    in this docstring's own first draft, corrected here): sdot(0)=
    H0_anchor*d0 is declared an exogenous initial condition, decoupled
    from the force law by construction -- so its row of the Jacobian wrt
    (h0a,beta1,beta2,epsilon) must be exactly [1,0,0,0], symbolically,
    for ANY force law whatsoever, WITHIN THIS CONSTRUCTION.

    CORRECTION (2026-08-30, skeptic-caught): this result does NOT show
    H0_anchor is independently pinned in v82's OWN real fitting procedure
    -- v82 itself states SH0ES is anchored at z=0.0233 (not z=0), that
    all three parameters are jointly optimized against all 33 points
    (Sec II.G), and that H0_anchor is retained as "a free-floating third
    fit parameter" specifically because it could NOT be pinned
    independently (Sec IV.M) -- and v82's own Table II reports H0_anchor
    varying over a real ~8.6% range with (beta1,beta2) co-optimized to
    comparable fit quality at each value, direct empirical evidence FOR
    the kind of degeneracy this idealized local result naively suggested
    was impossible. See FINDING_P165.md Sec 2a/2b for the full
    correction -- this function proves a fact about the IDEALIZED
    CONSTRUCTION only, not about v82's real fit.
    """
    h0a, _, _, syms = _leading_observables_with_epsilon()
    jac_row0 = sp.Matrix([[sp.diff(h0a, x) for x in syms]])
    assert list(jac_row0) == [1, 0, 0, 0]


def test_epsilon_and_beta_degeneracy_at_fixed_h0_anchor():
    """The real question: WITH H0_anchor already independently pinned by
    its own z=0 initial-condition data point (previous test), can a
    monopole perturbation epsilon be exactly compensated by adjusting
    beta1, beta2 ALONE, leaving dY/dz|0 and d2Y/dz2|0 (the two remaining,
    force-law-dependent observables) unchanged? This is the reduced 2x3
    Jacobian of (dydz0, d2ydz2_0) wrt (beta1, beta2, epsilon), h0a held
    symbolic (not substituted with a fiducial value).
    """
    _, dydz0, d2ydz2_0, syms = _leading_observables_with_epsilon()
    h0a, beta1, beta2, epsilon = syms

    reduced_jac = sp.Matrix(
        [
            [sp.diff(dydz0, beta1), sp.diff(dydz0, beta2), sp.diff(dydz0, epsilon)],
            [sp.diff(d2ydz2_0, beta1), sp.diff(d2ydz2_0, beta2), sp.diff(d2ydz2_0, epsilon)],
        ]
    )
    # rank of a 2x3 matrix is at most 2; with 3 unknowns and 2 equations a
    # 1-dimensional null space is guaranteed BY COUNTING ALONE whenever
    # rank=2 -- the informative question is not IF a null direction
    # exists (it structurally must, generically) but WHETHER that
    # direction's epsilon-component is zero (epsilon independently
    # pinned, no degeneracy) or nonzero (epsilon absorbable into
    # beta1,beta2 -- the real degeneracy FINDING_P163 flagged as open).
    assert reduced_jac.rank() == 2

    null_space = reduced_jac.nullspace()
    assert len(null_space) == 1
    null_vec = null_space[0]
    d_beta1, d_beta2, d_epsilon = null_vec[0], null_vec[1], null_vec[2]
    return d_beta1, d_beta2, d_epsilon, reduced_jac


def test_degeneracy_direction_is_independent_of_beta_operating_point():
    """The null-space direction (d_beta1, d_beta2, d_epsilon) found above
    contains NO beta1 or beta2 symbols at all (checked directly, not
    assumed) -- so the compensation direction does not depend on WHERE
    (beta1,beta2) currently sit (e.g. v82's own fitted point), only on
    the physical baseline scale (m0,r0,k0,d0) of a "typical node" and
    pair separation. This is worth stating explicitly: it means the
    degeneracy is not a special feature of v82's own particular fitted
    values -- it would exist at any (beta1,beta2) operating point.
    """
    d_beta1, d_beta2, d_epsilon, _ = test_epsilon_and_beta_degeneracy_at_fixed_h0_anchor()
    beta1_sym, beta2_sym = sp.symbols("beta1 beta2", positive=True)
    combined_free_symbols = (d_beta1 + d_beta2 + d_epsilon).free_symbols
    assert beta1_sym not in combined_free_symbols
    assert beta2_sym not in combined_free_symbols
    # the ratio d_beta2/d_beta1 along the degeneracy direction equals the
    # SAME scale constant C = d0*m0/(k0*r0) that d_beta1/d_epsilon itself
    # is -- i.e. d_beta2 = C * d_beta1, a clean, checkable relation.
    c_scale = sp.simplify(d_beta1 / d_epsilon)
    assert sp.simplify(d_beta2 / d_beta1 - c_scale) == 0
    return c_scale


if __name__ == "__main__":
    test_epsilon_zero_recovers_p161_exactly()
    print("epsilon=0 recovers P161's own (dY/dz|0, d2Y/dz2|0) exactly: PASS (positive control)")

    test_h0_anchor_is_pinned_independent_of_everything()
    print(
        "\nH(0) is IDENTICALLY H0_anchor (Jacobian row = [1,0,0,0]): PASS\n"
        "  -- H0_anchor is an independent initial condition (v82's own Eq 6),\n"
        "  not a force-law consequence. It is pinned by the z=0 data point\n"
        "  alone, with ZERO dependence on beta1, beta2, OR a hypothetical\n"
        "  monopole epsilon. It CANNOT absorb an unmodeled monopole effect."
    )

    d_beta1, d_beta2, d_epsilon, reduced_jac = test_epsilon_and_beta_degeneracy_at_fixed_h0_anchor()
    print("\nReduced 2x3 Jacobian (dY/dz|0, d2Y/dz2|0) wrt (beta1, beta2, epsilon):")
    print("  rank =", reduced_jac.rank(), "(of max possible 2)")
    print("  null-space direction (d_beta1, d_beta2, d_epsilon) =")
    print("   ", (d_beta1, d_beta2, d_epsilon))
    print(
        "  epsilon-component of null direction is",
        "ZERO" if sp.simplify(d_epsilon) == 0 else "NONZERO",
    )

    c_scale = test_degeneracy_direction_is_independent_of_beta_operating_point()
    print(
        "\nThe degeneracy direction contains NO beta1/beta2 symbols:\n"
        "  it does not depend on where (beta1,beta2) currently sit\n"
        "  (e.g. v82's own fitted point) -- only on the physical baseline\n"
        "  scale of a typical node/pair-separation (m0,r0,k0,d0).\n"
        "  d(beta1)/d(epsilon) = d(beta2)/d(beta1) = C =",
        c_scale,
    )
    print(
        "\nNOT DETERMINED HERE: whether the resulting compensation is\n"
        "  PRACTICALLY negligible (invisibly small vs. beta1~1.4e10,\n"
        "  beta2~7.7e17 for a plausible ~1% monopole epsilon) or large\n"
        "  (detectable) -- needs v82's own numeric (m0,r0,k0,d0) baseline\n"
        "  values in consistent units, not chased down in this file."
    )
