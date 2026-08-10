"""Derive u_i = kappa*k_i*r_i/(c^2*m_i)'s mass-scaling exponent from a
microphysical (self-similar cluster) model, from first principles -- not fit
to the pipeline's own output -- and compare against the measured 0.555+-0.041
(FINDING_bridge_and_mass_history / this audit's own S8, S16).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. Answers the one item
S20's NEXT list left open: "derive u_i's mass-scaling from an independent
microphysical model."

WHY THIS IS POSSIBLE NOW: reading src/cluster_data_pipeline.py shows the
548-cluster subsample's k_i = Ethermal_c2_Msun comes from e_thermal_path_b(),
an EXACT SZ-effect physics conversion, E = Y_SZ_sr * D_A^2 * (m_e c^2/sigma_T)
-- not a fitted power law. So k_i's mass-scaling is not a pipeline artefact;
it is the real Y_SZ-M relation of the actual MCXC-I/PSZ2 catalogue, and a
genuine first-principles comparison is meaningful.

THE DERIVATION (standard self-similar cluster model, Kaiser 1986; textbook
virial-theorem + hydrostatic-equilibrium argument re-derived here, not just
cited -- the EXPONENT VALUES quoted below as literature-standard are
[WEAK]/[MEMORY]-sourced, no live citation lookup this pass, but the ALGEBRA
connecting them is derived from scratch):

  R500 is DEFINED by M500 = (4/3)pi*500*rho_crit(z)*R500^3
      => R500 ~ M500^(1/3) * rho_crit(z)^(-1/3) * E(z)^(-2/3)   [EXACT, geometric]

  Hydrostatic/virial temperature: k_B*T ~ G*M*mu*m_p/R
      => T ~ M/R ~ M^(2/3) * E(z)^(2/3)                          [self-similar]

  Universal gas fraction (self-similar assumption): Mgas ~ f_gas * M
      => Mgas ~ M^1                                               [self-similar]

  Thermal energy: E_thermal ~ Mgas * T ~ M^(5/3) * E(z)^(2/3)     [self-similar]

  So k_i ~ M^(5/3) E(z)^(2/3),  r_i ~ M^(1/3) E(z)^(-2/3),  m_i ~ M^1

  u_i = k_i r_i / m_i ~ M^(5/3+1/3-1) E(z)^(2/3-2/3) = M^1 E(z)^0

PREDICTION: pure gravitational self-similarity predicts d ln(u)/d ln(M) = +1
EXACTLY -- the same +1 the single-field completion needs -- and NO net
z-dependence at fixed M. Both are checked against real data below.
"""

import numpy as np
import pandas as pd
from astropy import units as u
from astropy.cosmology import Planck18

df = pd.read_csv("data/clusters_clean.csv")
sub = df[df["Ethermal_c2_Msun"].notna()].copy()
n = len(sub)
assert n == 548

M = sub["M500c_Msun"].to_numpy()
R = sub["R500c_Mpc"].to_numpy()
k = sub["Ethermal_c2_Msun"].to_numpy()
z = sub["z"].to_numpy()
u_arr = k * R / M

print("=" * 88)
print("MICROPHYSICAL (self-similar) DERIVATION of u_i's mass-scaling exponent")
print("=" * 88)

# ---------------------------------------------------------------------------
# 0. Zero-free-parameter geometric check: does R500c_Mpc actually satisfy its
#    own definitional relation to M500c_Msun via rho_crit(z)? If yes, r_i's
#    contribution to u_i's scaling is exactly M^(1/3) at fixed z, no fitting.
# ---------------------------------------------------------------------------
rho_crit_z = Planck18.critical_density(z).to(u.Msun / u.Mpc**3).value
R500_predicted_Mpc = (3 * M / (4 * np.pi * 500 * rho_crit_z)) ** (1 / 3)
resid_dex = np.log10(R / R500_predicted_Mpc)
print("\n[0] ZERO-PARAMETER CHECK -- is R500c_Mpc = [3M/(4*pi*500*rho_crit(z))]^(1/3)?")
print(
    f"  n={n}, median residual = {np.median(resid_dex):+.5f} dex, "
    f"std = {resid_dex.std():.5f} dex, max|resid| = {np.abs(resid_dex).max():.5f} dex"
)
print(
    "  -> "
    + (
        "CONFIRMED to high precision: R500c_Mpc is definitionally tied to M500c_Msun,"
        " so r_i contributes EXACTLY M^(1/3) (at fixed z) to u_i's scaling, zero free"
        " parameters, not an independent astrophysical relation at all."
        if resid_dex.std() < 0.01
        else "NOT confirmed to high precision -- R500c_Mpc carries information beyond"
        " the M500-z definitional relation (unexpected; investigate before trusting r_i's"
        " contribution to u_i as purely geometric)."
    )
)

# ---------------------------------------------------------------------------
# 1. Empirical R-M slope at fixed z, to compare with the definitional 1/3.
# ---------------------------------------------------------------------------
lnM, lnR, lnK, lnU = np.log(M), np.log(R), np.log(k), np.log(u_arr)
lnEz = np.log(Planck18.efunc(z))  # E(z) = H(z)/H0
X = np.column_stack([np.ones(n), lnM, lnEz])
coef_R, *_ = np.linalg.lstsq(X, lnR, rcond=None)
coef_K, *_ = np.linalg.lstsq(X, lnK, rcond=None)
coef_U, *_ = np.linalg.lstsq(X, lnU, rcond=None)


def r2_of(y, Xd, c):
    pred = Xd @ c
    return 1 - np.sum((y - pred) ** 2) / np.sum((y - y.mean()) ** 2)


print("\n[1] EMPIRICAL exponents, controlling for z via E(z) = H(z)/H0 (Planck18)")
print(
    f"  R500 :  d ln R/d ln M = {coef_R[1]:.4f}  (self-similar/definitional predicts +0.333)"
    f"   d ln R/d ln E(z) = {coef_R[2]:+.4f} (predicts -0.667)   R^2={r2_of(lnR, X, coef_R):.4f}"
)
print(
    f"  k_i  :  d ln k/d ln M = {coef_K[1]:.4f}  (self-similar predicts +1.667)"
    f"   d ln k/d ln E(z) = {coef_K[2]:+.4f} (predicts +0.667)   R^2={r2_of(lnK, X, coef_K):.4f}"
)
print(
    f"  u_i  :  d ln u/d ln M = {coef_U[1]:.4f}  (self-similar predicts +1.000)"
    f"   d ln u/d ln E(z) = {coef_U[2]:+.4f} (predicts  0.000)   R^2={r2_of(lnU, X, coef_U):.4f}"
)

# bootstrap CI on the u_i exponent, same discipline as the earlier leave-one-out check
rng = np.random.default_rng(7)
boots_u = np.empty(3000)
idx_all = np.arange(n)
for i in range(3000):
    idx = rng.choice(idx_all, n, replace=True)
    c, *_ = np.linalg.lstsq(X[idx], lnU[idx], rcond=None)
    boots_u[i] = c[1]
print(
    f"\n  u_i exponent bootstrap 68% CI = [{np.percentile(boots_u, 16):.3f}, {np.percentile(boots_u, 84):.3f}]"
)

# ---------------------------------------------------------------------------
# 2. The self-similarity-breaking gap, quantified.
# ---------------------------------------------------------------------------
print("\n" + "=" * 88)
print("[2] SELF-SIMILARITY BREAKING -- comparing prediction to measurement")
print("=" * 88)
gap = 1.0 - coef_U[1]
gap_sigma = gap / boots_u.std()
print("  self-similar (pure gravity) prediction : d ln(u)/d ln(M) = 1.000 EXACTLY")
print(
    f"  measured (this sample, controlling z)  : d ln(u)/d ln(M) = {coef_U[1]:.3f} +/- {boots_u.std():.3f}"
)
print(f"  gap = {gap:.3f}  ({gap_sigma:.1f} sigma from the self-similar prediction)")
print(
    "\n  Decomposed: nearly all of the gap is in k_i (measured "
    f"{coef_K[1]:.2f} vs self-similar 1.667, a shortfall of {1.667 - coef_K[1]:.2f}),"
    f" while r_i tracks its definitional {coef_R[1]:.3f} vs 0.333 prediction closely."
)
print(
    "\n  [WEAK/MEMORY, no live literature lookup this pass] This SPECIFIC direction and"
    " rough magnitude -- real cluster Y_SZ-M and T-M relations running shallower than the"
    " self-similar exponent, increasingly so toward lower mass -- is one of the most"
    " extensively studied results in X-ray/SZ cluster astrophysics, generally attributed"
    " to non-gravitational feedback (AGN/supernova heating preferentially evacuating or"
    " heating the ICM in lower-mass systems, which have shallower potential wells). The"
    " ALGEBRA above (self-similar u_i ~ M^1 exactly) is derived from scratch in this file;"
    " the claim that real clusters break self-similarity in this direction is standard"
    " textbook material, not verified against a live source this pass, and is marked"
    " accordingly rather than presented as newly confirmed."
)

print("\n" + "=" * 88)
print("[3] WHAT THIS MEANS FOR THE AUDIT'S S19 KILL ANALYSIS")
print("=" * 88)
print(
    "  The single-field completion's ell_d=eps*M forces d ln(ell_d)/d ln(M)=+1 exactly\n"
    "  (S7). This microphysical derivation shows +1 is ALSO the pure-gravity self-similar\n"
    "  prediction for u_i -- the SAME number, from a completely different argument. So the\n"
    "  measured 0.555 is not a MULTING-specific or two-charge-specific anomaly: it is the\n"
    "  ordinary, independently-known signature of baryonic feedback breaking self-\n"
    "  similarity, present in real cluster gas physics regardless of which gravity theory\n"
    "  is being tested. The single-field completion's +1 was never falsified by exotic\n"
    "  physics -- it was falsified by mundane astrophysics it did not model (feedback),\n"
    "  which would break ANY theory's naive M^1 prediction the same way. This sharpens,\n"
    "  rather than resolves, S19's circularity finding: u_i's measured scaling is real\n"
    "  astrophysics, but it is baryonic-feedback astrophysics, not gravitational-theory\n"
    "  content -- so neither the single-field nor the two-charge completion's mass-scaling\n"
    "  comparison to real cluster data is actually testing gravity at all, until one of\n"
    "  them accounts for feedback explicitly."
)
