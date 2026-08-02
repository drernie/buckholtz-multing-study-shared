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

---

## Update 2026-08-02 — after Blind B

### Status changes

| Claim | New status |
|---|---|
| A 1/r³ term is present in public kSZ data | **NOT DETECTED** (ℓ̂_d = 0 exactly; Δχ² = 0.000000) |
| Weighted stat-only result ≈ 8.34 Mpc at r_lo = 6 | **CROSS-IMPLEMENTATION REPRODUCED** |
| Raw result ≈ 11.23 Mpc | **REPRODUCED AS AN ALTERNATIVE MODEL** |
| Spec v1 defines the analysis unambiguously | **REFUTED** |
| v1 is a frozen specification | **INVALIDATED** |
| A single physical limit equals 8.34 Mpc | **NOT ADMITTED** |
| The limit is conditional on r_lo | **VERIFIED** — monotone 5.43→8.97, no plateau |
| PV defines K₃ mathematically | **SUPPORTED** |
| PV is the unique physical completion | **OPEN** |
| Weighting of K₃ follows from the estimator | **OPEN / MODEL ASSUMPTION** (was over-claimed as DERIVED) |

### The distinction that matters

Admissible: *the numerical implementation of the intended weighted analysis has
been independently reproduced.*

**Not** admissible: *frozen specification v1 has been independently reproduced.*
Blind B proved the opposite — v1 does not determine a unique analysis.

### Blind B's independent numbers (its own computation, weighted reading)

```
K_2^w(100)  = 1.2024593877       K_3^w(100) = 0.015480160151
ell_d_hat   = 0.0000 exactly     unconstrained stationary point mu* = -3.5228
L95         = 8.34 +- 0.02 Mpc   (r_lo = 6, MC only)
r_lo scan   = 8.970 ... 5.427 Mpc, monotone, factor 1.65
coverage    = 0.948-0.952 across 8 mu_true, 200k sims each
Delta chi2  = 0.000000  ->  p = 0.500 (boundary mixture)
kSZ signal  = A_hat 0.024579 +- 0.004115  ->  5.97 sigma with the K_2 template
```

The 5.97σ detection of the kSZ signal itself matters: the null result on ℓ_d is
not caused by absence of data or of sensitivity to the signal.

### Agreement with our implementation

| quantity | ours | Blind B | Δ |
|---|---|---|---|
| K₃ʷ(100) | 0.015653 | 0.015480 | 1.1% |
| ℓ̂_d | 0.00 | 0.0000 | exact |
| L₉₅ at r_lo=6 | 8.50 | 8.34 | 1.9% |
| r_lo range | 9.00–5.25 | 8.970–5.427 | ~2% |

Numerical reproducibility: **achieved**. Specification reproducibility: **not**.

### Externally admissible statement

> We find no evidence for an additive 1/r³ contribution in the public
> pairwise-kSZ data. Under a pair-weighted, fixed-template continuum
> implementation with lower support boundary r_lo = 6 Mpc, independent
> implementations give a calibrated stat-only upper sensitivity near 8.3 Mpc
> for ℓ_d = A₃/A₂. Varying that unsupported boundary over its plausible range
> moves the endpoint from about 5.4 to 9.0 Mpc, so the result remains
> conditional on model support below the measured correlation-function range.
