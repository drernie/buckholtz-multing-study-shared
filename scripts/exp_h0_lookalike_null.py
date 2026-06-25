"""EXP-H0: Look-Elsewhere Null Test for Gap G3 Coincidences.

Question: Is the appearance of {4/3, 12, 36} in exceptional algebra a
genuine signal or expected noise from the small integer space?

Method:
  Enumerate ALL "interesting" algebraic dimensions ≤ 300:
  - Exceptional Lie group dims and root counts
  - Classical Lie group dims (SO(n), SU(n), Sp(n))
  - Division algebra dims (1,2,4,8)
  - Jordan algebra dims
  - SM-related integers
  Then count how many pairs give ratio = 4/3 ± 0.1%.
  And how many triples (a,b,c) satisfy a = b×c simultaneously.

This tells us: if we pulled 3 numbers at random from this space,
how often would we get {4/3 ratio, product=36, quotient=12}?
"""

from __future__ import annotations

print("=" * 70)
print("EXP-H0: Look-Elsewhere Null Test — Is {4/3, 12, 36} Special?")
print("=" * 70)

# ─── Algebraic dimension pool ─────────────────────────────────────────────
# All "interesting" integers from exceptional algebra, SM physics, etc.

# Exceptional Lie algebras
exc_dims = {14, 52, 78, 133, 248}  # G₂, F₄, E₆, E₇, E₈
exc_roots = {12, 48, 72, 126, 240}  # root counts
exc_ranks = {2, 4, 6, 7, 8}  # ranks

# Key representations
reps = {
    7,  # G₂ fund
    14,  # G₂ adjoint
    26,  # F₄ / E₆ coset
    27,  # J₃(O) = Albert algebra, F₄ rep
    56,  # E₇ fundamental
    248,  # E₈ adjoint
    16,  # Spin(9) spinor
    36,  # SO(9) dim
    9,  # SO(9) vector rep
    10,  # J₂(O) dim
}

# Division algebras
div_alg = {1, 2, 4, 8}  # ℝ,ℂ,ℍ,𝕆

# Jordan algebra dims: J_n(k) = k·n(n-1)/2 + n
jordan_dims = set()
for k in [1, 2, 4, 8]:
    for n in range(1, 6):
        jordan_dims.add(k * n * (n - 1) // 2 + n)

# Classical Lie groups SO(n): dim = n(n-1)/2
so_dims = {n * (n - 1) // 2 for n in range(2, 20)}

# SU(n): dim = n^2 - 1
su_dims = {n**2 - 1 for n in range(2, 15)}

# Sp(n): dim = n(2n+1)
sp_dims = {n * (2 * n + 1) for n in range(1, 10)}

# SM-related
sm_nums = {8, 3, 1, 12, 4, 6, 2, 45, 24}  # gauge gen counts

# Spacetime / generation counts
nat_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# Merge all
all_dims = (
    exc_dims
    | exc_roots
    | exc_ranks
    | reps
    | div_alg
    | jordan_dims
    | so_dims
    | su_dims
    | sp_dims
    | sm_nums
    | nat_nums
)
# Filter to ≤ 300
all_dims = {d for d in all_dims if 1 <= d <= 300}
all_dims_sorted = sorted(all_dims)

print(f"\n  Total 'interesting' algebraic integers ≤ 300: {len(all_dims)}")
print(f"  Pool: {all_dims_sorted}")

# ─── Count pairs with ratio ≈ 4/3 ────────────────────────────────────────
TARGET_RATIO = 4 / 3
TOL = 0.001  # 0.1% tolerance

print(f"\n--- Pairs (a,b) with a/b ≈ 4/3 ± {TOL * 100:.1f}% ---")
ratio_pairs = []
for a in all_dims_sorted:
    for b in all_dims_sorted:
        if b != 0 and a != b:
            r = a / b
            if abs(r - TARGET_RATIO) / TARGET_RATIO < TOL:
                ratio_pairs.append((a, b, r))

ratio_pairs.sort(key=lambda x: abs(x[2] - TARGET_RATIO))
print(f"  Found {len(ratio_pairs)} pairs:")
for a, b, r in ratio_pairs[:20]:
    print(f"    {a}/{b} = {r:.6f}  (Δ = {(r - TARGET_RATIO) / TARGET_RATIO * 100:+.4f}%)")

# ─── Among these pairs, how many have a = 36, b = 27 specifically? ───────
print("\n  Of these, Buckholtz-relevant pair dim(SO(9))/dim(J₃(𝕆)) = 36/27:")
buckholtz_pair = [(a, b) for a, b, r in ratio_pairs if a == 36 and b == 27]
if buckholtz_pair:
    print(f"    36/27 = {36 / 27:.6f}  ← IS in the list ✓")
else:
    print("    36/27 NOT found (would only appear if both 36 and 27 are in pool)")

# ─── Count triples (a,b,c) with a=b×c and a/b = 4/3 ─────────────────────
print("\n--- Triples (a,b,c): a/b = 4/3 AND a = b×k for some integer k ---")
triples = []
for a, b, _r in ratio_pairs:
    if a % b == 0:  # a exactly divisible by b (integer multiple)
        k = a // b
        triples.append((a, b, k))

print(f"  Found {len(triples)} such triples:")
for a, b, k in triples:
    print(f"    {a}/{b} = 4/3 (exact: {a}={b}×{4}/{3}), {a}={b}×{k}")

# ─── The key triple: {36, 27, 12} ────────────────────────────────────────
print("\n--- Key triple from Gap G3: {36, 27, 12} ---")
print("  36/27 = 4/3 (prefactor)")
print("  36 = 3 × 12 (product n×E)")
print("  27 = dim(J₃(𝕆))")
print("  12 = roots(G₂) = dim(SM gauge)")
print(f"  All three in pool: {{{36, 27, 12} <= all_dims}}")

# Is {36, 27, 12} simultaneously satisfying:
# 36/27 = 4/3 AND 36 = 3×12?
cond1 = abs(36 / 27 - 4 / 3) < 1e-10  # 4/3
cond2 = 36 == 3 * 12  # n×E
cond3 = 12 in exc_roots  # G₂ roots
cond4 = 27 in reps  # Albert algebra
print("\n  Simultaneous conditions:")
print(f"    36/27 = 4/3: {cond1}")
print(f"    36 = 3×12: {cond2}")
print(f"    12 ∈ exceptional root counts: {cond3}")
print(f"    27 ∈ exceptional reps: {cond4}")
all_cond = cond1 and cond2 and cond3 and cond4
print(f"\n  All conditions simultaneously: {all_cond}")

# ─── How often does a random triple from the pool satisfy all conditions? ─
print("\n--- Random Triple Probability Estimate ---")
N = len(all_dims)
# P(a/b = 4/3 for random pair) ≈ len(ratio_pairs) / N^2
n_ordered_pairs = N * (N - 1)
p_ratio = len(ratio_pairs) / n_ordered_pairs
print(f"  Pool size N = {N}")
print(
    f"  P(random pair has ratio 4/3 ± 0.1%) = {len(ratio_pairs)}/{n_ordered_pairs} = {p_ratio:.4f}"
)

# P(a = 3×b for random pair): count pairs where a = 3b exactly
exact_triples = [(a, b) for a in all_dims for b in all_dims if a == 3 * b]
p_triple = len(exact_triples) / n_ordered_pairs
print(
    f"  P(random pair has a = 3×b exactly) = {len(exact_triples)}/{n_ordered_pairs} = {p_triple:.4f}"
)

# Combined (not independent, but rough):
p_combined = p_ratio * p_triple  # very rough lower bound
print(f"  P(both conditions, rough lower) ≈ {p_combined:.6f} ({1 / p_combined:.0f}:1 odds)")
print(
    f"  → The triple {{36, 27, 12}} is {'EXPECTED' if p_ratio > 0.05 else 'UNUSUAL'} given pool size"
)

print("\n--- Summary ---")
print(f"""
  With {N} 'interesting' algebraic integers in the pool:
  - {len(ratio_pairs)} pairs have ratio 4/3 ± 0.1%
  - P(random pair ≈ 4/3) ≈ {p_ratio:.4f} = {p_ratio * 100:.2f}%

  The Buckholtz-relevant pair 36/27 IS one of {len(ratio_pairs)} such pairs.
  The triple {{36, 27, 12}} additionally satisfies 36 = 3×12.

  Verdict: With {len(ratio_pairs)} pairs having ratio ≈ 4/3, the coincidence
  is {"NOT TRIVIAL — relatively few pairs" if len(ratio_pairs) < 10 else "MODERATELY EXPECTED"}.
  The additional constraint 36 = 3×12 (from the Buckholtz product n×E)
  makes the triple {"MORE SPECIAL" if len(exact_triples) < 5 else "LESS SPECIAL"}.

  [INFERRED] The coincidence is not a trivial consequence of pool size,
  but also not astronomically unlikely. It needs a theoretical explanation.
""")
print("✅ EXP-H0 complete.")
