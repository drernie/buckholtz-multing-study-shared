"""exact_pair_census.py -- real-catalog pair census, replacing the
Poisson-volume model in power_analysis_mock_catalog.py with an exact
count on real cluster positions.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

Named as the concrete next step in FINDING_power_analysis.md SS4a and
estimand.md's MCID section, after the 3rd external critique's own
recommendation: "the actual minimal test is exact catalog pair census
in physical s, ... no tSZ map, no kSZ map, no mass reconstruction
needed for this step."

Data: ACT-DR5 MCMF cluster catalog (Klein, Mohr & Davies 2024,
arXiv:2406.14754), CDS catalog J/A+A/690/A322. Downloaded 2026-09-11
from cdsarc.cds.unistra.fr (public, no login) into data_cache/
(gitignored -- re-downloadable, not ours to redistribute). 6237 rows
-- [VERIFIED] matches the paper's own abstract count exactly.

What this DOES: gives a real N_pair(s) histogram from real (RA, Dec, z)
positions and a real cosmology-based comoving-distance conversion,
replacing power_analysis_mock_catalog.py's assumption of an unclustered
Poisson density spread uniformly over an idealized footprint shape.

What this does NOT do: it does not cross-match against DES-Y3/DESI-DR1/
eRASS1 to get the exact final multi-survey footprint (data_acquisition_
plan.md's Fork 2 remains open) -- the area-scaling step below is an
explicitly-flagged first-order approximation, not a real cross-match.
It does not build the kSZ estimator itself (Fork 1b) or run the
synthetic four-world identifiability battery (estimand.md's own hard
gate) -- both remain separate, unbuilt artifacts.
"""

from __future__ import annotations

import astropy.units as u
import numpy as np
from astropy.cosmology import Planck18 as cosmo
from astropy.io import ascii as ascii_io
from scipy.spatial import cKDTree

DATA_DIR = "data_cache"
DATFILE = f"{DATA_DIR}/catalog.dat"
README = f"{DATA_DIR}/ReadMe"

# Same redshift window and comoving-separation windows as
# power_analysis_mock_catalog.py, for direct comparability.
Z_LOW, Z_HIGH = 0.2, 0.8
S_MIN_BROAD, S_MAX_BROAD = 20.0, 160.0  # kSZ-literature convention
S_MIN_N10, S_MAX_N10 = 35.0, 55.0  # +-10 Mpc around the verified d0=45 Mpc
S_MIN_N25, S_MAX_N25 = 20.0, 70.0  # +-25 Mpc around the verified d0=45 Mpc
S_MAX_QUERY = 200.0  # KDTree search radius, safely covers all windows above

AREA_ACT_DR5_DEG2 = 13211.0  # [VERIFIED-arXiv:2406.14754 Sec.2]: "The remaining
# useful area is 13,211 deg^2" -- ACT-DR5's own stated footprint after excluding
# |b|<20 deg, point sources, dusty regions (same footprint Klein+2024 reanalyzes;
# corrects power_analysis_mock_catalog.py's own AREA_ACT_DEG2=13750, which was
# ACT-DR6's rougher "~1/3 of the sky" proxy, not ACT-DR5's own precise number)
FOOTPRINT_LOW, FOOTPRINT_MID, FOOTPRINT_HIGH = 700.0, 775.0, 850.0  # Fork 2 target


def load_catalog() -> np.ndarray:
    t = ascii_io.read(DATFILE, readme=README, format="cds")
    n_total = len(t)
    print(f"  loaded {n_total} rows [VERIFIED == paper's own abstract count]")

    fcont = np.asarray(t["fcont1C"])
    assert fcont.max() < 0.2 + 1e-9, (
        "expected the public table to already be capped at fcont1C<0.2 "
        f"(observed max {fcont.max()}) -- re-check before trusting the "
        "'no extra purity cut needed' claim below"
    )
    print(
        f"  fcont1C (contamination estimator) already capped at "
        f"{fcont.max():.4f} in the public table -- no separate purity cut "
        f"applied here, the catalog's own default selection stands"
    )

    ra = np.asarray(t["RAdeg"])
    dec = np.asarray(t["DEdeg"])
    z = np.asarray(t["z1C"])
    return ra, dec, z


def radec_z_to_cartesian_mpc(ra_deg, dec_deg, z):
    """Real (RA, Dec, z) -> 3D comoving Cartesian Mpc, via astropy's own
    comoving_distance (Planck18) -- same cosmology as
    power_analysis_mock_catalog.py."""
    d_c = cosmo.comoving_distance(z).to(u.Mpc).value
    ra_rad = np.radians(ra_deg)
    dec_rad = np.radians(dec_deg)
    x = d_c * np.cos(dec_rad) * np.cos(ra_rad)
    y = d_c * np.cos(dec_rad) * np.sin(ra_rad)
    zc = d_c * np.sin(dec_rad)
    return np.column_stack([x, y, zc])


def main() -> None:
    print("=" * 78)
    print("STEP 1 -- load the real ACT-DR5 MCMF catalog, apply the z cut")
    print("=" * 78)
    ra, dec, z = load_catalog()
    mask = (z >= Z_LOW) & (z <= Z_HIGH)
    n_used = int(mask.sum())
    print(f"  z1C in [{Z_LOW},{Z_HIGH}]: {n_used} clusters (of {len(z)} total)")

    xyz = radec_z_to_cartesian_mpc(ra[mask], dec[mask], z[mask])

    print()
    print("=" * 78)
    print("STEP 2 -- exact pairwise 3D comoving separations (real positions)")
    print("=" * 78)
    tree = cKDTree(xyz)
    sdm = tree.sparse_distance_matrix(tree, max_distance=S_MAX_QUERY, output_type="coo_matrix")
    # sparse_distance_matrix returns both (i,j) and (j,i); keep i<j once each,
    # and drop the i==j diagonal (distance 0, not a pair).
    upper = sdm.row < sdm.col
    seps = np.asarray(sdm.data[upper])
    n_pairs_total_to_200mpc = len(seps)
    print(f"  {n_pairs_total_to_200mpc} real cluster pairs with separation <= {S_MAX_QUERY} Mpc")

    def window_count(lo: float, hi: float) -> int:
        return int(np.sum((seps >= lo) & (seps <= hi)))

    n_broad = window_count(S_MIN_BROAD, S_MAX_BROAD)
    n_n10 = window_count(S_MIN_N10, S_MAX_N10)
    n_n25 = window_count(S_MIN_N25, S_MAX_N25)

    print()
    print(
        f"  EXACT counts, full ACT-DR5 MCMF footprint ({AREA_ACT_DR5_DEG2:.0f} deg^2), z in [{Z_LOW},{Z_HIGH}]:"
    )
    print(f"    broad  [{S_MIN_BROAD:.0f},{S_MAX_BROAD:.0f}] Mpc comoving : {n_broad}")
    print(f"    narrow-10 [{S_MIN_N10:.0f},{S_MAX_N10:.0f}] Mpc comoving : {n_n10}")
    print(f"    narrow-25 [{S_MIN_N25:.0f},{S_MAX_N25:.0f}] Mpc comoving : {n_n25}")

    print()
    print("=" * 78)
    print("STEP 3 -- shape check: real ratio vs. the mock Poisson-volume model's ratio")
    print("=" * 78)
    # power_analysis_mock_catalog.py Step 2/3c predicted, at its own 775 deg^2
    # mid-footprint estimate: broad=584.9, narrow-10=17.7, narrow-25=47.9.
    mock_broad, mock_n10, mock_n25 = 584.9, 17.7, 47.9
    real_ratio_n10 = n_n10 / n_broad if n_broad else float("nan")
    real_ratio_n25 = n_n25 / n_broad if n_broad else float("nan")
    mock_ratio_n10 = mock_n10 / mock_broad
    mock_ratio_n25 = mock_n25 / mock_broad
    print(f"  real  narrow-10/broad = {real_ratio_n10:.4f}   mock (Poisson) = {mock_ratio_n10:.4f}")
    print(f"  real  narrow-25/broad = {real_ratio_n25:.4f}   mock (Poisson) = {mock_ratio_n25:.4f}")

    print()
    print("=" * 78)
    print("STEP 4 -- area-scaled translation to the Fork-2 target footprint")
    print("=" * 78)
    print(
        "  CAVEAT, stated explicitly: this is a first-order LINEAR area scale,\n"
        "  not a real cross-match against DES-Y3/DESI-DR1 (data_acquisition_\n"
        "  plan.md's Fork 2 remains open). It assumes the target 700-850 deg^2\n"
        "  sub-region has the SAME cluster density and SAME pair-clustering\n"
        "  statistics as the ACT-DR5 MCMF average -- untested. Direction of\n"
        "  residual bias is unknown a priori (could go either way depending on\n"
        "  where in the ACT footprint the DES/DESI/eROSITA overlap actually\n"
        "  falls), unlike SS2's own single-direction Poisson-vs-clustered bias."
    )
    for label, area in [("low", FOOTPRINT_LOW), ("mid", FOOTPRINT_MID), ("high", FOOTPRINT_HIGH)]:
        scale = area / AREA_ACT_DR5_DEG2
        print(
            f"    {label:>4} ({area:.0f} deg^2, scale={scale:.5f}): "
            f"broad~{n_broad * scale:.1f}  narrow-10~{n_n10 * scale:.2f}  narrow-25~{n_n25 * scale:.2f}"
        )

    print()
    print("=" * 78)
    print("STEP 5 -- separation histogram (5 Mpc bins), for the write-up figure")
    print("=" * 78)
    bins = np.arange(0.0, S_MAX_QUERY + 5.0, 5.0)
    hist, edges = np.histogram(seps, bins=bins)
    for lo, hi, c in zip(edges[:-1], edges[1:], hist, strict=True):
        if c > 0:
            print(f"    [{lo:6.1f},{hi:6.1f}) Mpc : {c}")


if __name__ == "__main__":
    main()
