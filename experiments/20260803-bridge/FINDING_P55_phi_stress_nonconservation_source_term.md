# P55 — Step B2, Part 1: the matter source term `Q⁰ = -ĝ(δρφ̄̇+ρ̄δφ̇)`, derived from φ's own stress non-conservation, not inserted by hand — restricted to P46/P47's own established (Φ=Ψ=0) scope

**Date:** 2026-08-17
**Status:** Built, run, ruff clean, all assertions pass, after a substantial
in-build self-debugging cycle (see below — three real issues caught and
fixed BEFORE any skeptic review, kept visible rather than silently
patched). **Skeptic review (Step 8a): COMPLETE. Not a true kill — the
central `Q⁰` result and every symbolic-computation claim independently
confirmed by the skeptic's own from-scratch hand-derivation. One framing
overclaim found and fixed: "total conservation" is a closure condition
this file's own matter-sector split requires, not an automatic
consequence of diffeomorphism invariance. See Skeptic Verdict below.**
**Origin:** first sub-step of B2 in the user's refined "Euler/`G_matter`"
milestone. User's own equation: `∇_μT_m^μν=Q^ν`. This file derives `Q^ν`
(the `ν=0` component) from `φ`'s own stress-energy non-conservation — a
general covariant identity, not a force inserted by hand or by analogy
(KG-B2a, the user's own kill-gate).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P55_phi_stress_nonconservation_source_term.py`, ruff clean,
all assertions pass.

## Scope, stated up front

Derives `Q⁰` **only**, and only within `FINDING_P46`/`P47`'s own
established metric scope (unperturbed FRW, `Φ=Ψ=0` — only `φ` itself is
perturbed, not the metric). Does **not** yet assemble the linearized
matter continuity/Euler equations from `T_m^μν=ρu^μu^ν` (B2 Part 2,
separate, not-yet-started). Does **not** attempt the B1↔B2 compatibility
check. Does **not** extend `φ`'s own field equation to the `Φ,Ψ`-perturbed
metric.

## In-build self-debugging cycle (found and fixed before any skeptic review)

Kept visible per this campaign's "no silent fixes" discipline — three
distinct issues, found in sequence, each independently diagnosed and
fixed before moving to the next:

**1. Scope mismatch (a real methodological catch, not a code bug).** The
first version combined the **full** (`Φ,Ψ`-perturbed) metric machinery
from `FINDING_P48`/`P54` with `FINDING_P46`'s field equation, which was
derived — per `FINDING_P46`'s own docstring — "via Euler-Lagrange on the
full Lagrangian density... `g^{ij}=δ^{ij}/a²`" — the **unperturbed** FRW
metric. Combining a `Φ,Ψ`-inclusive covariant divergence with a
`Φ=Ψ=0`-derived field equation is exactly the "silently mix conventions"
trap the user's own KG-B2b warns about, in a new guise. Caught by this
script's **own** positive control (the general identity, which must hold
for *any* field equation, failed at linear order) — a real, non-vacuous
check. Fixed by restricting this finding's own metric to the same
`Φ=Ψ=0` scope `FINDING_P46`/`P47` already used.

**2. A hand-typed `box(φ)` formula, not computed from the same Christoffel
data.** Even after restricting scope, the identity still failed. The
`box(φ)` formula used for the identity's RHS had been hand-typed (by
analogy to `FINDING_P46`'s own printed formula) rather than computed via
the *same* `Γ` array feeding the covariant-divergence code — an
internal-consistency gap, not a physics error (independently
hand-verified beforehand: `∇_μT_φ^{μν}=(□φ)∂^νφ` is exactly true in
general). Fixed by adding `covariant_box()`, computing `□φ` from the same
`Γ` array as `covariant_div_upper()`, guaranteeing consistency by
construction.

**3. A sign-convention bookkeeping error.** After fixing (2), an assertion
comparing `covariant_box()`'s output to a hand-written "expected" form
still failed — because the hand-written expectation had the wrong overall
sign relative to `FINDING_P46`'s own actual convention (`FINDING_P46`'s
own script logic: `-box_phi - target_form.subs(rho,0) == 0` implies
`box_phi=-(φ̄̈+3Hφ̄̇)` on the source-free piece — an overall minus sign the
first draft's assertion omitted). Separately, the identity-check line
itself had accidentally absorbed a minus sign that belongs to a *later*
step (`Q^ν=-∇_μT_φ^{μν}`, from total conservation) into the *pure*
identity check, where no such sign belongs. Both fixed by re-deriving the
correct sign directly from `FINDING_P46`'s own script text, not by
guessing.

## Part 1–2 — machinery, reused

Metric: `g_00=-1, g_ii=a²` (matches `FINDING_P46`/`P47` exactly).
Christoffels: `christoffels_exact`, reused verbatim from `FINDING_P48`/`P54`.
`T^{μν}(φ)`: `FINDING_P47`'s own structural formula
(`∂^μφ∂^νφ-(1/2)g^{μν}(∂φ)²`), both indices raised with this metric's
inverse.

## Part 3 — positive control: the general identity on the background

```
□φ|_bg = -(φ̄̈+3Hφ̄̇)         (script assertion, matches FINDING_P46's own sign)
∇_μT_φ^{μ,0}|_bg = □φ|_bg · ∂^0φ|_bg     (script assertion, exact match)
```

**Confirmed.** This identity holds for *any* scalar field with the stated
`T_μν`, regardless of its equation of motion — a pure consequence of
metric compatibility (`∇g=0`). Verifying it directly, before trusting it
at linear order, caught issues 2 and 3 above.

## Part 4 — linear order, and `Q⁰` extraction

```
[□φ]^(1) matches -1 × FINDING_P46's own printed linear field-equation form   (script assertion)
[∇_μT_φ^{μ,0}]^(1) = [□φ]^(1)·∂^0φ|^(1)   (script assertion, exact match)
```

**Confirmed** at linear order too. Substituting `FINDING_P46`'s own actual
field equation `□φ=-ĝρ` (reused, not re-derived):

```
[∇_μT_φ^{μ,0}]^(1) = ĝ(δρ·φ̄̇+ρ̄·δφ̇)
Q⁰ := -[∇_μT_φ^{μ,0}]^(1)  (total conservation)  =  -ĝ(δρ·φ̄̇+ρ̄·δφ̇)
```

## Verdict [CORRECTED after context-blind skeptic review, Step 8a]

The general covariant identity `∇_μT_φ^{μν}=(□φ)∂^νφ` is confirmed by
direct symbolic computation, both on the background and at linear order,
on `FINDING_P46`/`P47`'s own established (`Φ=Ψ=0`) scope. Substituting
`FINDING_P46`'s own field equation gives the actual `ν=0` component of
`φ`'s stress non-conservation at linear order.

~~...and hence, via total stress-energy conservation, the matter-sector
source term `Q⁰=-ĝ(δρφ̄̇+ρ̄δφ̇)`, within this same scope.~~

**`Q⁰:=-[that quantity]` *is* the matter-sector source term IF total
stress-energy conservation holds** — independently re-derived (before
accepting the skeptic's critique) that this is **not** automatic from
diffeomorphism invariance alone in `FINDING_P46`'s own setup, which
treats `ρ` as an **external** scalar, not a fully dynamical dust field:
varying only the coupling term `ρ(1-ĝφ)` with respect to `g^μν`, holding
`ρ` fixed, leaves a residual `-(1-ĝφ)∂^νρ` that does not cancel unless
`ρ` separately satisfies its own conservation law. **Total conservation
is therefore a closure condition a genuine matter model must satisfy**
(B2 Part 2's job — a proper dust action, not just "whatever's left
over") — not a free-standing GR fact this file was entitled to assume
without qualification.

**Scope gap, discovered during this build, stated explicitly:** this file
does not extend to the `Φ,Ψ`-perturbed metric. `FINDING_P54`'s own `G_0i`
*does* include `Φ`. Reconciling this is required before the B1↔B2
compatibility check can be attempted honestly — either by deriving `φ`'s
own field equation on the full perturbed metric (a real, not-yet-started
extension of `FINDING_P46`), or by working in a further-restricted regime
where the mismatch provably doesn't matter (not established here either).
This gap is not a defect of this file's own derivation — it is an
honestly named boundary of what `FINDING_P46`/`P47` themselves ever
established.

This is **not** the matter Euler equation itself (B2 Part 2, separate,
not-yet-started) — it is the source term that will appear on its RHS,
derived from a general covariant identity plus an already-established
field equation, with KG-B2a (no hand-inserted force) satisfied by
construction.

## What this establishes, precisely

1. `Q⁰=-ĝ(δρφ̄̇+ρ̄δφ̇)`, derived (not inserted) from `φ`'s own stress
   non-conservation, within `FINDING_P46`/`P47`'s established `Φ=Ψ=0` scope.
2. A reusable `covariant_box()` helper, internally consistent with
   `covariant_div_upper()` by construction (both built from the same `Γ`
   array) — a genuine machinery addition for future steps in this
   sub-arc, alongside `FINDING_P48`/`P54`'s own `christoffels_exact`.
3. A concrete instance of the campaign's own "no silent fixes" discipline
   applied to a self-caught (not skeptic-caught) error chain — three
   distinct issues, kept visible rather than quietly patched.

## What this does NOT establish

1. **`Q^i` (the spatial components).** Only `Q⁰` is derived here; the
   spatial source term needed for the actual matter Euler equation is a
   separate computation, not attempted in this file.
2. **The matter continuity or Euler equation.** B2 Part 2, not started.
3. **Compatibility with `FINDING_P54`'s `G_0i`.** The scope gap (`Φ=Ψ=0`
   here vs. `Φ`-inclusive there) is named, not resolved.
4. **Any numeric value.** `ĝ`, `φ̄`, `ρ̄` all remain symbolic throughout.
5. **That total stress-energy conservation is automatic here.** It is a
   closure condition B2 Part 2's genuine matter model must satisfy, per
   the skeptic's own independently-verified argument (`FINDING_P46`
   treats `ρ` as external, not dynamical) — not a free-standing fact this
   file assumed without qualification.
6. **That the `T_φ` (kinetic-only) vs. `T_m` (everything else) split is
   independently justified.** Inherited from `FINDING_P47` without
   re-examination — a different split would give a numerically different
   `Q⁰`.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| General identity `∇_μT_φ^{μν}=(□φ)∂^νφ`, `+` sign | **CONFIRMED-REAL** — independently hand-derived from first principles (metric compatibility + symmetry of the scalar's second covariant derivative), sign confirmed exactly `+` | No change. |
| `□φ=-(φ̄̈+3Hφ̄̇)` on background matches `FINDING_P46`'s own convention | **CONFIRMED-REAL** — independently checked against `FINDING_P46`'s own script line (`-box_phi - target_form.subs(rho,0)==0`) directly | No change. |
| `covariant_box()` formula externally correct (not just internally consistent with `covariant_div_upper()`) | **CONFIRMED-REAL** — verified it is the standard covariant-Hessian-trace formula in its own right, not merely self-consistent | No change. |
| `Q⁰` extraction captures all `ε`-cross-terms | **CONFIRMED-REAL** — independently expanded the product `ĝ(ρ̄+εδρ)(φ̄̇+εδφ̇)` and confirmed both cross-terms present | No change. |
| `FINDING_P47`'s `T_μν(φ)`/metric reuse is clean | **CONFIRMED-REAL** — checked directly against `FINDING_P47`'s own stated scope, exact match | No change. |
| "Total conservation is the ONLY foundational GR fact taken as given" | **WEAKENED** — in `FINDING_P46`'s own setup (`ρ` treated as an external scalar, not a dynamical dust field), total conservation does not follow automatically from diffeomorphism invariance; it is a closure condition a genuine matter model must satisfy | **Fixed.** Reworded throughout (docstring, Verdict, this document) — independently re-derived the skeptic's own coupling-term-divergence argument before accepting. |
| Scope gap (`Φ=Ψ=0` here vs. `FINDING_P54`'s `Φ`-inclusive `G_0i`) | **Acknowledged, already correctly flagged** — not an internal defect, but the skeptic notes extending to `Φ≠0` will likely add new terms to `Q⁰`, not just extend the same formula | **Noted** — added to "What this does NOT establish." |
| Recomposition: does `T_φ` (kinetic-only) vs. `T_m` (everything else) split matter | **Flagged as a real, inherited assumption** (from `FINDING_P47`), not independently justified here | **Noted** as an open dependency, not fixed in this pass. |

**True kill assessment:** no. The central `Q⁰` result and every symbolic
computation independently survive the skeptic's own from-scratch
re-derivation. The one substantive issue was a framing overclaim about
how automatically "total conservation" applies — fixed by correctly
scoping it as a closure condition, not a free GR fact — the `Q⁰` formula
itself is unchanged.

## Reproduction

```bash
python experiments/20260803-bridge/P55_phi_stress_nonconservation_source_term.py
```
