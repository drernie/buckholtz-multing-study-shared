# docs/132 — Open Bottlenecks: Task Backlog

**Date:** 2026-07-22
**Status:** LIVING BACKLOG — the full set of open bottlenecks, framed as self-contained
tasks. Derived from `facts.json` (R001-R011, Q001-Q006, blockers) + `docs/122`
(cosmological-branch verdict v1-v6). Update status column as tasks are attacked.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

## ⚠️ RECOMPOSITION NOTE (2026-07-23, after external adversarial re-review)
The per-task "RESOLVED" labels below mean **"the scoped computation/artifact is done"**, NOT "the
physics question is closed." The honest global summary: *9 tasks examined, hypothesis space
substantially narrowed, several initially-strong verdicts softened, and a next discriminating test
specified per branch.* A downstream verdict is never stronger than its weakest mandatory dependency
(e.g. T2/T7 inherit the missing covariant bridge; T5/T6 inherit the unspecified thermal history).
Confirmed catch from that re-review: the paper's ΔN_eff=106.8 was g* itself, not N_eff units —
fixed (commit 58307b7, →~61, factor ~80-215). Follow-up tasks T1.1-T9.1 (preregistered scan, RG
boundary test, cogenesis Boltzmann, measurement-error null, hierarchical FDR) are tracked in
activeContext; recommended order: T8.1 → T1.1+T9.1 → T3.1 → T5.1+T6.1.

## How to read this
- **Tier A** = self-attackable NOW, no TJB and no fitting-blocked dependency.
- **Tier B** = blocked on TJB or infrastructure; do not attack until unblocked.
- Each Tier-A task is a competition-style brief: Context → Task → Kill/Success → Resources → Guardrail.
- Priority (value × tractability × independence): **T1 > T9 > T2** are the strongest; see per-task notes.

---

## Tier A — self-attackable now

### T1 — Eq.32: physics or a 1-in-83160 coincidence? (second-prediction test) — PRIORITY 1
- **Context:** `(4/3)·(m_τ/m_e)^12 = α_EM/α_G`, verified to 0.06% [VERIFIED], rank #1 of
  83160 formulas, p~6e-5 (R001). The project's strongest result, outside the cosmological
  STOP. The 4/3 origin is [VERIFIED-ABSENT] across 4 literature niches. Discriminator
  (Q001): a genuine structure yields a SECOND independent prediction; a coincidence does not.
- **Task:** Derive + test a second, independent, falsifiable prediction from Eq.32's
  structure (4/3 prefactor + integer exponent + α_G link): (a) does the same template with a
  different SU(3) Casimir (C_A=3) on the muon / another lepton pair give another <0.1%
  relation? (b) does Eq.32 blind-predict a quantity NOT used in its construction? (c) broaden
  the look-elsewhere space (>83160, other coefficient forms) — does rank #1 hold?
- **Kill/Success:** No second prediction AND no broadened-space competitor → honest downgrade
  to "single-label coincidence". A second <0.1% prediction emerges → strong non-numerology
  evidence, promote.
- **Resources:** `/boyko-specialist`, `/hypothesis-arbiter`, reuse `scripts/scan_reference_mass_robustness.py`. ~half-day.
- **Guardrail:** NOT_VALIDATION (our audit, not TJB's derivation); no numerology-chaining (Q002 flag).
- **Status:** RESOLVED 2026-07-22 — verdict **coincidence-leaning** [VERIFIED-BASH, coordinator-reproduced].
  Prong 1 (second prediction): clean NULL — 0 of 5 dictated-Casimir companions sub-0.1% (best miss 36%);
  per the Q001 discriminator this is the coincidence signature. Prong 2 (look-elsewhere v2): rank #1
  holds in the baseline 83,160 space and the simple-coefficient space (14,520), but degrades to #3
  (420,750 trials) and #5 (841,500 with sqrt(p/q) forms) — uniqueness is search-space-dependent.
  Empirical p falls to ~6e-6 as pools grow (mechanical; rank loss is the load-bearing fact).
  Artifact: `scripts/t1_eq32_second_prediction.py`.
  **Tail CLOSED 2026-07-22 (T1b, coordinator-verified):** competitors identified & classified —
  1 ALIAS (sqrt(16/9)·(m_tau/m_e)^12 IS Eq.32 rewritten; the sqrt family double-counts it), all real
  beaters EXOTIC (17/11·(m_p/m_e)^13; 12·(m_c/m_u)^15 with MSbar quark masses ±20% at n=15 = spurious
  precision; sqrt(9/11)·(m_t/m_c)^20), ZERO genuinely-distinct simple rivals. Rank-loss = mechanical
  pool noise → verdict SHARPENED to coincidence-leaning; physics-leaning NOT reopened.
  Artifact: `scripts/t1b_competitor_id.py`.

### T2 — MULTING dipole: observational-viability window (NO fitting) — PRIORITY 3
- **Context:** Fitting-branch STOPPED (R011). Separate, unmapped question: is the dipole
  observationally ALIVE? If ≈ Blanchet-Le Tiec dipolar DM (0804.3518), it inherits [VERIFIED,
  digitized]: (a) Planck 2nd-order dipole-field constraints (1312.6991); (b) an exponential
  instability, marginally safe only because τ_g~6e10 yr > 1.38e10 yr. β non-identifiable → map
  the constraint as a FUNCTION of β/η.
- **Task:** Derive the allowed window: for what dipole amplitude (as a function of β/η) does it
  (i) violate the Planck 2nd-order constraint, (ii) go unstable within a Hubble time? Produce a
  "viability band" where the dipole is both non-negligible AND observationally alive.
- **Kill/Success:** Band empty → strong constraint for TJB. Band exists → target region for any
  future derivation.
- **Resources:** boyko-agent + `literature/refs_digitized/` (Blanchet) + Planck numbers. ~1 day.
- **Guardrail:** NO_BRIDGE_FITTING (do not fit Table A1/H(z)); NOT_REFUTATION.
- **Status:** RESOLVED-PARTIAL 2026-07-22 [mission run, coordinator-verified] — window ALIVE (instability edge amplitude-independent, tau_g>t_H by 4.3x; Planck s_eq<~1.5e-3 upper edge), but MULTING beta-placement BLOCKED on Q005 bridge. Artifact: scripts/t2_dipole_viability.py + boyko_T2_report.md

### T3 — The 7:9:17 boson mass-ratio: real pattern or coincidence? (the Z-tension)
- **Context:** `m_W^2 : m_Z^2 : m_H^2 = 7 : 9 : 17` (R002). Higgs fits at 0.4σ, but Z shows
  5.5σ tension — an unexplained internal inconsistency.
- **Task:** Rigorous look-elsewhere on small-integer triples (a:b:c) fitting the measured
  ratios within the 7:9:17 tolerance — where does 7:9:17 rank? Separately: is the Z-tension a
  known EW radiative correction (W/Z via ρ-parameter / sin²θ_W)? Does accounting for it rescue
  or kill the pattern?
- **Kill/Success:** Many triples fit equally → 7:9:17 not special. Standout + Z-tension maps to
  a known EW correction → pattern strengthens.
- **Resources:** PDG 2024/2026 masses (facts.json) + look-elsewhere scan + `/boyko-specialist` (EW).
  ~half-day.
- **Guardrail:** NOT_VALIDATION; honest trials-factor.
- **Status:** RESOLVED 2026-07-22 [T3 mission + T3b one-loop follow-up, coordinator-verified] —
  look-elsewhere rank #1 (next triple ~8x worse chi2); Higgs 0.4σ; Z-tension citable = +3.8σ
  (R002 reconciled: 5.5σ was the tighter-dW vintage). **T3b EW one-loop check: NULL (with PARTIAL
  character)** — the SM loop shift is right-signed and ~right-sized (0.008 vs the naive 0.009 gap)
  but LOOP-INVARIANT for the mass ratio: κ is multiplicative (shifts tree and measurement together),
  and the Δr budget is spent reproducing measured m_W (SM predicts 80.39-80.49; 7:9:17 needs
  Δr ~0.003 smaller). Residual +3.7-3.8σ under BOTH readings. NOT derivation-adjacent via SM loops.
  Weakest premise [WEAK]: residual is NOT m_W-choice-invariant — raw CDF-II m_W collapses it to
  −1.4σ (PDG down-weights CDF, defensible, but must be stated). SM-loop line EXHAUSTED; only live
  lever = future m_W world-average (watch PDG/CMS). Skeptic (context-asymmetric): [CONFIRMED-REAL].
  Artifacts: scripts/t3_boson_ratio_lookelsewhere.py, scripts/t3b_ew_oneloop_check.py,
  boyko_T3_report.md + boyko_T3b_ew_oneloop.md

### T4 — Is the monopole's dominance fundamental, or a bad quadrupole form? (R011 open)
- **Context:** R011 v6: monopole baseline (r=0.7334) beats every MULTING config (proven
  analytically). Open: is that because the monopole is fundamentally the best cluster→H(z)
  tracer, or because the specific `(k_A·r_A)^2/D^4` form is bad?
- **Task:** Test out-of-sample / by permutation whether ANY principled combination of
  (k_A, r_A, D, z) beats the monopole. Falsification framing — is the monopole>dipole>quadrupole
  ranking robust.
- **Kill/Success:** None beats → monopole-dominance robust (strengthens STOP). One beats → the
  quadrupole FORM, not the physics, is the culprit.
- **Guardrail:** ⚠️ NO_BRIDGE_FITTING — permutation/holdout discipline only, NOT a fishing
  expedition over Table A1. This is the most fitting-risky task; frame strictly as falsification.
- **Status:** RESOLVED 2026-07-22 [mission run, coordinator-verified] — REJECT-leaning, STOP strengthened: among 13 pre-specified forms even the best cluster-physics tracer loses to trivial (1+z)^2 (0.8904 ceiling); cluster apparatus adds only scatter; monopole>dipole>quadrupole ranking robust in both holdout splits; permutation p<=0.001; NO coefficient fitted. Artifact: scripts/t4_monopole_dominance.py + boyko_T4_report.md

### T5 — Is the 5:1 dark/baryon ratio a real relic prediction or arithmetic? (N=5 unequal-mass)
- **Context:** `Ω_DM/Ω_b = 5×1.074 = 5.37 ≈ 5.36` [NOT KILLED, conditional]. The match assumes
  n_i≈n_b per dark sector — needs a relic-abundance/reheating calc. Competes with mirror-DM
  (Berezhiani). Fresh lead: arXiv:2512.14119 (ADM mass ~ proton mass).
- **Task:** Compute the relic abundance for the 5-isomer IDM scenario under explicit reheating
  assumptions; does 5.36 emerge naturally, or need fine-tuned n_i? Compare to the mirror-DM
  explanation of the same 5:1.
- **Kill/Success:** Needs fine-tuned n_i → arithmetic coincidence. Emerges naturally → real
  prediction, promote.
- **Resources:** `/boyko-specialist` (ADM/mirror-DM). **Guardrail:** NOT_VALIDATION.
- **Status:** RESOLVED 2026-07-22 [mission run, coordinator-verified] — REJECT-leaning: hitting 5.36 needs n_i/n_b=1 to ~1.2% per sector with no mechanism in corpus; mirror/ADM DERIVES the same 5:1 (competing explanation). Tuned arithmetic unless TJB supplies an isomer-level relic derivation. COUPLED to T6 (see cross-cutting note). Artifact: scripts/t5_relic_abundance.py + boyko_T5_report.md

### T6 — Honest ΔN_eff exclusion for IDM dark neutrinos (R005 redo)
- **Context:** `ΔN_eff = 15-81` vs Planck `2.99±0.17`. The "130-477σ" figure is flagged as
  FALSE PRECISION (back-of-envelope Gaussian tail) — not citable externally.
- **Task:** Compute ΔN_eff properly for the 5-isomer dark-neutrino scenario against the real
  Planck+BBN likelihood; test the 3 escapes (different BBN chemistry / hidden sector / decoupling).
- **Kill/Success:** Excluded even under generous escapes → hard constraint. Escape exists → open door.
- **Guardrail:** honest σ, no false precision (direct lesson from docs/122 v2).
- **Status:** RESOLVED-PARTIAL 2026-07-22 [mission run, coordinator-verified] — honest exclusion: thermalized 5-isomer dark nu excluded by FACTOR ~50 (retire '130-477sigma' everywhere); early-decoupling (g*~107 dilutes to ~0.61) and grav-only escapes open the door. CROSS-CUTTING: T5<->T6 escapes are COUPLED — the non-thermality that rescues N_eff removes T5's equal-density basis; they cannot both be claimed. Artifact: scripts/t6_neff_honest.py + boyko_T6_report.md

### T7 — The distinguishing 2nd-order signature: does Euclid DR1 already decide? (Blanchet Window A)
- **Context:** Dipolar DM = ΛCDM at 1st order; distinguishable only at 2nd order (CMB
  bispectrum / non-linear LSS growth / cluster-scale). Planck already constrains the primordial
  dipole (1312.6991). [VERIFIED, digitized]
- **Task:** Identify which 2nd-order observable MULTING's dipole would produce, and whether
  current Euclid DR1 / Planck already bound it to a decisive level. (Complement to T2: T2 = the
  instability/constraint window; T7 = the distinguishing signal + is the data already here.)
- **Kill/Success:** Data already excludes → signal dead. Insufficient precision → name the
  dataset that would decide.
- **Guardrail:** ⚠️ derivation-first ALLOWED, but the action adaptation is "the author's to do";
  we do constraint-mapping, not derive the theory for TJB.
- **Status:** RESOLVED-PARTIAL 2026-07-22 [mission run] — distinguishing signal = post-equality-growing bispectrum non-Gaussianity (Blanchet 1210.4106); CMB channel already Planck-bounded (1312.6991); Euclid DR1 LSS products release ~mid-2027 so DR1 does NOT already decide; MULTING-specific prediction Q006-gated. Artifact: boyko_T7_report.md (literature, no script)

### T8 — The unexplained ICM partial correlation (R010 open)
- **Context:** `partial r(δ_M, E_ICM | M_WL) = -0.701` — robust, survived H1c/H1d falsification,
  unexplained. It is a cluster-ICM effect, NOT the cosmic-web WHIM mechanism TJB proposes. The
  main test (H1b, WHIM via IllustrisTNG) is TNG-login-blocked, but the puzzle itself is
  attackable on the CCCP N=50 data we already have.
- **Task:** On CCCP N=50, investigate WHY this partial correlation exists: known mass-observable
  systematic, selection effect, or genuinely unexplained?
- **Kill/Success:** Maps to a known systematic → explained. Survives → registered anomaly (pearl).
- **Guardrail:** do NOT present as TJB's mechanism (different observable).
- **Status:** RESOLVED-PARTIAL 2026-07-22 [mission + T8.1 null test, coordinator-verified,
  skeptic-reviewed] — R010 leans **artifact of definitional T_X-coupling**, MEDIUM confidence
  (downgraded from agent's self-reported MEDIUM-HIGH after an independent context-asymmetric
  skeptic pass): r=-0.70 collapses to -0.08 under T_X control (HSE identity δ_M=M_WL-M_hydro(T_X)
  verified exactly); T8.1 measurement-error null (20,000 catalogs, 2 independent generative
  models) places the observed -0.7008 at the 30-60th percentile of a null built from definitional
  coupling + real per-cluster errors alone — near-median, not tail. NOT TJB's WHIM mechanism.
  **Skeptic-confirmed non-issue:** the one NAMED physical confound that could break the null's
  exchangeability assumption — AGN feedback — was independently already tested with REAL data in
  experiments/20260713-h1e-agn-feedback-confound (KILLED: controlling for K0 changes |r| by only
  +0.0038, K0 orthogonal to both δ_M and E_ICM at fixed M_WL, p>0.5). **Skeptic-confirmed open
  gap (CODE-VERIFIED, not yet addressed):** the null's own HSE slope (b_hse) and (M_WL,T_X,M_gas)
  covariance are fit ON THE SAME 50 clusters whose r=-0.70 is being tested — a circularity that
  could launder undetected physics into the null via the covariance matrix. Cheapest next test:
  leave-one-out refit of b_hse, or an externally-calibrated HSE slope (e.g. X-COP), rerun the null;
  if the null median shifts by |Δr|>0.05, the artifact verdict is unsafe. Minor noted gaps: median-
  only (not per-cluster) error deconvolution in Variant A [WEAK]; Pearson-vs-Spearman outlier
  sensitivity untested; CC/NCC discriminator underpowered [WEAK, n=8]. **Flag:** the skeptic pass
  cited two memory-file links ([[feedback_inverse_problem_circularity]],
  [[feedback_reason_b_narrower_than_framed]]) that do NOT exist in this project's memory —
  confirmed phantom sources, disregarded per integrity.md; the code-grounded findings (Attacks 1-3)
  were independently verified against the actual script and stand on their own.
  Artifacts: scripts/t8_icm_partial_mechanism.py, scripts/t8b_measurement_error_null.py,
  boyko_T8_report.md, boyko_T8b_null.md.

### T9 — Joint look-elsewhere across ALL of TJB's numerical relations (meta) — PRIORITY 2
- **Context:** The project has several claimed relations (Eq.32, 7:9:17, N=5.36, + preprint).
  The #1 referee attack is the JOINT trials factor: impressive individually, but how many were
  tested?
- **Task:** A unified rigorous joint look-elsewhere — given all claimed relations, what is the
  joint probability they all hold by chance? Which survive Bonferroni/FDR correction?
- **Kill/Success:** Most wash out under joint correction → the program is trials-inflated. A core
  survives → THAT core is the defensible external claim.
- **Resources:** reuse `scripts/scan_reference_mass_robustness.py`. High value for external credibility.
- **Guardrail:** do this BEFORE any external submission of a numerical result — bring the referee
  the honest joint figure rather than receive it as an objection.
- **Status:** RESOLVED 2026-07-22 — **surviving core = Eq.32 alone** [VERIFIED-BASH, coordinator-reproduced].
  Of 7 named relations, only 2 have any usable p (R001 trials-corrected 6e-5; R004 raw); 5 are
  [UNKNOWN] (consistency checks, not detections). Bonferroni (dependence-safe): Eq.32 survives 0.05
  up to family size ~800 (m=7 → 4.2e-4). BH/BY FDR q=0.05: Eq.32 to m~100; fσ8 marginal (washes out
  m≥100). No precise joint p quoted — shared lepton masses violate independence; fabricating one is
  exactly the inflation the audit exists to prevent. Active misses stay on record: m_Z 5.5σ, ΔN_eff
  (orders of magnitude; "130-477σ" = flagged false precision). SCOPE caveat: surviving cross-relation
  correction (this task) ≠ surviving within-formula-space broadening (T1's rank #3/#5) — both facts
  go together. Artifact: `scripts/t9_joint_lookelsewhere.py`.
  **Tail CLOSED 2026-07-22 (T9b, coordinator-verified):** fσ8 trials-corrected p computed both ways —
  proxy-count Bonferroni K=6-13 [WEAK archaeology] → p∈[0.011, 0.023]; AR(1) smoothness-preserving
  surrogate null p=0.018 (plain permutation 0.0015 flagged OPTIMISTIC — breaks curve smoothness).
  Least-favorable defensible p ≈ 0.023 → fσ8 stays MARGINAL, now QUANTIFIED (survives 0.05, does not
  wash out, does not reach strong). Artifact: `scripts/t9b_fsig8_trials_p.py`.

---

## Tier B — blocked (do not attack until unblocked)

| ID | Task | Unblocked by |
|---|---|---|
| B1 | Q004 — β_d/β_q from first principles | TJB reply to docs/121 (BETA-1) |
| B2 | Q005 — numerical F→H(z) bridge | β values + bridge form |
| B3 | Q003 — what is "K²" (Discord 2026-06-30) | ask TJB |
| B4 | Chart Q2/Q5 — red-curve functional form; what fixes H0≈73 | TJB reply to the H(z)-chart letter |
| B5 | H1b — WHIM-filament test via IllustrisTNG | TNG API access (infra, not TJB) |
| B6 | MCMC / PREDICTION blockers | completed bridge |

---

## Summary
- **9 self-attackable** (T1-T9) · **6 blocked** (B1-B6).
- Every Tier-A task is a falsifier / space-narrower, not a builder — the correct convergent-contour
  posture when the divergent input (TJB) is blocked. A NULL here is as valuable as a PROMOTE.
- None violates NO_BRIDGE_FITTING / NOT_VALIDATION under the stated guardrails.
- Recommended attack order: **T1 → T9 → T2** (strongest, fully in our hands).
