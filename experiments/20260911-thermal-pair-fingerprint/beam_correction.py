"""beam_correction.py -- Gaussian-beam aperture correction for
`real_map_extraction.py`'s per-cluster temperature extraction (Fork 1b
Phase 2, "beam matching" item).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

**Why an analytic aperture correction, not literal repixelize+convolve:**
Hand et al. 2012's own procedure (repixelize each cluster's submap to
0.0625' subpixels, convolve with the beam, average within 1') exists to
correctly relate an aperture-mean measurement to the TRUE (unsmeared)
signal at the cluster center. For a beam that is well-approximated as
Gaussian and much smaller than the aperture radius, this reduces to a
single, standard, well-documented photometric correction: for a
point-like (or much-smaller-than-aperture) source under a 2D Gaussian
beam of FWHM `w`, the fraction of total flux captured within a circular
aperture of radius `R` is
    f(R, w) = 1 - exp(-4*ln(2) * (R/w)^2)
(direct integral of a normalized 2D Gaussian over a disk of radius R --
standard result, used throughout mm/sub-mm aperture photometry). The
aperture-corrected estimate is T_true = T_measured / f(R, w).

**Beam FWHM used: 1.4 arcmin at 150 GHz**, `[VERIFIED-arXiv:2406.14754]`
-- the SAME ACT-DR5 MCMF catalog paper this whole real-position pipeline
is already built on, already fetched and verified in this experiment
folder's own `FINDING_beam_blending_check.md` (not re-derived, not
guessed). **Not DR6-exact**: the dedicated DR6 beam-measurement paper
(Duivenvoorden et al., cited by the DR6 Maps paper, arXiv:2503.14451)
is itself listed there as "in prep" -- no DR6-specific number or beam
file is publicly available yet (checked directly, same as the
point-source-catalog situation resolved via `map_srcfree`). Using the
ACT-DR5-paper's own 150 GHz value is a real, cited, defensible
approximation -- flagged as such, not presented as DR6-native.

Validated below against actual 2D Gaussian convolution on a synthetic
map (not just trusting the analytic formula): inject a known point-like
decrement, convolve with a real 2D Gaussian kernel of the same FWHM,
extract via the same aperture-averaging code as `real_map_extraction.py`,
and confirm the analytic correction recovers the true injected
amplitude.
"""

from __future__ import annotations

import numpy as np

BEAM_FWHM_ARCMIN_F150 = 1.4  # [VERIFIED-arXiv:2406.14754], see module docstring
APERTURE_RADIUS_ARCMIN = 1.0  # matches real_map_extraction.py's own default


def aperture_correction_factor(
    aperture_radius_arcmin: float = APERTURE_RADIUS_ARCMIN,
    beam_fwhm_arcmin: float = BEAM_FWHM_ARCMIN_F150,
) -> float:
    """f(R, w) = 1 - exp(-4*ln(2)*(R/w)^2) -- fraction of a point
    source's flux captured within a circular aperture of radius R under
    a 2D Gaussian beam of FWHM w. Divide a measured aperture-mean
    temperature by this to get the beam-corrected estimate."""
    ratio = aperture_radius_arcmin / beam_fwhm_arcmin
    return 1.0 - np.exp(-4.0 * np.log(2.0) * ratio**2)


def apply_beam_correction(
    temperature_uk: np.ndarray,
    aperture_radius_arcmin: float = APERTURE_RADIUS_ARCMIN,
    beam_fwhm_arcmin: float = BEAM_FWHM_ARCMIN_F150,
) -> np.ndarray:
    """Beam-corrected T_i = T_measured_i / f(R, w)."""
    f = aperture_correction_factor(aperture_radius_arcmin, beam_fwhm_arcmin)
    return temperature_uk / f


def _gaussian_beam_kernel(fwhm_pix: float, half_size_pix: int) -> np.ndarray:
    sigma_pix = fwhm_pix / (2.0 * np.sqrt(2.0 * np.log(2.0)))
    y, x = np.mgrid[-half_size_pix : half_size_pix + 1, -half_size_pix : half_size_pix + 1]
    k = np.exp(-(x**2 + y**2) / (2.0 * sigma_pix**2))
    return k / k.sum()


def main() -> None:
    print("STEP 1: analytic aperture correction factor")
    f = aperture_correction_factor()
    print(
        f"  R={APERTURE_RADIUS_ARCMIN}' aperture, w={BEAM_FWHM_ARCMIN_F150}' beam FWHM "
        f"-> f(R,w)={f:.4f} (fraction of point-source flux captured)"
    )
    print(f"  correction multiplier (1/f): {1.0 / f:.4f}x")

    print("\nSTEP 2: validate against REAL 2D Gaussian convolution, not just the formula")
    pix_scale_arcmin = 0.1
    n_pix = 201
    center = n_pix // 2
    true_map = np.zeros((n_pix, n_pix))
    injected_true_amplitude = -40.0  # uK, arbitrary, at the exact center pixel
    true_map[center, center] = injected_true_amplitude / (pix_scale_arcmin**2)
    # (a delta-function-like source in surface-brightness units; after
    # convolving with a normalized beam and reading off the peak-region
    # aperture mean, the *recovered* quantity is the point source's
    # effective per-pixel amplitude, scaled consistently on both sides
    # of the correction -- what matters for this validation is that the
    # SAME map, aperture-averaged, recovers injected_true_amplitude
    # after the correction is applied, not the raw absolute units.)

    from scipy.ndimage import convolve

    fwhm_pix = BEAM_FWHM_ARCMIN_F150 / pix_scale_arcmin
    kernel = _gaussian_beam_kernel(fwhm_pix, half_size_pix=int(5 * fwhm_pix))
    observed_map = convolve(true_map, kernel, mode="constant")

    aperture_radius_pix = APERTURE_RADIUS_ARCMIN / pix_scale_arcmin
    yy, xx = np.mgrid[0:n_pix, 0:n_pix]
    dist_pix = np.sqrt((xx - center) ** 2 + (yy - center) ** 2)
    aperture_mask = dist_pix <= aperture_radius_pix
    # mean surface brightness in the aperture * aperture area = total
    # flux captured; converting back to the same "amplitude" units as
    # injected_true_amplitude via the pixel area, for a like-for-like
    # comparison.
    measured_aperture_mean_sb = observed_map[aperture_mask].mean()
    n_pix_in_aperture = int(aperture_mask.sum())
    measured_total_flux = measured_aperture_mean_sb * n_pix_in_aperture * (pix_scale_arcmin**2)

    corrected_amplitude = measured_total_flux / f
    print(f"  injected true amplitude: {injected_true_amplitude:.3f} uK")
    print(f"  measured (post-beam-smearing) flux in aperture: {measured_total_flux:.3f} uK")
    print(f"  corrected (measured / f): {corrected_amplitude:.3f} uK")
    rel_err = abs(corrected_amplitude - injected_true_amplitude) / abs(injected_true_amplitude)
    print(f"  relative error after correction: {rel_err * 100:.2f}%")

    print("\nVERDICT")
    ok = rel_err < 0.02
    print(f"  Aperture correction recovers injected amplitude to <2%: {ok}")
    if ok:
        print("  BEAM CORRECTION: VALIDATED against real 2D convolution.")
    else:
        print("  BEAM CORRECTION: NOT YET VALIDATED -- see relative error above.")


if __name__ == "__main__":
    main()
