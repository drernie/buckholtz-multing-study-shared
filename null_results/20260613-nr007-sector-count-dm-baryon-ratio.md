# NR-007 — Sector Count Alone Does Not Derive Ω_DM/Ω_b ≈ 5

**Gate:** O7 — sector count → DM/baryon ratio  
**Date:** 2026-06-13  
**Verdict:** REJECTED_AS_DERIVATION / PATTERN_MATCH_ONLY  
**Labels:** O7_SECTOR_COUNT · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED  
           NOT_VALIDATION · NOT_REFUTATION · NOT_THEORY_FALSE

---

## Claim Tested

> The presence of 5 IDM dark-sector isomers (dark analogs to quarks, leptons,
> bosons, etc.) is sufficient to derive the cosmological DM-to-baryon density ratio
> Ω_DM/Ω_b ≈ 5 observed by Planck.

---

## Author Wording (verbatim, from available materials)

The author uses conditional / suggestive language, NOT a derivation claim:

- "might suggest" — not "derives"
- "can associate with" — not "equals"
- "is consistent with" — not "predicts from first principles"

**This is important:** the author did NOT claim a derivation in the available
text. The strong reading "5 isomers → Ω_DM/Ω_b=5" is an *external interpretation*
of the author's weaker statement. NR-007 rejects the strong reading, not the
author's actual framing.

---

## Result: REJECTED_AS_DERIVATION

Sector count is a necessary ingredient of any IDM-based cosmological ratio, but
it is **far from sufficient**. The following mechanisms are required to convert
"there are 5 dark sectors" into "Ω_DM/Ω_b ≈ 5" — and none are addressed in
currently available materials.

### Five Required Missing Mechanisms

| # | Mechanism | Why required | Status in available IDM materials |
|---|-----------|--------------|-----------------------------------|
| 1 | **Baryogenesis / dark baryogenesis** | Need equal or related production rates for SM and dark sectors; without this, sector count doesn't fix abundance ratio | MISSING |
| 2 | **Thermal history** | Dark-sector temperature T_dark/T_SM at decoupling sets number density; without T_dark, sector multiplicity is dimensionless | MISSING (M7-C BLOCKED) |
| 3 | **Dark sector mass spectrum** | Individual dark-sector particle masses determine relic densities; Ω_i ∝ m_i × n_i, not just sector count | MISSING |
| 4 | **Annihilation / freeze-out** | Dark sector relic abundance depends on annihilation cross-sections at freeze-out, not on sector multiplicity alone | MISSING |
| 5 | **Entropy budget** | DM/baryon ratio depends on relative entropy in each sector after reheating; entropy dilution can offset sector counting | MISSING |

### Pattern match vs derivation

```
Pattern match (available):
  "IDM has 5 dark sectors; Ω_DM/Ω_b ≈ 5; these numbers are the same."

What a derivation requires:
  Ω_DM/Ω_b = f(N_sectors, T_dark/T_SM, m_dark, <σv>, s_dark/s_SM)

The function f is not provided in currently available IDM materials.
Sector count N_sectors = 5 enters f as one of five arguments — it is
necessary but not sufficient.
```

---

## Connection to Prior Gates

| Gate | Verdict | Connection to O7 |
|------|---------|-----------------|
| M7-A (5:1 mass-ratio) | PARTIAL, `3b128dd` | Numerically close (5:1); no physical derivation |
| M7-B (dark isomer counting) | PARTIAL, `e624bd3` | Integer counting insufficient; thermal history absent |
| M7-C (N_eff thermal history) | BLOCKED, `9ebd05c` | T_dark, decoupling, relativistic species: all MISSING |

M7-C thermal-history blocker directly blocks O7: without T_dark/T_SM,
the sector count cannot be converted into a relic density.

**M7-C blocker remains active and propagates into O7.**

---

## What This Does NOT Prove

```
This null result does NOT prove:
  ✗ That Buckholtz made a false or overclaimed derivation
     (author text says "might suggest" — conditional, not assertive)
  ✗ That IDM is refuted or inconsistent
  ✗ That sector count is impossible in every future theory
  ✗ That Ω_DM/Ω_b ≈ 5 cannot eventually be derived in IDM
  ✗ That the coincidence N_sectors = Ω_DM/Ω_b is accidental (unknown)

Correct framing:
  ✓ Current available materials do not provide the 5 required mechanisms
  ✓ Sector count alone is insufficient for a cosmological derivation
  ✓ A future IDM extension that addresses mechanisms 1–5 could, in principle,
    derive Ω_DM/Ω_b ≈ 5 — this is an AUTHOR_EXTENSION_NEEDED verdict, not a kill
  ✓ The coincidence is consistent with IDM's framework but not yet predicted by it
```

---

## Decision: REJECT (derivation claim)

```
Claim "5 isomers derive Ω_DM/Ω_b≈5":  REJECTED_AS_DERIVATION

Mechanism: missing 5 required physical ingredients (baryogenesis, thermal
history, mass spectrum, annihilation/freeze-out, entropy budget).

Author intent: NOT rejected — author's conditional language ("might suggest")
is accurate. The strong derivation reading is external.

Future path: IDM extension addressing M7-C (thermal history) + mass spectrum
+ freeze-out could revisit this. Not on current critical path.

Do NOT retry without:
  - Explicit IDM thermal history (T_dark/T_SM) from author or derivation
  - Dark sector mass spectrum
  - Freeze-out mechanism in IDM framework
```

---

*O7_SECTOR_COUNT · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED*  
*NOT_VALIDATION · NOT_REFUTATION · NOT_THEORY_FALSE*  
*NR-007 registered 2026-06-13*
