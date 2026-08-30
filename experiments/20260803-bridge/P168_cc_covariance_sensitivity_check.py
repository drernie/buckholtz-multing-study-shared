"""P168 -- follow-up to FINDING_P167's own named residual gap: does
accounting for the Cosmic Chronometer sample's known SYSTEMATIC
covariance (as opposed to the purely diagonal/statistical sigma_H used
in P167) change the ~1.7-chi2 margin by which a physically-empty model
beat MULTING's own reported fit?

Source for the covariance structure [VERIFIED-arXiv, abstract fetched
directly, not agent-report alone]: Moresco, Jimenez, Verde, Cimatti &
Pozzetti, "Setting the Stage for Cosmic Chronometers II," ApJ 898, 82
(2020), arXiv:2003.07362. Key facts from the paper's own abstract:
  - "For current H(z) measurements, where the uncertainties due to
    metallicity and star formation history were already included... the
    additional systematic uncertainty is between 5.4% (at z=0.2) and
    2.3% (at z=1.5)" [using modern stellar libraries, "odd-one-out" SPS
    choice -- the paper's own headline, most-favorable-to-CC-data number].
  - This systematic (SPS-model-choice) is constructed as a RANK-1 outer
    product (paper's own Eq. 9): fully correlated across ALL redshift
    bins, not restricted to same-survey pairs.

HONEST SCOPE LIMITATIONS (not resolved here, stated explicitly):
  1. The paper's own Table 3 gives this fraction at 29 discrete z-bins,
     0.075<=z<=1.475; this file has only the ABSTRACT's two headline
     endpoint values (5.4% at z=0.2, 2.3% at z=1.5) and interpolates
     LINEARLY between them -- a rough approximation of the true curve,
     not a reproduction of Table 3 itself.
  2. The paper's own covariance construction is built from the Moresco
     group's OWN D4000-method measurements. Whether the SAME systematic
     fraction should be applied to the non-Moresco points in the
     standard 31-point compilation (Simon et al. 2005, Stern et al.
     2010, Zhang et al. 2014, Ratsimbazafy et al. 2017 -- different
     methodology, full spectral fitting not D4000-slope) is NOT
     established in the paper and is not resolved here. TWO variants are
     run: (A) apply to all 31 points as a conservative sensitivity
     bound, (B) apply only to the z-range the paper's own analysis
     covers (0<z<1.5) -- points outside get zero added systematic.
  3. Points outside [0.2, 1.5] use the nearest endpoint value (flat
     extrapolation), not the paper's own actual curve behavior there.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy.optimize import minimize

# Re-import the same verified 31+2 data points P167 already used
# [VERIFIED-arXiv, cross-checked against 2 independent sources, see P167]
CC_DATA = [
    (0.0700, 69.0, 19.6),
    (0.0900, 69.0, 12.0),
    (0.1200, 68.6, 26.2),
    (0.1700, 83.0, 8.0),
    (0.1791, 75.0, 4.0),
    (0.1993, 75.0, 5.0),
    (0.2000, 72.9, 29.6),
    (0.2700, 77.0, 14.0),
    (0.2800, 88.8, 36.6),
    (0.3519, 83.0, 14.0),
    (0.3802, 83.0, 13.5),
    (0.4000, 95.0, 17.0),
    (0.4004, 77.0, 10.2),
    (0.4247, 87.1, 11.2),
    (0.4497, 92.8, 12.9),
    (0.4700, 89.0, 49.6),
    (0.4783, 80.9, 9.0),
    (0.4800, 97.0, 62.0),
    (0.5929, 104.0, 13.0),
    (0.6797, 92.0, 8.0),
    (0.7812, 105.0, 12.0),
    (0.8754, 125.0, 17.0),
    (0.8800, 90.0, 40.0),
    (0.9000, 117.0, 23.0),
    (1.0370, 154.0, 20.0),
    (1.3000, 168.0, 17.0),
    (1.3630, 160.0, 33.6),
    (1.4300, 177.0, 18.0),
    (1.5300, 140.0, 14.0),
    (1.7500, 202.0, 40.0),
    (1.9650, 186.5, 50.4),
]
SH0ES = (0.0233, 73.04, 1.04)
DESI = (2.33, 236.1, 2.8)
FULL_33 = CC_DATA + [SH0ES, DESI]

MULTING_UNCONSTRAINED_CHI2 = 15.75  # k=3, [VERIFIED-PDF, same as P166/P167]
MULTING_SH0ES_ANCHORED_CHI2 = 15.78  # k=2

# Paper's own two headline endpoint values [VERIFIED-arXiv abstract]
Z_LO, FRAC_LO = 0.2, 0.054
Z_HI, FRAC_HI = 1.5, 0.023


def _systematic_fraction(z, restrict_to_paper_range):
    """Linear interpolation between the paper's own two headline points.
    Flat extrapolation outside [Z_LO, Z_HI]. If restrict_to_paper_range,
    returns 0 outside [Z_LO, Z_HI] instead (Variant B)."""
    if restrict_to_paper_range and not (Z_LO <= z <= Z_HI):
        return 0.0
    z_clamped = min(max(z, Z_LO), Z_HI)
    t = (z_clamped - Z_LO) / (Z_HI - Z_LO)
    return FRAC_LO + t * (FRAC_HI - FRAC_LO)


def _build_covariance(data, systematic_amplitude, restrict_to_paper_range, n_cc):
    """Cov = diag(sigma_stat^2) + rank-1 outer product of
    (fraction(z_i)*H_i, fraction(z_j)*H_j) -- Eq. 9 structure of
    arXiv:2003.07362. systematic_amplitude=0 recovers pure-diagonal
    (P167's own original treatment) exactly -- the positive control.

    CORRECTION (2026-08-31, skeptic-caught): the CC-specific SPS/IMF
    systematic must apply ONLY to the first n_cc entries of `data` (the
    actual Cosmic Chronometer points) -- SH0ES and DESI are NOT Cosmic
    Chronometer measurements (distance-ladder Cepheid calibration and
    BAO respectively) and have no documented connection to the Moresco
    et al. 2020 stellar-population-synthesis systematic. The original
    draft applied `_systematic_fraction` to ALL of `data` including
    those two points, via flat extrapolation -- a real bug, not a
    modeling choice, now fixed: `frac_h[i]=0` for any index >= n_cc.
    """
    n = len(data)
    cov = np.zeros((n, n))
    frac_h = np.zeros(n)
    for i, (z, h, sigma) in enumerate(data):
        cov[i, i] = sigma**2
        if i < n_cc:  # only actual Cosmic Chronometer points
            frac_h[i] = systematic_amplitude * _systematic_fraction(z, restrict_to_paper_range) * h
    cov += np.outer(frac_h, frac_h)
    return cov


def _dummy_h(z, y0, y1, y2):
    return np.sqrt(max(y0 + y1 * z + y2 * z**2, 1e-6))


def _gls_chi2(params, data, cov_inv):
    y0, y1, y2 = params
    resid = np.array([h_obs - _dummy_h(z, y0, y1, y2) for z, h_obs, _ in data])
    return resid @ cov_inv @ resid


def _fit_gls_unconstrained(data, cov):
    cov_inv = np.linalg.inv(cov)
    res = minimize(
        _gls_chi2,
        x0=[70.0**2, 50.0, 5.0],
        args=(data, cov_inv),
        method="Nelder-Mead",
        options={"xatol": 1e-8, "fatol": 1e-10, "maxiter": 20000},
    )
    return res.x, res.fun


def _fit_gls_anchored(data, cov, h0_fixed):
    cov_inv = np.linalg.inv(cov)
    y0_fixed = h0_fixed**2

    def obj(params):
        y1, y2 = params
        return _gls_chi2([y0_fixed, y1, y2], data, cov_inv)

    res = minimize(
        obj, x0=[50.0, 5.0], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10}
    )
    y1, y2 = res.x
    return (y0_fixed, y1, y2), res.fun


def test_positive_control_zero_systematic_recovers_p167_diagonal_result():
    """systematic_amplitude=0 must recover the pure-diagonal chi2 P167
    already found (14.073 unconstrained, 14.107 anchored), to a tight
    tolerance -- confirms the GLS machinery reduces correctly to the
    simpler, already-verified case before trusting it on the nonzero-
    covariance case.
    """
    cov = _build_covariance(
        FULL_33, systematic_amplitude=0.0, restrict_to_paper_range=False, n_cc=len(CC_DATA)
    )
    _, chi2_u = _fit_gls_unconstrained(FULL_33, cov)
    _, chi2_a = _fit_gls_anchored(FULL_33, cov, 73.04)
    assert abs(chi2_u - 14.073) < 0.01
    assert abs(chi2_a - 14.107) < 0.01


def run_variant(label, systematic_amplitude, restrict_to_paper_range):
    cov = _build_covariance(
        FULL_33, systematic_amplitude, restrict_to_paper_range, n_cc=len(CC_DATA)
    )
    popt_u, chi2_u = _fit_gls_unconstrained(FULL_33, cov)
    popt_a, chi2_a = _fit_gls_anchored(FULL_33, cov, 73.04)

    print(f"\n=== {label} ===")
    print(f"Unconstrained (k=3): chi2={chi2_u:.3f}  (P167 diagonal-only: 14.073)")
    print(f"  vs MULTING (k=3): chi2={MULTING_UNCONSTRAINED_CHI2}")
    print(f"  delta_chi2 = {chi2_u - MULTING_UNCONSTRAINED_CHI2:+.3f}")
    print(f"Anchored (k=2):      chi2={chi2_a:.3f}  (P167 diagonal-only: 14.107)")
    print(f"  vs MULTING (k=2): chi2={MULTING_SH0ES_ANCHORED_CHI2}")
    print(f"  delta_chi2 = {chi2_a - MULTING_SH0ES_ANCHORED_CHI2:+.3f}")
    return chi2_u, chi2_a


if __name__ == "__main__":
    test_positive_control_zero_systematic_recovers_p167_diagonal_result()
    print("Positive control (zero systematic recovers P167's own diagonal result): PASS")

    run_variant(
        "Variant A: systematic applied to ALL 31 CC points (conservative sensitivity bound)",
        systematic_amplitude=1.0,
        restrict_to_paper_range=False,
    )

    run_variant(
        "Variant B: systematic applied ONLY within paper's own analyzed range [0.2,1.5]",
        systematic_amplitude=1.0,
        restrict_to_paper_range=True,
    )

    print("\n=== Interpretation ===")
    print("If chi2 under either variant moves close to or past MULTING's own")
    print("15.75/15.78, the P167 diagonal-only margin (~1.7) does not survive")
    print("systematic covariance and the 'dummy beats MULTING' claim weakens")
    print("or reverses. If chi2 barely moves, the margin is likely robust to")
    print("this specific systematic (though NOT to an untested full")
    print("31-point covariance construction -- see module docstring, scope")
    print("limitation 2, which this file does not resolve).")
