"""low_z_uptick_robustness_check.py -- does the REAL low-z cosmic-chronometer
data show a robust "uptick" feature (H(z) curving back up toward z=0, read
right-to-left as TJB's 2026-08-02 email describes it), or is any apparent
feature driven by a single point?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive

SCOPE, stated up front: TJB's actual current chart (behind the 2026-08-12
Reddit-headline email) was not available to test directly -- no image was
attached to what we received. This tests the closest well-defined, data-
grounded version of the claim directly against data/hz_cc.csv (27 real,
independent Moresco+2022 cosmic-chronometer points, FLRW-independent,
NOT derived from Table A1 or any MULTING fit) -- not against TJB's own
rendered curve, which we do not have pixel data for.

METHOD:
  1. Fit the smooth LCDM baseline to all 27 points (reuses
     scripts/plot_hubble_anchoring.py's own free fit: H0, Om floated).
  2. On the low-z subsample (z<0.3, 9 points -- "low positive z" per TJB's
     own phrase), fit a local quadratic in z to the RESIDUALS from that
     smooth baseline. A genuine "uptick toward z=0" shows up as a
     significant, sign-consistent curvature term whose sign makes the
     residual curve turn upward as z->0.
  3. Leave-one-out: refit the quadratic 9 times, once per dropped point.
     If the curvature's sign or significance flips when ANY single point
     is removed, the feature is not robust.
  4. Weighted bootstrap (2000 resamples, respecting each point's own
     sigma_Hz) on the same statistic, for a confidence interval.

DECISIVE QUESTION: does the curvature survive LOO deletion of every single
point, and is its bootstrap CI bounded away from zero?
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

REPO = Path(__file__).resolve().parents[1]
CC_CSV = REPO / "data" / "hz_cc.csv"
LOW_Z_CUT = 0.3
N_BOOTSTRAP = 2000
SEED = 20260812  # fixed, stated -- not tuned after seeing the result


def lcdm(z: np.ndarray, h0: float, om: float) -> np.ndarray:
    return h0 * np.sqrt(om * (1.0 + z) ** 3 + (1.0 - om))


def quad_curvature(z: np.ndarray, resid: np.ndarray, sigma: np.ndarray) -> float:
    """Weighted quadratic fit resid ~ a + b*z + c*z^2; return c (curvature).
    c>0 means the residual curve bends UPWARD as z increases across this
    range -- equivalently, bends DOWNWARD (away from the smooth trend) as
    z decreases toward 0, i.e. NOT an uptick. c<0 bends the residual UP as
    z DECREASES toward 0 -- the "uptick read right-to-left" signature."""
    w = 1.0 / sigma**2
    design = np.vstack([np.ones_like(z), z, z**2]).T
    wdesign = design * w[:, None]
    coeffs, *_ = np.linalg.lstsq(wdesign.T @ design, wdesign.T @ resid, rcond=None)
    return float(coeffs[2])


def main() -> int:
    cc = pd.read_csv(CC_CSV, comment="#")
    z_all = cc["z"].to_numpy(float)
    h_all = cc["Hz_km_s_Mpc"].to_numpy(float)
    sig_all = cc["sigma_Hz"].to_numpy(float)

    print("=" * 78)
    print("LOW-z UPTICK ROBUSTNESS CHECK -- real Moresco+2022 chronometer data")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    popt, _ = curve_fit(lcdm, z_all, h_all, p0=[70.0, 0.3], sigma=sig_all, absolute_sigma=True)
    h0_fit, om_fit = popt
    print(f"\n[BASELINE] free LCDM fit to all 27 points: H0={h0_fit:.2f}, Om={om_fit:.3f}")

    mask_low = z_all < LOW_Z_CUT
    z_low, h_low, sig_low = z_all[mask_low], h_all[mask_low], sig_all[mask_low]
    n_low = len(z_low)
    print(f"\n[LOW-z SUBSAMPLE] {n_low} points, z in [{z_low.min():.3f}, {z_low.max():.3f}]")
    resid_low = h_low - lcdm(z_low, h0_fit, om_fit)
    for zi, hi, si, ri in zip(z_low, h_low, sig_low, resid_low, strict=True):
        print(
            f"  z={zi:.3f}  H_obs={hi:6.1f}+-{si:4.1f}  resid={ri:+6.1f}  resid/sigma={ri / si:+.2f}"
        )

    c_full = quad_curvature(z_low, resid_low, sig_low)
    print(f"\n[FULL-SAMPLE CURVATURE] c = {c_full:+.2f} km/s/Mpc per z^2")
    print("  (c<0: residuals bend UPWARD as z->0 -- the 'uptick read right-to-left' shape)")

    print("\n[LEAVE-ONE-OUT] refit curvature dropping each point once:")
    loo_signs = []
    for i in range(n_low):
        keep = np.ones(n_low, dtype=bool)
        keep[i] = False
        c_i = quad_curvature(z_low[keep], resid_low[keep], sig_low[keep])
        loo_signs.append(np.sign(c_i))
        print(
            f"  drop z={z_low[i]:.3f}: c = {c_i:+7.2f}  (sign {'same' if np.sign(c_i) == np.sign(c_full) else 'FLIPPED'})"
        )

    n_flips = sum(1 for s in loo_signs if s != np.sign(c_full))
    print(f"\n  -> sign flips under single-point deletion: {n_flips}/{n_low}")

    rng = np.random.default_rng(SEED)
    boot_c = np.empty(N_BOOTSTRAP)
    for b in range(N_BOOTSTRAP):
        h_b = h_low + rng.normal(0.0, sig_low)  # resample within each point's own uncertainty
        resid_b = h_b - lcdm(z_low, h0_fit, om_fit)
        boot_c[b] = quad_curvature(z_low, resid_b, sig_low)
    ci_lo, ci_hi = np.percentile(boot_c, [2.5, 97.5])
    frac_negative = float(np.mean(boot_c < 0))
    print(f"\n[BOOTSTRAP] {N_BOOTSTRAP} resamples (each point perturbed within its own sigma_Hz):")
    print(f"  c: mean={boot_c.mean():+.2f}, 95% CI=[{ci_lo:+.2f}, {ci_hi:+.2f}]")
    print(f"  fraction of resamples with c<0 (uptick-shaped): {frac_negative:.1%}")
    ci_excludes_zero = ci_lo > 0 or ci_hi < 0
    print(f"  95% CI excludes zero: {ci_excludes_zero}")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if n_flips == 0 and ci_excludes_zero:
        print("Curvature sign is stable under leave-one-out AND the bootstrap CI excludes")
        print("zero -- this WOULD be a robust feature, not single-point leverage.")
    else:
        print(f"Curvature sign flips under {n_flips}/{n_low} single-point deletions, and the")
        print(
            f"bootstrap 95% CI [{ci_lo:+.2f}, {ci_hi:+.2f}] {'excludes' if ci_excludes_zero else 'INCLUDES'} zero."
        )
        print("This is NOT a robust feature in the real, independent chronometer data at")
        print("this significance level -- consistent with noise around a smooth curve, not")
        print("evidence of genuine low-z curvature.")
    print()
    print("SCOPE: this tests the real data directly, not TJB's own rendered curve (not")
    print("available to us). If his 'uptick' is a feature of a FITTED model curve rather")
    print("than the raw data itself, this result bounds how much support the raw")
    print("observations alone can offer that fit -- it does not test the fit's own")
    print("machinery.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
