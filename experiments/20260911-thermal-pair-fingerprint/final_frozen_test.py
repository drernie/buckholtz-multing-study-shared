"""final_frozen_test.py -- runs the pipeline and criteria frozen in
`FROZEN_PROTOCOL_v1.md` (commit 8161242, written and committed BEFORE
this script was run). Mechanically applies that file's PROMOTE/REJECT/
INCONCLUSIVE logic -- no interpretive choices are made here that are
not already spelled out in the frozen file.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from beam_correction import apply_beam_correction
from exact_pair_census import radec_z_to_cartesian_mpc
from pairwise_ksz_estimator import MIN_PAIRS_PER_BIN, PairwiseResult, core_pairwise_estimator

CACHE_PATH = Path("data_cache/extracted_temperatures_srcfree_cache.npz")
RAW_SIG_THRESHOLD = 3.0  # FROZEN_PROTOCOL_v1.md condition 1
DETREND_SIG_THRESHOLD = 2.0  # FROZEN_PROTOCOL_v1.md condition 4
N_SMALL_R_BINS_CHECKED = 2  # "the two smallest-separation bins"
MAD_CLIP_SIGMA = 8.0  # same as run_real_data_phase2.py STEP 2b


def _pairwise_on(pos_mpc: np.ndarray, q: np.ndarray) -> PairwiseResult:
    n = len(q)
    diff = pos_mpc[:, None, :] - pos_mpc[None, :, :]
    s_ij = np.linalg.norm(diff, axis=2)
    iu0, ju0 = np.triu_indices(n, k=1)
    r_bins = np.quantile(s_ij[iu0, ju0], np.linspace(0.0, 1.0, 8))
    r_bins[0] = 0.0
    return core_pairwise_estimator(pos_mpc, q, r_bins)


def _print_result(res: PairwiseResult, label: str) -> None:
    print(f"\n  --- {label} ---")
    print(f"  {'r (Mpc)':>10} {'p_pair':>12} {'+/- err':>10} {'z':>8} {'n_pairs':>9}")
    for rc, p, e, npair in zip(res.r_centers, res.p_pair, res.p_pair_err, res.n_pairs, strict=True):
        z_score = p / e if e > 0 else np.nan
        print(f"  {rc:10.1f} {p:12.4f} {e:10.4f} {z_score:8.2f} {npair:9d}")


def main() -> None:
    if not CACHE_PATH.exists():
        raise SystemExit(f"Cache not found at {CACHE_PATH} -- run detrend_and_rerun.py first.")

    print("STEP 1: load cached real extraction (srcfree map, per FROZEN_PROTOCOL_v1.md)")
    d = np.load(CACHE_PATH)
    ra, dec, z, t_raw = d["ra"], d["dec"], d["z"], d["temperature_uk"]
    pos_mpc = radec_z_to_cartesian_mpc(ra, dec, z)
    print(f"  {len(t_raw)} real clusters")

    print("\nSTEP 2: beam correction (frozen: FWHM=1.4', per beam_correction.py)")
    t_beam = apply_beam_correction(t_raw)

    print("\nSTEP 3: MAD outlier flag (frozen: 8-sigma robust threshold)")
    med = np.median(t_beam)
    mad = np.median(np.abs(t_beam - med)) * 1.4826
    outlier = mad > 0 and np.abs(t_beam - med) > MAD_CLIP_SIGMA * mad
    n_outlier = int(np.sum(outlier))
    print(f"  {n_outlier} cluster(s) flagged and excluded")
    pos_v = pos_mpc[~outlier]
    t_v = t_beam[~outlier]

    print("\nSTEP 4: RAW pairwise result (frozen pipeline, no detrending)")
    res_raw = _pairwise_on(pos_v, -t_v)
    _print_result(res_raw, "RAW (beam-corrected)")

    print("\nSTEP 5: DETRENDED pairwise result (frozen: quadratic T(z) subtracted)")
    coeffs = np.polyfit(z[~outlier], t_v, deg=2)
    t_detrended = t_v - np.polyval(coeffs, z[~outlier])
    res_detrend = _pairwise_on(pos_v, -t_detrended)
    _print_result(res_detrend, "DETRENDED")

    print("\nSTEP 6: mechanically apply FROZEN_PROTOCOL_v1.md's PROMOTE/REJECT/INCONCLUSIVE logic")

    def _trusted(res: PairwiseResult, i: int) -> bool:
        return res.n_pairs[i] >= MIN_PAIRS_PER_BIN

    small_r_idx = list(range(N_SMALL_R_BINS_CHECKED))

    cond1_raw_sig = all(
        _trusted(res_raw, i) and abs(res_raw.p_pair[i] / res_raw.p_pair_err[i]) >= RAW_SIG_THRESHOLD
        for i in small_r_idx
    )
    cond2_correct_sign = all(res_raw.p_pair[i] < 0 for i in small_r_idx)
    valid_bins = [i for i in range(len(res_raw.p_pair)) if _trusted(res_raw, i)]
    max_abs_bin = max(valid_bins, key=lambda i: abs(res_raw.p_pair[i]))
    cond3_not_artifact_shape = max_abs_bin != valid_bins[-1]
    cond4_survives_detrend = all(
        _trusted(res_detrend, i)
        and abs(res_detrend.p_pair[i] / res_detrend.p_pair_err[i]) >= DETREND_SIG_THRESHOLD
        for i in small_r_idx
    )

    print(
        f"  Condition 1 (raw |z|>={RAW_SIG_THRESHOLD} in smallest {N_SMALL_R_BINS_CHECKED} bins): {cond1_raw_sig}"
    )
    print(f"  Condition 2 (correct sign, negative/infall, smallest bins): {cond2_correct_sign}")
    print(
        f"  Condition 3 (peak |p_pair| NOT at largest-separation bin; "
        f"peak is at bin index {max_abs_bin}, largest bin is index {valid_bins[-1]}): "
        f"{cond3_not_artifact_shape}"
    )
    print(
        f"  Condition 4 (detrended |z|>={DETREND_SIG_THRESHOLD} in smallest {N_SMALL_R_BINS_CHECKED} bins): {cond4_survives_detrend}"
    )

    if not (cond1_raw_sig and cond2_correct_sign):
        verdict = "REJECT"
    elif (
        cond1_raw_sig and cond2_correct_sign and cond3_not_artifact_shape and cond4_survives_detrend
    ):
        verdict = "PROMOTE"
    else:
        verdict = "INCONCLUSIVE"

    print(f"\nFINAL VERDICT (mechanical, per FROZEN_PROTOCOL_v1.md): {verdict}")
    print(
        "\nPer FROZEN_PROTOCOL_v1.md Section 3's own closing paragraph: this verdict,"
        " whatever it is, does NOT by itself establish or refute MULTING -- see that"
        " file for the full caveat before this number is used anywhere else."
    )
    print(
        "\nPer FROZEN_PROTOCOL_v1.md Section 4: an independent context-blind"
        " Agent(skeptic) review (criteria + numeric output only, no reasoning chain)"
        " is required before this verdict is reported as final."
    )


if __name__ == "__main__":
    main()
