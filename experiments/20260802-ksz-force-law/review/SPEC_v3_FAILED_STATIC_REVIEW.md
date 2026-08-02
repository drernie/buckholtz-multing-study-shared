# DRAFT SPECIFICATION v3 — kSZ dipole conditional upper limit

**STATUS: DRAFT. NOT FROZEN.** v2 passed the twelve acceptance questions —
two independent readers answered all twelve identically in content — and then
failed the defect stage. One severe under-determination was found by both
readers independently, and several further defects were found by one reader
only, which is the same failure shape as v1 at a finer grain.

v3 closes those. It may be labelled FROZEN only after a fresh dual-reader
review reports no SEVERE and no MAJOR.

Path: `DRAFT_v3 → STATIC_SPEC_REVIEW → FROZEN_v3 → Blind C`.
No blind run may be launched from this document.

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0: descriptive

---

## 0. Scope — what this document does and does not establish

This specification estimates a **conditional, stat-only upper limit on the
effective length ℓ_d = A₃/A₂** within one continuum pairwise-kSZ forward model.

It does **not**: place a limit on β_d; test Figure 3 of any preprint; establish
that the principal value is the physically correct UV completion; propagate
template uncertainty (§5); or determine r_lo from data (§6).

## 0a. Symbol registry — every symbol used below appears here

No symbol may be used in this document unless it is listed. No symbol may carry
two meanings.

| Symbol | Meaning | Defined in |
|---|---|---|
| `R` | separation at which a kernel is evaluated; equals `r_mp` of the bin | §2 |
| `r′` | integration variable, physical Mpc | §2 |
| `ρ` | `r′/R`, dimensionless | §2 |
| `r_lo`, `r_hi` | lower / upper limit of the kernel integral | §2, §6 |
| `ξ(r)` | two-point correlation function, interpolated | §7 |
| `K₂ʳᵃʷ, K₃ʳᵃʷ` | unweighted kernels | §2 |
| `K₂ʷ, K₃ʷ` | weighted kernels | §2 |
| `t(μ, r_lo)` | template vector, one entry per fitted bin | §8 |
| `d` | observed data vector, fitted bins only | §8 |
| `C` | data covariance, fitted bins only | §8 |
| `W` | the inverse covariance actually used in the likelihood | §8 |
| `A`, `Â(μ)`, `σ_A` | nuisance amplitude, its profiled value, its error | §8 |
| `μ` | the parameter of interest; **identical to ℓ_d**, in Mpc | §8 |
| `μ̂` | constrained MLE of μ | §8 |
| `χ²(μ)` | profiled objective | §8 |
| `q̃_μ` | one-sided test statistic | §8 |
| `q₉₅(μ)` | 0.95 quantile of the simulated q̃_μ distribution | §11 |
| `ACC`, `L₉₅` | acceptance set and its supremum | §9 |
| `α` | Hartlap factor | §8 |
| `h_data`, `h_cos` | two distinct values of h | §3 |
| `A₂`, `A₃` | see §8 — `A₂ ≡ A`, `A₃ ≡ A·μ` | §8 |

Symbols deliberately **not** defined and therefore forbidden in any equation:
undecorated `K_k`; `C₄`/`K₄`; `s`.

## 1. Input files — every file carries a usage status

| File | Status | Role |
|---|---|---|
| `dr6.hdf` → `df_pw` (`r_mp`, `ksz_curve`) | **USED_PRIMARY** | data vector |
| `dr6.hdf` → `df_cov` (18×18) | **USED_PRIMARY** | data covariance |
| `dr6.hdf` → `bs_curves` (1000×18) | **USED_CONTROL** | sets N=1000 for α; control 4 |
| `dr6.hdf` → `r_mp_over_h` | **USED_CONTROL** | fixes h_data; control 1 |
| `xi_zbin2.dat` | **USED_PRIMARY** | ξ(r) |
| `sdss_g_sqrtg.csv` | **USED_CONTROL** | control 3; never enters the fit |
| `covariances_sdss_g.txt` | **LISTED_BUT_UNUSED** | §5 — deliberately excluded |

### Controls — enumerated, with pass criteria

Each control has an output slot in §12. A control without a reported result is
a failed run, not a passed one.

| # | Check | Pass criterion |
|---|---|---|
| 1 | `r_mp_over_h[i] / r_mp[i] = h_data` for all 18 bins | max relative deviation < 1e-12 |
| 2 | `K₂ʷ` reproduces the shell-theorem limit: `C₂ = 1` inside, `0` outside | analytic case agrees to < 1e-10 |
| 3 | shape of `K₂ʷ(R)` vs shipped `g(R)` from `sdss_g_sqrtg.csv`, after amplitude-matching | scatter about the best-fit ratio reported; no threshold — this is a *reported diagnostic*, not a gate |
| 4 | sample covariance of the 1000 `bs_curves` equals `df_cov` | max relative deviation reported; no threshold |
| 5 | `K₃` node-refinement: double the quadrature resolution | relative change < 1e-3 |
| 6 | ε-sensitivity: recompute `K₃` at ε = 0.025 and 0.10 Mpc | relative change < 1e-3 (see §4) |
| 7 | amplitude profiling: `Â(μ)` from the closed form vs direct 1-D numerical minimisation over A | agreement < 1e-10 |

## 2. Kernels — raw and weighted are DISTINCT symbols

```
K_k^raw(R) = (1/R^k) · ∫_{r_lo}^{r_hi} ξ(r′) r′² C_k(r′/R) dr′     [see §4 for k=3]

K_k^w(R)   = K_k^raw(R) / (1 + ξ(R))
```

```
C_2(ρ) = 1 for ρ < 1, 0 for ρ > 1, and 1/2 at ρ = 1        (measure zero)
C_3(ρ) = 1/(2(1−ρ²)) + ln|(1+ρ)/(1−ρ)| / (4ρ)              (both sides of ρ=1)
```

`r_hi = 262.19 Mpc`, the upper end of the measured ξ range after conversion by
`h_data`. Because §7 sets ξ = 0 outside the measured range, any larger value is
numerically equivalent; the number is fixed here so that two implementers write
the same integral.

Mass at r′ > R is **included**; one-sided truncation is log-divergent for k=3.

**K₄ is excluded from v3.** Its pole is double and an ordinary principal value
does not define it.

### Status of the weighting — honest labelling

The factor 1/(1+ξ) is **DERIVED** for the monopole: linear theory gives
`v₁₂(r) = −(2/3)Hafr·ξ̄(r)/(1+ξ(r))`, the denominator normalising a conditional
mean, and the shipped `g(r)` is consistent with it for K₂ (control 3).

Applying the same normalisation to **K₃ is a MODEL ASSUMPTION**, not a
consequence of that derivation.

Two models are carried, never merged:

```
MODEL-W (primary)     : weighted K₂ and weighted K₃
MODEL-R (sensitivity) : raw K₂ and raw K₃
```

**Scope of each model** (this fixes what the MC is run for):

| | MODEL-W | MODEL-R |
|---|---|---|
| `μ̂` and stationary point | required | required |
| `L₉₅` at r_lo = 6.0 | required | required |
| full `L₉₅(r_lo)` scan | required | **not required** |
| coverage study | required | not required |

## 3. Units — two distinct h values, do not conflate

```
h_data = 0.6731    embedded in the shipped kSZ package
h_cos  = 0.677     NOT used to reconstruct any shipped coordinate
```

Regression invariant, control 1, all 18 bins:

```
r_mp_over_h[i] / r_mp[i] = h_data
```

Note the field name reads as `r_mp / h`; the equation above is what governs.
An implementation that produces `1/h_data` here has inverted the conversion and
must be corrected, not accommodated.

ξ separations arrive in h⁻¹Mpc and are multiplied by `1/h_data` once, at load,
giving physical Mpc. Reported ℓ_d is in physical Mpc.

## 4. Singular integrand — pole and logarithm are treated DIFFERENTLY

This section replaces v2's global ε-excision, which deleted a real contribution.

Split C₃ into its two pieces:

```
C_3(ρ) = P(ρ) + Λ(ρ),     P(ρ) = 1/(2(1−ρ²)),     Λ(ρ) = ln|(1+ρ)/(1−ρ)|/(4ρ)
```

- `P` has a **simple pole** at ρ = 1. It is defined by a Cauchy principal
  value: symmetric excision of `[R−ε, R+ε]` in the physical variable `r′`, with
  `ε → 0`. Numerically ε = 0.05 Mpc, and control 6 verifies ε-independence.
- `Λ` has an **integrable** logarithmic singularity. It is integrated over the
  **full** range `[r_lo, r_hi]` with no excision. Excising it removes a finite,
  non-cancelling contribution — this was a defect of v2.

Quadrature: adaptive Gauss–Kronrod on each subinterval, with the singular point
`r′ = R` as an explicit breakpoint, absolute and relative tolerance 1e-10.
Control 5 verifies node-independence.

**Applies to k=3 only.** C₂ has no pole; no excision anywhere in K₂.

The physical status of the PV prescription remains **OPEN** (§13).

## 5. Template covariance — deliberately excluded, and said so

`covariances_sdss_g.txt` is **not used**. K₂ and K₃ are treated as exact.
Every limit produced here is labelled:

> **stat-only, fixed-template**

The excluded uncertainty is not negligible: it runs from 0.56% at r = 25 Mpc to
10.4% at r = 225 Mpc, and the 1/r³ constraint is driven by the large-R bins.
Including it belongs to a future version.

## 6. r_lo — the primary output is a CURVE, not a point

r_lo has no first-principles justification. It is an upstream convention, and
it falls inside a gap in ξ (first measured bin 3.69 Mpc, second 11.08 Mpc at
h_data), so the region around it rests on interpolation, not measurement.

**Primary output:** `L₉₅(r_lo)` on the grid

```
r_lo ∈ {3.7, 4.2, 4.7, ... , 11.1} Mpc      step 0.5, both endpoints included
```

reported as a table. **Envelope** means exactly `[min, max]` of `L₉₅` over that
grid — nothing is fitted or smoothed.

**Conditional value** at r_lo = 6.0 Mpc is reported alongside, labelled
`MODEL-SUPPORT CONDITIONAL`.

Prior scans indicate the dependence is **monotone increasing in r_lo with no
interior plateau**; the run must report whether that held. No value of r_lo is
singled out by stability. The envelope must **not** be converted into a
symmetric error bar, and its midpoint must **not** be quoted as a central value.

## 7. Interpolation

```
ξ interpolation : cubic spline over the measured range
outside range   : ξ = 0
```

## 8. Fit and statistic — fully specified

```
MODEL-W:  t(μ, r_lo)[i] = −[ K₂ʷ(R_i)   − μ · K₃ʷ(R_i)   ]
MODEL-R:  t(μ, r_lo)[i] = −[ K₂ʳᵃʷ(R_i) − μ · K₃ʳᵃʷ(R_i) ]
```

The leading minus sign belongs to `t`. The model prediction is `A · t(μ)`, and
`A₂ ≡ A`, `A₃ ≡ A·μ`, so that `ℓ_d = A₃/A₂ = μ`.

```
bins  : all bins with 25 ≤ r_mp ≤ 225 Mpc, endpoints inclusive.
        This must select exactly 15 bins. If it does not, STOP and report —
        do not adjust the range to force the count.
d     : ksz_curve on those bins
C     : df_cov restricted to those bins  (slice first, then invert)
α     : (N − p − 2)/(N − 1),  N = 1000 (rows of bs_curves), p = 15
W     : α · C⁻¹        ← the Hartlap factor enters HERE and nowhere else
```

```
χ²(μ) = (d − Â(μ)·t(μ))ᵀ W (d − Â(μ)·t(μ))

Â(μ) = (tᵀ W d) / (tᵀ W t)        analytic profile, sign unconstrained
σ_A(μ) = (tᵀ W t)^(−1/2)
```

`Â` is allowed to be negative; no positivity constraint is imposed. Control 7
checks the closed form against direct numerical minimisation.

Constrained MLE — **prescribed as a global scan, not a local optimiser**,
because χ²(μ) is a ratio of quadratics in μ and may have more than one
stationary point:

```
μ_max = 60 Mpc
coarse : μ ∈ [0, 60] step 0.01, take the global minimum
refine : golden-section within ±0.01 of that minimum, tolerance 1e-6
μ̂     = the result, which lies in the CLOSED interval [0, μ_max]
```

This is a constrained minimisation, **not** an unconstrained minimum clipped
afterwards.

```
q̃_μ = 0                        if μ̂ > μ
    = χ²(μ) − χ²(μ̂)            if μ̂ ≤ μ
```

**Datasets whose μ̂ lands on the μ_max edge are RETAINED** in every sample,
observed and simulated, with q̃ computed by the definition above. They are
counted and their number reported (§12). They are never dropped: they sit on
the q̃ = 0 side, so discarding them would raise q₉₅ and silently widen the
limit. v2 said "flagged and counted" without saying retained — that ambiguity
moved the answer.

## 9. Upper endpoint — a supremum, not "the zero crossing"

```
ACC = { μ ≥ 0 :  q̃_μ^obs ≤ q₉₅(μ) }        acceptance set
L₉₅ = sup ACC
```

The acceptance set is named `ACC`, not `A`; `A` is the amplitude and nothing
else.

Computationally: scan μ upward over the §11 grid and take the **last
accepted → rejected transition**; interpolate the crossing linearly in μ
between those two bracketing points.

**μ = 0 is never the endpoint.** By construction q̃₀ ≡ 0 for every dataset, so
q₉₅(0) = q̃₀^obs = 0 and μ = 0 is always a trivial root.

**If no accepted → rejected transition exists** anywhere on the grid up to
μ_max, the run does **not** report a limit. It reports
`NO_LIMIT_WITHIN_CALIBRATED_RANGE` together with the largest calibrated μ. That
is a valid outcome, not a failure to be papered over.

## 10. Pseudo-data generation — one primary, others as branches

```
d^(b) ~ N( Â_obs(μ) · t(μ, r_lo),  C_gen )
```

`Â_obs(μ)` is profiled from the **observed** data once per (μ, r_lo) and then
held fixed across all simulations at that point. It is **not** refit per
simulated dataset for the purpose of setting the mean.

Within the *analysis* of each simulated dataset, the amplitude **is** re-profiled
by the §8 formula. Generation and analysis differ here deliberately.

```
C_gen (PRIMARY)  = C                        the sliced 15×15 shipped covariance
C_gen (branch 1) = C / α
C_gen (branch 2) = residual bootstrap: draw a row of bs_curves with replacement,
                   subtract the mean of the 1000 rows, restrict to the 15 fitted
                   bins, and add to the model mean
```

Amplitude branches: primary at `Â_obs(μ)`, branches at `Â_obs(μ) ± σ_A(μ)`.

Branch results are reported in §12; only the primary defines the headline limit.

## 11. Monte-Carlo protocol

```
calibration grid   : μ ∈ [0, 60] Mpc, step 0.1
refinement         : step 0.05 within ±2 Mpc of the coarse-grid crossing,
                     applied ONCE, not iterated
sims per μ         : 100 000; 200 000 within the refinement window
q₉₅(μ)             : the empirical 0.95 quantile, linear interpolation between
                     order statistics (numpy default), computed over ALL sims
                     including those with q̃ = 0
validation ensemble: disjoint RNG stream, 200 000 per checked μ,
                     at μ_true ∈ {2, 4, 6, 8, 10, 12, 14, 16} Mpc
RNG                : numpy default_rng(PCG64), seed = 20260802 for calibration
                     and 20260803 for validation
σ_MC(L₉₅)          : σ[q₉₅] / |d(q̃^obs − q₉₅)/dμ| at the crossing, where
                     σ[q₉₅] is the binomial quantile error
                     √(0.95·0.05/n) / f̂(q₉₅) with f̂ a Gaussian-KDE density
                     estimate, and the derivative is a central difference over
                     the two bracketing grid points
```

**The calibration is recomputed in full at every r_lo node of §6.** q₉₅(μ)
depends on the template shape, the template shape depends on r_lo through both
kernels, so a calibration computed at one r_lo is not valid at another. This is
expensive and it is not optional. v2 did not state this, and two readers
independently identified it as the point where two honest implementations
diverge.

**Known weakness, implemented anyway:** the crossing is taken between two
adjacent, independently simulated q₉₅ points, which amplifies MC noise rather
than averaging it. Fitting a smooth curve through the calibration grid would
reduce this at equal cost. Deferred so this version stays comparable with
existing runs.

## 12. Required outputs

1. `K₂ʷ(100)`, `K₃ʷ(100)`, `K₂ʳᵃʷ(100)`, `K₃ʳᵃʷ(100)`, **each at r_lo = 6.0**.
2. `μ̂` for MODEL-W and MODEL-R at r_lo = 6.0, with the unconstrained global
   minimiser of χ² over ℝ reported separately.
3. `L₉₅(r_lo)` table on the §6 grid, MODEL-W — the primary result.
4. Conditional `L₉₅` at r_lo = 6.0 for MODEL-W and MODEL-R, with σ_MC.
5. Coverage on the validation ensemble at the eight μ_true of §11, MODEL-W.
6. Δχ² between μ = 0 and μ = μ̂, and its p-value under the **50:50 boundary
   mixture** `½δ₀ + ½χ²₁`, the reference distribution for one bounded parameter.
7. Dual-unit run: repeat the full pipeline with all lengths in h⁻¹Mpc — ξ
   separations, r_mp, r_lo, r_hi, ε, **and the μ grid** — then convert the
   resulting limit back to Mpc. Report both and their relative difference; PASS
   is < 0.1%.
8. Results of controls 1–7 (§1), each with its measured value.
9. Count of datasets whose μ̂ hit the μ_max edge, observed and simulated.
10. Branch results of §10, as a table against the primary.
11. Any ambiguity, under-determination or internal inconsistency found while
    implementing — **this outranks every number above**.

## 13. Open issues — stated so they are not re-reported as discoveries

- PV is mathematically canonical for the pole term of C₃. Whether the physics
  instead requires halo exclusion, finite-size convolution, softening or a form
  factor is **OPEN**.
- Weighting of **K₃** is a model assumption (§2), not a derived result.
- r_lo is model support, not a numerical systematic, and dominates.
- No kSZ–ξ cross-covariance is published; independence is assumed.
- Template covariance is excluded by choice (§5); results are fixed-template.
- The crossing-interpolation noise amplification named in §11.

---

## Appendix — static review acceptance criteria

Two independent readers must answer these **identically in content**, and
neither may report a SEVERE or MAJOR defect, before this document may be
labelled FROZEN. They produce pseudocode only, no numbers.

1. Which kernels enter the fit, and for which model?
2. Where is 1/(1+ξ) applied?
3. Which h is used, and where?
4. How is the pole treated, how is the logarithm treated, and why differently?
5. How are pseudo-data generated, with what covariance and what amplitude?
6. Which inverse covariance enters the likelihood, and where does α enter?
7. What is μ̂, and by what algorithm?
8. What is q̃_μ, and what happens to edge datasets?
9. How is the upper limit selected, and what happens if there is no crossing?
10. What does r_lo mean, what is the primary output over it, and is the MC
    recomputed across it?
11. Which input files are unused, and what are the seven controls?
12. What exact claim is produced?
