# CLAIM — a real, genuinely independent-volume replication attempt of
# TNG300's `N=35` `rho_NN=-0.42` anomaly: 27 non-overlapping, TNG300-
# sized sub-volumes carved from FLAMINGO's real 1000 Mpc box, each
# independently scale-matched and measured with the SAME protocol

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b.
**Continues:** `FINDING_tng300_own_population_rho_nn_and_band.md`'s own
"What this DOES establish" section — `rho_NN=-0.42` at TNG300's own
`N=35` is "flagged as an anomaly worth independent replication in a
larger, genuinely different volume — not a standalone result." This is
that replication, explicitly requested by the user.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Why a single additional FLAMINGO point is not enough, and what this
## does instead

Reusing FLAMINGO's own already-existing `N=1200` result (`rho_NN=
-0.0231`) as "the replication" would be weak for two reasons: (1) it
was computed for a different original purpose, not framed as a
replication attempt; (2) it is ONE point estimate, at ONE size, and a
single non-matching point cannot cleanly answer "is `-0.42` a rare
outlier, or a common outcome of this small-`N` selection protocol at
all?" — that requires a DISTRIBUTION of independent draws at a
COMPARABLE `N`, not one large-`N` point.

**This design instead carves FLAMINGO's real, much larger box into
MANY genuinely independent, TNG300-sized regions**, and repeats
TNG300's own exact selection protocol independently in each — turning
one real, already-downloaded dataset into an empirical distribution of
the statistic in question, rather than a second single point.

## Method (frozen before running)

1. **Partition** FLAMINGO's real periodic `1000` Mpc box into a
   `3x3x3=27` grid of non-overlapping sub-cubes, each **EXACTLY**
   TNG300's own physical box size (`302.6267` Mpc — `205/0.6774`),
   covering `[0, 907.88)` Mpc per axis (a `92.12` Mpc margin per axis
   left unused, not periodic-wrapped into the grid — kept simple,
   avoids edge-wrap complications). **Feasibility confirmed live**
   (`_explore_flamingo_subvolume_feasibility.py`, real `hdfstream`
   data, no correlation computed): all `27` sub-cubes contain `98-171`
   halos above `~1.53e14` Msun (global top-`5000` by mass) — comfortably
   enough to find a local scale-matched `N` in every sub-cube.
2. **Per sub-cube, independently**: using ONLY the halos physically
   located inside that sub-cube, scan candidate local `N` in
   `{20,25,30,35,40,45,50,55,60,65,70,75,80}` computing ONLY the local
   median/mean true-nearest-neighbor separation (no correlation) —
   treating the sub-cube as its OWN periodic box of side `302.6267`
   Mpc for the minimum-image NN calculation, mirroring exactly how
   TNG300's own periodic box is treated (a stated methodological
   approximation, not a hidden one — see Caveats below). If exactly
   one or more candidate `N` satisfies "median AND mean both in
   `[40,45]` Mpc", select the one minimizing
   `|median-42.5|+|mean-42.5|` (pre-specified tie-break, decided now,
   before any sub-cube's own values are computed). If NO candidate `N`
   satisfies the criterion for a given sub-cube, that sub-cube
   contributes NO data point — reported explicitly, not silently
   dropped.
3. **For every sub-cube that yields a matched local `N`**: compute
   `rho_NN = Pearson r(log M_self, log M_true-nearest-neighbor)` on
   that sub-cube's own selected halos.
4. **Aggregate** the resulting `rho_NN` values (however many sub-cubes
   succeed, out of `27`) into an empirical distribution: report count,
   mean, SD, min/max, and — the specific falsifiable question — how
   many/what fraction reach `|rho_NN| >= 0.42` (matching or exceeding
   TNG300's own anomaly).

## Caveats, stated in advance

- **Each sub-cube is treated as an artificially self-periodic box for
  its own NN calculation** — this is NOT physically the same as an
  independent cosmological simulation with its own genuine periodic
  boundary conditions (a real halo just outside a sub-cube, which
  would be a true nearest neighbor in the unbounded/real FLAMINGO box,
  is invisible to that sub-cube's own calculation; a halo on the
  opposite face of the SAME sub-cube can be spuriously treated as
  "nearby" via the artificial local wrap). This exactly mirrors how
  TNG300's own single, real periodic box is treated in every prior
  test in this branch, so the METHOD is consistent across the
  comparison — but the 27 sub-volumes are not literally 27 independent
  simulations, only 27 independent REGIONS of one real simulation with
  real large-scale correlations between them (though at `302.6+` Mpc
  separation, well past most nonlinear correlation scales).
- **Different halo-finding pipeline, resolution, and cosmology from
  TNG300** (FLAMINGO: SWIFT/SOAP, `h=0.681`, `Om=0.3046`; TNG300:
  Arepo, `h=0.6774`, `Om=0.3089`) — a genuine, useful cross-code/cross-
  cosmology check, not a weakness.
- **This tests whether TNG300's OWN specific numeric result
  (`|rho_NN|>=0.42` at this exact small-`N` selection protocol) is
  common or rare — it does NOT by itself prove or disprove any
  particular physical mechanism**, per `NO_AUTHOR_ERROR` and this
  branch's own standing descriptive-only framing.

## What this would and would not settle

- **If `|rho_NN|>=0.42` occurs in a NON-negligible fraction of the
  successfully-matched sub-cubes** (e.g. several out of `~15-27`):
  supports the small-`N` sampling-noise explanation for TNG300's own
  result — `-0.42` is simply what this protocol commonly produces at
  this `N`, not a signal specific to TNG300.
- **If `|rho_NN|>=0.42` is rare or absent** across all successfully-
  matched sub-cubes: weakens the sampling-noise explanation and makes
  TNG300's own `-0.42` look more like a genuine outlier — worth further
  scrutiny (though still not, by itself, proof of a real physical
  signal, given the assembly-bias concern already on record).
- **Does NOT** resolve Hypothesis A vs. B from the FLAMINGO addendum
  (that question is about `rho_band`, not `rho_NN` alone, and is
  separate from this specific replication question).
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked to check: (a)
whether the artificial local-periodic treatment is defensible or
introduces a bias worth naming, (b) whether `27` (or fewer, if some
sub-cubes fail to match) independent draws are enough to say anything
about rarity, (c) whether the pre-specified tie-break rule could have
been gamed in hindsight (it was fixed before any sub-cube's own values
were computed — worth an explicit check that this was actually
honored).

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
