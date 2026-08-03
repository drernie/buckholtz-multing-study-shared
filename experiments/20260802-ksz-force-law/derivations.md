# Companion note to DRAFT_SPEC_v5 — derivations and reasoning

**This document is not part of the freeze gate.** It explains why the
prescriptions in `DRAFT_SPEC_v5.md` are what they are. An error here is
corrected here; it does not reopen the specification unless it implies that a
prescription is wrong, in which case the prescription is amended and the
specification goes back through review.

The separation exists because three rounds of static review found zero errors
in what the specification *prescribed* and six errors in what it *asserted
about itself*. Reasoning and instructions now live apart.

---

## 1. The two parts of `G₃`

```
G₃(ρ) = P(ρ) + Λ(ρ),    P = 1/(2(1−ρ²)),    Λ = ln|(1+ρ)/(1−ρ)|/(4ρ)
```

`P` has a simple pole at ρ = 1. Its integral exists only as a Cauchy principal
value: the divergences from the two sides are equal and opposite and cancel
under symmetric excision. The excision must be symmetric in the physical
variable `s`, not in ρ and not in a quadrature index, because that is the
variable in which the two contributions are mirror images.

`Λ` has a logarithmic singularity at ρ = 1, which is integrable. It needs no
regularisation, and excising a window around it removes a piece of the integral
that should be kept.

**Precise statement of what a global excision costs.** For an integrable
singularity the excised piece is `O(ε ln ε)` and vanishes as ε → 0. So a global
excision does not lose a contribution that survives the limit; it loses a
finite-ε artifact. At ε = 0.05 Mpc that artifact is not assumed negligible —
control 6 measures it, and the run stops if the ε-dependence exceeds 1e-3.

(v2 applied the excision globally. v3 corrected the treatment but justified it
by saying the excised piece was a contribution surviving the limit, which is
wrong for an integrable singularity. v4 corrected the justification. The
prescription has been the same since v3.)

`G₂` has no singularity — it is a step — so `Kraw2` reduces to an integral with
the step's location as the upper limit, and no excision appears anywhere in it.

`K₄` would carry a double pole. A double pole is not defined by an ordinary
principal value: the two sides diverge with the same sign and do not cancel. It
is excluded rather than regularised by a prescription this document does not
have.

## 2. What the Hartlap factor does

`Wt = alpha · V⁻¹`. Two facts follow.

**It cancels from `L95` exactly.**

```
Amp(μ)  = TᵀWt D / TᵀWt T  = TᵀV⁻¹D / TᵀV⁻¹T      — alpha cancels
Chi2(μ) = (D − Amp·T)ᵀ Wt (D − Amp·T)             — scales as alpha
Q(μ)    = Chi2(μ) − Chi2(muhat)                   — scales as alpha
```

Simulated datasets are analysed with the same `Wt`, so `Q95(μ)` scales as alpha
too. The comparison `Qobs(μ) ≤ Q95(μ)` is therefore invariant, and so is the
acceptance set, the interpolated crossing, and `SdMC`.

**It does not cancel from everything.**

```
AmpSd(μ) = sqrt( alpha / (TᵀWt T) )
```

so branches 3 and 4, which generate at `Amp ± AmpSd`, do depend on alpha. So
does branch 1, which uses `Vgen = V/alpha` by construction. So does the §15.6
p-value, which is read off an asymptotic distribution rather than from the
calibrated `Q95`.

(v4 stated the cancellation and then enumerated the exceptions incompletely,
omitting `AmpSd`. Numerically `alpha^(−1/2) = 1.0081`, so the omission is small,
but the claim was stated as exhaustive.)

## 3. `AmpSd` is the sampling standard deviation, not the Δχ²=1 width

With `D` distributed with covariance `V`,

```
Var(Amp) = TᵀWt V Wt T / (TᵀWt T)²
         = alpha² · TᵀV⁻¹ V V⁻¹ T / (TᵀWt T)²
         = alpha · (TᵀWt T) / (TᵀWt T)²
         = alpha / (TᵀWt T)
```

so the sampling standard deviation is `sqrt(alpha/(TᵀWt T))`, which is what §7
prescribes. The width at `Δχ² = 1` is `(TᵀWt T)^(−1/2)`, larger by
`alpha^(−1/2)`.

Checked numerically: over 4×10⁵ draws the empirical standard deviation of `Amp`
was 1.1363, against 1.1378 for `sqrt(alpha/(TᵀWt T))` and 1.1470 for the
Δχ²=1 width.

The sampling standard deviation is the right object for branches 3 and 4,
because those branches ask what happens if the true generating amplitude sits
one sampling error away from its estimate.

## 4. Stationary points and the constrained minimiser

With `T(μ) = Tu + μ·Tv`,

```
Chi2(μ) = cd − (ca + μ·cb)² / (cc + 2μ·ce + μ²·cf)
```

Differentiating and clearing the denominator, the stationarity condition
factors:

```
(ca + μ·cb) · [ (cb·cc − ca·ce) + μ·(cb·ce − ca·cf) ] = 0
```

**First factor.** `ca + μ·cb = 0` at `muzero = −ca/cb`. There the numerator of
the subtracted term vanishes, so `Chi2(muzero) = cd` — the global **maximum**,
not a minimum. It is also the point where `Amp` vanishes: the model predicts
zero at every μ there, so μ is unidentified in its neighbourhood. It is excluded
from the candidate set for `muhat` and reported separately as a diagnostic.

**Second factor.** `mu1 = (ca·ce − cb·cc)/(cb·ce − ca·cf)` is the global
minimum over ℝ.

**Why the candidate set is `{0, mumax} ∪ {mu1 if in range}`.** `Chi2` is smooth
on `[0, mumax]` with exactly one interior minimum candidate. If `mu1` lies in
the interval, the constrained minimum is at `mu1` or at an endpoint; if it does
not, the function is monotone on the interval and the minimum is at an endpoint.
Taking the smallest `Chi2` over that set is therefore exact.

Verified over 400 random configurations, 202 of them with `mu1` inside
`[0, 60]`: the candidate rule never returned a larger `Chi2` than a brute-force
scan at step 1e-4, and in five cases returned a smaller one because the scan
grid was too coarse.

(v4 wrote "evaluate at each root and at both endpoints and take the smallest"
without excluding out-of-interval roots, so a literal implementation could
return `mu1 < 0` as `muhat`.)

## 5. Why no statement is made about `μ > mumax`

`Q(μ)` does not increase monotonically toward its `μ → ∞` limit.

```
Chi2(∞) = cd − cb²/cf        (finite)
Chi2(muzero) = cd            (the global maximum)
```

So when `muzero > muhat`, `Q` rises from zero at `muhat` to a peak at `muzero`,
then falls to the plateau `cd − cb²/cf − Chi2(muhat)`. The plateau is not the
supremum of `Q`, and a threshold lying above the plateau can still be crossed —
twice — on the way to it.

Demonstrated on a synthetic configuration: peak `Q = 1.0386` at `muzero = 1.38`,
plateau `Q = 0.0944`; a threshold of 0.5665 sits above the plateau and is
nonetheless exceeded on `μ ∈ [1.08, 1.91]`, so the acceptance set is
disconnected.

Two consequences, both reflected in §10 of the specification:

1. No "no crossing at any μ" verdict is available from a plateau comparison.
2. `Q95(μ)` is never simulated above `mumax`, so nothing about `μ > mumax` is
   licensed by this computation at all. The specification therefore reports the
   accept/reject pattern over the calibrated range and stops there.

(v4 asserted that a plateau below `Q95` implied no crossing at any μ. That is
the largest single error the review found, because it gated a terminal verdict.)

## 6. The `SdMC` weights

The crossing solves `g(μ) = Qobs(μ) − Q95(μ) = 0`, interpolated linearly
between `μa` (where `ga ≤ 0`) and `μb` (where `gb > 0`):

```
L95 = μa + (μb − μa)·(−ga)/(gb − ga)
```

Write `wa = −ga/(gb − ga)` and `wb = 1 − wa`, the crossing fractions. Then

```
∂L95/∂ga = −(μb − μa)·gb/(gb − ga)²
∂L95/∂gb = +(μb − μa)·ga/(gb − ga)²
```

and with `slope = (gb − ga)/(μb − μa)`,

```
SdMC = sqrt( wb²·sd(ga)² + wa²·sd(gb)² ) / |slope|
```

The weights matter. Dropping them overstates `SdMC` by a factor between √2 and
2 — exactly 2 when the crossing sits mid-interval.

Checked numerically at `wa = 0.75`: direct Monte Carlo gave 0.002338, the
weighted formula 0.002306, the unweighted formula 0.004125.

(v3 propagated one node only and called a two-point secant a central difference.
v4 fixed the count and the naming and shipped the unweighted formula.)

`Qobs` is treated as exact in this propagation: it is a single deterministic
number given the data, whereas each `Q95` carries the Monte-Carlo error of its
own node.

## 7. The coverage band

The coverage statistic compares each validation dataset's `Q(mu_true)` against
`Q95(mu_true)`. Both sides are estimated:

- the fraction is a binomial proportion over `N_val = 200 000` draws;
- the threshold is a 0.95 quantile estimated from `N_cal = 100 000` draws, and
  its error feeds through the comparison at first order with the same
  `p(1−p)` scale.

So the standard deviation of `fraction − 0.95` is

```
sqrt( 0.95·0.05/N_val + 0.95·0.05/N_cal )
```

Numerically `sqrt(4.87e-4² + 6.89e-4²) = 8.44e-4`, against 4.87e-4 if the
threshold is treated as exact. A band of `3 × 4.87e-4` is therefore a 1.73σ
band, giving roughly 8% spurious failure per node and roughly 50% across eight
nodes. The specification uses the combined form.

The coverage study is generated at the same plug-in amplitude used for
calibration, so it checks the Neyman construction and the quantile estimator. It
does not check the plug-in treatment of the nuisance amplitude, and it does not
diagnose a limit that is tight because of a downward fluctuation — a
`CL_{s+b}` construction has correct coverage in exactly those runs. The
specification states the scope and makes no claim beyond it.

## 8. `r_lo` and the interpolant

The `ξ` table has its first two entries at 3.69 and 11.08 Mpc after conversion.
All eleven `r_lo` values used lie strictly between them. Every kernel integral
therefore begins inside an interval containing no measurement, and its lower
portion is determined by the §4 spline rather than by data.

The consequence is that `L95(r_lo)` measures the response of the procedure to
the interpolant and to the choice of support boundary. It is not a measured
dependence, and its range is not a data-derived uncertainty. No tightening of
the specification changes this; pinning the interpolant makes the curve
reproducible, not meaningful.

This is why §16 carries it as a standing scope statement rather than as an open
problem: it is a property of what is available, not a defect to be fixed.

**Open question, not decided here:** whether the `L95(r_lo)` curve should remain
the primary deliverable, be demoted to a labelled sensitivity study with a
conditional limit promoted, or whether the estimand should be reformulated so
that the quantity bounded is one the data actually support. The specification
currently takes the first option with honest labelling.

## 9. Stream derivation

The key is `(model_id, r_lo_id, j20, stage)`. It deliberately omits a branch
identifier so that every branch of §11 draws the same standard normals as the
primary at the same node: branch-minus-primary differences then reflect the
branch definition rather than independent Monte-Carlo noise. It includes a
stage field so that the coarse and refined passes at a coinciding μ are
independent samples rather than nested ones.

`j20 = round(μ/0.05)` is an integer for both the 0.1 coarse grid and the 0.05
refined grid.

The dual-unit run uses its own root sequence. Stream identity across the two
unit systems is not required and is not attempted: in converted units the μ
nodes are not at integer multiples of 0.05, so a shared key would not be
well-defined. The dual-unit comparison is therefore limited by Monte-Carlo
noise, which is why its threshold is 0.1% rather than machine precision.

(v4 required branches to share streams in one section and included `branch_id`
in the key in another, which are contradictory, and left the coarse and refined
stages sharing a key, which made the mandated re-simulation nested rather than
independent.)

## 10. What the controls do and do not establish

Control 1 verifies that `r_mp_over_h` and `r_mp` differ by the factor `hdata`.
It does not establish the absolute unit of `r_mp`: a global rescaling of both
arrays would pass. Nothing else in the control set anchors it either. The
specification therefore states explicitly that the absolute unit is not
established, rather than implying that control 1 covers it.

Control 2 compares the closed-form route for `Kraw2` against a numerical
integration that includes `G₂` explicitly with the step location as a
breakpoint. These are genuinely different computations, so the control can fail.

(v4's control 2 compared the prescribed expression against the same prescribed
expression and could not fail.)

Controls 3 and 4 are diagnostics with no threshold, and are marked as such. In
particular control 4 measures whether `df_cov` is the sample covariance of the
`bs_curves` rows — the premise under which the Hartlap factor is the correct
correction. It does not gate, because by §2 the factor cancels from every limit
reported; it matters only for the `[WEAK]`-marked p-value.

Control 8 compares `r_hi` and `rXiMin` against the file. Since §4 reads both
from the file rather than hard-coding them, this is an equality check on
float64 values rather than a tolerance on a rounded literal.

(v4 hard-coded `r_hi = 262.19` and demanded agreement to 1e-6 Mpc, a
nine-figure demand on a five-figure constant, which would have stopped the run.)

---

## Appendix — error log

Six claims that earlier versions asserted and that review found wrong. Recorded
because the pattern, not any individual item, is what changed the structure of
the specification.

| Version | Claim | Status | Found by |
|---|---|---|---|
| v2 | principal value applies to the whole of `G₃` | wrong — `Λ` is integrable | round-1 reader |
| v3 | the excised piece of `Λ` is a contribution surviving ε → 0 | wrong — it is `O(ε ln ε)` | round-2 reader |
| v3 | `{3.7, 4.2, …, 11.1}` with step 0.5 and both endpoints | arithmetically impossible | both round-2 readers |
| v4 | alpha survives only in the p-value and branch 1 | incomplete — `AmpSd ∝ alpha^(−1/2)` | both round-3 readers |
| v4 | `AmpSd = (TᵀWt T)^(−1/2)` is the amplitude's error | wrong object — Δχ²=1 width | round-3 reader |
| v4 | `SdMC = sqrt(sd_a² + sd_b²)/\|slope\|` | wrong — weights dropped | both round-3 readers |
| v4 | a plateau below `Q95` implies no crossing at any μ | wrong — `Q` peaks at `muzero` first | both round-3 readers |
| v4 | the candidate set gives the exact constrained minimiser | wrong — no clip to `[0, mumax]` | round-3 reader |
| v4 | three outcome labels | not a partition; the tight-limit case inverted | round-3 reader |

Every one of these lived in a passage where the specification was explaining or
justifying itself. Over the same three rounds, the prescriptive content —
kernels, units, grid, quadrature, the pole/logarithm split, the Hartlap
dimension, the closed form, the retention rule — accumulated zero confirmed
errors.
