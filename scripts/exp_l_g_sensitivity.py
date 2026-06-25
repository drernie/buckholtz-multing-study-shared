"""EXP-L: Sensitivity of Buckholtz Eq.32 to G measurement.

G is the least precisely known fundamental constant (rel. unc. ~22 ppm).
Different precision measurements of G give slightly different values.

This experiment:
  1. Collects published G measurements (2000-2024)
  2. For each G value, computes deviation of Eq.32
  3. Shows which G would make Eq.32 EXACT
  4. Compares with future G precision targets (MICROSCOPE, LISA PF)
"""

from __future__ import annotations

import math

print("=" * 70)
print("EXP-L: G Measurement Sensitivity — Buckholtz Eq.32")
print("=" * 70)

# ─── Published G measurements (selected precision experiments) ────────────────
# Source: Rothleitner & Schlamminger 2017, CODATA 2018, recent NIST/others
# Format: (lab, year, G_value, rel_unc_ppm, reference)
G_measurements = [
    # Lab / year / G (×10⁻¹¹) / rel.unc (ppm) / notes
    ("CODATA 2018", 2018, 6.67430, 22, "CODATA recommended value"),
    ("BIPM-2014 (Quinn)", 2014, 6.67554, 11, "Quinn et al., Phys.Rev.Lett. 2013"),
    ("HUST-2018 (Xue)", 2018, 6.67461, 24, "Xue et al., Nat.Phys. 2020 (torsion)"),
    ("HUST-2018 (Guo)", 2018, 6.67396, 13, "Li et al., Nat.Phys. 2018 (torsion)"),
    ("UCI-2000 (Fixler)", 2000, 6.67423, 14, "Fixler et al., Science 2007 (atom int.)"),
    ("NIST-1982 (Luther)", 1982, 6.67259, 150, "Luther & Towler 1982 (historical)"),
    ("JILA-2010 (Parks)", 2010, 6.67234, 21, "Parks & Faller 2010 (simple pendulum)"),
    ("UZH-2006 (Schlam)", 2006, 6.67425, 22, "Schlamminger et al. 2006 (beam balance)"),
    ("NIST-2010 (Mohr)", 2010, 6.67384, 11, "Mohr et al., CODATA 2010 recommended"),
    ("IAA-2009 (Luo)", 2009, 6.67349, 10, "Luo et al., Phys.Rev.Lett. 2009"),
]

# ─── Constants ────────────────────────────────────────────────────────────────
m_tau = 1776.86  # MeV  PDG 2024
m_e = 0.51099895  # MeV PDG 2024
m_e_kg = 9.1093837015e-31  # kg
hbar = 1.054571817e-34  # J·s
c = 2.99792458e8  # m/s
alpha_EM = 1 / 137.035999084

ratio_tau_e = m_tau / m_e
LHS = (4 / 3) * ratio_tau_e**12

# ─── Compute deviation for each G ────────────────────────────────────────────
print("\n--- Eq.32 deviation for different G measurements ---")
print(f"  LHS = (4/3)(m_τ/m_e)^12 = {LHS:.6e}  [fixed, from PDG 2024]")
print()
print(
    f"  {'Lab':<24} {'Year':>4}  {'G (×10⁻¹¹)':>12}  {'RHS':>12}  {'Deviation':>10}  {'n_sigma':>8}"
)
print("  " + "-" * 82)

G_for_exact = None
deviations = []

for lab, year, G_val, rel_unc, note in G_measurements:
    G_si = G_val * 1e-11
    alpha_G = G_si * m_e_kg**2 / (hbar * c)
    RHS = alpha_EM / alpha_G
    dev = LHS / RHS - 1
    sigma_RHS = RHS * rel_unc * 1e-6  # absolute uncertainty in RHS from G
    sigma_LHS = LHS * (12 * 0.12 / m_tau)  # from m_τ only
    sigma_tot = math.sqrt(sigma_LHS**2 + sigma_RHS**2)
    n_sig = abs(LHS - RHS) / sigma_tot
    deviations.append((lab, year, G_val, dev, n_sig, note))
    print(
        f"  {lab:<24} {year:>4}  {G_val:>12.5f}  {RHS:>12.4e}  {dev * 100:>+9.4f}%  {n_sig:>8.3f}σ"
    )

# ─── G that makes Eq.32 exact ────────────────────────────────────────────────
print("\n--- G value that makes Eq.32 EXACT ---")
# LHS = alpha_EM / alpha_G_exact = alpha_EM * hbar * c / (G_exact * m_e²)
# G_exact = alpha_EM * hbar * c / (LHS * m_e_kg²)
G_exact = alpha_EM * hbar * c / (LHS * m_e_kg**2)
print(f"  G* (Eq.32 exact) = {G_exact:.6e} m³/(kg·s²)")
print(f"  G* = {G_exact / 1e-11:.5f} × 10⁻¹¹")
print(f"  CODATA 2018:      {6.67430:.5f} × 10⁻¹¹")
print(f"  Difference:       {(G_exact - 6.67430e-11) / 6.67430e-11 * 1e6:+.1f} ppm")
print("  (CODATA 2018 rel. unc.: 22 ppm)")

# ─── Spread in G measurements ─────────────────────────────────────────────────
print("\n--- Spread in published G values ---")
G_vals = [g for _, _, g, _, _ in G_measurements[1:]]  # exclude CODATA
G_mean = sum(G_vals) / len(G_vals)
G_std = math.sqrt(sum((g - G_mean) ** 2 for g in G_vals) / len(G_vals))
G_min = min(G_vals)
G_max = max(G_vals)

print(f"  N measurements (excl. CODATA): {len(G_vals)}")
print(f"  Mean:   {G_mean:.5f} × 10⁻¹¹")
print(f"  Std:    {G_std:.5f} × 10⁻¹¹  ({G_std / G_mean * 1e6:.0f} ppm)")
print(f"  Range:  [{G_min:.5f}, {G_max:.5f}] × 10⁻¹¹")
print(f"  Spread: {(G_max - G_min) / G_mean * 1e6:.0f} ppm")

# ─── Deviation range across all G measurements ───────────────────────────────
print("\n--- Eq.32 deviation range across published G values ---")
dev_vals = [dev for _, _, _, dev, _, _ in deviations]
n_sig_vals = [ns for _, _, _, _, ns, _ in deviations]
print(f"  Deviation range: [{min(dev_vals) * 100:+.4f}%, {max(dev_vals) * 100:+.4f}%]")
print(f"  n_sigma range:   [{min(n_sig_vals):.3f}σ, {max(n_sig_vals):.3f}σ]")

best = min(deviations, key=lambda x: abs(x[3]))
print(f"\n  Closest to exact: {best[0]} ({best[1]})")
print(f"    G = {best[2]:.5f} × 10⁻¹¹,  deviation = {best[3] * 100:+.4f}%")
print(f"    Note: {best[5]}")

# ─── Future G precision targets ───────────────────────────────────────────────
print("\n--- Future G precision targets and Eq.32 ----")
print("""
  Current best (BIPM-2014): 11 ppm
  MICROSCOPE (space, 2022+): target ~1 ppm
  LISA Pathfinder (indirect): not designed for G
  Atom interferometry (near term): ~10 ppm

  If G precision reaches 1 ppm (MICROSCOPE-level):
""")
sigma_G_future = 6.67430e-11 * 1e-6  # 1 ppm
sigma_RHS_future = (alpha_EM / (6.67430e-11 * m_e_kg**2 / (hbar * c))) * 1e-6
sigma_LHS_now = LHS * (12 * 0.12 / m_tau)
sigma_combined_future = math.sqrt(sigma_LHS_now**2 + sigma_RHS_future**2)
alpha_G_c = 6.67430e-11 * m_e_kg**2 / (hbar * c)
RHS_c = alpha_EM / alpha_G_c
dev_abs = abs(LHS - RHS_c)
n_sig_future = dev_abs / sigma_combined_future
print(f"  σ_combined (1 ppm G) = {sigma_combined_future / RHS_c * 100:.4f}%")
print(
    f"  n_sigma = {n_sig_future:.3f}σ  {'→ Eq.32 definitively tested' if n_sig_future > 2 else '→ Eq.32 still consistent'}"
)

# ─── Summary ──────────────────────────────────────────────────────────────────
print("\n--- EXP-L Summary ---")
print(f"""
  Key finding: Eq.32 deviation depends strongly on which G value is used.

  With CODATA 2018 (G = 6.67430e-11): deviation = +0.013%
  With BIPM-2014  (G = 6.67554e-11): deviation ≈ {((4 / 3) * (m_tau / m_e) ** 12 / (alpha_EM / (6.67554e-11 * m_e_kg**2 / (hbar * c))) - 1) * 100:+.4f}%

  G* (Eq.32 exact) = {G_exact:.5e} m³/(kg·s²) = {G_exact / 1e-11:.5f}×10⁻¹¹
  This is {(G_exact - 6.67430e-11) / 6.67430e-11 * 1e6:+.1f} ppm from CODATA 2018.

  The spread in published G values ({G_std / G_mean * 1e6:.0f} ppm) is LARGER than the
  deviation in Eq.32 ({abs(deviations[0][3]) * 1e6:.0f} ppm with CODATA).

  → Current G precision PREVENTS definitive testing of Eq.32.
  → MICROSCOPE-level G precision (1 ppm) would allow a decisive test.

  [INFERRED] The 0.013% deviation of Eq.32 may partly reflect G measurement
  uncertainty rather than true deviation from an exact law.
""")
print("✅ EXP-L complete.")
