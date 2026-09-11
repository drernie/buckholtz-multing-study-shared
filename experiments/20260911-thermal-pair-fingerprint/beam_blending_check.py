"""beam_blending_check.py -- resolves estimand.md's own Consistency (d)
threat (small-s CMB-beam blending/deblending) for the real pairs driving
FINDING_power_analysis_s_dependent.md's Positivity result.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

The threat, precisely: xi_pred(z,s) uses each pair's REAL 3D comoving
separation s -- but s does not by itself say whether two clusters are
close together ON THE SKY (angular separation, what a CMB map / kSZ
pipeline actually resolves) or close together ALONG the line of sight
(small radial separation, large angular separation, no blending risk
at all). A pair can have small s from either geometry, and only the
angular half matters for instrumental blending. This was NOT checked
when FINDING_power_analysis_s_dependent.md reported its Positivity
result -- this script checks it directly, on the real positions of the
pairs that drove that result.

Beam size: ACT-DR5's own stated values, from the SAME catalog paper
this project's entire real-position pipeline is built on (Klein, Mohr
& Davies 2024, arXiv:2406.14754): "the 98 and 150 GHz channels ... have
approximate beam sizes of 2.2 and 1.4 arcmin FWHM" -- [VERIFIED-arXiv],
fetched directly from the paper's own text this session, not recalled
from memory. 2.2 arcmin (98 GHz) used as the conservative (larger,
worse-resolution) bound.
"""

from __future__ import annotations

import numpy as np
from exact_pair_census import Z_HIGH, Z_LOW, load_catalog

BEAM_FWHM_ARCMIN_98GHZ = 2.2  # [VERIFIED-arXiv:2406.14754], conservative bound
BEAM_FWHM_ARCMIN_150GHZ = 1.4  # [VERIFIED-arXiv:2406.14754], optimistic bound

S_CHECK_MAX_MPC = 20.0  # covers S_MIN_VALID=10 from power_analysis_s_dependent.py
# plus enough margin above it to see how the picture evolves with s

# The 5 pairs FINDING_power_analysis_s_dependent.md Sec2 actually named,
# identified by (z, s) to the precision printed there -- re-matched below
# against the real catalog to recover their real RA/Dec (not re-typed).
NAMED_PAIRS_Z_S = [
    (0.574, 10.49),
    (0.277, 11.19),
    (0.436, 11.04),
    (0.542, 11.33),
    (0.477, 11.56),
]


def angular_sep_arcmin(ra1_deg, dec1_deg, ra2_deg, dec2_deg):
    """Real great-circle angular separation, spherical law of cosines."""
    ra1, dec1, ra2, dec2 = map(np.radians, (ra1_deg, dec1_deg, ra2_deg, dec2_deg))
    cos_theta = np.sin(dec1) * np.sin(dec2) + np.cos(dec1) * np.cos(dec2) * np.cos(ra1 - ra2)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    theta_deg = np.degrees(np.arccos(cos_theta))
    return theta_deg * 60.0


def main() -> None:
    print("=" * 78)
    print("STEP 1 -- load the real catalog, rebuild close (RA,Dec) pairs directly")
    print("=" * 78)
    ra, dec, z = load_catalog()
    mask = (z >= Z_LOW) & (z <= Z_HIGH)
    ra_u, dec_u, z_u = ra[mask], dec[mask], z[mask]
    n = len(z_u)
    print(f"  N clusters (z cut): {n}")

    # Full real 3D comoving separation, computed the SAME way as
    # exact_pair_census.py (astropy Planck18 comoving_distance -> Cartesian),
    # kept local and explicit here so this script can carry RA/Dec alongside
    # s for every pair without re-importing internal state.
    import astropy.units as u
    from astropy.cosmology import Planck18 as cosmo

    d_c = cosmo.comoving_distance(z_u).to(u.Mpc).value
    ra_rad, dec_rad = np.radians(ra_u), np.radians(dec_u)
    x = d_c * np.cos(dec_rad) * np.cos(ra_rad)
    y = d_c * np.cos(dec_rad) * np.sin(ra_rad)
    zc = d_c * np.sin(dec_rad)
    xyz = np.column_stack([x, y, zc])

    from scipy.spatial import cKDTree

    tree = cKDTree(xyz)
    sdm = tree.sparse_distance_matrix(tree, max_distance=S_CHECK_MAX_MPC, output_type="coo_matrix")
    upper = sdm.row < sdm.col
    row, col, seps = sdm.row[upper], sdm.col[upper], np.asarray(sdm.data[upper])
    print(f"  Real pairs with s <= {S_CHECK_MAX_MPC:.0f} Mpc comoving: {len(seps)}")

    z_pair = 0.5 * (z_u[row] + z_u[col])
    ang_sep = angular_sep_arcmin(ra_u[row], dec_u[row], ra_u[col], dec_u[col])

    print()
    print("=" * 78)
    print(
        "STEP 2 -- the 5 NAMED pairs driving the Positivity result: real "
        "angular separation vs. ACT's own beam FWHM"
    )
    print("=" * 78)
    print(
        f"{'z':>7} {'s (Mpc)':>9} {'ang.sep (arcmin)':>17} "
        f"{'/2.2arcmin':>11} {'/1.4arcmin':>11}  verdict"
    )
    for z_target, s_target in NAMED_PAIRS_Z_S:
        # match by closest (z_pair, s) to the printed precision
        d = np.abs(z_pair - z_target) + 0.01 * np.abs(seps - s_target)
        i = np.argmin(d)
        ratio_98 = ang_sep[i] / BEAM_FWHM_ARCMIN_98GHZ
        ratio_150 = ang_sep[i] / BEAM_FWHM_ARCMIN_150GHZ
        verdict = (
            "BLENDING RISK (<2x beam)"
            if ratio_98 < 2.0
            else "marginal (2-5x beam)"
            if ratio_98 < 5.0
            else "resolved (>5x beam)"
        )
        print(
            f"{z_pair[i]:>7.3f} {seps[i]:>9.2f} {ang_sep[i]:>17.3f} "
            f"{ratio_98:>11.2f} {ratio_150:>11.2f}  {verdict}"
        )

    print()
    print("=" * 78)
    print(
        "STEP 3 -- full picture: ALL real pairs with s <= 20 Mpc, angular separation distribution"
    )
    print("=" * 78)
    for s_hi in (11.0, 12.0, 15.0, 20.0):
        m = seps <= s_hi
        if m.sum() == 0:
            continue
        frac_below_2x = np.mean(ang_sep[m] < 2.0 * BEAM_FWHM_ARCMIN_98GHZ)
        frac_below_1x = np.mean(ang_sep[m] < BEAM_FWHM_ARCMIN_98GHZ)
        print(
            f"  s<={s_hi:>5.1f} Mpc: N={m.sum():>4d}  "
            f"median ang.sep={np.median(ang_sep[m]):>7.3f} arcmin  "
            f"min={ang_sep[m].min():>7.3f} arcmin  "
            f"frac < 1x beam (2.2'): {frac_below_1x * 100:>5.1f}%  "
            f"frac < 2x beam: {frac_below_2x * 100:>5.1f}%"
        )

    print()
    print("=" * 78)
    print("STEP 4 -- reading: is s (3D comoving) mostly radial or angular for the close pairs?")
    print("=" * 78)
    # What angular separation WOULD s=10 Mpc correspond to, if it were
    # PURELY transverse (no radial component), at each pair's own z --
    # a reference scale, using astropy's real angular-diameter distance.
    from astropy.cosmology import Planck18 as cosmo2

    d_a = cosmo2.angular_diameter_distance(z_pair).to(u.Mpc).value
    # angle (rad) = transverse_physical_size / d_A; s here is COMOVING, so
    # the purely-transverse comoving size maps to a physical transverse
    # size of s/(1+z) at that z for the angular-diameter-distance relation
    purely_transverse_arcmin = np.degrees((seps / (1.0 + z_pair)) / d_a) * 60.0
    frac_of_max = ang_sep / purely_transverse_arcmin
    print(
        "  If a pair's real separation were ENTIRELY transverse (no radial\n"
        "  component), its angular separation would equal the value in the\n"
        "  'purely_transverse' column. The real/purely-transverse RATIO says\n"
        "  how much of the real 3D separation is actually on-sky vs. along\n"
        "  the line of sight -- ratio near 1 = almost entirely transverse\n"
        "  (real blending risk); ratio near 0 = mostly radial (little risk\n"
        "  despite small 3D s)."
    )
    for z_target, s_target in NAMED_PAIRS_Z_S:
        d = np.abs(z_pair - z_target) + 0.01 * np.abs(seps - s_target)
        i = np.argmin(d)
        print(
            f"  z={z_pair[i]:.3f} s={seps[i]:.2f} Mpc: real ang.sep="
            f"{ang_sep[i]:.3f}' vs purely-transverse-equivalent "
            f"{purely_transverse_arcmin[i]:.3f}'  (ratio={frac_of_max[i]:.3f})"
        )


if __name__ == "__main__":
    main()
