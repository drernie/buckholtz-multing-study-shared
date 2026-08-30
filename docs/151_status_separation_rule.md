# docs/151 — Status Separation Rule: Empirical status ⊥ Interpretation status

**Date:** 2026-08-31
**L0 (EstimandOps):** this rule is itself descriptive (a documentation
convention), not a physics claim.
**Source:** cross-domain methodological transfer, proposed by the user
after reviewing a digest on quantum-foundations methodology (von
Neumann's no-go theorem history, Bell's theorem, decoherence,
formalism/interpretation distinctions). Evaluated for project fit
2026-08-31 — see `experiments/20260803-bridge/` session log; the
physics-specific parts of that source (institutional-monopoly
narrative, the "von Neumann decided consciousness causes collapse"
claim) were explicitly excluded as not transferable (genetic fallacy /
oversimplified history) and are NOT part of this rule.

## Why this rule exists

A recurring failure mode, independently rediscovered by this project
several times under different names (`FINDING_P163`/`P165`'s
`H0,anchor` degeneracy discussion; `FINDING_P170`'s own closing line,
"a good `H(z)` fit says nothing, by itself, about the growth/lensing-
level mechanism"): **a good empirical/model result gets silently read
as confirmation of the mechanism or causal story that motivated it.**
Quantum foundations has a clean, well-known instance of the same
failure — decoherence explains the *appearance* of classicality
(an empirical/formal result) without automatically settling *which*
physical mechanism picks a single outcome (an interpretation question).
The two questions are logically independent, and conflating them is a
known trap in that field. This project's own version of the same trap:
**parameter-identifiable ≠ causally identifiable.**

## The rule

Every claim's verdict block carries up to three separate status tags,
never collapsed into one:

```
**Empirical/Model status:** [does the math/fit/formalism hold up —
  use this project's existing evidence markers: VERIFIED / SUPPORTED /
  WEAKENED / REJECTED / etc.]
**Ontological/mechanistic interpretation status:** [is the PHYSICAL
  MECHANISM behind the fit established, or merely one candidate that
  produces the same numbers — OPEN / SUPPORTED / NOT-IDENTIFIED /
  REJECTED]
**Causal/cosmological claim status:** [is the CAUSAL CHAIN from the
  local mechanism to the claimed global/observable consequence
  established — NON-IDENTIFIED / IDENTIFIED / PARTIALLY-IDENTIFIED]
```

Omit a field only when it is genuinely inapplicable (a pure-math
lemma has no ontological or causal status); never omit it because the
answer is unflattering.

## Worked example (this project's own core claim)

> **Claim:** MULTING's 3-parameter curve fits 33 `H(z)` data points
> with `χ²=15.75` (`FINDING_P166`-`P169`).
> **Empirical/Model status:** SUPPORTED — positive-controlled,
> skeptic-reviewed 4 times (`P166`-`P169`), margin over a physically-
> empty dummy model survives GLS-covariance treatment.
> **Ontological/mechanistic interpretation status:** OPEN — whether
> "thermal energy sources a real repulsive gravitational dipole" is
> the actual physical mechanism, vs. an unidentified alternative that
> reproduces the same fit, is not established by the fit itself
> (`FINDING_P162`'s own no-go findings bear directly on this).
> **Causal/cosmological claim status:** NON-IDENTIFIED — that local,
> pairwise node interactions bottom-up *cause* the observed global
> expansion history (as opposed to merely reproducing its numbers) is
> not established; `FINDING_P133`'s own rank-deficiency result and
> `FINDING_P170`'s own H(z)-vs-growth decoupling argument are both
> directly relevant here.

## Integration with existing discipline

This does not replace anything already in place — it names and
standardizes a distinction this project's own conventions already
gesture at piecemeal:

| Existing mechanism | Relationship to this rule |
|---|---|
| `NO_AUTHOR_ERROR` | Already separates "this project's reconstruction status" from "TJB's own theory status" — a different axis, orthogonal to this rule, both apply simultaneously. |
| Every `FINDING_*.md`'s "What this file does NOT establish" section | Already does INFORMAL status separation in prose; this rule asks for it as three explicit, greppable header fields, not only prose. |
| `pearl_registry/INDEX.md` | Rows MAY carry an inline status note (e.g. "empirical: SUPPORTED / mechanism: OPEN") when a pearl's own value depends on the distinction — not mandatory to retrofit every existing row, only new ones where the distinction is load-bearing. |
| `estimand-ops.md`'s L0 gate (descriptive/predictive/causal) | Answers "what KIND of claim is this" before analysis; this rule answers "how confirmed is EACH LAYER of an already-analyzed claim" after analysis. Complementary, different stage. |

## Where to apply going forward

- New `FINDING_P<n>.md` files: add the three-field block to the verdict
  section, alongside the existing evidence-marker discipline.
- Not retroactive by default — existing `FINDING_P1`-`P170` files keep
  their current verdict format; retrofit only if a specific file is
  revisited for another reason.

## What this rule does NOT establish

1. Not a claim that any specific MULTING mechanism is right or wrong —
   purely a documentation convention preventing a specific silent
   conflation.
2. Does not replace the EstimandOps L0 gate — L0 classifies the
   question type before analysis; this rule tags confirmation strength
   per layer after analysis.
3. Three status tags are a minimum useful split, not a claim that
   exactly three layers exist for every claim — a genuinely 4-layer
   claim (formalism / empirical / ontological / causal, as in the
   source analysis) may need a fourth field; use judgment.
