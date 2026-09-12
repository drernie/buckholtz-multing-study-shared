# FINDING — the "definitive global FLAMINGO estimand" (no sub-cubes,
# single geometrically-pre-registered global threshold, spatial-
# jackknife uncertainty on the full box) ALREADY EXISTS: a synthesis,
# no new computation

**Continues:** `CLAIM_flamingo_independent_rho_check.md` /
`FINDING_flamingo_independent_rho_check.md` (2026-09-12, N=1200 point
estimate) + `CLAIM_flamingo_addendum_jackknife_band_closure.md` /
`FINDING_flamingo_addendum_jackknife_band_closure.md` (2026-09-12,
spatial jackknife + `rho_band`). **User-requested synthesis** — no new
`hdfstream` call, no new script; the user explicitly chose to
consolidate rather than re-run, since the underlying data and jackknife
grid are deterministic and a fresh run cannot change the numbers.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Why this closes the "definitive estimand" question without a new
## run

The design the user specified — full FLAMINGO box, no artificial
sub-cube boundaries, ONE global mass threshold chosen geometrically
(NN-scale-only, no `rho` seen) before freezing it, a single pre-
registered `rho_NN` measurement, uncertainty from a real spatial
jackknife on the big box — **already exists, in full, across two
already-committed, already-skeptic-reviewed files, both predating the
27-subcube detour**:

1. `flamingo_independent_rho_check.py` (`CLAIM` committed `292e563`,
   before the script ran): `N_sub=1200` selected purely from
   `_explore_flamingo_scale.py`'s own NN-geometry-only bracket (median
   `41.00`, mean `43.70` Mpc at exploration time — no correlation
   computed before freezing `N`). Single, pre-registered measurement:
   `rho_NN = -0.0231`. No sub-cube anywhere — the search was always
   FLAMINGO's own real, full `1000` Mpc periodic box.
2. `flamingo_addendum_jackknife_band_closure.py` (correcting the
   originally-reported, since-withdrawn `"~13 sigma"` claim): real
   spatial delete-one-block jackknife, `125` blocks (`200` Mpc/side)
   tiling that SAME full `1000` Mpc box — `SE=0.0476`. Also added
   `rho_band = +0.0271` (`N_pairs=127`) on the SAME `N=1200`.

**The only procedural difference from the user's exact phrasing**: the
jackknife was added as a correction AFTER the point estimate was first
reported with a (later-withdrawn) permutation-null-based sigma claim,
rather than pre-registered as one unified point-estimate-plus-
uncertainty protocol from the start. This changes the ORDER in which
the numbers were produced, not the numbers themselves — both the
point estimate and the jackknife are deterministic functions of
FLAMINGO's own static catalog and the frozen `N=1200`/`125`-block grid,
so a fresh, freshly-unified re-run would reproduce them exactly.

## The definitive numbers (already established, restated here as the
## closing answer to this specific design question)

```
rho_NN   = -0.0231, jackknife SE = 0.0476  (real spatial block-jackknife,
                                             125 blocks, full 1000 Mpc box)
rho_band = +0.0271, jackknife SE = 0.1231  (N_pairs=127, underpowered)
N = 1200, single pre-registered threshold, no sweep, no sub-cubes
```

Both already passed independent, context-blind Step 8a skeptic review
(twice — once at the original FLAMINGO addendum, once again during the
`"13 sigma"` withdrawal) with every quantitative claim independently
re-derived before acceptance.

## Relationship to the separate 27-subcube thread (four tests, all
## already-committed) — a DIFFERENT question, not superseded by this
## one

The `27`-subcube work (`flamingo_subvolume_replication.py`,
`_periodic_wrap_bias.py`, `_true_global_nn.py`,
`_same_mcut_global_nn.py`) answered a DIFFERENT, narrower question:
**does TNG300's own specific `N=35`, TNG300-BOX-SIZED result
replicate in genuinely independent, TNG300-SIZED volumes carved from a
larger simulation?** That thread converged on: `n=10` is the binding
constraint, boundary-treatment details do not matter much, and no
sub-cube variant meaningfully differs from any other.

**This synthesis answers a separate, complementary question: what is
FLAMINGO's OWN best, most powerful, no-artificial-boundary estimate of
the SAME quantity, at FLAMINGO's own natural (much larger, `N=1200`)
scale-matched sample size?** Neither supersedes the other — they are
different estimands at different sample sizes, both honestly reported.

## What this DOES establish

- **The user's own "definitive global estimand" design is not a
  hypothetical improvement — it was already run, at the highest
  standard of rigor this branch has applied anywhere** (single
  pre-registered `N`, no sweep, real full-box periodicity, real
  spatial-jackknife uncertainty, twice-skeptic-reviewed).
- **`rho_NN` is small and consistent with zero at FLAMINGO's own best
  achievable power for this observable** (`N=1200`, `~36x` more halos
  than TNG300's own `N=35`).
- **The qualitative distance from `rho_NN<=-0.5`** (`FINDING_P158`'s
  own safety threshold) **remains large** under the jackknife SE —
  consistent with the branch's own already-corrected framing (no new
  precise sigma-count asserted here, per the withdrawn `"13 sigma"`
  lesson; the qualitative conclusion — excluded by a wide margin under
  multiple independently-derived SEs — stands as already recorded).
- **`rho_band` remains underpowered** (`N_pairs=127`) to cleanly
  discriminate whether the historical `TNG300` `+0.38` all-pairs
  reading reflects a different observable or a different population —
  unchanged from the addendum's own honest scope.

## What this does NOT establish

1. Does NOT provide a NEW number — this is a synthesis of already-
   reported, already-skeptic-reviewed results, not a new measurement.
2. Does NOT resolve the separate `27`-subcube thread's own open
   question (whether boundary treatment matters for a TNG300-SIZED
   sample specifically) — that remains `n=10`-limited and genuinely
   inconclusive, unaffected by this synthesis.
3. Does NOT establish a precise sigma-count for any threshold exclusion
   — deliberately, per this branch's own corrected discipline.
4. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).

## Status

**Closes the "definitive global FLAMINGO estimand" question by
pointing at already-completed, already-validated work rather than
duplicating it** — the most resource-honest outcome available, and a
concrete instance of this project's own Adaptive Iteration Branch Rule
(check what already exists before re-running). The whole 2026-09-12
FLAMINGO/P158 magnitude-mechanism thread — addendum, `"13 sigma"`
withdrawal, TNG300-own-population test, four-part `27`-subcube
replication saga, and this synthesis — is now internally consistent
and cross-referenced across every file it touched.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
