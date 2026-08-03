# DRAFT SPECIFICATION v5 — kSZ dipole conditional upper limit

**STATUS: DRAFT. NOT FROZEN.**

This document contains **prescriptions only**: what to compute, in what order,
with what constants and tolerances, and what to do when a check fails. It
contains no derivations, no justifications, and no commentary on earlier
versions. Reasoning lives in `derivations.md`, which is **not** part of the
freeze gate — an error there is corrected there and does not reopen this
document.

**Freeze gate, stated operationally:** two independent readers, each with this
document and nothing else, produce implementations that agree. A finding blocks
the freeze if and only if a reader can name two readings of this text that
would produce **different reported numbers or different reported outcome
labels**. Findings that do not meet that bar are logged and do not block.

Path: `DRAFT_v5 → STATIC_SPEC_REVIEW → FROZEN_v5 → Blind C`.
No blind run may be launched from this document.

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0: descriptive

---

## 0. Product

A conditional, stat-only, fixed-template 95% upper limit on
`ℓ_d = A₃/A₂ = μ`, in physical Mpc, within one continuum pairwise-kSZ forward
model.

Out of scope, and not to be inferred from any output of this procedure: any
limit on `β_d`; any test of any preprint figure; any claim that the principal
value is the physically correct ultraviolet completion; any propagation of
template uncertainty; any data-based determination of `r_lo`; any `CL_s`
protection.

Every reported limit carries the label **stat-only, fixed-template**.
Every `r_lo`-dependent output carries the label **MODEL-SUPPORT CONDITIONAL**.

## 1. Symbols

Complete. Nothing outside this table appears in any equation below.

| Symbol | Meaning |
|---|---|
| `R` | separation at which a kernel is evaluated; equals `r_mp` of a bin |
| `s` | integration variable, physical Mpc |
| `ρ` | `s/R` |
| `r_lo`, `r_hi` | limits of the kernel integral, Mpc |
| `ξ(r)` | correlation function, per §4 |
| `G₂(ρ)`, `G₃(ρ)` | geometric weights |
| `P(ρ)`, `Λ(ρ)` | the two additive parts of `G₃` |
| `ε` | excision half-width, Mpc |
| `Kraw2, Kraw3` | unweighted kernels |
| `Kw2, Kw3` | weighted kernels |
| `T(μ, r_lo)` | template vector over fitted bins |
| `D` | observed data vector, fitted bins |
| `Db` | one simulated data vector |
| `V` | data covariance, fitted bins |
| `Vgen` | covariance used to generate simulated data |
| `Wt` | weight matrix in the likelihood |
| `Amp(μ)` | profiled amplitude on `D` |
| `AmpSd(μ)` | sampling standard deviation of the profiled amplitude |
| `A₂`, `A₃` | `A₂ = Amp`, `A₃ = Amp·μ` |
| `μ` | parameter of interest, equals `ℓ_d`, Mpc |
| `muhat` | constrained minimiser, §7 |
| `muzero` | the μ at which the profiled amplitude vanishes, §7 |
| `mumax` | 60 Mpc |
| `Chi2(μ)` | profiled objective |
| `Q(μ)` | one-sided statistic |
| `Qobs(μ)` | `Q(μ)` evaluated on `D` |
| `Q95(μ)` | 0.95 quantile of simulated `Q(μ)` |
| `L95` | reported upper endpoint |
| `SdMC` | Monte-Carlo standard deviation of `L95` |
| `alpha`, `Nboot`, `Nbin` | Hartlap factor; 1000; 15 |
| `hdata` | 0.6731 |
| `gcurve(R)` | shipped pair-weight curve, control 3 only |
| `rXiMin` | smallest tabulated ξ separation after conversion, §4 |
| `IntGK` | the quadrature operator defined in §5 |
| `Tu`, `Tv` | the μ-independent parts of `T(μ) = Tu + μ·Tv`, §7 |
| `ca, cb, cc, ce, cf, cd` | the six scalar contractions defined in §7 |
| `mu1` | the second stationary point of `Chi2`, §7 |
| `Cand` | the candidate set for `muhat`, §7 |
| `Lchol` | lower Cholesky factor of `Vgen`, §8 |
| `z` | standard normal 15-vector, §8 |
| `AmpGen` | amplitude used to generate simulated data, §8 |
| `rootCal`, `rootVal`, `rootDual` | the three seed sequences, §8 |
| `key` | the stream key, §8 |
| `model_id`, `r_lo_id`, `j20`, `stage` | the four fields of `key`, §8 |
| `k`, `r_lo_k` | index and value of an `r_lo` grid node, §9 |
| `acc`, `j`, `jlast` | acceptance vector, its index, the last accepted index, §10 |
| `μa`, `μb` | the two bracketing refined nodes, §10 |
| `ga`, `gb` | `Qobs − Q95` at `μa` and `μb`, §10 |
| `wa`, `wb` | crossing fractions, §10 |
| `slope` | `(gb − ga)/(μb − μa)`, §10 |
| `sq(μ)`, `dens(μ)`, `n(μ)` | quantile error, density estimate, simulation count at a node, §10 |
| `mu_true` | injected value in the coverage study, §13 |
| `r_mp`, `ksz_curve`, `df_cov`, `bs_curves`, `r_mp_over_h` | fields of `dr6.hdf`, §2 |

`hdata` is the only value of `h` used anywhere in this procedure. No symbol in
this table carries a second meaning anywhere in this document. Where a symbol
is written with an argument (`Amp(μ)`, `sq(μ)`) or an index (`R_i`, `r_lo_k`),
it is the same symbol as its bare entry above.

Outcome labels are written in `UPPER_SNAKE_CASE` and are not symbols; the
complete list is §15.11.

## 2. Inputs

| File | Status | Use |
|---|---|---|
| `dr6.hdf` → `df_pw` (`r_mp`, `ksz_curve`) | PRIMARY | data vector |
| `dr6.hdf` → `df_cov` (18×18) | PRIMARY | data covariance |
| `dr6.hdf` → `bs_curves` (1000×18) | PRIMARY | fixes `Nboot`; generates branch-2 data; control 4 |
| `dr6.hdf` → `r_mp_over_h` | CONTROL | control 1 |
| `xi_zbin2.dat` | PRIMARY | `ξ` |
| `sdss_g_sqrtg.csv` | CONTROL | `gcurve`, control 3 |
| `covariances_sdss_g.txt` | UNUSED | not opened |

All arrays are cast to float64 on load, before any comparison.

## 3. Units

`r_mp` is in physical Mpc and is never converted.

`xi_zbin2.dat` column 1 is in h⁻¹Mpc. Multiply it by `1/hdata` once, at load, to
obtain physical Mpc. Column 2 is `ξ` and is dimensionless.

`r_lo`, `r_hi`, `ε`, `μ` and `L95` are all in physical Mpc.

## 4. ξ interpolation

```
abscissa   : s, physical Mpc
ordinate   : ξ
method     : cubic spline, not-a-knot boundary condition
             (scipy.interpolate.CubicSpline, bc_type='not-a-knot')
outside the tabulated range : ξ = 0
```

`r_hi` is set to the largest tabulated separation after conversion. It is read
from the file; no literal value is written into this document.

`rXiMin` is the smallest tabulated separation after conversion, likewise read
from the file.

**Guard G1.** Evaluate the interpolant on a uniform grid of 10 000 points over
`[rXiMin, r_hi]`. If `1 + ξ` is anywhere `≤ 0.01`, or if `ξ` anywhere falls
below `min(tabulated ξ) − 0.05·(max − min of tabulated ξ)`, STOP with
`SPLINE_OVERSHOOT` and report the offending `s`.

## 5. Kernels

```
G₂(ρ) = 1 for ρ < 1,  0 for ρ > 1,  1/2 at ρ = 1
P(ρ)  = 1 / (2(1 − ρ²))
Λ(ρ)  = ln|(1+ρ)/(1−ρ)| / (4ρ)
G₃(ρ) = P(ρ) + Λ(ρ)
ε     = 0.05 Mpc
```

```
Kraw2(R, r_lo) = (1/R²) · IntGK( ξ(s)·s² ,  r_lo → min(R, r_hi) )

Kraw3(R, r_lo) = (1/R³) · [ IntGK( ξ(s)·s²·P(s/R) ,  r_lo   → R−ε )
                          + IntGK( ξ(s)·s²·P(s/R) ,  R+ε    → r_hi )
                          + IntGK( ξ(s)·s²·Λ(s/R) ,  r_lo   → r_hi ) ]

Kw2(R, r_lo)   = Kraw2(R, r_lo) / (1 + ξ(R))
Kw3(R, r_lo)   = Kraw3(R, r_lo) / (1 + ξ(R))
```

`IntGK` is adaptive Gauss–Kronrod with absolute and relative tolerance 1e-10,
taking as breakpoints: the interval endpoints, `s = R` when it lies strictly
inside the interval, and every spline knot inside the interval. If the tolerance
is not achieved on any subinterval, STOP with `QUADRATURE_NOT_CONVERGED`.

**Guard G2.** Before evaluating `Kraw3`, require `r_lo < R − ε` and
`R + ε < r_hi` for every fitted `R` and every `r_lo` in use. Otherwise STOP with
`EXCISION_WINDOW_OUT_OF_RANGE`.

No kernel with `k = 4` is computed.

## 6. Models

```
MODEL-W :  T(μ, r_lo)[i] = −[ Kw2(R_i, r_lo)   − μ · Kw3(R_i, r_lo)   ]
MODEL-R :  T(μ, r_lo)[i] = −[ Kraw2(R_i, r_lo) − μ · Kraw3(R_i, r_lo) ]
```

The two are never combined, averaged or merged. The model prediction is
`Amp · T(μ)`.

| Deliverable | MODEL-W | MODEL-R |
|---|---|---|
| `muhat`, `muzero`, unconstrained minimiser | yes | yes |
| `L95` at `r_lo = 6.0` | yes | yes |
| `L95` over the `r_lo` grid | yes | no |
| coverage study | yes | no |
| §11 branches | yes | no |

Each model that requires an `L95` requires its own full Monte-Carlo
calibration.

## 7. Fit

```
bins  : every bin with 25 ≤ r_mp ≤ 225, endpoints inclusive.
        Require exactly 15. Otherwise STOP with BIN_COUNT_MISMATCH,
        reporting the count and the selected r_mp values.
D     : ksz_curve on those bins
V     : df_cov restricted to those bins (slice, then invert)
alpha : (Nboot − Nbin − 2)/(Nboot − 1),  Nboot = 1000, Nbin = 15
Wt    : alpha · V⁻¹
```

**Guard G3.** Before inverting, require `V` symmetric to 1e-12 relative and
positive definite (Cholesky succeeds), with condition number below 1e12.
Otherwise STOP with `COVARIANCE_ILL_CONDITIONED`.

Write `T(μ) = Tu + μ·Tv`, where `Tu` and `Tv` are the μ-independent vectors read
off §6 for the model in use. Define

```
ca = Tuᵀ Wt D      cb = Tvᵀ Wt D
cc = Tuᵀ Wt Tu     ce = Tuᵀ Wt Tv     cf = Tvᵀ Wt Tv
cd = Dᵀ Wt D
```

```
Amp(μ)    = (ca + μ·cb) / (cc + 2μ·ce + μ²·cf)
AmpSd(μ)  = sqrt( alpha / (cc + 2μ·ce + μ²·cf) )
Chi2(μ)   = cd − (ca + μ·cb)² / (cc + 2μ·ce + μ²·cf)
```

`Amp` is unconstrained in sign.

**Stationary points.** `Chi2` is stationary exactly where

```
(ca + μ·cb) · [ (cb·cc − ca·ce) + μ·(cb·ce − ca·cf) ] = 0
```

which gives

```
muzero = −ca/cb                                   (first factor)
mu1    = (ca·ce − cb·cc) / (cb·ce − ca·cf)        (second factor)
```

**Guard G4.** If `|cb| < 1e-300`, or `|cb·ce − ca·cf| < 1e-300`, or
`cf < 1e-300`, STOP with `DEGENERATE_QUADRATIC` and report `ca, cb, cc, ce, cf`.

**Constrained minimiser.** Form the candidate set

```
Cand = { 0, mumax } ∪ { mu1  if 0 ≤ mu1 ≤ mumax }
```

`muzero` is **never** a candidate. Evaluate `Chi2` on `Cand` and set `muhat` to
the argument giving the smallest value; on an exact tie take the smallest μ.

Report separately: `mu1` itself (the unconstrained stationary point of the
second factor), `muzero`, and whether `mu1` fell inside `[0, mumax]`.

**Statistic.**

```
Q(μ) = 0                       if muhat > μ
     = Chi2(μ) − Chi2(muhat)   if muhat ≤ μ
```

All simulated datasets are retained in every sample regardless of where their
`muhat` falls. **Boundary count** is defined as the number of datasets with
`muhat = 0` exactly, plus the number with `muhat = mumax` exactly, reported as
two separate integers.

## 8. Monte Carlo

```
scan grid    : μ = 0.1·j,  j = 1 … 600            (600 nodes; μ = 0 excluded)
refine step  : 0.05
sims coarse  : 100 000 per node
sims refined : 200 000 per node
```

`Q95(μ)` is the empirical 0.95 quantile of the simulated `Q(μ)` sample,
computed with linear interpolation between order statistics
(`numpy.quantile`, `method='linear'`), over the whole sample including zeros.

**Random streams.**

```
rootCal = SeedSequence(20260802)
rootVal = SeedSequence(20260803)
rootDual = SeedSequence(20260804)

key   = (model_id, r_lo_id, j20, stage)
        model_id : 0 for MODEL-W, 1 for MODEL-R
        r_lo_id  : the index k of §9 for a grid node; 100 for r_lo = 6.0
        j20      : round(μ / 0.05), an integer
        stage    : 0 coarse, 1 refined
gen   = default_rng(SeedSequence(entropy=<root>.entropy, spawn_key=key))
```

The key does **not** contain a branch identifier: every branch of §11 draws the
same standard normals as the primary at the same key. Coarse and refined stages
draw different streams.

Simulated data are formed as

```
Db = AmpGen · T(μ, r_lo)  +  Lchol · z ,      z ~ standard normal, 15-vector
```

where `Lchol` is the lower Cholesky factor of `Vgen`, except for branch 2 (§11).
`AmpGen` is fixed per `(model, r_lo, μ)` and does not vary across simulations.
Within the analysis of each simulated dataset the amplitude is re-profiled by
§7.

Primary: `Vgen = V`, `AmpGen = Amp(μ)` computed on `D`.

## 9. r_lo

```
r_lo_k = 3.8 + 0.8·k   Mpc,   k = 0 … 9
```

Ten nodes; the largest is 11.0. `r_lo = 6.0` is not one of them; it is an
eleventh, separate evaluation with its own full calibration and `r_lo_id = 100`.

`L95` is computed at all eleven. The reported **range** is
`[min, max]` of the ten grid values. Nothing is fitted or smoothed. The range is
never converted into a symmetric error bar and its midpoint is never reported as
a central value.

**Monotonicity report.** State whether the ten grid values are non-decreasing in
`r_lo` after allowing each value its own `SdMC`: the sequence counts as
non-decreasing if `L95(k+1) ≥ L95(k) − 2·sqrt(SdMC(k)² + SdMC(k+1)²)` for every
`k`. Report the verdict and the largest violation. Nodes returning a
non-numeric outcome label (§10) are excluded from both the range and this test,
and are listed.

## 10. Upper endpoint

Let `acc(j) = [ Qobs(0.1·j) ≤ Q95(0.1·j) ]` for `j = 1 … 600` on the coarse
grid. Exactly one of the following applies.

| Case | Condition | Action |
|---|---|---|
| **A** | `acc(j)` true for all `j` | report `NO_ENDPOINT_IN_RANGE`; report `max_j Qobs`, the μ at which it occurs, and `muzero` |
| **B** | `acc(j)` false for all `j` | bisect on `[0, 0.1]` to a tolerance of 1e-3 Mpc for the largest accepted μ; report `L95` with the label `BELOW_FIRST_NODE` |
| **C** | otherwise | let `jlast` be the largest `j` with `acc(j)` true and `acc(j+1)` false; proceed below |

In case C, re-simulate at 200 000 sims on the refined grid
`μ = 0.05·i` covering `[0.1·jlast − 2, 0.1·jlast + 2]`, clipped to
`[0.05, mumax]`. On that refined grid let `μa < μb` be the last adjacent pair
with `acc` true then false, and set

```
ga  = Qobs(μa) − Q95(μa)      (≤ 0)
gb  = Qobs(μb) − Q95(μb)      (> 0)
L95 = μa + (μb − μa)·(−ga)/(gb − ga)
```

If the refined grid contains no true→false pair, report
`REFINEMENT_LOST_CROSSING` together with the coarse `jlast`.

The full 600-entry `acc` vector is reported in every case, so that the case
selection is auditable.

No statement is made, and none may be inferred, about `μ > mumax`.

**Amplitude flag.** Report `AMPLITUDE_SIGN_CHANGE_IN_RANGE` when
`0 < muzero ≤ mumax`, together with `muzero`, `Amp(muhat)` and `AmpSd(muhat)`.
This is a reported flag, not a gate.

```
SdMC = sqrt( wb²·sq(μa)² + wa²·sq(μb)² ) / |slope|
  wa    = −ga / (gb − ga)
  wb    = 1 − wa
  slope = (gb − ga) / (μb − μa)
  sq(μ) = sqrt(0.95·0.05 / n(μ)) / dens(μ)
          n(μ)    : simulations at that node
          dens(μ) : Gaussian-KDE density of the strictly positive simulated
                    Q(μ) values, Silverman bandwidth, evaluated at Q95(μ),
                    multiplied by the fraction of the sample that is positive
```

If `Q95(μ) = 0` at either bracketing node, report `SdMC = NOT_DEFINED` and the
positive fraction at that node.

## 11. Branches

Run at `r_lo = 6.0`, MODEL-W, 100 000 sims per node, sharing the primary's
streams.

| Branch | Change from the primary |
|---|---|
| 1 | `Vgen = V / alpha` |
| 2 | `Db = AmpGen·T(μ) + (row − mean of the 1000 rows)[fitted bins]`, the row drawn with replacement using the same stream |
| 3 | `AmpGen = Amp(μ) + AmpSd(μ)` |
| 4 | `AmpGen = Amp(μ) − AmpSd(μ)` |

One at a time from the primary; not a cross. Report `L95` and `SdMC` for each
against the primary. Branch 2 carries the marker `[WEAK]` in the output.

## 12. Controls

| # | Check | Criterion | On failure |
|---|---|---|---|
| 1 | `r_mp_over_h[i] / r_mp[i]` equals `hdata` for all 18 bins | max relative deviation < 1e-9 | STOP `UNIT_INVARIANT_FAILED` |
| 2 | `Kraw2(R, 6.0)` from §5 against `IntGK( ξ(s)·s²·G₂(s/R), r_lo → r_hi )` with `s = R` as a breakpoint, at all 15 fitted `R` | max relative deviation < 1e-6 | STOP `K2_ROUTE_MISMATCH` |
| 3 | `Kw2(R, 6.0)` and `gcurve(R)`, each divided by its own value at the smallest fitted bin, compared at the 15 fitted `r_mp`; report the rms of their ratio about its mean | report only | none |
| 4 | sample covariance of the 1000 `bs_curves` rows, `1/(Nboot−1)` normalisation, all 18 bins, against `df_cov`; report max relative deviation | report only | none |
| 5 | `Kraw3` and `Kw3` at all 15 fitted `R`, `r_lo = 6.0`, recomputed at quadrature tolerance 1e-12 | max relative deviation < 1e-6 | STOP `QUADRATURE_NOT_STABLE` |
| 6 | the same kernels recomputed at `ε = 0.025` and `ε = 0.10`, each compared against the `ε = 0.05` values | max relative deviation < 1e-3 | STOP `PV_EPSILON_SENSITIVE` |
| 7 | `Amp(μ)` from §7 against direct 1-D numerical minimisation of `(D − a·T)ᵀ Wt (D − a·T)` over `a`, at `μ = 0` and `μ = 10`, both models | max relative deviation < 1e-9 | STOP `PROFILING_MISMATCH` |
| 8 | `r_hi` and `rXiMin` (§4) against the first and last converted separations in `xi_zbin2.dat` | exact equality of the float64 values | STOP `XI_RANGE_MISMATCH` |

Every control reports its measured value regardless of outcome. A control with
no reported value marks the run failed.

**Not established by any control above:** the absolute unit of `r_mp`. Control 1
compares two shipped arrays against each other and nothing else. No output may
assert the absolute unit of `r_mp`.

## 13. Coverage study

```
root        : rootVal
model       : MODEL-W,  r_lo = 6.0,  Vgen = V
mu_true     : 2, 4, 6, 8, 10, 12, 14, 16 Mpc
sims        : 200 000 per mu_true
AmpGen      : Amp(mu_true) computed on D
statistic   : the fraction of simulated datasets with
              Q(mu_true) ≤ Q95(mu_true)
Q95 source  : the coarse-grid value at that μ, 100 000 sims,
              never the refined-grid value
band        : |fraction − 0.95| < 3·sqrt( 0.95·0.05/200000
                                        + 0.95·0.05/100000 )
```

Report the fraction, the band, and PASS/FAIL per `mu_true`, plus the number of
`mu_true` values failing. No aggregate verdict is formed from the eight.

## 14. Dual-unit run

Repeat §5–§10 for MODEL-W at `r_lo = 6.0`, primary branch only, with every
length expressed in h⁻¹Mpc: the `ξ` abscissa, `r_mp`, the bin-selection window
`25` and `225`, `r_lo`, `r_hi`, `rXiMin`, `ε`, `mumax`, the coarse step `0.1`,
the refine step `0.05`, the `±2` refinement half-width, the case-B bisection
tolerance `1e-3`, and control 8's comparison. Quadrature tolerances are
relative and are not converted; the absolute tolerance is scaled by `hdata`.

Use `rootDual`; stream identity across the two unit systems is not required.

Convert the resulting `L95` back to physical Mpc and report the relative
difference against §10's value. PASS if below 0.1%. If either run returns a
non-numeric outcome label, report both labels and no percentage.

## 15. Outputs

Unless a section states otherwise, every item is at `r_lo = 6.0`.

1. `Kw2`, `Kw3`, `Kraw2`, `Kraw3` at the fitted bin whose `r_mp` is nearest to
   100 Mpc, ties broken toward the smaller `r_mp`; state that bin's `r_mp`.
2. `muhat`, `mu1`, `muzero`, and whether `mu1 ∈ [0, mumax]`, both models.
3. `L95` at all eleven `r_lo` values of §9, MODEL-W, with `SdMC` for each; the
   `[min, max]` range over the ten grid nodes; the monotonicity verdict and its
   largest violation.
4. `L95` and `SdMC` at `r_lo = 6.0`, both models.
5. The §13 coverage table.
6. `Chi2(0) − Chi2(muhat)`, and its p-value under the mixture
   `0.5·δ₀ + 0.5·χ²₁`. If the difference is 0, report p = 0.5. This item
   carries the marker `[WEAK]`.
7. The §14 dual-unit comparison.
8. Controls 1–8, each with its measured value and verdict.
9. Boundary counts (§7), observed and simulated, as two integers per
   `(r_lo, μ)` aggregated over μ.
10. The §11 branch table.
11. Every outcome label raised: `NO_ENDPOINT_IN_RANGE`, `BELOW_FIRST_NODE`,
    `REFINEMENT_LOST_CROSSING`, `AMPLITUDE_SIGN_CHANGE_IN_RANGE`,
    `SdMC = NOT_DEFINED`, and any STOP.
12. The 600-entry `acc` vector for every `L95` computed.
13. Any place where this document admits more than one implementation, is
    silent on a decision the implementer had to make, or is internally
    inconsistent. **This item outranks every number above.**

## 16. Standing scope statements

These are properties of the procedure, carried into every report of its output.
They are not defects and are not to be re-reported as discoveries.

- All eleven `r_lo` values lie strictly between the first and second tabulated
  separations of `ξ`. The `r_lo` dependence is a dependence on the §4
  interpolant over an interval containing no measurement.
- The `1/(1+ξ)` weighting is a modelling choice; MODEL-R is the alternative.
- The principal value is one prescription among several possible ultraviolet
  completions.
- `covariances_sdss_g.txt` is excluded; the kernels are treated as exact.
- No kSZ–ξ cross-covariance is available; independence is assumed.
- The Monte-Carlo calibration fixes the generating amplitude at its value
  profiled from the observed data.
- The endpoint is interpolated between two independently simulated `Q95`
  nodes.

---

## Appendix — static review questions

Two independent readers answer these from this document alone, pseudocode only,
no numbers. A finding blocks the freeze only under the operational gate stated
in the header.

1. Which kernels enter which model, and how is `Kraw2` integrated?
2. Where is `1/(1+ξ)` applied?
3. Which lengths are converted, and which are not?
4. How is `P` integrated, how is `Λ` integrated?
5. How is a simulated dataset formed, with what covariance and what amplitude?
6. What is `Wt`?
7. What is `muhat`, and which candidates enter the comparison?
8. What is `Q(μ)`, and what is the boundary count?
9. Which of cases A, B, C applies to a given `acc` vector, and what does each
   report?
10. What is `SdMC`, and when is it `NOT_DEFINED`?
11. What are the eight controls, and which of them stop the run?
12. What is reported, and what is out of scope?
