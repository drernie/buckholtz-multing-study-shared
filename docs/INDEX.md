# Documentation Index — Buckholtz IDM/MULTING Audit

**Last updated:** 2026-09-07 (docs 122-157 indexed; previously stale since 2026-07-12)
**Total documents:** 96 markdown files

**Note:** This index was regenerated 2026-07-12 after removing author-facing correspondence,
meeting notes, and communication-strategy documents from the public repo (letters, email drafts,
call outlines, send-readiness reviews — kept locally, not tracked here). Only technical/scientific
audit content remains indexed below. Some cross-references in older docs may point to files that
no longer exist in this repo; that is expected and not a bug.

---

## Quick Navigation

**Start here:**
- [WHAT_THIS_REPRODUCES.md](WHAT_THIS_REPRODUCES.md) — **scope clarification**: what the audit does/does not reproduce (read first)
- [52_reusable_assets_harvest.md](52_reusable_assets_harvest.md) — 5 reusable assets extracted from audit

**Current state:**
- [116_claim_status_matrix_v3.md](116_claim_status_matrix_v3.md) — current claim ledger (24 confirmed / 12 open / 16 rejected, as of 2026-06)
- [119_weaknesses_referee_map.md](119_weaknesses_referee_map.md) — 36 weaknesses, referee-style map
- [GITHUB_SHOWCASE_AUDIT.md](GITHUB_SHOWCASE_AUDIT.md) — repo showcase/health audit (most current status)
- [../.claude/memory/facts.json](../.claude/memory/facts.json) — live results/open-questions ledger (most current)

**If resuming work:**
- [.claude/memory/activeContext.md](../.claude/memory/activeContext.md) — current project state
- [54_mcmc_blocker_chain.md](54_mcmc_blocker_chain.md) — why MCMC is blocked

---

## Documents by Lifecycle Stage

### Stage 1: Parameter Extraction (docs 01–18)

**Beta Parameter Provenance:**
- [01_beta_definition_audit.md](01_beta_definition_audit.md) — β_d, β_q definition forensics
- [14_beta_source_trace_audit.md](14_beta_source_trace_audit.md) — Source confirmation: β_d=4.5, β_q=18.0
- [16_beta_provenance_reconciliation_summary.md](16_beta_provenance_reconciliation_summary.md) — Final β provenance status

**Equation Inventory:**
- [02_equation_inventory.md](02_equation_inventory.md) — All equations from manuscript
- [03_derived_fitted_assumed_unknown.md](03_derived_fitted_assumed_unknown.md) — Epistemic status classification
- [04_assumption_dependency_graph.md](04_assumption_dependency_graph.md) — Circular dependency detection

**Data Anchoring:**
- [05_data_anchoring_map.md](05_data_anchoring_map.md) — Where data comes from
- [13_internal_anchor_uniqueness.md](13_internal_anchor_uniqueness.md) — Uniqueness checks

**Rosetta Stone:**
- [06_rosetta_stone.md](06_rosetta_stone.md) — Author terminology → standard physics

**Numerology Audit:**
- [07_numerology_audit_eq15.md](07_numerology_audit_eq15.md) — π/e/golden ratio checks

**Fit Reproduction:**
- [18_fit_reproduction_requirements.md](18_fit_reproduction_requirements.md) — Fitted parameter protocol

---

### Stage 2: Table A1 Forensics (docs 17, 39, 41–42, 65–66, 68)

**Table A1 Extraction:**
- [17_table_A1_manual_verification_protocol.md](17_table_A1_manual_verification_protocol.md) — Verification protocol
- [39_appendix_a1_steps_3_7_forensic_reading.md](39_appendix_a1_steps_3_7_forensic_reading.md) — Steps 3–7 forensics
- [41_table_a1_transcription_notes.md](41_table_a1_transcription_notes.md) — Full transcription
- [42_table_a1_reverse_engineering_results.md](42_table_a1_reverse_engineering_results.md) — Reverse engineering results

**Table A1 Recomputation:**
- [65_private_artifact_plan_table_a1_recomputation.md](65_private_artifact_plan_table_a1_recomputation.md) — Recomputation plan (technical methodology, not correspondence)
- [66_table_a1_recomputation_report.md](66_table_a1_recomputation_report.md) — H_FLRW provenance mismatch finding — **load-bearing: read by `tests/test_hflrw_provenance_safety.py`, do not remove**

**H_FLRW Provenance Recovery:**
- [68_hflrw_provenance_recovery.md](68_hflrw_provenance_recovery.md) — H_FLRW mismatch diagnosis (p≈0.87 best fit) — also read by the same safety test

---

### Stage 3: Bridge Candidate Generation (docs 33, 36–38, 40, 43, 46–48, 50, 53, 73, 92)

**Bridge Strategy:**
- [36_force_to_expansion_bridge_triage.md](36_force_to_expansion_bridge_triage.md) — F_oP → H_MULT bridge triage
- [38_one_page_buckholtz_computational_bridge_summary.md](38_one_page_buckholtz_computational_bridge_summary.md) — One-page summary
- [53_three_path_hmult_roadmap_safe_memo.md](53_three_path_hmult_roadmap_safe_memo.md) — 3-path roadmap (SAFE memo)

**Bridge Candidates:**
- [40_hmult_algorithm_recovery_and_brainstorm.md](40_hmult_algorithm_recovery_and_brainstorm.md) — H_MULT algorithm recovery
- [43_bridge_candidate_math_stress_test.md](43_bridge_candidate_math_stress_test.md) — Mathematical stress test
- [37_discrete_lattice_mvb_hypothesis.md](37_discrete_lattice_mvb_hypothesis.md) — Lattice QFT hypothesis
- [92_bridge_candidate_registry.md](92_bridge_candidate_registry.md) — Catalog of all candidate bridges (F_oP → H_MULT)

**Deep Bridge Research:**
- [46_deep_bridge_research_sprint.md](46_deep_bridge_research_sprint.md) — Research sprint results
- [47_literature_bridge_map.md](47_literature_bridge_map.md) — Literature map
- [48_deep_bridge_independent_verification.md](48_deep_bridge_independent_verification.md) — Independent verification
- [50_deep_bridge_diagnostic_fit_rows_2_12.md](50_deep_bridge_diagnostic_fit_rows_2_12.md) — Diagnostic fit rows 2–12

**AI-Table Methodology:**
- [73_multi_ai_table_comparison_plan.md](73_multi_ai_table_comparison_plan.md) — Plan to compare Table A1 variants across AI services

**Public Formula Stripping:**
- [33_public_formula_stripping_report.md](33_public_formula_stripping_report.md) — What's public vs derived

---

### Stage 4: MCMC Blockers & Diagnostics (docs 30, 54–55)

**MCMC Status:**
- [54_mcmc_blocker_chain.md](54_mcmc_blocker_chain.md) — 5 blockers, 0 resolved, MCMC BLOCKED

**Conceptual Clarity:**
- [55_conceptual_status_of_hz_in_multing.md](55_conceptual_status_of_hz_in_multing.md) — H(z) operational meaning unclear

**Solar System Limit:**
- [30_multing_solar_system_limit_questions.md](30_multing_solar_system_limit_questions.md) — Solar system test questions

---

### Stage 5: Reusable Assets (docs 52)

- [52_reusable_assets_harvest.md](52_reusable_assets_harvest.md) — 5 assets extracted from the audit:
  1. **epi-registry** (score 19/20) — Parameter provenance framework
  2. **table-auditor** (score 18/20) — Table reverse engineering
  3. **bridge-auditor** (score 19/20) — Bridge candidate stress test
  4. Respectful clarification template
  5. Contribution strategy pattern

---

### Stage 6: Safety & Audit (docs 08, CODE_AUDIT, PARANOID, SCI_EVIDENCE)

- [08_supplementary_audit.md](08_supplementary_audit.md) — Supplementary audit
- [CODE_AUDIT_HARDENING.md](CODE_AUDIT_HARDENING.md) — Code audit hardening
- [PARANOID_MODE_FINAL_AUDIT.md](PARANOID_MODE_FINAL_AUDIT.md) — Paranoid mode final audit
- [SCI_EVIDENCE_AUDIT.md](SCI_EVIDENCE_AUDIT.md) — Scientific evidence audit

---

### Stage 7: Repo Status Checklists (docs 51, 58)

- [51_repo_waiting_state_checklist.md](51_repo_waiting_state_checklist.md) — Repo state checklist
- [58_repo_sanity_check.md](58_repo_sanity_check.md) — Repo sanity check

---

### Discovery Logs & Conflict Resolution (docs 27–28, 34)

- [27_source_conflict_log.md](27_source_conflict_log.md) — Source conflicts
- [28_value_reconciliation_protocol.md](28_value_reconciliation_protocol.md) — Value reconciliation
- [34_force_law_manual_verification_checklist.md](34_force_law_manual_verification_checklist.md) — F_oP verification

---

### Gold Candidates & Source Checks (docs 23–25)

- [23_gold_candidate_bbn_neff_source_check.md](23_gold_candidate_bbn_neff_source_check.md) — BBN N_eff candidate
- [24_gold_candidate_sidm_bullet_cluster_source_check.md](24_gold_candidate_sidm_bullet_cluster_source_check.md) — SIDM Bullet Cluster candidate
- [25_gold_candidate_dark_disk_gaia_source_check.md](25_gold_candidate_dark_disk_gaia_source_check.md) — Dark Disk Gaia candidate

---

### Miscellaneous (docs 10, 11, 15, 29, 35)

- [10_time_budget.md](10_time_budget.md) — Time budget
- [11_beta_normalization_math.md](11_beta_normalization_math.md) — Beta normalization math
- [15_notebooklm_beta_candidates.md](15_notebooklm_beta_candidates.md) — NotebookLM beta candidates
- [29_ppn_quick_check_requirements.md](29_ppn_quick_check_requirements.md) — PPN quick check requirements
- [35_ai_transcript_closure_candidate.md](35_ai_transcript_closure_candidate.md) — AI transcript closure

---

### Multi-AI Table Reproducibility (docs 76–83)

Supplementary inventory (76), extraction summary (77), CSV integrity (78–80),
ChatGPT source resolution (79), multi-AI comparison (81), Codex independent audit (82),
revision verification (83).

---

### Verification / Controls / Adversarial (docs 86–96)

Non-obvious physical paths (86), negative-control plan+results (87, 91),
bridge registry + lab plan (92, 94), PEMM adversarial (95), external audit verification (96).

---

### k_A Closure (doc 99)

- [99_k_a_closure_report.md](99_k_a_closure_report.md) — k_A closure report

---

### HD-MAVP & Sync (docs 100–102)

Autopsy (100), error-correction sync (101), vault sync (102).

---

### Evidence Locks & Claim Matrices (docs 107, 109, 111–116)

Technical evidence-lock checkpoints — pending/resolved status of specific verified claims, not correspondence:
- [111_beta_provenance_evidence_lock.md](111_beta_provenance_evidence_lock.md) — β provenance lock (cited elsewhere in this project's memory)
- 107, 107a, 109, 112–114 — further evidence locks
- 115: beta1 hold status
- [108_claim_status_matrix.md](108_claim_status_matrix.md) → superseded by **[116_claim_status_matrix_v3.md](116_claim_status_matrix_v3.md) (current)**

---

### Latest Technical Docs (docs 118–120)

- [118_journal_readiness_section_draft.md](118_journal_readiness_section_draft.md) — journal-readiness section draft
- [119_weaknesses_referee_map.md](119_weaknesses_referee_map.md) — 36 weaknesses (7 categories)
- [120_strong_inference_scout.md](120_strong_inference_scout.md) — strong-inference scan

---

### Bridge Solution Space & Closure (docs 122–128)

- [122_bridge_solution_space.md](122_bridge_solution_space.md) — solution space for a continuous reproducible `H_MULT(z)`
- [122_bottleneck_synthesis_cosmological_branch_verdict.md](122_bottleneck_synthesis_cosmological_branch_verdict.md) — bottleneck synthesis, cosmological-branch verdict ⚠️ *number collision, see note below*
- [123_f_to_hz_bridge_solution_space.md](123_f_to_hz_bridge_solution_space.md) — F→H(z) bridge solution space (deep mode)
- [124_shtanov_bridge_applied_to_F_oP.md](124_shtanov_bridge_applied_to_F_oP.md) — Shtanov & Sahni (2010) bridge applied to `F_oP` — **FALSIFIED** (naive mapping; `null_results` NR-016)
- [125_factorization_gate_result.md](125_factorization_gate_result.md) — P1 universality/factorization gate result *(still load-bearing; referenced through P158)*
- [126_nonuniqueness_of_closure_lemma.md](126_nonuniqueness_of_closure_lemma.md) — non-uniqueness of cosmological closure for `F_oP` (scoped lemma)
- [127_p2_deltaH_result.md](127_p2_deltaH_result.md) — P2 constructive test, `ΔH(a)` result *(read `FINDING_P157` first — it superseded this framing)*
- [128_p3_fsigma8_result.md](128_p3_fsigma8_result.md) — P3 `fσ8` test: broad claim **FALSIFIED**, narrow claim survives

### Lagrangian & CANDIDATE-L1 (docs 129–131)

- [129_q006_multing_lagrangian.md](129_q006_multing_lagrangian.md) — Q006: constructing the MULTING Lagrangian *(addressed 2026-09-07: `/hypothesis-arbiter` → unresolvable on current information)*
- [130_candidate_L1_evaluation.md](130_candidate_L1_evaluation.md) — CANDIDATE-L1 covariant reconstruction: evaluation + step-1 kill-test *(answered by `FINDING_P204`)*
- [131_L1_weakfield_matching_result.md](131_L1_weakfield_matching_result.md) — CANDIDATE-L1 weak-field matching *(⚠️ `FINDING_P204`: this doc is internally inconsistent about what its own `ξ_A` is)*

### kSZ Empirical Test (docs 132–134)

- [132_ksz_force_law_constraint.md](132_ksz_force_law_constraint.md) — first direct empirical test of the MULTING force layer (kSZ)
- [132_open_bottlenecks_task_backlog.md](132_open_bottlenecks_task_backlog.md) — open bottlenecks task backlog ⚠️ *number collision*
- [133_c1_source_to_prediction_closure.md](133_c1_source_to_prediction_closure.md) — C1 source-to-prediction closure trace
- [133_statistical_decision_record.md](133_statistical_decision_record.md) — statistical decision record, kSZ dipole limit ⚠️ *number collision*
- [134_claim_registry_ksz.md](134_claim_registry_ksz.md) — claim registry, kSZ dipole constraint

### Audit Trilogy (docs 134–136)

- [134_definitions_units_provenance_audit.md](134_definitions_units_provenance_audit.md) — Audit 2: definitions, units, source-of-truth provenance ⚠️ *number collision*
- [135_audit3_fair_model_comparison.md](135_audit3_fair_model_comparison.md) — Audit 3: independent end-to-end reproduction + fair model comparison
- [136_trilogy_verdict_and_decisions.md](136_trilogy_verdict_and_decisions.md) — trilogy verdict & decision log (Audits 1+2+3)

### TJB-Facing Tiers (docs 137–139)

- [137_tjb_immediate_help_brief.md](137_tjb_immediate_help_brief.md) — immediate help brief (GREEN tier)
- [138_tjb_optional_technical_modules.md](138_tjb_optional_technical_modules.md) — optional technical modules (AMBER tier)
- [139_internal_null_and_hypothesis_registry.md](139_internal_null_and_hypothesis_registry.md) — internal null/hypothesis registry (RED tier — **not author-facing**)

### Clean-Room & External Verification (docs 140–144)

- [140_v25_atomizer_source_map_and_clean_room_attempt.md](140_v25_atomizer_source_map_and_clean_room_attempt.md) — v25 source map, status mapping, clean-room reimplementation attempt
- [141_external_verification_desi_planck_moresco.md](141_external_verification_desi_planck_moresco.md) — external verification: DESI/Planck/Moresco
- [142_low_z_uptick_robustness_and_anchoring_reconfirmation.md](142_low_z_uptick_robustness_and_anchoring_reconfirmation.md) — low-z "uptick" robustness + anchoring-parity reconfirmation
- [143_reply_draft_reddit_headline.md](143_reply_draft_reddit_headline.md) — reply to TJB re: Reddit headline (2026-08-12)
- [144_new_multing_preprint_sh0es_fit_provenance.md](144_new_multing_preprint_sh0es_fit_provenance.md) — new preprint (202608.0943): SH0ES is a **fitted point**, not a held-out one

### Meta-Audit, Taxonomy, Stop-Rule (docs 145–148)

- [145_research_audit_and_harvest_report_20260817.md](145_research_audit_and_harvest_report_20260817.md) — project meta-audit: harvest scan + research audit *(source of truth for "what has this project established")*
- [146_failure_mode_taxonomy.md](146_failure_mode_taxonomy.md) — failure-mode taxonomy, 11 categories with real historical examples
- [147_campaign_stop_rule.md](147_campaign_stop_rule.md) — explicit stop-rule for the bridge campaign, the 4 named bottlenecks + reopen conditions
- [148_ic_sensitivity_inverse_problem.md](148_ic_sensitivity_inverse_problem.md) — IC-sensitivity inverse problem

### v82 Study Line (docs 149–154)

- [149_v82_preprint_study.md](149_v82_preprint_study.md) — v82 preprint study *(TJB's current work; cite v82 for anything new, v6 for anything already built)*
- [150_v82_vs_our_reconstruction_comparison.md](150_v82_vs_our_reconstruction_comparison.md) — systematic v82 vs. this project's reconstruction
- [151_status_separation_rule.md](151_status_separation_rule.md) — **status separation rule**: empirical ⊥ interpretation ⊥ causal, never collapsed
- [152_evidence_authority_deconflation_mapping.md](152_evidence_authority_deconflation_mapping.md) — "de-conflating evidence and authority" mapping
- [153_bottleneck1_reopen_gate_decision.md](153_bottleneck1_reopen_gate_decision.md) — bottleneck 1 (F→H_MULT(z)) reopen gate decision
- [154_eq32_numerology_literature_bibliography.md](154_eq32_numerology_literature_bibliography.md) — bibliography of historical "numerical coincidence" physics

### Most Recent (docs 155–158)

- [155_engineering_debt_cleanup_20260905.md](155_engineering_debt_cleanup_20260905.md) — engineering debt cleanup (mypy 24→0, CI-enforced)
- [156_bottleneck1_precondition_check_20260905.md](156_bottleneck1_precondition_check_20260905.md) — bottleneck 1 precondition check (`docs/153` §3a)
- [157_next_steps_plan_20260906.md](157_next_steps_plan_20260906.md) — next-steps plan; items 1-2 CLOSED per stop-rule, 3-5 DONE
- [158_provenance_modules_park_decision_20260907.md](158_provenance_modules_park_decision_20260907.md) — `source_provenance`/`conflict_resolver` **PARKED**; `docs/157`'s proposed wiring was a category error (value level vs chain level)

> **⚠️ Number collisions in this range.** Four numbers are used twice:
> **122**, **132**, **133**, **134**. The docs are distinct and all are
> listed above, but the sequence is not a unique key past 121 — cite by
> full filename, never by number alone, for anything in 122–134.
> Doc **121 does not exist**.


### Meta / Audit (named docs)

- [GITHUB_SHOWCASE_AUDIT.md](GITHUB_SHOWCASE_AUDIT.md)
- [PROJECT_AUDIT_2026_05_31.md](PROJECT_AUDIT_2026_05_31.md)
- [AUTHOR_VALUE_AUDIT_2026_05_31.md](AUTHOR_VALUE_AUDIT_2026_05_31.md)
- [HARVEST_SCAN_2026_05_31.md](HARVEST_SCAN_2026_05_31.md)
- [ERROR_CORRECTION_LOG.md](ERROR_CORRECTION_LOG.md)
- [DOUBLE_INVERSION_DIAGNOSTIC.md](DOUBLE_INVERSION_DIAGNOSTIC.md)
- [mechanism_insights.md](mechanism_insights.md)
- [meta/60_hypothesis_revival_engine_relevance.md](meta/60_hypothesis_revival_engine_relevance.md)
- [meta/63_chamberlin_platt_multi_hypothesis_protocol.md](meta/63_chamberlin_platt_multi_hypothesis_protocol.md)

---

## Documents NOT in Sequence

Some doc numbers are missing (e.g., 09, 12, 19–22, 26, 31, 44–45, 49, 56–57, 59–64, 69–72, 74–75, 84–85, 93, 97–98, 103–106, 117, 121). These were either:
- Author-facing correspondence / meeting notes / communication-strategy documents, removed from this public repo 2026-07-12 (kept locally)
- Never created (planning gaps)
- Merged into other docs

---

## File Naming Convention

```
<number>_<descriptive_slug>.md
```

**Special files (no number):**
- `CODE_AUDIT_HARDENING.md` — Code audit hardening
- `PARANOID_MODE_FINAL_AUDIT.md` — Paranoid audit
- `SCI_EVIDENCE_AUDIT.md` — Evidence audit
- `INDEX.md` — This file

---

## How to Navigate

**If you're new to this project:**
1. Read [WHAT_THIS_REPRODUCES.md](WHAT_THIS_REPRODUCES.md)
2. Read [52_reusable_assets_harvest.md](52_reusable_assets_harvest.md)
3. Read [.claude/memory/activeContext.md](../.claude/memory/activeContext.md)

**If resuming physics work:**
1. Read [54_mcmc_blocker_chain.md](54_mcmc_blocker_chain.md) — check which blockers resolved
2. Read [66_table_a1_recomputation_report.md](66_table_a1_recomputation_report.md) — H_FLRW provenance finding

**If extracting remaining assets:**
1. Read [52_reusable_assets_harvest.md](52_reusable_assets_harvest.md) — Asset 2 (table-auditor), Asset 3 (bridge-auditor)

---

## Safety Boundaries

**These docs contain NO:**
- Claims of author error (`NOT_AUTHOR_ERROR`)
- Claims of model validation (`NOT_VALIDATION`)
- Claims of model refutation (`NOT_REFUTATION`)
- Public claims about physics (`NO_PUBLIC_CLAIMS`)

**All artifacts labeled:**
- `OUR_RECONSTRUCTION` — our interpretations, not author's
- `SOURCE_CONFIRMED` — explicitly stated in manuscript
- `AUDIT_RECONSTRUCTION` — derived by us during audit

---

**Last updated:** 2026-09-07 (docs 122-157 indexed; previously stale since 2026-07-12)
