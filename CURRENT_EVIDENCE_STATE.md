# Current Evidence State — buckholtz-idm-multing-mvp

**Date:** 2026-09-03; quality snapshot refreshed 2026-09-05, and
substantially revised **2026-09-07** (37 commits: bottleneck 3 dissolved,
KG2 answered, H1b parked and its criterion repaired — see §7) ·
**§7.3 updated 2026-09-09:** TNG-300 access granted; H1b's WHIM half
(`E_WHIM`) executed at real `N=71` (`r=-0.429, p<0.001`, mass vs. WHIM%);
`M_HE` (4th ingredient) still external, search closed across 9 channels ·
**Verified 2026-09-07:** `pytest tests/` **995 tests across 68 files,
exit 0, zero failures**, `mypy src` **0 errors / 39 files**;
earlier snapshot read `pytest` 908 passed,
`ruff check .` clean, `ruff format --check src tests` clean, `mypy src`
0 errors/38 files, coverage 91% (`src/double_inversion_plots.py` 100%,
`src/cluster_data_pipeline.py` 93% — the remaining 7% is `_vizier_
download`'s own real body, two hard-to-trigger ImportError fallbacks,
and main()'s astroquery-missing SystemExit path; see docs/155 for the
scope reasoning).
**Supersedes as the entry point:** `README.md`'s dated quality-snapshot
line, `PROJECT_STATUS.md` (already self-flagged superseded),
`.claude/memory/goals.md` (43× stale repeated pending item from 2026-06-12).
**Does not supersede:** `.claude/memory/activeContext.md` (still the live,
per-commit source of truth for "what are we doing right now" —
this file is the slower-moving strategic layer above it).

---

## 1. What is reproduced

- **F_oP bilinear structure** (docs/125, P1) — exact 2-species form,
  alternating-sign rule derived as a theorem for the two-charge
  completion, not postulated.
- **Isotropic-average k-sector = exactly zero** at force level
  (double-layer theorem, ~1e-16 numerically) and at Shtanov-Sahni
  background-coupling level, for any q(a).
- **Eq.32 numerical match** (**0.0608%, 1.00σ, PDG 2024 m_τ=1776.93±0.09** —
  corrected 2026-09-11, this line previously read `0.0135%`, a value this
  project's own `code/eq32_verify.py` stopped using on 2026-07-11 when it
  fixed a PDG-2022 value that had been mislabeled "PDG 2024"; the fix
  propagated to `README.md`/`docs/CLAIM_PROOFS.md`/`docs/BOOK/*` at the
  time but never reached this file, created 6 weeks later — the exact
  provenance/status-drift failure this project's own `docs/146` Category 11
  already names, now recurring a second time, this time in this file
  itself. Caught by an external RDR-style audit of the public reviewer
  copy, re-verified here by running `code/eq32_verify.py` directly)
  — `[VERIFIED-BASH]`, unaffected by everything below; only its
  *interpretation* is contested.
- **AVB benchmark solving arm** — N=32 corpus, both arms, full pipeline
  (skeptic + blind Run-3 + K5 reproducibility) — real bug found+fixed in
  a global hook (`agent_tool_scope_guard.py`) along the way.
- **Cen, Bahcall & Gramann (1994) Figure 3 recovery** — digitized,
  cross-validated to 0.057% against the paper's own Table 1 anchor;
  sent to TJB 2026-09-03.
- **P191: a Fisher-information forecast shows bottleneck 3's "in-
  principle openness" (P190) is practically buildable** — synthetic
  H(z) points at z∈{3,5,7,10} would shrink v82's own (β1,β2) degeneracy
  ellipse by 73%/46%/14% at 1%/3%/10% assumed relative precision
  (MCID met at all three, though only marginally at 10%). A real bug
  (sparse-grid integration silently zeroing one point's Fisher
  information) was caught and fixed by a context-blind Step 8a skeptic
  pass before this number was trusted — see docs/145-style correction
  in `FINDING_P191` itself. Side finding: the (β1,β2) level-set slope
  peaks near z≈3 and *declines* thereafter — not monotonic, not simply
  saturating, as `CLAIM_P191`'s own outcome table had anticipated.
- **P192: TJB's own real fitted (β1,β2) make H²(z) go negative
  (mathematically undefined) at z≈16.957** — grid-converged (4
  densities), straddle-confirmed, skeptic CONFIRMED-REAL. The
  reconstructed model cannot even be evaluated past this boundary,
  regardless of what question is being asked there — a standing
  precondition for any future high-z work on this reconstruction, not
  a one-off caveat.
- **P193: the P191 pearl's own prediction is CONFIRMED** — z∈{12,14,16}
  gives up to **5.4× more** shrinkage than P191's own z∈{3,5,7,10} at
  matched precision (72.87% vs 13.6% at σ=10%, both finite-difference,
  apples-to-apples). Separate real methodological finding: standard
  finite-difference Hessian computation (this project's default since
  P176) does not converge at σ∈{1%,3%} this close to P192's found
  boundary — resolved with an independent analytic Fisher matrix,
  cross-validated at 0.1% agreement in the one case both methods reach.
  Two rounds of context-blind Step 8a skeptic review, both real issues
  found and fixed (a 100% unit-conversion bug; a methodological gap in
  the cross-validation's own scope).
- **`docs/156` + `FINDING_P195` (bottleneck 1, causal-compatibility
  sub-question)**: `docs/153`'s own §3a preconditions, checked against
  pre-existing same-day prior work it did not cite, show its literal
  "finite-r/single-pair calculation" is not buildable (`docs/126`'s
  proven non-uniqueness lemma + two independent prior BLOCKED/
  FALSIFIED attempts, `docs/124`/`docs/125`). The mechanically-correct
  alternative (`FINDING_P157`'s Jensen's-inequality reframing,
  `FINDING_P158`'s calculation, `ADDENDUM2`'s real halo-mass-function
  grounding) gives a real result for `z≤0.5`: population-averaging
  favors `F^(2)` over `F^(1)`, via a computed `ρ>0`. `FINDING_P195`
  stress-tested that result's sensitivity to an arbitrary population-
  floor choice — sign/threshold-robust, magnitude varies up to ~30×
  across tested alternatives (Step 8a skeptic-caught, honestly reported
  rather than smoothed into a bare "robust").
- **`FINDING_P196` (new thread, separate from the 4 named bottlenecks
  — TJB's own letter, 2026-08-30, pointing at v82 Section II.F's
  Class III circularity)**: an independent rebuild of a comparison
  first attempted in a different, inaccessible chat session (Girardi
  1998's velocity-dispersion-only `R_vir` vs a `ρ_crit(z)`-based
  radius, on 123 real HeCS-SZ clusters). The correlation reproduces
  robustly (`r≈0.88`), but the prior session's own headline "mean
  ratio 1.128" could **not** be reproduced — this session's rebuild
  gives 1.61 (Δ=200, matching the prior session's stated method) or
  2.49 raw / 1.47 after correction (Δ=500, v82's own actual stated
  target). Strong circumstantial arithmetic (`1.61×h(0.7)=1.127`)
  suggests the prior number had a units bug plus a wrong overdensity
  target — not certain, since that session's code no longer exists.
  **Not ready for TJB** — the corrected 1.47× residual is itself
  unexplained. See `CLAIM_P196`/`FINDING_P196`.
  **`FINDING_P196_ADDENDUM` (same day)**: propagated Duffy et al.
  (2008)'s own quoted concentration scatter (`σ(log₁₀c)=0.15`, Monte
  Carlo, `N=2000`/cluster) through the shape-correction step — explains
  essentially none of the residual (mean shift `=0.0000`, exactly as
  predicted; `0.1%` of the `11.1%` scatter, vs a `30%` materiality
  threshold). A clean null result, ruling out one specific candidate.
  Remaining candidate, not yet tested: Duffy et al.'s own Fig. 4 shows
  real X-ray-observed cluster concentrations run systematically
  *higher* than their simulated median — a one-directional bias, not
  scatter, which this check could not address.
  **`FINDING_P196_ADDENDUM2` (same day)**: substituted two real
  X-ray-measured concentration relations (Buote et al. 2007, Schmidt &
  Allen 2007) for Duffy et al.'s simulated median — both confirm the
  documented direction (real `c` runs 2-3.4× higher), but the final
  ratio barely moves (`1.4665→1.4703→1.4747`, `<0.6%`). A Step 8a
  skeptic pass found the mechanistic reason: `P196`'s own `ratio_2b`
  formula algebraically cancels `R500` entirely, reducing to
  `r_vir_2a/R178` — no concentration source could have moved it much,
  by construction. **Concentration (scatter and source) is now
  structurally ruled out** as an explanation for the residual — next
  candidates are `M200c`'s own measurement systematics or Girardi's
  own intrinsic scatter, not concentration modeling.
  **`FINDING_P197` (same day)**: tested candidate 1 (mass-measurement
  systematics) using HeCS-SZ's own second, independent mass column
  (`MSZ`, Planck SZ). A real Δ=200-vs-Δ=500 bug was found and fixed
  (`[VERIFIED-arXiv:1507.08289]`). Result: `M200c` and `MSZ` disagree
  by a real, large, unexplained `2.5×` — and substituting `MSZ` moves
  the downstream ratio closer to `1.0` (`1.4665→1.1710`) but **still
  fails the pre-registered MCID band**, and the shift is mostly
  explained by simple mass-rescaling arithmetic, not validated new
  physics (a second skeptic pass caught this too). Candidate 1: real
  effect, does not close the gap.
  **`FINDING_P198` (same day)**: tested candidate 2 (Girardi's own
  internal `R_c` inconsistency — their published formula used an
  earlier paper's `R_c=0.17 h⁻¹Mpc`, while their own improved
  centering method, same 1998 paper §4.3, finds `R_c=0.05`). Result:
  real `~14%` shift (`ratio_2b` `1.4665→1.2587`), still outside the
  MCID band. A skeptic pass found this substitution is a `~3.3×`
  extrapolation beyond where the underlying formula was calibrated,
  and that the 123-cluster re-run is arithmetically predetermined by
  the single coefficient ratio — reframed honestly, not presented as
  independent confirmation. **Both named candidates (1 and 2) are now
  tested: each real, neither sufficient alone. The `1.47×` residual
  remains substantially unexplained.**
  **5-step autonomous follow-up (same day, explicit go-ahead: "го все
  по очереди автономно"), `P199`-`P202`:** `FINDING_P199` (Gate 1/2
  provenance re-check) confirmed the `Δ=500` target is genuinely
  grounded in v82's own text (not a handoff misattribution), and found
  TJB's own paper already self-flags this radius construction as
  "Class III, circular... the most serious residual dependence."
  `FINDING_P200` (literature search) found a real, same-research-group,
  quantified caustic-mass sparse-sampling bias (Logan et al. 2022,
  `M_X/M_C=1.12` best case) — directionally consistent, direct
  within-dataset test `BLOCKED-INFRASTRUCTURE` (no real galaxy-count
  column available). `FINDING_P201` — a genuinely new hypothesis found
  by connecting two prior findings — tested real X-ray concentration in
  `P197`'s own `MSZ→M200` conversion step: real, mechanistically
  confirmed, MCID-crossing for one of two sources (Schmidt&Allen+07,
  robust to a skeptic-identified extrapolation confound, re-tested on a
  restricted sub-sample), but a second, more consequential skeptic
  finding shows scatter (`74.5%`, dominant component of the residual)
  is **structurally invariant** to any population-mean concentration
  correction — such corrections can only ever move a mean, never touch
  per-cluster scatter. `FINDING_P202` (synthesis: claim-decomposer +
  macro-locality applied to `P196`-`P201`'s accumulated evidence)
  concludes **`PART-OF-MACROSYSTEM`**: four independent, non-MULTING
  cluster mass/radius/concentration proxy comparisons this project
  produced (caustic-vs-SZ `2.5×`, caustic-vs-hydrostatic `1.12×`,
  concentration-source choice `15-32%`, Girardi-vs-NFW `1.47×` itself)
  all disagree by comparable, real amounts — the residual is best read
  as an instance of a well-documented, field-wide phenomenon (cluster
  mass proxies routinely disagree at the `10-150%+` level), not a
  local bug or a MULTING-specific anomaly. Six candidate mechanisms
  now tested total across `P196`-`P201`; none closes the gap alone.
- **New thread (same day), `experiments/20260906-evidence-authority/`,
  `E1`-`E4`: TJB's own 2026-08-30 invitation to develop "de-conflating
  evidence from authority" as an independent line (v82 §II.F cited as
  one example — see project memory `project_tjb_evidence_authority_
  invitation_20260830.md`).** `E1` found the topic is a mature,
  decades-deep cosmology subfield (Visser's "cosmography," Clarkson/
  Bassett/Lu FLRW-consistency tests, distance-duality-relation tests) —
  not open ground. `E2` found a SECOND circularity, self-diagnosed by
  TJB in his own Section IV.M: `H₀,anchor = ṡ₀/s₀`, an attempted
  direct-data grounding gives `~11 km/s/Mpc` (implausible), because the
  peculiar-velocity data used already assumes an `H₀` to subtract the
  Hubble flow first — TJB's own words, "circular in the same sense" as
  `r_X(z)`. `E3` tested whether TJB's own "not fixable" verdict on this
  is too strong; a Step 8a skeptic pass found one real, scale-matched
  structural exception (kSZ's velocity channel, real ACT-collaboration
  data at `30-230 Mpc`, overlapping the needed scale) but showed it
  relocates rather than removes the assumed-cosmology dependence — a
  second candidate (redshift drift) was FALSIFIED as a counterexample
  and withdrawn (wrong observable, wrong regime). `E4` completed the
  Class I/II/III map of v82's inputs and found TJB's own THIRD named
  limitation (`β₁`/`β₂` near-cancellation, v82 p.33) is not new ground
  for this project — `P133`/`P176`/`P190`-`P194` already constitute a
  substantial, tool-verified body of work on exactly this item.
  **`E5`-`E8` (same day, second option set):** `E5` measured that
  switching only the stellar-population model on Moresco's own two
  published tables shifts CC `H(z)` by a uniform `+6.80%` (12/15 points,
  spread `0.99` pp) — inside the community's own `8.91%` modelling
  budget, which is `100%` correlated across bins and NOT in `errHz`;
  neither v82 nor this project used it. **`E8` propagated that
  covariance through `P176`: the `(β₁,β₂)` small eigenvalue drops
  `4.0-7.6×` while the large one drops `9%` — `P190`'s degeneracy
  DIRECTION stands (`+0.6%`), its SEVERITY was understated `4-8×`;
  `P191`-`P194`'s forecasts sit on a baseline that optimistic (rerun
  named, not done).** The `21.2` χ² gap vs fixed Planck ΛCDM is
  `+22.03` from SH0ES alone, `−0.76` from the 31 CC points — quantifying
  v82's own reading. A sign flip vs free ΛCDM fired, survived
  re-optimisation, then was **demoted by the skeptic's kill test**: on
  Moresco's own 15 points MULTING keeps `+1.2`; the flip needs the 16
  non-Moresco points, which disagree with his 15. Robust statement:
  `|Δχ²| ∈ [−1.3, +2.6]` on `15-31` dof — **no discrimination between
  MULTING and free ΛCDM in either direction.** `E6`-`E7`: two-field
  classification (avoided/incurred), 3 external examples, one exact
  cross-domain match (LLM-as-judge); novelty check found the framework
  is NOT new (theory-ladenness, Doboszewski & Elder 2025) — only the
  `+6.8%` measurement is ours. **`E9`:** `provenance_audit` run over
  v82's full 10-input chain — `CIRCULAR=2` (both TJB's own diagnoses,
  re-derived), `OUTSIDE_SIGMA=1` (CC), `UNQUANTIFIED=6`, clean `1`
  (SH0ES, the input carrying the model gap). **`E10`:** the SNe-Ia
  two-fitter example is `BLOCKED` on data — VizieR's `DMe` column is a
  sample-combination modulus, not SALT-II (ReadMe + opposite `z`-trend
  to Kessler's own mechanism), and no `m_B` exists to reconstruct it;
  stays a citation (`w=−0.76` vs `−0.96`, Kessler+2009). The near-miss
  (a wrong number with the right sign) was caught by reading the column
  definition — same discipline that caught `E3` and `E5`. **`E11`
  (rerun `P191`-`P194` against `E8`'s baseline):** at `σ_synth≤10%`
  (their own grid), forecasts are numerically robust (factor `~1.001`,
  ranking unchanged) — but a skeptic pass showed this is ONE mechanism
  (synthetic Fisher information dominates the baseline `100-10,000×`),
  not two confirmations, and does NOT undercut `E8` — different regime.
  Exploratory wider scan (`σ=30-100%`, no `z~12-16` program exists on
  any roadmap): factor grows monotonically to `1.24-1.29×` by `σ=100%`
  — `E8`'s correction matters *more*, not less, at realistic precision.
  **`E12`** (does the `E8c` sign-flip reflect a real CC inter-group
  tension?): Moresco's 15 vs the other 16 give `H₀=66.8` vs `72.4` —
  visually large, but joint 2-param test gives `Δχ²=0.65` (threshold
  `6.18`) — **not material**, ordinary small-sample scatter, not a
  documented inconsistency. **`E13`** (option B, one of `E9`'s six
  `UNQUANTIFIED` deps measured): v82's gas-mass/thermal-energy input
  (Eq.13-14, cited to Ramos-Ceja+2025) carries a real `σ=0.49` ln-normal
  scatter (`-39%/+63%`, `4-7×` larger than `E5`'s CC finding), never
  quoted by v82, and — v82.md:332 — feeds directly into the same
  dipole/quadrupole (`β₁`,`β₂`) terms `E8`/`E11` already flagged.
  **`E14`** (novelty check on `E6`): `closely related`, not novel —
  Doboszewski & Elder (2025) already publish a richer 5-strategy
  taxonomy for exactly this problem; this project's own contribution is
  the concrete measurements (`E5`, `E13`), not the classification idea.
  **`experiments/20260910-moresco-bc03-vs-m11-refit/` (2026-09-10, runs
  `E5`'s own named-unrun computation, directly answers TJB's 2026-09-09
  question about table-switch sensitivity):** propagated the BC03↔M11
  table swap through this project's own `chi2_fixed_h0anchor`
  reconstruction (positive control PASS, reproduces TJB's Table II to
  `<=0.01` in χ²). Full 15-point swap: `Δχ²=-5.91` — MATERIAL by this
  project's own `MCID=2.0`. But that verdict is carried almost entirely
  by 2 of 15 points `E5` itself already flagged as carrying an
  *unverified* confound (method difference vs SPS choice at `z>0.7`,
  still unchecked) — excluding just those 2 points, `Δχ²=-0.585`: NOT
  MATERIAL. `H0_anchor` barely moves either way (`+0.04` to
  `+0.13 km/s/Mpc`); `β1`/`β2` shift `18-26%` in both versions,
  consistent with (not new proof of) the project's own known `β1`/`β2`-
  vs-`H0_anchor` degeneracy (`P176`). **Same day, follow-up:** re-ran both
  the full swap and the 13-clean-point check under Moresco's own full
  correlated systematic covariance (reusing `E8`/`E8b`'s own positive-
  control-verified machinery) instead of diagonal `σ_Hz` — verdict
  unchanged either way (every `Δχ²` within ~3% of its diagonal
  counterpart, both covariance-structure variants tested). The MATERIAL/
  NOT-MATERIAL crux was never about diagonal-vs-covariance error
  treatment; it is entirely about whether the 2 flagged excursion points
  are trusted. **Same day, closed:** traced the caveat's real source via
  the BC03 table's own `reference` column to Moresco et al. 2012
  (`[VERIFIED-arXiv:1201.3609]`), not the 2020 covariance paper. Read its
  method sections directly: one fitting procedure applied identically to
  both compared models ("BC03"/"MaStro" — numerically confirmed to be the
  model later renamed "M11," matching the CCcovariance repo's values to
  3 sig figs), no z-dependent switching. The paper self-reports, verbatim:
  "agreement with a mean difference of 0.5±0.4σ, except for the last
  point where there is a difference of 1.6σ" — independently recomputed
  from its own Table 1, `z=1.037` gives `1.64σ` (exact match to its own
  flagged outlier), `z=0.7812` gives `~1.04σ`. **Verdict: not a
  fit-method confound — real, author-acknowledged SPS sensitivity
  concentrated at the highest-`z`, smallest-sample point.** Full-15 vs
  clean-13 is "complete dataset" vs "authors' own tightest-agreement
  subset," both legitimate; this closes `E5`'s caveat without picking one
  reading as "correct." See `FINDING_moresco_table_sensitivity.md`.
- **P194: a dense information-profile scan of the (10,16.957) window**
  confirms `CLAIM_P194`'s falsifiable predicate (monotonic rise toward
  the boundary, 16.24%→75.12% shrinkage at σ=10%) and directly confirms
  its own pre-written correction that greedy top-N points are not
  guaranteed jointly optimal — P193's specific {12,14,16} beats the
  naive greedy top-3 at tight precision (1%, 3%) and loses narrowly at
  loose precision (10%), a real mixed result, not a clean win either
  way. A second, more targeted Step 8a skeptic pass (round 2, same day)
  found round 1's own fix incomplete: the rise is **not** uniquely a
  1/H(z) boundary-singularity effect — measured directly, cumulative
  E1(z)/E2(z) growth (2.3-2.4×) and 1/H(z)² boundary-proximity growth
  (7.0×) are comparable order of magnitude, both real, neither
  negligible. P193's own numbers are unaffected; only the mechanism
  attributed to them is now honestly qualified as entangled, not
  resolved. See `FINDING_P194`.

## 2. What is refuted or weakened

- **P189 finite-r shortcut** — REJECTED (category error, tautology).
- **P189b normalized derivation** — WEAKENED (normalization is a
  convention choice, not physically forced).
- **P158-ADDENDUM literature grounding** — REJECTED (real citations,
  wrong quantities — measurement-scatter ≠ population-spread).
- **P158-ADDENDUM2 real hmf/Tinker computation** — WEAKENED (correct for
  4 of 8 target redshifts; the other 4 extrapolate past the fit's own
  calibration range).
- **P190: v82's own (β1,β2) degeneracy is APPROXIMATE, not exact**
  (12.7% spread in the level-set slope across z) — skeptic CONFIRMED-REAL.
  Rules out the strongest "structurally unbreakable" reading of
  bottleneck 3, without providing a practical fix.
- **NR-020: Eq.32's timing-axis numerology criterion (H1) FALSIFIED**
  by a real historical counter-example (Balmer 1885) — a DoF-ratio-based
  fallback survived only as an unattacked hypothesis.
- **NR-021: the DoF-ratio criterion (H1') hit two independent problems**
  before power was even the binding constraint — real N=11 (not the
  needed ~60), and a blind inter-rater check found the primary predictor
  itself is coder-dependent (2-6× divergence on identical facts).
- **CONSILIENCE_eq32.md:** three independent methods (formal derivation,
  statistical null-model, real experimental check) converge on
  non-support for Eq.32 as a genuine relation — **and surfaced a real
  correction mid-synthesis**: Belle II already measured m_τ in 2023
  (1777.09±0.08±0.11 MeV), giving **1.84σ tension** with Eq.32's exact
  prediction (1776.840 MeV) — ambiguous, not decisive. `paper/main.tex`
  synced with this finding 2026-09-03.

## 3. What changed after v82

- The 2026-08-23 framing "no published F→H(z) bridge exists" is
  `OLD-FORMULATION-SUPERSEDED` — v82 publishes an explicit accretion-
  kinematics bridge with `m_A(z)`, `r_A(z)`, `k_A(z)` (docs/149, docs/153).
- This does **not** mean the bridge is validated or that bottleneck 1 is
  closed — it means the *precondition for asking the question* changed.
  The restated, still-open question: is this project's own isotropic-
  average Shtanov-Sahni closure compatible with v82's finite-r,
  single-pair construction? `docs/153` §3a names 3 preconditions; none
  were resolved on 2026-09-01 (4 attempts that day, all REJECT/WEAKENED
  — see §2).
- **`docs/156` (2026-09-05) checked `docs/153`'s own §3a preconditions
  against prior work `docs/153` itself did not cite** (`FINDING_P157`/
  `P158`, same day as `FINDING_P156`, predating `docs/153`). Finding:
  `docs/153`'s own literally-proposed "finite-r/single-pair calculation"
  (comparing an intermediate quantity via v82's route AND this
  project's own S-S closure route) is **not buildable** — the project's
  own S-S closure route has no closed-form finite-r analog, independent
  of v82, proven by `docs/126`'s own non-uniqueness-of-closure lemma
  (no evolution law for `q_i=k_i r_i` exists in the corpus) and
  confirmed by two prior independent attempts (`docs/124` FALSIFIED,
  `docs/125` BLOCKED). The mechanically-correct alternative
  `FINDING_P157` identified — Jensen's inequality on v82's own
  mass-derived scalar chain — was already built (`P158`) and partly
  literature-grounded (`ADDENDUM2`, real `ρ>0` for `z≤0.5`).
  `FINDING_P195` (same day) then checked that `z≤0.5` result's own
  sensitivity to an arbitrary population-floor choice: sign- and
  threshold-robust (never approaches `P158`'s `ρ>−0.5` decision
  boundary), but the magnitude varies up to ~30× across tested floor
  choices — reported honestly, not smoothed over.

## 4. Four open bottlenecks (per `docs/147`)

| # | Bottleneck | Status | What would move it |
|---|---|---|---|
| 1 | F→H_MULT(z) bridge | BLOCKED (restated 2026-09-01, `docs/153`); `docs/153`'s own literal next-step disproven as buildable, `docs/156` (2026-09-05) — mechanically-correct alternative line (`P157`→`P158`→`ADDENDUM2`→`P195`) gives a real, narrow, `z≤0.5`-only, magnitude-uncertain result. **The `z≥1.07` extension was ALREADY ATTEMPTED 2026-09-06** (`FINDING_P195_ADDENDUM_high_z_bias_literature_search.md`, bounded 2-query arXiv search, `SOURCE_NOT_FOUND`) — v82's own `z≥1.07` target points sit at peak height `ν≈10.6-50`, structurally beyond what any finite-volume N-body suite (Tinker+2010, Aemulus IV) can calibrate — a real physical reason, not just an unlucky search | Genuinely stalled on this line without new input: either a more exhaustive literature search (N-body pair-statistics papers, not bias fits) or an explicit decision to attempt a specialized N-body calculation outside this project's own tooling — **do not re-attempt the same literature-search pattern without a new candidate paper named first** (Adaptive Iteration Branch Rule) |
| 2 | Unique completion | Untouched, `docs/134`. **2026-09-07:** `/hypothesis-arbiter` on the dipole's ontology (`H_body` / `H_fluid` / `H_avg`) returned only the LEAST falsifiable survivor and recommended **stopping** structural computation rather than iterating. Recommendation taken. | A genuinely new input, not another variant |
| 3 | Absolute scale / observable mapping | **DISSOLVED 2026-09-07 (`FINDING_P206`)** — it was never a measurement gap. `P133`'s rank-2 result IS the one-dimensional **field-normalization redundancy** `FINDING_P52` had already derived on 2026-08-16; `P133` renamed it 8 days later and made it a bottleneck without connecting the two. `L := 2a−b−c` is the field-rescaling weight, the null direction `(−1, ½, ½)` is the `φ→λφ̄` generator, so rank 2 is **complete**: 3 coordinates, 1 redundancy, 2 physical d.o.f., all determined. Step 8a run twice with reworded prompts, both CONFIRMED-REAL. *(Prior text, kept: "STRUCTURALLY BLOCKED, quantified buildable path exists…" — the P191-P194 Fisher-forecast line is unaffected and still stands on its own terms.)* | Nothing — the question as posed had no solution and needed none. **What remains open is `P52`'s own KG2**, answered as far as data allows on 2026-09-07 (`P208`/`P209`, §7): both physical invariants are unmeasurable, each for a *different* structural reason |
| 4 | IC-sensitivity | CLOSED (campaign exhausted, question genuinely open) | A genuinely new mechanism class, not a 6th variant of the 5 already excluded |

## 5. One next differentiating test

**DONE 2026-09-05, with an explicit user go-ahead** — `FINDING_P191`.
Result: adding synthetic H(z) points at z∈{3,5,7,10} would shrink the
(β1,β2) degeneracy ellipse by 73%/46%/14% at 1%/3%/10% assumed relative
precision — MCID (≥10% shrink) met at all three, marginally at 10%.
Does **not** resolve bottleneck 3 (no real high-z data exists; the
absolute-scale/observable-mapping question, `docs/134`, is untouched) —
it shows the "in-principle openness" P190 found is practically
buildable, and quantifies the cost/benefit as a function of assumed
precision.

**DONE 2026-09-05 (same day), with an explicit user go-ahead** —
`FINDING_P192`. The requested second Fisher-forecast at z∈{20,30,50}
was **TASK_INFEASIBLE as specified**: TJB's own real fitted (β1,β2)
make `H²(z)` go negative (mathematically undefined) at z≈16.957 —
grid-converged, straddle-confirmed, skeptic CONFIRMED-REAL. All three
requested z sit past this boundary. Does not falsify P191's own pearl
prediction (the test that would confirm/deny it was never constructible
at these z) — it identifies a prior domain-of-validity constraint any
future z-choice past P191's z≤10 must respect.

**DONE 2026-09-05 (same day), with an explicit user go-ahead** —
`FINDING_P193`. z∈{12,14,16} gives up to 5.4× more shrinkage than
P191's own z∈{3,5,7,10} at matched precision — the P191 pearl's own
prediction CONFIRMED, more strongly than its own wording required.
Surfaced a real, separate methodological finding along the way:
standard finite-difference Hessian computation does not converge at
σ∈{1%,3%} this close to P192's found boundary — resolved with an
independent analytic Fisher matrix, itself cross-validated to <0.15%
agreement wherever finite-difference converges.

**DONE 2026-09-05 (same day), with an explicit user go-ahead** —
`FINDING_P194`. A dense scan of the full (10, 16.5) window confirms the
information profile rises monotonically toward the boundary (16.24%→
75.12% shrinkage at σ=10%) and directly confirms the claim's own
pre-written correction: the greedy top-3/top-4 set does **not**
uniformly beat P193's {12,14,16} — it wins at loose precision (σ=10%)
and loses at tight precision (σ=1%,3%), a genuinely mixed result. A
second, more targeted Step 8a skeptic pass found the rise is **not**
uniquely a 1/H(z) boundary-singularity effect as a first fix suggested
— measured directly, cumulative E1(z)/E2(z) growth (2.3-2.4×) and
1/H(z)² boundary-proximity growth (7.0×) are comparable order of
magnitude. P193's raw numbers are unaffected; the causal story behind
them is now honestly qualified as entangled among ≥3 co-varying
candidates, not resolved to one.

**Bottleneck 1, separate line — DONE 2026-09-05, with an explicit user
go-ahead** ("начни финитно-r/single-pair расчёт по docs/153 итд
автономно"), reinterpreted per `docs/156`'s own precondition check —
`docs/156` + `FINDING_P195`. `docs/153`'s literal proposed calculation
is not buildable; the mechanically-correct alternative line
(`P157`→`P158`→`ADDENDUM2`→`P195`) gives a real, sign-robust,
magnitude-uncertain `z≤0.5`-only result. **[UPDATED 2026-09-09] ALREADY ATTEMPTED, NULL, NOT A LIVE NEXT CANDIDATE**
— this file previously called the `z≥1.07` extension "recommended, not
authorized." It was in fact attempted the very next day, 2026-09-06
(`FINDING_P195_ADDENDUM_high_z_bias_literature_search.md`): a bounded,
real arXiv search for a validated nonlinear/high-peak-height halo-bias
treatment covering v82's own `ν≈10.6-50` target range returned
`SOURCE_NOT_FOUND`, with a real structural reason (exponentially rare
peaks, beyond any finite-volume N-body suite's calibration reach — not
merely an unlucky search). This section's own "recommended" framing was
stale for 3 days before being corrected here — found deliberately during
a 2026-09-09 bridge-search session, same failure class as `§6a`. **Do
not re-run the same literature-search pattern without a new candidate
paper or an explicit decision to attempt a specialized N-body
calculation** — that would be exactly the "5th variant of the
bottleneck-1 bridge shortcut" `CLAUDE.md`'s own exclusion zone forbids.

**RECOMMENDED, NOT AUTHORIZED, next candidate**: none named yet for
bottleneck 3 — P191→P194 has mapped the buildable path and its
information profile thoroughly; further work here would need either a
genuinely new question (not another z-set variant) or a decision to
apply the analytic Fisher matrix as the default method near any future
domain boundary elsewhere in the project. Pearled,
`pearl_registry/INDEX.md` next_check 2026-12-15 (3 rows: P193's
numerical-methods lesson, P194's confounded-single-coordinate-scan
lesson, and the confirmed-pearl chain P191→P193).

## 6. What cannot be claimed publicly right now

- That Eq.32 reflects a genuine physical relation (three independent
  checks converge on non-support; the numerical match itself remains
  real and unexplained).
- That the F→H_MULT(z) bridge is validated, resolved, or even that its
  3 named preconditions are close to answered (4 attempts today, 0
  resolved).
- That the (β1,β2) degeneracy is a solved or fully-characterized problem
  (P190 narrowed it, did not close it).
- That `paper/main.tex` is submission-ready — it is explicitly marked
  `NOT_FOR_SUBMISSION · PARTLY SUPERSEDED` and should stay marked that
  way until bottleneck 1 or 3 actually resolves.
- Any AVB benchmark result as confirming or refuting the treatment-vs-
  baseline hypothesis — N=25, McNemar p=1.0, underpowered by design.
- That P191's Fisher-forecast establishes real high-z H(z) data at the
  assumed precision is achievable, or that bottleneck 3 is resolved —
  it only shows a quantified, in-principle path exists (see §5).

## 6a. Ernest Prabhakar's 6-point critique — answered in full, sent,
## acknowledged — real, committed work missing from this file until
## 2026-09-09 (`[VERIFIED-BASH]`, found via `git log -- experiments/
## 20260906-evidence-authority/` and `correspondence/`, not guessed)

**Why this section exists:** the events below are dated 2026-09-06/07 —
chronologically BEFORE §7's own 2026-09-07 items — but were never added
to this file's own narrative when it was "substantially revised
2026-09-07." §7.6 ("the k question") is a downstream continuation of
TJB's 09-07 reply to the letter described here, but the letter itself,
the 21-item E-series that built it, and TJB's acknowledgment were never
summarized here. This is the same "real result sitting disconnected from
its index" pattern this project's own 2026-09-08 skill audit found
repeatedly elsewhere (`NR-024`/`CLAUDE.md` citation gap, `docs/114`↔
`docs/132`, `docs/158`'s wrong citation) — an instance inside this file
itself, found while looking for it deliberately (`/boyko-project-radar`
+ `/estimand-bridge`, 2026-09-09).

**What happened:** Ernest Prabhakar's 6-point critique (forwarded by TJB,
2026-09-06) paused a MULTING press release. This project answered all
six items, real computation each time, Step 8a skeptic pass on every
substantive one:

| item | question | answered by | verdict |
|---|---|---|---|
| 1 | AIC/BIC penalty | `FINDING_P166` (2026-08-30, pre-dates the critique — already existed) | `ΔAIC≈+1.2 to +1.4` (indistinguishable, Burnham-Anderson), `ΔBIC≈+2.7 to +2.9` (mild, not decisive, favor ΛCDM) — computed on v82's own two "fairer" benchmarks, in TJB's own words |
| 2 | node-radius circularity | `FINDING_E9`/`P199` (pre-dates the critique) | `CIRCULAR=2` (both TJB's own self-diagnosed), confirmed not new |
| 3 | "phantom turn" is extrapolation-only, untestable | `FINDING_E19` | WEAKENED after skeptic (6 real corrections) — minimum sits just past the 2nd-lowest sampled CC point (not future-extrapolated, Ernest's own follow-up already conceded this), but the dip is `8-13×` below the two nearest real points' own quoted 1σ — untestable TODAY at real precision, confirming Ernest's own corrected (not original) framing |
| 4 | no falsifiable prediction anywhere | `FINDING_E21` | WEAKENED after skeptic — 9 of 12 result groups are unambiguous fit re-expressions (substantially confirms Ernest), but 2-3 (`q(0)=-1.416`; `z=3.09/3.95` divergence points) are genuine, currently-untestable-but-real candidate predictions, not indistinguishable from the untestable extreme extrapolations the original draft lumped them with |
| 5 | `T0` implies `~3.7` keV vs `~7` keV from WL-calibrated M-T relations | `FINDING_E20` | WEAKENED after skeptic — one real relation (Kettula+2014) gives `T=5.23±0.7` keV at v82's own mass; v82's `T0` sits outside that band low-side; conditional on an unresolved mass-definition assumption (`M0` vs `M500`), only one paper checked |
| 6 | can Sergey independently reproduce the fit | `FINDING_E18` | WEAKENED after skeptic (4 real framing corrections) — re-executes and extends TJB's own already-independently-implemented script (not a from-scratch re-derivation); all 7 rows independently re-optimize to `<0.09%`; wide 2-3-orders-of-magnitude multi-seed global search finds no missed minimum |

**Supporting chain (E13, E15-E17, not critique items themselves but the
real computational work items 3-6 needed):** `E13` measured a real
`σ=0.49` scatter in v82's own cited `M_gas`-`T` source (never quoted by
v82 itself); `E15` sized its force-term effect (`+13%`/`+62%` on
`F1`/`F2`); `E16` found the correction is a closed-form reparametrization
of `(β1,β2)`, not a new degeneracy; `E17` (two skeptic rounds) separated
a real Jensen correction for `F0`/`F_accretion` from a large, unrelated
`M(z)`-vs-real-MAH systematic offset (up to `~5×` at `z=2.33`) that the
original ask never intended to surface.

**The letter:** drafted, red-team reviewed internally, sent for external
review (4 of 5 points accepted, 3 further self-caught edits, `v2→v3`),
**SENT 2026-09-07** (`e8b400b`, confirmed by Sergey). **TJB replied the
same day, 19:19** (`9987452`, `correspondence/tjb_reply_20260907_1919.md`):
*"Sergey did (indeed) send me a much-appreciated email that addresses
Ernie's 6 points..."* — four of the six items on TJB's own follow-up
revision list trace directly to material this project sent (verified by
re-reading his verbatim English original, not the auto-translation —
two wordings and one attribution were caught and corrected in that
file's own §3). **No reply required or sent** — his message asked
nothing; standing correspondence rules already correctly recognized this
(§ Standing Constraints, below, is accurate, not stale).

**What this does NOT mean:** none of items 1-6 establish MULTING is
correct or incorrect (`NO_AUTHOR_ERROR` — every verdict above is
WEAKENED/mixed, not a clean win for either side); the letter answers
Ernest's specific questions, it is not a general validation.

### 7. Session of 2026-09-07 — what changed (37 commits)

### 7.1 Bottleneck 3 dissolved, and it was our own result

`FINDING_P206`. See §4 row 3. The headline for a reader who reads nothing
else: **the project spent weeks treating as a measurement gap something it
had already derived and documented.** `P52` (08-16) computed the
redundancy; `P133` (08-24) recomputed the same structure under different
vocabulary and made it a bottleneck. Neither cites the other.

### 7.2 KG2 answered — `P208` + `P209`

`P52`'s residue ("form invariance ≠ value determined"). The physical space
is two-dimensional and **neither invariant is a number, for different
structural reasons**:

| invariant | why there is no number |
|---|---|
| `A g²` | **degenerate with `G`** — universal coupling ∝ mass plus an effectively massless mediator gives exactly Newtonian `1/r²`, absorbed into the measured Newton constant (`P23`, `P149`). Its one existing figure, `≲8.39×10⁻¹²` SI = **12.6% of G**, is called by `P53` itself *"not a direct experimental bound on MULTING's own Ag²"* |
| `η = κ/g` | enters observables **only as a product** with an unknown composition contrast |

**New, and the first external number ever to bear on `η`:** reducing
`P25`'s exact Eötvös expression gives `η_E = 2η·|Δψ|/r` with
`ψᵢ = Kᵢrᵢ/(Mᵢc²)`, and MICROSCOPE **[VERIFIED-arXiv 2209.15487]**
(`η(Ti,Pt) = [−1.5 ± 2.3 ± 1.5]×10⁻¹⁵`) yields

```
η · |Δψ|  ≤  2.5×10⁻⁸ m      [~2σ, quadrature convention]
```

`FINDING_P24` had explicitly given `η` no numeric value. This bounds a
**product**, not `η`: `Δψ` is the `k_A,k_P` row `MODEL_SPEC_AUDIT.md`
flags OPEN.

**Verdict: KG2 is blocked MODEL-side, not data-side.** The best
equivalence-principle experiment ever flown is already sharp enough to
bite; what stops it biting is a postulate the model never made definite.

### 7.3 H1 is not dead — its only real test never ran

`docs/159`, `parked/H1b-whim-thermal-mass-bias.md`. Every killed H1 arm
(H1a `NR-010`, H1c `NR-012`, H1d `NR-011`, H1e `NR-014`) used the
**cluster-interior ICM**. **H1b — the only WHIM arm, *"the actual filament
gas TJB refers to"*** — was designed and pre-registered on 2026-07-17 and
**never executed**, blocked 68 days on TNG-300 access. Now parked with
three measurable revival conditions, and the `decision.md` it had lacked.

**TNG access probed 2026-09-07, with a control: unanswerable anonymously.**
Site `200`, `/data/` `200`, `/api/` **403 at the root**, `/api/TNG300-1/`
`403`. So it is an authentication requirement, not a block on us — and a
`403` looks identical whether the July registration was approved or not.
**One login by the account holder settles it; nothing short of that does.**

**H1b's criterion was repaired before any data exists** (`P210`→`P212`,
`claim.md` AMENDMENTS 1 and 2, additive — originals not rewritten):
`KILL` had a dead band that *widened* with `N`, the middle `0.15–0.30` was
undefined, and a strongly negative result filed indistinguishably from
"no effect". Now a complete three-way partition with a sign-reversed
subtype (`U₉₅ < −0.30`), plus a **frozen structural-floor algorithm** whose
stratification is fixed deterministically by `N` alone. Noise floor
checked and clean; **the structural floor is still unknown** and must be
the first thing the data touches.

**Update 2026-09-09 — TNG-300 access GRANTED, and H1b's WHIM half has now
actually run.** The "one login settles it" line above is resolved: the
account holder logged in, an API key was obtained (kept outside the repo,
`~/.secrets/tng_api_key.env`). This is the first time any H1b ingredient
has been computed on real data, not just designed. `experiments/20260909-
tng-whim-pilot/`: a controlled pipeline (2 real positive controls per
cluster — gas-mass conservation, inner-ICM temperature — both pass 71/71)
measured `E_WHIM` (WHIM mass fraction in the `R200`-`3×R200` annulus) for
`N=71` real TNG-300 clusters, meeting H1b's own pre-registered minimum
sample size. Real, significant result: `r(M200,WHIM%)=-0.429, p<0.001` —
more massive clusters have systematically lower WHIM fraction — and a
quantified discrepancy against Li et al. 2025's own reported ~70% plateau
(this sample's mean: 33.4%). Two independent dynamical-state confound
proxies (`GroupNsubs`; CM/potential-minimum offset) were tested against
this residual and both came back null (`r≈0.07` and `r≈-0.08` after
de-trending mass, neither significant at `N=71`) — full detail in
`experiments/20260909-tng-whim-pilot/FINDING_stage2_batch_n71.md`.

**H1b itself — the `E_WHIM → delta_M` correlation — still has not run.**
The 4th ingredient, hydrostatic mass bias (`M_HE`), has no public
per-cluster catalog for TNG (confirmed by direct search of
`arXiv:2001.11508`'s own data-availability text — zero hits). A wider
search across 9 channels (TNG-native, then "The Three Hundred Project"
web portal ×3, GitHub, VizieR, ADS, and the source PDF's own appendices)
closed definitively: no published, per-cluster, ID-keyed `M_HE` table
exists anywhere checked. A data-request letter to that paper's authors
was drafted and **[VERIFIED-BASH] SENT 2026-09-09**
(`correspondence/draft_three_hundred_data_request_20260909.md`, real
verified recipient addresses, via browser automation after the Gmail
MCP send tool failed systemically). **Corrected 2026-09-10** — this
section previously read "deliberately not sent," stale since before the
send; caught live while checking for new correspondence, the same
"index-disconnected work" pattern named elsewhere in this file. Ball is
with the authors, `next_check` 2026-12-01; no reply as of 2026-09-10
(checked live). `NO_AUTHOR_ERROR`: none of this bears on MULTING or
TJB's own claims — it is this project's own infrastructure for a test
that has not yet run.

### 7.4 A measured fact about this repository

Citation among the 22 structure-word findings is **14/231 = 6%**
(`FINDING_P207`). *"Does not cite X" is the default in 94% of cases and
carries almost no information* — a base-rate control that withdrew three
quarters of that finding's own first draft. **Consequence: the citation
graph is not a retrieval mechanism here.** Indexes are, which is why both
broken ones were fixed the same day (`null_results/INDEX.md` did not index
NULL-verdict findings; `docs/INDEX.md` had been stale since 2026-07-12
with 40 docs missing). All 22 `NR-*` entries are now classified —
**`theory_killed` = 0 of 22**: MULTING's core claim has never been
directly tested.

### 7.5 ICM/local-expansion branch — CLOSED 2026-09-07, verdict REFUSE

Ernest Prabhakar (06.09) named local-expansion-vs-intracluster-thermal-
energy as "the only place I see you having an asymmetric advantage".
Worked end to end. **Verdict: `REFUSE(no_falsifiable_predicate_yet)`,
and the branch is stopped.**

Both versions of the test are closed, by independent mechanisms:

| test | verdict | mechanism |
|---|---|---|
| monotone sign | `CRITERION_INVALID` | the astrophysical floor shares the sign |
| shape (reversal) | no reversal in the model | `Q(z) > 1` globally |

**Strongest surviving physics statement:** at TJB's own published fit the
thermal-source response of pair fractional acceleration is negative,
`∂(ä/a)/∂k < 0`, at every epoch the construction can represent.
**NOT established:** `∂H_local/∂E_th < 0` — that is a different quantity
(s⁻¹ vs s⁻²) and needs a dynamical bridge `δ(ä/a) → δH_local(t)` that
does not exist. Any sentence of the form "more thermal energy means less
local expansion" is WITHDRAWN.

**Comparator side, now numerically closed:**
`C4-NUMERICALLY-CLOSED-WITHIN-THIS-LINEAR-FAMILY` — linear ΛCDM has no
finite compensation radius; survived smooth spectra, full EH98 wiggles,
independent BAO template to ~19× amplitude, and a `kmin`/`kmax`/`nk`/
`rmax`/`n_r` convergence sweep (26/26 points identical), with a
destructive mutation test proving the swept parameters are wired.

A Step 8a context-blind skeptic ran on the branch; nine repairs applied,
all independently re-verified by tool. See
`experiments/20260907-icm-expansion-correlation/` —
`AMENDMENTS_after_step8a_skeptic.md` first.

**Reopen condition:** unblock condition 1 of that folder's `claim.md` §8 —
a fixed reading of `k`, or a first-principles `β`. Both change `β₂/β₁`,
which is the only thing that could move `Q` below 1.


### 7.6 The `k` question — THREE attempts, ALL retracted the same day

`P214` claimed the fork was answered → Step 8a falsified 4 of 5 claims.
`P215`/`P216`/`P217` were then written from what survived → **three
independent Step 8a passes falsified all three.** Every killing citation was
re-read from source by me before acceptance. Record:
`FINDING_P215_P216_P217_RETRACTION_after_step8a.md`.

| id | why it died |
|---|---|
| **P215** | **Conclusion inverted.** v6:652-675 defines `k = EoA − E00,oA`, an excess over the **ground state**; a cold Fermi sea **is** the ground state ⇒ `k_deg = 0`. Degeneracy is the most **excluded** candidate, not the least. Also reproduced a factor-of-2 error `FINDING_P7:23` had flagged on 2026-08-11, on a row `P7:160-166` had already computed, against a target (`Table A1`) `CLAUDE.md` forbids. |
| **P216** | v82:1028 — *"This framework treats each **node** as a single, typical **object**"*. Nested, not competing. v82:1350-1355 is a matched pair about the **observer**. |
| **P217** | Both versions assert **both** properties, in swapped **registers**: v6 constrains `β` across objects in its equations (807-810, one `βd` for A and P), v82 constrains it across time in its procedure (647-652, 707-709). v6 itself uses *"positive"* (2214) **and** *"non-negative"* (2313) — the author's idiom, not a v82 inconsistency. |

**Root cause, all three: a one-sided search reported as a two-sided
comparison.** `P217` swept `β` in v82 only, then concluded about the v6↔v82
*relationship*. `P215` never ran the FL Step -3 pre-work check on its own
directory, where `FINDING_P7` already held the answer. `P216` cited only
sections where the theory is *applied*, none where it *bounds itself* — both
killing lines sit in sections named exactly that. And all three grepped the
**older, glued** v6 extraction while the sibling file's own header line 10
says it is the **PREFERRED text for grep/search**.

**Two "improvements" made mid-session both moved away from the sources:**
`"a real narrowing"` → `"axis substitution"`, and `"b1 > 0 is sourced"` →
`"not discharged"`. The earlier, less clever formulation was right both times.

**What actually survives from the whole `k` episode:**
- The `β₁` per-node / `β₂` per-pair asymmetry (`P216` §5) — accurate, standalone.
- The relativistic Fermi-gas physics in `P215` — independently confirmed,
  including a Jensen proof that uniform density is genuinely conservative.
- v82:1453 + 1461-1463: v82 declines a GR analog and assigns **binary pulsar
  timing** to GR's jurisdiction explicitly. External compact-object bounds
  test a hypothetical extension, not a claim v82 makes.
- **A live, propagating defect:** the `ℓ_d = 2β_d(u_A+u_P)` factor of 2,
  contradicting v6 Eq. (15) as derived. Open since 2026-08-11 (`P7:143-150`),
  now in a second file. Needs fixing at the source.

**The `k` question stands, and the corpus leans further against the
compact-object reading than any of these files claimed.**


## 7a. Session of 2026-09-08 — a full skill-audit day, missing from this
## file until 2026-09-09 (found via the same deliberate "what's
## disconnected" search that produced §6a and §5's bottleneck-1 fix)

Four skills run in sequence, user-directed, each producing real findings
— none previously summarized here:

**`/boyko-bridge-ladder`** (whole-theory map + verification agents) —
found `CLAUDE.md`'s own Eq.32 stop-rule cited the wrong file (`NR-019`
does not cover the 5-niche *external* literature search); fixed via a
new `null_results/20260908-nr024-...md` written specifically to close
the citation gap.

**`/boyko-why-ladder` + `/research-audit` + `/harvest`** (same day) —
found: `docs/114`'s O7 gate was circular on one step, already
independently fixed by `docs/132`'s T5/T6 finding but never cross-cited;
the `boyko_T*_report.md` files `docs/132` cites do not exist in the repo
(a session scratchpad reference, never committed); `docs/158:35` cited
the wrong file for the sign-rule theorem; `p∝size(G)^0.95` (harvest
score 16/20) sat unpromoted for 3 weeks. **Also corrected the same
day:** both this project's own synthesis AND a separately pasted
external AI analysis had mischaracterized `docs/132`'s T5/T6 finding as
"REJECT" — the source's own explicit verdict is `OPEN`; fixed via
`parked/T5T6-cogenesis-5to1-isomer-structure.md`.

**`p∝size(G)^0.95` mini-project** — read the primary source
(`FINDING_null_d_grammar.md`) before building anything: it already
forbids the exact cross-relation comparison a `pearl_registry` row had
proposed. Re-scoped to the 2 portable, non-comparative checklist parts,
applied to Eq.32's own harmonised grammar
(`experiments/20260810-eq32-look-elsewhere/
FINDING_eq32_checklist_second_application.md`): p-vs-size exponent
0.999 (11% residual, reproduces expected density-scaling diagnostic,
**not** a newly-discovered law); D2/D1 isolation test negative (1.50 vs
null median 2.01). `pearl_registry` row 107 corrected in place.

**`/hypothesis-arbiter` on a same-day unverified claim, real kill-test
— a claim withdrawn the same day it was made.** Earlier that day, this
project's own bridge-ladder synthesis had attributed `FINDING_E8`'s
4.0-7.6× Hessian eigenvalue sensitivity to a near-cancellation
amplification factor `C≈15` computed from TJB's own Table III at
z=1.07. `why-ladder` flagged this as an unverified Mechanism Claim (same
pattern already `REJECT`ed in `NR-019`) and delegated it. The arbiter
cycle (`FINDING_P221_hypothesis_arbiter_C_vs_E8.md`, positive control
exact against `generate_all_results.py`'s own headline_cases) computed
`C(z)` at all 33 real data points: range **14.9–747.4** (median 22.4) —
z=1.07 sits near the dataset's own *minimum*, not representative.
**H1 (C is a stable diagnostic) killed; the same-day C-vs-E8 claim is
withdrawn.** `docs/158`'s own G3 (weighted joint Monte Carlo) remains
the real decisive test if this thread is pursued further.

**What this does NOT mean:** none of the four skill runs found or
refuted anything about MULTING's own physics (`NO_AUTHOR_ERROR`) — all
four are process/self-consistency findings about this project's own
reconstruction and its own citation hygiene.


## 8. Thermal-pair kSZ fingerprint — from audit to a real observational
## test design (`20260911-thermal-pair-fingerprint`, full synthesis in
## `docs/161`)

**The single biggest strategic move of this entire project:** moved off
"fit `H(z)` better" (too integrated, weakly discriminating) onto a
concrete **pair-level** MULTING fingerprint — `ξ=KR/(Mc²s)`, evaluated
per real cluster pair from the real ACT-DR5 MCMF catalog, not a mock.
23-step journey, `docs/161` has the full table; headline items:

- **Killed the fixed-window design** (`NR-025`) — real cluster
  clustering does not single out ~45 Mpc as a special scale; the idea
  was not rescued by re-tuning the window, it was replaced by a
  continuous per-pair `ξ_pred(z,s)` design instead.
- **A real, load-bearing SUTVA bug found and fixed**: 43.2% of the old
  sampled pairs shared a cluster (halo reuse across "independent"
  pairs). Corrected via cluster-disjoint matching; corrected synthetic
  power ≈ **59.1%** at N=449, 3× noise (down from an uncorrected,
  WITHDRAWN 59.9%).
- **Synthetic four-world identifiability battery ADEQUATE**: MULTING,
  optical-depth-confounded, merger-confounded, and null worlds are
  distinguished by the pipeline; false-promotion of rival worlds ≈0.
  This closed the last named hard pre-data gate.
- **Fork 1a (data request) sent** 2026-09-11 to Gong/Bean, awaiting
  reply. **Fork 1b Phase 1 (own classical pairwise-kSZ estimator, Hand
  et al. 2012) built and validated on synthetic data same day** —
  independent context-blind review CONFIRMED, no sign/index bugs.
  Phase 2 (real ACT DR6 map + real DESI DR1 cross-match) not started.

**Where this stands on the idea→proof ladder:** between "falsifiable
test" and "synthetic validation" — immediately before a real
observational test, not yet at one. A positive thermal-pair result
would support this specific frozen MULTING force fingerprint over the
alternatives tested — it would **not** by itself validate the full IDM
construction, the isomers, the cosmological bridge, or `β₁,β₂`'s
fundamental origin (`docs/151` status-separation rule applies in full).
Full detail, novelty assessment (project-level yes, methodological
likely, priority-claim not yet checked), and the remaining real-data
steps: **`docs/161`**.

## Exclusion zone (do not start without a new triggering fact)

New numerology searches on Eq.32 beyond what NR-019/020/021 already
covered; ML-based spectral analysis; Tensor Train/FFT optimization of
existing code; a new MCMC run; a 5th variant of the bottleneck-1 bridge
shortcut. None of these change the status of the central claims —
`docs/147`'s own stop-rule already governs this.

## Known engineering debt (updated 2026-09-05, see docs/155)

**Closed 2026-09-05 (cleanup pass + same-day external-review fix
round):** `mypy` 24→0 errors, now blocking in CI (was advisory);
`ruff format` clean, now enforced in CI via a new `ruff format --check`
step (there wasn't one); `src/double_inversion_plots.py` 0%→100%
coverage; `src/cluster_data_pipeline.py` 0%→93% coverage (only the
real network I/O boundary is monkeypatched — `_vizier_download`,
`requests.get` — everything downstream runs for real; see docs/155 for
the reasoning and its addendum for why the first pass's 29% was too
conservative); `.claude/memory/goals.md`'s 43 stale duplicate entries
removed and archived; a real authorization ambiguity around the
Fisher-forecast test fixed (see docs/155 addendum).

**Closed 2026-09-07 (three debts, each of whose stated premise had to be
corrected first):** 13 lapsed `pearl_registry` `next_check` rows triaged —
5 were already ANSWERED by later work and simply never marked; `docs/INDEX.md` resynced, 40 docs (122-159) added, and **four number
collisions found while indexing (122/132/133/134 each used twice; doc 121
does not exist)** — cite by filename past 121; `source_provenance.py` /
`conflict_resolver.py` **PARKED** (`docs/158`) rather than wired —
`docs/157`'s proposed join was a category error (chain level vs value
level), and that module's docstring had the dependency arrow backwards.
Also corrected: two false *"no API key needed"* claims in
`scripts/illustris_tng_k_a.py` (the API 403s at its root). Provenance
checked before reporting — nothing downstream had cited it.

**Still open:** `pyproject.toml` version frozen at `0.3.0` since the MVP
era (a release decision, out of scope for engineering-hygiene passes).
