"""apply_v3_relabeling.py -- mechanically re-applies the split-label
verdict scheme frozen in `FROZEN_PROTOCOL_v3.md` to v1's and v2's own
already-frozen raw/detrended pairwise numbers, recomputed directly from
each test's own cached real-data extraction (not hand-transcribed from
the FINDING files).

NOT a new blind test -- v1's and v2's results are already known. What
is genuinely fixed in advance is the relabeling logic itself
(`FROZEN_PROTOCOL_v3.md`, committed before this script). Every pipeline
step below (beam correction, MAD outlier flag, pairwise estimator,
quadratic detrend, bin thresholds) is copied verbatim from
`final_frozen_test.py` / `final_frozen_test_v2.py` -- neither frozen
script is imported from or edited; this script only adds a new label
function on top of the same computation, run independently so a
transcription error in either original script cannot silently repeat
itself here.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from beam_correction import apply_beam_correction
from exact_pair_census import radec_z_to_cartesian_mpc
from pairwise_ksz_estimator import MIN_PAIRS_PER_BIN, PairwiseResult, core_pairwise_estimator

DATA_CACHE = Path("data_cache")
V1_CACHE = DATA_CACHE / "extracted_temperatures_srcfree_cache.npz"
V2_CACHE = DATA_CACHE / "extracted_temperatures_desi_v2_cache.npz"

RAW_SIG_THRESHOLD = 3.0
DETREND_SIG_THRESHOLD = 2.0
N_SMALL_R_BINS_CHECKED = 2
MAD_CLIP_SIGMA = 8.0


@dataclass(frozen=True)
class Conditions:
    cond1_raw_sig: bool
    cond2_correct_sign: bool
    peak_bin: int
    largest_bin: int
    peak_at_max_r: bool
    detrend_below_floor: bool


def _pairwise_on(pos_mpc: np.ndarray, q: np.ndarray) -> PairwiseResult:
    n = len(q)
    diff = pos_mpc[:, None, :] - pos_mpc[None, :, :]
    s_ij = np.linalg.norm(diff, axis=2)
    iu0, ju0 = np.triu_indices(n, k=1)
    r_bins = np.quantile(s_ij[iu0, ju0], np.linspace(0.0, 1.0, 8))
    r_bins[0] = 0.0
    return core_pairwise_estimator(pos_mpc, q, r_bins)


def _trusted(res: PairwiseResult, i: int) -> bool:
    return res.n_pairs[i] >= MIN_PAIRS_PER_BIN


def _print_result(res: PairwiseResult, label: str) -> None:
    print(f"\n  --- {label} ---")
    print(f"  {'r (Mpc)':>10} {'p_pair':>12} {'+/- err':>10} {'z':>8} {'n_pairs':>9}")
    for rc, p, e, npair in zip(res.r_centers, res.p_pair, res.p_pair_err, res.n_pairs, strict=True):
        z_score = p / e if e > 0 else np.nan
        print(f"  {rc:10.1f} {p:12.4f} {e:10.4f} {z_score:8.2f} {npair:9d}")


def _compute_conditions(res_raw: PairwiseResult, res_detrend: PairwiseResult) -> Conditions:
    small_r_idx = list(range(N_SMALL_R_BINS_CHECKED))
    cond1_raw_sig = all(
        _trusted(res_raw, i) and abs(res_raw.p_pair[i] / res_raw.p_pair_err[i]) >= RAW_SIG_THRESHOLD
        for i in small_r_idx
    )
    cond2_correct_sign = all(res_raw.p_pair[i] < 0 for i in small_r_idx)
    valid_bins = [i for i in range(len(res_raw.p_pair)) if _trusted(res_raw, i)]
    max_abs_bin = max(valid_bins, key=lambda i: abs(res_raw.p_pair[i]))
    largest_bin = valid_bins[-1]
    peak_at_max_r = max_abs_bin == largest_bin
    detrend_below_floor = not all(
        _trusted(res_detrend, i)
        and abs(res_detrend.p_pair[i] / res_detrend.p_pair_err[i]) >= DETREND_SIG_THRESHOLD
        for i in small_r_idx
    )
    return Conditions(
        cond1_raw_sig=cond1_raw_sig,
        cond2_correct_sign=cond2_correct_sign,
        peak_bin=max_abs_bin,
        largest_bin=largest_bin,
        peak_at_max_r=peak_at_max_r,
        detrend_below_floor=detrend_below_floor,
    )


def apply_v3_label(c: Conditions) -> str:
    """FROZEN_PROTOCOL_v3.md SS2 -- mechanical, no interpretive choices."""
    if not (c.cond1_raw_sig and c.cond2_correct_sign):
        return "NULL-BELOW-DETECTION-THRESHOLD"
    if c.peak_at_max_r and c.detrend_below_floor:
        return "REJECT-SUBSTRATE-SYSTEMATIC"
    if not c.detrend_below_floor:
        return "PROMOTE"
    return "INCONCLUSIVE"


def _run_v1() -> Conditions:
    if not V1_CACHE.exists():
        raise SystemExit(f"v1 cache not found at {V1_CACHE}")
    print("=== v1 (ACT-DR5 MCMF, srcfree map) ===")
    d = np.load(V1_CACHE)
    ra, dec, z, t_raw = d["ra"], d["dec"], d["z"], d["temperature_uk"]
    pos_mpc = radec_z_to_cartesian_mpc(ra, dec, z)
    print(f"  {len(t_raw)} real clusters (recomputed from cache, not hand-transcribed)")

    t_beam = apply_beam_correction(t_raw)
    med = np.median(t_beam)
    mad = np.median(np.abs(t_beam - med)) * 1.4826
    outlier = mad > 0 and np.abs(t_beam - med) > MAD_CLIP_SIGMA * mad
    pos_v, t_v, z_v = pos_mpc[~outlier], t_beam[~outlier], z[~outlier]

    res_raw = _pairwise_on(pos_v, -t_v)
    _print_result(res_raw, "RAW")
    coeffs = np.polyfit(z_v, t_v, deg=2)
    t_detrended = t_v - np.polyval(coeffs, z_v)
    res_detrend = _pairwise_on(pos_v, -t_detrended)
    _print_result(res_detrend, "DETRENDED")

    return _compute_conditions(res_raw, res_detrend)


def _run_v2() -> Conditions:
    if not V2_CACHE.exists():
        raise SystemExit(f"v2 cache not found at {V2_CACHE}")
    print("\n=== v2 (DESI DR1 LRG) ===")
    d = np.load(V2_CACHE)
    ra, dec, z, t_raw = d["ra"], d["dec"], d["z"], d["temperature_uk"]
    pos_mpc = radec_z_to_cartesian_mpc(ra, dec, z)
    print(f"  {len(t_raw)} real DESI LRG objects (recomputed from cache, not hand-transcribed)")

    t_beam = apply_beam_correction(t_raw)
    med = np.median(t_beam)
    mad = np.median(np.abs(t_beam - med)) * 1.4826
    outlier = mad > 0 and np.abs(t_beam - med) > MAD_CLIP_SIGMA * mad
    pos_v, t_v, z_v = pos_mpc[~outlier], t_beam[~outlier], z[~outlier]

    res_raw = _pairwise_on(pos_v, -t_v)
    _print_result(res_raw, "RAW")
    coeffs = np.polyfit(z_v, t_v, deg=2)
    t_detrended = t_v - np.polyval(coeffs, z_v)
    res_detrend = _pairwise_on(pos_v, -t_detrended)
    _print_result(res_detrend, "DETRENDED")

    return _compute_conditions(res_raw, res_detrend)


def main() -> None:
    c1 = _run_v1()
    c2 = _run_v2()

    label1 = apply_v3_label(c1)
    label2 = apply_v3_label(c2)

    print("\n=== FROZEN_PROTOCOL_v3.md SS2 mechanical relabeling ===")
    print(
        f"v1: cond1={c1.cond1_raw_sig} cond2={c1.cond2_correct_sign} "
        f"peak_at_max_r={c1.peak_at_max_r} (peak_bin={c1.peak_bin}, largest_bin={c1.largest_bin}) "
        f"detrend_below_floor={c1.detrend_below_floor} -> {label1}"
    )
    print(
        f"v2: cond1={c2.cond1_raw_sig} cond2={c2.cond2_correct_sign} "
        f"peak_at_max_r={c2.peak_at_max_r} (peak_bin={c2.peak_bin}, largest_bin={c2.largest_bin}) "
        f"detrend_below_floor={c2.detrend_below_floor} -> {label2}"
    )

    predicted = ("REJECT-SUBSTRATE-SYSTEMATIC", "NULL-BELOW-DETECTION-THRESHOLD")
    actual = (label1, label2)
    verdict = "CONFIRMED" if actual == predicted else "REFUTED"

    print("\n=== FROZEN_PROTOCOL_v3.md SS3 falsifiable prediction ===")
    print(f"  predicted: v1={predicted[0]}, v2={predicted[1]}")
    print(f"  actual:    v1={actual[0]}, v2={actual[1]}")
    print(f"  VERDICT: {verdict}")


if __name__ == "__main__":
    main()
