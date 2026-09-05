# FINDING P199 — Provenance check (Gate 1/2): is `P196`-`P198`'s own
# `Δ=500` target actually grounded in v82 itself, or inherited unverified
# from another chat session's paraphrase?

**Date:** 2026-09-06
**Continues:** `P196`-`P198` (Girardi `R_vir` vs NFW `R200`/`R500`
residual investigation). First of a 5-step autonomous follow-up the user
authorized after reviewing the P198 close-out.
**Method:** `artifact-provenance-gates.md` Gate 1 (Artifact Identity) +
Gate 2 (Target Provenance) — re-check the load-bearing "v82 uses an
`R500`-type target" claim against v82's own text and code directly,
not against the external "handoff" document's paraphrase of it (the
handoff is a summary written by a *different* chat session, never
independently re-verified against the primary source before P196 built
on it).

## Why this check, first

`P196` chose `Δ=500` because "v82's own Section II.F explicitly says
'R500-type definition.'" That sentence was taken from the handoff
document, not independently re-checked against v82's own PDF/markdown
extraction or its supplemental code. Per this project's own
`artifact-provenance-gates.md`, a conversational description is not a
verified identifier — the cheapest possible check, run first, is to
grep the claimed source for the thing said to be in it.

## Method

`grep -n -i "R500|R_500|r_vir|virial radius|aperture"` against
`data/source_material/buckholtz_202608.0943v1.v82.md` returned **zero
hits** on the first pass — a real, if initially alarming, signal.
Broadened to `girardi|Rvir|radius` and re-read the matched lines with
full surrounding context (`data/source_material/buckholtz_202608.0943
v1.v82.md:325-624`).

## Result: CONFIRMED, not misattributed — plus one relevant bonus find

The zero-hit first pass was a markdown-table-extraction artifact, not
a real absence: the PDF→MD conversion splits "R₅₀₀" across lines/cells
("R -type" ... "500" ... "definition"), invisible to a literal-string
grep. Reading the surrounding prose directly (lines 351-353, 601-613)
confirms, verbatim, in v82's own words:

> "Radius is derived, not given an independent exponent: R₅₀₀-type radii
> are conventionally defined via mass and the critical density [15],
> ρ_crit(z) ≡ 3H(z)²/(8πG)..." (line 351-353)

> "Class III, circular: ... This applies to the node radius, r_X(z),
> when constructed via the standard R₅₀₀-type definition, in which
> radius is set by an assumed critical-density evolution,
> r_X(z)³ ∝ m_X(z)/ρ_crit(z), ρ_crit(z)=ρ_crit,0·E(z)². This directly
> assumes the Friedmann equation to build an input that then feeds the
> very force law whose purpose is to independently predict H(z). We
> flag this as the most serious residual dependence in the present
> computations..." (line 601-613)

**Verdict: `P196`'s `Δ=500` target selection is genuinely grounded in
v82's own explicit text, not an artifact of the handoff's paraphrase.**
The handoff's summary was accurate on this specific point. Gate 1/2
pass: the artifact identity (which quantity v82's `r_X(z)` actually is)
and its provenance (v82's own stated definition, Eq. 11:
`r_X(z)=r_0·(m_X(z)/m_0)^(1/3)·E(z)^(-2/3)`, self-similar/critical-
density form) are both independently confirmed against the primary
source, not inherited unverified.

## Bonus find, on-topic but not previously surfaced in this project

v82 **itself** classifies its own `r_X(z)` construction as "Class III,
circular" and "the most serious residual dependence in the present
computations" (v82 Sec. II.F, quoted above) — TJB's own paper already
states, in his own words, that this exact radius construction inherits
the Friedmann-equation assumption it is meant to test independently.
This is `[VERIFIED-arXiv-md-extraction]`, directly quotable, and
consistent with this project's own `docs/151` status-separation
discipline (an *Empirical* fit is not thereby an *Ontological* claim) —
worth keeping in view for any future correspondence, though drafting
one is out of scope here (`NO TJB correspondence` unless separately
requested).

## What this does and does NOT establish

1. **Does** confirm `P196`-`P198`'s target selection (`Δ=500`) was not
   a misattribution or chain-of-custody error from the handoff.
2. **Does NOT** explain the `1.47×` Girardi-vs-NFW residual — this
   check was about whether we are comparing the *right quantity*, not
   about why the comparison disagrees. It closes off one candidate
   explanation for the whole investigation (a wrong target definition)
   without opening a new one.
3. **Does** sharpen the real open question for the next steps: v82's
   own `r_X(z)` is a *purely theoretical*, self-similar `R500`
   construction (mass + critical density only, Eq. 11) — it is not
   itself an independent *empirical* measurement. Girardi's `R_vir(σ)`
   is a completely different, independent, empirically-calibrated
   virial-theorem estimator. Comparing them tests whether two
   different mass/radius *proxies* for the same clusters agree — a
   question with a large, well-established literature on virial-mass-
   estimator systematics that this project has not yet consulted. That
   literature check is the natural next step (see `FINDING_P200`).
4. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   and source-verification discipline, not a claim about v82's
   correctness (v82's own Class III self-flag is TJB's own statement,
   quoted, not this project's assessment).
