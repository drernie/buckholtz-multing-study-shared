# CLAIM — scale-matched nearest-neighbor rho: which reading of the two
# `FINDING_mass_assortativity_and_scatter.md` readings (all-pairs
# rho=+0.38 vs. nearest-neighbor rho=0.019, n.s.) is physically the
# right one for v82's own construction?

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b, the test design below is frozen first.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Why the two existing readings disagree, and how to resolve it

The all-pairs reading (`rho=+0.38`) used the full top-1461-most-massive-
halo sample (mass floor `8.4e12 Msun`), whose median TRUE nearest-
neighbor separation is only **9.2 Mpc** — nowhere near v82's own fitted
`s(0)=45 Mpc` (`data/source_material/buckholtz_202608.0943v1.v82.md`,
Sec. IIC). The nearest-neighbor-restricted reading (`rho=0.019, n.s.`)
correctly asked for TRUE nearest neighbors, but measured them within
that SAME over-dense (9.2 Mpc-typical) sample — i.e., it answered "is
mass correlated between a halo and its nearest neighbor, when that
neighbor is typically only ~9 Mpc away," not "...when that neighbor is
typically ~45 Mpc away, as v82's own fit implies."

**Cheap feasibility check, run before this claim (EXPLORATORY, not a
claim itself):** `_explore_threshold_sweep.py`, reusing the same
already-downloaded `top_halos_pos_mass.csv` (no new API calls), found
that restricting to the **top ~50 most massive halos** (mass floor
`~2.8e14 Msun`) in the SAME box gives median true-nearest-neighbor
separation **46.5 Mpc**, mean **41.0 Mpc** — landing directly in v82's
own 40-45 Mpc range, unlike the full 1461-halo sample. A sparser,
higher-mass-selected population is therefore the scale-appropriate
comparison, not an arbitrary re-selection.

## The falsifiable question

At the mass threshold(s) where the SAMPLE's own typical nearest-neighbor
separation matches v82's own `s(0)=45 Mpc`, is the mass correlation
between true nearest-neighbor pairs closer to the all-pairs reading
(`~+0.38`, real assortativity) or the full-sample nearest-neighbor
reading (`~0.02`, essentially null)?

**H_scale-matched:** `rho` measured among TRUE nearest-neighbor pairs,
restricted to a mass-selected sub-sample whose own typical NN separation
is ~40-45 Mpc, is [to be measured — no result assumed]. Report the
actual number; do not force it toward either prior reading.

## Method (frozen)

- Reuse `top_halos_pos_mass.csv` (already downloaded, no new API calls).
- Sweep `N_sub` in `{30, 40, 50, 60, 80, 100}` most massive halos (a
  small range around the single value the exploratory sweep found, not
  just one cherry-picked N) — for EACH, report its own median/mean true
  NN separation (so the reader can see which `N_sub` actually lands in
  40-45 Mpc) and the Pearson `r(log M_self, log M_nearest_neighbor)`
  among ALL true nearest-neighbor pairs in that sub-sample (not
  restricted further by separation — `N_sub` is small enough that
  further band-restriction would leave too few pairs).
- **Negative control:** mass-shuffle within each sub-sample, same
  nearest-neighbor index structure, expect `r~0`.
- **Power caveat, stated up front:** `N_sub<=100` gives `df<=98`,
  and the smallest (`N_sub=30`) gives `df=28` — report `t`, `p`, and be
  explicit that a null result at small `N_sub` could reflect low power,
  not a genuine absence of correlation; a real (nonzero, significant)
  result at small `N_sub` is not similarly undermined by power (harder
  to get a false positive from noise alone at reasonable `p`-thresholds).

## What this would and would not settle

- **If scale-matched `rho` is significant and positive** (matching the
  all-pairs reading's sign/rough magnitude): the all-pairs reading was
  measuring something structurally right for v82's own scale, and its
  "broad large-scale bias" caveat is better read as "real assortativity
  that happens to extend broadly," not a scale-mismatch artifact —
  `FINDING_P158`'s directional prediction is grounded at the CORRECT
  physical scale, not just "some scale or other."
- **If scale-matched `rho` is null/small**, even accounting for the
  power caveat: neither existing reading was measuring the right thing
  cleanly, and the honest state remains genuinely ambiguous at small
  `N_sub` — to be reported as such, not forced toward a preferred
  answer.
- **Does NOT** resolve whether "top-N-most-massive-halos-in-a-205-Mpc/h-
  box" is itself the right operational definition of v82's own "node" —
  that mapping is itself an assumption, named explicitly, not tested
  here (v82's own `s(0)=45 Mpc` is a FITTED quantity, per `docs/149`'s
  own Sec. IIC reading — not independently derived from any halo
  catalog).

## Skeptic pass

Mandatory (Step 8a), context-blind, before any reading of this result is
treated as resolving the magnitude/mechanism ambiguity.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
