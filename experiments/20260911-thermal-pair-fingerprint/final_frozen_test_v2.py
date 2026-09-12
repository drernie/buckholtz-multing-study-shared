"""final_frozen_test_v2.py -- runs the pipeline and criteria frozen in
`FROZEN_PROTOCOL_v2.md` (independent-population holdout: DESI DR1 LRG
galaxies instead of v1's SZ-selected ACT-DR5 MCMF clusters). Mechanically
applies that file's PROMOTE/REJECT-MEASUREMENT-SUBSTRATE/INCONCLUSIVE
logic -- no interpretive choices are made here beyond what's already
spelled out in the frozen file.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from astropy.io import fits
from beam_correction import apply_beam_correction
from exact_pair_census import radec_z_to_cartesian_mpc
from pairwise_ksz_estimator import MIN_PAIRS_PER_BIN, PairwiseResult, core_pairwise_estimator
from real_map_extraction import extract_cluster_temperatures

DATA_CACHE = Path("data_cache")
ACT_MAP_PATH = DATA_CACHE / "act_dr4dr6_coadd_AA_night_f150_map_srcfree.fits"
DESI_NGC_PATH = DATA_CACHE / "LRG_NGC_clustering.dat.fits"
DESI_SGC_PATH = DATA_CACHE / "LRG_SGC_clustering.dat.fits"
CACHE_PATH = DATA_CACHE / "extracted_temperatures_desi_v2_cache.npz"

Z_LOW_V2, Z_HIGH_V2 = 0.4, 0.8  # frozen: DESI/MCMF overlap, FROZEN_PROTOCOL_v2.md SS1
N_SAMPLE = 4390  # frozen: matches v1's own sample size
RNG_SEED = 20260911
MAD_CLIP_SIGMA = 8.0
RAW_SIG_THRESHOLD = 3.0
DETREND_SIG_THRESHOLD = 2.0
N_SMALL_R_BINS_CHECKED = 2


def _load_desi_sample() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Real DESI DR1 LRG (RA, Dec, Z), NGC+SGC combined, frozen z-cut,
    frozen random subsample to N_SAMPLE."""
    ra_list, dec_list, z_list = [], [], []
    for path in (DESI_NGC_PATH, DESI_SGC_PATH):
        with fits.open(path) as hdul:
            data = hdul[1].data
            ra_list.append(np.asarray(data["RA"], dtype=float))
            dec_list.append(np.asarray(data["DEC"], dtype=float))
            z_list.append(np.asarray(data["Z"], dtype=float))
    ra = np.concatenate(ra_list)
    dec = np.concatenate(dec_list)
    z = np.concatenate(z_list)
    print(f"  {len(ra)} real DESI DR1 LRG objects loaded (NGC+SGC)")

    ok = np.isfinite(ra) & np.isfinite(dec) & np.isfinite(z) & (z >= Z_LOW_V2) & (z <= Z_HIGH_V2)
    ra, dec, z = ra[ok], dec[ok], z[ok]
    print(f"  {len(ra)} in frozen z-range [{Z_LOW_V2},{Z_HIGH_V2}]")

    rng = np.random.default_rng(RNG_SEED)
    if len(ra) > N_SAMPLE:
        idx = rng.choice(len(ra), size=N_SAMPLE, replace=False)
        ra, dec, z = ra[idx], dec[idx], z[idx]
    print(f"  {len(ra)} after frozen random subsample (seed={RNG_SEED})")
    return ra, dec, z


def _get_extraction() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if CACHE_PATH.exists():
        print(f"STEP 1: loading cached DESI extraction from {CACHE_PATH}")
        d = np.load(CACHE_PATH)
        return d["ra"], d["dec"], d["z"], d["temperature_uk"]

    print("STEP 1: no cache -- real extraction on DESI LRG positions")
    ra, dec, z = _load_desi_sample()
    extraction = extract_cluster_temperatures(
        str(ACT_MAP_PATH), ra, dec, aperture_radius_arcmin=1.0
    )
    valid = ~extraction.off_map & np.isfinite(extraction.temperature_uk)
    ra, dec, z = ra[valid], dec[valid], z[valid]
    t = extraction.temperature_uk[valid]
    print(f"  {len(t)} objects with a valid on-footprint extraction")
    CACHE_PATH.parent.mkdir(exist_ok=True)
    np.savez(CACHE_PATH, ra=ra, dec=dec, z=z, temperature_uk=t)
    return ra, dec, z, t


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
    ra, dec, z, t_raw = _get_extraction()
    pos_mpc = radec_z_to_cartesian_mpc(ra, dec, z)
    print(f"  {len(t_raw)} real DESI LRG objects ready")

    print("\nSTEP 2: beam correction (frozen: unchanged from v1)")
    t_beam = apply_beam_correction(t_raw)
    print(f"  raw T distribution: mean={np.mean(t_beam):+.3f} uK, std={np.std(t_beam):.3f} uK")

    print("\nSTEP 3: MAD outlier flag (frozen: unchanged, 8-sigma)")
    med = np.median(t_beam)
    mad = np.median(np.abs(t_beam - med)) * 1.4826
    outlier = mad > 0 and np.abs(t_beam - med) > MAD_CLIP_SIGMA * mad
    n_outlier = int(np.sum(outlier))
    print(f"  {n_outlier} object(s) flagged and excluded")
    pos_v = pos_mpc[~outlier]
    t_v = t_beam[~outlier]
    z_v = z[~outlier]

    print("\nSTEP 4: RAW pairwise result")
    res_raw = _pairwise_on(pos_v, -t_v)
    _print_result(res_raw, "RAW (beam-corrected, DESI LRG)")

    print("\nSTEP 5: DETRENDED pairwise result (frozen: quadratic T(z) subtracted)")
    coeffs = np.polyfit(z_v, t_v, deg=2)
    t_detrended = t_v - np.polyval(coeffs, z_v)
    res_detrend = _pairwise_on(pos_v, -t_detrended)
    _print_result(res_detrend, "DETRENDED (DESI LRG)")

    print("\nSTEP 6: mechanically apply FROZEN_PROTOCOL_v2.md's joint-clause logic")

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
    peak_at_max_r = max_abs_bin == valid_bins[-1]
    detrend_below_floor = not all(
        _trusted(res_detrend, i)
        and abs(res_detrend.p_pair[i] / res_detrend.p_pair_err[i]) >= DETREND_SIG_THRESHOLD
        for i in small_r_idx
    )
    systematic_detector_fires = peak_at_max_r and detrend_below_floor
    cond4prime_detrend_floor = not detrend_below_floor

    print(
        f"  Condition 1 (raw |z|>={RAW_SIG_THRESHOLD} in smallest {N_SMALL_R_BINS_CHECKED} bins): {cond1_raw_sig}"
    )
    print(f"  Condition 2 (correct sign): {cond2_correct_sign}")
    print(
        f"  Peak bin = {max_abs_bin}, largest-r bin = {valid_bins[-1]} -> peak_at_max_r = {peak_at_max_r}"
    )
    print(
        f"  Detrended below floor (|z|<{DETREND_SIG_THRESHOLD} in smallest bins) = {detrend_below_floor}"
    )
    print(
        f"  JOINT SYSTEMATIC-DETECTOR fires (peak_at_max_r AND below floor): {systematic_detector_fires}"
    )
    print(
        f"  Condition 4' (detrended |z|>={DETREND_SIG_THRESHOLD} floor, independent of shape): {cond4prime_detrend_floor}"
    )

    if (not (cond1_raw_sig and cond2_correct_sign)) or systematic_detector_fires:
        verdict = "REJECT-MEASUREMENT-SUBSTRATE"
    elif (
        cond1_raw_sig
        and cond2_correct_sign
        and (not systematic_detector_fires)
        and cond4prime_detrend_floor
    ):
        verdict = "PROMOTE"
    else:
        verdict = "INCONCLUSIVE"

    print(f"\nFINAL VERDICT (mechanical, per FROZEN_PROTOCOL_v2.md): {verdict}")
    print(
        "\nPer FROZEN_PROTOCOL_v2.md SS3: this is a methodological question (does v1's"
        " pattern travel with the SZ-selected population, or is it pipeline-wide?),"
        " NOT a MULTING test -- DESI LRGs carry no per-object mass characterization."
    )
    print(
        "\nPer FROZEN_PROTOCOL_v2.md SS5: an independent context-blind Agent(skeptic)"
        " review is required before this verdict is reported as final."
    )


if __name__ == "__main__":
    main()
