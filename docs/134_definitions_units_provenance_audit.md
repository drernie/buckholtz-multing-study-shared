# docs/134 — Audit 2: Definitions, Units, and Source-of-Truth Provenance

**Date:** 2026-07-23
**Origin:** User-proposed audit #2 ("main risk: prose value ≠ table value ≠ code value ≠
data-derived value" — three real instances of exactly this bug were found and fixed this session:
g*-vs-N_eff units confusion, k_A ~599× supplementary/formula mismatch, ε chain r_A/D≈1
mis-assumption). This audit formalizes the ledger so a fourth instance is caught by inspection,
not by luck.
**Scope:** every quantity that appears in more than one of {prose/supplementary text, Table A1,
this project's code, this project's real MCXC/PSZ2 data} for the MULTING force-law and cosmology
chain, plus the two units bugs found in the microphysics chain (N_eff, g*).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION
**Method:** no new computation — every cell below traces to a specific commit or file already in
this repo; this is consolidation + cross-reference, exactly as the C1 table (docs/133) was, but
with the columns the user specifically asked for (Table value / Code value / Data-derived value /
Consumers) made explicit per quantity.

---

## The ledger

| Quantity | Definition | Units | Source | Table A1 / supplementary value | Code value (this pipeline) | Data-derived value (real MCXC/PSZ2, n=548) | Consumers | Status |
|---|---|---|---|---|---|---|---|---|
| **k_A** | `E_ICM/c²` (TJB-confirmed, 2026-06-14 voice call) | M☉ | facts.json Q005 | `k_A/c²=3.16×10¹²` (Table A1 worked example) | `e_thermal_path_b` (SZ Compton-Y) | median k_A/M=1.7×10⁻⁶ | `src/cluster_data_pipeline.py`, `src/pearson_fit.py`, `paper/main.tex §beta` | 🟡 **MISMATCH FOUND**: supplementary's own stated formula `(3/2)M_Aσ_v²/c²` at `σ_v≈1000 km/s` gives 5.27×10⁹, not 3.16×10¹² — ~599× off ITS OWN formula. Real pipeline uses independent SZ/X-ray data, unaffected. Flagged directly to TJB (letter Q2/Q3, commit af3d5c4). |
| **r_A** | Cluster radius (r₅₀₀) | Mpc | MCXC catalogue | not separately tabulated as illustrative | real per-cluster | real per-cluster | same as k_A | 🟢 **CLEAN** — standard X-ray catalogue quantity, single definition throughout |
| **D(z)** | Inter-cluster (pair) distance | Mpc | paper's own text: "phenomenological hypothesis, not a derivation" (main.tex line ~488) | not specified by TJB anywhere found | `D₀/(1+z)`, `D₀=100 Mpc` (audit's own convention) | n/a — not a catalogue quantity | `src/pearson_fit.py phi()` | 🔴 **NEVER DEFINED BY AUTHOR** — our D₀=100 Mpc is our own choice; letter Q4 asks directly what D represents (physical/comoving/nearest-neighbour/averaged) |
| **β_d, β_q** | Dipole/quadrupole coupling coefficients | dimensionless | Table A1 + 3 independent AI-service extractions | Claude/Table A1: 4.5/18.0; Gemini: 4.25/8.10; ChatGPT: 0.78/0.19 | tested across the full continuous range (R011 v3-v6) | non-identifiable from data alone (Q004 HOLD) | `phi()` formula | 🔴 **NON-IDENTIFIABLE** — BRAI Birge Ratio R_B=15.9 (β_d) / 24.1 (β_q), p<10⁻⁴; the three source-attributed values are NOT consistent measurements of the same thing |
| **F_d/F_m (ε)** | Dipole/monopole force ratio | dimensionless | paper §beta illustrative example | **was** ε≈6×10⁻⁶ at β_d=4.5 (WRONG, see status) | ε formula: `βd·(k_A/M)·(r_A/D)` | median ε≈1.6×10⁻⁷ at β_d=4.5, real pipeline | `paper/main.tex §beta`, `scripts/t4_monopole_dominance.py` | 🟢 **FIXED this session** (commit c125179, T11): the illustrative 6×10⁻⁶ implicitly assumed r_A/D≈1 (cluster radius ≈ inter-cluster DISTANCE — physically impossible); real value ~30-65× smaller; corrected in paper |
| **H_MULT(z)** | `H_anchor·√(φ(z)/φ(z_ref))` | km/s/Mpc | paper's own text: "phenomenological formula... not a derivation" | AI-generated per-point curve (July-20 chart) | same formula, our own D(z)/β convention | R011: underperforms trivial `(1+z)²` baseline AND monopole-only at every β tested | `src/pearson_fit.py` | 🔴 **NOT A DERIVED FORMULA** — no action/Lagrangian exists (Q006); the published red curve's actual generating equation is unknown to us (letter Q1) |
| **N_eff (dark sector)** | Effective number of relativistic species, ΔN_eff units | dimensionless | paper's own earlier draft text (pre-58307b7) | `ΔN_eff=106.8` for full mirror SM | **BUG**: 106.8 was `g_eff` (=106.75) quoted directly AS ΔN_eff, not converted | correct: `ΔN_eff=g_*/[(7/8)·2]≈61` at T_dark=T_ν | `paper/main.tex §Neff` | 🟢 **FIXED this session** (commit 58307b7): g* is a degrees-of-freedom count, not the same object as ΔN_eff — conflating them overstated the exclusion factor (was ~380, now correctly ~215) |
| **g\*** | Effective relativistic degrees of freedom | dimensionless | standard SM thermal-history quantity | g_eff=106.75 (full mirror SM, correct value) | now correctly kept separate from ΔN_eff in code/paper | n/a (theoretical DOF count, not data-derived) | `paper/main.tex §Neff` | 🟢 **FIXED this session** — see N_eff row; the two quantities are now consistently distinguished |
| **Ωm (this session's H(z) work)** | Matter density parameter | dimensionless | Planck 2018 (0.3153) vs this audit's fiducial (0.317) | n/a — not TJB's quantity | `OM_FID=0.317` fixed for BOTH solid anchor curves (was NOT stated on the figure until this session's chart fix) | free-fit to real CC data: 0.317±0.042 | `scripts/plot_same_anchor_comparison_tjb.py` | 🟢 **FIXED this session** (commit af3d5c4): now explicitly labeled equal for both curves on the figure itself, not just implicit in the code |

---

## Additional provenance checks run (per the user's checklist)

- **SI ↔ astrophysical units:** checked for k_A (M☉ vs kg/c² — consistent throughout the real
  pipeline; the ~599× mismatch is NOT a unit-conversion error, it's a formula/value mismatch
  within the same M☉ units — confirmed by direct substitution, not a units slip).
- **Energy ↔ mass-equivalent (E/c²):** k_A is consistently defined as E/c² everywhere in our own
  pipeline; the open question is which E (thermal ICM vs kinetic (3/2)Mσ²), not the /c² step.
- **Physical ↔ comoving lengths:** D(z)'s ambiguity (physical/comoving/nearest-neighbour/averaged)
  is exactly this class of risk — flagged 🔴 above, directly asked (letter Q4).
- **H ↔ D_H/r_d:** already correctly handled in the DESI-related work (scripts/
  hz_desi_and_redcurve_space.py, docs/132 T7) — D_H/r_d is the actual DESI observable, H(z) in
  km/s/Mpc requires an r_d choice, made explicit there and in the letter's lower-priority
  questions.
- **Local pair-value ↔ cosmologically-averaged value:** this is precisely docs/133's split of
  F_d/F_m into formula/pair-conditional/cosmological-effective rows (the fix requested and
  applied 2026-07-22) — carried over into this ledger's F_d/F_m row.
- **Illustrative value ↔ real observed value:** the exact shape of all three bugs found this
  session (k_A, ε, N_eff) — this is the audit's own headline finding, stated below.

---

## Verdict

**PASS** for r_A (single clean definition, no discrepancy found).
**FAIL→FIXED this session** for F_d/F_m, N_eff, g* (real prose/code/table mismatches found and
corrected, commits c125179 and 58307b7).
**OPEN/MISMATCH-FLAGGED** for k_A (real mismatch found — supplementary's own formula doesn't
reproduce supplementary's own tabulated number — flagged to TJB, not yet resolved).
**NEEDS_DATA** for D(z), β_d, β_q, H_MULT(z) — no author-confirmed single definition exists for
any of these; this audit cannot manufacture one, only state precisely what is missing (this is
the same conclusion Audit 1/docs/133 reaches from the closure-chain side).

**Headline finding, stated precisely (revised 2026-07-23 — "hit rate" framing retracted):** in a
small set of the nine most safety-critical quantities in this chain, three independent, verified
prose/code/table discrepancies were found this session (k_A, ε, N_eff/g*). These nine rows were
**not a random sample** of every numeric quantity in the project, so a percentage is not a valid
frequency estimate — do not read this as "33% of all project numbers are wrong." What it does
establish: this is enough evidence to treat provenance defects (prose ≠ table ≠ code ≠
data-derived value) as a systemic risk class, and to check every future numeric claim in this
project — ours or TJB's own — through this ledger's method (definition → units → source → code
path → recomputation) before treating it as established, not assumed clean by default.

---

*Consolidation only. Every fact above traces to a session commit already made
(af3d5c4, c125179, 58307b7, and the docs/133 chain back to 4196f9a) or to facts.json. No new
computation performed for this document.*
