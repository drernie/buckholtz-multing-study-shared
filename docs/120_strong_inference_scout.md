# docs/120 — Strong Inference Scout: MULTING/IDM
# Prepared: 2026-06-17
# NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
# Related: docs/119_weaknesses_referee_map.md, docs/118_journal_readiness_section_draft.md

---

## 1. Scope & Null Model

**Объясняем:** Жизнеспособность фреймворка MULTING/IDM как альтернативы или дополнения к ΛCDM.

**Не входит:** Философские дискуссии о «paradigm shifts»; исторические аналогии; AI-промпты как доказательства.

**Единица анализа:** Каждый из 36 пунктов препринта + 3 новых уязвимости (A-5a/b/c, cold/small).

**Доступные данные:** MCXC+CC (443 кластера), XMM (23 кластера), PDG 2024, Planck 2018 (N_eff), Bullet Cluster (σ/m), Boyko reconstruction (2026-06-17).

**Критерий успеха:** Гипотеза выживает, если проходит kill-test; не выживает — если убита данными или логикой.

**H0 (Нулевая):** Все наблюдаемые эффекты (Hubble tension, DM:OM, массовые соотношения) объясняются шумом, подгонкой, selection bias или ΛCDM с известными расширениями.

---

## 2. Таблица гипотез

| ID | Гипотеза | Механизм | Что объясняет | Что не объясняет | Kill criterion | Status | Confidence |
|---|---|---|---|---|---|---|---|
| **H0** | ΛCDM (Null) | FLRW + Λ + CDM | CMB, BAO, SNe, структура | Hubble tension (стат.), природа DM | Если MULTING/IDM предсказывает verified феномен вне ΛCDM | ✅ Survives | 0.85 |
| **H1** | MULTING/IDM — полная замена ΛCDM | Dipole repulsion от k_A + 5 тёмных изомеров | H(z) без Λ, DM:OM≈5:1, массы частиц | Лагранжиан, β-rescaling, solar system, N_eff | Если β-rescaling требует >10³ без физики или ΔAIC>+2 vs Newton | ⚠️ Weak | 0.12 |
| **H2** | MULTING — только феноменологический фреймворк | Эффективная подгонка H(z) с 2 параметрами | Тренды H(z) | Микрофизика, происхождение β | Если β_d, β_q требуют z-зависимой подгонки | ⚠️ Weak | 0.30 |
| **H3** | IDM — самостоятельная модель DM (стандартная гравитация) | 5 зеркальных секторов SM | DM:OM ≈ 5:1 | Hubble tension, dipole gravity | ΔN_eff > 0.5 от тёмных секторов или σ/m > 1 см²/г | ❌ Killed | 0.08 |
| **H4** | Только эмпирические соотношения (Eq. 32, бозоны) | Неизвестная глубинная симметрия | Массовые соотношения фермионов/бозонов | Космология, расширение | Если PDG 2026 даёт отклонение Eq. 32 > 2σ | ✅ Survives | 0.55 |
| **H5** | Частичный MULTING (dipole реален, но нужна полевая теория) | Кинетическая энергия суб-объектов модифицирует гравитацию | Аномалии на масштабах кластеров | Глобальное расширение без усреднения | Если за 6 мес. нет лоренц-инвариантного лагранжиана | ⚠️ Weak | 0.22 |

---

## 3. Kill-Tests

| Гипотеза | Kill criterion | Минимальный тест | Что убьёт | Ожидаемый результат (если неверна) | Стоимость | Скорость |
|---|---|---|---|---|---|---|
| **H1** | β-rescaling без физического механизма ИЛИ ΔAIC > +2 vs Newton | Volume-limited fit 443 MCXC + XMM; сравнить AIC/BIC | β_d остаётся ~4.5 при физическом k_A, диполь незначим | ΔAIC = +2.5 в пользу монополя | 2 недели | Быстро |
| **H1** | Нет симметрийной группы для 6 изомеров | Попросить TJB явно указать группу или признать постулат | «6 — это феноменологический параметр» | Циклическая логика: 5:1 → 5 изомеров | 1 день (письмо) | Немедленно |
| **H3** | ΔN_eff от 5 тёмных секторов | Аналитический подсчёт: 5×(γ'+ν') + thermal history | ΔN_eff ≈ 88σ | Нарушение Planck 2018 (N_eff = 2.99±0.17) | 3 дня | Немедленно |
| **H3** | Тёмные нейтрино = HDM | Оценка m_ν_dark и T_dec; если m < 1 кэВ и T_thermal → HDM | Подавление структуры < 10 Мпк | Конфликт с Lyman-α forest | 2 дня | Немедленно |
| **H3** | Самовзаимодействие внутри изомера | σ/m ≈ 0.6 см²/г (ядерное сечение / масса) | Превышение Bullet Cluster limit | «MESI» на грани, не «cold» | 1 день | Немедленно |
| **H4** | Eq. 32 не выдерживает PDG 2026 | Сверка с новыми значениями m_τ, m_e, α, G | Отклонение > 2σ | Случайное совпадение | 1 день | Немедленно |
| **H5** | Невозможность лагранжиана | Попытка вариационного принципа для Eq. 14–17 | Нарушение сохранения энергии | Dipole term не выводится из действия | 6 месяцев | Медленно |

---

## 4. Discriminating Evidence

**H1 vs H2:** Можно ли предсказать β_d из физики кластера (k_A, M, r) без фита H(z)?
- Если да → поддержка H1. Если нет → поддержка H2.

**H1 vs H0:** Volume-limited выборка: доминирует ли диполь на низком z?
- H1: dipole доминирует при z < 0.5. H0: нет диполя.

**H3 vs H0:** Bullet Cluster σ/m > 0.5 см²/г?
- H3 предсказывает σ/m ~ 0.6. H0 (CDM): σ/m < 10⁻²⁴.
- Bullet Cluster limit < 1 см²/г → H3 marginally compatible, but not «cold».

**H4 vs H1:** Работают ли массовые соотношения без MULTING/IDM?
- Если Eq. 32 работает, но MULTING умирает → H4 выживает, H1 нет.

**H5 vs H1:** Лоренц-инвариантный лагранжиан для диполя?
- H1 уже заявляет следствие из Лоренц-инвариантности (Sec 2.2). Без лагранжиана — претензия без основания.

---

## 5. Preliminary Screen

| Гипотеза | Статус | Обоснование |
|---|---|---|
| **H0** | ✅ Survives | Нет killer evidence. Hubble tension — статистическая напряжённость. |
| **H1** | ⚠️ Weak | β-rescaling (7 порядков), ΔAIC = +2.5, нет лагранжиана, нет группы, ΔN_eff ~88σ. |
| **H2** | ⚠️ Weak | Возможен как феноменологический fit; Occam penalty: 2 параметра без микрофизики. |
| **H3** | ❌ Killed | ΔN_eff от 5 тёмных секторов нарушает CMB. Тёмные нейтрино = HDM. σ/m на грани. |
| **H4** | ✅ Survives | Eq. 32 (0.17σ), 7:9:17 Higgs (0.4σ). Независимы от MULTING/IDM. |
| **H5** | ⚠️ Weak | Концептуально возможно. Gate: лагранжиан за 6 мес. |

---

## 6. Red Team / Skeptic Mode

**H0 (ΛCDM):**
1. Hubble tension может быть систематикой (Cepheid калибровка, TRGB).
2. S8 tension — барионная обратная связь, не новая физика.
3. Природа DM открыта, но это не фальсификация ΛCDM.

**H4 (Эмпирические соотношения):**
1. При 4 константах (m_τ, m_e, α_EM, α_G) совпадение 0.17σ может быть случайным.
2. Масса Higgs менялась в PDG — постдикция, не предсказание.
3. δ = 0.03668 — свободный параметр; без вывода это overfitting.

**H5 (Частичный MULTING):**
1. «Dipole эффект» может быть барионным (AGN feedback), не гравитационным.
2. Selection bias — flux-limited искажают k_A.
3. Может требоваться модифицированная инерция (MOND), не гравитация.

**Что рецензент атакует первым:**
- H1: «Монополь статистически лучше полной формулы» (B-1) — smoking gun.
- H1: «6 изомеров без симметрийной группы» — не физика.
- H3: «Тёмные нейтрино = HDM» — мгновенный kill.

---

## 7. Evidence Ledger

| Вывод | Статус | Основа |
|---|---|---|
| Eq. 32 верна до 0.17σ (PDG 2024) | **FACT** | data |
| Монополь r=0.89, полная MULTING r=0.62 (MCXC+CC) | **FACT** | data |
| β_d=4.5 (Table A1) vs β_d~10⁷ (физический k_A) | **FACT** | data + reconstruction |
| β — fitted, не derived | **INFERENCE** | logic + data |
| 6 изомеров объясняют DM:OM ≈ 5:1 | **HYPOTHESIS** | insufficient_data |
| Лагранжиан для MULTING | **UNKNOWN** | insufficient_data |
| Термальная история 5 тёмных секторов | **UNKNOWN** | insufficient_data |
| ΔN_eff от 5 изомеров | **RECONSTRUCTION** | logic + analogy |
| 36-point анализ Бойко | **RECONSTRUCTION** | logic + data |

---

## 8. Confidence Scores

| Гипотеза | Confidence | Basis | Penalties |
|---|---|---|---|
| H0 | 0.85 | data + expert_prior | unresolved tensions |
| H1 | 0.12 | analogy + partial data | no Lagrangian, β-rescaling 7 orders, ΔAIC=+2.5, ΔN_eff~88σ, no symmetry group |
| H2 | 0.30 | logic + partial data | Occam penalty, no predictive power |
| H3 | 0.08 | logic | killed: ΔN_eff, HDM dark neutrinos, baryon asymmetry, σ/m at Bullet limit |
| H4 | 0.55 | data + logic | possible numerology, no mechanism, δ unexplained |
| H5 | 0.22 | logic + analogy | no Lagrangian, no screening mechanism |

---

## 9. Prioritized Next Tests

| # | Тест | Цена | Скорость | Discriminating power | Решающая сила |
|---|---|---|---|---|---|
| 1 | **β-rescaling resolution** (письмо TJB) | 1 день | Немедленно | Высокая (H1 vs H2) | Фатальная для H1 без ответа |
| 2 | **Volume-limited AIC/BIC** MCXC+XMM | 2 недели | Быстро | Высокая (H1 vs H0) | Фатальная, если ΔAIC > +2 |
| 3 | **ΔN_eff аналитический bound** | 3 дня | Немедленно | Фатальная (H3) | Уже убивает H3 |
| 4 | **PDG 2026 check** Eq. 32 | 1 день | Немедленно | Средняя (H4) | Robustness check |
| 5 | **Lagrangian attempt** | 6 месяцев | Медленно | Фатальная (H1/H5) | Gate 2 если H1 выживет |

---

## 10. Crucial Experiment

**Тест:** β-rescaling resolution via direct query to TJB.

**Протокол:**
1. Письмо TJB: «What physical mechanism rescales β_d from 4.5 (Table A1) to ~10⁷ when k_A = E_ICM/c²?»
2. Зафиксировать ответ в docs.
3. Механизм предложен → Gate 2 (Lagrangian).
4. «Fitting parameter» → H1 killed, pivot to H4 + H5 salvage.
5. Нет ответа 2 недели → H1 killed by default.

**Вероятности:**
- Осмысленный ответ: 30%
- «Future work»: 50%
- Конкретный механизм: 20%

---

## 11. Next Research Cycle

**Если H1 killed (confidence 0.12 → наиболее вероятно):**
- **Salvage H4:** Eq. 32 + бозонные соотношения как независимые паттерны. Опубликовать как «empirical mass relations» без MULTING/IDM.
- **Salvage H5:** Dipole gravity как открытая проблема без космологических претензий.
- **Publish Boyko reconstruction:** arXiv — «critical assessment» 36-point map + explicit kill criteria.

**Если H1 survives (маловероятно):**
- Gate 2: 6 мес. на лагранжиан.
- Gate 3: Screening mechanism.
- Gate 4: BBN/CMB consistency (thermal history).

**H3 уже killed:** Документировать явно в paper: «IDM violates ΔN_eff and produces hot dark matter; not viable CDM without additional structure.»

---

## Self-Audit
- ✅ H0 зафиксирована
- ✅ 6 гипотез + H0
- ✅ Kill-test для каждой
- ✅ Discriminating evidence
- ✅ Confounders для выживших
- ✅ Evidence Ledger
- ✅ Confidence с basis/penalties
- ✅ Crucial next test
- ✅ H1 confidence = 0.12 (не «любимая»)

---

*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*
*docs/120 issued 2026-06-17*
*Related: docs/119, docs/118, docs/structured_reading_v2_for_tjb.md*
