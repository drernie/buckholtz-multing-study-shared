# CLAIM — the real fix named by two prior FINDINGs: true, pre-cut
# global nearest-neighbor (computed across FLAMINGO's own real,
# physically-correct 1000 Mpc periodic box, BEFORE any sub-cube
# cutting) as ground truth for the periodic-vs-open comparison

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b. Kept lean (Structure-Bias Guard) — fully-specified follow-up to
two already-frozen tests, not a new open-ended hypothesis.
**Continues:** `FINDING_flamingo_subvolume_replication.md`'s own
"cheapest next steps" §2 and `FINDING_flamingo_subvolume_periodic_
wrap_bias.md`'s own closing recommendation — both name the same fix:
"a true pre-cut, whole-FLAMINGO global NN calculation as the actual
ground truth, compared against both periodic and open sub-cube
estimates." **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Why this is a genuine ground truth (not a third biased estimator)

FLAMINGO's own `1000` Mpc box is a REAL periodic cosmological
simulation — unlike the `27` artificially-carved `302.6267` Mpc sub-
cubes (which are NOT independently periodic; treating them as such was
the exact approximation both prior tests scrutinized), FLAMINGO's own
FULL box genuinely has periodic boundary conditions built into how it
was simulated. Computing each halo's nearest neighbor using the FULL
top-`5000`-by-global-mass sample (already downloaded, no new API call)
with FLAMINGO's own real `1000` Mpc periodic wrap is therefore the
actual, physically correct nearest-neighbor relationship — not a third
approximation with its own distortion.

## Method (frozen before running — reuses the SAME 10 already-selected
## `(cube_id, local_N)` samples, no new selection)

1. Download the SAME top-`5000`-by-mass halos (masses + positions),
   deterministic, matches both prior tests exactly.
2. Compute the FULL `5000x5000` periodic separation matrix using
   FLAMINGO's own real box size (`1000` Mpc — its own genuine
   periodicity, not a sub-cube's artificial one).
3. For EVERY halo, find its TRUE global nearest neighbor among all
   `5000` (the same mass-selected population every test in this
   branch already restricts to, since the physical question is mass
   assortativity AMONG comparably massive nodes, not nearest object of
   any size).
4. For each of the `10` already-frozen sub-cube samples (SAME
   `local_N` halos as both prior tests): compute `rho_NN_true`
   (correlating each halo's log-mass against its TRUE global nearest
   neighbor's log-mass — which may or may not be one of that sub-
   cube's own `local_N` members, and may or may not lie inside the
   sub-cube at all).
5. **The key mechanistic diagnostic neither prior test could
   measure**: for each sub-cube, what FRACTION of its `local_N` halos
   have a true nearest neighbor that lies OUTSIDE the sub-cube
   entirely? This is the direct, physical size of the "missing
   neighbor" problem — not inferred, measured.
6. Three-way comparison per sub-cube: `rho_NN_true` vs. the already-
   reported `rho_NN_periodic` and `rho_NN_open`. Aggregate: mean/SD of
   each, and — the correctly-specified test per the prior FINDING's
   own caught framing error — the AMPLITUDE deltas
   `|rho_periodic|-|rho_true|` and `|rho_open|-|rho_true|` (not signed
   deltas), to properly test whether either sub-cube approximation
   systematically shrinks or inflates relative to the real answer.

## What this would and would not settle

- **This gives the first genuinely unbiased reference point** in this
  specific replication thread — resolves the open question from both
  prior tests ("neither periodic nor open is a clean ground truth").
- **If `rho_NN_true`'s own distribution (across the `10` samples)
  still shows `0` or few reaching `|rho|>=0.42`**: strengthens (does
  not by itself prove, `n=10` is still small) the noise-explanation for
  TNG300's own anomaly, now on a properly-grounded reference.
- **If the "missing neighbor" fraction (step 5) is large**: explains
  mechanistically why sub-cube estimates diverge from the true answer,
  independent of whether the divergence happens to push `rho` up or
  down in any given cube.
- **Does NOT** add new sub-cubes or increase `n` beyond `10` — the
  power limitation from both prior tests is UNCHANGED; this test fixes
  the REFERENCE, not the sample size.
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked: (a) is
FLAMINGO's own real periodic box actually a valid ground truth here,
or does IT ALSO have a residual limitation worth naming (e.g., halos
below the top-`5000` mass cut that could, in principle, be a TRUE
nearest neighbor missed by this search); (b) does the amplitude-based
three-way comparison correctly avoid the signed-vs-amplitude framing
error already caught once in this same thread; (c) is the "missing
neighbor fraction" diagnostic computed and interpreted correctly.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
