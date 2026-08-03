# DRAFT SPECIFICATION v4 — kSZ dipole conditional upper limit

**STATUS: DRAFT. NOT FROZEN.** v3 was reviewed by two isolated readers. Both
independently returned the same two SEVERE defects, and their MAJOR lists
largely coincided — a change from the previous round, where the dangerous
defects were the ones only one reader saw. Residual ambiguity is now visible
rather than hidden, which is the reason this version exists rather than a
patch.

One of those two SEVERE was not a defect of the specification at all. It is a
property of the analysis, and §6 now says so out loud.

Path: `DRAFT_v4 → STATIC_SPEC_REVIEW → FROZEN_v4 → Blind C`.
Freeze criterion: **two independent readers, zero SEVERE and zero MAJOR.**
No blind run may be launched from this document.

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0: descriptive

---

## 0. Scope — what this document does and does not establish

This specification estimates a **conditional, stat-only, fixed-template 95%
upper limit on the effective length ℓ_d = A₃/A₂** within one continuum
pairwise-kSZ forward model.

It does **not**: place a limit on β_d (the coupling of the underlying force
law, not addressed here); test Figure 3 of any preprint; establish that the
principal value is the physically correct UV completion; propagate template
uncertainty (§5); or determine r_lo from data (§6 — and §6 now states that no
such determination is possible from the shipped ξ).

The construction is `CL_{s+b}` Neyman inversion with **no `CL_s` protection**.
A downward fluctuation therefore yields a tight limit independently of
sensitivity. This is a deliberate choice, listed in §13, and is the reason the
coverage study (§12) is a required output rather than an optional check.

## 0a. Symbol registry

Complete. Any symbol used anywhere below appears here. No symbol carries two
meanings. `C` alone is never the covariance — the covariance is `Cov`.

| Symbol | Meaning | §  |
|---|---|---|
| `R` | separation at which a kernel is evaluated | 2 |
| `r′` | integration variable, physical Mpc | 2 |
| `ρ` | `r′/R` | 2 |
| `r_lo`, `r_hi` | limits of the kernel integral | 2, 6 |
| `ξ(r)` | correlation function, interpolated per §7 | 7 |
| `ξ̄(r)` | volume-averaged ξ; appears only in the §2 justification | 2 |
| `G₂(ρ)` | geometric weight for k=2 (was `C_2`) | 2 |
| `G₃(ρ)` | geometric weight for k=3 (was `C_3`) | 2 |
| `P(ρ)`, `Λ(ρ)` | pole part and log part of `G₃` | 4 |
| `ε` | PV excision half-width, Mpc | 4 |
| `K₂ʳᵃʷ, K₃ʳᵃʷ` | unweighted kernels | 2 |
| `K₂ʷ, K₃ʷ` | weighted kernels | 2 |
| `t(μ, r_lo)` | template vector over fitted bins | 8 |
| `d` | observed data vector, fitted bins | 8 |
| `d⁽ᵇ⁾` | one simulated data vector | 10 |
| `Cov` | data covariance, fitted bins | 8 |
| `Cov_gen` | covariance used to generate pseudo-data | 10 |
| `W` | weight matrix entering the likelihood | 8 |
| `A`, `Â(μ)`, `Â_obs(μ)`, `σ_A(μ)` | amplitude; profiled; profiled from observed d; its error | 8, 10 |
| `A₂`, `A₃` | `A₂ ≡ A`, `A₃ ≡ A·μ` | 8 |
| `μ` | parameter of interest; **identical to ℓ_d**, Mpc | 8 |
| `μ̂`, `μ_max`, `μ_true` | constrained MLE; upper bound 60 Mpc; injected value in the coverage study | 8, 11 |
| `χ²(μ)` | profiled objective | 8 |
| `q̃_μ`, `q̃ᵒᵇˢ_μ` | one-sided statistic; its value on the observed data | 8 |
| `q₉₅(μ)` | 0.95 quantile of the simulated `q̃_μ` | 11 |
| `ACC`, `L₉₅` | acceptance set; its supremum | 9 |
| `σ_MC` | Monte-Carlo error on `L₉₅` | 11 |
| `α`, `N`, `p` | Hartlap factor; 1000; 15 | 8 |
| `h_data`, `h_cos` | 0.6731; 0.677 (declared, never used) | 3 |
| `g(R)` | shipped pair-weight curve, control 3 only | 1 |

Forbidden in any equation: undecorated `K_k`; `K₄`/`G₄`; `s`; bare `C`.

## 1. Input files

| File | Status | Role |
|---|---|---|
| `dr6.hdf` → `df_pw` (`r_mp`, `ksz_curve`) | **USED_PRIMARY** | data vector |
| `dr6.hdf` → `df_cov` (18×18) | **USED_PRIMARY** | data covariance |
| `dr6.hdf` → `bs_curves` (1000×18) | **USED_PRIMARY** | sets `N`; **generates branch-2 pseudo-data (§10)**; control 4 |
| `dr6.hdf` → `r_mp_over_h` | **USED_CONTROL** | control 1 |
| `xi_zbin2.dat` | **USED_PRIMARY** | ξ(r) |
| `sdss_g_sqrtg.csv` | **USED_CONTROL** | control 3; never enters the fit |
| `covariances_sdss_g.txt` | **LISTED_BUT_UNUSED** | §5 — deliberately excluded |

`bs_curves` was labelled USED_CONTROL in v3. That was wrong: §10 branch 2 uses
its rows to generate pseudo-data, which is an analysis role.

All arrays are cast to float64 immediately on load, before any comparison.

### Controls — with pass criteria AND consequences

| # | Check | Criterion | If it fails |
|---|---|---|---|
| 1 | `r_mp_over_h[i]/r_mp[i] = h_data`, all 18 bins | max rel. dev. < 1e-9 | **STOP.** The shipped units are not what §3 assumes. |
| 2 | `K₂ʳᵃʷ(R)` against the closed form `(1/R²)∫_{r_lo}^{R} ξ r′² dr′` on the same quadrature | rel. dev. < 1e-9 | **STOP.** `G₂` or the quadrature is wrong. |
| 3 | shape of `K₂ʷ(R)` vs shipped `g(R)`, both normalised by their value at the smallest fitted bin, compared at the 15 fitted `r_mp`; report rms of the ratio about its mean | **report only, no threshold** | nothing — diagnostic |
| 4 | sample covariance of the 1000 `bs_curves` rows (1/(N−1) normalisation, all 18 bins) vs `df_cov`; report max rel. dev. | **report only, no threshold** | nothing, but see §8 on what α is and is not doing |
| 5 | `K₃ʷ` and `K₃ʳᵃʷ` at all 15 fitted `R`, `r_lo = 6.0`, recomputed with quadrature tolerance 1e-12 instead of 1e-10 | max rel. dev. < 1e-6 | **STOP.** Quadrature not converged. |
| 6 | same kernels recomputed at ε = 0.025 and 0.10 Mpc | max rel. dev. < 1e-3 | **STOP.** The PV residual is not negligible; ε-extrapolation is required and this version does not specify one. |
| 7 | closed-form `Â(μ)` vs direct 1-D numerical minimisation over `A`, at μ = 0 and μ = 10, both models | rel. dev. < 1e-9 | **STOP.** Profiling is misimplemented. |
| 8 | `r_hi` (§2) equals the largest converted separation in `xi_zbin2.dat` | abs. dev. < 1e-6 Mpc | **STOP.** A too-small `r_hi` silently truncates the k=3 tail and no other control sees it. |

Every control reports its measured value in §12 whether or not it passes. A
control with no reported value is a failed run.

## 2. Kernels — raw and weighted are DISTINCT symbols

```
K_k^raw(R) = (1/R^k) · ∫_{r_lo}^{r_hi} ξ(r′) r′² G_k(r′/R) dr′     [k=3: see §4]

K_k^w(R)   = K_k^raw(R) / (1 + ξ(R))
```

```
G_2(ρ) = 1 for ρ < 1, 0 for ρ > 1, 1/2 at ρ = 1        (measure zero)
G_3(ρ) = 1/(2(1−ρ²)) + ln|(1+ρ)/(1−ρ)| / (4ρ)          (both sides of ρ=1)
```

`r_hi = 262.19 Mpc`. This is asserted to be the largest separation in
`xi_zbin2.dat` after conversion by `h_data`. **Control 8** verifies it: the
loaded ξ table's maximum converted separation must equal `r_hi` to within
1e-6 Mpc, else STOP. A value too large is harmless (§7 zeroes ξ beyond the
table); a value too small silently truncates the `r′ > R` tail that must be
retained, and no other control would notice.

`K₂` integrand: because `G₂` is a step, the integral is exactly
`(1/R²)∫_{r_lo}^{min(R, r_hi)} ξ(r′) r′² dr′`. Evaluate it that way, with
`min(R, r_hi)` as the upper limit — do **not** integrate the step function
numerically across its discontinuity. v3 gave no quadrature rule for `K₂` at
all, having scoped §4 to k=3.

Mass at r′ > R is **included** for k=3; one-sided truncation there is
log-divergent.

**K₄ is excluded.** Its pole is double; an ordinary principal value does not
define it.

### Status of the weighting

`1/(1+ξ)` is **DERIVED** for the monopole: linear theory gives
`v₁₂(r) = −(2/3)Hafr·ξ̄(r)/(1+ξ(r))`, the denominator normalising a conditional
mean. Applying the same normalisation to **K₃ is a MODEL ASSUMPTION**.

```
MODEL-W (primary)     : weighted K₂ and weighted K₃
MODEL-R (sensitivity) : raw K₂ and raw K₃
```

| | MODEL-W | MODEL-R |
|---|---|---|
| `μ̂`, unconstrained stationary point | required | required |
| `L₉₅` at r_lo = 6.0 | required | required |
| full `L₉₅(r_lo)` scan | required | not required |
| coverage study | required | not required |
| §10 branches | required | not required |

## 3. Units

```
h_data = 0.6731    embedded in the shipped kSZ package
h_cos  = 0.677     declared solely to record that it is NOT used
```

`r_mp` is already in physical Mpc and is **never** converted. ξ separations
arrive in h⁻¹Mpc and are multiplied by `1/h_data` once, at load. Reported ℓ_d
is in physical Mpc.

Control 1 checks the invariant `r_mp_over_h[i]/r_mp[i] = h_data`. This is a
property of the shipped file, not of the analysis code: if it fails, the file
is not what this specification assumes and the run stops. v3 told the reader to
"correct the implementation", which is not actionable — no code change alters a
ratio between two shipped arrays.

## 4. Singular integrand — pole and logarithm treated differently

```
G_3(ρ) = P(ρ) + Λ(ρ),     P(ρ) = 1/(2(1−ρ²)),     Λ(ρ) = ln|(1+ρ)/(1−ρ)|/(4ρ)
```

- `P` has a **simple pole** at ρ = 1 and is defined by a Cauchy principal
  value: symmetric excision of `[R−ε, R+ε]` in the physical variable `r′`.
  Numerically ε = 0.05 Mpc. Breakpoints: `r_lo`, `R−ε`, `R+ε`, `r_hi`.
- `Λ` is **integrable**. It is integrated over the full `[r_lo, r_hi]` with
  `r′ = R` as an explicit breakpoint and no excision.

Precondition, checked at runtime: `r_lo < R − ε` and `R + ε < r_hi` for every
fitted `R` and every `r_lo` used. Otherwise the symmetric cancellation does not
apply. STOP if violated.

Quadrature for both terms: adaptive Gauss–Kronrod on each subinterval delimited
by the breakpoints above, absolute and relative tolerance 1e-10, plus the ξ
spline knots as additional breakpoints. If the tolerance is not achieved, STOP.

**Correction to v3's stated reasoning.** v3 justified restoring `Λ` by saying
excision "removes a finite, non-cancelling contribution". That is imprecise:
for an integrable singularity the excised piece vanishes as ε → 0, so what a
global excision loses is a **finite-ε artifact**, not a contribution surviving
the limit. At the ε actually used the artifact is non-negligible, which is why
the split is made; the corrected treatment stands, the stated reason did not.

The physical status of the PV prescription remains **OPEN** (§13).

## 5. Template covariance — deliberately excluded

`covariances_sdss_g.txt` is **not used**; kernels are treated as exact. Every
limit is labelled:

> **stat-only, fixed-template**

The excluded uncertainty runs from 0.56% at r = 25 Mpc to 10.4% at r = 225 Mpc,
and the 1/r³ constraint is driven by the large-R bins.

## 6. r_lo — the honest statement

This section was rewritten after a static reader observed the following, which
is a fact about the analysis and not about the wording.

```
ξ measured at :  3.69 ·········· [no measurement] ·········· 11.08 Mpc
r_lo scanned  :   3.8 ─────────────────────────────────────→ 11.0
```

**Every node of the r_lo scan lies strictly inside a single unmeasured interval
of ξ.** There is therefore no value of r_lo in this range that is supported by
data, and no tightening of this specification can create one. The curve
`L₉₅(r_lo)` traces the behaviour of the **interpolant** across that gap, not a
measured dependence.

Consequences, all binding:

1. The envelope is a **interpolant-and-support sensitivity range**. It is not a
   data-derived uncertainty. It must never be converted into a symmetric error
   bar, and its midpoint must never be quoted as a central value.
2. The monotone behaviour reported in earlier runs is a property of the chosen
   interpolant at least as much as of the physics. The run must report whether
   monotonicity held (output slot §12.12), and that report is a statement about
   the interpolant.
3. §7 must pin the interpolant exactly, because it is the object being probed.

**Scan grid, by explicit rule with no second description:**

```
r_lo_k = 3.8 + 0.8·k   Mpc,   k = 0, 1, ..., 9        →  last node 11.0
```

Ten nodes. No other characterisation of this grid is given, so none can
contradict it. (v3 stated an enumeration, a step, and two endpoints that were
mutually unsatisfiable.)

**`r_lo = 6.0` is NOT a node of this grid** — `(6.0 − 3.8)/0.8 = 2.75`. It is a
separate conditional point, and it receives its **own full calibration** under
§11, not an interpolation from the table. It is reported labelled
`MODEL-SUPPORT CONDITIONAL`.

## 7. Interpolation — pinned, because §6 makes it the object under test

```
abscissa            : r, in physical Mpc (NOT log r)
ordinate            : ξ (NOT r²ξ)
method              : cubic spline, not-a-knot boundary condition
                      (scipy.interpolate.CubicSpline default, bc_type='not-a-knot')
outside table range : ξ = 0
```

Runtime guard: if the interpolant produces `1 + ξ(R) ≤ 0.01` at any fitted `R`,
STOP — the weighted kernels are not defined there and a spline overshoot must
not be absorbed silently.

## 8. Fit and statistic

```
MODEL-W:  t(μ, r_lo)[i] = −[ K₂ʷ(R_i)   − μ · K₃ʷ(R_i)   ]
MODEL-R:  t(μ, r_lo)[i] = −[ K₂ʳᵃʷ(R_i) − μ · K₃ʳᵃʷ(R_i) ]
```

The leading minus belongs to `t`. Prediction is `A·t(μ)`; `A₂ ≡ A`,
`A₃ ≡ A·μ`, hence `ℓ_d = A₃/A₂ = μ`.

```
bins  : all bins with 25 ≤ r_mp ≤ 225 Mpc, endpoints inclusive.
        This must select exactly 15 bins. If not, STOP and report.
d     : ksz_curve on those bins
Cov   : df_cov restricted to those bins — slice first, then invert
α     : (N − p − 2)/(N − 1),  N = 1000 rows of bs_curves, p = 15
W     : α · Cov⁻¹
```

```
χ²(μ) = (d − Â(μ)·t(μ))ᵀ W (d − Â(μ)·t(μ))
Â(μ)  = (tᵀ W d)/(tᵀ W t)        sign unconstrained
σ_A(μ) = (tᵀ W t)^(−1/2)
```

**What α does and does not do.** α cancels out of `Â` identically, so `χ²`
scales linearly with α, so `q̃` scales with α — and `q₉₅` is built from
simulations analysed with the same `W`, so it scales with α too. **The
acceptance set of §9, and therefore `L₉₅`, are exactly α-invariant.** α
survives only in the §12 Δχ²/p-value and in `Cov_gen` branch 1. v3's "α enters
here and nowhere else" was true and misleading; this paragraph replaces it.

Note also that α is the inverse-Wishart correction for a covariance built from
`N` **independent** realisations. `bs_curves` are resamples, and this document
does not establish that `df_cov` is their sample covariance — control 4
measures the discrepancy and does not gate on it. Because of the exact
cancellation above, this affects no limit reported here; it does affect §12's
p-value, which is therefore labelled `[WEAK]` on this ground in addition to
§12.6's own.

**Constrained MLE — closed form, not a scan.** `χ²(μ)` is a ratio of
quadratics in μ:

```
χ²(μ) = dᵀWd − (a + μb)² / (c + 2μe + μ²f)
  a = tuᵀWd, b = tvᵀWd, c = tuᵀWtu, e = tuᵀWtv, f = tvᵀWtv
  where t(μ) = tu + μ·tv,  tu = −K₂,  tv = +K₃  (the appropriate variant)
```

Stationarity of the subtracted term reduces to a quadratic in μ. Compute both
roots exactly, evaluate `χ²` at each root and at both endpoints `{0, μ_max}`,
and take the smallest — this is the exact constrained minimiser over the closed
interval `[0, μ_max]`, `μ_max = 60 Mpc`. Report also the unconstrained global
minimiser over ℝ, obtained from the same root set without the endpoint clamp.

v3 mandated a step-0.01 global scan per dataset. With ~601 calibration nodes ×
10⁵ simulations × 10 r_lo nodes that is not a runnable computation, so every
implementer would have invented an unstated shortcut. The closed form above is
exact and cheap; it is now the prescription, and no scan is authorised.

```
q̃_μ = 0                   if μ̂ > μ
    = χ²(μ) − χ²(μ̂)       if μ̂ ≤ μ
```

**Edge datasets are RETAINED** in every sample, observed and simulated, with
`q̃` computed as above; their count is reported (§12). They sit on the `q̃ = 0`
side, so discarding them would raise `q₉₅` and silently widen the limit.

## 9. Upper endpoint

```
ACC = { μ ∈ [0, μ_max] :  q̃ᵒᵇˢ_μ ≤ q₉₅(μ) }
L₉₅ = sup ACC
```

The set is named `ACC`; `A` is the amplitude and nothing else.

Because `q̃ᵒᵇˢ` need not be monotone and `q₉₅` is noisy, `ACC` may be
disconnected. Three cases, all defined:

| Case | Rule |
|---|---|
| a transition exists and the top node `μ_max` is **rejected** | `L₉₅` = the **last** accepted→rejected transition, interpolated linearly in `q̃ᵒᵇˢ_μ − q₉₅(μ)` between the two bracketing nodes |
| the top node is **accepted** | report `NO_UPPER_ENDPOINT` — `sup ACC = μ_max` and the limit is not resolved. Do not return an interior crossing. |
| no transition anywhere | report `NO_CROSSING` (see below) |

**μ = 0 is never the endpoint, and the interpolation must not return it.**
`q̃₀ ≡ 0` for every dataset, so `q₉₅(0) = q̃ᵒᵇˢ₀ = 0` and μ = 0 is always
accepted with the difference exactly zero. If the last accepted→rejected
transition is the pair `(0, first node)`, linear interpolation between an exact
zero and a positive value lands on μ = 0 — v3 named this degeneracy and then
prescribed an algorithm that walks into it. Rule: **the crossing search starts
at the first grid node above 0**, and μ = 0 is excluded from `ACC`'s
transition search (it remains in `ACC` as a member).

**On `NO_CROSSING`.** `t(μ)` is linear in μ, so as μ → ∞

```
χ²(∞) = dᵀWd − (K₃ᵀWd)² / (K₃ᵀWK₃)     — finite
```

`q̃_μ` therefore **saturates** rather than growing without bound. If its
plateau lies below `q₉₅`, no crossing exists at **any** μ, not merely within
the calibrated range, and extending the calibration cannot recover one. The
outcome is reported as `NO_CROSSING — statistic saturates below threshold`,
together with the plateau value and `q₉₅` at `μ_max`. v3's
`NO_LIMIT_WITHIN_CALIBRATED_RANGE` implied the opposite and is withdrawn.

**Identifiability.** `μ = A₃/A₂` is undefined as `A₂ → 0`, and §8 permits `Â`
to change sign. If `|Â(μ̂)| < σ_A(μ̂)`, the run reports
`AMPLITUDE_CONSISTENT_WITH_ZERO` alongside the limit: the ratio being bounded
is then a ratio of two quantities, one of which is not detected.

## 10. Pseudo-data generation

```
d⁽ᵇ⁾ ~ N( Â_gen · t(μ, r_lo),  Cov_gen )
```

`Â_obs(μ)` is profiled from the **observed** `d` once per (μ, r_lo, model) and
held fixed across all simulations at that point. Within the *analysis* of each
simulated dataset the amplitude **is** re-profiled by §8. This asymmetry is
deliberate; it makes the calibration a plug-in construction, which is listed in
§13.

```
PRIMARY   : Cov_gen = Cov              Â_gen = Â_obs(μ)
branch 1  : Cov_gen = Cov / α          Â_gen = Â_obs(μ)
branch 2  : residual bootstrap         Â_gen = Â_obs(μ)
branch 3  : Cov_gen = Cov              Â_gen = Â_obs(μ) + σ_A(μ)
branch 4  : Cov_gen = Cov              Â_gen = Â_obs(μ) − σ_A(μ)
```

**One-at-a-time from the primary. Four branches, not a cross.**

Branch 2, residual bootstrap: draw one of the 1000 `bs_curves` rows with
replacement, subtract the mean of all 1000 rows, restrict to the 15 fitted
bins, add to the model mean. **Caveat, binding on its interpretation:** the
resulting `q̃` distribution has at most 1000 distinct support points regardless
of the number of draws, so its 0.95 quantile is determined by a few dozen rows
and §11's `σ_MC` formula understates its error. Branch 2 is reported as an
indicative check only and carries the marker `[WEAK]`.

Branches are run at `r_lo = 6.0`, MODEL-W, with 100 000 simulations per μ, and
**share the primary's RNG streams** (§11) so that branch-minus-primary
differences are not dominated by independent Monte-Carlo noise.

## 11. Monte-Carlo protocol

```
calibration grid : μ ∈ [0, 60] Mpc, step 0.1                (601 nodes)
refinement       : step 0.05 within ±2 Mpc of the coarse crossing, applied ONCE
sims per μ       : 100 000 coarse; 200 000 in the refinement window
                   Refinement nodes that coincide with coarse nodes are
                   RE-SIMULATED at 200 000; the two samples are not merged.
                   The final crossing is taken on the refined grid alone.
q₉₅(μ)           : empirical 0.95 quantile, linear interpolation between order
                   statistics, over ALL simulations including those with q̃ = 0
```

**RNG — stream derivation is specified, because a bare seed is not enough.**

```
root       = numpy.random.SeedSequence(20260802)      calibration
             numpy.random.SeedSequence(20260803)      validation ensemble
per-node   = root.spawn_key extended by the integer tuple
             (model_id, branch_id, r_lo_index, mu_index_times_100)
generator  = numpy.random.default_rng(SeedSequence(entropy=root.entropy,
                                                   spawn_key=that tuple))
normal draw= Cholesky factor of Cov_gen, lower, applied to standard normals
```

Every simulation set is therefore reproducible independently of loop order, and
identical `(r_lo, μ)` nodes across branches receive identical standard normals.
v3 gave one seed for thousands of independent calibrations with no derivation
rule, which made the result depend on the order the loops happened to be
written.

**Calibration is recomputed in full at every r_lo node of §6, and separately at
r_lo = 6.0.** `q₉₅(μ)` depends on template shape; template shape depends on
r_lo through both kernels. Expensive, not optional.

```
validation ensemble : SeedSequence(20260803), disjoint from calibration,
                      200 000 per μ_true ∈ {2,4,6,8,10,12,14,16} Mpc,
                      MODEL-W, r_lo = 6.0, Cov_gen = Cov,
                      Â_gen = Â_obs(μ_true)
coverage statistic  : the fraction of validation datasets for which
                      μ_true ∈ ACC — i.e. q̃_{μ_true} ≤ q₉₅(μ_true).
                      This is the acceptance rate at μ_true, NOT the frequency
                      of L₉₅ ≥ μ_true; with ACC possibly disconnected the two
                      differ, and the acceptance rate is what the Neyman
                      construction guarantees.
pass criterion      : |coverage − 0.95| < 3·√(0.95·0.05/200000) at every μ_true
```

Because the validation ensemble is generated at `Â_obs(μ_true)` — the same
plug-in prescription used for calibration — this study **cannot** detect
plug-in bias in the nuisance parameter. It checks the Neyman construction, not
the profiling. Listed in §13.

```
σ_MC(L₉₅) = √( σ[q₉₅(μ_a)]² + σ[q₉₅(μ_b)]² ) / |slope|
  μ_a, μ_b : the two bracketing refined nodes
  slope    : (q̃ᵒᵇˢ−q₉₅)(μ_b) − (q̃ᵒᵇˢ−q₉₅)(μ_a) over (μ_b − μ_a)   [a secant]
  σ[q₉₅]   : √(0.95·0.05/n) / f̂(q₉₅), n the sims at that node,
             f̂ a Gaussian KDE with Silverman bandwidth fitted to the
             STRICTLY POSITIVE q̃ values only, rescaled by the positive
             fraction — the atom at q̃ = 0 must be excluded from the density
             estimate or the bandwidth is inflated by the point mass.
```

v3 propagated one bracketing point and called a two-point secant a central
difference; both are corrected above.

**Known weakness, retained:** the crossing still sits between two independently
simulated `q₉₅` points, which amplifies noise rather than averaging it. A
smooth fit through the calibration grid would reduce this at equal cost.
Deferred, so that this version stays comparable with existing runs.

## 12. Required outputs

Unless stated otherwise, every item is at `r_lo = 6.0`.

1. `K₂ʷ(R)`, `K₃ʷ(R)`, `K₂ʳᵃʷ(R)`, `K₃ʳᵃʷ(R)` at the **fitted bin nearest to
   100 Mpc**, with that bin's `r_mp` stated. (`R` is a bin separation by
   definition; there may be no bin at exactly 100.)
2. `μ̂` and the unconstrained stationary points, both models.
3. `L₉₅(r_lo)` on the §6 ten-node grid, MODEL-W — reported as the
   **interpolant-and-support sensitivity curve** of §6, with `[min, max]`.
4. Conditional `L₉₅` at r_lo = 6.0, both models, with `σ_MC`.
5. Coverage at the eight `μ_true`, MODEL-W, with the pass verdict.
6. Δχ² = χ²(0) − χ²(μ̂) ≥ 0, and its p-value under `½δ₀ + ½χ²₁`. **Marked
   `[WEAK]`**: it is the only asymptotic tail probability in an otherwise
   MC-calibrated analysis; μ is bounded at both ends, not one; and the mixture's
   regularity conditions fail where `Â → 0` (§9). If Δχ² = 0 exactly, report
   p = 0.5 and say so.
7. Dual-unit run. **Reading fixed:** every length is converted to h⁻¹Mpc —
   ξ separations, `r_mp`, `r_lo`, `r_hi`, `ε`, **and** `μ_max`, the μ grid
   bounds and all μ steps — the pipeline is re-run, and the resulting limit is
   converted back to Mpc. The comparison therefore tests that no length is
   handled in the wrong system; it is **not** a grid-discretisation test.
   Repeat at `r_lo = 6.0`, MODEL-W, primary branch only. PASS < 0.1%.
8. Controls 1–8, each with its measured value and verdict.
9. Edge-dataset counts, observed and simulated, per (r_lo, μ) aggregated.
10. Branch table: the four §10 branches against the primary, at r_lo = 6.0.
11. Whether `AMPLITUDE_CONSISTENT_WITH_ZERO` was raised (§9).
12. Whether `L₉₅(r_lo)` was monotone with no interior plateau — reported as a
    statement about the interpolant, per §6.
13. Any ambiguity, under-determination or internal inconsistency found while
    implementing — **this outranks every number above.**

## 13. Open issues — stated so they are not re-reported as discoveries

- PV is mathematically canonical for the pole term of `G₃`. Whether the physics
  requires halo exclusion, finite-size convolution, softening or a form factor
  instead is **OPEN**.
- Weighting of `K₃` is a model assumption, not a derived result.
- **No value of r_lo in the scanned range is supported by data** (§6). This is
  not a numerical systematic and cannot be removed by a better specification.
- The construction is `CL_{s+b}` with no `CL_s` protection (§0).
- The calibration is a plug-in construction in the nuisance amplitude, and the
  coverage study shares that assumption, so it cannot detect plug-in bias.
- α cancels from every limit reported here (§8); it is not doing the work its
  prominence suggests.
- No kSZ–ξ cross-covariance is published; independence is assumed.
- Template covariance is excluded by choice (§5).
- The crossing-interpolation noise amplification named in §11.

---

## Appendix — static review acceptance criteria

Two independent readers must answer these identically in content, **and neither
may report a SEVERE or a MAJOR defect**, before this document is labelled
FROZEN. Pseudocode only, no numbers.

1. Which kernels enter the fit, for which model, and how is `K₂` integrated?
2. Where is 1/(1+ξ) applied, and what is its epistemic status for each k?
3. Which h is used, where, and what is never converted?
4. How is the pole treated, how is the logarithm treated, and why differently?
5. How are pseudo-data generated, with what covariance and what amplitude?
6. Which weight matrix enters the likelihood, and what does α actually affect?
7. What is `μ̂`, and by what algorithm?
8. What is `q̃_μ`, and what happens to edge datasets?
9. How is the upper limit selected, and what are the three non-standard
   outcomes and their triggers?
10. What does r_lo mean, why is the scan not data-supported, and is the MC
    recomputed across it?
11. Which input files are unused, what are the eight controls, and what does a
    failing control do?
12. What exact claim is produced, and what is explicitly excluded from it?
