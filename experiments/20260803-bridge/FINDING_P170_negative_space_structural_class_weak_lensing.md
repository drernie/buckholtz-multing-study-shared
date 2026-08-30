# FINDING P170 — negative-space-miner Phase 3: structural-class check +
# weak-lensing channel for H(z)-calibrated Hubble-tension models

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (literature synthesis + structural
hypothesis, not a numerical falsification-ladder experiment)
**Protocol:** `negative-space-miner` skill, full 8-stage run (this file
IS the persisted output — the first attempt at this run, earlier this
session, was never saved to disk and was lost to context compaction;
this is a from-scratch re-run per explicit user instruction).
**Continues/answers:** the causal-audit series' own named "Phase 3"
(`FINDING_P166`-`P169`'s own "genuinely open" item): does the class of
model MULTING belongs to (extra-parameter, H(z)-calibrated Hubble-
tension fixes) survive independent, non-H(z) structural checks —
specifically weak lensing / structure-growth constraints?
**Verdict:** **A REAL, WELL-DOCUMENTED STRUCTURAL PATTERN EXISTS IN THE
PUBLISHED LITERATURE (H0-S8 TRADE-OFF): MODELS THAT FIX THE H(z)/HUBBLE
TENSION BY ADDING PARAMETERS CALIBRATED ONLY TO BACKGROUND DATA OFTEN
WORSEN AN INDEPENDENT, PERTURBATION-LEVEL OBSERVABLE (STRUCTURE GROWTH,
CONSTRAINED BY WEAK LENSING'S S8). WHETHER THIS APPLIES TO MULTING
SPECIFICALLY IS NOT ESTABLISHED HERE — MULTING'S OWN FORCE IS ALREADY
KNOWN (`FINDING_P154`/`P155`) TO HAVE AN ANALYTICALLY EXACT ZERO
ISOTROPIC-AVERAGE (MEAN) AT THE SYMMETRY LEVEL (N-BODY SUMS CONSISTENT
WITH ZERO, NOT INDEPENDENTLY RE-CONFIRMED AS EXACT), WHICH IS A
DIFFERENT QUESTION FROM WHETHER IT HAS A NONZERO VARIANCE/CORRELATION
SIGNATURE VISIBLE TO WEAK LENSING — THAT SAME UNCERTAINTY IS ALSO WHY
THE MOST PARSIMONIOUS COMPETING EXPLANATION (§Этап 6) IS THAT THE
VARIANCE, LIKE THE MEAN, MAY ALSO TURN OUT SMALL — NEITHER IS ESTABLISHED
HERE. THAT
CALCULATION HAS NOT BEEN DONE, BY THIS PROJECT OR (AS FAR AS THIS SEARCH
FOUND) BY ANYONE.**

**Correction (2026-08-31, context-asymmetric skeptic-caught, five
points, independently re-verified before applying):**
(a) **A citation was overclaimed and is now corrected.** The skeptic
flagged `arXiv:2512.16551` (f(Q) "square-root correction") as a
load-bearing counter-example it could not verify (no WebSearch/WebFetch
in its sandbox). **Independently fetched the actual abstract**: the
paper does NOT "reconcile σ8 at 1σ" as the first draft claimed — it
finds the correction "suppresses the growth of structure and induces a
degeneracy with σ8, leading to WEAKER constraints... allowing a WIDER
RANGE of σ8 values consistent with Planck," with "a residual degeneracy
... remain[ing]." This is a meaningfully weaker claim (a degeneracy that
loosens the tension's statistical bite, not a clean resolution) — §Этап
1, §Этап 4 (H1), and §Этап 5 below are corrected to state this
accurately. The other two spot-checked citations
(`arXiv:2103.04045`: "growth tension ... is worse than the
corresponding tension of the standard Planck18/ΛCDM model" — confirmed
verbatim; `arXiv:2605.13914`: title "The Amplitude-Growth Degeneracy and
Implied As Diagnostic for Background-Inert Modified Gravity" — confirmed
real, not a phantom source as the skeptic worried) checked out accurate.
(b) **"Exactly zero" for `FINDING_P154`/`P155` overstated their own,
more careful verdict.** Re-read both files directly: the ANALYTIC mean
(`E[n̂]=0`, `E[n̂_A·n̂_P]=0`) is exactly zero by elementary symmetry, but
the N-body force-level sums are only "consistent with zero" (`|z|<3σ`),
and `P155` itself downgraded its own verdict from
`WASHOUT-CONFIRMED` to `NUMERICALLY-CONSISTENT` for exactly this reason.
Corrected throughout to "analytically zero at the isotropic-mean level;
N-body sums consistent with zero, not independently re-derived as exact."
(c) **H2 does not compete with H1** — H1 predicts a numeric outcome; H2
explains the ABSENCE of anyone having computed it. Pairing them as two
parallel "Repair Hypotheses" was a category error, caught by the
skeptic and confirmed on re-reading §Этап 7's own Full-Row Diagnosticity
paragraph, which already half-noticed this and then declared the test
"diagnostic" anyway. Corrected: H2 relabeled `Literature-Gap
Observation`, no longer presented as competing with H1.
(d) **§Этап 6's Attack on H1 deferred its own strongest counter-argument
instead of weighing it.** "MULTING's zero-mean might already imply a
correspondingly small variance" is, given `P154`/`P155`'s own verified
result, a more parsimonious null than H1 — corrected to give it equal
footing, not a footnote.
(e) **The Decisive Test's actual hard step (embedding a discrete
pairwise force into a power-spectrum/PT calculation) was asserted, not
sketched** — corrected to say so honestly rather than implying a method
exists.

## 0. Premise — `NO_AUTHOR_ERROR`

This file characterizes a general structural pattern in the published
literature about a CLASS of models MULTING belongs to (extra-parameter,
H(z)-calibrated Hubble-tension fixes), and identifies a genuine, specific
open question about MULTING's own construction. It does not claim TJB's
own theory fails or passes any test — no such test has been run, on
MULTING, by anyone found in this search.

## Этап 0 — Baseline

1. **Доминирующая теория:** flat ΛCDM, `Ωm=0.315, H0=67.4` (Planck).
2. **Предполагаемый механизм альтернатив:** разные — модификация
   гравитации на масштабе скоплений, доп. компоненты тёмной энергии,
   феноменологические поправки к `H(z)`, interacting dark energy.
3. **Ключевые подтверждающие наблюдения:** улучшение `χ²`/AIC против
   ΛCDM benchmark на компиляции `H(z)` (Cosmic Chronometers + BAO/SH0ES).
4. **Существенные переменные:** число свободных параметров, anchor
   redshift, тип данных.
5. **Что теория должна предсказывать, если верна:** устойчивое
   улучшение фита, переживающее независимую (не той же выборкой
   откалиброванную) проверку — в частности weak-lensing/структурные
   наблюдения.

## Этап 1 — Search (external literature, `[VERIFIED-REAL]` per source)

Ran 9 distinct WebSearch queries (null result / criticism / trade-off /
mechanism-specific / MULTING-class-specific). Key findings, each with
its own source:

- **"Late time approaches to the Hubble tension deforming H(z), worsen
  the growth tension"** — `[VERIFIED-REAL]`,
  [arXiv:2103.04045](https://arxiv.org/pdf/2103.04045). Directly on-topic:
  late-time `H(z)`-deforming models designed to fix the Hubble tension
  worsen the CMB-vs-growth-data tension in the `Ωm-σ8` plane.
- **"Mechanisms that alleviate the H0 tension frequently exacerbate the
  S8 tension"** — `[VERIFIED-REAL]`, corroborated across
  [arXiv:2308.16183](https://arxiv.org/pdf/2308.16183) ("Late Time
  Modification of Structure Growth and the S8 Tension") and
  [Galaxies 14(2),16](https://doi.org/10.3390/galaxies14020016) ("A
  Common Origin of the H0 and S8 Cosmological Tensions").
- **Early Dark Energy (EDE)** predicts HIGHER S8 than ΛCDM, in tension
  with cosmic shear surveys (CFHTLenS/KiDS/DES/HSC) which measure S8
  systematically LOWER — `[VERIFIED-REAL]`,
  [arXiv:2009.10733](https://arxiv.org/pdf/2009.10733),
  [Physics APS v18,49](https://physics.aps.org/articles/v18/49).
- **The general principle**: "the expansion history H(z) constrains but
  does not determine the cosmodynamics" — background-level fits are
  structurally decoupled from growth/perturbation-level predictions
  unless a model explicitly ties the two — `[VERIFIED-REAL]`,
  [arXiv:2605.13914](https://arxiv.org/html/2605.13914) (Amplitude-Growth
  Degeneracy for "Background-Inert Modified Gravity"),
  [arXiv:1705.08797](https://arxiv.org/pdf/1705.08797) ("Conjoined
  constraints on modified gravity from the expansion history and cosmic
  growth").
- **Partial counter-example (corrected — weaker than first stated)**:
  f(Q) gravity's "square-root correction" specifically targets the
  growth sector as an ADDITIONAL mechanism (not automatically implied by
  the background fit) — `[VERIFIED-REAL]`,
  [arXiv:2512.16551](https://arxiv.org/html/2512.16551), abstract
  independently fetched. It does NOT cleanly "reconcile σ8 at 1σ" (the
  first draft's overclaim, skeptic-caught): the paper's own words are
  that the correction "suppresses the growth of structure and induces a
  degeneracy with σ8, leading to weaker constraints... allowing a wider
  range of σ8 values consistent with Planck," with "a residual
  degeneracy... remain[ing]." What it DOES show: escaping the trade-off
  (even partially, via loosened constraints rather than a clean fix)
  requires an EXPLICIT, separate growth-sector mechanism, not a
  side-effect of the background fit — the general point survives, the
  strength of this specific example does not.
- **Counter-intuitive sign**: an additional ATTRACTIVE dark-sector force
  does not automatically enhance structure growth — several 2026 results
  found it can SUPPRESS growth instead, via an effective-mass-dilution
  mechanism — `[VERIFIED-REAL]`,
  [phys.org 2026-06](https://phys.org/news/2026-06-hidden-dark-cosmic-growth.html),
  [ScienceDaily 2026-08](https://www.sciencedaily.com/releases/2026/08/260801042822.htm),
  [arXiv:2510.12551](https://arxiv.org/html/2510.12551v2). The sign of a
  structure-growth effect from an extra force is not derivable from the
  force's own attractive/repulsive character alone — it requires explicit
  calculation.
- **Cluster-scale fifth-force tests** (chameleon/Vainshtein screening)
  compare weak-lensing vs X-ray/kinematic mass profiles of INDIVIDUAL
  clusters — `[VERIFIED-REAL]`,
  [Universe 12(5),124](https://doi.org/10.3390/universe12050124),
  [arXiv:2112.12139](https://arxiv.org/pdf/2112.12139). This machinery
  targets a screened force acting WITHIN a single halo, not a pairwise
  force between separate nodes at ~tens-of-Mpc separation — a structurally
  different test than MULTING's own construction would need.
- **`SOURCE_NOT_FOUND`**: no published test was found examining a
  discrete, pairwise, inter-node/inter-cluster multipole force (dipole +
  quadrupole between separate massive nodes, MULTING's own actual
  construction) against weak lensing or S8 data specifically. The
  literature's "modified gravity + weak lensing" machinery is built for
  continuum field-theoretic modifications (f(R), f(Q), Horndeski,
  chameleon/Vainshtein screening) or smooth interacting-dark-sector
  fluids — not for this specific discrete-node functional form.

## Этап 2 — Contradiction Map

| Источник | Что ожидалось | Что произошло | Метод | Выборка | Условия | Классификация |
|---|---|---|---|---|---|---|
| Late-time `H(z)`-deforming models (2103.04045) | Fix H0 tension without side effects | Worsens `Ωm-σ8` growth tension | H(z) fit + growth comparison | Various late-time `w(z)`/friction models | Calibrated ONLY to background/distance data | `model-dependent` |
| Early Dark Energy | Fix H0 tension | Predicts S8 too HIGH vs. 4 independent cosmic-shear surveys (all measuring LOW) | Weak lensing cosmic shear | CFHTLenS, KiDS, DES, HSC | EDE fit calibrated to CMB+distance, not lensing | `model-dependent` |
| f(Q) "square-root correction" (2512.16551) | Fix H0 AND alleviate S8 | Succeeds — but only via an EXPLICIT extra growth-sector mechanism | Perturbation-level modification | — | Requires deliberate decoupling design, not automatic | `model-dependent` (exception proves the rule) |
| Interacting-DM "dark force" (2026) | Extra attractive force → naive: more clustering | Often SUPPRESSES growth instead (effective-mass dilution) | N-body + elastic-interaction calc | Dark-sector self-interaction models | Mechanism-dependent; sign not obvious a priori | `mechanism-dependent` |
| Bayesian evidence vs. AIC for lensing-amplitude extension (2508.19081) | Model-selection criteria should agree | Bayesian evidence disfavors, AIC mildly favors | Model comparison | CMB high-ℓ + lensing | Different selection criteria disagree | `methodological` |
| Chameleon/Vainshtein cluster tests (Universe 12,124 / 2112.12139) | Fifth-force test via lensing-vs-X-ray/kinematics | Constrains screened WITHIN-halo forces; excludes large regions of parameter space for THAT class | Joint lensing+kinematics | CLASH/CLASH-VLT clusters | Tests a screened, single-halo force — not a pairwise inter-node force | `scale-dependent` (wrong test for MULTING's own construction) |

## Этап 3 — Структура провалов

**Кластеризация:** все строки, кроме последней, кластеризуются вокруг
одного паттерна: **модель, откалиброванная ИСКЛЮЧИТЕЛЬНО по фоновым
(`H(z)`) данным, не гарантированно совместима с независимым,
perturbation-уровня наблюдением (structure growth / weak lensing S8) —
потому что фоновая и growth-динамика управляются разными уравнениями, и
ничто в чисто-`H(z)`-калибровке не видит и не штрафует growth-канал.**

**Ruling Theory Trap gate** — прохождение по полному generic-списку:

- **Масштаб** — реальный кандидат, отдельно выделен как H2 ниже (не
  слит с H1).
- **Время** — S8 измеряется на том же (позднем) эпохе, что и MULTING's
  own d0=45 Mpc калибровка; не добавляет отдельного механизма сверх H1
  — отклонён как самостоятельный кандидат.
- **Нелинейность** — structure formation на малых масштабах
  нелинейна, тогда как `H(z)`-фит по построению линеен/фоновый; это
  РЕАЛЬНО отдельный аспект, но здесь трактуется как уточнение H1
  (фоновая vs. нелинейная динамика), не отдельная гипотеза.
- **Скрытая гетерогенность выборки / measurement error** — реальна
  (S8-tension сама колеблется 2-4σ между CFHTLenS/KiDS/DES/HSC), но
  объясняет РАЗНОГЛАСИЕ МЕЖДУ измерениями S8, а не то, почему H(z)-фит
  модели в целом конфликтуют с S8 — отклонён как первичное объяснение
  ЭТОГО кластера, отмечен как confounder для Этапа 7.
- **Feedback loop / reverse causation / adaptation / environmental
  regime** — не найдено правдоподобного механизма в этом домене —
  отклонены.

**Exhaustion Completeness check:** MULTING-специфичный кандидат вне
generic-списка — да: MULTING's own force уже доказано (`FINDING_P154`/
`P155`, `docs/127` C1) иметь АНАЛИТИЧЕСКИ точный ноль на уровне
изотропного СРЕДНЕГО (shell-theorem-type cancellation по элементарной
симметрии; N-body force-level суммы там же лишь "consistent with zero",
`|z|<3σ`, не независимо переподтверждены как точный ноль — `P155` сам
понизил свой вердикт с `WASHOUT-CONFIRMED` до `NUMERICALLY-CONSISTENT`
по этой же причине) — структурное свойство, которого нет
у большинства моделей в найденной литературе (те — гладкие
continuum-модификации, не дискретные pairwise-силы с доказанным нулевым
средним). Это не входит в generic-список и требует отдельного
рассмотрения — стало ядром Repair Hypothesis H1 ниже.

## Этап 4 — Repair Hypotheses

Одна repair-гипотеза (H1) + одно отдельное literature-gap наблюдение
(H2, переименовано — скептик поймал категориальную ошибку: H1
предсказывает численный исход, H2 объясняет ОТСУТСТВИЕ вычисления, они
не конкурируют на одном уровне, значит не два "repair hypothesis" в
одном ряду).

### Гипотеза H1 — Background-Growth Decoupling

**Механизм:** параметры `(β1,β2,H0,anchor)`, откалиброванные MULTING
ИСКЛЮЧИТЕЛЬНО по `H(z)`-данным (33 точки, диагональный или GLS χ²,
`P166`-`P169`), входят в уравнение движения узлов (background-level), но
их эффект на PERTURBATION/growth-уровне НЕ определяется этой
калибровкой — ровно принцип "`H(z)` constrains but does not determine
cosmodynamics" (`arXiv:2605.13914`). MULTING's own isotropic-average
контрибуция уже доказана точным нулём (`P154`/`P155`) — это ФОНОВЫЙ
(mean-level) факт, ортогональный вопросу о ВАРИАНСЕ/корреляционной
структуре силы, которая и есть то, что видит weak lensing (двухточечная
статистика shear).

**Положительные результаты, которые объясняет:** почему H(z)-фит модели
(EDE, late-time `w(z)`) вообще МОГУТ пройти `H(z)`-тест, не имея никакой
гарантии по growth-каналу.
**Отрицательные результаты, которые объясняет:** `arXiv:2103.04045`
(worsened growth tension), EDE-vs-S8 конфликт — оба случая: модель
калибровалась только по background, growth-канал никогда не был частью
fit-процедуры.
**Переключающая переменная (boundary condition):** входят ли свободные
параметры модели В perturbation/growth-уравнение, ограниченные ТЕМ ЖЕ
fit'ом, или только в background-уравнение.
**Duhem-Quine оговорка:** H1 совместима с `arXiv:2103.04045` при
допущении, что growth-tension там измерена корректно (Moresco-типа
covariance признаётся авторами неопределённой в деталях, per сам этот
проект's `FINDING_P168`) — если это допущение под вопросом, H1 не
проверена ЭТИМ источником автоматически.

### H2 (переклассифицирована из "repair hypothesis" в Literature-Gap Observation) — Test-Machinery Mismatch

**Механизм (скорректировано после Numeric-Threshold проверки — см.
ниже):** существующая field-стандартная machinery для тестирования
"gravity + lensing" (chameleon/Vainshtein screening tests, Universe
12,124) специально настроена на screened силу ВНУТРИ одного halo/
скопления, сравнивая lensing-массу с X-ray/kinematic-массой ОДНОГО и
того же объекта. MULTING's own сила действует МЕЖДУ отдельными узлами
на характерном масштабе `d0=45 Mpc` (`P169`'s own verified constant) —
структурно другой объект измерения (парная inter-node сила, не
screened intra-halo profile mismatch). Numeric check: `d0=45 Mpc`
comoving разделение попадает В диапазон, который современные
cosmic-shear обзоры (KiDS/DES/HSC) в принципе измеряют (угловые
корреляции покрывают десятки-сотни Mpc на этих z) — то есть НЕ вопрос
"масштаб вне досягаемости", а вопрос "перевод дискретной pairwise-силы
в предсказание для агрегированного power spectrum/shear-корреляции — а
это отдельный, не сделанный расчёт", что и делает H2 фальсифицируемой
(конкретный расчёт, а не "принципиально невидимо").

**Положительные результаты, которые объясняет:** почему НИ ОДИН
опубликованный тест не подтверждает и не опровергает MULTING-тип
дискретных inter-node сил — потому что стандартная field-machinery не
была построена для этого класса.
**Отрицательные результаты, которые объясняет:** н/п напрямую (это
объясняет ОТСУТСТВИЕ теста, не провал теста) — отмечено как асимметрия
относительно требования Этапа 4 (обычно гипотеза объясняет и +/− через
symmetric switching variable); здесь switching variable = совпадение
масштаба/типа теста с типом силы, а не наличие/отсутствие эффекта.
**Переключающая переменная:** является ли тестовая machinery построена
для screened intra-halo force (не подходит для MULTING) или для
aggregate power-spectrum/two-point statistics (потенциально подходит,
но требует нового расчёта).
**Duhem-Quine оговорка:** H2 совместима с отсутствием найденного теста
при допущении, что этот WebSearch (9 запросов, ~30 источников) был
достаточно исчерпывающим — если существует непроверенный узкий
источник именно про discrete-node multipole gravity + lensing, H2 не
"доказана" отсутствием находки, только правдоподобна.

**Rescue-Unfalsifiability check (H1):** конкретный falsifier — Этап
6/7 ниже: расчёт покажет ненулевую или нулевую вариансную/lensing
сигнатуру, оба исхода различимы, H1 фальсифицируема.

**Rescue-Unfalsifiability check (H2 — корректировка после skeptic
review, см. Correction выше):** предыдущая версия называла H2
"частично снятой" правкой Numeric-Threshold — скептик верно поймал, что
эта правка КОСМЕТИЧЕСКАЯ, а не решающая: критерий закрытия ("расчёт
сделан → H2 подтверждена ИЛИ снята") циркулярен относительно самого
текущего состояния — H2 УЖЕ "подтверждена" самим фактом, что этот
9-запросный поиск ничего не нашёл, что и было ЕДИНСТВЕННЫМ основанием
для её формулировки. Честный статус: H2 — это НАБЛЮДЕНИЕ о состоянии
литературы (расчёт для этого класса моделей действительно не найден в
проведённом поиске), не проверяемая repair-гипотеза в смысле Этапа 4 —
поэтому она понижена до Literature-Gap Observation (см. заголовок H2
выше), а не остаётся в реестре гипотез наравне с H1.

## Этап 5 — Неожиданное предсказание

**Если H1 верна:** MULTING's H(z)-fit quality (P166-P169) должно
оставаться высоким НЕЗАВИСИМО от того, как MULTING's growth/S8
предсказание выглядит — то есть можно найти публикуемые H(z)-модели с
ХОРОШИМ fit, где growth-канал не автоматически ухудшен, а СВЯЗАН
отдельным, explicitly построенным механизмом. **Корректировка
(skeptic-caught):** f(Q) square-root correction (`arXiv:2512.16551`) —
более слабый counter-example, чем в первой версии: он не "чисто
согласовывает σ8 на 1σ", а лишь ОСЛАБЛЯЕТ ограничение (вырождение,
более широкий допустимый диапазон σ8, с "остаточным вырождением").
Всё ещё поддерживает саму СТРУКТУРУ H1 (growth-совместимость требует
отдельного механизма, не следует автоматом из background-фита) — но
НЕ демонстрирует чистое разрешение, только частичное смягчение.

**Если H2 (Literature-Gap Observation) верна:** должен существовать
(или быть легко строимым) прямой расчёт "MULTING's own pairwise force →
aggregate matter power spectrum shift → predicted ΔS8" — если такой
расчёт УЖЕ где-то сделан для структурно похожего дискретного-pairwise
класса (не найден в этом поиске), это опровергло бы H2 как наблюдение
о состоянии литературы.

## Этап 6 — Attack

**H1:** сильнейший контраргумент, взвешенный НАРАВНЕ (не отложенной
заметкой — skeptic-caught, см. Correction) — MULTING's own zero-mean
result (`P154`/`P155`) может УЖЕ означать, что вариансный/
корреляционный вклад ТОЖЕ пренебрежимо мал (не только средний), если
сила достаточно быстро убывает с расстоянием и её знак/величина хорошо
"перемешиваются" на масштабах survey. Учитывая, что аналитический
ноль СРЕДНЕГО уже строго доказан (`P154`/`P155`), эта альтернатива
(H0-null: "и среднее, и дисперсия малы по той же симметрии") —
БОЛЕЕ ЭКОНОМНОЕ объяснение, чем H1 (который предполагает дисперсия
существенна, а среднее — нет), и не опровергнута здесь. Оба (H1 и
H0-null) требуют ОДНОГО И ТОГО ЖЕ недостающего расчёта (Этап 7) для
различения — ни один не предпочтён этим файлом.
**H2:** сильнейший контраргумент — возможно, weak-lensing-тест
ДЕЙСТВИТЕЛЬНО неприменим по масштабу/типу, и H2 — просто "мы не искали
достаточно" под техническим языком; см. Correction выше — этот риск НЕ
снят Numeric-Threshold правкой, поэтому H2 понижена до наблюдения, не
проверяемой гипотезы.
**Общий confounder для H1/H0-null:** S8-tension сама колеблется 2-4σ
между опросами (CFHTLenS/KiDS/DES/HSC) — любой будущий "decisive test"
против S8 наследует эту неопределённость independent of MULTING.

## Этап 7 — Решающий тест

Не самый дешёвый, самый различающий (Cheapest Differentiating Test
Protocol, `falsification-ladder.md`):

- **Independent variable:** MULTING's own pairwise dipole+quadrupole
  force `F^(1),F^(2)` (already fully specified numerically, `P169`'s own
  verified constants `M0,d0,β1,β2`), evaluated at the two-point
  correlation / power-spectrum level (NOT just isotropic mean, which is
  already known to be zero).
- **Dependent variable:** predicted shift `ΔP(k)` in the matter power
  spectrum, or equivalently a predicted `ΔS8`, from this force's
  variance/correlation contribution.
- **Controls:** compare against the SAME calculation with `β1=β2=0`
  (pure Newtonian monopole only — should reproduce standard ΛCDM
  clustering) as a negative control; and against `arXiv:2510.12551`'s
  own interacting-DM elastic-force calculation as a METHODOLOGY control
  (confirms the calculation technique itself, applied to a KNOWN
  published force, reproduces that paper's own reported sign/magnitude,
  before trusting it on MULTING's own force).
- **Expected outcome under H1:** a nonzero, calculable `ΔS8` exists,
  sign not predictable from the force's attractive/repulsive character
  alone (must be computed).
- **Expected outcome under H0-null** (§Этап 6's own equally-weighted
  alternative): `ΔS8` comes out negligible, for the same symmetry-type
  reason the isotropic mean is exactly zero — this row is the one that
  actually DISCRIMINATES, between H1 and H0-null, not between H1 and H2
  (corrected — H2 is a Literature-Gap Observation, not a competing
  numeric hypothesis; running this test resolves H2 only as a
  byproduct, by being the calculation whose absence H2 observed).
- **Full-row diagnosticity check (corrected):** H1 and H0-null give
  DIFFERENT, mutually exclusive predictions on this exact row
  (nonzero vs. negligible `ΔS8`) — genuinely diagnostic between them.
  H1 and H2 were never diagnostically paired to begin with (skeptic-
  caught, see Correction) — that framing is removed.
- **Falsification criterion:** if `ΔS8` under MULTING's own force is
  found to be many orders of magnitude below current S8-measurement
  precision (`σ(S8)~0.01-0.02` across current surveys), H0-null is
  favored and the weak-lensing channel is confirmed NOT currently
  decisive for this model — a legitimate, non-rescue outcome, not
  evidence the model is "safe" in any broader sense.

**Cost, and an honest limit on how "specified" this test actually is
(skeptic-caught addition):** the IV/DV/controls above name WHAT to
compute; they do NOT solve the actual hard step — embedding a discrete,
fixed-separation (`d0=45 Mpc`) pairwise force between point-like nodes
into a continuous power-spectrum/perturbation-theory framework has no
off-the-shelf recipe (standard PT operates on smooth density fields;
node population statistics — Poisson? halo-mass-function-weighted?
correlated with the matter field? — are not specified here; which PT
scheme — SPT, EFT of LSS, a modified Boltzmann code — is not chosen).
This is a research problem, not an implementation task; this
file stops at naming the problem, not solving it. Requires either (a) a
perturbation-theory calculation of the two-point contribution of a
pairwise force with MULTING's own radial form — method NOT sketched
beyond this — or (b) an N-body/simulation-based approach analogous IN
SPIRIT to `arXiv:2510.12551`'s own elastic-interaction methodology,
adapted to MULTING's specific force law. Not a quick script; this is
genuinely new numerical work, matching `activeContext.md`'s own prior
framing of Phase 3 as needing "significant new numerical work."

## Этап 8 — Novelty Check (inline — capped at "closely related" per skill's own rule, no separate delegation this round)

The GENERAL pattern (H0-S8 trade-off, background-growth decoupling) is
**documented** — extensively published, not novel as a cosmological
principle (see Этап 1 sources). The SPECIFIC application — computing a
discrete pairwise inter-node multipole force's power-spectrum/S8
signature for a MULTING-type model — is, as far as this search found,
**apparently novel but unverified** (no counter-example found despite a
9-query search spanning general modified-gravity-lensing literature,
cluster-fifth-force tests, and interacting-dark-sector growth papers) —
capped at this status per the skill's own rule since no dedicated
`/novelty-assessment` multi-round delegation was run this session.

## Финальный вывод

### 1. Главная аномалия
The class of model MULTING belongs to (extra-parameter, H(z)-only
calibrated Hubble-tension fixes) has a well-documented tendency to
conflict with an INDEPENDENT observable (structure growth / S8) that
its own calibration never sees — yet MULTING's own specific
zero-isotropic-mean property (`P154`/`P155`) is a structural feature
most literature examples don't share, and its consequence for the
VARIANCE-level (lensing-visible) signature has never been computed, by
this project or (as far as found) anyone.

### 2. Самый информативный кластер провалов
The H0-S8 trade-off cluster (`arXiv:2103.04045`, `2308.16183`,
Galaxies 14(2),16, EDE-vs-lensing) — a real, repeatedly-documented
pattern, mechanistically explained by background-growth decoupling.

### 3. Лучшая Repair Hypothesis
**H1 (Background-Growth Decoupling)** — MULTING's H(z)-fit success says
nothing, by itself, about its growth/lensing-level prediction, because
the two are governed by structurally different equations and MULTING's
own calibration (`P166`-`P169`) never touches the growth sector. This is
`[INFERRED]` from the general literature pattern plus this project's own
verified fact (`P154`/`P155`'s zero-mean result) — not established as a
numeric prediction for MULTING itself.

### 4. Неожиданное предсказание
A model's growth-sector fate is not automatically implied by a good
H(z) fit — escaping (or even just loosening) the H0-S8 trade-off
requires an EXPLICIT, separate growth-sector mechanism
(`arXiv:2512.16551`'s own f(Q) example — corrected: a partial
loosening of the σ8 constraint via degeneracy, not a clean 1σ
reconciliation) — MULTING has not been checked for whether it has (or
lacks) such a mechanism, or needs one at all (per H0-null, §Этап 6).

### 5. Решающий тест
Compute MULTING's own pairwise force's two-point (power-spectrum/`ΔS8`)
contribution — genuinely new numerical work, not yet attempted. The
WHAT is specified in Этап 7 (IV/DV/controls/falsification criterion);
the HOW (embedding a discrete pairwise force into a PT/N-body
framework) is a named research problem, not a sketched method —
honestly stated as unsolved, not glossed over.

### 6. Novelty status
General pattern: `documented`. MULTING-specific application: `apparently
novel but unverified` (inline check only, 9-query search, no dedicated
`/novelty-assessment` delegation).

### 7. Confidence (раздельно)
- evidence strength (general H0-S8 pattern): HIGH — multiple independent
  peer-reviewed sources, consistent finding.
- evidence strength (MULTING-specific application): LOW — no direct
  calculation exists for this project's own construction.
- novelty (of the MULTING-specific decisive test): MEDIUM — plausible,
  not independently verified via dedicated novelty search.
- plausibility (H1): MEDIUM-HIGH — grounded in an established general
  principle plus this project's own verified zero-mean fact.
- falsifiability: HIGH for H1 vs. H0-null on the decisive test's own
  row (Этап 7, corrected); H2 is no longer treated as a falsifiable
  repair hypothesis — relabeled Literature-Gap Observation precisely
  because its original "falsifier" was circular (skeptic-caught, see
  Correction).
- experimental tractability: LOW — requires genuinely new
  perturbation-theory/N-body work with no existing recipe for embedding
  a discrete pairwise force at fixed separation into a power-spectrum
  calculation; the method itself, not just the computation, remains to
  be designed (corrected from an earlier LOW-MEDIUM that implied the
  method was already sketched).

## What this file does NOT establish

1. **Not a claim about MULTING's own theory being confirmed or refuted**
   by weak lensing (`NO_AUTHOR_ERROR`) — no calculation was performed on
   MULTING's own force; this file only establishes the STRUCTURAL
   question is real and open, and sketches how to answer it.
2. **Does not compute a numeric `ΔS8` prediction** — Этап 7's decisive
   test is specified, not executed.
3. **Does not resolve whether MULTING's own zero-isotropic-mean result
   (`P154`/`P155`) implies a correspondingly small variance/correlation
   signature** — this is exactly the open question, not answered here.
4. **The literature search (9 queries, ~30 sources) is not exhaustive** —
   a narrower, unfound source specifically testing discrete inter-node
   multipole gravity against lensing would revise §Этап 8's novelty
   status.
5. **Does not address the S8-tension's own internal measurement
   controversy** (2-4σ oscillating significance across surveys) — noted
   as a confounder for any future decisive test, not resolved here.
6. **Does not carry forward `FINDING_P154`'s own full scope caveat**
   (skeptic-caught, added here) — `P154`'s own "does NOT establish"
   section notes its zero-mean result assumes a filled-ball uniform
   density and independent node orientations; a population with genuine
   spatial-orientation correlations was not excluded there, only
   physically argued against via CMB isotropy. A variance/correlation-
   level question (this file's own open item) can be MORE sensitive to
   residual orientation correlations than the mean was — this file does
   not re-examine that assumption.
7. **The class-level pattern (H0-S8 trade-off) and the MULTING-specific
   structural counter-consideration (zero isotropic mean) point in
   OPPOSITE directions, and this file does not adjudicate between
   them** — presenting H1 as "the" repair hypothesis, with H0-null only
   named in §Этап 6, risks reading as more settled toward "MULTING likely
   has the problem" than the evidence supports; the honest state is
   symmetric: a real pattern exists in the class, a real structural
   reason exists why MULTING might not share it, and nothing computed
   here decides between them.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
