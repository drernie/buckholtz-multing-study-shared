# 155 — Engineering Debt Cleanup (2026-09-05)

**Scope:** autonomous, reversible engineering-hygiene pass through the
"Known engineering debt" items named in `CURRENT_EVIDENCE_STATE.md`.
Explicitly excluded from this pass (per that file's own boundaries and
this project's standing constraints): new physics bottleneck research,
any TJB correspondence, and the `pyproject.toml` version bump (a release
decision, not an engineering-hygiene one).

## What changed

| Item | Before | After | Commit |
|---|---|---|---|
| `ruff format` | 34 files unformatted | 0 | `c9a0ded` (prior phase) |
| `mypy src` | 24 errors, 7 files | **0 errors** | `1e43b75` |
| `goals.md` | 43 duplicate stale entries | cleaned, archived | `4c94456` |
| Test coverage, `double_inversion_plots.py` | 0% | **100%** | `511459a` |
| Test coverage, `cluster_data_pipeline.py` | 0% | 29% (pure functions only) | `511459a` |
| Project coverage (`--cov=src`) | 83% | 87% | `511459a` |
| Reviewer verdict log | — | tracked | `6dbd178` |

Final state, verified fresh after all changes: **901/901 tests pass**,
`ruff check .` clean, `mypy src` clean (0 errors, 38 files).

## mypy fixes — root causes, not blanket suppressions

24 errors were not 24 independent problems. `internal_anchor_search.py`
alone accounted for 11 of them, all from a single wrong return-type
annotation (`generate_simple_ratios() -> list[CandidateFormula]` when it
actually returns raw tuples, same convention as its three sibling
generator functions) that made mypy misread a downstream tuple-unpacking
loop. Fixing the one annotation cleared all 11.

The remaining 13 fell into three genuine categories, each fixed at the
actual cause rather than blanket-silenced:

- **Real optional field** (`appendix_a1_procedure_registry.py`):
  `TableA1Row.h_mult`/`sigma_mult` were typed `float` but the z=0 anchor
  row in the real `TABLE_A1` data genuinely carries `None` for both —
  that's the source data, not a bug. Widened to `float | None`.
- **Untyped-third-party `Any` leaking through arithmetic** (`cluster_schedule.py`,
  `k_a_independent.py`, `cluster_data_pipeline.py`): fractional-exponent
  `**` and astropy's stub-less `.value` accessor make mypy infer `Any`
  even though the runtime value is a real `float`. Fixed with scoped
  `float()` wraps at the return statement, not with `# type: ignore`.
- **One new mypy override** (`pyproject.toml`): astropy/astroquery lack
  type stubs, same situation this project already handles for
  scipy/matplotlib/pandas — added the matching
  `ignore_missing_imports = true` override rather than repeating
  per-call-site ignores.
- **One genuinely untraceable dynamic import** (`report.py`): a
  `sys.path.insert()` runtime fallback for direct-script execution,
  which mypy cannot trace statically — this is the one case where a
  scoped `# type: ignore[import-not-found]` was the correct fix, not a
  workaround (the imported module, `hmult_closure_candidates.py`, was
  verified to exist on disk before adding the ignore).
- **One list-vs-tuple mismatch** (`double_inversion_plots.py`):
  matplotlib's `imshow(extent=...)` wants a tuple; a list was passed.
  Pure type-only fix, no behavioral difference.

All fixes independently reviewed by `Agent(reviewer)` afterward
(context: staged diff only, no session history) — no logic bugs found;
its sole reservation (couldn't run pytest itself, sandboxed) is resolved
by the direct `pytest`/`ruff`/`mypy` runs recorded above, both before and
after committing.

## goals.md cleanup

`goals.md` had accumulated 43 near-identical "Carried from compaction"
blocks between 2026-06-12 and 2026-08-30 — a compaction hook appending
the same two stale pending items on every compaction, never pruned. Both
items (an "Option 1 bridge D̈∝F/M" test, and the C9 "why exponent 12"
mechanism question) are from the June/July Eq.32 mechanism-hunt, already
closed per `CLAUDE.md`'s own "CLOSED WORKSTREAMS" section. Full
pre-cleanup content archived at
`.claude/memory/archive/goals_pre-2026-09-05-stale-cleanup.md`, following
this project's established archive-before-trim convention (the same
pattern already used 20+ times for `activeContext.md`). Nothing deleted.

Also reverted, in passing: a compaction hook had inserted stray
`[summarized]` markers and doubled blank lines into `activeContext.md`
during this session's own context compaction. That was pure formatting
noise from the hook, not real content change — restored to the exact
pre-compaction byte content (confirmed via `git diff` showing no diff
after the fix).

## New test coverage — what was and wasn't added, and why

Two files sat at genuine 0% coverage: `double_inversion_plots.py` (pure
plotting side effects) and `cluster_data_pipeline.py` (a network-I/O data
pipeline: VizieR via astroquery, GitLab HTTP, a hardcoded literature
table). Both were flagged going in as needing careful scoping to avoid
validation theater — writing weak tests that assert nothing meaningful
just to move a coverage number.

**`double_inversion_plots.py` → 100%.** All 4 plotting functions
(`plot_isoline_for_z`, `plot_grid_heatmap`, `plot_h_comparison`,
`generate_all_plots`) are genuinely pure once given real `ClusterRow`/
`GridSearchSummary` inputs — no network, no external state. Tests use
matplotlib's `Agg` backend + `tmp_path` and assert the function runs to
completion and writes a non-empty PNG, including the "no admissible
result" branch (`best_physical`/`best_unconstrained` both `None`).
Deliberately **not** a pixel-content check — that would be a different
kind of theater (asserting a plot "looks right" without looking). What
this catches: wrong argument order/type, matplotlib API drift, broken
imports — real regression classes, honestly scoped.

**`cluster_data_pipeline.py` → 29%, not higher, on purpose.** Only the
functions with no network or filesystem dependency were tested:
`e_thermal_path_a`/`e_thermal_path_b` (thermal-energy formulas — checked
via linearity/monotonicity properties that any correct implementation
must satisfy, plus one anchored regression value, not just "does it
return the same number the code already returns"), `_sexagesimal_to_deg`
(hand-verified against a known coordinate transform:
06h58m30s → 104.625°), and `step3_merger_flags` (DataFrame
exclusion logic, both bare- and full-ID formats).
`step1_mcxc`/`step2_psz2`/`step4_export`/`step5_hz`/`main()` are left
uncovered deliberately — they hit real external services (VizieR,
GitLab), and mocking those out would test the mocks, not the pipeline,
while hitting the network from a unit test is flaky by construction.
This is a scope decision, not a gap that was missed.

**Side finding, not acted on:** `_HARD_EXCLUDE_NAMES`
(`cluster_data_pipeline.py:56`) is defined but never referenced by
`step3_merger_flags` — only `_HARD_EXCLUDE_IDS` is checked. Traced and
confirmed **not a live bug**: `cluster_id` always comes from MCXC's own
ID column (`step1_mcxc`), never the alternate names
(`"1E 0657-56"`, `"ACT-CL J0102-4915"`) that `_HARD_EXCLUDE_NAMES` holds
— so the set is effectively dead code given the actual data flow, not a
gap that lets a merger cluster through. Left as-is; noted here for
whoever next touches merger exclusion.

## Not done in this pass

- `pyproject.toml` version bump — a release decision.
- Any TJB correspondence.
- New physics bottleneck research.

## Addendum — external review fix round (2026-09-05, same day)

An external review of the pass above (verdict 8.5/10) found 7 issues.
Verified each against the actual repo state before acting — 6 confirmed
real, 1 (parent-repo dirty state) correctly out of scope. Fixed:

| # | Issue | Fix | Commit |
|---|---|---|---|
| P1 | `CURRENT_EVIDENCE_STATE.md`/`CLAUDE.md`/`README.md` still showed the pre-cleanup numbers (24 mypy errors, 83% coverage, both target files 0%) | Synced to real numbers, twice — once after the mypy/goals/coverage commits, again after this fix round's own coverage expansion | `7c46224` |
| P1 | Fisher-forecast test (bottleneck 3) was ambiguously worded — `activeContext.md` said "nothing pre-authorized beyond §5," which by exclusion implies §5 *is* authorized, though §5 itself never claims that | Applied the "RECOMMENDED, NOT AUTHORIZED" convention this project already uses for bottleneck 1 (`docs/153`) to bottleneck 3 as well, consistently across `CURRENT_EVIDENCE_STATE.md`, `activeContext.md`, `goals.md` | `7c46224` |
| P2 | CI's `mypy` step had `continue-on-error: true` (justified by debt that's now gone); no `ruff format --check` step existed | Made `mypy` blocking, added the format-check step | `a0a3cbe` |
| P2 | `cluster_data_pipeline.py`'s "29%, rest is network I/O" was too conservative — `step4_export` has zero network dependency, and the other steps' real transformation logic is separable from the actual I/O call | Monkeypatched only `_vizier_download`/`requests.get` (the real I/O boundary), not whole step functions — 29% → 93% | `0234e3b` |
| P3 | `double_inversion_plots.py`'s `plot_grid_heatmap` raised a `UserWarning` calling `legend()` with no labeled artists | Guarded on `best_physical`/`best_unconstrained` presence | `64c70d4` |
| P3 | `internal_anchor_search.py`'s mypy fix widened to bare `list[tuple]`, losing element-shape information | Added `RawFormula = tuple[str, float, float, tuple[str, ...]]`, applied consistently (return types + `all_formulas` + each generator's local `formulas` list, which needed its own annotation — mypy's list invariance narrows an unannotated local to the literal types actually appended) | `64c70d4` |
| P3 | Parent repo (`H - 11 Dr. Thomas J. Buckholtz`, one level up) has pre-existing uncommitted changes | Correctly identified by the review as out of scope — not touched | — |

One bug found while writing the new tests, in the test fixture itself
(not the source): an out-of-range `dec_deg=999` on a deliberately-
non-matching row broke `SkyCoord` construction for the *entire*
coordinate-fallback batch (built once for all unmatched rows together),
not just that row. Caught by the test failing, fixed to a valid-but-
distant coordinate — a small real lesson about `step2_psz2`'s batching
behavior, worth knowing if anyone extends `_crossmatch_idx`'s callers.

Final state after this fix round: 908 tests passing (901 → 908),
coverage 91% (87% → 91%), `cluster_data_pipeline.py` 93% (29% → 93%),
mypy/ruff/format all clean and now enforced in CI. 4 additional commits:
`7c46224`, `a0a3cbe`, `64c70d4`, `0234e3b`.
