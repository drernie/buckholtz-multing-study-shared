# Corpus Manifest — N=32 (26 defect-seeded + 6 clean)

Per plan Phase B. Each task is a self-contained "review this analysis"
mini-task with a public file (`task.md` + a script/data) and a private
answer key (`corpus/_answer_key/task_NNN.md`, never given to any arm).

**Leakage note (per the 2026-09-01 pilot findings):** no task below
touches TJB correspondence, Table A1/provenance-gate lore, Eq.32/4-3
numerology, or the artifact-identity ("Figure 3") incident — those
themes are contaminated via this project's own persistent MEMORY.md,
confirmed present even with the SubagentStart hook disabled. All tasks
below re-enact the underlying *mechanism* from `docs/146` in a fresh,
unrelated domain (materials science, signal processing, ML, finance,
engineering, chemistry) with fresh numbers and variable names.

| Task | Tier | Category (docs/146 #) | Domain | Defect? |
|---|---|---|---|---|
| task_001 | A | 1 — post-hoc numerology | materials science (lattice ratio) | Yes |
| task_002 | A | 2 — tautological control | signal processing (filter identity) | Yes |
| task_003 | A | 3 — false independence | ML (shared preprocessing across "independent" folds) | Yes |
| task_004 | A | 4 — silently-fixed parameter | curve fitting (2-param sweep, one fixed at 0) | Yes |
| task_005 | A | 5 — narrow-to-broad overclaim | statistics (subgroup result generalized) | Yes |
| task_006 | A | 6 — reused weakened result | engineering tolerance (soft bound cited as hard) | Yes |
| task_007 | A | 7 — control at trivial zero | circuit simulation (control run where term vanishes) | Yes |
| task_008 | A | 8 — domain heuristic misapplied | epidemiology-style stats (more-tests heuristic backwards) | Yes |
| task_009 | A | 9 — numerical artifact | numerical integration (quad overflow at extreme bound) | Yes |
| task_010 | A | 10 — recomposition overclaim | reliability engineering (chained sub-claims) | Yes |
| task_011 | A | 11 — provenance/attribution error | financial modeling (stale constant) | Yes |
| task_012 | A | 2 — tautological control (repeat) | chemistry/kinetics (definitional identity) | Yes |
| task_013 | A | 3 — false independence (repeat) | astronomy-adjacent, non-MULTING (shared calibration) | Yes |
| task_014 | A | 9 — numerical artifact (repeat) | optimization (boundary-copied bounds, P128-style) | Yes |
| task_015 | A | 4 — silently-fixed parameter (repeat) | ML hyperparameter sweep (hidden fixed regularization) | Yes |
| task_016 | B | 2 — tautological identity (closer lift, P51-style) | abstract algebra/physics-adjacent | Yes |
| task_017 | B | 7 — control at g=0 (closer lift, P74/P82-style) | field-coupling toy model | Yes |
| task_018 | B | 9 — quad overflow (closer lift, P122-style) | numerical integration, extreme exponent | Yes |
| task_019 | B | 11 — mutable-default-argument (closer lift, P4-style) | Python data-pipeline gotcha | Yes |
| task_020 | B | 4 — box-excluded optimum (closer lift, NR-013-style) | grid-search optimization | Yes |
| task_021 | C | Artifact Zoo: empty_input | ML pipeline | Yes |
| task_022 | C | Artifact Zoo: duplicate_ids | data pipeline (silent overwrite) | Yes |
| task_023 | C | Artifact Zoo: perfectly_separable (leakage) | ML classifier | Yes |
| task_024 | C | Artifact Zoo: all_nan_input | signal processing | Yes |
| task_025 | C | Artifact Zoo: non_hermitian-analog | linear algebra/PCA | Yes |
| task_026 | C | Artifact Zoo: adversarial_input | small ML inference script | Yes |
| task_027 | clean | — | statistics (correct control-group comparison) | No |
| task_028 | clean | — | ML pipeline (proper train/test split) | No |
| task_029 | clean | — | numerical integration (well-behaved bounds) | No |
| task_030 | clean | — | parameter sweep (properly profiled) | No |
| task_031 | clean | — | financial modeling (provenance-consistent) | No |
| task_032 | clean | — | signal processing (proper NaN handling) | No |

**One seeded defect per defect-task** (never 0/1/multiple mixed), per
Phase B's own anti-tautology rule. **n-gram overlap check**: every task
below is written from scratch in a domain this project has never used
for physics content — overlap with any `FINDING_P*.md`/`docs/*` text is
structurally near-zero by construction (different domain vocabulary),
not just checked after the fact.
