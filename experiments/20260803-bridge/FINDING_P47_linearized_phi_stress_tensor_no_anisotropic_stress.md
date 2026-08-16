# P47 — φ's linearized stress-energy on FRW confirms the standard zero-anisotropic-stress property of canonical scalars — a consistency check, not a MULTING-specific discovery

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — three framing/calibration
issues found, zero math errors: an "independent positive control" that
was really a self-consistency check, "6 independent checks" that were
really one algebraic fact in six locations, and a "candidate real null
result" framing that oversold a standard textbook property as a
MULTING-specific discovery.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
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

## Part 2 — self-consistency check, ~~positive control~~ [CORRECTED: not independent]

**[CORRECTED after skeptic review]** The original text called this a
"positive control." Both this `T₀₀` and `FINDING_P34`'s own `ρ_φ` are
derivations of the *same* textbook quantity (a canonical scalar's
homogeneous energy density) from the same physical setup — a consistent
sign or factor error would spoil both symmetrically. This is a
**self-consistency check** (catches gross algebra slips), not
independent verification against external ground truth.

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
identically zero at linear order.** `δT_ij = a²φ̄̇δφ̇·δ_ij` exactly:
**purely isotropic.** `φ`'s linearized stress-energy sources **no
anisotropic stress at all** at linear cosmological perturbation order,
for a homogeneous background `φ̄(t)`.

**[CORRECTED after skeptic review]** The original text called the six
component checks above "six independent checks." The skeptic asked a
sharp question: does this result actually depend on `δφ`'s *spatial*
structure, or would a purely time-dependent `δφ(t)` (no `x,y,z`
dependence at all) give the identical answer? Computed directly:

```
δT₁₁ with a purely t-dependent δφ(t):  a²φ̄̇·d/dt[δφ(t)]   — same shape
```

**Same functional shape as the general-`δφ(t,x,y,z)` result** (script
assertion, comparing each case against its own hand-built target of the
`a²φ̄̇·δφ̇` shape, since sympy treats `δφ(t,x,y,z)` and `δφ(t)` as
different function objects). This confirms: the six assertions above
are **not** six facts about `δφ`'s spatial structure — they are *one*
algebraic fact (`φ̄`'s homogeneity kills every term involving a spatial
derivative of `δφ` at linear order) appearing in six syntactic
locations. Downgraded from "six independent checks" accordingly.

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

1. A direct, computed verification that `φ`'s linearized stress-energy
   tensor is exactly isotropic at linear cosmological perturbation
   order — not assumed from the static `FINDING_P38`/`FINDING_P40`
   result.
2. **[CORRECTED]** This is a **standard, textbook property** of any
   canonical minimally-coupled scalar on FRW — the quintessence
   literature routinely relies on exactly this, inherited from the
   choice of kinetic term, **not a MULTING-specific discovery.** This
   finding's actual value: it confirms this reconstruction's `φ`-sector,
   having a canonical kinetic term, has not accidentally introduced a
   non-canonical piece that would break the standard behavior — a
   **consistency check**, not a discovery.
3. A structural explanation (checked, not assumed) for *why*: the
   anisotropic-generating term is second-order in `δφ` for a
   homogeneous background, unlike the static point-source case.
4. If the (not-yet-derived) trace-free Einstein equation takes the
   standard quasi-static form, `φ`'s own contribution to its source
   vanishes, suggesting `Φ_φ,k=Ψ_φ,k` at linear cosmological order —
   structurally different from `FINDING_P38`/`FINDING_P40`'s nonzero
   **static** two-body slip (a genuinely different regime, not a
   tension). This conditional is hedged throughout, not dropped.

## What this does NOT establish

1. **`γ(a,k)`, `μ(a,k)`, or `Σ(a,k)` numerically or symbolically.** No
   Einstein equation is derived or solved here — only the source term
   that would enter one.
2. **That `Φ_φ,k=Ψ_φ,k` is confirmed.** This is a *candidate* conclusion
   contingent on the (not-yet-derived) quasi-static Einstein equation
   actually taking the assumed standard form on FRW.
3. **Anything about matter's own anisotropic stress.** Pressureless dust
   is typically taken to have none at linear order (standard assumption
   in ΛCDM perturbation theory), but this is not independently checked
   or derived here — only `φ`'s own contribution is addressed.
4. **A contradiction with `FINDING_P38`/`FINDING_P40`'s static result.**
   Genuinely different physical regimes — both can be simultaneously
   true; no tension to resolve.
5. **The result at second or higher order in `δφ`.** The `ε²` term
   (which does contain `∂_iδφ∂_jδφ`, genuinely anisotropic) is
   identified but not computed.
6. **[CORRECTED, added]** **That `δφ`'s spatial structure was tested by
   the six per-component checks.** It was not — the result is unchanged
   for a purely time-dependent `δφ(t)`, verified directly.
7. **[CORRECTED, added]** **That this is a novel, MULTING-specific
   result.** It is the standard behavior of any canonical scalar on FRW;
   the same computation on plain quintessence would give the same answer.
8. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
9. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Stress tensor formula, sign conventions | **CONFIRMED** | No change. |
| Part 2 ("positive control") | **WEAKENED** — same textbook quantity derived twice, not independent | **Fixed** — relabeled self-consistency check. |
| Part 3/4 linearization math | **CONFIRMED** | No change — all 6 assertions verified correct by independent hand re-derivation. |
| "6 independent checks" framing | **WEAKENED** — result doesn't depend on `δφ`'s spatial structure at all | **Fixed.** Independently re-verified the sharp claim (result unchanged for `δφ(t)` alone) before accepting — matches exactly. New check added to the script and this doc. |
| "Candidate real null result" framing | **WEAKENED** — standard textbook property of canonical scalars, not MULTING-specific | **Fixed.** Reframed throughout as a consistency check confirming the reconstruction inherits standard behavior, per the skeptic's own suggested "bulletproof" framing. |
| Conditional hedging on `Φ_φ,k=Ψ_φ,k` | **CONFIRMED** — hedged consistently throughout, never dropped | No change. |
| Scope-gap list | **WEAKENED** — missing the three items above | **Fixed** — items 6–7 added. |

**The math survived entirely** — every skeptic-caught issue was a
framing or calibration question, not a computational error, independently
re-verified before any correction was accepted.

## Reproduction

```bash
python experiments/20260803-bridge/P47_linearized_phi_stress_tensor_no_anisotropic_stress.py
```
