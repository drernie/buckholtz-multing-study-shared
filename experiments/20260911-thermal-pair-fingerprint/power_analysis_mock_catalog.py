"""power_analysis_mock_catalog.py -- mock-catalog power analysis for the
thermal-pair fingerprint C1 kill-test (estimand.md's own MCID section).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

Runs entirely on synthetic data. No real catalog is touched (per
estimand.md's own Pre-Data Requirement -- this IS the pre-data step,
not a substitute for it; the synthetic four-world identifiability
battery estimand.md mandates is a SEPARATE, not-yet-built artifact this
script does not attempt).

Pipeline:
  1. Real N_clusters from a VERIFIED cluster number density (ACT-DR5 MCMF,
     arXiv:2406.14754: 6237 clusters) applied to the Fork-2 footprint
     estimate (700-850 sq deg, data_acquisition_plan.md).
  2. A real comoving-volume calculation (astropy.cosmology) converts that
     into an expected pair count within a stated separation window --
     NOT assumed, computed, and explicitly flagged as a *lower bound*
     (real clusters are positively biased tracers of large-scale
     structure; this uses an unclustered/Poisson pair-counting integral,
     which undercounts close pairs).
  3. Mock xi per cluster: mean M-z trajectory (from the closed
     2026-09-07 branch's own Q(z) table) times a log-normal scatter
     factor, sigma=0.49 (FINDING_E13) -- explicitly the SAME
     marginal-vs-joint substitution claim.md 3a already flagged as
     HYPOTHESIS, not fact. Carried forward honestly, not silently
     upgraded to a joint measurement.
  4. Three noise scenarios bracket the per-pair velocity/force-residual
     measurement uncertainty (this project does not have the source
     kSZ paper's own per-pair noise budget -- data_acquisition_plan.md's
     Fork 1 finding that the per-object table is not public means this
     cannot be looked up, only bracketed).
  5. Monte Carlo: for each (N_pairs, noise scenario), simulate many mock
     realizations under H_M (MULTING true) and H_0 (null), fit null vs.
     C1's frozen S_M model, and report the fraction of realizations that
     would PROMOTE / correctly REJECT, per estimand.md's own MCID
     candidate-region language.
"""

from __future__ import annotations

import numpy as np
from astropy.cosmology import Planck18 as cosmo
import astropy.units as u

rng = np.random.default_rng(20260911)

# ---- Step 1: real cluster density -> N_clusters in the Fork-2 footprint ----
N_ACT_MCMF = 6237  # [VERIFIED-arXiv:2406.14754], ACT-DR5 MCMF catalog
AREA_ACT_DEG2 = 13750.0  # [VERIFIED-REAL], LAMBDA DR6 page: "~1/3 of the sky"
density_per_deg2 = N_ACT_MCMF / AREA_ACT_DEG2

FOOTPRINT_LOW, FOOTPRINT_MID, FOOTPRINT_HIGH = 700.0, 775.0, 850.0  # Fork 2
N_clusters_mid = density_per_deg2 * FOOTPRINT_MID
N_clusters_low = density_per_deg2 * FOOTPRINT_LOW
N_clusters_high = density_per_deg2 * FOOTPRINT_HIGH

print("=" * 78)
print("STEP 1 -- cluster count from a real, verified density")
print("=" * 78)
print(
    f"  ACT-DR5 MCMF density: {density_per_deg2:.4f} clusters/deg^2 "
    f"({N_ACT_MCMF} / {AREA_ACT_DEG2:.0f} deg^2)"
)
print(
    f"  N_clusters in Fork-2 footprint: "
    f"{N_clusters_low:.0f} (700 deg^2) - {N_clusters_high:.0f} (850 deg^2), "
    f"mid={N_clusters_mid:.0f}"
)

# ---- Step 2: real comoving-volume pair count (lower bound, unclustered) ----
Z_LOW, Z_HIGH = 0.2, 0.8  # working range: lensing+tSZ+X-ray jointly detectable
S_MIN_MPC, S_MAX_MPC = 20.0, 160.0  # comoving separation window, matches the
# literature convention for kSZ pairwise-velocity bins (e.g. the classic
# Hand et al. 2012 / DESI-ACT pairwise-kSZ bin ranges)


def comoving_area_deg2_to_mpc2(area_deg2: float, z: float) -> float:
    d_c = cosmo.comoving_distance(z).to(u.Mpc).value
    area_sr = area_deg2 * (np.pi / 180.0) ** 2
    return area_sr * d_c**2


def pair_count_lower_bound(n_clusters: float, area_deg2: float) -> float:
    """Unclustered (Poisson) pair-counting integral, a LOWER bound: real
    clusters are positively biased tracers of large-scale structure, so
    the true close-pair count exceeds this."""
    v_low = cosmo.comoving_volume(Z_LOW).to(u.Mpc**3).value * (area_deg2 / 41253.0)
    v_high = cosmo.comoving_volume(Z_HIGH).to(u.Mpc**3).value * (area_deg2 / 41253.0)
    v_shell = v_high - v_low
    n_density = n_clusters / v_shell  # Mpc^-3
    # expected pairs per object within [s_min, s_max]: n_density * 4*pi*s^2 ds,
    # integrated; total pairs = N * (that) / 2
    shell_vol = (4.0 / 3.0) * np.pi * (S_MAX_MPC**3 - S_MIN_MPC**3)
    pairs_per_object = n_density * shell_vol
    return 0.5 * n_clusters * pairs_per_object, v_shell, n_density


N_pairs_mid, V_shell, n_dens = pair_count_lower_bound(N_clusters_mid, FOOTPRINT_MID)
N_pairs_low, _, _ = pair_count_lower_bound(N_clusters_low, FOOTPRINT_LOW)
N_pairs_high, _, _ = pair_count_lower_bound(N_clusters_high, FOOTPRINT_HIGH)

print("\n" + "=" * 78)
print("STEP 2 -- pair count from a real comoving-volume calculation (LOWER BOUND -- unclustered)")
print("=" * 78)
print(
    f"  z range {Z_LOW}-{Z_HIGH}, separation window {S_MIN_MPC:.0f}-{S_MAX_MPC:.0f} Mpc (comoving)"
)
print(f"  comoving shell volume (mid footprint): {V_shell:.3e} Mpc^3")
print(f"  number density: {n_dens:.3e} Mpc^-3")
print(
    f"  N_pairs (lower bound, Poisson): "
    f"{N_pairs_low:.1f} (700 deg^2) - {N_pairs_high:.1f} (850 deg^2), "
    f"mid={N_pairs_mid:.1f}"
)
print(
    "  NOTE: real clusters are positively biased tracers (2-point "
    "correlation excess) -- this UNDERCOUNTS true close pairs, likely "
    "by a factor of several. Treat as a floor, not the real number."
)

# ---- Step 3: mock xi per cluster, mean trajectory + E13-motivated scatter --
BETA1 = 1.433479e10
BETA2 = 7.806760e17
XI_CROSSING = 3.668913e-08  # verified in claim.md #4

# model's own mean trajectory value at the closest approach (z=1.443, from
# the closed 2026-09-07 branch's own Q(z) table)
XI_MEAN_TRAJECTORY = 3.210416e-08  # claim.md's own translated Q_min=1.7484

SIGMA_LN = 0.49  # FINDING_E13, M_gas-T scatter -- USED HERE AS A PROXY FOR
# xi's OWN scatter, exactly the substitution claim.md #3a flags as
# HYPOTHESIS, not measured. Carried forward explicitly, not silently.


def s_m_identical(xi: np.ndarray) -> np.ndarray:
    """claim.md's frozen two-node reduction, F/(GM^2/s^2)."""
    return -1.0 + 2.0 * BETA1 * xi - BETA2 * xi**2


def mock_xi_sample(n: int, mean_xi: float, sigma_ln: float) -> np.ndarray:
    # log-normal scatter around the mean trajectory value
    mu_ln = np.log(mean_xi) - 0.5 * sigma_ln**2  # so that E[xi]=mean_xi
    return rng.lognormal(mean=mu_ln, sigma=sigma_ln, size=n)


xi_test = mock_xi_sample(200_000, XI_MEAN_TRAJECTORY, SIGMA_LN)
frac_above_crossing = np.mean(xi_test > XI_CROSSING)
print("\n" + "=" * 78)
print("STEP 3 -- mock xi population, mean trajectory x E13-motivated log-normal scatter")
print("=" * 78)
print(f"  mean xi (trajectory): {XI_MEAN_TRAJECTORY:.4e}")
print(f"  crossing xi: {XI_CROSSING:.4e}")
print(
    f"  sigma_ln = {SIGMA_LN} (E13's M_gas-T scatter, used as a PROXY -- "
    f"claim.md #3a's own flagged HYPOTHESIS, not a measured xi-scatter)"
)
print(
    f"  fraction of mock pairs with xi > crossing (net-repulsive regime): "
    f"{frac_above_crossing * 100:.2f}%"
)

print("=" * 78)

# ---- Step 3b: separation-window sensitivity, named explicitly ----
# The 20-160 Mpc window (Step 2) is the general kSZ-pairwise-statistic
# literature convention. It is NOT the same as v82's own characteristic
# node separation, which pearl_registry's 2026-09-09 entry found is only
# weakly sourced (v82's own text names s0~30 Mpc, and explicitly REJECTS
# using it; "40-45 Mpc" -- used elsewhere in this project -- has NO
# textual source at all). A narrower window matching that number is
# computed too, for comparison, not as a replacement.
S_MIN_NARROW, S_MAX_NARROW = 20.0, 45.0


def pair_count_narrow(n_clusters: float, area_deg2: float) -> float:
    v_low = cosmo.comoving_volume(Z_LOW).to(u.Mpc**3).value * (area_deg2 / 41253.0)
    v_high = cosmo.comoving_volume(Z_HIGH).to(u.Mpc**3).value * (area_deg2 / 41253.0)
    n_density = n_clusters / (v_high - v_low)
    shell_vol = (4.0 / 3.0) * np.pi * (S_MAX_NARROW**3 - S_MIN_NARROW**3)
    return 0.5 * n_clusters * n_density * shell_vol


N_pairs_narrow_mid = pair_count_narrow(N_clusters_mid, FOOTPRINT_MID)
print("\nSTEP 3b -- separation-window sensitivity")
print(f"  20-160 Mpc (kSZ literature convention): N_pairs~{N_pairs_mid:.0f}")
print(
    f"  20-45 Mpc (v82's own s0~30 Mpc region, per pearl_registry "
    f"2026-09-09): N_pairs~{N_pairs_narrow_mid:.1f}"
)
print(
    "  These differ by >30x. Neither is authoritative until 'the pair' "
    "is pinned down (estimand.md's own Population section already "
    "defers to the source kSZ paper's convention -- that decision now "
    "has a real, quantified cost attached to it.)"
)
print("=" * 78)

# ---- Step 4-5: Monte Carlo power analysis, relative-noise-level framing --
# Matches this project's own established convention (FINDING_P191-P194):
# noise expressed as a fraction of the predicted SIGNAL's own population
# RMS, not an invented absolute km/s budget this project cannot verify
# (data_acquisition_plan.md's Fork 1: the source paper's per-object noise
# budget is not public).

N_MC = 4000  # Monte Carlo realizations per (N_pairs, noise level) cell
ALPHA = 0.05  # nominal two-sided significance for the amplitude test
DELTA_AIC_PROMOTE = 6.0  # "strong" per Kass-Raftery/this project's own
# P166 convention -- a stricter bar than the bare alpha=0.05 test alone


def s_m_pair(xi_a: np.ndarray, xi_b: np.ndarray) -> np.ndarray:
    """claim.md #7a's own general two-node S_M, not just the identical
    reduction."""
    return BETA1 * (xi_a + xi_b) - BETA2 * xi_a * xi_b


def one_trial(n_pairs: int, rel_noise: float, h_m_true: bool) -> tuple[float, float]:
    xi_a = mock_xi_sample(n_pairs, XI_MEAN_TRAJECTORY, SIGMA_LN)
    xi_b = mock_xi_sample(n_pairs, XI_MEAN_TRAJECTORY, SIGMA_LN)
    signal = s_m_pair(xi_a, xi_b)
    signal_rms = np.std(signal)
    noise_sigma = rel_noise * signal_rms
    y = (signal if h_m_true else 0.0) + rng.normal(0.0, noise_sigma, n_pairs)

    # Model 0 (null): y = const.  Model M (amplitude lambda on signal):
    # y = lambda*signal + const. Both fit by OLS; report lambda, its
    # standard error (for a z-test), and delta-AIC (null - full, positive
    # favors the MULTING-shaped model).
    design = np.column_stack([np.ones(n_pairs), signal])
    coef, _, _, _ = np.linalg.lstsq(design, y, rcond=None)
    resid_full = y - design @ coef
    rss_full = float(np.sum(resid_full**2))
    lam = coef[1]
    # OLS coefficient covariance (homoscedastic)
    sigma2_hat = rss_full / max(n_pairs - 2, 1)
    xtx_inv = np.linalg.inv(design.T @ design)
    lam_se = float(np.sqrt(sigma2_hat * xtx_inv[1, 1]))
    z_lambda = lam / lam_se if lam_se > 0 else 0.0

    rss_null = float(np.sum((y - np.mean(y)) ** 2))
    # AIC = n*ln(RSS/n) + 2k
    aic_null = n_pairs * np.log(rss_null / n_pairs + 1e-300) + 2 * 1
    aic_full = n_pairs * np.log(rss_full / n_pairs + 1e-300) + 2 * 2
    delta_aic = aic_null - aic_full  # positive favors the MULTING-shaped fit
    return z_lambda, delta_aic


print("\n" + "=" * 78)
print("STEP 4-5 -- Monte Carlo power analysis (N_MC=%d per cell)" % N_MC)
print("=" * 78)
print(f"{'N_pairs':>8} {'rel_noise':>10} {'P(promote|H_M)':>16} {'P(false_promote|H_0)':>22}")

n_pairs_scan = [50, 100, int(round(N_pairs_mid)), 500, 1000, 2000, 5000]
rel_noise_scan = [1.0, 3.0, 10.0]  # noise as a multiple of the signal's own RMS

results = []
for n_pairs in n_pairs_scan:
    for rel_noise in rel_noise_scan:
        promote_hm = 0
        promote_h0 = 0
        for _ in range(N_MC):
            z1, daic1 = one_trial(n_pairs, rel_noise, h_m_true=True)
            if abs(z1) > 1.96 and daic1 > DELTA_AIC_PROMOTE:
                promote_hm += 1
            z0, daic0 = one_trial(n_pairs, rel_noise, h_m_true=False)
            if abs(z0) > 1.96 and daic0 > DELTA_AIC_PROMOTE:
                promote_h0 += 1
        p_power = promote_hm / N_MC
        p_false = promote_h0 / N_MC
        results.append((n_pairs, rel_noise, p_power, p_false))
        print(f"{n_pairs:>8} {rel_noise:>10.1f} {p_power:>16.3f} {p_false:>22.3f}")

print("=" * 78)
print("VERDICT")
print("=" * 78)
for n_pairs in n_pairs_scan:
    row = [r for r in results if r[0] == n_pairs and r[1] == 3.0][0]
    print(
        f"  N_pairs={n_pairs:>5}, rel_noise=3x signal RMS: "
        f"power={row[2] * 100:.1f}%, false-promote rate={row[3] * 100:.1f}%"
    )
print(
    f"\n  At the Fork-2-derived N_pairs~{N_pairs_mid:.0f} (lower bound, "
    f"20-160 Mpc window), power at 3x noise is the load-bearing number "
    f"above -- read it, do not round it up before reporting."
)

# ---- Supplementary check: power at the NARROW-window pair count ----
print("\n" + "=" * 78)
print("SUPPLEMENTARY -- power at the v82-own-scale (20-45 Mpc) pair count")
print("=" * 78)
n_narrow = max(int(round(N_pairs_narrow_mid)), 2)
for rel_noise in rel_noise_scan:
    promote_hm = sum(
        1
        for _ in range(N_MC)
        if (lambda z, d: abs(z) > 1.96 and d > DELTA_AIC_PROMOTE)(*one_trial(n_narrow, rel_noise, True))
    )
    promote_h0 = sum(
        1
        for _ in range(N_MC)
        if (lambda z, d: abs(z) > 1.96 and d > DELTA_AIC_PROMOTE)(*one_trial(n_narrow, rel_noise, False))
    )
    print(f"  N_pairs={n_narrow} (narrow window), rel_noise={rel_noise:.1f}x: "
          f"power={promote_hm / N_MC * 100:.1f}%, false-promote={promote_h0 / N_MC * 100:.1f}%")
print(f"\n  n={n_narrow} is small enough that even the IDEALIZED, "
      f"no-confounder power number above should be read with caution -- "
      f"asymptotic z/AIC approximations are less reliable at this N.")

# ---- STEP 3c [AMENDED 2026-09-11, external critique verified before
# applying]: the narrow window used 20-45 Mpc PHYSICAL, sourced from
# pearl_registry's "s0~30 Mpc" note. That note is about a DIFFERENT
# number: v82's own text (data/source_material/buckholtz_202608.0943v1.
# v82.md:58-59, :318) defines the physical separation s(t)=a(t)x with
# s(0)=d0=45 Mpc -- the actual frozen IC, not the rejected s0~30 Mpc
# correlation-length grounding attempt. This project's OWN closed-branch
# code (FINDING_stage4, already read this session) already used exactly
# d(z)=d0/(1+z), d0=45 -- confirmed here again directly, not re-derived.
# Since x = d(z)*(1+z) = d0 is FIXED by this formula, the comoving
# separation of v82's own "spotlighted" background trajectory is a
# CONSTANT 45 Mpc at every z -- not something needing a (1+z) conversion
# applied to an already-physical window (that was the critique's own
# proposed fix, and it is closer than the original error but still
# doesn't match this project's own already-verified formula exactly).
print("\n" + "=" * 78)
print("STEP 3c -- CORRECTED characteristic separation, verified against "
      "v82's own text + this project's own FINDING_stage4 formula")
print("=" * 78)
D0_PHYSICAL_Z0 = 45.0  # [VERIFIED] v82.md lines 58-59, 318
print(f"  v82's own d(z) = d0/(1+z), d0={D0_PHYSICAL_Z0} Mpc PHYSICAL at z=0")
print(f"  => comoving x = d(z)*(1+z) = {D0_PHYSICAL_Z0} Mpc, CONSTANT at all z")
for z_check in [0.0, 0.5, 1.0]:
    print(f"     sanity check z={z_check}: d(z)={D0_PHYSICAL_Z0/(1+z_check):.2f} "
          f"Mpc physical (matches FINDING_stage4's own table)")

for label, (s_lo, s_hi) in [("narrow, +-10 Mpc", (35.0, 55.0)),
                             ("wide, +-25 Mpc", (20.0, 70.0))]:
    def pair_count_corrected(n_clusters, area_deg2, s_lo=s_lo, s_hi=s_hi):
        v_low = cosmo.comoving_volume(Z_LOW).to(u.Mpc**3).value * (area_deg2 / 41253.0)
        v_high = cosmo.comoving_volume(Z_HIGH).to(u.Mpc**3).value * (area_deg2 / 41253.0)
        n_density = n_clusters / (v_high - v_low)
        shell_vol = (4.0 / 3.0) * np.pi * (s_hi**3 - s_lo**3)
        return 0.5 * n_clusters * n_density * shell_vol

    n_pairs_corr = pair_count_corrected(N_clusters_mid, FOOTPRINT_MID)
    print(f"\n  window [{s_lo:.0f},{s_hi:.0f}] Mpc comoving ({label}, "
          f"centered on the VERIFIED 45 Mpc): N_pairs~{n_pairs_corr:.1f}")

    # power at this corrected N
    n_corr_int = max(int(round(n_pairs_corr)), 2)
    for rel_noise in [3.0]:
        promote_hm = sum(
            1 for _ in range(N_MC)
            if (lambda z, d: abs(z) > 1.96 and d > DELTA_AIC_PROMOTE)(*one_trial(n_corr_int, rel_noise, True))
        )
        print(f"    power at N={n_corr_int}, 3x noise: {promote_hm / N_MC * 100:.1f}%")
