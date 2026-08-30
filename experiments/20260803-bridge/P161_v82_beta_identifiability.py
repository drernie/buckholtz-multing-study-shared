"""P161 -- resolves the cross-cutting open item named in FINDING_P159 item 2
and FINDING_P160 item 3 (= docs/150 Sec 6 item 1): are v82's own 3 free fit
parameters (beta1, beta2, H0_anchor) LOCALLY jointly identifiable from the
shape of H(z) near z=0, the way this project's own (A,g,kappa) were found
NOT to be (FINDING_P133, rank(Jacobian)=2<3)?

Method: same Jacobian-rank methodology as FINDING_P133, applied to v82's
own construction. Build H(z)'s Taylor expansion around z=0 by solving the
coupled (s,z,H) system perturbatively in cosmic time t (v82's own Eqs
1-14, 23), extract (H(0), dY/dz|0, d2Y/dz2|0) where Y=H^2, and check the
rank of their Jacobian wrt (H0_anchor, beta1, beta2).

CORRECTION (2026-08-30, context-asymmetric skeptic-caught, round 2): the
first draft's verdict overstated 3 things, all fixed in place, not
silently:
  (a) "det(J) nonzero for any positive constants, not a numerical
      coincidence" was asserted from the clean final formula, without
      proving symbolically that beta1/beta2 never entered a fiducial
      substitution. `test_jacobian_entries_are_symbolically_beta_free`
      below proves it via `.free_symbols`, not observation.
  (b) H0_anchor != 0 is REQUIRED for the t<->z reparametrization (division
      by z1=-H0_anchor at every order) -- physically always true (H>0 in
      an expanding universe) but was an unstated assumption.
  (c) the identity "Hdot = sddot/s - H^2" (v82's own Eq 23) was framed as
      carrying independent physical content "analogous to" the FLRW
      acceleration equation. It does not: given H = sdot/s BY DEFINITION
      in this framework (v82's own Eq 19, "s in place of a"), this
      identity follows from the quotient rule ALONE -- zero new physical
      input beyond the definition of H and the actual equation of motion
      (mu*sddot=F_P) used elsewhere. Corrected in the docstrings below.
  (d) the original draft's "the distinguishing mechanism is radial power,
      NOT z-shape" claim tested only ONE of two needed controls (same
      z-shape + different radial power -> rank 3) and never tested the
      complementary case (different, REAL z-shape + matched radial power).
      `test_z_shape_alone_is_also_sufficient` below runs it: rank 3 as
      well. CONCLUSION CHANGED: both differences are INDEPENDENTLY
      sufficient to produce rank 3; degeneracy requires BOTH to be
      matched simultaneously (confirmed by the original same-shape/
      same-power negative control, still rank 2). Neither mechanism is
      shown to be dominant or necessary on its own.
  (e) the accretion correction (F_acc, Eqs 15-17) was dropped on
      force-BUDGET-share grounds (~0.3-0.4%, Table III) -- a magnitude
      argument applied to a structural (rank) question, which does not
      automatically license the omission, especially since F_acc has a
      SELF-REFERENTIAL dependence on H(z) itself (mdot_X(z)=1.1*H(z)*
      m_X(z), Eq 15-17) that could in principle entangle it with
      H0_anchor differently than expected. `test_accretion_term_does_not_
      change_rank` below re-runs the full calculation WITH F_acc included
      -- determinant is IDENTICAL (F_acc never depends on beta1/beta2 at
      all, so it structurally cannot change their columns of the
      Jacobian; only the H0a column could shift, and the rank is
      unaffected). This is now VERIFIED, not assumed.

SCOPE (still applies, not fixed by the above):
  - LOCAL / leading-order (2nd-order Taylor near z=0) only -- NOT a full
    numerical fit against all 33 of v82's own data points across its real
    z-range (0.07-2.33). A leading-order rank-3 result does not rule out
    a near-degeneracy (formally rank 3, but a very small singular value)
    that only a full numerical treatment would reveal.
  - Both nodes in the pair (A, P) are treated as identical "typical"
    nodes (m_A=m_P=m_X(z), etc.) -- matching the "typical object" framing
    of v82's own Sec II.D and IV.H.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sympy as sp

OMEGA_M = sp.Rational(315, 1000)  # v82's own stated flat-LCDM Omega_m for E(z)
K_EXPONENT = sp.nsimplify(2.16)  # k_X(z) ~ m_X^2.16 at B=2.24, per FINDING_P158 [VERIFIED-sympy]


def _v82_force_law(z, s, beta1, beta2, m0, r0, k0):
    """v82's own Eqs (10)-(14) [VERIFIED-PDF pp.6-7] and Eqs (2)-(4)
    [VERIFIED-PDF p.4-5], both nodes identical, NO accretion correction
    (see `_v82_force_law_with_accretion` for that extension).
    Returns (F_P, mu_reduced) as functions of z (symbolic) at separation s.
    """
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
    return f_p, mu


def _identifiability_jacobian(force_law_builder, with_accretion=False):
    """Solve the coupled (s,z,H) system perturbatively to 2nd order in
    cosmic time t around t=0, extract (H(0), dY/dz|0, d2Y/dz2|0) with
    Y=H^2, and return the 3x3 Jacobian wrt (H0_anchor, beta1, beta2).

    Requires H0_anchor != 0 (division by z1=-H0_anchor at every order of
    the t<->z reparametrization) -- always true physically (H>0 in an
    expanding universe), stated here as an explicit precondition.

    Eq 23 (Hdot = sddot/s - H^2) used below is not independent physical
    input -- given H=sdot/s by definition (v82's own Eq 19), it is the
    quotient-rule consequence of that definition alone. All physical
    content is in mu*sddot=F_P (the actual equation of motion) and
    dz/dt=-(1+z)H (the standard kinematic redshift relation).
    """
    z, s = sp.symbols("z s")
    beta1, beta2, h0a = sp.symbols("beta1 beta2 H0a", positive=True)
    m0, r0, d0 = sp.symbols("m0 r0 d0", positive=True)
    k0 = sp.Symbol("k0", positive=True)

    f_p, mu = force_law_builder(z, s, beta1, beta2, m0, r0, k0)

    if not with_accretion:
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
    else:
        # accretion correction [VERIFIED-PDF Eqs 15-17, p.8]: mdot_X(z)=
        # 1.1*H(z)*m_X(z), v_infall=sqrt(G*m_X/r_X), Delta_v_coh=f_coh*
        # f_merge*v_infall, F_acc=mdot_X*Delta_v_coh -- explicitly depends
        # on H(z) itself (a self-referential coupling), not just on z
        # through m_X(z)/r_X(z) as F_P does.
        m_x = m0 * (1 + z) ** sp.Rational(-11, 10)
        r_x = (
            r0
            * (m_x / m0) ** sp.Rational(1, 3)
            * sp.sqrt(OMEGA_M * (1 + z) ** 3 + (1 - OMEGA_M)) ** sp.Rational(-2, 3)
        )
        g = sp.Symbol("G", positive=True)
        fcoh, fmerge = sp.symbols("f_coh f_merge", positive=True)
        hval = sp.Symbol("Hval", positive=True)  # H(z) treated as an explicit input
        f_acc_expl = sp.Rational(11, 10) * hval * m_x * fcoh * fmerge * sp.sqrt(g * m_x / r_x)

        f_acc_at0 = f_acc_expl.subs({z: 0, hval: h0a})
        s1 = h0a * d0
        v0 = (f_p.subs({s: d0, z: 0}) - f_acc_at0) / mu.subs(z, 0)
        z1 = -h0a
        h1 = v0 / d0 - h0a**2

        d_fp_ds = sp.diff(f_p, s)
        d_fp_dz = sp.diff(f_p, z)
        d_facc_dz = sp.diff(f_acc_expl, z).subs({z: 0, hval: h0a})
        d_facc_dh = sp.diff(f_acc_expl, hval).subs(z, 0)
        d_mu_dz = sp.diff(mu, z)

        d_fp_dt0 = d_fp_ds.subs({s: d0, z: 0}) * s1 + d_fp_dz.subs({s: d0, z: 0}) * z1
        d_facc_dt0 = d_facc_dz * z1 + d_facc_dh * h1

        v1_dot = (d_fp_dt0 - d_facc_dt0) / mu.subs(z, 0) - (
            f_p.subs({s: d0, z: 0}) - f_acc_at0
        ) * d_mu_dz.subs(z, 0) * z1 / mu.subs(z, 0) ** 2
        s_ddd0 = v1_dot
        z_dd0 = -z1 * h0a - h1
        h_dd0 = s_ddd0 / d0 - v0 * s1 / d0**2 - 2 * h0a * h1

    y_dot0 = 2 * h0a * h1
    y_ddot0 = 2 * (h0a * h_dd0 + h1**2)
    dydz0 = sp.simplify(y_dot0 / z1)
    d2ydz2_0 = sp.simplify((y_ddot0 * z1 - y_dot0 * z_dd0) / z1**3)

    f_vec = [h0a, dydz0, d2ydz2_0]
    x_vec = [h0a, beta1, beta2]
    jac = sp.Matrix([[sp.diff(f, x) for x in x_vec] for f in f_vec])
    return jac


def test_negative_control_matched_shape_and_power_is_degenerate():
    """Grid cell (same z-shape, same radial power): F^(1), F^(2) forced to
    share both the same z-shape AND the same radial (1/s) power -- a
    synthetic, non-physical construction, not v82's own. beta1, beta2 can
    then only ever be constrained through a single combination. The
    Jacobian-rank method MUST report rank 2, or the methodology is broken.
    """

    def degenerate_force_law(z, s, beta1, beta2, m0, r0, k0):
        m_x = m0 * (1 + z) ** sp.Rational(-11, 10)
        x_z = m_x**2
        g = sp.Symbol("G", positive=True)
        f0 = -g * m_x**2 / s**2
        f1 = -g * beta1 * 2 * x_z / s**3
        f2 = -g * beta2 * x_z / s**3  # same 1/s^3 power as f1 (not v82's real 1/s^4)
        return f0 - f1 + f2, m_x / 2

    jac = _identifiability_jacobian(degenerate_force_law)
    assert sp.simplify(jac.det()) == 0
    assert jac.rank() == 2


def test_radial_power_alone_is_sufficient():
    """Grid cell (same z-shape, DIFFERENT real radial power): isolates
    whether radial-power difference alone (with z-shape matched) suffices.
    """

    def same_shape_real_power(z, s, beta1, beta2, m0, r0, k0):
        m_x = m0 * (1 + z) ** sp.Rational(-11, 10)
        x_z = m_x**2
        g = sp.Symbol("G", positive=True)
        f0 = -g * m_x**2 / s**2
        f1 = -g * beta1 * 2 * x_z / s**3
        f2 = -g * beta2 * x_z / s**4  # v82's own real quadrupole power
        return f0 - f1 + f2, m_x / 2

    jac = _identifiability_jacobian(same_shape_real_power)
    assert jac.rank() == 3


def test_z_shape_alone_is_also_sufficient():
    """Grid cell (DIFFERENT real z-shape, same radial power): the missing
    complementary control a skeptic flagged as absent from the first
    draft. Uses v82's own real m_X(z)/r_X(z)/k_X(z) exponents (genuinely
    different z-shapes for F1 vs F2) but FORCES both to the same 1/s^3
    radial power (not v82's real 1/s^4 for the quadrupole).
    """

    def real_shape_matched_power(z, s, beta1, beta2, m0, r0, k0):
        e_z = sp.sqrt(OMEGA_M * (1 + z) ** 3 + (1 - OMEGA_M))
        m_x = m0 * (1 + z) ** sp.Rational(-11, 10)
        r_x = r0 * (m_x / m0) ** sp.Rational(1, 3) * e_z ** sp.Rational(-2, 3)
        k_x = k0 * (m_x / m0) ** K_EXPONENT
        g = sp.Symbol("G", positive=True)
        f0 = -g * m_x**2 / s**2
        f1 = -g * beta1 * 2 * k_x * m_x * r_x / s**3
        f2 = -g * beta2 * k_x**2 * r_x**2 / s**3  # matched to f1's power (not real 1/s^4)
        return f0 - f1 + f2, m_x / 2

    jac = _identifiability_jacobian(real_shape_matched_power)
    assert jac.rank() == 3


def test_v82_own_construction_locally_identifiable():
    """The actual result (grid cell: real different z-shape AND real
    different radial power, v82's own construction as written).
    """
    jac = _identifiability_jacobian(_v82_force_law)
    det = sp.simplify(jac.det())
    assert det != 0
    assert jac.rank() == 3
    return jac, det


def test_jacobian_entries_are_symbolically_beta_free():
    """Proves (not just observes from the clean final determinant) that
    beta1, beta2 genuinely do not appear in ANY Jacobian entry -- i.e.
    the independence is an exact symbolic fact, not an artifact of
    substituting a fiducial (beta1,beta2,H0_anchor) point anywhere in the
    derivation (no such substitution is ever made in this file).
    """
    beta1, beta2 = sp.symbols("beta1 beta2", positive=True)
    jac = _identifiability_jacobian(_v82_force_law)
    for i in range(3):
        for j in range(3):
            entry_symbols = jac[i, j].free_symbols
            assert beta1 not in entry_symbols
            assert beta2 not in entry_symbols


def test_accretion_term_does_not_change_rank():
    """Re-runs the full calculation WITH the self-referential accretion
    correction (F_acc, depends on H(z) itself) included, rather than
    dismissing it on force-budget-share grounds alone. F_acc never
    depends on beta1/beta2 (it has no k_A/k_P/dipole-type dependence at
    all), so it structurally cannot alter their Jacobian columns --
    verified here, not assumed.
    """
    jac_with = _identifiability_jacobian(_v82_force_law, with_accretion=True)
    jac_without = _identifiability_jacobian(_v82_force_law, with_accretion=False)
    assert sp.simplify(jac_with.det() - jac_without.det()) == 0
    assert jac_with.rank() == 3


if __name__ == "__main__":
    test_negative_control_matched_shape_and_power_is_degenerate()
    print("Grid (same z-shape, same radial power):      rank=2, det=0  [degenerate control, PASS]")

    test_radial_power_alone_is_sufficient()
    print("Grid (same z-shape, DIFFERENT radial power):  rank=3         [PASS]")

    test_z_shape_alone_is_also_sufficient()
    print(
        "Grid (DIFFERENT z-shape, same radial power):  rank=3         [PASS -- was the missing control]"
    )

    jac, det = test_v82_own_construction_locally_identifiable()
    print("Grid (DIFFERENT z-shape, DIFFERENT radial power = v82's own):")
    print("  det(J) =", det)
    print("  rank(J) =", jac.rank())

    test_jacobian_entries_are_symbolically_beta_free()
    print("\nAll 9 Jacobian entries proven free of beta1, beta2 via .free_symbols: PASS")

    test_accretion_term_does_not_change_rank()
    print(
        "Accretion term (self-referential H(z) coupling) included: det(J) UNCHANGED, rank=3: PASS"
    )

    print(
        "\nConclusion: EITHER z-shape difference OR radial-power difference alone\n"
        "suffices for local identifiability; degeneracy requires BOTH matched\n"
        "simultaneously. Neither mechanism is individually necessary or dominant."
    )
