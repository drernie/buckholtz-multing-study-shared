# P47 — φ's linearized stress-energy on FRW sources zero anisotropic stress at linear order — a candidate real null result, structurally different from P38/P40's static slip

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** second of two steps toward the campaign's original `P36`
row (`PLAN_final_goal_20260814.md`). `FINDING_P46` solved the
field-equation side (`δφ_k`); this handles the source side.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P47_linearized_phi_stress_tensor_no_anisotropic_stress.py`,
ruff clean, all assertions pass.

## 0. Scope, deliberately narrowed before writing any code

The original plan for this step was "derive the perturbed Einstein
equations and assemble `γ(a,k)`." Before writing anything, I re-read
`FINDING_P38`'s own method (a full symbolic linearized Christoffel →
Ricci → Einstein tensor calculation, built for a **flat Minkowski**
background) and found that extending it correctly to an **FRW**
background — where the background Christoffels are already nonzero
(order `H`), not zero as in P38's case — is a genuinely much larger
derivation than anything attempted in this campaign so far. Given this
whole area's demonstrated fragility (`P36`'s own worst-correction
history; `FINDING_P46`'s own two rounds of correction, both in this
exact category of step), attempting that full derivation in one step
was not the responsible move. **Split off as a later, not-yet-started
step.** This finding instead handles the source side only: linearizing
`φ`'s own stress-energy tensor around a homogeneous FRW background.

## Part 1 — covariant `T_μν(φ)` on FRW

`FINDING_P37`'s own formula, extended from flat `η_μν` to the FRW
metric (`g₀₀=−1`, `g_ii=a²`, diagonal):

```
T_μν = ∂_μφ∂_νφ − (1/2)g_μν(∂φ)²,   (∂φ)² = −φ̇² + (∇φ)²/a²
```

## Part 2 — positive control

Background (`φ=φ̄(t)`, `ε=0`):

```
T₀₀ = φ̄̇²/2
```

**Matches `FINDING_P34`'s own `ρ_φ=φ̄̇²/2` exactly** (script assertion).

## Part 3 — linearize in `ε` (same method as `P44`/`P46`)

Split `φ=φ̄(t)+εδφ(t,x)`, take `d/dε` at `ε=0`:

```
δT₀₀ = φ̄̇δφ̇
δT₁₁ = δT₂₂ = δT₃₃ = a²φ̄̇δφ̇   (all three, verified equal — script assertion)
δT_xy = δT_xz = δT_yz = 0    (all three off-diagonal — script assertion)
```

## Part 4 — the traceless (anisotropic-stress) part, assembled explicitly

```
δT_ii (trace) = 3a²φ̄̇δφ̇
[δT_ii]_tracefree = 0   (all 3 components — script assertion)
```

**All 3 traceless-diagonal and all 3 off-diagonal components are
identically zero at linear order** — six independent checks, not one.
`δT_ij = a²φ̄̇δφ̇·δ_ij` exactly: **purely isotropic.** `φ`'s linearized
stress-energy sources **no anisotropic stress at all** at linear
cosmological perturbation order, for a homogeneous background `φ̄(t)`.

## Part 5 — why, checked not assumed

The anisotropic-stress-generating piece of `T_ij` is `∂_iφ∂_jφ` —
`FINDING_P38`'s static slip came from exactly this term (`~x_ix_j/r⁴`,
a genuine angular/`l=2` structure for a spatially-varying point-source
profile). For `φ=φ̄(t)+εδφ(t,x)`: `∂_iφ=ε∂_iδφ` (since `∂_iφ̄=0` by
homogeneity) — so `∂_iφ∂_jφ=ε²∂_iδφ∂_jδφ`, **second order** in `ε`. It
contributes nothing at first order — confirmed directly in Part 3/4,
not assumed from this structural argument alone (the structural
argument explains *why*, the computation *confirms* it).

## What this establishes, precisely

1. A component-by-component (6-way), computed verification that `φ`'s
   linearized stress-energy tensor is exactly isotropic at linear
   cosmological perturbation order — not assumed from the static
   `FINDING_P38`/`FINDING_P40` result, not cited from a textbook.
2. A structural explanation (checked, not assumed) for *why*: the
   anisotropic-generating term is second-order in `δφ` for a
   homogeneous background, unlike the static point-source case.
3. A candidate real null result, in the exact sense the campaign's own
   governing plan names as valid (its original `P36` row: *"if the
   quasi-static `μ,γ` come out exactly `Q=1,R=1`... document and stop
   this branch, do not force a distinguishing claim"*): if the
   trace-free Einstein equation takes the standard quasi-static form
   (not derived here), `φ`'s own contribution to its source vanishes,
   suggesting `Φ_φ,k=Ψ_φ,k` at linear cosmological order — structurally
   different from `FINDING_P38`/`FINDING_P40`'s nonzero **static**
   two-body slip.

## What this does NOT establish

1. **`γ(a,k)`, `μ(a,k)`, or `Σ(a,k)` numerically or symbolically.** No
   Einstein equation is derived or solved here — only the source term
   that would enter one.
2. **That `Φ_φ,k=Ψ_φ,k` is confirmed.** This is a *candidate* conclusion
   contingent on the (not-yet-derived) quasi-static Einstein equation
   actually taking the assumed standard form on FRW. That derivation is
   flagged as future work (§0), not attempted here.
3. **Anything about matter's own anisotropic stress.** Pressureless dust
   is typically taken to have none at linear order (standard assumption
   in ΛCDM perturbation theory), but this is not independently checked
   or derived here — only `φ`'s own contribution is addressed.
4. **A contradiction with `FINDING_P38`/`FINDING_P40`'s static result.**
   The two findings address genuinely different physical regimes
   (static two-body point-source vs. homogeneous-background linear
   cosmological perturbation) — both can be simultaneously true; there
   is no tension to resolve.
5. **The result at second or higher order in `δφ`.** Only linear order
   is addressed; the `ε²` term (which does contain `∂_iδφ∂_jδφ`, genuinely
   anisotropic) is explicitly identified but not computed.
6. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P47_linearized_phi_stress_tensor_no_anisotropic_stress.py
```
