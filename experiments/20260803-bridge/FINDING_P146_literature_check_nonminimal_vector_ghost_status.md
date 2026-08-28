# FINDING P146 — literature check resolves P145's two open operators
# specifically; Horndeski's own gauge-invariant term remains untested

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 literature
(Source Trace, `falsification-ladder.md` Step -4 — external claims, verified
against real papers, not asserted from memory)
**Verdict:** `NO-HEALTHY-MINIMAL-ESCAPE-AMONG-P145'S-CANDIDATES` — corrected
from an earlier draft's broader `NO-HEALTHY-MINIMAL-VECTOR-ESCAPE`, per
independent skeptic review (§0a below): the original verdict line
oversold what §6.2 itself already admitted (Horndeski's own gauge-invariant
term was never checked). This verdict applies **only** to `R_μνA^μA^ν` and
`(∇_μA^μ)²` — `P145`'s two candidates — not to the whole space of
non-minimal vector-curvature operators.
**Origin:** the "next cheap step" `P145` itself named: resolve `R_μνA^μA^ν`'s
sign/magnitude and `(∇_μA^μ)²`'s ghost status via literature check rather
than original derivation, per the user's own instruction this turn.

---

## 0a. Correction (same day, skeptic review) — read this first

An independent skeptic review of this file's source-trace disclosed its own
tool limitation up front (no WebSearch/WebFetch available to it that
dispatch) and, honestly, could not perform a true independent fetch — it
assessed plausibility from training-data familiarity instead, marking
results `[MEMORY-HIGH]`/`[UNVERIFIED-QUOTE]`/`[UNKNOWN]` rather than
pretending to have verified. Within that limit it still caught two real
issues, both fixed here:

1. **Marker honesty.** The Horndeski *exact formula* (§3, the three-term
   `F F R` combination) was obtained via a `WebSearch` synthesis, not a
   direct single-page `WebFetch` I personally read — it should carry the
   same `[VERIFIED-SYNTHESIS]` marker already honestly used for Claim B,
   not `[VERIFIED-QUOTE]`. Downgraded in §1/§3 below. The qualitative claim
   underneath it (Horndeski's admissible term is built from `F_μν`, never
   bare `A_μ`) remains well-supported — corroborated across multiple
   independent search results, and the gauge-non-invariance of
   `R_μνA^μA^ν` itself is directly checkable by hand (`§3` now shows the
   computation), not dependent on the exact formula's coefficients.
2. **Verdict-language overreach.** The original headline verdict read as
   if it closed the whole space of non-minimal vector-curvature couplings;
   §6.2 itself already said otherwise (Horndeski's own F-based term "not
   yet closed"). Fixed by narrowing the verdict label itself, not just the
   fine print — same class of error as `P143`/`P144`/`P145`'s own
   corrections: a narrow true finding stated with broader-than-earned
   verdict language.

**Independently re-verified, addressing the skeptic's biggest flagged
uncertainty:** Claim C (Hell 2024/2025) was re-fetched a second time,
independently, directly from `arxiv.org/abs/2403.18673` — confirmed real:
author Anamaria Hell, journal reference *Progress of Theoretical and
Experimental Physics* **2025**, 013E01, abstract opening matches what was
quoted in §5. This is now doubly `[VERIFIED-QUOTE]`, not resting on a
single fetch.

## 0. Method note

This step is a **Source Trace** (`falsification-ladder.md` Step -4), not a
derivation — every claim below is checked against a real, findable paper
(arXiv ID given), not recalled from training-data memory and presented as
fact. Confidence is marked per claim: `[VERIFIED-QUOTE]` (directly fetched
and quoted from the source), `[VERIFIED-SYNTHESIS]` (search-engine
synthesis across multiple hits, cross-checked but not directly quoted from
a single fetched page), `[WEAK]` (a single indirect source, stated as such).

## 1. Source register

| Claim | Source | Confidence |
|---|---|---|
| Horndeski (1976) derived the *unique* gauge-invariant, second-order (ghost-free) non-minimal coupling of a U(1) vector to curvature, built entirely from `F_μν` (qualitative claim) | Horndeski, *Conservation of Charge and the Einstein–Maxwell Field Equations*, J. Math. Phys. **17**, 1980 (1976); cross-confirmed via [arXiv:1308.1867](https://arxiv.org/abs/1308.1867) "Stability of Horndeski vector-tensor interactions" | Qualitative claim `[VERIFIED-SYNTHESIS]` (corrected from `[VERIFIED-QUOTE]` per skeptic review, §0a — corroborated across multiple independent search results, but the exact 3-term formula in §3 was not read from a single fetched page). The *logical* argument (`R_μνA^μA^ν` breaks gauge invariance) does not depend on the exact formula and is independently hand-verified in §3. |
| Generalized Proca theory: the most general local, ghost-free (3 physical d.o.f., 2nd-order EOM) massive-vector-tensor theory; curvature coupling and a `(∇·A)²`-type term are tied by a **fixed, non-free coefficient relation**, not independent operators; ghost-freedom requires a "special choice of coefficients" (Hessian degeneracy condition), not automatic | L. Heisenberg, *Generalization of the Proca Action*, [arXiv:1402.7026](https://arxiv.org/abs/1402.7026), JCAP **05** (2014) 015 | `[VERIFIED-SYNTHESIS]` — abstract-level synthesis, cross-checked across 2 independent search passes; exact Lagrangian coefficients not directly quote-verified from a fetched PDF (fetch attempts returned corrupted/unreadable PDF text) — see §4 caveat |
| Even a Generalized-Proca-consistent (ghost-free in the Ostrogradsky sense) non-minimal Proca-curvature coupling generically produces a **strong-coupling pathology** (longitudinal and tensor modes strongly coupled at the same scale, independent of how small the vector mass is) unless a further disformal compensating structure is added | A. Hell, *Unveiling the inconsistency of the Proca theory with non-minimal coupling to gravity*, [arXiv:2403.18673](https://arxiv.org/abs/2403.18673), PTEP **2025**, 013E01 | `[VERIFIED-QUOTE]` — abstract fetched and quoted directly, §5 below |

## 2. Novelty check (falsification-ladder.md Step -3)

Not a re-run of `P145` itself — `P145` explicitly deferred this exact
question ("likely via a literature check... rather than original
derivation") rather than attempting it. No prior entry in this project's
`null_results/INDEX.md` or `parked/INDEX.md` addresses non-minimal
vector-curvature couplings. Proceeding.

## 3. Finding A — if `A_μ` is a gauge field, `R_μνA^μA^ν` is inadmissible
## on symmetry grounds alone (decisive, no tuning question at all)

`P143`'s own baseline treated the vector mediator as coupling minimally to
a **conserved current** (`A_μJ^μ`) — the standard setup for a genuine U(1)
gauge field, where current conservation (`∂_μJ^μ=0`) is exactly what makes
the minimal coupling gauge-invariant. If `A_μ` in `P145`'s non-minimal
extension is the *same* gauge field, not a separately-introduced Proca
field, then Horndeski's own 1976 result settles the question outright:

> `I(g,A) = −¼(F_μνF^κλR^μν_κλ − 4F_μκF^νκR^μ_ν + F_μνF^μνR)`

is the **unique** local, second-order (ghost-free), *gauge-invariant*
non-minimal coupling of a U(1) vector field to curvature — built entirely
from the field strength `F_μν`, never from the bare potential `A_μ`.

**This part is independently hand-verifiable, not resting on the exact
formula's quote status:** under `A_μ → A_μ + ∂_μχ`,

```
δ(R_μνA^μA^ν) = R_μν(∂^μχ)A^ν + R_μνA^μ(∂^νχ) = 2R_μνA^μ∂^νχ
```

(using `R_μν`'s symmetry to combine the two terms). This is **not**
identically zero — it vanishes only in the non-generic special case
`R_μνA^μ=0` — so `R_μνA^μA^ν` genuinely is not gauge-invariant, confirmed
by direct computation, independent of which exact paper states Horndeski's
own admissible alternative. It is **not a legal operator in the
gauge-invariant sector at all** — not a question of tuning `λ`'s sign or
magnitude, it is excluded by symmetry before any dynamics is considered.

**Consequence:** `P145` tested the wrong operator, *if* `A_μ` is meant to
stay a gauge field consistent with `P143`'s own baseline. The
gauge-invariant alternative Horndeski's theorem actually licenses —
`F_μκF^νκR^μ_ν`-type terms — was not checked by `P145` at all. This is a
genuinely new, not-yet-closed candidate (§6.2 below), distinct from
anything in `P143`/`P144`/`P145`.

## 4. Finding B — if `A_μ` is Proca-type instead, `R_μνA^μA^ν` and
## `(∇_μA^μ)²` are not independent operators to begin with

If instead `A_μ` is treated as an already-massive Proca field (gauge
symmetry explicitly broken from the outset — a legitimate alternative
reading, since MULTING's own vector mediator was never established to be
gauge-invariant in the first place), a different, but equally decisive,
literature closes the question: Generalized Proca theory
(Heisenberg 2014) shows that a curvature-coupling term of this general
type and a `(∇_μA^μ)²`-type derivative term are **linked by the Ricci
identity** (`[∇_μ,∇_ν]A^ν = R_μνA^ν`, so integrating different orderings
of `∇A·∇A` by parts generates a curvature term with a coefficient fixed
relative to the derivative term's own coefficient) — they are not two
separate dials to turn, but one family with one free function.

**This retroactively sharpens a framing gap in `P145` itself:** treating
`R_μνA^μA^ν` (§3 there) and `(∇_μA^μ)²` (§5 there) as two *independent*
open operators, each with its own separate resolution, was already
somewhat imprecise — the correct literature ties them together. Recorded
here rather than silently, per this chain's own no-silent-correction
convention.

Crucially, ghost-freedom in this combined family is **not automatic for an
arbitrary coefficient** — Heisenberg's own result is that the
Ostrogradsky ghost is removed *only* for "a special choice of the
coefficients... through use of the degeneracy condition of the Hessian."
A generic, freely-chosen `λ` (as `P145` treated it) is *not* presumed
safe by this literature; it is presumed pathological unless it lands on
the specific degenerate combination.

## 5. Finding C — even the correctly-tuned combination is not automatically
## consistent: a further, generic strong-coupling pathology

Even granting the correct Generalized-Proca tuning (§4), Hell (2024/2025)
shows this is not the end of the story:

> "In the Minkowski background, this theory propagates five degrees of
> freedom... the non-linear coupling between the metric perturbations and
> the vector field indicates that both longitudinal and tensor modes
> become strongly coupled, at the same scale. This would imply that no
> matter how small the photon mass is, if non-minimal coupling is taken
> into account, gravitational waves would necessarily be strongly
> coupled." [direct quote, arXiv:2403.18673 abstract]

The fix requires introducing a **disformal** compensating structure on top
of the already-tuned Generalized-Proca combination — a further,
non-generic layer of structure, not a free parameter left over from `P145`
to simply set to a convenient value.

## 6. Verdict

**`NO-HEALTHY-MINIMAL-ESCAPE-AMONG-P145'S-CANDIDATES`** — corrected label
(§0a): this is narrower than "no non-minimal vector escape exists at
all." It closes exactly the two operators `P145` tested
(`R_μνA^μA^ν`, `(∇_μA^μ)²`) and explicitly leaves Horndeski's own
gauge-invariant term open (§6.2) — that exclusion is stated here, in the
verdict itself, not only in the fine print below. Read narrowly, exactly
as scoped:

- If `A_μ` is a gauge field: `R_μνA^μA^ν` is inadmissible by symmetry,
  full stop (§3). The gauge-invariant alternative (`F_μκF^νκR^μ_ν`-type)
  is a *different*, not-yet-tested candidate (§6.2 below) — this file
  does **not** close that door.
- If `A_μ` is Proca-type: `R_μνA^μA^ν` and `(∇_μA^μ)²` are not
  independent (§4); ghost-freedom needs a special, non-generic tuning
  (§4); even that tuning is not automatically fully consistent — a
  further strong-coupling pathology persists unless a disformal
  compensator is added (§5).

**Either reading disqualifies the operator P145 actually tested as a
*minimal* non-minimal vector operator** — per the user's own explicit
framing this session ("существует ли МИНИМАЛЬНЫЙ non-minimal vector
operator"). What survives, in both readings, requires additional
structure beyond a single free coefficient `λ`: either a completely
different operator (Horndeski's `F`-based term), or a precisely-tuned
combination plus a disformal fix. Neither is "minimal" in the sense the
user's own protocol asked for.

### 6.1 What this file DOES establish

1. `R_μνA^μA^ν`, as tested in `P145`, is not a viable minimal escape
   under either reading of what `A_μ` is.
2. `(∇_μA^μ)²`, as a freestanding operator (`P145`'s "genuine new
   physics" reading), is not independently well-defined — it is part of
   the same Generalized-Proca family as `R_μνA^μA^ν`, not a separate
   candidate with its own separate resolution.
3. This is a Source-Trace-backed closure, not a rushed derivation — three
   independent, real papers, cross-checked, point the same direction.

### 6.2 What this file does NOT establish — the one genuinely new,
### unclosed candidate this search surfaced

**Horndeski's own gauge-invariant term** —
`F_μνF^κλR^μν_κλ − 4F_μκF^νκR^μ_ν + F_μνF^μνR` — was not checked by
`P145` (which tested `R_μνA^μA^ν`, a different, non-gauge-invariant
operator) and is not checked here either (this file is a literature
closure of `P145`'s own candidates, not a new derivation). If `A_μ` stays
a gauge field, this is the natural next candidate for a `P147` power-
counting/sign check, analogous to `P143`'s own treatment of the minimal
coupling — genuinely new, not a repeat of anything in this chain so far.

### 6.3 Other scope limits

1. **Not a full literature review.** Three papers, chosen for direct
   relevance to the exact operators `P145` raised — not an exhaustive
   survey of vector-tensor EFT.
2. **The exact Generalized Proca coefficient relations (§4) are
   `[VERIFIED-SYNTHESIS]`, not `[VERIFIED-QUOTE]`** — PDF fetch attempts on
   Heisenberg (2014) and the follow-up "Beyond generalized Proca theories"
   paper returned corrupted/unreadable text; the qualitative conclusion
   (non-independence, special tuning required) is corroborated across
   multiple independent search passes and is standard, well-established
   physics in this literature, but the precise numerical coefficients
   were not directly quote-verified from a single fetched source.
3. **Does not touch MULTING itself** (Gate 1) — every operator discussed
   is this project's own candidate completion.
4. **Abelian only.** The gauge/Proca disjunction in §6 covers a `U(1)`
   vector, matching `P143`'s own baseline (`A_μJ^μ` for a scalar-charge
   current). A non-abelian internal index (`A_μ ∈ 𝔰𝔲(N)`) is not
   addressed, has no motivation from anything established in this
   project's own charge structure `(m_i, k_ir_i)`, and is left explicitly
   out of scope rather than silently assumed covered.
5. **Does not resolve `P142`'s overall verdict.** `P143` (derivative-cost
   for minimal vector coupling), `P144` (static-vector-dipole collapse to
   Branch S), and now `P146` (non-minimal vector-curvature couplings
   inadmissible/non-generic) together narrow the space further, but
   `P142`'s own decision tree (2-3 alternatives hitting the *same*
   obstacle) still has open threads: the two-scalar construction,
   TeVeS/Horndeski-scalar routes (`docs/123`'s own STILL-OPEN list), and
   now specifically Horndeski's *gauge-invariant vector* term (§6.2).
