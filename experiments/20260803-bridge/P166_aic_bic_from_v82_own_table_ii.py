"""P166 -- Phase 1 of the AIC/BIC calibration plan (Measurement Shadow /
Identifiability Breaker / negative-space-miner audits, 2026-08-30): compute
AIC/BIC on v82's OWN already-published chi^2 numbers (Table II, Sec. III),
using v82's own three flat-LCDM benchmarks as comparators. No new data, no
new fitting -- pure arithmetic on numbers TJB himself reports but explicitly
declines to combine into AIC/BIC (Sec. IV.I, "we do not report AIC or BIC
anywhere in this paper").

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import math

N_POINTS = 33  # v82's own N -- 31 Cosmic Chronometer + SH0ES + DESI


def aic(chi2, k):
    """Akaike Information Criterion. Lower = preferred."""
    return chi2 + 2 * k


def bic(chi2, k, n=N_POINTS):
    """Bayesian Information Criterion. Lower = preferred."""
    return chi2 + k * math.log(n)


def delta(chi2_a, k_a, chi2_b, k_b, n=N_POINTS):
    """(model A) - (model B) for chi2, AIC, BIC. Negative = A preferred."""
    d_chi2 = chi2_a - chi2_b
    d_aic = aic(chi2_a, k_a) - aic(chi2_b, k_b)
    d_bic = bic(chi2_a, k_a, n) - bic(chi2_b, k_b, n)
    return d_chi2, d_aic, d_bic


# --- v82's own published numbers [VERIFIED-PDF, Sec III, Table II, p.13] ---

# MULTING's own "unconstrained" (free-floating) best fit: (H0,anchor, beta1,
# beta2) all jointly optimized -- k=3. This is v82's own "spotlighted
# solution," chi2_33=15.75 [VERIFIED-PDF p.13, line ~754/795-797].
MULTING_UNCONSTRAINED = {"chi2": 15.75, "k": 3}

# MULTING's SH0ES-anchored row: H0,anchor FIXED at 73.04 (SH0ES value),
# beta1/beta2 re-optimized -- k=2 [VERIFIED-PDF p.13, line 755/799-801].
MULTING_SH0ES_ANCHORED = {"chi2": 15.78, "k": 2}

# LCDM Benchmark 1: fixed at Planck (H0=67.4, Om=0.315), NOT re-optimized --
# k=0. v82's own text calls this "not a demanding benchmark... fixed LCDM is
# not permitted to respond to SH0ES at all" [VERIFIED-PDF p.13, line 761-772].
LCDM_FIXED_PLANCK = {"chi2": 36.96, "k": 0}

# LCDM Benchmark 2: H0 and Om BOTH freely optimized against the same 33
# points (H0=71.83, Om=0.2724) -- k=2. v82's own text: "the more meaningful
# comparison, because it does not handicap LCDM" [VERIFIED-PDF p.13, line
# 775-793].
LCDM_REFIT_BOTH = {"chi2": 16.31, "k": 2}

# LCDM Benchmark 3: H0 FIXED at exactly 73.04 (matching MULTING's SH0ES-
# anchored case), only Om free -- k=1. v82's own text: "perhaps the fairest
# single comparison in this paper" [VERIFIED-PDF p.13, line 803-814].
LCDM_FIXED_H0_FREE_OM = {"chi2": 16.60, "k": 1}


def test_positive_control_handicapped_comparison_reproduces_v82_own_narrative():
    """Sanity check: comparing MULTING's unconstrained fit against v82's OWN
    admittedly-handicapped Benchmark 1 (fixed Planck, k=0) must reproduce
    v82's own qualitative claim of a large, clear win -- if this doesn't come
    out strongly negative (favoring MULTING), the AIC/BIC arithmetic itself
    is broken, independent of anything about the fairer benchmarks below.
    """
    d_chi2, d_aic, d_bic = delta(
        MULTING_UNCONSTRAINED["chi2"],
        MULTING_UNCONSTRAINED["k"],
        LCDM_FIXED_PLANCK["chi2"],
        LCDM_FIXED_PLANCK["k"],
    )
    assert d_chi2 < -20  # v82's own text: this is not a close comparison
    assert d_aic < -10  # unambiguous AIC win for MULTING here
    assert d_bic < -10  # unambiguous BIC win for MULTING here


def test_negative_control_bic_penalty_scales_with_n():
    """Sanity check on the BIC formula itself, independent of any real data:
    the ln(N) parameter-count penalty must grow with N (this is the entire
    point of BIC vs AIC -- BIC penalizes extra parameters more harshly as
    the dataset grows). A one-parameter difference should incur a small
    penalty at small N and a large penalty at large N.
    """
    small_n_penalty = bic(0, 1, n=3) - bic(0, 0, n=3)
    large_n_penalty = bic(0, 1, n=100_000) - bic(0, 0, n=100_000)
    assert small_n_penalty < large_n_penalty
    assert math.isclose(small_n_penalty, math.log(3))
    assert math.isclose(large_n_penalty, math.log(100_000))


def test_comparison_a_unconstrained_vs_fair_refit_benchmark():
    """MULTING's own spotlighted (unconstrained, k=3) row vs v82's own
    Benchmark 2 (k=2), which v82's own text calls "the more meaningful
    comparison, because it does not handicap LCDM."
    """
    d_chi2, d_aic, d_bic = delta(
        MULTING_UNCONSTRAINED["chi2"],
        MULTING_UNCONSTRAINED["k"],
        LCDM_REFIT_BOTH["chi2"],
        LCDM_REFIT_BOTH["k"],
    )
    assert math.isclose(d_chi2, -0.56, abs_tol=0.01)
    assert math.isclose(d_aic, 1.44, abs_tol=0.01)
    assert math.isclose(d_bic, 2.937, abs_tol=0.01)
    return d_chi2, d_aic, d_bic


def test_comparison_b_sh0es_anchored_vs_fairest_benchmark():
    """MULTING's own SH0ES-anchored (k=2) row vs v82's own Benchmark 3
    (k=1), which v82's own text calls "perhaps the fairest single
    comparison in this paper."
    """
    d_chi2, d_aic, d_bic = delta(
        MULTING_SH0ES_ANCHORED["chi2"],
        MULTING_SH0ES_ANCHORED["k"],
        LCDM_FIXED_H0_FREE_OM["chi2"],
        LCDM_FIXED_H0_FREE_OM["k"],
    )
    assert math.isclose(d_chi2, -0.82, abs_tol=0.01)
    assert math.isclose(d_aic, 1.18, abs_tol=0.01)
    assert math.isclose(d_bic, 2.677, abs_tol=0.01)
    return d_chi2, d_aic, d_bic


if __name__ == "__main__":
    test_positive_control_handicapped_comparison_reproduces_v82_own_narrative()
    print("Positive control (vs v82's own handicapped Benchmark 1): PASS")
    print("  -- large MULTING win reproduced, arithmetic itself is sound.")

    test_negative_control_bic_penalty_scales_with_n()
    print("\nNegative control (BIC formula's own N-scaling): PASS")

    d_chi2_a, d_aic_a, d_bic_a = test_comparison_a_unconstrained_vs_fair_refit_benchmark()
    print("\n=== Comparison A: MULTING unconstrained (k=3) vs v82's own")
    print("    Benchmark 2 (k=2, 'the more meaningful comparison') ===")
    print(f"  delta_chi2 = {d_chi2_a:+.3f}  (negative = MULTING's raw fit is better)")
    print(f"  delta_AIC  = {d_aic_a:+.3f}  (Burnham-Anderson: <2 = indistinguishable)")
    print(f"  delta_BIC  = {d_bic_a:+.3f}  (Kass-Raftery: 2-6 = 'positive', not 'strong')")

    d_chi2_b, d_aic_b, d_bic_b = test_comparison_b_sh0es_anchored_vs_fairest_benchmark()
    print("\n=== Comparison B: MULTING SH0ES-anchored (k=2) vs v82's own")
    print("    Benchmark 3 (k=1, 'perhaps the fairest single comparison') ===")
    print(f"  delta_chi2 = {d_chi2_b:+.3f}")
    print(f"  delta_AIC  = {d_aic_b:+.3f}")
    print(f"  delta_BIC  = {d_bic_b:+.3f}")

    print("\nConclusion: on v82's OWN two 'fairer' benchmarks (not the")
    print("handicapped fixed-Planck one), delta_AIC stays under the")
    print("indistinguishability threshold (~1.2-1.4 < 2) and delta_BIC gives")
    print("only 'positive' (not 'strong') Kass-Raftery support to LCDM.")
    print("v82's own raw-chi2 margin, already called 'narrow, not")
    print("substantial' in the text, is consumed almost entirely by the")
    print("standard parameter-count penalty on the fairer comparisons.")
