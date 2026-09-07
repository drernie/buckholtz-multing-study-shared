# Current Evidence State — buckholtz-idm-multing-mvp

**Date:** 2026-09-03; quality snapshot refreshed 2026-09-05, and
substantially revised **2026-09-07** (37 commits: bottleneck 3 dissolved,
KG2 answered, H1b parked and its criterion repaired — see §7) ·
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
- **Eq.32 numerical match** (0.0135%, PDG 2024) — `[VERIFIED]`, unaffected
  by everything below; only its *interpretation* is contested.
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
| 1 | F→H_MULT(z) bridge | BLOCKED (restated 2026-09-01, `docs/153`); `docs/153`'s own literal next-step disproven as buildable, `docs/156` (2026-09-05) — mechanically-correct alternative line (`P157`→`P158`→`ADDENDUM2`→`P195`) gives a real, narrow, `z≤0.5`-only, magnitude-uncertain result | `z≥1` (or `z≥1.07` on this alternative line) needs nonlinear-bias/N-body work, not another analytic substitution — same conclusion reached independently on two separate lines of attack |
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
magnitude-uncertain `z≤0.5`-only result. **RECOMMENDED, NOT AUTHORIZED,
next candidate for this line**: extending trustworthy `ρ` coverage to
`z≥1.07` would require nonlinear halo-bias or direct N-body pair
statistics — a materially larger, more specialized undertaking than
anything attempted so far on this line, not a quick follow-up.

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

## 7. Session of 2026-09-07 — what changed (37 commits)

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
