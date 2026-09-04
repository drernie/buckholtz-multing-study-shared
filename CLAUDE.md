# buckholtz-idm-multing-mvp

## PROJECT
- **Type:** research (not production, not MVP-app) — resolves the SessionStart
  dispatcher's recurring `AMBIGUOUS` classification.
- **Stack:** Python 3.11+ (dev on 3.13), sympy/scipy/numpy, pytest, ruff.
- **Goal:** epistemic audit / reconstruction of Dr. Thomas J. Buckholtz's
  IDM/MULTING cosmological framework — falsifiable claims, honest negative
  results, no overclaiming. NOT a validation or refutation of MULTING itself.
- **Tests:** `pytest tests/ -q` (901 passing) · `ruff check .` (clean) ·
  `mypy src` (0 errors, verified 2026-09-05).

## CANONICAL CONTEXT — read in this order at session start
0. **`CURRENT_EVIDENCE_STATE.md`** (added 2026-09-03) — 2-page canonical
   snapshot: reproduced / refuted-or-weakened / what changed after v82 /
   4 open bottlenecks / one next differentiating test / what cannot be
   claimed publicly. The fast-orientation entry point; read this first,
   then go deeper via the items below as needed.
1. `.claude/memory/activeContext.md` — live, updated per commit. Source of
   truth for "what are we doing right now."
2. `docs/145_research_audit_and_harvest_report_20260817.md` — comprehensive
   meta-audit, updated through Part 8 (2026-08-26). Source of truth for
   "what has this project established, and how well."
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
4. `PROJECT_STATUS.md` — **superseded snapshot** (v0.3, 2026-06-01). Kept for
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
- Eq.32's (4/3) coefficient mechanism-hunt — exhausted across 5 independent
  niches (`null_results/20260817-nr019-...md` + `docs/145` §24 of the v6
  report). The 0.0135% numerical match itself is `[VERIFIED]` and unaffected;
  only the *mechanism search* is exhausted.

## STANDING CONSTRAINTS
- **TJB correspondence: active as of 2026-08-30**, superseding the
  2026-08-14 "no correspondence" note (that note is historical — the user
  sent a full progress-report email 2026-08-27, TJB replied 2026-08-29
  proposing a video call, and the user explicitly requested a drafted
  reply 2026-08-30). Still draft only on an explicit, current request —
  never send unilaterally, and still follow the standing tone/content
  rules (formal address, no evaluative-authority words, share results
  rather than auditing, minimize questions — see global memory
  `feedback_tjb_*` entries and `lessons_learned.md`'s 2026-08-29 entry).
- `NO_AUTHOR_ERROR`: every finding is about this project's own
  reconstruction, never a claim about Dr. Buckholtz's own unpublished theory.

## NEVER
- Reconstruct F→H_MULT(z) by fitting against Table A1 (`NO_BRIDGE_FITTING`).
- Treat a `docs/145`/`docs/147` "unchanged" carry-forward number as freshly
  re-verified — it is explicitly not.
