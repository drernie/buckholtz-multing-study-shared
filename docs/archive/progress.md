# Progress — Buckholtz IDM/MULTING Audit

> ⚠️ **SUPERSEDED SNAPSHOT (flagged 2026-09-14, navigation pass). This file
> reads as a live to-do list and is not one.** Its unchecked boxes were
> accurate on its own last sync date (2026-07-18) and several have since been
> overtaken by events:
>
> - **Phase 3** records TNG API access as "still pending (18+ days silent)"
>   and the WHIM correlation as unstartable. TNG-300 access was **granted
>   2026-09-09** and H1b's `E_WHIM` half was executed at real `N=71`
>   (`r=-0.429, p<0.001`). H1b is now `PARKED` on a different missing
>   ingredient (`M_HE`), not on TNG access — see
>   `PROGRAM_CLOSEOUT_LEDGER.md` row 12 and `CURRENT_EVIDENCE_STATE.md` §7.3.
> - **Phase 5** predates two further outgoing letters and the current
>   `WAITING_ON_EXTERNAL` state of all three external dependencies.
> - The pointer counts are behind (this file says 14 falsified branches;
>   `null_results/` now holds 21).
>
> Kept unrewritten per the project's no-silent-correction convention. **Do not
> pick any unchecked box below up as a task** without first checking it against
> `CURRENT_EVIDENCE_STATE.md`, per `CLAUDE.md`'s `NEXT-STEP GATE`. Current
> state: [`PROGRAM_CLOSEOUT_LEDGER.md`](../../PROGRAM_CLOSEOUT_LEDGER.md).
>
> *Moved from the repository root to `docs/archive/` on 2026-09-14, when
> the root was reduced to live documents only. Its former path was
> `progress.md`.*

**This is a high-level phase tracker, not the source of truth.** Detailed status lives in:
`null_results/INDEX.md` (14 falsified branches), `pearl_registry/INDEX.md` (44 findings),
`experiments/*/decision.md` (per-experiment verdicts), `.claude/memory/activeContext.md`
(session-by-session narrative). This file exists to answer "what phase are we in" at a
glance — do not duplicate detailed numbers here; update the pointer, not the content.

Last synced: 2026-07-18, commit `61e7b00`. [Stale pointer noted 2026-08-26,
boyko-project-radar — content design is fine (correctly defers to
activeContext.md/pearl_registry/null_results, does not duplicate), only this
sync date is behind. Not rewritten here; update on next real phase change.]

---

## Phase 1 — Static/algebraic claims (Eq.32, 7:9:17) — SURVIVING, mechanism open

- [x] Eq.32 numerical verification against PDG 2024 (0.0135%→0.0608% after a real
  PDG-2022-vs-2024 mislabel was found and fixed, session 19)
- [x] Look-elsewhere scan (83,160 formulas, rank #1)
- [x] External peer-review-style adversarial passes (5+ rounds)
- [x] F4/G2/J3(O) mechanism candidate — tested, FALSIFIED-as-mechanism (same failure
  mode as NR-009), `paper/main.tex` corrected
- [x] 7:9:17 anchor-ambiguity cross-validated against an external review (pearl,
  2026-07-18)
- [ ] Mechanism for either relation — still `[UNKNOWN]`, no surviving candidate

## Phase 2 — H1 cluster-scale confound elimination (H1a–e) — CLOSED, reinterpreted

- [x] H1a raw ICM thermal energy — KILLED (NR-010)
- [x] H1d mass-threshold — KILLED (NR-011)
- [x] H1c morphology/wX — KILLED (NR-012)
- [x] H1e AGN feedback/K0 — KILLED (NR-014)
- [x] T_X shared-variable check (NR-015, 2026-07-18) — pre-registered SURVIVES prediction
  falsified; mechanism unresolved (definitional M_hydro–T_X coupling vs. genuine common
  physical driver, not distinguished by data in hand)
- [ ] Cool-core/non-cool-core stratification (NR-015's own proposed next step, cheap,
  data in hand) — NOT started
- [ ] Quantify Mahdavi et al. 2013's actual HSE-to-T_X leverage (literature-only) — NOT
  started

## Phase 3 — H1b (WHIM/filament), the one TJB-specific test — BLOCKED

- [x] Estimand + pre-registered criteria defined
- [x] TNG API technical bypass search — exhausted, all options (B/C/D) dead
- [x] The Three Hundred data-availability route confirmed via their own MNRAS statement
- [x] Outreach email sent to corresponding author (2026-07-18, user-reported)
- [ ] TNG API access — still pending (18+ days silent)
- [ ] The Three Hundred reply — pending (sent same day, too early to expect a reply)
- [ ] The actual WHIM correlation test — cannot start until one of the above unblocks

## Phase 4 — Cosmological bridge F→H(z) — BLOCKED, redirected

- [x] 8 direct-reconstruction attempts (NR-001–005, 008, 009, 013) — all failed, one
  common root (bridge underdetermined without TJB's parameters)
- [x] Duhem-Quine classification applied retroactively (pearl, 2026-07-18) — none of the
  8 is `theory_killed`, all are `bridge_family_killed` / `parameterization_killed`
- [x] Literature-search pivot (`docs/123`, boyko-goal-expansion-100, 53 candidate ideas)
- [ ] A literature-derived bridge candidate actually tried against Table A1 — NOT started

## Phase 5 — Correspondence (external, not code)

- [ ] TJB reply — outstanding ~18 days
- [ ] The Three Hundred reply — outstanding, sent today
- Both are hard blockers for Phase 3 and Phase 4 respectively; no code work can unblock
  either.

## Not started

- H1b execution itself (blocked on Phase 3/5)
- Any literature-bridge candidate execution (blocked on Phase 4, though the search itself
  is unblocked and could resume)
- `symbols.md` variable registry (flagged as a process gap since 2026-07-01, still open)
- Repo memory-hygiene cleanup (`activeContext.md`/`goals.md` bloat, flagged in the
  2026-07-17 research-audit, not yet acted on)
