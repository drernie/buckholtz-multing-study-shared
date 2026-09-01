"""P183 -- runs the z^3-regression across all 8 high-z leave-one-out
points that FINDING_P182's own skeptic proposed as the properly-framed
test of "diffuse" Taylor-truncation leverage (as opposed to P182's
single-point DESI-specific test, which the skeptic correctly called a
strawman of the diffuse hypothesis), per the user's direct request.

Motivation (verbatim from the skeptic's own Attack 2 on FINDING_P182):
"the correctly-framed test is a regression of LOO angle against
z_dropped^3 across all 8 high-z points. Slope, sign, and significance
of that regression -- not a single-point extremum test -- is what
'diffuse Taylor leverage' actually predicts." Under a diffuse model,
each point's contribution to Taylor-truncation error scales roughly as
z^3 (the leading term beyond a 2nd-order expansion); if this mechanism
is real, DROPPING a point with large z^3 should systematically IMPROVE
the match (removing that point's disproportionate truncation-error
pull), giving a NEGATIVE slope of LOO-angle vs z_dropped^3 across all 8
points -- a diffuse, distributed signal, not dependent on any single
point being special.

CORRECTION (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing): a skeptic review raised 8 attacks (dispatched with
a prompt that, by a repeat of the same project-side mistake FINDING_
P180 made, again omitted the actual source code -- the skeptic worked
from the claim and numbers alone, explicitly flagged the omission, and
still produced a substantively correct statistical critique; the 4
code-level bugs it listed as hypothetical/unverifiable were checked
directly against the real source below and REFUTED: LOO index
alignment is correct (z33[idx] and the drop that produced v are the
same idx); v_null's sign ambiguity from eigh is resolved by the
rescale-to-eps-component=1 convention, not a missing abs() -- no
antipodal-flip bug; eigenvector selection is eigh's standard ascending-
order eigvecs[:,0] (smallest eigenvalue), the same convention validated
throughout P177-P182; V_PRED is a fixed module-level constant, never
recomputed inside the LOO loop -- not circular).

ACCEPTED: presenting "p=0.0109" as formal statistical significance is
overreaching -- the 8 leave-one-out angles are NOT independent samples
(each shares 6 of 7 underlying points with every other LOO angle), so
the iid assumption behind linregress/spearmanr's p-values does not
hold. The regression numbers are retained as DESCRIPTIVE comparisons
(how much of the apparent trend depends on one point), not asserted as
formally significant/non-significant.

ACCEPTED: "p=0.7462 without DESI, therefore the effect was fake" over-
interprets non-significance as absence-of-effect, at a sample size
(n=7) with essentially no power to detect a modest real slope.

ACCEPTED, a previously-unconsidered confound: excluding DESI does not
just remove one point -- it roughly HALVES the x-range (z^3) of the
remaining 7 points (12.65 down to a max of 7.59), independently
collapsing the regression's power to detect ANY slope, real or not.
"Signal disappears without DESI" is therefore consistent with EITHER
"DESI was the whole signal" OR "removing DESI made the test underpowered
regardless" -- these are not distinguished here.

ACCEPTED, INDEPENDENTLY VERIFIED (not simply taken on the skeptic's
word): the observed slope is POSITIVE in both regressions (full:
+3.095e-05; excl-DESI: +3.210e-06), while THIS FILE'S OWN stated
mechanistic prediction (above) is a NEGATIVE slope. This is a genuine
sign mismatch, checked directly against the printed numbers -- not
"neutral," as the first draft's conclusion implied, but weak evidence
AGAINST the z^3-diffuse-leverage mechanism specifically (weak because
of the non-independence and low-power issues above, not because the
sign doesn't matter).

ACCEPTED: z^3 is one specific, unverified functional form among several
equally physically-plausible ones ((1+z)^3, ln(1+z), comoving distance,
etc.) -- not compared here. A single-form test cannot rule out a real
diffuse effect that shows up in a different functional form.

ACCEPTED, RESTATED explicitly (the same core confound FINDING_P182
already established, now shown to also contaminate the regression
framing, not just the single-point comparison): DESI's ~50x chi2-weight
(FINDING_P182) means removing it removes both the largest-z^3 point AND
the dominant weight-constraint on the near-null direction simultaneously
-- this regression cannot separate a z^3-driven mechanism from a
weight-driven one any better than P182's single-point test could.

NET RESULT: the first draft's specific narrative ("regression leverage-
point artifact, therefore no diffuse leverage, question stays neutral")
is corrected to a STRONGER, more precise null: this z^3-regression
cannot in principle discriminate genuine diffuse Taylor-truncation
leverage from DESI's simultaneous weight-and-range dominance, and even
setting that aside, the (statistically weak, non-independent, low-
power) sign of the observed effect points AWAY from, not toward, the
mechanism it was designed to detect.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np

# Shared TJB v82 physics kernel (constants + Efun..addot_over_a_eps) --
# see _v82_shared_physics.py docstring for extraction provenance.
from _v82_shared_physics import (
    KMSMPC_TO_SI,
    addot_over_a_eps,
)
from scipy import stats
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

HIGH_Z_MASK = z33 >= 1.0
HIGH_Z_INDICES = np.where(HIGH_Z_MASK)[0]

H0A0, B1_0, B2_0 = 73.22, 1.4335e10, 7.8067e17
C_IDEALIZED_LOCAL = 2.644421e07
V_PRED = np.array([C_IDEALIZED_LOCAL / B1_0, C_IDEALIZED_LOCAL**2 / B2_0, 1.0])

H1_HIGH_Z = 1e-5


def chi2_eps_indices(h0_anchor, beta1, beta2, eps, indices):
    """Same construction as FINDING_P177-P182's chi2."""
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
    """Same construction as FINDING_P178-P182's null_direction_subset."""

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


def high_z_loo_labeled():
    """Same leave-one-out computation as FINDING_P179/P182, for the
    high-z subsample only, returning (z_dropped, angle) pairs.
    """
    results = []
    for idx in HIGH_Z_INDICES:
        remaining = [i for i in HIGH_Z_INDICES if i != idx]
        _, v = null_direction_indices(remaining, H1_HIGH_Z)
        results.append((z33[idx], angle_to_prediction(v)))
    return results


def test_positive_control_matches_p179_p182():
    """Positive control: reproduce FINDING_P179/P182's own already-
    verified high-z leave-one-out angles.
    """
    results = high_z_loo_labeled()
    angles = np.array([a for _, a in results])
    assert abs(angles.mean() - 0.01952) / 0.01952 < 0.02
    desi_angle = [a for z, a in results if abs(z - Z_DESI) < 1e-6][0]
    assert abs(desi_angle - 0.01985) / 0.01985 < 0.02
    return results


def test_full_regression_descriptive_comparison():
    """DESCRIPTIVE only (see Correction: the 8 LOO angles are not
    independent samples, so linregress's p-value is not a valid formal
    significance test here). Verifies the reproducible FACT that the
    naive full-8 fit's r^2 drops sharply when DESI is excluded -- a
    real, checkable geometric property of the data, reported without
    asserting formal statistical significance either way.
    """
    results = test_positive_control_matches_p179_p182()
    z_dropped = np.array([z for z, _ in results])
    angles = np.array([a for _, a in results])
    z3 = z_dropped**3

    res_full = stats.linregress(z3, angles)
    mask = z_dropped < Z_DESI
    res_excl = stats.linregress(z3[mask], angles[mask])
    assert res_full.rvalue**2 > 3 * res_excl.rvalue**2, (
        f"expected r^2 to drop sharply without DESI (full={res_full.rvalue**2}, "
        f"excl={res_excl.rvalue**2}); if this fails, the range-restriction-confound "
        "framing in the module Correction should be revisited"
    )
    return res_full, res_excl


def test_slope_sign_opposes_mechanism_prediction():
    """Independently verifies the skeptic-caught sign mismatch: the
    module docstring's own stated mechanism predicts a NEGATIVE slope;
    the observed slope (both full-8 and excl-DESI) is POSITIVE. This is
    weak evidence AGAINST the z^3-diffuse-leverage mechanism, not
    neutral -- weak because of the non-independence/low-power issues
    documented in the Correction, not because the sign doesn't matter.
    """
    results = test_positive_control_matches_p179_p182()
    z_dropped = np.array([z for z, _ in results])
    angles = np.array([a for _, a in results])
    z3 = z_dropped**3
    res_full = stats.linregress(z3, angles)
    assert res_full.slope > 0, (
        f"expected positive (mechanism-opposing) slope, got {res_full.slope}; "
        "if this fails, the Correction's sign-mismatch claim should be revisited"
    )
    return res_full.slope


def test_spearman_reported_descriptively():
    """Spearman rank correlation (robust to a single extreme x-value,
    unlike OLS), reported descriptively -- same non-independence caveat
    as the OLS test applies here too (see Correction, Attack 1).
    """
    results = test_positive_control_matches_p179_p182()
    z_dropped = np.array([z for z, _ in results])
    angles = np.array([a for _, a in results])
    z3 = z_dropped**3
    rho, p = stats.spearmanr(z3, angles)
    return rho, p


if __name__ == "__main__":
    results = test_positive_control_matches_p179_p182()
    print("Positive control: matches FINDING_P179/P182's own high-z LOO angles -- PASS\n")

    print("=" * 70)
    print("High-z leave-one-out, labeled by z dropped and z^3")
    print("=" * 70)
    for z, a in results:
        tag = " <-- DESI" if abs(z - Z_DESI) < 1e-6 else ""
        print(f"  drop z={z:.4f}  z^3={z**3:.3f}  angle={a:.5f} deg{tag}")

    print()
    res_full, res_excl = test_full_regression_descriptive_comparison()
    print("=" * 70)
    print("z^3-regression: LOO angle ~ z_dropped^3 (DESCRIPTIVE, see Correction)")
    print("=" * 70)
    print(
        f"FULL (8 points):    slope={res_full.slope:.3e}  r^2={res_full.rvalue**2:.4f}  "
        f"naive-p={res_full.pvalue:.4f}"
    )
    print(
        f"EXCLUDING DESI (7):  slope={res_excl.slope:.3e}  r^2={res_excl.rvalue**2:.4f}  "
        f"naive-p={res_excl.pvalue:.4f}"
    )

    slope = test_slope_sign_opposes_mechanism_prediction()
    print(f"\nObserved slope sign: POSITIVE ({slope:.3e}) -- mechanism predicts NEGATIVE")

    rho, p_spear = test_spearman_reported_descriptively()
    print(f"Spearman rank correlation (all 8): rho={rho:.4f}  naive-p={p_spear:.4f}")

    print()
    print(
        "CONCLUSION (substantially revised, see module Correction): the naive full-8 "
        "z^3-regression's r^2 (0.69) drops sharply without DESI (0.02) -- a real, "
        "reproducible descriptive fact -- but NOT a clean 'leverage-point artifact, "
        "therefore no diffuse leverage' story as the first draft framed it: removing "
        "DESI also roughly halves the x-range, independently reducing power to detect "
        "ANY slope, and the naive p-values are not formally valid in the first place "
        "since the 8 LOO angles are non-independent. The stronger, correct conclusion: "
        "this z^3-regression test CANNOT discriminate real diffuse Taylor-truncation "
        "leverage from DESI's simultaneous weight-and-range dominance (the same core "
        "confound FINDING_P182 already established). Independently of that structural "
        "problem, the observed slope's SIGN is opposite the mechanism's own prediction "
        "(positive, not negative) -- weak evidence AGAINST the z^3-diffuse mechanism, "
        "not neutral, though weak given the non-independence and low sample size. "
        "FINDING_P177's open question remains completely unresolved."
    )
