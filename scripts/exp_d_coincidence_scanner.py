"""EXP-D: Systematic Mass-Coupling Coincidence Scanner.

Tests ALL combinations of:
  C × (m_i / m_j)^n = coupling_ratio

across the full particle physics mass spectrum and all known coupling constants.

Key question: Is (4/3)(m_τ/m_e)^12 = α_EM/α_G the MOST PRECISE coincidence
of this type in all of particle physics? Or are there better ones?

Coverage:
  - 15 particle masses (leptons, quarks, hadrons, bosons)
  - ~20 rational prefactors
  - exponents n = 1..24 (integer and half-integer)
  - 8 coupling constant ratios

Output: Top 30 hits sorted by |ratio-1|, with look-elsewhere context.
"""

from __future__ import annotations

import math
from itertools import combinations

# ─── Physical Constants ───────────────────────────────────────────────────────
G = 6.67430e-11
hbar = 1.054571817e-34
c = 2.99792458e8
m_e_kg = 9.1093837015e-31
alpha_EM = 1 / 137.035999084

alpha_G_e = G * m_e_kg**2 / (hbar * c)  # Buckholtz convention: G*m_e^2/hbar*c

m_p_kg = 1.67262192369e-27  # proton mass
alpha_G_p = G * m_p_kg**2 / (hbar * c)  # Carr-Rees convention
alpha_G_ep = G * m_e_kg * m_p_kg / (hbar * c)  # Dirac/Jentschura convention

sin2_thetaW = 0.23122  # sin²θ_W (MS-bar at m_Z)
alpha_s_mZ = 0.1179  # α_s at m_Z
GF_GeV2 = 1.1663788e-5  # G_Fermi in GeV^-2 (dimensionful — not used as-is)

# ─── Particle Masses (MeV) ────────────────────────────────────────────────────
MASSES = {
    # Charged leptons
    "e": 0.51099895,
    "μ": 105.6583755,
    "τ": 1776.86,
    # Quarks (MS-bar or pole as appropriate; PDG 2024)
    "u": 2.16,  # u quark MS-bar at 2 GeV
    "d": 4.67,  # d quark MS-bar at 2 GeV
    "s": 93.4,  # s quark MS-bar at 2 GeV
    "c": 1270.0,  # c quark pole mass
    "b": 4180.0,  # b quark pole mass
    "t": 172760.0,  # t quark pole mass
    # Gauge bosons
    "W": 80369.2,
    "Z": 91188.0,
    "H": 125200.0,
    # Hadrons
    "p": 938.272,  # proton
    "n": 939.565,  # neutron
    "π±": 139.57039,  # charged pion
}

# ─── Coupling Ratios ─────────────────────────────────────────────────────────
COUPLING_RATIOS = {
    "α_EM/α_G(e)": alpha_EM / alpha_G_e,  # Buckholtz
    "α_EM/α_G(p)": alpha_EM / alpha_G_p,  # Carr-Rees
    "α_EM/α_G(ep)": alpha_EM / alpha_G_ep,  # Dirac/Jentschura
    "α_G(e)/α_EM": alpha_G_e / alpha_EM,
    "1/α_EM": 137.035999084,
    "α_EM": alpha_EM,
    "α_s/α_EM": alpha_s_mZ / alpha_EM,
    "sin²θ_W/α_EM": sin2_thetaW / alpha_EM,
    "α_EM/sin²θ_W": alpha_EM / sin2_thetaW,
    "α_EM/α_s": alpha_EM / alpha_s_mZ,
    "1/sin²θ_W": 1.0 / sin2_thetaW,
    "α_s": alpha_s_mZ,
}

# ─── Prefactors ───────────────────────────────────────────────────────────────
PREFACTORS = {}
for p in range(1, 7):
    for q in range(1, 7):
        if math.gcd(p, q) == 1:
            PREFACTORS[f"{p}/{q}" if q != 1 else str(p)] = p / q
# Also add pi-related
PREFACTORS["π"] = math.pi
PREFACTORS["π/2"] = math.pi / 2
PREFACTORS["2π"] = 2 * math.pi
PREFACTORS["4π/3"] = 4 * math.pi / 3  # sphere volume (unit radius) / 1

# ─── Exponents ────────────────────────────────────────────────────────────────
EXPONENTS = list(range(1, 25)) + [0.5, 1.5, 2.5, 3.5]

# ─── Buckholtz Eq.32 reference ───────────────────────────────────────────────
EQ32_DEVIATION = abs((4 / 3) * (MASSES["τ"] / MASSES["e"]) ** 12 / (alpha_EM / alpha_G_e) - 1.0)

# ─── SCAN ─────────────────────────────────────────────────────────────────────
hits: list[dict] = []
total_tested = 0

mass_keys = list(MASSES.keys())
mass_pairs = [(a, b) for a, b in combinations(mass_keys, 2)]  # all unordered pairs

for m_a_name, m_b_name in mass_pairs:
    m_a = MASSES[m_a_name]
    m_b = MASSES[m_b_name]
    ratios_to_try = [(m_a / m_b, f"{m_a_name}/{m_b_name}"), (m_b / m_a, f"{m_b_name}/{m_a_name}")]

    for ratio_val, ratio_name in ratios_to_try:
        for exp in EXPONENTS:
            power_val = ratio_val**exp
            for pf_name, pf in PREFACTORS.items():
                lhs = pf * power_val
                for cr_name, cr_val in COUPLING_RATIOS.items():
                    total_tested += 1
                    frac = lhs / cr_val
                    dev = abs(frac - 1.0)
                    if dev < 0.005:  # within 0.5%
                        hits.append(
                            {
                                "prefactor": pf_name,
                                "mass_ratio": ratio_name,
                                "exponent": exp,
                                "coupling": cr_name,
                                "LHS": lhs,
                                "RHS": cr_val,
                                "LHS/RHS": frac,
                                "deviation": dev,
                                "dev_pct": dev * 100,
                                "is_eq32": (
                                    pf_name == "4/3"
                                    and ratio_name == "τ/e"
                                    and exp == 12
                                    and cr_name == "α_EM/α_G(e)"
                                ),
                            }
                        )

# ─── Sort and display ─────────────────────────────────────────────────────────
hits.sort(key=lambda h: h["deviation"])

print("=" * 75)
print("EXP-D: Systematic Mass-Coupling Coincidence Scanner")
print("=" * 75)
print(f"\n  Total combinations tested: {total_tested:,}")
print(f"  Mass pairs:               {len(mass_pairs)} pairs × 2 directions = {2 * len(mass_pairs)}")
print(f"  Prefactors:               {len(PREFACTORS)}")
print(f"  Exponents:                {len(EXPONENTS)}")
print(f"  Coupling ratios:          {len(COUPLING_RATIOS)}")
print(f"  Hits within 0.5%:         {len(hits)}")
print(f"\n  Buckholtz Eq.32 deviation: {EQ32_DEVIATION * 100:.4f}%")

print(f"\n{'#':3} {'Formula':55} {'LHS/RHS':10} {'Dev%':8} {'Eq32?':6}")
print("-" * 95)
for i, h in enumerate(hits[:35], 1):
    formula = f"{h['prefactor']}×({h['mass_ratio']})^{h['exponent']} = {h['coupling']}"
    eq32_mark = "★ EQ32" if h["is_eq32"] else ""
    print(f"{i:3}. {formula:55} {h['LHS/RHS']:10.6f}  {h['dev_pct']:7.4f}%  {eq32_mark}")

# ─── Look-elsewhere summary ────────────────────────────────────────────────
print("\n--- Look-Elsewhere Analysis ---")
better_than_eq32 = [h for h in hits if h["deviation"] < EQ32_DEVIATION and not h["is_eq32"]]
eq32_rank = next((i + 1 for i, h in enumerate(hits) if h["is_eq32"]), None)

print(f"  Eq.32 rank among all hits:   #{eq32_rank}")
print(f"  Hits MORE precise than Eq.32: {len(better_than_eq32)}")
if better_than_eq32:
    print(f"\n  Formulas more precise than Eq.32 ({EQ32_DEVIATION * 100:.4f}%):")
    for h in better_than_eq32[:10]:
        formula = f"{h['prefactor']}×({h['mass_ratio']})^{h['exponent']} = {h['coupling']}"
        print(f"    {formula}  →  dev={h['dev_pct']:.5f}%")
else:
    print("  ✓ NO formula in this search space beats Eq.32 in precision!")

# ─── Expected hits from noise ─────────────────────────────────────────────
threshold = EQ32_DEVIATION
expected_noise = total_tested * 2 * threshold  # uniform distribution
print("\n--- Statistical Context ---")
print(
    f"  Under null (coincidence), expected hits within ±{threshold * 100:.4f}%: {expected_noise:.1f}"
)
actual_better = len(better_than_eq32) + 1  # including eq32 itself
print(f"  Actual hits within ±{threshold * 100:.4f}%: {actual_better}")
if actual_better <= max(1, expected_noise * 2):
    print("  → Eq.32 is consistent with being the best genuine coincidence")
    print("     (observed ≤ 2× expected from noise)")
else:
    print(
        f"  → Multiple candidates at this precision level (expected noise = {expected_noise:.1f})"
    )

# ─── Category breakdown ───────────────────────────────────────────────────
print("\n--- Hits by Mass Category (within 0.5%) ---")
categories = {}
for h in hits:
    cat_parts = h["mass_ratio"].split("/")
    cat = f"{cat_parts[0]}/{cat_parts[1]}"
    categories[cat] = categories.get(cat, 0) + 1
for cat, cnt in sorted(categories.items(), key=lambda x: -x[1])[:10]:
    print(f"  {cat:15}: {cnt} hits")

print("\n✅ EXP-D complete.")
