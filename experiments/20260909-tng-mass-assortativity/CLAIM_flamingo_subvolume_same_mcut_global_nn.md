# CLAIM — same-mass-cut, full-box periodic NN diagnostic (user-
# designed fix): a geometric gate runs BEFORE any rho is computed;
# the gate's own outcome decides whether this branch of subcube work
# continues or is closed as invalid for this estimand

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b. Kept lean (Structure-Bias Guard) — the design was fully specified
by the user, not re-derived here.
**Continues:** `FINDING_flamingo_subvolume_true_global_nn.md`'s own
scale-mismatch finding. **User-designed and user-requested** — the
user independently identified the same construct-validity problem
this session's own follow-up check found, and specified the correct
fix directly (quoted/paraphrased below), pre-empting the need for a
separate skeptic pass on the DESIGN itself (a skeptic pass on the
RESULT is still run, per standing practice).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## The problem this fixes

`FINDING_flamingo_subvolume_true_global_nn.md`'s own "true global NN"
attempt searched each sub-cube halo's nearest neighbor among the
FULL top-`5000`-by-GLOBAL-mass FLAMINGO pool — a population `~4x`
DENSER than any sub-cube's own local selection, which silently changed
the estimand (measured mass assortativity at `~22` Mpc, not `40-45`
Mpc). Widening the geographic search AND changing the population
definition at the same time made the two effects (real boundary bias
vs. population-definition mismatch) inseparable.

## The fix (user-specified)

**Hold the population fixed to each sub-cube's own already-frozen mass
cut**, search geographically wider:

1. For each of the `10` already-matched `(cube_id, local_N)` pairs,
   recover `M_cut(k)` — the mass of the LEAST massive halo in that
   cube's own already-selected `local_N` sample (i.e., the mass
   threshold that selection implicitly used).
2. Build the population `{halo : mass >= M_cut(k)}` from the SAME
   already-downloaded top-`5000` global array (this population is
   automatically a SUBSET of the top-`5000` — no new download needed,
   since `M_cut(k)` is itself the mass of a halo already inside that
   top-`5000`).
3. For each of cube `k`'s own `local_N` halos, compute its nearest
   neighbor searching ONLY within `{mass >= M_cut(k)}`, using
   FLAMINGO's own REAL `1000` Mpc periodic box (genuine, not
   artificial, periodicity) — geographically unrestricted (a true
   neighbor anywhere in the box, at or above the SAME mass threshold
   that defined the local selection, is now visible).

This holds the population definition fixed (same mass cut, same
cube-specific selection that was already frozen) while fixing the
geography (true full-box periodicity instead of an artificial
sub-cube wrap) — isolating the ONE variable (boundary treatment) the
whole replication thread has been trying to test, from the population-
definition confound the top-`5000` attempt introduced by accident.

## The geometric gate — decided BEFORE computing any rho, per the
## user's own explicit instruction

**Exact numeric threshold, fixed here before the script runs (not
chosen after seeing the result)**: `PASS` if the aggregate median
same-`M_cut`, full-box NN separation falls in `[35, 55]` Mpc — a
tolerance around the original `40-45` Mpc target wide enough to allow
real per-cube environmental scatter (this design, unlike the original
sub-cube selection, does not re-tune per cube to hit the window
exactly), but nowhere near the top-`5000` attempt's own `~22` Mpc
result, so it still meaningfully discriminates "boundary artifact
confirmed absent" from "the scale-match itself doesn't survive
unrestricted geography." `FAIL` otherwise.

For each cube `k` (and in aggregate), compute the median/mean NN
separation under this same-`M_cut`, full-box treatment. **Compare
against the ORIGINAL local (sub-cube-restricted) `40-45` Mpc target
BEFORE looking at any correlation:**

- **If the same-`M_cut` full-box NN scale stays close to `40-45` Mpc**
  (materially closer than the top-`5000` attempt's `~22` Mpc): the gate
  PASSES — proceed to compute `rho_NN` under this treatment and compare
  to the already-reported periodic/open values. This is now a clean,
  population-matched test of whether sub-cube boundaries specifically
  distorted the earlier result.
- **If the same-`M_cut` full-box NN scale still drifts well below
  `40-45` Mpc**: the gate FAILS — this is the DEEPER result. It would
  mean the sub-cube's own local `40-45` Mpc scale-match was itself an
  artifact of the sub-cube's own limited candidate-neighbor set, not a
  real property of that mass-defined population. **Per the user's own
  explicit instruction: do NOT search for a new `N`/threshold to force
  a match — report this as invalidating the entire sub-cube-
  replication design for this estimand, and stop.**

## What this would and would not settle

- **Gate passes**: gives the first population-matched (not just
  boundary-matched) comparison of periodic vs. full-box-true `rho_NN`
  — the cleanest test this specific replication thread has produced.
- **Gate fails**: closes the sub-cube-replication line of work
  (`flamingo_subvolume_replication.py` and its two follow-ups) as
  invalid for testing TNG300's own `N=35` anomaly — not because the
  code was wrong, but because the underlying scale-matching procedure
  does not survive contact with a genuinely unrestricted geometry. The
  user's own named alternative (a single global mass threshold on the
  full FLAMINGO box, geometrically chosen without looking at `rho`,
  with spatial-jackknife uncertainty — no artificial sub-cubes at all)
  becomes the recommended next design, not attempted in this file.
- **Either way**: per the user's own explicit instruction, no further
  correlations are computed on the (population-mismatched) top-`5000`
  pool beyond what has already been reported — that attempt already
  served its purpose (catching the construct-validity bug).
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a) on the RESULT (not the design, which the user
specified directly) — context-blind, specifically asked: (a) is
`M_cut(k)`'s recovery from each cube's own frozen selection correct
and non-circular, (b) is the gate threshold ("close to 40-45" vs.
"drifts well below") applied honestly rather than post-hoc rationalized
toward whichever branch looks more convenient, (c) if the gate passes,
is the resulting rho comparison actually cleaner than the prior two
attempts or does some residual confound remain.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
