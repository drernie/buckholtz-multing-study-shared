"""real_map_extraction.py -- per-cluster temperature extraction from a
real ACT DR6 FITS temperature map (Fork 1b Phase 2). Companion to
`pairwise_ksz_estimator.py`, which implements the estimator MATH on any
per-cluster temperature array -- this file is where that array actually
comes from, once a real map exists.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

Method (Hand et al. 2012, arXiv:1203.4219, transcribed directly, same
citation `pairwise_ksz_estimator.py` already verified): *"a 10' by 10'
submap centered on the galaxy is repixellized into 0.0625' subpixels,
convolved with the ACT beam profile to smooth the map, and then
averaged over all subpixels within 1' of the galaxy."* This file
implements that procedure generically against whatever FITS WCS the map
actually declares (CAR projection expected for ACT DR6, per this
project's own prior note on the DR6 Compton-y map -- but the code below
reads the WCS from the file's own header via `astropy.wcs.WCS` rather
than hard-coding CAR, so it is not silently wrong if the real map turns
out to use a different valid FITS WCS).

**Validated here on a small SYNTHETIC local FITS file with a known
injected signal** -- no real ACT map has been read by this validation
pass. Real-map application (once `data_cache/act_dr4dr6_coadd_AA_night_
f150_map.fits` finishes downloading) is a separate, explicit next step,
not run automatically by this file's own `__main__`.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from astropy import units as u
from astropy.io import fits
from astropy.wcs import WCS

RNG_SEED = 20260911


@dataclass
class ExtractionResult:
    ra_deg: np.ndarray
    dec_deg: np.ndarray
    temperature_uk: np.ndarray
    n_pixels_used: np.ndarray
    off_map: np.ndarray  # True where the aperture fell (partly) outside the map


def extract_cluster_temperatures(
    fits_path: str,
    ra_deg: np.ndarray,
    dec_deg: np.ndarray,
    *,
    hdu_index: int = 0,
    aperture_radius_arcmin: float = 1.0,
) -> ExtractionResult:
    """Hand et al. 2012's own extraction procedure: mean map value
    within `aperture_radius_arcmin` of each cluster position. Reads
    real pixel values in a small box around each cluster (not the
    paper's own explicit repixelize-to-0.0625'-then-convolve-with-beam
    step -- that beam-matching refinement is a named, not-yet-built
    follow-up, see module docstring's own "not run automatically"
    note) -- this is the simple, honest first version: real pixels,
    real aperture, no beam convolution yet.

    Uses `memmap=True` so a multi-GB map is never loaded fully into
    memory -- only the small per-cluster boxes touched below are
    actually read off disk.
    """
    n = len(ra_deg)
    assert len(dec_deg) == n
    temperature = np.full(n, np.nan)
    n_pixels = np.zeros(n, dtype=int)
    off_map = np.zeros(n, dtype=bool)

    with fits.open(fits_path, memmap=True) as hdul:
        hdu = hdul[hdu_index]
        wcs = WCS(hdu.header).celestial
        data = hdu.data
        if data.ndim > 2:
            # ACT coadd maps carry Stokes I,Q,U as the leading axis --
            # intensity (kSZ/tSZ-relevant channel) is index 0.
            data = data[0]
        ny, nx = data.shape[-2:]

        # pixel scale (arcmin/pixel) from the WCS itself, not assumed
        pix_scale_deg = np.abs(wcs.proj_plane_pixel_scales()[0].to(u.deg).value)
        aperture_radius_deg = aperture_radius_arcmin / 60.0
        box_half_pix = int(np.ceil(aperture_radius_deg / pix_scale_deg)) + 1

        x_pix, y_pix = wcs.all_world2pix(ra_deg, dec_deg, 0)

        for i in range(n):
            xi, yi = x_pix[i], y_pix[i]
            if not (np.isfinite(xi) and np.isfinite(yi)):
                off_map[i] = True
                continue
            x0, x1 = int(round(xi)) - box_half_pix, int(round(xi)) + box_half_pix + 1
            y0, y1 = int(round(yi)) - box_half_pix, int(round(yi)) + box_half_pix + 1
            if x0 < 0 or y0 < 0 or x1 > nx or y1 > ny:
                off_map[i] = True
                continue
            box = data[y0:y1, x0:x1]
            yy, xx = np.mgrid[y0:y1, x0:x1]
            # real angular distance of every pixel center to the cluster,
            # via the WCS (correct near the poles / at any projection --
            # a flat pixel-distance approximation would not be)
            box_ra, box_dec = wcs.all_pix2world(xx, yy, 0)
            dra = (box_ra - ra_deg[i]) * np.cos(np.radians(dec_deg[i]))
            ddec = box_dec - dec_deg[i]
            ang_dist_deg = np.sqrt(dra**2 + ddec**2)
            sel = ang_dist_deg <= aperture_radius_deg
            sel &= np.isfinite(box)
            if np.sum(sel) == 0:
                off_map[i] = True
                continue
            temperature[i] = np.mean(box[sel])
            n_pixels[i] = int(np.sum(sel))

    return ExtractionResult(
        ra_deg=np.asarray(ra_deg),
        dec_deg=np.asarray(dec_deg),
        temperature_uk=temperature,
        n_pixels_used=n_pixels,
        off_map=off_map,
    )


def _make_synthetic_car_map(
    path: str,
    *,
    n_pix: int = 400,
    pix_scale_arcmin: float = 0.5,
    center_ra_deg: float = 150.0,
    center_dec_deg: float = 0.0,
) -> WCS:
    """A small, local, SYNTHETIC CAR-projection FITS file -- no real ACT
    data. Just large enough to hold a handful of test apertures."""
    wcs = WCS(naxis=2)
    wcs.wcs.ctype = ["RA---CAR", "DEC--CAR"]
    wcs.wcs.crpix = [n_pix / 2, n_pix / 2]
    wcs.wcs.crval = [center_ra_deg, center_dec_deg]
    wcs.wcs.cdelt = [-pix_scale_arcmin / 60.0, pix_scale_arcmin / 60.0]
    data = np.zeros((n_pix, n_pix), dtype=np.float32)
    hdu = fits.PrimaryHDU(data=data, header=wcs.to_header())
    hdu.writeto(path, overwrite=True)
    return wcs


def main() -> None:
    import tempfile
    from pathlib import Path

    rng = np.random.default_rng(RNG_SEED)
    tmpdir = Path(tempfile.mkdtemp(prefix="ksz_extraction_test_"))
    synthetic_path = str(tmpdir / "synthetic_car_map.fits")

    print("STEP 1: build a small synthetic CAR-projection FITS map (no real ACT data)")
    wcs = _make_synthetic_car_map(synthetic_path)

    # Inject a KNOWN, constant-amplitude decrement at 3 known positions,
    # and add background noise everywhere -- positive/negative control
    # for the EXTRACTION code, independent of pairwise_ksz_estimator.py's
    # own already-validated estimator math.
    n_test = 3
    known_ra = np.array([150.0, 150.05, 149.9])
    known_dec = np.array([0.0, 0.02, -0.03])
    injected_temperature_uk = np.array([-10.0, -25.0, 5.0])  # arbitrary, distinct

    with fits.open(synthetic_path, mode="update") as hdul:
        data = hdul[0].data
        noise_sigma = 3.0
        data[:] = rng.normal(0.0, noise_sigma, data.shape).astype(np.float32)
        for ra, dec, t in zip(known_ra, known_dec, injected_temperature_uk, strict=True):
            x0, y0 = wcs.all_world2pix([ra], [dec], 0)
            xi, yi = int(round(x0[0])), int(round(y0[0]))
            # fill a small disk (radius ~1.2') around the injection point
            # with the exact known temperature, matching the aperture
            # this file's own extractor will later average over.
            for dy in range(-6, 7):
                for dx in range(-6, 7):
                    if dx * dx + dy * dy <= 25:  # ~1' radius at 0.5'/pix
                        data[yi + dy, xi + dx] = t
        hdul.flush()

    print(f"  injected {n_test} known apertures: {injected_temperature_uk.tolist()} uK")

    print("\nSTEP 2: extract with extract_cluster_temperatures() -- POSITIVE CONTROL")
    res = extract_cluster_temperatures(synthetic_path, known_ra, known_dec)
    max_abs_err = 0.0
    for i in range(n_test):
        err = abs(res.temperature_uk[i] - injected_temperature_uk[i])
        max_abs_err = max(max_abs_err, err)
        print(
            f"  cluster {i}: injected={injected_temperature_uk[i]:+.2f} uK, "
            f"extracted={res.temperature_uk[i]:+.2f} uK, "
            f"n_pixels={res.n_pixels_used[i]}, off_map={res.off_map[i]}"
        )
    print(f"  max |extracted - injected|: {max_abs_err:.3f} uK (must be small, noise-limited)")

    print("\nSTEP 3: NEGATIVE CONTROL -- position far outside any injection, pure noise")
    far_ra = np.array([150.5])
    far_dec = np.array([0.5])
    res_far = extract_cluster_temperatures(synthetic_path, far_ra, far_dec)
    print(
        f"  extracted={res_far.temperature_uk[0]:+.3f} uK "
        f"(expect ~0 +/- noise/sqrt(n_pixels), n_pixels={res_far.n_pixels_used[0]})"
    )

    print("\nSTEP 4: off-map handling -- position outside the small synthetic map entirely")
    off_ra = np.array([200.0])
    off_dec = np.array([60.0])
    res_off = extract_cluster_temperatures(synthetic_path, off_ra, off_dec)
    print(f"  off_map flag: {res_off.off_map[0]} (must be True)")

    print("\nVERDICT")
    extraction_ok = max_abs_err < 2.0  # a few uK tolerance, noise-limited aperture mean
    negative_ok = abs(res_far.temperature_uk[0]) < 4 * 3.0 / np.sqrt(
        max(res_far.n_pixels_used[0], 1)
    )
    off_map_ok = bool(res_off.off_map[0])
    print(f"  Positive control (known injection recovered): {extraction_ok}")
    print(f"  Negative control (empty aperture ~0): {negative_ok}")
    print(f"  Off-map detection: {off_map_ok}")
    if extraction_ok and negative_ok and off_map_ok:
        print("  EXTRACTION CODE: VALIDATED on synthetic data.")
    else:
        print("  EXTRACTION CODE: NOT YET VALIDATED -- see failing check(s) above.")


if __name__ == "__main__":
    main()
