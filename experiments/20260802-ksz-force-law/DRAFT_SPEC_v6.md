# DRAFT SPECIFICATION v6 — kSZ dipole conditional upper limit

**STATUS: DRAFT. NOT FROZEN.**

Prescriptions only. Reasoning lives in `derivations.md`, which is not part of
the freeze gate. Every change from v5 is a registered entry in
`ambiguity_ledger_v6.md`; no derivation, explanation or method change is added.

**Freeze gate.** A finding blocks the freeze if and only if two implementations,
both compatible with this text, could differ in the simulated data, a kernel,
the likelihood, a terminal state, or a reported output. A reader must supply
`Reading A` / `Reading B` / `Affected output`. If the second reading contradicts
another explicit line of this document, it is not a blocking finding.

Path: `DRAFT_v6 → LOCAL_STATIC_LINT → TEST_VECTOR_PASS → DUAL_READER_REVIEW →
COMPUTATIONALLY_FROZEN_v6 → BLIND_C`.

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0: descriptive

---

## 0. Product

A conditional, stat-only, fixed-template 95% upper limit on
`ℓ_d = A₃/A₂ = μ`, in physical Mpc, within one continuum pairwise-kSZ forward
model.

Out of scope, and not inferable from any output: any limit on `β_d`; any test
of any preprint figure; any claim about the physical correctness of the
principal value; template-uncertainty propagation; any data-based determination
of `r_lo`; `CL_s` protection; any statement about `μ > mumax`; the absolute unit
of `r_mp`.

Every reported limit carries the label **stat-only, fixed-template**. Every
output computed at a value of `r_lo` carries the label **MODEL-SUPPORT
CONDITIONAL**; that is every numeric item of §15 except items 8 and 11.

## 1. Symbols

Nothing outside this table appears in any equation. No entry carries a second
meaning. A symbol written with an argument (`Amp(μ)`) or an index (`R_i`) is the
same symbol as its bare entry.

| Symbol | Meaning |
|---|---|
| `R`, `R_i` | separation at which a kernel is evaluated; `r_mp` of fitted bin `i` |
| `s` | integration variable, physical Mpc |
| `rho` | `s/R` |
| `r_lo`, `r_hi`, `rXiMin` | kernel integral limits; largest and smallest tabulated ξ separation |
| `xi` | correlation function, §4 |
| `G2`, `G3`, `Pp`, `Lam` | geometric weights; the pole and log parts of `G3` |
| `eps` | excision half-width, Mpc |
| `Kraw2`, `Kraw3`, `Kw2`, `Kw3` | the four kernels |
| `IntGK` | the adaptive quadrature operator defined in §5 |
| `sdev`, `iqr`, `npos` | inputs to `hkde`, §10 |
| `q` | the per-bin ratio formed in control 1 |
| `u`, `v` | the two normalised curves compared in control 3 |
| `y`, `a` | a data vector passed to the fit, §7; the scalar minimised in control 7 |
| `w` | the boundary index of `edgeCount`, 0 or 1, §7 |
| `p`, `q_` | consecutive retained node indices in the monotonicity test, §9 |
| `m` | guard-G1 grid index, §4 |
| `rowIndex` | branch-2 bootstrap row indices, shape `(nsim,)`, dtype int64, §8 |
| `maxViolation` | the monotonicity margin defined in §9 |
| `hasFall` | the case predicate defined in §10 |
| `Tu`, `Tv`, `Tvec` | template parts and `Tvec(μ) = Tu + μ·Tv` |
| `Dvec` | observed data vector, fitted bins |
| `Dsim` | one simulated data vector |
| `Vcov`, `Vgen`, `Wt`, `Lchol` | data covariance; generating covariance; weight matrix; lower Cholesky factor of `Vgen` |
| `zdraw` | standard normal array, shape `(nsim, 15)`, dtype float64, §8 |
| `Amp`, `AmpSd`, `AmpGen` | profiled amplitude; its sampling standard deviation; the generating amplitude |
| `A2`, `A3` | `A2 = Amp`, `A3 = Amp·μ` |
| `mu` | parameter of interest, equals `ℓ_d`, Mpc |
| `muhat`, `muzero`, `mu1`, `mumax` | constrained minimiser; zero of `Amp`; second stationary point; 60 |
| `Cand` | candidate set for `muhat`, §7 |
| `ca, cb, cc, ce, cf, cd` | the six contractions, §7 |
| `Chi2` | profiled objective |
| `Qstat`, `Qobs`, `Q95` | statistic; its value on `Dvec`; the 0.95 quantile of the simulated sample |
| `acc`, `jj`, `jlast` | acceptance vector; its index; **the largest `jj` with `acc(jj)` true and `acc(jj+1)` false**, §10 |
| `mua`, `mub`, `ga`, `gb`, `wa`, `wb`, `slope` | bracketing nodes and crossing quantities, §10 |
| `L95`, `SdMC`, `sq`, `dens`, `nsim` | endpoint; its Monte-Carlo error; quantile error; density estimate; simulations at a node |
| `hkde` | KDE bandwidth; `hkde = 0.9·min(sdev, iqr/1.34)·npos^(−1/5)`, §10 |
| `Drel`, `Dabs`, `tauAbs` | deviation measures and their floor, §12.0 |
| `alpha`, `Nboot`, `Nbin` | Hartlap factor; 1000; 15 |
| `smax`, `smin` | largest and smallest singular value of `Vcov`, §7 |
| `[WEAK]` | an evidence marker attached to a reported item; never an outcome label |
| `hdata` | 0.6731 |
| `gcurve` | shipped pair-weight curve, control 3 |
| `rootCal`, `rootVal`, `rootDual`, `rootUsed` | the three seed sequences and the one assigned to the current consumer, §8 |
| `keyModel`, `keyRlo`, `keyMu`, `keyStage`, `keyStep` | the five key fields, §8 |
| `kk`, `ii`, `bb`, `i` | `r_lo` node index; refined-grid index; simulation index; fitted-bin index |
| `key`, `rng` | the stream key tuple and the generator it seeds, §8 |
| `max_i` | maximum over the fitted-bin index `i` |
| `edgeCount`, `degenCount` | counters, §7 |
| `muTrue` | injected value, §13 |
| `r_mp`, `ksz_curve`, `df_cov`, `bs_curves`, `r_mp_over_h` | fields of `dr6.hdf`, §2 |

Kernel orders are written as literals (`Kraw2`, `Kraw3`) and never as a symbol.

Two disjoint label sets. **Outcome labels** are listed in §15.11 and are the
only labels a run may emit. **Document-status labels** are
`NOT_VALIDATION`, `NOT_REFUTATION`, `OUR_RECONSTRUCTION`,
`STATIC_SPEC_REVIEW`, `LOCAL_STATIC_LINT`, `TEST_VECTOR_PASS`,
`DUAL_READER_REVIEW`, `COMPUTATIONALLY_FROZEN_v6`, `BLIND_C`,
`MODEL-SUPPORT CONDITIONAL`; they annotate this document and are never emitted
by a run.

## 2. Inputs

| File | Status | Use |
|---|---|---|
| `dr6.hdf` → `df_pw` (`r_mp`, `ksz_curve`) | PRIMARY | data vector |
| `dr6.hdf` → `df_cov` | PRIMARY | data covariance |
| `dr6.hdf` → `bs_curves` | PRIMARY | fixes `Nboot`; branch-2 data; control 4 |
| `dr6.hdf` → `r_mp_over_h` | CONTROL | control 1 |
| `xi_zbin2.dat` | PRIMARY | `xi` |
| `sdss_g_sqrtg.csv` | CONTROL | `gcurve`, control 3 |
| `covariances_sdss_g.txt` | UNUSED | not opened |

Every array is cast to float64 on load, before any comparison. Required shapes,
checked on load: `r_mp` (18,), `ksz_curve` (18,), `df_cov` (18,18),
`bs_curves` (1000,18), `r_mp_over_h` (18,). A mismatch is `INVALID_INPUT`.

## 3. Units

`r_mp` is in physical Mpc and is not converted anywhere in §4–§13. §14 is a
separate run in which every length listed there, including `r_mp`, is
re-expressed; see §14 for what re-expression means.

`xi_zbin2.dat` column 1 is in h⁻¹Mpc and is multiplied by `1/hdata` once, at
load. Column 2 is `xi`, dimensionless.

`r_lo`, `r_hi`, `rXiMin`, `eps`, `mu`, `L95` are in physical Mpc.

## 4. xi interpolation

Sort the loaded pairs by converted separation, ascending, before anything else.

```
abscissa : s, physical Mpc
ordinate : xi
method   : scipy.interpolate.CubicSpline(s, xi, bc_type='not-a-knot')
outside the tabulated range : xi = 0
rXiMin = s[0]        r_hi = s[-1]        (after the sort)
```

**Guard G1.** Evaluate the interpolant at `s = rXiMin + (r_hi − rXiMin)·m/9999`
for `m = 0 … 9999`. If `1 + xi(s) ≤ 0.01` at any of them, or `xi(s)` is below
`min(tabulated xi) − 0.05·(max − min of tabulated xi)`, emit `STOP_RUN` with
`SPLINE_OVERSHOOT` and the smallest offending `s`.

## 5. Kernels

```
G2(rho)  = 1 for rho < 1,  0 for rho > 1,  1/2 at rho = 1
Pp(rho)  = 1 / (2(1 − rho^2))
Lam(rho) = ln|(1+rho)/(1−rho)| / (4·rho)
G3(rho)  = Pp(rho) + Lam(rho)
eps      = 0.05
```

```
Kraw2(R, r_lo) = (1/R^2) · IntGK( xi(s)·s^2 , r_lo → R )

Kraw3(R, r_lo) = (1/R^3) · [ IntGK( xi(s)·s^2·Pp(s/R) , r_lo → R−eps )
                           + IntGK( xi(s)·s^2·Pp(s/R) , R+eps → r_hi )
                           + IntGK( xi(s)·s^2·Lam(s/R), r_lo → r_hi ) ]

Kw2(R, r_lo)   = Kraw2(R, r_lo) / (1 + xi(R))
Kw3(R, r_lo)   = Kraw3(R, r_lo) / (1 + xi(R))
```

`IntGK(f, a → b)` is adaptive Gauss–Kronrod with absolute and relative tolerance
1e-10, breakpoints being `a`, `b`, `R` when `a < R < b`, and every spline knot
strictly inside `(a, b)`. Failure to reach tolerance is `STOP_RUN`
`QUADRATURE_NOT_CONVERGED`.

**Guard G2.** For every fitted `R` and every `r_lo` in use, require
`r_lo < R − eps` and `R + eps < r_hi`; otherwise `STOP_RUN`
`EXCISION_WINDOW_OUT_OF_RANGE`. Under G2, `R < r_hi` always, which is why
`Kraw2`'s upper limit is written as `R`.

`Kraw4` and `Kw4` are not computed and appear nowhere else in this document.

## 6. Models

```
MODEL-W :  Tu[i] = −Kw2(R_i, r_lo)   ,  Tv[i] = +Kw3(R_i, r_lo)
MODEL-R :  Tu[i] = −Kraw2(R_i, r_lo) ,  Tv[i] = +Kraw3(R_i, r_lo)
Tvec(mu) = Tu + mu·Tv
```

Prediction is `Amp · Tvec(mu)`; `A2 = Amp`, `A3 = Amp·mu`, `ℓ_d = A3/A2 = mu`.
The two models are never combined, averaged or merged. `keyModel` is 0 for
MODEL-W and 1 for MODEL-R.

| Deliverable | MODEL-W | MODEL-R |
|---|---|---|
| `muhat`, `mu1`, `muzero` | yes | yes |
| `L95` at `r_lo = 6.0` | yes | yes |
| `L95` over the `r_lo` grid | yes | no |
| coverage study | yes | no |
| §11 branches | yes | no |

Each model requiring an `L95` gets its own full calibration.

## 7. Fit

```
bins  : every bin with 25 ≤ r_mp ≤ 225, endpoints inclusive.
        Require exactly 15, else STOP_RUN BIN_COUNT_MISMATCH with the count
        and the selected r_mp values.
Dvec  : ksz_curve on those bins
Vcov  : df_cov restricted to those bins (slice, then invert)
alpha : (Nboot − Nbin − 2)/(Nboot − 1) = 983/999
Wt    : alpha · inverse(Vcov)
```

**Guard G3.** Require `max|Vcov − Vcovᵀ| ≤ 1e-12 · max|Vcov|`, Cholesky of
`Vcov` succeeds, and `cond2(Vcov) = smax/smin` from the singular values of `Vcov` is below 1e12.
Otherwise `INVALID_INPUT` `COVARIANCE_ILL_CONDITIONED`.

For a data vector `y` (either `Dvec` or a `Dsim`):

```
ca = Tuᵀ Wt y      cb = Tvᵀ Wt y     cd = yᵀ Wt y
cc = Tuᵀ Wt Tu     ce = Tuᵀ Wt Tv    cf = Tvᵀ Wt Tv

Amp(mu)   = (ca + mu·cb) / (cc + 2·mu·ce + mu^2·cf)
AmpSd(mu) = sqrt( alpha / (cc + 2·mu·ce + mu^2·cf) )
Chi2(mu)  = cd − (ca + mu·cb)^2 / (cc + 2·mu·ce + mu^2·cf)
```

`Amp` is unconstrained in sign.

```
Chi2 is stationary exactly where
    (ca + mu·cb) · [ (cb·cc − ca·ce) + mu·(cb·ce − ca·cf) ] = 0

muzero = −ca/cb
mu1    = (ca·ce − cb·cc) / (cb·ce − ca·cf)
Cand   = {0, mumax} ∪ {mu1 if 0 ≤ mu1 ≤ mumax}          muzero is never in Cand
muhat  = the element of Cand minimising Chi2; on an exact tie, the smallest
```

**Guard G4**, applied to every fit, observed and simulated. If
`|cb| < 1e-300`, or `|cb·ce − ca·cf| < 1e-300`, or `cf < 1e-300`, then:

- on the observed fit → `INVALID_INPUT` `DEGENERATE_QUADRATIC` with the six
  contractions;
- on a simulated fit → increment `degenCount[keyModel, keyRlo, jj]`, drop that
  dataset from that node's sample, and continue. The dropped dataset does not
  enter the quantile sample and does not enter its denominator.

```
Qstat(mu) = 0                        if muhat > mu
          = Chi2(mu) − Chi2(muhat)   if muhat ≤ mu
```

**Counters.** `edgeCount[keyModel, keyRlo, jj, w]` with `w = 0` counting
simulated datasets whose `muhat` is exactly 0 and `w = 1` counting those whose
`muhat` is exactly `mumax`. Datasets are counted and **retained** in every
sample. `degenCount[keyModel, keyRlo, jj]` counts G4 drops. Both are int64.

## 8. Monte Carlo

```
coarse grid : mu = 0.1·jj ,  jj = 1 … 600
refined grid: mu = 0.05·ii , ii integer, window per §10
nsim        : 100000 on the coarse grid, 200000 on the refined grid
```

`Q95(mu)` is `numpy.quantile(sample, 0.95, method='linear')` over the whole
surviving sample at that node, zeros included.

### Random streams — the full contract

```
rootCal  = numpy.random.SeedSequence(20260802)
rootVal  = numpy.random.SeedSequence(20260803)
rootDual = numpy.random.SeedSequence(20260804)
```

| Consumer | Root |
|---|---|
| §9 `r_lo` scan, §10 endpoint, §11 branches | `rootCal` |
| §13 coverage study | `rootVal` |
| §14 dual-unit run | `rootDual` |

```
key = (keyModel, keyRlo, keyMu, keyStage, keyStep)

keyModel : 0 MODEL-W, 1 MODEL-R
keyRlo   : kk in 0…9 for a grid node of §9; 100 for r_lo = 6.0
keyMu    : round(mu / 0.05) as an integer, half-away-from-zero
keyStage : 0 coarse, 1 refined, 2 coverage, 3 case-B bisection
keyStep  : 0 everywhere except keyStage = 3, where it is the 1-based
           bisection iteration number

rootUsed = the root assigned to the consumer by the table above

rng = numpy.random.default_rng(
          numpy.random.SeedSequence(entropy=rootUsed.entropy, spawn_key=key))
```

The key is index arithmetic and carries no units. It is identical in the §14
run; §14 converts lengths, never key fields.

**Branches share the primary's streams.** `key` contains no branch field, so at
a given node every branch of §11 consumes the same underlying stream as the
primary.

**Consumption order at a node**, executed exactly once per node:

```
zdraw = rng.standard_normal(size=(nsim, 15), dtype=numpy.float64)   # C order
      → simulation bb uses zdraw[bb, :]
if the branch is branch 2:
      rowIndex = rng.integers(0, 1000, size=nsim, dtype=numpy.int64)
      → drawn AFTER zdraw, which is generated and discarded, so that the
        normal stream stays aligned with the primary
```

No other draw is made from `rng`.

```
Dsim[bb] = AmpGen · Tvec(mu) + Lchol · zdraw[bb, :]
```

except branch 2 (§11). `Lchol` is the lower Cholesky factor of `Vgen`.
`AmpGen` is fixed per `(keyModel, keyRlo, keyMu)` and does not vary across
simulations; within the analysis of each `Dsim` the amplitude is re-profiled by
§7.

Primary: `Vgen = Vcov`, `AmpGen = Amp(mu)` computed on `Dvec`.

## 9. r_lo

```
r_lo(kk) = 3.8 + 0.8·kk   Mpc ,   kk = 0 … 9
```

`r_lo = 6.0` is not a node of this grid. It is a separate evaluation with
`keyRlo = 100` and its own full calibration.

`L95` is computed at all eleven. The reported **range** is `[min, max]` over
those nodes of the ten-node grid whose `L95` is numeric. A node whose `L95` is
an outcome label is excluded and listed; a node whose `L95` is numeric stays in
the range **even if it also raised a label**.

**Monotonicity.** Over the retained nodes in ascending `kk`, with consecutive
retained nodes `p` and `q`, the sequence passes if

```
L95(q_) ≥ L95(p) − 2·sqrt( SdMC(p)^2 + SdMC(q_)^2 )   for every consecutive pair
```

Excluded nodes remove both comparisons that involve them; the gap is not
closed. A node whose `SdMC` is `NOT_DEFINED` is treated as excluded for this
test only. Report the verdict, and the **largest violation**, defined as

```
maxViolation = max over pairs of [ L95(p) − 2·sqrt(SdMC(p)^2 + SdMC(q_)^2) − L95(q_) ]
```

taking the maximum over the same pairs. If the sequence passes, report
`maxViolation` as the same expression's maximum, which is then non-positive.

## 10. Upper endpoint

Compute `acc(jj) = [ Qobs(0.1·jj) ≤ Q95(0.1·jj) ]` for `jj = 1 … 600` on the
coarse grid. Define `hasFall` as true when some `jj` in `1 … 599` has `acc(jj)`
true and `acc(jj+1)` false. The four cases below are mutually exclusive and
cover every possible `acc` vector.

| Case | Condition | Action |
|---|---|---|
| **A** | every `acc(jj)` true | `NO_ENDPOINT_IN_RANGE`. Report `max Qobs` over the grid, the `mu` attaining it, and `muzero`. No `L95`. `SdMC = NOT_DEFINED`. |
| **B** | every `acc(jj)` false | bisect as below; `L95` numeric with label `BELOW_FIRST_NODE` |
| **C** | `hasFall` true | `jlast` = the largest such `jj`; refine as below |
| **D** | not A, not B, `hasFall` false | `NO_FALLING_TRANSITION`. Report `acc`, the smallest `jj` with `acc(jj)` true, and `muzero`. No `L95`. `SdMC = NOT_DEFINED`. |

**Case B — bisection.** Evaluate acceptance at `mu` using `rootCal`,
`keyStage = 3`, `keyStep` the 1-based iteration number, and `nsim = 100000`.
Start from the bracket `[0, 0.1]`, whose left end is accepted by construction
and whose right end is rejected because case B holds. Bisect until the bracket
is narrower than 1e-3 Mpc, at most 20 iterations. `L95` is the accepted end of
the final bracket; `mua`, `mub` are that bracket's ends and `SdMC` is computed
from them by the formula below.

**Case C — refinement.** Re-simulate at `nsim = 200000`, `keyStage = 1`, on
`mu = 0.05·ii` for every integer `ii` with
`0.1·jlast − 2 ≤ 0.05·ii ≤ 0.1·jlast + 2`, clipped to `[0.05, mumax]`. On that
grid take the **last** adjacent pair `(mua, mub)` with acceptance true then
false. If no such pair exists, report `REFINEMENT_LOST_CROSSING` with `jlast`,
no `L95`, and `SdMC = NOT_DEFINED`.

```
ga    = Qobs(mua) − Q95(mua)          ≤ 0
gb    = Qobs(mub) − Q95(mub)          > 0
L95   = mua + (mub − mua)·(−ga)/(gb − ga)
wa    = −ga/(gb − ga)     wb = 1 − wa
slope = (gb − ga)/(mub − mua)
SdMC  = sqrt( wb^2·sq(mua)^2 + wa^2·sq(mub)^2 ) / |slope|
```

`mu = 0` is not evaluated and is never an endpoint.

```
sq(mu)   = sqrt(0.95·0.05 / nsim(mu)) / dens(mu)
dens(mu) = (positive fraction at mu) · KDE(mu) evaluated at Q95(mu)
KDE(mu)  : Gaussian kernel density over the strictly positive Qstat values at
           that node, bandwidth
               hkde = 0.9 · min( sdev , iqr/1.34 ) · npos^(−1/5)
           with sdev the standard deviation of those positive values with
           ddof = 1, iqr their 75th minus 25th percentile by
           numpy.quantile(method='linear'), and npos their count.
           If iqr = 0, use hkde = 0.9 · sdev · npos^(−1/5).
           If that is also 0, emit SdMC = NOT_DEFINED.
           Floor: hkde = max(hkde, 1e-9).
```

If `Q95(mu) = 0` at either bracketing node, `SdMC = NOT_DEFINED`, and the
positive fraction at that node is reported.

**Amplitude flag.** Emit `AMPLITUDE_SIGN_CHANGE_IN_RANGE` when
`0 < muzero ≤ mumax`, with `muzero`, `Amp(muhat)` and `AmpSd(muhat)`. It is a
reported flag; it changes nothing.

The full 600-entry `acc` vector is reported in all four cases.

## 11. Branches

MODEL-W, `r_lo = 6.0`, `keyRlo = 100`, sharing the primary's streams. The
coarse grid uses `nsim = 100000`; case-C refinement uses `nsim = 200000` exactly
as in the primary. One at a time from the primary; four branches, not a cross.

| Branch | Change |
|---|---|
| 1 | `Vgen = Vcov / alpha` |
| 2 | `Dsim[bb] = AmpGen·Tvec(mu) + (bs_curves[rowIndex[bb]] − mean of the 1000 rows) restricted to the fitted bins` |
| 3 | `AmpGen = Amp(mu) + AmpSd(mu)` |
| 4 | `AmpGen = Amp(mu) − AmpSd(mu)` |

Report `L95` and `SdMC` for each against the primary. Branch 2 carries the
marker `[WEAK]`.

## 12. Controls

### 12.0 Deviation measures and terminal verbs

```
Dabs(x, y) = max_i | x_i − y_i |
Drel(x, y) = max_i ( | x_i − y_i | / max( |y_i| , tauAbs ) )
tauAbs     = 1e-30 unless a control names another value
```

`y` is the second-named quantity in each control row. A control passes if its
stated criterion holds.

| Verb | Meaning |
|---|---|
| `STOP_RUN` | the whole run ends; §15 items 1–7, 9, 10, 12 are absent |
| `STOP_BRANCH` | that branch's row is absent from §15.10; the run continues |
| `FLAG_AND_RETAIN` | recorded and reported; nothing is removed |
| `INVALID_INPUT` | the inputs do not satisfy this specification; the run ends |
| `NUMERICAL_FAILURE` | a computation did not converge; the run ends |

**Execution order.** Controls 1 and 8 run immediately after §4. Controls 2, 5,
6, 7 run after the kernels at `r_lo = 6.0` exist and before §8. Controls 3, 4
and 9 run in the same place and are report-only. §9–§14 run only if no
terminal verb has fired. Every control emits its measured value whether or not
it passes; a control with no emitted value marks the run failed.

### 12.1 The controls

| # | Check | Criterion | Verb on failure |
|---|---|---|---|
| 1 | `q[i] = r_mp_over_h[i] / r_mp[i]`, all 18 bins. Report `Drel(q, hdata·ones)` and `Drel(q, (1/hdata)·ones)`, and which is smaller | the smaller of the two < 1e-9 | `INVALID_INPUT` `UNIT_INVARIANT_FAILED` |
| 2 | `Kraw2(R, 6.0)` against `(1/R^2)·IntGK( xi(s)·s^2·G2(s/R), r_lo → r_hi )`, all 15 fitted `R` | `Drel` < 1e-6 | `STOP_RUN` `K2_ROUTE_MISMATCH` |
| 3 | `u[i] = Kw2(R_i,6.0)/Kw2(R_0,6.0)`, `v[i] = gcurve(R_i)/gcurve(R_0)` with `R_0` the smallest fitted bin and `gcurve` linearly interpolated onto the 15 fitted `r_mp`; report the standard deviation of `u/v` about its mean, `ddof = 1` | report only | none |
| 4 | sample covariance of the 1000 `bs_curves` rows, `ddof = 1`, all 18 bins, against `df_cov`; report `Drel` with `tauAbs = 1e-12·max|df_cov|` | report only | none |
| 5 | `Kraw3` and `Kw3` at the 15 fitted `R`, `r_lo = 6.0`, recomputed at quadrature tolerance 1e-12 | `Drel` < 1e-6 | `NUMERICAL_FAILURE` `QUADRATURE_NOT_STABLE` |
| 6 | the same kernels at `eps = 0.025` and `eps = 0.10`, each against the `eps = 0.05` values, guard G2 re-applied at each `eps` | `Drel` < 1e-3 and G2 holds | `STOP_RUN` `PV_EPSILON_SENSITIVE` |
| 7 | `Amp(mu)` against `scipy.optimize.minimize_scalar` of `(Dvec − a·Tvec)ᵀ Wt (Dvec − a·Tvec)` over `a`, `method='brent'`, `tol=1e-14`, at `mu = 0` and `mu = 10`, both models | `Drel` < 1e-9 | `STOP_RUN` `PROFILING_MISMATCH` |
| 8 | `rXiMin` and `r_hi` against the first and last converted separations after the §4 sort | exact float64 equality | `INVALID_INPUT` `XI_RANGE_MISMATCH` |
| 9 | SHA-256 of the first 1000 float64 values of `zdraw` at `key = (0, 100, 2, 0, 0)` under `rootCal`, taken as their raw little-endian bytes in C order | report the digest | none |

Control 9 exists so that two implementations can be compared on the stream
itself rather than on downstream numbers.

## 13. Coverage study

```
root      : rootVal          keyStage : 2          keyModel : 0
r_lo      : 6.0              keyRlo   : 100        Vgen : Vcov
muTrue    : 2, 4, 6, 8, 10, 12, 14, 16 Mpc
nsim      : 200000 per muTrue
AmpGen    : Amp(muTrue) computed on Dvec
Q95 used  : the coarse-grid value at that mu, keyStage = 0, nsim = 100000
statistic : the fraction of simulated datasets with Qstat(muTrue) ≤ Q95(muTrue)
band      : |fraction − 0.95| < 3·sqrt(0.95·0.05/200000 + 0.95·0.05/100000)
```

Report the fraction, the band, and PASS or FAIL per `muTrue`, and the number of
`muTrue` failing. No aggregate verdict is formed.

## 14. Dual-unit run

Repeat §5–§10 for MODEL-W at `r_lo = 6.0`, primary branch only, under
`rootDual`.

**Re-expression** means: the same physical length written in h⁻¹Mpc, that is
multiplied by `hdata`. It applies to the `xi` abscissa, `r_mp`, the bin-window
bounds 25 and 225, `r_lo`, `r_hi`, `rXiMin`, `eps`, `mumax`, the coarse step
0.1, the refined step 0.05, the ±2 refinement half-width, and the case-B
bisection tolerance 1e-3. Because the window and `r_mp` are re-expressed
together, the same 15 bins are selected.

Key fields are index arithmetic and are **not** re-expressed. `keyMu` is the
same integer as in §10.

Quadrature: the relative tolerance stays 1e-10; the absolute tolerance is
multiplied by `hdata`.

Convert the resulting `L95` back to physical Mpc by dividing by `hdata`, and
report `|L95_dual − L95|/L95`. PASS if below 0.1%. If either run reports an
outcome label instead of a number, report both labels and no percentage.

## 15. Outputs

### 15.0 Reporting

Items are produced in the order below. A terminal verb from §12.0 determines
which are absent. Every item states its array shape where it has one. Unless a
section says otherwise, an item is at `r_lo = 6.0`.

1. `Kw2`, `Kw3`, `Kraw2`, `Kraw3` at the fitted bin whose `r_mp` is nearest to
   100 Mpc, ties to the smaller `r_mp`; state that `r_mp`. Shape (4,).
2. `muhat`, `mu1`, `muzero`, and whether `0 ≤ mu1 ≤ mumax`, both models.
   Shape (2, 4).
3. `L95` and `SdMC` at all eleven `r_lo`, MODEL-W; the `[min, max]` range over
   the retained ten-node grid; the monotonicity verdict; `maxViolation`; the
   list of excluded nodes. Shapes (11,), (11,), (2,).
4. `L95` and `SdMC` at `r_lo = 6.0`, both models. Shape (2, 2).
5. Coverage: fraction, band, verdict per `muTrue`, and the failure count.
   Shape (8, 3).
6. `Chi2(0) − Chi2(muhat)` and its p-value under `0.5·δ₀ + 0.5·χ²₁`; p = 0.5 if
   the difference is 0. MODEL-W only. Marked `[WEAK]`.
7. The §14 comparison.
8. Controls 1–9, each with its measured value and verdict.
9. `edgeCount` summed over `jj`, reported as `edgeByRlo[keyModel, keyRlo, w]`,
   shape (2, 11, 2), int64; and `degenCount` summed over `jj`, shape (2, 11),
   int64. The observed dataset's own boundary state is reported separately as
   two 0/1 integers per `(keyModel, keyRlo)`, shape (2, 11, 2).
10. Branch table: `L95` and `SdMC` for branches 1–4 against the primary.
    Shape (5, 2).
11. Every outcome label emitted.
12. The `acc` vector for every `L95` attempted. Shape (·, 600), bool.
13. Any place where this document admits more than one implementation, is
    silent on a decision the implementer had to make, or is internally
    inconsistent. **This outranks every number above.**

### 15.11 Outcome labels

The complete set a run may emit:

```
SPLINE_OVERSHOOT              QUADRATURE_NOT_CONVERGED
EXCISION_WINDOW_OUT_OF_RANGE  BIN_COUNT_MISMATCH
COVARIANCE_ILL_CONDITIONED    DEGENERATE_QUADRATIC
NO_ENDPOINT_IN_RANGE          BELOW_FIRST_NODE
NO_FALLING_TRANSITION         REFINEMENT_LOST_CROSSING
AMPLITUDE_SIGN_CHANGE_IN_RANGE
NOT_DEFINED                   UNIT_INVARIANT_FAILED
K2_ROUTE_MISMATCH             QUADRATURE_NOT_STABLE
PV_EPSILON_SENSITIVE          PROFILING_MISMATCH
XI_RANGE_MISMATCH             INVALID_INPUT
NUMERICAL_FAILURE             STOP_RUN
STOP_BRANCH                   FLAG_AND_RETAIN
```

## 16. Standing scope statements

Properties of the procedure, carried into every report of its output. They are
not defects and are not to be reported as discoveries.

- All eleven `r_lo` values lie strictly between the first and second tabulated
  separations of `xi`. The `r_lo` dependence is a dependence on the §4
  interpolant over an interval containing no measurement.
- The `1/(1+xi)` weighting is a modelling choice; MODEL-R is the alternative.
- The principal value is one prescription among several possible ultraviolet
  completions.
- `covariances_sdss_g.txt` is excluded; the kernels are treated as exact.
- No kSZ–xi cross-covariance is available; independence is assumed.
- The calibration fixes the generating amplitude at its value profiled from the
  observed data.
- The endpoint is interpolated between two independently simulated `Q95` nodes.

---

## Appendix — static review questions

Two independent readers answer these from this document alone, pseudocode only,
no numbers, applying the freeze gate stated in the header.

1. Which kernels enter which model, and how is `Kraw2` integrated?
2. Where is `1/(1+xi)` applied?
3. Which lengths are converted, where, and which are not?
4. How is `Pp` integrated, how is `Lam` integrated?
5. How is a simulated dataset formed — covariance, amplitude, and the exact
   order in which the stream is consumed?
6. What is `Wt`?
7. What is `muhat`, and which candidates enter the comparison?
8. What is `Qstat`, and what do `edgeCount` and `degenCount` count?
9. Which of cases A, B, C, D applies to a given `acc` vector, and what does
   each report?
10. What is `SdMC`, and in which states is it `NOT_DEFINED`?
11. What are the nine controls, which terminal verb does each raise, and in
    what order do they run?
12. What is reported, with what shapes, and what is out of scope?
