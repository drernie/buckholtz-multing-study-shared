# buckholtz-idm-multing-mvp

## PROJECT
- **Type:** research (not production, not MVP-app) — resolves the SessionStart
  dispatcher's recurring `AMBIGUOUS` classification.
- **Stack:** Python 3.11+ (dev on 3.13), sympy/scipy/numpy, pytest, ruff.
- **Goal:** epistemic audit / reconstruction of Dr. Thomas J. Buckholtz's
  IDM/MULTING cosmological framework — falsifiable claims, honest negative
  results, no overclaiming. NOT a validation or refutation of MULTING itself.
- **Tests:** `pytest tests/ -q` (881 passing) · `ruff check .` (clean).

## CANONICAL CONTEXT — read in this order at session start
1. `.claude/memory/activeContext.md` — live, updated per commit. Source of
   truth for "what are we doing right now."
2. `docs/145_research_audit_and_harvest_report_20260817.md` — comprehensive
   meta-audit, updated through Part 8 (2026-08-26). Source of truth for
   "what has this project established, and how well."
3. `docs/147_campaign_stop_rule.md` — the 4 named bottlenecks
   (F→H_MULT(z) / Unique completion / Absolute scale / IC-sensitivity), their
   current status, and the explicit reopen conditions for each.
4. `PROJECT_STATUS.md` — **superseded snapshot** (v0.3, 2026-06-01). Kept for
   history, banner-flagged, not the current state. Do not treat its numbers
   (858 tests, "beta unclear" blocker) as live.

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
- **No TJB correspondence in this phase** (user instruction, 2026-08-14,
  unrevoked as of this file's writing). Do not draft or send anything to
  Dr. Buckholtz without an explicit, current request.
- `NO_AUTHOR_ERROR`: every finding is about this project's own
  reconstruction, never a claim about Dr. Buckholtz's own unpublished theory.

## NEVER
- Reconstruct F→H_MULT(z) by fitting against Table A1 (`NO_BRIDGE_FITTING`).
- Treat a `docs/145`/`docs/147` "unchanged" carry-forward number as freshly
  re-verified — it is explicitly not.
