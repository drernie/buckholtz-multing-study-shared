"""detrend_and_rerun.py -- direct, decisive test of the redshift-
selection-confound hypothesis `diagnose_tsz_selection_confound.py`
raised: does subtracting a smooth T(z) trend and re-running the SAME
pairwise estimator collapse `run_real_data_phase2.py`'s own observed
signal (up to 4.35 sigma, monotonically growing with separation)?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

**Why this test, not just the correlation coefficient:** the raw
Pearson r(T,z)=0.068 is small, but real quartile means show a genuine,
directionally-consistent ~18uK trend (z=[0.2,0.376): -60.0uK vs
z=[0.635,0.8): -42.3uK) buried under 90uK of per-cluster scatter. A
small LINEAR correlation coefficient does not rule out a trend that,
once run through the actual pairwise weighting (Eq. 3's c_ij, which
grows for pairs with very different r_i -- i.e. very different z, the
exact pairs dominating large-separation bins), could still produce the
observed effect size. Detrend-and-rerun tests the real mechanism
directly instead of a proxy statistic.

Caches the (slow, ~10 min) per-cluster extraction to
`data_cache/extracted_temperatures_cache.npz` so repeated analysis
scripts on the same real data don't repeat that cost.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from exact_pair_census import Z_HIGH, Z_LOW, load_catalog, radec_z_to_cartesian_mpc
from pairwise_ksz_estimator import MIN_PAIRS_PER_BIN, core_pairwise_estimator
from real_map_extraction import extract_cluster_temperatures

# srcfree = ACT's own point-source-subtracted variant, adopted
# 2026-09-12 (see run_real_data_phase2.py's module docstring) -- cache
# filename changed too, so a stale raw-map cache is never silently
# reused under the srcfree name.
ACT_MAP_PATH = "data_cache/act_dr4dr6_coadd_AA_night_f150_map_srcfree.fits"
CACHE_PATH = Path("data_cache/extracted_temperatures_srcfree_cache.npz")


def _get_real_extraction() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Returns (ra, dec, z, temperature_uk) for real, on-map,
    finite-temperature clusters -- from cache if present, else extracts
    and writes the cache."""
    if CACHE_PATH.exists():
        print(f"STEP 1: loading cached extraction from {CACHE_PATH}")
        d = np.load(CACHE_PATH)
        return d["ra"], d["dec"], d["z"], d["temperature_uk"]

    print("STEP 1: no cache found -- real extraction (this is the ~10 min step)")
    ra, dec, z = load_catalog()
    ra = np.asarray(ra, dtype=float)
    dec = np.asarray(dec, dtype=float)
    z = np.asarray(z, dtype=float)
    ok = np.isfinite(ra) & np.isfinite(dec) & np.isfinite(z) & (z >= Z_LOW) & (z <= Z_HIGH)
    ra, dec, z = ra[ok], dec[ok], z[ok]
    extraction = extract_cluster_temperatures(ACT_MAP_PATH, ra, dec, aperture_radius_arcmin=1.0)
    valid = ~extraction.off_map & np.isfinite(extraction.temperature_uk)
    ra, dec, z = ra[valid], dec[valid], z[valid]
    temperature_uk = extraction.temperature_uk[valid]
    CACHE_PATH.parent.mkdir(exist_ok=True)
    np.savez(CACHE_PATH, ra=ra, dec=dec, z=z, temperature_uk=temperature_uk)
    print(f"  cached to {CACHE_PATH} for future re-use")
    return ra, dec, z, temperature_uk


def _run_estimator(pos_mpc: np.ndarray, q: np.ndarray, label: str) -> None:
    n = len(q)
    diff = pos_mpc[:, None, :] - pos_mpc[None, :, :]
    s_ij = np.linalg.norm(diff, axis=2)
    iu0, ju0 = np.triu_indices(n, k=1)
    r_bins = np.quantile(s_ij[iu0, ju0], np.linspace(0.0, 1.0, 8))
    r_bins[0] = 0.0
    res = core_pairwise_estimator(pos_mpc, q, r_bins)
    print(f"\n  --- {label} ---")
    print(f"  {'r (Mpc)':>10} {'p_pair':>12} {'+/- err':>10} {'z':>8} {'n_pairs':>9}")
    for rc, p, e, npair in zip(res.r_centers, res.p_pair, res.p_pair_err, res.n_pairs, strict=True):
        if npair < MIN_PAIRS_PER_BIN:
            continue
        z_score = p / e if e > 0 else np.nan
        print(f"  {rc:10.1f} {p:12.4f} {e:10.4f} {z_score:8.2f} {npair:9d}")


def main() -> None:
    ra, dec, z, t = _get_real_extraction()
    pos_mpc = radec_z_to_cartesian_mpc(ra, dec, z)
    print(f"  {len(t)} real clusters loaded")

    print("\nSTEP 2: ORIGINAL result -- raw T, no detrending (reproduces run_real_data_phase2.py)")
    _run_estimator(pos_mpc, -t, "ORIGINAL (raw T)")

    print("\nSTEP 3: fit and subtract a smooth T(z) trend (quadratic, the simplest model")
    print("  that can capture the non-monotonic quartile pattern seen in the diagnostic)")
    coeffs = np.polyfit(z, t, deg=2)
    t_trend = np.polyval(coeffs, z)
    t_detrended = t - t_trend
    print(f"  fit: T(z) = {coeffs[0]:.3f}*z^2 + {coeffs[1]:.3f}*z + {coeffs[2]:.3f}")
    print(
        f"  residual std after detrending: {np.std(t_detrended):.3f} uK "
        f"(was {np.std(t):.3f} uK before)"
    )

    print("\nSTEP 4: DETRENDED result -- same estimator, same bins, T(z)-trend removed")
    _run_estimator(pos_mpc, -t_detrended, "DETRENDED (T(z) removed)")

    print("\nHONEST SUMMARY")
    print("  If the detrended signal collapses toward |z|<3 across all bins, the")
    print("  z-dependent tSZ-selection artifact is confirmed as the dominant driver")
    print("  of the original signal. If it survives largely unchanged, the confound")
    print("  hypothesis is NOT sufficient by itself -- still not evidence for kSZ,")
    print("  since beam matching / point-source masking / a frozen protocol remain")
    print("  entirely unaddressed regardless of this test's outcome.")


if __name__ == "__main__":
    main()
