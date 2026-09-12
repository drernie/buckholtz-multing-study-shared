# CLAIM — third independent cross-check of scale-matched nearest-
# neighbor rho, using real FLAMINGO L1_m9 data (third distinct
# cosmology, ~114x TNG300's volume, single PRE-REGISTERED threshold —
# explicitly designed to avoid the nested-sweep trap that falsified
# both prior attempts)

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b.
**Continues:** `CLAIM_scale_matched_nearest_neighbor_rho.md` (TNG300,
FALSIFIED — nested sweep, single-shuffle null) and `CLAIM_magneticum_
independent_rho_check.md` (Magneticum, FALSIFIED — SAME nested-sweep
trap recurred even with a proper permutation null).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## What is different this time — a genuine design fix, not a repeat

Both prior attempts swept multiple NESTED mass-rank thresholds and
(the second time, even with a real permutation null) still fell into
treating several heavily-overlapping sub-samples as if they were
independent confirmations. **This design fix removes the trap at its
root: ONE single N_sub is pre-registered below, chosen from an
EXPLORATORY bracketing pass (`_explore_flamingo_scale.py`, not a
claim) before this file was written, and no other threshold will be
analyzed as part of the primary test.** This directly avoids the
look-elsewhere/nesting problem rather than re-litigating it after the
fact.

## Data (real, this session)

FLAMINGO `L1_m9` fiducial run, `z=0` (`halo_properties_0077.hdf5`),
downloaded via the `hdfstream` service (`pip install hdfstream`, no
account/token needed — confirmed live, user-approved). Box: `1000 Mpc`
physical at `z=0` (SWIFT's own convention — `h`-scale exponent `0` on
the position field, confirmed directly, NOT `h^-1 Mpc` despite the
`L1000` naming). Cosmology (from the file's own `Cosmology` group,
`h=0.681, Omega_m=0.3046`) — a THIRD distinct cosmology from both
`TNG` (Planck 2015, `h=0.6774, Omega_m=0.3089`) and `Magneticum`
(WMAP7, `h=0.704, Omega_m=0.272`). Mass: `SO/200_crit/TotalMass`
(spherical-overdensity `M200c`) — the SAME mass definition `TNG300`
used (unlike `Magneticum`'s `m500c`), maximizing direct comparability
to the `TNG300` result specifically.

**Volume: `(1000/302.6)^3 ~ 114x` `TNG300`'s volume** — by far the
largest of the three simulations checked.

## Pre-registered threshold (chosen from the exploratory bracket,
## BEFORE this claim is used to run the decisive test)

```
N_sub = 1200 (top 1200 most massive halos by SO/200_crit/TotalMass)
mass floor (exploratory readout): 3.386e14 Msun
exploratory median true-NN separation: 41.00 Mpc
exploratory mean true-NN separation:   43.70 Mpc
```

Both median and mean land cleanly inside v82's own `40-45 Mpc` target
window (unlike every low-`N` point in both prior attempts, which had
median-outside or mean-outside slippage). `N_sub=1200` gives a sample
size `~8-12x` larger than either prior attempt's own scale-matched
range (`TNG300`: `N=30-50`; `Magneticum`: `N=100-150`).

## The falsifiable question

`rho = Pearson r(log M200c_self, log M200c_true-nearest-neighbor)`
among the `N_sub=1200` most massive `L1_m9` halos, against a proper
permutation-null distribution (`>=1000` shuffles). **This is the ONE
number this test reports as its primary result** — no sweep, no
secondary thresholds promoted to confirmatory status.

## What this would and would not settle

- **If significant and positive**: independent, cross-code, cross-
  cosmology, well-powered support for `rho>0` (hence `rho>-0.5`) at
  v82's own target scale — the strongest evidence this project's own
  `P158` thread has produced, given the sample-size improvement.
- **If null**: a third independent non-result, at last with adequate
  statistical power to trust a null as a real null rather than a
  power-starved one — the magnitude/mechanism question would then be
  reasonably concluded UNDETERMINED with real confidence, not merely
  "not yet measured with enough data."
- **Does NOT** resolve whether "top-N-most-massive-halos" is the right
  operational definition of v82's own "node" (same open mapping
  question named in both prior attempts).
- **Does NOT** by itself validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind, before this result is treated as
resolving or informing the magnitude/mechanism question — specifically
asked to check whether the single-pre-registered-threshold design
actually closes the nesting/look-elsewhere gap from the prior two
attempts, not just whether the number itself looks right.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
