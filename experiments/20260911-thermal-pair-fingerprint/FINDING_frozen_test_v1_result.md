# FINDING — frozen test v1: mechanical verdict INCONCLUSIVE, skeptic-confirmed

**Continues:** `FROZEN_PROTOCOL_v1.md` (criteria fixed and committed at
`8161242`, executor committed at `c79074e`, both BEFORE this file's
own result existed) → `final_frozen_test.py`'s actual run.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## Result

| r (Mpc) | raw p_pair | raw z | detrended z | n_pairs |
|---|---|---|---|---|
| 592.9 | -13.24 | -4.23 | +0.38 | 1,376,265 |
| 1442.2 | -22.94 | -4.02 | +0.39 | 1,376,265 |
| 1946.2 | -35.35 | -4.25 | -0.03 | 1,376,265 |
| 2457.8 | -51.08 | -3.72 | +0.17 | 1,376,265 |
| 2992.9 | -82.42 | -3.25 | +0.32 | 1,376,265 |
| 3562.4 | -149.58 | -2.92 | -0.06 | 1,376,265 |
| 4786.8 | -209.49 | -1.43 | -0.60 | 1,376,264 |

**Mechanical evaluation of `FROZEN_PROTOCOL_v1.md` §3:**
- Condition 1 (raw |z|≥3 in the 2 smallest-r bins): **True** (4.23, 4.02)
- Condition 2 (correct sign, negative): **True**
- Condition 3 (peak |p_pair| NOT at largest-r bin): **False** — the
  maximum, 209.49, sits exactly at the largest-separation bin (index 6
  of 6)
- Condition 4 (detrended |z|≥2 in the 2 smallest-r bins): **False**
  (0.38, 0.39)

**VERDICT: INCONCLUSIVE** (conditions 1-2 pass → not REJECT; conditions
3-4 fail → not PROMOTE).

## Independent skeptic review (Step 4 of the frozen protocol)

Context-blind `Agent(skeptic)` — given only `FROZEN_PROTOCOL_v1.md`'s
criteria + the raw numeric table above, no session reasoning chain.
**Verdict: CONFIRMED.** Independently re-derived all four conditions
from the raw numbers, checked for exploitable ambiguity in bin
indexing, "largest bin" definition, and the one-pair discrepancy in the
last bin's `n_pairs` (1,376,264 vs 1,376,265 elsewhere) — none of it
changes any condition. Spot-checked directly against the raw log by me
as well (`audit-verification-gate.md`: an agent's `[VERIFIED]` is this
session's `[INFERRED]` until independently re-checked) — matches.

**One substantive observation the skeptic added, correctly flagged as
a policy question, not an application error:** the raw `|p_pair|`
sequence is *strictly monotonically increasing* across all 7 bins
(13.24 → 22.94 → 35.35 → 51.08 → 82.42 → 149.58 → 209.49), the peak
sits exactly at the largest-separation bin, and detrending collapses
every bin to `|z|≤0.60`. The skeptic's own words: *"a textbook large-
scale-trend artifact... If future revisions want REJECT to fire on
wrong-shape-plus-detrend-kill patterns, an explicit shape-artifact
clause would need to be added."* Per `FROZEN_PROTOCOL_v1.md`'s own
hard rule ("neither this file's criteria nor the pipeline they point
to may be edited in light of the result"), this is **not applied
retroactively** — v1's own criteria produce INCONCLUSIVE, and that
stands as v1's result. The observation is recorded here for a possible
v2 criteria design, not smuggled into v1's own verdict.

## What INCONCLUSIVE means here, concretely

This is the **same confound already diagnosed and documented**
(`FINDING_first_real_data_run_tsz_selection_confound.md`) — the frozen
run reproduces it almost exactly (same shape, same collapse-under-
detrend pattern, now in beam-corrected absolute units). The frozen test
did not discover anything numerically new; it **mechanically confirmed,
under pre-registered rules written before this run, that this specific
pipeline at this sample size does not yet show a real, shape-consistent
kSZ signal** — the significant-looking raw numbers are the redshift-
selection artifact, not evidence of pairwise infall.

## What this does NOT establish

Per `FROZEN_PROTOCOL_v1.md` §3's own closing paragraph, unchanged by
this result: no τ-weighting, no DR6-native beam/point-source products,
N=4390 (not survey-scale), single frequency band, no independent
replication. **This is not a REJECT of kSZ, and it is absolutely not
evidence about MULTING either way** — it is the honest outcome of a
first-pass, pre-registered, real-data test built on top of the
project's own already-known-imperfect pipeline.

## Status

**v1 frozen test complete: INCONCLUSIVE, skeptic-confirmed.** Per
`docs/151`'s status-separation rule: Empirical status = inconclusive at
this sample/pipeline; Ontological status = untouched (no mechanism
claim made either way); Causal status = untouched. Any further real-
data attempt (larger sample, τ-weighting, a v2 protocol with a
shape-artifact REJECT clause) is a new, separately-named test, not an
amendment to this one.
