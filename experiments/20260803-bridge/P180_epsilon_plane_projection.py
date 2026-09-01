"""P180 -- runs the comparison FINDING_P178's own "what this file does
NOT establish" section named as undone (and the user explicitly asked
to try): compare FINDING_P165/P175's predicted epsilon-compensation
direction (V_PRED) to the FULL 2D near-degenerate plane the two
smallest eigenvalues (lambda1, lambda2) span, not to a single
arbitrarily-picked eigenvector (v1) as FINDING_P177/P178/P179 did.

Motivation: FINDING_P179 showed |lambda1/lambda2| is 8-10 orders of
magnitude below 1 in every LEAVE-ONE-OUT run, meaning v1 (the smallest-
eigenvalue eigenvector) IS a numerically well-isolated, non-arbitrary
direction there. This file separately confirms the same holds for the
three BASE samples this file actually uses (full-33pt, low-z 8pt,
high-z 8pt -- not the 7-point leave-one-out variants), and asks: even
granting v1 is well-isolated from v2, does V_PRED's small angle to v1
(0.006-0.02 deg, from FINDING_P177/P178) reflect the STIFF (v3, well-
constrained) direction of the real fit at all, or does it lie entirely
within the flat, poorly-constrained (v1,v2) plane -- meaning the data
barely constrains the "disagreement" at all?

CORRECTION (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing): the first draft additionally computed an in-plane
"mixing_angle" (how far V_PRED's projection sits from the v1 axis
versus the v2 axis within the plane) and presented it as SEPARATE
confirming evidence that V_PRED is "specific to v1, not generic within
the plane." A skeptic review -- despite a prompt-construction error on
this project's side that omitted the actual source code, so the review
worked from the claim and reported numbers only -- proved this framing
wrong from first principles, independently re-derived and confirmed
here: for the orthogonal decomposition V_PRED = a1*v1 + a2*v2 + a3*v3,
the three angles satisfy the EXACT spherical-right-triangle identity
`cos(full_angle) = cos(angle_to_plane) * cos(mixing_angle)` -- not
merely a small-angle approximation. Checked numerically against all
three samples: `sqrt(angle_to_plane^2 + mixing_angle^2)` matches
`full_angle` to ~1e-11 deg (floating-point noise), confirming the exact
identity holds, not just approximately. This means mixing_angle carries
NO independent information beyond full_angle and angle_to_plane -- it
is not a second, corroborating measurement, and the "specific to v1 vs
generic in-plane" claim built on it is RETRACTED. The only genuinely
new, non-redundant quantity this file adds is angle_to_plane itself.
Also added: an explicit lambda1/lambda2 check for the three BASE
samples (the skeptic could not assume this without seeing the numbers;
P179 only checked the 7-point leave-one-out variants) -- confirmed well
separated (~1e-8 to 1e-9) in all three, so v1 is not an arbitrary choice
within a near-degenerate pair here either. Also noted honestly: V_PRED's
coordinate NORMALIZATION uses the fitted beta1_0, beta2_0 (to match the
Hessian's own rescaled coordinates) even though its underlying constant
C_IDEALIZED_LOCAL (FINDING_P175) comes from independent z=0 baseline
quantities, not from beta1/beta2 fitting -- V_PRED is not claimed to be
fully unrelated to the real fit. And: no rigorous statistical null
distribution is offered for "how surprising" a given angle_to_plane
value is -- the comparison here is descriptive (angle_to_plane relative
to the already-known full_angle), not a calibrated significance test.

Method: decompose V_PRED exactly in the orthonormal eigenbasis
(v1, v2, v3) of the real 3x3 (beta1, beta2, epsilon) Hessian, at TJB's
own real fit point, for three cases: the full 33-point sample, the
low-z 8-point subsample, and the high-z 8-point subsample (same
construction as FINDING_P177/P178/P179's chi2, reproduced verbatim).

  angle_to_plane  = angle between V_PRED and its own projection onto
                    span(v1, v2) -- how much of V_PRED points into the
                    STIFF (v3) direction at all. This is the one new,
                    non-redundant quantity.
  mixing_angle    = angle, WITHIN the 2D plane, between V_PRED's
                    projection and the v1 axis -- reported for
                    completeness and as an exact-identity sanity check
                    on the code (see Correction), NOT as independent
                    evidence of anything.

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
FULL_INDICES = np.arange(N_POINTS)

H0A0, B1_0, B2_0 = 73.22, 1.4335e10, 7.8067e17
C_IDEALIZED_LOCAL = 2.644421e07
V_PRED = np.array([C_IDEALIZED_LOCAL / B1_0, C_IDEALIZED_LOCAL**2 / B2_0, 1.0])

# Converged step sizes. LOW/HIGH: FINDING_P178's own explicit sweep.
# FULL: swept here -- h1=1e-4 reproduces FINDING_P177's own reported
# eigenvalues (-1.14e-6, 70.6, 588321) and angle (0.0172 deg) exactly;
# h1=1e-3 is NOT yet converged (gives 0.066 deg, wrong by 4x) and
# h1=1e-2 breaks entirely (wrong eigenvalue ordering) -- included as a
# documented convergence check, not left as an unverified guess.
H1_FULL = 1e-4
H1_LOW_Z = 1e-5
H1_HIGH_Z = 1e-5


def chi2_eps_indices(h0_anchor, beta1, beta2, eps, indices):
    """Same construction as FINDING_P177/P178/P179's chi2_eps_subset."""
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


def hessian_eig_indices(indices, h1, h3=0.02):
    """Real numeric 3x3 Hessian in rescaled (x1=beta1/beta1_fit,
    x2=beta2/beta2_fit, eps) coordinates, diagonalized. Returns eigvals
    ascending and the ORTHONORMAL eigenvector matrix (columns), not
    rescaled -- rescaling is done downstream only where needed.
    """

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
    return np.linalg.eigh(hessian)


def angle_to_prediction_from_v1(v1_raw):
    """Same metric FINDING_P177/P178/P179 used: rescale v1 so its
    eps-component is 1 (matching V_PRED's own normalization), then take
    the basis-independent angle to V_PRED.
    """
    v = v1_raw / v1_raw[2]
    cos_angle = np.dot(v, V_PRED) / (np.linalg.norm(v) * np.linalg.norm(V_PRED))
    return np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))


def plane_diagnostics(indices, h1, h3=0.02):
    """Exact decomposition of V_PRED in the orthonormal eigenbasis
    (v1, v2, v3): V_PRED = a1*v1 + a2*v2 + a3*v3. From this,
    angle_to_plane (deviation into the stiff v3 direction) and
    mixing_angle (in-plane specificity to v1 versus v2) follow exactly,
    with no approximation.
    """
    eigvals, eigvecs = hessian_eig_indices(indices, h1, h3)
    v1, v2, v3 = eigvecs[:, 0], eigvecs[:, 1], eigvecs[:, 2]
    full_angle = angle_to_prediction_from_v1(v1)
    a1, a2, a3 = np.dot(V_PRED, v1), np.dot(V_PRED, v2), np.dot(V_PRED, v3)
    full_norm = np.linalg.norm(V_PRED)
    angle_to_plane = np.degrees(np.arcsin(np.clip(abs(a3) / full_norm, -1, 1)))
    mixing_angle = np.degrees(np.arctan2(abs(a2), abs(a1)))
    return {
        "eigvals": eigvals,
        "full_angle_v1_deg": full_angle,
        "angle_to_plane_deg": angle_to_plane,
        "mixing_angle_deg": mixing_angle,
        "lam1_lam2_ratio": abs(eigvals[0] / eigvals[1]),
        "lam2_lam3_ratio": abs(eigvals[1] / eigvals[2]),
    }


def test_positive_control_full_sample_matches_p177():
    """Positive control: the full-33-point full_angle_v1 must reproduce
    FINDING_P177's own already-verified 0.0172 deg (and its reported
    eigenvalues -1.14e-6, 70.6, 588321) to within 1%.
    """
    d = plane_diagnostics(FULL_INDICES, H1_FULL)
    assert abs(d["full_angle_v1_deg"] - 0.0172) / 0.0172 < 0.01, (
        f"full-sample angle {d['full_angle_v1_deg']} != 0.0172"
    )
    assert abs(d["eigvals"][1] - 70.6) / 70.6 < 0.01, f"lambda2 {d['eigvals'][1]} != 70.6"
    return d


def test_positive_control_subsamples_match_p178_p179():
    """Positive control: low-z/high-z full_angle_v1 must reproduce
    FINDING_P178/P179's own already-verified 0.0062/0.0195 deg to
    within 1%.
    """
    d_low = plane_diagnostics(LOW_Z_INDICES, H1_LOW_Z)
    d_high = plane_diagnostics(HIGH_Z_INDICES, H1_HIGH_Z)
    assert abs(d_low["full_angle_v1_deg"] - 0.0062) / 0.0062 < 0.01
    assert abs(d_high["full_angle_v1_deg"] - 0.0195) / 0.0195 < 0.01
    return d_low, d_high


def test_v_pred_lies_almost_entirely_in_the_flat_plane():
    """V_PRED's deviation from v1 must be almost entirely WITHIN the
    flat (v1,v2) plane, not into the stiff v3 direction -- i.e.
    angle_to_plane << full_angle_v1, for all three samples. This is the
    file's one genuinely new, non-redundant quantity (see Correction).
    """
    for label, idx, h1 in [
        ("full", FULL_INDICES, H1_FULL),
        ("low-z", LOW_Z_INDICES, H1_LOW_Z),
        ("high-z", HIGH_Z_INDICES, H1_HIGH_Z),
    ]:
        d = plane_diagnostics(idx, h1)
        assert d["angle_to_plane_deg"] < 0.1 * d["full_angle_v1_deg"], (
            f"{label}: angle_to_plane {d['angle_to_plane_deg']} not << "
            f"full_angle {d['full_angle_v1_deg']}"
        )


def test_lambda1_lambda2_separation_in_base_samples():
    """Skeptic-requested check (not covered by FINDING_P179, which only
    checked the 7-point leave-one-out variants): for the three BASE
    samples this file actually uses (full-33pt, low-z 8pt, high-z 8pt),
    lambda1 must be well separated from lambda2 -- otherwise "v1" would
    be an arbitrary choice within a near-degenerate pair, and comparing
    V_PRED against it specifically would be meaningless.
    """
    for label, idx, h1 in [
        ("full", FULL_INDICES, H1_FULL),
        ("low-z", LOW_Z_INDICES, H1_LOW_Z),
        ("high-z", HIGH_Z_INDICES, H1_HIGH_Z),
    ]:
        d = plane_diagnostics(idx, h1)
        assert d["lam1_lam2_ratio"] < 1e-4, (
            f"{label}: lambda1/lambda2={d['lam1_lam2_ratio']:.3e} not well separated"
        )


def test_exact_spherical_identity_holds():
    """Skeptic-caught correction (see module Correction): mixing_angle
    is NOT independent evidence -- it is exactly determined by
    full_angle and angle_to_plane via the spherical-right-triangle
    identity cos(full) = cos(angle_to_plane) * cos(mixing_angle). This
    test verifies that identity holds to numerical precision, as a
    correctness check on the decomposition code (NOT a physics claim).
    """
    for label, idx, h1 in [
        ("full", FULL_INDICES, H1_FULL),
        ("low-z", LOW_Z_INDICES, H1_LOW_Z),
        ("high-z", HIGH_Z_INDICES, H1_HIGH_Z),
    ]:
        d = plane_diagnostics(idx, h1)
        full_rad = np.radians(d["full_angle_v1_deg"])
        plane_rad = np.radians(d["angle_to_plane_deg"])
        mix_rad = np.radians(d["mixing_angle_deg"])
        lhs = np.cos(full_rad)
        rhs = np.cos(plane_rad) * np.cos(mix_rad)
        assert abs(lhs - rhs) < 1e-9, f"{label}: identity mismatch {lhs} vs {rhs}"


if __name__ == "__main__":
    print("=" * 70)
    print("Positive controls")
    print("=" * 70)
    d_full = test_positive_control_full_sample_matches_p177()
    d_low, d_high = test_positive_control_subsamples_match_p178_p179()
    print(
        f"full={d_full['full_angle_v1_deg']:.5f} (P177: 0.0172), "
        f"low-z={d_low['full_angle_v1_deg']:.5f} (P178/179: 0.0062), "
        f"high-z={d_high['full_angle_v1_deg']:.5f} (P178/179: 0.0195) -- PASS\n"
    )

    print("=" * 70)
    print("Plane-projection diagnostics")
    print("=" * 70)
    for label, idx, h1 in [
        ("FULL-33pt", FULL_INDICES, H1_FULL),
        ("LOW-z", LOW_Z_INDICES, H1_LOW_Z),
        ("HIGH-z", HIGH_Z_INDICES, H1_HIGH_Z),
    ]:
        d = plane_diagnostics(idx, h1)
        print(f"\n{label}:")
        print(f"  eigvals = {d['eigvals']}")
        print(
            f"  lambda1/lambda2 = {d['lam1_lam2_ratio']:.3e}   "
            f"lambda2/lambda3 = {d['lam2_lam3_ratio']:.3e}"
        )
        print(f"  full_angle(V_PRED, v1)      = {d['full_angle_v1_deg']:.5f} deg")
        print(f"  angle(V_PRED, plane(v1,v2)) = {d['angle_to_plane_deg']:.5f} deg")
        print(
            f"  mixing_angle(v1 vs v2 axis) = {d['mixing_angle_deg']:.5f} deg  (NOT independent, see Correction)"
        )

    test_v_pred_lies_almost_entirely_in_the_flat_plane()
    test_lambda1_lambda2_separation_in_base_samples()
    test_exact_spherical_identity_holds()
    print(
        "\nAll checks PASS. The one new, non-redundant finding: V_PRED lies "
        "almost entirely within the flat (v1,v2) plane, not into the stiff "
        "v3 direction (angle_to_plane 20-100x smaller than the full angle "
        "to v1, in all three samples) -- V_PRED's tiny deviation from v1 "
        "sits in the direction the real data barely constrains at all, not "
        "in the direction the data measures well. mixing_angle is reported "
        "for completeness only -- it is exactly determined by the other two "
        "(spherical identity, verified to ~1e-9), not separate evidence. "
        "lambda1/lambda2 confirmed well-separated (~1e-8 to 1e-9) in all "
        "three BASE samples, so v1 is not an arbitrary pick within a "
        "near-degenerate pair here either."
    )
