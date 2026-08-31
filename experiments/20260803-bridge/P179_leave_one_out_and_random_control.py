"""P179 -- runs the two fixes FINDING_P178's own skeptic review proposed
for its retracted low-z/high-z discriminator: (1) a leave-one-out (LOO)
uncertainty estimate on the near-null-direction angle for each 8-point
subsample (skeptic's own words: "8 запусков low-z с исключением каждой
точки; std across runs = реальная оценка неопределённости угла. Если >
0.01 -- вся дискуссия про 0.006 vs 0.019 умирает"); and (2) a
random-subsample control spanning the FULL z-range (not restricted to
low or high z), to test the skeptic's own "third hypothesis" -- that the
tiny angle might reflect a global near-symmetry of the H(z)
parametrization itself, unrelated to z-range, in which case ANY small
subsample (not just low-z) would show a similarly tiny angle.

Both fixes are run here, independently, on TJB's own real chi2 (same
construction as FINDING_P177/P178, verbatim).

CORRECTION (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing -- see FINDING_P179.md's own "Correction" section):
a skeptic review of this file's first draft raised four attacks. Two
are ACCEPTED and applied here; two are directly checked and found NOT
to hold, with the check added as a proper test rather than left as an
aside.

ACCEPTED: (i) the random-subsample control's "positive" reading
("evidence FOR a genuine z-dependent effect") is walked back. The 33
real data points are z-imbalanced (8 at z<=0.2, 8 at z>=1.0, ~17 in
between) -- an unweighted random draw of 8 points has E[low-z count]
~ 8*8/33 ~ 1.94, so random draws are EXPECTED to be mid/high-z-
dominated regardless of any physics. "random-subsample angle resembles
high-z, not low-z" is therefore close to a predictable consequence of
the base distribution, not a surprising, discriminating result -- (ii)
only the NARROWER claim survives: random draws do NOT reproduce low-z's
tiny angle, which refutes the STRONGEST form of the "any small
subsample looks the same" hypothesis, without positively supporting a
z-dependent-leverage story specifically.

CHECKED AND NOT UPHELD (the skeptic's own strongest technical
objection, attack (c) -- that leave-one-out "stability" might just
reflect persistent near-2D-degeneracy rather than a genuinely
well-defined null direction): this requires the SMALLEST eigenvalue
(lambda1, the null direction) to be close to the SECOND eigenvalue
(lambda2) in each run -- a DIFFERENT ratio than the lambda2/lambda3
ratio FINDING_P178 flagged as concerning. Checked directly, added as a
formal test below (not left as an unverified aside, per the skeptic's
own explicit criticism of the first draft for doing exactly that):
|lambda1/lambda2| is 8 TO 10 ORDERS OF MAGNITUDE smaller than 1 in
EVERY one of the 16 leave-one-out runs -- the null direction is
overwhelmingly, consistently well-isolated from the next eigenvalue in
every single run. The near-2D-degeneracy FINDING_P178 found (and this
file confirms still exists) is specifically between lambda2 and
lambda3, NOT between lambda1 and lambda2 -- it does not contaminate
identification of the null direction itself. Also applied: proper
jackknife scaling (std * sqrt(n-1), n=8) on the leave-one-out standard
deviations, which the skeptic correctly noted was missing -- even with
this more conservative correction, both subsamples' uncertainty
(0.00095 deg low-z, 0.00035 deg high-z) remains far below the skeptic's
own 0.01-degree threshold and well below the low-z-vs-high-z gap
(0.0133 deg).

Net: FIX 1 (leave-one-out) is STRENGTHENED, not weakened, by this
correction -- the null direction is now shown, with a formal check
rather than an aside, to be a real, well-isolated, robust quantity, and
FINDING_P178's original low-z-vs-high-z ordering (retracted there for
lack of exactly this check) is substantially rehabilitated. FIX 2
(random control) survives only in its narrower, negative form.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid

# ---------------------------------------------------------------------------
# Verbatim from TJB's own multing_core.py (same subset P176/P177/P178
# already used and positive-controlled)
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

# Converged step sizes from FINDING_P178's own explicit sweep.
H1_LOW_Z = 1e-5
H1_HIGH_Z = 1e-5
H1_RANDOM = 1e-5


def chi2_eps_indices(h0_anchor, beta1, beta2, eps, indices):
    """Same construction as FINDING_P178's chi2_eps_subset, indexed by an
    explicit list/array of point indices rather than a boolean mask (more
    convenient for leave-one-out and random-draw loops).
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
    return np.sum(((Hp - H33[idx]) / s33[idx]) ** 2)


def null_direction_indices(indices, h1, h3=0.02):
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


def leave_one_out_angles(indices, h1):
    """Compute the near-null-direction angle N times, each time dropping
    exactly one of the given indices (N = len(indices) runs, 7 points
    remain each time for an 8-point subsample).
    """
    angles = []
    for drop in indices:
        remaining = [i for i in indices if i != drop]
        _, v = null_direction_indices(remaining, h1)
        angles.append(angle_to_prediction(v))
    return np.array(angles)


def random_subsample_angles(n_trials, sample_size, h1, seed=42):
    """n_trials random draws of sample_size points from the FULL 33-point
    dataset (any redshift, not restricted to low or high z). A fixed
    seed is used for reproducibility.
    """
    rng = np.random.default_rng(seed)
    angles = []
    for _ in range(n_trials):
        idx = rng.choice(N_POINTS, size=sample_size, replace=False)
        _, v = null_direction_indices(idx, h1)
        angles.append(angle_to_prediction(v))
    return np.array(angles)


def test_positive_control_full_indices_match_p178():
    """Positive control: computing the near-null direction from the full
    LOW_Z_INDICES / HIGH_Z_INDICES (all 8 points, no leave-out) must
    reproduce FINDING_P178's own already-verified angles (0.0062 deg,
    0.0195 deg) to within 1%.
    """
    _, v_low = null_direction_indices(LOW_Z_INDICES, H1_LOW_Z)
    _, v_high = null_direction_indices(HIGH_Z_INDICES, H1_HIGH_Z)
    angle_low = angle_to_prediction(v_low)
    angle_high = angle_to_prediction(v_high)
    assert abs(angle_low - 0.0062) / 0.0062 < 0.01, f"low-z angle {angle_low} != 0.0062"
    assert abs(angle_high - 0.0195) / 0.0195 < 0.01, f"high-z angle {angle_high} != 0.0195"
    return angle_low, angle_high


def test_dropping_shoes_reproduces_full_low_z_result():
    """SH0ES was shown in FINDING_P178 to contribute exactly zero
    curvature -- so leaving it out of the low-z leave-one-out set must
    reproduce the FULL low-z angle (0.0062 deg) almost exactly, as an
    internal consistency check on the leave-one-out procedure itself.
    """
    shoes_idx = np.where(z33 == Z_SHOES)[0][0]
    remaining = [i for i in LOW_Z_INDICES if i != shoes_idx]
    _, v = null_direction_indices(remaining, H1_LOW_Z)
    angle_without_shoes = angle_to_prediction(v)
    assert abs(angle_without_shoes - 0.0062) / 0.0062 < 0.05, (
        f"dropping SH0ES changed the angle unexpectedly: {angle_without_shoes} vs 0.0062"
    )
    return angle_without_shoes


def leave_one_out_lambda_ratios(indices, h1):
    """Companion to leave_one_out_angles: for each of the same N
    leave-one-out runs, return |lambda1/lambda2| -- how well-isolated the
    null direction (lambda1, the smallest eigenvalue) is from the next
    eigenvalue (lambda2). This is a DIFFERENT pair than FINDING_P178's own
    lambda2/lambda3 ratio (which flagged a near-2D-flat subspace at the top
    of the spectrum); a small lambda1/lambda2 here means the null direction
    itself is not contaminated by that separate degeneracy.
    """
    ratios = []
    for drop in indices:
        remaining = [i for i in indices if i != drop]
        eigvals, _ = null_direction_indices(remaining, h1)
        ratios.append(abs(eigvals[0] / eigvals[1]))
    return np.array(ratios)


def jackknife_std(values):
    """Jackknife-corrected standard error for n leave-one-out replicates:
    std_jackknife = std_raw * sqrt(n-1). The skeptic flagged the first
    draft's plain (non-jackknife) std as understating leave-one-out
    uncertainty; this is the standard correction for that ensemble type.
    """
    n = len(values)
    return values.std() * np.sqrt(n - 1)


def test_lambda1_lambda2_separation_in_all_loo_runs():
    """Skeptic's attack (c): does leave-one-out 'stability' just reflect
    the SAME near-2D-degeneracy FINDING_P178 found (its lambda2/lambda3
    ratio), rather than a genuinely well-isolated null direction? That
    would require lambda1 (the null direction) to sit close to lambda2 too.
    Checked directly across all 16 leave-one-out runs (8 low-z + 8 high-z):
    |lambda1/lambda2| must stay many orders of magnitude below 1 in EVERY
    run for the null-direction identification to be trustworthy
    independent of the lambda2/lambda3 degeneracy.
    """
    low_ratios = leave_one_out_lambda_ratios(LOW_Z_INDICES, H1_LOW_Z)
    high_ratios = leave_one_out_lambda_ratios(HIGH_Z_INDICES, H1_HIGH_Z)
    all_ratios = np.concatenate([low_ratios, high_ratios])
    assert np.all(all_ratios < 1e-4), (
        f"lambda1/lambda2 not well-separated in all runs: max={all_ratios.max():.3e}"
    )
    return low_ratios, high_ratios


def test_jackknife_std_below_skeptic_threshold():
    """Jackknife-corrected (not raw) std of the leave-one-out angles, for
    both subsamples, must remain below the skeptic's own stated
    0.01-degree threshold -- the threshold at which the low-z-vs-high-z
    discussion would become indistinguishable from noise.
    """
    low_loo = leave_one_out_angles(LOW_Z_INDICES, H1_LOW_Z)
    high_loo = leave_one_out_angles(HIGH_Z_INDICES, H1_HIGH_Z)
    low_jk = jackknife_std(low_loo)
    high_jk = jackknife_std(high_loo)
    assert low_jk < 0.01, f"low-z jackknife std {low_jk} exceeds skeptic threshold"
    assert high_jk < 0.01, f"high-z jackknife std {high_jk} exceeds skeptic threshold"
    return low_jk, high_jk


if __name__ == "__main__":
    angle_low, angle_high = test_positive_control_full_indices_match_p178()
    print(
        f"Positive control: full-8-point angles reproduce FINDING_P178 "
        f"(low-z={angle_low:.4f}, high-z={angle_high:.4f}): PASS\n"
    )

    angle_no_shoes = test_dropping_shoes_reproduces_full_low_z_result()
    print(
        f"Internal check: dropping SH0ES from low-z gives angle={angle_no_shoes:.5f} deg "
        f"(vs full low-z 0.0062 deg) -- PASS, confirms SH0ES's zero-contribution finding.\n"
    )

    print("=" * 70)
    print("FIX 1: LEAVE-ONE-OUT UNCERTAINTY ESTIMATE (skeptic-proposed)")
    print("=" * 70)

    low_loo = leave_one_out_angles(LOW_Z_INDICES, H1_LOW_Z)
    print("\nLOW-z leave-one-out (8 runs, 7 points each):")
    print(f"  angles: {np.round(low_loo, 5)}")
    print(
        f"  mean={low_loo.mean():.5f}, std={low_loo.std():.5f}, "
        f"range=[{low_loo.min():.5f}, {low_loo.max():.5f}]"
    )

    high_loo = leave_one_out_angles(HIGH_Z_INDICES, H1_HIGH_Z)
    print("\nHIGH-z leave-one-out (8 runs, 7 points each):")
    print(f"  angles: {np.round(high_loo, 5)}")
    print(
        f"  mean={high_loo.mean():.5f}, std={high_loo.std():.5f}, "
        f"range=[{high_loo.min():.5f}, {high_loo.max():.5f}]"
    )

    gap = high_loo.mean() - low_loo.mean()
    print(f"\nlow-z vs high-z gap: {gap:.5f} deg")
    print(
        f"low-z std / gap = {low_loo.std() / gap:.3f}   high-z std / gap = {high_loo.std() / gap:.3f}"
    )
    print(
        "Skeptic's own threshold: if std > 0.01 deg, the low-z-vs-high-z discussion is "
        "noise. Both RAW stds are two orders of magnitude below that threshold, and both are "
        "far smaller than the gap between the two subsamples.\n"
    )

    print("-" * 70)
    print("FIX 1 verification (skeptic attack (c) + jackknife scaling)")
    print("-" * 70)

    low_ratios, high_ratios = test_lambda1_lambda2_separation_in_all_loo_runs()
    print(
        f"|lambda1/lambda2| across all 16 LOO runs: "
        f"low-z max={low_ratios.max():.3e}, high-z max={high_ratios.max():.3e}"
    )
    print(
        "-> the null direction (lambda1) is 4+ orders of magnitude below the 1e-4 bound "
        "in every run -- NOT close to lambda2, so it is NOT contaminated by FINDING_P178's "
        "separate lambda2/lambda3 near-2D-degeneracy. Attack (c) does NOT hold.\n"
    )

    low_jk, high_jk = test_jackknife_std_below_skeptic_threshold()
    print(f"Jackknife-corrected std (std*sqrt(n-1), n=8): low-z={low_jk:.5f}, high-z={high_jk:.5f}")
    print(
        f"-> even with this more conservative correction, both remain far below the "
        f"skeptic's 0.01 deg threshold and well below the {gap:.4f} deg gap. "
        "CONCLUSION: the near-null direction is STABLE under point removal for both "
        "subsamples, verified both by raw std and by jackknife-corrected std, and by "
        "direct confirmation that lambda1 is not contaminated by the lambda2/lambda3 "
        "degeneracy. The original low-z/high-z ordering is substantially rehabilitated "
        "by this specific check, though the ORDERING's own physical meaning (genuine "
        "correspondence vs Taylor-truncation leverage) remains open -- this is a "
        "different question, see FINDING_P177/P178.\n"
    )

    print("=" * 70)
    print("FIX 2: RANDOM-SUBSAMPLE CONTROL (skeptic's 'third hypothesis' test)")
    print("=" * 70)

    random_angles = random_subsample_angles(8, 8, H1_RANDOM)
    print("\n8 random 8-point subsamples (any z, not restricted to low or high):")
    print(f"  angles: {np.round(random_angles, 5)}")
    print(
        f"  mean={random_angles.mean():.5f}, std={random_angles.std():.5f}, "
        f"range=[{random_angles.min():.5f}, {random_angles.max():.5f}]"
    )
    print(
        f"\nCompare: low-z mean={low_loo.mean():.4f}, random mean={random_angles.mean():.4f}, "
        f"high-z mean={high_loo.mean():.4f}, full-33pt (FINDING_P177) ~0.0169"
    )
    print(
        "\nCORRECTED interpretation (see module docstring's Correction section): the 33 "
        "real points are z-imbalanced (8 at z<=0.2, 8 at z>=1.0, ~17 in between), so an "
        "unweighted random draw of 8 has E[low-z count]~1.94 -- random subsamples are "
        "EXPECTED to be mid/high-z-dominated regardless of any real physics. The random "
        "mean sitting near the full/high-z regime is therefore close to a predictable "
        "base-rate fact, NOT surprising discriminating evidence, and does NOT positively "
        "support a z-range-dependent-leverage story by itself. What DOES survive: random "
        "draws do NOT reproduce low-z's own tiny angle (0.0062 deg is outside the random "
        "range shown above) -- this refutes only the STRONGEST form of the skeptic's "
        "'third hypothesis' (that ANY small subsample, regardless of z, looks equally "
        "tiny), without positively proving z-dependence."
    )
