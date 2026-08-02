# docs/134 — Claim registry: kSZ dipole constraint

**L0:** descriptive · NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
Invalidated claims are **retained**, never deleted — the lineage is the record.

---

## Active claims

### ACT-KSZ-ELL-D-WEIGHTED-STAT-v1

```
Result:      L95 = 8.00 Mpc  (stat-only)
Status:      CROSS-IMPLEMENTATION-REPLICATED
Coverage:    0.9480 +- 0.0035 (independent validation ensemble) — PASS
Nuisance:    8.00 / 8.50 / 7.50 for A_cond / +1s / -1s
Best fit:    ell_d_hat = 0.00 (unconstrained -3.50, clipped 0.00)
Scope:       stat-only; pair-weighted estimator; r_lo = 6 Mpc;
             PV prescription eps = 0.05 Mpc; 15 bins 25-225 Mpc
Blockers:    estimator derivation, double-counting audit, r_lo,
             units dual-run, Blind B
Spec:        docs/133
```

### ACT-KSZ-ELL-D-RAW-STAT-v1

```
Result:      L95 = 11.00 Mpc  (stat-only)
Status:      REPLICATED-WITH-COVERAGE-CAVEAT
Coverage:    0.9605 +- 0.0031 — CONSERVATIVE OVERCOVERAGE (3.4 sigma high)
Issue:       grid-quantised endpoint; the 0.5 Mpc calibration step is a
             HYPOTHESIS for the overcoverage, not a demonstration
Nuisance:    11.00 / 11.00 / 11.00 — insensitive
Best fit:    ell_d_hat = +3.20 (unconstrained +3.20, so clipping is a no-op)
Scope:       stat-only; raw (unweighted) estimator; otherwise as above
Blockers:    as above, plus the fine-grid coverage regression
Spec:        docs/133
```

**These two must not be merged.** They are different forward-model definitions,
not two measurements of one quantity. No averaging, no combined systematic.

## Verified methodological claims

| Claim | Status |
|---|---|
| A one-sided upper limit requires q̃_μ, not the two-sided q_μ | **VERIFIED** (two independent implementations) |
| Analytic amplitude profiling is correctly implemented | **VERIFIED** (7e-15 / 1.4e-14 vs direct optimisation) |
| Constrained MLE coincides with unconstrained-then-clipped **in this task** | **VERIFIED — task-specific**, not a general result |
| C₂ = 1 inside / 0 outside (shell theorem) | **VERIFIED** both implementations |
| Mass at r′ > R is required for p > 2; one-sided truncation is log-divergent | **VERIFIED** |
| K₃ exists only as a Cauchy principal value (simple antisymmetric pole) | **VERIFIED** |
| K₄ has a double pole — no PV, not constrainable this way | **VERIFIED** |
| No statistically significant 1/r³ signal | **ROBUSTLY SUPPORTED** |

## Open

| Question | Status |
|---|---|
| Is the pair-weighted estimator the correct one? | **OPEN / PROVISIONALLY FAVOURED** |
| Is the raw estimator correct? | **DISFAVOURED, NOT FORMALLY REFUTED** |
| Is PV the *physical* UV completion? | **NOT ESTABLISHED** (mathematically canonical only) |
| Does r_lo materially move the limit? | **SUPPORTED BY BLIND A, not locally reproduced** |
| Is 8.00 Mpc a final physical limit? | **NOT ADMITTED** |
| Blind B reproduction | **OPEN** |

## Invalidated lineage — retained deliberately

```
ACT-KSZ-ELL-D-15-17-v1
  Result:      15.0-17.5 Mpc
  Status:      INVALIDATED
  Reason:      two-sided statistic used to build a one-sided upper limit
  Superseded:  ACT-KSZ-ELL-D-WEIGHTED-STAT-v1, ACT-KSZ-ELL-D-RAW-STAT-v1

ACT-KSZ-ELL-D-5.95-v1
  Result:      5.95 Mpc
  Status:      INVALIDATED
  Reason:      grid-dependent; K3 log-divergent, K4 linearly divergent,
               masked by a fixed 240-node quadrature
  Detected by: blind analytic skeptic with zero code execution

ACT-KSZ-BETA-D-9E5-v1
  Result:      beta_d < 9e5
  Status:      INVALIDATED
  Reason:      0.3 x 100 Mpc = 30 Mpc landed on the sign-change wall;
               an artifact of the perturbative slope formula, never a likelihood

ACT-KSZ-ELL-D-10-v1
  Result:      ~10 Mpc
  Status:      SUPERSEDED
  Reason:      kernel integrated only r' < R, omitting the opposite-sign
               outside-mass contribution (-15.8%)
```

## Note on the word "independent"

The re-check reimplemented the statistic without importing or reading Blind A's
code — but it **knew Blind A's numbers in advance**. Correct label:
**cross-implementation numerical replication**. `INDEPENDENTLY REPRODUCED` is
reserved for Blind B, run against a frozen specification with no knowledge of
expected values.
