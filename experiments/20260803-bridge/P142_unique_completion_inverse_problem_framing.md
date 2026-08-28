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

## Update, 2026-08-26 (same day, user said "продолжай P142") — first alternative done

**`P143`** (`FINDING_P143_vector_mediator_powercounting.md`) — the first of the
2-3 alternative ansätze, chosen because it was the one residual branch `docs/131`
argued qualitatively rather than computed (vector-mediated, not scalar). Result:
`VECTOR-MONOPOLE-ROUTE-REQUIRES-AT-LEAST-ONE-EXTRA-DERIVATIVE` — a positive-
control-tested (exponent AND coefficient, exact match to the textbook Newton/
Coulomb `1/(4π)` normalization) Riesz-potential power-counting derivation, upgrading
`docs/131`'s vector-mediator dismissal from asserted to derived, but only for its
*first* premise (the derivative-count requirement) — an independent skeptic review
caught an early-draft overreach conflating "≥1 extra derivative" with Ostrogradsky
"higher-derivative", corrected same-day (see `FINDING_P143` §3a).

**Reading against this file's own decision tree (§ above):** this is one data
point, not yet a verdict — one alternative construction (vector, monopole-order)
hits a DIFFERENT obstacle (derivative-coupling cost) than the scalar branches
(EP-tension), at an EARLIER stage (can't even reach the right power law cheaply,
before the sign question is even asked). Consistent with, not yet proof of, the
"tension is structural across constructions" hypothesis — the specific obstacle
differs by construction class, which is itself informative but not the same as
2-3 alternatives all hitting literally the SAME EP-tension. 1-2 more alternatives
(e.g. a two-scalar construction, or the still-open TeVeS/Horndeski routes named in
`docs/123`'s own STILL-OPEN list) needed before this file's decision tree can be
honestly applied.

## Update, 2026-08-26 (same day) — P144, a search-space narrowing step

Before building a third numerical alternative, `P144`
(`FINDING_P144_static_mediator_scope_narrowing.md`) asked a cheaper question
first: does `docs/131`'s "vector/antisymmetric sector" residual branch name
one open alternative, or several distinct ones — and are they all genuinely
untested? Two reasoning-based arguments (no new numerics — a
structural/logical finding, same class as `FINDING_P139`):

- A tensor/2-form mediator at monopole order would repeat `P143`'s own
  `Δα=1` conclusion (spin-independent power-counting fact), or has no
  natural minimal point-source coupling at all — not a genuine third
  alternative either way.
- A vector field entering at dipole order, given MULTING's dipole is
  source-confirmed *static* (`docs/131` line 68), reduces to Branch S's own
  `cosθ` angular structure (a static source has no vector/magnetic
  character to give it a genuinely different sign-preference) — collapses
  into the already-tested EP-tension, not a new escape.

Leaves one specific, still-untested candidate: a **non-minimally-coupled**
vector construction (vector structure engineered without relying on source
motion) — not yet attempted, likely to inherit a `P143`-style
derivative-coupling cost of its own, per this file's own scope note.

**Status: independent context-asymmetric skeptic review CONFIRMED** the
bottom line (all `docs/131` quotes verified exact, all physics re-derived
independently, no missed escape route). Three precision repairs applied
same-day — none changed the conclusion. Matches this project's own
precedent (`P143` §3a) of not
treating a reasoning-heavy physics claim as final before independent
context-asymmetric check.

## Update, 2026-08-26 (same day) — P145, the operator-basis gate on P144's
## one surviving candidate

Per the user's own explicit, detailed protocol (a cheap structural gate
before any full numerical construction): `P145`
(`FINDING_P145_nonminimal_vector_operator_gate.md` +
`P145_nonminimal_vector_operator_gate.py`) classified the user's 4 proposed
non-minimal vector operators (`A_μJ^μ`, `F_μνF^μν`, `R_μνA^μA^ν`,
`(∇_μA^μ)²`) against 6 admissibility criteria, added one more (a
magnetization-current coupling, directly motivated by `P144`'s own flagged
"static = steady-state, currents permitted" loophole), and computed the two
candidates that survived qualitative filtering:

- `R_μνA^μA^ν`: **closed by computation** — linearized Ricci tensor
  verified (sympy) to vanish identically in the two-body static vacuum
  configuration (positive control: `∇²(1/r)=0` for `r≠0`).
- Magnetization-current (permanent-dipole) coupling: **closed by
  computation** — dipole-dipole interaction energy's global minimum
  (verified both symbolically and by an 8M-point numerical grid-search
  robustness check) is the attractive "head-to-tail" configuration; the
  repulsive "head-to-head" configuration is the unstable energy maximum —
  same qualitative structure as `docs/131`'s own Branch S, for a genuinely
  different angular form.
- `(∇_μA^μ)²`: **left explicitly unresolved** — splits into a
  gauge-artifact reading (no new physics) and a genuine-physics reading
  whose ghost-freedom needs a literature-grounded or constrained-Hamiltonian
  check this step's own "cheap gate" scope doesn't cover; not force-closed.

**Correction (same day, independent skeptic review): the `R_μνA^μA^ν`
closure was WRONG.** The skeptic caught the error precisely — checking
`R_μν=0` for `r≠0` verifies vacuum Ricci-flatness *away* from a source, but
`R_μν` is proportional to `T_μν` by the field equations themselves and has
delta-function support *at* each source (`R_00=4πGMδ³(x)`). Evaluating the
operator's contribution properly (independently re-derived, not just
accepted — divergence-theorem check confirms the delta-function
normalization) gives a genuine `1/r³` force with a *free-sign* coupling
`λ` — the target power law reached directly (`Δα=0`), not zero at all.
Separately, the magnetization-current closure (§4) was WEAKENED: it closes
a *dipole-dipole* configuration, not a matched re-test of `docs/131`'s own
*monopole-dipole* Branch S — a qualitative parallel, not an equivalence.

**Corrected verdict: `TWO-OPERATORS-OPEN`**, not `NO-HEALTHY-VECTOR-ESCAPE`.
`R_μνA^μA^ν` (sign AND magnitude of `λ` unconstrained by anything
established) and `(∇_μA^μ)²` (ghost status unresolved) both remain
genuinely open — neither closed, neither confirmed as a working escape.
Next cheap step before `P146`: resolve these two via literature check
(EFT positivity bounds; Einstein-aether-type no-ghost conditions), not
original re-derivation. Both files corrected in place, same-day, per this
project's own no-silent-correction convention (matches `P143` §3a, `P144`
§0/1a).

**Second, independent skeptic review of the corrected version: CONFIRMED
survives.** Fresh context, re-derived `R_00=4πGMδ³(x)` two independent
ways, confirmed the interaction-potential arithmetic line-by-line, found
no overclaim in the verdict language, confirmed the dipole-dipole caveat
on §4 is material (stated 4 times) not token. Found 3 additional
presentational gaps, none verdict-changing, folded in same-day: (1) the
calculation only used one of two symmetric curvature-times-field terms
(doubling coefficient, not changing power law/sign); (2) self-force/
renormalization structure (standard point-particle EFT, doesn't undermine
the result) named explicitly; (3) `λ`'s natural EFT magnitude (dim-6
operator, `λ~1/M²` suppression) added as a **third** open axis alongside
sign and ghost-freedom — "reaches the power law" ≠ "reaches the target
magnitude." `P142`'s decision tree: two operators genuinely open, neither
a confirmed escape, neither justifies `P146` yet.


## Update, 2026-08-26 (same day) — P146, literature check resolves both
## open operators (via Source Trace, not derivation)

Per `P145`'s own recommendation and the user's explicit instruction:
`P146` (`FINDING_P146_literature_check_nonminimal_vector_ghost_status.md`)
runs a proper Source Trace (`falsification-ladder.md` Step -4) against 3
real papers — Horndeski (1976, J. Math. Phys. 17, 1980), Heisenberg
(2014, arXiv:1402.7026, Generalized Proca), Hell (2024/2025,
arXiv:2403.18673) — rather than attempting an original derivation.

**Two mutually-reinforcing findings close both of `P145`'s open threads:**
- **If `A_μ` is a gauge field** (matching `P143`'s own "conserved
  current" baseline): Horndeski's 1976 theorem uniquely fixes the
  gauge-invariant, ghost-free non-minimal vector-curvature coupling as a
  term built entirely from `F_μν`, never bare `A_μ` — `R_μνA^μA^ν` is
  simply **not gauge-invariant**, hence not an admissible operator at all,
  independent of any sign/magnitude question.
- **If `A_μ` is Proca-type instead**: Generalized Proca theory
  (Heisenberg 2014) shows `R_μνA^μA^ν` and `(∇_μA^μ)²` are **not
  independent operators** — tied by the Ricci identity with a fixed
  relative coefficient — and ghost-freedom needs a special, non-generic
  tuning, not automatic for a free `λ`. Even correctly tuned, Hell
  (2024/2025) shows a further strong-coupling pathology persists unless a
  disformal compensator is added.

**Verdict: `NO-HEALTHY-MINIMAL-VECTOR-ESCAPE`** — read narrowly: neither
reading of what `A_μ` is gives a *minimal* healthy non-minimal operator,
matching the user's own explicit "минимальный" framing. **One genuinely
new, still-open candidate surfaced**: Horndeski's own gauge-invariant term
(`F_μκF^νκR^μ_ν`-type) was never checked by `P145` (which tested the
wrong, non-gauge-invariant operator) — a real `P147` candidate if the
gauge-field reading is the right one to pursue further.

Skeptic review dispatched (Source-Trace verification: are the 3 citations
real, accurately quoted, and does the disjunctive argument actually cover
the space) — result pending.

**Correction (same day, skeptic review of P146): verdict-language narrowed
+ marker fixed.** The skeptic dispatch itself lacked WebSearch/WebFetch
that turn (disclosed honestly, not faked) — it assessed plausibility from
training-data familiarity rather than true independent fetch. Within that
limit it still caught two real issues: (1) the Horndeski exact-formula
marker was `[VERIFIED-QUOTE]` when it was actually obtained via WebSearch
synthesis, not a page I personally read — downgraded to
`[VERIFIED-SYNTHESIS]`, matching the honesty standard already used for the
Generalized Proca claim; the *logical* argument (gauge non-invariance of
`R_μνA^μA^ν`) doesn't depend on the exact formula and is now hand-verified
in the file itself. (2) The headline verdict `NO-HEALTHY-MINIMAL-VECTOR-
ESCAPE` oversold what §6.2 already admitted — Horndeski's own F-based term
was never checked. Renamed to `NO-HEALTHY-MINIMAL-ESCAPE-AMONG-P145'S-
CANDIDATES`, with the P147 exclusion now stated in the verdict line itself,
not buried. Separately, re-fetched Claim C (Hell 2024/2025) a second,
independent time — confirmed real (author, journal ref match). Added an
explicit non-abelian out-of-scope note per the skeptic's own flagged gap.
