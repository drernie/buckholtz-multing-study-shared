# docs/160 — docs/119 weaknesses map: status delta, 2026-06-17 → 2026-09-10
# Prepared by: Sergey Boyko (with Claude) · Ronin Institute
# Scope: what changed, per item, for docs/119's ~26 referee-style weaknesses
# NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
# Method: general-purpose Agent cross-check against the live repo (52 tool
# calls, Read/Grep only, no training-data assumptions), then independently
# spot-checked (docs/150 existence, F-2/MOND grep) before accepting.

---

## Why this file exists

`docs/119_weaknesses_referee_map.md` (2026-06-17) is a pre-mortem of ~26
referee-style weaknesses against TJB's v6 preprint and this project's own
reconstruction of it. Three months and a substantially expanded preprint
(v82, Zenodo 22004287) later, most of the items read differently — not
because this project "closed" them one by one, but because five structural
events happened in between and several items' underlying object changed
out from under them. This file is the delta, item by item, so a reader
does not have to re-derive it from `CURRENT_EVIDENCE_STATE.md` and 50+
individual findings.

## The five structural drivers (most of the movement below traces to one of these)

1. **v82's publication** — a real F_oP→H(z) bridge, real `r_A(z)`/`k_A(z)`/
   `m_A(z)` evolution laws, a real χ² fit (Table II) replacing v6's
   AI-prompt-derived Table A1. Does not mean "resolved" — TJB's own text
   self-flags part of this "Class III, circular" (`docs/149` §2), and this
   project's own follow-up (`FINDING_P196`→`P202`) found the mismatch is
   structural, not cosmetic.
2. **`table_a1_is_ai_output.md`** (2026-08-03) — TJB's own caption confirms
   Table A1 is "responses, to our prompt, by one online service that has
   bases in artificial intelligence," not a MULTING calculation. Closes/
   reclassifies C-1, C-2, F-1, F-7 in one stroke.
3. **TJB decoupled IDM from MULTING** (2026-09-02 email: "Perhaps best if
   you leave IDM out of your post... the MULTING aspects do not need
   IDM.") — does not technically resolve D-1 through D-5, but lowers their
   priority for anything author-facing.
4. **Methodology pivot from Pearson r to χ²** (`E5`-`E12`, `FINDING_P166`)
   — direct answer to B-7; recomputes B-1/B-2/B-4 more rigorously (similar
   non-support conclusion, now on honest statistics).
5. **`FINDING_P196`→`P202`** (cluster radius/mass proxy chain) — the
   deepest new characterization here: turns A-7/G-3's vague "TJB never
   confirmed R500" into a quantified, field-wide 10-150%+ mass-proxy
   disagreement phenomenon, not a local bug.

## Status delta, all items (B-3, G-1 already closed as of 2026-06-18, excluded)

| Code | June verdict | Status now | Evidence |
|---|---|---|---|
| A-1 | No Lagrangian/field eqs | **DEEPENED** | `docs/129` Q006 + `/hypothesis-arbiter` (2026-09-07): "unresolvable on current information"; `docs/130`/`131`, `FINDING_P204` — CANDIDATE-L1 internally inconsistent, FAILS on sign |
| A-2 | β_d/β_q free, 3 AI services disagree | **SUPERSEDED** | v82 §II.G: single χ² fit (`docs/149` §2), not AI-service outputs. New open Q: β1/β2/H0,anchor identifiability (`docs/150` §6) |
| A-3 | No F_oP→H(z) bridge | **SUPERSEDED** | v82 §II.B-C explicit bridge (`docs/149` §3, `docs/150` §0). Restated as bottleneck 1, still BLOCKED (`docs/153`) |
| A-4 | D=D0/(1+z) phenomenological | **SUPERSEDED+DEEPENED** | v82 Eq.11 supplies own r_A(z) via R500/ρ_crit(z) — TJB self-flags "Class III circular" |
| A-5 | 6 isomers, no symmetry group | **PARTIALLY ADDRESSED** | `parked/T5T6-cogenesis-5to1-isomer-structure.md` (corrected 09-08): OPEN not REJECT; deprioritized by IDM/MULTING split |
| A-6 | δ≈0.03668 fit, no derivation | **UNCHANGED** | no post-June file touches this |
| A-7 | r_A=R500 unconfirmed | **DEEPENED+RECOMPUTED** | `FINDING_P196`→`P202`: R500/R200/R2500 sensitivity quantified as field-wide phenomenon; `P199` confirms Δ=500 provenance |
| B-1/B-2 | monopole/trivial beat full formula | **RECOMPUTED** | E5-E12: `|Δχ²|∈[−1.3,+2.6]` — "no discrimination between MULTING and free ΛCDM in either direction," different method, similar verdict |
| B-4 | ΔAIC=+2.5 vs ΛCDM | **RECOMPUTED** | `FINDING_P166` on v82's own "fairer" benchmarks: ΔAIC≈1.2-1.4 (indistinguishable), ΔBIC≈2.7-2.9 (mild) |
| B-5 | n=22 unbiased sample too small | **PARTIALLY ADDRESSED** | work shifted to v82's N=33 CC+SH0ES+DESI set; original XMM n=22 test never expanded |
| B-6 | no error propagation | **PARTIALLY ADDRESSED** | χ² method is σ-weighted by construction; no explicit bootstrap CI added |
| B-7 | Pearson r insensitive to scale | **SUPERSEDED** | project adopted χ² as default (`experiments/20260910-moresco-bc03-vs-m11-refit/`) |
| C-1/C-2 | β_d mismatch across sources, ×4400 | **SUPERSEDED** | Table A1 confirmed AI output — nothing real to compare against |
| C-3 | implied β 100× above Gemini | **SUPERSEDED+DEEPENED** | `docs/150` §6 (`P163`,`P165`): "tier mismatch," not a units gap — v82's monopole has zero free coefficient |
| D-1 | ΔN_eff=88σ, no escape route | **CONTEXTUALLY SUPERSEDED** | IDM/MULTING decoupling (2026-09-02); technically untouched |
| D-2 | no Bullet Cluster σ_DM/m | **UNCHANGED** | no post-June file |
| D-3 | no DM isomer masses | **UNCHANGED** | T5T6 addresses structure, not masses |
| D-4 | "reach formula" one of four | **UNCHANGED** | no post-June file |
| D-5 | no 21-cm prediction | **UNCHANGED** | no post-June file |
| E-1 | m_Z² 5.5σ (C6) | **UNCHANGED** | no post-June file |
| E-2 | C9/Eq.32 numerology, no mechanism | **DEEPENED** | `CONSILIENCE_eq32.md` (3 methods converge non-support); Belle II 2023 m_τ: was 0.17σ, now 1.84σ; mechanism hunt exhausted (`NR-019/020/021/024`) |
| E-3 | inflaton 30.4 GeV, not at LHC | **UNCHANGED** | no post-June file |
| F-1 | App.A1 = AI prompt in paper | **CLOSED+SUPERSEDED** | `table_a1_is_ai_output.md`; v82 replaces with real χ² fit |
| F-2 | no MOND/MOG/f(R) comparison | **UNCHANGED** | independently grepped — all "MOND" hits are pre-June (`docs/06`) or unrelated substring matches (epi-registry test log) |
| F-3 | no rotation-curve test | **UNCHANGED** | no post-June file |
| F-4 | no BAO test | **UNCHANGED** | DESI z=2.33 used as an anchor point; no dedicated MULTING-BAO prediction test |
| F-5 | no strong-lensing test | **PARTIALLY ADDRESSED** | `parked/P170-weak-lensing-decisive-test.md` — adjacent (weak-lensing) route attempted, ARCHIVE, method missing not data |
| F-6 | no χ²/likelihood analysis | **SUPERSEDED+CLOSED** | v82 itself reports χ² (Table II); project reproduces + computes AIC/BIC |
| F-7 | "9/12 within σ_FLRW" (AI claim) | **CLOSED** | `table_a1_is_ai_output.md` directly explains why |
| G-2 | D=D0/(1+z) our hypothesis | **SUPERSEDED** | see A-4 |
| G-3 | β·radius not physically constrained | **DEEPENED+RECOMPUTED** | `FINDING_P196`→`P202` |
| G-4 | k_A scale mismatch ×1000 | **DEEPENED** | tier mismatch (`P163`/`P165`) + KG2 finding: Ag² degenerate with G itself |

## Genuinely untouched since June (honest gap list, not a to-do list)

**A-6, D-2, D-3, D-4, D-5, E-1, E-3, F-2, F-3, F-4** — no file, experiment,
or index entry postdating 2026-06-17 addresses any of these. Not claimed
as "still true weaknesses of MULTING" (`NO_AUTHOR_ERROR`) — only that this
project has not looked at them again in three months. Do not re-open
without a genuinely new reason, per this project's own stop-rule
discipline (`docs/147`).

## What this does NOT mean

None of the SUPERSEDED/CLOSED verdicts above mean MULTING itself is
correct or that TJB's own weaknesses are resolved — several come back
*deepened* (A-4, C-3, G-3, G-4) precisely because v82's own construction
self-admits circularity that this project's later work then quantified.
"Superseded" means the *object docs/119 criticized* changed, not that the
criticism was answered.

**Related:** `docs/119_weaknesses_referee_map.md` (the source list),
`CURRENT_EVIDENCE_STATE.md` (canonical live snapshot), `docs/150` (v82 vs.
reconstruction comparison), `table_a1_is_ai_output.md`.
