# FINDING — FLAMINGO independent rho cross-check: WEAKENED to a real,
# well-powered null specifically for true-nearest-neighbor pairs; does
# NOT contradict the earlier all-pairs +0.38 reading (different
# observable), but firmly excludes a large rho for the observable this
# test actually measures

**Continues:** `CLAIM_flamingo_independent_rho_check.md` (committed
`292e563`, BEFORE `flamingo_independent_rho_check.py` was run) →
`FINDING_scale_matched_nearest_neighbor_rho.md` (`TNG300`, FALSIFIED)
→ `FINDING_magneticum_independent_rho_check.md` (`Magneticum`,
FALSIFIED — same nesting trap).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, from a live `hdfstream` connection, ONE
## pre-registered N — no sweep)

```
N = 1200 (real FLAMINGO L1_m9 fiducial z=0 halos, top-1200 by M200c)
median true-NN separation: 41.08 Mpc
mean true-NN separation:   43.70 Mpc

r (real) = -0.0231, t = -0.80, p = n.s.

Permutation null (1000 draws): mean = 0.0015, SD = 0.0359
Permutation p-value (two-sided): 0.5250
Sigma from null: -0.69
```

A clean, consistent-with-zero result — the first genuinely well-powered
measurement in this branch's own magnitude/mechanism thread (`N=1200`
vs. `TNG300`'s `N=30-50` and `Magneticum`'s `N=100-150`).

## Independent skeptic review (Step 8a, context-blind)

Given only the claim's own question, this result, and the design
rationale (single pre-registered `N`, chosen from a separate
exploratory pass). **Verdict: WEAKENED** — real null, but not as broad
in scope as a first reading suggests. All points independently
re-checked before accepting:

1. **Power calculation, independently re-derived: minimum detectable
   `|rho|` at 80% power, two-sided `alpha=0.05`, is `(1.96+0.84) *
   0.0359 ~ 0.10`.** Re-computed directly: `|rho|=0.38 -> ~10.6 sigma`
   (decisively excluded), `|rho|=0.20 -> ~5.6 sigma` (excluded),
   `|rho|=0.10 -> ~2.8 sigma` (borderline), `|rho|<0.05` not excluded
   by this data. **Response: accepted as the honest sensitivity of this
   specific test** — a large positive `rho` (comparable to `TNG300`'s
   own `+0.38` all-pairs number) is ruled out for this observable; a
   small one is not.
2. **Objection (accepted): true-nearest-neighbor pairs are a
   STRUCTURALLY DIFFERENT observable from "all pairs within a
   separation band"** (the source of `TNG300`'s own `+0.38` reading).
   NN selects isolated/local pairs; the band-based reading includes
   every pair at that separation regardless of whether either member's
   TRUE nearest neighbor is even in the pair. **This test does NOT
   contradict or falsify the `+0.38` reading** — it answers a different
   question that happens to sit at a similar separation. Framing it as
   "resolving" the earlier reading would itself violate this project's
   own Gate 1 (Artifact Identity) discipline — different objects,
   despite superficial similarity. Corrected explicitly here.
3. **Periodicity concern (raised, independently re-checked in the
   actual code — not just asserted): CONFIRMED handled correctly.**
   `true_nn()` applies the standard minimum-image convention (`diff -
   box_mpc * round(diff/box_mpc)`) before finding each halo's nearest
   neighbor — the skeptic raised this without having seen the code
   (only the printed results were given, per Context Asymmetry), so
   this is a legitimate question correctly answered by checking the
   actual implementation, not a live bug.
4. **Non-independence of the 1200 "pairs"** (each halo can be another's
   nearest neighbor multiple times; nearest-neighbor is directional, not
   mutual) — **already correctly absorbed by the permutation null**:
   independently re-verified the null `SD` (`0.0359`) is wider than the
   naive i.i.d. expectation `1/sqrt(N-1) = 0.0289` — exactly the
   inflation expected from real pair non-independence, confirming the
   permutation test (not the parametric `t`-test) is the trustworthy
   number, as already used for the primary result above.
5. **Selection-on-scale concern**: choosing `N=1200` because its own
   typical NN spacing matched the target window is selection on the
   SEPARATION axis, not on the correlation value itself — the
   false-positive rate is preserved (the null is computed at the SAME
   `N`). **Accepted nuance**: this is not literally "blind" in the
   sense of never having looked at ANY property of the sample before
   fixing `N` — stated precisely here rather than oversold as fully
   blind.

**Response (Step 8a matrix): all five points accepted, none dismissed,
independently re-verified (including re-reading this test's own code
for point 3) before accepting** (`audit-verification-gate.md`).

## What this DOES establish

- **The first well-powered measurement in this branch's own
  magnitude/mechanism thread.** For the TRUE-nearest-neighbor
  observable specifically, at `N=1200` (an order of magnitude larger
  than either prior attempt), `rho` is consistent with zero and a
  large positive value (`|rho| gtrsim 0.10`, which would include
  `TNG300`'s own all-pairs `+0.38` reading IF that same magnitude held
  for true-NN pairs) is decisively excluded.
- **`rho > -0.5` (`FINDING_P158`'s own safety threshold for the
  directional prediction) is now excluded from being violated with
  very high confidence** (`-0.5` sits `~13 sigma` from this
  measurement's own null distribution) — a genuine strengthening of
  that specific conclusion, with real statistical power behind it for
  the first time, not merely "no evidence found yet."
- Real, live, no-account/no-token public access to a THIRD independent
  simulation (`FLAMINGO`, third distinct cosmology, `~114x` [**CORRECTED
  2026-09-12: actually `~36x`, arithmetic error, see `CLAIM_flamingo_
  independent_rho_check.md`'s own correction note — no effect on any
  reported number**] `TNG300`'s
  volume) confirmed working via `hdfstream` — a genuinely useful,
  reusable capability for any future test needing more statistical
  power than `TNG300` or `Magneticum` alone can offer.

## [2026-09-12 correction, same day, not a rewrite — see
## `FINDING_flamingo_addendum_jackknife_band_closure.md`]

The `"rho > -0.5 ... excluded ... ~13 sigma"` sentence above (in "What
this DOES establish") is **WITHDRAWN as originally phrased** — caught
by the user, not self-caught. It divided the distance from the point
estimate to `-0.5` by the permutation-null SD (`0.0359`, the spread of
`rho_hat` under `H0: rho=0`), which is not automatically the correct
standard error for testing the distant composite hypothesis
`H0: rho<=-0.5` (`Var(rho_hat)` is not constant in `rho`). The
underlying qualitative conclusion survives, now corroborated by THREE
independent SE estimates (naive i.i.d. `0.0289`, permutation-null
`0.0359`, block-jackknife `0.0476`) instead of resting on one borrowed
number — but no single precise sigma-count is defensible this far into
a tail on non-i.i.d., spatially-clustered, truncated-selection data.
Read the addendum file for the full correction, the added `rho_band`
observable on the same subsample, and the Step 8a skeptic Response
Matrix.

## What this does NOT establish

1. **Does NOT contradict or resolve `TNG300`'s own all-pairs `+0.38`
   reading** — different observable (true-NN vs. all-pairs-in-band),
   per skeptic point 2 above. Both stand as independently-obtained,
   non-contradicting facts about two different quantities.
2. **Does NOT establish that `rho` is exactly zero or rule out a small
   positive value** (`rho lesssim 0.05-0.10` remains fully consistent
   with this result).
3. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).
4. **Does NOT resolve whether "top-N-most-massive-halos" is the right
   operational definition of v82's own "node"** — the same open mapping
   question named in both prior attempts, still not addressed.
5. Does not test the all-pairs-in-band observable at this simulation's
   own scale-matched separation — a genuinely different, not-yet-run
   test that WOULD be directly comparable to `TNG300`'s own `+0.38`
   reading, named here as a concrete next step, not attempted.

## Status

**A real, well-powered, honestly-scoped result — the strongest single
data point this branch's magnitude/mechanism thread has produced.**
Combined with the two prior (underpowered, genuinely undetermined)
attempts: the true-nearest-neighbor mass correlation at v82's own
target scale is now measured, with real statistical power, to be small
and not significantly different from zero — ruling out a large
positive value for THIS SPECIFIC observable, while leaving the
separate all-pairs-in-band question (where `TNG300`'s own `+0.38`
comes from) untouched by this particular test.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
