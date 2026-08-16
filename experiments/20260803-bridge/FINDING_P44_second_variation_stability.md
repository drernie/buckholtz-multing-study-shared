# P44 — Second variation `δ²S`: no ghost at quadratic order (theory-wide, not solution-specific), and a direct structural link to why P45 (minimal `V(φ)`) matters

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** twelfth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), second of three symmetry/action-theoretic
checks the user authorized in sequence ("го все по очереди").
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P44_second_variation_stability.py`, ruff clean, all
assertions pass.

## 0. Honest scope, applied from the start

`FINDING_P43`'s Part B was corrected the same day for presenting a check
that held for *any* static field as if it were evidence about *one*
specific field. This finding applies that lesson pre-emptively: **Part 1
below tests, with a generic symbolic background, whether the second
variation depends on the specific solution at all — before any claim
is made about what the result means.**

## Part 1 — does `δ²S` depend on the background?

Expanding `P35`'s own Lagrangian `L(φ_bg+εδ)` to `O(ε²)` for a **generic**
symbolic background `φ_bg(t,x,y,z)` (not yet the specific radial profile),
and extracting the pure `δ²` term:

```
d²L/dε² |_(ε=0) = δ̇² − (∂_xδ)² − (∂_yδ)² − (∂_zδ)²
```

**Contains `φ_bg`? No** (script assertion). This is a structural
consequence of `P35`'s matter coupling being *exactly linear* in `φ`
(`−ρĝφ`, no `φ²` or higher term) — the action has no self-interaction
and no potential `V(φ)`, already known from `FINDING_P34`'s own
"stiff-fluid, `w=1`" dead end. **Any check built on this second variation
is a check of the whole theory, not of the specific static solution
`φ(r)=ĝM/(4πr)`.**

## Part 2 — no-ghost check

The resulting quadratic Lagrangian `L₂=(1/2)[δ̇²−(∇δ)²]` has canonical
momentum `π_δ=δ̇` and Hamiltonian density:

```
H₂ = π_δδ̇ − L₂ = (1/2)δ̇² + (1/2)(∇δ)²
```

A **sum of squares** (script assertion), manifestly `≥0` for every
configuration, zero only at `δ=const`. This is the standard no-ghost
criterion — a ghost has a kinetic term with the wrong relative sign,
making `H` unbounded below. **Passes: no ghost at this order**, for the
theory as a whole (there is no background-dependent term for a specific
solution to fail the check on).

## Part 3 — what this does and does not say about `φ(r)=ĝM/(4πr)`

**Does NOT mean** the specific static solution is "stable" in any sense
particular to it — `δ²S` doesn't know which solution (or whether any
solution at all) sits at `φ_bg`; the same `H₂≥0` result holds for
`φ_bg=0` or any other configuration, static or not.

**Does mean** the theory as a whole has no ghost at quadratic order — a
genuine, if structurally unsurprising, fact.

**Direct link to `P34`/`P45`:** the background-independence found in
Part 1 is exactly what "no `V(φ)` exists in this action" predicts — a
nonzero `V(φ)` is precisely what would introduce a `V''(φ_bg)δ²` term
into `L₂`, making stability background-dependent and turning "is *this*
solution stable" into a well-posed, solution-specific question for the
first time. This motivates `P45` (minimal `V(φ)`) directly, rather than
`P45` being an independent, unrelated next step.

## What this establishes, precisely

1. `δ²S` is exactly background-independent — verified symbolically on a
   generic background, not assumed (Part 1).
2. The theory has no ghost at quadratic order (Part 2) — a genuine,
   theory-wide fact.
3. A concrete, derived (not asserted) structural reason `P45`'s `V(φ)`
   step is the right next move: it is precisely what would make Part 1's
   independence result stop holding (Part 3).

## What this does NOT establish

1. **Stability of the specific solution `φ(r)=ĝM/(4πr)`** — the check has
   zero solution-specific content; it would hold identically for any
   background, including the trivial one.
2. **Anything about the gravitational sector** — this is `δ²S_φ` on a flat
   background (matter+`φ` only), not a coupled metric-`φ` perturbation
   analysis, matching the scope of every prior finding in this sub-arc
   (`P37`, `P38`, `P40`, `P42`, `P43`).
3. **Anything about the κ (dipole) sector** — monopole (`g`) sector only.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P44_second_variation_stability.py
```
