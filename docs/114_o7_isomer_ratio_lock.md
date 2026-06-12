# docs/114 — O7 Isomer Ratio Lock

**Date:** 2026-06-13  
**Gate:** O7 — sector count → DM/baryon ratio  
**Supersedes:** O7 open-item entries in docs/108, docs/112  
**Session start protocol:** docs/112 (master) → docs/113 (HD-MAVP-1) → **this file (O7)**

```
SAFETY LABELS (HARD):
  NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_MODEL_FALSIFICATION
  INTERNAL_DIAGNOSTIC_ONLY · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED
  NOT_THEORY_FALSE · NOT_AI_HALLUCINATION_CLAIM · NOT_FABRICATION_CLAIM
  O7_SECTOR_COUNT
```

---

## 1. Verdict

```
O7 status:   REJECTED_AS_DERIVATION / PATTERN_MATCH_ONLY / AUTHOR_EXTENSION_NEEDED

Claim tested:  "5 IDM isomers → Ω_DM/Ω_b ≈ 5"  (strong derivation reading)
Source:        Author text says "might suggest" — conditional, not assertive
Result:        Strong derivation reading is NOT supported by available materials
Author intent: NOT rejected — conditional language is accurate
```

---

## 2. Author Wording (CRITICAL)

The author uses weak / suggestive language — NOT a derivation claim:

| Author text | What it means | What it does NOT mean |
|-------------|---------------|-----------------------|
| "might suggest" | numerological coincidence noted | derivation from first principles |
| "can associate with" | pattern linkage proposed | causal or quantitative derivation |
| "is consistent with" | not contradicted | predicted by IDM |

**FORBIDDEN reading:**  
> "Buckholtz derived Ω_DM/Ω_b from sector count."

**CORRECT reading:**  
> "The author observes that 5 IDM sectors coincides with Ω_DM/Ω_b ≈ 5 and notes this might suggest a connection. No derivation is offered."

---

## 3. What Derivation Requires (Missing Mechanisms)

To convert sector count N_sectors=5 into a cosmological ratio requires the following
physical inputs. None are addressed in currently available IDM materials.

| # | Mechanism | Physical role | IDM status |
|---|-----------|---------------|------------|
| 1 | **Baryogenesis / dark baryogenesis** | Fixes production rates for SM vs dark sectors | MISSING |
| 2 | **Thermal history (T_dark/T_SM)** | Sets number densities at decoupling; N_sectors alone is dimensionless without T_dark | MISSING — M7-C BLOCKED |
| 3 | **Dark sector mass spectrum** | Ω_i ∝ m_i × n_i; need individual masses, not just sector count | MISSING |
| 4 | **Annihilation / freeze-out** | Relic density is set by <σv> at freeze-out, not by N_sectors | MISSING |
| 5 | **Entropy budget** | DM/baryon ratio depends on entropy per sector after reheating | MISSING |

**Formal statement:**
```
Derivation requires:
  Ω_DM/Ω_b = f(N_sectors, T_dark/T_SM, m_dark, <σv>, s_dark/s_SM)

Available from IDM materials:
  N_sectors = 5  (sector count only — one of five arguments)

Gap: the function f and four of five arguments are unspecified.
```

---

## 4. Prior Gate Chain (M7 sub-gates)

| Gate | Verdict | Commit | Propagation to O7 |
|------|---------|--------|-------------------|
| M7-A (5:1 mass-ratio) | PARTIAL | `3b128dd` | Numerical coincidence confirmed; no derivation |
| M7-B (dark isomer counting) | PARTIAL | `e624bd3` | Integer counting insufficient; thermal history absent |
| M7-C (N_eff thermal history) | **BLOCKED** | `9ebd05c` | T_dark, decoupling, N_eff_dark: ALL MISSING |

**M7-C blocker propagates directly to O7:**  
Without T_dark/T_SM, sector count cannot be converted to relic density.  
The M7-C blocker remains active and is NOT lifted by this O7 verdict.

---

## 5. What This Does NOT Mean

```
NOT proven by O7 verdict:
  ✗ Buckholtz made a false or overclaimed derivation (author text: "might suggest")
  ✗ IDM is refuted or internally inconsistent
  ✗ The sector count coincidence is numerologically accidental (unknown)
  ✗ Ω_DM/Ω_b ≈ 5 cannot eventually be derived in IDM
  ✗ Sector counting is impossible in every future dark-sector theory

Correct framing:
  ✓ Available IDM materials do not provide the 5 required mechanisms
  ✓ Sector count alone is insufficient for a cosmological derivation
  ✓ Pattern match (coincidence) ≠ derivation (calculation from physics)
  ✓ A future IDM extension addressing M7-C + mass spectrum + freeze-out
    COULD derive Ω_DM/Ω_b ≈ 5 — O7 verdict = AUTHOR_EXTENSION_NEEDED, not KILL
  ✓ The coincidence is consistent with IDM's framework but not yet predicted by it
```

---

## 6. Mechanistic Insights (O7)

**INSIGHT-7a** [VERIFIED-tool via prior M7 gates, M7-C: `9ebd05c`]:  
M7-C thermal history blocker propagates to O7. Sector counting without T_dark is
dimensionless — it produces a dimensionless ratio only if all sectors have equal mass
and entropy, which requires additional assumptions unavailable in current materials.

**INSIGHT-7b** [INFERRED, chain: baryogenesis → relic density → Ω_DM/Ω_b]:  
Even if N_sectors=5 is correct, the 5:1 ratio depends on baryogenesis asymmetry (η_B)
and dark sector production efficiency, both of which can differ by orders of magnitude
depending on the mechanism. Sector count is compatible with ratios from ~0.01 to ~1000
without further constraints.

**INSIGHT-7c** [INFERRED, from IDM isomer structure]:  
IDM isomers cover quarks, leptons, gauge bosons, Higgs analogs, and gravitational analogs.
The dark mass spectrum for each is unknown. Without masses, Ω_i cannot be computed even
if T_dark/T_SM were known. Two independent unknowns (T_dark, m_dark) enter the derivation
before sector count becomes meaningful.

---

## 7. Decision: REJECTED_AS_DERIVATION

```
REJECT reason:    Missing 5 required physical ingredients
Author intent:    NOT rejected — conditional language is accurate and scientifically appropriate
Future path:      IDM extension addressing M7-C (T_dark) + mass spectrum + freeze-out
                  could revisit; NOT on current critical path; gated behind Q1+Q2 TJB answers

Do NOT retry O7 without:
  - Explicit IDM thermal history (T_dark/T_SM) from author or derived from IDM framework
  - Dark sector mass spectrum for at least 3 of 5 sectors
  - Freeze-out mechanism specified in IDM framework
  - Baryogenesis mechanism for dark sectors

Current blocker: M7-C (active), propagates to O7.
```

---

## 8. Evidence Block

| # | Evidence | Source | Label |
|---|----------|--------|-------|
| E-01 | Author text: "might suggest" / "can associate with" (not "derives") | Available IDM materials | [VERIFIED-tool gate log] |
| E-02 | M7-A verdict PARTIAL: 5:1 numerically close; no derivation | commit `3b128dd` | [VERIFIED-tool] |
| E-03 | M7-B verdict PARTIAL: integer counting insufficient; no thermal history | commit `e624bd3` | [VERIFIED-tool] |
| E-04 | M7-C verdict BLOCKED: T_dark, decoupling, N_eff_dark ALL MISSING | commit `9ebd05c` | [VERIFIED-tool] |
| E-05 | Baryogenesis mechanism: not addressed in available IDM materials | OUR_RECONSTRUCTION audit | [INFERRED] |
| E-06 | Dark sector mass spectrum: not specified in available IDM materials | OUR_RECONSTRUCTION audit | [INFERRED] |
| E-07 | Freeze-out/annihilation: not addressed in available IDM materials | OUR_RECONSTRUCTION audit | [INFERRED] |
| E-08 | Entropy budget: not addressed in available IDM materials | OUR_RECONSTRUCTION audit | [INFERRED] |

---

## 9. State After This Gate

```
ACTIVE GATES:         NONE
O7 STATUS:            CLOSED — REJECTED_AS_DERIVATION
M7-C BLOCKER:         ACTIVE (unchanged — O7 verdict does not lift it)
TJB EMAIL:            SENT 2026-06-12; earliest follow-up 2026-06-18
HD-MAVP-2:            HOLD (requires Q1+Q2; not authorized)
M8-B:                 LOW PRIORITY (Φ-normalization forensic)
BETA-1:               HOLD (controlled AI β replication)
MCMC:                 BLOCKED (0/5 blockers resolved)
SESSION STATE:        WAITING_FOR_TJB
```

---

## 10. Documents Updated This Gate

| File | Role |
|------|------|
| `null_results/20260613-nr007-sector-count-dm-baryon-ratio.md` | NR-007 — decision record |
| `null_results/INDEX.md` | NR-007 row added |
| `docs/112_waiting_for_tjb_master_lock.md` | O7 pointer added |
| **`docs/114_o7_isomer_ratio_lock.md`** | **This file — O7 lock** |

---

*O7_SECTOR_COUNT · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED*  
*NOT_VALIDATION · NOT_REFUTATION · NOT_THEORY_FALSE*  
*docs/114 issued 2026-06-13*
