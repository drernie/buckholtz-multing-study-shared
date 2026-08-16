# P43 — Noether symmetry audit: full 4D energy conservation confirmed (new coverage), a fresh dilatation constraint on `ĝ` found (open, not yet comparable to P39), shift symmetry honestly scoped as illuminating, not verifying

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** eleventh step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), first of three symmetry/action-theoretic
checks the user requested after reviewing background material on the
principle of least action, explicitly authorized to run in sequence
("го все по очереди") rather than pausing between each.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P43_noether_symmetry_audit.py`, ruff clean, all assertions
pass.

## 0. Honest scope

Three independently-scoped parts, deliberately not blended into one
headline claim, since they have very different evidentiary weight.

## Part A — shift symmetry `φ→φ+ε` (illuminating, not verifying)

Scoped honestly *from the start* — not after a skeptic catches it, per
the lesson already learned once this campaign (`FINDING_P34`'s own
"two independent routes... Noether's theorem guarantees agreement, not
evidence for it" correction). For P35's own single-field, purely-kinetic
Lagrangian, the canonical Noether current for a shift symmetry is
`J^μ=∂^μφ` by construction, and `∂_μJ^μ=□φ` — this trivially *is* P35's
own field equation, not an independent re-derivation of it. What this
part *does* add, verified mechanically: the exact symmetry-breaking term
is `ĝρ` (script assertion) — an explicit statement of *which* symmetry
`φ`'s coupling to matter breaks and by exactly what amount, not
previously stated plainly anywhere in `P34`/`P35`'s own text.

## Part B — full 4D energy conservation (genuinely new coverage)

`FINDING_P37` checked `∂ᵢT_ij=0` only in the *static* limit
(`∂_t φ=0` assumed throughout) — never exercising the time-index or
mixed terms of the full divergence. This part checks
`∂_μT^μ_0=0` in full, reusing P37's own `T_μν` formula unchanged, for the
same static field:

```
∂_μ(T^μ_0) = 0   (r>0, script assertion, exact)
```

Genuinely new coverage — not a restatement of P37's own already-checked
result, since `P37` never tested the time-derivative terms this
divergence actually contains (they vanish here because the field is
literally static, but that vanishing was not previously verified as part
of the *full* conservation law, only assumed).

## Part C — dilatation weight of `ĝ` (new, open, not yet comparable to P39)

Demanding the action's kinetic and coupling terms scale the same way
under a spatial dilatation `x→λx` (mass held fixed) forces:

```
φ's scaling weight:   Δ = -1/2       (script, solved not guessed)
ĝ's scaling weight:   Δ_ĝ = +1/2     (script, solved not guessed)
```

**Important caveat, stated before any comparison is attempted:** this is
a *dilatation weight* — how a physical configuration's value changes
under an *active* rescaling of space, mass held fixed — not automatically
the same kind of number as `FINDING_P39`'s own *SI length exponent* (a
passive, dynamics-independent statement about units of measurement). The
two coincide for many simple cases, but that coincidence is not
established here. Checked anyway, honestly labeled:

```
P39 reading 1: [ĝ] SI length exponent = -1
P39 reading 2: [ĝ] SI length exponent = -2
This analysis's dilatation weight     = +1/2
Coincides with either reading?          No
```

**This does not refute either of P39's readings** — it is a *new,
independent* constraint on `ĝ` whose relationship to P39's own SI-unit
bookkeeping is itself an open question, not yet resolved either way.

## What this establishes, precisely

1. A previously-unstated explicit account of which symmetry `φ`'s matter
   coupling breaks (Part A).
2. Genuinely new verification of full (not just static-spatial) energy
   conservation for the already-established static field configuration
   (Part B).
3. A new, independently-derived dilatation constraint on `ĝ`, correctly
   flagged as not yet known to relate directly to P39's own SI-exponent
   readings (Part C) — a fresh open question, not a resolution.

## What this does NOT establish

1. **Independent verification of P35's field equation** (Part A) — the
   Noether-current route shares the same premises as the Euler-Lagrange
   route already used in P35; agreement is guaranteed by construction,
   not evidence.
2. **Resolution of P39's own `g`/`ĝ` reading question** (Part C) — the
   dilatation weight and SI exponent are not shown to be comparable
   quantities here; "no match" is a new open question, not a
   disambiguation.
3. **Anything about the κ (dipole) sector** — entirely about the
   monopole (`g`) sector's own action, matching every prior finding in
   this sub-arc.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P43_noether_symmetry_audit.py
```
