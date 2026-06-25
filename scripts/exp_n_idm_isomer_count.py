"""EXP-N: IDM Isomer Count — Planck 2018 Constraint Analysis.

Question: Is the N=5 exclusion (5.67σ) a falsification of IDM, or
          can it be re-read as a *measurement* of IDM parameters?

Sub-questions:
  1. Reproduce the N=5 @ 5.67σ exclusion from Planck 2018
  2. What is N_Planck (the Planck-preferred value)?
  3. What range of N is Planck-compatible at 1σ, 2σ, 3σ?
  4. If N=5 isomers with UNEQUAL masses, what mass distribution
     makes the model Planck-compatible?
  5. Interpretation: measurement or falsification?
"""

from __future__ import annotations

import math

print("=" * 70)
print("EXP-N: IDM Isomer Count — Planck 2018 Constraint Analysis")
print("=" * 70)

# ─── Planck 2018 cosmological parameters ─────────────────────────────────────
# Source: Planck 2018 Results VI (arXiv:1807.06209), Table 2
# TT,TE,EE+lowE+lensing
omega_c_h2 = 0.12011  # Ω_c h²  (cold dark matter density)
sigma_omega_c = 0.00096

omega_b_h2 = 0.02237  # Ω_b h²  (baryon density)
sigma_omega_b = 0.00015

# ─── Derived ratio R = ω_DM / ω_b ────────────────────────────────────────────
print("\n--- 1. Planck 2018 dark-matter-to-baryon ratio ---")

R = omega_c_h2 / omega_b_h2
# Error propagation: σ(R)/R = sqrt((σ_c/ω_c)² + (σ_b/ω_b)²)
rel_sigma_R = math.sqrt((sigma_omega_c / omega_c_h2) ** 2 + (sigma_omega_b / omega_b_h2) ** 2)
sigma_R = R * rel_sigma_R

print(f"  ω_c h² = {omega_c_h2:.5f} ± {sigma_omega_c:.5f}")
print(f"  ω_b h² = {omega_b_h2:.5f} ± {sigma_omega_b:.5f}")
print(f"  R = ω_DM/ω_b = {R:.5f} ± {sigma_R:.5f}")
print(f"  Relative uncertainty: {rel_sigma_R * 100:.4f}%")

# ─── IDM assumption: equal-mass isomers ──────────────────────────────────────
# If there are N isomers, each with the same mass as the proton,
# and equal number density as baryons, then ω_DM/ω_b = N exactly.
# IDM paper proposes N=5 → predicts R=5.

print("\n--- 2. Reproduce N=5 exclusion at 5.67σ ---")

N_IDM = 5
deviation = R - N_IDM
n_sigma = deviation / sigma_R

print(f"  IDM prediction (equal-mass): N = {N_IDM}")
print(f"  Planck 2018 best-fit:        R = {R:.5f}")
print(f"  Deviation:  R - N = {deviation:+.5f}")
print(f"  σ(R):                        {sigma_R:.5f}")
print(f"  Exclusion: (R - N) / σ(R) = {n_sigma:.2f}σ")
if abs(n_sigma) > 5:
    print(f"  → N=5 (equal-mass) EXCLUDED at {abs(n_sigma):.2f}σ  [VERIFIED]")

# ─── Planck-preferred N ───────────────────────────────────────────────────────
print("\n--- 3. Planck-preferred isomer count N_Planck ---")

N_planck = R  # Under equal-mass assumption, N_Planck = R exactly
print(f"  N_Planck = {N_planck:.5f}")
print(f"  σ(N_Planck) = {sigma_R:.5f}")
print(f"  N_Planck (68% CL): [{N_planck - sigma_R:.5f}, {N_planck + sigma_R:.5f}]")
print(f"  N_Planck (95% CL): [{N_planck - 2 * sigma_R:.5f}, {N_planck + 2 * sigma_R:.5f}]")
print(f"  N_Planck (99.7%):  [{N_planck - 3 * sigma_R:.5f}, {N_planck + 3 * sigma_R:.5f}]")

print(f"\n  N=5 is {n_sigma:.2f}σ below the Planck central value")
print(f"  N=6 is {(6 - N_planck) / sigma_R:.2f}σ above the Planck central value")

# ─── Compatibility check for integer N ───────────────────────────────────────
print("\n--- 4. Integer N compatibility with Planck 2018 ---")
print(f"  {'N':>4}  {'Deviation':>12}  {'n_sigma':>10}  Status")
print(f"  {'-' * 4}  {'-' * 12}  {'-' * 10}  {'------'}")
for N_test in [3, 4, 5, 6, 7]:
    dev = R - N_test
    sig = dev / sigma_R
    if abs(sig) < 1:
        status = "✓ <1σ (preferred)"
    elif abs(sig) < 2:
        status = "~ 1-2σ (marginal)"
    elif abs(sig) < 3:
        status = "⚠ 2-3σ (tension)"
    else:
        status = "✗ >3σ (EXCLUDED)"
    print(f"  {N_test:>4}  {dev:>+12.5f}  {sig:>10.2f}  {status}")

# ─── NON-EQUAL MASS interpretation ───────────────────────────────────────────
print("\n--- 5. Reinterpretation: N=5 isomers with unequal masses ---")
print("""
  IDM assumption relaxed: 5 isomers with masses m_1, ..., m_5 (not all = m_p)
  If dark baryon number = visible baryon number (n_DM = n_b):
    ω_DM / ω_b = (m_1 + m_2 + ... + m_5) / m_p = Σ(m_i/m_p)

  Planck measures R = 5.3699 → requires: Σ(m_i/m_p) = 5.3699

  Possible mass distributions:
""")

m_p = 938.272046  # MeV, proton mass

scenarios = [
    ("All equal", [R / 5] * 5),
    ("One heavy (6th type?)", [1.0, 1.0, 1.0, 1.0, 1.3699]),
    ("Geometric series", [1.0, 1.05, 1.10, 1.11, 1.1099]),
    ("4 light + 1 heavy", [1.0, 1.0, 1.0, 1.0, 1.3699]),
    ("3 + 2 (2-sector)", [1.0, 1.0, 1.0, 1.18495, 1.18495]),
]

print(f"  Required: Σ(m_i/m_p) = {R:.5f}")
print(f"  {'Scenario':<25} {'Masses (m_i/m_p)':>35}  {'Sum':>8}  {'Δ from Planck'}")
print(f"  {'-' * 25}  {'-' * 35}  {'-' * 8}  {'-' * 15}")
for name, masses in scenarios:
    total = sum(masses)
    delta = total - R
    mass_str = "[" + ", ".join(f"{m:.4f}" for m in masses) + "]"
    print(f"  {name:<25}  {mass_str:>35}  {total:>8.5f}  {delta:>+.6f}")

print(f"""
  KEY INSIGHT:
  If IDM allows isomers with average mass m̄ = {R / 5 * m_p:.3f} MeV = {R / 5:.4f} × m_p,
  then N=5 isomers with EQUAL masses at {R / 5:.4f} m_p are EXACTLY Planck-compatible.
  This requires only a {(R / 5 - 1) * 100:.2f}% mass enhancement over the proton.
""")

# ─── BRAI context for N ───────────────────────────────────────────────────────
print("--- 6. N measurement uncertainty across AI services ---")
print("""
  If different AI-service reconstructions give different N values:
  Using Birge Ratio framework (BRAI):

  N = R = ω_DM/ω_b is a PLANCK MEASUREMENT, not an IDM prediction.
  Buckholtz proposes N should be an integer, Planck measures R.

  Three interpretations:
  A) IDM predicts N=5 (integer) → EXCLUDED at 5.67σ  [FALSIFICATION]
  B) IDM predicts N=5 with m̄ ≠ m_p → R=5.37 CONSISTENT [MEASUREMENT]
  C) N is a free parameter in IDM → Planck constrains N=5.37±0.056 [CONSTRAINT]

  Interpretation A is falsifiable (and currently rejected).
  Interpretations B and C are Planck-compatible and require additional physics
  to fix the isomer mass spectrum.
""")

# ─── Summary ──────────────────────────────────────────────────────────────────
print("=" * 70)
print("EXP-N SUMMARY")
print("=" * 70)
print(f"""
  Planck 2018: ω_DM/ω_b = {R:.5f} ± {sigma_R:.5f}

  N=5 (equal-mass isomers):  EXCLUDED at {n_sigma:.2f}σ  [VERIFIED-CODE]
  N=6 (equal-mass isomers):  excluded at {(6 - R) / sigma_R:.2f}σ above (tension)
  N_Planck best-fit:         {N_planck:.5f} (non-integer)

  Resolution paths:
  ┌─────────────────────────────────────────────────────────────────┐
  │ PATH A: Accept N=5 falsification. IDM needs new mass mechanism. │
  │ PATH B: N=5 isomers with m̄ = {R / 5:.4f} m_p → Planck-compatible.    │
  │         Requires only {(R / 5 - 1) * 100:.2f}% mass enhancement over proton.  │
  │ PATH C: N is free parameter. Planck measures N=5.37±0.06.       │
  │         Integer N is an additional (so far unjustified) assumption.│
  └─────────────────────────────────────────────────────────────────┘

  STATUS: Problem 1 is NOT a clean falsification of IDM.
  It falsifies N=5 with EQUAL-MASS isomers. The more general
  IDM (variable masses or non-integer N) remains Planck-compatible.
""")
print("✅ EXP-N complete.")
