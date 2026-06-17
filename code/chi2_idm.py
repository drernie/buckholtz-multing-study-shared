"""
chi2_idm.py — Formal kill of IDM integer isomer count
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
"""

import numpy as np

# Planck 2018 TT,TE,EE+lowE+lensing (Table 2, Aghanim+2020)
omega_b = 0.022383  # baryon density parameter (h^-2)
omega_dm = 0.12011  # dark matter density parameter (h^-2)
sigma = 0.0012  # 1-sigma uncertainty on omega_dm

# IDM prediction: omega_dm = N * omega_b
# (assumes equal baryon density per isomer, equal mass, equal asymmetry)
N_optimal = omega_dm / omega_b

print("=" * 55)
print("IDM χ²(N) test — Planck 2018 vs integer isomer count")
print("=" * 55)
print(f"\nPlanck 2018: ω_DM = {omega_dm}, ω_b = {omega_b}")
print(f"IDM requires N = ω_DM / ω_b = {N_optimal:.4f}  ← non-integer\n")
print(f"{'N':>4} | {'pred ω_DM':>12} | {'χ²':>8} | {'σ':>6} | {'status':>10}")
print("-" * 55)

for N in range(1, 11):
    pred = N * omega_b
    chi2 = ((pred - omega_dm) / sigma) ** 2
    sigma_n = np.sqrt(chi2)
    status = "✅ best" if N == 5 else ("❌ killed" if sigma_n > 3 else "⚠️ marginal")
    print(f"{N:>4} | {pred:>12.6f} | {chi2:>8.1f} | {sigma_n:>6.1f}σ | {status:>10}")

print(
    f"\nN=5 (IDM): χ² = {((5 * omega_b - omega_dm) / sigma) ** 2:.1f}"
    f" = {np.sqrt(((5 * omega_b - omega_dm) / sigma) ** 2):.1f}σ from Planck"
)
print(f"N=5 predicts ω_DM = {5 * omega_b:.5f}, Planck = {omega_dm:.5f}")
print(
    f"Absolute difference: {abs(5 * omega_b - omega_dm):.5f}"
    f" = {abs(5 * omega_b - omega_dm) / omega_dm * 100:.1f}%"
)
print("\nVERDICT: Integer N=5 is EXCLUDED at 6.8σ by Planck 2018.")
print("IDM requires N ≈ 5.37 (non-integer) OR unequal isomer masses.")
print("Either way: 'simple count' argument is formally killed.")
