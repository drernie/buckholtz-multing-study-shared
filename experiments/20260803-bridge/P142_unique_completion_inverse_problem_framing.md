# P142 — Unique-completion inverse problem: framing only (no derivation yet)

**Date:** 2026-08-26
**Bottleneck:** #2 (Unique completion), per `docs/147` — explicitly NOT bottleneck 4
(IC-sensitivity, closed today as `BOTTLENECK-4-NATURAL-CLOSURE`). This P-number
continues the bridge-campaign's own numbering sequence but targets a different,
still-OPEN bottleneck; no reopen condition from `docs/147` bottleneck 4 applies here.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0: descriptive/structural

---

## Zero-Signal Gate (falsification-ladder.md Step -5)

- **Entity:** local, Lorentz-invariant, ghost-free covariant field theories whose
  weak-field limit reproduces `F_oP`'s established bilinear structure (docs/125) and
  the derived alternating-sign rule (`FINDING_two_charge_completion.md`).
- **Falsifiable predicate:** the admissible class of such theories is FINITE and SMALL
  (1-2 inequivalent classes up to field redefinition) vs. an unbounded family.
- **Measurable outcome:** an explicit operator-basis enumeration, truncated at a
  stated EFT order, checked against the weak-field matching constraint that already
  falsified `CANDIDATE-L1` on the EP axis (`docs/131`).

All three present → gate passes, not `REFUSE`.

## EstimandOps L0

**Question type: Descriptive/structural**, not causal, not predictive in the
empirical-ML sense. This is a mathematical classification question (what field
theories are compatible with an established structure under stated symmetry/
consistency constraints), not a population-level empirical estimate — the standard
EstimandOps L1 attributes (population, intervention, comparator, summary measure)
do not map cleanly onto it, per `falsification-ladder.md`'s own Structure-Bias Guard
(reasoning-heavy/structural steps should not be forced into an empirical-estimand
template that does not fit). Natural-language statement instead:

> *"We ask whether the space of local, ghost-free, Lorentz-invariant covariant
> completions reproducing `F_oP`'s weak-field limit is narrow (1-2 classes) or wide
> (unbounded family), given the constraints already established this campaign."*

**What this does NOT mean:** it is not a claim that TJB's own (possibly unpublished)
construction is one of the classes found; it is not a re-derivation of `CANDIDATE-L1`;
it does not resolve whether MULTING's own repulsive dipole is physical — only whether
the SPACE of candidate completions consistent with the established local structure is
tractable to enumerate at all.

## Why this question is well-posed now, and wasn't before today

Three prerequisites, all satisfied only as of this session:
1. `F_oP`'s exact bilinear structure is established (docs/125, P1, pre-existing).
2. `docs/123`'s own P0 unknown (is the dipole a true vector?) is resolved from source
   text (today, this session) — an operator-basis enumeration would have been
   premature while this was open, since the answer changes which operators are even
   candidates.
3. `CANDIDATE-L1`'s EP-tension (docs/131) gives a concrete, checkable discriminant:
   any new candidate class either reproduces the same tension (informative — the
   tension is structural, not an artifact of one ansatz) or avoids it (informative —
   a genuinely new completion class, worth pursuing further).

## Cheapest differentiating test (per CDT Protocol, falsification-ladder.md)

**NOT** a full EFT operator-basis classification (expensive, high risk of getting
lost in an open-ended enumeration — exactly the "moonshot" category `docs/123`'s own
portfolio structure warned against pursuing first).

**Instead:** enumerate 2-3 alternative simple ansätze reproducing the SAME weak-field
limit as `CANDIDATE-L1` (e.g., a vector-mediated construction instead of scalar; a
two-scalar construction instead of one-scalar-two-charge; a construction with a
non-standard kinetic term) and check ONLY whether each hits the same EP/ghost/
staticity tension `docs/131` found, or avoids it.

- **If all tested alternatives hit the same tension:** strong evidence the tension is
  structural (a consequence of reproducing a repulsive dipole per se), not an
  artifact of one construction choice — this would be a genuinely new, stronger
  result than `docs/131` itself claims (which explicitly scopes itself to one
  attempt, `docs/139` R-5).
- **If at least one alternative avoids it:** a concrete new completion candidate,
  worth a full weak-field matching check (repeating `docs/131`'s own protocol on the
  new ansatz).
- **Kill condition for this whole sub-question:** if 2-3 obvious alternatives are hard
  to even construct compatibly with the established bilinear structure (docs/125),
  that itself is informative — narrows toward "the admissible class may be exactly
  1" rather than requiring a wider search.

## What this file does NOT do

Does not attempt the derivation itself — framing only, per the user's own explicit
request to run this "in turn" (по очереди) after the TJB-report drafting step, not
simultaneously with it. Does not touch bottleneck 4 (closed, session STOP still in
force). Does not touch `F→H_MULT(z)` (bottleneck 1, external-blocked). Does not
quote any `k[h/Mpc]`. Does not touch MULTING itself (Gate 1) — both the two-charge
completion and any alternative ansatz are this project's own construction.

## Next step (not started here)

Actually construct 2-3 alternative ansätze and run the cheapest test above. This is
real derivation work, not a continuation of today's framing pass — a fresh session
context (or at minimum a fresh turn budget) is the right place for it, per this
project's own discipline against cramming heavy derivation onto an already-long
session (today: full radar, 53-card re-score, contradiction-scan, claim-decomposer,
TJB letter draft, this framing — six substantial deliverables already).
