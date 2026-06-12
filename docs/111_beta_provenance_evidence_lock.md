# docs/111 — BETA-0 β Provenance Evidence Lock

**Date:** 2026-06-13  
**Gate:** BETA-0 — consolidate β_d / β_q provenance evidence, no new AI models  
**Replaces:** scattered β references across docs/01, 14, 15, 16 + M2-G4 handoff  
**Status:** WAITING_FOR_TJB (Q3 open)

```
SAFETY LABELS (HARD):
  BETA_PROVENANCE_AUDIT · NOT_AUTHOR_CONFIRMED · PHENOMENOLOGICAL_PARAMETER
  AI_MEDIATED_CANDIDATE · NOT_VALIDATION · NOT_REFUTATION
  INTERNAL_DIAGNOSTIC_ONLY · OUR_RECONSTRUCTION
  NOT_FABRICATION_CLAIM · NOT_THEORY_FALSE
```

---

## 1. β Candidate Table by Source

| Source | β_d value | β_q value | Provenance status | Notes |
|--------|-----------|-----------|-------------------|-------|
| Claude (NotebookLM analysis) | **4.5** | **18.0** | `AI_MEDIATED_CANDIDATE` | Reported from manuscript Appendix/Table A1 via NotebookLM; not directly read from printed text |
| Gemini (audit reconstruction) | **≈4.25** | **≈8.10** | `AI_MEDIATED_CANDIDATE` | Reconstructed in parallel session; source method unknown |
| ChatGPT (audit reconstruction) | **≈0.78** | **≈0.19** | `AI_MEDIATED_CANDIDATE` | Reconstructed in parallel session; may use different normalization |
| TJB (partial Q3 response) | *not given* | *not given* | `AUTHOR_PARTIAL` | "phenomenological computation… remains to be determined" |
| First-principles derivation | — | — | `NOT_FOUND` | No derivation from IDM/MULTING internal structure found |

**Value spread:**
- β_d: 0.78 → 4.5 — factor **5.8×**
- β_q: 0.19 → 18.0 — factor **95×**

No two AI sources agree. No source is author-confirmed.

---

## 2. Current Classification

```
β_d and β_q are NOT established as physical constants.

Current status:
  AI_MEDIATED_CANDIDATE — reported by 3 AI services with divergent values
  PHENOMENOLOGICAL_PARAMETER — TJB partial confirmation (Q3)
  NOT_AUTHOR_CONFIRMED — no definitive author statement on values or derivation

Use permission: DO_NOT_USE_FOR_MODELING
Modeling remains BLOCKED until Q3 resolved and values confirmed.
```

---

## 3. Evidence Supporting This Classification

### 3a. Divergent AI Values

Three independent AI services produced mutually inconsistent β values.  
The factor spread (β_d: 5.8×, β_q: 95×) is far outside any plausible unit-conversion
or normalization difference for a single well-defined physical quantity.

**Implication [INFERRED]:** Either (a) the AI services inferred different fitting
conventions, or (b) β is under-constrained and each service selected a different
local minimum. Neither interpretation supports treating any single AI value as the
author's canonical β.

**Evidence marker:** `[VERIFIED-tool]` — values extracted from multi-AI comparison
CSVs (docs/73, data/multi_ai_comparison/).

### 3b. TJB Partial Q3 Confirmation (Author's Own Words)

Source: docs/71_author_response_analysis.md, line 160. Author email response, 2026-05-30.

> *"About connections between F_oP and H_MULT(z), please note that computing F_oP requires estimating beta_d and beta_q. Thus, there is (already) an aspect of 'phenomenological computation.' It is possible that, eventually, people will determine that (at least) beta_d is a 'fundamental physics constant' that applies for much more than interactions between neighboring, non-colliding galaxy clusters; but, such 'remains to be determined.'"*

**What this confirms:**
- β_d and β_q are currently phenomenological / computational estimates
- Author acknowledges uncertainty about their fundamental status
- Author did NOT provide numerical values or a derivation in this response

**What this does NOT confirm:**
- Numerical values of β_d or β_q
- Whether existing AI-reported values (4.5, 18.0, 4.25, 8.10, 0.78, 0.19) are correct
- Whether β can or cannot eventually be derived from first principles

**Evidence marker:** `[VERIFIED]` — direct quote from author email, referenced in docs/71.

### 3c. M2-G4: Fisher Rank Non-Identifiability (commit 91ea667)

Under the reconstructed Claude Φ-normalization bridge
(`H²(z) = H²_anchor · Φ(z)/Φ(z_anchor)`, OUR_RECONSTRUCTION):

| Parameter scenario | Practical rank | Key finding |
|--------------------|----------------|-------------|
| θ = [β_d, β_q] | rank 1 (not 2) | β_q|α_D cosine 0.861 — collinear |
| θ = [β_d, β_q, H_anchor] | rank 1 | Only H_anchor has power |
| θ = [β_d, β_q, H_anchor, α_D] | rank 2 | α_D + H_anchor live; β dead |

Max relative sensitivity: β_d → **7×10⁻¹⁰**; β_q → **7×10⁻⁷** (both effectively zero).

**Key finding:** Under the reconstructed bridge, the objective function is flat to ~10⁻⁷
with respect to both β_d and β_q. The β-pair is **practically non-identifiable** —
any fitted β value is unconstrained by the stated fit procedure.

**Caveat:** M2-G4 used OUR_RECONSTRUCTION of the bridge, not the author's actual bridge.
The non-identifiability may change when Q1 is resolved.

**Evidence marker:** `[VERIFIED-tool]` — Fisher/SVD/Jacobian analysis, 4/4 tests pass,
commit 91ea667.

### 3d. ASRE: k_A / D_eff Schedule Degeneracy (commit 507ead9)

ASRE gate established that k_A(z) and D_eff(z) cannot be separately determined from
Table A1 alone without the author's Q1 bridge formula. Since β_d and β_q appear inside
the bridge as normalization parameters:

- Any β value consistent with one (k_A, D_eff) assumption may be inconsistent with another
- The factor-95× spread in β_q across AI services is consistent with different implicit
  assumptions about the cluster schedule and bridge form
- β degeneracy is a structural consequence of bridge degeneracy (ASRE Insight)

**Evidence marker:** `[VERIFIED-tool]` — ASRE gate, reports/asre_required_schedule.json,
Verdict: PARTIAL, commit 507ead9.

### 3e. No First-Principles Derivation Found

Searched across:
- Buckholtz preprint (available sections)
- docs/01_beta_definition_audit.md
- docs/14_beta_source_trace_audit.md
- docs/16_beta_provenance_reconciliation_summary.md
- TJB email responses (docs/71)

**Result:** No derivation of β_d or β_q from IDM/MULTING internal structure (mass spectra,
coupling constants, force law, geometry) found in any source.

**Caveat:** Author materials may contain a derivation not yet shared.

**Evidence marker:** `[INFERRED]` — absence of evidence, not evidence of absence.
Q3 (full author answer) could resolve this.

---

## 4. What Remains Open

### Q3 (TJB, status: OPEN, reply not before 2026-06-18)

**Question asked (email 2026-06-12):** Are β_d and β_q derived from first principles
within MULTING, or are they fitted/estimated parameters? If fitted: to which dataset,
and what is the fitting procedure?

**TJB partial answer (2026-05-30):** "phenomenological computation… remains to be determined."

**What a full Q3 answer would resolve:**
1. Whether AI-reported values (4.5/18.0 or 4.25/8.10 or 0.78/0.19) match author's intent
2. Whether β are physical constants, fitting parameters, or computational conventions
3. Whether a first-principles derivation exists or is expected
4. Which normalization scheme (if any) reconciles the factor-95× discrepancy in β_q

**Until Q3 resolved:** β status remains `AI_MEDIATED_CANDIDATE / PHENOMENOLOGICAL_PARAMETER`.

---

## 5. What This Does NOT Prove

```
This evidence does NOT prove:
  ✗ That β_d or β_q were fabricated
  ✗ That no physical derivation of β exists or is possible
  ✗ That the author's values are wrong
  ✗ That MULTING theory is false or refuted
  ✗ That any AI service gave incorrect values (each may reflect different assumptions)
  ✗ That the spread in AI values implies error (could be normalization differences)
  ✗ That M2-G4 non-identifiability applies to the author's actual bridge (only OUR_RECONSTRUCTION)

Correct framing:
  ✓ Three AI services produced divergent β values (documented fact)
  ✓ TJB confirmed β are phenomenological estimates (documented fact)
  ✓ M2-G4 showed β non-identifiable under one reconstructed bridge (OUR_RECONSTRUCTION)
  ✓ ASRE showed bridge degeneracy makes individual β underdetermined (structural finding)
  ✓ No first-principles derivation found in available sources (absence of evidence)
```

---

## 6. β Status Summary

| Parameter | AI range | TJB status | M2-G4 status | Use permission |
|-----------|----------|------------|--------------|----------------|
| β_d | 0.78 – 4.5 (5.8×) | phenomenological | non-identifiable (OUR_RECON) | DO_NOT_USE |
| β_q | 0.19 – 18.0 (95×) | phenomenological | non-identifiable (OUR_RECON) | DO_NOT_USE |

---

## 7. Next Optional Gate

### BETA-1: Controlled AI Replication

**Status:** NOT STARTED. Requires explicit user approval before execution.

**Scope (if approved):**
- Use a single standardized prompt across 2–3 AI services to elicit β under identical conditions
- Document prompt, context given, and response — not just numerical output
- Assess whether divergence is prompt-sensitive (normalization) or stable (structural)

**Exit condition:** BETA-1 would clarify whether AI divergence is due to prompt variation
(resolvable) or structural ambiguity in the model (not resolvable without Q3).

**Safety constraints (if executed):**
- No claim that any resulting value is the author's intended β
- No MCMC with derived values
- All results labeled AI_MEDIATED_CANDIDATE · NOT_AUTHOR_CONFIRMED
- No public release

**Trigger for approval:** User explicitly says "run BETA-1" or equivalent.

---

## 8. Evidence Block

```
EVIDENCE BLOCK — BETA-0 (2026-06-13)

CONFIRMED [VERIFIED or VERIFIED-tool]:
  [1] Claude β: β_d=4.5, β_q=18.0 (NotebookLM-mediated, AI_MEDIATED_CANDIDATE)
  [2] Gemini β: β_d≈4.25, β_q≈8.10 (audit reconstruction, AI_MEDIATED_CANDIDATE)
  [3] ChatGPT β: β_d≈0.78, β_q≈0.19 (audit reconstruction, AI_MEDIATED_CANDIDATE)
  [4] β_d spread: 0.78–4.5, factor 5.8× [VERIFIED-tool: multi-AI CSV]
  [5] β_q spread: 0.19–18.0, factor 95× [VERIFIED-tool: multi-AI CSV]
  [6] TJB Q3 partial: β are "phenomenological computation… remains to be determined"
      [VERIFIED: direct quote, docs/71 line 160]
  [7] M2-G4: Fisher rank [β_d, β_q] = 1 under OUR_RECONSTRUCTION bridge
      β_d rel-sensitivity 7e-10; β_q 7e-7; objective flat to ~1e-7
      [VERIFIED-tool: commit 91ea667, 4/4 tests pass]
  [8] ASRE: k_A/D_eff^p uniquely constrained but individual k_A, D_eff not separable
      Bridge degeneracy → β degeneracy structural
      [VERIFIED-tool: commit 507ead9, 42/42 tests pass]
  [9] No first-principles derivation found in available materials
      [INFERRED from absence; Q3 could resolve]

OPEN [requires TJB Q3]:
  [O1] Author's canonical β_d value and derivation method
  [O2] Author's canonical β_q value and derivation method
  [O3] Whether first-principles derivation exists (author's own physics, not AI-mediated)
  [O4] Which normalization convention explains the 95× spread in β_q

NOT PROVEN [explicitly excluded]:
  Fabrication, theory falsity, AI-hallucinated values as such
```

---

## 9. Verdict

```
BETA-0 VERDICT: PASS

Rationale:
  - All four required evidence streams consolidated (AI values, TJB partial,
    M2-G4 non-identifiability, ASRE degeneracy)
  - β classification updated to AI_MEDIATED_CANDIDATE / PHENOMENOLOGICAL_PARAMETER
  - Safety language enforced: no fabrication claim, no theory-false language
  - Q3 open status correctly documented
  - BETA-1 gate identified but NOT started (requires explicit approval)
  - No new AI calls made; no MCMC; no TJB contact

Evidence quality: sufficient for a freeze-point.
Modeling readiness: BLOCKED (DO_NOT_USE until Q3 resolved + values confirmed).
Public claim readiness: NO.
```

---

## 10. Files Changed

| File | Change |
|------|--------|
| docs/111_beta_provenance_evidence_lock.md | NEW — this document |

*No scripts, tests, or reports created — this is a consolidation gate only.*

---

## 11. Current β Status

```
CURRENT_BETA_STATUS: AI_MEDIATED_CANDIDATE / PHENOMENOLOGICAL_PARAMETER

  β_d: 3 AI values (0.78, 4.25, 4.5) — no consensus, no confirmation
  β_q: 3 AI values (0.19, 8.10, 18.0) — no consensus, no confirmation

  DO_NOT_USE_FOR_MODELING
  DO_NOT_PUBLISH_AS_AUTHOR_VALUES
  DO_NOT_CLAIM_FABRICATION

  Next resolution path: TJB Q3 answer (not before 2026-06-18)
```

---

## 12. Next State

```
NEXT_STATE: WAITING_FOR_TJB (unchanged)

  Active gates:          NONE
  Q3 status:             OPEN (email sent 2026-06-12)
  Earliest follow-up:    2026-06-18 (one polite nudge, same Q scope)

  Next β gate:
    BETA-1 (controlled AI replication) — requires explicit approval, not default
    BETA-1 would clarify AI divergence source but NOT resolve Q3

  Hard constraints:
    NO modeling with any β value until Q3 resolved
    NO public claims about β status
    NO second email before 2026-06-18

STOP
```

---

*BETA_PROVENANCE_AUDIT · NOT_AUTHOR_CONFIRMED · PHENOMENOLOGICAL_PARAMETER*  
*AI_MEDIATED_CANDIDATE · NOT_VALIDATION · NOT_REFUTATION*  
*NOT_FABRICATION_CLAIM · NOT_THEORY_FALSE*  
*BETA-0 gate closed 2026-06-13 · docs/111_beta_provenance_evidence_lock.md*
