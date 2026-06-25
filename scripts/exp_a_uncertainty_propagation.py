"""EXP-A: Uncertainty propagation for Buckholtz Eq.32.

Claim: (4/3)(m_tau/m_e)^12 = alpha_EM / alpha_G
Eq: LHS/RHS = 1.000135 (0.0135% deviation)

This script computes the FULL measurement uncertainty in LHS/RHS
from PDG 2024 + CODATA 2018/2022 uncertainties.

Key questions:
  Q1: Is 0.0135% within or outside 1-sigma measurement noise?
  Q2: Which constant dominates the uncertainty budget?
  Q3: How much m_tau precision do we need for a 1-sigma confirmation?
"""

from __future__ import annotations

import math

# ─── Constants + Uncertainties (CODATA 2018 / PDG 2024) ─────────────────────
# Exact (defined in SI since 2019):
c_exact = 2.99792458e8  # m/s  (exact)
hbar_exact = 1.054571817e-34  # J·s  (exact)

# Measured:
G_val = 6.67430e-11
G_unc = 0.00015e-11  # CODATA 2018 (rel: 22 ppm)
m_e_kg = 9.1093837015e-31
m_e_unc_kg = 0.0000000028e-31  # CODATA 2018
alpha_EM = 1 / 137.035999084
alpha_EM_unc = 1.5e-10 * alpha_EM  # rel 0.15 ppb

# PDG 2024 lepton masses
m_tau_MeV = 1776.86
m_tau_unc_MeV = 0.12  # ±0.12 MeV
m_e_MeV = 0.51099895
m_e_unc_MeV = 0.00000001  # negligible

# ─── Compute central values ──────────────────────────────────────────────────
alpha_G = G_val * m_e_kg**2 / (hbar_exact * c_exact)
LHS = (4 / 3) * (m_tau_MeV / m_e_MeV) ** 12
RHS = alpha_EM / alpha_G
ratio = LHS / RHS

# ─── Partial derivatives (log-space) ────────────────────────────────────────
# LHS = (4/3)(m_tau/m_e)^12
# d(ln LHS)/d(ln m_tau) = +12
# d(ln LHS)/d(ln m_e)   = -12
# RHS = alpha_EM * hbar * c / (G * m_e_kg^2)
# d(ln RHS)/d(ln alpha_EM) = +1
# d(ln RHS)/d(ln G)         = -1
# d(ln RHS)/d(ln m_e_kg)    = -2

# Relative uncertainties
rel_m_tau = m_tau_unc_MeV / m_tau_MeV  # dominant for LHS
rel_m_e_MeV = m_e_unc_MeV / m_e_MeV  # negligible
rel_G = G_unc / G_val  # dominant for RHS
rel_alpha = alpha_EM_unc / alpha_EM  # negligible
rel_m_e_kg = m_e_unc_kg / m_e_kg  # small

# LHS relative uncertainty
lhs_unc_rel = math.sqrt((12 * rel_m_tau) ** 2 + (12 * rel_m_e_MeV) ** 2)
# RHS relative uncertainty
rhs_unc_rel = math.sqrt(rel_alpha**2 + rel_G**2 + (2 * rel_m_e_kg) ** 2)
# Total uncertainty on ratio LHS/RHS
total_unc_rel = math.sqrt(lhs_unc_rel**2 + rhs_unc_rel**2)

deviation_rel = abs(ratio - 1.0)
sigma = deviation_rel / total_unc_rel

# ─── Print results ──────────────────────────────────────────────────────────
print("=" * 65)
print("EXP-A: Uncertainty Propagation — Buckholtz Eq.32")
print("=" * 65)
print(f"\n  alpha_G               = {alpha_G:.6e}")
print(f"  LHS = (4/3)(r^12)     = {LHS:.6e}")
print(f"  RHS = aEM/aG          = {RHS:.6e}")
print(f"  LHS/RHS (ratio)       = {ratio:.8f}")
print(f"  Deviation from 1.0    = {deviation_rel * 100:.6f}%  ({deviation_rel:.4e})")

print("\n--- Uncertainty Budget ---")
print(f"  rel σ(m_τ) [PDG 2024] = {rel_m_tau * 100:.4f}%  ({rel_m_tau:.2e})")
print(f"  12 × rel σ(m_τ)       = {12 * rel_m_tau * 100:.4f}%  ← LHS dominant")
print(f"  rel σ(m_e) [MeV]      = {rel_m_e_MeV:.2e}  (negligible)")
print(f"  rel σ(G)              = {rel_G * 100:.4f}%  ({rel_G:.2e})  ← RHS dominant")
print(f"  rel σ(α_EM)           = {rel_alpha:.2e}  (negligible)")
print(f"  rel σ(m_e) [kg]       = {rel_m_e_kg:.2e}  (negligible)")
print(f"\n  σ_LHS / LHS           = {lhs_unc_rel * 100:.4f}%  (dominated by m_τ)")
print(f"  σ_RHS / RHS           = {rhs_unc_rel * 100:.4f}%  (dominated by G)")
print(f"  σ_TOTAL / (LHS/RHS)   = {total_unc_rel * 100:.4f}%")

print("\n--- Statistical Significance ---")
print(f"  Deviation             = {deviation_rel * 100:.4f}%")
print(f"  Total 1-sigma         = {total_unc_rel * 100:.4f}%")
print(f"  Significance          = {sigma:.3f} σ")
if sigma < 1.0:
    print("  VERDICT: Deviation is WITHIN 1-sigma measurement noise")
    print("  Formula is CONSISTENT with exact equality at current precision")
else:
    print("  VERDICT: Deviation EXCEEDS 1-sigma → formula not exact, or measurement error")

# ─── Sensitivity: how precise must m_tau be for N-sigma confirmation? ─────
print("\n--- m_τ Precision Required for N-sigma confirmation ---")
print("  (assuming G and other constants unchanged)")
for n_sigma in [1.0, 2.0, 3.0, 5.0]:
    # Need: total_unc_rel = deviation_rel / n_sigma
    # total_unc_rel^2 = (12 * rel_m_tau_new)^2 + rhs_unc_rel^2
    target_total = deviation_rel / n_sigma
    lhs_needed_sq = target_total**2 - rhs_unc_rel**2
    if lhs_needed_sq > 0:
        rel_needed = math.sqrt(lhs_needed_sq) / 12
        m_tau_unc_needed = rel_needed * m_tau_MeV
        print(
            f"  {n_sigma:.0f}σ: need σ(m_τ) ≤ {m_tau_unc_needed * 1000:.2f} keV  "
            f"(current: {m_tau_unc_MeV * 1000:.0f} keV, need {m_tau_unc_MeV / m_tau_unc_needed:.1f}× improvement)"
        )
    else:
        print(
            f"  {n_sigma:.0f}σ: NOT ACHIEVABLE — RHS uncertainty ({rhs_unc_rel * 100:.4f}%) "
            f"already larger than needed ({target_total * 100:.4f}%)"
        )

# ─── Sensitivity to G ─────────────────────────────────────────────────────
print("\n--- Sensitivity to G measurement ---")
print(f"  Current σ(G)/G = {rel_G * 100:.4f}%  (CODATA 2018)")
print(f"  If G known exactly: total σ → {12 * rel_m_tau * 100:.4f}%")
print(
    f"  → significance would be {deviation_rel / (12 * rel_m_tau):.3f} σ  (no change: m_τ dominates)"
)

# ─── Contribution table ───────────────────────────────────────────────────
print("\n--- Uncertainty Contribution Table ---")
contributions = [
    ("m_τ [PDG]   (×12 power)", 12 * rel_m_tau, "LHS"),
    ("G [CODATA]             ", rel_G, "RHS"),
    ("m_e_kg [CODATA] (×2)  ", 2 * rel_m_e_kg, "RHS"),
    ("m_e_MeV [PDG]   (×12) ", 12 * rel_m_e_MeV, "LHS"),
    ("α_EM [CODATA]          ", rel_alpha, "RHS"),
]
for name, val, _side in contributions:
    frac = val / total_unc_rel * 100
    bar = "█" * int(frac / 2)
    print(f"  {name}: {val * 100:.5f}% [{frac:4.1f}%] {bar}")

print(f"\n  Total σ: {total_unc_rel * 100:.5f}%")
print(f"  Deviation: {deviation_rel * 100:.5f}%  ({sigma:.3f}σ)")
print("\n✅ EXP-A complete.")
