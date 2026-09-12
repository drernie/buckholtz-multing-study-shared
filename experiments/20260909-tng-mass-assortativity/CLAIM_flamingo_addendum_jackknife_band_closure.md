# CLAIM — FLAMINGO addendum: correct the permutation-null-SD-as-CI
# overclaim, add the all-pairs-in-band observable on the SAME frozen
# subsample, and get a real CI via spatial block-jackknife

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b.
**Continues:** `CLAIM_flamingo_independent_rho_check.md` /
`FINDING_flamingo_independent_rho_check.md` (`N=1200`, real FLAMINGO
`L1_m9`, `rho_NN = -0.0231`, permutation-null `SD=0.0359`).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Why this addendum exists — a real statistical error, caught by the
## user, not self-caught

`FINDING_flamingo_independent_rho_check.md`'s own "What this DOES
establish" section states: *"`rho > -0.5` ... is now excluded ... `-0.5`
sits `~13 sigma` from this measurement's own null distribution."* This
conflates two different quantities:

- the **permutation-null SD** (`0.0359`) — the spread of `rho_hat`
  under `H0: rho=0` (masses fully randomized relative to position, at
  this `N` and this spatial geometry);
- the **standard error of `rho_hat` needed to test the composite
  hypothesis `H0: rho<=-0.5`** — which is NOT the same quantity. The
  sampling variance of a correlation-coefficient estimator is not
  constant in `rho` (the classical motivation for the Fisher
  `z`-transform: `Var(rho_hat) ~ (1-rho^2)^2/(n-1)` under iid bivariate
  normal — shrinks as `|rho|` grows away from `0`). Using the
  null-distribution SD (computed AT `rho=0`) as if it also applied at
  `rho=-0.5`, and reporting the resulting distance as `"13 sigma
  exclusion,"` is stronger than the test that was actually run
  licenses. This is the same class of error `artifact-provenance-
  gates.md` Gate 4 names generally: a scale/quantity computed for one
  purpose silently reused for a different one.

**Correction, not retraction:** the underlying result (`rho_NN` small,
consistent with zero, a large `|rho|` decisively excluded via the
power calculation in `FINDING_flamingo_independent_rho_check.md`
skeptic point 1) is untouched. Only the specific `"13 sigma"` /
`"excluded"` phrasing for the composite threshold `rho<=-0.5` is
withdrawn, replaced by a properly-constructed CI (below).

## What this addendum adds (three real gaps, per the user's own
## critique)

1. **A real CI for `rho_NN`**, via spatial delete-one-block jackknife
   over the periodic box — not a null-hypothesis SD borrowed for a
   different hypothesis.
2. **The all-pairs-in-band observable, `rho_band = Corr(log M_i, log
   M_j | 40<=s_ij<=45 Mpc)`, computed on the SAME frozen `N=1200`
   subsample** used for `rho_NN` — not a different population. This
   directly separates two candidate explanations for why `TNG300`'s
   own all-pairs `+0.38` and this branch's true-NN near-zero readings
   differ:
   - **Hypothesis A** (different observable): `rho_band` on this SAME
     `FLAMINGO` `N=1200` subsample comes out positive/elevated relative
     to `rho_NN` — the difference is the estimand, not the simulation.
   - **Hypothesis B** (different population/simulation/cosmology):
     `rho_band` on this subsample is ALSO near zero — the `TNG300`
     `+0.38` reading does not reproduce here regardless of which
     observable is used, pointing at a population- or simulation-level
     difference instead.
3. **An honest, pre-specified test of `H0: rho<=-0.5`** using the
   jackknife-derived CI, not a borrowed SD.

## Method (frozen before running)

- **Reuse the exact same `N_SUB=1200` selection** (top-1200 by
  `SO/200_crit/TotalMass`, same file, same deterministic mass-rank
  ordering — re-querying gives the identical subsample, since the
  underlying catalog is static).
- **`rho_band`**: from the already-computed full pairwise separation
  matrix (periodic minimum-image, same convention as `true_nn()`),
  select all UNORDERED pairs `(i,j)`, `i<j`, with `40 <= s_ij <= 45`
  Mpc. Symmetrize (each pair contributes both `(log M_i, log M_j)` and
  `(log M_j, log M_i)`) before computing Pearson `r`, matching the
  symmetric definition of the observable (no reason to privilege
  either member's ordering). Report `N_pairs` found — pre-registering
  the expectation that this will be SMALL (density in this mass-
  selected `N=1200` subsample is far sparser than the full-catalog
  sample `TNG300`'s own `+0.38`/`N_pairs=4694` was measured on), so the
  resulting CI on `rho_band` from this specific test may be too wide to
  discriminate A from B on its own — reported honestly either way, not
  forced to a verdict the data cannot support.
- **Spatial block jackknife**: partition the periodic `1000 Mpc` box
  into a `5x5x5=125`-block grid (`200 Mpc` per side — chosen to be
  well above the `~42 Mpc` typical NN separation, so a removed block
  does not systematically clip the NN relationship structure; `125`
  blocks gives `~9.6` halos/block on average, enough blocks for a
  stable jackknife variance estimate). For each of the `125` replicates,
  drop that block's halos, recompute `rho_NN` (nearest-neighbor
  reassigned within the remaining `~1190` halos) and `rho_band` (pairs
  recomputed within the remaining halos) on the reduced set. Jackknife
  variance: `Var_jack = (k-1)/k * sum_i (theta_i - theta_bar)^2`, `k=125`.
  **Chosen over a resampling bootstrap explicitly**: a naive block
  bootstrap on point-pattern nearest-neighbor structure creates
  duplicate positions when a block is drawn more than once, which can
  spuriously offer a zero-separation "self" as nearest neighbor unless
  duplicated blocks are also spatially shifted (toroidal-shift
  correction) — delete-one-block jackknife avoids this artifact
  entirely and is the standard choice for NN/clustering error bars in
  the observational literature (Norberg-style jackknife covariance).
- **CI and threshold test**: report `point_estimate +/- 1.96*SE_jack`
  (95%) and `+/- 2.576*SE_jack` (99%) for both `rho_NN` and
  `rho_band`. State explicitly whether `-0.5` falls inside or outside
  each CI. **Caveat, stated in advance**: `SE_jack` is a LOCAL estimate
  (perturbing the actual data near its own observed `rho`, close to
  `0`) — under the same Fisher-type variance-shrinkage-with-`|rho|`
  argument used above to reject the borrowed permutation-null SD, this
  local SE is plausibly an OVERESTIMATE of the true SE at `rho=-0.5`
  itself (where sampling variance would typically be smaller), making
  a "still excluded under this SE" verdict a conservative one, not an
  optimistic one — the opposite bias from the withdrawn `"13 sigma"`
  claim.

## What this would and would not settle

- **If `rho_band` on this same subsample comes out clearly positive**:
  supports Hypothesis A (observable difference explains the `TNG300`
  `+0.38` vs. true-NN near-zero gap) — a real, single-dataset
  discriminating result.
- **If `rho_band` is also near zero (within its own, likely wide,
  jackknife CI)**: does not by itself prove Hypothesis B (small `N_pairs`
  may simply mean this specific test is underpowered to detect
  anything) — report the honest power limitation rather than reading a
  wide null as confirmation of B.
- **Either way**: replaces the withdrawn `"13 sigma"` phrasing with a
  properly-scoped CI-based statement about `rho<=-0.5`.
- **Does NOT** resolve whether "top-N-most-massive-halos" is the right
  operational definition of v82's own "node" (still open, unchanged
  from both prior FLAMINGO/Magneticum/TNG300 findings).
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked to check: (a)
whether the jackknife block size/count is defensible for this NN
statistic, (b) whether the `rho_band` sample size is large enough to
support whatever verdict (A/B/underpowered) this addendum reaches, (c)
whether the corrected CI-based `-0.5` statement is itself properly
scoped this time.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
