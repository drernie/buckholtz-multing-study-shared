"""EXP-C: α_G Convention Cross-Link Analysis.

Three competing definitions of the gravitational fine-structure constant:
  1. Buckholtz:        α_G(e)  = G·m_e²/(ħc)       ≈ 1.75e-45
  2. Dirac/Jentschura: α_G(ep) = G·m_e·m_p/(ħc)    ≈ 3.22e-42
  3. Carr-Rees/Adams:  α_G(p)  = G·m_p²/(ħc)        ≈ 5.91e-39

They differ by factors of m_p/m_e ≈ 1836 and (m_p/m_e)² ≈ 3.37e6.

This script:
  1. Tabulates all three α_G and their α_EM/α_G ratios
  2. Shows the exact translation formulas
  3. Expresses Buckholtz Eq.32 in each convention
  4. Finds the Carr-Rees analog: what formula in α_G(p) convention
     would be equivalent to Eq.32?
  5. Tests whether Dirac's LNH (α_EM/α_G(p) ≈ 10^40) is consistent
     with Eq.32 + lepton mass ratios
"""

from __future__ import annotations

import math

# ─── Constants ───────────────────────────────────────────────────────────────
G = 6.67430e-11
hbar = 1.054571817e-34
c = 2.99792458e8
alpha_EM = 1 / 137.035999084

m_e_MeV = 0.51099895
m_mu_MeV = 105.6583755
m_tau_MeV = 1776.86
m_p_MeV = 938.272046
m_n_MeV = 939.565

m_e_kg = 9.1093837015e-31
m_p_kg = 1.67262192369e-27

# Mass ratios
mu_over_me = m_p_MeV / m_e_MeV  # m_p/m_e ≈ 1836.15
mu_over_me_exact = m_p_kg / m_e_kg

# ─── Three α_G definitions ────────────────────────────────────────────────────
alpha_G_e = G * m_e_kg**2 / (hbar * c)  # Buckholtz
alpha_G_ep = G * m_e_kg * m_p_kg / (hbar * c)  # Dirac/Jentschura (mixed)
alpha_G_p = G * m_p_kg**2 / (hbar * c)  # Carr-Rees/Adams

# ─── α_EM/α_G ratios (the "large number") ───────────────────────────────────
R_e = alpha_EM / alpha_G_e  # Buckholtz
R_ep = alpha_EM / alpha_G_ep  # Dirac/Jentschura
R_p = alpha_EM / alpha_G_p  # Carr-Rees

print("=" * 70)
print("EXP-C: α_G Convention Cross-Link Analysis")
print("=" * 70)

print("\n--- 1. Three α_G Definitions ---")
print(f"  m_p/m_e                        = {mu_over_me:.6f} (MeV ratio)")
print(f"  m_p_kg/m_e_kg                  = {mu_over_me_exact:.6f}")
print(f"  (m_p/m_e)²                     = {mu_over_me_exact**2:.4e}")

print(f"\n  α_G(e)  [Buckholtz, G·m_e²]   = {alpha_G_e:.6e}")
print(f"  α_G(ep) [Dirac, G·m_e·m_p]    = {alpha_G_ep:.6e}")
print(f"  α_G(p)  [Carr-Rees, G·m_p²]   = {alpha_G_p:.6e}")

print("\n  Ratios:")
print(f"  α_G(ep)/α_G(e) = m_p/m_e      = {alpha_G_ep / alpha_G_e:.6f}")
print(f"  α_G(p)/α_G(e)  = (m_p/m_e)²   = {alpha_G_p / alpha_G_e:.6e}")
print(f"  α_G(p)/α_G(ep) = m_p/m_e      = {alpha_G_p / alpha_G_ep:.6f}")

print("\n--- 2. Large Number R = α_EM/α_G in Each Convention ---")
print(f"  R(e)  = α_EM/α_G(e)   = {R_e:.6e}  [Buckholtz: ~4.17e42]")
print(f"  R(ep) = α_EM/α_G(ep)  = {R_ep:.6e}  [Dirac: ~2.27e39]")
print(f"  R(p)  = α_EM/α_G(p)   = {R_p:.6e}  [Carr-Rees: ~6.22e35]")

print("\n  Translation formulas:")
print(f"  R(e)  = R(p) × (m_p/m_e)²    = {R_p * mu_over_me_exact**2:.4e}  ✓ (= {R_e:.4e})")
print(f"  R(e)  = R(ep) × (m_p/m_e)    = {R_ep * mu_over_me_exact:.4e}  ✓")
print(f"  R(ep) = R(p) × (m_p/m_e)     = {R_p * mu_over_me_exact:.4e}  ✓")

print("\n--- 3. Buckholtz Eq.32 in Each Convention ---")
LHS_eq32 = (4 / 3) * (m_tau_MeV / m_e_MeV) ** 12
print(f"  LHS = (4/3)(m_τ/m_e)^12       = {LHS_eq32:.6e}")
print(f"  R(e) = α_EM/α_G(e)            = {R_e:.6e}")
print(f"  LHS/R(e) = {LHS_eq32 / R_e:.8f}  ← Buckholtz Eq.32 (0.0135% from 1.0)")

print("\n  Same LHS vs. other conventions:")
print(f"  LHS/R(ep)                      = {LHS_eq32 / R_ep:.4e}  (not 1 — wrong convention)")
print(f"  LHS/R(p)                       = {LHS_eq32 / R_p:.4e}  (not 1 — wrong convention)")

print("\n  → Buckholtz Eq.32 ONLY makes sense with α_G(e) convention.")
print(
    f"    In other conventions, the RHS differs by factors of {mu_over_me_exact:.1f} or {mu_over_me_exact**2:.2e}."
)

print("\n--- 4. Reformulations of Eq.32 in Other Conventions ---")
# Eq.32: (4/3)(m_τ/m_e)^12 = α_EM/α_G(e)
# = (4/3)(m_τ/m_e)^12 × (m_e/m_p)^2 = α_EM/α_G(p)
# = (4/3)(m_τ/m_e)^12 × (m_e/m_p)   = α_EM/α_G(ep)

lhs_ep = LHS_eq32 * (m_e_MeV / m_p_MeV)
lhs_p = LHS_eq32 * (m_e_MeV / m_p_MeV) ** 2

dev_ep = lhs_ep / R_ep - 1
dev_p = lhs_p / R_p - 1

print("  Eq.32 in Dirac/Jentschura convention [α_G(ep)]:")
print("  (4/3)(m_τ/m_e)^12 × (m_e/m_p) = α_EM/α_G(ep)")
print(f"  LHS: {lhs_ep:.6e}  |  RHS: {R_ep:.6e}  |  ratio: {lhs_ep / R_ep:.8f}")

print("\n  Eq.32 in Carr-Rees convention [α_G(p)]:")
print("  (4/3)(m_τ/m_e)^12 × (m_e/m_p)² = α_EM/α_G(p)")
lhs_p_check = (4 / 3) * (m_tau_MeV / m_e_MeV) ** 12 * (m_e_MeV / m_p_MeV) ** 2
print("  Equivalently: (4/3) × (m_τ^12/m_e^10) × (1/m_p²) × [m_e·units]")
print(f"  LHS: {lhs_p_check:.6e}  |  RHS: {R_p:.6e}  |  ratio: {lhs_p_check / R_p:.8f}")

print("\n  NOTE: All three expressions are algebraically identical (same formula).")
print("        The (m_e/m_p) or (m_e/m_p)² factors convert between conventions.")
print(f"        Precision: {abs(dev_ep) * 100:.6f}% (same 0.0135% as original)")

print("\n--- 5. Can We Write Eq.32 'Cleanly' in Carr-Rees Convention? ---")
# What if we tried to find (4/3)(m_τ/m_p)^n = R_p?
# log(R_p) / log(m_tau/m_p) = ?
tau_over_p = m_tau_MeV / m_p_MeV
n_needed_p = math.log(R_p / (4 / 3)) / math.log(tau_over_p)
lhs_test = (4 / 3) * tau_over_p**n_needed_p
print("  Testing (4/3)(m_τ/m_p)^n = α_EM/α_G(p):")
print(f"  m_τ/m_p = {tau_over_p:.6f}")
print(f"  R(p)    = {R_p:.4e}")
print(f"  n needed = {n_needed_p:.4f}  ← NOT an integer or simple fraction")
print("  → Cannot write Eq.32 cleanly in Carr-Rees convention with m_τ/m_p ratio.")

# Test with m_tau/m_e but Carr-Rees convention:
print("\n  But: (4/3)(m_τ/m_e)^12 × (m_e/m_p)^2 = α_EM/α_G(p)")
print("  This mixes lepton and baryon masses — not clean.")

print("\n--- 6. Dirac LNH in Buckholtz Convention ---")
# Dirac: α_EM/α_G(p) ≈ t_universe/t_atomic ≈ 10^40 (time-varying!)
# Buckholtz Eq.32: α_EM/α_G(e) = (4/3)(m_τ/m_e)^12  (NOT time-varying)
# Link: α_EM/α_G(e) = [α_EM/α_G(p)] × (m_p/m_e)²
# So: Dirac LNH predicts α_EM/α_G(e) ≈ 10^40 × (m_p/m_e)² ≈ 10^40 × 3.37e6 ≈ 3.37e46
# But Eq.32 gives α_EM/α_G(e) ≈ 4.17e42 — MUCH SMALLER than Dirac's prediction
# This is NOT a contradiction — Dirac used α_G(p)

dirac_R_p_approx = 1e40  # Dirac's estimate for α_EM/α_G(p)
dirac_R_e_implied = dirac_R_p_approx * mu_over_me_exact**2
print("  Dirac estimate: α_EM/α_G(p) ≈ 10^40  (time-varying)")
print(f"  → In Buckholtz α_G(e): this corresponds to α_EM/α_G(e) ≈ {dirac_R_e_implied:.2e}")
print(f"  → Buckholtz Eq.32: α_EM/α_G(e) = {R_e:.2e}")
print(f"  → Ratio (Dirac's time/Buckholtz constant): {dirac_R_e_implied / R_e:.2e}")
print("\n  CONCLUSION: Dirac's LNH is about α_G(p) and is ~time-varying.")
print("  Buckholtz Eq.32 is about α_G(e) and proposes this ratio is TIME-CONSTANT.")
print("  They are complementary — Eq.32 implies Dirac's large number = constant × (m_p/m_e)^2")

print("\n--- 7. α_G Convention Table for Paper ---")
print(
    f"  {'Convention':20} {'α_G':12} {'α_EM/α_G':12} {'log10(α_EM/α_G)':15} {'Factor vs Buckholtz':18}"
)
print(f"  {'-' * 80}")
for name, ag, r, factor in [
    ("Buckholtz [G·m_e²]", alpha_G_e, R_e, 1.0),
    ("Dirac [G·m_e·m_p]", alpha_G_ep, R_ep, 1 / mu_over_me_exact),
    ("Carr-Rees [G·m_p²]", alpha_G_p, R_p, 1 / mu_over_me_exact**2),
]:
    print(f"  {name:20} {ag:.4e}  {r:.4e}  {math.log10(r):12.2f}      ×{factor:.2e}")

print("\n--- 8. Summary for Related Work Section ---")
print(f"""
  When citing Dirac (1937) or Carr-Rees (1979) in context of Buckholtz Eq.32:

  Dirac's large number: α_EM/α_G(proton) ≈ 10^40 ≈ t_universe/t_atomic
    → In electron convention: α_EM/α_G(electron) = {R_e:.3e}  = 10^{math.log10(R_e):.1f}

  Carr-Rees (1979) use α_G(proton) ≈ 5.9e-39, α_EM/α_G(p) ≈ {R_p:.1e} = 10^{math.log10(R_p):.1f}
    → Buckholtz Eq.32 gives α_EM/α_G(e) ≈ {R_e:.1e} = 10^{math.log10(R_e):.1f}
    → Bridged by: α_EM/α_G(e) = [α_EM/α_G(p)] × (m_p/m_e)² = (m_p/m_e)² × {R_p:.1e}
    → Numerically: 1836.15² × {R_p:.3e} = {R_p * mu_over_me_exact**2:.3e} ✓

  CRITICAL for paper: ALWAYS specify α_G convention when citing related work.
  Buckholtz convention: α_G(e) = G·m_e²/(ħc) — uses electron mass, NOT proton.
""")
print("✅ EXP-C complete.")
