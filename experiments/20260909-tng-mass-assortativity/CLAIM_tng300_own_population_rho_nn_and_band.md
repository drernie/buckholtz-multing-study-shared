# CLAIM — the real discriminating test named in `FINDING_flamingo_
# addendum_jackknife_band_closure.md`: measure BOTH `rho_NN` and
# `rho_band` on TNG300's OWN population, matching FLAMINGO's own
# selection protocol, instead of comparing FLAMINGO against TNG300's
# published (differently-selected) `+0.38`

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b.
**Continues:** `FINDING_flamingo_addendum_jackknife_band_closure.md`'s
own named next step ("the real discriminating test: compute both
`rho_NN` and `rho_band` on `TNG300`'s OWN population... not attempted
here"). **User-requested**, not self-initiated.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Why this is the real discriminating test

The `TNG300` `+0.38` number that has been cited throughout this branch
was measured on the FULL cached `top_halos_pos_mass.csv` sample
(`N=1461`, mass floor `8.4e12` Msun) — a much denser, non-mass-matched
population, not selected to match v82's own `40-45` Mpc target
separation at all (that sample's own typical NN spacing is `9.2` Mpc,
per `FINDING_scale_matched_nearest_neighbor_rho.md`). Comparing
FLAMINGO's mass-matched `rho_band` (on its own `N=1200` subsample,
selected so typical NN spacing lands in `40-45` Mpc) against this
number is therefore NOT a clean single-axis comparison — simulation
AND selection protocol both differ at once. **This test holds the
selection protocol fixed** (top-N by mass, chosen so BOTH median and
mean true-NN separation land in `40-45` Mpc — FLAMINGO's own protocol)
and changes only the simulation, isolating that one axis.

## Avoiding the reuse of an already-outcome-tainted `N_sub`

`FINDING_scale_matched_nearest_neighbor_rho.md`'s own (FALSIFIED)
nested sweep already computed `r` at `N_sub in {30,40,50,60,80,100}`.
Freezing any of those six values now would not be a blind pre-
registration — their correlation values are already known, so picking
one would be selecting on the outcome, not the scale match, exactly
the failure mode that sweep was falsified for. **This claim freezes a
`N_sub` NOT in that set**, chosen purely from a fresh NN-scale-only
exploratory bracket (`_explore_tng300_own_population_scale.py`, no
correlation computed, matching `_explore_flamingo_scale.py`'s own
role) over new candidate values `{35,42,44,45,46,47,48,52,55,58,65,70,
75}`.

## Pre-registered threshold

```
N_sub = 35 (top-35 most massive halos in the cached top_halos_
             pos_mass.csv, real TNG300 data, no new API call)
exploratory median true-NN separation: 43.92 Mpc
exploratory mean true-NN separation:   42.25 Mpc
```

The ONLY candidate among the 13 scanned whose BOTH median and mean land
inside `[40,45]` Mpc. Genuinely small (`N=35` vs. FLAMINGO's `N=1200`)
— `TNG300`'s own box (`302.6` Mpc physical, `~36x` smaller volume than
`FLAMINGO`) simply does not contain enough sufficiently-massive,
sufficiently-separated halos to match FLAMINGO's statistical power at
this scale, as `FINDING_scale_matched_nearest_neighbor_rho.md`'s own
"effectively zero usable independent boxes" analysis already
established. **This test is explicitly NOT expected to be well-powered
— its value is the qualitative, same-protocol, cross-simulation
comparison, not a new precision measurement.**

## The falsifiable question (two numbers, ONE frozen population)

1. `rho_NN = Pearson r(log M200c_self, log M200c_true-nearest-
   neighbor)` among the `N_sub=35`.
2. `rho_band = Corr(log M_i, log M_j | 40<=s_ij<=45 Mpc)` among the
   SAME `N_sub=35` (symmetrized pairs, same convention as the FLAMINGO
   addendum).

Uncertainty: a proper permutation-null (`>=1000` draws, mass-shuffle),
matching this branch's own established convention — NOT a block-
jackknife, which would be unstable with only `35` halos spread across
the box (too few halos per spatial block for a stable delete-one-block
variance estimate; explicitly a different, size-appropriate choice from
the FLAMINGO addendum, not an inconsistency).

## What this would and would not settle

- **If `rho_band` on this `N=35` TNG300 subsample comes out clearly
  elevated relative to `rho_NN`** (mirroring the qualitative pattern a
  band-vs-NN difference would predict): supports Hypothesis A
  (observable difference) — the band/NN gap shows up within one
  simulation under matched selection, not just across simulations.
- **If both `rho_NN` and `rho_band` are small/near-zero on this matched
  subsample** (mirroring FLAMINGO's own pattern): supports Hypothesis B
  (the historical `+0.38` was a population/selection effect — matching
  the selection to `40-45` Mpc removes it in BOTH simulations, not just
  one) — though at `N=35` this reads as consistent-with-B, not a
  decisive confirmation, given the small sample.
- **Given the expected low power (`N=35`), a genuinely INCONCLUSIVE
  outcome (wide CI compatible with both hypotheses) is a legitimate,
  pre-anticipated result** — to be reported as such, not forced toward
  either hypothesis.
- **Does NOT** resolve whether "top-N-most-massive-halos" is the right
  operational definition of v82's own "node" (unchanged, open question
  across this entire branch).
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked to check: (a)
whether `N_sub=35`'s selection is genuinely blind to outcome (not
picked because its correlation looked interesting), (b) whether the
permutation-null approach is appropriate at this small `N`, (c) whether
any conclusion drawn (A / B / inconclusive) is actually licensed by the
resulting statistical power.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
