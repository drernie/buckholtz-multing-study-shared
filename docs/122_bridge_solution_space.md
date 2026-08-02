# docs/122 — Solution Space: continuous reproducible H_MULT(z)

**Skill:** boyko-goal-expansion-100 (deep) · **Date:** 2026-07-22
**Safety:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
**Scope:** how to obtain a continuous, reproducible H_MULT(z) that is the *theory's*
prediction (not our fit). This is the Q1/Q5 bridge, the BETA-1 HOLD blocker.

---

## 1. Goal formalization (verifiable)

- **primary_goal:** produce H_MULT(z) as a continuous function reproducible from
  stated inputs, distinguishable from an arbitrary interpolation of the 12 Table A1 points.
- **success (strong):** a map (force law + specified cluster schedule k_A(z), r_A(z),
  D(z) + fixed β) → H(z) that reproduces the 12 Table A1 rows to their tolerance AND
  is derived, not fitted per-point.
- **success (weak, fallback):** a continuous H(z) with calibrated uncertainty, explicitly
  labelled "interpolation, not MULTING theory."
- **refutation of the whole direction:** prove the strong map is *underdetermined* by all
  public information (identifiability no-go) → then only TJB can close it, and our correct
  deliverable becomes the no-go proof itself.
- **unknowns:** k_A(z), r_A(z), D_C:AB(z) schedules; the F_oP→H mapping; physical β_d,β_q.

## 2. Feasibility gate

- **Weak sub-goal:** feasibility **8/10** (today's honest-diagram script is step 1).
- **Strong sub-goal WITHOUT TJB:** feasibility **2–3/10**. The cluster schedule is
  unpublished and appears underdetermined (see E1/D6). This is not a coding gap; it is a
  missing-information gap. Do NOT present it as almost solved.
- Consequence (per skill Step 1): the space below is weighted toward toy-models,
  identifiability/no-go work, and cheap internal-consistency tests — not "ready solutions."

## 3. Gap map (logical breaks)

- G-α: is w_eff(z) (already in Table A1) a *closed* EoS that regenerates H_MULT(z)? If yes,
  the continuous form exists internally, for free. **Untested. Highest-leverage gap.**
- G-β: is (β_d, β_q, schedule) identifiable from Table A1 alone? (Fisher rank.)
- G-γ: does the non-monotone ε(z) forbid every monotone single-schedule bridge? (extends NR-004)
- G-δ: how many distinct (schedule, β) reproduce the 12 points to tolerance? (degeneracy count)

## 4. Lens map (≥12 of 25, each tied to THIS task)

| Lens | Tie to bridge |
|---|---|
| Inverse problems (21) | recover k_A(z) from ε(z) — ill-posed, needs regularization |
| Numerical methods (11) | Padé / Chebyshev / spline continuation of 12 points |
| Statistics & causality (9) | GP with calibrated uncertainty; identifiability |
| Dynamical systems (5) | kinematic route ä/a=f(F_oP) as an ODE |
| Control theory (6) | system identification: cluster input → H(z) output |
| Info theory (7) | lower bound on info needed to fix the schedule |
| ML (14) | symbolic regression / PINN for closed-form H(z) |
| Optimization (10) | constrained fit with theory-fixed signs |
| Physical analogies (16) | effective dark-energy fluid via w_eff |
| No-go/falsification (24) | identifiability & degeneracy impossibility results |
| Formal verification (13) | dimensional & existence/uniqueness proofs |
| New hybrids (25) | GP-mean + physics-prior combinations |

## 5. Idea space (deduped; ~62 distinct mechanisms, NOT padded to 100)

> Honest count note: after dedup this problem yields ~60 *distinct mechanisms*, not 100.
> It is a "recover one specific missing function" problem, not an open-ended design space.
> Padding to 100 would require renaming the same interpolation/schedule mechanisms — refused
> per skill Step 7. Blocks below.

### Block A — direct & adjacent (author + force-law + fluid)
- A1 Ask TJB for the explicit F_oP→H_MULT(z) mapping (follow-up to docs/121). Test: reply. Falsifier: he confirms it is AI-black-box → strong sub-goal dead without him.
- A2 Ask TJB for the schedule tables k_A(z),r_A(z),D(z). Test: reply.
- A3 Ask TJB / read the 3 AI-service supplementary transcripts for the actual H(z) routine. Test: transcript present in supplementary.
- A4 Compare Claude/ChatGPT/Gemini supplementary H(z) tables → their spread = bridge ambiguity (BRAI-style). Test: 3 tables differ. Falsifier: identical → single routine exists.
- **A7 Effective-fluid route: does w_eff(z) (Table A1 col) integrate via Friedmann+continuity back to H_MULT(z)?** Test: 1-day arithmetic on the CSV. Falsifier: integral ≠ H_MULT column → w_eff is decorative, not the bridge.
- A5 Kinematic route ä/a = N_eff·F_oP/(μ·D) (Candidate B); pin N_eff,μ from theory. Test: reproduces 12 points. Falsifier: needs per-z retuning.
- A6 Potential route: Φ(z) from F_oP; H²∝Φ(z)/Φ_anchor. Test: monotone Φ can't give non-monotone ε → likely falsified (link G-γ).
- A8 Constrained MULTING polynomial A(1+z)²+B(1+z)³+C(1+z)⁴ with theory-fixed signs A>0,B<0,C>0 (partly in code/beta_cv.py). Test: sign-constrained fit AIC vs ΛCDM.
- A10 k_A(z) from X-ray scaling relations (L_X–T, M–T) observationally. Test: plug into force law.
- A11 k_A(z)=E_ICM(z) from IllustrisTNG hydro sim. Test: TNG pull (API pending). Falsifier: sim E_ICM monotone → can't make ε peak.
- A12 r_A(z),D(z) from halo mass function + concentration–mass relation. Test: forward force law.
- A14 Two-component decomposition of ε(z) (existing open experiment) into monopole/dipole/quadrupole z-runs. Test: 2-bump fit.
- A16 Bootstrap from the H_w_eff column consistency (internal cross-check).

### Block B — cross-domain transfers (8-question gate passed for each)
- B1 Tikhonov-regularized inverse (tomography): recover smooth k_A(z) from ε(z). Falsifier: no smooth schedule fits → underdetermined.
- **B2 Gaussian Process regression: continuous H(z) + calibrated bands, labelled non-theory.** Cheapest honest weak-goal solution.
- **B3 Symbolic regression (PySR, outputs/ exists): closed-form H(z) minimizing fit×complexity.** Falsifier: min-complexity form is just ΛCDM-like → no distinct MULTING form.
- B5 RG-flow: treat β_d(z),β_q(z) as running couplings; find beta-function. Gate: objects=couplings, operation=flow — structural, not word-match.
- B6 System identification (control): transfer function cluster-input→H(z).
- B7 Padé[2/2] rational approximant: bounded extrapolation vs polynomial blow-up.
- B8 Chebyshev expansion: certified truncation-error extrapolation.
- B9 Cosmography (Taylor of a(t)): model-independent H(z); compare MULTING points to q0,j0 series.
- B11 Log-normal-in-(1+z) spectral basis where a z≈0.40 peak is natural.
- B12 Fokker–Planck transport for cluster energy → k_A(z) as a PDE solution.
- B16 Bayesian model averaging: a posterior OVER bridges, not one bridge.
- B17 PINN: force law as soft constraint, learn H(z).
- B18 Kalman/state-space: latent smooth H(z) from 12 noisy row-measurements.
- B21 Homogenization (multiscale PDE): coarse-grain cluster force to cosmic H(z).
- B22 Mean-field average of pairwise force over cluster distribution → effective H(z).
- B23 Green's-function: H(z)=kernel ⊛ cluster source.
- B25 Extreme-value tail model for the z>2 extrapolation region specifically.
- **B26 Buckingham-Pi dimensional analysis: the dimensionless groups any bridge MUST contain — constrains functional form before fitting.**

### Block C — hybrids
- C1 GP mean + force-law prior. C2 Symbolic regression seeded with theory basis.
- C3 w_eff-fluid + GP residual. C4 Tikhonov schedule + forward force law.
- C5 RG-running β + dimensional constraint. C6 Two-component ε + Padé per component.
- C7 Sim E_ICM + kinematic route. C8 Bayesian avg over {poly,Padé,GP,fluid}.
- C9 PINN with w_eff continuity. C10 Cosmography with MULTING-fixed jerk.

### Block D — computational tests
- D1 Fit all continuous forms; rank by AIC + extrapolation stability.
- D2 Leave-one-out on 12 points (loo_epsilon_analysis.json) — which forms self-extrapolate.
- **D3 Internal consistency: does w_eff integrate back to H_MULT? (pure CSV arithmetic).**
- D4 TNG E_ICM(z)→force law vs Table A1.
- D5 Monte-Carlo schedule uncertainty → H(z) band.
- **D6 Fisher-rank identifiability of (β_d,β_q,schedule) from Table A1 (m2_g4 seed exists).**
- D7 PySR run on 12 points with complexity budget.
- D8 Sensitivity of high-z H to each schedule assumption.
- D9 3-AI-service table spread = bridge uncertainty.
- D10 Blind: fit z<1, predict z>2, check vs Table A1 high-z rows.

### Block E — no-go / inverse / falsification
- **E1 Identifiability no-go: Fisher rank < #parameters → bridge underdetermined by public info.**
- E2 Non-monotonicity theorem: ε(z) peak forbids any monotone single-schedule bridge (extends NR-004).
- E3 Degeneracy-with-ΛCDM: any 3-param continuous form is AIC-indistinguishable on current data (already shown, ΔAIC≈+5).
- E4 Degeneracy census: count (schedule,β) combos reproducing 12 points to tolerance.
- E5 Complexity bound: no elementary closed form below Kolmogorov budget K fits (from PySR).
- E6 Gauge-freedom: absent k_A(z), the schedule is a relabeling freedom.
- E7 Extrapolation genericity: high-z blow-up is generic to polynomials → extrapolation is model-choice, not MULTING.
- E8 Aliasing check: is the z≈0.40 peak an artifact of 12-point sampling?
- E9 Energy-condition falsifier: does ä/a=f(F_oP) need positive pressure violating PPN?
- E10 Info lower bound: fixing the bridge needs ≥1 observable outside Table A1.

### Block F — formal verification
- F1 Symbolic dimensional-consistency proof of force-law→H(z) (sympy).
- F2 Existence/uniqueness of the kinematic-route ODE (Picard–Lindelöf).
- F3 Interval-arithmetic certified extrapolation bounds.
- F4 Verify fitted signs (A>0,B<0,C>0) match force-law sign structure.
- F5 Convergence radius of the chosen series in (1+z).

### Block G — new math constructions
- G1 "MULTING kernel" K(z,z'): H²(z)=∫K ρ_cluster dz' — integral representation.
- G2 Reparametrization u(z) making ε monotone → tractable bridge.
- G3 Ansatz H_MULT=H_FLRW·√(1+ε), ε from a stated generating function.
- G4 β_d,β_q as z-dependent form factors from a structure function S(z).
- G5 Schedule functional with an Euler–Lagrange eq yielding k_A(z) (ties to Blanchet-action lead).

### Block H — minimal prototypes
- H1 (1h) Padé+GP vs poly extrapolation (reuse today's script).
- H2 (1d) w_eff↔H_MULT consistency (D3).
- H3 (1d) Fisher-rank identifiability (D6, reuse m2_g4).
- H4 (1wk) TNG E_ICM→force law (D4, when API unblocks).
- H5 (1h) PySR on 12 points (D7, reuse outputs/).

## 6. Top-12 (by adjusted_score; full cards in §skill-cards below)

1. **A7/D3** w_eff→H_MULT internal-fluid consistency — cheapest, could hand a continuous form for free.
2. **E1/D6** Fisher-rank identifiability no-go — decides if strong sub-goal is even possible without TJB.
3. **A1/A2** Ask TJB for bridge + schedule — only path to the *theory's* curve.
4. **B3/D7** Symbolic regression for closed-form H(z).
5. **E4** Degeneracy census (how many bridges fit).
6. **B2** GP with calibrated uncertainty (honest weak-goal deliverable).
7. **B26** Dimensional-analysis constraint on bridge form.
8. **A14** Two-component ε decomposition.
9. **B7** Padé extrapolation (fixes poly blow-up).
10. **A11/D4** Simulation E_ICM(z) schedule (TNG).
11. **E2** Non-monotonicity theorem (extends NR-004).
12. **B1** Tikhonov inverse for smooth schedule.

## 7. Portfolios

- **Conservative (this week, no TJB, no TNG):** A7/D3, E1/D6, E4, B2, B26 — all reuse existing CSVs/artifacts.
- **Balanced (2–4 wks):** + B3/D7 symbolic regression, A14 two-component, B7 Padé, D10 blind extrapolation.
- **Moonshot:** G1 MULTING-kernel integral representation + G5 schedule-from-action (Blanchet-Lagrangian lead) — derive the bridge from first principles. Low feasibility, high payoff.

## 8. Dependency matrix (key)

- A7/D3 → if PASS, most other bridge work is moot (continuous form exists). Run FIRST.
- E1/D6 → gates everything: if underdetermined, Blocks A5/A10/A12/B1 (schedule recovery) are impossible without new data.
- A11/D4 depends on TNG API (currently blocked).
- Everything strong-sub-goal depends on A1/A2 (TJB) unless E1 says otherwise.

## 9. Prototyping plan

- **Day:** A7/D3 (w_eff↔H_MULT arithmetic) + H3 Fisher rank + H5 PySR.
- **Week:** E4 degeneracy census + B2 GP band + B7 Padé + D10 blind test.
- **Month:** two-component ε (A14) + dimensional-analysis paper section (B26); if TNG unblocks, D4.
- **Year:** G1/G5 first-principles bridge (only if E1 says identifiable OR TJB supplies schedule).

## 10. Negative results / already killed (do NOT repropose)

NR-001 constant-ε · NR-002 power-law · NR-003 PS comoving density (monotone) ·
NR-004 virial k_A (monotone) · NR-016 Shtanov naive mapping. Common cause: monotone
single-schedule inputs cannot make ε(z) peak at z≈0.40. Any new schedule idea MUST address
the non-monotonicity (G-γ) or it repeats these.

## 11. Unknowns register

| Unknown | Who answers | How |
|---|---|---|
| Is w_eff a closed EoS regenerating H_MULT? | us | D3, 1 day |
| Is the bridge identifiable from Table A1? | us | D6 Fisher rank |
| The actual schedule k_A(z),r_A(z),D(z) | TJB | A1/A2 |
| Is F_oP→H AI-black-box or a stated formula? | TJB | A3 |

## 12. Sources

- Project: facts.json, null_results/INDEX.md (NR-001..016), reports/bridge_derivation_attempt.json,
  reports/m2_g4_fisher_rank_identifiability.*, reports/loo_epsilon_analysis.json,
  outputs/…hall_of_fame.csv, code/beta_cv.py, scripts/aic_model_comparison.py,
  data/table_a1_reported.csv (cols w_eff, H_w_eff), audit/fairness_diagnostics.py.
- External methods named are standard (GP regression, Padé, Tikhonov, PySR, Fisher information,
  cosmography) — not fabricated; specific citations to be added if promoted past prototype.
