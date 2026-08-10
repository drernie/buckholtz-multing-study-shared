# Carrying ℓ_q² = 2ℓ_d² to a test: three separate answers, none of them "confirmed"

**Date:** 2026-08-10 · closes the "next step" left open by
`FINDING_R7_collapses_to_one_action.md` §6
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Scripts:** `ksz_test_lq2_eq_2ld2.py` (this folder), symbolic work inline below

The instruction was to take `ℓ_q² = 2ℓ_d²` from a structural statement to a test.
It now is testable — the missing link, a derivation from the theory's own fitted
parameters to `ℓ_d, ℓ_q`, is supplied in §2. But the test does not return a
verdict on the prediction, for three independent reasons found at three different
levels. Each is recorded separately, because collapsing them into "inconclusive"
would lose the part that matters.

---

## 1. The prediction is weaker than it was labelled — it is a choice, not a consequence

`FINDING_R7...` presented `ℓ_q² = 2ℓ_d²` as a sharp falsifiable prediction with no
freedom left after `ε = ℓ_d`. That is true *of the specific action written down*
and not of the class it belongs to.

Take the general field-dependent-kinetic Lagrangian `L = ½ f(Φ) (dΦ/dr)²`, with
`f(Φ) = 1 + f₁Φ + f₂Φ² + f₃Φ³ + …`, canonicalise (`dχ/dΦ = √f`), impose the same
harmonic `χ = 1/r`, and match to `−U/A₂ = 1/r − ℓ_d/(2r²) + ℓ_q²/(3r³) − ℓ₅³/(4r⁴)`.
Solving order by order (`sympy`, series inversion):

```
ell_d   = f1/2
ell_q^2 = f1^2/2 - f2/2        =  2*ell_d^2 - f2/2
ell_5^3 = 7*f1^3/12 - 13*f1*f2/12 + f3/2
```

The R7 action is the `f₂ = f₃ = 0` member, and reproduces the earlier results
exactly (`ℓ_q² = 2ℓ_d²`, `ℓ₅³ = 14ℓ_d³/3`) — an independent confirmation of that
algebra. But the general relation is

> **ℓ_q² = 2ℓ_d² − f₂/2**

and each successive order introduces exactly one new `f_n`, each solvable for that
`f_n` given the corresponding `ℓ`. The class therefore carries **exactly as many
free parameters as MULTING has `A_n` coefficients**. It re-parametrises the force
law; it does not constrain it.

**Consequence.** `ℓ_q² = 2ℓ_d²` is the prediction of *minimality* — a linear
kinetic function — not of covariant completion. Measuring `ℓ_q/ℓ_d` does not test
the framework; it **measures `f₂`**. Status downgraded from *sharp falsifiable
prediction* to *definition of the minimal member*. Promoting it back would require
an independent principle forcing `f₂ = 0`, which nothing in the corpus supplies.

## 2. The missing map from β to ℓ, now derived

`FINDING_R7...` deliberately declined this, correctly, on Gate 1 grounds. It is
short. From the prompt TJB gave the AI services
(`data/beta1_responses/prompt_v1.md:44`, verbatim: *"use the formulas
r_dA = β_d r_A, r_dP = β_d r_P, and |r_qAB|² = (β_q)² r_A r_P"*) together with the
preprint's `F_d`, `F_q`, dividing by `G m_P` and writing `u_i ≡ k_i r_i /(c² m_i)`
(a length):

```
ell_d   = A3/A2 = beta_d (u_A + u_P)
ell_q^2 = A4/A2 = beta_q^2  u_A u_P
```

so `ℓ_q²/ℓ_d² = (β_q/β_d)² · u_A u_P/(u_A+u_P)²`. The cluster properties **cancel
exactly** when the two objects are alike, and the implemented `phi`
(`scripts/t4_monopole_dominance.py`) uses one cluster for both, so:

> **R7 ⇒ β_q = 2√2 β_d = 2.8284 β_d** — a pure number, no astrophysics.

| | value |
|---|---|
| Table A1 (AI-fitted) `β_q/β_d = 18.0/4.5` | **4.0000** |
| R7 prediction | **2.8284** |
| discrepancy | **exactly √2** (verified to machine precision) |
| implied | `ℓ_q² = 4ℓ_d²` ⇒ `f₂ = −4ℓ_d² = −f₁²` |

**This is not a falsification, and must not be recorded as one.** Those β values
were *fitted* by an online AI service to the observed `H(z)` — the prompt says so
in its own words — so using them as a validation target would test the fitting
procedure, not the theory (Gate 2, Target Provenance). Nor is `f₂ = −f₁²` a
recognisable closed form, so neither ratio is privileged by the shape of `f`.

For unlike objects the prediction relaxes to an inequality, `β_q ≥ 2√2 β_d`
(saturated iff `u_A = u_P`), which the observed 4.0 satisfies; consistency would
need `u_A/u_P = 3+2√2 ≈ 5.83`. That escape is closed for the implemented `phi`,
which forces `u_A = u_P`.

## 3. At those β values the terms being tested are physically inert

With `u = (E_thermal/c²/M₅₀₀)·R₅₀₀` measured on the project's own 548 clusters
(`data/clusters_clean.csv`): median `u = 1.75×10⁻⁶ Mpc`, so at `β_d = 4.5`,
`ℓ_d ≈ 1.6×10⁻⁵ Mpc`. Against intercluster `D ~ 40 Mpc`:

```
dipole / monopole      ~  ell_d/D    ~ 4e-7
quadrupole / monopole  ~  ell_q^2/D^2 ~ 1e-13
```

Whatever the AI's fit of `β_d = 4.5, β_q = 18.0` was doing, it was not doing it
through these terms. This is independently consistent with this project's earlier
monopole-dominance result and with the B0 finding that Table A1 is AI output.

## 4. The independent test cannot be run — and why that is itself the finding

The pairwise-kSZ likelihood (`experiments/20260802-ksz-force-law`) constrains
`ℓ_d = A3/A2` and `ℓ_q2 = A4/A2` **directly from data**, independent of `H(z)` and
of any β conversion, and it already builds the `K₄` kernel. It never scanned it —
every fit there was one-dimensional with `ℓ_q2 ≡ 0`. Adding the second dimension
is one grid. Doing so returns `NaN` everywhere, and the reason is not a bug:

```
POSITIVE CONTROL  C_2(rho) == 1 (shell theorem), regulator-independent:
  eps=1e-6 / 1e-9 / 1e-12 : max|C_2 - 1| = 3.75e-11 in every case   PASS

K_k at r = 95 Mpc:
  k   eps=1e-6      eps=1e-9      eps=1e-12
  2   1.35666e+00   1.35666e+00   1.35666e+00     stable
  3   2.57377e-02   2.57505e-02   inf             regulator-dependent
  4   5.89082e-03   inf           inf             divergent

grid refinement at eps=1e-9 (n_node 120 -> 480):
  k=2  ratio 1.001      converged
  k=3  ratio 1.106      NOT converged, grows with resolution
  k=4  inf              divergent
```

The control passing at *every* regulator is what makes this a physics statement
rather than a coding one: the geometry is right, so the divergences are real.
`C_k(ρ)` — the force of a shell of radius `r'` at a field point at radius `r`,
relative to a point mass — behaves as `ρ→1` like

| force power | `C_k(ρ→1)` | shell integral |
|---|---|---|
| `1/r²` | `→ 1` (shell theorem) | finite |
| `1/r³` | `~ (1−ρ)⁻¹` | log-divergent |
| `1/r⁴` | `~ (1−ρ)⁻²` | power-divergent |

**MULTING's higher-multipole force terms, summed over a continuous matter
distribution, are not defined without a short-distance regulator, and the
published force law supplies none.** The existing `ℓ_d` constraint is finite only
because `c_shell` clamps `ρ ≤ 1 − 10⁻⁹`; that clamp is an arbitrary number, and
`K₃` moves 10.6 % under a 4× grid refinement. Per FL Step 2a this is
`BLOCKED-INFRASTRUCTURE` for the `ℓ_q²` test and `UNTRUSTED-ENVIRONMENT` for the
`ℓ_d` result already on record — **neither is evidence about the R7 prediction, and
neither may be recorded as such.**

### The diagnosis, which partly rehabilitates the covariant completion

The divergence comes from summing pairwise `1/r³` and `1/r⁴` forces over a
continuum — i.e. from assuming **linear superposition**. The covariant completion
is nonlinear precisely in the kinetic sector, so superposition does not hold in
it; there `Φ` solves one field equation sourced by `ρ`, the multipole terms are
the Taylor series of that single exact solution rather than separate forces to be
added, and no shell integral appears anywhere.

So the completion makes no numerical prediction (§1), but it **removes a genuine
pathology of the pairwise-force formulation**. That is a structural result and a
better reason to pursue it than `ℓ_q² = 2ℓ_d²` ever was.

---

## Verdict

```
ell_q^2 = 2 ell_d^2 as a prediction : DOWNGRADED -- it is the f2 = 0 member of a
                                      class with one free parameter per order,
                                      not a consequence of covariant completion
beta -> ell map                     : DERIVED, [VERIFIED] against the prompt's own
                                      formulas; beta_q = 2*sqrt(2)*beta_d
Test vs Table A1 beta values        : NOT PERFORMED AS A TEST (Gate 2: fitted
                                      target). Recorded as a consistency note:
                                      observed 4.0 vs predicted 2.83, factor sqrt(2)
Test vs pairwise kSZ (independent)  : BLOCKED-INFRASTRUCTURE -- K_4 divergent,
                                      K_3 non-convergent; control passes, so the
                                      divergence is physical, not numerical
Existing kSZ ell_d constraint       : UNTRUSTED-ENVIRONMENT -- regulator-dependent
New structural result               : MULTING's 1/r^3, 1/r^4 terms over a continuum
                                      need a short-distance regulator the published
                                      law does not supply; the nonlinear field
                                      formulation does not have this problem
```

## What would unblock each

1. **§1** — an independent principle fixing `f₂ = 0` (a symmetry, or a derivation
   of `f` from the Lorentz-invariance argument MULTING starts from). Without it,
   `ℓ_q/ℓ_d` is a measurement of `f₂`, not a test.
2. **§4** — solve the field equation for the actual matter distribution instead of
   superposing pairwise forces. This is not a patch to `c_shell`; it is the
   nonlinear calculation, and it is the same missing object as G3/Q006.
3. Only after 2 does an independent `ℓ_q²` constraint exist at all.

## Incidental findings, both verified, neither in scope here

- `n = 548`, flagged `[PROVENANCE UNRESOLVED]` in `paper/main.tex`, is resolved:
  `data/pearson_r_test_results.md` — clusters with `E_thermal/c²` (Path B `Y_SZ`),
  `z = 0.011–0.888`, from MCXC-I ∩ PSZ2.
- `scripts/t4_monopole_dominance.py:123` uses `(k*r)**2 / D**4` for the quadrupole
  term of `phi`. The preprint's `F_q/(G m_P)` gives `k² r²/(m D⁴)` for a single
  object — a factor `1/M₅₀₀` is missing, and the three terms of `phi` as coded are
  not dimensionally homogeneous. Since `M₅₀₀` varies cluster to cluster this is not
  absorbed by the `phi/phi_ref` normalisation and does affect the reported Pearson
  `r`. Flagged, not fixed here.
