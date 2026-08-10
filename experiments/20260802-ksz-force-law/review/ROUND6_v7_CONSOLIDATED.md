# Round 6 — static review of DRAFT_SPEC_v7

**Date:** 2026-08-10
**Reader:** one reader, this session. A second, independent reader is still required
before `DUAL_READER_REVIEW` is satisfied.
**Applied gate:** the v7 freeze gate. A finding blocks if and only if two
implementations, both compatible with the four normative files, could differ in
the simulated data, a kernel, the likelihood, a terminal state, or a reported
output. `Reading A` / `Reading B` / `Affected output` supplied for each. A
reading contradicted by a normative file is not blocking and is recorded as
resolved.

**Machine gates run first, both clean:**

| gate | result |
|---|---|
| `spec_lint.py DRAFT_SPEC_v7.md` | 0 findings (11 prose checks) |
| `spec_gate.py` | 10 / 10 PASS, 0 problems; 32766 acceptance vectors enumerated, two interpreters agree on every one; four normative hashes recorded |

**Verdict: 1 blocking finding. v7 does not freeze.**

---

## BLOCKING — R6-01: `clip` has no declared semantics

**Where.** `reference_config.yaml → grids.refined.clip: [0.05, 60.0]`, applied to
the refined grid that `state_machine.yaml → actions.refine_last_fall` defines as

```
mu = 0.05*ii   for every integer ii with   0.1*jlast - 2 <= 0.05*ii <= 0.1*jlast + 2
```

**Reading A — restrict.** The grid is the windowed set intersected with
`[0.05, 60.0]`; nodes outside the interval are dropped. A window reaching below
`0.05` yields a grid whose smallest node is `0.05`, present once.

**Reading B — clamp.** Each node outside the interval is replaced by the nearer
endpoint. This is the semantics of the word in `numpy.clip`, and `numpy` is the
library idiom used throughout the file. A window reaching below `0.05` yields a
grid in which `0.05` appears once for every out-of-range `ii`.

**Both readings are compatible with the normative files.** Neither `clip` nor an
equivalent operator is named in `libraries:`, although §0 states that
`reference_config.yaml` governs "every constant, every library call and its
options", and the same file does spell out clamping where it means it —
`inputs.gcurve.outside_range: "clamp to the end values; numpy.interp default"`.
The contrast between a named clamp there and a bare `clip` here is what leaves
the reading open.

**Affected output — item 9, `edge_count`.**
`output_schema.json → n:9 → edge_count`, shape `[2, 11, 4, 2]`, axes
`[model, rlo, stage, boundary]`, dtype `int64`. Per IDX-01 every fit increments
the bucket of its own stage. Under Reading B a window that overruns the left
bound contributes one boundary increment per clamped node; under Reading A it
contributes at most one. The two implementations report **different integers in
a declared output array**.

**Reachability — not an edge case.** The left bound is overrun whenever
`0.1*jlast - 2 < 0.05`, i.e. `jlast <= 20`, i.e. whenever the coarse crossing
sits below `mu = 2.0` Mpc. Since the product is an upper limit on `ℓ_d`, a limit
below 2 Mpc is a plausible and arguably expected outcome; `jlast = 1` already
triggers it. The right bound is overrun for `jlast >= 581`.

**Not covered by a witness.** `test_vectors.json` contains no occurrence of
`clip` and one of `jlast`; no registered vector exercises a window that overruns
either bound.

**Minimal resolution — no v8 required.** One registered ledger entry, one line in
`reference_config.yaml`, one witness:

```yaml
grids:
  refined:
    clip: [0.05, 60.0]
    clip_semantics: restrict      # or: clamp
```

plus a test vector with `jlast <= 20` pinning the resulting `edge_count`. If
`restrict` is chosen the line is a clarification; if `clamp` is chosen it should
name the call, as every other operator in `libraries:` does.

---

## RESOLVED — not blocking

**R6-02 — order of the nine controls.** §12 and the appendix ask in what order
the controls run; no normative file states one. Not blocking: `output_schema.json
→ n:8` declares `measured` and `verdict` as shape-`[9]` arrays indexed by control
number, not by execution order, with the per-control value counts fixed
(control 1 → 3, control 5 → 2, control 6 → 4, the rest → 1); and
`state_machine.yaml → control_completion` requires all nine to complete before
any terminal verb is honoured, so no verb can truncate the set in an
order-dependent way. Execution order is unobservable in every declared output.

**R6-03 — `muzero` undefined in the prose.** Appears in `S1.reports`
(`state_machine.yaml`) without a definition in `DRAFT_SPEC_v7.md`. Not blocking:
it is a declared column of item 1 in `output_schema.json`, so it is registered,
which is also why `spec_lint.py`'s "identifiers not in registry" check is clean.

---

## Points examined and found tight

Recorded so a second reader need not re-derive them.

- **Totality of the endpoint classification.** S1–S4 partition every acceptance
  vector given `acc(0) = true`; `spec_gate.py` check 9 confirms two independent
  interpreters agree across 32766 vectors, and `state_machine.yaml` states the
  8190-vector proof for lengths 2..13. The `zero_node` block resolves the v6
  contradiction ("left end accepted by construction" vs "mu = 0 is never an
  endpoint") by evaluation rather than assertion, which is what makes
  `NO_FALLING_TRANSITION` unreachable rather than merely unlikely.
- **Bisection termination.** `[0, 0.1]` with `stop_when` bracket width `< 1e-3`
  needs 7 halvings against `max_iterations: 20`; the two cannot conflict, and
  `L95_rule` is defined under either exit.
- **Tie resolution.** One rule (`argmax_left`), scoped to "every other argmax or
  argmin anywhere", with the total-tie case reachable and witnessed (TV02).
- **RNG stream.** `consumption: "normals first, always; integers only for branch 2,
  after the normals"` fixes the order; `keyMu = round(mu/0.05)` makes duplicate
  grid nodes seed-identical, so R6-01 cannot desynchronise the stream — it
  affects counters only.
- **Empty sets.** `empty_set_contract` covers both collections in all three
  cardinalities; no silent `max`/`min` over an empty collection remains.

---

## Recommended next transition

```
DRAFT_v7 → LOCAL_STATIC_LINT ✅ → SPEC_GATE ✅ → DUAL_READER_REVIEW ⟵ here
```

1. Register R6-01 in `ambiguity_ledger_v7.md`, add `clip_semantics` to
   `reference_config.yaml`, add the witness to `test_vectors.json`, re-run both
   gates (hashes in `spec_gate.py` check 10 will change by design).
2. Obtain the **second** independent reader. This review is one of two; the
   transition is not satisfied by a single reader, and this reader has now seen
   the spec and cannot serve as the second.
3. On zero further blocking findings: `COMPUTATIONALLY_FROZEN_v7 → BLIND_C`.

Per the standing stop rule, R6-01 changes a numeric output and therefore blocks
the freeze, but it is a one-line normative clarification and does **not** justify
a v8.

---

## Scope

This review reads the specification and its four normative files. It runs no
part of the procedure, touches no data, and makes no statement about `ℓ_d`,
about MULTING, or about any preprint figure. Labels unchanged:
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive.
