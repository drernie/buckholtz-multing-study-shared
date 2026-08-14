# P33 — MULTING's own monopole coupling has the same matter-sector functional form as a mass-varying (conformally-coupled) scalar; the gravitational-sector consequences of that literature class are NOT thereby established for MULTING

**Date:** 2026-08-14
**Status:** **CORRECTED after context-blind skeptic review, same day.** The
original title claimed a "literature-grounded classification" that
"strengthens P32's Part B." Five sub-claims were WEAKENED on review (none
core-predicate-false — the surviving structural observation is real, see
§2). The most consequential correction: §3's original text imported
gravitational-sector consequences (metric field equations "remain standard
GR") from a fully-specified literature theory onto MULTING, whose own
action has no gravitational sector at all — the same "same-looking
prefactor ⇒ same physical conclusion" pattern already caught twice this
session (`FINDING_P29`, `FINDING_P31`). Full verdict in the new §5 below.
Original text below is preserved with corrections applied in place
(struck-through where withdrawn, replaced where narrowed) rather than
deleted, per this session's standing correction discipline.

**Origin:** the first well-scoped step toward the full covariant-action
derivation the mechanism-frame gate (`FINDING_P32`) ultimately needs. Rather
than attempt the full `S→` Einstein equations + scalar equation + matter
equation → `μ(a,k),γ(a,k),Σ(a,k),G_matter(a,k)` extraction in one pass —
real, substantial GR work this project has explicitly and repeatedly
deferred (`FINDING_P30`, `FINDING_P32`) to avoid rushing under time
pressure — this finding answers a cheaper, well-posed sub-question first:
is MULTING's own coupling a *recognized* type in the scalar-tensor
literature, with already-established consequences?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P33_covariantize_mass_varying_classification.py`

## 0. Honest scope, stated before anything else

This finding does **not** derive Einstein's equations, does not linearize
the metric around FRW, and does not extract `μ`, `γ`, or `Σ` directly. It
establishes a **classification** — which standard family of scalar-tensor
coupling MULTING's own action belongs to — and cites that family's
*already-established*, textbook-level consequences from real literature.
This is evidence toward resolving the mechanism-frame gate, not a
resolution of it; the full derivation remains the larger, deferred next
step (§4).

## 1. Method

~~`two_field_action_closure.py`'s own monopole sector: a standard
relativistic kinetic term `−mc∫dτ` plus the already-established interaction
term `+g·m·φ∫dτ` (both re-verified this session). Summed:`~~

**[CORRECTED]** The claim that the `−mc∫dτ` kinetic term was "re-verified
this session by direct re-read of `two_field_action_closure.py`" was
**false**, caught by skeptic review and independently re-confirmed before
accepting the correction (`grep -n "R\b|Einstein.Hilbert|Ricci|sqrt(-g)|g_{munu}|metric"
two_field_action_closure.py` → zero matches; separately, the file contains
no standalone matter-kinetic term anywhere). `two_field_action_closure.py`
contains only the scalar field's own kinetic term `(1/2)(∂φ)²` and the
worldline interaction terms (`g·mᵢ·φ` monopole, `pᵢ·∇φ` dipole). The
`−mc∫dτ` term is a standard, textbook-obvious assumption **this finding
supplies** — any sensible relativistic point particle needs one — not
something read from the source. Only the interaction term `+g·m·φ∫dτ` is
genuinely present in the source and was genuinely re-verified.

This finding's own constructed sum:

```
S_total/dτ = −m·c + g·m·φ
```

Factored to expose a mass-varying-particle form (`S = −c∫dτ·m_eff(φ)`):

```
m_eff(φ)/m = (c − g·φ)/c = 1 − (g/c)·φ
```

**Exact, not an approximation** — the original coupling term was already
linear in `φ`, verified symbolically (consistency check: zero difference
between the factored and original forms).

## 2. Result — covariantization and classification

The covariant form replaces flat-space `dτ` with proper time along the
particle's worldline in the (possibly curved) metric `g_μν`:

```
S_i = −c∫dτ_curved · m_eff(φ(xᵢ)),   m_eff(φ) = m·(1 − (g/c)·φ)
```

Manifestly a scalar (covariant) action, reducing exactly to ~~the known
flat-space form~~ **[CORRECTED] this finding's own constructed flat-space
form (§1)** when `g_μν→η_μν` — not to a term-for-term transcription of the
source's own bracket, which also contains the separate dipole term
`pᵢ·∇φ`, scoped out here (legitimately, matching every prior finding in
this sub-arc, but the scoping itself does not make the result "the known"
form as if uniquely sourced). This is precisely the structure of a
**mass-varying / conformally-coupled scalar** — matter built from a
conformally-rescaled ("Jordan-frame") metric `g_μν = A(φ)²·g̃_μν`, with
`A(φ)≈1+α·φ` to linear order. Identifying MULTING's own coupling with this
standard form (elementary symbol-matching on a linear equation — not an
independent verification of any physics claim, see §5 point 5):

```
α = −g/c
```

This algebraic identification is exact and survives the correction below.

## 3. What the literature quote is, and is NOT, evidence for

**[CORRECTED — the consequential fix.]** The original version of this
section moved directly from "MULTING's coupling matches the standard
conformal-coupling functional form (§2)" to "therefore MULTING's own
metric field equations remain standard GR, with an extra fifth-force term
only in matter's equation of motion" — importing a **gravitational-sector**
consequence from a literature class onto MULTING. That step does not go
through, independently re-verified before accepting the skeptic's
correction: `two_field_action_closure.py` has **zero matches** for any
gravitational-sector content (`grep` for Einstein-Hilbert / Ricci scalar /
metric determinant / `g_μν` — nothing). "Jordan frame" and "Einstein
frame" are two *descriptions of one fully-specified theory*, whose data
includes the metric's *own* gravitational action (an Einstein-Hilbert term
or equivalent). MULTING's action, as reconstructed throughout this
project, specifies **no gravitational sector at all** — it is a scalar
field's own kinetic term plus its worldline coupling to matter, nothing
else. So the quote below is accurate evidence about *arXiv:1804.07180's
own theory*, which does have both frames properly defined — it is **not**,
without an additional, separately-justified assumption this finding does
not supply, evidence about MULTING.

**[VERIFIED-WEBFETCH, accurate as a transcription of the cited paper —
NOT thereby evidence about MULTING, see correction above]** Direct quote,
arXiv:1804.07180 ("Fifth forces, Higgs portals and broken scale
invariance"), their eq. 1:

> "The SM degrees of freedom {ψ} move on geodesics determined by the
> Jordan-frame metric g_μν=A²(χ)g̃_μν"

— i.e., in *that paper's fully-specified theory*, matter moves on a metric
*conformally related to, but not identical to*, the canonical
Einstein-frame metric `g̃`, whose own field equations are the standard
ones that theory builds on. Nothing here establishes that MULTING *has* an
Einstein-frame metric with standard field equations — that would require
MULTING to specify a gravitational sector, which it does not.

**[WEAK, and now doubly so]**: the further claim (that in this literature
class the Einstein-frame metric's own field equations take standard,
unmodified GR form, with matter picking up the extra fifth-force term
instead) was already marked `[WEAK]` in the original version for a
different reason (WebSearch-synthesized, not pinned to one direct quote).
It now carries a second, more fundamental weakness: even at `[VERIFIED]`
strength, it would still be a claim about the *cited paper's* theory, not
about MULTING, for the reason given above.

**Narrowed consequence for `FINDING_P32`'s Part B:** what survives is the
**structural functional-form match** itself (§2: `α=−g/c`, exact) — MULTING's
monopole coupling, IF supplemented by a standard kinetic term, has the same
matter-sector algebraic shape that conformally-coupled matter has in a
standard scalar-tensor theory's Einstein frame. This is a real, narrow,
worth-recording observation. It does **not** strengthen `FINDING_P32`'s
Part B with an additional, independent, literature-grounded argument the
way the original text claimed — `FINDING_P32`'s Part B (the
kinetic-term-mismatch argument, which needs no assumption about MULTING's
unspecified gravitational sector) remains the stronger, self-contained
point. This finding is now best read as a smaller, more conditional
*supplement* noting a suggestive structural parallel, not an independent
strengthening.

## 4. What this does NOT establish

1. **Einstein's equations for MULTING's own completion.** No
   Einstein-Hilbert term has been added, no metric perturbation performed.
   This finding classifies the *matter-sector* coupling only.
2. **That MULTING's own construction actually follows the standard
   conformally-coupled template beyond the point-particle level.** The
   classification match is exact at the level of a single point particle's
   worldline action (§2) — whether this extends cleanly to the full
   multi-particle, field-theoretic completion (with `φ`'s own dynamics,
   backreaction, and the still-unaddressed dipole/`κ` sector) is not
   verified here.
3. **A quantitative bound or formula for `μ(a,k)`, `γ(a,k)`, or `Σ(a,k)`.**
   Only a qualitative classification and its known consequences.
4. **The literature-consensus claim (§3, `[WEAK]`) at `[VERIFIED]`
   strength.** Two further WebFetch attempts at a single, cleanly-quotable
   canonical source (a review paper's abstract, and a frame-equivalence
   paper's abstract) both returned insufficient detail — the broader claim
   rests on WebSearch-synthesized consensus plus one direct structural
   quote, not two independent direct quotes of the exact same statement.
5. **A resolution of `FINDING_P32`'s mechanism-frame gate.** This is
   evidence toward resolving it, via a cheaper route than a full
   derivation — not the resolution itself. The full covariant-action
   derivation (Einstein equations + scalar equation + matter equation,
   simultaneously) remains the larger, deferred next step, per the same
   caution `FINDING_P30`/`FINDING_P32` already stated.
6. **Anything about `κ`.** Entirely about the monopole (`g`) sector,
   matching every prior finding in this sub-arc.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   P1's action and a published external literature classification — not a
   claim about TJB's own unpublished theory.
8. **[ADDED after correction] That MULTING has, or is assumed to have, any
   particular gravitational sector at all.** §3's original text implicitly
   assumed MULTING's own metric field equations would be "standard GR" —
   this is not established anywhere in the action as reconstructed by this
   project, and this finding does not supply that assumption. Whatever
   MULTING's gravitational completion turns out to be (if TJB's own theory
   specifies one) is fully open.

## 5. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with `claim.md`-equivalent content (this finding, pre-correction)
+ the script, **no session history**, per Falsification Ladder Context
Asymmetry Rule. Five sub-claims, each judged independently, none
core-predicate-false:

| # | Sub-claim reviewed | Verdict | Disposition |
|---|---|---|---|
| A | `−mc∫dτ` kinetic term "re-verified this session by direct re-read" of the source | **WEAKENED** | False evidentiary claim — independently re-confirmed absent from source via grep; term relabeled as a supplied, standard assumption (§1) |
| B | "Reduces exactly to the known flat-space form" | **WEAKENED** | Conflated this finding's own constructed sum with the source's own (larger) bracket; relabeled as this finding's own construction (§2) |
| C | Literature classification's gravitational-sector consequences ("metric equations remain standard GR") transfer to MULTING | **WEAKENED (most consequential)** | Requires MULTING to have a specified gravitational sector, independently re-confirmed via grep that it has none; same "same-looking prefactor ⇒ same conclusion" pattern already caught in `FINDING_P29`/`FINDING_P31` — this reviewer was explicitly asked to check for it (§3 rewritten) |
| D | `[VERIFIED-WEBFETCH]` marker implies the quote is evidence about MULTING | **WEAKENED** | Marker split: quote accuracy `[VERIFIED-WEBFETCH]` vs. relevance-to-MULTING unestablished (§3) |
| E | Sympy steps (distribution, `sp.solve` coefficient match) constitute independent verification | **WEAKENED** | Elementary algebra dressed as substantive checks — fourth occurrence this session (after P26, P29, P30) and a **regression** from `FINDING_P32`'s own already-applied fix minutes earlier the same day; script docstrings and print statements now carry the same disclaimer P32 uses |

**What survives:** the exact algebraic identification `α=−g/c` (§2) —
MULTING's monopole coupling, if given a standard kinetic term, has the
matter-sector functional form of a conformally-coupled scalar. **What does
not survive:** the evidentiary claims about what was "verified" from the
source, and the transfer of gravitational-sector literature consequences
onto a theory (MULTING) that has no gravitational sector specified. Kill
classification: framing/scope, not core-predicate-false — matches the
pattern of every other correction this session except `FINDING_P31`'s
mechanism-frame correction, which changed a numeric bound's interpretation
rather than just framing.

## Reproduction

```bash
python experiments/20260803-bridge/P33_covariantize_mass_varying_classification.py
```
