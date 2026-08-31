"""P184 -- runs the DESI-uncertainty-homogenized rerun that FINDING_
P182 and FINDING_P183 both explicitly named as the only way to break
the DESI weight/redshift confound, per the user's direct request.

FINDING_P182 found DESI's leave-one-out deviation (dropping DESI gives
the largest, worst angle among the 8 high-z drops) is confounded: DESI
carries ~50x the chi2-weight of a typical other high-z point (sigma=2.8
vs 14-50.4), so its outsized influence could be entirely a measurement-
weight artifact, unrelated to its redshift. FINDING_P183's z^3-
regression across all 8 points hit the identical confound in a
different statistical framing.

Method: set DESI's sigma to the MEDIAN of the other 7 high-z points'
sigmas (20.0, matching the z=1.037 point's own sigma) -- neutralizing
its weight advantage while leaving its real H(z) value, its real
redshift, and its real measurement-TYPE (BAO/Lyman-alpha, vs cosmic
chronometers for the other 7) unchanged. Rerun the leave-one-out
analysis (FINDING_P179/P182) and the z^3-regression (FINDING_P183)
under this homogenized weighting.

If DESI's outsized leave-one-out influence was PURELY a weight
artifact, homogenizing its sigma should make it unremarkable among the
8 drops (like SH0ES already is). If it persists, the weight confound is
resolved but NOT the redshift-vs-measurement-type confound (DESI is
still the only BAO/Lyman-alpha point in an otherwise cosmic-chronometer
sample) -- this rerun can rule OUT "purely weight," but cannot, by
itself, rule IN "genuinely Taylor-truncation/redshift" over "genuinely
measurement-type."

CORRECTION (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing -- this dispatch DID include the actual source code,
confirmed by the skeptic itself, closing the gap named twice this
session in FINDING_P180/P183): a skeptic review raised 7 attacks. Two
were addressed by running the exact additional checks proposed, which
STRENGTHENED rather than weakened the finding; the rest are accepted
as wording/reporting corrections.

ADDRESSED, RESULT STRENGTHENS THE FINDING -- a single homogenized-
sigma choice is not a robustness test (skeptic's Attack 1): swept
sigma_DESI across the entire REALISTIC range spanned by the other 7
points' real sigmas (14.0 to 50.4) plus their mean (27.6). DESI remains
the max of 8 leave-one-out drops at EVERY one of these values. Only at
an unrealistic sigma=100 (2x the largest real measurement uncertainty
in the entire 33-point dataset) does DESI stop being strictly the max,
and even then by a negligible margin (0.0199 vs 0.01985). The original
single-value result was not fragile.

ADDRESSED, RESULT STRENGTHENS THE FINDING -- homogenizing only DESI
still leaves a 3.6x sigma spread among the other 7 (skeptic's Attack
5, "not true weight equalization"): reran with ALL 8 high-z sigmas set
to an identical common value (tested 20.0, 27.6, 30.0) -- true,
complete weight equalization. DESI STILL gives the largest leave-one-
out angle (0.01988 deg vs next-highest 0.01963 deg) at every value
tested. This is materially stronger evidence than the original single-
point-homogenized test that DESI's outsized influence is not a weight
artifact in any form.

ACCEPTED -- the full-8-point angle barely moves (0.01946 to 0.01950
deg, ~0.2%) under a ~50x weight cut, which is worth stating plainly
rather than only noting as a "sanity check": it suggests DESI's raw
chi2-weight was never the dominant driver of the FULL-sample fit
geometry to begin with -- the original P182 "~50x weight, therefore a
likely confound" framing somewhat overstated how much weight alone
was doing. This does not contradict the leave-one-out results above
(a point's PRESENCE vs its WEIGHT are different levers), but the
wording "RULES OUT the pure weight-artifact explanation" is too strong
given this; softened below.

ACCEPTED -- the z-score computed from only 7 (non-independent, same
issue FINDING_P183 already identified) leave-one-out angles is not a
formal significance number, and was printed without a live caveat in
the original draft. Retained as a descriptive distance only, with the
caveat now stated inline wherever printed, not just in a docstring.

ACCEPTED -- "naive-p" values printed without an inline caveat could be
misread as valid significance tests despite the docstring's warning.
Fixed: caveat now printed alongside every naive-p value, not just
noted once in prose.

ACCEPTED -- the sign-persistence test reported only sign, not
magnitude, hiding whether homogenization moved the slope substantially
toward zero (partial confound resolution) or barely at all. Fixed:
both slope values are now printed together for direct comparison.

ACCEPTED -- "measurement-type confound" was named without a concrete
causal mechanism, closer to "we don't know what else it could be" than
a specific, falsifiable alternative. Reworded below to state this
honestly, without withdrawing the point (DESI genuinely is the only
BAO/Lyman-alpha point in this subsample) but without dressing it up as
a fully specified hypothesis either.

NET RESULT: the core finding is upgraded, not weakened -- DESI's
outsized leave-one-out influence survives BOTH a realistic sigma sweep
AND a full weight-equalization variant, considerably stronger evidence
against "purely a weight artifact" than the single-value test alone.
The over-strong "RULES OUT" language and unflagged significance
numbers are corrected; the z^3-regression sign-mismatch with the
Taylor-truncation-leverage mechanism (FINDING_P183) persists unchanged
under every weighting scheme tested here.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy import stats
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own multing_core.py (same subset P176-P183 already
# used and positive-controlled)
# ---------------------------------------------------------------------------
MSUN_TO_KG = 1.98847e30
MPC_TO_M = 3.08567758e22
KEV_TO_J = 1.602176634e-16
KMSMPC_TO_SI = 3.24077929e-20
G = 6.674e-11
c = 299792458.0
Om_planck = 0.315
OL_planck = 0.685
H0_planck_si = 67.4 * KMSMPC_TO_SI

M0_kg = 1.193082e45
d0_m = 45.0 * MPC_TO_M
T0_keV = 3.7163
mu_mol = 0.6
m_proton = 1.67262192e-27
T_piv_keV = 2.27
Mgas_piv_kg = 2.28e13 * MSUN_TO_KG
z_piv = 0.25
B_real = 2.24
C_real = -1.00
f_merge = 0.25
f_coh = 1.0 / 3.0

rho_crit0 = 3.0 * H0_planck_si**2 / (8.0 * np.pi * G)


def Efun(z, Om=Om_planck, OL=OL_planck):
    return np.sqrt(Om * (1.0 + z) ** 3 + OL)


def M_of(z):
    return M0_kg * (1.0 + z) ** (-1.1)


def T_keV_of(z):
    return T0_keV * (M_of(z) / M0_kg) ** (2.0 / 3.0) * Efun(z) ** (2.0 / 3.0)


def Mgas_of(z):
    return Mgas_piv_kg * (T_keV_of(z) / T_piv_keV) ** B_real * (Efun(z) / Efun(z_piv)) ** C_real


def k_of(z):
    return 1.5 * (Mgas_of(z) / (mu_mol * m_proton)) * (T_keV_of(z) * KEV_TO_J)


def rho_crit(z):
    return rho_crit0 * Efun(z) ** 2


def R_of(z):
    return (3.0 * M_of(z) / (4.0 * np.pi * 500.0 * rho_crit(z))) ** (1.0 / 3.0)


def d_of(z):
    return d0_m * (1.0 + z) ** (-1.0)


def m_dot(z):
    return 1.1 * (H0_planck_si * Efun(z)) * M_of(z)


def v_infall(z):
    return np.sqrt(G * M_of(z) / R_of(z))


def F_accretion(z):
    return m_dot(z) * (f_coh * f_merge * v_infall(z))


def addot_over_a_eps(z, b1, b2, eps):
    M, R, k, d = M_of(z), R_of(z), k_of(z), d_of(z)
    F0 = (1 + eps) * (-G) * M * M / d**2
    F1 = b1 * (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2
    F2 = b2 * (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2
    F_total = F0 - F1 + F2 - F_accretion(z)
    return (F_total / (M / 2.0)) / d


CC_POINTS = [
    (0.07, 69.0, 19.6),
    (0.09, 69.0, 12.0),
    (0.12, 68.6, 26.2),
    (0.17, 83.0, 8.0),
    (0.179, 75.0, 4.0),
    (0.199, 75.0, 5.0),
    (0.2, 72.9, 29.6),
    (0.27, 77.0, 14.0),
    (0.28, 88.8, 36.6),
    (0.352, 83.0, 14.0),
    (0.38, 83.0, 13.5),
    (0.4, 95.0, 17.0),
    (0.4, 77.0, 10.2),
    (0.425, 87.1, 11.2),
    (0.45, 92.8, 12.9),
    (0.47, 89.0, 49.6),
    (0.478, 80.9, 9.0),
    (0.48, 97.0, 62.0),
    (0.593, 104.0, 13.0),
    (0.68, 92.0, 8.0),
    (0.781, 105.0, 12.0),
    (0.875, 125.0, 17.0),
    (0.88, 90.0, 40.0),
    (0.9, 117.0, 23.0),
    (1.037, 154.0, 20.0),
    (1.3, 168.0, 17.0),
    (1.363, 160.0, 33.6),
    (1.43, 177.0, 18.0),
    (1.53, 140.0, 14.0),
    (1.75, 202.0, 40.0),
    (1.965, 186.5, 50.4),
]
zd = np.array([p[0] for p in CC_POINTS])
Hd = np.array([p[1] for p in CC_POINTS])
sd = np.array([p[2] for p in CC_POINTS])

Z_SHOES, H_SHOES, SIG_SHOES = 0.0233, 73.04, 1.04
Z_DESI, H_DESI, SIG_DESI = 2.33, 236.1, 2.8

z33 = np.concatenate([zd, [Z_SHOES], [Z_DESI]])
H33 = np.concatenate([Hd, [H_SHOES], [H_DESI]])
s33_orig = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))
N_POINTS = len(z33)

HIGH_Z_MASK = z33 >= 1.0
HIGH_Z_INDICES = np.where(HIGH_Z_MASK)[0]

H0A0, B1_0, B2_0 = 73.22, 1.4335e10, 7.8067e17
C_IDEALIZED_LOCAL = 2.644421e07
V_PRED = np.array([C_IDEALIZED_LOCAL / B1_0, C_IDEALIZED_LOCAL**2 / B2_0, 1.0])

H1_HIGH_Z = 1e-5

# Homogenized sigma: DESI's sigma set to the median of the OTHER 7
# high-z points' sigmas -- neutralizes its ~50x weight advantage
# (FINDING_P182) while leaving redshift, H(z) value, and measurement
# TYPE unchanged.
_DESI_ARRAY_IDX = HIGH_Z_INDICES[np.argmin(np.abs(z33[HIGH_Z_INDICES] - Z_DESI))]
_OTHER_HIGH_Z_SIGMAS = s33_orig[HIGH_Z_INDICES][z33[HIGH_Z_INDICES] < Z_DESI]
SIG_DESI_HOMOG = float(np.median(_OTHER_HIGH_Z_SIGMAS))
S33_HOMOG = s33_orig.copy()
S33_HOMOG[_DESI_ARRAY_IDX] = SIG_DESI_HOMOG


def chi2_eps_indices(h0_anchor, beta1, beta2, eps, indices, s33_use):
    """Same construction as FINDING_P177-P183's chi2, generalized to
    accept an arbitrary sigma array (default behavior unchanged if
    s33_use=s33_orig is passed).
    """
    aa = np.array([addot_over_a_eps(zx, beta1, beta2, eps) for zx in ZFINE])
    integrand = aa / (1.0 + ZFINE)
    ds_raw = np.concatenate(([0.0], cumulative_trapezoid(integrand, ZFINE)))
    i0 = np.argmin(np.abs(ZFINE - Z_SHOES))
    ds = ds_raw - ds_raw[i0]
    H2 = (h0_anchor * KMSMPC_TO_SI) ** 2 + 2.0 * ds
    if np.any(H2 <= 0):
        return 1e12
    Hm = np.sqrt(H2) / KMSMPC_TO_SI
    idx = np.asarray(list(indices))
    Hp = np.interp(z33[idx], ZFINE, Hm)
    return np.sum(((Hp - H33[idx]) / s33_use[idx]) ** 2)


def null_direction_indices(indices, h1, s33_use, h3=0.02):
    """Same construction as FINDING_P178-P183's null_direction_subset,
    generalized to accept an arbitrary sigma array.
    """

    def f(x1, x2, x3):
        return chi2_eps_indices(H0A0, x1 * B1_0, x2 * B2_0, x3, indices, s33_use)

    def d2(i, j, base, hi, hj):
        if i == j:
            p, m = list(base), list(base)
            p[i] += hi
            m[i] -= hi
            return (f(*p) - 2 * f(*base) + f(*m)) / hi**2
        pp, pm, mp, mm = list(base), list(base), list(base), list(base)
        pp[i] += hi
        pp[j] += hj
        pm[i] += hi
        pm[j] -= hj
        mp[i] -= hi
        mp[j] += hj
        mm[i] -= hi
        mm[j] -= hj
        return (f(*pp) - f(*pm) - f(*mp) + f(*mm)) / (4 * hi * hj)

    base = (1.0, 1.0, 0.0)
    h11, h22, h33 = d2(0, 0, base, h1, h1), d2(1, 1, base, h1, h1), d2(2, 2, base, h3, h3)
    h12 = d2(0, 1, base, h1, h1)
    h13, h23 = d2(0, 2, base, h1, h3), d2(1, 2, base, h1, h3)
    hessian = np.array([[h11, h12, h13], [h12, h22, h23], [h13, h23, h33]])
    eigvals, eigvecs = np.linalg.eigh(hessian)
    v_null = eigvecs[:, 0]
    v_null = v_null / v_null[2]
    return eigvals, v_null


def angle_to_prediction(v_null):
    cos_angle = np.dot(v_null, V_PRED) / (np.linalg.norm(v_null) * np.linalg.norm(V_PRED))
    return np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))


def high_z_loo_labeled(s33_use):
    """Same leave-one-out computation as FINDING_P179/P182/P183, high-z
    subsample only, parameterized by which sigma array to use.
    """
    results = []
    for idx in HIGH_Z_INDICES:
        remaining = [i for i in HIGH_Z_INDICES if i != idx]
        _, v = null_direction_indices(remaining, H1_HIGH_Z, s33_use)
        results.append((z33[idx], angle_to_prediction(v)))
    return results


def test_positive_control_original_weights_match_prior_findings():
    """Positive control: with the ORIGINAL (unhomogenized) sigma array,
    reproduce FINDING_P179/P182/P183's own already-verified full-8
    high-z angle.
    """
    _, v = null_direction_indices(HIGH_Z_INDICES, H1_HIGH_Z, s33_orig)
    angle = angle_to_prediction(v)
    assert abs(angle - 0.01946) / 0.01946 < 0.02, f"angle={angle} != 0.01946"
    return angle


def test_homogenization_does_not_wildly_change_full_sample_angle():
    """Sanity check: homogenizing DESI's weight should shift the
    full-8-point angle only modestly (it changes the fit, but should
    not produce a wildly different geometry) -- confirms the
    homogenized-weight chi2 machinery is well-behaved, not broken.
    """
    _, v = null_direction_indices(HIGH_Z_INDICES, H1_HIGH_Z, S33_HOMOG)
    angle = angle_to_prediction(v)
    assert abs(angle - 0.01946) / 0.01946 < 0.10, (
        f"homogenized full-8 angle ({angle}) shifted implausibly far from original (0.01946)"
    )
    return angle


def test_desi_still_the_max_after_homogenization():
    """The key test: even with DESI's chi2-weight neutralized to match
    the other high-z points, dropping DESI must STILL give the largest
    (worst) angle among the 8 leave-one-out drops -- if this holds, the
    weight confound is resolved but DESI's outsized influence persists,
    ruling OUT "purely a weight artifact."
    """
    results = high_z_loo_labeled(S33_HOMOG)
    desi_angle = [a for z, a in results if abs(z - Z_DESI) < 1e-6][0]
    all_angles = [a for _, a in results]
    assert desi_angle == max(all_angles), (
        f"DESI ({desi_angle}) is no longer the max after homogenization -- "
        f"the weight confound may fully explain the original P182 finding"
    )
    return results, desi_angle


def test_desi_deviation_descriptive_distance():
    """Reports a DESCRIPTIVE distance only (not a formal significance
    number, per FINDING_P183's own caution about non-independent LOO
    samples, and the skeptic's added point that n=7's own std is itself
    a biased, unreliable estimator) -- how far DESI's homogenized-weight
    leave-one-out angle sits from the other 7's own spread.
    """
    results, desi_angle = test_desi_still_the_max_after_homogenization()
    other = np.array([a for z, a in results if abs(z - Z_DESI) >= 1e-6])
    distance_ratio = abs(desi_angle - other.mean()) / other.std()
    assert distance_ratio > 2.0, (
        f"expected DESI's homogenized deviation to remain a notable outlier "
        f"(ratio={distance_ratio}); if this fails, the persistence claim should be revisited"
    )
    return distance_ratio


def test_sigma_sweep_desi_remains_max_across_realistic_range():
    """Skeptic-requested robustness check (Attack 1): a single
    homogenized-sigma choice is not a robustness test. Sweeps
    sigma_DESI across the entire REALISTIC range spanned by the other 7
    high-z points' own real sigmas (14.0 to 50.4) plus their mean.
    DESI must remain the max leave-one-out drop at every one of these
    -- if it doesn't, the single-value P184 finding was fragile.
    """
    sweep_values = [14.0, 17.0, 20.0, float(np.mean(_OTHER_HIGH_Z_SIGMAS)), 33.6, 40.0, 50.4]
    outcomes = {}
    for sig_val in sweep_values:
        s33_test = s33_orig.copy()
        s33_test[_DESI_ARRAY_IDX] = sig_val
        results = high_z_loo_labeled(s33_test)
        desi_a = [a for z, a in results if abs(z - Z_DESI) < 1e-6][0]
        all_a = [a for _, a in results]
        outcomes[sig_val] = desi_a == max(all_a)
    assert all(outcomes.values()), (
        f"DESI is NOT the max at every realistic sigma value: {outcomes} -- "
        "the single-value P184 finding may have been fragile"
    )
    return outcomes


def test_fully_equalized_all_8_sigmas_desi_still_max():
    """Skeptic-requested stronger test (Attack 5): homogenizing only
    DESI still leaves a 3.6x sigma spread among the other 7 -- not true
    weight equalization. This test sets ALL 8 high-z sigmas to an
    identical common value (true, complete weight equalization) and
    checks DESI still gives the largest leave-one-out angle. This is
    materially stronger evidence than the single-point-homogenized test.
    """
    common_values = [20.0, float(np.mean(_OTHER_HIGH_Z_SIGMAS)), 30.0]
    outcomes = {}
    for common_sig in common_values:
        s33_test = s33_orig.copy()
        for idx in HIGH_Z_INDICES:
            s33_test[idx] = common_sig
        results = high_z_loo_labeled(s33_test)
        desi_a = [a for z, a in results if abs(z - Z_DESI) < 1e-6][0]
        all_a = [a for _, a in results]
        outcomes[common_sig] = (desi_a == max(all_a), desi_a)
    assert all(v[0] for v in outcomes.values()), (
        f"DESI is NOT the max under full weight equalization: {outcomes} -- "
        "this would substantially weaken the 'not purely weight' conclusion"
    )
    return outcomes


def test_z3_regression_sign_still_opposes_mechanism():
    """Independently checks whether FINDING_P183's sign-mismatch
    (observed slope positive, mechanism predicts negative) survives
    weight-homogenization. If the sign flips to negative once the
    weight confound is removed, that would be a real update in favor
    of the Taylor-truncation-leverage mechanism; if it stays positive,
    the mechanism-opposing observation is independent of the weight
    confound. Also reports (skeptic's Attack 6) the ORIGINAL
    unhomogenized slope for direct magnitude comparison, not just sign.
    """
    results_homog = high_z_loo_labeled(S33_HOMOG)
    z_dropped = np.array([z for z, _ in results_homog])
    angles_homog = np.array([a for _, a in results_homog])
    z3 = z_dropped**3
    res_homog = stats.linregress(z3, angles_homog)

    results_orig = high_z_loo_labeled(s33_orig)
    angles_orig = np.array([a for _, a in results_orig])
    res_orig = stats.linregress(z3, angles_orig)

    assert res_homog.slope > 0, (
        f"expected the sign-mismatch to persist under homogenization (slope={res_homog.slope}); "
        "if this fails, FINDING_P183's mechanism-opposing conclusion needs revisiting"
    )
    return res_homog, res_orig


if __name__ == "__main__":
    print(
        f"Homogenized DESI sigma: {SIG_DESI_HOMOG} (was {SIG_DESI}, ~{(20.0 / SIG_DESI) ** 2:.0f}x weight cut)\n"
    )

    angle_orig = test_positive_control_original_weights_match_prior_findings()
    print(f"Positive control: original-weight full high-z angle = {angle_orig:.5f} deg -- PASS\n")

    angle_homog_full = test_homogenization_does_not_wildly_change_full_sample_angle()
    print(
        f"Homogenized-weight full high-z angle: {angle_homog_full:.5f} deg (sanity check -- PASS)\n"
    )

    print("=" * 70)
    print("High-z leave-one-out with DESI sigma homogenized, labeled by z")
    print("=" * 70)
    results, desi_angle = test_desi_still_the_max_after_homogenization()
    for z, a in results:
        tag = " <-- DESI (sigma homogenized)" if abs(z - Z_DESI) < 1e-6 else ""
        print(f"  drop z={z:.4f}: angle={a:.5f} deg{tag}")

    distance_ratio = test_desi_deviation_descriptive_distance()
    print(
        f"\nDESI drop is STILL the max of 8 (descriptive distance from other-7 mean, "
        f"in units of their own std -- NOT a formal significance test, n=7 non-"
        f"independent samples: {distance_ratio:.2f})"
    )

    print()
    print("=" * 70)
    print("Robustness check 1: sigma sweep across the realistic range (skeptic Attack 1)")
    print("=" * 70)
    sweep_outcomes = test_sigma_sweep_desi_remains_max_across_realistic_range()
    for sig_val, is_max in sweep_outcomes.items():
        print(f"  sigma_DESI={sig_val:.1f}: DESI is max = {is_max}")
    print("  (all realistic values: DESI remains max -- PASS)")

    print()
    print("=" * 70)
    print("Robustness check 2: FULL weight equalization, all 8 sigmas equal (Attack 5)")
    print("=" * 70)
    equal_outcomes = test_fully_equalized_all_8_sigmas_desi_still_max()
    for common_sig, (is_max, desi_a) in equal_outcomes.items():
        print(f"  common_sigma={common_sig:.2f}: DESI-drop-angle={desi_a:.5f}  is_max={is_max}")
    print("  (true weight equalization: DESI STILL max -- PASS, stronger than check 1)")

    res_homog, res_orig = test_z3_regression_sign_still_opposes_mechanism()
    print()
    print("=" * 70)
    print("z^3-regression: homogenized vs original slope (skeptic Attack 6)")
    print("=" * 70)
    print(
        f"  ORIGINAL weights:     slope={res_orig.slope:.3e}  r^2={res_orig.rvalue**2:.4f}  "
        f"naive-p={res_orig.pvalue:.4f}  [non-independent LOO samples; not a valid p-value]"
    )
    print(
        f"  HOMOGENIZED weights:  slope={res_homog.slope:.3e}  r^2={res_homog.rvalue**2:.4f}  "
        f"naive-p={res_homog.pvalue:.4f}  [non-independent LOO samples; not a valid p-value]"
    )
    print("  Both slopes POSITIVE -- opposite the mechanism's predicted NEGATIVE sign")

    print()
    print(
        "CONCLUSION (see module Correction for the full set of skeptic-caught wording "
        "fixes): homogenizing DESI's chi2-weight does NOT make its leave-one-out "
        "influence unremarkable -- confirmed robustly across a realistic sigma sweep "
        "AND a full weight-equalization variant (all 8 high-z sigmas set identical), "
        "not just the single original value. This is real evidence that DESI's outsized "
        "influence is NOT purely a weight artifact -- stronger evidence than the single-"
        "value test alone provided. However: the full-8-point angle barely moves under "
        "a ~50x weight cut (0.01946 to 0.01950 deg, ~0.2%), suggesting DESI's raw weight "
        "was never the dominant driver of the FULL-sample fit geometry to begin with -- "
        "a point's PRESENCE and its WEIGHT are different levers, and this result is about "
        "presence, not weight, primarily. The z^3-regression's slope sign remains "
        "POSITIVE under every weighting scheme tested, opposite what the diffuse "
        "Taylor-truncation-leverage mechanism (FINDING_P183) predicts -- homogenizing "
        "the weight did not fix that sign mismatch. A genuine, still-unspecified "
        "confound remains: DESI is the only BAO/Lyman-alpha measurement in an otherwise "
        "all-cosmic-chronometer high-z subsample -- 'furthest in redshift' and 'only "
        "point of this measurement type' remain entangled for this one point, with no "
        "concrete mechanism proposed for why measurement type specifically would matter. "
        "FINDING_P177's open question remains unresolved."
    )
