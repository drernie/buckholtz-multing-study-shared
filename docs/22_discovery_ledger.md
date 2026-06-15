# Discovery Ledger — Buckholtz IDM/MULTING Audit

**Purpose:** Track all findings from the IDM/MULTING reproducibility audit, classified by type, verification status, and value.

**Status:** Active tracking (updated 2026-05-27)

**Audit context:** This ledger tracks findings from epistemic audit of Buckholtz IDM/MULTING framework, NOT validation or refutation.

---

## Classification Legend

| Type | Definition | Example | Action |
|------|------------|---------|--------|
| **gold_candidate** | Potentially valuable finding requiring verification | External constraint testable against new dataset | Source + test |
| **copper_result** | Useful confirmed result, not breakthrough | Arithmetic reproduction of Eq.15 | Document + cite |
| **diamond_method** | Methodological/process innovation (reusable) | Provenance audit framework | Generalize + publish |
| **fool_gold** | Looks valuable but isn't (numerology, circular) | 20 alternative formulas for beta_d_2 | Flag + warn |
| **dead_end** | Investigated, does not work or blocked | Missing H-MULT formula (blocker) | Document + wait |
| **source_missing_constraint** | Constraint exists but applicability unknown (no discussion in materials) | BBN/N_eff (isomer thermal history not discussed) | Ask author |
| **unknown** | Not yet classified | Newly discovered claim | Investigate |

---

## Discovery Table

### Finding 1: Beta Values Fitted to H(z)

| Field | Value |
|-------|-------|
| **Finding** | Beta_d=4.5 and beta_q=18.0 are fitted phenomenological parameters (AI-assisted thought experiment), NOT theoretically derived constants |
| **Type** | `copper_result` |
| **Evidence** | ✅ Manually verified from preprints202511.0598.v6.pdf, Appendix A.3, Table A1. Exact quote: "Regarding H-MULT, the online service reported choosing beta_d = 4.5 and beta_q = 18.0." Context: AI-assisted fit to minimize H(z) deviations. |
| **Source status** | `manuscript_reported_fitted` (manually verified 2026-05-27) |
| **Verification status** | ✅ VERIFIED — manual verification complete, provenance documented in beta_provenance.py |
| **Next test** | (1) Reproduce Table A1 fit after H-MULT formula received. (2) Compare fit quality with ΛCDM on same dataset (χ²/dof, AIC, BIC). (3) DO NOT use for predictions (circular reasoning). |
| **Value for project** | HIGH — establishes use permission boundary (fit reproduction ALLOWED, predictions FORBIDDEN). Prevents circular reasoning validation claims. |
| **Safe wording** | "Beta values were fitted to H(z) observations and can be used to reproduce the manuscript fit, but cannot be used to predict H(z) on new data (circular reasoning)." |
| **Unsafe wording** | ❌ "Beta values validate MULTING against H(z) observations" (circular: fitted to H(z)). ❌ "Beta values predict H(z)" (already fitted to it). ❌ "Zero-parameter predictions" (2 parameters fitted). |

---

### Finding 2: Eq.15 Arithmetic Reproduction

| Field | Value |
|-------|-------|
| **Finding** | Eq.15 numerical relation `(4/3) * (m_tau² / m_e²)⁶ ≈ k_e * e² / (G * m_e²)` reproduces to ~1% relative error using PDG 2022 + CODATA 2018 constants |
| **Type** | `copper_result` |
| **Evidence** | ✅ 99/99 tests pass, including test_eq15_constants.py::test_eq15_numerical_reproduction. LHS ≈ 2.43×10⁴¹, RHS ≈ 2.40×10⁴¹, relative error 1.2%. |
| **Source status** | `arithmetic_confirmed` (physical mechanism UNKNOWN) |
| **Verification status** | ✅ ARITHMETIC VERIFIED — numbers match. ❌ PHYSICS UNEXPLAINED — exponent 6 and prefactor 4/3 not derived from first principles. |
| **Next test** | (1) Attempt derivation of exponent 6 from symmetry/RG flow. (2) Test alternative exponents (5, 7) — if multiple work within 10%, classify as numerology (Sabine Kill Criterion C). (3) Search literature for similar relations. |
| **Value for project** | MEDIUM — confirms Buckholtz's arithmetic is correct, but does NOT confirm physical interpretation. Useful as existence proof: "numerical coincidence exists, origin unclear." |
| **Safe wording** | "Eq.15 arithmetic relation reproduces to ~1% error with standard physics constants. Physical mechanism for exponent 6 and prefactor 4/3 is unknown and requires derivation from first principles." |
| **Unsafe wording** | ❌ "Eq.15 proves connection between particle physics and cosmology" (mechanism unknown). ❌ "AI discovered fundamental relation" (arithmetic only, not derivation). ❌ "Exponent 6 is unique" (not tested alternatives). |

---

### Finding 3: Beta Numerology Risk (Internal Anchors)

| Field | Value |
|-------|-------|
| **Finding** | Beta_d_2=0.78 has 20 alternative formulas within 5% error (uniqueness score 0.10). Beta_d_1=4.25 has 7 alternatives within 1.2% error. No beta value achieves uniqueness score >0.7. |
| **Type** | `fool_gold` |
| **Evidence** | ✅ Documented in docs/13_internal_anchor_uniqueness.md. Audit reconstruction betas (beta_d_1, beta_d_2, beta_q_2) derived from internal anchors (1,2,3,4,7,9,17) but multiple formulas match. Sabine audit: Numerology Score 4/5. |
| **Source status** | `audit_reconstruction` (NOT Buckholtz stated, OUR inference) |
| **Verification status** | ✅ NUMEROLOGY CONFIRMED — multiple exact rational matches without uniqueness. ⚠️ HIGH structured numerology risk for beta_d_2 (20 alternatives). |
| **Next test** | (1) Request explicit beta derivation formula from Buckholtz. (2) If no derivation exists, classify as fitted (not derived). (3) Do NOT use audit-reconstructed values for modeling (circular reasoning: testing OUR inference, not Buckholtz's model). |
| **Value for project** | CRITICAL — prevents false uniqueness claims. Documents that audit-reconstructed beta values (17/4, 7/9) are NOT source-confirmed and have low uniqueness. |
| **Safe wording** | "Multiple formulas (7-20 alternatives) from internal anchors match beta candidate values within small error margins, indicating structured numerology risk. Explicit derivation formula from author required to resolve ambiguity." |
| **Unsafe wording** | ❌ "Beta values uniquely determined by internal anchors" (20 alternatives exist). ❌ "17/4 is the only formula that works" (7 alternatives within 1.2%). ❌ "Buckholtz derived beta_d=4.25 from Eq.20" (WE inferred this, not confirmed by author). |

---

### Finding 4: Missing H-MULT Functional Form (UPDATED 2026-05-29)

| Field | Value |
|-------|-------|
| **Finding** | Appendix A1 Step 5 does NOT provide explicit computational formula H_MULT(z; beta_d, beta_q, m_A, r_A, k_A, ...). Force formulas (F_m, F_d, F_q) and scaling relations (r_dA = β_d × r_A) are provided, but bridge F_oP → H_MULT(z) is UNDER_SPECIFIED — only procedural instruction exists: *"How well can you fit (by using my monopole, dipole, and quadrupole components of gravity) the data..."* |
| **Type** | `dead_end` (until resolved) |
| **Evidence** | ✅ Forensic extraction complete: docs/39_appendix_a1_steps_3_7_forensic_reading.md. Step 5 provides: (1) scaling relations r_dA/r_dP/r_qAB ✅, (2) constraint "minimize σ from H-data" ✅, (3) AI discretion "Feel free to use any or all the information" ✅. Step 5 does NOT provide: (1) functional form H_MULT(z, ...) ❌, (2) objective function beyond "minimize σ" ❌, (3) computational procedure ❌. |
| **Source status** | `formula_missing` + `procedural_only` (Priority 1 question for Buckholtz) |
| **Verification status** | ❌ BLOCKED — Appendix A1 forensic extraction confirms: bridge formula missing. Table A1 H_MULT values are AI service output (not author calculation). Cannot reproduce Table A1 computation without explicit formula. |
| **Next test** | (1) Update clarification brief (docs/26) with Step 5 finding. (2) Send updated question: "Step 5 instructs AI to fit monopole/dipole/quadrupole to H-data but does not provide computational formula H_MULT(z, β_d, β_q, ...). Could you provide explicit formula or confirm if AI interpretation is intended?" (3) After formula received: implement, reproduce Table A1, verify. |
| **Value for project** | CRITICAL BLOCKING — Appendix A1 analysis upgraded this from "formula unclear" to "formula UNDER_SPECIFIED with forensic evidence". #1 blocker for ANY H(z) computation (table reproduction OR prediction). |
| **Safe wording** | "Appendix A1 Step 5 provides force formulas and scaling relations but does NOT provide explicit computational formula H_MULT(z; β_d, β_q, ...). Bridge from pairwise forces to cosmological expansion remains under-specified. Table A1 H_MULT values are AI service output following procedural instruction, not author calculation." |
| **Unsafe wording** | ❌ "Formula is in Appendix A1" (only scaling relations, NOT full formula). ❌ "We can compute H_MULT from Step 5" (procedural only, NOT computational). ❌ "Table A1 proves formula works" (AI output, not verified computation). |

---

### Finding 5: Table A1 Extraction Framework

| Field | Value |
|-------|-------|
| **Finding** | Created complete Table A1 extraction framework: CSV template, extraction log (320+ lines), 14 validation tests (structural, numeric, cosmological ranges). |
| **Type** | `diamond_method` |
| **Evidence** | ✅ Files created: data/table_a1_raw.csv (template), data/table_a1_extraction_log.md (protocol), tests/test_table_a1_extraction.py (14 tests). 101/113 tests passing (12 skipped awaiting data). Framework includes: column validation, z monotonicity, H>0 checks, time range (0-13.8 Gyr), OCR error detection. |
| **Source status** | `methodological_innovation` (reusable protocol) |
| **Verification status** | ✅ FRAMEWORK COMPLETE — template + protocol + tests ready. ⏸️ DATA PENDING — awaits manual transcription by user (PDF not available to Claude Code). |
| **Next test** | (1) User transcribes Table A1 from manuscript PDF. (2) Run: pytest tests/test_table_a1_extraction.py -v (expect 14/14 pass). (3) Apply framework to other tables (Table A2, supplementary tables). |
| **Value for project** | HIGH (methodological) — reusable for ANY tabular data extraction from papers. Validation-first approach catches transcription errors automatically. Template can be generalized to other cosmology H(z) datasets. |
| **Safe wording** | "Created validation-first table extraction framework with 14 automated quality checks (structure, numerics, cosmological ranges). Framework is reusable for extracting tabular data from scientific manuscripts with instant error feedback." |
| **Unsafe wording** | N/A (pure methodology, no physics claims) |

---

### Finding 6: Provenance Audit Framework

| Field | Value |
|-------|-------|
| **Finding** | Developed beta provenance registry with 6 statuses (source_confirmed, manuscript_reported_fitted, audit_reconstruction, source_missing, etc.) + use permission hierarchy (source_confirmed / fit_reproduction_only / do_not_use). Prevents circular reasoning by tracking fitted vs derived. |
| **Type** | `diamond_method` |
| **Evidence** | ✅ Implemented in src/beta_provenance.py (BetaProvenance dataclass with 9 fields). 25 provenance tests enforce constraints. Circular reasoning guards: beta fitted to H(z) → cannot "predict" H(z). Manual verification protocol (docs/17). Sabine audit integration (docs/19). |
| **Source status** | `methodological_innovation` (audit framework) |
| **Verification status** | ✅ FRAMEWORK COMPLETE — 6 beta candidates tracked, 0/6 source-confirmed (H(z) modeling blocked), 2/6 manuscript-reported-fitted (fit reproduction allowed). |
| **Next test** | (1) Apply framework to other marginalized theories (track fitted vs derived claims). (2) Generalize to other parameter types (not just betas). (3) Publish as standalone audit methodology. |
| **Value for project** | VERY HIGH (methodological) — solves "fitted → validation" circular reasoning problem that appears in MANY alternative physics papers. Reusable for auditing ANY theory with phenomenological parameters. Framework enforces: "fitted to X → cannot validate with X." |
| **Safe wording** | "Provenance audit framework tracks source verification (confirmed/fitted/reconstructed/missing) and use permission (predictions/fit-reproduction/blocked). Prevents circular reasoning by explicitly marking fitted parameters and forbidding their use for validation claims." |
| **Unsafe wording** | N/A (pure methodology) |

---

### Finding 7: BBN / N_eff as Candidate External Constraint

| Field | Value |
|-------|-------|
| **Finding** | BBN/N_eff constraint CANNOT be assessed for relevance to IDM because Buckholtz does NOT discuss thermal history, particle content of isomers, dark-sector temperature ratios, or reheating mechanisms in available materials. |
| **Type** | `source_missing_constraint` (downgraded from gold_candidate) |
| **Evidence** | ✅ SOURCE CHECK COMPLETE (2026-05-28, docs/23_gold_candidate_bbn_neff_source_check.md). Searched local docs for: N_eff, BBN, nucleosynthesis, thermal history, reheating, temperature ratio, mirror sector. Result: NO mentions (except in rosetta: "mirror-matter-like" Medium match 5/10, but NOT confirmed as thermally populated). "6 isomers" mentioned but NO discussion of particle content (dark photons? dark neutrinos?) or thermal population. |
| **Source status** | `source_missing` (cannot assess applicability without thermal history) |
| **Verification status** | ⏸️ BLOCKED — Relevance unknown. BBN/N_eff applies to thermally populated relativistic dark sectors. Buckholtz does NOT state whether isomers are: (1) full mirror sectors with dark photons/neutrinos, (2) cold/non-relativistic sectors, (3) asymmetrically reheated (T_dark << T_visible). Cannot determine if constraint applies. |
| **Next test** | ✅ IMMEDIATE: Ask Buckholtz: "Do the five dark isomers contain thermally populated relativistic particles (dark photons, dark neutrinos) at early times (T ~ MeV)? If yes: (a) What is T_dark/T_visible? (b) Does model predict ΔN_eff? If no (dark sectors are cold): BBN/N_eff does not apply." See docs/23 section "Next Steps" for full question template. |
| **Value for project** | UNKNOWN (depends on answer) — IF isomers are thermally populated mirror sectors → VERY HIGH (independent constraint, BBN gold standard). IF isomers are cold/non-relativistic → NOT APPLICABLE (constraint irrelevant). Cannot proceed without clarification. |
| **Safe wording** | "BBN/N_eff constraints may be relevant if IDM's dark isomers are thermally populated mirror sectors. Buckholtz does not discuss thermal history, particle content, or temperature ratios in available materials. Applicability cannot be determined without explicit clarification from author. Question sent: 'Are dark isomers thermally populated at BBN epoch?'" (see docs/23_gold_candidate_bbn_neff_source_check.md for full safe question template) |
| **Unsafe wording** | ❌ "BBN validates/falsifies MULTING" (applicability unknown). ❌ "MULTING predicts N_eff" (not discussed). ❌ "6 isomers ruled out by BBN" (unknown if thermally populated). ❌ "Buckholtz ignores BBN" (may not apply to his model). ❌ "IDM predicts ΔN_eff = X" (no calculation possible without T_dark/T_visible). |

---

### Finding 8: SIDM / Bullet Cluster as Candidate External Constraint

| Field | Value |
|-------|-------|
| **Finding** | SIDM/Bullet Cluster constraint CANNOT be assessed for relevance to IDM because Buckholtz does NOT specify whether 6 isomers are collisionless or self-interacting, does NOT provide σ/m, and does NOT clarify whether dipole/quadrupole are DM-DM scattering (SIDM) or modified gravity contributions. |
| **Type** | `source_missing_constraint` (downgraded from gold_candidate) |
| **Evidence** | ✅ SOURCE CHECK COMPLETE (2026-05-28, docs/24_gold_candidate_sidm_bullet_cluster_source_check.md). Searched local docs for: SIDM, self-interacting, Bullet Cluster, cross-section, dark atom, dark photon, SEA-DM, MEA-DM, collisional, dissipative. Result: Bullet Cluster acknowledged in data anchoring map ("tests collisionless nature") but NO analysis of IDM consistency. NO discussion of σ/m, self-interactions, or whether isomers are collisionless. Critical ambiguity: dipole/quadrupole mentioned but NOT clarified whether these are DM-DM scattering or modified gravity. |
| **Source status** | `source_missing` (cannot assess applicability without interaction definition) |
| **Verification status** | ⏸️ BLOCKED — Relevance unknown. Bullet Cluster constrains self-interacting dark matter (σ/m < 1–2 cm²/g at cluster velocities ~3500 km/s). Buckholtz does NOT state whether isomers are: (1) collisionless (like ΛCDM, σ/m ~ 0), (2) self-interacting (like SIDM, σ/m > 0), (3) mixed (collisionless majority + self-interacting minority). Dipole/quadrupole interpretation unknown: are these DM-DM scattering forces (→ Bullet applies) or modified gravity contributions (→ Bullet does NOT directly constrain)? Cannot determine if constraint applies. |
| **Next test** | ✅ IMMEDIATE: Ask Buckholtz: "Are the 6 isomers collisionless or self-interacting? If self-interacting: what is predicted σ/m? Are MULTING dipole/quadrupole interactions BETWEEN dark matter particles (DM-DM scattering) or contributions to gravitational potential (modified gravity)?" See docs/24 section "Next Steps" for full question template with three upgrade paths (collisionless → not_applicable, self-interacting → gold_candidate, mixed → partially_applicable). |
| **Value for project** | UNKNOWN (depends on answer) — IF isomers are self-interacting with σ/m ~ 0.1–1 cm²/g → VERY HIGH (independent constraint, Bullet Cluster gold standard, testable on multiple scales). IF isomers are collisionless (σ/m ~ 0) → NOT APPLICABLE (Bullet Cluster automatically satisfied, constraint irrelevant). IF dipole is modified gravity (not DM-DM scattering) → MEDIUM (affects cluster dynamics differently, requires separate analysis). Cannot proceed without clarification. |
| **Safe wording** | "SIDM/Bullet Cluster constraints may be relevant if IDM's 6 isomers have self-interactions (σ/m > 0). Buckholtz does not specify whether isomers are collisionless or self-interacting in available materials. Dipole/quadrupole terms mentioned in MULTING but NOT clarified whether these represent DM-DM scattering (SIDM) or modified gravity contributions. Bullet Cluster acknowledged in data anchoring map but NOT analyzed for IDM consistency. Applicability cannot be determined without interaction definition from author. Question sent: 'Are isomers collisionless or self-interacting? What is σ/m?'" (see docs/24_gold_candidate_sidm_bullet_cluster_source_check.md for full safe question template) |
| **Unsafe wording** | ❌ "Bullet Cluster validates/falsifies MULTING" (applicability unknown). ❌ "MULTING predicts σ/m" (not discussed). ❌ "6 isomers ruled out by Bullet Cluster" (unknown if self-interacting). ❌ "Dipole repulsion = self-interaction" (may be modified gravity, not DM-DM scattering). ❌ "IDM predicts σ/m = X" (no calculation possible without interaction type, dark force strength, particle masses). ❌ "Most dark matter is collisionless in IDM" (not stated — may be 100% collisionless, 100% SIDM, or mixed). |

---

### Finding 9: Dark Disk / Gaia as Candidate External Constraint

| Field | Value |
|-------|-------|
| **Finding** | Gaia/dark-disk constraint CANNOT be assessed for relevance to IDM because Buckholtz does NOT specify: (1) at what scales dipole operates (cosmological Mpc vs galactic kpc), (2) whether isomers are dissipative (dark photons, radiative cooling, dark atoms), (3) whether dark disk formation is predicted. Beta_d ~ 4.25 → inferred scale ~2.4 Mpc (OUR analysis, group/cluster scale, 240× larger than galactic 10 kpc) suggests dipole may NOT operate locally, but NOT explicitly stated. |
| **Type** | `source_missing_constraint` (downgraded from gold_candidate) |
| **Evidence** | ✅ SOURCE CHECK COMPLETE (2026-05-28, docs/25_gold_candidate_dark_disk_gaia_source_check.md). Searched local docs for: Gaia, DR2/DR3, dark disk, Milky Way, dissipative, cooling, dark atom, dark photon, stellar streams, substructure, vertical profile, scale height. Result: NO mentions of Gaia, dark disk, Milky Way, dissipative cooling, or galactic-scale predictions. NO discussion of whether isomers are dissipative or remain halo-like. Scale range NOT specified (cosmological vs galactic). Dimensional inference from beta_d (docs/12): L ~ 2.4 Mpc (group/cluster), NOT galactic kpc — but this is OUR analysis, NOT author statement. |
| **Source status** | `source_missing` (cannot assess applicability without scale range + dissipative specification) |
| **Verification status** | ⏸️ BLOCKED — Relevance unknown. Gaia constrains local dark matter (r ~ 8 kpc, z ~ 0–1 kpc): ρ_DM(z=0) ~ 0.3–0.6 GeV/cm³, dark disk mass M_disk/M_halo < 0.3–0.5. Constraint applies IF: (1) dipole operates at galactic scales kpc (modifies ρ_DM(z) locally) OR (2) isomers are dissipative (dark atoms, dark EM → cool and form dark disk). Buckholtz does NOT state: scale range of dipole (Mpc only? kpc also?), whether isomers dissipative (dark photons? radiative cooling?), whether dark disk formation predicted. Inferred scale L ~ 2.4 Mpc from beta_d suggests dipole may NOT reach kpc scales (only group/cluster Mpc), but NOT confirmed. Cannot determine if constraint applies. |
| **Next test** | ✅ IMMEDIATE: Ask Buckholtz: "At what scales does MULTING dipole operate? (A) Cosmological only (Mpc–Gpc, affects H(z)) → Gaia not applicable. (B) All scales including galactic (kpc) → Gaia applies, need ρ_DM(z) prediction. (C) Scale-dependent with cutoff → specify cutoff. Additionally: Are 6 isomers dissipative (dark photons, radiative cooling, dark atoms)? If dissipative: do they form dark disk or remain halo-like?" See docs/25 section "Next Steps" for full question template combining all three gold candidates (BBN, SIDM, Gaia). |
| **Value for project** | UNKNOWN (depends on answer) — IF dipole operates at kpc AND isomers dissipative → MEDIUM-HIGH (dark disk constraint testable with Gaia vertical kinematics). IF dipole only Mpc OR isomers non-dissipative → NOT APPLICABLE (Gaia irrelevant, local kinematics unaffected). Inferred scale L ~ 2.4 Mpc (group/cluster, OUR analysis) suggests likely NOT APPLICABLE, but confirmation needed. Cannot proceed without scale range clarification. |
| **Safe wording** | "Gaia/dark-disk constraints may be relevant if IDM predicts dissipative dark matter forming disk-like structures at galactic scales (kpc). Buckholtz does not specify: (1) scale range of dipole (cosmological Mpc vs galactic kpc), (2) whether isomers are dissipative (dark photons, radiative cooling, dark atoms), (3) whether dark disk formation predicted. Dimensional analysis from beta_d ~ 4.25 suggests L ~ 2.4 Mpc (group/cluster scale, 240× larger than galactic), implying dipole may not operate locally — but this is OUR inference, NOT author statement. Gaia not cited in materials. Applicability cannot be determined without scale specification. Question sent: 'At what scales does dipole operate? Are isomers dissipative?'" (see docs/25_gold_candidate_dark_disk_gaia_source_check.md for full safe question template) |
| **Unsafe wording** | ❌ "Gaia validates/falsifies MULTING" (applicability unknown). ❌ "MULTING predicts dark disk" (disk formation not discussed). ❌ "6 isomers ruled out by Gaia" (scale range unknown, may not reach kpc). ❌ "Dipole operates at all scales" (scale range NOT specified — may be cosmological only). ❌ "IDM predicts ρ_DM(z) = X" (no calculation possible without: dipole functional form at kpc, dissipative cooling rate, dark disk scale height). ❌ "Dark isomers form dark atoms" (not discussed — atomic structure requires dark photons + dark electrons, not confirmed). |

---

### Finding 10: Fit-vs-Prediction Protocol (Circular Reasoning Prevention)

| Field | Value |
|-------|-------|
| **Finding** | Developed explicit protocol distinguishing fit reproduction (retrodiction) from prediction (falsification). Fitted parameters CANNOT validate against the dataset they were fitted to. Use permission hierarchy enforces: `source_confirmed` (predict OK) / `fit_reproduction_only` (retrodiction OK, prediction FORBIDDEN) / `do_not_use` (blocked). |
| **Type** | `diamond_method` |
| **Evidence** | ✅ Implemented in beta_provenance.py (use_permission_status field). Documented in docs/18_fit_reproduction_requirements.md (section 2: "What is allowed" vs "What is not allowed"). Circular reasoning guard: beta fitted to H(z) → marked `allowed_for_fit_reproduction_only` → tests enforce: cannot claim "predictions". 25 provenance tests verify enforcement. |
| **Source status** | `methodological_innovation` (anti-circular-reasoning protocol) |
| **Verification status** | ✅ PROTOCOL COMPLETE — enforced by tests, documented in beta provenance. Prevents: "fitted to X → validates with X" fallacy. |
| **Next test** | (1) Apply protocol to other marginalized theories with fitted parameters. (2) Generalize to non-cosmology domains (particle physics fits, astrophysics models). (3) Publish as standalone methodology: "Preventing Validation Theater in Phenomenological Models." |
| **Value for project** | VERY HIGH (methodological) — solves a COMMON problem in alternative physics papers: fitted parameters presented as "predictions" or "validations". Protocol is reusable across domains. Explicit enforcement via code + tests makes it auditable. |
| **Safe wording** | "Fit-vs-prediction protocol distinguishes retrodiction (reproducing a fit on the same dataset) from prediction (testing on new data). Fitted parameters are marked `allowed_for_fit_reproduction_only` and CANNOT be used for validation claims against the fit dataset (circular reasoning). Protocol enforced by automated tests." |
| **Unsafe wording** | N/A (pure methodology) |

---

## Summary Statistics

| Type | Count | Verified | Pending | Blocked |
|------|-------|----------|---------|---------|
| **gold_candidate** | 0 | 0 | 0 | 0 |
| **copper_result** | 2 | 2 | 0 | 0 |
| **diamond_method** | 4 | 4 | 0 | 0 |
| **fool_gold** | 1 | 1 | 0 | 0 |
| **dead_end** | 1 | 0 | 0 | 1 |
| **source_missing_constraint** | 3 | 3 | 0 | 0 |
| **unknown** | 0 | — | — | — |
| **TOTAL** | **11** | **10** | **0** | **1** |

**Key:**
- **Verified:** Evidence confirmed, status documented
- **Pending:** Requires primary source verification (Buckholtz manuscripts)
- **source_missing_constraint:** Cannot assess constraint applicability without source discussion (downgraded from gold_candidate)
  - Finding 7 (BBN/N_eff): thermal history not discussed, particle content unknown
  - Finding 8 (SIDM/Bullet Cluster): interaction type not specified (collisionless vs SIDM?), dipole interpretation ambiguous (DM-DM scattering vs modified gravity?)
  - Finding 9 (Gaia/dark disk): scale range not specified (cosmological Mpc vs galactic kpc?), dissipative processes not discussed (dark atoms? radiative cooling?)
- **Blocked:** Cannot proceed (missing formula/data)

---

## Priority Actions

### Immediate (no blockers):

1. ✅ **Document verified findings** (copper + diamond) — DONE (this ledger)
2. ⏸️ **Extract Table A1** — awaits user manual transcription
3. ⏸️ **Send Priority 1-3 questions** to Dr. Buckholtz (H-MULT formula, dataset source, sigma_MULT definition)

### High priority (pending primary source):

4. ✅ **Search Buckholtz manuscripts** for BBN/N_eff (Finding 7) — DONE (source_missing, see docs/23_gold_candidate_bbn_neff_source_check.md)
5. ✅ **Search Buckholtz manuscripts** for SIDM/Bullet Cluster (Finding 8) — DONE (source_missing, see docs/24_gold_candidate_sidm_bullet_cluster_source_check.md)
6. ✅ **Search Buckholtz manuscripts** for dark disk/Gaia (Finding 9) — DONE (source_missing, see docs/25_gold_candidate_dark_disk_gaia_source_check.md)

**Result:** All 3 gold candidates downgraded to `source_missing_constraint`. Common issue: Buckholtz defines IDM at HIGH LEVEL ("6 isomers", "multipole terms") but does NOT specify MICROPHYSICS (particle content, interactions, scales, thermal history). Without microphysics → cannot compute observables (N_eff, σ/m, ρ_DM(z)) → cannot determine constraint applicability.

**Search protocol:**
- ✅ Local docs search: grep for keywords (Finding 7: NO BBN/N_eff/thermal history in materials)
- WebSearch: "Buckholtz IDM BBN", "Buckholtz MULTING N_eff", etc. (IF local search incomplete)
- arXiv: search author:"Buckholtz" + keywords (IF author has arXiv preprints)
- If found: extract prediction, compare with observations
- If NOT found: add to clarification questions for Buckholtz

### Medium priority (after formula received):

7. ⏸️ **Reproduce Table A1 fit** — requires H-MULT formula (Finding 4 blocker resolution)
8. ⏸️ **Test alternative exponents** for Eq.15 (Finding 2 numerology check)
9. ⏸️ **Request explicit beta derivation** from Buckholtz (Finding 3 resolution)

---

## Gold Candidate Deep Dive (ALL THREE DOWNGRADED)

**Original status:** 3 gold candidates (BBN/N_eff, SIDM/Bullet Cluster, Gaia/dark disk)  
**Current status:** 0 gold candidates — all 3 downgraded to `source_missing_constraint` (2026-05-28)

**Common reason:** Buckholtz defines IDM at HIGH LEVEL ("6 isomers", "multipole terms") but does NOT specify MICROPHYSICS (particle content, interactions, scales, thermal history). Without microphysics → cannot compute observables (N_eff, σ/m, ρ_DM(z)) → cannot determine constraint applicability.

---

### 1. BBN / N_eff (Finding 7) — DOWNGRADED to source_missing_constraint

**Previous status (gold_candidate):**
- Independent dataset (z~10⁹ vs z<2), different physics (nucleosynthesis vs expansion)
- Unfitted parameter (N_eff NOT in H(z) fit)
- Strong constraint (Planck 2018 N_eff = 2.99 ± 0.17)

**Why downgraded (2026-05-28):**
- Source check complete (docs/23_gold_candidate_bbn_neff_source_check.md)
- Buckholtz does NOT discuss: thermal history, particle content of isomers, dark-sector temperatures, reheating
- Cannot assess applicability without knowing: Are isomers thermally populated? Do they contain dark photons/neutrinos?
- BBN/N_eff applies to thermally populated relativistic sectors — unknown if this describes IDM

**New classification:** `source_missing_constraint`

**Next action:** Ask Buckholtz: "Do dark isomers contain thermally populated relativistic particles at BBN epoch (T ~ MeV)?"

**Upgrade path:** IF Buckholtz confirms isomers are thermally populated mirror sectors → upgrade to gold_candidate. IF isomers are cold/non-relativistic → mark not_applicable.

---

### 2. SIDM / Bullet Cluster (Finding 8) — DOWNGRADED to source_missing_constraint

**Previous status (gold_candidate):**
- Independent dataset (cluster vs cosmology), different observable (lensing+X-ray vs H(z))
- Unfitted parameter (σ/m NOT in H(z) fit)
- Strong constraint (Bullet Cluster σ/m < 1–2 cm²/g)

**Why downgraded (2026-05-28):**
- Source check complete (docs/24_gold_candidate_sidm_bullet_cluster_source_check.md)
- Buckholtz does NOT specify: whether isomers are collisionless or self-interacting, what σ/m is, whether dipole/quadrupole are DM-DM scattering or modified gravity
- Bullet Cluster acknowledged in data anchoring map ("tests collisionless nature") but NO analysis of whether IDM is consistent
- Cannot assess applicability without knowing: interaction type (collisionless vs SIDM), cross-section σ/m, dipole interpretation (self-interaction vs modified gravity)

**Critical ambiguity:** MULTING mentions "dipole/quadrupole interactions" but does NOT clarify:
- Are these interactions BETWEEN dark matter particles (self-scattering → Bullet Cluster applies)?
- OR contributions to gravitational potential (modified gravity → Bullet Cluster does NOT directly constrain)?

**New classification:** `source_missing_constraint`

**Next action:** Ask Buckholtz: "Are the 6 isomers collisionless or self-interacting? If self-interacting, what is predicted σ/m? Are dipole/quadrupole DM-DM scattering or modified gravity contributions?"

**Upgrade path:** 
- IF collisionless → mark `not_applicable` (Bullet Cluster automatically satisfied)
- IF self-interacting → upgrade to `gold_candidate`, request σ/m, compare with σ/m < 1–2 cm²/g
- IF mixed (collisionless majority + self-interacting minority) → `partially_applicable`

---

### 3. Dark Disk / Gaia (Finding 9) — DOWNGRADED to source_missing_constraint

**Previous status (gold_candidate):**
- Independent dataset (kpc vs Gpc), different method (stellar kinematics vs expansion)
- Unfitted parameter (ρ_DM(z) NOT in H(z) fit)
- Moderate constraint (Gaia ρ_DM(z=0) = 0.3–0.6 GeV/cm³)

**Why downgraded (2026-05-28):**
- Source check complete (docs/25_gold_candidate_dark_disk_gaia_source_check.md)
- Buckholtz does NOT specify: scale range of dipole (cosmological Mpc vs galactic kpc), whether isomers are dissipative (dark photons, radiative cooling, dark atoms), whether dark disk formation predicted
- Gaia NOT cited in materials (only in OUR discovery ledger as candidate)
- Cannot assess applicability without knowing: dipole scale range, dissipative/non-dissipative

**Critical inference (OUR analysis, NOT author statement):**
- Beta_d ~ 4.25 → dimensional analysis (docs/12) → inferred scale L ~ 2.4 Mpc (group/cluster)
- This is 240× larger than galactic scales (Milky Way disk ~ 10 kpc = 0.01 Mpc)
- Suggests dipole may NOT operate at kpc scales → Gaia likely not applicable
- BUT: this is OUR inference, NOT explicit scale range from Buckholtz

**New classification:** `source_missing_constraint`

**Next action:** Ask Buckholtz: "At what scales does MULTING dipole operate? Cosmological (Mpc) or also galactic (kpc)? Are dark isomers dissipative (dark photons, radiative cooling)? Do they form dark disk or remain halo-like?"

**Upgrade path:**
- IF dipole only Mpc (cosmological) → mark `not_applicable` (Gaia measures kpc scales, dipole doesn't reach there)
- IF dipole also kpc AND isomers dissipative → upgrade to `gold_candidate` (after ρ_DM(z) calculation)
- IF dipole kpc but isomers non-dissipative → `partially_applicable` (halo density constraint, not disk)

---

**Common theme (all 3 constraints):** INDEPENDENT of H(z) fit (different datasets, eras, scales). IF MULTING makes predictions in these areas WITHOUT fitting to them → genuine tests, not circular validation. BUT: predictions require microphysics specification (particle content, interactions, scales, thermal history) — currently missing.

---

## Fool-Gold Deep Dive

**Why Finding 3 (beta numerology) is fool-gold:**

1. **Multiple alternatives:** Beta_d_2=0.78 has 20 formulas within 5% error (uniqueness 0.10)
2. **Post-hoc fitting:** Audit reconstructed betas AFTER seeing candidate values → selection bias
3. **No mechanistic derivation:** Formulas are arithmetic combinations of integers (1,2,3,4,7,9,17), no physics
4. **Circular reasoning risk:** Using OUR reconstruction to validate Buckholtz's model = testing OUR inference
5. **Sabine numerology score:** 4/5 questions = YES (π/e/φ patterns, no lagrangian, multiple alternatives, no uniqueness)

**How to convert fool-gold → copper:**
- Buckholtz provides EXPLICIT derivation formula (not post-hoc reconstruction)
- Formula has uniqueness score >0.7 (fewer alternatives)
- Derivation from symmetry/lagrangian (not arithmetic coincidence)

**Current status:** Fool-gold (numerology confirmed), NOT copper (no mechanistic derivation).

---

## Diamond Method Deep Dive

**Why Findings 5, 6, 10 are diamond methods (not just tools):**

### Finding 5: Table A1 Extraction Framework
- **Reusable:** Template applies to ANY tabular data from papers
- **Validation-first:** 14 tests written BEFORE data extraction (TDD for data)
- **Error detection:** Catches OCR/transcription errors automatically
- **Generalizable:** Can extend to other cosmology datasets (Pantheon+, BAO compilations)

### Finding 6: Provenance Audit Framework
- **Solves common problem:** Fitted → validation circularity in MANY alternative physics papers
- **Explicit tracking:** 6 provenance statuses + use permission hierarchy
- **Enforceable:** 25 tests prevent misuse of fitted parameters
- **Generalizable:** Applies to ANY theory with phenomenological parameters

### Finding 10: Fit-vs-Prediction Protocol
- **Prevents validation theater:** Fitted parameters cannot validate against fit dataset
- **Clear boundary:** Retrodiction (allowed) vs prediction (requires independent data)
- **Automated enforcement:** Tests check use_permission_status before allowing claims
- **Generalizable:** Protocol applies across domains (cosmology, particle physics, astrophysics)

**Why diamond (not just gold):**
- **Process innovation:** Not just a result, but a METHOD for getting results
- **Reusable:** Can be applied to future audits (other theories, other parameters)
- **Enforceable:** Implemented in code + tests (not just documentation)
- **Publishable:** Methodological papers: "Provenance Audit for Phenomenological Models", "Validation-First Data Extraction Protocol"

---

## Next Steps by Type

### Gold candidates (3):
1. **Search primary sources** — check if Buckholtz addresses BBN/SIDM/Gaia
2. **If found:** Extract predictions, compare with observations
3. **If NOT found:** Add to clarification questions for Buckholtz
4. **If predictions exist AND pass:** Upgrade to `copper_result` (confirmed useful)
5. **If predictions exist AND fail:** Downgrade to `dead_end` (falsified)

### Copper results (2):
1. **Document thoroughly** — findings verified, ready for citation
2. **Safe wording templates** — use for future communications with Buckholtz
3. **Sabine audit integration** — cross-reference with epistemological analysis

### Diamond methods (4):
1. **Generalize frameworks** — extend to other theories/datasets
2. **Publish methodology** — standalone papers on provenance audit, extraction protocol, fit-vs-prediction
3. **Open-source release** — GitHub repo for audit framework (reusable by others)

### Fool-gold (1):
1. **Document clearly** — warn against false uniqueness claims
2. **Request explicit derivation** — from Buckholtz (convert fool-gold → copper if derivation exists)
3. **Do NOT use for modeling** — audit-reconstructed values blocked

### Dead-end (1):
1. **Wait for blocker resolution** — H-MULT formula from Buckholtz (Priority 1 question)
2. **Document thoroughly** — what was attempted, why blocked, what's needed
3. **If unresolved long-term:** Document as "incomplete but transparent"

---

## Communication Protocol

**When presenting findings to Dr. Buckholtz:**

### DO ✅:
- Use **safe wording** from this ledger
- Distinguish **gold candidates** (pending verification) from **copper results** (verified)
- Mark **requires_primary_source** explicitly (do not assume)
- Present **diamond methods** as contributions to reproducibility (not criticism)
- Frame **fool-gold** as "requires clarification" (not "wrong")

### DO NOT ❌:
- Use **unsafe wording** from this ledger
- Present **gold candidates** as confirmed (they're pending)
- Present **audit reconstructions** as Buckholtz's claims (they're OUR inference)
- Present **fitted parameters** as predictions (circular reasoning)
- Present **numerology** as uniqueness (20 alternatives exist)

---

---

### Finding 11: PPN Check Status

| Field | Value |
|-------|-------|
| **Finding** | PPN (Parametrized Post-Newtonian) check for Solar System compatibility is BLOCKED — MULTING lacks weak-field metric, Solar System limit, k_A definition, and COM frame specification |
| **Type** | `source_missing_constraint` |
| **Evidence** | ✅ Analyzed manuscript: no weak-field metric provided, no explicit Solar System limit, no k_A definition for ordinary matter, no COM frame behavior specified. See docs/29_ppn_quick_check_requirements.md for 7 blocked checks. |
| **Source status** | `source_missing` (6 interpretation branches, all require author clarification) |
| **Verification status** | ✅ VERIFIED — 7 PPN checks defined (PPN-1 through PPN-7), all BLOCKED or UNKNOWN. 21 tests passing (test_ppn_checklist.py). |
| **Next test** | (1) Send author questions (docs/26 Priority 2). (2) If weak-field metric provided → extract γ, β parameters. (3) If cluster-scale-only confirmed → mark PPN as NOT_APPLICABLE. (4) If preferred frame confirmed → check α₁, α₂, α₃ constraints. |
| **Value for project** | MEDIUM — establishes honest blocker status (prevents premature refutation OR validation claims). Demonstrates audit discipline (will NOT claim "MULTING ruled out" without evidence). |
| **Safe wording** | "PPN check is currently not possible because MULTING lacks a weak-field metric, Solar System limit, and k_A definition. Author clarification required on: metric formulation, local applicability, kinetic energy parameters, COM frame behavior, preferred frame effects." |
| **Unsafe wording** | ❌ "MULTING is ruled out by PPN constraints" (no checks performed). ❌ "MULTING violates Solar System tests" (no local predictions available). ❌ "PPN parameters show MULTING is inconsistent with GR" (no PPN parameters derived). ❌ "MULTING passes Solar System tests" (no tests performed). |

**Interpretation branches (NOT claims — questions):**
1. **Branch 1 (local mass dipole):** HIGH PPN risk if dipole = Solar System mass distribution
2. **Branch 2 (kinetic energy dipole):** Requires k_A + COM frame definition
3. **Branch 3 (velocity-dependent):** Preferred frame risk (α₁, α₂ constraints very tight)
4. **Branch 4 (metric modification):** Needs weak-field metric to extract γ, β
5. **Branch 5 (cluster-scale only):** Solar System PPN may not apply if r << r_d cutoff
6. **Branch 6 (phenomenological H(z)):** Not enough for PPN (different regime)

**Blockers (cannot proceed without):**
- Weak-field metric or explicit Solar System limit
- k_A definition for ordinary matter (Sun, Earth)
- COM frame / preferred frame clarification
- Cutoff function f(r/r_d) or scale-dependent coupling
- Statement: do dipole/quadrupole apply to ordinary matter or dark matter only?

---

### Finding 12: MULTING Force-Law Layer Found, H(z) Closure Missing

| Field | Value |
|-------|-------|
| **Finding** | Public formula-stripping found candidate pairwise MULTING force-law equations (F_m, F_d, F_q, F_oP) and beta length-scale definitions (r_dA, r_dP, r_qAB), but NO closed H_MULT(z) formula for cosmological expansion |
| **Type** | `copper_result` (force-law layer) + `dead_end` (cosmological closure) |
| **Evidence** | ✅ Documented in docs/33_public_formula_stripping_report.md. Force equations: monopole F_m = G m_A m_P / r², dipole F_d = G c⁻² (k_A m_P |r_dA| + k_P m_A |r_dP|) / r³, quadrupole F_q = G k_A k_P c⁻⁴ |r_qAB|² / r⁴, total F_oP = F_m - F_d + F_q. Dimensional analysis confirms correct units. Beta length scales: r_dA = beta_d × r_A, r_dP = beta_d × r_P, |r_qAB|² = beta_q² × r_A × r_P. |
| **Source status** | `SOURCE_CANDIDATE` (awaiting manual PDF verification against preprints202511.0598.v6.pdf) |
| **Verification status** | ⏸️ PENDING — dimensional analysis passed (18/18 tests in test_multing_force_law_dimensionality.py), source verification NOT yet performed (manual PDF check required) |
| **Next test** | (1) Manual verification: read preprints202511.0598.v6.pdf character-by-character, confirm formulas exact match. (2) If verified → upgrade status SOURCE_CANDIDATE → SOURCE_CONFIRMED. (3) If NOT verified → downgrade to SOURCE_INCORRECT, re-extract manually. (4) Ask Buckholtz: mean-field approximation? Closure relations for m_A(z), r_A(z), k_A(z)? H_MULT(z) formula? |
| **Value for project** | MEDIUM — distinguishes force-law layer (potentially available) from cosmological closure (missing). Prevents premature H(z) modeling. Documents MCMC blocker explicitly. |
| **Safe wording** | "MULTING provides candidate pairwise force-law equations with monopole, dipole, and quadrupole terms. Public materials do not provide computational closure for mapping this force law to cosmological expansion H(z) or for MCMC parameter estimation. Force-law layer is documented as SOURCE_CANDIDATE (awaiting manual verification). H(z) modeling is BLOCKED pending closure relations and forward model." |
| **Unsafe wording** | ❌ "MULTING force law is complete and ready for H(z) modeling" (closure missing). ❌ "We can now compute H(z) from MULTING" (no mapping provided). ❌ "MCMC fitting is ready" (no forward model). ❌ "Force equations are source-confirmed" (still SOURCE_CANDIDATE, manual verification pending). |

**What We Have (force-law layer):**
- Pairwise force between objects A and P
- Depends on: masses (m_A, m_P), radii (r_A, r_P), kinetic energies (k_A, k_P), separation (r)
- Sign structure: monopole (+), dipole (−), quadrupole (+) — why dipole subtractive requires clarification
- Dimensional analysis: all force components have correct units [kg·m/s²]

**What We Do NOT Have (cosmological closure — CRITICAL BLOCKERS):**
1. **Mean-field approximation:** Pairwise force → stress-energy tensor T_μν
2. **Cosmological averaging:** Sum over galaxy clusters, voids, cosmic web
3. **Closure relations:** How m_A(z), r_A(z), k_A(z), D_C:AB(z) evolve with redshift
4. **Friedmann-like equations:** Modified H²(z; beta_d, beta_q, ...)
5. **Likelihood function:** P(H_obs | H_MULT(z; params)) for MCMC

**Code permission (enforced by tests):**
- Force laws: `allowed_for_dimensional_check` — can verify units, CANNOT compute H(z)
- Length scales: `allowed_for_record_only` — can document, CANNOT compute forces
- H(z) modeling: `NOT_ALLOWED` — explicitly blocked until closure provided

**MCMC readiness:** BLOCKED — no H_MULT(z) forward model

**Files created:**
- src/multing_force_law_records.py (dataclasses + records, 291 lines)
- tests/test_multing_force_law_dimensionality.py (18 tests, all passing)
- docs/33_public_formula_stripping_report.md (comprehensive report, 561 lines)

---

### Finding 13: Heuristic H-MULT Closure Candidate (AI Transcript)

| Field | Value |
|-------|-------|
| **Finding** | Possible heuristic scaling formula H_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)] appears in AI transcript materials, where Phi(z) = A_m(z) - A_d(z) + A_q(z). This is a phenomenological table-reproduction candidate, NOT rigorous physical derivation. |
| **Type** | `copper_result` (formula documented) + `dead_end` (predictive use blocked by missing cluster table) |
| **Evidence** | ✅ Documented in docs/35_ai_transcript_closure_candidate.md. Heuristic scaling preserves force-law sign structure (monopole + / dipole - / quadrupole +). Requires cluster variables (m_A(z), r_A(z), k_A(z)) to evaluate Phi(z) → cannot compute H_MULT without this. Status: AI_TRANSCRIPT_REPORTED (not source-confirmed). |
| **Source status** | `AI_TRANSCRIPT_REPORTED` (from AI materials, awaiting source confirmation) |
| **Verification status** | ⏸️ PENDING — source confirmation NOT yet performed (need to ask Buckholtz if this formula appears in manuscript or separate publication) |
| **Next test** | (1) Ask Buckholtz Q1-Q6 (docs/35 questions: formula source, cluster table, amplitude definitions, anchor point, sigma_MULT, rigorous derivation). (2) If cluster variables provided → attempt Table A1 reproduction. (3) If rigorous derivation provided → upgrade status, reassess use permission. (4) If neither provided → mark as phenomenological dead-end. |
| **Value for project** | MEDIUM — documents possible table-reproduction path (if cluster variables exist), prevents premature predictive modeling claims, enforces MCMC blocker. Distinguishes "may reproduce table" from "predicts H(z)". |
| **Safe wording** | "A possible heuristic scaling H_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)] appears in AI transcript materials. This may reproduce the reported Table A1 H_MULT column IF cluster variables (m_A(z), r_A(z), k_A(z)) are provided for all tabulated redshifts. However, this is a phenomenological formula, not a rigorous derivation from field equations. It cannot predict H(z) on new redshifts without full cluster variable table. MCMC parameter estimation remains blocked pending formal closure." |
| **Unsafe wording** | ❌ "This predicts cosmic expansion" (requires cluster table for all z). ❌ "This validates MULTING against H(z) observations" (phenomenological fit). ❌ "This is the Buckholtz H(z) equation" (AI transcript, not source-confirmed). ❌ "MCMC shows beta_d=4.5 and beta_q=18.0 are optimal" (fitted, not tested). ❌ "H_MULT outperforms ΛCDM" (no model comparison performed). ❌ "We can now compute H(z) from MULTING" (only for z where cluster variables known). |

**What We Have (heuristic closure candidate):**
- Formula: Phi(z) = A_m(z) - A_d(z) + A_q(z), H_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)]
- Sign structure: matches force-law (+ monopole - dipole + quadrupole)
- Known inputs: beta_d = 4.5, beta_q = 18.0 (from Table A1, fitted)
- Status: AI_TRANSCRIPT_REPORTED (not source-confirmed)

**What We Do NOT Have (CRITICAL BLOCKERS for table reproduction):**
1. **Cluster variable table:** m_A(z), r_A(z), k_A(z) for all z_i in Table A1 (CRITICAL)
2. **H_anchor:** Reference Hubble parameter (H(z=0)? H_FLRW? other?)
3. **z_anchor:** Anchor redshift (z=0? z=0.5? other?)
4. **Amplitude definitions:** How are A_m(z), A_d(z), A_q(z) defined? (force amplitudes? potential? dimensionless?)
5. **sigma_MULT definition:** How are uncertainties computed?
6. **Formal derivation:** Phi(z) → H(z) mapping from field equations
7. **Parameter count:** How many free parameters total?
8. **AIC/BIC comparison:** MULTING vs ΛCDM model comparison

**Use permission (enforced by tests):**
- ✅ ALLOWED: Document formula, attempt table reproduction IF cluster variables provided
- ❌ NOT ALLOWED: Predictive modeling (requires cluster table for all z)
- ❌ NOT ALLOWED: MCMC parameter estimation (no forward model, no likelihood)

**MCMC readiness:** BLOCKED — no forward model H_MULT(z; params) computable for arbitrary z

**Table reproduction readiness:** CANDIDATE — possible IF cluster variables provided (not guaranteed to match)

**Files created:**
- src/hmult_closure_candidates.py (dataclasses + guards, 292 lines)
- tests/test_hmult_closure_candidate_status.py (27 tests, all passing)
- docs/35_ai_transcript_closure_candidate.md (comprehensive report, 653 lines)

---

## Finding 14 — Force-to-Expansion Bridge Triage: Zero Source-Supported Routes (2026-05-28)

| Field | Value |
|-------|-------|
| **Finding** | Systematic triage of all possible F_oP → H(z) bridge routes found ZERO source-supported paths. Six routes evaluated (A-F): 2 computational reconstructions, 3 speculative toy models, 1 dead end. Critical blocker: Q0 (force-to-expansion mapping) must be answered before MCMC can proceed. |
| **Type** | `critical_blocker` (MCMC blocked) + `copper_result` (triage complete, all routes documented) |
| **Evidence** | ✅ Documented in docs/36_force_to_expansion_bridge_triage.md + src/bridge_candidate_registry.py. Evaluated routes: (A) Newtonian dust + extra forces, (B) Effective stress-energy tensor, (C) Parametrized Friedmann, (D) Scalar field / dark energy, (E) N-body backreaction, (F) PPN extrapolation. Status: 0 SOURCE_SUPPORTED, 2 COMPUTATIONAL_RECONSTRUCTION, 3 SPECULATIVE_TOY_MODEL, 1 DEAD_END. MCMC readiness: BLOCKED (no forward model). |
| **Source status** | `SOURCE_MISSING` — no manuscript material describes F_oP → H(z) mapping |
| **Verification status** | ✅ VERIFIED (2026-05-28) — triage complete, all 6 routes evaluated and classified |
| **Next test** | Priority 0: Ask Buckholtz Q0 (How does F_oP = F_m - F_d + F_q translate into H(z)? Is there a modified Friedmann equation, effective stress-energy tensor, spatial averaging prescription, or phenomenological parametrization?). If Q0 answered → implement source-supported bridge route → unblock MCMC. If Q0 not answered → mark as permanent blocker, archive speculative routes, publish repository as incomplete. |
| **Value for project** | HIGH — prevents premature MCMC attempts on unsupported routes, documents why MCMC is blocked (not arbitrary), identifies critical path forward (Q0 answer), enforces distinction between "audit reconstruction" and "Buckholtz's model". |
| **Safe wording** | "The pairwise MULTING force law is documented (SOURCE_CANDIDATE), but the mapping from F_oP to cosmological expansion H(z) is not found in available materials. Six possible bridge routes exist (Newtonian dust, stress-energy, parametrized Friedmann, scalar field, backreaction, PPN). None are source-supported. Implementing any route without author confirmation = testing our interpretation, not Buckholtz's model. MCMC parameter estimation remains blocked pending Q0 clarification." |
| **Unsafe wording** | ❌ "MULTING is refuted because homogeneous averaging nulls dipole" (assumes standard averaging without confirming approach). ❌ "The model is inconsistent — no bridge from F_oP to H(z) exists" (bridge may exist in unpublished work). ❌ "We proved MULTING cannot work" (documented absence of source material, not physical impossibility). ❌ "PPN rules out MULTING" (PPN checks blocked). ❌ "The force law is wrong" (force law is SOURCE_CANDIDATE, not SOURCE_INCORRECT). |

**Bridge Matrix:**

| Route | Type | Status | Source Support | MCMC Ready | Q0 Needed |
|-------|------|--------|----------------|------------|-----------|
| **A. Newtonian dust + extra forces** | Computational reconstruction | CANDIDATE | ❌ NO | ❌ NO | ✅ YES |
| **B. Effective stress-energy tensor** | Speculative toy model | CANDIDATE | ❌ NO | ❌ NO | ✅ YES |
| **C. Parametrized Friedmann (MGCAMB)** | Computational reconstruction | CANDIDATE | ❌ NO | ❌ NO | ✅ YES |
| **D. Scalar field / dark energy map** | Speculative toy model | CANDIDATE | ❌ NO | ❌ NO | ✅ YES |
| **E. N-body → fluid backreaction** | Speculative toy model | CANDIDATE | ❌ NO | ❌ NO | ✅ YES |
| **F. PPN extrapolation to cosmology** | Dead end | REJECTED | ❌ NO | ❌ NO | ❌ NO (wrong regime) |

**Critical nuance — Standard Averaging vs Non-Standard:**

Standard homogeneous Newtonian averaging would null dipole/quadrupole background contributions (spatial gradients average to zero in FRW symmetry). **This is NOT a refutation of MULTING.** It means one of the following:
1. MULTING uses non-standard averaging (backreaction framework, Q-cosmology)
2. Dipole/quadrupole enter as effective stress-energy components (not geometric averaging)
3. Dipole/quadrupole are cluster-scale only (not cosmological background)
4. MULTING is metric modification (not Newtonian + forces)

Without author clarification (Q0), we cannot determine which (if any) applies.

**Priority 0 Question (Q0):**
> "How does the pairwise MULTING force law F_oP = F_m - F_d + F_q translate into a cosmological background expansion equation H(z)? Is there a modified Friedmann equation, an effective stress-energy tensor, a spatial averaging prescription (e.g., backreaction framework), or is H_MULT(z) a phenomenological parametrization independent of the pairwise force law?"

**MCMC blocker chain:**
```
No Q0 answer
  ↓
No F_oP → H(z) mapping
  ↓
No forward model H_MULT(z; params)
  ↓
No MCMC
```

**Files created:**
- docs/36_force_to_expansion_bridge_triage.md (comprehensive triage, 15 sections)
- src/bridge_candidate_registry.py (dataclasses + guards, 6 bridge records)
- tests/test_bridge_candidate_registry.py (28 tests, all passing)

**Relationship to Finding 13 (heuristic closure candidate):**

Heuristic Phi(z) scaling (docs/35) is **one possible bridge** (phenomenological parametrization), but:
- Not source-confirmed (AI_TRANSCRIPT_REPORTED)
- Requires cluster variables (not provided)
- Phenomenological (fitted, not derived)

Finding 14 shows **5 other possible routes** (A, B, D, E, F), none source-supported. All routes remain **audit reconstructions** or **speculative proposals** until Q0 answered.

---

## Finding 15 — Minimum Viable Bridge Candidate: Discrete Lattice + Virial Effective-Fluid Route (2026-05-28)

| Field | Value |
|-------|-------|
| **Finding** | After evaluating 6 bridge routes (Finding 14), the strongest non-source-supported candidate is: pairwise forces → discrete cluster lattice (Wigner-Seitz cells) → nearest-neighbor dynamics → virial pressure P = -⟨r · F⟩/(3V) → effective fluid (ρ_eff, P_eff) → Friedmann acceleration ä/a = -(4πG/3)(ρ + 3P) → H(z). This is a RESEARCH_HYPOTHESIS, NOT source-supported. |
| **Type** | `copper_result` (strongest candidate documented) + `research_hypothesis` (computational reconstruction candidate, not source-confirmed) |
| **Evidence** | ✅ Documented in docs/37_discrete_lattice_mvb_hypothesis.md + src/minimum_viable_bridge_registry.py. Route uses: (1) discrete topology (cosmic web as nearest-neighbor lattice), (2) virial theorem (pairwise forces → thermodynamic pressure), (3) Friedmann acceleration equation (more fundamental than H² equation). Status: RESEARCH_HYPOTHESIS, NOT_SOURCE_SUPPORTED, NOT_MCMC_READY. 10 required inputs documented (lattice geometry, neighbor count, cell volume, m_A(z), k_A(z), k_B(z), r_A(z), anisotropy tensor, time averaging, boundary conditions). 5 risks documented (may become "our model", backreaction too small, lattice breaks homogeneity, parameter degeneracy, no author confirmation). |
| **Source status** | `NOT_SOURCE_SUPPORTED` — no manuscript material confirms discrete lattice / virial pressure approach |
| **Verification status** | ✅ RESEARCH_HYPOTHESIS COMPLETE (2026-05-28) — route documented, tests passing (28/28), MCMC status enforced |
| **Next test** | (1) Ask Buckholtz Q_MVB (Does MULTING use discrete lattice approximation? Is virial pressure P = -⟨r · F⟩/(3V) the bridge to Friedmann? If not, what is the correct averaging prescription?). (2) If confirmed → implement MVB forward model, unblock MCMC. (3) If rejected → archive route, await alternative. (4) Order-of-magnitude check: estimate P_virial / P_ΛCDM before full implementation — if ratio < 0.01, reject early. |
| **Value for project** | MEDIUM — provides constructive path forward (if author confirms), prevents ad-hoc route invention, documents what inputs are needed, distinguishes this from heuristic Phi(z) scaling (Finding 13). Does NOT unblock MCMC (remains NOT_MCMC_READY). |
| **Safe wording** | "After systematic bridge triage (Finding 14), the strongest candidate route is: discrete cluster lattice → virial pressure → Friedmann acceleration → H(z). This route is physically motivated (virial theorem), mathematically tractable (well-defined operators), and testable (requires 10 inputs). However, it is a research hypothesis / computational reconstruction candidate. It is NOT source-supported. Implementing it without author confirmation = testing our interpretation, not Buckholtz's model. MCMC remains blocked pending Q_MVB answer." |
| **Unsafe wording** | ❌ "This solves the F_oP → H(z) bridge" (not source-confirmed). ❌ "This proves MULTING uses discrete lattice" (hypothesis, not proof). ❌ "MCMC is now ready" (still blocked). ❌ "This validates MULTING cosmology" (route not confirmed). ❌ "Buckholtz's approach uses virial pressure" (unless explicitly confirmed). ❌ "The only viable path forward" (5 other routes exist, though weaker). |

**Why MVB is useful:**

1. **Physically motivated:** Virial theorem is standard statistical mechanics (P = -⟨r · F⟩/(3V)) — no ad-hoc formulas
2. **Mathematically tractable:** Well-defined operators (spatial averaging, nearest-neighbor sum, cell volume)
3. **Testable:** Requires specific inputs (lattice geometry, neighbor count) — can verify or falsify
4. **Distinct from Phi(z):** Heuristic scaling (Finding 13) is phenomenological fit; MVB is mechanistic reconstruction
5. **Constructive path:** Identifies exactly what author clarification is needed (Q_MVB)

**Why MVB is NOT source-supported:**

1. No manuscript material mentions discrete lattice, Wigner-Seitz cells, or cluster-neighbor topology
2. No manuscript material mentions virial pressure or virial theorem
3. No manuscript material mentions Friedmann acceleration equation (only H² equation referenced)
4. This route is **our reconstruction** from first principles, not Buckholtz's stated approach
5. Cannot implement without author confirmation → risk of "testing our model, not Buckholtz's"

**Difference from Finding 13 (heuristic Phi(z) scaling):**

| Aspect | Finding 13 (Phi(z) scaling) | Finding 15 (MVB discrete lattice) |
|--------|-----------------------------|------------------------------------|
| **Type** | Phenomenological parametrization | Mechanistic reconstruction |
| **Origin** | AI transcript materials | First-principles virial theorem |
| **Inputs** | Cluster amplitudes A_m, A_d, A_q | Lattice geometry, neighbor count, virial sum |
| **Formula** | H_MULT² ∝ Phi(z) = A_m - A_d + A_q | P_virial = -⟨r · F⟩/(3V) → Friedmann acceleration |
| **Status** | AI_TRANSCRIPT_REPORTED | RESEARCH_HYPOTHESIS |
| **Use case** | May reproduce Table A1 if cluster variables exist | May predict H(z) if lattice inputs confirmed |

Both are **computational reconstruction candidates**. Neither is source-supported. Q0 and Q_MVB together ask author to choose/confirm the bridge route.

**Author clarification question (Q_MVB):**
> "Does MULTING use a discrete lattice approximation (e.g., Wigner-Seitz cells, cluster-based topology) to map pairwise forces F_oP to cosmological pressure? Specifically: (1) Is the cosmic web modeled as nearest-neighbor interactions between discrete cells? (2) Is virial pressure P = -⟨r · F⟩ / (3V) the bridge to Friedmann acceleration ä/a = -(4πG/3)(ρ + 3P)? (3) If not, what is the correct spatial averaging prescription for F_oP → H(z)?"

**MCMC readiness:** STILL BLOCKED — MVB is research hypothesis, not source-confirmed bridge

**Files created:**
- docs/37_discrete_lattice_mvb_hypothesis.md (comprehensive route documentation, 12 sections)
- src/minimum_viable_bridge_registry.py (dataclasses + guards, MVB candidate record)
- tests/test_minimum_viable_bridge_registry.py (28 tests, all passing)

---

## Finding 16 — Appendix A1 Forensic Extraction: H_MULT Formula Missing, AI Discretion Allowed (2026-05-29)

| Field | Value |
|-------|-------|
| **Finding** | Word-level forensic extraction of Appendix A1 Steps 3–7 confirms: (1) Force formulas provided ✅, (2) Scaling relations provided ✅, (3) β_d, β_q fitted to minimize σ from H-data ✅, (4) H_MULT computational formula NOT provided ❌. Step 5 gives only procedural instruction: *"How well can you fit (by using my monopole, dipole, and quadrupole components of gravity) the data..."* with AI discretion: *"Feel free to use any or all the information"*. Table A1 H_MULT values = AI service output, not author calculation. |
| **Type** | `critical_blocker` (H_MULT formula missing) + `copper_result` (forensic extraction complete, all evidence documented) |
| **Evidence** | ✅ Forensic extraction: docs/39_appendix_a1_steps_3_7_forensic_reading.md (full verbatim quotes from Steps 3–7). Programmatic encoding: src/appendix_a1_procedure_registry.py (16 variables, 5 steps, Table A1 data). Verification: tests/test_appendix_a1_procedure_registry.py (26/26 tests passed). Step 5 provides: scaling relations (r_dA = β_d × r_A, r_dP = β_d × r_P, |r_qAB|² = β_q² × r_A × r_P) ✅, constraint (minimize standard-deviations from H-data) ✅, AI discretion allowed ✅. Step 5 does NOT provide: functional form H_MULT(z, β_d, β_q, m_A, r_A, k_A, ...) ❌, objective function details ❌, computational procedure ❌. |
| **Source status** | `UNDER_SPECIFIED` — procedural instruction only, NOT computational formula. Table A1 = AI service interpretation, not author-verified calculation. |
| **Verification status** | ✅ FORENSIC EXTRACTION COMPLETE (2026-05-29) — all Steps 3–7 extracted verbatim, variable provenance table complete, bridge status confirmed: PARTIAL (heuristic only, NO formula) |
| **Next test** | (1) Update clarification brief (docs/26, docs/38) with Step 5 finding. (2) Add to Priority 1 question: "Appendix A1 Step 5 instructs AI service to fit monopole/dipole/quadrupole to H-data but does not provide explicit computational formula H_MULT(z; β_d, β_q, ...). Table A1 reports H_MULT values as AI service output. Could you provide the explicit formula, or confirm that AI interpretation (heuristic scaling? virial pressure? other?) matches your intended approach?" (3) After formula received: implement, reproduce Table A1, verify against reported values. |
| **Value for project** | CRITICAL — upgrades Finding 4 from "formula unclear" to "formula UNDER_SPECIFIED with forensic evidence". Provides exact verbatim quotes to cite when asking author. Documents AI discretion scope. Distinguishes source-confirmed (force formulas ✅) from under-specified (H_MULT formula ❌). Confirms Table A1 as empirical reference, NOT predictive model. |
| **Safe wording** | "Forensic extraction of Appendix A1 Steps 3–7 confirms that force formulas and scaling relations are provided, but H_MULT computational formula is NOT. Step 5 gives procedural instruction ('fit by using monopole, dipole, quadrupole') and allows AI discretion ('Feel free to use any or all the information'). Table A1 H_MULT values are AI service output following this instruction. Without explicit formula, we can store Table A1 as empirical data table but cannot compute H_MULT(z) on new redshifts or perform MCMC parameter estimation." |
| **Unsafe wording** | ❌ "Formula is in Appendix A1" (only scaling relations, NOT full H_MULT formula). ❌ "We can compute H_MULT from Step 5" (procedural only, NOT computational). ❌ "Table A1 proves the formula works" (AI interpretation, not verified). ❌ "Author calculated H_MULT values" (AI service calculated them). ❌ "Step 5 is complete" (under-specified for reproducible computation). |

**What Appendix A1 Steps 3–7 Provide:**

| Step | Title | Provides | Status |
|------|-------|----------|--------|
| **3** | Time Range | t_ROE,min definition, Set of Times | SOURCE_CONFIRMED |
| **4** | Galaxy Cluster Parameters | Table structure: Time, z, m_A, r_A, D_C:AB, k_A/c², H-data | AUTHOR_PROMPT_INSTRUCTION |
| **5** | Approximate Matches | Scaling relations (r_dA/r_dP/r_qAB), β_d/β_q fitting constraint, AI discretion | **UNDER_SPECIFIED** |
| **6** | Future Projections | FLRW comparison request, MULTING crossover time estimate | BLOCKED (requires H_MULT formula) |
| **7** | w_eff Comparison | w_eff(z) computation via FLRW, comparison table | SOURCE_CONFIRMED |

**What Appendix A1 Steps 3–7 Do NOT Provide (CRITICAL):**

1. **H_MULT functional form:** No equation H_MULT = f(z, β_d, β_q, m_A, r_A, k_A, ...) ❌
2. **Objective function:** Beyond "minimize standard-deviations" — no specific loss function, no weighting scheme ❌
3. **Computational procedure:** Step-by-step algorithm for computing H_MULT from cluster parameters ❌
4. **Cluster variable table:** m_A(z), r_A(z), k_A(z) values for all z_i in Table A1 ❌
5. **AI service implementation:** What formula/method did AI service actually use? Unknown ❌

**Variable Provenance Matrix (16 variables extracted):**

| Variable | Provenance | Code Permission | Step |
|----------|------------|-----------------|------|
| Time, z, H-data | DATA | CODE_READY | 3–4 |
| m_A, r_A, D_C:AB, k_A/c² | AI_ESTIMATED | NOT_CODE_READY | 4 |
| β_d, β_q | FITTED_PHENOMENOLOGICAL | ALLOWED_FOR_TABLE_REPRODUCTION_ONLY | 5 |
| H-MULT | **UNDER_SPECIFIED** | **BLOCKED** | 5 |
| H-FLRW, σ_FLRW | FORMULA_PROVIDED | CODE_READY | 5 |
| w_eff, H-w_eff, σ_w_eff | AI_ESTIMATED / DERIVED | CODE_READY | 7 |

**Bridge Finding (F_oP → H_MULT):**

**Question:** Does Appendix A1 explicitly define F_oP → H_MULT(z)?  
**Answer:** NO, formula missing  
**Status:** PARTIAL — procedural/heuristic bridge only, NOT computational formula

**Evidence:**
- Force formulas: F_m, F_d, F_q, F_oP provided (Step 2) ✅
- Scaling relations: r_dA = β_d × r_A, etc. provided (Step 5) ✅
- H_MULT(z) formula: NOT provided ❌
- AI discretion: "Feel free to use any or all the information" ✅ (bridge delegated to AI)

**Implications:**

1. **Table A1 reproduction:** Can store as empirical data ✅, CANNOT compute H_MULT(z) on new redshifts ❌
2. **β_d, β_q fitting:** Method under-specified (objective function beyond "minimize σ" unclear) ❌
3. **MCMC parameter estimation:** BLOCKED (no H_MULT likelihood function) ❌
4. **Future projections (Step 6):** BLOCKED (requires H_MULT(z) formula) ❌
5. **Validation/falsification:** BLOCKED (cannot test MULTING predictions without formula) ❌

**Code permission enforcement (26 tests):**

```python
# From test_appendix_a1_procedure_registry.py (all passing)
assert h_mult.provenance == VariableProvenance.UNDER_SPECIFIED
assert h_mult.code_permission == CodePermission.BLOCKED
assert is_operation_blocked("H_MULT(z) computation — formula missing")
assert is_operation_blocked("MCMC parameter estimation — requires H_MULT(z) likelihood function")
assert not hasattr(registry, "compute_Hz")  # No H_MULT function exists
```

**Files created:**
- docs/39_appendix_a1_steps_3_7_forensic_reading.md (full forensic extraction, 9.5 KB)
- src/appendix_a1_procedure_registry.py (programmatic encoding, 14 KB)
- tests/test_appendix_a1_procedure_registry.py (26 tests, 26/26 passed)

**Updated files:**
- docs/18_fit_reproduction_requirements.md (added Step 5 finding)
- docs/22_discovery_ledger.md (Finding 4 updated, Finding 16 added)
- PROJECT_STATUS.md (version v0.2-appendix-a1-forensic)

**Relationship to other findings:**

- **Finding 4 (Missing H-MULT formula):** UPGRADED with forensic evidence from Appendix A1
- **Finding 12 (Force-law layer found):** Confirms force formulas are SOURCE_CANDIDATE, H_MULT closure still missing
- **Finding 13 (Heuristic Phi(z) scaling):** One possible AI interpretation, not source-confirmed
- **Finding 14 (Bridge triage):** Zero source-supported routes — Appendix A1 confirms this (no explicit bridge)
- **Finding 15 (MVB discrete lattice):** Another possible interpretation, not source-confirmed

---

**Document status:** ACTIVE — updated as audit progresses

**Last updated:** 2026-05-29  
**Next review:** After author clarification received, after H_MULT formula provided, after Table A1 reproduction attempted  
**Maintainer:** Buckholtz IDM/MULTING audit team

## Finding 18: Row 1 Table A1 Sigma Anomaly (2026-05-29)

**Status:** SOURCE_TABLE_OUTLIER  
**Classification:** Localized inconsistency (1/12 rows)  
**Impact:** Does not invalidate Rows 2-12

**Finding:** Row 1 (z=0) sigma values have larger-than-expected differences:
- sigma_MULT: reported 1.30, calculated -1.727 → diff 3.027 (27× tolerance)
- Rows 2-12: max diff 0.039 (all within tolerance)

**Recommendation:** Exclude Row 1 from internal fits until author clarifies (Q14).

**Reference:** docs/43 Part 7, data/table_a1_reported.csv Row 1 note

---

## Finding 19: Candidate B Dimensional Bridge Audit (2026-05-29)

**Status:** BEST_INTERNAL_RECONSTRUCTION_CANDIDATE (not source-confirmed)  
**Classification:** Mathematical stress test complete  
**MCMC:** BLOCKED (missing m_A(z), k_A(z), r_A(z), D_AB(z), N_eff)

**Finding:** Discrete Lattice ODE passes dimensional/sign checks:
- Formula: ä/a = N_eff × F_oP / (μ × D_AB)
- Units: [F/(μ×D)] = [T⁻²] = [ä/a] ✅
- Sign: Consistent with late-time acceleration ✅

**Risk:** May become our model, not Buckholtz's (requires author confirmation Q15).

**Alternatives:**
- Phi(z) heuristic: TABLE_ONLY (dimensionally under-specified)
- Candidate G (Potential): NEEDS_VERIFICATION (a⁻⁵ unverified)

**Reference:** docs/43, src/bridge_candidate_math_audit.py

---

## Finding 20: MCMC Blocker Chain (2026-05-29)

**Status:** MCMC_BLOCKED, AUTHOR_CONFIRMATION_REQUIRED  
**Classification:** Project-wide blocker documentation  
**Impact:** HIGH — prevents MCMC validation until resolved

**Finding:** MCMC comparison (ΛCDM vs. MULTING) blocked by **four sequential requirements**:

1. **Source-Confirmed Bridge Missing** (Blocker 1)
   - F_oP → H_MULT(z) rule not specified in Appendix A1
   - Hamiltonian H²(a)=H₀²[Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵] algebraically valid but NOT confirmed
   - Status: AUTHOR_CONFIRMATION_REQUIRED (Q15, Q16 prepared)

2. **Cluster Variables Missing** (Blocker 2)
   - Cannot compute Ω coefficients without m_A(z), r_A(z), D_AB(z), N_eff
   - Status: MISSING_INPUTS (Q17 prepared)

3. **Independent Data Missing** (Blocker 3)
   - Table A1 used for beta fit → circular if also validation set
   - Need: Pantheon+, BAO, or Cosmic Chronometers
   - Status: OUT_OF_SAMPLE_REQUIRED

4. **Complexity Penalty Not Applied** (Blocker 4)
   - MULTING (5 params) vs. ΛCDM (3 params) requires AIC/BIC
   - Status: COMPLEXITY_PENALTY_REQUIRED

**Current unblock status:** 0/4 resolved → MCMC remains BLOCKED

**Safe work allowed:**
- ✅ Internal diagnostic fit (INTERNAL_DIAGNOSTIC_FIT_ONLY)
- ✅ Leave-one-out stability
- ✅ Baseline comparisons
- ✅ Q15-Q17 preparation

**Unsafe work (blocked):**
- ❌ MCMC as Buckholtz validation
- ❌ Prediction on new z
- ❌ Public validation claim
- ❌ Using "Buckholtz formula" for Hamiltonian

**Evidence classification:**
- H_MULT 6× closer to H_obs: ✅ RETRODICTION_EVIDENCE
- Table A1 validation: ❌ NOT_PREDICTION (beta fitted on this data)

**Next test:** Wait for author response → if Hamiltonian confirmed: implement compute_Hz_MULTING with SOURCE_CONFIRMED status → integrate Cosmic Chronometers → run MCMC with AIC/BIC.

**Value:** CRITICAL — documents exactly why MCMC is blocked and what must happen to unblock.

**Reference:** docs/54_mcmc_blocker_chain.md (full 16 KB documentation)

---

## Finding 21: k_A(z) Is the Missing Function for Predictive Bridge (2026-06-06)

**Status:** INTERNAL_CLOSURE_TEST | NOT_VALIDATION | AUTHOR_CONFIRMATION_REQUIRED  
**Impact:** HIGH — constructive path for author correspondence

**Finding:** Independent k_A(z) (Press-Schechter + virial, α@z=0) can replace CSV k_A in the Phi-ratio bridge without refitting β. Closure PASS/FAIL measures implementation self-consistency, not theory validity.

**Evidence:** `src/k_a_closure_test.py`, γ_req≈2.27 in `d_required_solver.py`.

**Safe wording:** "Implementation closure test." **Unsafe:** "MULTING falsified."

---

## Finding 22: Double-Inversion Diagnostic (2026-06-06)

**Status:** VERIFIED_DIAGNOSTIC | NOT_VALIDATION | NOT_REFUTATION | AUTHOR_BRIDGE_NEEDED

**Finding:** Stage 1 isolines + Stage 2 (γ, α) grid test whether physically admissible (D, k_A) trajectories exist that reproduce H_obs — goal is falsification picture, not new fit layer.

**Reference:** `docs/DOUBLE_INVERSION_DIAGNOSTIC.md`

---
