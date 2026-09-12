# FINDING — Magneticum independent rho cross-check: FALSIFIED as a
# resolving test, WEAKENED as a data point; the same nesting trap that
# falsified the TNG-300 attempt recurs in a completely different
# simulation

**Continues:** `CLAIM_magneticum_independent_rho_check.md` (committed
`af81339`, BEFORE `magneticum_independent_rho_check.py` was run) →
`FINDING_scale_matched_nearest_neighbor_rho.md` (the `TNG300`-only
attempt, also FALSIFIED as a resolving test).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Result (real, downloaded data — Magneticum Box2_hr/snap_140,
## 10,493 real clusters, proper 1000-draw permutation null)

```
N_sub  mass_floor(Msun/h)  med_NN(Mpc)  mean_NN(Mpc)  r(real)  t     p       null_mean  null_SD  perm_p
100    1.583e14            45.00        49.52         0.1577   1.58  n.s.    -0.0088    0.1229   0.2130
110    1.525e14            42.88        48.50         0.1416   1.49  n.s.    -0.0075    0.1202   0.2360
120    1.451e14            41.61        46.52         0.2102   2.34  <0.05   -0.0071    0.1163   0.0710
125    1.432e14            40.83        45.73         0.1701   1.91  n.s.    -0.0034    0.1102   0.1320
130    1.369e14            38.60        44.75         0.1762   2.02  <0.05   -0.0090    0.1126   0.1160
140    1.319e14            39.25        43.44         0.1617   1.92  n.s.    -0.0086    0.1061   0.1340
150    1.271e14            38.31        41.21         0.1070   1.31  n.s.    -0.0068    0.1026   0.2900
```

All 7 values are positive (`0.11-0.21`) — qualitatively different from
`TNG300`'s own sign-flipping sweep (`-0.50` to `+0.09`). At first
reading this looked like real corroboration for `rho>0` at v82's own
scale, from a genuinely independent simulation. **This does not survive
scrutiny — see the skeptic review below, independently re-verified.**

## Independent skeptic review (Step 8a, context-blind)

Given only the claim's own question, this table, and the null/scale
context. **Verdict: FALSIFIED as a resolving test, WEAKENED at best as
a data point.** All points independently re-checked before accepting:

1. **The 7 thresholds are severely non-independent — the SAME nesting
   trap that falsified the `TNG300` attempt.** `N_sub=100` is a strict
   subset of `N_sub=110`, ..., of `N_sub=150`; adjacent thresholds share
   `91-95%` of clusters, and even the two extremes (`N=100` vs. `N=150`)
   share `100/150 = 67%`. **"All 7 positive" is effectively ONE
   measurement repeated with heavy overlap, not 7 independent
   confirmations** — under the null, one positive draw has `~50%`
   probability, not `(1/2)^7`. Re-checked directly: correct.
2. **Properly treated as one effective measurement**: mean of the 7
   `r` values is `~0.16`, against a null `SD` of `~0.11` — **`~1.3-1.5
   sigma` from zero, not significant.** Every individual permutation `p`
   is `>=0.07`; the single best point (`N_sub=120, p=0.071`) is exactly
   the kind of borderline-threshold cherry-pick this project's own prior
   `TNG300` skeptic pass already flagged as illegitimate to lean on.
3. **The parametric `t`-test and the permutation `p`-value disagree at
   `N_sub=120,130`** (`t`-test `<0.05`, permutation `>0.05` at both).
   The permutation result should be trusted: `N<=150` is small, the
   nearest-neighbor pairing is not i.i.d. (see point 5), and the `t`-test
   assumes both large-`N` normality and independence that the permutation
   test does not need to assume.
4. **Window-slippage recurs, milder but real**: `mean_NN` at
   `N_sub=100,110` (`49.52, 48.50 Mpc`) sits OUTSIDE the `40-45 Mpc`
   target — re-checked directly against the printed table: correct.
   Same failure shape as `TNG300`'s own `N_sub=30` point (median outside
   the window despite looking significant).
5. **Cross-simulation comparison is not rigorously matched.**
   `TNG300` and `Magneticum` differ in code, cosmology, random phases,
   halo/cluster finder, AND mass definition (`m500c` here vs. `M_Crit200`
   there) — "Magneticum is sign-consistent where `TNG300` was not" is
   suggestive, but not a controlled comparison; the same permutation-
   null, same-`N`-range analysis was never re-run on `TNG300` itself for
   a fair side-by-side. Under the null, "different sign in one
   simulation, positive in another" is also the expected pattern for two
   independent noise-dominated small-`N` measurements.
6. **Nearest-neighbor pairing is asymmetric** (A's nearest neighbor
   being B does not imply B's nearest neighbor is A) — a cluster can be
   "the neighbor" of several different anchors, so treating `N` clusters'
   own-NN relations as `N` independent pairs overstates the effective
   sample size further, on top of point 1's nesting issue.

**Response (Step 8a matrix): Accepted, no dismissal, all six points
independently re-verified against the raw numbers before accepting**
(`audit-verification-gate.md`).

## What this DOES establish

- **A second, independently-obtained confirmation that the underlying
  methodological trap (nested/non-independent threshold sweeps
  masquerading as multiple confirmations) is not specific to `TNG300`
  or to this project's own choice of dataset** — it recurred, in a
  different shape (consistently marginal instead of sign-flipping), in
  a completely different, independently-downloaded simulation. This
  strengthens (does not merely repeat) the `pearl_registry` lesson
  already recorded from the `TNG300` attempt.
- **The magnitude/mechanism question is now UNDETERMINED across TWO
  independent simulations**, not just one — a more robust "genuinely
  don't know" than either dataset could establish alone, which is
  itself informative: this is not `TNG300`-specific bad luck, the
  underlying rarity of massive, appropriately-separated clusters at
  this exact scale in any single reasonably-sized box appears to be a
  real, structural data-scarcity problem, not a fluke of one
  simulation's own realization.

## What this does NOT establish

1. **Not corroboration of `rho>0` at v82's own scale** — the "all 7
   positive" pattern does not survive the nesting correction; properly
   treated as one measurement, it is `~1.3-1.5 sigma`, not significant.
2. **Not evidence against `rho>0` either** — genuinely undetermined,
   same as the `TNG300` result.
3. Not a claim about v82's own theory (`NO_AUTHOR_ERROR`).
4. **Not the final word** — a rigorous, matched re-analysis (same
   permutation-null method, same `N`-range logic, applied identically
   to BOTH `TNG300` and `Magneticum` side by side) has not been done;
   named as the concrete next step if this question is worth pursuing
   further, not attempted here.

## Status

**Genuinely UNRESOLVED, now independently reconfirmed as unresolved
rather than resolved — recorded honestly, not forced toward the
positive-looking raw pattern.** Two independent simulations, two
independent skeptic passes, the same core trap in both. A future
attempt would need either a single, sufficiently large independent
simulation with genuinely non-overlapping sub-samples (not nested
thresholds on one catalog), or accept that this specific question may
not be answerable with currently-accessible public simulation data at
adequate statistical power.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
