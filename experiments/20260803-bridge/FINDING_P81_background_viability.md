# FINDING P81 — **V-REGION.** The completion has a viable corner, and its boundary is located

**Status:** built, run, verdict **V-REGION** against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P81_background_viability.py`

> **Part of this result is not new, and that is said first rather than buried.**
> The `λ → 0` wall reproduces `FINDING_P69`'s central claim by a different route.
> What is new is the `ĝ` boundary and the extent of the region.

---

## The gap this closes

`FINDING_P63` proved the coupled background **closes** (Bianchi-consistent).
`FINDING_P64` found trajectories that **exist** numerically. Neither asked
whether any of them is physically **viable** over a cosmological span — and those
are different questions. A system can be perfectly consistent and still drive
itself into `ρ_phys < 0` or through the `1 − ĝφ̄ = 0` surface within a decade.

The campaign's only viability datum was a **single point**: `FINDING_P77`'s side
check I4 gave `min(1−ĝφ̄) = 0.87` at `(ĝ, λ) = (1, 1)`. One point is not a
region, and the arc had been quoting it as though the surrounding corner were
known.

**Predicate** (pre-registered in `TZ_P79_P82` before any scan), over ≥8 decades:
`a > 0`, `ρ_phys > 0`, `min(1−ĝφ̄) > 0.1`, `H` monotone.

---

## Controls — all three, and C3 exists so the gate can say *no*

| | check | result |
|---|---|---|
| **C1** | reproduce P77's one known point | `0.8717` against P77's reported `0.87` — **agrees at the 2 d.p. P77 actually reported** |
| **C2** | `ĝ=0` viable at every `λ` (no coupling ⇒ `1−ĝφ̄ ≡ 1`) | passes at `λ = 0, 0.1, 1, 10` |
| **C3** | an absurd point must **fail** | `(50, 1)` → `ρ_phys ≤ 0`, `min(1−ĝφ̄) = −86.2`, `H` non-monotone |

C1 is deliberately checked only to **two decimal places**. P77's I4 is prose, not
an importable function, so this *is* a transcription comparison — the exact shape
of `FINDING_P78`'s A3 failure. Quoting agreement tighter than the source reported
it would manufacture precision that does not exist.

---

> ### ⚠ NOTE FILED BY `FINDING_P86` — the `min_M` column for **failing** points
>
> P86 added a **terminal event** to `viability()` that stops integration once
> `1−ĝφ̄` reaches `−1`, because everything past that is the solver fighting a
> runaway the predicate has already rejected (`FLOOR` is `0.1`).
>
> **Nothing in this file's verdict changes.** Viable points never reach `M = −1`
> and take a bitwise-identical code path; the `ok` flag is unchanged everywhere.
> P86C validated this against P83's located boundary, which came back
> `2.751767` — relative difference `1.764e-07`.
>
> **What does change:** for *non-viable* points the reported `min(1−ĝφ̄)` is now
> the value **at the stop** (`−1`), not the global minimum over the span. So the
> figures `−7.9e+04`, `−5.5e+09`, `−1.9e+13` quoted below are **no longer
> reproducible by the current code** — they were correct when measured and are
> kept as the record of that run.
>
> **One gain:** `(2, 0)`, listed below as UNRESOLVED, is now **measured** and
> non-viable — `M` reaches `−1` at `t = 153.9`.

## The Substrate Gate applied to a scan — **three** outcomes, not two

The first run marked `(2, 0)` and `(5, 0)` as **non-viable** because the
integrator gave up on them. That is my own rule violated: *"the test could not
run" is not "the predicate is false."* Both were reclassified:

```
viable      : 49 of 63
non-viable  : 12   (measured, predicate false)
UNRESOLVED  :  2   (not measured -- never evidence either way)
```

The temptation to fold them in was real — both sit in the `λ=0` column between
points that fail catastrophically (`−5.5e+09` at `ĝ=1.5`, `−1.9e+13` at `ĝ=3`),
so they are *almost certainly* the same blow-up. **Almost certainly is an
inference, not a measurement**, and they are excluded from both buckets.

---

## The region

Cells are `min(1−ĝφ̄)`; `–` means not viable or unresolved.

| `ĝ \ λ` | `0` | `0.01` | `0.1` | `0.5` | `1` | `2` | `10` |
|---|---|---|---|---|---|---|---|
| **0** | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| **0.25** | 0.9205 | 0.9723 | 0.9758 | 0.9783 | 0.9794 | 0.9805 | 0.9832 |
| **0.5** | 0.6897 | 0.9268 | 0.9390 | 0.9473 | 0.9507 | 0.9541 | 0.9617 |
| **0.75** | – | 0.8643 | 0.8907 | 0.9077 | 0.9147 | 0.9214 | 0.9360 |
| **1** | – | 0.7851 | 0.8312 | 0.8602 | **0.8717** | 0.8828 | 0.9064 |
| **1.5** | – | 0.5743 | 0.6801 | 0.7425 | 0.7667 | 0.7894 | 0.8363 |
| **2** | ? | 0.2827 | 0.4850 | 0.5958 | 0.6374 | 0.6757 | 0.7531 |
| **3** | – | – | – | 0.2147 | 0.3081 | 0.3912 | 0.5513 |
| **5** | ? | – | – | – | – | – | – |

`min(1−ĝφ̄)` falls monotonically with `ĝ` at fixed `λ` and rises monotonically
with `λ` at fixed `ĝ`. **One** connected component, all 49 points.

### The `λ → 0` wall is **not** a new result

Every `λ=0` failure at `ĝ ≥ 0.75` — `0.0285`, then `−7.9e+04`, `−5.5e+09`,
`−1.9e+13` — is `FINDING_P69` again: *"the P65–P67 pathology is an artifact of
the `V=0` truncation."* P69 established that by removing the truncation on one
axis; P81 arrives at the same wall from a systematic two-parameter scan that was
not built to look for it. **A second route to a standing result, not a new one.**

> #### ⚠ NARROWED BY `FINDING_P83` — the wall is **initial-condition dependent**
>
> P83 re-ran this edge under the `φ̄̇(1)` lever and the classification **flips**:
>
> | lever | `λ=0` at `ĝ=0.75` | kinetic fraction |
> |---|---|---|
> | ×0.1 | **viable** | 0.056 % |
> | ×0.25 | **viable** | 0.349 % |
> | ×0.5 | **viable** | 1.38 % |
> | ×1 | not viable | 5.31 % |
> | ×2 | not viable | 18.3 % |
> | ×4 | not viable | 47.3 % |
>
> The flip sits **between ×0.5 and ×1, inside the matter-dominated range**, so it
> is not a change of cosmological regime.
>
> **But the flip is far less dramatic than it looks, and the first version of
> this note over-read it.** P83's boundary function gives
> `ĝ_crit(λ=0) = 0.776737 → 0.738209` from `×0.1` to `×1` — the boundary moves
> **~5 %** across a ten-fold lever change. The cell above flips only because
> `ĝ = 0.75` happens to sit within a few percent of `ĝ_crit ≈ 0.76`. **A grid
> point on a knife edge, not a wall on wheels.**
>
> **What this corrects:** the sentence above reads as though `V=0` is fatal at
> `ĝ ≥ 0.75` full stop. It is fatal there **only when the scalar's initial
> velocity is large enough** — and the `ĝ` at which that switches over is itself
> stable to ~5 %. `V=0` alone is not the killer; `V=0` *together with* sufficient
> `φ̄̇(1)` is.
>
> **What this does NOT do** (Gate 1 — a verdict on one artifact does not transfer
> to another): it does not refute or narrow `FINDING_P69` itself. P69 worked at
> the P65–P68 arc's own parameters, not at `(ĝ, λ) = (0.75, 0)`. Testing P69's
> claim under its own settings was **not done here**, and no such claim is made.
> What is narrowed is **this file's wording**, which over-generalised.

### What *is* new: the `ĝ` boundary

P69 never scanned `ĝ`. P81 locates a second edge: at small `λ`, the completion
fails above `ĝ ≈ 2.8`. Refined in Part D at `λ = 0.1`:

| `ĝ` | 2 | 2.25 | 2.5 | 2.75 | 3 |
|---|---|---|---|---|---|
| `min(1−ĝφ̄)` | 0.4850 | 0.3699 | 0.2423 | **0.1010** | −0.0551 |

**Is the boundary an artifact of the `0.1` threshold?** The `0.1` floor is a
pre-registered convention; the *physical* singularity is at `min(1−ĝφ̄) = 0`,
where `ρ_phys` changes sign. Linearly interpolating the two measured points
either side puts that zero at `ĝ ≈ 2.91`, against `≈ 2.75` for the `0.1` margin —
a `5.5 %` difference `[INFERRED — linear interpolation between two measured
points, not itself a measurement]`. **The verdict does not depend on the
threshold choice.**

## Part D — the boundary is a surface, not a grid artifact

Part C's flood fill sees nothing finer than the step, so both edges were bisected
across:

- **`λ → 0` at `ĝ = 0.75`:** `0.0285 → 0.8051 → 0.8200 → 0.8358 → 0.8497 →
  0.8643` for `λ = 0, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2`. **Monotone.** Note the jump
  is at `λ = 0` **exactly** — even `λ = 1e-4` is already deep in the viable
  region. The wall is at the truncation itself, not at "small `λ`".
- **`ĝ` at `λ = 0.1`:** monotone, table above.

**Monotone on both**, so the boundary is a surface the coarse grid sampled rather
than an accident of where grid points landed.

---

## What is NOT established

- **Connectivity below the grid step.** A flood fill on a coarse grid cannot see
  finer holes, and none is excluded.
- **That viability means correctness.** It is **necessary, never sufficient** — a
  background that does not destroy itself is not thereby right.
- **The two unresolved points.** `(2,0)` and `(5,0)` are not evidence in either
  direction.
- **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in force.
- **Anything about MULTING itself** (Gate 1). The completion is ours, and a
  verdict on our reconstruction does not transfer to Dr. Buckholtz's model.
- **Perelman condition 5** (external reconstruction) — still not met.
