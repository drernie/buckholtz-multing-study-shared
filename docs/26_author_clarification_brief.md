# Author Clarification Brief — Dr. Thomas J. Buckholtz

**Date:** 2026-05-28  
**Status:** Ready for review before sending  
**Purpose:** Source-grounding questions for reproducibility audit

---

## 1. Purpose

Dr. Buckholtz,

I am building a small reproducibility and epistemic-audit layer for selected parts of your IDM/MULTING work. My goal is **not** to validate or challenge the model, but to **separate definitions from predictions** and ensure I am representing your work accurately.

I have reached a stage where further progress requires clarification from you on several points. I am trying to make my audit **source-grounded** before doing any modeling or numerical calculations.

---

## 2. What I Have Already Verified

From manual verification of manuscript `preprints202511.0598.v6.pdf`, Appendix A.3, Table A1:

✅ **Beta values:**
- beta_d = 4.5
- beta_q = 18.0

✅ **Context:**
- These values were selected by an AI-assisted online service to minimize standard deviations from observed H(z)
- They are **fitted phenomenological parameters**, not derived theoretical constants
- I am treating them as **fit-reproduction parameters** (I can reproduce the Table A1 fit after receiving the formula), **not** as theoretical predictions (I will not claim they "predict" H(z) since they were fitted to it)

This distinction is important to avoid circular reasoning in my audit.

---

## 2a. What I Have Documented (Awaiting Verification)

From public-source formula-stripping pass (docs/33_public_formula_stripping_report.md):

⏸️ **MULTING pairwise force-law equations (SOURCE_CANDIDATE, awaiting manual PDF verification):**
- Monopole: F_m = G m_A m_P / r²
- Dipole: F_d = G c⁻² (k_A m_P |r_dA| + k_P m_A |r_dP|) / r³
- Quadrupole: F_q = G k_A k_P c⁻⁴ |r_qAB|² / r⁴
- Total: F_oP = F_m - F_d + F_q

⏸️ **Beta length-scale definitions (SOURCE_CANDIDATE, awaiting manual PDF verification):**
- r_dA = beta_d × r_A
- r_dP = beta_d × r_P
- |r_qAB|² = beta_q² × r_A × r_P

⏸️ **Dimensional analysis:** Units verified for all force components [kg·m/s²]

**Status:** Documented as SOURCE_CANDIDATE until I manually verify character-by-character against the PDF. Dimensional analysis passed, but force-law-to-H(z) mapping **not found** in public materials (see section 3 questions below).

**What I will NOT do without your clarification:**
- Implement H_MULT(z) solver (bridge F→H(z) not explicit in preprint; force formulas F_m/F_d/F_q present in Step 2 p.33, but F_oP→H mapping absent)
- Perform MCMC parameter estimation (requires H_MULT forward model)
- Claim validation or refutation of MULTING (not my goal)
- Use force law for predictions (closure relations missing)

---

## 2b. Heuristic H-MULT Closure Candidate (AI Transcript)

From AI transcript / supplementary materials analysis (docs/35_ai_transcript_closure_candidate.md):

⚠️ **Possible heuristic scaling formula (AI_TRANSCRIPT_REPORTED status):**
- Phi(z) = A_m(z) - A_d(z) + A_q(z)  (multipole amplitude scaling factor)
- H_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)]  (scaled Hubble parameter)

**Status:** AI_TRANSCRIPT_REPORTED — appears in AI-generated materials, NOT verified in manuscript equations.

**Sign structure:** Matches force-law structure (F_oP = F_m - F_d + F_q), but physical derivation (Phi(z) → H(z) mapping from field equations) **not found**.

**Required inputs for evaluation (9 total):**
- ✅ beta_d = 4.5, beta_q = 18.0 (known from Table A1)
- ❌ m_A(z), r_A(z), k_A(z) — cluster variable evolution (MISSING)
- ❌ D_C:AB(z) — comoving distance (computable, but which A/B?)
- ❌ H_anchor, z_anchor — reference point (MISSING)
- ❌ **Cluster variable table** — m_A(z_i), r_A(z_i), k_A(z_i) for all z_i in Table A1 (**CRITICAL BLOCKER**)

**What this formula MAY enable (if cluster variables provided):**
- Table A1 reproduction attempt (phenomenological fit verification)
- Comparison: H_MULT(z_i) from heuristic vs reported values

**What this formula does NOT enable:**
- H(z) prediction on new redshifts (requires cluster table for all z)
- MCMC parameter estimation (no forward model for arbitrary z)
- Out-of-sample validation (fitted to data it would "predict")
- Uncertainty estimates (sigma_MULT definition missing)

**Use permission status:**
- ALLOWED_FOR_TABLE_REPRODUCTION_CANDIDATE (if cluster variables provided)
- NOT_ALLOWED_FOR_PREDICTION (missing cluster table)
- NOT_ALLOWED_FOR_MCMC (no rigorous derivation, no likelihood)

**Safe wording:** "Heuristic scaling candidate exists but requires cluster variable table for table reproduction. Cannot predict on new redshifts. MCMC remains blocked."

**Questions for clarification (extends Q1-Q4 below):**
- Q1a: Is the heuristic formula H_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)] documented in the manuscript or a separate publication?
- Q1b: How are A_m(z), A_d(z), A_q(z) defined? Are they force amplitudes, potential amplitudes, or dimensionless scaling factors?
- Q1c: What are the values of H_anchor and z_anchor?
- Q4a: For Table A1 redshifts, what are the values of m_A(z_i), r_A(z_i), k_A(z_i)? Is there a cluster catalog or evolution model?

---

## 2c. Minimum Viable Bridge (MVB) Question — Discrete Lattice + Virial Pressure (Optional, Long-Horizon)

After reviewing six possible bridge routes from the pairwise force law (F_oP) to cosmological expansion (H(z)), the strongest **computational reconstruction candidate** from a first-principles perspective would be:

**Route:** Pairwise forces → discrete cluster lattice (Wigner-Seitz cells) → nearest-neighbor dynamics → virial pressure P = -⟨r · F⟩/(3V) → effective fluid (ρ_eff, P_eff) → Friedmann acceleration ä/a = -(4πG/3)(ρ + 3P) → H(z)

**Status:** This is NOT found in any manuscript materials I have reviewed. It is a **research hypothesis / computational reconstruction** that our audit team developed as a possible mechanistic bridge. **I am not claiming this is your approach.**

**Question (Q_MVB, optional):**
> Should the MULTING force law be interpreted through a discrete cluster-neighbor picture, where pairwise forces between neighboring clusters generate an effective pressure or cell-scale expansion? Or is there another averaging prescription that maps F_oP into the H_MULT(z) values in Appendix A/Table A1?

**Context:**
- Virial theorem (P = -⟨r · F⟩/(3V)) is standard statistical mechanics — provides a well-defined operator to map forces to pressure
- Discrete lattice (Wigner-Seitz cells) avoids the issue that standard homogeneous averaging would null dipole/quadrupole contributions
- This is distinct from the heuristic Phi(z) scaling (section 2b) which is phenomenological

**Why I'm asking (optional to answer):**
- This route is physically motivated but requires author confirmation to distinguish "our reconstruction" from "Buckholtz's model"
- If this is **not** your intended approach, I will archive it and wait for your clarification (Q1-Q4 above)
- If this **is** close to your approach, it would help me understand what inputs are needed (lattice geometry, neighbor count, cell volume, etc.)

**Safe wording I will use:**
- "After bridge route triage, discrete lattice + virial pressure is the strongest candidate from first principles. However, it is NOT source-supported. It is a research hypothesis requiring author confirmation. Implementing it without confirmation = testing our interpretation, not Buckholtz's model."

**What I will NOT say:**
- ❌ "This solves the F_oP → H(z) bridge" (not source-confirmed)
- ❌ "Buckholtz's approach uses virial pressure" (unless you explicitly confirm)
- ❌ "This proves MULTING cosmology" (hypothesis, not proof)

**Note:** This question is lower priority than Q1-Q4 above. If you prefer to focus on the H-MULT formula and dataset questions first, that is completely fine. The MVB route remains an internal research hypothesis until/unless you confirm it aligns with your model.

---

## 3. Questions — H-MULT Fit Reproduction

To reproduce the Table A1 H-MULT column and compare with H-FLRW, I need:

### Q1: H-MULT Functional Form

**Question:**
> Could you provide the explicit functional form for H_MULT(z; beta_d, beta_q)?

**Context:**
- The manuscript mentions monopole, dipole, and quadrupole terms
- I have not found the exact combination formula (e.g., H_MULT = H_monopole + beta_d × H_dipole(z) + beta_q × H_quadrupole(z), or a different form)
- I need this to implement a solver and reproduce Table A1

**Example of what would help:**
- Explicit equation with z-dependence
- OR reference to equation number in a prior publication
- OR explicit statement if the formula is proprietary or still being finalized

---

### Q2: H(z) Dataset

**Question:**
> Which observed H(z) dataset was used in Table A1?

**Options:**
- Cosmic chronometers (galaxy ages) — which compilation? (Moresco+ 2012? 2016? 2022?)
- Pantheon+ SNIa H(z) measurements
- BAO measurements
- Combination of datasets
- Custom dataset

**Why this matters:**
- To reproduce the fit, I need the same input data
- To avoid circular reasoning, I need to document: "beta values fitted to dataset X → cannot claim to predict dataset X"

---

### Q3: sigma_MULT Definition

**Question:**
> How is sigma_MULT (the fit quality metric in Table A1) defined?

**Possibilities:**
- Number of standard deviations: |H_MULT(z) - H_obs(z)| / σ_obs
- Chi-squared contribution: ((H_MULT - H_obs) / σ_obs)²
- Cumulative metric across all redshift bins
- Something else

**Why this matters:**
- To verify fit quality claims
- To compare H-MULT fit quality with H-FLRW (ΛCDM) fit quality on the same dataset

---

### Q4: AI-Estimated vs Fixed Quantities

**Question:**
> In Appendix A.3, the manuscript mentions that the online AI service estimated m_A, r_A, k_A, D_C:AB, and selected beta_d and beta_q.
> 
> Which of these quantities were:
> (A) Estimated by the AI (free parameters in the fit)?
> (B) Fixed by you (input constraints to the AI)?

**Why this matters:**
- Counting free parameters (more free parameters = easier to fit any dataset → lower evidential value)
- Understanding which quantities are theoretically predicted vs phenomenologically fitted

---

## 4. Questions — IDM Microphysics (External Constraints)

I am reviewing three independent observational constraints that **may** be relevant to IDM:
1. Big Bang Nucleosynthesis (BBN) and effective neutrino species (N_eff)
2. Self-Interacting Dark Matter (SIDM) and Bullet Cluster observations
3. Gaia stellar kinematics and dark disk constraints

To determine whether these constraints apply, I need clarification on the **microphysical structure** of the 6 dark isomers.

**Important:** I am **not** claiming these constraints refute or validate IDM. I am trying to determine **whether they are applicable** to your model. If they are not applicable (e.g., because dark isomers do not have the relevant properties), I will document that and move on.

---

### Q5: Thermal History (BBN / N_eff)

**Question:**
> Do the 5 dark isomers contain thermally populated relativistic particles (e.g., dark photons, dark neutrinos) at early times (temperature T ~ MeV, BBN epoch)?

**If yes:**
- What is the dark-sector temperature ratio T_dark / T_visible?
- Does the model predict the effective number of neutrino species (N_eff)?
- Current observational constraint: Planck 2018 + BBN gives N_eff = 2.99 ± 0.17

**If no (dark sectors are cold or decoupled at BBN):**
- BBN/N_eff constraints do not apply → I will document this and archive that constraint

**Why this matters:**
- BBN is the gold-standard early-universe constraint
- IF dark isomers are thermally populated → BBN constrains their particle content
- IF dark isomers are cold/non-relativistic → BBN is irrelevant

---

### Q6: Self-Interactions (SIDM / Bullet Cluster)

**Question:**
> Are the 6 dark isomers collisionless (self-interaction cross-section σ/m ~ 0, like standard CDM) or self-interacting (σ/m > 0, like SIDM)?

**If self-interacting:**
- What is the predicted self-interaction cross-section σ/m (in cm²/g)?
- Is σ/m velocity-dependent?
- Current observational constraint: Bullet Cluster (1E 0657-56) gives σ/m < 1–2 cm²/g at cluster collision velocities (~3500 km/s)

**If collisionless:**
- Bullet Cluster constraint automatically satisfied → I will document this

**Additional question:**
> Are the MULTING dipole/quadrupole terms interactions **between dark matter particles** (DM-DM scattering forces) or contributions to **spacetime curvature** (modified gravity, like f(R) or TeVeS vector fields)?

**Why this matters:**
- IF dipole = DM-DM scattering → Bullet Cluster constrains dipole amplitude
- IF dipole = modified gravity → Bullet Cluster does not directly constrain dipole (different physics)

---

### Q7: Scale Range and Dissipative Processes (Gaia / Dark Disk)

**Question:**
> At what physical scales do the MULTING dipole/quadrupole terms operate?

**Options:**
- (A) Cosmological scales only (Mpc–Gpc, affects H(z) expansion but not local dark matter distribution)
- (B) All scales including galactic (kpc, affects local dark matter density and vertical profile)
- (C) Scale-dependent with a cutoff (strong at Mpc, weak or zero at kpc)

**If (A) — cosmological only:**
- Gaia constraints (local dark matter, r ~ 8 kpc) do not apply → I will document this

**If (B) or (C) — also galactic:**
- Gaia stellar kinematics constrain local dark matter: ρ_DM(z=0) ~ 0.3–0.6 GeV/cm³
- Need prediction for ρ_DM(z) vertical profile to compare

**Additional question:**
> Are the 6 dark isomers dissipative (dark photons, radiative cooling, dark atom formation)?

**If dissipative:**
- Dark isomers can cool and collapse into disk-like structures (dark disk)
- Gaia constrains dark disk mass: M_disk / M_halo < 0.3–0.5

**If non-dissipative:**
- Dark isomers remain halo-like (spherical/ellipsoidal distribution, like standard ΛCDM)
- No dark disk formation → dark disk constraint does not apply

**Why this matters:**
- Dimensional analysis from beta_d ~ 4.25 (if dimensionless) suggests a characteristic scale L ~ 2.3–2.6 Mpc (galaxy group / cluster scale, **240× larger** than Milky Way disk ~ 10 kpc)
- This suggests dipole may **not** operate at galactic scales, but I want to confirm this interpretation is correct

---

## 5. Safe Wording Examples

When I write about your model in my audit documentation, I am using phrasing like:

✅ **Safe:**
- "Buckholtz's model proposes 6 isomers (5 dark, 1 ordinary). The microphysical structure is not specified in available materials."
- "Beta values are fitted to H(z) observations and can be used to reproduce the manuscript fit, but cannot be used to predict H(z) on new data (circular reasoning)."
- "BBN/N_eff constraints may be relevant **if** dark isomers are thermally populated. Applicability cannot be determined without clarification."
- "I may be misunderstanding the scale range of dipole terms. Could you clarify whether they operate at cosmological (Mpc) or galactic (kpc) scales?"

❌ **Avoiding:**
- "BBN disproves IDM"
- "This is numerology"
- "Your model violates X"
- "MULTING predicts Y" (when Y was not explicitly predicted by you)

I want to ensure I am representing your work accurately and not putting words in your mouth.

---

## 6. Appendix A1 Step 5 Forensic Finding (BLOCKER — PRIORITY 1)

**Context:**

I performed word-level forensic extraction of Appendix A1 Steps 3–7 from preprints202511.0598.v6.pdf (pages 31–38). Full extraction documented in `docs/39_appendix_a1_steps_3_7_forensic_reading.md`.

**What Step 5 provides:**

1. ✅ Scaling relations (explicit): r_dA = β_d × r_A, r_dP = β_d × r_P, |r_qAB|² = β_q² × r_A × r_P
2. ✅ Fitting instruction: *"minimize standard-deviations away from observed H(z)"*
3. ✅ AI discretion: *"Feel free to use any or all the information"*
4. ✅ Fitted values (Table A1): β_d = 4.5, β_q = 18.0

**What Step 5 does NOT provide:**

❌ Explicit functional form H_MULT(z; β_d, β_q, m_A, r_A, k_A, ...)  
❌ Computational algorithm (beyond "fit by using monopole, dipole, quadrupole")  
❌ Cluster variable table m_A(z), r_A(z), k_A(z) for Table A1 redshifts  
❌ Objective function details (beyond "minimize σ")

**Bridge status:** PARTIAL — procedural instruction only, NOT computational formula.

**Implication:**

Table A1 H_MULT column is AI service output following Step 5 procedural instruction, NOT author-verified calculation. I can store Table A1 as empirical data, but I cannot compute H_MULT(z) on NEW redshifts without explicit formula.

**What I want to understand:**

I may be misunderstanding the computational step between pairwise forces F_oP and cosmological expansion H_MULT(z). Could you clarify:

1. **Explicit H_MULT formula:** What is H_MULT(z; β_d, β_q, m_A, r_A, k_A, ...)? How do monopole/dipole/quadrupole combine?
2. **Cluster variables:** For Table A1 reproduction, do you have tabulated m_A(z), r_A(z), k_A(z) for z = 0 to 8.5?
3. **AI interpretation:** Did the AI service use a specific method (heuristic scaling? virial pressure? other?)? Is there a procedure description I can reference?

**Alternative interpretations I considered:**

After systematic triage (`docs/36_force_to_expansion_bridge_triage.md`):

- **(A) Heuristic phenomenological scaling** (`docs/35_ai_transcript_closure_candidate.md`): Phi(z) = A_m - A_d + A_q, H_MULT² = H_anchor² × [Phi/Phi_anchor]. Status: AI_TRANSCRIPT_REPORTED (not manuscript-verified).
- **(B) Discrete lattice + virial pressure** (`docs/37_discrete_lattice_mvb_hypothesis.md`): Nearest-neighbor cluster lattice, P_virial = -⟨r·F⟩/(3V), Friedmann acceleration. Status: RESEARCH_HYPOTHESIS (audit reconstruction, not manuscript-supported).

**Neither is source-confirmed.** I want to avoid implementing my own interpretation and misrepresenting your framework.

**Blocked capabilities:**

Without explicit H_MULT formula or cluster variable table:
- ❌ Reproduce Table A1 numerically
- ❌ Compute H_MULT(z) on new redshifts
- ❌ Build forward model for MCMC
- ❌ Compare MULTING vs ΛCDM on independent datasets

**Respectful request:**

Could you provide:
1. Explicit formula H_MULT(z; β_d, β_q, ...), OR
2. Confirmation that AI interpretation (A), (B), or another matches your approach, OR
3. Cluster variable table for Table A1 redshifts?

I want to represent MULTING accurately and avoid testing my interpretation instead of your model.

**If not addressed in published materials:**

I will document this as a computational bridge blocker and note that Table A1 is stored as empirical reference (TABLE_REPORTED) but not predictive (BLOCKED for new z). Repository will be published transparently with this blocker documented.

---

## 7. Summary of What I Am Asking For

**Fit reproduction (PRIORITY 1 — needed to proceed):**
1. H_MULT(z; beta_d, beta_q) functional form (see Q6 Appendix A1 finding)
2. H(z) dataset used in Table A1
3. sigma_MULT definition
4. Which quantities were AI-estimated vs fixed
5. Cluster variable table m_A(z), r_A(z), k_A(z) OR confirmation of AI interpretation route

**Microphysics (PRIORITY 2 — determines applicability of external constraints):**
6. Thermal history: thermally populated at BBN? T_dark/T_visible?
7. Self-interactions: collisionless or SIDM? σ/m? Dipole = DM-DM scattering or modified gravity?
8. Scale range: dipole operates at Mpc or kpc? Dissipative or halo-like?

If any are still being worked out or are proprietary, I will document that as "not yet specified in published materials" and move on. I am **not** expecting you to derive new results for my audit — I am just trying to avoid misrepresenting what you have already published or communicated.

---

## 7. Email Version (Concise)

**Subject:** Reproducibility Audit — Clarification Questions on IDM/MULTING

Dear Dr. Buckholtz,

I am building a small reproducibility audit for selected parts of your IDM/MULTING work. My goal is not to validate or challenge the model, but to separate definitions from predictions and avoid misrepresenting your work.

I have verified that beta_d = 4.5 and beta_q = 18.0 appear in Table A1 (Appendix A.3) as fitted values. I am treating them as fit-reproduction parameters (not theoretical predictions) to avoid circular reasoning.

To proceed, I need clarification on four points:

**H-MULT fit reproduction:**
1. Could you provide the explicit H_MULT(z; beta_d, beta_q) functional form (monopole + dipole + quadrupole combination)?
2. Which H(z) dataset was used in Table A1 (cosmic chronometers? Pantheon+? BAO?)?
3. How is sigma_MULT (fit quality metric) defined?
4. Which quantities (m_A, r_A, k_A, D_C:AB) were AI-estimated vs fixed?

**IDM microphysics (determines applicability of BBN, SIDM, Gaia constraints):**
5. Do dark isomers contain thermally populated relativistic particles at BBN (T ~ MeV)? If yes, what is T_dark/T_visible?
6. Are dark isomers collisionless (σ/m ~ 0) or self-interacting? Are dipole/quadrupole DM-DM scattering or modified gravity?
7. At what scales does dipole operate (cosmological Mpc or galactic kpc)? Are isomers dissipative (dark atoms, radiative cooling)?

If any are still being finalized, I will document "not yet specified" and move on. I am not asking for new derivations — just trying to source-ground my audit before doing further modeling.

Full details: [link to docs/26 if sending repo]

Best regards,  
[Your name]

---

## 8. PPN Questions (Priority 2 — After H-MULT Formula)

**Purpose:** Assess whether MULTING dipole/quadrupole terms are consistent with Solar System tests (Cassini light deflection γ parameter, Mercury perihelion β parameter).

**Current status:** PPN check is BLOCKED — MULTING lacks weak-field metric, Solar System limit, k_A definition, and COM frame specification.

**Questions:**

### Q8: Metric Formulation
> Does MULTING have a weak-field metric (g_μν = η_μν + h_μν), or is it formulated as a Newtonian-style force correction?

**If metric:** Could you provide the weak-field expansion to O(GM/rc², v²/c²)? This would allow extracting PPN parameters γ and β.

### Q9: Local Applicability
> Do dipole/quadrupole terms apply to ordinary matter (Sun, planets) or only to dark matter clusters?

**Context:** r_d = beta_d × r_A ~ 4.5-45 Mpc (cosmological scale), Solar System r ~ 10⁻⁸ Mpc. Is there a scale cutoff (e.g., dipole vanishes for r << r_d)?

### Q10: Kinetic Energy Parameter k_A
> What is k_A for the Sun? For Earth?

**Context:** Manuscript mentions "sub-object kinetic energy" k_A in dipole term description. Is k_A = (1/2) M v² (classical kinetic energy)? Relative to what frame (Solar System COM? Galaxy COM? Cosmic rest frame)?

### Q11: COM Frame Behavior
> Does the MULTING dipole term vanish when computed in the center-of-mass frame of the system?

**Why this matters:** If dipole vanishes in COM, it may be frame-dependent artifact rather than physical dipole moment.

### Q12: Preferred Frame Effects
> Is MULTING Lorentz-invariant, or does it introduce a preferred cosmic rest frame?

**Context:** If dipole is velocity-dependent relative to cosmic rest frame, PPN parameters α₁, α₂ would deviate from zero. Constraints are very tight: α₁ < 10⁻⁴ (lunar laser ranging), |α₂| < 4×10⁻⁷ (CMB dipole).

### Q13: Solar System PPN Recovery
> Does MULTING recover γ = 1 and β = 1 (GR values) in the Solar System?

**Context:** Current constraints are γ - 1 = (2.1 ± 2.3) × 10⁻⁵ (Cassini), β - 1 = (-4.1 ± 7.8) × 10⁻⁵ (Mercury). Is there a section in your work addressing Solar System constraints?

**If cluster-scale only:** If dipole/quadrupole activate only at r ~ r_d ~ Mpc scales, Solar System PPN checks may not apply.

**Interpretation branches (NOT claims — questions for clarification):**
1. If dipole = local mass distribution → PPN γ, β likely ≠ 1
2. If dipole = kinetic energy (galaxy frame) → preferred frame risk (α₁ constraints)
3. If dipole = velocity-dependent → Local Lorentz Invariance violation (α₁, α₂ constraints)
4. If dipole = metric modification → need weak-field expansion
5. If dipole = cluster-scale only (r < r_d cutoff) → PPN not applicable
6. If dipole = phenomenological H(z) only → no local predictions

**Safe vs unsafe wording:**

✅ **Safe:**
- "PPN check is currently not possible because MULTING lacks a weak-field metric. Author clarification required."
- "If dipole is cluster-scale only (r ~ Mpc), Solar System PPN checks may not apply."

❌ **Avoiding:**
- "MULTING is ruled out by PPN constraints" (no checks performed)
- "MULTING violates Solar System tests" (no local predictions available)
- "PPN parameters show MULTING is inconsistent with GR" (no PPN parameters derived)

**Detailed analysis:** See docs/29_ppn_quick_check_requirements.md (7 PPN checks, all BLOCKED) and docs/30_multing_solar_system_limit_questions.md (7 open questions).

### Q14: Row 1 Table A1 Sigma Standardization

> While checking Table A1, I found that the sigma columns appear internally consistent for Rows 2–12, but Row 1 at z=0 seems to use a different convention or contains an ambiguity. Could you clarify whether the z=0 row was treated as an anchor point, whether the sigma value is signed or absolute, and which H-data uncertainty should be used?

**Context:** Row-level sigma consistency audit (with adaptive tolerance by decimal precision) found:

**Row 1 (z=0):**
- sigma_MULT reported: 1.30 (positive)
- sigma_MULT calculated: (71.1 - 73.0) / 1.1 = -1.727 (negative)
- Difference: 3.027 >> tolerance 0.11 (**27× exceeded**)

**Rows 2–12 (z=0.06 to 8.5):**
- sigma_MULT: max diff = 0.001 ✅ (all within tolerance)
- sigma_FLRW: max diff = 0.039 ✅ (all within tolerance)

**Additional observation:** PDF Table A1 shows "H-data: 73.0 ± 1.6" for Row 1, but sigma_FLRW back-calculation is more consistent with sigma_H = 1.1 than 1.6. This suggests that H-data observational uncertainty (±1.6) may differ from the sigma_H value used for standardization (1.1).

**Possible interpretations:**
1. Row 1 sigma_MULT is reported as absolute value |1.727| ≈ 1.30 (rounded)
2. z=0 anchor point uses different standardization formula
3. Transcription or rounding convention specific to z=0

**Impact:** This is a **localized** issue — Rows 2–12 remain internally consistent. I am currently excluding Row 1 from any internal diagnostic fits until this is clarified.

**Safe wording:** I may be misunderstanding the standardization procedure at z=0. Could you clarify the computational step for Row 1 sigma values, or confirm whether the printed Table A1 values are correct as-is?

### Q15: Force-to-Expansion Bridge Method

> I may be misunderstanding the intended computational bridge from MULTING pairwise forces to the Hubble parameter H(z). I am exploring a possible interpretation where the pairwise MULTING acceleration F_oP/μ is converted into a scale-factor acceleration by dividing by the intercluster distance D_AB:
>
> ä/a = N_eff × F_oP / (μ × D_AB)
>
> where N_eff is an effective neighbor count or averaging factor. Is this close to the intended calculation route for Table A1, or does the AI service use a different averaging or phenomenological rule?

**Context:** After conducting a mathematical stress test of possible F_oP → H_MULT(z) bridge candidates (docs/43_bridge_candidate_math_stress_test.md), I found:

**Candidate B (Discrete Lattice ODE):**
- Formula: ä/a = N_eff × F_oP(D_AB, z) / (μ × D_AB)
- Dimensional check: ✅ PASS — [F/(μ×D)] = [acceleration/length] = [1/time²] = [ä/a]
- Sign convention: ✅ VERIFIED — consistent with late-time acceleration if dipole (repulsive) dominates
- Status: **BEST internal reconstruction candidate** (not source-confirmed)

**Missing inputs for this route:**
- m_A(z), k_A(z), r_A(z) — cluster variable evolution
- D_AB(z) — intercluster distance (cosmological or peculiar?)
- N_eff — averaging factor / neighbor geometry

**Alternative: Phi(z) heuristic (from AI transcript):**
- Formula: H_MULT²(z) = H_anchor² × [Phi(z) / Phi_anchor]
- Status: Useful for Table A1 reproduction, but dimensionally under-specified (force **ratios** → H² without explicit length scale D_AB)
- Classification: TABLE_REPRODUCTION_HEURISTIC_ONLY (not a forward predictive model)

**Why this matters:**
- If the bridge is discrete lattice averaging → cluster variables required for MCMC
- If the bridge is phenomenological scaling → Table A1 reproduction only, no prediction on new z
- If the bridge is something else → please clarify so I can represent it accurately

**Safe wording:** I am exploring a possible computational interpretation. Is this close to the intended Table A1 calculation route, or does the service use a different method?

---

## 9. Next Steps After Receiving Response

**If H-MULT formula received:**
- Implement H_MULT(z; beta_d, beta_q) solver
- Reproduce Table A1 fit
- Compare H-MULT vs H-FLRW fit quality on same dataset
- Document results in `docs/18_fit_reproduction_requirements.md`

**If microphysics clarified:**

| Answer | Action |
|--------|--------|
| Isomers thermally populated at BBN | Upgrade Finding 7 (BBN/N_eff) to `gold_candidate`, compute or request N_eff prediction |
| Isomers cold at BBN | Mark Finding 7 as `not_applicable`, archive |
| Isomers self-interacting | Upgrade Finding 8 (SIDM/Bullet Cluster) to `gold_candidate`, request σ/m |
| Isomers collisionless | Mark Finding 8 as `not_applicable` |
| Dipole operates at kpc scales | Upgrade Finding 9 (Gaia/dark disk) to `gold_candidate` (if dissipative) or `partially_applicable` (if non-dissipative) |
| Dipole only Mpc scales | Mark Finding 9 as `not_applicable` |

**If no response or "still being finalized":**
- Document blocker explicitly in README.md
- Publish repository as incomplete but transparent
- Note: "Further work requires author clarification on [X, Y, Z]"
- Move on to other projects

---

## 10. Acknowledgment

I want to emphasize:
- I am **not** claiming to validate or refute IDM/MULTING
- I am **not** using this audit to "disprove" your model
- I **am** trying to build a transparent, source-grounded reproducibility layer
- I **am** separating what is clearly defined (beta values from Table A1) from what requires clarification (H-MULT formula, microphysics)

Your work proposes interesting ideas (6 isomers, multipole cosmology, Eq.15 relation), and I want to represent them accurately. If I have misunderstood anything in this brief, please let me know.

Thank you for your time.

---

**Attachments (if sending full repo):**
- `docs/18_fit_reproduction_requirements.md` — full list of what's needed for fit reproduction
- `docs/23_gold_candidate_bbn_neff_source_check.md` — BBN/N_eff applicability analysis
- `docs/24_gold_candidate_sidm_bullet_cluster_source_check.md` — SIDM/Bullet Cluster applicability analysis
- `docs/25_gold_candidate_dark_disk_gaia_source_check.md` — Gaia/dark disk applicability analysis
- `docs/22_discovery_ledger.md` — summary of all 11 findings from audit

**Note:** These documents are internal audit materials. They contain technical details and safe/unsafe wording templates. The questions above are the core items I need clarification on.
