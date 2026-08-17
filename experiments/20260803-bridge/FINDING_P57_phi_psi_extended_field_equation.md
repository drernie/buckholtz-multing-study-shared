# P57 — the `Φ,Ψ`-extension of `FINDING_P46`'s own field equation for `δφ`

**Date:** 2026-08-17
**Status:** Built, run, ruff clean, all assertions pass, after one genuine
self-caught sign error (found and fixed before any skeptic review — see
below). **Skeptic review (Step 8a): PENDING, not yet run.**
**Origin:** direct response to the user's own physics review of P56
(2026-08-17), which flagged the `FINDING_P50A` re-scan as the highest-value
next step. Re-deriving `FINDING_P50A`'s Part 7 continuity equation under
the closure `∇_μT_m^{μν}=Q^ν` first requires `Q^0` on `FINDING_P48/P54`'s
own `Φ,Ψ`-perturbed metric — but `FINDING_P55/P56`'s `Q^0`/`Q^1` were built
on `FINDING_P46`'s `Φ=Ψ=0`-only field equation. Naively substituting the
`Φ=Ψ=0` `Q^0` into `FINDING_P50A`'s `Φ,Ψ`-perturbed continuity equation
would repeat exactly P55's own self-caught "scope mismatch between reused
findings" failure mode (eleventh named category). This file closes that
gap at its root: the field equation itself.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P57_phi_psi_extended_field_equation.py`, ruff clean, all
assertions pass.

## Scope decision, stated up front

This file does **only** the field-equation extension — deliberately, per
this campaign's own established "one step at a time" granularity (P46,
P47, P48 were split the same way rather than combined into one sprawling
derivation). The extended `Q^0`/`Q^1` (needed for the actual `FINDING_P50A`
re-scan) and the `FINDING_P50A` correction itself are **not** attempted
here — named as explicit next steps. This single result deliberately
unblocks **two** previously-named open gaps at once (the `FINDING_P50A`
re-scan, and the B1↔B2 compatibility check against `FINDING_P54`'s own
`Φ`-inclusive `G_0i`) — a direct application of the Cheapest Differentiating
Test Protocol: one calculation, two blockers closed.

## Method

Same single perturbation parameter used throughout this whole campaign
(`FINDING_P48`, `P54`, `P55`, `P56`) — **not** a nonstandard two-epsilon
device. Since `box(φ)` is linear in `φ`, and `FINDING_P46`'s own covariant-
box cross-check (Part 2c) already established `box(φ)=-ĝρ` as the field
equation via a generally-covariant operator (built from Christoffel
symbols, which transform correctly under *any* metric), reusing that exact
operator on `FINDING_P48/P54`'s own `Φ,Ψ`-perturbed metric — with
`φ=φ̄(t)+εδφ(t,x,y,z)` and `ρ=ρ̄(t)+εδρ(t,x,y,z)` at the **same** order `ε`
as the metric's own `εΦ`, `εΨ` terms (P48/P54's own convention) — gives the
standard single first-order cosmological-perturbation calculation, not an
ad hoc extension.

## Self-caught sign error (found and fixed before any skeptic review)

The first version compared `box(φ)+ĝρ` directly, termwise, against P34/
P46's own "forward" sign convention (`φ̈+3Hφ̇-…-ĝρ`) and got a spurious
assertion failure. Independently checked before patching: `covariant_box`
applied to a purely `t`-dependent `φ̄(t)` on the unperturbed metric gives
`-( φ̄̈+3Hφ̄̇)`, matching `FINDING_P46`'s own hand-rolled `box_phi` exactly
(the same sign already independently verified in `FINDING_P55`) — `box(φ)`
carries an overall minus sign relative to P34/P46's forward convention.
Fixed by flipping the sign once, matching the established convention
directly instead of comparing up to an unstated sign.

## Part 1–2 — metric and field split, reused machinery

Metric: `ds²=-(1+2εΦ)dt²+a²(1-2εΨ)(dx²+dy²+dz²)`, identical to
`FINDING_P48/P54`. `φ=φ̄(t)+εδφ(t,x,y,z)`, `ρ=ρ̄(t)+εδρ(t,x,y,z)`, at the
same order `ε` as the metric's own perturbation.

## Part 3 — `ε⁰` (background) piece — kill-gate

```
ε⁰:  φ̄̈ + 3Hφ̄̇ = ĝρ̄
```

Matches `FINDING_P34` exactly (trivial at `Φ=Ψ=0`, but checked directly,
not assumed).

## Part 4 — `ε¹` piece: the deliverable

```
δφ̈ + 3Hδφ̇ - ∇²δφ/a² - ĝδρ
  - 2Φφ̄̈ - 6HΦφ̄̇ - Φ̇φ̄̇ - 3Ψ̇φ̄̇ = 0
```

**The genuine positive control:** setting `Φ` and `Ψ` to identically zero
(the *functions*, not `ε→0` — `ε¹` is already taken) reduces **exactly**
to `FINDING_P46`'s own Part 3 result — checked via direct symbolic
subtraction, zero residual, not merely asserted similar.

**The new terms**, sourced by `Φ` and `Ψ`:

```
-2Φφ̄̈ - 6HΦφ̄̇ - Φ̇φ̄̇ - 3Ψ̇φ̄̇
```

## Part 5 — sanity checks on the new terms

Splitting by which metric perturbation sources what:

```
Φ-only:  -2Φφ̄̈ - 6HΦφ̄̇ - Φ̇φ̄̇
Ψ-only:  -3Ψ̇φ̄̇
```

Both pieces are generically nonzero for `φ̄̇≠0` — both the lapse
perturbation `Φ` and the spatial-curvature perturbation `Ψ` directly
source `δφ`'s own equation of motion once `φ̄` is time-evolving,
independent of any `ĝ` coupling to matter. This is standard
rolling-scalar-in-FRW physics (gravitational time-dilation sourcing), not
MULTING-specific — the same structure appears for any minimally-coupled
canonical scalar with a time-evolving background value.

**On-shell simplification** (checked explicitly as on-shell, not
overclaimed as an unconditional algebraic identity): using `FINDING_P34`'s
own background equation of motion (`φ̄̈+3Hφ̄̇=ĝρ̄`, i.e. `p34_eq:=
φ̄̈+3Hφ̄̇-ĝρ̄=0`), the residual between the `Φ`-only piece and the candidate
simplified form `-2Φĝρ̄-Φ̇φ̄̇` was verified to equal exactly `-2Φ·p34_eq` —
i.e. the simplification `Φ-only → -2Φĝρ̄-Φ̇φ̄̇` holds **on** the background
solution, not as a free-standing algebraic fact:

```
Φ-only (on-shell) = -2Φĝρ̄ - Φ̇φ̄̇
```

## Verdict

The `Φ,Ψ`-extended field equation for `δφ` is derived and passes its one
genuine positive control (`Φ=Ψ=0` reduces exactly to `FINDING_P46`'s own
Part 3 equation) plus an independent background-equation check (`ε⁰`
matches `FINDING_P34` exactly). The new `Φ,Ψ`-sourced terms are extracted
explicitly, not buried in an unexamined combined expression, and one of
them (`Φ`-only) is further simplified on-shell using `FINDING_P34`'s own
background equation.

## What this establishes, precisely

1. The full `Φ,Ψ`-extended linear field equation for `δφ`, with its two
   positive controls (background→P34, `Φ=Ψ=0`→`FINDING_P46` Part 3) both
   independently verified via direct symbolic subtraction.
2. The new source terms `Φ` and `Ψ` add to `δφ`'s equation of motion,
   proportional to `φ̄̇` — standard gravitational time-dilation sourcing
   for any rolling scalar, present regardless of `ĝ`.
3. An on-shell simplification of the `Φ`-only piece, explicitly checked
   (not asserted) to hold only given `FINDING_P34`'s own background
   equation, not as an unconditional identity.

## What this does NOT establish

1. **The extended `Q^0`/`Q^1` source terms.** `FINDING_P55/P56`'s own
   deliverable, now needing the same `Φ,Ψ`-extension applied to
   `T_φ^{μν}`'s own covariant divergence — a separate, not-yet-started
   step, though this file's field equation is the direct prerequisite.
2. **The `FINDING_P50A` correction itself.** Requires (1) first.
3. **The B1↔B2 compatibility check** against `FINDING_P54`'s own
   `Φ`-inclusive `G_0i`. Also requires (1) — this file's field equation is
   a shared prerequisite for both open tasks named in P56's own verdict.
4. **Any numeric value.** `ĝ`, `φ̄`, `ρ̄`, `Φ`, `Ψ` remain symbolic
   throughout.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

**Pending.** To be completed before this finding is considered closed,
matching this campaign's standing discipline.

## Reproduction

```bash
python experiments/20260803-bridge/P57_phi_psi_extended_field_equation.py
```
