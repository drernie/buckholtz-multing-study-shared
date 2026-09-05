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
- **P193: the P191 pearl's own prediction is CONFIRMED** — z∈{12,14,16}
  gives up to **5.4× more** shrinkage than P191's own z∈{3,5,7,10} at
  matched precision (72.87% vs 13.6% at σ=10%, both finite-difference,
  apples-to-apples). Separate real methodological finding: standard
  finite-difference Hessian computation (this project's default since
  P176) does not converge at σ∈{1%,3%} this close to P192's found
  boundary — resolved with an independent analytic Fisher matrix,
  cross-validated at 0.1% agreement in the one case both methods reach.
  Two rounds of context-blind Step 8a skeptic review, both real issues
  found and fixed (a 100% unit-conversion bug; a methodological gap in
  the cross-validation's own scope).
- **P194: a dense information-profile scan of the (10,16.957) window**
  confirms `CLAIM_P194`'s falsifiable predicate (monotonic rise toward
  the boundary, 16.24%→75.12% shrinkage at σ=10%) and directly confirms
  its own pre-written correction that greedy top-N points are not
  guaranteed jointly optimal — P193's specific {12,14,16} beats the
  naive greedy top-3 at tight precision (1%, 3%) and loses narrowly at
  loose precision (10%), a real mixed result, not a clean win either
  way. A second, more targeted Step 8a skeptic pass (round 2, same day)
  found round 1's own fix incomplete: the rise is **not** uniquely a
  1/H(z) boundary-singularity effect — measured directly, cumulative
  E1(z)/E2(z) growth (2.3-2.4×) and 1/H(z)² boundary-proximity growth
  (7.0×) are comparable order of magnitude, both real, neither
  negligible. P193's own numbers are unaffected; only the mechanism
  attributed to them is now honestly qualified as entangled, not
  resolved. See `FINDING_P194`.

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
| 3 | Absolute scale / observable mapping | STRUCTURALLY BLOCKED, quantified buildable path exists and CONFIRMED stronger further from baseline (P191→P193), within a known domain limit (P192: z<16.957); P194 mapped the full information profile across the window and found the "further is better" mechanism is entangled (not resolved) between 3 co-varying candidates | A real high-z H(z) survey — z∈{12,14,16} (P193) is competitive but not uniformly better than a denser greedy set (P194); precision-dependent — see §5 |
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

**DONE 2026-09-05 (same day), with an explicit user go-ahead** —
`FINDING_P193`. z∈{12,14,16} gives up to 5.4× more shrinkage than
P191's own z∈{3,5,7,10} at matched precision — the P191 pearl's own
prediction CONFIRMED, more strongly than its own wording required.
Surfaced a real, separate methodological finding along the way:
standard finite-difference Hessian computation does not converge at
σ∈{1%,3%} this close to P192's found boundary — resolved with an
independent analytic Fisher matrix, itself cross-validated to <0.15%
agreement wherever finite-difference converges.

**DONE 2026-09-05 (same day), with an explicit user go-ahead** —
`FINDING_P194`. A dense scan of the full (10, 16.5) window confirms the
information profile rises monotonically toward the boundary (16.24%→
75.12% shrinkage at σ=10%) and directly confirms the claim's own
pre-written correction: the greedy top-3/top-4 set does **not**
uniformly beat P193's {12,14,16} — it wins at loose precision (σ=10%)
and loses at tight precision (σ=1%,3%), a genuinely mixed result. A
second, more targeted Step 8a skeptic pass found the rise is **not**
uniquely a 1/H(z) boundary-singularity effect as a first fix suggested
— measured directly, cumulative E1(z)/E2(z) growth (2.3-2.4×) and
1/H(z)² boundary-proximity growth (7.0×) are comparable order of
magnitude. P193's raw numbers are unaffected; the causal story behind
them is now honestly qualified as entangled among ≥3 co-varying
candidates, not resolved to one.

**RECOMMENDED, NOT AUTHORIZED, next candidate**: none named yet for
bottleneck 3 — P191→P194 has mapped the buildable path and its
information profile thoroughly; further work here would need either a
genuinely new question (not another z-set variant) or a decision to
apply the analytic Fisher matrix as the default method near any future
domain boundary elsewhere in the project. Pearled,
`pearl_registry/INDEX.md` next_check 2026-12-15 (3 rows: P193's
numerical-methods lesson, P194's confounded-single-coordinate-scan
lesson, and the confirmed-pearl chain P191→P193).

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
