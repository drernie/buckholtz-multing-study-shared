# P44 — Second variation of the density: no ghost/tachyon/gradient instability (theory-wide, not solution-specific) — the P45 link corrected to require a non-quadratic `V(φ)`

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — Part 3's "P45 link" claim was
wrong for the simplest case (a mass term) and is now stated precisely,
with the counterexample computed explicitly rather than left in prose.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
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

## Part 1 — does `δ²L` depend on the background?

Expanding `P35`'s own Lagrangian *density* `L(φ_bg+εδ)` to `O(ε²)` for a
**generic** symbolic background `φ_bg(t,x,y,z)` (not yet the specific
radial profile), and extracting the pure `δ²` term:

```
d²L/dε² |_(ε=0) = δ̇² − (∂_xδ)² − (∂_yδ)² − (∂_zδ)²
```

**Contains `φ_bg`? No** — verified via a direct derivative check
`∂/∂φ_bg` (script assertion), corrected from an earlier atom-membership
test which would pass even on an unsimplified residual term.

**[CORRECTED after skeptic review]** Two terminology precisions, neither
changing the arithmetic: (1) this is `δ²` of the Lagrangian **density**
`L`, not literally `δ²S` (the action integral) — the two coincide once
boundary terms drop under integration, but the object actually computed
is pointwise, and `φ_bg` was never required to satisfy any field
equation for this density-level result to hold. (2) The result is
verified for **this one Lagrangian**, not proved as a general theorem;
the sharper general condition is "`L` at most quadratic in `φ` with
`φ`-independent coefficients" — linear-in-`φ` is *sufficient* but *not
necessary* (a constant-coefficient mass term would also give a
background-independent result — see the corrected Part 3). **Any check
built on this second variation is a check of this action as a whole, not
of the specific static solution `φ(r)=ĝM/(4πr)`.**

## Part 2 — no-ghost check

The resulting quadratic Lagrangian `L₂=(1/2)[δ̇²−(∇δ)²]` has canonical
momentum `π_δ=δ̇` and Hamiltonian density:

```
H₂ = π_δδ̇ − L₂ = (1/2)δ̇² + (1/2)(∇δ)²
```

A **sum of squares** (script assertion), manifestly `≥0` for every
configuration, zero only at `δ=const`. This is the standard no-ghost
criterion — a ghost has a kinetic term with the wrong relative sign,
making `H` unbounded below. **Passes: no ghost**, for this action as a
whole (there is no background-dependent term for a specific solution to
fail the check on).

**[CORRECTED after skeptic review]** This result is *stronger* than "no
ghost" alone — the exact sum-of-squares form also rules out a tachyon
(no wrong-sign mass term — there is no mass term at all here) and a
gradient instability (no wrong-sign spatial-gradient term). "At this
order" is also slightly misleading: `L` is *exactly* quadratic in `φ`,
so `L₂` is exact, not a leading-order truncation — there is no nonlinear
correction to worry about at any order for the linearized fluctuation.
(This check is silent on Ostrogradsky-type higher-derivative ghosts,
since `L` has only first derivatives of `φ` — not applicable here, but
would need separate treatment if a future step added higher
derivatives.)

## Part 3 — what this does and does not say about `φ(r)=ĝM/(4πr)` ~~(direct structural link to P45)~~ [CORRECTED: link requires non-quadratic `V(φ)`]

**Does NOT mean** the specific static solution is "stable" in any sense
particular to it — `δ²L` doesn't know which solution (or whether any
solution at all) sits at `φ_bg`; the same `H₂≥0` result holds for
`φ_bg=0` or any other configuration, static or not.

**Does mean** this action has no ghost/tachyon/gradient instability at
quadratic order — a genuine, if near-tautological, fact given the
coupling is exactly quadratic.

~~**Direct link to `P34`/`P45`:** the background-independence found in
Part 1 is exactly what "no `V(φ)` exists in this action" predicts — a
nonzero `V(φ)` is precisely what would introduce a `V''(φ_bg)δ²` term
into `L₂`, making stability background-dependent...~~

**[CORRECTED after skeptic review]** The original claim above was
checked only against prose, not computed — and is **false for the
simplest case**. Computed explicitly (`P44_second_variation_stability.py`,
Part 3):

```
mass term   V=(1/2)m²φ²:    d²(−V)/dε²|_0 = −m²δ²        depends on φ_bg? NO
cubic term  V=λφ³/6:        d²(−V)/dε²|_0 = −λδ²φ_bg      depends on φ_bg? YES
```

A quadratic `V` (mass term) is a "nonzero `V(φ)`" that does **not** make
stability background-dependent — `V''=m²` is a constant. **Only a `V`
with `V'''≠0` (cubic or higher — genuine self-interaction beyond a mass
term) introduces `φ_bg`-dependence.** The link to `P45` survives *only*
if `P45`'s "minimal `V(φ)`" is understood to mean cubic-or-higher — now
stated explicitly rather than left ambiguous. This motivates `P45`
specifically exploring a non-quadratic `V(φ)`, not "any `V(φ)` at all."

## What this establishes, precisely

1. `δ²L` (density-level) is exactly background-independent for this
   action — verified symbolically on a generic background via a direct
   derivative check, not assumed (Part 1).
2. This action has no ghost, tachyon, or gradient instability at
   quadratic order (Part 2) — a genuine, if near-tautological, fact.
3. **[CORRECTED]** A precise (not vague) condition under which `P45`'s
   `V(φ)` step would produce a genuinely solution-specific stability
   question: `V(φ)` must be non-quadratic (`V'''≠0`) — computed
   explicitly via a mass-term counterexample and a cubic confirming
   case, not asserted in prose (Part 3).

## What this does NOT establish

1. **Stability of the specific solution `φ(r)=ĝM/(4πr)`** — the check has
   zero solution-specific content; it would hold identically for any
   background, including the trivial one.
2. **Anything about the gravitational sector** — this is `δ²L` on a flat
   background (matter+`φ` only), not a coupled metric-`φ` perturbation
   analysis, matching the scope of every prior finding in this sub-arc
   (`P37`, `P38`, `P40`, `P42`, `P43`).
3. **[CORRECTED, added]** **That any `V(φ)` added at `P45` would create a
   solution-specific stability question** — only a non-quadratic `V`
   does; a mass term would not.
4. **Anything about the κ (dipole) sector** — monopole (`g`) sector only.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 1 (`δ²S` terminology, EOM not enforced, "structural" generalized beyond one Lagrangian) | **WEAKENED** — arithmetic correct, terminology and generality overstated | **Fixed.** Clarified `δ²L` (density) vs `δ²S` (action), noted `φ_bg` need not solve any EOM for this result, scoped the "structural" claim to this one action, and named the sharper general condition (quadratic-with-constant-coefficients, not just linear). Also strengthened the assertion from atom-membership to a direct derivative check. |
| Part 2 ("no ghost at this order") | **WEAKENED** — result is stronger than stated (also rules out tachyon/gradient instability) and "at this order" undersold the exactness (`L` is exactly quadratic, not truncated) | **Fixed.** Both points added explicitly, with the Ostrogradsky-inapplicability caveat noted for completeness. |
| Part 3 ("nonzero `V(φ)` makes stability background-dependent") | **FALSIFIED** — false for a quadratic `V` (mass term); only non-quadratic `V` introduces `φ_bg`-dependence | **Fixed.** Independently re-derived both the mass-term counterexample and the cubic confirming case before accepting — matches skeptic exactly. Script now computes both cases explicitly; finding doc corrected with struck-through original claim and the precise condition stated. |
| Additional: leaky assertion (atom-membership vs. direct derivative check) | **Confirmed methodological gap** | **Fixed** — see Part 1 response above. |
| Additional: "theory-wide, discriminating" framing risks overselling a near-tautological result | **Confirmed framing risk** | **Fixed** — Part 3 now explicitly calls the no-ghost result "near-tautological given the coupling is exactly quadratic," not a positive discriminating finding about MULTING specifically. |

No FALSIFIED verdict here meets the Step 8a "true kill" bar — Parts 1 and
2 survive as corrected (terminology/scope precision, not retraction);
Part 3's core computational content (background-independence, no-ghost)
survives unchanged, and its P45-motivation claim survives narrowed to
the mathematically correct condition, consistent with this campaign's
established correction discipline (cf. `FINDING_P43`).

## Reproduction

```bash
python experiments/20260803-bridge/P44_second_variation_stability.py
```
