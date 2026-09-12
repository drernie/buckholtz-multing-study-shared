# CLAIM — quantify the periodic-wrap dilution bias named in
# `FINDING_flamingo_subvolume_replication.md`'s own Step 8a skeptic
# review (item 2), via a direct open-boundary comparison on the SAME
# already-selected sub-cubes

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b. Kept lean (per the Structure-Bias Guard) — this is a direct, fully-
specified diagnostic follow-up to an already-frozen test, not a new
open-ended hypothesis.
**Continues:** `FINDING_flamingo_subvolume_replication.md`'s own Step
8a skeptic item 2 and its own "cheapest next steps" §2 ("compute
`rho_NN` in each sub-cube twice: once local-periodic, once non-
periodic/open-boundary; the difference quantifies the wrap-artefact
size"). **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Method (frozen before running — no new selection, reuse exactly
## what was already chosen)

**Freeze the exact `10` `(cube_id, local_N)` pairs already selected by
`flamingo_subvolume_replication.py`'s own real, committed output** —
no re-selection, no new geometric scan:

```
cube=1  N=40 | cube=2  N=55 | cube=4  N=35 | cube=5  N=30 | cube=7  N=30
cube=8  N=30 | cube=12 N=40 | cube=17 N=45 | cube=25 N=45 | cube=26 N=50
```

For each, using the SAME `local_N` halos (same global top-`5000`
download, deterministic — re-querying `hdfstream` reproduces the
identical set):

1. **Periodic NN** (as already computed): minimum-image nearest
   neighbor within that sub-cube treated as its own `302.6267` Mpc
   periodic box.
2. **Open-boundary NN** (new): nearest neighbor via plain Euclidean
   distance, NO wraparound — the sub-cube's own edges are real
   boundaries, not periodic.
3. **Per sub-cube**: `rho_NN` under each treatment; the FRACTION of
   halos whose identified nearest neighbor DIFFERS between the two
   treatments (`nn_idx_periodic != nn_idx_open`) — this is the direct,
   mechanistic measure of how often the wrap actually changes which
   pair is being correlated, not just an indirect inference from `rho`
   alone; median/mean NN separation under both treatments (periodic
   `<=` open for every halo, by construction of minimum-image — this
   inequality is a mathematical certainty, not a hypothesis, and is
   reported as a sanity check on the implementation, not a finding).

## The falsifiable question

Does `rho_NN` computed with an honest open boundary differ
systematically (in magnitude and/or direction) from the already-
reported periodic-wrap version, across the `10` already-selected sub-
cubes? Specifically: is the fraction of halos with a swapped nearest-
neighbor identity large enough to plausibly explain a meaningful share
of the periodic-vs-open `rho_NN` gap?

## What this would and would not settle

- **If the open-boundary `rho_NN` values are systematically LARGER in
  magnitude** (more negative, since `-0.42`-direction is the concern)
  than the periodic ones, on sub-cubes with a non-trivial swapped-
  neighbor fraction: confirms the skeptic's named dilution mechanism
  is real and gives its approximate size — strengthens the case that
  the `0/10` result from the periodic version is partly a methodology
  artifact, not purely a statement about the underlying noise floor.
- **If the two treatments give closely similar `rho_NN` values** (small
  swapped-neighbor fraction, small `rho` differences): weakens the
  dilution-bias concern specifically (though does NOT resolve the
  SEPARATE, already-established underpowering problem — `n=10` stays
  `n=10` either way).
- **Does NOT** resolve whether TNG300's own `-0.42` is real signal or
  noise — this quantifies ONE specific named bias in ONE specific
  replication attempt, nothing more.
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked whether the
open-boundary treatment introduces its OWN bias (e.g., halos near a
sub-cube edge systematically get artificially INFLATED NN separations
under open boundaries too, since their true neighbor may be just
outside — a different, not necessarily smaller, artifact) — i.e.,
whether "open boundary" is a clean ground truth or just a different
approximation with its own distortion, and what that implies for how
to read the comparison.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
