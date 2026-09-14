# START HERE — what to read, and what not to trust

**Added 2026-09-14. Navigation only.** This file introduces no claim, number,
derivation, or status change. It exists because the repository root holds 13
Markdown files with no way to tell, at a glance, which describe the project's
current state and which are dated snapshots kept for history. Every factual
statement below is a pointer to a file that already says it.

**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR

---

## The three-line answer

1. **Program phase: `WAITING + CONSOLIDATION`, not active discovery** (set
   2026-09-13). No new computation without a specific reopen trigger firing on
   a specific claim.
2. **Where the current state lives:**
   [`PROGRAM_CLOSEOUT_LEDGER.md`](PROGRAM_CLOSEOUT_LEDGER.md) (the 1–2 page
   index) and [`CURRENT_EVIDENCE_STATE.md`](CURRENT_EVIDENCE_STATE.md) (the
   evidence behind it). Both are frozen 2026-09-13 baselines.
3. **Nothing else in the root is current.** Nine of the 13 root files are
   dated snapshots. Two of them still read as live to-do lists and are the
   easiest things in this repository to misread — see `progress.md` and
   `DISCOVERY_GATE.md` in the map below.

---

## Document map — repository root

**Tier vocabulary applies to documents, not to claims.** It is deliberately
disjoint from the claim-status vocabulary
(`SOLVED`/`CLOSED-BOUNDED`/`DISSOLVED`/`EXHAUSTED`/`STOPPED`/`NON-IDENTIFIED`)
that [`PROGRAM_CLOSEOUT_LEDGER.md`](PROGRAM_CLOSEOUT_LEDGER.md) defines in its
own header and marks as not interchangeable. A `LIVE` document can contain a
`STOPPED` claim; a `HISTORICAL` document does not thereby contain refuted
physics. The two axes are independent.

- **`LIVE`** — reflects the state of the project as of its own last update.
- **`FROZEN`** — deliberately fixed at a date; being un-updated is the point,
  not decay.
- **`PROCESS`** — standing rules and workflow notes; slow-moving by design,
  not a status report.
- **`HISTORICAL`** — a dated snapshot, superseded on at least one specific
  point. Kept unrewritten per the project's no-silent-correction convention.

### `LIVE`

| File | Role | Last substantive update |
|---|---|---|
| [`PROGRAM_CLOSEOUT_LEDGER.md`](PROGRAM_CLOSEOUT_LEDGER.md) | **Fastest orientation.** 13 major claims, each with evidence IDs, status, strongest support, strongest counterevidence, and its own explicit reopen condition. Also carries the `WAITING + CONSOLIDATION` governance protocol, the `DO NOT RETRY WITHOUT NEW INPUT` list, and the external-reply trigger table. | 2026-09-13 |
| [`CURRENT_EVIDENCE_STATE.md`](CURRENT_EVIDENCE_STATE.md) | **Canonical detail.** What is reproduced, what is refuted or weakened, the open bottlenecks, and an explicit list of what cannot be claimed publicly. The Ledger is an index into this file. | 2026-09-13 |
| [`README.md`](README.md) | Project framing, source preprint, disclaimers, install and test instructions, epistemic label taxonomy. Its dated quality-snapshot line is explicitly superseded as an entry point by `CURRENT_EVIDENCE_STATE.md`. | 2026-09-13 |
| [`CLAUDE.md`](CLAUDE.md) | Agent/contributor operating instructions: canonical reading order, the v6-vs-v82 source-version rule, closed workstreams, standing constraints, and the process rules added after the 2026-09-07 retractions. Read this before contributing anything. | 2026-09-13 |

**On the two reading orders.** `CLAUDE.md` puts `CURRENT_EVIDENCE_STATE.md`
first and the Ledger second; `README.md` puts the Ledger first. This is not a
contradiction and neither is wrong — they address different readers. An agent
or contributor about to *do work* must read the full evidence file first, per
`CLAUDE.md`'s `NEXT-STEP GATE` (process rule 5), which exists specifically
because a stale document once outranked a fresher canonical state three times
in one conversation. A human reviewer *orienting* wants the 1–2 page index
first. Pick by which of those you are.

### `FROZEN`

| File | Role | Frozen at |
|---|---|---|
| [`PREREGISTRATION_v82_prospective_tests.md`](PREREGISTRATION_v82_prospective_tests.md) | Three prospective tests with PASS/FAIL thresholds, committed before the relevant measurements exist. Its own header states plainly that these are *not* retroactive predictions about the 33-point fit, and grades two of the three as *weak* in discriminating power. Do not update; a change to the frozen parameters voids it and requires a new pre-registration. | 2026-09-07 |

### `PROCESS`

| File | Role | Last update |
|---|---|---|
| [`decisions.md`](decisions.md) | Standing project-specific decisions (framing labels, `NO_EMAIL_WITHOUT_APPROVAL`, H1-program methodology choices). Binding unless explicitly revisited. Not a status report, so its date is not staleness. | 2026-07-22 |
| [`lessons_learned.md`](lessons_learned.md) | Workflow and tooling lessons only. Its own scope note is load-bearing: falsified *scientific* claims belong in `null_results/` with the full template, never here. | 2026-08-30 |

### `HISTORICAL` — superseded, kept for history

| File | Snapshot of | Superseded on | Read instead |
|---|---|---|---|
| [`PROJECT_STATUS.md`](PROJECT_STATUS.md) | v0.3.0 MVP, 2026-06-01 | Already banner-flagged in-file since 2026-08-26. Its test counts and its "beta definitions unclear" primary blocker are stale. | `CURRENT_EVIDENCE_STATE.md` |
| [`progress.md`](progress.md) | Phase tracker, last synced 2026-07-18 | **Reads as a live to-do list and is not one.** Its Phase 3 records TNG API access as pending and the WHIM correlation as unstartable; TNG-300 access was granted 2026-09-09 and the `E_WHIM` half was executed at real `N=71`. Its Phase 5 correspondence state also predates two further outgoing letters. | `PROGRAM_CLOSEOUT_LEDGER.md` rows 11–12, `CURRENT_EVIDENCE_STATE.md` §7.3 |
| [`DISCOVERY_GATE.md`](DISCOVERY_GATE.md) | Eq.32 gate, 2026-06-27 | **Two independent supersessions.** (a) Its headline figure, `0.17σ (0.0135%)`, is the PDG-2022 value that `code/eq32_verify.py` stopped using on 2026-07-11; the current figure is `0.0608%`, `1.00σ`, PDG 2024. (b) Its unchecked boxes — deriving `4/3` from `F₄/J₃(O)`, and the `α_G` mechanism — read as open work, but that mechanism hunt is `EXHAUSTED` (5 external niches + 3 internal attempts) and sits inside `CLAUDE.md`'s explicit exclusion zone. Do not pick these up as a task list. | `PROGRAM_CLOSEOUT_LEDGER.md` row 7 |
| [`CODE_AUDIT_HARDENING.md`](CODE_AUDIT_HARDENING.md) | First `sci-code-audit` pass, 2026-09-06 | Not a status report and self-scoped as a first pass over load-bearing paths only, not all 39 `src/` files. Its own two queued follow-ups remain open. No finding here changed a numeric result. | — (accurate as a dated audit record) |
| [`APPENDIX_A1_EXTRACTION_SUMMARY.md`](APPENDIX_A1_EXTRACTION_SUMMARY.md) | Appendix A1 forensic extraction, 2026-05-29 | Its central finding (the `H_MULT(z)` formula is absent from the source, so the bridge is under-specified) still stands and is load-bearing. Its surrounding version and test counts are v0.2-era. Note it reads v6; everything after 2026-08 reads v82. | `docs/WHAT_THIS_REPRODUCES.md`, `CLAUDE.md` source-version rule |
| [`CHANGELOG.md`](CHANGELOG.md) | Releases through `0.4.0`, 2026-06-06 | Version-tagged releases stopped; the project moved to a dated per-experiment trail. Roughly three months of work postdates the last entry and is recorded in `experiments/`, `null_results/`, and `docs/` instead. | `git log`, `CURRENT_EVIDENCE_STATE.md` |

---

## Reading paths

**Reviewing this as a physicist, ~15 minutes.** The full version of this path,
with its framing note on the repository's own blunt internal vocabulary, is in
[`README.md`](README.md#start-here-if-you-are-reviewing-this-as-a-physicist).
In short: [`PROGRAM_CLOSEOUT_LEDGER.md`](PROGRAM_CLOSEOUT_LEDGER.md) →
[`CURRENT_EVIDENCE_STATE.md`](CURRENT_EVIDENCE_STATE.md) →
[`docs/151_status_separation_rule.md`](docs/151_status_separation_rule.md) (the
rule every verdict obeys: empirical, ontological, and causal status are three
separate fields) → [`null_results/INDEX.md`](null_results/INDEX.md) (21
registered dead ends — the register exists so a killed direction cannot
quietly return).

**Checking one specific claim.** Find it in
[`PROGRAM_CLOSEOUT_LEDGER.md`](PROGRAM_CLOSEOUT_LEDGER.md), follow its evidence
IDs into `experiments/<id>/`, and read the `CLAIM_*` file before the
`FINDING_*` file — the claim was pre-registered, the finding came after.

**Is there a falsifiable prediction?**
[`PREREGISTRATION_v82_prospective_tests.md`](PREREGISTRATION_v82_prospective_tests.md).

**About to contribute or run something.** [`CLAUDE.md`](CLAUDE.md) in full,
then `CURRENT_EVIDENCE_STATE.md` in full before proposing any next step. The
`DO NOT RETRY WITHOUT NEW INPUT` list in the Ledger's governance section names
five directions that are default-forbidden, and "we could still compute
something" is explicitly not a reopen condition.

## Subdirectory indexes

| Index | Covers | Note |
|---|---|---|
| [`docs/INDEX.md`](docs/INDEX.md) | numbered `docs/` | Its header reads `Total documents: 96` and describes coverage through `docs/157`. Checked 2026-09-14: 142 `.md` files are present and `docs/161`–`162` are not indexed. A resync was already queued as out-of-scope in `CODE_AUDIT_HARDENING.md` layer 9. |
| [`null_results/INDEX.md`](null_results/INDEX.md) | 21 falsified directions | Each entry carries a Kill Analysis and a Relaxation Map. |
| [`pearl_registry/INDEX.md`](pearl_registry/INDEX.md) | side-findings, each with a `next_check` anchor | Its own header documents a known column-schema divergence from the global protocol. |
| [`parked/INDEX.md`](parked/INDEX.md) | archived-but-not-refuted threads | `H1b` lives here. |

There is no `experiments/INDEX.md`; enter `experiments/` through the Ledger's
evidence IDs instead.

---

## One caveat about this repository specifically

This is the **derived reviewer copy**, regenerated from a private source
repository by `scripts/refresh_shared_repo.sh` — which strips private
correspondence from every commit and force-pushes a rewritten history. Edits
made directly here do not survive the next regeneration. Anything worth
keeping has to be applied in the source repository. See the two-repository
table in [`CLAUDE.md`](CLAUDE.md).

Two consequences for a reader of *this* copy:

- **`.claude/memory/activeContext.md` does not exist here.** `CLAUDE.md`
  (item 1), `CURRENT_EVIDENCE_STATE.md`, and `progress.md` all name it as the
  live per-commit source of truth for "what are we doing right now." It is
  stripped from every commit of this copy by design. Those references resolve
  only in the private source repo; treat them as pointing at something you
  cannot read rather than something missing.
- **`data/source_material/` is git-ignored**, so the preprints and the
  author's supplemental code are not here either. They are on
  [Zenodo](https://zenodo.org/records/22004287) and
  [preprints.org](https://doi.org/10.20944/preprints202608.0943.v1), and must
  be fetched to re-run everything. This is also why one test file does not
  collect from a clean clone — see `README.md`'s status line.
