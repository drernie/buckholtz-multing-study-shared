# M7-C Thermal History / N_eff Blocker

**Gate:** M7-C  
**Date:** 2026-06-12  
**Upstream:** K0 PASS · M2-G4 PASS · M7-A PARTIAL · M7-B PARTIAL · EC-1 PASS · VS-1 PARTIAL · AB-2 PASS

---

## 1. Status Labels

```
M7_THERMAL_HISTORY_AUDIT
N_EFF_BLOCKER
NOT_VALIDATION
NOT_REFUTATION
INTERNAL_DIAGNOSTIC_ONLY
AUTHOR_DERIVATION_NEEDED
```

---

## 2. Claim / Context

**Audit question:**  
Do the five dark isomers of IDM have enough specified thermal history to compute ΔN_eff and compare to BBN/CMB constraints?

**Context from M7-B:** The 5:1 dark-to-ordinary isomer ratio gives approximate post-hoc integer-counting match to Planck ρ_DM/ρ_OM, but thermal history was identified as absent. This gate probes whether that absence blocks the N_eff / BBN test independently.

**Known from A5 in docs/100:** External tests (BBN, PPN, Bullet Cluster) are listed as `[MCMC_BLOCKED]` pending SC-2 + A0 resolution. This gate asks a narrower question: even if SC-2 + A0 were resolved, could we compute ΔN_eff? Answer: NO — because the thermal history inputs are simply absent from the preprint.

---

## 3. Required Physics Ingredients

Standard formula (EXTERNAL_STANDARD_PHYSICS):

```
ΔN_eff = (4/7) × (g_D / 2) × (T_dark / T_ν)^4
```

- `g_D` = effective dark bosonic degrees of freedom at BBN/recombination  
- `T_dark / T_ν` = dark sector temperature relative to SM neutrino temperature  
- Planck 2018 bound: N_eff = 2.99 ± 0.17 (1σ); ΔN_eff > 0.4 excluded at 1σ

To apply this formula to IDM, the following ingredients are required:

| ID | Ingredient | Status | Note |
|---|---|---|---|
| I1 | Number of relativistic dark species at BBN/recombination | **NOT_FOUND** | AUTHOR_DERIVATION_NEEDED |
| I2 | Dark-to-visible temperature ratio T_dark/T_visible | **NOT_FOUND** | AUTHOR_DERIVATION_NEEDED |
| I3 | Decoupling temperature of dark sector from SM bath | **NOT_FOUND** | AUTHOR_DERIVATION_NEEDED |
| I4 | Entropy-transfer history between dark and visible sector | **NOT_FOUND** | AUTHOR_DERIVATION_NEEDED |
| I5 | Whether dark photons/gluons/neutrinos exist and are relativistic at BBN | **AUTHOR_HINTED** | existence implied (preprint line 1063-1065), thermal properties absent |
| I6 | Coupling/thermalization assumptions between dark and SM sectors | **NOT_FOUND** | AUTHOR_DERIVATION_NEEDED |
| I7 | Explicit IDM calculation or bound for ΔN_eff | **NOT_FOUND** | NO_FORMULA_IN_SOURCE |
| I8 | Standard ΔN_eff formula | EXTERNAL_STANDARD_PHYSICS | cannot apply without I1-I6 |

**Summary:** 6/7 required ingredients NOT_FOUND. 1/7 AUTHOR_HINTED (dark particle existence implied but no masses, temperatures, or relict densities given).

---

## 4. Source Evidence Table

| Search term | Preprint hits | Supplementary hits | Classification |
|---|---|---|---|
| N_eff / Neff (cosmological) | 0 — all "ineffect" false positives | 0 | NOT_FOUND |
| BBN / Big Bang Nucleosynthesis | 0 | 0 | NOT_FOUND |
| thermal history | 0 | 0 | NOT_FOUND |
| T_dark / dark temperature | 0 | 0 | NOT_FOUND |
| dark sector / dark radiation | 0 | 0 | NOT_FOUND |
| dark photon / dark neutrino | 0 | 0 | NOT_FOUND |
| entropy transfer | 0 | 0 | NOT_FOUND |
| decoupling | line 2568 (bibliography only) | 0 | NOT_FOUND (bibliography) |
| thermal | lines 673, 697 (cluster virial energy) | lines 550, 1114 (cluster σ_v) | NOT_FOUND for dark sector |
| CMB | line 1846 (Hubble Tension, FLRW ref) | line 182, 1456 (FLRW/chronometers) | NOT_FOUND for BBN context |
| five dark (isomers) | line 1063-1065: "might associate with SM counterparts" | 0 | AUTHOR_HINTED (I5) |

**Key preprint text (I5 — only relevant hit):**  
Line 1063-1065: *"Each one of the five dark-matter isomers might associate with a set of elementary particles for which there is one elementary-particle counterpart for each known (or ordinary-matter) elementary particle."*

This implies dark photons, dark leptons, dark gluons may exist — but provides:
- No mass spectrum for dark particles
- No thermal population statement
- No production mechanism
- No coupling to SM bath
- No decoupling or freeze-out temperature

---

## 5. Computability Verdict

**ΔN_eff computable from IDM preprint:** NO

| Parameter needed | Available in IDM? |
|---|---|
| g_D (dark d.o.f.) | ✗ NOT FOUND |
| T_dark / T_ν | ✗ NOT FOUND |
| Decoupling T | ✗ NOT FOUND |
| Which dark particles relativistic at BBN | ✗ NOT FOUND (only hinted) |

**Symbolic bound (using external physics + hypothetical full dark SM mirror):**

If IDM dark sector is a full SM mirror (implied by I5) AND decoupled at T ≫ QCD scale:

```
g_D_eff ≈ g_SM_eff / (g_SM at decoupling)^(4/3) × g_SM_eff
```

For a full SM mirror with 106.75 SM d.o.f. at decoupling near T_EW~100 GeV:

```
T_dark / T_ν ≈ (43/4 × 1/g_SM_at_decoup)^(1/3)  → very small
→ ΔN_eff  → 0  (if decoupled early enough)
```

But this is a hypothetical calculation — IDM specifies none of these inputs. The number could range from 0 to ~40 depending on assumptions. **This calculation is BLOCKED without author input.**

---

## 6. What Can / Cannot Be Tested Now

| Test | Status | Reason |
|---|---|---|
| ΔN_eff calculation | BLOCKED | Thermal history absent |
| BBN light element yields | BLOCKED | Dark particle relict densities unknown |
| CMB N_eff constraint | BLOCKED | T_dark unknown |
| Bullet Cluster (DM cross-section) | BLOCKED (also by SC-2) | Bridge gap + thermal history |
| PPN orbital constraints | BLOCKED (also by SC-2) | Bridge gap |
| 5:1 isomer integer-counting | PARTIAL (M7-B) | Mass derivation unresolved |

---

## 7. Questions Unlocked for TJB

*(To add to Q1-Q3 in docs/104 if Q1-Q3 are answered satisfactorily — do NOT send now)*

| Q_ID | Question | Depends on |
|---|---|---|
| Q_TH1 | Were the five dark isomers ever thermally populated in the early universe? | Author intent |
| Q_TH2 | What is T_dark/T_visible for each dark sector? | Production mechanism |
| Q_TH3 | At what temperature did the dark sector decouple from the SM bath? | Coupling constant |
| Q_TH4 | Which dark-sector particles are relativistic at BBN (T~MeV) and at recombination (T~eV)? | Mass spectrum |
| Q_TH5 | What ΔN_eff does IDM predict, and how does it compare to Planck 2018 (ΔN_eff < 0.4 at 1σ)? | All of above |

**Priority:** Q_TH1-Q_TH5 are lower priority than Q1-Q3 in docs/104. Q1-Q3 must be answered before thermal history becomes actionable.

---

## 8. Overclaim Guard

| Forbidden claim | Why forbidden |
|---|---|
| "IDM violates BBN" | We have no IDM thermal history to compute. Cannot falsify what isn't specified. |
| "N_eff constraint rules out IDM" | Same — no IDM ΔN_eff is given to compare against Planck. |
| "IDM predicts ΔN_eff = X" | IDM makes no such prediction. Invented would be OUR_RECONSTRUCTION. |
| "Five dark sectors add ΔN_eff ~ 5×SM" | False — depends on decoupling T, T_dark/T_ν; could be ~0 if decoupled early. |

**Scope:** This audit is INTERNAL_DIAGNOSTIC_ONLY. No claims about IDM validity are made. Thermal history absence is a completeness observation, not a refutation.

---

## 9. Verdict: **BLOCKED**

Thermal history is not specified in the preprint. The IDM framework:
- DOES imply dark particles may exist (I5: AUTHOR_HINTED)
- DOES NOT specify T_dark, decoupling temperature, coupling to SM, or ΔN_eff
- DOES NOT calculate or bound N_eff

**This is a separate blocker from SC-2 / bridge (A0).** Even if the bridge formula were known, ΔN_eff could not be computed without thermal history inputs. The two blockers are independent.

```
VERDICT: BLOCKED
Reason:  6/7 required thermal ingredients NOT_FOUND in IDM preprint.
         ΔN_eff computation requires AUTHOR_DERIVATION_NEEDED.
         Standard physics formula I8 cannot be applied without IDM inputs I1-I6.
```

---

## 10. Next Recommended Gate

1. **User review of docs/104** (Q1-Q3 author email) — primary blocker. Thermal history questions (Q_TH1-5) are secondary.
2. **TJB response to Q1-Q3** → if bridge + cluster params resolved → M7-D or F1/F2 gates
3. **Thermal history questions (Q_TH1-5)** → only useful AFTER bridge resolved; may be added to follow-up email

---

*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY · N_EFF_BLOCKER*  
*M7-C gate closed 2026-06-12*
