# CODE_AUDIT_HARDENING — buckholtz-idm-multing-mvp / 2026-09-06

First run of `sci-code-audit` on this project (never run before). Scope:
active pipelines — `src/cluster_data_pipeline.py` → `src/pearson_fit.py` →
`src/report.py` (this project's own F→H(z) construction, used by the
`P*`/`r011` lineage), and `src/provenance_audit.py` + `experiments/
20260906-evidence-authority/E8-E15` (TJB's own v82 33-point chi2 chain,
today's active line). Not a from-scratch review of all 39 `src/` files or
20+ experiment folders — real evidence gathered on the load-bearing paths,
per the Cheapest Differentiating Test Protocol.

## Audit Status: COMPLETE (first pass — not exhaustive)

## Layers Checked (10/10)

| Layer | Status | Findings | Action |
|-------|--------|---------|--------|
| 0 — Stop spread | ✅ | No new physics claim made during this audit | — |
| 1 — Materiality | ⚠️ | `src/conflict_resolver.py` + `src/source_provenance.py` are tested (2 test files) but called by NOTHING else in the repo — not `report.py`, not `provenance_audit.py`, not any experiment. They implement a symbol-precedence/conflict-resolution registry that looks like exactly the "symbol registry" gap #2 named as open in `~/.claude/rules/research-methodology.md`, built here and never wired in. | Note only — see plan below |
| 2 — Silent fallbacks | ✅ | Full `src/` grep for `except: pass/continue`, `fillna`, `nan_to_num`, silent `return None/[]/{}`: zero bare `except: pass`; the 2 `except Exception` sites are both in `cluster_data_pipeline.py` (audited last session — already log the real exception at `warning` level); every `return None` found is a documented "not found" sentinel, not a masked failure | — |
| 3 — Metrics/norms | ✅ | `pearson_fit.py`'s `grid_search_pearson`/`single_pearson` compute one Pearson r per parameter point — no multi-seed/multi-run aggregation, so the "mean of ratios vs ratio of means" risk this layer specifically warns about does not apply here | — |
| 4 — Core computation | ✅ | Covariance construction (`E8_full_covariance_propagation.build_cov_cc`→`make_chi2_cov`) uses `scipy.linalg.cho_factor`, which raises `LinAlgError` on a non-SPD matrix — an implicit but real positive-definiteness check, exercised by this session's own new `test_covariance_pipeline_runs_end_to_end` | — |
| 5 — Invariants | ⚠️ | No centralized `assert_valid_covariance()`/`assert_valid_chi2()` utility — invariant checks (chi2≥0, eigenvalue>0, SPD) are ad hoc, one-off asserts inside individual test functions (today's own new E8/E11 tests included) rather than a reusable invariant layer | Note only — low urgency, current coverage is real even if not centralized |
| 6 — Controls/baseline | ✅ | Already the project's strongest layer — every `E`/`P` experiment this session carries positive controls reproducing TJB's own published numbers to <0.5%, plus at least one negative/floor control (e.g. E15's σ→0 unity check, E8's 100%-correlated negative control) | — |
| 7 — Data provenance | ✅ | Cross-checked: `data/hz_cc.csv`'s sha256(pandas-hash) is `9a3af5f845c2f4a4`, byte-identical to the hash recorded in `experiments/20260713-r011-beta-profile-nesting/decision.md` from **2 months earlier** — the underlying Moresco H(z) table has not silently drifted between the July `r011` line and today's `E5`/`E8` line, despite the dead-URL bug found today (the bug only affected the *live-fetch* path; the hardcoded fallback both lines actually used has been stable) | — |
| 8 — Statistical interpretation | ✅ | MCID thresholds are pre-registered before each experiment (`CLAIM_E*.md` files exist for every `E` script), not fitted after seeing results — already this project's own discipline | — |
| 9 — Docs/code mismatch | ⚠️ | `CLAUDE.md`'s own header stated "908 passing" — now fixed to 939 (this pass). `PROJECT_STATUS.md` is separately, explicitly banner-flagged as superseded (CLAUDE.md already says so). `docs/INDEX.md` itself says "Last updated: 2026-07-12" and its own numbered sections stop around doc 120 — it does not cover docs 121-157, a real, dated gap | `CLAUDE.md` count fixed; `docs/INDEX.md` full resync is a separate, larger task, out of scope for this pass — noted, not done |
| 10 — Reproducibility | ⚠️ | CI (`.github/workflows/ci.yml`) runs real matrix tests on Python 3.11/3.12/3.13 — verified. But `pyproject.toml`/`requirements.txt` pin only lower bounds (`numpy>=1.24.0` etc.), no lockfile — a future numpy/scipy release could shift floating-point results at the margin. Partial mitigation: every numeric test already uses an explicit relative-tolerance MCID (not exact equality), so small drift would not silently pass as "unchanged" — it would fail loudly | Acceptable for a research repo; would only become urgent if a CI run starts failing on tolerance after a dependency bump |

## Overall Verdict

**PROVISIONAL — no STOP-level finding.** The two ⚠️ items with concrete
follow-up value are Layer 1 (unwired symbol-conflict registry) and Layer 9
(one stale number in `CLAUDE.md`). Everything else is either clean or an
accepted, honestly-stated tradeoff (Layer 10).

## Rerun Required?

**NO.** No finding here changes any existing numeric result — this audit
found gaps in *infrastructure* and *documentation currency*, not errors in
any promoted claim.

## "Антистыдный" чеклист

- [x] Audit run for the first time (not externally triggered — self-initiated per today's `boyko-project-radar` blind-spot list)
- [x] Not ignored — findings recorded below, not silently dropped
- [x] Materiality distinguished (active pipeline vs. unused registry module)
- [x] Bugs found: none new (the Layer 2/9 items are non-bugs — a docs number and an unwired module)
- [x] Documented in this file
- [x] `CLAUDE.md` test-count sync — done this pass
- [ ] `conflict_resolver.py`/`source_provenance.py` wiring decision — queued (see `docs/157`)
- [ ] `docs/INDEX.md` resync (docs 121-157 missing) — queued, out of scope for this pass
