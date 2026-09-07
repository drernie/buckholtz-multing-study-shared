# FINDING P220 — propagating v82's own two QUOTED nuisance uncertainties
# (B, C) through the frozen fit makes the model undefined (H² < 0 somewhere
# on the grid) in 26% of draws, and moves χ²₃₃ across a range that dwarfs
# MULTING's own margin over flat ΛCDM

**Date:** 2026-09-07
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Artifact:** `P220_joint_BC_uncertainty_propagation.py`
**Answers:** `docs/158` item 3 (joint uncertainty propagation through the
`F^(1)`/`F^(2)` near-cancellation v82 itself admits, Table III /
~lines 1514, 1721)

---

## 1. Scope — deliberately narrow, and why

v82 quotes a real statistical uncertainty for exactly **two** of the inputs
feeding `k(z)`: the mass-gas-fraction scaling exponents from an independent
3061-cluster X-ray sample (Ramos-Ceja et al., **v82:440**):

> `B = 2.24 ± 0.03`, `C = −1.00 (+0.29/−0.30)`

No other input in `multing_core.py` carries a quoted statistical
uncertainty. In particular `T0_keV = 3.7163` is **not** measured — v82:
404-420 states it is *recalibrated*, chosen so the implied gas fraction
sits at `0.13` (an earlier `T0=6.0 keV` gave gas fractions `0.35-0.37`,
rejected as unrealistic), and admits directly:

> *"There is no single T₀ that simultaneously satisfies realistic gas
> fractions and realistic mass-temperature normalization"* — implied
> temperature `~3.3-3.6 keV` here vs `~7 keV` independent weak-lensing
> scalings would suggest for the same mass.

That is a stated **systematic** tension, not a statistical error bar.
Sampling it via a Gaussian draw would fabricate precision that does not
exist. It is probed here as one labelled **scenario**, not a Monte Carlo
input.

`(β₁, β₂, H0_anchor)` are held **fixed** at v82's own frozen fitted point
throughout — this measures how much `(B,C)` measurement uncertainty alone
moves the outcome, not whether a re-optimized fit would compensate.

## 2. Controls — both exact

**PC1**, v82's own printed fractional decomposition at `z=1.07`
(`generate_all_results.py:183-187`'s own normalization,
`gross = |F0|+|F1|+|F2|+|Facc|`, each term as %-of-gross):

| term | computed | paper |
|---|---:|---:|
| `F0` | −0.06 % | −0.06 |
| `−F1` | 53.04 % | 53.04 |
| `F2` | −46.54 % | −46.54 |
| `net` | 6.09 % | 6.09 |

**PC2**: `χ²₃₃(B=2.24, C=−1.00) = 15.75` — exact match to v82's own Table II.

## 3. Result — the near-cancellation quantified across `z`

Monte Carlo, `N=20000`, `B ~ Normal(2.24, 0.03)`, `C` drawn asymmetrically
matching the quoted `+0.29/−0.30`:

| `z` | `−F1%` mean±std | `F2%` mean±std | `net%` mean±std | sign flips |
|---:|---:|---:|---:|---:|
| 0.280 | 51.22 ± 0.33 | −48.42 ± 0.33 | 2.44 ± 0.65 | 0.03 % |
| 0.593 | 52.42 ± 1.51 | −47.20 ± 1.54 | 4.84 ± 3.02 | 5.43 % |
| 1.070 | 53.07 ± 3.55 | −46.51 ± 3.64 | 6.14 ± 7.10 | 19.13 % |
| 1.965 | 52.99 ± 6.80 | −46.49 ± 7.01 | 5.99 ± 13.59 | 33.05 % |

The individual `F1`/`F2` percentages barely move (std under a few percent
of gross even at `z=1.965`) — but because they sit at ~53% and ~−46.5%,
**the small individual scatter lands almost entirely on the ~6% net
remainder**, and the fraction of draws where the net sign flips (dipole
vs. quadrupole dominance reverses) climbs from negligible at low `z` to
**one draw in three** at `z=1.965`. This is exactly the fragility v82's own
Table III language describes qualitatively, now measured.

## 4. Result — fit quality collapses under (B,C) alone

`χ²₃₃` distribution, same MC, `(β₁,β₂,H0_anchor)` unchanged:

| | value |
|---|---:|
| at `(B,C)` mean (= v82's own reported value) | 15.75 |
| MC mean | 772.92 |
| MC std | 854.06 |
| MC 5th–95th percentile | **[24.0, 2194.0]** |
| fraction with `H² < 0` somewhere on the grid | **26.00 %** |
| flat-ΛCDM benchmark, for scale (no B/C dependence) | 16.31 |

**The MULTING fit's entire published advantage over flat ΛCDM is
`16.31 − 15.75 = 0.56` in `χ²`.** The 5th-percentile alone under `(B,C)`
uncertainty (`24.0`) already exceeds the ΛCDM benchmark; the median and
mean are an order of magnitude worse. And in one draw in four, the model
does not evaluate at all (`H² < 0` on part of the grid) — a q  ualitatively
stronger failure than a bad `χ²`.

## 4a. Self-check — the sensitivity is not a Monte Carlo tail artifact

Before trusting §4's headline numbers, ran a 1-D scan holding one parameter
at its quoted mean and stepping the other by whole σ — the cheapest
possible way to check the MC result isn't driven by a narrow sampling
artifact:

| `C` (B fixed at 2.24) | σ | `χ²₃₃` |
|---:|---:|---:|
| −1.900 | −3σ | 1573.0 |
| −1.600 | −2σ | 1538.1 |
| −1.300 | −1σ | 930.3 |
| −1.000 | 0 | **15.75** |
| −0.710 | +1σ | **NaN** |
| −0.420 | +2σ | NaN |
| −0.130 | +3σ | NaN |

| `B` (C fixed at −1.00) | σ | `χ²₃₃` |
|---:|---:|---:|
| 2.15 | −3σ | 125.1 |
| 2.18 | −2σ | 68.0 |
| 2.21 | −1σ | 29.8 |
| 2.24 | 0 | **15.75** |
| 2.27 | +1σ | 32.5 |
| 2.30 | +2σ | 88.8 |
| 2.33 | +3σ | 196.3 |

**A single-parameter, one-sigma shift in `C` alone — well inside its
quoted uncertainty — either multiplies `χ²` by ~60× or makes the model
undefined. A one-sigma shift in `B` alone (a tight ±1.3% relative
uncertainty) already roughly doubles `χ²`.** The optimum is not merely
imprecise; it sits at a sharp, narrow ridge in `(B,C)` space. This
confirms §3-§4's Monte Carlo result is not a sampling-tail artifact — the
sensitivity is visible in the cheapest possible single-parameter check.

## 5. The T0 scenario — not sampled, but probed, and it breaks

| `T0` | label | `χ²₃₃` |
|---|---|---:|
| 3.716 keV | default (gas-fraction-calibrated) | 15.75 |
| 5.358 keV | halfway to weak-lensing `~7 keV` | **NaN** |

Moving `T0` only **halfway** toward the value v82's own cited independent
weak-lensing scalings would suggest — without touching `(β₁,β₂,H0_anchor)`
at all — makes `H² < 0` somewhere on the grid. The model does not merely
fit worse under this shift; it stops evaluating.

## 6. What this does and does not establish

**Establishes:** with the fitted parameters held fixed, the model's output
is highly sensitive to two inputs that v82 itself quotes real uncertainty
for, and to a third (`T0`) it admits has no single consistent value at
all. The published `χ²=15.75` and the model's evaluability itself are not
robust to nuisance-parameter uncertainty that v82's own text supplies.

**Does not establish:** that a **refit** of `(β₁,β₂,H0_anchor)` at
perturbed `(B,C)` would fail similarly — that is untested, and could in
principle partially compensate (or could widen the picture further; this
project does not know which). Does not establish that flat ΛCDM is
preferred once ΛCDM's own nuisance parameters are propagated the same way
(not attempted here — ΛCDM's `χ²=16.31` in the comparison above is a fixed
Planck-value benchmark, not itself uncertainty-propagated).

**Consistent with, and quantifies, v82's own admitted language**
(near-cancellation, Table III) rather than contradicting anything the
paper states.

## 7. Caveats

1. Only 2 of the several nuisance inputs to `k(z)` carry a quoted
   uncertainty; this is a lower bound on total fragility, not a full
   accounting.
2. `(β₁,β₂,H0_anchor)` not re-optimized per draw — by design (§1), but
   this means the result characterizes sensitivity **at the published
   optimum**, not the sensitivity of a re-fit procedure.
3. `C`'s asymmetric uncertainty was sampled via a folded-normal
   approximation on each side, not the paper's own (unstated) exact
   distributional form.
4. No Step 8a pass on this finding.
