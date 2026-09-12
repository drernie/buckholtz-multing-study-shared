"""run_real_data_phase2.py -- first end-to-end real-data pass, Fork 1b
Phase 2: real ACT DR6 f150 GHz temperature map + real ACT-DR5 MCMF
cluster positions -> `pairwise_ksz_estimator.py`'s own validated
estimator math.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

**THIS IS AN ENGINEERING SHAKEOUT RUN, NOT THE PRE-REGISTERED TEST.**
`FINDING_pairwise_ksz_estimator_phase1.md`'s own remaining-work list
(item 4) requires freezing code and criteria BEFORE looking at any
result -- that freeze has NOT happened yet. This script's job is to
confirm the pipeline runs end-to-end on real data and to look honestly
at what the numbers look like, not to produce a claim about MULTING.
Concretely missing before any real claim would be licensed:

  - **[RESOLVED 2026-09-12]** Beam matching: analytic aperture
    correction (see `beam_correction.py`), validated against real 2D
    Gaussian convolution to 0.37% agreement. Uses FWHM=1.4' at f150,
    `[VERIFIED-arXiv:2406.14754]` (the ACT-DR5 MCMF catalog paper this
    pipeline already relies on) -- NOT DR6-native (the dedicated DR6
    beam paper, Duivenvoorden et al., is itself "in prep" per the DR6
    Maps paper's own reference list, same situation as the point-source
    catalog below). A uniform per-cluster multiplier does not change
    any z-score/significance result, only the absolute uK scale.
  - **[RESOLVED 2026-09-12]** Point-source handling: Hand et al. 2012
    excluded galaxies within 1' of a FIRST-catalog radio source. No
    equivalent DR6 point-source catalog is publicly released yet
    (Vargas et al., the dedicated DR6 point-source paper cited by the
    DR6 Maps paper itself, arXiv:2503.14451, is listed there as "2025,
    in preparation" -- checked directly in that paper's own reference
    list, not assumed). Used ACT's own `map_srcfree` product instead --
    the same DR6.02 coadd with all >=5-sigma point sources already
    subtracted by the ACT pipeline itself (median flux limit 8.4 mJy at
    f150, per the Maps paper's own Table in section V). This is a
    real, better-than-DIY-masking fix: no cluster is dropped, and the
    subtraction was done by the survey team with full knowledge of
    their own beam/noise properties.
  - No tau-weighting (this project's basic estimator does not need it
    for a detection statistic, per `pairwise_ksz_estimator.py`'s own
    module docstring -- but it means every cluster is weighted equally
    regardless of mass, losing real SNR a mass-weighted version would
    have).
  - N_kSZ (the T<->momentum normalization) is UNKNOWN -- results below
    are reported in raw temperature-difference units (uK), never
    converted to a physical velocity or compared to a physical
    threshold.

Any number this script prints is `[VERIFIED-SYNTHETIC-PIPELINE, REAL-
DATA-INPUT]` in the sense that the CODE ran on real data, not that the
result has been vetted as a real measurement -- see
`~/.claude/rules/skeptic-triggers.md` on why a clean-looking first
number on real data is exactly the shape of claim that needs a
skeptic pass before it means anything.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from beam_correction import (
    BEAM_FWHM_ARCMIN_F150,
    aperture_correction_factor,
    apply_beam_correction,
)
from exact_pair_census import Z_HIGH, Z_LOW, load_catalog, radec_z_to_cartesian_mpc
from pairwise_ksz_estimator import MIN_PAIRS_PER_BIN, core_pairwise_estimator
from real_map_extraction import extract_cluster_temperatures

RNG_SEED = 20260911
DATA_CACHE = Path(__file__).resolve().parent / "data_cache"
# srcfree = ACT's own point-source-subtracted variant (see module
# docstring's 2026-09-12 resolution note) -- preferred over the raw
# map now that both are available.
ACT_MAP_PATH = DATA_CACHE / "act_dr4dr6_coadd_AA_night_f150_map_srcfree.fits"


def _load_real_cluster_positions() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Real ACT-DR5 MCMF (RA, Dec, z), z-restricted per this
    experiment's own established Z_LOW/Z_HIGH convention -- returns
    (ra, dec, z, pos_mpc), no subsampling (real-data run uses the full
    restricted shell, unlike Phase 1's N=300 synthetic-signal
    validation, which subsampled only for jackknife wall-clock cost)."""
    ra, dec, z = load_catalog()
    ra = np.asarray(ra, dtype=float)
    dec = np.asarray(dec, dtype=float)
    z = np.asarray(z, dtype=float)
    ok = np.isfinite(ra) & np.isfinite(dec) & np.isfinite(z) & (z >= Z_LOW) & (z <= Z_HIGH)
    ra, dec, z = ra[ok], dec[ok], z[ok]
    pos_mpc = radec_z_to_cartesian_mpc(ra, dec, z)
    return ra, dec, z, pos_mpc


def main() -> None:
    if not ACT_MAP_PATH.exists():
        print(f"ACT map not found at {ACT_MAP_PATH} -- download not finished yet. Aborting.")
        sys.exit(1)
    size_gb = ACT_MAP_PATH.stat().st_size / 1e9
    print(f"STEP 0: real ACT DR6.02 f150 GHz map found, {size_gb:.3f} GB on disk")
    if size_gb < 5.0:
        print(
            "  WARNING: file is smaller than the verified 5.35 GB Content-Length -- "
            "download may be incomplete. Proceeding anyway; extraction will report "
            "off_map=True for anything beyond the truncated data."
        )

    print(f"\nSTEP 1: real ACT-DR5 MCMF cluster positions, z in [{Z_LOW:.1f},{Z_HIGH:.1f}]")
    ra, dec, z, pos_mpc = _load_real_cluster_positions()
    n_clusters = len(ra)
    print(f"  {n_clusters} real clusters")

    print("\nSTEP 2: real per-cluster temperature extraction from the ACT map")
    print(
        "  (aperture mean, 1' radius, map_srcfree -- point sources pre-subtracted; "
        "beam correction applied in STEP 2a below)"
    )
    extraction = extract_cluster_temperatures(
        str(ACT_MAP_PATH), ra, dec, aperture_radius_arcmin=1.0
    )
    n_off_map = int(np.sum(extraction.off_map))
    n_ok = n_clusters - n_off_map
    print(
        f"  {n_ok}/{n_clusters} clusters land inside the map footprint; {n_off_map} off-map (outside ACT's ~19,000 deg^2 coverage or too close to its edge)"
    )
    if n_ok < MIN_PAIRS_PER_BIN:
        print("  Too few clusters land on the map to run the estimator meaningfully. Stopping.")
        sys.exit(1)

    valid = ~extraction.off_map & np.isfinite(extraction.temperature_uk)
    pos_v = pos_mpc[valid]
    temp_v = extraction.temperature_uk[valid]
    print(f"  {len(temp_v)} clusters with a finite extracted temperature")

    print("\nSTEP 2a: beam (aperture) correction -- see beam_correction.py")
    beam_f = aperture_correction_factor()
    print(
        f"  1' aperture / {BEAM_FWHM_ARCMIN_F150}' FWHM beam -> f={beam_f:.4f}, "
        f"applying 1/f={1.0 / beam_f:.4f}x to every cluster uniformly"
    )
    temp_v = apply_beam_correction(temp_v)
    print(
        "  NOTE: a uniform multiplicative correction rescales p_pair AND its jackknife"
        " error by the same factor -- it does NOT change any z-score/significance"
        " result below, only the absolute uK scale (relevant once N_kSZ is known)."
    )
    print(
        f"  raw T distribution: mean={np.mean(temp_v):+.3f} uK, "
        f"std={np.std(temp_v):.3f} uK, min={np.min(temp_v):+.2f}, max={np.max(temp_v):+.2f}"
    )

    print("\nSTEP 2b: robust outlier flag (extra safety net on top of map_srcfree)")
    print(
        "  map_srcfree already subtracts >=5-sigma sources; this flags any surviving"
        " extreme outlier (e.g. a source just under that threshold, or a residual)."
    )
    med = np.median(temp_v)
    mad = np.median(np.abs(temp_v - med)) * 1.4826  # normal-consistent robust sigma
    clip_threshold = 8.0  # deliberately generous -- this is a safety net, not a real cut
    outlier = mad > 0 and np.abs(temp_v - med) > clip_threshold * mad
    n_outlier = int(np.sum(outlier))
    print(
        f"  robust median={med:+.3f} uK, robust sigma (MAD-based)={mad:.3f} uK, "
        f"{n_outlier} cluster(s) beyond {clip_threshold} robust-sigma flagged and excluded"
    )
    if n_outlier > 0:
        pos_v = pos_v[~outlier]
        temp_v = temp_v[~outlier]

    print("\nSTEP 3: pairwise-momentum estimator on REAL extracted temperatures")
    print("  (q = -T directly, N_kSZ=1 -- raw temperature-difference units, not physical velocity)")
    n_bins_target = 7
    n_v = len(pos_v)
    diff = pos_v[:, None, :] - pos_v[None, :, :]
    s_ij = np.linalg.norm(diff, axis=2)
    iu0, ju0 = np.triu_indices(n_v, k=1)
    r_bins = np.quantile(s_ij[iu0, ju0], np.linspace(0.0, 1.0, n_bins_target + 1))
    r_bins[0] = 0.0

    q = -temp_v  # q_i = -T_i / N_kSZ, N_kSZ=1 (see module docstring)
    res = core_pairwise_estimator(pos_v, q, r_bins)

    print(f"  {'r (Mpc)':>10} {'p_pair (uK)':>14} {'+/- err':>10} {'z':>8} {'n_pairs':>9}")
    any_trusted = False
    for rc, p, e, npair in zip(res.r_centers, res.p_pair, res.p_pair_err, res.n_pairs, strict=True):
        trusted = npair >= MIN_PAIRS_PER_BIN
        z_score = p / e if e > 0 else np.nan
        flag = "" if trusted else f"  [SKIP: n_pairs<{MIN_PAIRS_PER_BIN}]"
        if trusted:
            any_trusted = True
        print(f"  {rc:10.1f} {p:14.4f} {e:10.4f} {z_score:8.2f} {npair:9d}{flag}")

    print("\nHONEST SUMMARY -- read this before drawing any conclusion")
    print("  This is a first-pass engineering shakeout, not the pre-registered")
    print("  real-data test. Missing before any claim: beam matching, point-source")
    print("  masking, tau-weighting, and an actual freeze-then-look protocol.")
    print("  A signal (or non-signal) here says the PIPELINE runs end-to-end on")
    print("  real data -- it does NOT yet say anything trustworthy about MULTING.")
    if not any_trusted:
        print(
            "  No bin reached MIN_PAIRS_PER_BIN -- no usable real-data signal to even discuss yet."
        )


if __name__ == "__main__":
    main()
