# MULTING / H_MULT — Diagnostic Brief
**Prepared for: Meeting with Dr. Thomas J. Buckholtz**
**Status: AUDIT FINDINGS — not a refutation, a precision protocol**
**Evidence level: [VERIFIED] from Supplementary arXiv:2025.11.0598.v6 unless marked**

---

## A. CONFIRMED (from Supplementary)

- Force ansatz clearly stated: `F_total = F_m − F_d + F_q`
- Dipole length: `r_dA = β_d × r_A` (β_d is a length-ratio multiplier, not a power-law exponent)
- Quadrupole amplitude: `F_q ~ β_q² × r_A² / D⁴`
- All three AI services (ChatGPT, Claude, Gemini) applied Step 1–8 protocol consistently
- β values were chosen to **minimize σ** from observed H(z) data (Step 5, all transcripts)

---

## B. AUTHOR BRIDGE NOT CONFIRMED (missing forward path)

- No explicit formula mapping `F_total(z) → H_MULT(z)` appears in main paper or Supplementary that we could independently verify
- H_MULT values in Table A1 are **AI-service outputs** — their exact computational path is not shown
- Our reconstructions (Option 1–5 candidates) remain **OUR_RECONSTRUCTION_ONLY** — not author-validated
- The computational path `force law → acceleration ODE → H(z)` was not confirmed by TJB in available materials

> **Key question:** Can you provide the explicit derivation or code mapping MULTING force terms to H_MULT(z), so we can confirm which bridge you intended?

---

## C. FITTED PARAMETERS (not predictions)

| AI Service | β_d  | β_q   | Spread |
|-----------|------|-------|--------|
| ChatGPT   | 0.78 | 0.19  |        |
| Claude    | 4.50 | 18.00 |        |
| Gemini    | 4.25 | 8.10  |        |
| **Range** | **5.8×** | **94.7×** | β_q² range: **8975×** |

β_d and β_q are a **phenomenological-estimation layer**: each AI service minimized σ against observed H(z) data (Step 5). TJB acknowledged this is a "phenomenological computation" aspect. At 94.7× spread in β_q, the result is sensitive to which AI ran Step 5 — they are not independently derived physical constants.

> **Key question:** Which AI service's β values appear in Table A1 of the main paper?

---

## D. MECHANISM FAILURE (numbers from Supplementary)

From **Claude Supplementary, Step 6** (lines 1316–1326):

```
F_d / F_m at D = 50 Mpc = 2 × k_A × β_d × r_A / (m_A × D)
                         ≈ 2 × 3.16e12 × 4.5 × 1.7 / (3.16e14 × 50)
                         ≈ 3.1 × 10⁻³
```

- Dipole-monopole crossover radius: **r_crossover ≈ 0.153 Mpc** [from Supplementary line 1326]
- Typical cluster radius: ~1.7 Mpc
- Typical inter-cluster separation: ~50 Mpc

**Dipole dominates only at r < 0.153 Mpc — sub-cluster scales, not cosmological.**

For F_d/F_m = 1 at D = 50 Mpc: requires **β_d ≈ 1471** (327× larger than current value).

C11/C12 ("dipole dominance at late times") are falsified for all three AI-generated parameter sets at inter-cluster distances.

---

## E2. H_FLRW TABLE MISMATCH (Q5 finding) [COMPUTED]

Stated formula [VERIFIED line 1226]: `H_FLRW(z) = 67.4 × √(0.315(1+z)³ + 0.685)`

Actual Table A1 values vs formula output:

| z    | H_FLRW (table) | Formula output | Δ%    |
|------|---------------|----------------|-------|
| 0.06 | 68.1          | 69.5           | −2.0% |
| 1.00 | 95.7          | 97.1           | −1.4% |
| 8.50 | 398.5         | ~712           | ~−44% |

Root cause [INFERRED from line 1257]: "time↔z conversion uses standard cosmology as a coordinate tool only" — the Table uses an approximate chronology (t↔z lookup) that diverges from the exact ΛCDM integral at high z.

> **Key question (Q5):** Do the z values in Table A1 come from exact ΛCDM inversion ∫dz/H(z) or an approximation? The high-z rows show up to 44% mismatch with stated formula.

---

## E3. H_MULT OPERATIONAL NATURE (Q6 finding) [VERIFIED + COMPUTED]

**Hypothesis-arbiter verdict:**

| Hypothesis | Kill-test | Result |
|-----------|-----------|--------|
| H₁: H_MULT = metric ȧ/a (BAO/SNe-ready) | χ(z) = ∫c dz/H_MULT vs BAO DM | **KILLED at z > 1.5** |
| H₂: H_MULT = phenomenological, table-level only | Lines 663–665, 1200 ("Friedmann-like"), 1366 (w_eff post-hoc) | **SURVIVES** |

**χ(z) kill-test results** (trapezoidal from 12 Table A1 points):

| z    | χ_MULT (Mpc) | χ_ΛCDM (Mpc) | Δ%      | Verdict |
|------|-------------|-------------|---------|---------|
| 0.38 | 1499.5      | 1511.0      | −0.8%   | OK      |
| 0.51 | 1951.6      | 1975.0      | −1.2%   | OK      |
| 0.61 | 2295.2      | 2306.5      | −0.5%   | OK      |
| 1.50 | 4805.0      | 4483.2      | +7.2%   | WARN    |
| 3.20 | 7986.9      | 6695.6      | +19.3%  | FAIL    |
| 8.50 | 13332.2     | 9272.4      | +43.8%  | FAIL    |

**Note:** Low-z BAO agreement (<1.2%) is an accidental cancellation between higher H₀ anchor (73.0 vs 67.4) and Φ(z) shape — not evidence of metric equivalence.

**Implication:** H_MULT cannot be substituted into BAO likelihoods at z > 1, SNe distance moduli, or CMB distance priors without an explicit metric derivation.

> **Key question (Q7):** Does H_MULT represent the metric expansion rate H = ȧ/a — such that comoving distances χ(z) = ∫c dz/H_MULT can be compared directly to BAO DM measurements — or is it an effective quantity valid only for table-level comparison with cosmic chronometer H(z)?

---

## E. WHAT IS INTERESTING

**CPL projection of H_MULT** (effective dark energy parametrization of H_MULT shape):

| Parameter | H_MULT CPL fit | DESI+CMB+DESY5 | σ-distance |
|-----------|---------------|----------------|-----------|
| w₀        | −0.690        | −0.725 ± 0.071 | **0.49σ** ✅ |
| wₐ        | +0.402        | −1.06 +0.35/−0.31 | **4.18σ** ❌ |
| H₀        | 68.83         | 67.19 ± 0.69   | **2.38σ** ⚠️ |

*[VERIFIED] DESI values from JCAP 2025 021 (arXiv:2404.03002v3), Table 3, DESI+CMB+DESY5 w0waCDM row.*

H_MULT reproduces DESI-like w₀ to within 0.49σ, but the dark energy *evolution* (wₐ) strongly disagrees with DESI+DESY5 (4.18σ). H₀ from CPL fit (68.83) is 2.38σ above DESI w0waCDM value (67.19) — expected, since H_MULT is anchored to SH0ES H₀=73.0.

**Also:** Claude's Supplementary (line 1413) states DESI hints at `w₀ < −1` and `wₐ > 0`, but DESI+CMB+DESY5 actually gives `w₀ = −0.725 > −1` and `wₐ = −1.06 < 0` — both signs reversed.

---

## F. KEY QUESTIONS FOR MEETING (Q1–Q12 index)

*Q1–Q7 below. Q8–Q12 are in sections G–H4 (detailed findings with evidence).*

1. **Bridge (Q1):** "Can you share the explicit formula or code that maps MULTING forces to H_MULT(z)? The Supplementary shows AI outputs but not the derivation step."

2. **Provenance (Q3):** "β_q varies 94.7× across the three AI transcripts (0.19 to 18.0). Which parameter set underlies Table A1 in the main paper?"

3. **Mechanism (Q3/C11):** "At D = 50 Mpc with the Claude parameters, F_d/F_m ≈ 0.003 — dipole dominates only below 0.153 Mpc. Is there a version of the model where dipole repulsion operates at inter-cluster scales?"

4. **Cluster parameters (Q4):** "The Supplementary uses geometric means of log-ranges for m_A and k_A, arithmetic means for r_A and D. Are these the exact values you intended for Table A1, or were different cluster parameters used in the main paper?"

5. **H_FLRW chronology (Q5):** "Do the z values in Table A1 come from exact ΛCDM inversion ∫dz/H(z), or an approximate t↔z lookup? At z = 8.5 the Table H_FLRW (398.5) differs ~44% from the stated formula output."

6. **Metric nature (Q7 — critical):** "Does H_MULT represent the metric expansion rate H = ȧ/a — such that comoving distances χ(z) = ∫c dz/H_MULT can be compared directly to BAO DM measurements at z > 1 — or is it an effective quantity valid only for table-level comparison with cosmic chronometer H(z)?"

---

## G. BRIDGE AMBIGUITY — AI SELF-DISCLOSURE (Q8 finding) [VERIFIED lines 562–587]

The Claude AI Supplementary explicitly admits the bridge is undefined — and lists 4 options:

> *"no explicit mapping has yet been defined between pairwise intercluster forces and the large-scale expansion scalar H(z)... several distinct possibilities exist:"*
> 1. Newtonian shell: D̈ ∝ F/M
> 2. Energy balance: Ḋ² ~ U_eff(D)
> 3. Phenomenological ansatz: H² ∝ ⟨FD⟩
> 4. Effective-fluid reinterpretation with pressure term
> *"Please tell me which approach you want me to use."*

**What each AI received:**
- ChatGPT [line 594]: TJB specified Option 1 (Newtonian). ChatGPT used D̈ ∝ F/M.
- Claude: AI used "effective pressure" language (line 1194) but implemented Option 3 — H²∝Φ(z)/Φ(anchor) (lines 1201–1209).
- Gemini: [unknown — not visible in Supplementary excerpt]

**Internal contradiction in Claude Supplementary:** labels the approach "effective pressure" (Option 4 language) but implements a normalized ratio (Option 3). These produce different optimal β values.

**User candidate P_eff = −⟨r·F_oP⟩/(3V) is Option 4.** Claude implemented Option 3. They are physically distinct — Option 4 enters via ä/a = −4πG(ρ+3P_eff)/3; Option 3 enters via H²∝ρ_eff directly.

> **Key question (Q8):** "Is the intended bridge for Table A1 related to an effective-pressure / virial approach — P_eff = −⟨r·F_oP⟩/(3V) — used as an effective fluid term in a Friedmann-like acceleration equation? Or is the direct normalized ratio H²∝Φ(z)/Φ(anchor) closer to your intent? I am not assuming either — I am asking whether this family of bridges is close or wrong."

---

## H4. FORCE → POTENTIAL → H_MULT (Q12 finding) [VERIFIED main paper lines 387–391, 398, 1546]

**Full IDM force law has velocity-dependent terms** [line 387–391]: retarded-time r + (ṁ_oP)ṙ terms present, but TJB **de-emphasizes** them: *"We assume that modeling can adequately de-emphasize terms… that might appear as additional additive terms."*

**After de-emphasis:** Eq. (4) becomes F = F(r) only — a conservative central force. V(r) = −∫F_oP dr is well-defined:
- V_m ≈ −G T_m / D (monopole, ~1/D)
- V_d ≈ −G T_d / (2D²) (dipole, ~1/D²)
- V_q ≈ −G T_q / (3D³) (quadrupole, ~1/D³)

**Critical scaling gap** [COMPUTED]:
- Energy balance bridge: H² ∝ V/D² ∝ **Φ(z)/D(z)** (extra 1/D factor)
- Phenomenological ratio bridge (Claude AI): H² ∝ **Φ(z)/Φ(anchor)** (no D factor)
- At z=0→8.5, D changes ~10×: the two bridges give materially different H(z) shapes and different optimal β.

**Lagrangian: future work** [line 1546]: *"Develop a full set of field equations and Lagrangian terms for MULTING+IDM"* — no formal Lagrangian yet.

> **Key question (Q12):** "In the de-emphasized force law (Eq. 4), V(r) = −∫F_oP dr is well-defined. The energy-balance bridge Ḋ²~2[E−V(D)]/m_P gives H²∝Φ/D — an extra factor of 1/D vs the direct ratio H²∝Φ(z)/Φ(anchor) that the AI used. Would integrating the force terms into V(r) misrepresent the intended calculation, or is the energy-balance approach closer to your intent?"

## H3. ISOTROPIC LIMIT (Q11 finding) [VERIFIED main paper line 554 + 1422]

**MULTING is explicitly a directed-pair model.** Main paper line 554: *"We consider 3-vectors r that share one direction (that is, the 3-vectors are parallel to each other)."* All force terms in Supplementary line 1199 are scalar projections along r̂.

**Tension between levels:**
- Micro (two-body): directed pair, non-isotropic by design [line 554]
- Macro (cosmological): H²∝Φ applied as global isotropic H(z) — Friedmann-like assumes isotropy

**Not-spherically-symmetric aspects** acknowledged as future work [main paper line 1422]: *"Determine the extent to which not-spherically-symmetric aspects of MULTING repulsion…"* — current version does not resolve the isotropic transition.

**Hypothesis-arbiter verdict:**
- H₁ (dipole cancels in isotropic limit): KILLED by design — model is explicitly directed, not an isotropic ensemble
- H₂ (NN structure preserves nonzero dipole): SURVIVES — single directed pair, F_d always repulsive along r̂
- H₃ (tension between directed micro and isotropic macro): SURVIVES — open question, acknowledged by TJB as future work

> **Key question (Q11):** "The force law is defined for a directed pair, and the main paper notes that not-spherically-symmetric aspects are a future research direction. In a large-scale isotropic distribution of neighboring clusters, directed dipole contributions might average over orientations. Does the model address the transition from a directed pair to a global isotropic H(z)? Is there a sense in which the dipole persists — e.g., because the nearest-neighbor network has a preferred connectivity — or is this handled implicitly by the single representative pair?"

## H2. LATTICE / NEIGHBORING-CLUSTER STRUCTURE (Q10 finding) [VERIFIED + INFERRED]

**Zero matches** for "lattice", "voronoi", "tessellation", "cell", "node", "periodic" in Supplementary [VERIFIED].

**TJB prompt** [lines 193, 215–217, 228–230, 534]: uses "neighboring non-colliding" and "nearest-neighbor separations" — NN language present but **neighbor relation never formalized**.

**AI implementation** [line 1193]: resolved ambiguity as a single representative two-body pair (arithmetic mean of D range) — mean-field, not lattice.

**Dimensional gap** [INFERRED from lines 1201–1209]: Φ has units [acceleration = m/s²]; H² has units [s⁻²]. Bridge H²∝Φ is dimensionally inconsistent without a length divisor. A Voronoi cell diameter D_cell would provide it. Current implementation avoids the issue via anchor normalization (ratio Φ/Φ₀ is dimensionless).

**Cross-domain:** Lindquist–Wheeler (1957, Rev.Mod.Phys.) placed N Schwarzschild masses at lattice nodes and showed H_lattice ≈ H_FLRW — a direct structural analog. If MULTING clusters are lattice nodes with IDM force law, the bridge to H(z) is grounded.

> **Key question (Q10):** "Is MULTING intended to model clusters as nodes in a nearest-neighbor network or Voronoi tessellation — where each cluster owns a domain ~D³ and H(z) emerges from averaging Φ over that domain? Or is the single representative pair (mean-field) the intended level? A lattice/Voronoi interpretation would (a) fix the dimensional bridge Φ→H²; (b) connect to Lindquist–Wheeler cosmology; (c) enable non-zero kinematic Q_D from cell variance."

## H. BUCHERT / BACKREACTION (Q9 finding) [VERIFIED by grep + structure]

**Zero mentions** of "Buchert", "backreaction", "Q_D", "kinematic backreaction", or "domain averaging" in Supplementary or main paper [VERIFIED].

**Hypothesis-arbiter verdict:**

| Hypothesis | Kill-test | Result |
|-----------|-----------|--------|
| H₁: Q_D intended explicitly | grep: 0 matches for Buchert/Q_D/backreaction | **KILLED** |
| H₂: Averaging = parameter estimation only | Single representative pair [lines 1210–1215] | **SURVIVES** |
| H₃: Q_D emergent consequence | No ensemble of pairs → no Var(θ) → Q_D = 0 by construction | **KILLED** |

**Structure:** MULTING uses one representative cluster pair (geometric/arithmetic mean of ranges). Buchert Q_D requires a spatial field θ(x) over a domain. Single-pair model → Q_D = 0 by construction, not a physical result.

**Open extension:** If an ensemble P(D) were used instead of a single D, Q_D = Var[H_MULT(D)] ≠ 0 would emerge naturally — a legitimate Buchert backreaction from MULTING. Not currently implemented.

> **Key question (Q9):** "Does MULTING involve Buchert-style domain averaging, with dipole repulsion contributing to Q_D = ⅔[⟨θ²⟩−⟨θ⟩²]? The Supplementary uses a single representative pair rather than an ensemble, making Q_D = 0 by construction. Is this correct, or is there an intended ensemble interpretation — e.g., integrating over P(D) — from which Q_D ≠ 0 would emerge?"

---

---

## J. H_FLRW CONVENTION RECOVERY [VERIFIED — hflrw_recovery.py]

**Confirmed:** H_FLRW in Table A1 is NOT standard ΛCDM. [VERIFIED prev sweep, MAE>100 for all ΛCDM variants]

**Recovery: H² = H₀²[Ωm(1+z)^n + (1-Ωm)], sweeping n**

| Model | n | Ωm | MAE (km/s/Mpc) | Verdict |
|-------|----|-----|-----------------|---------|
| ΛCDM Planck | 3.0 | 0.315 | 110.3 | KILLED |
| H_FLRW best fit | **2.0** | **0.389** | **2.96** | ✅ RECOVERED |
| Power law H₀(1+z)^0.769 | — | — | 11.8 | weak |
| H=β/t^γ (time-based) | — | — | 7.8 | weak |

**Finding:** H_FLRW ≈ H₀√[0.389·(1+z)² + 0.611] (MAE = 2.96 km/s/Mpc)

The (1+z)² scaling — as opposed to standard (1+z)³ — physically corresponds to a **spatial curvature term** in Friedmann cosmology (open FLRW with Ωk=0.389, ΩΛ=0.611, Ωm≈0). This is NOT matter+Λ ΛCDM.

**Local growth rate [COMPUTED]:** H_FLRW grows as ~(1+z)^0.18 at z=0 and ~(1+z)^0.89 at z=8.5 — far below ΛCDM's ~(1+z)^1.5 at high z. Ratio: H_FLRW/H_ΛCDM ~ (1+z)^{−0.39}.

**Consequence:** All σ_FLRW values in Table A1 use this non-ΛCDM baseline. If σ_FLRW is presented as "ΛCDM residual," the comparison is systematically misleading.

> **Key question (Q5-updated):** "The H_FLRW column in Table A1 is best described by H ≈ H₀√[0.39·(1+z)² + 0.61] (MAE ≈ 3 km/s/Mpc), which grows ~2.78× slower at z=8.5 than standard ΛCDM. This resembles an open/curvature-dominated Friedmann model (Ωk(1+z)², not Ωm(1+z)³). What cosmological model generates the H_FLRW column — standard ΛCDM, your own IDM background, or something else?"

## I. FAIRNESS DIAGNOSTICS [VERIFIED — fairness_diagnostics.py] [secondary — computational]

**Question:** Does H_MULT's better χ² survive AIC/BIC after DoF correction?

### Model comparison (n=12 Table A1 points)

| Model | χ² | k | AIC | RMS_σ | Notes |
|-------|----|---|-----|-------|-------|
| ΛCDM Planck vanilla | 41.70 | 0 | 41.70 | 1.864 | Planck H₀=67.4, unfitted to this data |
| ΛCDM SH0ES (H₀=73.0, Ωm free) | 17.20 | 1 | 19.20 | 1.197 | Same H₀ anchor as H_MULT |
| ΛCDM free (H₀, Ωm both free) | 15.44 | 2 | 19.44 | 1.134 | Best possible ΛCDM |
| **H_MULT reported (β_d, β_q)** | **0.263** | **2** | **4.26** | **0.148** | β_d=4.5, β_q=18.0 fitted to this data |

**ΔAIC (positive = H_MULT wins):**
- vs ΛCDM Planck vanilla: +37.4 ← 75% from anchor mismatch, not physics
- vs ΛCDM SH0ES (same anchor, k=1): **+14.9** ← decisive by Jeffreys scale (>10)
- vs ΛCDM free (same DoF, k=2): **+15.2** ← decisive

### Three findings

**Finding 1 — Anchor effect (75% of vanilla advantage)** [VERIFIED]:
z=0 row contributes 31.4/41.7 = **75%** of ΛCDM Planck's χ². Reason: H_MULT anchors to H₀=73.0, so σ_MULT(z=0) = 0 by construction; ΛCDM Planck uses H₀=67.4 → σ_FLRW(z=0) = −5.6 (SH0ES tension). Three-quarters of H_MULT's apparent advantage disappears when ΛCDM is given the same H₀ anchor.

**Finding 2 — H_MULT still wins decisively after equalization** [VERIFIED]:
Even with ΛCDM anchored to SH0ES H₀=73.0 and Ωm free (k=1 vs H_MULT's k=2), ΔAIC = +14.9. After DoF correction H_MULT genuinely fits the H(z) curve shape better than ΛCDM — not an artifact.

**Finding 3 — ΛCDM+SH0ES requires unphysical Ωm** [VERIFIED]:
Best-fit ΛCDM with H₀=73.0 (SH0ES) needs Ωm = 0.082 — far below CMB+BAO value of ~0.30. The optimizer hit the lower boundary. This means: **ΛCDM and SH0ES H₀ are mutually inconsistent with the H(z) data shape.** H_MULT resolves this by using a non-ΛCDM shape — but at the cost of 2 tuned parameters.

> **Key question (fairness):** "H_MULT achieves ΔAIC=+15 over ΛCDM_SH0ES with the same DoF. But ΛCDM with SH0ES H₀ requires Ωm~0.08 (vs CMB/BAO ~0.30) — suggesting the H(z) shape itself constrains this. Would a fairer comparison be H_MULT (3 params: H₀, β_d, β_q) vs w₀wₐCDM (3 params: H₀, w₀, wₐ) on these 12 points?"

*[secondary — raise only if discussion turns to statistical comparison]*

---

## K. RANGE UNDERDETERMINATION (Direction 5) [VERIFIED — range_underdetermination.py]

**Question:** Does the 94.7× spread in β_q reflect genuine physics, or a structural under-specification of cluster parameters?

### K1. Effective coupling analysis (at z=0)

| Service | ε_d = F_d/F_m | ε_q = F_q/F_m | β_q |
|---------|--------------|--------------|-----|
| Claude  | 1.10×10⁻³   | **1.54×10⁹** | 18.00 |
| Gemini  | 1.62×10⁻³   | **2.87×10⁹** | 8.10 |
| ChatGPT | 1.91×10⁻⁴   | **1.71×10⁵** | 0.19 |

[VERIFIED from range_underdetermination.py, Section A]

**Critical observation:** ε_q >> 1 for ALL three services. The quadrupole term (F_q) exceeds the monopole (F_m) by factors of 10⁵ to 10⁹. ChatGPT's β_q = 0.19 — the smallest — still gives ε_q = 170,000.

### K2. Quadrupole dominance theorem [INFERRED from ε_q >> 1]

When ε_q >> 1, the Φ formula simplifies:

```
Φ(z) = m_A/D² − 2·k_A·β_d·r_A/D³ + k_A²·β_q²·r_A²/D⁴
     ≈ k_A²·β_q²·r_A²/D⁴         (quadrupole term dominates)

Φ(z)/Φ(0) ≈ [D(0)/D(z)]⁴       (β cancels in ratio)
```

**Consequence:** In the quadrupole-dominated limit, H²_MULT(z)/H²_anchor ≈ [D(0)/D(z)]⁴ — **independent of β_d and β_q**. The bridge is determined entirely by how D(z) evolves with z, not by optimization of β.

### K3. Optimization landscape: completely flat [VERIFIED]

Grid scan over β_d ∈ [0.1, 20], β_q ∈ [0.05, 50] (25×35 = 875 points):
- Every single point: RMS_σ = **6.525** (identical to 4 decimal places)
- β_q range within RMS_σ < 7.02: **1000× span** (0.05 to 50)
- No gradient: no ridge, no valley, no preferred β direction

[VERIFIED range_underdetermination.py, Section C]

**Root cause of flat landscape:** Since ε_q >> 1 for all β in the scan, Φ(z)/Φ(0) ≈ [D(0)/D(z)]⁴ regardless of β — β leaves no fingerprint on H_MULT(z).

### K4. β_q spread is algebraically guaranteed by k_A range [VERIFIED]

From Section B of script: 100× range in k_A (1e11 to 1e13 M_sun) requires 100× compensation in β_q to maintain constant ε_q:

| k_A (M_sun) | β_q needed for same ε_q |
|-------------|------------------------|
| 1×10¹¹      | 180.0 |
| 1×10¹²      | 18.0  ← Claude geom-mean |
| 1×10¹³      | 1.80  |

The 94.7× observed β_q spread is explained as: different AI services chose different representative k_A values from within the stated range (1e11–1e13), and compensated by choosing different β_q. All achieve ε_q >> 1, all give identical H_MULT shape.

### K5. True determinant of H_MULT(z): the D(z) schedule [INFERRED]

If H²_MULT(z) ≈ H²_anchor × [D(0)/D(z)]⁴, then for the formula to reproduce H_obs exactly, the AI services need:

```
D(z) = D(0) × [H_anchor / H_obs(z)]^{1/2}
```

Example: D(0) = 50 Mpc, H_obs(8.5) = 420 → D(8.5) = 50 × (73/420)^{1/2} = 50 × 0.417 = 20.8 Mpc.

The Claude cluster CSV gives D(8.5) = 3–15 Mpc (geom mean 6.7 Mpc). If the AI services used ~19–21 Mpc at z=8.5, they implicitly matched H_obs by D(z) choice — not β optimization.

> **Key question (Q14):** "At z=8.5, the quadrupole term ε_q = (k_A·β_q·r_A)²/(m_A·D²) ≫ 1 for all three AI parameter sets — meaning H²_MULT ≈ H²_anchor × [D(0)/D(z)]⁴, with β values having no influence on the shape. The fit quality is then determined by the assumed D(z) schedule, not by β optimization. Were the D(z) values at each redshift derived from a physical scaling relation (e.g., comoving-to-physical conversion of observed cluster separations), or chosen to reproduce H_obs(z)? This matters because it determines whether β_d and β_q are physical parameters or free handles on an already-determined curve."

---

## L. k_A CLOSURE TEST + DOUBLE INVERSION [NOT_VALIDATION — v0.4.0, 2026-06-06]

**Purpose:** Test whether Table A1 H_MULT **implementation** can use **independently specified** `k_A(z)` and physically admissible `D(z)` — without refitting β, k_A, or D. This is an **internal closure test**, not theory falsification.

| Item | Value |
|------|-------|
| Labels | NOT_VALIDATION, INTERNAL_CLOSURE_TEST, AUTHOR_CONFIRMATION_REQUIRED |
| MCMC | BLOCKED (`is_mcmc_allowed = False`) |
| β (fixed) | β_d=4.5, β_q=18.0 (Table A1 fitted — not refitted here) |
| D_required | γ_req ≈ 2.27 (z≥0.4) vs γ_csv ≈ 0.90 |
| PASS criterion | RMS_σ(indep k_A) ≤ 2× CSV retrodiction |

**Stage 1 (isolines):** For each z, plot `(D, k_A)` pairs satisfying `H_bridge = H_obs`; overlay physical box (`D > 2r_A`, k_A>0, CSV range).

**Stage 2 (grid):** `D(z)=D₀(1+z)^{-γ}`, `k_A(z)=k₀(1+z)^{-α}`; grid γ∈[0,4], α∈[-6,6]; find best physical vs unconstrained MAE.

> **Constructive question for Dr. Buckholtz:** Does k_A represent a physical kinetic-energy parameter estimable independently of H(z), or an effective fit coordinate in the Table A1 workflow?

> The most constructive next step may be to make k_A(z) an independently specified physical input rather than a fitted schedule. Does IDM/MULTING provide an independent rule for k_A(z), or would you be open to testing one using simulations or virial/ICM scaling?

**Files:** `src/k_a_closure_test.py`, `src/k_a_independent.py`, `src/double_inversion_*.py`, `audit/run_k_a_closure_audit.py`, `audit/run_double_inversion_diagnostic.py`, `docs/98`, `docs/99`, `docs/DOUBLE_INVERSION_DIAGNOSTIC.md`

---

---

## M. SELF-CONSISTENCY AUDIT [VERIFIED-tool — self_consistency_diagnostic.py, 2026-06-09]

**Safety:** NOT_VALIDATION, NOT_REFUTATION, NOT_AUTHOR_ERROR, INTERNAL_DIAGNOSTIC_ONLY
**Epistemics:** EXPLORATORY_DIAGNOSTIC, NOT_PREREGISTERED — findings discovered during analysis, not predicted in advance. Treat as hypothesis-generating, not confirmatory.

### M1. H_MULT = 1.074 × H_FLRW (Option 3 bridge decorativeness test)

| Stat | Value |
|------|-------|
| Mean ratio H_MULT / H_FLRW | **1.074** |
| Scatter (std/mean) | 2.6% |
| Pearson corr(H_MULT, H_FLRW) | **0.99993** |

[VERIFIED-tool] Across all 12 Table A1 rows, H_MULT tracks H_FLRW with near-perfect correlation. The **Option 3 bridge** (H²∝Phi/Phi₀ from Claude Supplementary) adds no independent H(z) information for these parameter sets — it is a ~7% scalar stretch of the FLRW baseline. Whether this holds for other bridge variants (Option 1: D̈∝F/M; Option 2: energy balance) is not tested here.

### M2. Self-consistency failure (bridge formula vs reported values)

Using Claude's own cluster params (CSV geometric means) + β_d=4.5, β_q=18.0:

| Quantity | z=0.00 | z=8.50 | Change |
|----------|--------|--------|--------|
| Phi(z)/Phi(0) | 1.000000 | 0.001313 | **DECREASES ×762** |
| H_pred(bridge) | 73.0 | **0.096 km/s/Mpc** | ×762 DROP |
| H_MULT_reported | 73.0 | **418.1 km/s/Mpc** | ×5.7 RISE |
| Reproduction gap (forward path) | — | — | **×4365 at z=8.5** |

[VERIFIED-tool] Using our reconstructed cluster params and Option 3 bridge, the forward path does not reproduce Table A1 H_MULT values: our H_pred **falls** to ~0.1 km/s/Mpc while Table A1 reports **418 km/s/Mpc**. Status: TABLE_A1_FORWARD_PATH_NOT_REPRODUCED from currently reconstructed formulas. [AUTHOR_BRIDGE_NOT_CONFIRMED — OUR_RECONSTRUCTION_ONLY]

**Implication:** The D(z) schedule actually used by the AI service to generate Table A1 must differ substantially from the CSV geometric-mean cluster params.

**Repr.value robustness (Part F multiverse):** Gap survives arithmetic-mean params — ×3944 vs ×4365 geom (9.7% change). Inconsistency is repr.value-robust at the documented endpoints [VERIFIED-tool, Part F].

### M3. Gemini cross-check (dataset independence)

| Service | β_d | β_q | H_pred behavior | Failure mode |
|---------|-----|-----|-----------------|--------------|
| Claude  | 4.50 | 18.00 | DECREASES monotonically | Trend reversal |
| Gemini  | 4.25 | 8.10  | FLAT (~73 km/s/Mpc all z) | No growth |

[VERIFIED-tool] Both services fail to generate observed H(z) growth — via different failure modes. Conclusion is **dataset-independent**: the bridge structure cannot produce a rising H(z) given physically declining cluster separation.

### M4. Claim table update

| Claim | Prior status | New status | Evidence |
|-------|-------------|------------|----------|
| C11: ε_q >> 1 (quadrupole dominates) | ✅ "at high z" | ✅ **corrected: ALL z** | ε_q ≥ 1.7×10⁵ at every row |
| C12: dipole dominates at late times | ⚠️ | ❌ **REFUTED** | max ε_d = 1.5×10⁻³, never > 1 |
| C14: bridge formula H²∝Phi exists | ✅ | ⚠️ **PARTIAL** | formula exists but gives wrong direction |

**C12 refutation:** Dipole dominance requires D < 2·k_A·β_d·r_A/m_A ≈ 0.015 Mpc at z=0. Actual inter-cluster separation D = 44.7 Mpc — three orders of magnitude larger. Dipole is **never** dynamically relevant at cosmological scales with these parameters.

### M5. Skeptic gate

[CONFIRMED-REAL] Three independent falsification tests attempted by skeptic agent:
1. Alternative β values → same forward-path reproduction gap (β cancels in ratio)
2. Gemini params → different failure mode, same conclusion
3. Real CC data (32 Moresco points) → ΛCDM n≈3 fits well; AI table best fit n≈2

All three failed to falsify the headline finding. Skeptic verdict: CONFIRMED-REAL.

> **Key question (Q15):** "Phi(z) computed from the CSV cluster parameters (geometric means of log-ranges) decreases ×762 from z=0 to z=8.5 — yet H_MULT in Table A1 increases ×5.7. This suggests the D(z) schedule actually used to generate Table A1 differs from the CSV geometric means. Could you clarify which D(z) values were used — and whether they come from a physical scaling relation or were chosen to match H_obs directly? This would let us close the largest open reproducibility gap."

---

## N. REAL DATA VERIFICATION [VERIFIED-REAL — Moresco et al., 2022-06-09]

**Safety:** NOT_VALIDATION, NOT_REFUTATION, COMPARISON_ONLY

### N1. Real cosmic chronometer coverage

The 12 H_obs entries in the AI Supplementary table span z = 0.00 – 8.50.

| z range | Real CC data (Moresco+) | AI table H_obs |
|---------|------------------------|----------------|
| z ≤ 1.965 | **32 published points** (Moresco 2022, arXiv:2201.07241) | 8 of 12 rows |
| z = 2.10 | No published CC data | AI row — **extrapolation** |
| z = 3.20 | No published CC data | AI row — **extrapolation** |
| z = 5.00 | No published CC data | AI row — **extrapolation** |
| z = 8.50 | No published CC data | AI row — **extrapolation** |

[VERIFIED-REAL] **4 of 12 AI table rows (z > 2) have no observational counterpart.** Cosmic chronometer observations currently reach only to z ≈ 1.97. The high-z rows are AI-generated extrapolations, not measured data.

### N2. ΛCDM fit to real CC data

Fitting H²(z) = H₀²[Ω_m(1+z)^n + (1−Ω_m)] to 32 real Moresco CC points:

| Model | Best fit | χ²/dof |
|-------|----------|--------|
| Real CC + ΛCDM (n=3 fixed) | H₀=68.2, Ω_m=0.319 | **0.485** ✅ |
| AI H_obs table (best fit) | n=1.95, not n=3 | AI table not ΛCDM |
| Real ΛCDM at z=8.5 | H = **1129 km/s/Mpc** | — |
| AI H_obs at z=8.5 | H = **420 km/s/Mpc** | — |

[VERIFIED-REAL] Real ΛCDM fits the 32 observed CC points well (χ²/dof = 0.49). The AI-generated H_obs at z=8.5 (420 km/s/Mpc) is **2.7× lower** than standard ΛCDM extrapolation (1129 km/s/Mpc) at the same redshift.

### N3. Implication for prior findings

| Prior finding | Revised status after real-data check |
|---------------|--------------------------------------|
| I. ΔAIC H_MULT vs ΛCDM | [VERIFIED-REAL for z≤2; UNVERIFIED for z>2 rows] |
| E. CPL projection (wₐ discrepancy) | Uses z>2 extrapolations — weaker evidential weight |
| J. H_FLRW convention recovery | Valid for z≤2 rows; high-z rows are extrapolated baseline |
| K. Quadrupole dominance | Structural finding — unaffected by real-data status |
| M. Self-consistency gap | Structural finding — unaffected by real-data status |

> **Key question (N):** "The four high-z rows in Table A1 (z = 2.10, 3.20, 5.00, 8.50) use H_obs values that have no published cosmic chronometer counterpart. What observational source, if any, underlies these H_obs entries? Are they from a specific survey, an AI-generated extrapolation, or a theoretical prediction from MULTING itself?"

---

*All numbers verified from Supplementary PDF or computed from formulas therein.*
*CPL fit, self-consistency diagnostic, and real-data comparison: internal diagnostics only.*
*NOT MCMC, NOT prediction, NOT validation, NOT refutation.*
