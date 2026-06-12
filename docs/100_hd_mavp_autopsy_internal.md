# HD-MAVP Autopsy Report — Internal Diagnostic
## Buckholtz IDM/MULTING (preprints202511.0598.v6)

**Создан:** 2026-06-12  
**Методология:** HD-MAVP v3.9.0 (режим Math_Code + Contradiction) + Falsification Ladder Full  
**Тип проекта:** RESEARCH — EstimandOps L0 + FL Full-Ladder  
**Арсенал:** Claude-cod-top-2026 v3.9.0

```
SAFETY LABELS (HARD):
  NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_ERROR
  INTERNAL_DIAGNOSTIC_ONLY · AUTHOR_CLARIFICATION_REQUIRED
  MCMC_BLOCKED (0/5 blockers resolved)
  NO_EMAIL_WITHOUT_APPROVAL · NO_PUBLIC_CLAIMS
```

---

## EXECUTIVE SUMMARY

Цель: установить, воспроизводимы ли таблицы препринта независимо от автора.

**Вердикт текущий (2026-06-12):**
> Мы не доказали и не опровергли MULTING как физическую теорию.
> Мы установили: наша реконструкция Table A1 расходится с заявленными значениями
> на ×4365 при z=8.5. Причина — отсутствие авторской bridge-формулы F→H(z).
> AI-сервис заполнил этот зазор неявно. Без ответов TJB на Q1–Q3 —
> независимое воспроизведение невозможно.

---

## БЛОК ТЕКУЩЕГО СОСТОЯНИЯ

| Параметр | Значение |
|---|---|
| Verified baseline (SC-2 gap) | ×4365 [VERIFIED-tool 2026-06-12] |
| SC-1 ratio | H_MULT = 1.074 × H_FLRW, scatter 2.6% |
| SC-4 dipole | ε_d < 10⁻³ at ALL z (our reconstruction) |
| **SC-6 (F5)** | **ε_d = 3.1×10⁻⁷ at LG scale (β_d=4.5). β_d needed for ε_d=1: 14.6M. [VERIFIED-tool 2026-06-12]** |
| Bridge status | NOT_IN_PREPRINT — AI-implicit H²∝Φ/Φ₀ |
| β_d, β_q | 4.5 / 18.0 — AI-fitted, NOT first principles |
| TJB last contact | 2026-05-30 (reproducibility plan sent) |
| Next contact | NOT BEFORE 2026-06-18 |
| MCMC | BLOCKED (0/5 resolved) |

---

## ЧАСТЬ I — АВТОПСИЯ: ТЕКУЩИЕ НАХОДКИ

### Легенда статусов
- `[FALSIFIED-LOCAL]` — опровергнуто под нашей реконструкцией (не авторской)
- `[BLOCKER]` — зазор, требующий ответа автора
- `[MCMC_BLOCKED]` — тест заблокирован до разрешения BLOCKER
- `[PARTIAL]` — частично подтверждено / частично опровергнуто
- `[OPEN]` — не тестировалось, нет данных
- `[VERIFIED-tool]` — подтверждено инструментом

### Namespace Note (EC-1 Guardrail 2026-06-12)
**SC-1…SC-5** = Self-Consistency Diagnostics (из `audit/self_consistency_diagnostic.py`).
**M1…M8** = Playbook Modules (M1 Force Law, M2 Bridge Gap, M7 Dark Matter…).
Эти два namespace НЕ взаимозаменяемы. SC-блоки — числовые диагностики;
M-блоки — структурные модули анализа. Не использовать M1–M5 для обозначения SC-блоков.

### Guardrails (EC-1 2026-06-12)
```
agent-verified из предыдущей сессии = [INFERRED] в текущей сессии
  → требует tool-верификации через Bash/Read/Grep перед использованием.
[FALSIFIED-LOCAL] ≠ [REFUTED]
  → скоп всегда: наша реконструкция + наши CSV-параметры.
[FALSIFIED-LOCAL] ≠ "MULTING опровергнут"
  → автор не подтвердил параметры и bridge. Q1-Q3 для TJB не заданы.
```

---

| # | Атом (ядро гипотезы) | Входные данные / Момент старта | Скрытое допущение (где спрятана ложь) | Kill Condition (критерий фальсификации) | Методология / Угол | Проделанная работа (как ломали) | Результат / Доказательство | Статус | Интерпретация / Жемчужина |
|---|---|---|---|---|---|---|---|---|---|
| **A0** | **Bridge F_oP → H(z)** | Eq. 17 (F_oP) + Table A1 H_MULT(z) | Автор математически вывел H(z) из уравнений сил | Отсутствие явной формулы моста ИЛИ расхождение >10× | Code & Data Audit: обратный инжиниринг через логи AI-сервиса | Прочитан Appendix A.1 pp.32–36; искали bridge в Step 5 | **Blocker-1:** Формулы сил F_m/F_d/F_q присутствуют (Step 2 Guidelines, p.33). Bridge F→H(z) = формула H²∝Φ/Φ₀ в препринте отсутствует. AI-сервис использовал её неявно. (AUTHOR_BRIDGE_NEEDED) | `[BLOCKER]` | H(z) — AI-аппроксимация, не физический вывод. Q1 для TJB: какой переход F→H предполагался? |
| **A1** | **Базовая самосогласованность** | CSV cluster params (Claude Supplementary) + восстановленная bridge H²∝Φ/Φ₀ | При подстановке реальных D(z) Φ(z) воспроизводит таблицу | H_pred(z) ≠ H_MULT(z) с разрывом >10× | Asymptotic analysis: прямой пересчёт на z=8.5 с нашими params | Прогнан `self_consistency_diagnostic.py`: Φ(z=8.5)/Φ(0) = 2e⁻⁶ | **SC-2 [VERIFIED-tool]:** H_pred=0.096 vs H_MULT=418.1. Gap ×4365. Robust: arith_mean → ×3944 | `[FALSIFIED-LOCAL]` | **Pearl #1:** Наши CSV params → H падает. Авторские params неизвестны. Разрыв = missing D(z)-schedule. Q2 для TJB |
| **A2** | **Механизм MULTING: диполь доминирует** | Заявление Step 5: "ensure dipole dominates at low z" + CSV params | k_A достаточна для F_d > F_m хотя бы при малых z | ε_d = F_d/F_m < 1 на ВСЕХ z (при наших CSV-параметрах, OUR_RECONSTRUCTION) | Dimensional & Magnitude estimation: расчёт ε_d по 12 точкам | Part D `self_consistency_diagnostic.py`: ε_d вычислен для всех z | **SC-4 [VERIFIED-tool]:** max ε_d ≈ 10⁻³. Dipole does NOT dominate under our params. Step 5 instruction not reproduced under our reconstruction. (NOT_AUTHOR_CONFIRMED) | `[FALSIFIED-LOCAL]` | D_crossover для ε_d=1 при z=0: нужно D≈0.0003 Mpc. Реальный D=44.7 Mpc. Scope: наша реконструкция. AUTHOR_BRIDGE_NEEDED |
| **A3** | **β параметры: физический смысл** | β_d=4.5, β_q=18.0 (Table A1 caption) | β имеют фундаментальное физическое происхождение | β не выводятся из первых принципов / требуют подгонки под каждую эпоху | Source check: аудит происхождения констант | Анализ переписки TJB (2026-05-30): "beta phenomenological (fitted, may or may not be fundamental)" | **Blocker-3:** TJB сам подтвердил — β феноменологические. AI-сервис минимизировал σ от H(z) | `[BLOCKER]` | **Pearl #2:** H_MULT ≈ 1.074 × H_FLRW `[SC-1 / OUR_OBSERVATION / TABLE_LEVEL_DIAGNOSTIC]`. Circular fit: β обучен на H(z) → имитирует H(z). Q3: есть ли предсказание β из first principles? |
| **A4** | **H_MULT vs наблюдения: качество фита** | Table A1: σ_MULT < 0.4 на всём диапазоне z | Качество фита = независимое подтверждение теории | σ_MULT статистически не лучше β-оптимизированного ΛCDM | Model selection: BIC-сравнение | SC-1: H_MULT = 1.074×H_FLRW. Ratio не константа: 1.024–1.108 (структурированный остаток) | **SC-1 [VERIFIED-tool]:** r=0.99959. Это near-trivial (монотонные кривые всегда коррелируют ~0.999). BIC не посчитан | `[PARTIAL]` | Хороший фит ≠ независимая физика. Нужен BIC + out-of-sample тест. Без bridge — in-sample только |
| **A5** | **Внешние тесты (BBN / PPN / Bullet Cluster)** | IDM 5 изомеров + локальная гравитация | Теория внутренне согласована и готова к внешним данным | Нарушение BBN (N_eff), орбит (PPN), столкновений (Bullet) | Всё заблокировано до SC-2 + A0 resolved | Не начато: нет смысла пока bridge неизвестен | — | `[MCMC_BLOCKED]` | Freeze all astro simulations. Внутренний разрыв ×4365 делает внешние тесты бессмысленными |

---

## ЧАСТЬ II — ПЛАН БУДУЩИХ ТЕСТОВ (заблокированные / открытые)

| # | Тест | Зависит от | Unlock условие | Методология | Ожидаемый результат | Статус |
|---|---|---|---|---|---|---|
| **F1** | Воспроизведение Table A1 с авторским D(z) | Q2 TJB ответ | TJB раскрывает D(z)-schedule | Подставить авторский D(z) в `self_consistency_diagnostic.py` | Gap ×4365 → должен упасть до <1.1× | `[WAITING_TJB]` |
| **F2** | Вывод bridge из уравнений TJB | Q1 TJB ответ | TJB даёт явную формулу F→H | Аналитическая деривация + numerical check | Должна совпасть с H²∝Φ/Φ₀ или дать новую формулу | `[WAITING_TJB]` |
| **F3** | BIC vs ΛCDM | F1 разблокирован | SC-2 resolved | Байесовский information criterion: MULTING(2 params) vs ΛCDM(6) | Если BIC_MULT > BIC_ΛCDM → предпочтительнее ΛCDM | `[BLOCKED_F1]` |
| **F4** | Out-of-sample предсказание | F1 + F2 resolved | Bridge + correct params | Предсказать H(z) вне Table A1 (z=9, z=10, z=12) | Должны совпасть с данными независимо от β-фита | `[BLOCKED_F2]` |
| **F5** | Local Group anomaly | НЕ заблокирован | Нет зависимостей | Расчёт F_d между MW и Andromeda при β_d=4.5 | Если dipole доминирует при z≈0 → MW/Andromeda должны отталкиваться. Факт: они сближаются | `[OPEN — CAN RUN NOW]` |
| **F6** | IDM 5:1 ratio vs UDG каталог | F1 resolved | Bridge известен | Проверка: UDG Dragonfly 44 (DM-only), NGC 1052-DF2 (no DM) | Жёсткое 5:1 ratio не может объяснить 1000:1 или 0:1 | `[BLOCKED_F1]` |
| **F7** | Dark neutron stability: CPT check | F2 resolved | Физический механизм понят | Проверка: изменение масс лептонов → нарушение CPT? | Fine-tuning без обоснования → falsified | `[BLOCKED_F2]` |
| **F8** | β_q evolution: постоянство со временем | Q3 TJB ответ | TJB о физике β | Проверить: одинаково ли β_q для разных AI-сервисов | Claude β_q=18.0, Gemini β_q=8.10 → уже расходятся | `[PARTIAL — уже видно]` |

---

## ЧАСТЬ III — СМЕРТЕЛЬНЫЕ ВОПРОСЫ ДЛЯ TJB

*(Одобрение перед отправкой: NO_EMAIL_WITHOUT_APPROVAL)*

| Q# | Вопрос | Основание (SC-код) | Тип | Unlock |
|---|---|---|---|---|
| **Q1** | Какая явная формула перехода F_oP → H(z) предполагалась в Step 5? H²∝Φ/Φ₀ в тексте отсутствует. | SC-3, Blocker-1 | Bridge | A0, F2 |
| **Q2** | Какой D_C:AB(z)-schedule использовался AI-сервисом? Наши CSV geometric means → H_pred=0.096 vs H_MULT=418.1 (gap ×4365 при z=8.5) | SC-2, Blocker-2 | Reproducibility | A1, F1 |
| **Q3** | Есть ли физически выводимое предсказание β_d, β_q из первых принципов — независимо от фита к H(z)? Иначе: чем MULTING отличается от ΛCDM с 2 свободными параметрами? | SC-1, SC-4, Blocker-3 | Falsifiability | A3, F3, F4 |
| **Q4** *(опциональный)* | Local Group: если диполь доминирует при z≈0, почему Андромеда приближается к Млечному Пути, а не удаляется? | F5, Red Team A2 | Mechanism | F5 |

---

## ЧАСТЬ IV — PEARL REGISTRY

*(Ценные находки независимо от истинности теории)*

| Pearl # | Название | Инсайт | Применение | Testable prediction |
|---|---|---|---|---|
| **P1** | Reproducibility-First Rule | Проверяй числовую воспроизводимость ДО анализа физического смысла. Разрыв ×4365 обнаружен за 1 день аудита | Любой препринт с таблицами без открытого кода | "Если нет кода — нет физики" |
| **P2** | AI-β Circular Fit | β, подобранное AI под H(z), создаёт H_MULT ≈ 1.074×H_FLRW. Это не независимое подтверждение — это in-sample имитация | Любое использование AI для подгонки параметров теории | BIC должен штрафовать MULTING vs ΛCDM |
| **P3** | Bridge Hallucination Pattern | AI-сервис изобрёл H²∝Φ/Φ₀ чтобы заполнить зазор в Step 5 — и эта формула выглядит как авторская. Без аудита кода — незаметно | Паттерн для других "AI-assisted" препринтов | Проверяй: есть ли bridge в тексте или только в AI-выходе? |
| **P4** | Multi-AI Disagreement = Model Instability | Claude β_q=18.0, Gemini β_q=8.10. Расхождение AI-сервисов → модель не имеет уникального решения | Любая модель с β-подгонкой | Если разные AI дают разные β → нет uniqueness |
| **P5** | Data-Driven H(z) fitting (независимо от MULTING) | Попытка описать H(z) без FLRW-метрики — ценная альтернативная методология | Data-driven cosmology | Сравнение BIC: MULTING vs Gaussian Process fit vs ΛCDM |

---

## ЧАСТЬ V — EVIDENCE INVENTORY

*(Все verified числа — source of truth)*

| Метрика | Значение | Метод | Дата | SC-код |
|---|---|---|---|---|
| H_MULT/H_FLRW mean ratio | 1.0736 | `self_consistency_diagnostic.py` Part B | 2026-06-12 | SC-1 |
| Scatter ratio | 2.6% | Part B | 2026-06-12 | SC-1 |
| corr(H_MULT, H_FLRW) | 0.99959 | Part B | 2026-06-12 | SC-1 |
| Φ(z=8.5)/Φ(0) | 0.000002 | Part A | 2026-06-12 | SC-2 |
| H_pred(z=8.5) | 0.096 km/s/Mpc | Part A | 2026-06-12 | SC-2 |
| Gap vs reported | ×4365 | Part A | 2026-06-12 | SC-2 |
| Gap (arith_mean) | ×3944 | Part F | 2026-06-12 | SC-5 |
| max ε_d (all z) | ~10⁻³ | Part D | 2026-06-12 | SC-4 |
| β_d (Claude AI) | 4.5 | Table A1 caption | — | Blocker-3 |
| β_q (Claude AI) | 18.0 | Table A1 caption | — | Blocker-3 |
| β_d (Gemini AI) | 4.25 | Supplementary CSV | — | SC-5/F8 |
| β_q (Gemini AI) | 8.10 | Supplementary CSV | — | SC-5/F8 |

---

## ИНСТРУКЦИЯ ПО ОБНОВЛЕНИЮ

```
Когда обновлять:
  — При каждом новом SC-verified result → PART I + PART V
  — При ответе TJB → PART II Unlock columns + ЧАСТЬ III
  — При новом pearl → PART IV
  — При запуске нового теста → PART II статус

Не делать:
  — Менять статус [VERIFIED-tool] на слабее без перезапуска скрипта
  — Добавлять [FALSIFIED] без scope qualifier (local/global)
  — Удалять [MCMC_BLOCKED] до решения ALL 5 blockers
```

---

## SC-6: F5 LOCAL GROUP ANOMALY — РЕЗУЛЬТАТ [VERIFIED-tool 2026-06-12]

**Данные (источники):**
- m_MW = 1.0e12 M_sun [Bland-Hawthorn+2016], m_M31 = 1.5e12 M_sun [Tamm+2012]
- r_virial_MW = 0.21 Mpc [Deason+2020], r_virial_M31 = 0.22 Mpc [Tamm+2012]
- r_sep = 0.785 Mpc [van der Marel+2012]
- σ_internal = 150 km/s (обе галактики) → k_A/c² = 1.25e5 M_sun (MW), 1.88e5 M_sun (M31)
- Наблюдаемое движение: v_radial = −109 km/s (СИНЯЯ ЛИНИЯ = приближаются)

**Результаты [VERIFIED-tool 2026-06-12]:**

| Сценарий | β_d | ε_d = F_d/F_m | ε_q = F_q/F_m |
|---|---|---|---|
| A: Table A1 (β_d=4.5) | 4.5 | **3.1×10⁻⁷** | 3.8×10⁻¹³ |
| B: Pure geometry (β=1) | 1.0 | 6.9×10⁻⁸ | 1.2×10⁻¹⁵ |
| C: β_d needed for ε_d=1 | **14,585,185** | 1.0 | — |

**β_d нужен ×3,241,152 больше чем 4.5 для доминирования диполя при LG**

**Cluster cross-check (тот же β):**

| β_d | ε_d при LG | ε_d при кластере (z=0) |
|---|---|---|
| 4.5 | 3.1×10⁻⁷ | 1.1×10⁻³ |
| 14,585,185 | 1.0 | **3573** |

### SC-6 РЕЗУЛЬТАТ: DIPOLE NOT REPRODUCED AT LG SCALE [FALSIFIED-LOCAL — OUR_RECONSTRUCTION]

```
Путь 1: β_d=4.5  → ε_d=3×10⁻⁷ при LG
         Отталкивание в 3,240,000 раз слабее гравитации.
         Диполь не доминирует при LG-масштабе под нашими параметрами (SC-4 расширен до LG).
         Приближение MW→M31 консистентно (гравитация побеждает),
         но диполь при β_d=4.5 не достигает доминирования при LG под нашими params.
         (OUR_RECONSTRUCTION — автор мог использовать другой k_A(z) schedule.)

Путь 2: β_d=14.6M → ε_d=1 при LG
         НО: ε_d=3573 при кластере → Table A1 H(z) полностью разрушен.
         Нет единственного β_d, удовлетворяющего обоим условиям.
```

**Статус:** `[FALSIFIED-LOCAL]` — скоп: наша реконструкция + данные LG  
**Scope qualifier:** Автор может использовать другой k_A(z) schedule. Q15 для TJB остаётся.

---

*Документ живой. Обновлять по ходу сессий.*  
*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*
