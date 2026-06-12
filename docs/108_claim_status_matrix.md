# docs/108 — Claim Status Matrix

**Date:** 2026-06-12  
**Gate:** Post-M8C Claim Status Lock  
**Replaces:** docs/107 (adds M8-C results + status upgrades)

```
SAFETY LABELS (HARD):
  NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_MODEL_FALSIFICATION
  INTERNAL_DIAGNOSTIC_ONLY · OUR_RECONSTRUCTION
  NO_EMAIL_BEFORE_2026-06-18 · NO_PUBLIC_CLAIMS · NO_MCMC
```

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
| 1 | Формулы сил `F_m`, `F_d`, `F_q`, `F_oP` присутствуют в препринте | **CONFIRMED** | AUTHOR_MODEL | Прямое чтение препринта; мы не говорим "формул нет" |
| 2 | Явный author-confirmed bridge `F_oP → H_MULT(z)` не найден в публичных материалах | **CONFIRMED BLOCKER** | AUTHOR_MODEL | Главный воспроизводимостный блокер Table A1 (Q1) |
| 3 | Step 5 использует логику "fit H(z)", а не строго "compute H(z)" | **CONFIRMED / HIGH-SIGNAL** | OUR_RECONSTRUCTION | Анализ AI-bridge gap; разные AI сервисы дают разные β |
| 4 | Claude, Gemini, ChatGPT дают разные `β_d`, `β_q` | **CONFIRMED** | OUR_RECONSTRUCTION | Multi-AI CSV comparison (docs/73) |
| 5 | `β_d`, `β_q` — phenomenological / AI-assisted fitting coefficients при текущих данных | **CONFIRMED-AS-CURRENT-INTERPRETATION** | OUR_RECONSTRUCTION | Пока нет независимого правила вывода β без подгонки к H(z) |
| 6 | M2-G4: под reconstructed Claude bridge β-параметры не идентифицируются из Table A1 | **CONFIRMED** | OUR_RECONSTRUCTION | Fisher/rank: кривая задаётся anchor/schedule, а не β |
| 7 | Table A1: сильный паттерн `H_MULT ≈ scaled H_FLRW` (ε(z) ≠ const, но мало) | **CONFIRMED** | TABLE_LEVEL_DIAGNOSTIC | ε(z) = (H_MULT/H_FLRW)² − 1 вычислена по всем 11 точкам |
| 8 | SC-2: наша реконструкция даёт gap ×4365 при z=8.5 | **CONFIRMED** | OUR_RECONSTRUCTION | Не refutation theory; доказывает failure OUR bridge |
| 9 | F5/Local Group: при наших параметрах `F_d/F_m ≈ 3×10⁻⁷` (в ~3.3M× слабее гравитации) | **CONFIRMED** | OUR_RECONSTRUCTION | С β_d=4.5; falsifies local dominance under our reconstruction |
| 10 | M7-A Eq31 `7:9:17` численно близко, derivation отсутствует | **PARTIAL CONFIRMED** | AUTHOR_MODEL | Численная близость есть; физическая теорема не выведена |
| 11 | M7-C: `ΔN_eff` для IDM нельзя вычислить из препринта | **CONFIRMED BLOCKED** | AUTHOR_MODEL | Нет T_dark/T_visible, decoupling, thermal history, relativistic species count |
| 12 | Mirror DM: если IDM ≈ mirror sectors, нужен холодный dark sector (`T_dark/T_SM < ~0.27–0.37`) | **CONFIRMED CONDITIONAL** | CONDITIONAL_BENCHMARK | При равной температуре ΔN_eff=22–81 → 130–477σ над Planck |
| 13 | ε(z) = (H_MULT/H_FLRW)² − 1 немонотонна; пик ε=0.2277 при z=0.40; минимум ε=0.0481 при z=5.0 | **CONFIRMED** | TABLE_LEVEL_DIAGNOSTIC | M8-A + M8-A-R1 adversarial re-audit (commit add7cba): все 11 значений независимо верифицированы |
| 14 | Простая constant-ε и power-law bridge не объясняют Table A1; secondary structure z=1.0–1.5 тоже | **CONFIRMED** | OUR_RECONSTRUCTION | M8-A + M8-A-R1 (PASS) + M8-C подтверждают |
| 15 | Письмо Q1–Q3 TJB отправлено 2026-06-12 | **CONFIRMED** | CONFIRMED_OPERATIONAL | Commit 9513289; ответ ожидается не ранее 2026-06-18 |
| 16 | M8-C: Survey count rate dN/dz пикует вблизи z=0.40–0.65 при подходящем M_min; вторичная структура не объяснена | **PARTIAL / CONFIRMED** | OUR_RECONSTRUCTION | Лучший Pearson r=0.723 (M_min=1e14); пик на z=0.40 при M_min=5e14. Verdict PARTIAL, <HYPOTHESIS> |

---

## 2. OPEN — Открыто / требует ответа автора

| # | Question | Status | What closes it |
|--:|---|---|---|
| 1 | Есть ли у Buckholtz физический bridge в голове, но незаписанный явно? | **OPEN** | Ответ TJB на Q1 |
| 2 | Какой настоящий bridge использовался для Table A1? | **OPEN / Q1** | Формула `F_oP / Φ / A_m,A_d,A_q → H_MULT(z)` от автора |
| 3 | Какие `D_C:AB(z)`, `k_A(z)`, `r_A(z)`, `r_P(z)` использовались? | **OPEN / Q2** | Таблицы или schedule от автора |
| 4 | β — физические константы, author-selected или AI-fitted? | **OPEN / Q3** | Независимое правило для `β_d`, `β_q` |
| 5 | Может ли MULTING физически заменить Λ через дипольное отталкивание? | **OPEN** | Корректный Friedmann/Raychaudhuri bridge |
| 6 | Почему ε(z) пикует около z≈0.4? | **OPEN / PARTIAL_EVIDENCE** | M8-C: dN/dz пикует там же при M_min=5e14 (r=0.541); qualitative only. Нужен k_A(z) для количественного ответа |
| 7 | IDM = полноценная mirror-sector theory или только похожая идея? | **OPEN** | Автор должен уточнить: полные mirror sectors или другая конструкция |
| 8 | Почему 5 изомеров дают именно Ω_DM/Ω_b ≈ 5? | **OPEN** | Baryogenesis / asymmetry / thermal history / mass spectrum |
| 9 | Можно ли построить scale-dependent / screened β, чтобы снять SC-6 tension? | **OPEN** | Механизм screening: chameleon/symmetron/Vainshtein или авторский |
| 10 | Можно ли использовать Table A1 как prediction? | **DOUBTFUL / OPEN** | Нужен out-of-sample test: точки, не участвовавшие в fit |
| 11 | Можно ли делать MCMC? | **BLOCKED** | Нет bridge и likelihood definition (Q1+Q2) |
| 12 | Можно ли проверять BBN / CMB / Bullet Cluster полноценно? | **BLOCKED** | Нужны thermal history и interaction model |
| 13 | Можно ли публиковать сильные claims? | **NO / WAIT** | До ответа автора и полного re-audit — нельзя |

---

## 3. REJECTED_AS_CLAIM — Неверно / нельзя так утверждать

| # | Statement | Status | Correct version |
|--:|---|---|---|
| 1 | "MULTING доказан как неверная теория" | **REJECTED — OVERCLAIM** | "Public materials do not yet support independent reproduction of Table A1." |
| 2 | "Мы опровергли Buckholtz" | **REJECTED — OVERCLAIM** | "We found reproducibility blockers and failures under our reconstruction." |
| 3 | "Формул в статье нет" | **REJECTED — FALSE** | Формулы сил есть; нет explicit bridge F→H(z) |
| 4 | "SC-2 gap ×4365 доказывает, что теория ложна" | **REJECTED — SCOPE ERROR** | Gap ×4365 доказывает failure OUR reconstruction с public CSV + reconstructed bridge |
| 5 | "Claude bridge — это точно bridge автора" | **REJECTED — NOT_ESTABLISHED** | Это `AI_MEDIATED_BRIDGE_CANDIDATE`, not author-confirmed |
| 6 | "AI точно сгаллюцинировал Table A1" | **REJECTED — OVERCLAIM** | "AI-mediated bridge risk; Table A1 depends on unverified computational step" |
| 7 | "β_d=4.5 и β_q=18.0 — константы природы" | **REJECTED — NOT SUPPORTED** | Phenomenological / AI-assisted fit candidates пока |
| 8 | "5 dark isomers автоматически дают 5:1 mass ratio" | **REJECTED — FALSE AS DERIVATION** | Sector count alone insufficient; нужны temperature, asymmetry, masses, entropy history |
| 9 | "IDM проходит N_eff, потому что dark sectors невидимы" | **REJECTED — UNSUPPORTED** | Thermally populated sectors влияют на radiation density независимо от "видимости" |
| 10 | "Mirror DM audit закрывает M7-C полностью" | **REJECTED — SCOPE ERROR** | Даёт conditional benchmark; author-model N_eff всё ещё blocked |
| 11 | "Local Group F5 окончательно убивает MULTING" | **REJECTED — OVERCLAIM** | Falsifies local dominance under our reconstruction, not author theory |
| 12 | "M8 доказал невозможность любого bridge" | **REJECTED — FALSE** | M8-C: PARTIAL support for survey dN/dz. Нужен k_A(z) schedule |
| 13 | "Можно запускать MCMC прямо сейчас" | **REJECTED — BLOCKED** | MCMC_BLOCKED: нет bridge, likelihood, parameter provenance |
| 14 | "Можно делать публичный claim про ложное AI-научное знание" | **REJECTED — TOO EARLY** | Только reproducibility audit language; author-unconfirmed AI-mediated risk |

---

## 4. Сводка

| Категория | Что входит | Сила |
|---|---|---|
| **CONFIRMED** | Нет опубликованного bridge, разные β, failure нашей реконструкции, N_eff blocker, Local Group force hierarchy, Mirror conditional constraint, ε(z) non-monotonic | Сильная evidence-base |
| **OPEN** | Авторский bridge, schedules, β provenance, 5:1 physical derivation, thermal history, scale-dependent β, cluster-formation bridge | Требует TJB или новых gates |
| **REJECTED** | "теория ложна", "AI всё сгаллюцинировал", "gap=refutation", "5 изомеров → 5:1 автоматически", "можно MCMC" | Overclaim / methodological error |

---

## 5. Формула проекта (каноническая)

```
CONFIRMED:
  По публичным материалам Table A1 пока не воспроизводится независимо.
  Простые bridge-кандидаты (constant, power law) не объясняют ε(z) форму.
  Press-Schechter survey rate качественно совпадает с пиком ε (PARTIAL/HYPOTHESIS).

OPEN:
  Возможно, у автора есть неоформленный bridge / schedule / physical intuition.
  Вероятность отсутствия любой авторской bridge formula: ~70-80% [INFERRED].
  Chain: TJB ответил позитивно + не опровергает вопросы →
  автор не обязательно не имеет bridge в голове.

REJECTED:
  Утверждать, что мы уже опровергли MULTING.
  Утверждать, что мы доказали AI-фальсификацию.
```

---

## 6. Gate Chain (полный)

| Gate | Verdict | Commit |
|---|---|---|
| M2-G4 β non-identifiability | PASS | 91ea667 |
| M7-A Eq31 mass-ratio | PARTIAL | 3b128dd |
| M7-B 5:1 dark isomer ratio | PARTIAL | e624bd3 |
| M7-C N_eff thermal history | BLOCKED | 9ebd05c |
| SC-6/F5 LG anomaly | FALSIFIED-LOCAL | 2026-06-12 |
| AB-2 Author email | SENT | 9513289 |
| EOD-1 Evidence Lock | PASS | 397575c |
| M7-C2 Mirror DM N_eff | IF_MIRROR · BLOCKED | 6c64253 |
| M8-A Bridge Derivation | CONFIRMED (post-reaudit) | 30473a2 |
| M8-A-R1 Adversarial Re-Audit | PASS (4 corrections) | add7cba |
| EOD-2 Evidence Lock | PASS | (docs/107) |
| M8-C Closure Schedule | PARTIAL / <HYPOTHESIS> | d1638d4 |
| **EOD-3 Claim Status Matrix** | **PASS** | this file |

---

*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*  
*EOD-3 gate closed 2026-06-12 · Next: M8-B or wait TJB (not before 2026-06-18)*
