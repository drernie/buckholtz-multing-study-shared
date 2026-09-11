# NR-025 — thermal-pair-fingerprint fixed-window pair-count test design:
# REJECT (the test design, not the underlying MULTING mechanism)

**Date:** 2026-09-11
**Full writeup:** `experiments/20260911-thermal-pair-fingerprint/
FINDING_window_width_resolution.md` (this is the null_results copy, per
`falsification-ladder.md`'s own REJECT protocol — read the full writeup
for all tables and detail).
**Continues:** `FINDING_power_analysis.md` §6 (Exact Pair Census), which
fixed the window *center* (`d0=45` Mpc comoving, `[VERIFIED]` against
v82's own text) but left the window *WIDTH* undetermined.

## Claim tested

"A fixed comoving-separation window around `s=45` Mpc, counting real
cluster pairs within it and fitting one amplitude to the predicted
`S_M` shape, is a viable C1 kill-test — provided a defensible window
width can be chosen."

## What killed it

Two independent checks, both run on real ACT-DR5 MCMF cluster positions
(`arXiv:2406.14754`, `[VERIFIED]` row count):

1. **Q_stat** — power vs. window half-width, real `N(width)` from the
   real pairwise-separation array, same Monte Carlo methodology
   (`N_MC=4000`, `ΔAIC>6`+`|z|>1.96`, 3x noise) used throughout this
   branch. Power is monotonically increasing in width for `N≳15`
   (9.7%→97.8% across half-widths 2.5→75 Mpc) — **no interior optimum**.
   Under the current model (every pair drawn from the same `xi`
   distribution regardless of its own separation), widening the window
   is trivially always better for power.
2. **Q_data** — the real two-point correlation excess `1+ξ(s) =
   N_observed(s)/N_Poisson(s)`, computed analytically (not fit) from
   the real `N=4390`, real `z`-shell volume, real footprint. It is a
   smoothly, monotonically **declining** function of `s` (standard
   large-scale-structure behavior) — `[40,50)` Mpc, the bin containing
   `s=45`, is not even a local maximum among its own neighbors
   (`[30,40)=2.93` and `[50,60)=2.04` both exceed it, `[40,50)=1.97`).

Together: no width maximizes power (short of converging on the already
separately-tested broad-window statistic), and no width is picked out
by the real data's own clustering statistics either. `s=45` Mpc has no
independent physical signature — it is solely `v82`'s own frozen
initial condition for one hypothetical trajectory.

## Kill Analysis

- **Killed:** the specific test design — "count real pairs within an
  arbitrary window around a fixed separation, fit one amplitude." No
  width for that design is derivable from power-maximization (monotone)
  or from real clustering data (no local feature at 45 Mpc).
- **NOT killed:** MULTING's underlying `ξ∝1/s`, sign-crossing force
  law; the broad-window kSZ-literature test (already separately
  answered, `N≈449`, `100%` power at the Fork-2 mid footprint — a
  different, non-characteristic-specific test); the possibility of a
  genuinely different test design.
- **Relaxation map:** the one surviving, not-yet-built option is a
  continuous fit of `S_M(s)` against each real pair's own separation
  (not sorted into a window) — a different Summary Measure, requiring
  an `estimand.md` amendment before any code, per this branch's own
  standing FL/EstimandOps discipline. Not attempted here; named as the
  live option for the next decision point.

## Revival condition

Only a materially different test design (the `s`-dependent fit named
above, or some other Endpoint choice not yet named) — not a different
window width under the same count-based design, which this entry
already shows has no principled choice.
