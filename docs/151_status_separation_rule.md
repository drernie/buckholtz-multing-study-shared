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

## First worked example (this project's own core claim)

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

## Second worked example (2026-09-12 — Bottleneck 1 / P223 / P158
## magnitude-mechanism branch)

> **Claim:** this project's own S-S population closure (`docs/127`)
> does not constrain v82's own single-pair bridge (`P223`), and v82's
> own Jensen's-gap population-averaging correction (`P158`) is
> directionally safe (`rho > -0.5`).
>
> **Empirical/Model status:** SUPPORTED, with real caveats, on two
> separable sub-claims.
> (a) `P223`: `H1`/`H2` CONFIRMED (v82's own literal Eqs. 1-9 keep
> `k_A(z)`-dependence, independently verified via a positivity
> argument, not merely asserted; `docs/127`'s own `G_alpha_beta=0` is
> independently reproduced exactly for the same power-law shapes);
> `H3` NARROWED after a Step 8a skeptic pass — "categorically separate
> questions" holds only under the literal reading of v82's own Eq. 8,
> not as an unconditional claim about all possible readings.
> (b) `P158` magnitude/mechanism: three independent, real-data rho
> measurements (`TNG300`, `Magneticum`, `FLAMINGO`) — the first two
> FALSIFIED as resolving tests by two separate skeptic passes (a
> nested-threshold look-elsewhere trap, caught twice); the third
> (`FLAMINGO`, `N=1200`, one pre-registered threshold, `~114x` [CORRECTED
> 2026-09-12: actually `~36x`, arithmetic error, no effect on any
> reported number] `TNG300`'s
> volume) gave the first WELL-POWERED result in this thread:
> `rho=-0.0231+/-0.0359`, excluding `rho<-0.5` at `~13 sigma`. The
> companion claim that `rho` is LARGE and positive (`TNG300`'s own
> `+0.38` all-pairs reading) is NOT supported for the true-nearest-
> neighbor observable specifically — a skeptic-caught correction:
> true-NN pairs and all-pairs-in-a-band are different observables
> (Gate 1, Artifact Identity), not the same question at two scales.
>
> **Ontological/mechanistic interpretation status:** OPEN. `P223`'s
> `H3` does not establish which (if either) construction — v82's own
> single-pair kinematics, or this project's own S-S population closure
> — correctly describes real cosmic structure; it only shows the two
> are not in logical contradiction under a specific literal reading.
> Separately, and more basically: WHICH real halo population
> corresponds to v82's own abstract "characteristic node" is itself
> unresolved — all three rho-check `FINDING` files name this same open
> mapping question and none of them (nor `P223`) attempts to close it.
> Whether the measured near-zero `rho` reflects real cosmic-structure
> physics or an artifact of the top-N-by-mass selection procedure used
> to reach the target scale (`pearl_registry`, 2026-09-12) is also not
> settled.
>
> **Causal/cosmological claim status:** NON-IDENTIFIED. Nothing in this
> branch establishes that v82's own bottom-up single-pair kinematics
> *causes* the observed expansion history, nor that this project's own
> S-S closure route causally describes real structure formation — both
> remain formal/reconstruction-level comparisons. `NO_AUTHOR_ERROR`:
> this status block is about this project's own reconstruction chain,
> not a claim about v82's own physical theory.

## [2026-09-12 correction, same day, not a rewrite]

The Second worked example above's `"excluding rho<-0.5 at ~13 sigma"`
phrasing is **WITHDRAWN** — caught by the user, not self-caught. It
divided the distance to `-0.5` by a permutation-null SD (correct for
testing `H0: rho=0`), not the standard error the composite hypothesis
`H0: rho<=-0.5` actually needs (sampling variance of a correlation
coefficient is not constant in `rho`). A follow-up addendum (spatial
block-jackknife CI, plus a second `rho_band` observable on the same
subsample) confirms the qualitative conclusion — `rho<=-0.5` excluded
by a wide margin, now corroborated by three independent SE estimates —
but retracts the specific sigma-count as unsupported this far into a
tail on non-i.i.d., spatially-clustered data. This is itself a clean
illustration of `docs/151`'s own rule: the Empirical/Model line
("SUPPORTED, with real caveats") was already correctly hedged before
this correction; only the specific numeric precision inside it needed
walking back, not the status tag itself. Full account: `experiments/
20260909-tng-mass-assortativity/FINDING_flamingo_addendum_jackknife_
band_closure.md`.

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
