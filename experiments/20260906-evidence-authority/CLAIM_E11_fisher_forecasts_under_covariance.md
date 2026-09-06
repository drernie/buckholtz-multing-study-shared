# CLAIM E11 — rerun the P191-P194 Fisher forecasts against E8's corrected
# degeneracy baseline

**Date:** 2026-09-06 (pre-registered BEFORE any code)
**Continues:** `FINDING_E8` — which found the `(β₁,β₂)` degeneracy this
project measured in `P176`/`P190` is `4.0-7.6×` more severe under
Moresco's own CC covariance, and named this rerun as its next step.
Explicit user go-ahead: "давай сделаем пересчёт".

## L0 (EstimandOps)

**Question type: descriptive.** How do `P193`/`P194`'s Fisher-forecast
results — which synthetic high-`z` `H(z)` points shrink the `(β₁,β₂)`
degeneracy, and by how much — change when the 31 real CC points carry
Moresco's covariance instead of diagonal errors?

## The trap, named before the numbers exist

Synthetic points add a fixed contribution to the Hessian. The covariance
weakens only the 31 real points. **With a weaker baseline, the same
synthetic set produces a LARGER percentage shrinkage** — so a "%
shrinkage" endpoint would make `P191`-`P194` look *more* convincing while
the actually-achievable constraint gets *worse*. That headline would be
false in substance.

**Therefore the endpoint is the absolute post-augmentation width,
not the percentage:**

```
t_aug = sqrt(2 / λ_small,aug)      fractional-shift units, P191's own definition
```

`P176`'s baseline: `t = sqrt(2/70.60) = 16.8%`. `E8`'s corrected
baselines: `sqrt(2/17.46) = 33.8%` (Moresco default), `sqrt(2/9.27) =
46.4%` (stress). The baseline *width* doubles to nearly triples before
any synthetic point is added.

## Two pre-registered questions

**Q1 — ranking.** Does `P193`'s window `z ∈ {12,14,16}` remain the most
informative, and does `P194`'s dense-scan ordering within `(10, 16.957)`
survive? *Prior expectation:* yes — ranking is set by the degeneracy
*direction*, which `E8` found unchanged to `<1%`.

**Q2 — absolute attainability.** At `σ_synth = 10%` in the best window,
what `t_aug` is actually reachable under the honest covariance? *Prior
expectation:* materially worse than `P194` reports.

## Pre-registered MCID

- **Q1 MATERIAL** if the best window changes, OR the greedy-vs-joint
  ranking in `P194` reorders at the top, OR the domain boundary
  `z≈16.957` moves by `>5%` (it should not move at all — it depends on
  the fiducial model, not on errors; if it does, that is a bug).
- **Q2 MATERIAL** if `t_aug(σ=10%, best window)` degrades by more than
  `1.5×` relative to `P194`'s diagonal value.
- **Not claimed in advance:** that any `P191`-`P194` *relative* conclusion
  is wrong. Expectation: relative survives, absolute does not.

## Method

1. Reuse `P194`'s `augmented_chi2` structure verbatim for the synthetic
   term; replace the real-33-point diagonal term with `E8`'s
   covariance-weighted `rᵀC⁻¹r` (`make_chi2_cov`, Moresco default and
   stress variants).
2. Numeric Hessian in `P176`/`P191`'s rescaled coordinates (`hessian_eig`)
   — the same estimator `P191`-`P194` used, so differences are
   attributable to the covariance alone.
3. Report, per error model × window × `σ_synth`: `λ_small,aug`, `t_aug`,
   and — for transparency only — the % shrinkage, labelled as the
   misleading metric it is.

## Controls

- **Regression:** with modelling terms zeroed, `E11` must reproduce
  `P193`/`P194`'s diagonal `λ_small,aug` at `{12,14,16}`, `σ=10%` to
  `<0.1%`.
- **Floor:** `σ_synth → ∞` must return `E8`'s covariance baseline
  (`17.46` / `9.27`) to `<0.1%`.
- **Ceiling:** `σ_synth → 0` should be error-model-independent (synthetic
  dominates) — if the ceiling differs between diagonal and covariance
  by more than numerical noise, something is wrong.
- **Boundary invariance:** `H²(z)<0` onset must stay at `16.957`.

## What this claim does NOT say

- Nothing about MULTING vs ΛCDM — this is entirely about how much a
  hypothetical future measurement could constrain this project's own
  reconstruction's parameters.
- Nothing about whether `z~12-16` `H(z)` measurements are feasible —
  `P191`-`P194` already flagged that as out of scope.
- `NO_AUTHOR_ERROR`.
