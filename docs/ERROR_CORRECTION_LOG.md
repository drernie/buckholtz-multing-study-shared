# Error Correction Log — Evidence Table (2026-06-12)

**Trigger:** Evidence table presented in chat with M1–M5 labels; three claims wrong or mis-framed.
**Rule violated:** `audit-verification-gate.md` — чужой [VERIFIED] = мой [INFERRED]; нельзя выдавать за верифицированное без tool-прогона.

---

## Error 1 — FRAMING (SC-1 / было "M1")

**Что написал:**
> "H_MULT = 1.074 × H_FLRW (автор вычисляет H_MULT как множитель к FLRW)"

**Что неверно:**
Автор вычисляет H-MULT через силы (F_m, F_d, F_q, Appendix A.1 p.33). Формула 1.074 × H_FLRW — наше диагностическое наблюдение о числовом выходе Table A1, не об авторском методе.

**Исправление [VERIFIED-tool 2026-06-12]:**
```
SC-1: ЧИСЛОВОЙ ВЫХОД Table A1 (из AI-сервиса) эмпирически близок к 1.074 × H_FLRW.
  mean ratio = 1.0736, scatter 2.6%, corr = 0.99959
  НЕ означает: автор использует эту формулу.
  ОЗНАЧАЕТ: AI-сервис с β_d=4.5, β_q=18.0 создаёт выход, пропорциональный H_FLRW.
  Scope: Table A1 (Claude AI service output only).
```

---

## Error 2 — FACTUAL (SC-3 / было "M3")

**Что написал:**
> "Step 5 Appendix A1 не содержит явной формулы H_MULT(z)"

**Что неверно:**
Step 2 Guidelines (p.33) содержит формулы сил:
- F_m = Gm_A·m_P/r²
- F_d = Gk_Ac⁻²m_P|r_dA|/r³ + Gk_Pc⁻²m_A|r_dP|/r³
- F_q = Gk_Ak_Pc⁻⁴|r_qAB|²/r⁴
- F_oP = F_m − F_d + F_q

Step 5 (p.34) явно отсылает к этим формулам: "use the formulas r_dA = β_d·r_A …".

**Исправление:**
```
SC-3: Appendix A.1 СОДЕРЖИТ формулы для сил (Step 2 Guidelines, p.33).
  ОТСУТСТВУЕТ: явная формула перехода F_oP → H(z).
  Step 5 говорит "use my monopole, dipole, and quadrupole components to fit H(z)"
  но не задаёт bridge F→H. AI-сервисы заполняют этот зазор неявно (H²∝Φ/Φ₀).
  Правильный claim: "Bridge F→H не указан в тексте; используется AI-implicit."
```

---

## Error 3 — SCOPE (SC-4 / было "M4")

**Что написал:**
> "C12 REFUTED: диполь не доминирует нигде"

**Что неверно:**
Step 5 явно инструктирует: "Ensure that dipole repulsion **dominates** at low redshift."
Автор конструировал модель так, чтобы диполь доминировал при малых z.
Критик прав: текст препринта утверждает доминирование диполя как feature модели.

**Исправление [VERIFIED-tool 2026-06-12]:**
```
SC-4: Под НАШИМИ реконструированными кластерными параметрами (геом. средние CSV)
  ε_d < 1 на ВСЕХ z → диполь не доминирует в нашей реконструкции.
  НЕ означает: утверждение автора опровергнуто.
  ОЗНАЧАЕТ: наши CSV-параметры не воспроизводят доминирование диполя.
  Правильный label: C12_NOT_REPRODUCED_UNDER_OUR_RECONSTRUCTION (не REFUTED).
  Нерешённый вопрос: какой D(z)-schedule использовал AI-сервис автора?
```

---

## Error 4 — NAMESPACE COLLISION

**Что написал:**
> Таблица с метками M1–M5

**Что неверно:**
В проекте существуют M-модули (M1 Force Law, M2 Bridge Gap, M7 Dark Matter...).
SC-блоки из `audit/self_consistency_diagnostic.py` — отдельный namespace.
Использование "M1–M5" для SC-блоков создаёт коллизию.

**Исправление:**
Diagnostic findings из self_consistency_diagnostic.py → переименовать в **SC-1…SC-5**.
M-модули playbook → сохранить как M1, M2, M7… без изменений.

---

## Corrected Evidence Table (SC-series) [VERIFIED-tool 2026-06-12]

| # | Входные данные | Статус | Проделанная работа | Результат | Интерпретация | Допущение автора |
|---|---|---|---|---|---|---|
| **SC-1** | Table A1, 12 точек (Claude AI output) | ✅ VERIFIED-tool | Ratio H_MULT/H_FLRW по всем строкам | mean=1.074, scatter=2.6%, corr=0.99959 | Числовой выход пропорционален H_FLRW. НЕ авторская формула | β_d, β_q — константы, не функции времени |
| **SC-2** | Reconstructed Φ(z) из CSV cluster params | ✅ VERIFIED-tool | H²∝Φ/Φ₀ bridge с нашими параметрами | H_pred: 73→0.096 km/s/Mpc (↓×762). Gap ×4365 vs reported | Наша реконструкция → H падает, Table A1 растёт. Bridge не совпадает | k_A(z), D_C:AB(z) — взяты из CSV (не из авторского расчёта) |
| **SC-3** | Appendix A.1 Steps 1–8 (текст препринта) | ✅ VERIFIED-read | Чтение pp.32–36 | Формулы F_m/F_d/F_q присутствуют (Step 2 Guidelines). F→H bridge ОТСУТСТВУЕТ | AI-сервисы используют implicit bridge H²∝Φ/Φ₀ — не задан TJB явно | Bridge formula не задана, AI выбирает её самостоятельно |
| **SC-4** | Claude CSV cluster params, β_d=4.5, β_q=18.0 | ✅ VERIFIED-tool | ε_d = F_d/F_m по 12 точкам | ε_d < 1 на ВСЕХ z (max ε_d ≈ 10⁻³). Диполь не доминирует | НЕ опровержение автора. Наши CSV-параметры не воспроизводят dipole dominance | Step 5 требует "ensure dipole dominates at low z" — нашими параметрами не достигается |
| **SC-5** | SC-2 headline (gap ×4365) | ✅ VERIFIED-tool | Multiverse: arith_mean vs geom_mean repr. | Arith: gap ×3944 (−9.7%). Phi ratio = 0.000002 в обоих случаях | SC-2 робастен к выбору repr.value | Intermediate z: только geom (нет задокументированных диапазонов) |

---

## Правила нарушенные → fix

| Правило | Нарушение | Fix |
|---|---|---|
| `audit-verification-gate.md` | SC-1..SC-5 взяты из summary предыдущей сессии без перезапуска | Прогнал `self_consistency_diagnostic.py` → [VERIFIED-tool 2026-06-12] |
| `integrity.md` — Verify-Before-Claim | M3 написан без чтения текста Step 5 | Прочитал pp.32–36 → исправил формулировку |
| Scope discipline | M4 "REFUTED" без qualifier | Добавлен scope: "под нашей реконструкцией" |
| Namespace | M1–M5 для SC-блоков | Переименованы в SC-1…SC-5 |

---

*Файл создан: 2026-06-12. NOT_VALIDATION NOT_REFUTATION INTERNAL_DIAGNOSTIC_ONLY*
