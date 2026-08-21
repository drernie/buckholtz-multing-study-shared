# FINDING P74 — `μ` fixed, then shown **not to be a property of the model**

**Status:** built, run, reviewed context-blind, **three of its own claims retracted
after review**, rebuilt around what survives.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P74_gauge_correct_mu.py`

> **Headline.** Both defects `FINDING_P73` named are fixed. The file then issued
> **NO D2/D3 verdict** — and review showed **the reason it gave was wrong**. The
> verdict still stands, on two *different* grounds, one of which was only found by
> the reviewer. Under FL, "the diagnostic cannot give a verdict" is a third
> outcome, not a euphemism for failure.

---

## A. The reference density, **derived** `[VERIFIED-SYMPY]`

P73's Test 3 wrote `δρ + 3H·q_tot` from memory, got no `μ→1`, and abandoned the
fix. Derived instead — P73 proved both constraints are first class, so they hold
along the *whole* solution and are usable as identities at any `t`:

```
C₀ᵢ = 0   ⟹   Ψ̇ + HΨ = −4πG·δq_tot
C₀₀ = 0   ⟹   3H(Ψ̇+HΨ) + (k²/a²)Ψ + 4πG·δρ_tot = 0
──────────────────────────────────────────────────────────
          −(k²/a²)Ψ  =  4πG·[ δρ_tot − 3H·δq_tot ]
```

| candidate | result |
|---|---|
| `Δ = δρ − 3H·δq` | **EXACT** |
| `Δ = δρ + 3H·δq` (P73 Test 3) | **fails**, residual `−24πG·H·δq_tot` |

Residual *exactly twice* the term — the standing tell for a sign flip. **P73's
Test 3 failed because its sign was wrong**, and the sign is fixed by the
constraint algebra, not by convention.

### The corollary — now with a number `[VERIFIED-BASH]`

With the **total** comoving density this is an **identity**: `μ_tot ≡ 1` for any
`ĝ`, any `λ`. The reviewer correctly noted this was asserted algebraically and
**never checked numerically** — a real omission. Checked (Part G3):

```
worst |μ_tot − 1| along the ĝ=1 solution:  9.07×10⁻¹¹
```

Three orders below the integrator drift. So

```
μ := −(k²/a²)Ψ / (4πG·Δ_m)  =  1 + Δ_φ/Δ_m
```

**every deviation of `μ` from 1 is the scalar's own comoving density in units of
the matter's** — `μ`'s entire information content is the split, not the Poisson
equation.

---

## B. Lock mass — passes, but certifies **much less** than first claimed

Pure GR + dust (`ĝ=0, λ=0, φ̄̇(1)=0, δφ=δφ̇=0`), scalar sector verified identically
zero. Residual **2.27×10⁻⁸** at `rtol=1e-11`.

### ⚠️ RETRACTED — "the floor is set by the lock mass, not the solver"

The tolerance sweep that justified this ran at `ĝ=1`, **not on the lock mass**.
Swept properly (G1) `[VERIFIED-BASH]`:

| rtol | lock-mass max\|μ−1\| | ratio |
|---|---|---|
| 10⁻⁸ | 3.009×10⁻⁷ | |
| 10⁻¹⁰ | 1.103×10⁻⁷ | 0.366 |
| 10⁻¹¹ | 2.269×10⁻⁸ | 0.206 |
| 10⁻¹² | 9.384×10⁻⁹ | 0.414 |
| 10⁻¹³ | 2.697×10⁻⁹ | 0.287 |

**Monotone with rtol → it is integrator drift.** The floor is real *as a floor*,
but its **value is a choice of rtol**, not a fact about the model. Sentence
retracted.

### ⚠️ WEAKENED — "the control discriminates"

The reviewer argued the lock mass is blind to *any* modification proportional to
the coupling, since `ĝ=0` kills it. Tested by **fabricating one** (G2)
`[VERIFIED-BASH]`:

| definition | lock-mass residual |
|---|---|
| the real `Δ_m` | **2.2689×10⁻⁸** |
| `Δ_m + 7ĝρ_Aδφ` (pure invention) | **2.2689×10⁻⁸** |

**Identical to five digits.** The control certifies the sign and the `3H` factor
of the *matter* branch — and **nothing that vanishes at `ĝ=0`.**

---

## C–D. The measurement

At `t=10⁶`, all three modes subhorizon (`k/aH = 5.6 / 56 / 564`), unlike P73's
`t=10³` where `k=0.1` had `k/aH = 0.57`.

| k | μ(ĝ=1) | μ(ĝ=0) | **Δμ** |
|---|---|---|---|
| 0.1 | 1.000554393 | 1.000000001 | **5.544×10⁻⁴** |
| 1.0 | 0.999983690 | 1.000000000 | **−1.631×10⁻⁵** |
| 10 | 1.000000532 | 1.000000000 | **5.323×10⁻⁷** |

`μ(ĝ=0) = 1` to `10⁻⁹` — a **second control passing**: a decoupled scalar decays
into irrelevance, exactly as it should. This is the file's strongest internal
consistency check.

---

## E. ⚠️ FALSIFIED — "the result is initial-data independent"

Part E renormalised `δφ(1)` per `k` and found Δμ unchanged (1037× vs 1042×). The
reviewer's objection: **only `δφ(1)` was varied**, and it is subdominant by
amplitude, so "no change" was near-tautological. Correct. Tested with a real
lever (G4) `[VERIFIED-BASH]`:

| variation | Δμ (k=0.1) | Δμ (k=1) | Δμ (k=10) |
|---|---|---|---|
| baseline | 5.544×10⁻⁴ | −1.631×10⁻⁵ | 5.323×10⁻⁷ |
| `Ψ₀ ×100` | 5.628×10⁻⁴ | −1.632×10⁻⁵ | 5.323×10⁻⁷ |
| **`φ̄̇(1) ×0.5`** | **−1.121×10⁻³** | −6.161×10⁻⁵ | 1.020×10⁻⁶ |
| **`φ̄̇(1) ×2`** | **−1.891×10⁻⁵** | −3.205×10⁻⁵ | −4.353×10⁻⁷ |

`Ψ₀` by 100× moves it **<2 %**. `φ̄̇(1)` by 2× **swings it 59× and inverts its
sign.** **Δμ is not a property of the model in this setup — it depends on an
initial condition.**

---

## F. The stop — one half retracted, the other half sharpened

### ⚠️ F1 RETRACTED — the pole argument

F1 argued `Δ_m`'s zero-crossings make the `t=10⁶` reading arbitrary. That only
holds if a crossing is *near* `t=10⁶`. Located (G5) `[VERIFIED-BASH]`:

| k | `Δ_m` crossings at t = |
|---|---|
| 0.1 | 1.39, 19.4, 32.9 |
| 1.0 | 1.24 |
| 10 | 1.08 |

**All at `t < 35`** — five decades before the evaluation. The pole inference is
**wrong and retracted.** What survives from F1 is only the control read-out: the
extra crossings at `k=0.1` (3 vs 1 against the ĝ=0 control) are coupling-caused.
That is about *early* behaviour and does not reach `t=10⁶`.

### F2 CONFIRMED and sharpened — the real ground

With F1 gone, F2 is load-bearing, so it was tested properly. The reviewer raised
aliasing: decade-boundary sampling of an oscillation. Sampled densely (G6)
`[VERIFIED-BASH]`:

| k | sign flips in `[10⁵, 10⁶]` | min | max |
|---|---|---|---|
| 0.1 | **25** | −6.375×10⁻⁴ | 9.935×10⁻⁴ |
| 1.0 | **0** | −1.704×10⁻⁴ | −2.367×10⁻⁶ |
| 10 | **25** | −4.980×10⁻⁷ | 7.830×10⁻⁶ |

**Not aliasing.** 25 genuine flips per decade at `k=0.1` and `k=10`, bounded
amplitude — a real oscillation with an envelope, exactly `FINDING_P70`'s `φ̄`
behaviour propagating into the diagnostic. At `k=1`, zero flips: its
non-convergence is genuine decay, not oscillation.

---

## Verdict — **NO VERDICT**, on two grounds, neither the original one

`FINDING_P60`'s D2-vs-D3 stays **open**.

1. **Δμ oscillates ~25×/decade** at `k=0.1` and `k=10`, so no single `t` gives a
   stable reading. `FINDING_P70` hit the same wall and fixed it by quoting the
   **envelope**. Not applied here — naming it is not doing it.
2. **Δμ depends on `φ̄̇(1)` strongly enough to change sign**, so it is not a
   property of the model at all in this setup. **This ground was found only by
   the reviewer.**

The pole argument the file first gave is **retracted**.

### What survives

1. `Δ = δρ − 3H·δq`, **derived**, PLUS form shown to fail — P73's Test 3 sign
   question is closed.
2. **`μ_tot ≡ 1` numerically** at `9.07×10⁻¹¹`, so `μ`'s content is the split.
3. `μ(ĝ=0) → 1` to `10⁻⁹` — decoupling correctly implemented.
4. Extra `Δ_m` crossings at `k=0.1` are coupling-caused (early times only).

### What this does NOT establish

1. Any D2/D3 verdict. Explicitly withheld.
2. That the ≤5.5×10⁻⁴ Δμ is a signal — it is IC-dependent and oscillating.
3. That the lock mass certifies the definition — it is blind to any
   ĝ-proportional term, demonstrated by fabrication.
4. That the numerical floor is intrinsic — it is rtol-chosen.
5. That the matter/total split is derived — P60 Route B convention.
6. Anything at `k ∉ [0.1, 10]`, or `(ĝ,λ) ≠ (1,1)`; that `k` maps to `h/Mpc`.
7. **Anything about MULTING itself** (Gate 1): `V` is *our* construction.

---

## Skeptic Verdict (Step 8a)

**`[FALSIFIED]` on three subsidiary claims; core conclusion `[CONFIRMED-REAL]`.**
Review was context-blind (`claim.md` + code only). **The reviewer had neither Bash
nor Write** — every number it gave was hand-arithmetic or an explicit hypothesis,
and it said so. Per `audit-verification-gate` that made all of it `[INFERRED]` to
me, so **all six claims were independently re-run** before any was accepted;
those runs are now Part G of the artifact, not scratch work.

| # | Concern | My independent re-run | Response |
|---|---|---|---|
| 1 | "Floor set by lock mass, not solver" untested on the lock mass | **CONFIRMED.** Residual falls monotonically 3.0e-7→2.7e-9 with rtol | **RETRACTED** (G1) |
| 2 | Lock mass blind to any ĝ-proportional modification | **CONFIRMED.** Fabricated `+7ĝρ_Aδφ` gives *identical* 2.2689e-8 | **WEAKENED** (G2) |
| 3 | `μ_tot ≡ 1` never checked numerically | **CONFIRMED as omission.** Now 9.07e-11 — better than their predicted ≤1e-7 | **FIXED, claim strengthened** (G3) |
| 4 | Part E has no lever; "IC-independent" unsupported | **CONFIRMED, and worse than they argued.** `φ̄̇(1)` swings Δμ 59× and flips sign | **FALSIFIED** (G4) |
| 5 | Crossings may be early transients ⟹ F1 unjustified | **CONFIRMED.** All at `t<35`, five decades early | **F1 RETRACTED** (G5) |
| 6 | F2 may be aliasing | **REFUTED.** 25 real sign flips per decade at two of three `k` | **F2 stands**, now load-bearing (G6) |

**Kill assessment.** The core conclusion — `μ` is not usable as a pointwise-in-`t`
diagnostic here — **survives**, and concern 4 *added* an independent reason for
it. Four of six concerns forced retractions; none touched the Part A derivation.
This is a **rebuilt finding, not a dead one**.

**Where the reviewer was wrong:** its aliasing hypothesis (concern 6) was refuted
by the dense sampling it could not run itself.

**AOG:** no hypothesis was relaxed to save anything — claims were **removed** and
the underlying question stayed open. AOG does not apply; nothing was promoted.

**Perelman condition 5 (external reconstruction):** still **not met**.
