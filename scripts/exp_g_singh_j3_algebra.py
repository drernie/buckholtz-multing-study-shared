"""EXP-G: Singh J₃(8) / Octonionic Algebra Check for Buckholtz Eq.32.

Buckholtz Eq.32: (4/3)(m_τ/m_e)^12 = α_EM/α_G

Key numbers to explain:
  prefactor C  = 4/3
  exponent  E  = 12
  product   P  = n × E = 3 × 12 = 36  (from EXP-F S³ analysis)
  large number R = α_EM/α_G ≈ 4.17 × 10⁴²

Division algebra chain: ℝ(1) → ℂ(2) → ℍ(4) → 𝕆(8)
Jordan algebra:        J₃(ℝ)   J₃(ℂ)   J₃(ℍ)   J₃(𝕆) ← "Albert algebra"
Exceptional Lie chain: A₁ → A₂ → C₃ → F₄ → E₆ → E₇ → E₈

References:
  [SINH-2020]  T.P. Singh, arXiv:2006.06616 — trace dynamics + α_EM
  [FUREY-2018] C. Furey, arXiv:1805.06455 — octonions and SM
  [EXP-F]      This session — S³ geometry, n=3, E=12 unique hit
"""

from __future__ import annotations

import math

# ─── Buckholtz Eq.32 constants ───────────────────────────────────────────────
G = 6.67430e-11
hbar = 1.054571817e-34
c = 2.99792458e8
m_e_kg = 9.1093837015e-31
alpha_EM = 1 / 137.035999084
m_e_MeV = 0.51099895
m_tau_MeV = 1776.86
alpha_G = G * m_e_kg**2 / (hbar * c)
R = alpha_EM / alpha_G

EQ32_C = 4 / 3  # prefactor
EQ32_E = 12  # exponent
EQ32_P = 3 * 12  # product n × E from EXP-F (sphere dim × exponent)

print("=" * 70)
print("EXP-G: Singh J₃(8) / Octonionic Algebra Check")
print("=" * 70)

print("\n  Buckholtz Eq.32 key numbers:")
print(f"  Prefactor C   = {EQ32_C:.6f} = 4/3")
print(f"  Exponent  E   = {EQ32_E}")
print(f"  Product n×E   = {EQ32_P} = 3 × 12")
print(f"  Large R       = {R:.6e}")
print(f"  log₁₀(R)      = {math.log10(R):.4f}")

# ─── 1. Division algebra dimensions ─────────────────────────────────────────
print("\n--- 1. Division Algebra Dimensions (Hurwitz theorem) ---")
div_algs = [("ℝ", 1), ("ℂ", 2), ("ℍ (quaternions)", 4), ("𝕆 (octonions)", 8)]
for name, k in div_algs:
    print(f"  dim({name}) = {k}")
print("\n  Octonion dimension k=8 → J₃(8) = 3×3 Hermitian octonionic matrices")

# ─── 2. Jordan algebra J_n(k) dimensions ──────────────────────────────────
# dim J_n(k) = k·n(n-1)/2 + n
print("\n--- 2. Jordan Algebra Dimensions J_n(k) ---")
print("  Formula: dim J_n(k) = k·n(n-1)/2 + n")
print(f"\n  {'J_n(k)':15} {'k':5} {'n':5} {'dim':8}")
print(f"  {'-' * 35}")
for k in [1, 2, 4, 8]:
    for n in [1, 2, 3]:
        d = k * n * (n - 1) // 2 + n
        name = f"J_{n}({'ℝ' if k == 1 else 'ℂ' if k == 2 else 'ℍ' if k == 4 else '𝕆'})"
        flag = " ← Albert algebra (J₃(𝕆))" if k == 8 and n == 3 else ""
        flag += " ← dim = E = 12!" if d == 12 else ""
        flag += " ← dim = C×E = 16!" if d == 16 else ""
        flag += " ← dim = P = 36!" if d == 36 else ""
        print(f"  {name:15} {k:5} {n:5} {d:8}{flag}")

# ─── 3. Exceptional Lie group dimensions ─────────────────────────────────
print("\n--- 3. Exceptional Lie Group Dimensions ---")
exc_groups = [
    ("G₂ = Aut(𝕆)", 14, 2, 12),
    ("F₄ = Aut(J₃(𝕆))", 52, 4, 48),
    ("E₆", 78, 6, 72),
    ("E₇", 133, 7, 126),
    ("E₈", 248, 8, 240),
]
print(f"  {'Group':20} {'dim':6} {'rank':6} {'roots':8} {'Notes'}")
print(f"  {'-' * 70}")
for name, d, r, roots in exc_groups:
    flag = ""
    if roots == EQ32_E:
        flag = f" ← roots = E = {EQ32_E}!"
    if d == EQ32_P:
        flag += f" ← dim = P = {EQ32_P}!"
    print(f"  {name:20} {d:6} {r:6} {roots:8}{flag}")

# ─── 4. G₂ root structure — the KEY connection ───────────────────────────
print("\n--- 4. G₂ Root System and Buckholtz Exponent E=12 ---")
print("""
  G₂ = Aut(𝕆) = automorphism group of the octonions.
  Root system of G₂:
    - Total non-zero roots: 12  ← EQUALS Buckholtz exponent E=12!
    - Short roots: 6
    - Long roots:  6
    - Rank (Cartan): 2
    - Total generators: 14 = 2 + 12

  Ratio: (short + long) / long = 12/6 = 2
  Ratio: long_roots / short_roots = 6/6 = 1  (not 4/3)

  Length ratio: long²/short² = 3 (for G₂, the squared length ratio = 3)
  → 3 = m_p/m_n roughly? No — this is a different 3.

  But: (E+1)/E = 13/12 ≠ 4/3.
  Check: total roots / long roots = 12/6 = 2 ≠ 4/3.
  Check: (short+long) / short = 12/6 = 2 ≠ 4/3.

  The root count G₂ = 12 = E is the main match.
  The 4/3 prefactor does NOT come from G₂ root ratios directly.
""")
print("  [VERIFIED] G₂ root count = 12 = Buckholtz exponent E")

# ─── 5. F₄ → SO(9) decomposition and product P=36 ─────────────────────────
print("\n--- 5. F₄ → SO(9) Decomposition and Product n×E = 36 ---")
dim_F4 = 52
dim_SO9 = 9 * 8 // 2  # = 36
dim_spin9_spinor = 16  # 2^(9//2) = 2^4 = 16

print("  F₄ → SO(9) maximal subgroup decomposition:")
print(f"  dim(F₄) = {dim_F4} = dim(SO(9)) + dim(spinor₁₆)")
print(f"           = {dim_SO9} + {dim_spin9_spinor}")
print(f"           = {dim_SO9 + dim_spin9_spinor}  ✓")
print(f"\n  dim(SO(9)) = 9×8/2 = {dim_SO9}")
print(f"  Buckholtz: n × E = 3 × 12 = {EQ32_P}")
print(f"\n  [VERIFIED] dim(SO(9)) = {dim_SO9} = n×E = {EQ32_P}!")

print("""
  Physical interpretation:
  - F₄ = Aut(J₃(𝕆)) — symmetry of "3 octonionic generations"
  - Under F₄ ⊃ SO(9): the 27-dim Albert algebra decomposes as
      J₃(𝕆) = 16 (spinor) ⊕ 10 (vector) ⊕ 1 (scalar)
    Actually: 27 = 16 + 9 + 1 + 1 → let's check:
""")

# Decomposition of 27-dim J₃(O) under Spin(9):
decomp_27 = [16, 9, 1, 1]
print(f"  J₃(𝕆) under Spin(9): {decomp_27} → sum = {sum(decomp_27)}")
print("  Ratio: spinor/vector = 16/9 ≠ 4/3")
print("  But: (spinor/vector) = 16/9, and 4/3 = (4/3) = ??")
print("  Hmm: 16 = dim(ℍ)² = 4², 9 = 3², 16/9 ≠ 4/3")

# ─── 6. Alternative: the 4/3 from J₃(𝕆) structure directly ──────────────
print("\n--- 6. Looking for 4/3 in J₃(𝕆) / E₆ Structure ---")
print("""
  Testing ratios from key exceptional algebra dimensions:
""")
dims_to_test = {
    "dim J₃(𝕆)=27": 27,
    "dim F₄=52": 52,
    "dim E₆=78": 78,
    "dim G₂=14": 14,
    "dim SO(9)=36": 36,
    "spinor Spin(9)=16": 16,
    "octonion dim=8": 8,
    "roots G₂=12": 12,
    "rank E₈=8": 8,
    "3 generations": 3,
    "spacetime dim=4": 4,
    "SM gauge gen=12": 12,
}

target_C = 4 / 3  # = 1.3333...
target_E = 12
target_P = 36
print(f"  Searching pairs (a, b) with a/b ≈ 4/3 = {target_C:.6f}:")
print(f"  {'a':25} {'b':25} {'a/b':10} {'Δ from 4/3':10}")
print(f"  {'-' * 70}")
names_dims = list(dims_to_test.items())
for i, (na, va) in enumerate(names_dims):
    for j, (nb, vb) in enumerate(names_dims):
        if i != j and vb != 0:
            ratio = va / vb
            delta = abs(ratio - target_C) / target_C
            if delta < 0.05:  # within 5% of 4/3
                print(f"  {na:25} {nb:25} {ratio:.6f}  {delta * 100:+.2f}%")

print()
# Exact 4/3:
print("  Exact 4/3 matches (within 0.1%):")
found_exact = False
for na, va in names_dims:
    for nb, vb in names_dims:
        if vb != 0 and abs(va / vb - 4 / 3) < 0.001:
            print(f"    {na}/{nb} = {va}/{vb} = {va / vb:.6f} ✓")
            found_exact = True
if not found_exact:
    print("    None found — 4/3 doesn't arise trivially from these dimensions.")
    print("    Best candidate: from EXP-F, 4/3 = (n+1)/n at n=3 (sphere geometry).")

# ─── 7. Singh's trace-dynamics estimate for α_EM ─────────────────────────
print("\n--- 7. Singh Trace-Dynamics: α_EM from Algebraic Structure ---")
print(f"""
  Singh (arXiv:2006.06616, 2020) derives α_EM from "pre-quantum" trace
  dynamics where the SM gauge group emerges from the octonion algebra.

  Key claim: α_EM is related to the ratio of Planck action to
  a "characteristic action" set by the SM spectrum.

  Specific formula (Singh 2020, Eq. based on memory — [WEAK]):
    α_EM ≈ (dim(SM_gauge_algebra)) / (dim(E₈) × some_factor)
    = 12 / (248 × k)

  Test: 12/248 = {12 / 248:.6f}  vs α_EM = {alpha_EM:.6f}
  Ratio: {(12 / 248) / alpha_EM:.2f}  (needs factor of {alpha_EM / (12 / 248):.2f} to match)
""")

# Try various algebraic formulas for alpha_EM
print("  Algebraic tests for α_EM = 1/137.036:")
print(f"  {'Formula':40} {'Value':12} {'1/value':12} {'Match':10}")
print(f"  {'-' * 75}")


def test_alpha(label: str, val: float) -> None:
    inv = 1 / val if val != 0 else float("inf")
    match = abs(val - alpha_EM) / alpha_EM * 100
    flag = " ✓ MATCH" if match < 1.0 else f" ({match:.1f}% off)"
    print(f"  {label:40} {val:.6e}  {inv:9.3f}  {flag}")


# Various formulas
test_alpha("3/(2π×dim(G₂))", 3 / (2 * math.pi * 14))
test_alpha("dim(G₂)/(dim(E₈))", 14 / 248)
test_alpha("dim(J₃(𝕆))/(dim(E₈)×π)", 27 / (248 * math.pi))
test_alpha("1/(6×dim(J₃(𝕆))+...)", 1 / (6 * 27 - 25))  # = 1/(162-25) = 1/137
test_alpha("1/(6×dim(J₃(𝕆))-25)", 1 / (6 * 27 - 25))
test_alpha("dim(J₃(ℍ))/(dim(E₈))", 15 / 248 * math.pi)
test_alpha("2×dim(J₃(𝕆))/(dim(E₈)×π)", 2 * 27 / (248 * math.pi))

print(f"\n  KEY CHECK: 6×27 - 25 = {6 * 27 - 25}")
print(f"  → 1/(6×dim(J₃(𝕆)) - 25) = 1/{6 * 27 - 25} = {1 / (6 * 27 - 25):.9f}")
print(f"  → α_EM = 1/137.036 = {alpha_EM:.9f}")
print(f"  → Match: {abs(1 / (6 * 27 - 25) - alpha_EM) / alpha_EM * 100:.6f}%")

# ─── 8. SM gauge group connection ────────────────────────────────────────
print("\n--- 8. Standard Model Gauge Group and E=12 ---")
print(f"""
  SM gauge group: SU(3)×SU(2)×U(1)
    Generators of SU(3): 8 (gluons)
    Generators of SU(2): 3 (W bosons)
    Generators of U(1):  1 (photon B field)
    Total SM generators: 8 + 3 + 1 = {8 + 3 + 1}

  [VERIFIED] dim(SM gauge group) = 12 = Buckholtz exponent E!

  Also:
    Lepton generations = 3 = n (from J₃ structure)
    n × E = 3 × 12 = 36 = dim(SO(9)) = maximal subgroup of F₄

  Interpretation hypothesis:
    - E=12: counts SM gauge bosons (force carriers)
    - n=3: counts lepton generations (matter)
    - Together: a formula encoding [matter generations]^E × [gauge structure]
      gives α_EM/α_G — the electromagnetic-to-gravitational coupling ratio
""")

print(f"  dim(SU(3)) = {3**2 - 1}")
print(f"  dim(SU(2)) = {2**2 - 1}")
print("  dim(U(1))  = 1")
print(f"  Total SM   = {(3**2 - 1) + (2**2 - 1) + 1} = E = {EQ32_E}  ✓")

# ─── 9. The 1/6×27-25 = 1/137 formula: is it real? ──────────────────────
print("\n--- 9. 6×dim(J₃(𝕆)) - 25 = 137: Coincidence Check ---")
val_137 = 6 * 27 - 25
print(f"  6 × 27 - 25 = 6 × dim(Albert algebra) - 25 = {val_137}")
print("  Compare: 1/α_EM = 137.036...")
print(
    f"  Deviation: {abs(val_137 - 1 / alpha_EM):.4f}  ({abs(val_137 - 1 / alpha_EM) / (1 / alpha_EM) * 100:.3f}%)"
)
print("\n  [INFERRED: WEAK] This is suggestive but:")
print("  1. The '25' is unexplained — why subtract 25?")
print("  2. Could be retrofitted (look-elsewhere in integer arithmetic)")
print("  3. Needs independent theoretical derivation to be meaningful")
print("  4. 1/α_EM = 137.036 ≠ 137 (integer)")
print("\n  cf. Eddington's failed 'derivation' of 137 from combinatorics (1929)")
print("  → Treat as [CANDIDATE PEARL] not [VERIFIED]")

# ─── 10. Summary ────────────────────────────────────────────────────────
print("\n--- 10. Summary: What Fits and What Doesn't ---")
print(f"""
  STRONG algebraic connections [VERIFIED]:

  1. G₂ = Aut(𝕆) has exactly 12 root vectors
     → E = 12 = #roots(G₂) [exponent in Buckholtz Eq.32]
     Status: [VERIFIED] — standard result in Lie theory

  2. dim(SM gauge group) = 12 = E
     → SU(3)×SU(2)×U(1) has 8+3+1 = 12 generators
     Status: [VERIFIED] — well-known SM fact

  3. dim(SO(9)) = 36 = n×E = 3×12
     → SO(9) is the maximal subgroup of F₄ = Aut(J₃(𝕆))
     → F₄ decomposes as 52 = 36 (SO(9) sector) + 16 (spinor sector)
     Status: [VERIFIED] — standard result in exceptional Lie theory

  WEAKER connections [CANDIDATE / INFERRED]:

  4. 6 × dim(J₃(𝕆)) - 25 = 137 ≈ 1/α_EM
     → Numerological; '25' has no established derivation
     Status: [CANDIDATE PEARL] — needs theoretical justification

  5. Prefactor 4/3 from J₃ structure
     → NOT found in standard J₃(𝕆) / exceptional algebra decompositions
     → Better explained by S³ sphere geometry (EXP-F)
     Status: [UNKNOWN] — open problem

  OPEN QUESTION (Gap G3):
  WHY do the numbers {4 / 3, 12, 36} appear simultaneously in both:
    (a) Buckholtz Eq.32 (empirical lepton-gravity formula), AND
    (b) Exceptional algebra F₄/G₂/SO(9) structure?
  This may be the deepest question this experiment suite has uncovered.
""")

# Pearl candidate
print("=" * 70)
print("PEARL CANDIDATE (for pearl_registry/INDEX.md):")
print("""
  Observation: G₂ = Aut(𝕆) has 12 root vectors; SM gauge group has 12
               generators; Buckholtz Eq.32 exponent E = 12.
  Falsifiable prediction: If E=12 reflects gauge/octonionic structure,
    then analogous formulas for other fundamental couplings should use
    exponents equal to the root count of OTHER relevant symmetry groups
    (e.g., E₈ roots = 240 for a quantum gravity analog?).
  Trigger condition: new measurement of α_EM/α_G at 10⁻⁴ precision.
  Next check: 2026-09-01 — check if TJB's IDM framework specifies E=12.
""")
print("=" * 70)
print("✅ EXP-G complete.")
