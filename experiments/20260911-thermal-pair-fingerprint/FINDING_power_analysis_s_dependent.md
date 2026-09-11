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

---

## 4. What this does NOT establish

1. The sign-near-crossing sub-check in `estimand.md`'s own PROMOTE
   region ("the highest-`ξ` stratum shows sign consistent with the
   predicted crossing") is **not implemented** in this script's
   `promote()` — only the two AIC/`z`-test comparisons are. Named, not
   silently folded in.
2. The `[20,160]` Mpc population window is carried forward from the old
   design, **not independently re-verified** against the source kSZ
   paper's own methods section — `estimand.md`'s own Population
   criterion still names that as open.
3. The small-`s` Consistency (d) instrumental threat (CMB-beam
   blending/deblending) is handled here only by a blanket
   `S_MIN_VALID=10` Mpc cut — **not** the real angular-separation-vs-
   beam-size check `estimand.md` itself says is still needed. The
   5 pairs driving §2's headline result sit at `s≈10.5-11.6` Mpc,
   **close to that same cut** — worth flagging explicitly: §2's result
   would be the first place a small-`s` instrumental artifact could
   masquerade as a Positivity success, and this has not been checked.
4. Real power will be lower than every number above — these are
   best-case, confounder-free upper bounds; the synthetic four-world
   identifiability battery has not run.
5. Not a claim about MULTING (`NO_AUTHOR_ERROR`) — entirely about
   whether this project's own reconstructed test design is statistically
   viable and whether its own Positivity assumption holds on real
   geometry.

## Status

**Computed, `[VERIFIED-run]`. Two real results, kept separate:**

```
Positivity (xi_pred > crossing, no scatter): CONFIRMED on 3.978% of
  real pairs (306/7693) -- stronger basis than the old scatter-only
  argument, but flagged against caveat #3 above (small-s instrumental
  risk, untested).
Power at Fork-2 scale (N~449, 3x noise, two-part bar): 98.6% -- real,
  comparable to the old design's own N=449 number, with a strictly
  harder pass bar.
Power at smaller, un-capped N (this design's real advantage): a full
  curve now exists (10-2000 pairs) -- no window-width ceiling.
```

Next, in order, none built yet: (1) the real angular-separation-vs-
beam-size check for Consistency (d), specifically re-examining whether
§2's own closest pairs survive it; (2) the sign-near-crossing PROMOTE
sub-check; (3) the synthetic four-world identifiability battery
(`estimand.md`'s own hard pre-data gate) — still the requirement before
any real kSZ/tSZ data is touched.
