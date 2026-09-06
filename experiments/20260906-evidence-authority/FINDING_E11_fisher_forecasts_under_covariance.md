# FINDING E11 — the P191-P194 Fisher forecasts are numerically robust to
# `E8`'s corrected baseline in the tested regime, but the "two robust
# results" reading is wrong: it is one mechanism (synthetic-information
# domination), and the mechanism itself is scope-limited

**Date:** 2026-09-06
**Claim:** `CLAIM_E11_fisher_forecasts_under_covariance.md` (pre-registered)
**Script:** `E11_fisher_forecasts_under_covariance.py`
**Continues:** `FINDING_E8`, which found `P176`/`P190`'s degeneracy
`4.0-7.6×` more severe than diagonal errors suggested, and named this
rerun as its next step.

## Controls — 6 total, all pass; PC6 added after a Step 8a skeptic finding

| control | result |
|---|---|
| PC1 regression: modelling terms zeroed → `P194`'s own diagonal result | `<0.1%` |
| PC2 floor: `σ_synth→∞` returns `E8`'s own covariance baseline | `<0.1%` both variants |
| PC3 analytic Fisher vs finite-difference Hessian | `0.09-3.8%` |
| PC4 ceiling: `σ_synth→10⁻⁶`, all three baselines agree | `8.8×10⁻⁸` relative |
| PC5 domain boundary `z=16.957` (depends on the model, not errors) | unchanged |
| **PC6 (added post-hoc, Step 8a):** doubling the modelling covariance moves the **baseline** small eigenvalue by a real, predicted amount | Moresco `17.7→9.3`, stress `9.8→7.6`, both pass |

**Why PC6 exists.** The first draft treated PC4 (ceiling agreement) as
evidence the covariance was correctly wired in. A skeptic pass pointed
out this is backwards: **PC4's agreement is predicted by the domination
mechanism itself, regardless of whether the covariance is read at
all** — a silently-ignored-covariance bug would produce the identical
number. PC6 is the actual positive control: it perturbs the covariance
by a known factor and requires the baseline curvature to respond. It
does, confirming the covariance path is live — but this had to be
demonstrated separately, not inferred from the ceiling test.

## The result, recomposed as one finding, not two

The first draft reported "Q1 (ranking unchanged) and Q2 (absolute width
unchanged) both confirm the forecasts are robust" as two independent
confirmations. **They are the same finding, viewed twice**, and a
second skeptic pass named the mechanism directly:

> At `σ_synth ≤ 10%`, a single synthetic point's own Fisher information
> is `~100-10,000×` larger than the real 31 points' curvature contribution
> (baseline small eigenvalue `9-70`). Once added, the augmented curvature
> is dominated by the synthetic term almost completely — which
> **deductively forces both outcomes**: the ranking (set by the synthetic
> gradient's own shape) cannot depend on the baseline, and the absolute
> width (`~O(λ_baseline/λ_synthetic)` relative correction) barely moves.

**The correct statement:** *in the regime where an added synthetic
point's information swamps the baseline, the baseline choice cannot
matter — this is an identity, not a robustness result about `P193`/
`P194` specifically.* Numbers, `σ_synth=10%`, `{z=12,14,16}`:

| | diagonal | Moresco default | stress |
|---|---|---|---|
| `t_aug` | `4.563%` | `4.567%` | `4.565%` |
| factor vs diagonal | — | `1.001` | `1.001` |

Neither pre-registered MCID fires (ranking unchanged; factor `≪1.5×`).

## What this means for `E8` — scope-differentiated, not undercut

`E8`'s own finding (the degeneracy is `4-8×` worse than reported)
**still stands and still matters** — for the *currently available*
posterior (no synthetic data), and for any future measurement whose
precision is *comparable to or looser than* the baseline errors. `E11`
shows only that a specific, tight forecast regime (`σ_synth≤10%`, three
`z`-points) is **prior-swamped**: the forecast would look almost
identical under *any* baseline of a size comparable to `E8`'s own
correction. `E8` and `E11` answer different questions about different
regimes; `E11` does not rescue `P193`/`P194` from a threat `E8` never
actually posed to them.

## Exploratory: where does the domination mechanism itself break down?

Not covered by `P193`/`P194`'s own grid (`σ_synth ≤ 10%`), and flagged
by the skeptic: **no `z≈12-16` `H(z)` measurement program exists on any
roadmap, and the existing `z<2` chronometers themselves carry `5-10%`
errors** — `σ_synth=10%` at `z=14` is already an optimistic assumption.
A wider, exploratory scan (no MCID pre-registered — no prior claim was
made about this regime):

| `σ_synth` | `t_aug` diagonal | `t_aug` Moresco | factor | `t_aug` stress | factor |
|---|---|---|---|---|---|
| `30%` | `6.45%` | `6.51%` | `1.01` | `6.53%` | `1.01` |
| `50%` | `8.61%` | `9.09%` | `1.06` | `9.19%` | `1.07` |
| `100%` | `12.46%` | `15.41%` | **`1.24`** | `16.09%` | **`1.29`** |

**The factor grows monotonically as `σ_synth` loosens** — consistent
with the domination mechanism weakening exactly as expected. It has not
crossed the `1.5×` MCID by `σ=100%`, but the trend is unambiguous and
worth stating rather than letting the `σ≤10%` result imply indefinite
robustness. If a real future `z~12-16` measurement is more realistically
`σ_synth ≳ 20-50%` than `≤10%`, `E8`'s baseline correction would matter
more, not less, than at the tested points.

## What this does NOT establish

1. Does not establish that `P191`-`P194`'s conclusions are "confirmed" —
   the robustness found is a mathematical consequence of one parameter
   regime, not new evidence for the forecasts' own premises (that such
   measurements are achievable at all — never claimed by `P191`-`P194`
   either).
2. Does not establish a materiality verdict for `σ_synth>10%` — the
   wide scan is exploratory, no MCID was pre-registered for it, and
   `1.5×` was not reached at `σ=100%`.
3. `NO_AUTHOR_ERROR`.
