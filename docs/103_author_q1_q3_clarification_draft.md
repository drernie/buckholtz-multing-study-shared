# Author Clarification Draft — Q1–Q3

**Gate:** AB-1  
**Date:** 2026-06-12  
**Status:** DRAFT · NOT_SENT · Awaiting user approval  
**Safety labels:** OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · TABLE_LEVEL_DIAGNOSTIC · NOT_VALIDATION · NOT_REFUTATION  
**Upstream:** EC-1 PASS (a9eca5d) · VS-1 PARTIAL (85c7c1f)

---

## Internal Safety Review (DO NOT SEND THIS SECTION)

**Do-not-say checklist — CLEARED:**
- ❌ "theory is false" — NOT PRESENT
- ❌ "formula fake" — NOT PRESENT
- ❌ "AI hallucinated" — NOT PRESENT
- ❌ "fatal flaw" without OUR_RECONSTRUCTION scope — NOT PRESENT
- ❌ Universal refutation claims — NOT PRESENT

**Scope labels applied:**
- All numerical gaps are labeled OUR_RECONSTRUCTION
- All bridge candidates are labeled NOT_AUTHOR_CONFIRMED
- H_MULT ≈ 1.074×H_FLRW observation is labeled TABLE_LEVEL_DIAGNOSTIC
- No MCMC, no prediction, no validation claim

**Open risk before sending:**  
`MASTER Source & Findings` vault file was NOT FOUND during VS-1 search.  
Manual check of that file recommended before sending this draft.  
See: docs/102_vs1_vault_sync_report.md — Remaining Risks section.

---

## DRAFT EMAIL — START

---

Subject: Reproducibility follow-up: three clarification questions on Table A1 calculation

Dear Dr. Buckholtz,

Thank you for your earlier response and for your openness to discussing the reproducibility aspects of the IDM/MULTING framework. I am continuing my independent audit and have reached a point where three specific gaps prevent me from proceeding further without your guidance.

**Purpose of this message:** I am trying to reproduce Table A1 (Appendix A.3) independently, and I need to understand three technical details about how H_MULT(z) was computed. My goal is accurate representation of your work — not to validate or challenge it.

I want to be explicit about the scope of what I have done so far:

- I reconstructed the calculation using cluster parameter estimates extracted from the AI-generated supplementary materials (CSV format, geometric means).
- Under my reconstruction, I observe a large gap between my predicted H_MULT(z) and your reported values — which I take as a signal that I am missing a key ingredient, not as a statement about your theory.
- I am treating all of my numerical findings as **OUR_RECONSTRUCTION** results that are not author-confirmed.

With that context, my three questions are:

---

**Q1 — Bridge formula (F_oP → H_MULT(z))**

In Appendix A.1 (Step 2 Guidelines, p. 33), the force components F_m, F_d, F_q and the combined F_oP are clearly defined. Step 5 (p. 34) instructs the AI service to use these components to compute H_MULT(z), but I have not been able to identify the explicit formula that maps the force or potential quantities to H_MULT(z).

Could you clarify: **what is the intended calculation route from F_oP (or from the multipole amplitudes A_m, A_d, A_q) to H_MULT(z)?** For example, is there an intermediate scalar potential Φ(z), a Friedmann-type acceleration equation, or a direct ratio formula? Even a one-sentence description of the intended route would allow me to reconstruct the calculation correctly.

*Context: I have encountered a scaling candidate H_MULT²(z) = H_anchor² × [Φ(z)/Φ_anchor] that appeared in AI-generated supplementary materials, but I cannot confirm whether this reflects your intended calculation or is an artifact of the AI service. I am not assuming either way.*

---

**Q2 — Cluster variable schedules**

For Table A1 to be reproducible, I need the values (or the schedule / evolution model) for the following cluster variables at each of the 12 redshifts in Table A1:

- D_C:AB(z) — comoving separation between clusters A and B
- k_A(z), k_P(z) — dipole-strength parameters for clusters A and P
- r_A(z), r_P(z) — size or radius parameters for clusters A and P

Could you share the cluster variable tables (or the evolution model) that the AI service used to generate Table A1? Alternatively, if there is a published cluster catalog or a standard dataset underlying these values, a reference would be equally helpful.

*Context: Under my reconstructed cluster parameters (geometric means from the supplementary CSV), my predicted H_MULT(z) is substantially lower than your reported values — which I interpret as meaning my cluster parameters do not match the ones the AI service used. I am not inferring any error in your calculation; I simply cannot reproduce it without knowing the intended cluster inputs.*

---

**Q3 — β_d and β_q: physical status**

Table A1 caption states β_d = 4.5, β_q = 18.0, selected by the AI service to minimize standard deviations from observed H(z). You confirmed in your earlier response that these are phenomenological parameters.

My question is: **is there an independent physical principle, constraint, or derivation that determines β_d and β_q without fitting them to the observed H(z) data?** For example, a dimensional argument, a lattice symmetry, a mass-ratio relation, or a first-principles prediction.

If β_d and β_q are freely adjustable parameters constrained only by fitting to H(z), that is a perfectly valid phenomenological description — I just need to understand the model correctly when I compute how many free parameters MULTING uses relative to ΛCDM.

*Context: I am asking because, under the Table A1 data, the ratio H_MULT/H_FLRW is approximately 1.07 (our TABLE_LEVEL_DIAGNOSTIC observation), and I want to understand whether this level of fit improvement is expected from a 2-parameter family, or whether the framework makes a sharper prediction.*

---

I am happy to share my reconstruction code and internal diagnostics if that would help clarify where my reconstruction diverges from your intended calculation. None of my internal analysis constitutes a validation or refutation of MULTING — it is an audit layer designed to help me represent your work accurately.

Thank you for your time.

Sincerely,  
Sergei Kucherenko  
[ORCID: 0009-0009-2178-5701 / Ronin Institute]

---

## DRAFT EMAIL — END

---

## Scope Boundary Reminder (INTERNAL)

| Label | Meaning | Where applied in draft |
|---|---|---|
| `OUR_RECONSTRUCTION` | Our cluster param estimates, not author-confirmed | Q1 context, Q2 context |
| `NOT_AUTHOR_CONFIRMED` | Bridge formula candidate from AI output, not manuscript | Q1 paragraph 2 |
| `TABLE_LEVEL_DIAGNOSTIC` | H_MULT ≈ 1.07×H_FLRW observation from Table A1 only | Q3 context |

---

## Evidence Appendix (INTERNAL — not sent to author)

Claims in this draft are based on:

| Claim | Source file | Section |
|---|---|---|
| Force formulas F_m/F_d/F_q exist in Step 2 p.33 | `docs/100_hd_mavp_autopsy_internal.md` | Part I, A0 Result |
| Bridge F→H absent from preprint | `docs/100_hd_mavp_autopsy_internal.md` | Part I, A0 Result (Blocker-1) |
| Gap ×4365 at z=8.5 (OUR_RECONSTRUCTION) | `docs/100_hd_mavp_autopsy_internal.md` | Part I, A1 / Part V Evidence Inventory |
| AI candidate H²∝Φ/Φ₀ (NOT_AUTHOR_CONFIRMED) | `docs/26_author_clarification_brief.md` | Section 2b |
| D_C:AB(z), k_A(z), r_A(z) schedules missing | `docs/26_author_clarification_brief.md` | Section 2b, Required inputs |
| β_d=4.5, β_q=18.0 phenomenological (TJB confirmed) | `docs/100_hd_mavp_autopsy_internal.md` | Part I, A3 |
| H_MULT ≈ 1.074×H_FLRW TABLE_LEVEL_DIAGNOSTIC | `docs/100_hd_mavp_autopsy_internal.md` | Part I, A3 (OUR_OBSERVATION tag) |
| β_q Claude 18.0 vs Gemini 8.10 | `docs/100_hd_mavp_autopsy_internal.md` | Part V Evidence Inventory |

---

## Open Risks Before Sending

1. **MASTER Source & Findings vault file NOT FOUND** (VS-1 finding) — manual check required before sending. See `docs/102_vs1_vault_sync_report.md`.
2. **NO_EMAIL_WITHOUT_APPROVAL gate** — this draft is NOT SENT until user explicitly approves.
3. **Q3 wording ("how many free parameters")** — verify user is comfortable with BIC framing before sending.

---

*NOT_VALIDATION · NOT_REFUTATION · NOT_SENT · DRAFT_ONLY*  
*AB-1 gate closed 2026-06-12*
