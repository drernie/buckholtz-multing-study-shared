# NR-005 — Intrinsic Cluster Formation Cannot Be Distinguished from Selection Artifact

**Gate:** HD-MAVP-1  
**Date:** 2026-06-13  
**Verdict:** REJECT (partial — intrinsic PS density alone killed; selection artifact survives)  
**Labels:** HD_MAVP_1 · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · SELECTION_BIAS_AUDIT

---

## Claim Tested

> Intrinsic cluster formation history (PS comoving density without volume or selection)
> can explain the ε(z) peak at z=0.40 observed in Table A1.

---

## Result

**REJECT for Candidate A (PS comoving density alone):**

| M_min | r(ε, n_PS) | Verdict |
|-------|------------|---------|
| 1e14  | +0.076     | INSUFFICIENT |
| 5e14  | −0.100     | INSUFFICIENT |
| 2e15  | −0.253     | INSUFFICIENT |

Intrinsic PS density n(>M, z) is monotone decreasing with z. It cannot peak at z=0.40.
The correlation with ε is INSUFFICIENT for all tested mass thresholds.
Candidate A verdict: **KILLED**.

**SURVIVES_AS_ARTIFACT for selection function:**

r(ε, f_sel_alone) = **0.666** — instrument model with ZERO cluster physics  
reproduces 92% of the M8-C best signal (r=0.723).

| Candidate | r | Verdict |
|-----------|---|---------|
| C (SZ selection × dN/dz) | 0.664–0.683 | PARTIAL |
| f_sel alone (zero physics) | 0.666 | > threshold |

The selection function f_sel(z) = (z/0.40)² × exp(−2(z/0.40 − 1)) peaks at z=0.40
by SZ instrument physics (beam dilution at low z + flux fading at high z). Its correlation
with ε demonstrates that ANY survey-selected quantity can spuriously correlate with ε without
reflecting physical cluster formation.

**Note:** Intrinsic dN/dz (PS × volume element, Candidate B) gives r=0.772 for M_min=1e14,
ABOVE the selection function alone. This means M8-C's r=0.723 could reflect intrinsic dN/dz
at the right mass scale — but the mass scale is undetermined without Q2.

---

## Why the Claim Fails (Partial)

**For Candidate A (pure formation history):** monotone by construction — cannot reproduce
the non-monotone ε structure regardless of M_min. Killed by INSIGHT-3 analog (PS density
is well-understood and decreasing).

**For the broader selection-bias claim:** The r=0.666 from f_sel alone shows that the
M8-C r=0.723 signal is **ambiguous** — it could be:
1. Real intrinsic dN/dz at the right M_min (Candidate B: r=0.773 for M_min=1e14)
2. Selection artifact (f_sel alone: r=0.666)
3. A combination of both

Without Q2 (author's cluster schedule), these cannot be separated.

---

## Mechanistic Insight — INSIGHT-5 (extended)

**INSIGHT-5a** [VERIFIED-tool]: `r(ε, f_sel_alone) = 0.666`  
The SZ survey selection function (zero physics instrument model) produces r=0.666 with ε.  
This means the M8-C correlation of r=0.723 has a **non-physical alternative explanation**:  
it could arise entirely from the coincidence that SZ surveys detect clusters preferentially  
at z≈0.40, the same redshift where ε peaks.

**INSIGHT-5b** [VERIFIED-tool]: Intrinsic dN/dz is M_min-sensitive  
For M_min=1e14: r=0.773 (SURVIVES without selection)  
For M_min=5e14: r=0.699 (PARTIAL without selection)  
For M_min=2e15: r=0.560 (INSUFFICIENT without selection)  
The peak location of intrinsic dN/dz shifts from z=0.65 (M_min=1e14) to z=0.40 (M_min=5e14),  
making the signal M_min-dependent — not a robust prediction.

**INSIGHT-5c** [THEOREM]: ΛCDM dark energy transition cannot explain ε peak  
f_DE(z) = Ω_Λ/(Ω_m(1+z)³+Ω_Λ) is monotone decreasing; r(ε, f_DE) = 0.167 (INSUFFICIENT)  
z_eq (Λ-matter equality) = 0.296, proximity 0.104 to ε peak — suggestive but insufficient.  
The ΛCDM transition epoch is nearby but f_DE has the wrong (monotone) shape.

---

## What This Does NOT Prove

```
This null result does NOT prove:
  ✗ That ε peak at z=0.40 is a selection artifact
  ✗ That M8-C r=0.723 is wrong or meaningless
  ✗ That cluster formation is unrelated to ε
  ✗ That the author's bridge tracks selection rather than physics
  ✗ That any M_min value is the "correct" one

Correct framing:
  ✓ Intrinsic PS density alone CANNOT explain ε peak — r too low for all M_min
  ✓ f_sel alone produces r=0.666 — non-physical alternative exists
  ✓ Signal ambiguity: intrinsic dN/dz (M_min=1e14) and selection function
    give comparable r; cannot distinguish without Q2
  ✓ Candidate D (ΛCDM transition) KILLED — wrong shape
```

---

## What Remains Open

- Q2 (TJB, not before 2026-06-18): Which cluster scale/mass range does the author's
  bridge target? This directly determines which M_min applies, resolving the Candidate B
  vs Candidate C ambiguity.
- Once Q2 answered: test whether author's non-monotone schedule is closer to dN/dz
  (intrinsic) or to dN/dz × f_sel (observed with selection).

---

## Decision: REJECT (partial)

```
Claim "intrinsic PS formation explains ε peak":  REJECTED
Next attempt requires: fundamentally different formation model (not PS),
OR Q2 (author cluster schedule) to constrain M_min.

Alternative survival: selection-artifact hypothesis SURVIVES pending Q2.
```

---

## Files

| File | Role |
|------|------|
| `scripts/hdmavp1_epsilon_cluster_audit.py` | Audit script, 4 candidates |
| `tests/test_hdmavp1_epsilon_cluster_audit.py` | 41 tests, all pass |
| `reports/hdmavp1_epsilon_cluster_audit.json` | Full report, Verdict=PARTIAL-KILL |

---

*HD_MAVP_1 · OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION*  
*NR-005 registered 2026-06-13 · null_results/20260613-intrinsic-formation-selection-ambiguity.md*
