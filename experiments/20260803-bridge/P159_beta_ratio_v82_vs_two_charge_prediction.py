"""P159 -- compares v82's fitted beta1/beta2 (Eqs. 2-4) against this project's
own derived beta_d=2, beta_q=sqrt(6) (two_charge_completion.py). Establishes,
via dimensional analysis of v82's own printed equations plus v6's own defining
relations (rdA=beta_d*rA, |rqAB|^2=(beta_q)^2*rA*rP), that the structurally
correct, unit-independent comparison is a RATIO (beta_q/beta_d vs
sqrt(beta2)/beta1), not a raw magnitude comparison.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sympy as sp


def test_v82_beta1_beta2_are_dimensionless():
    """v82 Eqs. (2)-(4) [VERIFIED-PDF p.4-5]:
      F0 = -G mA mP / s^2
      F1 = beta1*(-G kA c^-2 mP rA/s^3) + beta1*(-G mA kP c^-2 rP/s^3)
      F2 = beta2*(-G kA kP c^-4 rA rP/s^4)
    Using symbolic units (M=mass, L=length, T=time, E=energy=M L^2 T^-2),
    verify each equation is dimensionally complete in force (M L T^-2)
    WITHOUT beta1/beta2 contributing any dimension -- i.e. both are true
    dimensionless numbers by construction, independent of unit system.
    """
    M, ln, T = sp.symbols("M L T", positive=True)  # mass, length, time dims
    G_dim = ln**3 / (M * T**2)
    c_dim = ln / T
    energy_dim = M * ln**2 / T**2  # k_A, k_P are "thermal energy"
    force_dim = M * ln / T**2

    f0_dim = G_dim * M * M / ln**2
    assert sp.simplify(f0_dim - force_dim) == 0

    f1_term_dim = G_dim * energy_dim * (1 / c_dim**2) * M * ln / ln**3
    assert sp.simplify(f1_term_dim - force_dim) == 0

    f2_dim = G_dim * energy_dim**2 * (1 / c_dim**4) * ln**2 / ln**4
    assert sp.simplify(f2_dim - force_dim) == 0
    # All three checks pass with beta1, beta2 absent from the dimensional
    # bookkeeping entirely -- confirming both are dimensionless.


def test_our_kernel_matches_v82_term_structure():
    """factorization_gate.py's own kernel (kappa_mm=G, kappa_mq=G*beta_d/c^2,
    kappa_qq=G*beta_q^2/c^4) [VERIFIED-file, scripts/factorization_gate.py
    lines 41,65] reproduces v82's own printed force terms EXACTLY under the
    substitution beta_d -> beta1, beta_q^2 -> beta2 -- i.e. beta1 corresponds
    to beta_d DIRECTLY (linear), beta2 corresponds to beta_d_q SQUARED.
    """
    G, c, beta1, beta2 = sp.symbols("G c beta1 beta2", positive=True)
    kA, kP, mA, mP, rA, rP, s = sp.symbols("kA kP mA mP rA rP s", positive=True)

    # v82's own printed F1, F2 [VERIFIED-PDF p.4-5], no extraneous factor of 2
    f1_v82 = beta1 * (-G * kA / c**2 * mP * rA / s**3) + beta1 * (-G * mA * kP / c**2 * rP / s**3)
    f2_v82 = beta2 * (-G * kA * kP / c**4 * rA * rP / s**4)

    # our own factorization_gate.py kernel, B_rec/C_rec [VERIFIED-file], with
    # q_i = k_i r_i, evaluated at r=s
    kappa_mq = G * beta1 / c**2  # substituting beta_d -> beta1 (the claim)
    kappa_qq = G * beta2 / c**4  # substituting beta_q^2 -> beta2 (the claim)
    f1_ours = -kappa_mq * (mA * kP * rP + mP * kA * rA) / s**3
    f2_ours = -kappa_qq * (kA * rA) * (kP * rP) / s**4

    assert sp.simplify(f1_v82 - f1_ours) == 0
    assert sp.simplify(f2_v82 - f2_ours) == 0


def test_v6_raw_equations_independently_match_v82():
    """Round-2 fix (skeptic-caught circularity in Round 1): compare v82's
    own Eqs (2)-(4) not against OUR kernel (factorization_gate.py, which
    was itself built by substituting v6's Eqs 18-20 into a template --
    not independent), but against v6's own RAW Eqs (14)-(17)
    [VERIFIED-grep, v6 lines 780-811], BEFORE v6's own Eqs (18)-(20)
    substitute beta_d, beta_q in. Two genuinely separate primary sources.
    """
    G, c, beta_d, beta_q, beta1, beta2 = sp.symbols("G c beta_d beta_q beta1 beta2", positive=True)
    kA, kP, mA, mP, rA, rP, r = sp.symbols("kA kP mA mP rA rP r", positive=True)

    Fm = mA * mP / r**2
    # v6's raw Eqs 14-16 (G folded out, ratio to Fm taken) then its own
    # Eq 18-20 substitution: r_dA=beta_d*rA, r_dP=beta_d*rP, r_qAB^2=beta_q^2*rA*rP
    Fd_over_Fm_v6 = sp.simplify(
        (kA / c**2 * mP * (beta_d * rA) / r**3 + kP / c**2 * mA * (beta_d * rP) / r**3) / Fm
    )
    Fq_over_Fm_v6 = sp.simplify((kA * kP / c**4 * (beta_q**2 * rA * rP) / r**4) / Fm)

    # v82's own Eqs 2-4, directly [VERIFIED-PDF p.4-5]
    Fd_over_Fm_v82 = sp.simplify(
        (beta1 * (kA / c**2 * mP * rA / r**3 + mA * kP / c**2 * rP / r**3)) / Fm
    )
    Fq_over_Fm_v82 = sp.simplify((beta2 * kA * kP / c**4 * rA * rP / r**4) / Fm)

    assert sp.simplify(Fd_over_Fm_v6.subs(beta_d, beta1) - Fd_over_Fm_v82) == 0
    assert sp.simplify(Fq_over_Fm_v6.subs(beta_q, sp.sqrt(beta2)) - Fq_over_Fm_v82) == 0


def test_kappa_cancels_in_ratio():
    """Resolves the second Round-1 gap: two_charge_completion.py's own
    kappa (an undetermined normalization, never assigned a value/dimension
    anywhere in this project) enters beta_d, beta_q identically and
    cancels exactly in their ratio -- confirmed by matching the
    two-point-charge construction's own tiers against v6's RAW (pre-Eq
    18-20) force law and solving for beta_d, beta_q in terms of kappa.
    """
    kappa, beta_d, beta_q = sp.symbols("kappa beta_d beta_q", positive=True)
    kA, kP, mA, mP, rA, rP, c = sp.symbols("kA kP mA mP rA rP c", positive=True)

    uA = kappa * kA * rA / (c**2 * mA)
    uB = kappa * kP * rP / (c**2 * mP)
    ell_d = 2 * (uA + uB)  # two_charge_completion.py's own verified result
    ell_q2 = 6 * uA * uB

    lhs_d = beta_d * (kA * rA / (c**2 * mA) + kP * rP / (c**2 * mP))
    sol_beta_d = sp.solve(sp.Eq(lhs_d, ell_d), beta_d)[0]
    lhs_q2 = beta_q**2 * (kA * kP * rA * rP / (c**4 * mA * mP))
    sol_beta_q = sp.sqrt(sp.solve(sp.Eq(lhs_q2, ell_q2), beta_q**2)[0])

    assert sp.simplify(sol_beta_d - 2 * kappa) == 0
    assert sp.simplify(sol_beta_q - kappa * sp.sqrt(6)) == 0

    ratio = sp.simplify(sol_beta_q / sol_beta_d)
    assert sp.simplify(ratio - sp.sqrt(6) / 2) == 0
    return sol_beta_d, sol_beta_q, ratio


def test_ratio_comparison():
    """The unit-independent, structurally-correct comparison: our own
    derived (not fitted) ratio beta_q/beta_d = sqrt(6)/2 (kappa-independent,
    per test_kappa_cancels_in_ratio), versus v82's own fitted analog
    sqrt(beta2)/beta1 [VERIFIED-PDF, Table II best-fit row, beta1~1.4e10,
    beta2~7.7e17, per docs/149].
    """
    beta1_v82 = 1.4e10
    beta2_v82 = 7.7e17
    ratio_v82 = beta2_v82**0.5 / beta1_v82

    ratio_ours = float(sp.sqrt(6) / 2)

    discrepancy = ratio_ours / ratio_v82
    assert 18 < discrepancy < 21  # sanity band around the ~19.5x found
    return ratio_ours, ratio_v82, discrepancy


if __name__ == "__main__":
    test_v82_beta1_beta2_are_dimensionless()
    print("v82's own Eqs (2)-(4) are dimensionally complete without beta1/beta2")
    print("carrying dimension -- both are TRUE dimensionless numbers: PASS")

    test_our_kernel_matches_v82_term_structure()
    print("\nOur own kernel (factorization_gate.py) matches v82's printed F1/F2")
    print("exactly under beta_d->beta1 (linear), beta_q^2->beta2 (squared): PASS")
    print("(Round 1 -- later found circular, see test below)")

    test_v6_raw_equations_independently_match_v82()
    print("\nv6's own RAW Eqs 14-17 (pre-beta_d/beta_q substitution), matched")
    print("independently against v82's own Eqs 2-4: EXACT MATCH (Round 2, non-circular): PASS")

    sol_beta_d, sol_beta_q, ratio = test_kappa_cancels_in_ratio()
    print(f"\nkappa resolution: beta_d(TJB) = {sol_beta_d}, beta_q(TJB) = {sol_beta_q}")
    print(f"  ratio beta_q/beta_d = {ratio}  -- kappa cancels exactly: PASS")

    ratio_ours, ratio_v82, discrepancy = test_ratio_comparison()
    print("\nUnit-independent ratio comparison:")
    print(f"  our derived beta_q/beta_d           = sqrt(6)/2  = {ratio_ours:.4f}")
    print(f"  v82 fitted analog sqrt(beta2)/beta1  =            {ratio_v82:.4f}")
    print(f"  discrepancy factor                   =            {discrepancy:.2f}x")
