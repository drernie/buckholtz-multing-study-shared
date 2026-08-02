# DRAFT SPECIFICATION v2 — kSZ dipole conditional upper limit

**STATUS: DRAFT. NOT FROZEN.** v1 was labelled FROZEN and was not: an
independent implementer following it honestly showed that its text admits
several materially different readings, one of them trivially degenerate. A
specification is judged by its symbols, not by its author's intent.

Path to freezing: `DRAFT_v2 → STATIC_SPEC_REVIEW → DUAL_READER_DRY_RUN →
FROZEN_v2 → Blind C`. No blind run may be launched from this document.

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0: descriptive

---

## 0. Scope — what this document does and does not establish

This specification estimates a **conditional, stat-only upper limit on the
effective length ℓ_d = A₃/A₂** within one continuum pairwise-kSZ forward model.

It does **not**: place a limit on β_d; test Figure 3 of any preprint; establish
that the principal value is the physically correct UV completion; propagate
template uncertainty (see §5); or determine r_lo from data (see §6).

## 1. Input files — every file carries a usage status

| File | Status | Role |
|---|---|---|
| `dr6.hdf` → `df_pw` (`r_mp`, `ksz_curve`) | **USED_PRIMARY** | data vector |
| `dr6.hdf` → `df_cov` (18×18) | **USED_PRIMARY** | data covariance |
| `dr6.hdf` → `bs_curves` (1000×18) | **USED_CONTROL** | sets N=1000 for Hartlap; control 7 checks it equals `df_cov` |
| `dr6.hdf` → `r_mp_over_h` | **USED_CONTROL** | fixes h_data, §3 |
| `xi_zbin2.dat` | **USED_PRIMARY** | ξ(r) |
| `sdss_g_sqrtg.csv` | **USED_CONTROL** | external check of K₂ʷ; never enters the fit |
| `covariances_sdss_g.txt` | **LISTED_BUT_UNUSED** | see §5 — deliberately excluded, result is fixed-template |

No file may sit in the input package without a status.

## 2. Kernels — raw and weighted are DISTINCT symbols

```
K_k^raw(R) = (1/R^k) · PV ∫_{r_lo}^{r_hi} ξ(r') r'^2 C_k(r'/R) dr'

K_k^w(R)   = K_k^raw(R) / (1 + ξ(R))
```

The undecorated symbol `K_k` is **not defined** in this document and must not
appear in any model equation.

```
C_2(ρ) = 1 for ρ < 1, 0 for ρ > 1                                   (exact)
C_3(ρ) = 1/(2(1−ρ²)) + ln|(1+ρ)/(1−ρ)| / (4ρ)      (both sides of ρ=1)
```

Mass at r′ > R is **included**; one-sided truncation is log-divergent for k=3.

**K₄ is excluded from v2.** Its pole is double and an ordinary principal value
does not define it.

### Status of the weighting — honest labelling

The factor 1/(1+ξ) is **DERIVED** for the monopole: linear theory gives
`v12(r) = −(2/3)Hafr·ξ̄(r)/(1+ξ(r))`, the denominator normalising a conditional
mean, and the shipped `g(r)` confirms it for K₂ (control 6).

Applying the same normalisation to **K₃ is a MODEL ASSUMPTION**, not a
consequence of that derivation. v1 labelled the whole section DERIVED; that was
an over-claim, corrected here.

Two models are therefore carried, never merged:

```
MODEL-W (primary)     : weighted K₂ and weighted K₃
MODEL-R (sensitivity) : raw K₂ and raw K₃
```

## 3. Units — two distinct h values, do not conflate

```
h_data      = 0.6731    embedded in the shipped kSZ package
h_cosmology = 0.677     NOT used to reconstruct any shipped coordinate
```

`h_data` is fixed by the data itself. Regression invariant, must hold for all
18 bins:

```
r_mp_over_h / r_mp = h_data     (exactly, to floating precision)
```

ξ separations arrive in h⁻¹Mpc and are converted with `h_data`, once, at load.
Reported ℓ_d is in physical Mpc.

v1 asserted "h enters exactly ONCE" with h=0.677. That was **false**: h also
enters implicitly through the upstream-fixed r_lo, and 0.677 disagrees with the
data. Using h_data improves the external template match by ~8× (shape scatter
1.8e-3 → 2.2e-4).

## 4. Principal value — formal definition, and where it applies

```
PV ∫ f(r') dr' = lim_{ε→0⁺} [ ∫_{r_lo}^{R−ε} f dr' + ∫_{R+ε}^{r_hi} f dr' ]
```

Symmetry is in the **physical variable r′**, not in a grid index, not in ρ.
Numerically ε = 0.05 Mpc.

**Applies to k=3 only.** C₂ has no pole; applying an exclusion there removes a
one-sided slice of a nonzero integrand and is a bias, not a regularisation.
v1 applied it globally — corrected.

The physical status of the PV prescription remains **OPEN** (§9).

## 5. Template covariance — deliberately excluded, and said so

`covariances_sdss_g.txt` is **not used**. The kernels K₂ and K₃ are treated as
exact. Consequently every limit produced here is labelled:

> **stat-only, fixed-template**

The excluded uncertainty is not negligible: it runs from 0.56% at r=25 Mpc to
10.4% at r=225 Mpc, and the 1/r³ constraint is driven by the large-R bins.
v1 listed this file and silently set its information to zero without saying so;
that omission is corrected by this explicit exclusion. Including it belongs to
a future v3.

## 6. r_lo — the primary output is a CURVE, not a point

r_lo has no first-principles justification. It is an upstream convention, and
it falls inside a gap in ξ (first bin 3.69 Mpc, second 11.08 Mpc at h_data), so
the region around it rests on interpolation rather than measurement.

**Primary output:** `L₉₅(r_lo)` over `r_lo ∈ [3.7, 11.1] Mpc`, reported as a
table and an envelope.

**Conditional value** at r_lo = 6.0 Mpc is reported alongside, explicitly
labelled `MODEL-SUPPORT CONDITIONAL`.

Prior scans show the dependence is **monotone with no interior plateau**, so no
value of r_lo is singled out by stability. The envelope must **not** be
converted into a symmetric error bar, and its midpoint must **not** be quoted
as a central value.

## 7. Interpolation

```
ξ interpolation : cubic spline over the measured range
outside range   : ξ = 0
```

## 8. Fit and statistic — fully specified

```
MODEL-W:  p_kSZ(R) = −A [ K₂^w(R) − ℓ_d K₃^w(R) ]
MODEL-R:  p_kSZ(R) = −A [ K₂^raw(R) − ℓ_d K₃^raw(R) ]

bins        : 15 bins, 25 ≤ r_mp ≤ 225 Mpc
covariance  : df_cov, sliced to the fitted bins
Hartlap     : α = (N−p−2)/(N−1), N = 1000, p = 15
amplitude   : nuisance, profiled analytically, Â(μ) = tᵀC⁻¹d / tᵀC⁻¹t
parameter   : ℓ_d ≥ 0, in Mpc
```

Constrained MLE and one-sided statistic:

```
μ̂ = argmin_{μ ∈ [0, μ_max]} χ²_prof(μ),        μ_max = 60 Mpc

q̃_μ = 0                                  if μ̂ > μ
    = χ²_prof(μ) − χ²_prof(μ̂)            if μ̂ ≤ μ
```

μ̂ is the constrained minimiser over the closed interval, **not** an
unconstrained minimum clipped afterwards. If μ̂ lands on the μ_max edge, the
dataset must be flagged and counted, not silently accepted.

## 9. Upper endpoint — defined as a supremum, not as "the zero crossing"

```
A = { μ ≥ 0 :  q̃_μ^obs ≤ q₀.₉₅(μ) }        acceptance set
L₉₅ = sup A
```

Computationally: scan μ upward and take the **last accepted → rejected
transition**; interpolate the crossing linearly between those two grid points.

**μ = 0 is never the endpoint.** By construction q̃₀ ≡ 0 for every dataset, so
`q₀.₉₅(0) = q̃₀^obs = 0` and μ=0 is always a trivial root. v1 said "interpolate
the zero crossing", which a literal reader resolves at μ=0 and returns
L₉₅ = 0. That defect is the reason this section was rewritten.

## 10. Pseudo-data generation — one primary, others as branches

```
d^(b) ~ N( m(μ, Â(μ)), C_gen )

C_gen (PRIMARY)      = df_cov                      [the shipped covariance]
C_gen (branch 1)     = df_cov / α_Hartlap
C_gen (branch 2)     = resample the 1000 bs_curves
```

v1 fixed the mean and left the dispersion unstated; the three readings spread
the endpoint by ~0.26 Mpc (3%), an order of magnitude above MC error.

Nuisance-amplitude generation: primary at `Â(μ)`, branches at `Â(μ) ± 1σ_A`.

## 11. Monte-Carlo protocol

```
calibration grid   : μ ∈ [0, 20] Mpc, step 0.1
refinement         : step 0.05 within ±2 Mpc of the crossing
sims per μ         : 100 000 minimum; 200 000 within the refinement window
validation ensemble: disjoint RNG stream, ≥ 200 000 per checked μ
RNG                : numpy default_rng (PCG64); seed reported
MC uncertainty     : report σ_MC(L₉₅) from the q₀.₉₅ error and dq_obs/dμ
```

v1's floor of 12 000 was too weak: the endpoint's seed-to-seed sd is 0.075 Mpc
at 12 000 and 0.009 at 200 000. Reporting the seed does not make a number
seed-independent.

**Known weakness, implemented anyway:** the crossing is taken between two
adjacent, independently simulated q₀.₉₅ points, which amplifies MC noise rather
than averaging it. Fitting a smooth curve through the calibration grid would
reduce this by ~an order of magnitude at equal cost. Deferred to v3 so that v2
stays comparable with existing runs.

## 12. Required outputs

1. `K₂^w(100)`, `K₃^w(100)`, `K₂^raw(100)`, `K₃^raw(100)`.
2. `ℓ̂_d` for MODEL-W and MODEL-R, with the unconstrained stationary point.
3. `L₉₅(r_lo)` table over [3.7, 11.1] — the primary result.
4. Conditional `L₉₅` at r_lo = 6.0 Mpc, with σ_MC.
5. Coverage on the disjoint validation ensemble, several μ_true.
6. Δχ² and p-value for the 1/s³ term.
7. Dual-unit run, **stating whether the μ grid was converted** (it must be).
8. Any ambiguity, under-determination or internal inconsistency — outranks
   every number above.

## 13. Open issues — stated so they are not re-reported as discoveries

- PV is mathematically canonical for this integral. Whether the physics instead
  requires halo exclusion, finite-size convolution, softening or a form factor
  is **OPEN**.
- Weighting of **K₃** is a model assumption (§2), not a derived result.
- r_lo is model support, not a numerical systematic, and dominates.
- No kSZ–ξ cross-covariance is published; independence is assumed.
- Template covariance is excluded by choice (§5); results are fixed-template.

---

## Appendix — static review acceptance criteria

Two independent readers must answer these **identically in content** before
this document may be labelled FROZEN. They produce pseudocode only, no numbers.

1. Which kernels enter the fit?
2. Where is 1/(1+ξ) applied?
3. Which h is used, and where?
4. Where is the PV applied, and where is it not?
5. How are pseudo-data generated, with what covariance?
6. Which covariance enters the likelihood?
7. What is μ̂?
8. What is q̃_μ?
9. How is the upper limit selected?
10. What does r_lo mean, and what is the primary output over it?
11. Which input files are unused?
12. What exact claim is produced?
