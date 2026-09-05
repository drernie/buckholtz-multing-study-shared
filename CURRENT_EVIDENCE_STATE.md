# Current Evidence State — buckholtz-idm-multing-mvp

**Date:** 2026-09-03, quality snapshot refreshed 2026-09-05, then again
after an external review's fix round the same day (see
`docs/155_engineering_debt_cleanup_20260905.md` for the full cleanup
report and its own addendum) · **Verified:** `pytest tests/` 908 passed,
`ruff check .` clean, `ruff format --check src tests` clean, `mypy src`
0 errors/38 files, coverage 91% (`src/double_inversion_plots.py` 100%,
`src/cluster_data_pipeline.py` 93% — the remaining 7% is `_vizier_
download`'s own real body, two hard-to-trigger ImportError fallbacks,
and main()'s astroquery-missing SystemExit path; see docs/155 for the
scope reasoning).
**Supersedes as the entry point:** `README.md`'s dated quality-snapshot
line, `PROJECT_STATUS.md` (already self-flagged superseded),
`.claude/memory/goals.md` (43× stale repeated pending item from 2026-06-12).
**Does not supersede:** `.claude/memory/activeContext.md` (still the live,
per-commit source of truth for "what are we doing right now" —
this file is the slower-moving strategic layer above it).

---

## 1. What is reproduced

- **F_oP bilinear structure** (docs/125, P1) — exact 2-species form,
  alternating-sign rule derived as a theorem for the two-charge
  completion, not postulated.
- **Isotropic-average k-sector = exactly zero** at force level
  (double-layer theorem, ~1e-16 numerically) and at Shtanov-Sahni
  background-coupling level, for any q(a).
- **Eq.32 numerical match** (0.0135%, PDG 2024) — `[VERIFIED]`, unaffected
  by everything below; only its *interpretation* is contested.
- **AVB benchmark solving arm** — N=32 corpus, both arms, full pipeline
  (skeptic + blind Run-3 + K5 reproducibility) — real bug found+fixed in
  a global hook (`agent_tool_scope_guard.py`) along the way.
- **Cen, Bahcall & Gramann (1994) Figure 3 recovery** — digitized,
  cross-validated to 0.057% against the paper's own Table 1 anchor;
  sent to TJB 2026-09-03.
- **P191: a Fisher-information forecast shows bottleneck 3's "in-
  principle openness" (P190) is practically buildable** — synthetic
  H(z) points at z∈{3,5,7,10} would shrink v82's own (β1,β2) degeneracy
  ellipse by 73%/46%/14% at 1%/3%/10% assumed relative precision
  (MCID met at all three, though only marginally at 10%). A real bug
  (sparse-grid integration silently zeroing one point's Fisher
  information) was caught and fixed by a context-blind Step 8a skeptic
  pass before this number was trusted — see docs/145-style correction
  in `FINDING_P191` itself. Side finding: the (β1,β2) level-set slope
  peaks near z≈3 and *declines* thereafter — not monotonic, not simply
  saturating, as `CLAIM_P191`'s own outcome table had anticipated.
- **P192: TJB's own real fitted (β1,β2) make H²(z) go negative
  (mathematically undefined) at z≈16.957** — grid-converged (4
  densities), straddle-confirmed, skeptic CONFIRMED-REAL. The
  reconstructed model cannot even be evaluated past this boundary,
  regardless of what question is being asked there — a standing
  precondition for any future high-z work on this reconstruction, not
  a one-off caveat.

## 2. What is refuted or weakened

- **P189 finite-r shortcut** — REJECTED (category error, tautology).
- **P189b normalized derivation** — WEAKENED (normalization is a
  convention choice, not physically forced).
- **P158-ADDENDUM literature grounding** — REJECTED (real citations,
  wrong quantities — measurement-scatter ≠ population-spread).
- **P158-ADDENDUM2 real hmf/Tinker computation** — WEAKENED (correct for
  4 of 8 target redshifts; the other 4 extrapolate past the fit's own
  calibration range).
- **P190: v82's own (β1,β2) degeneracy is APPROXIMATE, not exact**
  (12.7% spread in the level-set slope across z) — skeptic CONFIRMED-REAL.
  Rules out the strongest "structurally unbreakable" reading of
  bottleneck 3, without providing a practical fix.
- **NR-020: Eq.32's timing-axis numerology criterion (H1) FALSIFIED**
  by a real historical counter-example (Balmer 1885) — a DoF-ratio-based
  fallback survived only as an unattacked hypothesis.
- **NR-021: the DoF-ratio criterion (H1') hit two independent problems**
  before power was even the binding constraint — real N=11 (not the
  needed ~60), and a blind inter-rater check found the primary predictor
  itself is coder-dependent (2-6× divergence on identical facts).
- **CONSILIENCE_eq32.md:** three independent methods (formal derivation,
  statistical null-model, real experimental check) converge on
  non-support for Eq.32 as a genuine relation — **and surfaced a real
  correction mid-synthesis**: Belle II already measured m_τ in 2023
  (1777.09±0.08±0.11 MeV), giving **1.84σ tension** with Eq.32's exact
  prediction (1776.840 MeV) — ambiguous, not decisive. `paper/main.tex`
  synced with this finding 2026-09-03.

## 3. What changed after v82

- The 2026-08-23 framing "no published F→H(z) bridge exists" is
  `OLD-FORMULATION-SUPERSEDED` — v82 publishes an explicit accretion-
  kinematics bridge with `m_A(z)`, `r_A(z)`, `k_A(z)` (docs/149, docs/153).
- This does **not** mean the bridge is validated or that bottleneck 1 is
  closed — it means the *precondition for asking the question* changed.
  The restated, still-open question: is this project's own isotropic-
  average Shtanov-Sahni closure compatible with v82's finite-r,
  single-pair construction? `docs/153` §3a names 3 preconditions; none
  are resolved (4 attempts today, all REJECT/WEAKENED — see §2).

## 4. Four open bottlenecks (per `docs/147`)

| # | Bottleneck | Status | What would move it |
|---|---|---|---|
| 1 | F→H_MULT(z) bridge | BLOCKED | z≥1 needs nonlinear-bias/N-body, not another analytic substitution |
| 2 | Unique completion | Untouched, `docs/134` | — |
| 3 | Absolute scale / observable mapping | STRUCTURALLY BLOCKED, quantified buildable path exists (P191) within a now-known domain limit (P192: z<16.957) | A real high-z H(z) survey at z∈{3,5,7,10}, 1-10% precision (P191); or a 3rd Fisher-forecast at z∈(10,17), the last window before the found boundary (pearled, `pearl_registry` next_check 2026-12-15) — see §5 |
| 4 | IC-sensitivity | CLOSED (campaign exhausted, question genuinely open) | A genuinely new mechanism class, not a 6th variant of the 5 already excluded |

## 5. One next differentiating test

**DONE 2026-09-05, with an explicit user go-ahead** — `FINDING_P191`.
Result: adding synthetic H(z) points at z∈{3,5,7,10} would shrink the
(β1,β2) degeneracy ellipse by 73%/46%/14% at 1%/3%/10% assumed relative
precision — MCID (≥10% shrink) met at all three, marginally at 10%.
Does **not** resolve bottleneck 3 (no real high-z data exists; the
absolute-scale/observable-mapping question, `docs/134`, is untouched) —
it shows the "in-principle openness" P190 found is practically
buildable, and quantifies the cost/benefit as a function of assumed
precision.

**DONE 2026-09-05 (same day), with an explicit user go-ahead** —
`FINDING_P192`. The requested second Fisher-forecast at z∈{20,30,50}
was **TASK_INFEASIBLE as specified**: TJB's own real fitted (β1,β2)
make `H²(z)` go negative (mathematically undefined) at z≈16.957 —
grid-converged, straddle-confirmed, skeptic CONFIRMED-REAL. All three
requested z sit past this boundary. Does not falsify P191's own pearl
prediction (the test that would confirm/deny it was never constructible
at these z) — it identifies a prior domain-of-validity constraint any
future z-choice past P191's z≤10 must respect.

**RECOMMENDED, NOT AUTHORIZED, next candidate** (same convention
`docs/153` §3a uses for bottleneck 1 — being the best-scoped candidate
is not pre-approval to run): a **third** Fisher-forecast using
synthetic z in the last remaining well-defined window, `(10, 17)` —
between P191's own z≤10 and P192's found boundary at z≈16.957 (e.g.
z∈{12,14,16}) — pearled, `pearl_registry/INDEX.md` next_check
2026-12-15. The P191/P192 machinery is already positive-controlled and
reusable; this would only need a different `synth_zs` argument, already
checked to stay within the domain of validity.

## 6. What cannot be claimed publicly right now

- That Eq.32 reflects a genuine physical relation (three independent
  checks converge on non-support; the numerical match itself remains
  real and unexplained).
- That the F→H_MULT(z) bridge is validated, resolved, or even that its
  3 named preconditions are close to answered (4 attempts today, 0
  resolved).
- That the (β1,β2) degeneracy is a solved or fully-characterized problem
  (P190 narrowed it, did not close it).
- That `paper/main.tex` is submission-ready — it is explicitly marked
  `NOT_FOR_SUBMISSION · PARTLY SUPERSEDED` and should stay marked that
  way until bottleneck 1 or 3 actually resolves.
- Any AVB benchmark result as confirming or refuting the treatment-vs-
  baseline hypothesis — N=25, McNemar p=1.0, underpowered by design.
- That P191's Fisher-forecast establishes real high-z H(z) data at the
  assumed precision is achievable, or that bottleneck 3 is resolved —
  it only shows a quantified, in-principle path exists (see §5).

## Exclusion zone (do not start without a new triggering fact)

New numerology searches on Eq.32 beyond what NR-019/020/021 already
covered; ML-based spectral analysis; Tensor Train/FFT optimization of
existing code; a new MCMC run; a 5th variant of the bottleneck-1 bridge
shortcut. None of these change the status of the central claims —
`docs/147`'s own stop-rule already governs this.

## Known engineering debt (updated 2026-09-05, see docs/155)

**Closed 2026-09-05 (cleanup pass + same-day external-review fix
round):** `mypy` 24→0 errors, now blocking in CI (was advisory);
`ruff format` clean, now enforced in CI via a new `ruff format --check`
step (there wasn't one); `src/double_inversion_plots.py` 0%→100%
coverage; `src/cluster_data_pipeline.py` 0%→93% coverage (only the
real network I/O boundary is monkeypatched — `_vizier_download`,
`requests.get` — everything downstream runs for real; see docs/155 for
the reasoning and its addendum for why the first pass's 29% was too
conservative); `.claude/memory/goals.md`'s 43 stale duplicate entries
removed and archived; a real authorization ambiguity around the
Fisher-forecast test fixed (see docs/155 addendum).

**Still open:** `pyproject.toml` version frozen at `0.3.0` since the MVP
era (a release decision, out of scope for engineering-hygiene passes).
