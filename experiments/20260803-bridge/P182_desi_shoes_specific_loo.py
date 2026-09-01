"""P182 -- runs the low-z-vs-high-z discriminator again, this time
USING the leave-one-out results FINDING_P179 already computed and
validated, per the user's direct request ("try low-z vs high-z on the
leave-one-out results again"). FINDING_P179 established the low-z
(0.0062 deg) vs high-z (0.0195 deg) angle ordering is a real, stable,
well-isolated numeric fact -- but explicitly left FINDING_P177's
original question (genuine correspondence vs. Taylor-truncation
leverage) unresolved, since establishing RELIABILITY of the ordering
is a different question from using it to actually DISCRIMINATE between
the two explanations.

This file completes that discrimination attempt using the leave-one-out
results themselves, not just their aggregate stability. The
"Taylor-truncation leverage" concern (FINDING_P177's own framing):
V_PRED is an idealized LOCAL (z=0-centered, 2nd-order Taylor expansion)
construction -- it may match well specifically for data near its own
expansion point (z=0, low-z) simply because Taylor expansions are most
accurate near their expansion point, and progressively worse further
away. Under this mechanism, DESI (z=2.33, the single most extreme,
furthest-from-z=0 point in the entire 33-point dataset) should be the
SINGLE MOST INFLUENTIAL point pulling the high-z near-null direction
away from V_PRED -- so dropping DESI specifically should produce the
LARGEST IMPROVEMENT (angle decrease) among all 8 high-z leave-one-out
drops, if this mechanism is real and DESI-driven.

Symmetric check on the low-z side: SHOES (z=0.0233, FINDING_P178's own
established zero-curvature-contribution point) should show NO special
behavior when dropped, unlike a genuine, informative low-z point.

CORRECTION (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing -- the first draft's "argues AGAINST DESI-specific
Taylor leverage" conclusion is RETRACTED and replaced with an honest
"inconclusive, and confounded" verdict): a skeptic review (given the
actual code) raised several attacks, independently checked before
accepting.

ACCEPTED, CONFIRMED BY DIRECT CHECK -- fatal confound: DESI's
measurement uncertainty (sigma=2.8) is dramatically smaller than every
other high-z point's (14-50.4, median ~20) -- DESI carries roughly 50x
the chi2-WEIGHT (1/sigma^2) of a typical other high-z point. Since the
near-null eigenvector is shaped by the WEIGHTED residual structure,
dropping DESI is expected to shift that eigenvector by an outsized
amount purely from removing a disproportionately heavy data point --
completely independent of DESI's redshift/Taylor-distance. "Furthest
from z=0" and "highest chi2-weight" are perfectly confounded for this
one point in this dataset; this file's design cannot separate them.

ACCEPTED: the "DESI-drop should show the LARGEST IMPROVEMENT if
Taylor-leverage is real" prediction was a strawman of the actual
(diffuse) leverage hypothesis. A properly diffuse model (leverage
roughly proportional to z^3 for each point) predicts DESI's marginal
leverage over the next-most-extreme high-z point (z=1.965) is only
~1.7x, not dominant -- such a model predicts mild point-to-point
variation among all 8 drops, not a single stark outlier, and does NOT
specifically predict "DESI drop looks different from the rest" in the
way this file's docstring originally claimed.

CHECKED, NOT SIMPLY ACCEPTED -- the specific claim that the observed
effect (~0.0003 deg) is "within 1 std of noise" (skeptic's own number,
using FINDING_P179's own established high-z jackknife std=0.00035 deg)
is ITSELF methodologically questionable and was independently
re-derived, not taken at face value: that jackknife std is computed
from the spread of ALL 8 leave-one-out values, INCLUDING the DESI-drop
value being tested for being an outlier -- an outlier inflates the very
statistic used to judge whether it's an outlier (a form of circularity).
Excluding DESI from its own reference set (comparing it only to the
spread of the OTHER 7 drops) gives a much higher apparent significance
(z~3.7-9 depending on whether the small-n=7 std is jackknife-corrected)
-- but that alternative is itself unstable, built from only 7 points
whose own std is poorly estimated. Net: the significance of DESI's
deviation is GENUINELY AMBIGUOUS, swinging from ~1 sigma to ~4-9 sigma
depending on which standard, defensible statistic is used -- this
ambiguity is reported explicitly below, not resolved by picking
whichever number sounds better.

ACCEPTED: the first draft used the MEAN of the 8 leave-one-out angles
as a stand-in for the real full-8-point angle, without directly
computing the latter. Fixed: the real, non-leave-one-out full-sample
angle is now computed directly and used throughout.

ACCEPTED: the SHOES sanity check (falls within [min,max] of the other
7) was weak -- strengthened to require it fall close to their MEAN
(within 1 std), which it does (checked).

NET RESULT: this file's original conclusion ("dropping DESI argues
against DESI-specific Taylor leverage") does NOT survive. The correct,
honest conclusion is that this specific test -- leave-one-out applied
to identify a single dominant point -- cannot discriminate here,
because DESI's outsized measurement precision is a complete,
unresolvable (with this dataset) confound for its outsized redshift,
and even setting that aside, the statistical significance of its
leave-one-out deviation is itself ambiguous depending on reference
statistic. FINDING_P177's open question (genuine correspondence vs.
Taylor-truncation leverage) remains as unresolved as FINDING_P179 left
it -- this file neither narrows nor rules out either explanation.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np

# Shared TJB v82 physics kernel (constants + Efun..addot_over_a_eps) --
# see _v82_shared_physics.py docstring for extraction provenance.
from _v82_shared_physics import (
    KMSMPC_TO_SI,
    addot_over_a_eps,
)
from scipy.integrate import cumulative_trapezoid

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
s33 = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))
N_POINTS = len(z33)

LOW_Z_MASK = z33 <= 0.2
HIGH_Z_MASK = z33 >= 1.0
LOW_Z_INDICES = np.where(LOW_Z_MASK)[0]
HIGH_Z_INDICES = np.where(HIGH_Z_MASK)[0]

H0A0, B1_0, B2_0 = 73.22, 1.4335e10, 7.8067e17
C_IDEALIZED_LOCAL = 2.644421e07
V_PRED = np.array([C_IDEALIZED_LOCAL / B1_0, C_IDEALIZED_LOCAL**2 / B2_0, 1.0])

# Converged step sizes -- FINDING_P178's own explicit sweep, reused
# unchanged in FINDING_P179.
H1_LOW_Z = 1e-5
H1_HIGH_Z = 1e-5


def chi2_eps_indices(h0_anchor, beta1, beta2, eps, indices):
    """Same construction as FINDING_P177/P178/P179's chi2."""
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
    return np.sum(((Hp - H33[idx]) / s33[idx]) ** 2)


def null_direction_indices(indices, h1, h3=0.02):
    """Same construction as FINDING_P178/P179's null_direction_subset."""

    def f(x1, x2, x3):
        return chi2_eps_indices(H0A0, x1 * B1_0, x2 * B2_0, x3, indices)

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


def leave_one_out_labeled(indices, h1):
    """Same computation as FINDING_P179's leave_one_out_angles, but
    returns (z_dropped, angle) pairs instead of a bare array -- needed
    to identify DESI/SHOES specifically rather than relying on array
    position.
    """
    results = []
    for idx in indices:
        remaining = [i for i in indices if i != idx]
        _, v = null_direction_indices(remaining, h1)
        results.append((z33[idx], angle_to_prediction(v)))
    return results


def test_positive_control_matches_p179():
    """Positive control: reproduce FINDING_P179's own already-verified
    leave-one-out angle arrays (mean/range) for both subsamples, AND
    the real (non-LOO) full-sample angles (skeptic-requested fix --
    the LOO mean is not used as a full-sample proxy here, see
    Correction).
    """
    low = leave_one_out_labeled(LOW_Z_INDICES, H1_LOW_Z)
    high = leave_one_out_labeled(HIGH_Z_INDICES, H1_HIGH_Z)
    low_angles = np.array([a for _, a in low])
    high_angles = np.array([a for _, a in high])
    assert abs(low_angles.mean() - 0.00620) / 0.00620 < 0.02
    assert abs(high_angles.mean() - 0.01952) / 0.01952 < 0.02

    _, v_low_real = null_direction_indices(LOW_Z_INDICES, H1_LOW_Z)
    _, v_high_real = null_direction_indices(HIGH_Z_INDICES, H1_HIGH_Z)
    angle_low_real = angle_to_prediction(v_low_real)
    angle_high_real = angle_to_prediction(v_high_real)
    assert abs(angle_low_real - 0.0062) / 0.0062 < 0.02
    assert abs(angle_high_real - 0.0195) / 0.0195 < 0.02
    return low, high, angle_low_real, angle_high_real


def test_shoes_drop_close_to_mean():
    """Strengthened per skeptic request: SHOES, already established to
    contribute zero curvature (FINDING_P178/P179), must fall close to
    the MEAN of the other 7 low-z leave-one-out drops (within 1 std),
    not merely somewhere inside their range (a much weaker bar, true
    for ~75% of draws from any common distribution by chance).
    """
    low, _, _, _ = test_positive_control_matches_p179()
    shoes_angle = [a for z, a in low if abs(z - Z_SHOES) < 1e-6][0]
    other = np.array([a for z, a in low if abs(z - Z_SHOES) >= 1e-6])
    z_score = abs(shoes_angle - other.mean()) / other.std()
    assert z_score < 1.0, f"SHOES drop is {z_score:.2f} std from the other-7 mean, not close"
    return shoes_angle, other, z_score


def test_desi_weight_confound_is_real():
    """Confirms (does not paper over) the skeptic-caught fatal confound:
    DESI's measurement uncertainty is dramatically smaller than the
    other high-z points', giving it outsized chi2-weight independent of
    its redshift. This is reported as a documented limitation, not
    something this file can resolve.
    """
    high_z_sigmas = s33[HIGH_Z_INDICES]
    desi_sigma = s33[HIGH_Z_INDICES][np.argmin(np.abs(z33[HIGH_Z_INDICES] - Z_DESI))]
    other_sigmas = high_z_sigmas[np.abs(z33[HIGH_Z_INDICES] - Z_DESI) >= 1e-6]
    weight_ratio = (np.median(other_sigmas) / desi_sigma) ** 2
    assert weight_ratio > 10, (
        "expected DESI to carry substantially more chi2-weight; confound not confirmed"
    )
    return weight_ratio


def test_desi_deviation_significance_is_ambiguous():
    """Reports (does not resolve) the skeptic-caught significance
    ambiguity: DESI's leave-one-out deviation, measured against the
    OTHER 7 drops' own spread (excluding DESI from its own reference,
    jackknife-corrected for n=7), versus measured against FINDING_P179's
    own already-established high-z jackknife std (which includes DESI's
    own value, inflating the reference). Both z-scores are returned;
    no single verdict is asserted here beyond "these disagree."
    """
    _, high, _, angle_high_real = test_positive_control_matches_p179()
    desi_angle = [a for z, a in high if abs(z - Z_DESI) < 1e-6][0]
    other_high = np.array([a for z, a in high if abs(z - Z_DESI) >= 1e-6])

    z_excl_desi = abs(desi_angle - other_high.mean()) / (other_high.std() * np.sqrt(6))
    p179_jackknife_std = 0.00035  # FINDING_P179's own established value
    z_incl_desi = abs(desi_angle - angle_high_real) / p179_jackknife_std

    assert z_excl_desi > z_incl_desi, (
        "expected the exclude-DESI z-score to exceed the include-DESI one "
        "(the latter is inflated by DESI's own value); if this ever fails, "
        "the module Correction's ambiguity claim should be revisited"
    )
    return desi_angle, other_high, z_excl_desi, z_incl_desi


if __name__ == "__main__":
    low, high, angle_low_real, angle_high_real = test_positive_control_matches_p179()
    print("Positive control: matches FINDING_P179's LOO arrays + real full-sample angles -- PASS")
    print(
        f"Real full low-z angle: {angle_low_real:.5f} deg, real full high-z angle: {angle_high_real:.5f} deg\n"
    )

    print("=" * 70)
    print("LOW-z leave-one-out, labeled by z dropped")
    print("=" * 70)
    for z, a in low:
        tag = " <-- SHOES (known zero-contribution)" if abs(z - Z_SHOES) < 1e-6 else ""
        print(f"  drop z={z:.4f}: angle={a:.5f} deg{tag}")

    print()
    print("=" * 70)
    print("HIGH-z leave-one-out, labeled by z dropped")
    print("=" * 70)
    for z, a in high:
        tag = " <-- DESI" if abs(z - Z_DESI) < 1e-6 else ""
        print(f"  drop z={z:.4f}: angle={a:.5f} deg{tag}")

    print()
    shoes_angle, other_low, shoes_z = test_shoes_drop_close_to_mean()
    print(
        f"SHOES drop ({shoes_angle:.5f}) is {shoes_z:.2f} std from other-7 mean -- close, as expected.\n"
    )

    weight_ratio = test_desi_weight_confound_is_real()
    print(
        f"DESI chi2-weight vs median other high-z point: ~{weight_ratio:.0f}x -- FATAL CONFOUND\n"
    )

    desi_angle, other_high, z_excl, z_incl = test_desi_deviation_significance_is_ambiguous()
    print(f"DESI drop: {desi_angle:.5f} deg")
    print(
        f"Significance excluding DESI from its own reference (jackknife, n=7): {z_excl:.2f} sigma"
    )
    print(
        f"Significance including DESI in the reference (P179's own jackknife std): {z_incl:.2f} sigma"
    )
    print()
    print(
        "CONCLUSION (substantially revised from the first draft, see module "
        "Correction): this file does NOT establish that dropping DESI argues "
        "against DESI-specific Taylor-truncation leverage. Two fatal problems: "
        "(1) DESI's measurement uncertainty is far smaller than the other high-z "
        "points', giving it outsized chi2-weight completely confounded with its "
        "redshift distance -- this test cannot separate 'DESI matters because it "
        "is far from z=0' from 'DESI matters because it is precisely measured'; "
        "(2) the statistical significance of DESI's leave-one-out deviation is "
        "itself ambiguous, swinging from ~1 sigma to several sigma depending on "
        "which standard reference statistic is used. FINDING_P177's open question "
        "(genuine correspondence vs. Taylor-truncation leverage) remains exactly "
        "as unresolved as FINDING_P179 left it."
    )
