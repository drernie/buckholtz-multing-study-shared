# P43 — Noether symmetry audit: shift symmetry confirmed (Part A survives), the other two parts corrected after skeptic review — Part B's "new coverage" was a kinematic triviality, Part C's dilatation number was assumption-dependent

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same day
after context-blind skeptic review — Part B and Part C headlines both
falsified and reworked; Part A survives intact.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
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

## Part B — full 4D energy conservation ~~(genuinely new coverage)~~ [CORRECTED: kinematic triviality, not new coverage]

`FINDING_P37` checked `∂ᵢT_ij=0` only in the *static* limit
(`∂_t φ=0` assumed throughout) — never exercising the time-index or
mixed terms of the full divergence. This part checks
`∂_μT^μ_0=0` in full, reusing P37's own `T_μν` formula unchanged, for the
same static field:

```
∂_μ(T^μ_0) = 0   (r>0, script assertion, exact)
```

~~Genuinely new coverage — not a restatement of P37's own already-checked
result, since `P37` never tested the time-derivative terms this
divergence actually contains (they vanish here because the field is
literally static, but that vanishing was not previously verified as part
of the *full* conservation law, only assumed).~~

**[CORRECTED after skeptic review]** The arithmetic above is correct but
the "genuinely new coverage" claim is false. Direct check, added to the
script: `T_i0 = ∂_iφ·∂_0φ = ∂_iφ·0 = 0` **identically**, for *any* static
field regardless of whether `φ` solves its field equation — the check
never needed `φ`'s dynamics at all. `T_00` is manifestly `t`-independent
for the same reason, so `∂_t(T_00)=0` trivially. The result holds for
*any* `T_μν` of this two-derivative structural form on *any* static
configuration; it is a fact about staticity, not about this specific
`T_μν`. P37's own `∂ᵢT_ij=0` check on the *spatial* components is
genuinely non-trivial (it requires `φ`'s on-shell field equation) —
that's the real reason P37 checked `ij` and not `0`, and this part does
not add coverage beyond it.

## Part C — dilatation weight of `ĝ` ~~(new, open, not yet comparable to P39)~~ [CORRECTED: SPECULATIVE, assumption-dependent]

Demanding the action's kinetic and coupling terms scale the same way
under a spatial dilatation `x→λx` (mass held fixed) forces:

```
φ's scaling weight:   Δ = -1/2       (script, solved not guessed)
ĝ's scaling weight:   Δ_ĝ = +1/2     (script, solved not guessed)
```

~~**Important caveat, stated before any comparison is attempted:** this is
a *dilatation weight*... [original caveat retained below, but it did not
go far enough — see correction]~~

**[CORRECTED after skeptic review]** The `+1/2` number is real arithmetic
*given two unstated choices*, neither derived from the action itself:

1. **`ρ`'s scaling weight was assumed, not derived.** The script picked
   `ρ_w=-3` (density with mass held fixed under rescaling). Independently
   verified sensitivity (`P43_noether_symmetry_audit.py`, Part C cross-check
   (i)):

   | `ρ_w` assumption | meaning | resulting `Δ_ĝ` |
   |---|---|---|
   | `0` | external prescribed source, mass not fixed | `-5/2` |
   | `-3` | mass-fixed density (this script's original choice) | `+1/2` |
   | `-2` | point mass `M~λ¹`, `ρ=M·δ³(r)` | `-1/2` |

   `+1/2` is one point in a range the script never justified choosing.

2. **Spatial-only dilatation is not the natural symmetry to check.** This
   action is meant to be part of a Lorentz-*covariant* completion — the
   natural transformation is the full 4D `x^μ→λx^μ`, not a spatial-only
   slice of a static configuration. Independently verified (cross-check
   (ii)): full 4D dilatation forces `Δ_φ=-1` (the standard canonical
   scaling dimension of a 4D scalar field, not `-1/2`) and `Δ_ĝ=0` (not
   `+1/2`), holding `ρ_w=-3` fixed.

Two individually-defensible notions of dilatation give two different
numbers (`+1/2` vs `0`); nothing in this analysis privileges one. The
original caveat ("dilatation weight may not be the same kind of number as
P39's SI exponent") was true but insufficient — it flagged one risk
(comparability to P39) while missing two more load-bearing ones
(the `ρ`-scaling assumption, the spatial-only-vs-4D choice) that make the
number itself non-robust, prior to any comparison to P39 at all.

```
P39 reading 1: [ĝ] SI length exponent = -1
P39 reading 2: [ĝ] SI length exponent = -2
Spatial-only dilatation weight (original) = +1/2
Full 4D dilatation weight (corrected)     =  0
Neither coincides with either P39 reading, under either convention.
```

**Downgraded status: `[SPECULATIVE]`.** Not a derived constraint on `ĝ` —
a convention- and assumption-dependent number that happens not to match
P39's readings under the specific choices tried, with no basis yet for
preferring any one choice.

## What this establishes, precisely

1. A previously-unstated explicit account of which symmetry `φ`'s matter
   coupling breaks (Part A) — **survives skeptic review unchanged.**
2. ~~Genuinely new verification of full (not just static-spatial) energy
   conservation~~ **[CORRECTED] Nothing beyond what P37 already
   established** — Part B's check is a kinematic triviality of staticity,
   not new dynamical coverage.
3. ~~A new, independently-derived dilatation constraint on `ĝ`~~
   **[CORRECTED] An illustration of how sensitive a naive dilatation-weight
   calculation is to unstated modeling choices** — not a constraint, and
   not (yet) comparable to P39 in any established way.

## What this does NOT establish

1. **Independent verification of P35's field equation** (Part A) — the
   Noether-current route shares the same premises as the Euler-Lagrange
   route already used in P35; agreement is guaranteed by construction,
   not evidence.
2. **[CORRECTED, added]** **Any dynamical content of `T_μν` beyond
   staticity itself** (Part B) — the `∂_μT^μ_0=0` check would pass for
   *any* two-derivative `T_μν` on *any* static field; it is not evidence
   that this project's specific `T_μν` is correct.
3. **[CORRECTED, was "resolution of P39's reading question," now
   broader]** **Any well-defined value for `ĝ`'s scaling weight at all**
   (Part C) — the `+1/2` result depends on an underived `ρ`-scaling
   assumption and a nonstandard spatial-only dilatation choice; a
   different, equally defensible choice gives `0`. Resolution of P39's
   own reading question would require first fixing these upstream choices
   on independent grounds, which this finding does not do.
4. **Anything about the κ (dipole) sector** — entirely about the
   monopole (`g`) sector's own action, matching every prior finding in
   this sub-arc.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part A (`dL/dε=ĝρ`, "not independent verification of P35") | **CONFIRMED** | No change. Hand-derivation matched; reasoning that this is a tautology of Noether's identity (not fresh evidence) also independently confirmed correct. |
| Part B ("genuinely new coverage") | **FALSIFIED** — the arithmetic is right but the check is a kinematic triviality of staticity alone, content-free for *any* `T_μν` of this structural form | **Fixed.** Independently re-derived (`T_i0=0` identically, `∂_t T_00=0` trivially) before accepting — matches skeptic exactly. Script and this doc corrected: headline downgraded from "new coverage" to "kinematic triviality, no new coverage beyond P37." |
| Part C ("new independent constraint, `Δ_ĝ=+1/2`") | **FALSIFIED** — depends on an undocumented `ρ`-scaling assumption (`ρ_w=-3`) and an unmotivated spatial-only-vs-full-4D choice; both drivers independently verified to change the answer | **Fixed.** Independently re-derived the `ρ_w` sensitivity table and the full-4D cross-check (`Δ_φ=-1`, `Δ_ĝ=0`) before accepting — matches skeptic's structural argument, numbers confirmed via sympy. Script and this doc corrected: headline downgraded from "new constraint" to `[SPECULATIVE]`. |
| Scoping gap: "does NOT establish" section missing Part B/C caveats | **Confirmed gap** | **Fixed** — items 2 and 3 added above. |

No FALSIFIED verdict here meets the Step 8a "true kill" bar (core predicate
false, no viable response) — Part A survives fully, and Parts B/C survive
as corrected, honestly-downgraded findings rather than deleted ones,
consistent with this campaign's established practice (cf. `FINDING_P8`'s
retraction, `FINDING_P28`'s retraction).

## Reproduction

```bash
python experiments/20260803-bridge/P43_noether_symmetry_audit.py
```
