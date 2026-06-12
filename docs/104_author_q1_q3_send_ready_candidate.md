# Author Clarification — Send-Ready Candidate

**Gate:** AB-2  
**Date:** 2026-06-12  
**Status:** SEND_READY_CANDIDATE · NOT_SENT · Awaiting user approval  
**Upstream:** AB-1 (8277cf0) · EC-1 PASS · VS-1 PARTIAL  
**Open gate:** MASTER vault file not confirmed clean — user manual check required before sending

---

<!-- EMAIL BEGINS — everything below this line is the message to TJB -->

**Subject:** Reproducibility follow-up: three clarification questions on Table A1

---

Dear Dr. Buckholtz,

Thank you for your continued openness on the IDM/MULTING reproducibility work. I have now completed an initial independent reconstruction of Table A1 (Appendix A.3) and have reached a point where three specific gaps prevent further progress. This message contains only those three questions.

**Purpose:** I am working to reproduce the numerical values in Table A1 from the published force-law equations. My goal is accurate representation of your calculation — not to validate or challenge the framework.

**Where I am:** The force components (F_m, F_d, F_q, F_oP) defined in Appendix A.1, Step 2 (p. 33) are clear and dimensionally verified. What I have not been able to identify is the explicit step that maps F_oP — or the underlying multipole amplitudes — to the H_MULT(z) values in Table A1. All numerical gaps I observe are artifacts of my own reconstruction using estimated cluster parameters from the supplementary materials; I am not drawing conclusions about the framework from them.

---

**Q1 — Bridge: F_oP → H_MULT(z)**

Appendix A.1, Step 5 instructs the AI service to use the monopole, dipole, and quadrupole components to fit H(z), but the explicit mapping formula is not stated. Could you describe the intended calculation route — even briefly? For example: is there an intermediate potential Φ(z) whose ratio to a reference value gives H²? Or an acceleration equation of the form ä/a = f(F_oP)? A one-sentence description would allow me to implement the step correctly.

*Note: A scaling relation of the form H²(z) = H²_anchor · Φ(z)/Φ_anchor appears in AI-generated supplementary materials, but I cannot confirm whether this reflects your intended method or is a heuristic introduced by the AI service. I am not assuming either way.*

---

**Q2 — Cluster variable schedules**

Reproducing Table A1 requires the cluster input values at each of the 12 redshift rows: the comoving separation D_C:AB(z), the dipole-strength parameters k_A(z) and k_P(z), and the size parameters r_A(z) and r_P(z). Could you share the table, evolution model, or catalog reference that the AI service used for these inputs?

*Under my reconstructed cluster parameters (geometric means from the supplementary CSV), my predicted H_MULT(z) diverges substantially from your reported values — which I interpret as meaning my cluster inputs do not match those used in Table A1. Providing the intended values would resolve this.*

---

**Q3 — β_d and β_q: physical basis**

The caption for Table A1 states that β_d = 4.5 and β_q = 18.0 were selected by the AI service to minimize standard deviations from observed H(z). You confirmed in a prior exchange that these are phenomenological parameters. My question is whether there is an independent physical principle — a dimensional argument, a symmetry, a mass-ratio relation — that constrains or predicts β_d and β_q without fitting them to H(z) data. If no such principle exists and they are freely adjustable, that is a valid phenomenological description; I just need to represent the model parameter count accurately.

*For reference: under the Table A1 data, the ratio H_MULT / H_FLRW is approximately 1.07 — a TABLE_LEVEL_DIAGNOSTIC observation from my reconstruction, not a physical claim about the framework.*

---

If you are willing to provide any or all of the above, I can rerun my private reproducibility pipeline with full provenance labeling and share the results with you before any public communication.

Thank you for your time.

Sincerely,  
Sergei Kucherenko  
ORCID: 0009-0009-2178-5701 / Ronin Institute

---

<!-- EMAIL ENDS -->

---

**Safety footer (file-level, not sent to author):**

```
NOT_PUBLIC_CLAIM · NOT_VALIDATION · NOT_REFUTATION
SUBJECT_TO_AUTHOR_CLARIFICATION · OUR_RECONSTRUCTION
NOT_SENT — awaiting user approval before sending
```

*AB-2 gate 2026-06-12*
