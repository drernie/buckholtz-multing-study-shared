"""
H_FLRW Convention Recovery — Direction 1
Systematic search for the formula generating H_FLRW column in Table A1.

KNOWN FACT: Standard ΛCDM (all variants) predicts H(z=8.5) ≈ 1109 km/s/Mpc.
Table A1 reports H_FLRW(z=8.5) = 398.5 km/s/Mpc — a 2.78× discrepancy.
Previous sweep: ALL standard ΛCDM variants fail with MAE > 100. [VERIFIED]

HYPOTHESIS-ARBITER (5 candidates):
  H₁: H_FLRW = H₀ × (1+z)^α  (pure power law, no Λ)
  H₂: H_FLRW = H₀ × sqrt[Ωm(1+z)^n + (1-Ωm)]  (dark energy, varying n)
  H₃: H_FLRW = f(t_table) derived from table's own t column (H = β/t^γ)
  H₄: H_FLRW = H₀ × (1+z)^(3/2) × (Ωm)^0.5  (pure matter, Ω free)
  H₅: H_FLRW is an integer-rounded or otherwise mangled ΛCDM output

DATA: Table A1 (Claude AI, claude_approximate_matches.csv)
"""

import numpy as np
from scipy.optimize import curve_fit, minimize_scalar

# Table A1 data
TABLE = [
    # z, H_obs, sigma_H, H_FLRW_reported, t_gyr
    (0.00, 73.0, 1.0, 67.4, 13.5),
    (0.06, 69.0, 3.0, 68.1, 13.0),
    (0.14, 74.0, 4.0, 69.3, 12.0),
    (0.25, 79.0, 4.5, 71.5, 11.0),
    (0.40, 82.0, 5.0, 75.0, 10.0),
    (0.65, 92.0, 7.0, 83.0, 9.0),
    (1.00, 105.0, 8.0, 95.7, 8.0),
    (1.50, 125.0, 15.0, 114.8, 7.0),
    (2.10, 150.0, 20.0, 140.3, 6.0),
    (3.20, 195.0, 30.0, 187.6, 5.0),
    (5.00, 270.0, 50.0, 265.2, 4.0),
    (8.50, 420.0, 90.0, 398.5, 3.0),
]

z_arr = np.array([r[0] for r in TABLE])
H_rep = np.array([r[3] for r in TABLE])  # H_FLRW as reported
t_arr = np.array([r[4] for r in TABLE])  # cosmic time from table (Gyr)
H0_rep = H_rep[0]  # = 67.4

GYR_TO_KMS_MPC = 977.8  # 1 Gyr^{-1} in km/s/Mpc

DIV = "=" * 72


def mae(pred, obs):
    return float(np.mean(np.abs(pred - obs)))


def rmse(pred, obs):
    return float(np.sqrt(np.mean((pred - obs) ** 2)))


# ──────────────────────────────────────────────────────────
# H1: Pure power law  H = H0 * (1+z)^α
# ──────────────────────────────────────────────────────────
def h_powerlaw(z, alpha):
    return H0_rep * (1 + z) ** alpha


res_pl = curve_fit(h_powerlaw, z_arr[1:], H_rep[1:], p0=[0.5])
alpha_best = res_pl[0][0]
H_pl = h_powerlaw(z_arr, alpha_best)
mae_pl = mae(H_pl, H_rep)
rmse_pl = rmse(H_pl, H_rep)

# What alpha does each individual point imply?
alphas_individual = np.log(H_rep[1:] / H0_rep) / np.log(1 + z_arr[1:])

# ──────────────────────────────────────────────────────────
# H2: Dark-energy variant  H² = H0²[Ωm(1+z)^n + (1-Ωm)]
# Vary n (matter power index), fit Ωm
# ──────────────────────────────────────────────────────────
best_h2 = {"mae": 1e9}
h2_sweep = []
for n in np.arange(1.0, 4.01, 0.1):

    def chi2_h2(Om, n_power=n):
        if Om <= 0 or Om >= 1.5:
            return 1e10
        H_pred = H0_rep * np.sqrt(Om * (1 + z_arr) ** n_power + (1 - Om))
        return float(np.sum((H_pred - H_rep) ** 2))

    res = minimize_scalar(chi2_h2, bounds=(-0.5, 1.5), method="bounded")
    Om = res.x
    H_pred = H0_rep * np.sqrt(Om * (1 + z_arr) ** n + (1 - Om))
    m = mae(H_pred, H_rep)
    r = rmse(H_pred, H_rep)
    h2_sweep.append((n, Om, m, r))
    if m < best_h2["mae"]:
        best_h2 = {"n": n, "Om": Om, "mae": m, "rmse": r, "H_pred": H_pred}


# ──────────────────────────────────────────────────────────
# H3: H = β / t^γ  (power law in cosmic time from table)
# ──────────────────────────────────────────────────────────
def h_time(t, beta, gamma):
    return beta / t**gamma


try:
    res_t = curve_fit(h_time, t_arr, H_rep, p0=[200.0, 0.8])
    beta_t, gamma_t = res_t[0]
    H_t = h_time(t_arr, beta_t, gamma_t)
    mae_t = mae(H_t, H_rep)
    rmse_t = rmse(H_t, H_rep)
except Exception:
    beta_t, gamma_t, H_t, mae_t, rmse_t = 0, 0, H_rep * 0, 999, 999


# ──────────────────────────────────────────────────────────
# H4: Pure matter  H = H0 * sqrt(Ωm) * (1+z)^(3/2)
# ──────────────────────────────────────────────────────────
# Fit Ωm using all non-zero z points
def chi2_h4(Om):
    H_pred = H0_rep * np.sqrt(Om) * (1 + z_arr) ** 1.5
    return float(np.sum((H_pred - H_rep) ** 2))


res_h4 = minimize_scalar(chi2_h4, bounds=(0.001, 2.0), method="bounded")
Om_h4 = res_h4.x
H_h4 = H0_rep * np.sqrt(Om_h4) * (1 + z_arr) ** 1.5
mae_h4 = mae(H_h4, H_rep)
rmse_h4 = rmse(H_h4, H_rep)

# ──────────────────────────────────────────────────────────
# H5: ΛCDM standard (Planck) for reference
# ──────────────────────────────────────────────────────────
H_lcdm_planck = 67.4 * np.sqrt(0.315 * (1 + z_arr) ** 3 + 0.685)
mae_lcdm = mae(H_lcdm_planck, H_rep)
rmse_lcdm = rmse(H_lcdm_planck, H_rep)

# ──────────────────────────────────────────────────────────
# BONUS: ratio deformation — what is H_FLRW / H_ΛCDM?
# ──────────────────────────────────────────────────────────
ratio = H_rep / H_lcdm_planck


# Fit ratio ~ (1+z)^β
def ratio_model(z, beta):
    return (1 + z) ** beta


res_ratio = curve_fit(ratio_model, z_arr, ratio, p0=[-0.4])
beta_ratio = res_ratio[0][0]
ratio_fitted = ratio_model(z_arr, beta_ratio)

# ──────────────────────────────────────────────────────────
# LOCAL α(z): effective power index at each point
# ──────────────────────────────────────────────────────────
# α(z) = d(ln H_FLRW)/d(ln(1+z)) via central differences
alpha_local = np.gradient(np.log(H_rep), np.log(1 + z_arr))

# ──────────────────────────────────────────────────────────
# PRINT RESULTS
# ──────────────────────────────────────────────────────────
print(f"\n{DIV}")
print("  H_FLRW CONVENTION RECOVERY — Table A1 vs candidate models")
print(f"  n=12 points | H0={H0_rep} km/s/Mpc | H_FLRW(z=8.5)={H_rep[-1]} (reported)")
print(DIV)

print("\n  [A] MODEL COMPARISON SUMMARY")
print(f"  {'Model':<42} {'MAE':>7} {'RMSE':>8}  {'max_err@z':>14}")
models = [
    ("ΛCDM Planck (H0=67.4, Ωm=0.315) [prev]", H_lcdm_planck, mae_lcdm, rmse_lcdm),
    (f"H1: power law H0*(1+z)^{alpha_best:.3f}", H_pl, mae_pl, rmse_pl),
    (
        f"H2: DE H²=H0²[Ωm(1+z)^n+(1-Ωm)] n={best_h2['n']:.1f} Ωm={best_h2['Om']:.3f}",
        best_h2["H_pred"],
        best_h2["mae"],
        best_h2["rmse"],
    ),
    (f"H3: H=β/t^γ  β={beta_t:.1f} γ={gamma_t:.3f}", H_t, mae_t, rmse_t),
    (f"H4: pure matter H0*sqrt(Ωm)*(1+z)^1.5  Ωm={Om_h4:.4f}", H_h4, mae_h4, rmse_h4),
]
for name, H_pred, m, r in models:
    errs = np.abs(H_pred - H_rep)
    worst_z = z_arr[np.argmax(errs)]
    print(f"  {name:<42} {m:>7.2f} {r:>8.2f}  max={errs.max():.1f}@z={worst_z:.2f}")

print(f"\n  [B] BEST MODEL DETAIL: H2 (n={best_h2['n']:.1f}, Ωm={best_h2['Om']:.3f})")
print(f"  {'z':>6} {'H_reported':>12} {'H_predicted':>12} {'residual':>10} {'%err':>7}")
for i, row in enumerate(TABLE):
    z = row[0]
    h_obs = H_rep[i]
    h_pred = best_h2["H_pred"][i]
    resid = h_pred - h_obs
    pct = 100 * resid / h_obs
    print(f"  {z:>6.2f} {h_obs:>12.1f} {h_pred:>12.1f} {resid:>10.2f} {pct:>6.1f}%")

print("\n  [C] LOCAL α(z) — effective power index d(ln H)/d(ln(1+z))")
print("  (Standard ΛCDM → α ranges from ~0.2 at z=0 to ~1.5 at z=8.5)")
print(f"  {'z':>6} {'H_FLRW':>10} {'α_local':>10} {'H_FLRW/H_ΛCDM':>15}")
for i in range(len(z_arr)):
    print(f"  {z_arr[i]:>6.2f} {H_rep[i]:>10.1f} {alpha_local[i]:>10.3f} {ratio[i]:>15.4f}")

print(f"\n  Power-law fit to ratio H_FLRW/H_ΛCDM ~ (1+z)^β: β={beta_ratio:.4f}")
print(f"  Ratio deformation MAE: {mae(ratio_fitted, ratio):.4f} (dimensionless)")

print("\n  [D] H3 DETAIL — H = β/t^γ fit to table time column")
print(f"  β={beta_t:.3f} km/s/Mpc·Gyr^γ,  γ={gamma_t:.4f}")
print(f"  {'z':>6} {'t_gyr':>8} {'H_FLRW':>10} {'H_t_pred':>12} {'residual':>10}")
for row in TABLE:
    z, _, _, h_flrw, t = row
    h_pred = h_time(t, beta_t, gamma_t)
    print(f"  {z:>6.2f} {t:>8.1f} {h_flrw:>10.1f} {h_pred:>12.2f} {h_pred - h_flrw:>10.2f}")

print("\n  [E] H2 SWEEP — MAE vs matter power index n")
print(f"  {'n':>5} {'best_Ωm':>10} {'MAE':>10} {'RMSE':>10}")
for n, Om, m, r in h2_sweep:
    marker = " ← BEST" if abs(n - best_h2["n"]) < 0.05 else ""
    print(f"  {n:>5.1f} {Om:>10.4f} {m:>10.2f} {r:>10.2f}{marker}")

print("\n  [F] VERDICT (hypothesis-arbiter)")
best_mae = min(m for _, _, m, _ in models)
best_name = [name for name, _, m, _ in models if m == best_mae][0]
print(f"  Best model: {best_name}")
print(f"  Best MAE: {best_mae:.2f} km/s/Mpc")
print()
if best_mae < 5:
    verdict = "RECOVERED — formula found with MAE < 5 km/s/Mpc"
elif best_mae < 15:
    verdict = "PARTIAL — best candidate plausible but not exact"
else:
    verdict = "NOT RECOVERED — no tested formula explains H_FLRW column"
print(f"  VERDICT: {verdict}")
print(f"\n  NOTE: ΛCDM Planck MAE = {mae_lcdm:.1f} km/s/Mpc for reference (prev sweep confirmed)")
print(f"  The H_FLRW column grows as ~(1+z)^α with α→{alpha_local[-1]:.2f} at z=8.5,")
print("  far slower than ΛCDM's effective α≈1.5 at high z.")
print(f"\n{DIV}\n")
