# NCG spectral-triple thread — rebuild from prose + pre-registered main experiment

**Date:** 2026-08-10 · **Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
**Question type (L0):** descriptive — existence/properties of mathematical structures
(no data estimand, no causal claim, no prediction about measurements).

---

## Gate 1 — Artifact Identity (почему этот эксперимент начинается с реконструкции)

```yaml
artifact_id:          ARTIFACT_CHAT_2026-08-10_NCG_PROSE_SUMMARY
source:               prose summary pasted by user into this session, 2026-08-10
date_created:         unknown (external conversation, exact date not stated)
date_received:        2026-08-10
publication_status:   private correspondence (chat transcript), NO artifacts
relates_to:           adjacent to this repo's Eq.32<->Singh line (exp_f_s3_geometry.py,
                      exp_g_singh_j3_algebra.py, exp_j_connes_ncg.py, NR-009) but
                      NONE of its specific claims (C11..C43, OB10, OB11, D^t family,
                      T<->1-T) have artifacts anywhere in this repository -- verified
                      by repo-wide grep for distinctive markers, 0 hits.
```

**Hard rule applied:** статусы (✅/❌/❓) из прозы — самооценка ТОЙ сессии. Здесь они
все стартуют как `[PROSE-ONLY]` и получают статус только после независимой
реконструкции в этой папке. Никакой перенос вердиктов между артефактами.

## Zero-Signal Gate

| Поле | Значение |
|---|---|
| Entity | Игрушечное семейство операторов `D^t(n,σ)=σ(n+3/2)+(t−1/2)·3`; блочная конструкция `D⁰⊕D¹`; спинорная структура на `S³×S⁶` (Cl(0,3)×Cl(6,0)); три triality-канала Spin(8); матричный параметр `T` |
| Falsifiable predicates | (P1) `spec(D¹)=−spec(D⁰)` аналитически; (P2) одиночный `D⁰` НЕ допускает антикоммутирующей градуировки, а `D⁰⊕D¹` — допускает, с явной `γ`; (P3) все три triality-канала имеют одинаковое SU(3)-содержание `1⊕1⊕3⊕3̄`; (P4) зарядовое сопряжение в Cl(6,3) даёт `BB̄=−I`, при том что наивный аргумент «9≡1 mod 8» дал бы `+I`; (P5) `T↔1−T` — унитарная эквивалентность |
| Measurable outcome | каждый predicate = PASS/FAIL символьного или численного вычисления в скриптах этой папки |

Gate: **PASS** — все три поля заполнены из самого материала.

## Scope этого раунда (rebuild) vs следующего (main experiment)

**Этот раунд:** только реконструкция P1–P5 независимым кодом. Это репродукции с
известными целевыми ответами (проза их называет) — НЕ слепой тест. Честная
формулировка результата: «утверждение прозы воспроизводится/не воспроизводится
независимой реализацией, построенной по его словесной спецификации».

**Следующий раунд (main experiment, `A + D_full + triality`)** — конструкция
настоящей алгебры `A`, оператора `D_full` с недиагональным `X`, проверка
first-order/J/ориентируемости, и red-team на `N_gen=3`. Он НЕ начат. Его
kill-условия предрегистрируются ЗДЕСЬ, до любой попытки конструкции:

## Pre-registered kill conditions (написаны ДО main experiment, 2026-08-10)

- **K1 (first-order):** если ни одна неигрушечная `A` (строго богаче `C⊕C`) на
  `H₀⊕H₁`, совместимая с уже установленной SU(3)/triality-структурой, не
  удовлетворяет first-order condition вместе с `D_block` и согласованным `J` —
  «полная спектральная тройка» остаётся OPEN, конструкция фиксируется как
  spectrum-only model, НЕ спектральная тройка.
- **K2 (red-team №5):** если существует унитарное преобразование, уважающее
  симметрии конструкции и стирающее различие трёх каналов на уровне всех
  наблюдаемых — `N_gen=3` в этой конструкции = артефакт представления;
  CONDITIONAL → KILLED, без права мягкой переформулировки в той же ветке
  (Minimal Relaxation Rule: новая ветка, новый ID).
- **K3 (X-трихотомия):** если `X≠0` допустим и никакая симметрия его не
  запрещает — независимость поколенческих секторов = ручное предположение;
  статус factorization-claim → DOWNGRADED, не PROMOTE.
- **K4 (triality как 1⊗t):** если OB11(iii) не реализуется (нет `U_t` с
  `U_t D U_t⁻¹ = D` в ковариантной форме) — `H ≃ H_matter⊗H_generation` НЕ
  установлена; headline `N_gen=3` остаётся CONDITIONAL в этой ветке навсегда.

**Что этот результат НЕ будет означать (записано заранее):**
1. Даже полный успех main experiment НЕ доказывает, что физика *требует* двух
   секторов — только что они совместимы с конструкцией (модальность
   «допустимо», не «необходимо»).
2. Репродукции этого раунда НЕ повышают статус физической интерпретации —
   только внутреннюю согласованность математики.
3. Ничто здесь не переносится на MULTING/Eq.32 автоматически — смежность
   темы (Singh, октонионы) ≠ логическая связь (Gate 1).

## Скрипты этой папки

| Скрипт | Претензии | Контроли |
|---|---|---|
| `rebuild_c43_grading.py` | P1, P2, P5 | аналитика + числовая трункация; no-go для одиночного D⁰ как позитивный контроль на сам механизм проверки градуировки |
| `rebuild_ob11_triality.py` | P3 | целочисленная арифметика весов, multiset-сравнение; контроль: 8v через известное 7⊕1 |
| `rebuild_ob10_clifford.py` | P4 | два позитивных контроля с ПРОТИВОПОЛОЖНЫМИ известными ответами: Cl(0,3) → −I (псевдореальность SU(2)) и Cl(2,0) → +I; плюс прямое сравнение Cl(9,0) vs Cl(6,3) — сама «ловушка сигнатуры» |
