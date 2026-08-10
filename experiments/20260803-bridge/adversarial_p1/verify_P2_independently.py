"""Independent re-derivation of FINDING_P2_charge_identifiability.md's three
numbers, using fresh code -- not P2_charge_identifiability_chexmate.py's own
functions (resid(), the nearest-neighbour loop, np.linalg.lstsq call). Same
discipline as counterfactual_checks.py applied to two_charge_completion.py:
an independent code path is required before a result counts as re-verified,
per this audit's own S0 rule.

Also independently checks the one methodological decision the whole result
hinges on: is chexmate_real_TX.csv's M500_Msun circular with its own TX_keV
(i.e. was M derived FROM T via a self-similar-like relation, making "M*T" a
fake second charge-estimator)? P2 claims yes (slope~1.55, near self-similar
3/2) and therefore avoids M_cx entirely. Checked here from scratch.
"""

import numpy as np
import pandas as pd
from scipy import stats

CC = "data/clusters_clean.csv"
CX = "data/chexmate_real_TX.csv"
CM = "data/chexmate_combined.csv"

print("=" * 88)
print("INDEPENDENT VERIFICATION of FINDING_P2_charge_identifiability.md")
print("=" * 88)

# ---------------------------------------------------------------------------
# 0. The circularity-trap claim: is chexmate_real_TX.csv's M500_Msun derived
#    from its own TX_keV via something close to the self-similar M ~ T^1.5 law?
# ---------------------------------------------------------------------------
cx = pd.read_csv(CX)
slope_MT, intercept_MT, r_MT, p_MT, se_MT = stats.linregress(
    np.log(cx["TX_keV"]), np.log(cx["M500_Msun"])
)
print("\n[0] CIRCULARITY CHECK -- chexmate_real_TX.csv: ln(M500_Msun) vs ln(TX_keV)")
print(f"  slope = {slope_MT:.3f} +/- {se_MT:.3f}   r = {r_MT:.4f}   (self-similar predicts 1.5)")
print(
    f"  -> the SLOPE {'CONFIRMS' if abs(slope_MT - 1.5) < 3 * se_MT else 'DOES NOT CONFIRM'}"
    f" P2's claim that M500_Msun is consistent with a self-similar M-T scaling-relation origin."
    # Reworded after code review (2026-08-10): r=0.864 (not near 1) does NOT by itself argue
    # for circularity -- a near-exact formula would show r near 1, limited only by rounding.
    # r=0.864 is what a real scaling-relation MASS ESTIMATE (fit with its own intrinsic
    # scatter, a standard practice, not a raw independent measurement) would look like too.
    # The slope match to 1.5 is the load-bearing evidence for "scaling-relation-like origin";
    # r alone does not independently strengthen or weaken that reading.
    f" r={r_MT:.3f} is moderate, which is expected for a scaling-relation-based mass estimate"
    f" carrying its own intrinsic scatter -- it neither confirms nor rules out circularity by"
    f" itself; the slope match is the load-bearing evidence here, not r."
)

# ---------------------------------------------------------------------------
# 1. Step 1 -- multivariate regression ln(k) ~ ln(M) + ln(1+z), fresh sklearn-
#    free implementation via numpy normal equations (different code path from
#    P2's np.linalg.lstsq call, same underlying math but independently typed).
# ---------------------------------------------------------------------------
d = pd.read_csv(CC)
s = d[d["Ethermal_c2_Msun"].notna()].copy()
n1 = len(s)
lnM = np.log(s["M500c_Msun"].to_numpy())
lnZ1 = np.log1p(s["z"].to_numpy())
lnK = np.log(s["Ethermal_c2_Msun"].to_numpy())

X = np.column_stack([np.ones(n1), lnM, lnZ1])
XtX_inv = np.linalg.inv(X.T @ X)
coef = XtX_inv @ X.T @ lnK
pred = X @ coef
ss_res = np.sum((lnK - pred) ** 2)
ss_tot = np.sum((lnK - lnK.mean()) ** 2)
r2 = 1 - ss_res / ss_tot
resid_scatter = np.sqrt(ss_res / (n1 - 3))

print(f"\n[1] STEP 1 re-derived (normal-equations, n={n1})")
print(f"  R^2 = {r2:.4f}   alpha (d ln k/d ln M at fixed z) = {coef[1]:.4f}")
print(f"  residual scatter = {resid_scatter:.4f} nat = {resid_scatter / np.log(10):.4f} dex")
print("  P2's own numbers: R^2=0.6538, alpha=1.020, scatter=0.540 nat")
print(
    f"  -> match: R^2 diff={abs(r2 - 0.6538):.4f}, alpha diff={abs(coef[1] - 1.020):.4f}"
    f" -- {'REPRODUCED' if abs(r2 - 0.6538) < 0.01 and abs(coef[1] - 1.020) < 0.01 else 'DISCREPANCY FOUND'}"
)

# ---------------------------------------------------------------------------
# 2. Step 2 -- internal CHEX-MATE noise floor, independent recomputation.
# ---------------------------------------------------------------------------
cm = pd.read_csv(CM)
both = cm[cm["Ti_from_TX"].notna() & cm["Ti_from_sigma"].notna()].copy()
n2 = len(both)
log_ratio = np.log(both["Ti_from_TX"].to_numpy()) - np.log(both["Ti_from_sigma"].to_numpy())
sig_ratio = np.std(log_ratio, ddof=1)
sig_per_est = sig_ratio / np.sqrt(2)
print(f"\n[2] STEP 2 re-derived (n={n2})")
print(f"  sigma(ln ratio) = {sig_ratio:.4f} nat = {sig_ratio / np.log(10):.4f} dex")
print(f"  implied per-estimator noise = {sig_per_est:.4f} nat = {sig_per_est / np.log(10):.4f} dex")
print("  P2's own numbers: 0.354 nat ratio scatter, 0.109 dex per-estimator")
print(f"  -> {'REPRODUCED' if abs(sig_ratio - 0.354) < 0.01 else 'DISCREPANCY FOUND'}")

# ---------------------------------------------------------------------------
# 3. Step 3 -- positional cross-match, written from scratch (vectorised, not
#    the original's per-row idxmin loop) to catch a matching bug independently.
# ---------------------------------------------------------------------------
ra_s = s["ra_deg"].to_numpy()
dec_s = s["dec_deg"].to_numpy()
k_s = s["Ethermal_c2_Msun"].to_numpy()
M_s = s["M500c_Msun"].to_numpy()

matched = []
for _, row in cx.iterrows():
    dra = (ra_s - row["ra_deg"]) * np.cos(np.radians(row["dec_deg"]))
    dde = dec_s - row["dec_deg"]
    sep_arcmin = np.sqrt(dra**2 + dde**2) * 60.0
    j = np.argmin(sep_arcmin)
    if sep_arcmin[j] < 3.0:
        matched.append(
            {
                "sep": sep_arcmin[j],
                "z": row["z"],
                "TX_cx": row["TX_keV"],
                "k_pipe": k_s[j],
                "M_pipe": M_s[j],
            }
        )
mm = pd.DataFrame(matched)
n3 = len(mm)
print(f"\n[3] STEP 3 re-derived (independent cross-match code, <3'): n = {n3} of {len(cx)}")

lnM3 = np.log(mm["M_pipe"].to_numpy())
slope_k, intercept_k, r_k, p_k, se_k = stats.linregress(lnM3, np.log(mm["k_pipe"].to_numpy()))
slope_t, intercept_t, r_t, p_t, se_t = stats.linregress(lnM3, np.log(mm["TX_cx"].to_numpy()))
resid_k = np.log(mm["k_pipe"].to_numpy()) - (intercept_k + slope_k * lnM3)
resid_t = np.log(mm["TX_cx"].to_numpy()) - (intercept_t + slope_t * lnM3)
rho, rho_p = stats.pearsonr(resid_k, resid_t)
se_null = 1 / np.sqrt(max(n3 - 3, 1))
sig1_dex = np.std(resid_k, ddof=2) / np.log(10)
sig2_dex = np.std(resid_t, ddof=2) / np.log(10)
sig_int = np.sqrt(max(rho, 0)) * np.sqrt(np.std(resid_k, ddof=2) * np.std(resid_t, ddof=2))

print(
    f"  slope(k_pipe|M) = {slope_k:.3f}   slope(TX_cx|M) = {slope_t:.3f} (self-similar predicts 0.667)"
)
print(f"  scatter at fixed M: k_pipe {sig1_dex:.3f} dex, TX_cx {sig2_dex:.3f} dex")
print(
    f"  CORRELATION OF RESIDUALS rho = {rho:+.4f} (p={rho_p:.3f}, two-sided), null SE ~ {se_null:.3f}"
)
print(f"  implied shared scatter = {sig_int / np.log(10):.4f} dex")
print("  P2's own numbers: slope_k=1.292, slope_TX=0.480, rho=+0.361, sig_int=0.069 dex")
print(
    f"  -> rho diff = {abs(rho - 0.361):.4f}  -- "
    f"{'REPRODUCED' if abs(rho - 0.361) < 0.02 else 'DISCREPANCY FOUND'}"
)

# guards, re-derived
zc = mm["z"].to_numpy()
sepc = mm["sep"].to_numpy()
print("\n  [GUARDS, re-derived]")
print(f"  corr(resid_k, z)   = {stats.pearsonr(resid_k, zc)[0]:+.3f}")
print(f"  corr(resid_TX, z)  = {stats.pearsonr(resid_t, zc)[0]:+.3f}")
print(f"  corr(resid_k, sep) = {stats.pearsonr(resid_k, sepc)[0]:+.3f}")
print(f"  corr(resid_TX,sep) = {stats.pearsonr(resid_t, sepc)[0]:+.3f}")

# ---------------------------------------------------------------------------
# Bootstrap on rho -- P2 quoted only an analytic null SE, not an empirical CI.
# At n=25 this is exactly the regime where the two can disagree; check it.
# ---------------------------------------------------------------------------
print("\n[4] BOOTSTRAP CI on rho (not computed in the original finding -- new check)")
rng = np.random.default_rng(9)
boots = np.empty(5000)
idx_all = np.arange(n3)
for i in range(5000):
    idx = rng.choice(idx_all, n3, replace=True)
    try:
        boots[i] = stats.pearsonr(resid_k[idx], resid_t[idx])[0]
    except Exception:
        boots[i] = np.nan
boots = boots[~np.isnan(boots)]
lo, hi = np.percentile(boots, [16, 84])
lo95, hi95 = np.percentile(boots, [2.5, 97.5])
frac_negative = float(np.mean(boots <= 0))
print(f"  point estimate rho = {rho:+.3f}")
print(f"  bootstrap 68% CI = [{lo:+.3f}, {hi:+.3f}]   95% CI = [{lo95:+.3f}, {hi95:+.3f}]")
print(f"  fraction of bootstrap resamples with rho <= 0: {frac_negative:.1%}")
print(
    "  -> "
    + (
        "the 95% CI excludes 0 -- stronger than P2's own framing suggested."
        if lo95 > 0
        else f"the 95% CI includes 0 ({frac_negative:.0%} of resamples give rho<=0) -- confirms"
        " P2's own 'suggestive, not decisive' framing was the right call, if anything slightly"
        " generous."
    )
)
