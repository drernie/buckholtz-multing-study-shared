# FINDING — synthetic four-world identifiability battery: ADEQUATE

**Date:** 2026-09-11
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Artifact:** `synthetic_four_world_battery.py` — real code, real
output, `[VERIFIED-run]` (`N_MC=4000` per cell, 12 cells: 4 worlds × 3
`N` values, all at 3x noise).
**Continues:** `estimand.md`'s own Pre-Data Requirement — the
synthetic four-world identifiability battery, its own named hard gate
before any code may touch real kSZ/tSZ data (`falsification-ladder.md`
Step 2b, Oracle Adequacy Gate). Built on the SUTVA-corrected sampling
machinery from `FINDING_sutva_dependency_correction.md`, not the
withdrawn design — the battery was never run against the bug.

---

## 1. The four worlds, as actually generated

1. **World MULTING** — `power_analysis_s_dependent.py`'s own
   `one_trial(..., h_m_true=True)`, unchanged: real `(z,s)`, real
   `ξ_pred(z,s)`, lognormal scatter, `S_M` sources `y`.
2. **World optical-depth-confounded** — `y` LINEAR in `ξ_pred(z,s)`
   (exactly Model 2's own regressor), amplitude-matched to World 1's
   own signal RMS at the same sample. Operationalizes "a real
   `ξ`-correlated channel exists, but not `S_M`'s specific quadratic-
   reversal shape" — the closest available proxy given this mock has no
   explicit per-cluster `K`/`G` variables to route a literal
   `G→τ→V_kSZ` backdoor through.
3. **World merger-confounded** — `y` driven by `1/s` ALONE, with NO
   `z`-dependence (unlike real `ξ_pred`, which entangles `z` via `Q(z)`
   and `s` together), same amplitude-matching convention. A
   structurally distinct confound from World 2, not a relabeling.
4. **World null** — `one_trial(..., h_m_true=False)`, unchanged: pure
   noise, no signal at all.

All four sample from the SAME real, cluster-disjoint matching
(`1651` pairs, `[VERIFIED-run]`, same construction as the corrected
power analysis) via without-replacement draws — the battery itself
respects the SUTVA fix from the start.

---

## 2. Result

| world | N=100 | N=449 | N=1000 | expectation |
|---|---|---|---|---|
| 1 MULTING | 27.0% | 57.2% | 59.5% | SHOULD promote |
| 2 optical-depth-confounded | 0.0% | 0.0% | 0.0% | should NOT |
| 3 merger-confounded | 0.0% | 0.0% | 0.0% | should NOT |
| 4 null | 0.2% | 0.1% | 0.0% | should NOT |

**Verdict: ADEQUATE.** Worlds 2 and 3 promote at exactly `0.0%` across
every scanned `N` — the pipeline's three-part bar (beat Model 0 AND
Model 2 AND show the direction-matched sign reversal at `ξ_peak`)
correctly rejects both confound types with no exceptions in `4000×3×2`
mock trials. World 4 stays at the same low baseline already established
elsewhere in this branch (`0.0-0.2%`, consistent with the corrected
power analysis's own false-promote rate). World 1 promotes at a real,
substantial rate, growing with `N` as expected.

**Cross-check, noted honestly, not hidden:** World 1's own `57.2%` at
`N=449` differs slightly from the dedicated power analysis's `59.1%`
at the identical `(N, noise)` point (`FINDING_sutva_dependency_
correction.md`). Both use the same underlying `(z,s)` disjoint
matching and the same `one_trial()`, but the two scripts run
independent RNG streams in a different call order (this script's own
`rng` drives world-2/3 generation and the sample draw, while `one_trial()`
draws from `power_analysis_s_dependent.py`'s own module-level `rng`) —
a `~1.9`-point gap at `N_MC=4000` is within the expected range of
inter-run Monte Carlo variation from that difference, not a
discrepancy requiring investigation; both numbers tell the same
qualitative story.

---

## 3. What this does NOT establish

1. Worlds 2/3 are **operationalized proxies**, not literal simulations
   of the real DAG's `G→τ→V_kSZ` or `Dyn→{K,V_true}` paths — this mock
   has no explicit per-cluster `K`/`G`/`Dyn` variables. A more faithful
   battery would need those built first; named, not attempted here.
2. Passing this battery clears `estimand.md`'s own hard pre-data gate —
   it does **not** touch real kSZ/tSZ data, and does **not** validate
   anything about MULTING itself (`NO_AUTHOR_ERROR`).
3. Only `3x` noise was scanned for the battery itself (the dedicated
   power analysis already covers `1x/3x/10x` for World 1 alone) —
   narrower coverage than the main power grid, a scope choice, not an
   oversight.
4. Does not resolve the `[20,160]` Mpc population window's own open
   status, or the matching tie-break ambiguity already named in
   `FINDING_sutva_dependency_correction.md`.
5. A `0.0%` promote rate for worlds 2/3 at `N_MC=4000` is consistent
   with a true rate anywhere below roughly `0.1%` (the one-sided 95%
   upper confidence bound for zero successes in 4000 trials) — reported
   as `0.0%`, not overclaimed as "provably impossible."

## Status

**PASSED — ADEQUATE, `[VERIFIED-run]`:**

```
World MULTING:                 27.0%-59.5% promote (grows with N, as expected)
World optical-depth-confounded: 0.0% promote at every scanned N
World merger-confounded:        0.0% promote at every scanned N
World null:                     0.0-0.2% promote (matches established false-promote baseline)
Oracle Adequacy Gate verdict:   ADEQUATE
```

Per `estimand.md`'s own Status section, this was the last remaining
named hard gate before any code touching real kSZ/tSZ data. Next, per
`data_acquisition_plan.md`'s own Fork 1: build the classical pairwise-
kSZ estimator (Fork 1b, the largest remaining real cost in this branch,
still `~1-3 weeks` per that plan's own estimate) — or send the real
data-request in parallel (Fork 1, option 1a). Neither started here;
this file closes the LAST synthetic/mock-only gate, not the real-data
acquisition itself.
