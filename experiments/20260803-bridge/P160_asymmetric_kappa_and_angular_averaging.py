"""P160 -- closes the two remaining open items FINDING_P159 named but did
not test: (1) does asymmetric coupling (kappa_A != kappa_P) between the
two nodes preserve MULTING's own dipole functional form; (2) is there a
free orientation angle in MULTING's own two-body dipole construction that
would require averaging (as opposed to P157/P158's separate, POPULATION-
level averaging question, which this file does not touch).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sympy as sp


def _dipole_and_quad_coefficients(kappa_a, kappa_p):
    """Re-run two_charge_completion.py's own mirror-symmetric derivation
    [VERIFIED-file] with the charge substitution generalized to allow
    kappa_A != kappa_P (the original file used a single shared kappa).
    Returns (C3, C4) -- the dipole and quadrupole tier coefficients.
    """
    r, dA, dB = sp.symbols("r d_A d_B", positive=True)
    mA, mB, qA, qB = sp.symbols("m_A m_B q_A q_B", real=True)

    def interaction(sign_a, sign_b):
        a_charges = [(mA, 0), (sign_a * qA, dA / 2), (-sign_a * qA, -dA / 2)]
        b_charges = [(mB, r), (sign_b * qB, r + dB / 2), (-sign_b * qB, r - dB / 2)]
        return sum(sa * sb / (zb - za) for sa, za in a_charges for sb, zb in b_charges)

    def series_uf(u):
        eps = sp.Symbol("eta", positive=True)
        us = u.subs({dA: eps * dA, dB: eps * dB})
        us = sp.series(us, eps, 0, 3).removeO().subs(eps, 1)
        us = sp.simplify(sp.expand(us))
        return us, sp.simplify(-sp.diff(us, r))

    _, f_sym = series_uf(interaction(+1, -1))  # the mirror-symmetric config
    fs = sp.expand(f_sym)
    B3, B4 = -fs.coeff(r, -3), fs.coeff(r, -4)

    kA, kP, rA, rP, cc = sp.symbols("k_A k_P r_A r_P c", positive=True)
    subs = {qA: -kappa_a * kA / cc**2, qB: -kappa_p * kP / cc**2, dA: rA, dB: rP}
    C3 = sp.simplify(B3.subs(subs))
    C4 = sp.simplify(B4.subs(subs))
    return C3, C4


def test_symmetric_kappa_matches_multing_form():
    """Positive control: kappa_A=kappa_P=kappa must recover the original
    file's own result exactly. Note: m_A, m_B must be declared `real=True`
    here, matching `_dipole_and_quad_coefficients`'s own internal
    declaration -- sympy treats Symbol('m_A', real=True) and
    Symbol('m_A', positive=True) as distinct objects, so a mismatched
    assumption here would make an algebraically-equal expression fail to
    simplify to 0 (caught by this test itself on first run).
    """
    kappa = sp.Symbol("kappa", positive=True)
    C3, C4 = _dipole_and_quad_coefficients(kappa, kappa)
    kA, kP, rA, rP, cc = sp.symbols("k_A k_P r_A r_P c", positive=True)
    mA, mB = sp.symbols("m_A m_B", real=True)
    expected_C3 = 2 * kappa * (kA * mB * rA + kP * mA * rP) / cc**2
    expected_C4 = 6 * kappa**2 * kA * kP * rA * rP / cc**4
    assert sp.simplify(C3 - expected_C3) == 0
    assert sp.simplify(C4 - expected_C4) == 0


def test_asymmetric_kappa_breaks_multing_dipole_form():
    """Does kappa_A != kappa_P still give a force expressible as a SINGLE
    coefficient times MULTING's own symmetric combination
    (k_A*m_P*r_A + k_P*m_A*r_P)? v6/v82's own Eq 15/Eq 3 write exactly one
    beta_d (beta1) multiplying that whole symmetric sum -- not two
    separate per-node coefficients.
    """
    kappa_a, kappa_p = sp.symbols("kappa_A kappa_P", positive=True)
    C3, C4 = _dipole_and_quad_coefficients(kappa_a, kappa_p)

    # m_A, m_B must be `real=True` to match _dipole_and_quad_coefficients's
    # own internal declaration (see the comment in the positive-control
    # test above) -- otherwise .coeff() silently fails to match at all.
    kA, kP, rA, rP, cc = sp.symbols("k_A k_P r_A r_P c", positive=True)
    mA, mB = sp.symbols("m_A m_B", real=True)
    # C3 must be a LINEAR COMBINATION of the two symmetric terms with a
    # SINGLE shared coefficient for MULTING's own form to hold. .expand()
    # first -- .coeff() does not look inside an un-expanded factored form
    # like "2*(term1 + term2)/c**2".
    C3_expanded = sp.expand(C3)
    coeff_kA_term = sp.simplify(C3_expanded.coeff(kA * mB * rA))
    coeff_kP_term = sp.simplify(C3_expanded.coeff(kP * mA * rP))
    assert sp.simplify(coeff_kA_term - 2 * kappa_a / cc**2) == 0
    assert sp.simplify(coeff_kP_term - 2 * kappa_p / cc**2) == 0
    # the two coefficients are EQUAL iff kappa_A == kappa_P -- asymmetric
    # coupling gives two DIFFERENT coefficients, which MULTING's own
    # single-beta_d equation cannot represent unless kappa_A=kappa_P.
    are_equal_only_if_symmetric = sp.simplify(coeff_kA_term - coeff_kP_term)
    assert sp.simplify(are_equal_only_if_symmetric - 2 * (kappa_a - kappa_p) / cc**2) == 0

    # quadrupole tier: robust, since it depends only on the PRODUCT
    # kappa_A*kappa_P, which is well-defined even if kappa_A != kappa_P.
    expected_C4 = 6 * kappa_a * kappa_p * kA * kP * rA * rP / cc**4
    assert sp.simplify(C4 - expected_C4) == 0


if __name__ == "__main__":
    test_symmetric_kappa_matches_multing_form()
    print("Symmetric kappa_A=kappa_P recovers two_charge_completion.py's own")
    print("original result exactly: PASS (positive control)")

    test_asymmetric_kappa_breaks_multing_dipole_form()
    print("\nAsymmetric kappa_A != kappa_P:")
    print("  dipole tier -- gives TWO separate coefficients (2*kappa_A/c^2,")
    print("  2*kappa_P/c^2) on the k_A and k_P terms respectively. MULTING's")
    print("  own Eq 15/Eq 3 write ONE beta_d for the whole symmetric sum --")
    print("  asymmetric kappa is NOT expressible in that form unless")
    print("  kappa_A=kappa_P. Symmetric kappa is REQUIRED by MULTING's own")
    print("  written equations, not merely assumed for convenience.")
    print("  quadrupole tier -- ROBUST: depends only on kappa_A*kappa_P,")
    print("  a well-defined product regardless of the individual values.")

    print("\nAngular averaging: resolved by direct primary-source reading,")
    print("not computation -- see FINDING_P160 Sec 2 (v82 p.17, Sec IV.F).")
