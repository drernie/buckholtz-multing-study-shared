# buckholtz-idm-multing-mvp

## PROJECT
- **Type:** research (not production, not MVP-app) — resolves the SessionStart
  dispatcher's recurring `AMBIGUOUS` classification.
- **Stack:** Python 3.11+ (dev on 3.13), sympy/scipy/numpy, pytest, ruff.
- **Goal:** epistemic audit / reconstruction of Dr. Thomas J. Buckholtz's
  IDM/MULTING cosmological framework — falsifiable claims, honest negative
  results, no overclaiming. NOT a validation or refutation of MULTING itself.
- **Tests:** `pytest tests/ -q` (979 passing, 2026-09-06) · `ruff check .`
  (clean) · `mypy src` (0 errors, blocking in CI, verified 2026-09-05).

## CANONICAL CONTEXT — read in this order at session start
0. **`CURRENT_EVIDENCE_STATE.md`** (added 2026-09-03) — 2-page canonical
   snapshot: reproduced / refuted-or-weakened / what changed after v82 /
   4 open bottlenecks / one next differentiating test / what cannot be
   claimed publicly. The fast-orientation entry point; read this first,
   then go deeper via the items below as needed.
0a. **`PROGRAM_CLOSEOUT_LEDGER.md`** (added 2026-09-13, frozen baseline
    of the same date) — a 1-2-page claim-by-claim index (claim / evidence
    IDs / status / support / counterevidence / reopen-if), built ONLY
    from `CURRENT_EVIDENCE_STATE.md`. Marks the end of this project's
    discovery campaign and the start of consolidation → publication →
    external challenge — **no new computation** without a specific
    reopen condition firing on a specific row. Precise status vocabulary
    (`SOLVED`/`DISSOLVED`/`EXHAUSTED`/`STOPPED`/`CLOSED-BOUNDED`/
    `NON-IDENTIFIED`) is not interchangeable — read the Ledger's own
    header before using any of these words elsewhere.
1. `.claude/memory/activeContext.md` — live, updated per commit. Source of
   truth for "what are we doing right now."
2. `docs/145_research_audit_and_harvest_report_20260817.md` — comprehensive
   meta-audit, updated through Part 9 (2026-09-09, a portable meta-pattern:
   "real work disconnected from its own index," found 5× in 2 days —
   see Part 9 itself for the worked cases; Parts 1-8 unchanged). Source of
   truth for "what has this project established, and how well."
3. `docs/147_campaign_stop_rule.md` — the 4 named bottlenecks
   (F→H_MULT(z) / Unique completion / Absolute scale / IC-sensitivity), their
   current status, and the explicit reopen conditions for each. **[2026-09-01]
   Bottleneck 1's gate decision is now made — see `docs/153`.** The original
   2026-08-23 framing ("no published bridge exists") is `OLD-FORMULATION-
   SUPERSEDED` (v82 published one — `docs/149`) — this tag kills exactly
   that one claim, it is NOT "F→H(z) is solved" or "the bridge is correct."
   It is RESTATED, not simply reopened: the new, precisely-scoped, still-
   OPEN question is whether this project's own S-S closure result
   (isotropic-average, r→∞) is compatible with v82's
   own finite-r, single-pair bridge construction — GO-eligible per `docs/147`'s
   own criterion 2, but not authorized to run without a separate explicit
   go-ahead. `docs/147`'s own bottleneck-1 entry is annotated with a pointer,
   not rewritten.
4. `docs/archive/PROJECT_STATUS.md` — **superseded snapshot** (v0.3, 2026-06-01).
   [Moved out of the repository root 2026-09-14 along with five other dated
   snapshots; see `docs/archive/README.md`. The root now holds live documents
   only, and the standing process files are at `docs/meta/decisions.md` and
   `docs/meta/lessons_learned.md`.] Kept for
   history, banner-flagged, not the current state. Do not treat its numbers
   (858 tests, "beta unclear" blocker) as live.

## SOURCE PREPRINT VERSION — v6 for everything already built, v82 going forward
This project's entire F_oP/dipole/quadrupole/S–S-background reconstruction
(`docs/124`-`127`, `two_charge_completion.py`, `two_field_action_closure.py`,
`P1`-`P155`) is built on **v6** (`data/source_material/buckholtz_
preprints202511.0598.v6.pdf`). TJB's own current work is a **different,
substantially expanded document**, `data/source_material/buckholtz_
202608.0943v1.v82.pdf` ("Multi-Tier Newtonian Gravity...," Zenodo 22004287)
— see `docs/149_v82_preprint_study.md` for the full structural comparison
and `data/source_material/README.md` for the version-provenance note. **Cite
v6 for anything already established; cite v82 for anything new going
forward; never conflate the two without checking.**

## METHODOLOGY
This project runs the full FL/EstimandOps stack from `~/.claude/rules/`
(`falsification-ladder.md`, `estimand-ops.md`, `artifact-provenance-gates.md`,
`audit-verification-gate.md`). Every experiment lives under
`experiments/<id>/`, gets a positive control before its claim is trusted, and
resolves to `null_results/` (REJECT), `parked/` (ARCHIVE), or stays active.
`pearl_registry/INDEX.md` tracks side-findings with a `next_check` anchor.

**Hard rule inherited from the global stack:** a fit is never its own
validation target (Gate 2). Table A1 in the TJB preprint is confirmed
**AI-output**, not a MULTING calculation (`docs/145` Part 8 / Secция 8 of the
v6 report) — never reconstruct the bridge by fitting against it.

**`docs/151_status_separation_rule.md`** — every claim's verdict
separates Empirical/Model status from Ontological-interpretation status
from Causal-claim status, three fields, never collapsed into one. A
good `H(z)` fit (empirical) is not thereby a confirmed mechanism
(ontological) or a confirmed bottom-up causal story (causal) —
parameter-identifiable ≠ causally identifiable.

## CLOSED WORKSTREAMS — do not reopen without the stated condition
- `[WS: round-2-strategic-arbiter]` — CLOSED 2026-08-24 (`docs/145` Part 6).
- `BOTTLENECK-4-NATURAL-CLOSURE` (IC-sensitivity) — CLOSED 2026-08-26
  (`docs/145` Part 8, `docs/147` point 4). 5 mechanism candidates excluded.
  Physical question remains **genuinely open** — only the search campaign on
  this information set is exhausted. Reopen only with: a genuinely new
  mechanism class (not equivalent to pole/early-transient/horizon-crossing/
  gauge/mode-projection), a new verified external fact, or explicit user
  override.
- Eq.32's (4/3) coefficient mechanism-hunt — exhausted across two
  complementary searches, correctly cited: **internal** group-theoretic
  attempts (`null_results/20260817-nr019-...md`, 3 attempts: S³, F₄/G₂/J₃(𝕆),
  SM-gauge-dim) and **external** literature niches
  (`null_results/20260908-nr024-...md`, 5 niches: SU(3)-flavour,
  geometric-Koide, Dirac-LNH, classical-EM 4/3-problem, strong-gravity/
  electron-mass). **Correction, 2026-09-08:** this line previously cited only
  `NR-019` for the 5-niche claim — `NR-019` does not cover it; `NR-024` was
  written specifically to close that citation gap (found by a
  `/boyko-bridge-ladder` verification pass). 3 of `NR-024`'s 5 niche-verdicts
  are `[MEMORY]`-tier (reconstructed from cross-session notes, not
  re-derived this session) — see that file for exact confidence per niche.
  The 0.0135% numerical match itself is `[VERIFIED]` and unaffected by any
  of this; only the *mechanism search* is exhausted.

## TWO REPOSITORIES — this one is the only one you ever edit (added 2026-09-11)

| | this repo | the reviewer copy |
|---|---|---|
| remote | `sergeeey/buckholtz-idm-multing-study` | `sergeeey/buckholtz-multing-study-shared` |
| path | `buckholtz-idm-multing-mvp/` | `../buckholtz-multing-shared/` |
| role | **source of truth.** All work happens here. History contains private correspondence; never share it. | **purely derived.** Private letters and `.claude/` stripped from every commit. Given to one external reviewer. |

**Hard rule:** never edit the copy by hand — regenerate it with
`bash scripts/refresh_shared_repo.sh` (add `--push` when satisfied). If you
catch yourself editing a file under `buckholtz-multing-shared/`, stop: the
change belongs here, and the copy should be rebuilt from it. The script keeps
exactly two copy-only deltas (the CI badge, which 404s for an outside reader,
and the clone directory name) and verifies afterwards that nothing private
survived.

`correspondence/` is git-ignored here as of 2026-09-11: the letters stay on
disk and in the Obsidian vault archive, but never re-enter git.

## STANDING CONSTRAINTS
- **TJB correspondence: `WAITING_ON_EXTERNAL` as of 2026-09-13** — the
  ball is on his/Ernest's side (last outgoing: repo-share letter,
  2026-09-11 08:14, no reply since). **Do not initiate a new letter just
  because research time freed up** — this is an external dependency, not
  an active task. Return to it only if: (a) he replies, (b) a new result
  materially changes the actual question posed to him, or (c) an
  explicitly pre-set follow-up interval elapses (none currently set).
  When correspondence does resume: still draft only on an explicit,
  current request — never send unilaterally, and still follow the
  standing tone/content rules (formal address, no evaluative-authority
  words, share results rather than auditing, minimize questions — see
  global memory `feedback_tjb_*` entries and `docs/meta/lessons_learned.md`'s
  2026-08-29 entry).
- `NO_AUTHOR_ERROR`: every finding is about this project's own
  reconstruction, never a claim about Dr. Buckholtz's own unpublished theory.

## PROCESS RULES — added 2026-09-07 after 4 same-day retractions (P215/P216/P217, and P214 earlier)
All four shared one root cause: a one-sided search reported as a two-sided
comparison, plus reading the applied sections of a source before its
self-limiting ones. See `experiments/20260803-bridge/
FINDING_P215_P216_P217_RETRACTION_after_step8a.md` §4 for the full account.

1. **Step -3 pre-work check is MANDATORY on this project's OWN directories**,
   not just external literature. Before writing a new `FINDING_P<n>` under
   `experiments/20260803-bridge/`, `grep` that same folder for the topic
   first — `FINDING_P7` already held the answer to `P215`'s question and was
   never checked (`ls experiments/20260803-bridge/FINDING_P*` +
   `grep -l <topic>` first, always).
2. **Grep the CLEAN extraction, not the glued one.** `data/source_material/
   buckholtz_preprints202511.0598.v6_pymupdf-clean.md` is the preferred
   search target (its own header line 10 says so) — the older `.md` glues
   words together and produces false negatives (`grep -c -i node` on it
   returned 2, both from "neutrinodensities"; zero on the clean file too,
   but for the right reason).
3. **Read a source's self-limiting sections BEFORE its applied ones**, when
   both exist. v82 has one titled "Circumstances where this framework
   should not be expected to be accurate" (§IV.H) and a fitting-protocol
   retrospective (§IV.S, ~line 1716) — both contained the sentence that
   falsified a same-day finding, and both were read last, not first.
4. **A comparative claim about two documents requires a search run on
   BOTH**, not one document swept and the other assumed silent. `P217`
   swept `β` in v82 only and stated a conclusion about the v6↔v82
   relationship; the same sweep on v6 dissolved it in a minute.
5. **NEXT-STEP GATE — added 2026-09-13, after a same-conversation class
   of error (P223, `P191`, bottleneck 2 — three instances of ONE
   defect: a stale document/label/memory outranking a fresher canonical
   state).** Before recommending, or starting, any new research work —
   read `CURRENT_EVIDENCE_STATE.md` in full FIRST, not `docs/147`, not
   session memory, not a partial grep. Check explicitly: is this task
   already done? Was it stopped by an explicit prior decision (e.g. an
   arbiter/skeptic recommendation that was taken)? Has its upstream
   status changed since the file you're about to cite was last updated?
   Required order: **CURRENT STATE → OPEN DEPENDENCIES → EVI → NEXT
   ACTION** — never "old roadmap → memory → recommendation." Concrete
   incident: recommended running `P191`'s Fisher-forecast (done
   2026-09-05, `P192`-`P194` too) and attacking bottleneck 2 directly
   ("never attacked" — false, `/hypothesis-arbiter` already returned a
   stop recommendation, taken, 2026-09-07) — both wrong because
   `docs/147` was read without cross-checking the more current
   `CURRENT_EVIDENCE_STATE.md`. Full account: `CURRENT_EVIDENCE_STATE.md`
   header note (2026-09-13) and `docs/147`'s own bottleneck-1/2
   annotations from the same date.

## NEVER
- Reconstruct F→H_MULT(z) by fitting against Table A1 (`NO_BRIDGE_FITTING`).
- Treat a `docs/145`/`docs/147` "unchanged" carry-forward number as freshly
  re-verified — it is explicitly not.
