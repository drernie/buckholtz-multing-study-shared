# FINDING — Stage 4: `d_flip` is **not derivable** inside the single-pair
# construction, and the shape test dies with it

> **[AMENDED 2026-09-07 — Step 8a skeptic]** Nine corrections were applied
> to this branch after a context-blind skeptic pass, all independently
> re-verified by tool before acceptance. **Read
> `AMENDMENTS_after_step8a_skeptic.md` before quoting anything below.**
> Load-bearing among them: any sentence of the form *"more thermal energy
> means less local EXPANSION"* is **WITHDRAWN** — the computed quantity is
> the response of ACCELERATION (s^-2), and no statement about `H` (s^-1)
> follows without integrating over history. No claim was killed.

**Date:** 2026-09-07
**Artifact:** `stage4_is_dflip_reachable.py`
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Status:** Stage-4 result, **not promoted**, no Step 8a pass.

---

## 1. The question

Stage 3b flagged `d_flip / d₀ = 2.06` as "outside the construction" but
left it qualitative. **Can `d_flip` be derived inside the construction at
all?**

**Answer: no.** Two independent reasons, both computed.

## 2. Reason 1 — `d` is not a free variable, and moving it moves everything

Inside v82's own kernel, `d = d_of(z) = d₀/(1+z)`. It cannot be varied
independently: `k(z)`, `R(z)`, `M(z)` all evolve with the same `z`.

`Q(z) = (b₂/b₁)·k(z)R(z)/(M(z)c²d(z))` is therefore **a function of `z`
alone**. The sign question needs no free `d` at all — just evaluate it.

| z | a = 1/(1+z) | d_of(z) [Mpc] | **Q(z)** | sign |
|---|---|---|---|---|
| −0.900 | 10.000 | 450.00 | 8.2400 | − |
| −0.750 | 4.000 | 180.00 | 4.5804 | − |
| **−0.514** | **2.058** | **92.59** | **3.0207** | **−** |
| −0.250 | 1.333 | 60.00 | 2.3578 | − |
| 0.000 | 1.000 | 45.00 | 2.0594 | − |
| 0.500 | 0.667 | 30.00 | 1.8214 | − |
| 1.000 | 0.500 | 22.50 | 1.7581 | − |
| 2.330 | 0.300 | 13.51 | 1.7659 | − |
| 5.000 | 0.167 | 7.50 | 1.8484 | − |
| 10.000 | 0.091 | 4.09 | 1.9567 | − |
| 16.900 | 0.056 | 2.51 | 2.0510 | − |

> **`Q(z) > 1` at every redshift from `z = −0.95` to `z = 16.9`**, minimum
> **`1.7484` at `z = 1.443`**. The response `∂(ä/a)/∂k` is **negative at
> every epoch the construction can represent** — the whole fitted range,
> the future branch, and up to `P192`'s own `H² < 0` boundary at
> `z = 16.957`.

**The decisive row is `z = −0.514`.** That is the epoch whose separation
*is* 92.59 Mpc — and `Q` there is **3.02**, not 1. Reaching the separation
the naive calculation pointed at does **not** reach the reversal, because
`k`, `R`, `M` moved too.

**Margin:** a reversal would require `b₂/b₁` smaller by a factor ≥ 1.748
(`5.446×10⁷ → 3.115×10⁷`) to make `Q` touch 1 at its minimum. The fit is
not marginally short of a reversal; it is short by 75%.

## 3. Reason 2 — `d_flip` was never a single number `[CORRECTION]`

PC1 checked whether `Q(z)·d_of(z)` is constant — it must be, if `d_flip`
is a fixed scale.

| z | Q(z) | `Q·d_of(z)` [Mpc] |
|---|---|---|
| 0.00 | 2.0594 | **92.673** |
| 0.50 | 1.8214 | **54.642** |
| 1.00 | 1.7581 | **39.558** |
| 2.33 | 1.7659 | **23.864** |

**A 74% spread across the fitted range.** `92.67 Mpc` is the **z = 0 value
only**.

**This corrects Stage 1 §4 and Stage 3b in place.** Both treated `d_flip`
as *a* scale — "the reversal sits at 92.67 Mpc." It does not; the
`d`-only reading gives a different number at every redshift, because
holding `k`, `R`, `M` at their `z=0` values while varying `d` is not an
operation the model supports.

## 4. Consequence — the shape test dies

Stage 3c had just established, by computation, that the standard picture
has **no** reversal in either limit, so a reversal would have been
discriminating. Stage 4 removes the other half of that comparison:

> **MULTING as constructed has no reversal either.** The 92.67 Mpc
> reversal was an artifact of *our* extension — treating `d` as a free
> population variable at fixed `z=0` — which `FINDING_P157` had already
> established v82 does not do.

| test | verdict | established by |
|---|---|---|
| monotone sign | **`CRITERION_INVALID`** — floor shares the sign | Stage 3 |
| shape (reversal) | **no reversal exists in the model** | **Stage 4** |

**Both versions of Ernest's test are now closed**, by two different and
independent mechanisms.

## 5. What survives, and it is not nothing

The computation leaves one clean, model-internal statement:

> At TJB's own published fit, `∂(ä/a)/∂k < 0` **at every epoch the
> construction can represent**. In this model more intracluster thermal
> energy means *less* local expansion, monotonically, with no crossover
> anywhere — the opposite of the intuitive reading of the mechanism, and
> stable across the entire domain rather than only at `z=0`.

That is a stronger and more robust statement than Stage 1's, which held
only at the fitted redshifts.

## 6. What this does NOT establish

1. **Not that MULTING is wrong** (`NO_AUTHOR_ERROR`). This is arithmetic
   on the published force law at one published parameter row.
2. **Not that no reversal exists for other `(b₁,b₂)`.** `Q ∝ b₂/b₁`; a fit
   with that ratio ≥1.75× smaller would have one. `β` remains
   `Q004`/`BETA-1`-blocked, so this is conditional on the published fit.
3. **Not that a population version is illegitimate** — only that it is
   *ours*, not the model's, and cannot be reported as a MULTING
   prediction.
4. **Does not revive the monotone test.** Stage 3's `CRITERION_INVALID`
   is independent of everything here.

## 7. Consequence for the direction

`claim.md`'s `REFUSE(no_falsifiable_predicate_yet)` now has a second,
stronger reason behind it. The direction closes: not because the data are
missing, but because the model as published makes no reversing prediction
to test, and its monotone prediction is one the cosmic web already makes.

Route back open only via unblock condition 1 of `claim.md` §8 — a fixed
reading of `k`, or a first-principles `β` — since both would change
`b₂/b₁` and could move `Q` below 1.
