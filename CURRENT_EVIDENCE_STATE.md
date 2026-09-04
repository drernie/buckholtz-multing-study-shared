# Current Evidence State — buckholtz-idm-multing-mvp

**Date:** 2026-09-03 · **Verified this session:** `pytest tests/` 881 passed,
`ruff check .` clean, `ruff format --check src tests` 34 files would
reformat, `mypy src` 24 errors/7 files, coverage 83% (`src/cluster_data_
pipeline.py` and `src/double_inversion_plots.py` both 0%).
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
| 3 | Absolute scale / observable mapping | STRUCTURALLY BLOCKED, sharpened by P190 | Fisher-forecast on synthetic high-z H(z) points (pearled, not started) |
| 4 | IC-sensitivity | CLOSED (campaign exhausted, question genuinely open) | A genuinely new mechanism class, not a 6th variant of the 5 already excluded |

## 5. One next differentiating test

**Fisher-information forecast for bottleneck 3** (pearled, `pearl_registry/
INDEX.md` next_check 2026-11-15): does adding synthetic H(z) points at
z>2 (where P190's single-z slope diverges furthest from the low-z end)
measurably rotate/shrink the (β1,β2) degeneracy ellipse? This is the one
open bottleneck with a concrete, not-externally-blocked, not-yet-attempted
next step — everything else either needs external data (Belle II Run 2,
TJB's own β_d derivation) or a genuinely new idea, not another rerun.

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

## Exclusion zone (do not start without a new triggering fact)

New numerology searches on Eq.32 beyond what NR-019/020/021 already
covered; ML-based spectral analysis; Tensor Train/FFT optimization of
existing code; a new MCMC run; a 5th variant of the bottleneck-1 bridge
shortcut. None of these change the status of the central claims —
`docs/147`'s own stop-rule already governs this.

## Known engineering debt (real, verified, not urgent)

`mypy` 24 errors/7 files (advisory in CI, not blocking); `ruff format`
34 files not yet reformatted; `src/cluster_data_pipeline.py` and
`src/double_inversion_plots.py` at 0% test coverage (the former is a
real data pipeline, not just a plotting layer — higher priority of the
two); `pyproject.toml` version frozen at `0.3.0` since the MVP era;
`.claude/memory/goals.md` carries 43 repeats of a 2026-06-12 stale
pending item, never cleaned across ~90 days of compaction cycles.
