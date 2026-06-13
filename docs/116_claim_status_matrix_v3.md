# docs/116 — Claim Status Matrix v3

**Date:** 2026-06-13  
**Gate:** Post-LOO-TNG-AIC Session Lock  
**Supersedes:** docs/108 (v2, 2026-06-12)  
**Incorporates:** docs/113 (HD-MAVP-1), docs/114 (O7 lock), commit d1b5025 (LOO + TNG)

```
SAFETY LABELS (HARD):
  NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_MODEL_FALSIFICATION
  INTERNAL_DIAGNOSTIC_ONLY · OUR_RECONSTRUCTION
  NO_EMAIL_BEFORE_2026-06-18 · NO_PUBLIC_CLAIMS · NO_MCMC
  NOT_THEORY_FALSE · NOT_AI_HALLUCINATION_CLAIM · NOT_FABRICATION_CLAIM
```

---

## What Changed from v2 (docs/108)

| Area | v2 status | v3 status | Source |
|------|-----------|-----------|--------|
| O6 — ε peak vs cluster history | PARTIAL_EVIDENCE | OPEN / SELECTION_AMBIGUITY | docs/113 HD-MAVP-1 |
| O8 — 5 isomers → Ω_DM/Ω_b ≈ 5 | OPEN | REJECTED_AS_DERIVATION (NR-007) | docs/114 |
| O11 — MCMC possible? | BLOCKED | BLOCKED / PARTIAL (blocker 4 ✅) | commits 46277b9 + d1b5025 |
| Intrinsic PS formation | not explicitly tested | KILLED (r=−0.10 to +0.08 all M_min) | docs/113, NR-005 |
| f_sel artifact | not tested | SURVIVES (r=0.666, 85% of M8-C variance) | docs/113, NR-005 |
| AIC/BIC model comparison | — | ΔAIC=−16.65 decisive IN-SAMPLE | commit 46277b9 |
| LOO leverage analysis | — | z_peak=0.603, r=0.921, 0 outliers (LogNormal) | commit d1b5025 |
| TNG merger proxy | — | r=0.652, NON-MONOTONE, peak z=0.40 | commit d1b5025 |
| BETA-1 | — | INFRA_READY / HOLD | docs/115 |

---

## Scope Field Legend

| Scope | Meaning |
|---|---|
| `AUTHOR_MODEL` | Claim about the preprint's stated physics |
| `OUR_RECONSTRUCTION` | Claim about our independent reconstruction from public CSV |
| `TABLE_LEVEL_DIAGNOSTIC` | Claim about numerical patterns in Table A1 values |
| `CONDITIONAL_BENCHMARK` | Claim valid only IF a specific assumption holds |
| `CONFIRMED_OPERATIONAL` | Administrative/process claim, independently verifiable |

---

## 1. CONFIRMED — Зафиксировано аудитом

| # | Claim | Status | Scope | Evidence |
|--:|---|---|---|---|
| 1 | Формулы сил `F_m`, `F_d`, `F_q`, `F_oP` присутствуют в препринте | **CONFIRMED** | AUTHOR_MODEL | Прямое чтение препринта |
| 2 | Явный author-confirmed bridge `F_oP → H_MULT(z)` не найден в публичных материалах | **CONFIRMED BLOCKER** | AUTHOR_MODEL | Q1 blocker; 0/5 MCMC blockers resolved |
| 3 | Step 5 использует логику "fit H(z)", а не строго "compute H(z)" | **CONFIRMED / HIGH-SIGNAL** | OUR_RECONSTRUCTION | AI-bridge gap; разные AI сервисы дают разные β |
| 4 | Claude, Gemini, ChatGPT дают разные `β_d`, `β_q` | **CONFIRMED** | OUR_RECONSTRUCTION | Multi-AI CSV comparison (docs/73) |
| 5 | `β_d`, `β_q` — phenomenological / AI-assisted fitting при текущих данных | **CONFIRMED-AS-CURRENT-INTERPRETATION** | OUR_RECONSTRUCTION | Нет независимого правила вывода β без подгонки |
| 6 | M2-G4: β-параметры не идентифицируются из Table A1 (Fisher rank 1) | **CONFIRMED** | OUR_RECONSTRUCTION | commit 91ea667 |
| 7 | Table A1: ε(z) ≠ const; пик ε=0.2277 при z=0.40; минимум ε=0.0481 при z=5.0 | **CONFIRMED** | TABLE_LEVEL_DIAGNOSTIC | M8-A-R1 adversarial re-audit (commit add7cba) |
| 8 | SC-2: наша реконструкция даёт gap ×4365 при z=8.5 | **CONFIRMED** | OUR_RECONSTRUCTION | Failure нашего bridge, не refutation theory |
| 9 | F5/Local Group: при наших параметрах `F_d/F_m ≈ 3×10⁻⁷` — в ~3.3M× слабее гравитации | **CONFIRMED** | OUR_RECONSTRUCTION | Falsifies local dominance under our reconstruction only |
| 10 | M7-A Eq31 `7:9:17` численно близко; derivation отсутствует | **PARTIAL CONFIRMED** | AUTHOR_MODEL | Численная близость есть; теорема не выведена |
| 11 | M7-C: ΔN_eff для IDM нельзя вычислить из препринта | **CONFIRMED BLOCKED** | AUTHOR_MODEL | Нет T_dark/T_visible, decoupling, thermal history |
| 12 | Mirror DM условие: нужен T_dark/T_SM < ~0.27–0.37 | **CONFIRMED CONDITIONAL** | CONDITIONAL_BENCHMARK | При равной T: ΔN_eff → 130–477σ над Planck |
| 13 | ε(z) немонотонна: peak z=0.40, min z=5.0, secondary uptick z=8.5 | **CONFIRMED** | TABLE_LEVEL_DIAGNOSTIC | M8-A + M8-A-R1 (commit add7cba) |
| 14 | Constant-ε и power-law bridges не объясняют Table A1 | **CONFIRMED** | OUR_RECONSTRUCTION | M8-A + M8-C |
| 15 | Письмо Q1–Q3 TJB отправлено 2026-06-12 | **CONFIRMED** | CONFIRMED_OPERATIONAL | commit 9513289 |
| 16 | M8-C: Survey dN/dz пикует вблизи z=0.40–0.65 при M_min=1e14; вторичная структура не объяснена | **PARTIAL** | OUR_RECONSTRUCTION | Pearson r=0.723; verdict PARTIAL, HYPOTHESIS |
| — | **NEW v3 additions below** | | | |
| 17 | HD-MAVP-1: Intrinsic PS density n(>M,z) KILLED — r=−0.10 to +0.08 для всех M_min | **CONFIRMED** | OUR_RECONSTRUCTION | commit 80c44a0, NR-005 |
| 18 | HD-MAVP-1: f_sel alone (zero physics) r=0.666 — воспроизводит 85% дисперсии M8-C | **CONFIRMED** | OUR_RECONSTRUCTION | commit 80c44a0, NR-005; SURVIVES_AS_ARTIFACT |
| 19 | M8-D: k_A(z) ∝ H(z)^(4/3) — монотонна по теореме; все MAVS anti-correlated (best r=−0.26) | **CONFIRMED** | OUR_RECONSTRUCTION | commit 9100b0a, NR-004 |
| 20 | ΛCDM f_DE монотонна (r=0.167); z_eq=0.296 — близко, но wrong shape | **CONFIRMED** | OUR_RECONSTRUCTION | commit 80c44a0 HD-MAVP-1 |
| 21 | AIC/BIC: ΔAIC=−16.65 (decisive), ΔBIC=−11.85 для MULTING vs ΛCDM IN-SAMPLE на Table A1 | **CONFIRMED** | TABLE_LEVEL_DIAGNOSTIC | commit 46277b9, reports/aic_model_comparison.json |
| 22 | LOO: LogNormal fit r=0.921, z_peak=0.603, 68% CI=[0.597, 0.681]; 0 high-leverage точек | **CONFIRMED** | OUR_RECONSTRUCTION | commit d1b5025, reports/loo_epsilon_analysis.json |
| 23 | TNG analytical: виральная k_A монотонна для всех M_min ∈ {1e14, 5e14, 2e15} M_sun | **CONFIRMED** | OUR_RECONSTRUCTION | commit d1b5025, NR-004 consistent |
| 24 | TNG analytical: merger rate proxy (Fakhouri 2008) r=+0.652, NON-MONOTONE, пик z=0.40 | **CONFIRMED** | OUR_RECONSTRUCTION | commit d1b5025; PARTIAL match с ε(z) primary peak |

---

## 2. OPEN — Открыто / требует ответа автора

| # | Question | Status | What closes it |
|--:|---|---|---|
| O1 | Есть ли у Buckholtz физический bridge (незаписанный явно)? | **OPEN** | Ответ TJB на Q1 |
| O2 | Какой настоящий bridge использовался для Table A1? | **OPEN / Q1** | Формула `F_oP → H_MULT(z)` от автора |
| O3 | Какие `D_C:AB(z)`, `k_A(z)`, `r_A(z)`, `r_P(z)` использовались? | **OPEN / Q2** | Расписание от автора |
| O4 | β — физические константы, author-selected или AI-fitted? | **OPEN / Q3** | Независимое правило для `β_d`, `β_q` |
| O5 | Может ли MULTING физически заменить Λ через дипольное отталкивание? | **OPEN** | Корректный Friedmann/Raychaudhuri bridge |
| O6 | Почему ε(z) пикует около z≈0.4? | **OPEN / SELECTION_AMBIGUITY** | Три конкурирующих объяснения; Q2 — единственный дискриминатор (см. docs/113 §9) |
| O7 | IDM = полноценная mirror-sector theory или только похожая идея? | **OPEN** | Автор должен уточнить конструкцию |
| O9 | Можно ли построить scale-dependent β, чтобы снять SC-6 tension? | **OPEN** | Механизм screening |
| O10 | Можно ли использовать Table A1 как prediction? | **DOUBTFUL / OPEN** | Нужен out-of-sample тест |
| O11 | Можно ли делать MCMC? | **BLOCKED / PARTIAL** | 1/5 blockers ✅ (AIC/BIC + LOO); Q1+Q2+Q3 → 0/5 core blockers |
| O12 | Можно ли проверять BBN / CMB / Bullet Cluster? | **BLOCKED** | Thermal history + interaction model |
| O13 | Можно ли публиковать сильные claims? | **NO / WAIT** | До ответа автора и полного re-audit |

> **O8 — удалён из OPEN.** Перемещён в REJECTED_AS_DERIVATION (см. § 3 ниже).

---

## 3. REJECTED_AS_CLAIM и REJECTED_AS_DERIVATION

| # | Statement | Status | Correct version |
|--:|---|---|---|
| R1 | "MULTING доказан как неверная теория" | **REJECTED — OVERCLAIM** | "Public materials do not yet support independent reproduction of Table A1." |
| R2 | "Мы опровергли Buckholtz" | **REJECTED — OVERCLAIM** | "We found reproducibility blockers and failures under our reconstruction." |
| R3 | "Формул в статье нет" | **REJECTED — FALSE** | Формулы сил есть; нет explicit bridge F→H(z) |
| R4 | "SC-2 gap ×4365 доказывает, что теория ложна" | **REJECTED — SCOPE ERROR** | Gap ×4365 = failure нашей реконструкции с public CSV + reconstructed bridge |
| R5 | "Claude bridge — это точно bridge автора" | **REJECTED — NOT_ESTABLISHED** | `AI_MEDIATED_BRIDGE_CANDIDATE`, not author-confirmed |
| R6 | "AI точно сгаллюцинировал Table A1" | **REJECTED — OVERCLAIM** | "AI-mediated bridge risk; Table A1 depends on unverified computational step" |
| R7 | "β_d=4.5 и β_q=18.0 — константы природы" | **REJECTED — NOT SUPPORTED** | Phenomenological / AI-assisted fit candidates пока |
| R8 | "5 dark isomers → 5:1 mass ratio (derivation)" | **REJECTED_AS_DERIVATION** | Sector count alone insufficient; 5 mechanisms missing (M7-C, baryogenesis, mass spectrum, freeze-out, entropy). Author text: "might suggest" — NOT derivation. [docs/114, NR-007] |
| R9 | "IDM проходит N_eff, потому что dark sectors невидимы" | **REJECTED — UNSUPPORTED** | Thermally populated sectors влияют на radiation density |
| R10 | "Local Group F5 окончательно убивает MULTING" | **REJECTED — OVERCLAIM** | Falsifies local dominance under our reconstruction, not author theory |
| R11 | "M8 доказал невозможность любого bridge" | **REJECTED — FALSE** | Merger proxy r=0.652 non-monotone — non-virial shapes exist |
| R12 | "Можно запускать MCMC прямо сейчас" | **REJECTED — BLOCKED** | MCMC_BLOCKED: нет bridge, likelihood, parameter provenance |
| R13 | "Можно делать публичный claim про ложное AI-научное знание" | **REJECTED — TOO EARLY** | Только reproducibility audit language |
| R14 | "ε пик при z=0.40 — подтверждённый selection artifact" | **REJECTED — OVERCLAIM** | Artifact SURVIVES as hypothesis; Q2 decisive. NOT confirmed. [docs/113] |
| R15 | "M8-C r=0.723 spurious или неверен" | **REJECTED — FALSE** | Значение верно; интерпретация ambiguous |
| R16 | "AIC/BIC ΔAIC=−16.65 доказывает MULTING out-of-sample" | **REJECTED — IN_SAMPLE_ONLY** | IN-SAMPLE на Table A1; out-of-sample blocked pending Q1 |

---

## 4. Сводка

| Категория | Количество | Суть |
|---|---|---|
| **CONFIRMED** | 24 | Bridge missing (Q1), ε non-monotone, MAVS/PS kills, f_sel artifact, AIC ΔAIC=−16.65, LOO z_peak=0.603, TNG merger r=0.652 |
| **OPEN** | 12 | Q1/Q2/Q3 from TJB; O6 SELECTION_AMBIGUITY; O11 PARTIAL |
| **REJECTED** | 16 | Overclaims, scope errors, R8=REJECTED_AS_DERIVATION |

---

## 5. Формула проекта (каноническая, v3)

```
CONFIRMED:
  По публичным материалам Table A1 пока не воспроизводится независимо (Q1 MISSING).
  ε(z) немонотонна; пик z=0.40 ambiguous: три конкурирующих объяснения (docs/113 §9).
  Intrinsic PS formation KILLED. f_sel artifact SURVIVES. Merger rate NON-MONOTONE (r=0.652).
  AIC/BIC: decisive IN-SAMPLE; LOO: LogNormal z_peak=0.603 robust.

OPEN:
  Авторский bridge / schedule / β canonical values — только TJB закрывает.
  O6 SELECTION_AMBIGUITY: selection vs intrinsic vs bridge artifact — Q2 decisive.

REJECTED:
  "MULTING refuted" · "AI всё сгаллюцинировал" · "gap=refutation"
  "5 изомеров → 5:1 автоматически" (REJECTED_AS_DERIVATION)
  "AIC/BIC доказывает MULTING out-of-sample"
```

---

## 6. O6 Ambiguity — Краткая карта (из docs/113)

| Explanation | Signal | Status |
|-------------|--------|--------|
| H1: Intrinsic PS formation | r=−0.10 to +0.08 | **KILLED** |
| H2: Observed selection / schedule | r=0.666–0.773 | **SURVIVES / PARTIAL** |
| H3: Bridge functional-form artifact | not independently tested | **OPEN** |
| H4: ΛCDM f_DE transition mimicry | r=0.167, wrong shape | **WEAK / KILLED** |

**Q2 is the ONLY discriminator. Correct: "peak is ambiguous; Q2 decisive."**

---

## 7. MCMC Blockers — состояние v3

| Blocker | Status | Required |
|---------|--------|----------|
| 1a. Bridge method | ❌ MISSING | Author answer Q1 |
| 1b. Operational meaning | ❌ UNCLEAR | Author answer Q1 |
| 2. Cluster variables schedule | ❌ MISSING | Author answer Q2 |
| 3. Independent data | ❌ MISSING | Integrate Pantheon+ or BAO |
| 4. Complexity penalty | ✅ PARTIAL | AIC/BIC (commit 46277b9) + LOO z_peak CI (commit d1b5025) — IN-SAMPLE only |

**0/4 core blockers (1a,1b,2,3) resolved. Until all resolved: MCMC = BLOCKED.**

---

## 8. Gate Chain (полный, v3)

| Gate | Verdict | Commit |
|---|---|---|
| M2-G4 β non-identifiability | PASS | 91ea667 |
| M7-A Eq31 mass-ratio | PARTIAL | 3b128dd |
| M7-B 5:1 dark isomer ratio | PARTIAL | e624bd3 |
| M7-C N_eff thermal history | BLOCKED | 9ebd05c |
| SC-6/F5 LG anomaly | FALSIFIED-LOCAL | — |
| AB-2 Author email | SENT | 9513289 |
| EOD-1 Evidence Lock | PASS | 397575c |
| M7-C2 Mirror DM N_eff | IF_MIRROR · BLOCKED | 6c64253 |
| M8-A Bridge Derivation | CONFIRMED | 30473a2 |
| M8-A-R1 Adversarial Re-Audit | PASS | add7cba |
| EOD-2 Evidence Lock | PASS | docs/107 |
| M8-C Closure Schedule | PARTIAL / HYPOTHESIS | d1638d4 |
| EOD-3 Claim Status Matrix v2 | PASS | docs/108 |
| M8-D MAVS Virial+PS | FAIL | 9100b0a |
| EOD-4 Post-M8D Evidence Lock | PASS | docs/109 |
| HD-MAVP-1 Cluster Audit | PARTIAL-KILL | 80c44a0 |
| Post-HD-MAVP Lock | PASS | docs/113 |
| O7 Isomer Ratio Lock | REJECTED_AS_DERIVATION | docs/114 |
| BETA-1 Hold | INFRA_READY / HOLD | docs/115 |
| AIC/BIC Model Comparison | PARTIAL (IN-SAMPLE) | 46277b9 |
| LOO Leverage + TNG Proxy | PASS | d1b5025 |
| **EOD-5 Claim Status Matrix v3** | **PASS** | **this file** |

---

## 9. Active Gates and STOP State

```
ACTIVE GATES:  NONE

HOLD (requires explicit approval):
  HD-MAVP-2:  HOLD — requires Q1+Q2 (not authorized)
  M8-B:       LOW PRIORITY — Φ-normalization forensic
  BETA-1:     HOLD — controlled AI β replication (docs/115)

STOP — awaiting TJB response
  Email sent: 2026-06-12 (Q1, Q2, Q3)
  Earliest follow-up: 2026-06-18
  No new gates until TJB responds OR explicit user approval

IF TJB answers Q1+Q2:
  → Unlock bridge implementation
  → Resolve O6 ambiguity (intrinsic vs selection vs artifact)
  → Unlock MCMC design
  → LogNormal z_peak=0.603 becomes testable against author k_A(z)

IF TJB answers Q3:
  → Update β status, potentially unlock modeling

IF no reply by ~2026-07-12:
  → Consider archiving as AUTHOR_DECLINED_DETAIL
```

---

**SESSION START PROTOCOL (next session):**
1. Check email — TJB reply?
2. Read docs/112 (master lock) + docs/113 (HD-MAVP-1) + docs/116 (this file)
3. No new gates without explicit approval

---

*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*  
*NOT_THEORY_FALSE · NOT_AI_HALLUCINATION_CLAIM · NOT_FABRICATION_CLAIM*  
*EOD-5 gate closed 2026-06-13 · docs/116_claim_status_matrix_v3.md*
