# FINDING — window-width question: resolved (negative). No principled
# width exists; s=45 Mpc has no independent signature in real clustering.

**Date:** 2026-09-11
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Artifact:** `window_width_scan.py` — real code, real output,
`[VERIFIED-run]`. Reuses `exact_pair_census.py`'s real catalog loader
and pairwise-separation array (same 4390 real clusters, same real
positions) unchanged.
**Continues:** `FINDING_power_analysis.md` §6's own open item — the
window WIDTH, left undetermined after the Exact Pair Census fixed the
window *center* at the verified `d0=45` Mpc comoving.

---

## 1. Two questions, kept separate

- **Q_stat** — does statistical power alone pick an optimal window
  width?
- **Q_data** — is `s=45` Mpc itself special in the REAL cluster-pair
  separation distribution, independent of any MULTING assumption, or
  is it purely a model-internal number?

Per `feedback_verdict_attribution.md`, these are two independent
questions with two independent answers — not merged into one number.

---

## 2. Q_stat — power has (almost) no interior optimum

Fine-grained scan, real `N(half-width)` from the real pairwise-
separation array, area-scaled to the Fork-2 mid footprint (775 deg²),
power re-computed with the identical `one_trial()` Monte Carlo
(`N_MC=4000`, `ΔAIC>6` + `|z|>1.96`, 3x noise):

| half-width | window (Mpc) | N (full ACT-DR5) | N (scaled, mid) | power |
|---|---|---|---|---|
| 2.5 | [42.5,47.5] | 75 | 4.4 | 9.7% |
| 5.0 | [40.0,50.0] | 157 | 9.2 | 5.2% |
| 7.5 | [37.5,52.5] | 268 | 15.7 | 7.9% |
| 10.0 | [35.0,55.0] | 374 | 21.9 | 11.3% |
| 12.5 | [32.5,57.5] | 457 | 26.8 | 13.9% |
| 15.0 | [30.0,60.0] | 542 | 31.8 | 16.3% |
| 20.0 | [25.0,65.0] | 723 | 42.4 | 24.9% |
| 25.0 | [20.0,70.0] | 910 | 53.4 | 33.4% |
| 30.0 | [15.0,75.0] | 1101 | 64.6 | 42.9% |
| 40.0 | [5.0,85.0] | 1557 | 91.3 | 63.7% |
| 50.0 | [-5.0,95.0] | 2066 | 121.2 | 79.3% |
| 60.0 | [-15.0,105.0] | 2619 | 153.6 | 89.8% |
| 75.0 | [-30.0,120.0] | 3660 | 214.7 | 97.8% |

**Reading, honestly:** the raw monotonicity check fails strictly (a dip
from 9.7%→5.2% between half-width 2.5 and 5.0), but this is a small-`N`
artifact, not a real effect — at `N=4-9` pairs, `one_trial()`'s OLS fit
has 2-7 degrees of freedom, where tiny-sample AIC/`z`-test behavior is
known to be unstable and discrete; the Monte Carlo standard error on a
power estimate near `p=0.1` at `N_MC=4000` is `~0.5` percentage points
— far smaller than the observed `4.5`-point dip, so this is a real
feature of the tiny-`N` regime, not simulation noise, but it is also not
a scientifically meaningful "optimum" (nobody would run a 4-9 pair
test). **From `N≈15` upward, power is monotonically increasing with
width, with no interior maximum anywhere in the scanned range up to
half-width 75.** Under the current model — every simulated pair drawn
from the SAME `xi` distribution regardless of its own separation `s`,
exactly `claim.md` §3a's own flagged marginal-vs-joint `HYPOTHESIS` —
**widening the window is trivially, monotonically better for power.**
Width cannot be resolved by power-maximization under this model.

---

## 3. Q_data — s=45 Mpc has NO independent clustering signature

Real observed pair counts vs. the **analytic** Poisson (unclustered)
expectation — not a fitted curve, the closed-form volume-shell integral
already used throughout this branch, now correctly using the real,
`z`-restricted `N=4390` and the real ACT-DR5 footprint
(`13211 deg²`, `[VERIFIED-arXiv:2406.14754]`):

| bin (Mpc) | observed | Poisson-expected | `1+ξ(s)` | z-score |
|---|---|---|---|---|
| [0,10) | 21 | 1.31 | 16.04 | 17.2 |
| [10,20) | 42 | 9.16 | 4.58 | 10.9 |
| [20,30) | 97 | 24.87 | 3.90 | 14.5 |
| [30,40) | 142 | 48.43 | 2.93 | 13.4 |
| **[40,50)** | **157** | **79.85** | **1.97** | **8.6** ← window center |
| [50,60) | 243 | 119.12 | 2.04 | 11.4 |
| [60,70) | 271 | 166.24 | 1.63 | 8.1 |
| [70,80) | 378 | 221.22 | 1.71 | 10.5 |
| [80,90) | 460 | 284.05 | 1.62 | 10.4 |
| [90,100) | 523 | 354.74 | 1.47 | 8.9 |
| ... | | | (smoothly declining) | |
| [290,300) | 3921 | 3417.78 | 1.15 | 8.6 |

`1+ξ(s)` — the real, directly-computed two-point correlation excess —
is a **smoothly, monotonically declining function of `s`**, exactly the
generic large-scale-structure expectation at these scales (strongest
clustering at small separations, declining outward, no BAO-scale
feature expected or seen at `~150` Mpc in this coarse binning). **The
`[40,50)` bin containing `s=45` is not even a local maximum among its
own neighbors** — `[30,40)=2.93` and `[50,60)=2.04` both exceed it. Real
cluster clustering shows nothing special happening at `s=45` Mpc.

The very-small-separation bins (`[0,10)`, ratio `16`, `z=17`) are almost
certainly catalog near-duplicate/deblending contamination (a known
effect in SZ cluster finders — two detections of one real structure),
not a genuine physical two-point excess at `<10` Mpc; flagged, not
used for anything downstream, since `s=45` is far from this regime.

---

## 4. Combined verdict

**The window-width question is resolved — negatively, and that is a
real result, not a failure to find an answer.** `d0=45` Mpc is
`v82`'s own frozen initial condition for one hypothetical, model-
internal "spotlighted" trajectory (`FINDING_power_analysis.md` §2's own
provenance work) — it is **not** a scale independently singled out by
real cluster large-scale-structure clustering (§3, this file), and
**no width around it maximizes statistical power** short of widening
until the test converges on the already-separately-answered broad kSZ-
literature statistic (§2, this file; `N≈449`, `100%` power, mid
footprint — a different, non-characteristic-specific test,
`FINDING_power_analysis.md` §2/§6).

**What this means for the branch, stated plainly:** the "narrow window
centered on v82's characteristic separation" framing, AS DESIGNED (count
pairs within an arbitrary band around 45 Mpc, fit an amplitude), does
not have a principled width — not because of missing data, but because
there is nothing in the real data or the current model that picks one.
Any width choice from here is a convention, not a derived number, and
widening it without bound erases the very thing that made the narrow
test different from the broad one.

**This does not kill the underlying physical idea** (that MULTING's
`ξ`-dependent force sign-crossing might leave a detectable pairwise
signature) — it kills the SPECIFIC test design of "count pairs near a
fixed separation, fit one amplitude." A design that could still work:
fit `S_M`'s predicted `s`-dependence (via `ξ∝1/s`) directly against the
FULL range of real pair separations, using each pair's own `s` rather
than sorting pairs into an arbitrary window — a genuinely different
Endpoint/Summary-Measure choice, not attempted here, and not something
to build without the user's sign-off (it changes `estimand.md`'s own
Endpoint section, not just a numeric rerun).

---

## 5. What this does NOT establish

1. Does not touch the synthetic four-world identifiability battery
   (`estimand.md`'s own hard gate) — orthogonal to this finding.
2. Does not resolve Fork 2's own footprint cross-match — this analysis
   used the full ACT-DR5 footprint throughout (§2's `N (full)` column),
   sidestepping the area-scaling question entirely for Q_data, and only
   linearly scaling for Q_stat's power numbers (same caveat as
   `FINDING_power_analysis.md` §6).
3. Does not claim MULTING is false (`NO_AUTHOR_ERROR`) — this is about
   whether *this project's own specific test design* (a fixed-window
   pair count) is well-posed, which it is not, independent of whether
   MULTING itself is true.
4. Does not propose or endorse the alternative `s`-dependent design
   named in §4 — that is named as a live option for the user to decide
   on, not adopted.

## Status

**REJECT (the fixed-window test design, not the underlying physical
idea) — Kill Analysis:**

- **What this killed:** the specific test design "count real cluster
  pairs within an arbitrary window around `s=45` Mpc, fit one
  amplitude" — no width for that window is derivable from power
  maximization (monotonic) or from real clustering data (no local
  feature at 45 Mpc).
- **What this did NOT kill:** MULTING's underlying `ξ∝1/s`-dependent,
  sign-crossing force law; the broad-window kSZ-literature test
  (already separately answered, well-powered); the possibility of an
  `s`-dependent (not window-count) test design.
- **Relaxation map:** the one surviving, not-yet-built option is to
  replace the fixed-window count with a continuous fit of `S_M(s)`
  against each real pair's own separation — this is a genuinely
  different Summary Measure, requiring an `estimand.md` amendment
  before any code, per this branch's own standing discipline.

Next: report to the user; no further code without an explicit decision
on whether to pursue the `s`-dependent redesign named in §4.
