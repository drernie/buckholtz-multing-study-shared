"""
beta_rescaling.py — Quantify and visualize the β-rescaling gap
Table A1 gives β_d = 4.5; physical k_A = E_ICM/c² requires β_d >> 10³.
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
"""

import numpy as np

# ──────────────────────────────────────────────
# Physical inputs
# ──────────────────────────────────────────────
G = 6.67430e-11  # m³ kg⁻¹ s⁻²
c = 299792458.0  # m/s
c2 = c**2
M_sun_kg = 1.989e30  # kg

# Typical galaxy cluster parameters (MCXC median)
M_cluster_Msun = 5e14  # total mass, solar masses
R500_Mpc = 0.8  # Mpc
Mpc_to_m = 3.0857e22  # 1 Mpc in meters

M_cluster_kg = M_cluster_Msun * M_sun_kg
R500_m = R500_Mpc * Mpc_to_m

# ICM thermal energy: E_ICM ~ N_e * k_B * T_X
# For T_X ~ 5 keV cluster, f_gas ~ 0.15, mean molecular weight ~ 0.6 m_p
kT_keV = 5.0  # keV, typical X-ray temperature
kT_J = kT_keV * 1.602e-16  # J
f_gas = 0.15
m_p = 1.673e-27  # kg
mu = 0.6  # mean molecular weight in units of m_p

N_particles = (f_gas * M_cluster_kg) / (mu * m_p)
E_ICM = N_particles * kT_J  # total ICM thermal energy (J)
k_A = E_ICM / c2  # k_A in kg (TJB definition: E/c²)
k_A_Msun = k_A / M_sun_kg  # in solar masses

# ──────────────────────────────────────────────
# Dipole force ratio: F_d / F_m
# ──────────────────────────────────────────────
# F_d/F_m = β_d * (k_A / M) * (R500 / D)
# For self-matching: set r_A = R500, D = some probing distance
# At D = R500 (within the cluster):
r_ratio = R500_m / R500_m  # = 1 (r_A/D = 1 at cluster boundary)
mass_ratio = k_A_Msun / M_cluster_Msun

beta_table_A1 = 4.5
beta_gemini = 2e4  # Gemini AI service reported value
beta_needed_for_epsilon_10pct = 0.10 / mass_ratio  # to get F_d/F_m = 10%

epsilon_table_A1 = beta_table_A1 * mass_ratio * r_ratio
epsilon_gemini = beta_gemini * mass_ratio * r_ratio

print("=" * 65)
print("β-rescaling gap analysis: F_d/F_m at cluster scale")
print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
print("=" * 65)
print("\nCluster parameters (MCXC median):")
print(f"  M_cluster = {M_cluster_Msun:.1e} M_☉")
print(f"  R500      = {R500_Mpc:.1f} Mpc")
print(f"  T_X       = {kT_keV:.0f} keV")
print(f"  f_gas     = {f_gas:.2f}")

print("\nPhysical k_A from E_ICM/c²:")
print(f"  E_ICM = {E_ICM:.3e} J")
print(f"  k_A   = {k_A_Msun:.3e} M_☉  ({k_A_Msun / M_cluster_Msun:.2e} of M_cluster)")

print(f"\n  mass_ratio k_A/M = {mass_ratio:.3e}")

print("\nDipole force fractions ε = F_d/F_m = β_d × (k_A/M) × (r_A/D):")
print(f"  β_d = {beta_table_A1} (Table A1):  ε = {epsilon_table_A1:.2e}  ← NEGLIGIBLE")
print(f"  β_d = {beta_gemini:.0e} (Gemini): ε = {epsilon_gemini:.2e}  ← MARGINALLY OBSERVABLE")
print(f"  β_d needed for ε=10%: {beta_needed_for_epsilon_10pct:.2e}")
print(f"  β_d needed for ε=1%:  {0.01 / mass_ratio:.2e}")

print("\nβ GAP:")
print(f"  Table A1 / physical: {beta_needed_for_epsilon_10pct / beta_table_A1:.1e}")
print(f"  → {np.log10(beta_needed_for_epsilon_10pct / beta_table_A1):.1f} orders of magnitude")
print(f"  → For ε=1%: {np.log10(0.01 / mass_ratio / beta_table_A1):.1f} orders of magnitude")
print(f"  → Gemini β bridges to: {np.log10(epsilon_gemini):.1f} (log10 of ε)")

print("\nSolar system comparison (for reference):")
# Sun: k_Sun ≈ 3e-17 M_sun (corona thermal energy), R_sun = 7e8 m, D = 1 AU = 1.5e11 m
k_sun_Msun = 3e-17
R_sun_AU = 0.00465  # R_sun in AU
D_AU = 1.0
epsilon_sun = beta_table_A1 * (k_sun_Msun / 1.0) * (R_sun_AU / D_AU)
print(f"  k_sun = {k_sun_Msun:.1e} M_☉  (corona E/c²)")
print(f"  ε_solar(β=4.5) = {epsilon_sun:.2e}  → Cassini < 2.3e-5 ✅")

print("\nSUMMARY:")
print(
    f"  Table A1 value β_d=4.5 makes dipole NEGLIGIBLE ({epsilon_table_A1:.0e}) at cluster scale."
)
print(f"  For observational signature (~1%), need β_d ≈ {0.01 / mass_ratio:.1e}.")
print(f"  Gemini β_d≈2e4 gives ε≈{epsilon_gemini:.0e} (marginally non-negligible).")
print("  This β-rescaling gap is the main unresolved issue for MULTING H(z) test.")
print("  Resolution requires: derivation of β from cluster physics (TJB Q1).")
