# docs/133 — Statistical Decision Record: kSZ dipole limit

**Date:** 2026-08-02 · **L0:** descriptive
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
**Scope:** freezes every statistical choice behind `ACT-KSZ-ELL-D-*-STAT-v1`.
**This is NOT a final physical limit.** See §6 for what remains open.

---

## 1. Frozen specification

| Item | Value |
|---|---|
| Primary parameter | ℓ_d = A₃/A₂, in Mpc |
| Parameter domain | ℓ_d ≥ 0 (repulsive dipole in the model under test) |
| Test statistic | one-sided q̃_μ (see §2) |
| Nuisance | amplitude A, analytically profiled |
| Nuisance variation | A_cond, A_cond ± 1σ_A |
| μ grid (evaluation) | 0 … 60 Mpc, step 0.05 |
| μ grid (calibration) | 0 … 20 Mpc, step 0.5 ← **quantises the raw endpoint** |
| Calibration ensemble | 4000 sims per μ |
| Validation ensemble | 4000 sims, **separate draws** from calibration |
| RNG seed | 11081987 (numpy default_rng) |
| Covariance | shipped 18×18, sliced to the 15 fitted bins |
| Hartlap factor | α = (N−p−2)/(N−1) = 983/999 = 0.9840, N=1000, p=15 |
| Fitted bins | 15 bins, 25 ≤ r ≤ 225 Mpc |
| Weighting convention | **two separate claims** — raw and pair-weighted, never merged |
| UV / PV prescription | symmetric exclusion \|r′−R\| ≥ ε, ε = 0.05 Mpc → approximates the Cauchy principal value |
| r_lo | 6.0 Mpc (upstream choice — **not justified from first principles**) |
| r_hi | 262.19 Mpc (full ξ range; contribution beyond is 0.0072% of the kernel) |
| ξ interpolation | cubic spline, zero outside the measured range |
| Units | ξ separations converted Mpc/h → Mpc with h = 0.677; kernels and ℓ_d in Mpc |

## 2. The statistic, and why the previous one was wrong

An earlier attempt used the **two-sided** profile statistic
`q_μ = χ²(μ) − χ²(μ̂)` to build a **one-sided** upper limit. That is the wrong
object. The correct one is

```
q̃_μ = 0                        if μ̂ > μ
     = χ²(μ) − χ²(μ̂)           if 0 ≤ μ̂ ≤ μ
```

with μ̂ the **constrained** MLE, `argmin_{μ≥0} χ²_prof(μ)` — not an
unconstrained minimum clipped afterwards. In this problem the two coincide
(verified, §3 G2), but that is a property of this dataset, not a general fact.

Amplitude profiled analytically:
`Â(μ) = tᵀC⁻¹d / tᵀC⁻¹t`, `t(μ) = −(K₂ − μK₃)`, which makes χ² a rational
function of μ — the reason ~10⁷ evaluations are tractable.

## 3. Gate results

| Gate | raw | weighted |
|---|---|---|
| G1 analytic profiling vs direct 2-param optimisation | 7.1×10⁻¹⁵ PASS | 1.4×10⁻¹⁴ PASS |
| G2 constrained MLE vs unconstrained-then-clipped | +3.20 = 3.20 identical | −3.50 → 0.00 = 0.00 identical |
| G3 q̃ in three regimes (μ>μ̂, μ=μ̂, μ<μ̂) | 0.80 / 0.00 / 0.00 PASS | 0.92 / 0.00 / 0.00 PASS |
| G4/G5 nuisance A_cond / +1σ / −1σ | 11.00 / 11.00 / 11.00 | 8.00 / 8.50 / 7.50 |
| G6 coverage, **independent** ensemble | 0.9605 ± 0.0031 **CHECK** | 0.9480 ± 0.0035 PASS |

## 4. Results

| Claim ID | Endpoint | Status |
|---|---|---|
| `ACT-KSZ-ELL-D-WEIGHTED-STAT-v1` | L₉₅ = 8.00 Mpc | CROSS-IMPLEMENTATION-REPLICATED |
| `ACT-KSZ-ELL-D-RAW-STAT-v1` | L₉₅ = 11.00 Mpc | REPLICATED-WITH-COVERAGE-CAVEAT |

Kernel values, for the record: raw K₂(100)=1.214870, K₃(100)=0.015754;
weighted K₂(100)=1.207118, K₃(100)=0.015653. Blind A obtained 1.210167 /
0.015593 (raw) — 0.4% and 1.0% apart, yet the endpoints agree exactly, because
the limit depends on shape and statistics rather than kernel normalisation.

## 5. On the word "independent"

The re-check did **not** import or read Blind A's code, and reimplemented the
statistic from scratch. But it **knew Blind A's numbers** — they were written
into its PASS criterion before it ran. Correct label:

> **Cross-implementation numerical replication** (independent-code
> reimplementation *after* result disclosure).

This is stronger than a re-run, weaker than blind reproduction. The status
`INDEPENDENTLY REPRODUCED` is reserved for **Blind B**: a frozen specification
handed to an implementer with no knowledge of the expected values.

## 6. Open gates — none of these are closed by this record

1. **Estimator convention.** Whether the observable carries `1/(1+ξ)` must be
   *derived* from `p̂_kSZ → v₁₂ → ξ̄/(1+ξ)`, and audited for double counting
   (the denominator may already be inside the published data vector). "Weighted
   is more conservative" is **not** an argument — and in fact weighted gives the
   *tighter* bound here, which is beside the point either way. Two separate
   claim IDs are retained until this is settled.
2. **r_lo = 6 Mpc** is a MODEL-SUPPORT UNCERTAINTY, not a numerical systematic,
   until it is established what it represents (edge of published table? physical
   exclusion? limit of linear theory?). Must not be conflated with the exclusion
   ε around the singularity at r′ = R — different objects.
3. **PV as *physical* completion is NOT ESTABLISHED.** It is mathematically
   canonical for this singular integral; the physics may instead require halo
   exclusion, finite-size convolution, softening, or a form factor. Also unfixed:
   whether the symmetric removal is in \|r′−R\|, in \|s\|, or in dimensionless ρ —
   the Jacobian makes these differ at finite ε.
4. **Raw over-coverage 0.9605 ± 0.0031** (3.4σ above nominal). Conservative —
   the interval is too wide, not too narrow — but "it is the 0.5 Mpc grid" is a
   hypothesis, not a demonstration. Regression test: μ step 0.1–0.25, more MC
   near crossing, interpolate q₀.₉₅(μ) − q_obs(μ), repeat validation.
   Until then 11.00 is a **grid-quantised conservative endpoint**.
5. **Units dual-run** not performed: whole pipeline in h⁻¹Mpc and in Mpc, limits
   must differ by exactly h with no double conversion.
6. **Blind B** not run.

## 7. Do not merge raw and weighted

8 and 11 Mpc must **not** be averaged or folded into one systematic. They are
two different forward-model definitions, not two measurements of one quantity.

## 8. Admitted headline

> Two independently written implementations reproduce the absence of a
> significant 1/r³ signal and stat-only one-sided endpoints of order 8–11 Mpc,
> depending on the estimator definition. These are not yet a single physical
> constraint: weighting convention, r_lo, units and the physical status of the
> principal value must be frozen before Blind B.

---

## 9. Gate results — appended 2026-08-02, after the four regressions

### Gate 1 — fine-grid coverage: over-coverage WAS a grid artefact

| | before (0.5 Mpc grid) | after (0.1 Mpc + interpolation) |
|---|---|---|
| raw endpoint | 11.00 | **11.185** |
| raw coverage | 0.9605 ± 0.0031 (+3.4σ) | **0.9481 ± 0.0020 (−0.95σ)** |

12000 sims per μ. The endpoint was found by interpolating the zero crossing of
q95(μ) − q_obs(μ) rather than taking the last accepted node. Shift +0.185 Mpc,
below half the old step. **The "grid-quantised conservative endpoint" label is
withdrawn.** Mechanism: q_obs rises smoothly (1.15 → 5.79) while q95 fluctuates
in a narrow band 2.54–2.77 (MC noise ~±0.1); with a 0.5 Mpc step the crossing
fell between nodes, systematically lowering the endpoint and raising coverage.

### Gate 2 — estimator convention: DERIVED, not chosen

The pair-weighting factor belongs to the model, and applying it does not
double-count. Chain:

1. `v12(r) = -(2/3) H a f r · ξ̄(r)/(1+ξ(r))` — the denominator normalises a
   CONDITIONAL mean (velocity given a pair exists at r; pair count ∝ 1+ξ(r)).
   [DERIVED, standard linear theory]
2. `export_sdss_pairwise_curve.py:65` builds `g = [1/(1+ξ)]·I/r²` as the
   TEMPLATE. [CODE-VERIFIED]
3. `fit1.py:72`: `delta = p_pw - p_sdss * amplitude`, i.e. `ksz_curve` is the
   DATA and `g` is the MODEL. [CODE-VERIFIED]

Therefore the factor lives in the template; the data vector is a measurement
and cannot "already contain" it. **Double counting excluded.**

A data-side test ("is data/g flat in r?") was attempted first and is INVALID:
with no detected signal, data/g is noise about zero (−0.037 … +0.023, sign
change at r=225), scatter 0.767 vs 0.790 — a 3% difference on a 77% scatter.
It cannot discriminate. Recorded so it is not repeated.

`fit2.py` omits the factor and is therefore an incomplete model of v12. The
weighted convention becomes PRIMARY; raw is retained as lineage.

### Gate 3 — r_lo: MODEL-SUPPORT UNCERTAINTY, and it dominates

r_lo = 6 Mpc falls **inside a gap in the ξ data**: first bin 3.69 Mpc, second
11.08 Mpc. Everything between rests on interpolation, not measurement.

| interp | r_lo | UL95 |
|---|---|---|
| spline | 3.7 | 9.00 |
| spline | 6.0 | 8.50 |
| spline | 11.1 | 5.25 |
| linear | 6.0 | 9.00 |

**Spread 5.25–9.50 Mpc, factor 1.8** — larger than the UV prescription (×1.56),
the convention, or ξ (±7%). Mass below 6 Mpc is only 1.6% of I(100), so the
sensitivity comes from the K3/K2 weighting, not from the amount of mass.
The interpolation scheme alone moves the limit 0.5 Mpc at fixed r_lo.

**μ̂ = 0.00 for every r_lo and both interpolations.** The qualitative null
result is completely insensitive; only the upper limit moves.

### Gate 4 — dual-units: PASS at 0.048%

| path | endpoint at Δχ²=2.7 |
|---|---|
| A, physical Mpc | 8.660 Mpc |
| B, h⁻¹Mpc | 5.860 h⁻¹Mpc → 8.656 Mpc |

Difference 0.048%. `(K3/K2)_A / (K3/K2)_B = 0.677000` in every bin (min = max),
exactly h — correct, since K3/K2 has dimension 1/length. Two "failures" in the
first run were errors in the TEST, not the pipeline: an inverted expectation
(1/h instead of h) and an absolute tolerance of 1e-6 applied to an
interpolation residual of 2.9e-5 on χ² ≈ 20 (relative 1.5e-6).

Frozen unit record:

```
reported ell_d unit      : physical Mpc
input xi coordinate      : h^-1 Mpc as shipped
pair-separation unit     : Mpc (dr6.hdf r_mp)
adopted h                : 0.677
conversion location      : exactly once, at xi load
PV epsilon               : Mpc, scaled with the working unit
```

### Consolidated uncertainty budget

| source | effect on the limit |
|---|---|
| **r_lo (model-support, data gap)** | **×1.8 — dominant** |
| UV prescription (hard vs Plummer) | ×1.56 |
| ξ interpolation scheme at fixed r_lo | 0.5 Mpc |
| ξ measurement (correlated draws) | ±7% |
| coverage threshold | now calibrated, negligible |
| units | 0.048% |
| tail closure | 0.007% |

### Status after four gates

- No dipole detection: **ROBUSTLY SUPPORTED**, μ̂ = 0 under every variation
- Weighted estimator: **VERIFIED** (derivation + code)
- Fiducial limit at r_lo = 6 Mpc, spline: **8.50 Mpc** — must always be quoted
  with the r_lo and interpolation attached
- A single r_lo-independent number: **STILL NOT ADMITTED**
- Blind B: **RUNNING**
