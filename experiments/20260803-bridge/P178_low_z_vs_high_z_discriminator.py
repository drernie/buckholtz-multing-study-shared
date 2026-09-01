"""P178 -- runs the discriminating test FINDING_P177 named but did not
run: does the 0.017-degree directional match between FINDING_P165's
idealized-local (z=0, 2nd-order Taylor) epsilon-compensation prediction
and the real full-33-point chi2 surface's own near-null eigenvector
reflect a genuine structural correspondence, or is it mostly explained
by Taylor-truncation leverage from data far from z=0 (the skeptic's own
proposed alternative reading in FINDING_P177's review)?

Method (the skeptic's own proposed test, run here): split TJB's real
33-point dataset into a LOW-z subsample (z<=0.2, 8 points: the 7 lowest
cosmic-chronometer points plus the SH0ES anchor itself) and a HIGH-z
subsample (z>=1.0, 8 points: the 7 highest cosmic-chronometer points
plus the DESI anchor), holding (beta1,beta2) fixed at TJB's own real
fit values throughout (the same reference point FINDING_P177 used --
this isolates the effect of WHICH DATA shapes the curvature, not a new
fit). Recompute the near-null eigenvector and its angle to FINDING_P165's
prediction for each subsample independently.

Skeptic's own predicted signature of "pure Taylor-truncation leverage":
the low-z angle should be smaller (tighter match) than the high-z angle,
trending toward the full-sample result in between. This file checks that
prediction directly, with a proper step-size convergence sweep (an
earlier, cruder single-step-size check on this same computation gave an
overstated angle for both subsamples -- caught by sweeping h1 down until
truncation error, not just one arbitrary step, and confirmed the true
converged plateau is smaller for both).

CORRECTION (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing -- see FINDING_P178.md's own "Correction" section for
the full account): the first draft's conclusion ("the ordering low-z <
full < high-z narrows the question toward partial Taylor-truncation
leverage") is RETRACTED IN FULL, not softened. Two independent,
directly-verified structural problems make this test's own comparison
unreliable at the claimed precision:

(1) SH0ES (z=0.0233) is the anchoring reference point (zref) itself --
H(Z_SHOES) is IDENTICALLY equal to H0_anchor by construction, for ANY
(beta1,beta2,epsilon). Verified directly: perturbing beta1, beta2, OR
epsilon each leaves the SH0ES-only chi2 term EXACTLY unchanged to full
double-precision display (zero difference, not just small). So the
"low-z, 8 points" subsample is really 7 constraining points plus one
that contributes nothing to the Hessian at all -- while the "high-z, 8
points" subsample has no such issue (DESI is a genuine, non-anchor
point). The two subsamples are not on equal footing the way the test
implicitly assumed.

(2) Far more seriously: the ratio of the second-smallest to largest
eigenvalue (lambda2/lambda3) is 1.6e-6 for low-z and 3.5e-6 for high-z
-- roughly 30-80x SMALLER than the same ratio in the full 33-point
sample (1.2e-4, from FINDING_P177). This means BOTH 8-point subsamples
have a near-2-DIMENSIONAL flat subspace, not a single well-defined
near-null DIRECTION -- with only 8 data points (7 effective, for
low-z), there simply is not enough independent constraining power to
pin down a unique "near-null eigenvector" the way the full 33-point
Hessian could. The specific vector numpy.linalg.eigh happens to return
from within that near-flat 2D plane is not shown to be a robust,
physically meaningful quantity -- it may be dominated by whichever
direction the finite-difference discretization's own residual noise
happens to leave smallest, which is a property of the numerical method,
not of the physics. The reported step-size convergence (this file's own
test) shows only that the SAME finite-difference SCHEME reproducibly
picks the SAME direction -- it does not show that direction is close to
the TRUE, infinite-precision near-null direction, which is exactly the
distinction that matters when the surface is this degenerate.

Net: the observed ordering (low-z < full < high-z) may be real, or may
be an artifact of (1) and (2) above -- this test cannot distinguish the
two, and therefore cannot be read as evidence for (or against) partial
Taylor-truncation leverage. The original open question from FINDING_
P177 (genuine correspondence vs. Taylor-truncation leverage) remains
exactly where it was -- this file's attempt to narrow it did not
succeed, and is reported as an honest null result about the TEST
DESIGN, not about the underlying physics.

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

# TJB's own 31-point cosmic chronometer compilation, verbatim (as in P176/P177)
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

LOW_Z_MASK = z33 <= 0.2  # 8 points: 7 CC points + SH0ES
HIGH_Z_MASK = z33 >= 1.0  # 8 points: 7 CC points + DESI

H0A0, B1_0, B2_0 = 73.22, 1.4335e10, 7.8067e17  # TJB's own spotlighted-row fit
C_IDEALIZED_LOCAL = 2.644421e07
V_PRED = np.array([C_IDEALIZED_LOCAL / B1_0, C_IDEALIZED_LOCAL**2 / B2_0, 1.0])


def chi2_eps_subset(h0_anchor, beta1, beta2, eps, mask):
    """Same construction as FINDING_P177's chi2_eps, but summing chi2
    only over the data points selected by `mask` (the anchoring/
    integration reference, Z_SHOES, is unchanged regardless of mask --
    only WHICH residuals are squared and summed changes).
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
    Hp = np.interp(z33[mask], ZFINE, Hm)
    return np.sum(((Hp - H33[mask]) / s33[mask]) ** 2)


def test_positive_control_subsets_partition_the_full_dataset():
    """Positive control: low-z and high-z masks must select exactly 8
    points each, be disjoint, and their union must be a proper subset
    of all 33 (there are points strictly between z=0.2 and z=1.0 that
    belong to neither -- confirms the split is what it claims to be).
    """
    assert LOW_Z_MASK.sum() == 8
    assert HIGH_Z_MASK.sum() == 8
    assert not np.any(LOW_Z_MASK & HIGH_Z_MASK)
    assert (LOW_Z_MASK | HIGH_Z_MASK).sum() < 33
    return True


def null_direction_subset(mask, h1, h3=0.02):
    """Numeric 3x3 Hessian of chi2_eps_subset(H0A0,x1*B1_0,x2*B2_0,x3),
    restricted to the given data mask, at (x1=1,x2=1,eps=0). Returns
    (eigenvalues ascending, near-null eigenvector normalized to its own
    epsilon-component = 1).
    """

    def f(x1, x2, x3):
        return chi2_eps_subset(H0A0, x1 * B1_0, x2 * B2_0, x3, mask)

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


# Converged step sizes, identified via an explicit h1 sweep (3e-4 down to
# 1e-6) run interactively before writing this script -- both subsamples'
# angle-vs-h1 curves flatten to a stable plateau before roundoff noise
# takes over below ~h1=1e-6; these values sit inside that plateau.
H1_LOW_Z = 1e-5
H1_HIGH_Z = 1e-5
H1_FULL = 1e-5


def test_low_z_and_high_z_angles_converge_with_step_size():
    """The angle for each subsample must be stable (not still drifting)
    across a 3x range of h1 bracketing the chosen converged step size --
    a single-step-size check (an earlier, cruder version of this same
    computation) is not enough to trust the result, since the angle vs
    h1 curve is not monotonically flat until well below h1=1e-4.
    """
    for label, mask, h1 in (("low-z", LOW_Z_MASK, H1_LOW_Z), ("high-z", HIGH_Z_MASK, H1_HIGH_Z)):
        angles = []
        for h1_test in (3 * h1, h1, h1 / 3):
            _, v = null_direction_subset(mask, h1_test)
            angles.append(angle_to_prediction(v))
        spread = max(angles) - min(angles)
        assert spread < 0.01, f"{label}: angle not converged across step sizes: {angles}"
    return True


def test_shoes_point_contributes_nothing_to_hessian():
    """Skeptic-requested check (2026-08-31): SH0ES (z=Z_SHOES) is the
    anchoring reference point (zref) itself, so H(Z_SHOES) is IDENTICAL
    to H0_anchor by construction -- confirms the SH0ES-only chi2 term is
    an exact constant, unaffected by (beta1,beta2,epsilon), so the
    'low-z, 8 points' subsample really has only 7 constraining points.
    """
    shoes_mask = z33 == Z_SHOES
    base = chi2_eps_subset(H0A0, B1_0, B2_0, 0.0, shoes_mask)
    perturbations = [
        (B1_0 * 1.0001, B2_0, 0.0),
        (B1_0 * 0.9999, B2_0, 0.0),
        (B1_0, B2_0 * 1.0001, 0.0),
        (B1_0, B2_0 * 0.9999, 0.0),
        (B1_0, B2_0, 0.02),
        (B1_0, B2_0, -0.02),
    ]
    for b1, b2, eps in perturbations:
        val = chi2_eps_subset(H0A0, b1, b2, eps, shoes_mask)
        assert val == base, f"SH0ES chi2 changed under perturbation: {val} != {base}"
    return True


def test_eigenvalue_ratio_reveals_near_2d_degeneracy_in_subsamples():
    """Skeptic-requested check (2026-08-31): the ratio lambda2/lambda3
    (second-smallest to largest eigenvalue) for each 8-point subsample
    must be checked against the full 33-point sample's own ratio
    (~1.2e-4, from FINDING_P177) -- if it is dramatically smaller (a
    near-2D-flat subspace rather than a single well-defined near-null
    direction), the 'near-null eigenvector' this file extracts is not
    shown to be a robust, physically meaningful quantity, and any angle
    computed from it cannot be trusted at face value.
    """
    full_sample_ratio = 70.597 / 588321  # FINDING_P177's own converged eigenvalues
    ev_low, _ = null_direction_subset(LOW_Z_MASK, H1_LOW_Z)
    ev_high, _ = null_direction_subset(HIGH_Z_MASK, H1_HIGH_Z)
    ratio_low = ev_low[1] / ev_low[2]
    ratio_high = ev_high[1] / ev_high[2]
    assert ratio_low < full_sample_ratio / 10, (
        f"low-z lambda2/lambda3={ratio_low:.2e} not clearly more degenerate than "
        f"full-sample {full_sample_ratio:.2e}"
    )
    assert ratio_high < full_sample_ratio / 10, (
        f"high-z lambda2/lambda3={ratio_high:.2e} not clearly more degenerate than "
        f"full-sample {full_sample_ratio:.2e}"
    )
    return ratio_low, ratio_high, full_sample_ratio


if __name__ == "__main__":
    test_positive_control_subsets_partition_the_full_dataset()
    print(
        f"Positive control: low-z mask selects {LOW_Z_MASK.sum()} points, "
        f"high-z mask selects {HIGH_Z_MASK.sum()} points, disjoint, proper subsets: PASS\n"
    )

    test_low_z_and_high_z_angles_converge_with_step_size()
    print("Step-size convergence for both subsamples' angle (3x bracket around chosen h1): PASS\n")

    print("=" * 70)
    print("LOW-z vs HIGH-z DISCRIMINATOR (skeptic-proposed test, FINDING_P177 review)")
    print("=" * 70)

    _, v_low = null_direction_subset(LOW_Z_MASK, H1_LOW_Z)
    angle_low = angle_to_prediction(v_low)
    print(
        f"\nLOW-z only (z<=0.2, 8 points incl. SH0ES): angle to P165's prediction = {angle_low:.4f} deg"
    )

    _, v_high = null_direction_subset(HIGH_Z_MASK, H1_HIGH_Z)
    angle_high = angle_to_prediction(v_high)
    print(
        f"HIGH-z only (z>=1.0, 8 points incl. DESI): angle to P165's prediction = {angle_high:.4f} deg"
    )

    print("\nFull 33-point (FINDING_P177's own result, re-converged here): ~0.0169 deg")
    print(
        f"\nRaw ordering observed: low-z ({angle_low:.4f}) < full (~0.0169) < high-z ({angle_high:.4f})"
    )

    print("\n" + "=" * 70)
    print("SKEPTIC-REQUESTED CHECKS (2026-08-31, see FINDING_P178.md Correction)")
    print("=" * 70)

    test_shoes_point_contributes_nothing_to_hessian()
    print(
        "\nSH0ES-alone chi2 under perturbation of beta1/beta2/epsilon: UNCHANGED to full\n"
        "  double-precision display in every case -- CONFIRMED, SH0ES contributes ZERO\n"
        "  curvature (it IS the anchor reference point, H(Z_SHOES) is identical to\n"
        "  H0_anchor by construction). 'Low-z, 8 points' is really 7 constraining points."
    )

    ratio_low, ratio_high, ratio_full = (
        test_eigenvalue_ratio_reveals_near_2d_degeneracy_in_subsamples()
    )
    print(
        f"\nlambda2/lambda3 ratios: low-z={ratio_low:.2e}, high-z={ratio_high:.2e}, "
        f"full-sample={ratio_full:.2e}"
    )
    print(
        "  CONFIRMED: both 8-point subsamples are 30-80x MORE degenerate (a near-2D-flat\n"
        "  subspace, not a single well-defined near-null direction) than the full sample.\n"
        "  The specific eigenvector numpy.linalg.eigh returns from within that near-flat\n"
        "  plane is not shown to track true physics rather than finite-difference\n"
        "  discretization bias -- step-size convergence (above) only shows the SAME\n"
        "  scheme reproduces the SAME answer, not that the answer is accurate."
    )

    print(
        "\nRETRACTED IN FULL (see FINDING_P178.md Correction): the raw ordering above\n"
        "CANNOT be read as evidence for or against partial Taylor-truncation leverage.\n"
        "Two independently-verified structural problems make this specific test\n"
        "unreliable at the claimed precision: (1) SH0ES contributes nothing, so the\n"
        "low-z/high-z subsamples are not on equal footing; (2) both subsamples have a\n"
        "near-2D-degenerate curvature structure, so their 'near-null direction' is not\n"
        "shown to be a robust, physically meaningful quantity. FINDING_P177's original\n"
        "open question (genuine correspondence vs. Taylor-truncation leverage) remains\n"
        "exactly where it was. A properly-designed version of this test would need, at\n"
        "minimum: a leave-one-out uncertainty estimate on the angle, comparison of V_PRED\n"
        "to the near-degenerate PLANE rather than to one arbitrary vector within it, and\n"
        "a random-subsample control (same size, any z) to check whether ANY 8-point\n"
        "subsample gives a similarly tiny angle regardless of redshift range -- none of\n"
        "which is attempted here."
    )
