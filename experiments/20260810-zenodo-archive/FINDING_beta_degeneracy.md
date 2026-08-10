# The F1/F2 cancellation is extreme, and the fit is stable anyway — because β₁ and β₂ are degenerate

**Date:** 2026-08-10 · **Stage:** reproduction of Zenodo 10.5281/zenodo.21204955
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## Summary

Reproducing the archive shows the net specific force is a small residue of two
much larger, nearly-cancelling terms. At z = 0.07 the dipole and quadrupole
terms cancel to **99.1 %**, so a 1 % error in either would change the net by a
factor of two. That invites the obvious referee objection: *a result built as
the difference of two large numbers is fragile.*

**Measured, that objection does not hold.** The published fit is stable under
perturbation — but not for the reason a reader might assume. It is stable
because β₁ and β₂ are strongly degenerate: the data constrain essentially one
combination of them, and a perturbation in one is absorbed almost exactly by
the other.

The same measurement carries a second, separate consequence, in the opposite
direction: because only the combination is constrained, the **individual** β
values are far less determined than their five quoted significant figures
suggest.

Both consequences follow from one calculation and neither should be reported
without the other.

---

## Two questions that are easy to conflate

| | Question | Answer |
|---|---|---|
| **A. Structural** | Perturb one β, hold the other. How much does the net move? | Amplification 8.8×–111.6× |
| **B. Effective** | Perturb one β and let the fit re-optimise the other, which is what a fit actually does. How much does χ² move? | Δχ² ≤ 0.2 for a 5 % move |

Reporting A alone overstates fragility. Reporting B alone hides the
conditioning. The numbers below give both.

---

## What the numbers show

All computed with the archive's own `multing_core.py` and its own χ²
(33 points: 31 cosmic chronometers + SH0ES + DESI, diagonal errors),
unmodified. The published χ²₃₃ = 15.78 was reproduced as an anchor
before any perturbation. `[VERIFIED-BASH]`

### A. The cancellation, in units of |net|

| z | F₀ | −F₁ | F₂ | −F_acc | net | amplification |
|---|---|---|---|---|---|---|
| 1.965 | −0.010 | +8.796 | −7.716 | −0.071 | 1.000 | 8.8× |
| 1.070 | −0.009 | +8.657 | −7.589 | −0.059 | 1.000 | 8.7× |
| 0.500 | −0.013 | +12.069 | −10.981 | −0.075 | 1.000 | 12.1× |
| **0.070** | −0.106 | **+111.444** | **−111.643** | −0.694 | −1.000 | **111.6×** |
| 0.000 | −0.026 | +27.758 | −28.557 | −0.175 | −1.000 | 27.8× |

Note also that F₀ — the ordinary Newtonian monopole — contributes **1 % or
less** of the net at every z sampled.

### B. One-at-a-time: β₂ held fixed

| δβ₁ | χ²₃₃ | Δχ² |
|---|---|---|
| ±0.2 % | 16.4 | +0.6 |
| ±1 % | 31.1–32.7 | **+15.3 … +16.9** |
| ±5 % | 348–541 | +333 … +525 |

### C. Effective: β₂ re-optimised

| δβ₁ | β₂ refit | Δχ² |
|---|---|---|
| ±0.2 % | ∓0.23 % | **+0.000** |
| ±1 % | ±1.11 % | **+0.008** |
| ±5 % | ±5.58 % | **+0.197** |

### D. Conditioning of the two-parameter fit

```
across the valley (β₂ held)    : Δχ² = 1 at  0.249 % move in β₁
along  the valley (β₂ refit)   : Δχ² = 1 at 11.30  % move in β₁
anisotropy                     : 45×
degeneracy direction           : δβ₂ = +1.116 · δβ₁
```

### E. Does the H(z) curve survive?

A 1 % shift in β₁ with β₂ re-fitted moves H(z) by **less than 0.25 %** across
0 ≤ z ≤ 2.33, against observational uncertainties of order a few per cent.

---

## Correction, 2026-08-10 — the answer depends on which quantity is measured

An external reading of the same archive reported that a 1 % shift in β₁ moves
z_min by ±0.03 — an order of magnitude more fragile than anything in section E
above. Both results are right; they measure different things, and the
difference is the point.

E measures H(z), a **value**. z_min is a **zero of the derivative**. In a flat
region a derivative's root can wander while the function barely moves, so
stability of H(z) does not transfer to stability of z_min.

Measured directly on the same fit `[VERIFIED-BASH]`:

| δβ₁ | z_min, β₂ held | z_min, β₂ refitted |
|---|---|---|
| −1 % | 0.12789 (+0.0316) | 0.09293 (−0.0034) |
| +1 % | 0.06710 (−0.0292) | 0.09947 (+0.0032) |
| ±5 % | — | ∓0.016 |

Re-fitting stabilises z_min by roughly 10×, so the without-refit figure
overstates the fragility. But even fully refitted, z_min moves **3.3 % relative
— that is Δz_min = ±0.0032, on a base of z_min = 0.0963** — for a 1 % move in
β₁, against **< 0.25 %** for H(z). The derivative feature is about 13× more
sensitive than the function.

Both numbers are quoted deliberately. A percentage on a quantity near 0.1 reads
more dramatically than the shift is: ±0.003 in redshift is small in absolute
terms, and whether it matters depends on what resolution the claim "a turning
point near z ≈ 0.1" is asserted at. The 13× ratio is the transferable statement;
the 3.3 % is scale-dependent and should never travel without its absolute
companion.

Why the derivative is the fragile one, structurally: at an extremum
`H'(z*) = 0`, so a perturbation shifts the root by roughly
`δz* ≈ −δH'(z*) / H''(z*)`. The minimum here is shallow, `|H''|` is small, and a
small numerator over a small denominator moves the root while leaving the
function almost unchanged. Since the paper's headline feature *is* the minimum,
this is the number that carries the claim — and inputs such as T₀ are known far
worse than 1 %.

Independent cross-check: the external reading obtained z_min = 0.0963 for the
H₀ = 73.04 row; this work obtains 0.09631 for the same row. Two implementations
agree to five decimals. (Its quoted 0.0988 is the H₀ = 73.22 spotlighted row —
a different configuration, not a discrepancy.)

---

## Consequences

**1. The fragility objection is answered — within a stated boundary.**
What is excluded is fragility to perturbations **inside the fitted β-manifold**:
the near-cancellation does not by itself make the H(z) fit unstable, because
the fit moves along a degenerate valley. What is **not** excluded is fragility
to changes in the physical inputs (T₀, M₀, d₀, the scaling exponents, the
ΛCDM-conditioned E(z)) or in the form of the force law — none of those were
perturbed here. Nor does it extend to derivative features: see the correction
above. A referee raising "difference of large numbers" can be answered with C
and E; a referee asking "is z ≈ 0.1 a sharp prediction?" cannot.

**2. The β values are quoted more precisely than the data determine them.**
`assumptions.yaml` lists β₁ = 1.4233e+10 and β₂ = 7.7443e+17 to five
significant figures. The fit determines the combination roughly 45× better
than either value alone: β₁ can move ±11 % along the degeneracy direction for
Δχ² = 1. Stating the constrained combination (δβ₂ ≈ 1.116 δβ₁) alongside the
point values would represent the constraint honestly. This is a question of
how the numbers are reported, not of whether they are right.

**3. A naive finite-difference Hessian is unreliable here — at this step size
and integrator precision.** A plain central-difference Hessian at the optimum
returned a **negative eigenvalue (−3.5)**, impossible at a minimum: the valley
is flat enough that curvature along it falls below the integrator/interpolation
noise floor at a 0.2 % step. This is a diagnostic failure of that particular
estimator, **not** a claim that Hessian-based covariance is impossible here —
automatic differentiation, tighter integration tolerances, Richardson
extrapolation or analytic derivatives could each recover a valid curvature
matrix. The workaround used here (quadratic fit to the χ² profile along each
direction) is noise-tolerant and is what produced D. The practical warning
stands: anyone using default finite differences risks a non-positive-definite
covariance and may misread it as "the fit did not converge".

**Coordinates matter for D.** The slope 1.116 is in *fractional* perturbations,
equivalently d ln β₂ / d ln β₁ — it is not the slope in the (β₁, β₂) plane. The
45× is a ratio of χ²-profile widths, which need not equal the axis ratio of a
posterior: priors, valley curvature and non-Gaussianity all change it.

---

## Scope

This measures the numerical conditioning of one published fit. It says nothing
about whether MULTING is correct, nothing about the physical interpretation of
β₁ and β₂, and nothing about the model comparison against ΛCDM. It does not
address the archive's own separately-disclosed open items (the T₀ recalibration
tension, the self-referential d₀, the "not independently data-grounded" M₀).

The near-cancellation itself is reported here as a measured property, not as a
criticism: a small residue of large opposing terms is a normal situation in
physics (it is how, for example, binding energies work). What matters is
whether it is disclosed and whether the fit is conditioned — the first is now
measured, the second is answered in the affirmative.

---

## Artifacts

- `sensitivity_f1f2.py` — this folder; runs against the archive's `code/`
  directory unmodified, reproduces χ²₃₃ = 15.78 as an anchor first
- Source archive: Zenodo 10.5281/zenodo.21204955, inner file
  `zenodo_archive_v17.zip`, MD5 `9cc38e1b5a4ac6286b635910acf0f5c2` — verified
  byte-for-byte against the published checksum before any analysis

## Related

- `REPRODUCTION_RECORD.md` (this folder) — the full reproduction result
- `experiments/20260803-bridge/FINDING_table_a1_provenance.md` — B0, the
  finding this archive supersedes by moving to real observational data
