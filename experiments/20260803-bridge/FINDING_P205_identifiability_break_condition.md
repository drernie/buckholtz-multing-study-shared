# FINDING P205 — the exact condition that breaks `P133`'s rank-2
# identifiability failure: `2a ≠ b + c`

**Date:** 2026-09-07
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 math (symbolic, no data, no fit)
**Artifact:** `scripts/p205_identifiability_break_condition.py`
**Continues:** `FINDING_P133` (structural non-identifiability of
`(A, g, κ)`), addressing bottleneck #4 of the 33-item map.

## What `P133` left open

`P133` proved the observable set

```
O1 = A g²      O2 = A κ²      O3 = κ / g
```

has `rank(J) = 2 < 3` in `(A, g, κ)`, because `O2 ≡ O1 · O3²`. That is
structural: **no precision improvement on these three ever identifies
the parameters.** `P133` established the obstruction. It did not say
what would remove it.

## Result — the break condition, derived and verified

Working in log space (monomials become linear), the three observables
span only

```
(1, 2, 0)  and  (0, −1, 1)
```

A candidate new observable `O4 = A^a g^b κ^c` lies **inside** that
degenerate span iff its exponents satisfy the compatibility condition,
computed exactly as the determinant of the augmented system:

```
2a − b − c = 0
```

**Therefore `O4` raises the rank to 3 — i.e. makes `(A, g, κ)`
identifiable — if and only if**

```
                    2a ≠ b + c
```

**In particular, a direct measurement of any ONE of `A`, `g`, or `κ`
alone suffices** — `(1,0,0)`, `(0,1,0)`, `(0,0,1)` each give `2a−b−c =
2, −1, −1` respectively, all non-zero.

Equally important, the negative direction: **no further observable of
the `O1`/`O2`/`O3` family will ever work, at any precision.** Anything
built as a product of the existing ones inherits `2a = b + c`.

## Verification `[VERIFIED-run]`

The script does not assert the algebra, it recomputes it:

- **PC1 (positive control):** rank of the Jacobian of `(O1,O2,O3)` in
  `(A,g,κ)` computed directly → **2**, reproducing `P133`. Asserted.
- **PC2 (identity control):** `O2 − O1·O3²` simplified → **0**.
  Asserted. The degeneracy *is* this identity.
- **7 candidate checks**, each with the rank **recomputed** from a
  fresh 4×3 Jacobian and compared against the condition's prediction —
  including two **negative controls** (`O1` and `O3` themselves, which
  must *not* break it, and do not). All 7 agree.

## What this does and does NOT establish

**Does establish:** a sharp, checkable, exhaustive criterion for what
kind of new measurement resolves `P133`'s degeneracy — turning "the
parameters are structurally unidentifiable" into "here is precisely the
class of observables that would identify them, and precisely the class
that never will."

**Does NOT establish:**
1. That such an observable is physically accessible. The criterion is
   about *exponent structure*, not about whether anything in the sky
   measures `A`, `g`, or `κ` singly. Finding one is a separate problem
   and is not solved here.
2. That `(A, g, κ)` are the right parameters to identify — that framing
   comes from `P133` and is inherited, not re-examined.
3. Anything about the monomial assumption. The criterion covers
   observables of **monomial** form `A^a g^b κ^c`. A non-monomial
   observable (a sum of terms, a ratio with additive structure) is
   outside this analysis — `[UNKNOWN]`, and the most likely place for
   this result to be too narrow.
4. Anything about v82's correctness — `NO_AUTHOR_ERROR`. This is about
   this project's own reconstruction of the observable set.

## Pearl Registry / next step

The criterion converts an open bottleneck into a **search with a
filter**: scan candidate cosmological/cluster observables, compute each
one's `(a,b,c)` scaling in `(A,g,κ)`, keep only those with
`2a ≠ b + c`. That scan has not been done and is the natural next step
— cheap per candidate, and now guaranteed not to waste effort on
observables that provably cannot help.
