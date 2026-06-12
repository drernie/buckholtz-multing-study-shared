# M8-A-R1 — Bridge Derivation Adversarial Re-Audit

**Date:** 2026-06-12  
**Method:** Context-blind falsification (FL adversarial protocol)  
**Input:** Table A1 data + bridge derivation claims only — no session history  
**Verdict:** PARTIAL → PASS (after 4 corrections)

```
Labels: OUR_RECONSTRUCTION · INTERNAL_DIAGNOSTIC_ONLY
        NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_CONFIRMED
```

---

## Re-Audit Checks

### Check 1 — Data provenance

- H_MULT > H_FLRW in ALL 11 rows [verified by independent arithmetic]
- z=0 absent — this is a hole, but ε(0) would approach 0 physically, so diagnostic is not invalidated
- No evidence of hidden normalization in raw H(z) values (km/s/Mpc units consistent throughout)

**Result: PASS**

---

### Check 2 — ε(z) independent recomputation

Independent arithmetic (ε = (H_MULT/H_FLRW)² − 1):

| z | H_FLRW | H_MULT | ε (independent) | ε (claimed) | Match? |
|---|--------|--------|-----------------|-------------|--------|
| 0.06 | 68.1 | 70.2 | 0.06262 | 0.0626 | ✓ |
| 0.14 | 69.3 | 73.5 | 0.12489 | 0.1249 | ✓ |
| 0.25 | 71.5 | 78.8 | 0.21462 | 0.2146 | ✓ |
| 0.40 | 75.0 | 83.1 | 0.22766 | 0.2277 | ✓ |
| 0.65 | 83.0 | 91.4 | 0.21265 | 0.2127 | ✓ |
| 1.00 | 95.7 | 104.2 | 0.18553 | 0.1855 | ✓ |
| 1.50 | 114.8 | 126.5 | 0.21423 | 0.2142 | ✓ |
| 2.10 | 140.3 | 151.8 | 0.17064 | 0.1707 | ✓ |
| 3.20 | 187.6 | 197.3 | 0.10610 | 0.1061 | ✓ |
| 5.00 | 265.2 | 271.5 | 0.04810 | 0.0481 | ✓ |
| 8.50 | 398.5 | 418.1 | 0.10078 | 0.1008 | ✓ |

**All 11 ε values verified. Claimed peak (z=0.40, ε=0.2277) and min (z=5.0, ε=0.0481) confirmed.**

**Result: PASS**

---

### Check 3 — Non-monotonicity

Sign of change in ε between consecutive z points:

```
z=0.06→0.14: +0.062 (↑)
z=0.14→0.25: +0.090 (↑)
z=0.25→0.40: +0.013 (↑) ← global peak
z=0.40→0.65: −0.015 (↓) ← first descent
z=0.65→1.00: −0.027 (↓)
z=1.00→1.50: +0.029 (↑) ← SECONDARY STRUCTURE (not mentioned in M8-A)
z=1.50→2.10: −0.044 (↓)
z=2.10→3.20: −0.065 (↓)
z=3.20→5.00: −0.058 (↓) ← global minimum
z=5.00→8.50: +0.053 (↑) ← uptick (SINGLE POINT)
```

**Non-monotonicity confirmed. However: M8-A Claim 1 ("peaks at 0.40, min at 5.0") understates the complexity.**  
Structure is: RISE→PEAK(0.40)→FALL→LOCAL_MIN(1.00)→RISE(1.50)→FALL→GLOBAL_MIN(5.00)→UPTICK(8.50)

**Correction applied (see Section below).**

---

### Check 4 — Constant-ε candidate

mean(ε) = 1.66782/11 = 0.15162  
max|ε − mean| = max(0.076 at z=0.40, 0.104 at z=5.0) = **0.104**  
Threshold 0.05 is heuristic (not derived from data). But max_residual=0.104 is **2.1× the threshold** — verdict is robust even if threshold changed to 0.08.

**Result: CONFIRMED FAIL**

---

### Check 5 — Power-law α range

Independent pairwise α = ln(ε_{i+1}/ε_i) / ln((1+z_{i+1})/(1+z_i)):

| z-pair | α |
|--------|---|
| 0.06→0.14 | +9.49 ← leverage (endpoint) |
| 0.14→0.25 | +5.88 |
| 0.25→0.40 | +0.52 |
| 0.40→0.65 | −0.42 ← sign change |
| 0.65→1.00 | −0.71 |
| 1.00→1.50 | +0.64 ← sign change |
| 1.50→2.10 | −1.06 |
| 2.10→3.20 | −1.57 |
| 3.20→5.00 | −2.22 ← leverage (endpoint) |
| 5.00→8.50 | +1.61 ← sign change |

Range [−2.22, +9.49] confirmed. Sign changes at z=0.40, z=1.00, z=5.00.  
**Note:** Both extremes (α=+9.49 and α=−2.22) sit on endpoint z-pairs — single-point leverage. Remove z=0.06 → α_max falls to +5.88. Core claim (no single α) survives.

**Result: CONFIRMED FAIL**

---

### Check 6 — Press-Schechter interpretation

Original wording in `analyze_nonmonotonicity()` output:  
> "ε(z) peaks at z≈0.40 — consistent with galaxy cluster number density peak (Press-Schechter: n_cluster peaks at z~0.4-0.6)"

This is a **descriptive observation** (peak location coincides numerically) presented with language that implies physical causation. Per EstimandOps: descriptive result → NEVER interpret causally without DAG + identifiability.

**Verdict: OVERCLAIM (causal language without causal evidence)**  
**Correction: mark as `<HYPOTHESIS>` + "numerical coincidence, no DAG, descriptive only"**

---

### Check 7 — Docstring "VERIFIED from Table A1"

Original: `"Key finding (VERIFIED from Table A1):"`  
Problem: H_MULT values are outputs of an AI service reconstructed from the preprint, NOT independently measured observational data. "VERIFIED" implies tool-confirmed physical truth. The correct label is TRANSCRIBED (data copied correctly from Table A1) + arithmetic verified (ε formula applied correctly).

**Verdict: TERMINOLOGY OVERCLAIM**  
**Correction: "[TRANSCRIBED from Table A1, arithmetic verified]"**

---

### Check 8 — Statistical robustness

**Robustness to removing z=8.50:**  
Peak (z=0.40) and global minimum (z=5.00) survive. Non-monotonicity still present (secondary structure at z=1.0–1.5).  
→ Claims 1–3 are robust to endpoint removal.

**Robustness to removing z=0.06:**  
α_max falls from +9.49 to +5.88. Range still [−2.22, +5.88]. Sign changes persist.  
→ Claim 3 is robust (verdict FAILS survives).

**One-point leverage risks:**  
- Uptick at z=8.50: one data point. Should not be cited as "confirmed uptick" — mark as single-point observation.
- α_max=+9.49 is leverage-sensitive (comes from z=0.06→0.14 pair alone).

---

## Corrections Applied (M8-A-R1 → post-corrections M8-A script)

| # | Type | Original | Correction |
|---|------|----------|------------|
| 1 | Terminology | `"VERIFIED from Table A1"` in docstring | `"[TRANSCRIBED from Table A1, arithmetic verified]"` |
| 2 | Incompleteness | Claim 1 omits secondary structure at z=1.0–1.5 | Added secondary structure + single-point leverage note for z=8.5 |
| 3 | Overclaim | Press-Schechter as fact | Marked `<HYPOTHESIS>` + "numerical coincidence, no DAG, descriptive only" |
| 4 | Threshold origin | 0.05 threshold unmarked | Added comment: heuristic; max_residual=0.104 is 2.1× threshold → verdict robust |

---

## Final Verdict

```
VERDICT: PASS (after corrections)

CONFIRMED_CLAIMS:
  ✓ ε(z) arithmetic — all 11 values independently verified
  ✓ Non-monotonicity — multiple sign changes confirmed
  ✓ Peak z=0.40 (ε=0.2277), minimum z=5.0 (ε=0.0481)
  ✓ Constant-ε bridge FAILS — max residual 0.104 >> 0.05 (robust to threshold)
  ✓ Power-law bridge FAILS — α sign changes at 3 z-values

CORRECTED_CLAIMS:
  ~ Claim 1 now includes: secondary structure z=1.0–1.5, uptick z=8.5 = single-point leverage
  ~ Press-Schechter: now <HYPOTHESIS> not stated fact
  ~ Docstring: VERIFIED → TRANSCRIBED

FALSIFIED_CLAIMS:
  ✗ None — no numerical or logical error found

RISKS (remaining):
  - 11 points over sparse z: structure between points unobserved
  - z=0 absent: ε behavior at very low z unknown
  - H_MULT provenance = AI service output, not observational; Table A1 itself is OUR_RECONSTRUCTION

NEXT GATE:
  M8-C — Closure Schedule / Cluster Formation Bridge
  Goal: test whether n_cluster(z) or similar cluster-evolution model
  can generate non-monotonic ε(z) with primary peak near z≈0.40
```

---

*OUR_RECONSTRUCTION · INTERNAL_DIAGNOSTIC_ONLY · NOT_VALIDATION · NOT_REFUTATION*
