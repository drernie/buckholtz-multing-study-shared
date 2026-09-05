# FINDING P201 — Real X-ray concentration is a real, partial,
# mechanistically-confirmed contributor to `P197`'s `MSZ/M200c` residual
# — for one of two real sources, robust to an extrapolation confound —
# but structurally cannot touch the residual's dominant scatter

**Date:** 2026-09-06
**Claim:** `CLAIM_P201_real_concentration_msz_conversion.md`
**Script:** `P201_real_concentration_msz_conversion.py`
**Continues:** `FINDING_P199` (provenance, confirmed) → `FINDING_P200`
(literature search, Logan et al. 2022, real-but-insufficient,
correlation test blocked by data availability) → this file, third of
the 5-step autonomous follow-up. First genuinely new hypothesis of the
5 steps, found by connecting two already-verified project findings
(`P196_ADDENDUM2`'s real-concentration result and `P197`'s own
Duffy-08-anchored `MSZ→M200` conversion) that were never previously
combined.

## Result

**Positive controls pass** (2/2, both exact round-trips against
already-verified baselines — `P197`'s own solver at `Δ=500`, and
`P196_ADDENDUM2`'s own solver at `Δ=200` — both `<1e-4` relative error).

**Mechanistic prediction confirmed in direction, for both real sources:**
substituting real X-ray concentration for Duffy+08's simulated relation
in the `MSZ→M200`-equivalent conversion moves `mean(MSZ_equiv/M200c)`
down (toward `1.0`), exactly as predicted before running:

| Source | Median concentration used | Mean ratio | Δ vs Duffy+08 baseline |
|---|---|---|---|
| Duffy+08 (simulated, baseline) | 3.50 | 2.5049 | — |
| Buote+07 (real X-ray) | 6.33 | 2.3453 | `-0.1596` |
| Schmidt&Allen+07 (real X-ray) | 9.79 | 2.1889 | `-0.3160` |

Against the pre-registered MCID (`Δmean < -0.2`): Schmidt&Allen+07
crosses it, Buote+07 does not.

## Step 8a skeptic pass (context-blind, claim + code only) — verdict:
## WEAKENED, with one concrete, checkable, and then directly-tested
## confound

The skeptic independently reproduced every number bit-for-bit against
the live catalog and confirmed both positive controls, the mechanistic
direction, and the absence of a `Δ`-convention circularity or `h`-factor
bug (`DISMISSED` on both). It raised one real, quantified concern:

> **`99.2%` of the HeCS-SZ sample sits below Schmidt&Allen+07's own
> pivot mass** (`~1.14×10¹⁵ M_☉` at `h=0.7`), and their steeper mass
> slope (`a=-0.45` vs Buote's `α=-0.172`) produces astrophysically
> implausible concentrations (`c_vir > 10` for `44.7%` of the sample,
> `median c=9.79`) when extrapolated into this lower-mass regime — a
> concrete, mechanistic alternative explanation for why Schmidt&Allen+07
> alone crosses the MCID: extrapolation artifact, not a more faithful
> real measurement.

**Follow-up run immediately after the skeptic pass** (per the
skeptic's own suggested check, added to `P201_real_concentration_msz_
conversion.py`): restrict to the `20/123` clusters with `MSZ ≥ 0.5×`
Schmidt&Allen's own pivot mass, where their concentration comes out
physically reasonable (`median c=6.66`, `0%` with `c>10`, vs `44.7%` on
the full sample). **The Schmidt&Allen+07 crossing survives on this
sub-sample** (`Δ=-0.2461`, still `< -0.2`; Buote+07 still does not
cross, `Δ=-0.1349`). This does not fully dismiss the skeptic's concern
(the full-sample number is still partly extrapolation-inflated), but it
shows the effect is not *purely* an extrapolation artifact — it
persists, smaller but still MCID-crossing, in the regime where
Schmidt&Allen's relation is legitimately calibrated.

## A second skeptic finding, more important than the first, and general
## to this entire line of investigation

> **Scatter (`74.5%→74.6%→74.5%`) is essentially invariant across all
> three concentration sources — and this is close to a mathematical
> necessity of the method, not a coincidence.** Every cluster at the
> same `(MSZ, z)` receives an *identical* concentration under any of
> these population-mean `c(M,z)` relations — none use a per-cluster
> measured concentration. A smooth, deterministic reparameterization of
> `MSZ→MSZ_equiv` can only ever shift the *mean* of
> `MSZ_equiv/M200c`; it cannot explain point-to-point scatter that comes
> from real cluster-to-cluster deviations from whichever mean relation
> is assumed.

This is the more consequential finding: it means **no future candidate
mean concentration-mass relation — real, simulated, or otherwise —
could ever close the dominant `74.5%` scatter component of `P197`'s
residual through this specific conversion step**, only re-center its
mean. The residual's scatter, not just its offset, is what makes
`M200c` and `MSZ` genuinely disagree cluster-by-cluster; a mean-only
correction, however real, leaves that untouched.

## Verdict

**Real, mechanistically-confirmed, partial contributor** — for one of
two real concentration sources (Schmidt&Allen+07), robust to a real
extrapolation confound the skeptic identified and this file then
directly tested. Not confirmed for the other (Buote+07), which misses
the pre-registered MCID on both the full sample and the restricted
sub-sample. And, per the skeptic's second, more general finding,
**structurally incapable of touching the residual's dominant scatter
component** regardless of which concentration source is used — the
same "real, partial, insufficient" pattern as every other tested
candidate in the `P196`-`P201` line, but now with an honest, quantified
reason why *no* future candidate in this specific family (mean
concentration-mass reparameterization) could ever fully close it.

## What this does NOT establish

1. Does not establish Schmidt&Allen+07's own relation as more correct
   than Buote+07's for HeCS-SZ's specific population — the two real,
   independent measurements disagree with each other (median `c=6.33`
   vs `9.79`) by an amount comparable to the effect being tested.
2. Does not close `P197`'s own residual — even the surviving,
   sub-sample-robust Schmidt&Allen+07 effect (`Δ=-0.25` to `-0.32`) is
   a fraction of the `~1.5` (mean ratio `2.5`) gap to `1.0`.
3. Does not, and per the scatter-invariance argument above cannot ever,
   address the `74.5%` scatter that is the residual's dominant
   component — only its mean.
4. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction.

## Where this leaves the whole residual-investigation line

Across `P196`-`P201`, five named or discovered candidate mechanisms
have now been tested, each real data, positive controls, and (for the
two most consequential, P196-P198 and this file) Step 8a skeptic
review:

| Candidate | Verdict |
|---|---|
| Concentration scatter (`ADDENDUM`) | Ruled out — negligible |
| Concentration source, for `P196`'s own ratio (`ADDENDUM2`) | Ruled out algebraically — `R500` cancels there |
| Mass-measurement method, caustic vs SZ (`P197`) | Real (`2.5×` disagreement), insufficient alone |
| Girardi's own `R_c` inconsistency (`P198`) | Real (`~14%` shift), extrapolation-bound, insufficient alone |
| Caustic sparse-sampling bias (`P200`, literature) | Real, directionally consistent, `BLOCKED` on direct within-dataset test (no `Ng` data available) |
| Concentration source, for `P197`'s `MSZ→M200` conversion (`P201`) | Real for one of two sources, mean-only by construction, insufficient alone |

**No single tested mechanism, across six candidates now, closes any of
the residuals in this investigation.** A genuinely new, structural
finding emerges from this specific step: `P197`'s residual is
dominated by *scatter*, not offset, and mean-relation corrections of
any kind are structurally the wrong tool for that — a real constraint
on what future work in this direction could accomplish, not previously
stated anywhere in `P196`-`P200`.
