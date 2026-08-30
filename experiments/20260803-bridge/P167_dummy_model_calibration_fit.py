"""P167 -- Phase 2 of the AIC/BIC calibration plan (FINDING_P166's own
named next step): fit a physically-EMPTY 3-parameter model (no cluster-
gravity story, no dark-energy story -- a bare quadratic in z for Y=H^2)
to the SAME 33 real H(z) data points v82 itself uses (31 Cosmic
Chronometer + SH0ES + DESI), using the SAME two comparison regimes
FINDING_P166 already extracted from v82's own Table II (unconstrained
k=3; SH0ES-anchored k=2). If this physically-empty model matches
MULTING's own chi^2 about as well, that's direct evidence the specific
dipole/quadrupole physics is not what earns MULTING's own fit quality --
ordinary 3-parameter curve flexibility could do most or all of the work.

Data: 31-point Cosmic Chronometer compilation, cross-verified against TWO
independent primary sources (Gomez-Valent & Amendola 2018, arXiv:1802.01505;
Yu, Ratra & Wang 2018, arXiv:1711.03437) -- 31/31 rows confirmed matching
on z and H(z); 30/31 rows also matching on sigma_H. One flagged
discrepancy (z=0.47: source A sigma=49.6, source B sigma=50) is handled
via an explicit sensitivity check (Stage 8 below), not silently resolved
by picking one value. SH0ES (z=0.0233, H=73.04+-1.04) and DESI DR2
Lyman-alpha (z=2.33, H=236.1+-2.8) are v82's own quoted values
[VERIFIED-PDF, already used in FINDING_P163/P165/P166].

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import math

import numpy as np
from scipy.optimize import curve_fit

# --- Data: 31-point Cosmic Chronometer compilation [VERIFIED-arXiv,
# cross-checked against arXiv:1802.01505 (Table, Sect 2) AND
# arXiv:1711.03437 (Table 1, method "a" rows), 31/31 rows agree on z,H;
# 30/31 agree on sigma_H -- z=0.47 flagged, handled in Stage 8 below]
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
    (0.4700, 89.0, 49.6),  # sensitivity-checked below (source B: 50.0)
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
assert len(CC_DATA) == 31

# v82's own two quoted anchor points [VERIFIED-PDF, same as FINDING_P163/166]
SH0ES = (0.0233, 73.04, 1.04)
DESI = (2.33, 236.1, 2.8)

FULL_33 = CC_DATA + [SH0ES, DESI]
assert len(FULL_33) == 33

# v82's own Table II numbers this file compares against [VERIFIED-PDF,
# same source as FINDING_P166]
MULTING_UNCONSTRAINED_CHI2 = 15.75  # k=3
MULTING_SH0ES_ANCHORED_CHI2 = 15.78  # k=2, H0,anchor fixed at 73.04


def _dummy_model(z, y0, y1, y2):
    """Physically-empty Y=H^2 quadratic in z. No dark-energy story, no
    cluster-gravity story -- ordinary curve-fitting flexibility only."""
    return y0 + y1 * z + y2 * z**2


def _h_model(z, y0, y1, y2):
    return np.sqrt(np.clip(_dummy_model(z, y0, y1, y2), 1e-6, None))


def _chi2(data, y0, y1, y2):
    total = 0.0
    for z, h_obs, sigma in data:
        h_model = _h_model(np.array([z]), y0, y1, y2)[0]
        total += ((h_obs - h_model) / sigma) ** 2
    return total


def _fit_unconstrained(data):
    """k=3: all of (y0,y1,y2) free."""
    zs = np.array([d[0] for d in data])
    hs = np.array([d[1] for d in data])
    sigmas = np.array([d[2] for d in data])
    p0 = [70.0**2, 50.0, 5.0]
    popt, _ = curve_fit(_h_model, zs, hs, p0=p0, sigma=sigmas, absolute_sigma=True, maxfev=20000)
    return popt, _chi2(data, *popt)


def _fit_anchored(data, h0_fixed):
    """k=2: y0 fixed so H(z=0)=h0_fixed exactly (mirrors MULTING's own
    SH0ES-anchored case, which fixes H0,anchor and re-optimizes the
    remaining two parameters)."""
    y0_fixed = h0_fixed**2
    zs = np.array([d[0] for d in data])
    hs = np.array([d[1] for d in data])
    sigmas = np.array([d[2] for d in data])

    def model_anchored(z, y1, y2):
        return _h_model(z, y0_fixed, y1, y2)

    p0 = [50.0, 5.0]
    popt, _ = curve_fit(
        model_anchored, zs, hs, p0=p0, sigma=sigmas, absolute_sigma=True, maxfev=20000
    )
    y1, y2 = popt
    return (y0_fixed, y1, y2), _chi2(data, y0_fixed, y1, y2)


def _fit_constant(data):
    """k=1 negative control: H(z)=y0 constant, no z-dependence at all.
    Must fit clearly WORSE than the k=3 case -- if it doesn't, the fit
    machinery is not actually sensitive to the data's own shape."""
    zs = np.array([d[0] for d in data])
    hs = np.array([d[1] for d in data])
    sigmas = np.array([d[2] for d in data])

    def model_const(z, y0):
        return _h_model(z, y0, 0.0, 0.0)

    popt, _ = curve_fit(model_const, zs, hs, p0=[70.0**2], sigma=sigmas, absolute_sigma=True)
    return popt, _chi2(data, popt[0], 0.0, 0.0)


def aic(chi2, k):
    return chi2 + 2 * k


def bic(chi2, k, n=33):
    return chi2 + k * math.log(n)


def test_positive_control_recovers_known_synthetic_curve():
    """Generate synthetic data from a KNOWN quadratic Y(z) curve plus
    Gaussian noise matching the real sigmas' typical scale, fit the same
    unconstrained procedure, and confirm (a) recovered parameters are
    close to the injected ones and (b) the resulting chi2 is consistent
    with the injected noise (reduced chi2 near 1 for a correctly-
    specified model) -- confirms the fitting code itself works before
    trusting it on real data.
    """
    rng = np.random.default_rng(20260830)
    true_y0, true_y1, true_y2 = 70.0**2, 45.0, 8.0
    zs = np.array([d[0] for d in FULL_33])
    sigmas = np.array([d[2] for d in FULL_33])
    h_true = _h_model(zs, true_y0, true_y1, true_y2)
    h_synth = h_true + rng.normal(0, sigmas)
    synth_data = list(zip(zs.tolist(), h_synth.tolist(), sigmas.tolist(), strict=True))

    popt, chi2_synth = _fit_unconstrained(synth_data)
    assert abs(popt[0] - true_y0) / true_y0 < 0.05
    reduced_chi2 = chi2_synth / (33 - 3)
    assert 0.4 < reduced_chi2 < 2.5  # generous band, just checking sanity


def test_negative_control_constant_model_fits_worse():
    """k=1 constant-H(z) model must fit clearly worse than the k=3
    quadratic -- sanity check that the fitting procedure is actually
    sensitive to the real data's own shape, not just returning a
    trivially-good chi2 regardless of model flexibility.
    """
    _, chi2_const = _fit_constant(FULL_33)
    _, chi2_quad = _fit_unconstrained(FULL_33)
    assert chi2_const > chi2_quad + 50  # must be substantially worse


def run_comparisons(data, label):
    popt_u, chi2_u = _fit_unconstrained(data)
    popt_a, chi2_a = _fit_anchored(data, 73.04)

    print(f"\n=== {label} ===")
    print(
        f"Unconstrained (k=3) dummy fit: chi2={chi2_u:.3f}  (Y0,Y1,Y2)={tuple(round(p, 3) for p in popt_u)}"
    )
    print(f"  vs MULTING unconstrained (k=3): chi2={MULTING_UNCONSTRAINED_CHI2}")
    d_chi2_u = chi2_u - MULTING_UNCONSTRAINED_CHI2
    d_aic_u = aic(chi2_u, 3) - aic(MULTING_UNCONSTRAINED_CHI2, 3)
    print(
        f"  delta_chi2 = {d_chi2_u:+.3f}   delta_AIC = {d_aic_u:+.3f}  (same k, so delta_AIC=delta_chi2)"
    )

    print(
        f"\nSH0ES-anchored (k=2) dummy fit: chi2={chi2_a:.3f}  (Y1,Y2)={tuple(round(p, 3) for p in popt_a[1:])}"
    )
    print(f"  vs MULTING SH0ES-anchored (k=2): chi2={MULTING_SH0ES_ANCHORED_CHI2}")
    d_chi2_a = chi2_a - MULTING_SH0ES_ANCHORED_CHI2
    d_aic_a = aic(chi2_a, 2) - aic(MULTING_SH0ES_ANCHORED_CHI2, 2)
    print(f"  delta_chi2 = {d_chi2_a:+.3f}   delta_AIC = {d_aic_a:+.3f}")

    return chi2_u, chi2_a


if __name__ == "__main__":
    test_positive_control_recovers_known_synthetic_curve()
    print("Positive control (recovers known synthetic curve, sane reduced chi2): PASS")

    test_negative_control_constant_model_fits_worse()
    print("Negative control (k=1 constant model fits substantially worse than k=3): PASS")

    chi2_u_main, chi2_a_main = run_comparisons(FULL_33, "MAIN RUN (sigma_H=49.6 at z=0.47)")

    # Stage 8 sensitivity check: does the flagged z=0.47 discrepancy
    # (source A: 49.6, source B: 50) change the qualitative conclusion?
    data_alt = list(FULL_33)
    idx_047 = next(i for i, d in enumerate(data_alt) if abs(d[0] - 0.47) < 1e-6)
    z047, h047, _ = data_alt[idx_047]
    data_alt[idx_047] = (z047, h047, 50.0)
    chi2_u_alt, chi2_a_alt = run_comparisons(data_alt, "SENSITIVITY CHECK (sigma_H=50.0 at z=0.47)")

    print("\n=== Sensitivity summary ===")
    print(
        f"Unconstrained dummy chi2: {chi2_u_main:.3f} (sigma=49.6) vs {chi2_u_alt:.3f} (sigma=50.0)"
    )
    print(
        f"Anchored dummy chi2:      {chi2_a_main:.3f} (sigma=49.6) vs {chi2_a_alt:.3f} (sigma=50.0)"
    )
    print("Conclusion depends on this row only if these numbers differ enough to")
    print("cross the MULTING comparison values above -- check by eye.")
