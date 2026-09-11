# FINDING — mock-catalog power analysis for the s-dependent design:
# a real, deterministic Positivity result, plus real power numbers

**Date:** 2026-09-11
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Artifact:** `power_analysis_s_dependent.py` — real code, real output,
`[VERIFIED-run]` (18m20s real runtime, `N_MC=4000` per cell, 39 cells).
**Continues:** `estimand.md`'s own 4th-pass amendment (s-dependent
Endpoint/Summary Measure), which named this exact script — a new mock-
catalog power analysis, reusing real `(z,s)` — as the concrete next
artifact, not built at amendment time.

**[SUPERSEDED IN PART, 2026-09-11, same day, see `FINDING_sutva_
dependency_correction.md`.]** An external review of the published repo
found the sampling in §3 below violated `estimand.md`'s own SUTVA
exclusion rule (a real cluster could appear in >1 sampled pair per
trial — 43.2% did, at `N=449`). Verified, fixed (real cluster-disjoint
matching, sampling without replacement). **The headline `59.9%` power
number at `N=449` is WITHDRAWN — the corrected number is `59.1%`**
(within Monte Carlo noise of the withdrawn one, for a specific, reported
reason: this mock has no per-cluster shared latent variable). The
Positivity fraction moved more: `3.978%→4.664%`. This file's own numbers
below are kept for the historical record (mark-don't-erase); read the
correction file for what actually holds now.

---

## 1. What this is, and what it is NOT

Same scope discipline as `power_analysis_mock_catalog.py`: entirely
mock/synthetic outcome data (`y`), on REAL `(z,s)` covariates. No kSZ/
tSZ map touched; `estimand.md`'s own Pre-Data Requirement (the synthetic
four-world identifiability battery) has still not run and is not
satisfied by this script. Every power number below is a best-case,
confounder-free upper bound.

---

## 2. The headline result: Positivity is no longer merely plausible

**`estimand.md`'s own Positivity check named this as "the cheapest
possible check" — computed here for the first time, deterministically,
no scatter assumption:**

```
xi_pred(z,s) over 7693 real ACT-DR5 MCMF pairs (s in [10,160] Mpc
comoving, z in [0.2,0.8]):
  min    = 9.18e-09
  median = 1.24e-08
  max    = 1.42e-07
xi_crossing = 3.669e-08

Fraction of REAL pairs with xi_pred > xi_crossing: 3.978%
```

**306 real cluster pairs, purely from their own measured `(z,s)` and
`v82`'s own trajectory `Q(z)`, already sit in the net-repulsive regime
— with zero appeal to `FINDING_E13`'s mass scatter.** The five closest
pairs span a real range of redshift (`z=0.277` to `z=0.574`), not one
coincidental object:

| z | s (Mpc) | `ξ_pred` | vs. crossing |
|---|---|---|---|
| 0.574 | 10.49 | `1.423e-7` | `3.9×` above |
| 0.277 | 11.19 | `1.397e-7` | `3.8×` above |
| 0.436 | 11.04 | `1.376e-7` | `3.7×` above |
| 0.542 | 11.33 | `1.322e-7` | `3.6×` above |
| 0.477 | 11.56 | `1.306e-7` | `3.6×` above |

**This is a materially stronger basis for Positivity than the old
design had.** `claim.md` §4's own argument ("a 63%-per-1σ scatter
comfortably covers a 14% gap") was a plausibility argument about
population scatter around one trajectory value. This result needs no
scatter argument at all — real, close pairs cross the threshold from
separation alone, because `ξ∝1/s` and real pairs get much closer than
`v82`'s own `45` Mpc trajectory separation. `estimand.md`'s Endpoint
section named this consequence and flagged it "not yet checked" — it is
now checked, and it holds.

**Caveat, stated as plainly as the result:** this is `ξ_pred`, the
model's own deterministic central prediction from real `(z,s)` — it is
**not** a claim that any real pair's OBSERVED dynamics has been checked
against it. No kSZ/tSZ data has been touched. This closes a
plausibility gap in the design, not the causal question itself.

---

## 3. Power results

Full grid, `N_pairs` bootstrap-resampled from the real 7693-pair pool,
`ΔAIC>6` on **both** comparisons (Model 1 beats Model 0 **and** beats
Model 2) **and** `|z_λ|>1.96` — matching `estimand.md`'s own two-part
PROMOTE bar, stricter than the old design's one-part (beat null only)
bar:

| N_pairs | 1x noise | 3x noise | 10x noise |
|---|---|---|---|
| 10 | 40.7% | 3.7% | 1.3% |
| 20 | 71.5% | 5.6% | 0.7% |
| 30 | 83.5% | 10.4% | 1.1% |
| 50 | 94.2% | 19.2% | 0.9% |
| 75 | 98.0% | 32.2% | 1.0% |
| 100 | 99.7% | 44.9% | 1.9% |
| 150 | 99.9% | 65.6% | 3.2% |
| 200 | 100.0% | 80.4% | 3.9% |
| 300 | 100.0% | 93.7% | 7.0% |
| **449** | 100.0% | **98.6%** | 14.0% |
| 500 | 100.0% | 99.2% | 16.2% |
| 1000 | 100.0% | 100.0% | 44.0% |
| 2000 | 100.0% | 100.0% | 82.8% |

False-promote rate stayed low throughout (`0.1%-1.2%`, below nominal
`α=0.05`) — the two-part bar is, if anything, conservative.

**Comparison to the old (window-based, REJECTED) design at the same
footprint-scaled `N=449`:** old design, one-part bar, `100.0%` power
@3x noise; new design, two-part bar, `98.6%` power @3x noise, `0.2%`
false-promote. **Read this carefully, not naively:** the new design is
NOT more per-pair-efficient than the old one — its bar is strictly
harder to clear (beat two competing models, not one), so a slightly
lower power at matched `N` is expected, not a regression. **The real
payoff is not shown by comparing at N=449** — it is that this design is
not capped at a window's `18-53` pairs the way `NR-025` showed the old
design had no principled way to exceed. The full real population here
is `7693` pairs (or `449` at the Fork-2 mid-footprint linear scaling) —
either is directly usable, with no window-width decision to make at
all.

**[SUPERSEDED, same day, by §3a below]** The `98.6%` two-part-bar
number above is an intermediate result, not the final one — §3a adds
the sign-near-crossing sub-check estimand.md's own PROMOTE region
requires, dropping `N=449`'s power to `59.9%` under the complete,
three-part bar. Kept here, struck through in spirit not deleted, so the
size of that specific cost is visible.

---

## 3a. [ADDED, same day] The sign-near-crossing sub-check — implemented,
## a real and substantial power cost

`estimand.md`'s own PROMOTE region requires a third condition beyond
the two AIC/`z`-test comparisons already run: *"the highest-`ξ`
stratum shows sign consistent with the predicted crossing (not merely
a steeper slope)."* Not implemented in §3 above — implemented here.

**Operationalization, stated as a deliberate, honest choice, not a
literal reading of "crossing":** `S_M(ξ)=2β₁ξ-β₂ξ²` is a downward
parabola, rising for `ξ<ξ_peak` and falling for `ξ>ξ_peak`, where
`ξ_peak=β₁/β₂=1.836×10⁻⁸`. This is close to but **not** `ξ_crossing
=3.669×10⁻⁸` (`ξ_crossing` solves `S_M(ξ)=1`, the point the TOTAL force
changes sign; `ξ_peak` solves `dS_M/dξ=0`, the point the CORRECTION
TERM's own slope changes sign — they are numerically close only because
`S_M`'s peak value, `~263`, is so far above `1` that both roots of
`S_M=1` sit near `S_M`'s own zero-crossings). This script stratifies at
`ξ_peak`, not `ξ_crossing`, for a real, checked reason: real pairs
above `ξ_crossing` are rare (`306/7693=3.98%`), too few for a per-trial
stratified slope fit at realistic `N`; real pairs above `ξ_peak` are
common (`1457/7693=18.9%`, `[VERIFIED]` on the real pool), making the
check statistically usable. The sub-check tests the same qualitative
non-monotonic REVERSAL that produces the eventual crossing, not the
literal crossing point itself.

**Sanity check before trusting the full run:** a single `n=500` trial
under `H_M` true showed `sign_low=+1, sign_high=-1` (exactly the
predicted pattern, with `z_λ=7.79`, `ΔAIC₀₁=55.5`, `ΔAIC₂₁=12.8` — all
strongly significant); the same check under `H_0` true showed
`sign_low=-1, sign_high=+1` (the WRONG pattern, correctly rejected)
with weak, insignificant AIC/`z` statistics. The check behaves as
designed before being trusted on the full scan.

**Full re-run, `N_MC=4000`, all three conditions required jointly**
(auto-fails if either stratum has `<5` points):

| N_pairs | 1x noise | 3x noise | 10x noise |
|---|---|---|---|
| 10 | 0.3% | 0.0% | 0.0% |
| 20 | 12.7% | 1.1% | 0.1% |
| 30 | 36.6% | 3.7% | 0.4% |
| 50 | 63.4% | 12.2% | 0.5% |
| 75 | 70.0% | 21.4% | 0.7% |
| 100 | 73.6% | 31.0% | 1.2% |
| 150 | 73.6% | 42.6% | 2.1% |
| 200 | 74.3% | 51.1% | 2.7% |
| 300 | 75.0% | 56.9% | 4.4% |
| **449** | 77.8% | **59.9%** | 8.5% |
| 500 | 78.1% | 60.1% | 10.2% |
| 1000 | 82.8% | 62.2% | 26.3% |
| 2000 | 87.9% | 66.0% | 47.7% |

False-promote stayed low throughout (`0.0%-0.1%`), if anything lower
than the two-condition run — the third condition makes the test more
conservative on the null side too, not just harder to pass under `H_M`.

**The headline comparison, updated: at `N=449` (Fork-2 mid footprint),
3x noise, power drops from `98.6%` (two-part bar) to `59.9%`
(three-part bar) — a real, substantial, and honestly-reported cost.**
This is not a design flaw: the sign-near-reversal condition is a
genuinely harder, more specific requirement (a real non-monotonic
feature, not just an amplitude fit), and `power_analysis_mock_
catalog.py`'s own analogous old-design number (`100.0%`) never had to
clear anything like it. Power collapses toward `0%` at small `N`
(`N=10`: `0.0-0.3%` across all noise levels) because the high-`ξ`
stratum (`~19%` of the sample) rarely reaches the `5`-point minimum
needed to fit a trustworthy sign at all — an honest, expected
consequence of the design, not a bug.

## 4. What this does NOT establish

1. `ξ_peak≠ξ_crossing` (§3a) — the sign-near-crossing sub-check is
   operationalized as a sign-near-REVERSAL check at `ξ_peak`, a
   documented, honest choice, not a literal test at `ξ_crossing`
   itself (too few real pairs there for a per-trial stratified fit).
2. The `[20,160]` Mpc population window is carried forward from the old
   design, **not independently re-verified** against the source kSZ
   paper's own methods section — `estimand.md`'s own Population
   criterion still names that as open.
3. **[RESOLVED, same day, see `FINDING_beam_blending_check.md` §3a]**
   The small-`s` Consistency (d) instrumental threat is now checked
   directly for all `306` real Positivity pairs, not just the 5
   illustrated here — `5/306` (`1.6%`) at real risk, blending-risk-
   excluded fraction `3.913%` vs. `3.978%` unfiltered. A small, real,
   quantified correction, not an open unknown.
4. Real power will be lower than every number above — these are
   best-case, confounder-free upper bounds; the synthetic four-world
   identifiability battery has not run. This now applies on TOP of an
   already-reduced `59.9%` (three-part bar), not the earlier `98.6%`.
5. Not a claim about MULTING (`NO_AUTHOR_ERROR`) — entirely about
   whether this project's own reconstructed test design is statistically
   viable and whether its own Positivity assumption holds on real
   geometry.

## Status

**[UPDATED, same day] Computed, `[VERIFIED-run]`. Three real results,
kept separate:**

```
Positivity (xi_pred > crossing, no scatter): CONFIRMED on 3.978% of
  real pairs (306/7693) -- stronger basis than the old scatter-only
  argument. Beam-blending checked directly for all 306 (FINDING_beam_
  blending_check.md): only 5/306 (1.6%) at real risk, blending-risk-
  excluded fraction 3.913% -- essentially unchanged.
Power at Fork-2 scale (N~449, 3x noise), FINAL three-part bar (beat
  Model 0 AND Model 2 AND the sign-near-reversal check): 59.9%, down
  from the intermediate two-part-bar number of 98.6% -- a real,
  substantial, honestly-quantified cost of testing the FULL promote()
  criterion estimand.md actually specifies, not a regression.
Power at smaller, un-capped N (this design's real advantage over the
  window-based one): a full curve now exists (10-2000 pairs) under the
  complete three-part bar -- no window-width ceiling, even though
  absolute power at small N is now honestly much lower than the
  two-part-bar numbers first suggested.
```

Next, in order, none built yet: the synthetic four-world identifiability
battery (`estimand.md`'s own hard pre-data gate) — the last requirement
named in this branch before any real kSZ/tSZ data is touched. Both the
beam-blending threat and the sign-near-crossing sub-check, previously
open, are now closed.
