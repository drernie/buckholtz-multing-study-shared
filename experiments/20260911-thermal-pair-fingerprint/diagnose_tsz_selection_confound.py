"""diagnose_tsz_selection_confound.py -- cheap diagnostic for the most
likely explanation of run_real_data_phase2.py's own first-pass result
(a strong, monotonically-growing-with-separation p_pair(r) signal, up
to 4.35 sigma, on RAW uncorrected temperatures with mean=-49uK).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

**Hypothesis under test:** the ACT-DR5 MCMF cluster catalog is ITSELF
tSZ-selected (Multi-Component Matched Filter confirmation of ACT's own
SZ-detected candidates) -- extracting "temperature at the cluster
position" from an ACT temperature map is then partially circular (the
cluster is IN the catalog largely because it has a strong decrement
there). If survey depth/mass-completeness evolves with redshift (a
well-known SZ-survey effect: a roughly z-independent SZ flux limit
means only increasingly massive, higher-decrement clusters are
detectable at higher z), T_i should correlate with z_i / r_i (distance
from observer). Pairs with the LARGEST 3D separation `s` are
overwhelmingly pairs with very DIFFERENT r_i (one low-z, one high-z,
not physically associated) -- if T correlates with r, such pairs get a
large, systematic (T_i-T_j) difference with LARGE Eq.3 weight `c_ij`
(which grows with |r_i-r_j|), reproducing exactly the observed
"grows with separation" pattern WITHOUT any real kSZ/velocity signal.

This is a cheap, direct, decisive test: does T_i actually correlate
with z_i (or r_i)? No pairwise machinery needed.
"""

from __future__ import annotations

import numpy as np
from astropy.io import fits
from exact_pair_census import Z_HIGH, Z_LOW, load_catalog, radec_z_to_cartesian_mpc
from real_map_extraction import extract_cluster_temperatures
from scipy import stats

ACT_MAP_PATH = "data_cache/act_dr4dr6_coadd_AA_night_f150_map.fits"


def main() -> None:
    print("STEP 0: check the map's own declared units (BUNIT), not assumed")
    with fits.open(ACT_MAP_PATH) as hdul:
        header = hdul[0].header
        bunit = header.get("BUNIT", "NOT SET")
        print(f"  BUNIT = {bunit!r}")

    print("\nSTEP 1: real ACT-DR5 MCMF cluster positions + redshifts")
    ra, dec, z = load_catalog()
    ra = np.asarray(ra, dtype=float)
    dec = np.asarray(dec, dtype=float)
    z = np.asarray(z, dtype=float)
    ok = np.isfinite(ra) & np.isfinite(dec) & np.isfinite(z) & (z >= Z_LOW) & (z <= Z_HIGH)
    ra, dec, z = ra[ok], dec[ok], z[ok]
    print(f"  {len(ra)} real clusters, z in [{Z_LOW},{Z_HIGH}]")

    print("\nSTEP 2: re-extract temperatures (same as the shakeout run, for a direct T-vs-z test)")
    extraction = extract_cluster_temperatures(ACT_MAP_PATH, ra, dec, aperture_radius_arcmin=1.0)
    valid = ~extraction.off_map & np.isfinite(extraction.temperature_uk)
    z_v = z[valid]
    t_v = extraction.temperature_uk[valid]
    pos_v = radec_z_to_cartesian_mpc(ra[valid], dec[valid], z_v)
    r_v = np.linalg.norm(pos_v, axis=1)

    print("\nSTEP 3: does T_i correlate with z_i (redshift) or r_i (distance from observer)?")
    r_z, p_z = stats.pearsonr(z_v, t_v)
    r_r, p_r = stats.pearsonr(r_v, t_v)
    print(f"  Pearson r(T, z)  = {r_z:+.4f}  (p={p_z:.2e})")
    print(f"  Pearson r(T, r)  = {r_r:+.4f}  (p={p_r:.2e})")

    print("\nSTEP 4: mean T in redshift quartiles -- direct, visual, no model assumed")
    quartile_edges = np.quantile(z_v, [0, 0.25, 0.5, 0.75, 1.0])
    for i in range(4):
        lo, hi = quartile_edges[i], quartile_edges[i + 1]
        sel = (z_v >= lo) & (z_v <= hi) if i == 3 else (z_v >= lo) & (z_v < hi)
        print(
            f"  z in [{lo:.3f},{hi:.3f}): n={np.sum(sel):4d}, "
            f"mean T={np.mean(t_v[sel]):+8.3f} uK, median T={np.median(t_v[sel]):+8.3f} uK"
        )

    print("\nVERDICT")
    strong_corr = abs(r_z) > 0.1 and p_z < 1e-6
    print(f"  T significantly correlates with z: {strong_corr} (|r|={abs(r_z):.4f}, p={p_z:.2e})")
    if strong_corr:
        print(
            "  CONFIRMS the redshift-dependent-selection hypothesis: the shakeout run's"
            " 'signal' is very likely dominated by this artifact, not kSZ. The pairwise"
            " estimator must NOT be trusted on raw T until this is removed (e.g. by"
            " detrending T against z/mass before differencing, or restricting to a"
            " narrow, mass-matched sub-sample)."
        )
    else:
        print(
            "  Does NOT confirm this specific hypothesis -- the growing-with-r pattern"
            " needs a different explanation, not yet identified. Do not treat the"
            " shakeout's p_pair(r) numbers as a kSZ signal either way without further"
            " investigation."
        )


if __name__ == "__main__":
    main()
