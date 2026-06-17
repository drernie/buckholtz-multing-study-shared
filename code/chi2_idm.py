"""
chi2_idm.py — Formal kill of IDM integer isomer count
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
"""

import numpy as np

# Planck 2018 TT,TE,EE+lowE+lensing (Table 2, Aghanim+2020)
omega_b = 0.022383  # baryon density parameter (h^-2)
sigma_b = 0.00015  # 1-sigma uncertainty on omega_b
omega_dm = 0.12011  # dark matter density parameter (h^-2)
sigma_dm = 0.0012  # 1-sigma uncertainty on omega_dm

# IDM prediction: omega_dm = N * omega_b
# (assumes equal baryon density per isomer, equal mass, equal asymmetry)
N_optimal = omega_dm / omega_b

print("=" * 65)
print("IDM χ²(N) test — Planck 2018 vs integer isomer count")
print("NOTE: sigma_total = sqrt(sigma_dm² + (N*sigma_b)²) — both propagated")
print("=" * 65)
print(f"\nPlanck 2018: ω_DM = {omega_dm} ± {sigma_dm}, ω_b = {omega_b} ± {sigma_b}")
print(f"IDM requires N = ω_DM / ω_b = {N_optimal:.4f}  ← non-integer\n")
print(f"{'N':>4} | {'pred ω_DM':>12} | {'σ_total':>9} | {'n_σ':>6} | {'status':>10}")
print("-" * 60)

for N in range(1, 11):
    pred = N * omega_b
    # Proper error propagation: uncertainty on pred = N * sigma_b
    sigma_total = np.sqrt(sigma_dm**2 + (N * sigma_b) ** 2)
    diff = abs(pred - omega_dm)
    n_sigma = diff / sigma_total
    status = "✅ best" if N == 5 else ("❌ killed" if n_sigma > 3 else "⚠️ marginal")
    print(f"{N:>4} | {pred:>12.6f} | {sigma_total:>9.6f} | {n_sigma:>6.2f}σ | {status:>10}")

N = 5
pred5 = N * omega_b
sigma_total5 = np.sqrt(sigma_dm**2 + (N * sigma_b) ** 2)
n_sigma5 = abs(pred5 - omega_dm) / sigma_total5

print("\nN=5 detail:")
print(f"  pred = 5 × {omega_b} = {pred5:.6f}")
print(f"  diff = |{pred5:.6f} - {omega_dm}| = {abs(pred5 - omega_dm):.6f}")
print(f"  σ_total = √({sigma_dm}² + (5×{sigma_b})²) = {sigma_total5:.6f}")
print(f"  n_σ = {abs(pred5 - omega_dm):.6f} / {sigma_total5:.6f} = {n_sigma5:.2f}σ")
print(f"\nN=5 predicts ω_DM = {pred5:.5f}, Planck = {omega_dm:.5f}")
print(
    f"Absolute difference: {abs(pred5 - omega_dm):.5f} = {abs(pred5 - omega_dm) / omega_dm * 100:.1f}%"
)
print(f"\nVERDICT: Integer N=5 is EXCLUDED at {n_sigma5:.1f}σ by Planck 2018")
print("(properly propagating uncertainties on both ω_DM and ω_b).")
print("IDM requires N ≈ 5.37 (non-integer) OR unequal isomer masses.")
print("Either way: 'simple count' argument is formally killed.")
