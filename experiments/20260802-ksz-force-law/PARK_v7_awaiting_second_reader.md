# v7 — parked at DUAL_READER_REVIEW, awaiting a genuinely independent second reader

**Date:** 2026-08-10
**State:** `DRAFT_v7 → LOCAL_STATIC_LINT ✅ → SPEC_GATE ✅ → DUAL_READER_REVIEW (1 of 2) ⟵ here`
**Not reached:** `COMPUTATIONALLY_FROZEN_v7`, `BLIND_C`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## Why parked rather than frozen

Two readings of v7 were performed today and each returned exactly one blocking
finding. Both are now resolved and both gates are green. That is not sufficient
to freeze, for one reason:

**Neither reading is an independent second reader.**

| reading | independence, per this project's own ladder | found |
|---|---|---|
| this session, direct | none — same context that then wrote the resolution | CLIP-01 |
| `skeptic`, isolated context | **Weak–Medium** — same model, no reasoning chain, no session history | LABELS-01 |

The project's Independent Verification Strength Ladder places "same model,
isolated context" at Weak–Medium, below "different model" and well below
"independently-written code". `DUAL_READER_REVIEW` is recorded as **not
satisfied**. Declaring it passed on a Weak–Medium reading, and then running
Blind C on that basis, would put a provenance artifact immediately upstream of
the track's terminal scientific output — the exact failure class this track's
whole gate structure exists to prevent.

What the skeptic run does establish, and it is worth keeping: it read the
post-CLIP-01 state without knowing CLIP-01 had been raised, and independently
recorded that entry as pinned. The fix reads as closed to someone who does not
know it was written.

---

## Round 6 — what was found and closed

### CLIP-01 — `clip` interval given without the operation

`reference_config.yaml → grids.refined.clip: [0.05, 60.0]` admitted two
implementable readings — restrict (drop out-of-range nodes) and clamp
(`numpy.clip` semantics, replace with the boundary). Under clamp one boundary
node appears once per out-of-range `ii`; since IDX-01 had established that every
fit increments `edge_count`, the duplicates become visible in a declared `int64`
array. Reachable whenever `jlast ≤ 20`, i.e. whenever the limit falls below
2 Mpc — the expected regime for an upper limit, not an edge case.

Resolved as **restrict**, in `reference_config.yaml → grids.refined.clip_semantics`,
witnessed by TV21. A grid is a set of distinct evaluation points; duplicates are
seed-identical under `keyMu = round(mu/0.05)` and carry no information, and
inflating a boundary counter with them would defeat its diagnostic purpose.

### LABELS-01 — items 11 and 13 had no set-vs-multiset semantics and no order

`output_schema.json` items 11 `labels_emitted` and 13 `ambiguity_report` were the
only variable-length string arrays and the only multi-row outputs without an
ordering discipline — items 10 and 12 both carry `row_order`. Multiset-chronological
and set-canonical give different lengths and different index-to-label mappings.
Reachable on any run raising a label twice; up to four branches can raise
`STOP_BRANCH`.

Resolved as **set, deduplicated, byte-wise ascending**, witnessed by TV22 as a
metamorphic test: permuting the raise order and repeating a label must leave both
items byte-identical.

The chronological alternative was rejected for a second reason beyond taste.
Making the label array chronological would make the execution order of the nine
controls observable — and that order is pinned nowhere. It was earlier and
correctly dismissed as a non-finding precisely because item 8 is indexed by
control number rather than by execution order. A locally correct fix would have
reopened a finding already closed on the ground of unobservability.

---

## Consequence for the stop rule

The standing rule was: freeze when a round changes no numeric output.

LABELS-01 is a counterexample from inside this track. `[A, B]` and `[B, A]` hold
identical values while binding them to different categories: no number changes,
the meaning does. The rule is therefore strengthened to require, between two
consecutive independent rounds, no change of

1. **numeric** output,
2. **semantic** content, and
3. **classification**.

Equivalently: convergence of a specification is governed not by the number of
review rounds but by the disappearance of new *semantic* degrees of freedom.
Recorded in `pearl_registry/INDEX.md` with a falsifiable prediction, since it is
transferable well beyond this track.

---

## Revival condition

Parked. Resumes when **one** of the following is available:

1. a second reader who has not seen v7 — a different model, or a person; or
2. an independently-written implementation of the normative files, which is a
   strictly stronger check than a reading and would supersede requirement 1.

Until then no freeze, and Blind C is not launched. Both gates and both
resolutions stand and need not be redone; the parked state is a missing reader,
not a missing result.

## Verified state at parking

| | |
|---|---|
| `spec_lint.py` | 0 findings |
| `spec_gate.py` | 10 / 10 PASS, 0 problems |
| ledger entries | 19, every one with a witness |
| test vectors | 22 |
| `state_machine.yaml` | `43326a88f027f8c9` — untouched today |
| `reference_config.yaml` | `026c47d467b62486` — changed by CLIP-01 |
| `output_schema.json` | `350f41b398f59919` — changed by LABELS-01 |
| `test_vectors.json` | `4ac59411c129273e` — changed by TV21, TV22 |

---

## Update, 2026-08-11 — still parked, same revival condition, more fixed

A properly-scoped second reader (this file's own revival condition item 1,
attempted with `Agent(skeptic)`) found and closed 3 more real gaps —
`SDMC-01`, `CTRL7-01`, `NAN-01` — see
`review/SPEC_v7_FAILED_DUAL_READER_REVIEW.md`'s "CURRENT STATUS" section
for the full detail. An EARLIER, wrongly-scoped run of the same tool first
raised ~20 false-positive findings by excluding `DRAFT_SPEC_v6.md` from
its context; that mistake is documented and corrected in the same file.

**This does not change the parked status or its revival condition.** Per
this file's own Independent Verification Strength Ladder above,
`Agent(skeptic)` — however carefully scoped — is same-model, isolated
context: Weak–Medium, the same tier as the original ROUND6 skeptic run,
not "a different model, or a person" (item 1) or "an independently-written
implementation" (item 2). Both are still what `v7` is actually waiting on.

| | |
|---|---|
| `spec_gate.py` | 10 / 10 PASS, 0 problems (re-verified after the fix) |
| `spec_lint.py DRAFT_SPEC_v6.md` | 0 findings |
| ledger entries | 22, every one with a witness |
| test vectors | 25 (`TV23`, `TV24`, `TV25` added) |
| `state_machine.yaml` | `4faba98d5835acad` — changed by `sdmc_contract`, `CTRL7-01` |
| `reference_config.yaml` | `026c47d467b62486` — unchanged today |
| `output_schema.json` | `d4d412ab0e568e93` — changed by `NAN-01` |
| `test_vectors.json` | `10f410df0cf42ef8` — changed by `TV23`, `TV24`, `TV25` |
