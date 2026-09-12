# CLAIM — independent cross-check of scale-matched nearest-neighbor
# rho using real Magneticum Box2_hr data (WMAP7 cosmology, different
# code from TNG's Arepo)

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b.
**Continues:** `CLAIM_scale_matched_nearest_neighbor_rho.md` /
`FINDING_scale_matched_nearest_neighbor_rho.md` (the TNG-300-only
attempt, FALSIFIED as a resolving test by a skeptic pass — small-N,
look-elsewhere, single-shuffle-as-null issues).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Data (real, downloaded this session, not simulated)

`Magneticum Box2_hr, snap_140 (z=0.033)` cluster catalog — 10,493 real
clusters, `m500c` in `[7.04e12, 1.03e15] Msun/h`, positions in
`kpc/h`. Box side `352 Mpc/h` (WMAP7, `h=0.704`) = `500.0 Mpc` physical
— `4.5x` `TNG300`'s volume. Downloaded via plain HTTP (verified
`Content-Length` match, `880414` bytes) from
`wwwmpa.mpa-garching.mpg.de/HydroSims/Magneticum/Downloads/`.

**Exploratory feasibility check** (`_explore_magneticum_scale.py`, not
a claim): swept `N_sub` (top-N most massive clusters) and found `N_sub
in [100,150]` gives both median AND mean true-nearest-neighbor
separation inside or immediately adjacent to v82's own `40-45 Mpc`
target — unlike the earlier `TNG300` sweep's `N_sub=30` point, which
landed outside the window by its own median.

## What this improves on the earlier (falsified) TNG-300 attempt

1. **A genuinely different, independent dataset** — different
   simulation code (Magneticum's own SPH/Gadget-family code, not
   Arepo), different cosmology (WMAP7 `Omega_m=0.272` vs. `TNG`'s
   Planck `Omega_m=0.309`), different initial conditions/random phases.
   Not a resolution/physics variant of the same box (unlike
   `TNG300-2/3`).
2. **A pre-existing, physically-motivated population** (a real
   "cluster" catalog, `m500c`-selected by the Magneticum team's own
   pipeline) rather than an arbitrary top-N cut invented for this test
   — the top-N-by-mass sub-selection is still applied on top of it to
   reach the target scale, so the mass-rank-thinning caveat
   (`pearl_registry`, 2026-09-12) still applies and is NOT waived here.
3. **A proper permutation null** (>=1000 shuffles, reporting the full
   null distribution's mean/SD and a percentile-based p-value) instead
   of the earlier single-shuffle-draw comparison — directly addresses
   the skeptic's Objection 3 from the `TNG300` attempt.

## The falsifiable question (identical in spirit to the TNG-300 attempt)

At `N_sub` in `{100, 110, 120, 125, 130, 140, 150}` (bracketing the
`40-45 Mpc` target from both sides, not one cherry-picked value),
measure `rho = Pearson r(log m500c_self, log m500c_true-nearest-
neighbor)`. Report the real value against a real permutation-null
distribution (1000 shuffles) for each `N_sub`, plus each point's own
median/mean true-NN separation (so scale-match quality is visible, not
assumed).

## What this would and would not settle

- **If the real `rho` at the scale-matched `N_sub` range is
  consistently significant and positive** (comparable in sign/rough
  magnitude to `TNG300`'s own all-pairs `+0.38` reading): independent,
  cross-code, cross-cosmology support for `rho>0` at v82's own scale —
  a real strengthening of `FINDING_P158`'s directional prediction.
- **If null or unstable across the swept range** (matching `TNG300`'s
  own inconclusive scale-matched result): the magnitude/mechanism
  question stays genuinely undetermined — a second independent
  non-result, not a resolution either way.
- **Does NOT** resolve whether "top-N-most-massive-clusters" is the
  right operational definition of v82's own "node" — same open mapping
  question named in the `TNG300` attempt, not addressed here either.
- **Does NOT** by itself validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind, before this result is treated as
adding to or resolving the magnitude/mechanism question.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
