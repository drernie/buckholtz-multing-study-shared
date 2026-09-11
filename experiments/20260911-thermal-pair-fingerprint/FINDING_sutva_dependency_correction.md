# FINDING — SUTVA/dependency bug in the power analysis, found by external
# review of the published repo: real, verified, fixed — practical impact
# on the headline power number turned out small; impact on Positivity
# was real and non-trivial

**Date:** 2026-09-11
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Source:** an external, independent review of the published shared
repository (`buckholtz-multing-study-shared`), pasted by the user.
Verified directly before applying, per `method_verify_pasted_ai_
reports.md` — not accepted on the critique's own word.
**Continues:** `power_analysis_s_dependent.py`, `FINDING_power_
analysis_s_dependent.md`.

---

## 1. The claim, and what verification actually found

**Claim:** `estimand.md`'s own Population/SUTVA exclusion rule ("a
cluster appearing in more than one candidate pair is assigned to at
most one pair... the same physical object cannot licitly appear as an
independent unit twice") was violated by `power_at_n()`'s own
`rng.integers(0, pool_n, size=n_target)` — sampling WITH REPLACEMENT
from the full 7693-pair COMBINATORIAL pool (every candidate pair among
4390 clusters), not a cluster-disjoint set.

**Verified directly, not taken on the critique's word:**

```
N clusters: 4390        N candidate pairs (pool): 7693
mean # candidate pairs per cluster: 3.93   max: 18

Single trial, N=449: 439 unique pair-rows drawn (10 literal duplicate
  draws), and of the 449 sampled pairs, 194 (43.2%) shared a real
  cluster with at least one OTHER sampled pair in the SAME trial.
```

**The claim is correct.** This is a real, structural violation of the
independence `one_trial()`'s own OLS fits implicitly assume, and of
`estimand.md`'s own explicit exclusion rule — not a minor statistical
nitpick.

**A second, separately-checked claim in the same critique** ("the
public repo shows 943 commits, not the claimed 961") was checked
independently against the GitHub API (`gh api repos/.../branches/main`
and `gh api .../commits --paginate`), not just local `git log`: **both
return 961 commits, tip SHA `9e0d3418...`, exactly matching what was
pushed.** The critique's own "943" figure does not reproduce — most
likely a transient web-UI cache right after the force-push finished
re-indexing, not a real discrepancy. Stated plainly since the critique
itself flagged this as unconfirmed on their end.

---

## 2. The fix

Added `build_disjoint_matching()` — a real greedy matching over the
candidate-pair graph (clusters = nodes, candidate pairs = edges):
walk candidate pairs in a given order, accept a pair only if NEITHER
cluster has been used by an already-accepted pair. This is
`estimand.md`'s own exclusion rule, made concrete and executable.

**Tie-break order matters, and is reported, not hidden:**

| order | disjoint pairs | Positivity fraction |
|---|---|---|
| RANDOM (primary, used below) | 1651 | 4.664% |
| smallest-`s`-first (sensitivity) | 1665 | 15.135% |
| (original combinatorial pool, for reference) | 7693 | 3.978% |

**The smallest-`s`-first version is a real, confirmed bias** — exactly
the self-serving-selection risk flagged when this matching was first
designed (choosing "closest match first" without real `M/Env/Dyn`
matching variables risks silently favoring the small-`s`/high-`ξ`
regime this whole branch's headline results live in). It was
deliberately NOT used as the primary construction for this reason; the
`3.2×` fraction inflation it produces (`15.135%` vs `3.978%`) confirms
that caution was warranted. **The RANDOM-order result — a real, smaller
increase (`4.664%` vs `3.978%`, `+17%` relative) — is the reported,
primary number.**

`power_at_n_disjoint()` replaces `power_at_n()`'s with-replacement
sampling with `rng.choice(pool_n, size=n_target, replace=False)` drawn
from this real disjoint set — within one Monte Carlo trial, no cluster
and no pair repeats. `power_at_n()` itself is kept, explicitly marked
`[WITHDRAWN DESIGN]`, only for the honest before/after comparison.

---

## 3. The corrected numbers — real, and a genuine surprise

**Positivity moved (a real, modest increase):** `3.978%` (combinatorial,
`[WITHDRAWN]`) → **`4.664%`** (random-order disjoint, `[VERIFIED-run]`,
the corrected number).

**Power, at the same `N=449`, `3x` noise reference point, barely
moved:**

```
(a) old window-based design (REJECTED, NR-025):        100.0%
(b) WITHDRAWN s-dependent, with-replacement (this
    script's own prior run):                            59.9%
(c) CORRECTED s-dependent, without-replacement from
    the real disjoint matching:                          59.1%
```

**`59.9%→59.1%` is within Monte Carlo noise** (`N_MC=4000`, expected
SE on a proportion near 0.6 is `~0.8` percentage points) — this is
NOT evidence the bug didn't matter in principle; it is a real,
measured fact about THIS SPECIFIC mock's own generative structure.
**Stated plainly, not glossed over:** `one_trial()`'s mock draws fresh,
independent `xi_a`, `xi_b`, and noise PER ROW regardless of whether two
rows happen to share a real cluster — the mock has no per-cluster
latent variable that would make cluster-sharing produce correlated
rows. So the SUTVA violation was a real, structural correctness bug
(the sampled rows were not drawn from a valid disjoint population,
exactly as the critique said) — but its PRACTICAL consequence for the
power number specifically was small, because this simplified mock does
not yet model the kind of shared-cluster measurement dependence that
would make repeated-cluster pairs behave differently from independent
ones. **A more realistic future mock — one with an explicit per-cluster
latent measurement/systematic term — could show a larger gap; this one
does not, and that is reported honestly rather than assumed away.**

Full corrected power grid (`N_MC=4000`, `10`-`1000` pairs, real
disjoint ceiling `1651` — `N=2000` dropped as infeasible):

| N_pairs | 1x | 3x | 10x |
|---|---|---|---|
| 10 | 0.3% | 0.1% | 0.0% |
| 50 | 62.2% | 11.0% | 0.5% |
| 100 | 69.5% | 28.4% | 1.1% |
| 200 | 70.7% | 48.1% | 2.5% |
| **449** | 73.9% | **59.1%** | 8.4% |
| 1000 | 78.7% | 59.1% | 24.9% |

False-promote stayed at `0.0-0.2%` throughout, if anything slightly
lower than the withdrawn design's own numbers.

---

## 4. What this does NOT establish

1. Does not establish that SUTVA violations are generally harmless for
   this design — only that, for THIS mock's own simplified generative
   model (no shared-cluster latent variable), the practical effect on
   `N=449`'s power was small. A different, more realistic mock could
   show a larger effect; this has not been built or tested.
2. Does not resolve the matching tie-break ambiguity — `estimand.md`'s
   own "closest match on the matching variables" (`M`, `z`, `Env`,
   `Dyn`) cannot be implemented faithfully without those variables,
   which this mock does not have. RANDOM order is the primary, honest
   choice made here, not a resolution of what the real matching rule
   should be.
3. Does not touch the `[20,160]` Mpc population window's own open
   status (still not independently re-verified against the source kSZ
   paper's own methods section).
4. Not a claim about MULTING (`NO_AUTHOR_ERROR`) — entirely about
   whether this project's own mock design respects its own estimand's
   stated unit of analysis.

## Status

**Fixed, `[VERIFIED-run]`, both directions of the correction reported
honestly:**

```
Bug: CONFIRMED real (43.2% of sampled pairs at N=449 shared a cluster
  with another sampled pair in the same trial before the fix).
Fix: real cluster-disjoint matching (1651 pairs, random-order tie-break,
  chosen specifically to avoid the smallest-s-first bias also measured
  and reported: 3.2x Positivity inflation, correctly NOT used).
Positivity: 3.978% (withdrawn) -> 4.664% (corrected) -- real, modest increase.
Power @ N=449, 3x: 59.9% (withdrawn) -> 59.1% (corrected) -- within MC
  noise, a genuine and reported surprise, explained by this mock's own
  lack of a per-cluster shared latent variable, not asserted away.
Commit-count discrepancy (943 vs 961): 961 independently reconfirmed via
  GitHub API, not just local git -- the critique's own flagged
  uncertainty resolved, no real discrepancy found.
```

Next: the synthetic four-world identifiability battery (`estimand.md`'s
own hard pre-data gate), now built on this corrected, SUTVA-compliant
sampling machinery from the start — not run against the withdrawn
design.
