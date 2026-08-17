# P53 — a soft/conditional external scale constraint on P52's `Ag²` invariant already existed in this project (P22/P31, under an explicit mapping, not a direct measurement); it does not extend to `gφ` or `λ₄A²`, and does not resolve P51's Reading-1-vs-Reading-2 question

**Date:** 2026-08-17
**Status:** Built, run, ruff clean, all assertions pass. **Skeptic review
(Step 8a): COMPLETE. Not a true kill — one consequential citation error
found (wrong bridge cited for the A-continuity claim) and fixed with a
better-supported one; three framing tightenings applied. See Skeptic
Verdict below.**
**[USER-FLAGGED PRECISION CORRECTION, same day, after skeptic review.]**
`Ag²≲8.39×10⁻¹²` must be called a **soft/conditional ceiling under an
explicit mapping**, never a *direct measurement* of `Ag²`. This was
already present as a caveat inherited from `FINDING_P22`'s own §3
(target-population mismatch: Archidiacono's `φ` couples only to dark
matter, MULTING's `g` couples to mass generically), but this finding's
own headline/Verdict language ("genuine external anchor," "external
non-self-referential number") risked reading stronger than that caveat
allows. Corrected throughout below — provenance kept clean, per Gate 2
(Target Provenance): this is an **external scale constraint under an
explicit, unverified mapping**, not a prediction, not a fit to MULTING's
own data, and not a direct experimental bound on MULTING's own `Ag²`.
**Origin:** direct response to the stop-rule reached after P52 — three
consecutive normalization-audit steps (P50B, P51, P52) each independently
hit the same wall: internal field-redefinition-covariance/rank-nullspace
methods cannot fix a *number*, only a combination's *form*. The user's own
framing after P52: further internal variations have low information
value; the next step needs a genuinely new *source* of information, not a
fourth variation of the same method. Before building anything new, a
Novelty Check (FL Step -3) was run — it found the needed external source
**already exists in this project**, from a different sub-thread
(P21/P22/P31, 2026-08-13), never before connected to P52's brand-new
invariance proof (which did not exist until this session).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P53_ag2_external_anchor_synthesis.py`, ruff clean, all
assertions pass.

## 0. Novelty Check (FL Step -3), done before writing this script

- `docs/129` (Q006, 2026-07-22): grepped the *entire* TJB preprint for
  `lagrangian|action|variational|euler-lagrange|field equation|hamiltonian`
  — **zero hits**. MULTING's own published corpus specifies the theory
  entirely at the level of two-body forces; there is no covariant action
  in the source at all. A source-level "grep for where `g`/`φ` is fixed"
  (the originally-proposed P53 scope, from the prior turn's plan) would
  only re-confirm `docs/129` at one further remove — not new information.
- `FINDING_P21`/`FINDING_P22` (2026-08-13) **already** established a
  genuine external numeric ceiling on `Ag²` — not from TJB's corpus, but
  from an independently-published paper (Archidiacono, Castorina,
  Redigolo, Salvioni, arXiv:2204.08484, JCAP 10 (2022) 074) via a
  completely unrelated mechanism (a fifth-force bound on a dark-matter-only
  scalar), mapped onto this project's own `A·g²=4π·ΔG` identity.
- `FINDING_P52` (this session) independently proved `Ag²` is exactly the
  field-redefinition-invariant combination the whole normalization-audit
  sub-campaign was searching for. Nothing in the repo could have connected
  P22's number to P52's proof before today, because P52 did not exist
  before today. **This is the new-source-of-information step**: connect
  an old external number to a brand-new internal result that makes it
  trustworthy in a way it could not have been shown to be before.

## 1. Pre-registered outcomes and kill-gates

**M1 — mapping confirmed:** P22/P31's `A` (`φ_true := A·φ_raw`,
`FINDING_P21`) and P52's `A` (`:=C⁻¹`) are the same quantity.
**M2 — mapping broken:** an inconsistency is found; the ceiling would not
straightforwardly apply to P52's invariant.
**M3 — reading caveat, applies regardless of M1/M2:** P22/P31's ceiling
was computed under P39's Reading 1 — this does not resolve whether Reading
1 is the physically correct one (P51's own open question).

**KG1 (unit/definition continuity):** if P52's `A:=C⁻¹` cannot be traced
to P21's `A:=φ_true/φ_raw` through an *already-established* finding, this
synthesis is void (M2).
**KG2 (no new precision claimed):** this finding must not upgrade P22/P31's
own "soft ceiling, not precision result" status.

## Part 1 — re-derive P22/P31's ceiling, not copy the number

```
A·g² = 4π·β·G_N   (FINDING_P21 + FINDING_P22, two independently-quoted
                    routes from Archidiacono et al., verified to agree
                    exactly — P22's own positive control, reused)
```

Using `β≲0.01` (P22's independently-verified abstract headline figure)
and `G_N=6.6743×10⁻¹¹` SI:

```
A·g² ≲ 8.3872×10⁻¹²   (SI, m³kg⁻¹s⁻², Reading 1)
```

**Confirmed (script assertion): matches `FINDING_P22`'s own reported
`8.39×10⁻¹²` to <1%.** Note reused, not re-claimed as fresh confirmation:
`FINDING_P31` derives a near-identical `~8.39×10⁻¹²` via a *different*
external paper (Bean & Tangmatitham growth-rate bound) — this project's
own pearl registry already flags this as **not independent convergence**
(both are ~1%-level bounds through the identical conversion formula).

## Part 2 — KG1: is P22/P31's `A` the same as P52's `A:=C⁻¹`?

Not re-derived from scratch here — doing so would repeat P51's own
mistake of treating a shared construction as independent confirmation.

~~Instead: `FINDING_P50B`'s own pre-registered decisive-check requirement
(two independent canonicalization routes) already established this.
Route A (kinetic-term canonicalization, `A:=C⁻¹` by definition) and
Route B (P19's own Green's-function force law — the *same* machinery
P21's `φ_raw`/`A` split used) **agreed exactly** in P50B's own
build+skeptic cycle. **→ M1 (mapping confirmed), conditional on trusting
`FINDING_P50B`'s own already-corrected result** — an honest limitation,
stated explicitly, not re-verified from first principles here.~~

**[CORRECTED after context-blind skeptic review, Step 8a]** The original
citation above was the **wrong bridge**. `FINDING_P50B`'s own skeptic
pass already downgraded that specific claim ("two independent
canonicalization routes," Part 4) to "propagation-verification, not
independent derivation" — Route 2 solves the Euler-Lagrange equation from
the *same* Lagrangian as Route 1, so their agreement is a necessary
consequence of variational calculus, not independent confirmation.
Citing it at pre-correction strength repeated, in miniature, this
session's own recurring failure mode. Independently re-checked (re-read
`FINDING_P50B` in full) before correcting.

**The better-supported bridge:**
1. `FINDING_P21`'s own skeptic-added note (S2): *"the identical physics
   results from placing an equivalent factor in the kinetic term instead
   (`(1/2A)(∂φ)²`)"* — P21's own text already states the
   coupling-normalization vs. kinetic-term placement of `A` is
   convention-equivalent.
2. `FINDING_P50B` **Part 5** (dimensional analysis, *not* Part 4): under
   Reading 1, the kinetic term `C(∂φ)²` must itself carry
   Lagrangian-density dimension, forcing `[A]=[C⁻¹]=kg⁻¹m³s⁻²=[G_N]`
   exactly — P21's own `[A]=[G_N]` result, re-derived from the *same*
   general-`C` Lagrangian P52 uses, not merely analogous to it.

**→ M1 (mapping confirmed), conditional on these two already-established
results** — not re-verified from first principles here, an honest
limitation.

**[Added after skeptic review]** `A` plays a conceptually *different*
role in each finding: P21 treats `A` as a fixed dimensional constant of
the theory (to be measured); P52 treats `A:=C⁻¹` as a free parameter
subject to the redefinition freedom (`w(A)=2`). Both conventions give the
*same* invariant `Ag²`, and the external bound transfers either way — but
this is a real conceptual asymmetry between the two findings, not a
detail to gloss over.

## Part 3 — KG2/M3: the ceiling is Reading-1-specific

`FINDING_P21` states plainly: "`g`'s dimensionlessness is an assumption
made here, not established." That assumption **is** P39's Reading 1 by
construction. `FINDING_P42` independently confirmed this same
Reading-1-specificity for a *different* shared-constant result
(`Ω_φ`/`Φ−Ψ`), and found it explicitly fails under Reading 2. `FINDING_P51`
(this session) could not determine whether Reading 1 or Reading 2 is
physically correct.

**→ M3 holds regardless of M1/M2**: the ceiling is a real, external,
non-self-referential number — but it lives *inside* Reading 1's
convention, not outside the Reading-1-vs-Reading-2 question. ~~It answers
a **different** open question (P52's free-coefficient stipulation,
partially) than the one P51 left open (which reading is correct) — two
logically independent open threads, now explicitly distinguished rather
than conflated.~~ **[CORRECTED after skeptic review]** the ceiling is
**consistent with, but does not itself validate,** the free-coefficient
stipulation P52's N1 rests on — a bound on the product `Ag²` says nothing
about whether `C,g,λ₄` are individually free to co-transform, which is
what that stipulation claims. Still logically independent of P51's
Reading question, just stated more precisely.

**[Added after skeptic review]** What this Part checks is only
**dimensional** invariance across readings: `[Ag²]` comes out as `[G_N]`
under both Reading 1 (`FINDING_P50B` Part 5) and Reading 2 (checked
directly: `[A]_R2=kg⁻¹m⁵s⁻⁴`, `[g²]_R2=m⁻²s²`, product `=kg⁻¹m³s⁻²=[G_N]`
— script assertion). The **numerical** value of the `β→Ag²` mapping under
a genuine Reading-2 re-derivation is **unexamined** — it could differ
non-trivially from `8.39×10⁻¹²`, not merely carry a different label.
Dimensional agreement across readings does not imply numerical agreement.

## Part 4 — what this connects, and what it does not

P52 found three weight-zero invariants for the committed monopole action:
`Ag²` (force strength), `gφ` (interaction — the same combination entering
P50A's `μ_metric=1−ĝφ̄`), and `λ₄A²` (self-interaction). **Only `Ag²` has
an external numeric handle** (this finding) — `gφ` and `λ₄A²` remain
completely unanchored, by any source, internal or external, found
anywhere in this project to date. A real asymmetry in the invariant
lattice's evidentiary status, not previously stated explicitly.

**Important negative result, stated precisely:** the `Ag²` ceiling does
**not** bound `μ_metric`'s deviation from 1 (`gφ̄`), because that requires
*both* splitting `Ag²` into `A` and `g` individually (P22 §4: not
established) *and* a value for `φ̄` (P52 Part 7: not determined, free
initial conditions). Two additional, unresolved unknowns — this finding
does not attempt to supply either.

## Part 5 — [SPECULATIVE, clearly conditional] an extra assumption's implication for `g` alone

**Not established anywhere in this project — flagged, not smuggled.** *If*
`A`'s numerical magnitude is order-1 in units of `G_N` (an additional,
unsupported assumption), then:

```
g² ≲ (Ag²)/G_N ≈ 0.126
g  ≲ 0.35   (dimensionless, Reading 1)
```

This is a scoping exercise only: it shows the `Ag²` ceiling is not
automatically in tension with P21's own working assumption that `g` is
dimensionless and presumably `O(1)`-ish — it does **not** validate the
`A~G_N` assumption, which has no independent support anywhere in this
project.

## Verdict [CORRECTED after context-blind skeptic review, Step 8a]

**M1 confirmed, conditional on `FINDING_P21`'s own S2 note
(coupling-vs-kinetic-term placement of `A` is convention-equivalent) plus
`FINDING_P50B`'s Part 5 dimensional derivation (`[A]=[G_N]` under Reading
1)** — not, as originally cited, P50B Part 4's two-route agreement, which
P50B's own skeptic pass already downgraded to "propagation-verification,
not independent derivation" (KG4 only partially satisfied). Citing the
wrong bridge at pre-correction strength was itself caught and fixed.
P22/P31's `Ag²≲8.39×10⁻¹²` (SI, Reading 1) is a **soft/conditional
ceiling under an explicit mapping** — not a direct experimental
measurement of MULTING's own `Ag²` — that applies to the *same* `Ag²`
that `FINDING_P52` proved is the field-redefinition-invariant
force-strength combination, though `A` plays a conceptually different
role in each finding (P21: fixed dimensional constant; P52: free
redefinition parameter). Both conventions give the same invariant, and
the constraint transfers either way, **carrying the same mapping-not-
measurement caveat throughout**. This is, in the specific sense P50B/P51/
P52 each said was missing, a genuine *external scale constraint* — it
comes from an independently-published paper's fifth-force bound (a
different physical mechanism entirely — DM-only coupling, not MULTING's
own universal coupling, per `FINDING_P22` §3), not from this project's
own internal rank/nullspace or dimensional-covariance machinery. That
external-ness is real; its precision and direct applicability are not.

**M3 holds regardless:** the ceiling does not resolve P51's separate,
still-open Reading-1-vs-Reading-2 question. Only dimensional invariance
across readings was checked — the numerical value of a genuine Reading-2
re-derivation is unexamined, not assumed equal to `8.39×10⁻¹²`.

**The ceiling is consistent with, but does not itself validate, the
free-coefficient stipulation P52's N1 rests on** — a bound on the product
`Ag²` says nothing about whether `C,g,λ₄` are individually free to
co-transform.

**Scope, stated precisely:** only one of P52's three invariants (`Ag²`)
has this external handle. `gφ` (hence `μ_metric`) and `λ₄A²` remain
completely unanchored. The `Ag²` ceiling does not, by itself, bound
`μ_metric`'s deviation from 1.

**Part 5's `g≲0.35` figure is explicitly speculative**, conditional on an
extra, unestablished assumption — not promoted to a project result.

## What this establishes, precisely

1. A genuine external (non-self-referential) numeric ceiling on `Ag²`
   already exists in this project (P21/P22/P31, 2026-08-13), and — for
   the first time — is shown to apply to the *specific* invariant `Ag²`
   that P52 (this session) proved is field-redefinition-invariant.
2. This satisfies the "new source of information, not a fourth internal
   variation" stop-rule condition reached after P52 — the anchor was
   already in the repo, just never connected to P52's result.
3. The invariant lattice from P52 has an asymmetric evidentiary status:
   `Ag²` has an external ceiling; `gφ` and `λ₄A²` do not.
4. Two previously-conflatable open questions (P51's Reading-1-vs-Reading-2,
   P52's free-coefficient stipulation) are shown to be logically
   independent — the P22/P31 ceiling is consistent with the latter
   (without validating it) and bears not at all on the former.
5. `A` plays a genuinely different conceptual role across findings (P21:
   fixed dimensional constant; P52: free redefinition parameter) — both
   converge on the same invariant `Ag²`, worth stating explicitly rather
   than treating the shared symbol as automatically the same object.

## What this does NOT establish

1. **A numeric value for `A` or `g` individually.** Only the product's
   ceiling.
2. **Any bound on `μ_metric`'s deviation from 1.** Requires both an
   `A`/`g` split and a value for `φ̄`, neither available.
3. **Resolution of P51's Reading-1-vs-Reading-2 question.** The ceiling is
   Reading-1-specific and does not test which reading is correct.
4. **Any anchor for `gφ` or `λ₄A²`.** Completely unanchored, unaffected by
   this finding.
5. **Validation of the Part 5 speculative `A~G_N` assumption.** Presented
   as a scoping exercise only, explicitly not a project result.
6. **Independent re-verification of `FINDING_P50B`'s own A-continuity
   result.** Reused, not re-derived — an honest limitation of this
   synthesis, stated in Part 2.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 2 (KG1 continuity: P21's `A` = P52's `A`, cited via `FINDING_P50B` Part 4's "two independent routes") | **WEAKENED — consequential, near-load-bearing** — P50B's own skeptic pass already downgraded that specific claim to "propagation-verification, not independent derivation"; citing it at pre-correction strength repeated the failure it was meant to avoid | **Fixed.** Re-cited via `FINDING_P21`'s S2 placement-equivalence note + `FINDING_P50B` **Part 5**'s dimensional derivation instead. Independently re-verified by re-reading `FINDING_P50B` in full before applying. |
| Part 1 (`8.39×10⁻¹²` arithmetic reproduction) | **CONFIRMED-REAL** — `4π×0.01×6.6743×10⁻¹¹=8.3870×10⁻¹²`, matches to <1% | No change. |
| P21-vs-P52 `A` as possibly different physical operations | **WEAKENED (conceptual clarity)**, not falsified — both give the same invariant `Ag²`, but `A` plays a fixed-constant role in P21 vs. a free-redefinition-parameter role in P52 | **Fixed.** Explicit note added to Part 2 and the Verdict. |
| Part 5 (`A~G_N` scoping arithmetic) | **CONFIRMED** arithmetic; framing borderline (no independent motivation for `A~G_N` anywhere in the project; risk of the `g≲0.35` figure being quoted out of context) | **Accepted as already-adequate** — `[SPECULATIVE]` tag and explicit "no independent support" language were already present; kept load-bearing. |
| M3 verdict language ("answers a different open question — P52's free-coefficient stipulation, partially") | **WEAKENED — overclaim** — an external bound on `Ag²` does not resolve whether `C,g,λ₄` are individually free; it neither validates nor undermines that stipulation | **Fixed.** Reworded to "consistent with, but does not itself validate." |
| M3 (Reading-1-specificity) | **WEAKENED — partial understatement** — only dimensional invariance of `Ag²` across readings was checked; the *numerical* value of a genuine Reading-2 re-derivation is unexamined, could differ non-trivially from `8.39×10⁻¹²` | **Fixed.** Explicit dimensional-vs-numerical distinction added to Part 3, with a script assertion verifying `[Ag²]_Reading2=[G_N]` (dimensions only). |
| Reliance on `FINDING_P31` as informal corroboration | **CONFIRMED handling** — already explicitly flagged as non-independent convergence (same conversion formula), not claimed as fresh confirmation | No change. |

**True kill assessment:** **no.** No claim's core predicate is false with
no viable fix. The central M1-conditional claim ("P22/P31's ceiling
applies to the *same* `Ag²` P52 proved invariant") survives — the
citation supporting it was wrong, not the claim itself, and a
better-supported citation was available and independently re-verified
before substituting it in. This is qualitatively different from P51's and
P52's true-kill-adjacent verdicts: there, the pre-registered test itself
could not discriminate its own alternatives; here, the test's conclusion
holds, only its stated justification needed replacing.

## Reproduction

```bash
python experiments/20260803-bridge/P53_ag2_external_anchor_synthesis.py
```
