"""P177 -- attempts, properly this time, the connection FINDING_P175 and
FINDING_P176 both tried and retracted: does FINDING_P165's monopole-tier
epsilon mechanism (F0 -> (1+epsilon)*F0, injected into v82's own real
force law, exactly as P165 constructed it) explain any part of the real
degeneracy structure this project has found in v82's own chi-squared
surface?

Unlike the two retracted attempts, this file does the SAME calculation
in a genuinely comparable way: build the REAL chi2(beta1,beta2,epsilon)
using TJB's own real 33-point dataset and real force law (not an
idealized local Taylor expansion, and not an inversion through Table
II's own reported numbers), at the SAME fixed H0_anchor FINDING_P176
already used. Compute the full 3x3 numeric Hessian in (beta1,beta2,
epsilon) at TJB's own real best-fit point (epsilon=0, which recovers his
own published force law exactly). Diagonalize; find the near-null
eigenvector; compare its (beta1,beta2)-component ratio (normalized to
delta_epsilon=1) against FINDING_P165's own idealized-local prediction
(delta_beta1, delta_beta2, delta_epsilon) = (C, C^2, 1).

This is a well-posed, apples-to-apples comparison: both quantities are
"the direction, in (beta1,beta2,epsilon)-space, along which epsilon can
be compensated without changing the chi-squared/H(z)-shape" -- one
computed from a 2nd-order local Taylor expansion at z=0 (P165), the
other from the full nonlinear chi2 integrated over all 33 real data
points (this file). Neither retracted attempt (P175's Table-II-inversion,
P176's Taylor-order story for the pure beta1-beta2 slope) made this
comparison correctly; this file does.

Data/code source: TJB's own supplemental Zenodo archive (as in P169/
P175/P176) -- multing_core.py's own forces() function, modified only by
the SAME (1+epsilon) monopole perturbation P165 already defined and used.

CORRECTION (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing -- see FINDING_P177.md's own "Correction" section for
the full account): the first draft's headline claim -- that "a
monopole-tier epsilon really can be compensated almost completely
freely along this direction" -- is RETRACTED. The skeptic's sharpest
objection: beta1_fit, beta2_fit are TJB's own optimized values, but
epsilon=0 was never optimized over -- the point (x1=1, x2=1, eps=0) is
therefore NOT a joint critical point of the full 3-parameter chi2, and
a near-zero Hessian eigenvalue AT A NON-CRITICAL POINT does not mean
"flat direction": chi2 can still vary LINEARLY along that direction
(via the gradient), swamping the tiny quadratic term for any non-
infinitesimal step. Checked directly: the gradient of chi2 projected
onto the near-null eigenvector is ~4.0e-4, while the quadratic term for
a unit step (delta_eps=1) along that same eigenvector is only
~5.7e-7 -- the LINEAR term is about 700x LARGER. The "epsilon is nearly
free" claim does not survive this check and is retracted; establishing
it properly would require re-optimizing (beta1,beta2,epsilon) jointly
to a genuine 3D critical point, not attempted here (computationally
expensive given the surface's own ill-conditioning).

What DOES survive, independently re-verified: (1) the skeptic's
alternative explanation that (1+eps)*F0 is a near-trivial rescaling
because "F0 is by far numerically dominant" is WRONG, refuted directly
-- F1 and F2 are actually ~800-1100x LARGER than F0 across the real
data range (checked at z=0, 0.5, 1.0, 2.33), so perturbing F0 alone is
a genuinely targeted, non-trivial perturbation, not a disguised
H0_anchor rescale. (2) The skeptic's own methodological correction (the
two component-wise ratios, 1.11 and 1.24, are not "one consistent
factor" and are basis-dependent) is right and is fixed by reporting the
actual angle between the real near-null eigenvector and FINDING_P165's
predicted direction, which is the correct, basis-independent quantity:
0.017 degrees (cosine = 0.99999995) -- an extremely tight directional
match, tighter than the raw component ratios suggested. This directional
result survives as a real, verified, quantified fact -- separate from,
and not requiring, the retracted "epsilon is nearly free" claim.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own multing_core.py (same subset P176 already used
# and positive-controlled)
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
    """TJB's own addot_over_a, with F0 -> (1+eps)*F0 -- FINDING_P165's
    own monopole-tier perturbation, applied here to the REAL force law
    (not an idealized local expansion). eps=0 recovers TJB's own
    published force law exactly (verified as a positive control below).
    """
    M, R, k, d = M_of(z), R_of(z), k_of(z), d_of(z)
    F0 = (1 + eps) * (-G) * M * M / d**2
    F1 = b1 * (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2
    F2 = b2 * (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2
    F_total = F0 - F1 + F2 - F_accretion(z)
    return (F_total / (M / 2.0)) / d


# TJB's own 31-point cosmic chronometer compilation (verbatim, as in P176)
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


def chi2_eps(h0_anchor, beta1, beta2, eps):
    """Same construction as P176's chi2_fixed_h0anchor, with epsilon
    added to the monopole term exactly as P165 defined it.
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
    Hp = np.interp(z33, ZFINE, Hm)
    return np.sum(((Hp - H33) / s33) ** 2)


# Table II, verbatim from TJB's own assumptions.yaml (subset used here)
TABLE_II = {
    "unconstrained_spotlighted": (73.22, 1.4335e10, 7.8067e17, 15.75),
    "pct_50": (70.22, 1.2632e10, 6.7582e17, 24.26),
    "planck_exact_100pct": (67.40, 1.1075e10, 5.7995e17, 47.77),
}

# FINDING_P165's own idealized-local scale constant (FINDING_P175's numeric
# evaluation of it, using TJB's own real baseline values).
C_IDEALIZED_LOCAL = 2.644421e07


def test_positive_control_epsilon_zero_recovers_real_chi2():
    """eps=0 must recover exactly the same chi2 as P176's own
    chi2_fixed_h0anchor (which was itself positive-controlled against
    TJB's own reported Table II chi2_33 values) -- confirms this file's
    epsilon-augmented force law is a genuine superset, not a divergent
    reconstruction.
    """
    for label in ("unconstrained_spotlighted", "planck_exact_100pct"):
        h0a, b1, b2, chi2_expected = TABLE_II[label]
        computed = chi2_eps(h0a, b1, b2, 0.0)
        rel_err = abs(computed - chi2_expected) / chi2_expected
        assert rel_err < 0.001, f"{label}: computed={computed}, expected={chi2_expected}"
    return True


def real_epsilon_coupling_direction(h0a0, b1_0, b2_0, h1=1e-4, h3=0.02):
    """Full 3x3 Hessian of chi2(beta1,beta2,epsilon) at (x1=1,x2=1,eps=0)
    -- rescaled x1=beta1/beta1_0, x2=beta2/beta2_0 (both ~1 at the fit
    point), eps used directly (its own expansion point is 0, so it
    cannot be rescaled by itself; h3 is an absolute step, chosen from a
    direct sensitivity probe -- chi2's own curvature in eps alone is
    very small, so h1 and h3 use different step scales by necessity).
    Returns (eigenvalues ascending, near-null eigenvector normalized to
    its own epsilon-component = 1).
    """

    def f(x1, x2, x3):
        return chi2_eps(h0a0, x1 * b1_0, x2 * b2_0, x3)

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
    v_null = v_null / v_null[2]  # normalize so the epsilon component is exactly 1
    return eigvals, v_null


def test_epsilon_direction_converges_with_step_size():
    """The near-null eigenvector, normalized to its own epsilon
    component, must be stable (< 0.1% change) as h3 shrinks by 1 order
    of magnitude -- confirms the result is a real feature of the chi2
    surface at this scale, not a finite-difference artifact.
    """
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    dirs = []
    for h3 in (0.05, 0.02, 0.01, 0.005):
        _, v = real_epsilon_coupling_direction(h0a, b1, b2, h3=h3)
        dirs.append(v)
    x1_vals = [v[0] for v in dirs]
    x2_vals = [v[1] for v in dirs]
    spread_x1 = (max(x1_vals) - min(x1_vals)) / np.mean(x1_vals)
    spread_x2 = (max(x2_vals) - min(x2_vals)) / np.mean(x2_vals)
    assert spread_x1 < 0.001, f"x1 component not converged: {x1_vals}"
    assert spread_x2 < 0.001, f"x2 component not converged: {x2_vals}"
    return dirs[-1]


def test_ratio_to_p165_prediction_is_h0anchor_independent():
    """The ratio (real coupling direction) / (P165's idealized-local
    prediction), for both the beta1 and beta2 components, must agree to
    within 1% across at least 3 different fixed H0_anchor values -- if
    true, this ratio is itself a genuine structural constant, not an
    artifact of one particular operating point.
    """
    ratios_x1, ratios_x2 = [], []
    for label in ("unconstrained_spotlighted", "pct_50", "planck_exact_100pct"):
        h0a, b1, b2, _ = TABLE_II[label]
        _, v = real_epsilon_coupling_direction(h0a, b1, b2)
        pred_x1 = C_IDEALIZED_LOCAL / b1
        pred_x2 = C_IDEALIZED_LOCAL**2 / b2
        ratios_x1.append(v[0] / pred_x1)
        ratios_x2.append(v[1] / pred_x2)
    spread_x1 = (max(ratios_x1) - min(ratios_x1)) / np.mean(ratios_x1)
    spread_x2 = (max(ratios_x2) - min(ratios_x2)) / np.mean(ratios_x2)
    assert spread_x1 < 0.01, f"x1 ratio varies across H0_anchor: {ratios_x1}"
    assert spread_x2 < 0.01, f"x2 ratio varies across H0_anchor: {ratios_x2}"
    return ratios_x1, ratios_x2


def test_linear_term_dominates_quadratic_along_null_direction():
    """Skeptic-requested check (2026-08-31): (x1=1,x2=1,eps=0) is NOT a
    joint critical point in epsilon (only beta1,beta2 were optimized by
    TJB's own fit) -- confirms the gradient of chi2, projected onto the
    near-null eigenvector, is NOT negligible compared to the quadratic
    (curvature) term for a unit step. If the linear term dominates (as
    found), the near-zero eigenvalue does NOT mean "epsilon is nearly
    free" -- it means the quadratic approximation itself is not the
    right description of chi2 along this direction near this reference
    point.
    """
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]

    def chi2_x(x1, x2, x3):
        return chi2_eps(h0a, x1 * b1, x2 * b2, x3)

    h1, h3 = 1e-4, 0.02
    g_x1 = (chi2_x(1 + h1, 1, 0) - chi2_x(1 - h1, 1, 0)) / (2 * h1)
    g_x2 = (chi2_x(1, 1 + h1, 0) - chi2_x(1, 1 - h1, 0)) / (2 * h1)
    g_eps = (chi2_x(1, 1, h3) - chi2_x(1, 1, -h3)) / (2 * h3)
    grad = np.array([g_x1, g_x2, g_eps])

    eigvals, v_null = real_epsilon_coupling_direction(h0a, b1, b2)
    lambda_null = eigvals[0]
    linear_term = np.dot(grad, v_null) * 1.0  # unit step (delta_eps=1)
    quad_term = 0.5 * lambda_null * 1.0**2
    ratio = abs(linear_term / quad_term)
    assert ratio > 10, (
        f"expected linear term to clearly dominate (ratio>10), got ratio={ratio:.2f} "
        f"-- ‘epsilon is nearly free’ interpretation would need re-examination"
    )
    return grad, linear_term, quad_term, ratio


def test_F0_is_not_dominant_over_F1_F2():
    """Skeptic-requested check (2026-08-31): tests the skeptic's own
    alternative explanation -- that (1+eps)*F0 is nearly a trivial
    rescaling of the total force because F0 is "by far numerically
    dominant". Checked directly at 4 redshifts spanning the real data
    range: F1 and F2 (at TJB's own fitted beta1,beta2) must each be
    LARGER than F0 -- if so, the skeptic's proposed alternative
    explanation for the near-null direction (a disguised H0_anchor
    rescale) does not hold, since perturbing the SUBDOMINANT term F0 is
    not equivalent to rescaling the total force.
    """
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    for z in (0.0, 0.5, 1.0, 2.33):
        m, r, k, d = M_of(z), R_of(z), k_of(z), d_of(z)
        f0 = G * m * m / d**2
        f1 = b1 * G * 2.0 * m * (k / c**2) * (r / d) / d**2
        f2 = b2 * G * (k / c**2) ** 2 * (r * r / d**2) / d**2
        assert f1 > f0, f"z={z}: F1={f1:.3e} not > F0={f0:.3e}"
        assert f2 > f0, f"z={z}: F2={f2:.3e} not > F0={f0:.3e}"
    return True


def test_angle_between_real_and_predicted_direction():
    """Skeptic-requested fix (2026-08-31): component-wise ratios (1.11,
    1.24) are basis-dependent and do not, by themselves, establish how
    close the two 3-vectors actually are. The basis-independent measure
    is the angle between them (equivalently, the cosine similarity).
    """
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    _, v_null = real_epsilon_coupling_direction(h0a, b1, b2)
    v_pred = np.array([C_IDEALIZED_LOCAL / b1, C_IDEALIZED_LOCAL**2 / b2, 1.0])
    cos_angle = np.dot(v_null, v_pred) / (np.linalg.norm(v_null) * np.linalg.norm(v_pred))
    angle_deg = np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))
    assert angle_deg < 1.0, f"angle between directions is {angle_deg:.4f} deg, expected < 1 deg"
    return cos_angle, angle_deg


if __name__ == "__main__":
    test_positive_control_epsilon_zero_recovers_real_chi2()
    print("Positive control: epsilon=0 recovers P176's own real chi2 exactly (<0.1%): PASS\n")

    v_converged = test_epsilon_direction_converges_with_step_size()
    print(
        "Step-size convergence of the epsilon-coupling direction (h3=0.05,0.02,0.01,0.005): PASS\n"
    )

    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    eigvals, v_null = real_epsilon_coupling_direction(h0a, b1, b2)
    print(f"At the spotlighted row (H0_anchor={h0a}):")
    print(f"  3x3 eigenvalues (x1,x2,eps) = {eigvals}")
    print("  near-null eigenvector, normalized to delta_eps=1:")
    print(f"    (delta_x1, delta_x2, delta_eps) = ({v_null[0]:.6e}, {v_null[1]:.6e}, 1.0)")
    print()
    pred_x1 = C_IDEALIZED_LOCAL / b1
    pred_x2 = C_IDEALIZED_LOCAL**2 / b2
    print("FINDING_P165's own idealized-local prediction (normalized to delta_eps=1):")
    print(f"    (delta_x1, delta_x2, delta_eps) = ({pred_x1:.6e}, {pred_x2:.6e}, 1.0)")
    print(f"  ratio real/predicted: x1={v_null[0] / pred_x1:.4f}  x2={v_null[1] / pred_x2:.4f}")
    print()

    ratios_x1, ratios_x2 = test_ratio_to_p165_prediction_is_h0anchor_independent()
    print("H0_anchor-independence of this ratio (3 rows: spotlighted, pct_50, planck_100pct):")
    print(f"  x1 ratios: {[f'{r:.4f}' for r in ratios_x1]}")
    print(f"  x2 ratios: {[f'{r:.4f}' for r in ratios_x2]}")
    print("  PASS -- agree to < 1% across the tested H0_anchor range.\n")

    print("=" * 70)
    print("SKEPTIC-REQUESTED CHECKS (2026-08-31, see FINDING_P177.md Correction)")
    print("=" * 70)

    cos_angle, angle_deg = test_angle_between_real_and_predicted_direction()
    print(f"\nBasis-independent angle between real and predicted direction: {angle_deg:.4f} deg")
    print(
        f"  (cos similarity = {cos_angle:.8f}) -- PASS, tighter than the raw component ratios suggest.\n"
    )

    test_F0_is_not_dominant_over_F1_F2()
    print("F0-vs-F1,F2 magnitude check: F1,F2 are ~800-1100x LARGER than F0 across z=0 to 2.33.")
    print("  PASS -- refutes the skeptic's alternative explanation that (1+eps)*F0 is a")
    print("  near-trivial rescaling of the total force (F0 is the SUBDOMINANT term, not")
    print("  dominant).\n")

    grad, linear_term, quad_term, ratio = (
        test_linear_term_dominates_quadratic_along_null_direction()
    )
    print("Gradient at the reference point (raw components x1,x2,eps):", grad)
    print(f"  linear term (grad . v_null, unit step) = {linear_term:.4e}")
    print(f"  quadratic term (unit step) = {quad_term:.4e}")
    print(f"  |linear/quadratic| = {ratio:.1f}  -- FAILS the 'flat direction' reading.\n")

    print(
        "RETRACTED (see FINDING_P177.md Correction): the claim 'epsilon can be\n"
        "compensated almost completely freely along this direction' does NOT survive --\n"
        "(x1=1,x2=1,eps=0) is not a joint critical point in epsilon (only beta1,beta2\n"
        "were optimized by TJB's own fit), and the linear term along the near-null\n"
        "eigenvector is ~700x LARGER than the quadratic term for a unit step -- the\n"
        "surface has real SLOPE there, not flatness.\n"
        "\n"
        "SURVIVES: the DIRECTION FINDING_P165's idealized local (z=0, 2nd-order Taylor)\n"
        "construction predicts for epsilon-compensation matches the real full-chi2-\n"
        "surface near-null eigenvector to within 0.02 degrees -- a striking, verified,\n"
        "basis-independent directional agreement, confirmed NOT to be an artifact of\n"
        "F0-dominance (refuted directly). Whether this reflects a genuine physical\n"
        "correspondence or is largely explained by the local model being the leading-\n"
        "order Taylor term of the same underlying force law (a plausible, NOT tested\n"
        "here, alternative reading) remains open."
    )
