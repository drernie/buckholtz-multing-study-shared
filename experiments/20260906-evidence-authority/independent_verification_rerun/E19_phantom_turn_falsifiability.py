"""E19 -- is v82's H(z) "phantom turn" (a minimum near the present,
then rising) supported by real data, or below measurement precision at
low z? Answers Ernest Prabhakar's item 3.

Reuses (does not re-derive) E18's own already-verified H_of_z_single
from multing_fit_rerun.py -- this file adds only the minimum-finding,
data-range, and signal-vs-noise comparison, no new physics.

[SELF-CORRECTED after Step 8a skeptic, 6 real points, all fixed here --
see FINDING_E19's own Response Matrix for the full account. Process
note, disclosed not hidden: the first skeptic dispatch described this
method in prose rather than pasting the actual source -- the standing
project rule (paste the real code, always) was violated a third time.
Every point below was independently re-verified against real
math/data, not accepted on the skeptic's word alone.]

1. The original "signal-to-noise ratio" divided two PERCENTAGES with
   different denominators (dip%/H_model vs sigma%/H_data) -- not the
   same as an absolute-units ratio, and could silently mis-scale at a
   redshift where H_model and H_data diverge more. Fixed: compute both
   the dip and the noise in absolute km/s/Mpc, take their ratio
   directly (see `signal_vs_noise_absolute` below).
2. Comparing the dip only against 1-2 raw CC points' OWN sigma
   overestimates the noise floor relative to what the FIT's own
   parameter-covariance-propagated uncertainty on H_min would give --
   a full covariance propagation is out of this experiment's scope;
   the finding now states this explicitly as an unresolved caveat, not
   a "RESOLVED" conclusion.
3. "z_min sits within the CC data's sampled range" is technically true
   but rhetorically overclaims density of coverage -- z_min sits just
   past the 2nd-lowest CC point, in a sparsely-sampled interval, not on
   dense coverage. Reworded in the printed output.
4. The z_min discrepancy against TJB's own Claude-session-claimed value
   is COHERENT and ONE-SIDED across BOTH configurations (this
   project's z_min is higher in both cases) -- not attributable to
   "TJB's imprecision" without further checking. Reported as such.
5. Removed "RESOLVED"/"refutes" language -- reworded per this project's
   own standing rule against evaluative-authority framing.
6. PC1 is [TRIVIAL-BY-CONSTRUCTION], relabeled honestly. Added a real,
   non-trivial positive control (`test_positive_control_synthetic_
   known_minimum`) against a toy function with an ANALYTICALLY known
   minimum, run through the identical grid+refine machinery. Extended
   SC1's scan range to rule out other minima at higher z.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import csv
import os

import numpy as np
import yaml
from multing_fit_rerun import _HERE, H_of_z_single, z_SHOES
from scipy.optimize import minimize_scalar

ASSUMPTIONS_PATH = os.path.join(_HERE, "assumptions.yaml")
with open(ASSUMPTIONS_PATH) as f:
    _A = yaml.safe_load(f)
TABLE_II = _A["fitted_configurations"]

CC_DATA_PATH = os.path.join(
    _HERE,
    "..",
    "..",
    "..",
    "data",
    "source_material",
    "zenodo_21204955_supplemental",
    "data",
    "cosmic_chronometer_31pt.csv",
)

# TJB's own (externally-commissioned) Claude session's claimed values,
# for direct, explicit comparison -- not re-derived, quoted from his email.
TJB_CLAUDE_CLAIM = {
    "unconstrained_spotlighted": {"z_min": 0.086, "H_min": 72.4},
    "sh0es_anchored_0pct": {"z_min_range": (0.085, 0.09), "H_min": 72.2},
}


def load_cc_data():
    """Real, archived cosmic-chronometer data -- z, H, sigma, unmodified."""
    rows = []
    with open(os.path.abspath(CC_DATA_PATH)) as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append((float(r["z"]), float(r["H_kms_Mpc"]), float(r["sigma_kms_Mpc"])))
    return sorted(rows, key=lambda t: t[0])


def find_h_minimum(h_func, beta_1, beta_2, h0_anchor_kms, z_lo=1e-6, z_hi=0.5, n_grid=2000):
    """Grid scan + local refinement to find the precise (z, H) minimum
    of a given H(z)-shaped function. Parameterized over h_func so the
    same machinery can be exercised on a synthetic, analytically-known
    test function (see the positive control below), not only on the
    real MULTING H(z)."""
    z_grid = np.linspace(z_lo, z_hi, n_grid)
    H_grid = np.array([h_func(z, beta_1, beta_2, h0_anchor_kms) for z in z_grid])
    i_min = int(np.argmin(H_grid))
    lo = z_grid[max(0, i_min - 5)]
    hi = z_grid[min(n_grid - 1, i_min + 5)]
    res = minimize_scalar(
        lambda z: h_func(z, beta_1, beta_2, h0_anchor_kms),
        bounds=(lo, hi),
        method="bounded",
        options={"xatol": 1e-8},
    )
    z_min, H_min = res.x, res.fun
    return z_min, H_min, z_grid, H_grid


def find_h_minimum_real(beta_1, beta_2, h0_anchor_kms, z_hi=0.5, n_grid=2000):
    z_min, H_min, z_grid, H_grid = find_h_minimum(
        lambda z, b1, b2, h0: H_of_z_single(z, b1, b2, h0),
        beta_1,
        beta_2,
        h0_anchor_kms,
        z_hi=z_hi,
        n_grid=n_grid,
    )
    H_today = H_of_z_single(0.0, beta_1, beta_2, h0_anchor_kms)
    return z_min, H_min, H_today, z_grid, H_grid


def _synthetic_test_function(z, a, b, h0):
    """A toy function, UNRELATED to MULTING physics, with an
    analytically known minimum: h(z) = h0 + a*(z-b)**2. Minimum is
    exactly at z=b, value h0, by elementary calculus -- lets the
    grid+refine MACHINERY itself be checked against a known-correct
    answer, independent of whether the real MULTING physics is right."""
    return h0 + a * (z - b) ** 2


def test_positive_control_synthetic_known_minimum():
    """[Real, non-trivial control -- per Step 8a skeptic point 6.]
    Run the SAME find_h_minimum machinery on a toy function whose
    minimum is known exactly (z=0.15, value=70.0) and confirm it is
    recovered to high precision."""
    a, b_true, h0_true = 500.0, 0.15, 70.0
    z_min, H_min, _zg, _Hg = find_h_minimum(
        _synthetic_test_function, a, b_true, h0_true, z_lo=1e-6, z_hi=0.5, n_grid=2000
    )
    assert abs(z_min - b_true) < 1e-4, (z_min, b_true)
    assert abs(H_min - h0_true) < 1e-6, (H_min, h0_true)


def test_positive_control_anchor_recovered_trivial():
    """[TRIVIAL-BY-CONSTRUCTION -- per Step 8a skeptic point 6, relabeled
    honestly. This tests the anchoring code path, not the H(z) shape --
    H(z_SHOES)=H0_anchor is a definitional identity in this
    parametrization, not an independent check.]"""
    row = TABLE_II["unconstrained_spotlighted"]
    h = H_of_z_single(z_SHOES, row["beta_1"], row["beta_2"], row["H0_anchor_kms"])
    assert abs(h - row["H0_anchor_kms"]) < 1e-6, (h, row["H0_anchor_kms"])


def test_minimum_stable_across_grid_density():
    """Robustness check: the found z_min must be stable (<1% relative)
    across a 10x/10x change in grid density -- a NUMERICAL convergence
    check only (per Step 8a skeptic point 6: this does not by itself
    validate that the value is physically correct, only that the
    minimization is not a discretization artifact)."""
    row = TABLE_II["unconstrained_spotlighted"]
    z_min_200, _, _, _, _ = find_h_minimum_real(
        row["beta_1"], row["beta_2"], row["H0_anchor_kms"], n_grid=200
    )
    z_min_2000, _, _, _, _ = find_h_minimum_real(
        row["beta_1"], row["beta_2"], row["H0_anchor_kms"], n_grid=2000
    )
    z_min_20000, _, _, _, _ = find_h_minimum_real(
        row["beta_1"], row["beta_2"], row["H0_anchor_kms"], n_grid=20000
    )
    rel_200_2000 = abs(z_min_200 - z_min_2000) / z_min_2000
    rel_2000_20000 = abs(z_min_2000 - z_min_20000) / z_min_20000
    assert rel_200_2000 < 0.01, (z_min_200, z_min_2000, rel_200_2000)
    assert rel_2000_20000 < 0.01, (z_min_2000, z_min_20000, rel_2000_20000)
    return z_min_200, z_min_2000, z_min_20000


def test_sign_change_confirms_genuine_local_minimum_extended_range():
    """dH/dz must change sign exactly once over an EXTENDED range
    (z in [1e-6, 5], not just [1e-6, 0.5] -- per Step 8a skeptic point
    6: rules out a second local minimum at higher z that could
    otherwise be the one TJB's own Claude session actually meant)."""
    row = TABLE_II["unconstrained_spotlighted"]
    z_min, _H_min, _H_today, z_grid, H_grid = find_h_minimum_real(
        row["beta_1"], row["beta_2"], row["H0_anchor_kms"], z_hi=5.0, n_grid=20000
    )
    dH = np.diff(H_grid)
    sign_changes = np.sum(np.diff(np.sign(dH)) != 0)
    assert sign_changes == 1, (sign_changes, z_min)
    return z_min


def signal_vs_noise_absolute(H_today, H_min, sigma_abs_kms):
    """[Fixed per Step 8a skeptic point 1.] Absolute-units ratio: dip in
    km/s/Mpc divided by sigma in km/s/Mpc -- dimensionally consistent,
    not a ratio of two percentages with different denominators."""
    dip_abs = H_today - H_min
    return dip_abs, dip_abs / sigma_abs_kms


if __name__ == "__main__":
    test_positive_control_synthetic_known_minimum()
    print(
        "PC1 [real, non-trivial] synthetic toy function's known minimum (z=0.15, H=70.0) recovered: PASS"
    )

    test_positive_control_anchor_recovered_trivial()
    print("PC2 [TRIVIAL-BY-CONSTRUCTION] H(z_SHOES) recovers H0_anchor: PASS")

    z_min_ext = test_sign_change_confirms_genuine_local_minimum_extended_range()
    print("SC1 dH/dz changes sign exactly once over z in [1e-6,5] (no other minimum found): PASS")

    z200, z2000, z20000 = test_minimum_stable_across_grid_density()
    print(
        f"RC1 [numerical convergence only, not physical validation] z_min stable across grid density: "
        f"n=200 -> {z200:.5f}, n=2000 -> {z2000:.5f}, n=20000 -> {z20000:.5f}: PASS\n"
    )

    print("=" * 100)
    print("PART A -- independently-located H(z) minimum, both TJB Table II configurations")
    print("=" * 100)
    found = {}
    for cfg_name in ("unconstrained_spotlighted", "sh0es_anchored_0pct"):
        row = TABLE_II[cfg_name]
        z_min, H_min, H_today, _zg, _Hg = find_h_minimum_real(
            row["beta_1"], row["beta_2"], row["H0_anchor_kms"]
        )
        found[cfg_name] = (z_min, H_min, H_today)
        dip_abs, _ratio_placeholder = signal_vs_noise_absolute(H_today, H_min, 1.0)
        print(f"  {cfg_name}:")
        print(f"    H0_anchor (z={z_SHOES})  = {row['H0_anchor_kms']:.4f} km/s/Mpc")
        print(f"    minimum at z            = {z_min:.5f}")
        print(f"    H_min                   = {H_min:.4f} km/s/Mpc")
        print(f"    H(z=0, today)           = {H_today:.4f} km/s/Mpc")
        print(f"    dip depth, absolute     = {dip_abs:.4f} km/s/Mpc")

    print("\n" + "=" * 100)
    print("PART A2 -- direct comparison against TJB's own Claude session's claimed values")
    print("(NOT attributed to either side's error without further checking -- see interpretation)")
    print("=" * 100)
    for cfg_name, claim in TJB_CLAUDE_CLAIM.items():
        z_min, H_min, _H_today = found[cfg_name]
        if "z_min" in claim:
            rel = 100.0 * (z_min - claim["z_min"]) / claim["z_min"]
            print(
                f"  {cfg_name}: project z_min={z_min:.5f} vs TJB Claude z~{claim['z_min']} "
                f"-> {rel:+.1f}% (project is {'HIGHER' if rel > 0 else 'LOWER'})"
            )
        else:
            lo, hi = claim["z_min_range"]
            inside = lo <= z_min <= hi
            print(
                f"  {cfg_name}: project z_min={z_min:.5f} vs TJB Claude's stated range "
                f"[{lo},{hi}] -> {'INSIDE' if inside else 'OUTSIDE (above)' if z_min > hi else 'OUTSIDE (below)'}"
            )
    print(
        "\n  Both configurations show the project's own z_min ABOVE TJB's Claude-session value/range"
        " -- a COHERENT, ONE-SIDED offset, not scattered in both directions. This is reported as an"
        " unresolved, one-sided discrepancy, not attributed to 'TJB's imprecision' -- candidate"
        " explanations on EITHER side (a coarser age-redshift conversion on TJB's Claude session's"
        " side vs an unverified definitional subtlety on this project's side) are both possible and"
        " neither is confirmed here."
    )

    print("\n" + "=" * 100)
    print("PART B -- real CC data's own redshift coverage vs the found minimum location")
    print("=" * 100)
    cc = load_cc_data()
    z_lowest, H_lowest, sigma_lowest = cc[0]
    z_2nd, H_2nd, sigma_2nd = cc[1]
    print(f"  Lowest-z CC data point:  z={z_lowest}, H={H_lowest}+-{sigma_lowest} km/s/Mpc")
    print(f"  2nd-lowest-z CC point:   z={z_2nd}, H={H_2nd}+-{sigma_2nd} km/s/Mpc")
    print(f"  SH0ES anchor point:      z={z_SHOES} (below the CC data's own lowest z)")

    z_min, H_min, H_today = found["unconstrained_spotlighted"]
    print(f"\n  Found minimum location: z_min={z_min:.4f}")
    print(
        f"  -> z_min ({z_min:.4f}) sits just past the CC data's 2nd-lowest sampled point (z={z_2nd})"
        f" -- technically inside the data's own min-max z range, but in a SPARSELY-SAMPLED interval"
        f" between two individually noisy points, not on dense coverage. This is a weaker statement"
        f" than 'well-constrained by data' -- it means 'not on a future-extrapolated curve,' nothing"
        f" stronger. [Reworded per Step 8a skeptic point 3.]"
    )

    print("\n" + "=" * 100)
    print(
        "PART C -- signal (absolute dip) vs real, quoted noise (absolute CC sigma) at nearby points"
    )
    print(
        "[Fixed per Step 8a skeptic point 1: absolute km/s/Mpc ratio, not percentage-of-percentage]"
    )
    print("=" * 100)
    dip_abs, ratio_lowest = signal_vs_noise_absolute(H_today, H_min, sigma_lowest)
    _dip_abs2, ratio_2nd = signal_vs_noise_absolute(H_today, H_min, sigma_2nd)
    print(f"  Dip depth, absolute:                {dip_abs:.3f} km/s/Mpc")
    print(
        f"  Real quoted sigma at nearest points: {sigma_lowest} km/s/Mpc (z={z_lowest}), "
        f"{sigma_2nd} km/s/Mpc (z={z_2nd})"
    )
    print(
        f"  Ratio (dip_abs / sigma_abs):        {ratio_lowest:.3f}x (vs lowest-z point), "
        f"{ratio_2nd:.3f}x (vs 2nd-lowest)"
    )
    print(
        "\n  CAVEAT [per Step 8a skeptic point 2, not resolved here]: this compares the dip against"
        " RAW, individual CC point sigma -- NOT against the fit's own parameter-covariance-propagated"
        " uncertainty on H_min itself, which requires propagating beta1/beta2/H0_anchor's joint"
        " covariance through the nonlinear H(z) function (out of this experiment's scope). The fit's"
        " OWN uncertainty on H_min could in principle be TIGHTER than any single raw data point's own"
        " sigma (that is the general point of fitting many points jointly) -- so this ratio is a"
        " LOWER BOUND on how hard the dip would be to detect against the fit's own best uncertainty,"
        " not a final word. What IS established: measured against the actual, individual, quoted"
        " uncertainty of the two real data points nearest the claimed minimum, the dip is well below"
        " one sigma at both."
    )
    print(
        "\n  Also note [circularity caveat, per Step 8a skeptic point 6]: this project's own H_min"
        " value agrees closely with TJB's Claude session's claimed H_min (~72.4) largely because both"
        " evaluate the SAME closed-form MULTING H(z) formula with the SAME published beta values --"
        " agreement on the VALUE at a roughly-known z is close to forced. The genuinely diagnostic"
        " quantity is z_min itself (Part A2), where the two do NOT agree."
    )
