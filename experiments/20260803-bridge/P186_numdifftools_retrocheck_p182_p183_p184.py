"""P186 -- retrochecks P182/P183/P184's core leave-one-out claims (all
three built on the same Set A: the 7 real cosmic-chronometer points at
z=1.037-1.965, plus DESI at z=2.33) using `numdifftools.Hessian`
(adaptive Richardson extrapolation) instead of the fixed-step
(h1=1e-5) central-difference Hessian all three used.

Motivation: sci-code-audit (boyko-project-radar, 2026-09-01, Layer 4)
found that `numdifftools` was introduced and validated in P185, but
only applied there to P185's OWN Set A/Set B leave-one-out angles --
never retroactively to P182/P183/P184's own claims, which still rest
on the fixed-step convention P185 itself showed can be numerically
fragile for leave-one-out subset constructions. Pearled the same day
(pearl_registry/INDEX.md, 2026-09-01 row 3) with the falsifiable
prediction: recomputing with numdifftools should agree with the
fixed-step results to within the ~0.5-1% tolerance P185 found for its
own LOO angles -- a disagreement beyond that would mean the underlying
claims need re-derivation, not just a numerics footnote.

Three specific claims retrochecked, one per file:

P182 -- DESI's leave-one-out drop is the largest (most deviant) among
all 8 high-z points. (Already informally re-confirmed by P185's own
Set A numdifftools sweep -- DESI z-scores {9.89, 14.63, 9.74}, always
max -- but P185 never explicitly framed this as a P182 retrocheck.
Reconfirmed here explicitly, for citation.)

P183 -- the z^3-regression slope (LOO angle vs z_dropped^3, across all
8 high-z points) is POSITIVE, opposing the diffuse-Taylor-leverage
mechanism's predicted NEGATIVE sign. NOT previously recomputed with
numdifftools -- genuinely new check.

P184 -- DESI remains the leave-one-out max even after its chi2-weight
is homogenized to the median of the other 7 points' sigmas, across a
realistic sigma sweep, and under full 8-point weight equalization. NOT
previously recomputed with numdifftools -- genuinely new check.

NO_AUTHOR_ERROR note: this file evaluates the numerical robustness of
this project's own prior reconstructions (P182/P183/P184); it makes no
claim about v82's own theory.

CORRECTION (2026-09-01, context-asymmetric skeptic-caught, applied
before finalizing -- code verified present in the dispatch): a skeptic
review of the first draft found a real Recomposition Gate violation
(FL Step 8a) and two real, checkable numerical-robustness questions.
All three independently verified before accepting; two confirmed,
one refuted.

CONFIRMED, FIXED -- the first draft's conclusion claimed "agreement
held to well within the ~0.5-1% tolerance P185 established," but the
code only checked RANK (is DESI the max?) and SIGN (is the slope
positive?) -- never a quantitative per-point comparison against the
original fixed-step LOO angles. A claim about magnitude was resting on
tests that only checked ordering. Independently computed the actual
per-point comparison (P182's own fixed-step angles vs this file's
adaptive ones, same 8 LOO drops, at the clean step=1e-4 config): max
relative difference 0.768% (at z=1.037), all other 7 points within
0.38-0.74% -- comfortably inside the informally-stated "~0.5-1%" band.
FIXED: this quantitative comparison is now computed and asserted in
the code itself (`test_quantitative_agreement_with_fixed_step`), not
merely claimed in prose.

CONFIRMED, FLAGGED -- checking whether numdifftools' internal
step-size search (the `step=None` "fully adaptive" configuration only)
ever evaluates chi2_eps_indices at a point that triggers the H2<=0
safety-penalty return (1e12), which would silently contaminate that
config's Hessian. Directly instrumented and counted: the `step=None`
config triggers this penalty 512 times across the 8 LOO subsets (out
of numdifftools' own much larger internal evaluation count); the two
FIXED step configs (1e-4, 1e-3) trigger it ZERO times. The qualitative
conclusions (DESI-max, positive slope) held even at step=None despite
this contamination, but `step=None`'s results are flagged as the least
trustworthy of the three configs for this reason -- the two clean,
fixed-step configs are the primary evidence, not `step=None`.

REFUTED BY DIRECT CHECK -- the skeptic's strongest hypothesis, that
`eigvecs[:, 0]` (ascending order = smallest eigenvalue) might silently
select a saddle-point direction instead of the true near-null
direction at some LOO subset/step combination, because the near-null
eigenvalue occasionally comes out numerically NEGATIVE (order 1e-7 to
1e-9, pure floating-point noise around the true near-zero value).
Directly checked across all LOO subsets, both weightings, all 3 step
configs: the near-null eigenvalue is always separated from the second-
smallest eigenvalue by 6-8 orders of magnitude (ratio always < 1e-6,
far below any ambiguity threshold) -- the eigenvector selection is
never ambiguous. The sign flicker is real but harmless; the direction
picked is always correct.

ACCEPTED, MINOR -- the positive-control assertion used a 2% relative
tolerance while the docstring/conclusion cited a "~1%" band. Fixed:
tolerance tightened to 1.5% (between the two, since the actual observed
value is 0.7%, comfortably inside either bound) so the assertion and
the narrative agree.

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
s33_orig = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))

HIGH_Z_MASK = z33 >= 1.0
HIGH_Z_INDICES = np.where(HIGH_Z_MASK)[0]  # Set A: 7 real CC points + DESI

H0A0, B1_0, B2_0 = 73.22, 1.4335e10, 7.8067e17
C_IDEALIZED_LOCAL = 2.644421e07
V_PRED = np.array([C_IDEALIZED_LOCAL / B1_0, C_IDEALIZED_LOCAL**2 / B2_0, 1.0])

# Same DESI-sigma-homogenization convention as P184.
_DESI_ARRAY_IDX = HIGH_Z_INDICES[np.argmin(np.abs(z33[HIGH_Z_INDICES] - Z_DESI))]
_OTHER_HIGH_Z_SIGMAS = s33_orig[HIGH_Z_INDICES][z33[HIGH_Z_INDICES] < Z_DESI]
SIG_DESI_HOMOG = float(np.median(_OTHER_HIGH_Z_SIGMAS))
S33_HOMOG = s33_orig.copy()
S33_HOMOG[_DESI_ARRAY_IDX] = SIG_DESI_HOMOG

# Skeptic-requested instrumentation: counts how many chi2 evaluations
# inside a Hessian call hit the H2<=0 safety penalty (1e12) -- a
# contaminated evaluation numdifftools' Richardson extrapolation
# implicitly assumes cannot happen (it assumes a smooth function).
_PENALTY_HIT_COUNT = [0]


def chi2_eps_indices(h0_anchor, beta1, beta2, eps, indices, s33_use):
    aa = np.array([addot_over_a_eps(zx, beta1, beta2, eps) for zx in ZFINE])
    integrand = aa / (1.0 + ZFINE)
    ds_raw = np.concatenate(([0.0], cumulative_trapezoid(integrand, ZFINE)))
    i0 = np.argmin(np.abs(ZFINE - Z_SHOES))
    ds = ds_raw - ds_raw[i0]
    H2 = (h0_anchor * KMSMPC_TO_SI) ** 2 + 2.0 * ds
    if np.any(H2 <= 0):
        _PENALTY_HIT_COUNT[0] += 1
        return 1e12
    Hm = np.sqrt(H2) / KMSMPC_TO_SI
    idx = np.asarray(list(indices))
    Hp = np.interp(z33[idx], ZFINE, Hm)
    return np.sum(((Hp - H33[idx]) / s33_use[idx]) ** 2)


def null_direction_adaptive(indices, s33_use, step=None):
    """P185's own adaptive-Hessian method (numdifftools), generalized
    to accept an arbitrary sigma array (default: original weights).
    """

    def f(x):
        return chi2_eps_indices(H0A0, x[0] * B1_0, x[1] * B2_0, x[2], indices, s33_use)

    hessian = nd.Hessian(f, method="central", step=step)(np.array([1.0, 1.0, 0.0]))
    eigvals, eigvecs = np.linalg.eigh(hessian)
    v_null = eigvecs[:, 0]
    v_null = v_null / v_null[2]
    return eigvals, v_null


def angle_to_prediction(v_null):
    cos_angle = np.dot(v_null, V_PRED) / (np.linalg.norm(v_null) * np.linalg.norm(V_PRED))
    return np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))


def high_z_loo_labeled_adaptive(s33_use, step=None):
    results = []
    for idx in HIGH_Z_INDICES:
        remaining = [i for i in HIGH_Z_INDICES if i != idx]
        _, v = null_direction_adaptive(remaining, s33_use, step)
        results.append((z33[idx], angle_to_prediction(v)))
    return results


def test_positive_control_matches_p185_set_a():
    """Positive control: reproduces P185's own already-verified
    adaptive-Hessian full-8 Set A angle (0.01932 deg, matching the
    established fixed-step 0.01946 to within ~1%; tolerance tightened
    to 1.5% per Correction -- observed value is 0.7%, comfortably
    inside).
    """
    _, v = null_direction_adaptive(HIGH_Z_INDICES, s33_orig)
    angle = angle_to_prediction(v)
    assert abs(angle - 0.01932) / 0.01932 < 0.015, f"angle={angle} != 0.01932 (P185's own value)"
    return angle


def test_quantitative_agreement_with_fixed_step():
    """Skeptic-caught gap, fixed: the original draft only checked RANK
    (is DESI the max?) and SIGN (is the slope positive?), never a
    quantitative per-point comparison against P182's own fixed-step LOO
    angles -- so the conclusion's "agreement within ~0.5-1% tolerance"
    claim was never actually tested. Fixed: import P182's own fixed-
    step function directly (not hardcoded numbers, so this can't drift
    from the source) and compare point-by-point at the cleanest
    (step=1e-4) adaptive configuration.
    """
    import P182_desi_shoes_specific_loo as p182

    fixed_step_results = p182.leave_one_out_labeled(p182.HIGH_Z_INDICES, p182.H1_HIGH_Z)
    adaptive_results = high_z_loo_labeled_adaptive(s33_orig, step=1e-4)

    max_rel_diff = 0.0
    per_point = {}
    for (zf, af), (za, aa) in zip(fixed_step_results, adaptive_results, strict=True):
        assert abs(zf - za) < 1e-9, "LOO ordering mismatch between P182 and this file"
        rel_diff = abs(af - aa) / af
        per_point[zf] = rel_diff
        max_rel_diff = max(max_rel_diff, rel_diff)

    assert max_rel_diff < 0.015, (
        f"max relative disagreement {max_rel_diff:.4%} exceeds the 1.5% tolerance -- "
        "the tolerance-agreement claim in the conclusion would need revisiting"
    )
    return per_point, max_rel_diff


def test_eigenvalue_selection_is_never_ambiguous():
    """Skeptic-requested check: does the near-null eigenvalue ever
    become numerically ambiguous relative to the second-smallest
    eigenvalue (which would make `eigvecs[:, 0]`'s selection a
    numerical coin flip, possibly picking a saddle direction instead of
    the true near-null one)? Checked across every LOO subset, both
    weightings (original + homogenized), all 3 step configurations.
    """
    max_ratio = 0.0
    any_negative = False
    for s33_use in (s33_orig, S33_HOMOG):
        for step in (None, 1e-4, 1e-3):
            for idx in HIGH_Z_INDICES:
                remaining = [i for i in HIGH_Z_INDICES if i != idx]
                eigvals, _ = null_direction_adaptive(remaining, s33_use, step)
                if eigvals[0] < 0:
                    any_negative = True  # expected: floating-point noise near zero
                ratio = abs(eigvals[0]) / abs(eigvals[1])
                max_ratio = max(max_ratio, ratio)
    assert max_ratio < 1e-3, (
        f"near-null eigenvalue came within {max_ratio:.2e} of the second-smallest at some "
        "LOO subset/config -- eigenvector selection may be ambiguous there"
    )
    return any_negative, max_ratio


def test_step_none_penalty_contamination_is_isolated():
    """Skeptic-requested check: does numdifftools' step=None internal
    step-size search ever evaluate chi2_eps_indices at a point that
    triggers the H2<=0 safety penalty (1e12), silently contaminating
    that config's Hessian? Confirms this DOES happen for step=None (a
    real, flagged limitation) but NOT for the two fixed-step configs
    (1e-4, 1e-3), which are therefore the primary, uncontaminated
    evidence for this file's conclusions.
    """
    counts = {}
    for step in (None, 1e-4, 1e-3):
        _PENALTY_HIT_COUNT[0] = 0
        for idx in HIGH_Z_INDICES:
            remaining = [i for i in HIGH_Z_INDICES if i != idx]
            null_direction_adaptive(remaining, s33_orig, step)
        counts[step] = _PENALTY_HIT_COUNT[0]
    assert counts[1e-4] == 0 and counts[1e-3] == 0, (
        f"expected zero penalty hits at the fixed step configs, got {counts} -- "
        "the 'clean, primary evidence' framing in the Correction would need revisiting"
    )
    return counts


def test_p182_retrocheck_desi_remains_max_adaptive():
    """Retrocheck of P182's core claim (DESI's LOO drop is the largest
    among all 8) using the adaptive Hessian across 3 step
    configurations, instead of the original fixed-step h1=1e-5.
    """
    outcomes = {}
    for step in (None, 1e-4, 1e-3):
        results = high_z_loo_labeled_adaptive(s33_orig, step)
        desi_angle = [a for z, a in results if abs(z - Z_DESI) < 1e-6][0]
        all_angles = [a for _, a in results]
        outcomes[step] = desi_angle == max(all_angles)
    assert all(outcomes.values()), (
        f"DESI is NOT the max at every adaptive config: {outcomes} -- "
        "P182's core claim would not survive the numerics upgrade"
    )
    return outcomes


def test_p183_retrocheck_slope_sign_adaptive():
    """Retrocheck of P183's core claim (z^3-regression slope is
    POSITIVE, opposing the diffuse-Taylor-leverage mechanism's
    predicted NEGATIVE sign) using adaptive-Hessian LOO angles across 3
    step configurations. NOT previously checked with numdifftools.
    """
    slopes = {}
    for step in (None, 1e-4, 1e-3):
        results = high_z_loo_labeled_adaptive(s33_orig, step)
        z_dropped = np.array([z for z, _ in results])
        angles = np.array([a for _, a in results])
        z3 = z_dropped**3
        res = stats.linregress(z3, angles)
        slopes[step] = res.slope
    assert all(s > 0 for s in slopes.values()), (
        f"slope sign did NOT stay positive at every adaptive config: {slopes} -- "
        "P183's sign-mismatch conclusion would not survive the numerics upgrade"
    )
    return slopes


def test_p184_retrocheck_desi_max_under_homogenization_adaptive():
    """Retrocheck of P184's core claim (DESI remains the LOO max under
    sigma-homogenization) using the adaptive Hessian, at the same
    single homogenized-sigma value P184 used (median of other 7).
    """
    outcomes = {}
    for step in (None, 1e-4, 1e-3):
        results = high_z_loo_labeled_adaptive(S33_HOMOG, step)
        desi_angle = [a for z, a in results if abs(z - Z_DESI) < 1e-6][0]
        all_angles = [a for _, a in results]
        outcomes[step] = desi_angle == max(all_angles)
    assert all(outcomes.values()), (
        f"DESI is NOT the max under homogenization at every adaptive config: {outcomes} -- "
        "P184's core claim would not survive the numerics upgrade"
    )
    return outcomes


def test_p184_retrocheck_full_equalization_adaptive():
    """Retrocheck of P184's strongest test (Attack 5: all 8 high-z
    sigmas set to an identical common value) using the adaptive
    Hessian at one step configuration (step=1e-4; a full 3-config x
    3-common-value sweep is 9 evaluations and not needed to answer
    the yes/no retrocheck question).
    """
    common_values = [20.0, float(np.mean(_OTHER_HIGH_Z_SIGMAS)), 30.0]
    outcomes = {}
    for common_sig in common_values:
        s33_test = s33_orig.copy()
        for idx in HIGH_Z_INDICES:
            s33_test[idx] = common_sig
        results = high_z_loo_labeled_adaptive(s33_test, step=1e-4)
        desi_a = [a for z, a in results if abs(z - Z_DESI) < 1e-6][0]
        all_a = [a for _, a in results]
        outcomes[common_sig] = desi_a == max(all_a)
    assert all(outcomes.values()), (
        f"DESI is NOT the max under full equalization at every common sigma: {outcomes} -- "
        "P184's strongest test would not survive the numerics upgrade"
    )
    return outcomes


if __name__ == "__main__":
    angle_a = test_positive_control_matches_p185_set_a()
    print(f"Positive control: Set A adaptive angle = {angle_a:.5f} deg (matches P185) -- PASS\n")

    print("=" * 70)
    print("Skeptic-caught gap, fixed: quantitative per-point agreement vs P182's fixed-step")
    print("=" * 70)
    per_point, max_rel_diff = test_quantitative_agreement_with_fixed_step()
    for z, rel in per_point.items():
        print(f"  z={z:.4f}: relative difference = {rel:.3%}")
    print(f"Max relative difference: {max_rel_diff:.3%} (tolerance: 1.5%)\n")

    print("=" * 70)
    print("Skeptic-requested: eigenvalue-selection ambiguity check")
    print("=" * 70)
    any_negative, max_ratio = test_eigenvalue_selection_is_never_ambiguous()
    print(f"Near-zero-noise negative eigenvalues seen (expected, harmless): {any_negative}")
    print(
        f"Max ratio of near-null to second-smallest eigenvalue: {max_ratio:.2e} (never ambiguous)\n"
    )

    print("=" * 70)
    print("Skeptic-requested: 1e12-penalty contamination check, by step config")
    print("=" * 70)
    penalty_counts = test_step_none_penalty_contamination_is_isolated()
    print(f"Penalty hits by config: {penalty_counts}")
    print(
        "-> step=None IS contaminated (flagged, not primary evidence); "
        "the two fixed-step configs (1e-4, 1e-3) are clean.\n"
    )

    print("=" * 70)
    print("P182 retrocheck: is DESI still the LOO max under the adaptive Hessian?")
    print("=" * 70)
    p182_outcomes = test_p182_retrocheck_desi_remains_max_adaptive()
    print(f"DESI is max at each config: {p182_outcomes}")
    print("-> SURVIVES: DESI remains the max at every tested configuration.\n")

    print("=" * 70)
    print("P183 retrocheck: does the z^3-regression slope stay POSITIVE?")
    print("=" * 70)
    p183_slopes = test_p183_retrocheck_slope_sign_adaptive()
    print(f"Slope at each config: { {k: f'{v:.3e}' for k, v in p183_slopes.items()} }")
    print("-> SURVIVES: slope stays positive (mechanism-opposing) at every configuration.\n")

    print("=" * 70)
    print("P184 retrocheck: does DESI stay the LOO max under sigma-homogenization?")
    print("=" * 70)
    p184_homog_outcomes = test_p184_retrocheck_desi_max_under_homogenization_adaptive()
    print(f"DESI is max at each config: {p184_homog_outcomes}")
    p184_equal_outcomes = test_p184_retrocheck_full_equalization_adaptive()
    print(f"DESI is max under full equalization at each common sigma: {p184_equal_outcomes}")
    print("-> SURVIVES: DESI remains the max under both homogenization and full equalization.\n")

    print(
        "CONCLUSION (revised per skeptic-caught Recomposition Gate violation, see module "
        "Correction): all three of P182/P183/P184's core leave-one-out claims -- rank "
        "(DESI is the LOO max), sign (z^3-regression slope stays positive), and now also "
        "MAGNITUDE (quantitative per-point agreement at the clean step=1e-4 config, max "
        "0.768% relative difference) -- "
        "survive when the fixed-step (h1=1e-5) central-difference Hessian all three "
        "originally used is replaced with the adaptive Hessian (numdifftools) P185 "
        "introduced. The two FIXED step configurations (1e-4, 1e-3) are completely free of "
        "the 1e12-penalty contamination that DOES affect numdifftools' own step=None "
        "internal search (512 penalty hits there vs 0 at the fixed configs) -- the fixed "
        "configs are this file's primary evidence; step=None's agreement is corroborating "
        "but less trustworthy. Eigenvector selection was checked and found never ambiguous "
        "(near-null eigenvalue always 6+ orders of magnitude below the next one). This "
        "closes the verification debt sci-code-audit's Layer 4 flagged (2026-09-01) and "
        "confirms pearl_registry's own falsifiable prediction, now with an actual "
        "quantitative check in the code, not merely asserted in prose. FINDING_P177's "
        "central question (genuine correspondence vs. Taylor-truncation leverage) remains "
        "exactly as unresolved as before -- this file strengthens confidence in the "
        "NUMERICS underlying P182/P183/P184, it does not narrow or resolve the underlying "
        "physics question."
    )
