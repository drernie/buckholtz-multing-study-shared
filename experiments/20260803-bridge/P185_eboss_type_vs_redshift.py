"""P185 -- tests whether DESI's outsized leave-one-out influence
(FINDING_P182/P184) is driven by its measurement TYPE (BAO/Lyman-alpha,
vs. cosmic-chronometer for the rest of the sample) or by its extreme
REDSHIFT (z=2.33, the furthest point in the entire 33-point dataset),
by adding a REAL, independently-published BAO-type point at a
NON-extreme redshift and checking whether it shows the same outsized
leave-one-out behavior DESI does.

FINDING_P184 broke the weight confound (DESI's outsized influence is
not purely because of its small measurement uncertainty) but could not
separate "redshift extremity" from "measurement type" -- DESI is the
only BAO-type point in the sample AND the single most extreme redshift
point, and TJB's real 33-point dataset offers no second point of
either kind to test with.

Literature search (this session, WebSearch + ADS) found:
- NO published cosmic-chronometer point exists above z=1.965 (the
  existing ceiling in TJB's own dataset) -- that branch is genuinely
  closed, not merely unexplored.
- A real, independent BAO-type measurement DOES exist at a
  NON-extreme redshift: Neveux et al. 2020 (MNRAS 499, 210,
  arXiv:2007.08999), the completed SDSS-IV/eBOSS DR16 quasar BAO
  analysis, z_eff=1.480, D_H(z)/r_d = 13.26 +/- 0.55. Converted to
  H(z) using a fiducial sound horizon r_d=147.09 Mpc (Planck-2018-
  like, the standard convention in BOSS/eBOSS/DESI papers -- NOT
  independently re-derived or verified against TJB's own DESI-point
  provenance; noted as an inference, not confirmed fact):
      H(z=1.480) = c / (r_d * D_H/r_d) = 153.707 +/- 6.375 km/s/Mpc

This is a quasar-clustering BAO measurement (different tracer than
DESI's Lyman-alpha forest), at z=1.480 -- squarely WITHIN the existing
7-point cosmic-chronometer high-z range (1.037 to 1.965), not at the
edge. Same broad TYPE difference from the CC points (BAO vs. not) as
DESI, but NOT an extreme-redshift point.

Method: build a second 8-point set (7 CC + eBOSS, "Set B"), parallel
in construction to the original 7 CC + DESI ("Set A", FINDING_P178-
P184's own already-established set), and compare leave-one-out
behavior: does dropping eBOSS show the same outsized deviation DESI
shows in Set A, or does it behave like an ordinary point?

CORRECTION (2026-09-01, context-asymmetric skeptic-caught, applied
before finalizing -- code verified present in the dispatch): a skeptic
review raised 6 attacks. Two independently checked and CONFIRMED as
real problems requiring a methodology change (not just a caveat); the
underlying finding survives, on stronger numerics, once fixed. Two
accepted as genuine, unaddressed limitations. Two addressed directly.

CONFIRMED BY DIRECT CHECK, THEN FIXED -- Set B's finite-difference
numerics were genuinely fragile (documented below), and per-point
step-size sensitivity was checked directly: EVERY one of the 7 CC
points' own leave-one-out angles in Set B showed comparable or larger
step-size noise than eBOSS's own drop (e.g. the z=1.037 point's drop
varied by 0.0025 deg across step sizes, larger than eBOSS's own
variation) -- meaning the fixed-step z-score computed in the first
draft had a NOISE-INFLATED denominator, potentially biasing the result
toward "eBOSS looks ordinary" for a numerical, not physical, reason.
FIXED: replaced the hand-rolled fixed-step central-difference Hessian
with `numdifftools.Hessian` (adaptive Richardson extrapolation),
independently verified stable for Set A (angle range 0.0193-0.0194
deg across 3 step configurations, vs. the established 0.01946) and
markedly more stable for Set B too (though still less clean than Set
A). Recomputing BOTH sets' leave-one-out z-scores with this SAME,
fairer method across 3 independent step configurations: DESI's
z-score is 9.74-14.63 (always the max); eBOSS's z-score is 0.45-0.89
(never the max) -- the qualitative finding survives a genuinely fair,
apples-to-apples numerical comparison, not just the original noisy one.

ACCEPTED, NARROWS THE CONCLUSION -- "BAO measurement type" was never
actually a single controlled category. eBOSS (Neveux et al. 2020) is a
QUASAR-CLUSTERING BAO measurement; DESI's own point is a LYMAN-ALPHA
FOREST BAO measurement -- different tracers, different systematics,
different modeling. This file tests only whether quasar-clustering
BAO reproduces DESI's outsized behavior; it does NOT test Lyman-alpha-
forest BAO specifically, which remains a live, untested alternative
explanation. The conclusion is narrowed accordingly throughout.

ACCEPTED, UNADDRESSED LIMITATION -- the r_d=147.09 Mpc fiducial sound
horizon used to convert eBOSS's D_H/r_d to H(z) carries its own
uncertainty (not propagated into SIG_EBOSS) and is a ΛCDM-calibrated
value; a shift of a few percent would shift H_EBOSS by a comparable
amount. Not swept here -- documented as an open sensitivity, not
resolved.

ACCEPTED, UNADDRESSED LIMITATION -- eBOSS's H(z) value could happen to
sit unusually close to the existing cosmic-chronometer trend (a
different confound: "residual size at insertion," not type or
redshift). A proper test would re-run with eBOSS's H(z) value
artificially shifted at fixed z and sigma; not attempted here. Partial,
informal reassurance: with the adaptive Hessian, the actual maximum
leave-one-out deviation in Set B belongs to an ORDINARY cosmic-
chronometer point (z=1.037), not eBOSS -- if "on-trend-ness" alone
explained low LOO influence, there is no obvious reason an ordinary
CC point should exceed it.

NO_AUTHOR_ERROR note: this is an external, exploratory addition this
project made to TJB's real 33-point dataset for diagnostic purposes
only -- it does not represent any combination TJB himself constructed,
tested, or endorsed, and no claim about v82's own theory follows from
it.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numdifftools as nd
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

# NEW (this file only) -- eBOSS DR16 quasar BAO point, see module
# docstring for full provenance and the rd_fid=147.09 Mpc conversion.
Z_EBOSS, H_EBOSS, SIG_EBOSS = 1.480, 153.707, 6.375

z34 = np.concatenate([zd, [Z_SHOES], [Z_DESI], [Z_EBOSS]])
H34 = np.concatenate([Hd, [H_SHOES], [H_DESI], [H_EBOSS]])
s34 = np.concatenate([sd, [SIG_SHOES], [SIG_DESI], [SIG_EBOSS]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z34])))

H0A0, B1_0, B2_0 = 73.22, 1.4335e10, 7.8067e17
C_IDEALIZED_LOCAL = 2.644421e07
V_PRED = np.array([C_IDEALIZED_LOCAL / B1_0, C_IDEALIZED_LOCAL**2 / B2_0, 1.0])

H1_SET_A = 1e-5  # converged for Set A per FINDING_P178's own explicit sweep

CC_HIGH_INDICES = np.where((z34 >= 1.0) & (z34 < 2.0) & (z34 != Z_DESI) & (z34 != Z_EBOSS))[0]
DESI_IDX = np.where(np.abs(z34 - Z_DESI) < 1e-9)[0][0]
EBOSS_IDX = np.where(np.abs(z34 - Z_EBOSS) < 1e-9)[0][0]
SET_A = np.concatenate([CC_HIGH_INDICES, [DESI_IDX]])
SET_B = np.concatenate([CC_HIGH_INDICES, [EBOSS_IDX]])


def chi2_eps_indices(h0_anchor, beta1, beta2, eps, indices):
    """Same construction as FINDING_P177-P184's chi2."""
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
    Hp = np.interp(z34[idx], ZFINE, Hm)
    return np.sum(((Hp - H34[idx]) / s34[idx]) ** 2)


def null_direction_indices(indices, h1, h3=0.02):
    """Same construction as FINDING_P178-P184's null_direction_subset."""

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


def loo_angles(indices, h1):
    """First-draft method (fixed-step central differences). Kept for
    the positive control and for documenting the numerical fragility
    -- NOT used for the file's final comparison (see Correction).
    """
    results = []
    for idx in indices:
        remaining = [i for i in indices if i != idx]
        _, v = null_direction_indices(remaining, h1)
        results.append((z34[idx], angle_to_prediction(v)))
    return results


def null_direction_adaptive(indices, step=None):
    """Skeptic-motivated fix: adaptive-step Hessian via Richardson
    extrapolation (numdifftools), used as the file's primary,
    trustworthy method for both Set A and Set B -- a fair,
    apples-to-apples comparison (see Correction).
    """

    def f(x):
        return chi2_eps_indices(H0A0, x[0] * B1_0, x[1] * B2_0, x[2], indices)

    hessian = nd.Hessian(f, method="central", step=step)(np.array([1.0, 1.0, 0.0]))
    eigvals, eigvecs = np.linalg.eigh(hessian)
    v_null = eigvecs[:, 0]
    v_null = v_null / v_null[2]
    return eigvals, v_null


def loo_angles_adaptive(indices, step=None):
    results = []
    for idx in indices:
        remaining = [i for i in indices if i != idx]
        _, v = null_direction_adaptive(remaining, step)
        results.append((z34[idx], angle_to_prediction(v)))
    return results


def test_positive_control_set_a_matches_p178_p184():
    """Positive control: Set A (7CC+DESI) must reproduce FINDING_P178-
    P184's own already-verified full-8 high-z angle, both with the
    original fixed-step method (h1=1e-5) and the adaptive method.
    """
    _, v = null_direction_indices(SET_A, H1_SET_A)
    angle = angle_to_prediction(v)
    assert abs(angle - 0.01946) / 0.01946 < 0.02, f"angle={angle} != 0.01946"

    _, v_adaptive = null_direction_adaptive(SET_A)
    angle_adaptive = angle_to_prediction(v_adaptive)
    assert abs(angle_adaptive - 0.01946) / 0.01946 < 0.02, (
        f"adaptive angle={angle_adaptive} != 0.01946"
    )
    return angle, angle_adaptive


def test_set_b_fixed_step_is_numerically_fragile():
    """DOCUMENTS (does not paper over) the genuine numerical fragility
    found while positive-controlling this file with the ORIGINAL
    fixed-step method: Set B's near-null eigenvalue is small enough
    relative to its own second eigenvalue that the computed angle is
    sensitive to h1 choice, AND (skeptic-caught, checked directly) this
    sensitivity is comparable across ALL 8 points' own leave-one-out
    angles, not specific to eBOSS -- meaning a z-score computed from
    this method has a noise-inflated denominator. This motivates the
    switch to the adaptive method below for the actual comparison.
    """
    angles = [
        angle_to_prediction(null_direction_indices(SET_B, h1)[1]) for h1 in (2e-6, 1e-5, 2e-5)
    ]
    assert max(angles) - min(angles) > 0.0002, (
        f"expected Set B's fixed-step angle to vary noticeably across h1 (angles={angles}); "
        "if this fails, the fragility documented in FINDING_P185.md may no longer apply"
    )
    return angles


def test_eboss_not_max_across_adaptive_configs():
    """The key robustness test, on the FIXED (adaptive-Hessian) method:
    across 3 independent step configurations, is eBOSS's leave-one-out
    drop ever the maximum of the 8? Must be consistently False for the
    'eBOSS behaves ordinarily' finding to hold on trustworthy numerics.
    """
    outcomes = {}
    for step in (None, 1e-4, 1e-3):
        results = loo_angles_adaptive(SET_B, step)
        eboss_angle = [a for z, a in results if abs(z - Z_EBOSS) < 1e-6][0]
        all_angles = [a for _, a in results]
        outcomes[step] = eboss_angle == max(all_angles)
    assert not any(outcomes.values()), (
        f"eBOSS IS the max at some adaptive config: {outcomes} -- "
        "the 'eBOSS behaves ordinarily' finding would need revisiting"
    )
    return outcomes


def test_desi_and_eboss_zscores_fair_comparison():
    """The decisive, apples-to-apples test: using the SAME adaptive
    method for both sets, across 3 independent step configurations,
    DESI's z-score must be dramatically larger than eBOSS's at every
    configuration -- confirming the qualitative finding survives fair
    numerics, not just the original (noise-biased) fixed-step method.
    """
    desi_zscores = {}
    eboss_zscores = {}
    for step in (None, 1e-4, 1e-3):
        results_a = loo_angles_adaptive(SET_A, step)
        desi_angle = [a for z, a in results_a if abs(z - Z_DESI) < 1e-6][0]
        other_a = np.array([a for z, a in results_a if abs(z - Z_DESI) >= 1e-6])
        desi_zscores[step] = abs(desi_angle - other_a.mean()) / other_a.std()

        results_b = loo_angles_adaptive(SET_B, step)
        eboss_angle = [a for z, a in results_b if abs(z - Z_EBOSS) < 1e-6][0]
        other_b = np.array([a for z, a in results_b if abs(z - Z_EBOSS) >= 1e-6])
        eboss_zscores[step] = abs(eboss_angle - other_b.mean()) / other_b.std()

    assert all(eboss_zscores[s] < desi_zscores[s] / 3 for s in desi_zscores), (
        f"DESI/eBOSS z-scores not clearly separated: DESI={desi_zscores} eBOSS={eboss_zscores}"
    )
    return desi_zscores, eboss_zscores


if __name__ == "__main__":
    angle_fixed, angle_adaptive = test_positive_control_set_a_matches_p178_p184()
    print(
        f"Positive control: Set A full angle = {angle_fixed:.5f} (fixed-step), "
        f"{angle_adaptive:.5f} (adaptive) -- both match P178-184 -- PASS\n"
    )

    print("=" * 70)
    print("Set B fixed-step fragility (first draft's method -- documented limitation)")
    print("=" * 70)
    fragility_angles = test_set_b_fixed_step_is_numerically_fragile()
    print(
        f"Set B full-sample angle across h1=(2e-6, 1e-5, 2e-5): {[f'{a:.5f}' for a in fragility_angles]}"
    )
    print("-> NOT a clean plateau -- motivated switching to the adaptive method below\n")

    print("=" * 70)
    print("Set A (7CC + DESI) leave-one-out -- adaptive Hessian, step=1e-4")
    print("=" * 70)
    for z, a in loo_angles_adaptive(SET_A, 1e-4):
        tag = " <-- DESI" if abs(z - Z_DESI) < 1e-6 else ""
        print(f"  drop z={z:.4f}: angle={a:.5f} deg{tag}")

    print()
    print("=" * 70)
    print("Set B (7CC + eBOSS) leave-one-out -- adaptive Hessian, step=1e-4")
    print("=" * 70)
    for z, a in loo_angles_adaptive(SET_B, 1e-4):
        tag = " <-- eBOSS" if abs(z - Z_EBOSS) < 1e-6 else ""
        print(f"  drop z={z:.4f}: angle={a:.5f} deg{tag}")

    print()
    max_outcomes = test_eboss_not_max_across_adaptive_configs()
    print(f"Is eBOSS the max, at each adaptive config: {max_outcomes}")
    print("-> eBOSS is NEVER the max, at any tested configuration\n")

    desi_zscores, eboss_zscores = test_desi_and_eboss_zscores_fair_comparison()
    print(
        f"DESI z-scores (adaptive, 3 configs):  { {k: round(v, 2) for k, v in desi_zscores.items()} }"
    )
    print(
        f"eBOSS z-scores (adaptive, 3 configs): { {k: round(v, 2) for k, v in eboss_zscores.items()} }"
    )

    print()
    print(
        "CONCLUSION (substantially revised, see module Correction): a real, "
        "independently-published QUASAR-CLUSTERING BAO point (Neveux et al. 2020, "
        "eBOSS DR16, z=1.48) added at a non-extreme redshift within the existing "
        "cosmic-chronometer range behaves like an ORDINARY point under a fair, "
        "apples-to-apples numerical comparison (adaptive Hessian, same method for "
        "both sets, 3 independent step configurations): never the maximum drop, "
        "z-score 0.45-0.89 at every configuration, versus DESI's 9.74-14.63 at the "
        "same configurations. This is real evidence against 'quasar-clustering BAO "
        "measurement type' as the driver of DESI's outsized influence -- narrower "
        "than 'BAO type in general,' since DESI's own point is a LYMAN-ALPHA FOREST "
        "measurement, a different tracer with different systematics, which remains "
        "UNTESTED and a live alternative explanation. Two further limitations are "
        "documented, not resolved: the r_d=147.09 Mpc conversion's own uncertainty "
        "was not propagated or swept, and a 'residual size at insertion' confound "
        "(is eBOSS's H(z) value just unusually close to the existing trend?) was not "
        "directly tested, though informally weakened by the actual maximum in Set B "
        "belonging to an ordinary CC point, not eBOSS. This does not, by itself, "
        "resolve FINDING_P177's central question (genuine correspondence vs. "
        "Taylor-truncation leverage) -- it narrows, but does not close, which "
        "confound explains FINDING_P182's original observation."
    )
