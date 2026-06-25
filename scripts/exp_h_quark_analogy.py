"""EXP-H: Quark Analogy — Does Buckholtz Eq.32 Pattern Hold for Quarks?

Buckholtz Eq.32 (leptons):
  (4/3)(m_τ/m_e)^12 = α_EM/α_G   where α_G = G·m_e²/(ħc)

If E=12 reflects G₂ structure (leptons in G₂ sector of E₈),
and quarks live in F₄ sector (48 roots), then the quark analog might be:

  C × (m_top/m_up)^E_quark = α_s/α_G_quark ?

or some other mass ratio combination.

This experiment tests:
  1. Direct analogy: (4/3)(m_t/m_u)^12 vs α_s/α_G (lepton convention)
  2. F₄ root count: (4/3)(m_t/m_u)^48 vs same RHS
  3. Quark convention for α_G: G·m_p²/(ħc) [Carr-Rees]
  4. Family scan: all 6 quarks, all sphere prefactors, integer exponents 1-24
  5. Cross-sector: mixed quark-lepton formulas

If ANY quark formula matches with deviation <0.1%, it STRENGTHENS E₈ hypothesis.
If NONE matches, it falsifies the E₈/F₄×G₂ route (Route 3).
"""

from __future__ import annotations

import math

# ─── Constants ────────────────────────────────────────────────────────────────
G = 6.67430e-11
hbar = 1.054571817e-34
c = 2.99792458e8
m_e_kg = 9.1093837015e-31
m_p_kg = 1.67262192369e-27
alpha_EM = 1 / 137.035999084

# Quark masses (PDG 2024, MS-bar at 2 GeV for light, pole for heavy)
# MeV
m_u = 2.16  # up   (2 GeV MS-bar)
m_d = 4.67  # down (2 GeV MS-bar)
m_s = 93.4  # strange (2 GeV MS-bar)
m_c = 1270.0  # charm (pole ≈ 1.67 GeV, or MS-bar at m_c ≈ 1270)
m_b = 4180.0  # bottom (pole ≈ 4.78 GeV, or MS-bar at m_b ≈ 4180)
m_t = 172_690.0  # top (pole mass, PDG 2024: 172.69 GeV)

# Lepton masses (PDG 2024)
m_e = 0.51099895
m_mu = 105.6583755
m_tau = 1776.86

# α_G conventions
alpha_G_e = G * m_e_kg**2 / (hbar * c)  # Buckholtz: G·m_e²/ħc ≈ 1.75e-45
alpha_G_p = G * m_p_kg**2 / (hbar * c)  # Carr-Rees: G·m_p²/ħc ≈ 5.91e-39
alpha_G_ep = G * m_e_kg * m_p_kg / (hbar * c)  # Dirac: G·m_e·m_p/ħc ≈ 3.22e-42

# Strong coupling
alpha_s_mZ = 0.1180  # α_s(m_Z) PDG 2024
alpha_s_1GeV = 0.400  # α_s(1 GeV) approx (non-perturbative regime edge)
alpha_s_tau = 0.33  # α_s(m_τ) ≈ 0.33 (approximate)

print("=" * 70)
print("EXP-H: Quark Analogy Test for Buckholtz Eq.32 Pattern")
print("=" * 70)

print("\n  Quark masses (PDG 2024):")
quarks = [("u", m_u), ("d", m_d), ("s", m_s), ("c", m_c), ("b", m_b), ("t", m_t)]
for name, m in quarks:
    print(f"    m_{name} = {m:.4f} MeV")

print("\n  α_G conventions:")
print(f"    α_G(e)  = {alpha_G_e:.4e}   → α_EM/α_G(e)  = {alpha_EM / alpha_G_e:.4e}")
print(f"    α_G(ep) = {alpha_G_ep:.4e}  → α_EM/α_G(ep) = {alpha_EM / alpha_G_ep:.4e}")
print(f"    α_G(p)  = {alpha_G_p:.4e}   → α_EM/α_G(p)  = {alpha_EM / alpha_G_p:.4e}")

print("\n  Strong coupling:")
print(f"    α_s(m_Z) = {alpha_s_mZ:.4f} → α_s/α_G(e) = {alpha_s_mZ / alpha_G_e:.4e}")

# ─── 1. Direct analogy: same formula for top/up ──────────────────────────
print("\n--- 1. Direct Lepton Analogy: (4/3)(m_q_heavy / m_q_light)^12 ---")
print(
    f"  Buckholtz reference: (4/3)(m_τ/m_e)^12 / (α_EM/α_G(e)) = {(4 / 3) * (m_tau / m_e) ** 12 / (alpha_EM / alpha_G_e):.6f}"
)

print("\n  Testing C=4/3, E=12 for all quark pairs, RHS = α_EM/α_G(e):")
R_lep = alpha_EM / alpha_G_e
for hn, hm in [("t", m_t), ("b", m_b), ("c", m_c)]:
    for ln, lm in [("u", m_u), ("d", m_d), ("s", m_s)]:
        ratio = hm / lm
        lhs = (4 / 3) * ratio**12
        dev = (lhs / R_lep - 1) * 100
        if abs(dev) < 50:  # show if within 50%
            print(f"    (4/3)(m_{hn}/m_{ln})^12 / R = {lhs / R_lep:.4f}  ({dev:+.2f}%)")

# ─── 2. F₄ root count: exponent = 48 ───────────────────────────────────
print("\n--- 2. F₄ Root Count (E_quark = 48): (4/3)(m_t/m_u)^48 ---")
print("  F₄ = Aut(J₃(𝕆)) has 48 positive roots (96 total non-zero roots)")
print("  If quarks live in F₄ sector: analog exponent = 48")

for hn, hm in [("t", m_t), ("b", m_b)]:
    for ln, lm in [("u", m_u), ("d", m_d)]:
        ratio = hm / lm
        try:
            lhs_48 = (4 / 3) * ratio**48
        except OverflowError:
            lhs_48 = float("inf")
        dev = (lhs_48 / R_lep - 1) * 100 if not math.isinf(lhs_48) else float("inf")
        print(f"  (4/3)(m_{hn}/m_{ln})^48 = {lhs_48:.3e}  vs R = {R_lep:.3e}")
        print(f"  → Ratio = {lhs_48 / R_lep:.3e}  ({dev:+.3e}%)")

# ─── 3. With α_s instead of α_EM ────────────────────────────────────────
print("\n--- 3. Strong Coupling Analog: C×(m_t/m_u)^E = α_s/α_G ---")
print("  Using α_s(m_Z) = 0.1180 and various α_G conventions:")

for ag_name, ag_val in [("α_G(e)", alpha_G_e), ("α_G(ep)", alpha_G_ep), ("α_G(p)", alpha_G_p)]:
    R_s = alpha_s_mZ / ag_val
    print(f"\n  α_s/{ag_name} = {R_s:.4e}  (log₁₀ = {math.log10(R_s):.2f})")
    for hn, hm in [("t", m_t), ("b", m_b), ("c", m_c)]:
        for ln, lm in [("u", m_u), ("d", m_d)]:
            r_mass = hm / lm
            log_r = math.log10(r_mass)
            log_R = math.log10(R_s)
            # Exact exponent for C=4/3
            E_exact = (log_R - math.log10(4 / 3)) / log_r
            E_int = round(E_exact)
            dist = abs(E_exact - E_int)
            if dist < 0.05:  # near-integer exponent
                lhs = (4 / 3) * r_mass**E_int
                dev = (lhs / R_s - 1) * 100
                print(
                    f"    (4/3)(m_{hn}/m_{ln})^{E_int}  E*={E_exact:.3f}  dev={dev:+.3f}%  *** NEAR-INTEGER ***"
                )

# ─── 4. Full sphere-family grid for quarks (top/up) ──────────────────────
print("\n--- 4. Full Sphere-Family Grid: (n+1)/n × (m_t/m_u)^E = α_s/α_G(e) ---")
R_su = alpha_s_mZ / alpha_G_e
r_tu = m_t / m_u
log_r_tu = math.log10(r_tu)
print(f"  m_t/m_u = {r_tu:.2f},  α_s/α_G(e) = {R_su:.4e}")
print("  Searching for (n, E) with |(n+1)/n × (m_t/m_u)^E - R| < 5%:")
hits = []
for n in range(1, 14):
    pf = (n + 1) / n
    for E in range(1, 13):
        lhs = pf * r_tu**E
        dev = (lhs / R_su - 1) * 100
        if abs(dev) < 5:
            hits.append((n, E, pf, lhs, dev))

hits.sort(key=lambda x: abs(x[-1]))
if hits:
    print(f"  Found {len(hits)} hits:")
    for n, E, _pf, _lhs, dev in hits:
        print(f"    n={n}, E={E}: {n + 1}/{n} × (m_t/m_u)^{E} dev={dev:+.2f}%")
else:
    print("  No hits within 5%.")

# ─── 5. Cross-sector: lepton × quark mixed formulas ─────────────────────
print("\n--- 5. Cross-Sector Mixed Formulas ---")
print("  Testing: (m_τ/m_e)^a × (m_t/m_u)^b = α_EM/α_G(e) or α_s/α_G(e)")
print("  for integer a+b = 12 (keeping total exponent = E = 12)")

r_te = m_tau / m_e
r_tu = m_t / m_u

for a in range(0, 13):
    b = 12 - a
    lhs = r_te**a * r_tu**b
    for R_name, R_val in [("α_EM/α_G(e)", R_lep), ("α_s/α_G(e)", R_su)]:
        dev = (lhs / R_val - 1) * 100
        if abs(dev) < 1.0:
            print(
                f"    (m_τ/m_e)^{a} × (m_t/m_u)^{b} / {R_name} = {lhs / R_val:.6f}  ({dev:+.4f}%)"
            )

print("\n--- 6. Summary ---")
print(f"""
  Key question: Does the Buckholtz pattern generalize to quarks?

  Results:
  1. Direct analogy (4/3)(m_t/m_u)^12 ≠ α_EM/α_G (wrong by many orders of mag)
     → Quark masses span different range than lepton masses

  2. F₄ root count E=48 gives astronomical LHS >> RHS
     → F₄/E=48 quark analog does NOT work with these mass ratios

  3. α_s analog: {len(hits)} near-integer solutions found in sphere-family grid

  4. Cross-sector: (m_τ/m_e)^a × (m_t/m_u)^(12-a) — check output above

  Interpretation:
  - If NO quark analog exists → Eq.32 is lepton-specific (G₂ sector only)
  - If α_s analog found → supports E₈ → F₄×G₂ routing
  - The mass hierarchy m_t/m_u ≈ {m_t / m_u:.0f} vs m_τ/m_e ≈ {m_tau / m_e:.0f}
    makes a direct structural analog unlikely with the same exponent.
""")
print("✅ EXP-H complete.")
