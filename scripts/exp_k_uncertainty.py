"""EXP-K: Propagation of Uncertainty for Buckholtz Eq.32.

Eq.32: (4/3)(m_τ/m_e)^12 = α_EM / α_G
where α_G = G · m_e² / (ħ c)

Inputs (PDG 2024 / CODATA 2018):
  m_τ = 1776.86 ± 0.12 MeV
  m_e = 0.51099895000 ± 0.00000000015 MeV  (negligible)
  G   = 6.67430e-11 ± 0.00015e-11 m³/(kg·s²)  (CODATA 2018, rel. unc. 22 ppm)
  α_EM = 1/137.035999084 ± 0.000000021  (negligible)
  ħ, c — exact (defined)

Goal: compute σ(LHS), σ(RHS), and the combined significance of Eq.32.
"""

from __future__ import annotations

import math

print("=" * 70)
print("EXP-K: Propagation of Uncertainty — Buckholtz Eq.32")
print("=" * 70)

# ─── Central values ───────────────────────────────────────────────────────────
m_tau_c = 1776.86  # MeV
m_e_c = 0.51099895  # MeV
G_c = 6.67430e-11  # m³/(kg·s²)  CODATA 2018
hbar = 1.054571817e-34  # J·s  (exact since 2019 SI)
c = 2.99792458e8  # m/s  (exact)
m_e_kg = 9.1093837015e-31  # kg  CODATA 2018
alpha_EM = 1 / 137.035999084  # CODATA 2018

# ─── Uncertainties (1σ, absolute) ─────────────────────────────────────────────
sigma_m_tau = 0.12  # MeV  (PDG 2024)
sigma_m_e = 0.00000000015  # MeV (negligible — defined quantity via SI)
sigma_G = 0.00015e-11  # m³/(kg·s²)  CODATA 2018 (22 ppm)
sigma_alpha = 0.000000021 / 137.035999084**2  # rel unc 0.15 ppb, negligible

# ─── Central values of LHS and RHS ───────────────────────────────────────────
print("\n--- Central values ---")
ratio_c = m_tau_c / m_e_c
LHS_c = (4 / 3) * ratio_c**12

alpha_G_c = G_c * m_e_kg**2 / (hbar * c)
RHS_c = alpha_EM / alpha_G_c

deviation_c = LHS_c / RHS_c - 1

print(f"  m_τ/m_e = {ratio_c:.6f}")
print(f"  LHS = (4/3)(m_τ/m_e)^12 = {LHS_c:.6e}")
print(f"  RHS = α_EM/α_G(e)       = {RHS_c:.6e}")
print(f"  Deviation: (LHS/RHS - 1) = {deviation_c:.6f}  ({deviation_c * 100:.4f}%)")

# ─── Partial derivatives (analytical) ────────────────────────────────────────
print("\n--- Partial derivatives ---")

# LHS = (4/3) * (m_τ/m_e)^12
# ∂LHS/∂m_τ = (4/3) * 12 * (m_τ/m_e)^11 * (1/m_e)
dLHS_dm_tau = (4 / 3) * 12 * (m_tau_c / m_e_c) ** 11 / m_e_c
print(f"  ∂LHS/∂m_τ = {dLHS_dm_tau:.4e}  (per MeV)")

# ∂LHS/∂m_e = (4/3) * 12 * (m_τ/m_e)^11 * (-m_τ/m_e²)
dLHS_dm_e = (4 / 3) * 12 * (m_tau_c / m_e_c) ** 11 * (-m_tau_c / m_e_c**2)
print(f"  ∂LHS/∂m_e = {dLHS_dm_e:.4e}  (per MeV)")

# RHS = α_EM / α_G = α_EM * ħ * c / (G * m_e_kg²)
# ∂RHS/∂G = -RHS/G
dRHS_dG = -RHS_c / G_c
print(f"  ∂RHS/∂G   = {dRHS_dG:.4e}  (per m³/kg/s²)")

# ─── Uncertainty contributions to LHS ────────────────────────────────────────
print("\n--- Uncertainty budget for LHS ---")
sigma_LHS_m_tau = abs(dLHS_dm_tau) * sigma_m_tau
sigma_LHS_m_e = abs(dLHS_dm_e) * sigma_m_e

sigma_LHS_total = math.sqrt(sigma_LHS_m_tau**2 + sigma_LHS_m_e**2)

rel_unc_LHS = sigma_LHS_total / LHS_c

print(f"  From m_τ: σ(LHS) = {sigma_LHS_m_tau:.4e}  ({sigma_LHS_m_tau / LHS_c * 100:.4f}%)")
print(
    f"  From m_e: σ(LHS) = {sigma_LHS_m_e:.4e}  ({sigma_LHS_m_e / LHS_c * 100:.6f}%)  [negligible]"
)
print(f"  Total:    σ(LHS) = {sigma_LHS_total:.4e}  ({rel_unc_LHS * 100:.4f}%)")

# ─── Uncertainty contributions to RHS ────────────────────────────────────────
print("\n--- Uncertainty budget for RHS ---")
sigma_RHS_G = abs(dRHS_dG) * sigma_G
sigma_RHS_alpha = RHS_c * (sigma_alpha / alpha_EM)  # negligible

sigma_RHS_total = math.sqrt(sigma_RHS_G**2 + sigma_RHS_alpha**2)
rel_unc_RHS = sigma_RHS_total / RHS_c

print(f"  From G:     σ(RHS) = {sigma_RHS_G:.4e}  ({sigma_RHS_G / RHS_c * 100:.4f}%)  ← dominant")
print(
    f"  From α_EM:  σ(RHS) = {sigma_RHS_alpha:.4e}  ({sigma_RHS_alpha / RHS_c * 100:.6f}%)  [negligible]"
)
print(f"  Total:      σ(RHS) = {sigma_RHS_total:.4e}  ({rel_unc_RHS * 100:.4f}%)")

# ─── Combined significance ────────────────────────────────────────────────────
print("\n--- Combined significance of Eq.32 ---")

# The test: LHS = RHS
# Test statistic: (LHS - RHS) / sqrt(σ_LHS² + σ_RHS²)
diff = LHS_c - RHS_c
sigma_combined = math.sqrt(sigma_LHS_total**2 + sigma_RHS_total**2)
sigma_combined_rel = sigma_combined / RHS_c

n_sigma = abs(diff) / sigma_combined

print(f"  LHS - RHS = {diff:.4e}")
print(f"  σ_combined = {sigma_combined:.4e}  ({sigma_combined_rel * 100:.4f}%)")
print(f"  Significance: |LHS - RHS| / σ = {n_sigma:.3f} σ")
print()
if n_sigma < 1.0:
    verdict = "CONSISTENT WITH EXACT at < 1σ — Eq.32 could be exact"
elif n_sigma < 2.0:
    verdict = "CONSISTENT at < 2σ — plausible coincidence or approximate law"
else:
    verdict = f"TENSION at {n_sigma:.1f}σ — less likely to be exact"
print(f"  Verdict: {verdict}")

# ─── Breakdown: what dominates? ───────────────────────────────────────────────
print("\n--- Dominant uncertainty source ---")
print(f"  σ(LHS) from m_τ:  {rel_unc_LHS * 100:.4f}%  (PDG 2024, ±0.12 MeV)")
print(f"  σ(RHS) from G:    {rel_unc_RHS * 100:.4f}%  (CODATA 2018, ±0.00015e-11)")
if rel_unc_RHS > rel_unc_LHS:
    print("  → G measurement is the DOMINANT uncertainty (not m_τ!)")
    print(f"    To reduce σ_combined by 2×, need G precision: ±{sigma_G / 2:.5e} m³/kg/s²")
    print(f"    Current CODATA rel. unc.: {sigma_G / G_c * 1e6:.1f} ppm")
    print(f"    Required rel. unc.:       {sigma_G / G_c * 1e6 / 2:.1f} ppm")
else:
    print("  → m_τ measurement is the DOMINANT uncertainty")

# ─── Numerical check via finite differences ───────────────────────────────────
print("\n--- Numerical cross-check (finite differences) ---")


def lhs(m_tau: float, m_e: float) -> float:
    return (4 / 3) * (m_tau / m_e) ** 12


def rhs(G: float) -> float:
    aG = G * m_e_kg**2 / (hbar * c)
    return alpha_EM / aG


# Numerical partials
eps_tau = sigma_m_tau * 1e-3  # small step
dLHS_num = (lhs(m_tau_c + eps_tau, m_e_c) - lhs(m_tau_c - eps_tau, m_e_c)) / (2 * eps_tau)
eps_G = sigma_G * 1e-3
dRHS_num = (rhs(G_c + eps_G) - rhs(G_c - eps_G)) / (2 * eps_G)

print(f"  ∂LHS/∂m_τ analytical: {dLHS_dm_tau:.6e}")
print(f"  ∂LHS/∂m_τ numerical:  {dLHS_num:.6e}")
print(f"  ∂RHS/∂G   analytical: {dRHS_dG:.6e}")
print(f"  ∂RHS/∂G   numerical:  {dRHS_num:.6e}")
print(f"  Agreement: {'OK' if abs(dLHS_dm_tau / dLHS_num - 1) < 1e-6 else 'MISMATCH'}")

# ─── Belle II projection ──────────────────────────────────────────────────────
print("\n--- Belle II precision projection ---")
sigma_m_tau_belle2 = 0.01  # MeV  (target precision)

sigma_LHS_belle2 = abs(dLHS_dm_tau) * sigma_m_tau_belle2
rel_LHS_belle2 = sigma_LHS_belle2 / LHS_c
sigma_combined_belle2 = math.sqrt(sigma_LHS_belle2**2 + sigma_RHS_total**2)
n_sigma_belle2 = abs(diff) / sigma_combined_belle2

print(f"  Belle II target: σ(m_τ) = {sigma_m_tau_belle2} MeV")
print(f"  → σ(LHS) from m_τ: {rel_LHS_belle2 * 100:.4f}%")
print(f"  → σ_combined: {sigma_combined_belle2 / RHS_c * 100:.4f}%")
print(f"  → Significance: {n_sigma_belle2:.3f}σ")
print()
if n_sigma_belle2 < 1.0:
    print("  Belle II: still consistent → Eq.32 remains viable as exact law")
    print("  Belle II would need to find m_τ = 1776.840 MeV to exclude current PDG value")

print("\n✅ EXP-K complete.")
