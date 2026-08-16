# P51 — the Reading-1/Reading-2 equivalence test was mis-designed: both load-bearing checks turned out to have zero discriminating power, for two different reasons, both independently re-verified before accepting the correction

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — the FIRST true-kill-adjacent
verdict in this entire covariant-completion campaign. The original
headline ("E1 confirmed at the structural/dimensional level") is
RETRACTED, not softened. Both correction claims independently
re-verified symbolically before being accepted, per
`audit-verification-gate.md` discipline — this was not taken on the
skeptic's word.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
**Origin:** direct continuation of P50B, per the user's own refined
staging: `λ=αc` (α unknown, not assumed 1), pre-registered E1/E2/E3
outcomes, six-step protocol, two red-team tests.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P51_reading_equivalence_gate.py`, ruff clean, all assertions
pass.

## 0. Pre-registered outcomes and hard kill criterion

**E1 — full equivalence.** A single `λ` preserves `S`, `gφ`, `Ag²`,
`m_eff/m`, the field equation, and `F`, with `dτ` unchanged.
**E2 — partial equivalence.** Localizes a real gap to a specific term.
**E3 — inequivalent.** No single `λ` works — an external anchor is
genuinely needed.
**Hard kill:** the same `λ` must simultaneously transform `φ`, `g`, `A`,
`S`, `m_eff`, `F`.

## Part 1 — Reading 1/Reading 2 tuples

```
[φ]_R1=kg⁰m²s⁻²   [g]_R1=dimensionless   [A]_R1=[G_N]
[φ]_R2=kg⁰m³s⁻³   [g]_R2=kg⁰m⁻¹s¹        [A]_R2=[G_N·c²]=kg⁻¹m⁵s⁻⁴
```

Confirmed correct (script assertion) — this arithmetic **survives** the
correction below intact.

## Part 2 — the "two independent routes" is a forced identity, not evidence

`[λ]` computed two ways, both giving `[c]`:

```
[λ] from φ-route (φ_R2/φ_R1) = [c]
[λ] from g-route (g_R1/g_R2) = [c]
```

**[CORRECTED after skeptic review]** The original text called this
agreement independent evidence ("no a priori reason these two ratios
needed to coincide"). **False.** Independently re-verified symbolically
before accepting the skeptic's claim — both routes reduce to the
**literal same expression**, by direct substitution of how Reading 2 was
constructed *from* Reading 1 in the first place (`g_R2:=c/φ_R1`, `φ_R2`
self-consistently re-derived from the same `g·m·φ=energy` template):

```
φ_R2/φ_R1 = energy/(c·mass)
g_R1/g_R2 = energy/(c·mass)
difference = 0
```

**This is a tautology, not independent confirmation.** Both "routes" are
the same equation rearranged — forced the moment `g_R2` was defined as
`c/φ_R1` and `φ_R2` was re-derived from the same template. **Part 2
provides zero discriminating evidence for E1 vs E3.**

## Part 3 — interaction invariant, and why it doesn't help either

```
gφ = g'φ'                    (confirmed, any λ)
1−(g/c)φ = 1−(g'/c)φ'        (confirmed, any λ)
```

**[CORRECTED after skeptic review, strengthened]** The original text said
these checks are "not independent evidence that `λ=c` specifically" —
true but understated. **Since Parts 3–6 hold for *any* `λ`, they have
zero power to discriminate E1 from E3 at all** — not just "not specific
to `λ=c`." Any two dimensionally-consistent `(φ,g,A)` triples sharing
this Lagrangian's general gauge-covariance structure would *also* pass
Parts 3–6, whether or not they encode the same physics. **The
pre-registered "hard kill criterion" is therefore not capable, by
construction, of distinguishing its own two stated alternatives — a
genuine design flaw in the pre-registration itself, not merely an
inconclusive result.**

**P50A consequence — survives, unaffected by the correction:** since
`ĝ:=g/c`, this check shows `ĝφ̄` is invariant for **any** field
redefinition of this type. `P50A`'s `μ_metric=1−ĝφ̄` correction is
confirmed field-redefinition invariant, entirely independent of resolving
E1 vs E3 — this conclusion never depended on the (now-retracted) headline.

## Parts 4–6 — force, field equation, worldline: same status as Part 3

All confirmed to hold for any `λ` (force substituted into the actual
P50B formula, not just symbolically; the full field-equation
substitution giving `EOM_R2=EOM_R1/λ` exactly — a common nonzero factor,
stronger than checking individual terms; the worldline gate passing by
inspection). **All real, useful facts about the theory's general
covariance — none discriminate E1 from E3, for the same reason as Part 3.**

## Part 7 — round-trip, downgraded

`R1→R2→R1` via `λ` then `1/λ`: exact recovery (script assertion).
**[CORRECTED after skeptic review]** The original text called this a
"red-team test" passing a "negative control." **The skeptic correctly
noted this is a trivial algebraic consequence of invertibility** — for
any `x↦f(λ)x`, applying `f(λ)` then `f(1/λ)` returns `x` by construction;
it cannot fail unless the inverse-transformation bookkeeping itself
contains an arithmetic error. **Downgraded:** a basic correctness check
(worth keeping — would have caught a sign/inverse error), not a test with
genuine falsification power over E1/E3.

## Part 8 — `λ→2λ`, unchanged: honestly demonstrates the method's limit

A dimension tuple carries no dimensionless prefactor — `[2c]=[c]`
exactly, as a tuple. `α` (in `λ=αc`) remains genuinely undetermined by
dimensional analysis alone. This part's honesty was already correct in
the original version and needed no correction.

## Verdict — fully rewritten

**The pre-registered test was mis-designed.** Both load-bearing pieces
turned out to have zero discriminating power, for two different reasons,
both independently re-verified symbolically before accepting:

1. Part 2's "two independent routes agree" is a forced algebraic
   identity, not independent confirmation.
2. Parts 3–6, true for any `λ`, cannot distinguish "R1 and R2 are the
   same physics" from "R1 and R2 are unrelated but each internally
   consistent with this Lagrangian's general covariance."

**Corrected verdict: E1-vs-E3 for R1/R2 specifically is undetermined by
this analysis** — neither confirmed nor refuted. This is a methodological
finding (the test itself was uninformative), not a null result about the
physics.

**What survives, kept honestly:**
- The dimension arithmetic (Part 1) — correct, verified.
- The theory's general gauge-covariance (Parts 3–6) — real, useful,
  extends `FINDING_P50B`'s partial coverage to the full field equation
  and a direct force-substitution check — just not informative about
  R1 vs R2 specifically.
- **`P50A`'s `ĝφ̄` invariance — unchanged.** Never depended on resolving
  E1 vs E3, since it holds for any `λ`.

**What a genuinely discriminating test would need:** something sensitive
to the readings' *numerical* relationship, not just their shared
dimensional template — an independent physical anchor, or an action term
that is *not* automatically covariant under field redefinition (none
identified in this campaign). Pure dimensional/algebraic analysis, as
attempted in `P50B` and here, has reached its limit for this specific
question.

## What this establishes, precisely

1. `[A]_R2=[G_N·c²]` exactly — a correct, verified fact.
2. The theory admits a full one-parameter gauge-covariance family
   (interaction, force, field equation, worldline all invariant under
   any `λ`) — genuinely new content beyond `FINDING_P50B`.
3. `P50A`'s `μ_metric` correction is field-redefinition invariant,
   independent of the R1/R2 question.
4. **A real methodological lesson:** a pre-registered "hard kill
   criterion" can itself be non-discriminating — this must be checked
   (does the criterion actually distinguish the stated alternatives?),
   not just executed.

## What this does NOT establish

1. **Whether R1 and R2 are the same physics or genuinely different
   theories.** Fully open — this finding's original attempt to answer
   this question failed on its own terms.
2. **Any resolution of `FINDING_P39`'s original ambiguity.** Still open,
   in the same state P39 and P50B left it.
3. **A numeric comparison to `FINDING_P22`/`P31`'s ceiling.**
4. **The matter Euler equation, or `T₀ᵢ`/`G₀ᵢ`** — out of scope.
5. **Anything about the κ (dipole) sector.**
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 1 dimension arithmetic (`[A]_R2=[G_N·c²]`) | **CONFIRMED** | No change. |
| Part 2 "two independent routes, no a priori reason to coincide" | **FALSIFIED** — algebraically forced identity, traced explicitly | **Fixed** — independently re-derived symbolically (matching the skeptic's own derivation) before accepting; retracted, replaced with the explicit forced-identity demonstration. |
| Parts 3–6 as evidence for E1 | **FALSIFIED** — hold for any `λ`, therefore cannot discriminate E1 from E3 at all (not merely "not specific to `λ=c`") | **Fixed** — reframed as real-but-non-discriminating; the pre-registered hard-kill criterion itself named as flawed. |
| Pre-registered "hard kill" criterion's discriminating power | **FALSIFIED** — automatically satisfied by any pair of dimensionally-consistent readings sharing the Lagrangian's covariant structure, related or not | **Fixed** — stated explicitly as a design flaw in the pre-registration, not an inconclusive execution. |
| Part 7 round-trip as a "red-team test" | **FALSIFIED** — trivially guaranteed for any invertible transformation of this form | **Fixed** — downgraded to a basic correctness check, not a falsification test. |
| Part 8 `λ→2λ`, honesty about `α` | **CONFIRMED** | No change — already correctly scoped in the original. |
| Headline "E1 CONFIRMED AT THE STRUCTURAL/DIMENSIONAL LEVEL" | **FALSIFIED** — rests entirely on Part 2 (circular) and Parts 3–6 (uninformative); the only genuinely established fact (`[A]_R2=[G_N·c²]`) is a consequence of R2's own definition, not a bridge to R1 | **Retracted**, not softened — replaced with "E1-vs-E3 undetermined." |
| "Consistent with being two points on the same gauge orbit" | **WEAKENED** — defensible as a *necessary* consistency statement, but not evidence of *sufficiency*; R1/R2 are equally compatible with being unrelated readings sharing the same template | **Fixed** — removed from the verdict; replaced with the honest "undetermined" framing. |

**Overall: this meets the "true kill" bar for the headline claim.** The
skeptic's own suggested Perelman-audit mapping: `BLOCKED_BY_DEFINITION` —
the pre-registered test was mis-designed, not merely inconclusively
executed. The underlying scientific question (are R1 and R2 the same
physics?) is **not** falsified — it remains genuinely open, exactly where
`FINDING_P39` and `FINDING_P50B` left it. What died is the specific claim
that *this* test resolved it.

## Reproduction

```bash
python experiments/20260803-bridge/P51_reading_equivalence_gate.py
```
