"""P158 -- the mechanically-appropriate calculation FINDING_P157 named but did
not attempt: does population-averaging v82's own mass-derived scalar inputs
(m_X, r_X, k_X, per v82 Eqs. 10-14) bias its force-term decomposition (Table
III), via Jensen's inequality -- not the angular-cancellation mechanism P157
correctly retracted.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR

Two independent verification methods: sympy (exact/analytic) and Monte Carlo
(N=4,000,000, independent random draws) -- both required to agree before any
number here is trusted, per this project's own Independent Verification
Strength Ladder.

CORRECTION (2026-08-30, context-asymmetric skeptic-caught): the original
version assumed m_A independent of m_P (correlation rho=0) and stated the
F2>F1 enhancement ordering as robust "regardless of scatter size." A
dispatched skeptic found this false in general -- the ordering is a function
of BOTH scatter size and the SIGN of the log-mass correlation rho between
paired nodes, and flips below a specific threshold. `jensen_enhancement_
correlated` and `test_correlation_threshold` below generalize the original
independence-only functions and verify that threshold independently (closed
form, then Monte Carlo). The independence-only functions are kept, unchanged,
as the rho=0 special case -- verified below to be recovered exactly.
"""

import numpy as np
import sympy as sp


def mass_exponent_chain(beta):
    """v82 Eqs. 10-14 [VERIFIED-PDF pp.6-7], mass-power-law chain at FIXED z
    (E(z) factors are z-only constants at fixed z, and cancel in every ratio
    used below -- they never multiply a mass-dependent quantity that varies
    across the population at that z).
      r_X(z) ~ m_X^(1/3)                              [Eq 11]
      T_X(z) ~ m_X^(2/3)                               [Eq 12]
      M_gas,X(z) ~ T_X(z)^beta ~ m_X^(2*beta/3)         [Eq 13, beta=B=2.24 fit]
      k_X(z) = const * M_gas,X(z) * T_X(z) ~ m_X^(2*(beta+1)/3)   [Eq 14]
    Returns (r_exponent, k_exponent, kr_exponent).
    """
    r_exp = sp.Rational(1, 3)
    k_exp = sp.Rational(2, 3) * (beta + 1)
    kr_exp = sp.simplify(r_exp + k_exp)
    return r_exp, k_exp, kr_exp


def test_mass_exponent_chain_at_B_2_24():
    beta = sp.Rational(224, 100)  # v82's own fitted B = 2.24 +/- 0.03 (p.7)
    r_exp, k_exp, kr_exp = mass_exponent_chain(beta)
    assert sp.simplify(k_exp - sp.Rational(54, 25)) == 0  # 2.16 exactly
    assert abs(float(kr_exp) - 2.4933333333333336) < 1e-9
    return float(kr_exp)


def force_term_mass_degrees(kr_exp):
    """Total mass-degree (sum of exponents on m_A, m_P) for each v82 force
    tier, from its own printed formulas (Eqs. 2-4):
      F^(0) ~ m_A * m_P                          -> degree 2 (bilinear)
      F^(1) ~ k_A*m_P*r_A + k_P*m_A*r_P          -> degree kr_exp + 1
      F^(2) ~ k_A*k_P*r_A*r_P = (k_A r_A)(k_P r_P) -> degree 2*kr_exp
    """
    return {"F0": 2, "F1": kr_exp + 1, "F2": 2 * kr_exp}


def jensen_enhancement_symbolic(p_val, sigma):
    """R(p) = E[m^p]/E[m]^p for lognormal ln(m)~N(mu,sigma^2). Scale (mu)
    cancels exactly in the ratio -- only the scatter sigma matters.
    Closed form: R(p) = exp(p*sigma^2*(p-1)/2).
    """
    p, s = sp.symbols("p s", positive=True)
    R = sp.exp(p * s**2 * (p - 1) / 2)
    return R.subs({p: p_val, s: sigma})


def test_jensen_positive_controls():
    """R(0)=1 and R(1)=1 exactly -- no Jensen bias for the trivial/linear
    cases, regardless of scatter. If these failed, the formula would be wrong.
    """
    for p_val in (0, 1):
        for sigma in (0.2, 0.5, 1.0):
            val = jensen_enhancement_symbolic(p_val, sigma)
            assert sp.simplify(val - 1) == 0, f"R({p_val}) must be exactly 1"


def monte_carlo_cross_check(kr_exp, sigma_lnm, n=4_000_000, seed=0):
    """Independent method (brute-force sampling, no formula injected) to
    verify: (a) F0's enhancement is ~1 (independence control), (b) F1's
    matches the analytic R(p), (c) F2's matches R(p)^2.
    """
    rng = np.random.default_rng(seed)
    m_a = np.exp(rng.normal(0.0, sigma_lnm, n))
    m_p = np.exp(rng.normal(0.0, sigma_lnm, n))

    f0_pop = np.mean(m_a * m_p)
    f0_rep = np.mean(m_a) * np.mean(m_p)

    kr_a, kr_p = m_a**kr_exp, m_p**kr_exp
    f1_pop = np.mean(kr_a * m_p + kr_p * m_a)
    f1_rep = np.mean(m_a) ** kr_exp * np.mean(m_p) + np.mean(m_p) ** kr_exp * np.mean(m_a)

    f2_pop = np.mean(kr_a * kr_p)
    f2_rep = np.mean(m_a) ** kr_exp * np.mean(m_p) ** kr_exp

    return {
        "F0_enhancement": f0_pop / f0_rep,
        "F1_enhancement": f1_pop / f1_rep,
        "F2_enhancement": f2_pop / f2_rep,
    }


def test_monte_carlo_matches_analytic(sigma_lnm=0.5):
    kr_exp = test_mass_exponent_chain_at_B_2_24()
    mc = monte_carlo_cross_check(kr_exp, sigma_lnm)
    r_analytic = float(jensen_enhancement_symbolic(kr_exp, sigma_lnm))

    assert abs(mc["F0_enhancement"] - 1.0) < 0.01, "F0 independence control failed"
    assert abs(mc["F1_enhancement"] - r_analytic) / r_analytic < 0.01
    assert abs(mc["F2_enhancement"] - r_analytic**2) / r_analytic**2 < 0.02
    return mc, r_analytic


def jensen_enhancement_correlated(p_val, sigma, rho):
    """Bivariate lognormal: ln(m_A), ln(m_P) jointly normal, each variance
    sigma^2, log-space correlation rho (rho=0 recovers independence). Closed
    form (E[exp(aX+bY)] = exp((a^2+b^2+2ab*rho)*sigma^2/2) for zero-mean
    jointly-normal X,Y -- the mean cancels in every ratio below):
      F0 enhancement = exp(rho*sigma^2)
      F1 enhancement = exp( p*sigma^2*(p + 2*rho - 1)/2 )
      F2 enhancement = exp( p*sigma^2*(p*rho + p - 1) )
    Returns (F0_enh, F1_enh, F2_enh).
    """
    p, s, r = sp.symbols("p s r", real=True)
    log_f0 = r * s**2
    log_f1 = p * s**2 * (p + 2 * r - 1) / 2
    log_f2 = p * s**2 * (p * r + p - 1)
    subs = {p: p_val, s: sigma, r: rho}
    return (
        float(sp.exp(log_f0.subs(subs))),
        float(sp.exp(log_f1.subs(subs))),
        float(sp.exp(log_f2.subs(subs))),
    )


def test_correlated_recovers_independence_case():
    """Positive control: rho=0 must reproduce the original independence-only
    F0=1, F1=R(p), F2=R(p)^2 results exactly.
    """
    kr_exp = test_mass_exponent_chain_at_B_2_24()
    for sigma in (0.2, 0.5, 0.7):
        f0, f1, f2 = jensen_enhancement_correlated(kr_exp, sigma, 0.0)
        r = float(jensen_enhancement_symbolic(kr_exp, sigma))
        assert abs(f0 - 1.0) < 1e-9
        assert abs(f1 - r) < 1e-9
        assert abs(f2 - r**2) < 1e-9


def test_correlation_threshold():
    """Where does the F2>F1 ordering flip? log(F2/F1) = q*sigma^2*(q-1)*(2*rho+1)/2
    (derived by direct expansion, sympy-verified) -- for q>1, sigma>0, this is
    zero exactly at rho=-1/2, independent of q and sigma. Below that threshold
    F2's enhancement is SMALLER than F1's, reversing the original claim's
    ordering. Also verifies where F1's OWN enhancement crosses 1 (a separate,
    more negative threshold) -- there is a regime (-0.7467 < rho < -0.5) where
    F1 is still enhanced (>1) but F2 is enhanced LESS than F1.
    """
    q, s, r = sp.symbols("q s r", real=True)
    log_f1 = q * s**2 * (q + 2 * r - 1) / 2
    log_f2 = q * s**2 * (q * r + q - 1)
    log_ratio = sp.simplify(log_f2 - log_f1)
    factored = sp.factor(log_ratio)
    assert sp.simplify(factored - q * s**2 * (q - 1) * (2 * r + 1) / 2) == 0

    q_val = sp.nsimplify(2.4933333333333336)
    threshold_f2_over_f1 = sp.solve(sp.Eq(log_ratio.subs(q, q_val), 0), r)
    threshold_f1_itself = sp.solve(sp.Eq(log_f1.subs(q, q_val), 0), r)
    assert threshold_f2_over_f1 == [sp.Rational(-1, 2)]
    return float(threshold_f2_over_f1[0]), float(threshold_f1_itself[0])


def monte_carlo_correlated(kr_exp, sigma_lnm, rho, n=4_000_000, seed=0):
    """Independent method for the correlated case: draw correlated lognormal
    pairs directly (Cholesky on the 2x2 log-space covariance), no formula
    injected.
    """
    rng = np.random.default_rng(seed)
    cov = np.array([[sigma_lnm**2, rho * sigma_lnm**2], [rho * sigma_lnm**2, sigma_lnm**2]])
    lnm = rng.multivariate_normal([0.0, 0.0], cov, n)
    m_a, m_p = np.exp(lnm[:, 0]), np.exp(lnm[:, 1])

    f0_pop, f0_rep = np.mean(m_a * m_p), np.mean(m_a) * np.mean(m_p)
    kr_a, kr_p = m_a**kr_exp, m_p**kr_exp
    f1_pop = np.mean(kr_a * m_p + kr_p * m_a)
    f1_rep = np.mean(m_a) ** kr_exp * np.mean(m_p) + np.mean(m_p) ** kr_exp * np.mean(m_a)
    f2_pop, f2_rep = np.mean(kr_a * kr_p), np.mean(m_a) ** kr_exp * np.mean(m_p) ** kr_exp

    return f0_pop / f0_rep, f1_pop / f1_rep, f2_pop / f2_rep


def test_monte_carlo_matches_correlated_analytic(sigma_lnm=0.5, rho=-0.5):
    kr_exp = test_mass_exponent_chain_at_B_2_24()
    f0_mc, f1_mc, f2_mc = monte_carlo_correlated(kr_exp, sigma_lnm, rho)
    f0_a, f1_a, f2_a = jensen_enhancement_correlated(kr_exp, sigma_lnm, rho)
    assert abs(f0_mc - f0_a) / f0_a < 0.02
    assert abs(f1_mc - f1_a) / f1_a < 0.02
    assert abs(f2_mc - f2_a) / f2_a < 0.02
    return (f0_mc, f1_mc, f2_mc), (f0_a, f1_a, f2_a)


if __name__ == "__main__":
    kr_exp = test_mass_exponent_chain_at_B_2_24()
    degrees = force_term_mass_degrees(kr_exp)
    print("Mass-degree of each force tier:", {k: float(v) for k, v in degrees.items()})

    test_jensen_positive_controls()
    print("Jensen positive controls (R(0)=R(1)=1): PASS")

    print("\nIllustrative enhancement factors by log-mass scatter sigma_lnm:")
    print(f"{'sigma':>6} {'F1 enh = R(p)':>15} {'F2 enh = R(p)^2':>18}")
    for sigma in (0.2, 0.3, 0.5, 0.7):
        r = float(jensen_enhancement_symbolic(kr_exp, sigma))
        print(f"{sigma:>6} {r:>15.4f} {r**2:>18.4f}")

    mc, r_analytic = test_monte_carlo_matches_analytic(0.5)
    print("\nMonte Carlo cross-check (sigma_lnm=0.5, N=4e6):")
    print(f"  F0 enhancement (must be ~1): {mc['F0_enhancement']:.4f}")
    print(f"  F1 enhancement MC={mc['F1_enhancement']:.4f} vs analytic R(p)={r_analytic:.4f}")
    print(f"  F2 enhancement MC={mc['F2_enhancement']:.4f} vs analytic R(p)^2={r_analytic**2:.4f}")

    test_correlated_recovers_independence_case()
    print("\nCorrelated-case control (rho=0 recovers independence results exactly): PASS")

    thr_ratio, thr_f1 = test_correlation_threshold()
    print("\nCorrelation thresholds (q=2.4933, exact, independent of sigma):")
    print(f"  F2/F1 ordering flips at rho = {thr_ratio:.4f}")
    print(f"  F1's own enhancement crosses 1 at rho = {thr_f1:.4f}")

    print("\nEnhancement vs correlation rho (sigma_lnm=0.5):")
    print(f"{'rho':>8} {'F0 enh':>10} {'F1 enh':>10} {'F2 enh':>10} {'F2/F1':>10}")
    for rho in (-1.0, -0.7467, -0.5, -0.2, 0.0, 0.5):
        f0, f1, f2 = jensen_enhancement_correlated(kr_exp, 0.5, rho)
        print(f"{rho:>8.4f} {f0:>10.4f} {f1:>10.4f} {f2:>10.4f} {f2 / f1:>10.4f}")

    mc_c, an_c = test_monte_carlo_matches_correlated_analytic(0.5, -0.5)
    print("\nMonte Carlo cross-check at threshold (sigma=0.5, rho=-0.5, N=4e6):")
    print(f"  analytic (F0,F1,F2)={tuple(round(x, 4) for x in an_c)}")
    print(f"  Monte Carlo         ={tuple(round(x, 4) for x in mc_c)}")
