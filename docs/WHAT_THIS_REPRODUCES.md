# What This Audit Actually Reproduces

**Status:** Scope-clarification document (no validation, no refutation)
**Date:** 2026-06-01
**Purpose:** State precisely what this repository does and does NOT reproduce, so no reader — including the author — mistakes the work for a test of IDM/MULTING physics.

---

## One-sentence summary

> This repository reproduces and audits an **AI-service-mediated computation** (Table A1 and its beta parameters), **not** Buckholtz's physical theory — because the theory's bridge from the multipole force law to H_MULT(z) is under-specified in the source material.

---

## The reproduction chain (why framing matters)

The object under audit is several steps removed from "Buckholtz physics":

1. Buckholtz gives a **prompt** to AI services (ChatGPT, Claude, Gemini) — explicitly *"trying not to give directions as to how to do the steps"* (Section 2.5; correspondence 2026-05-30).
2. Each AI service **independently fits** beta parameters to observed H(z) and emits a Table-A1-like table.
3. This repository takes Table A1 (the **Claude** output) as a reference and builds a diagnostic bridge, fits beta to that table, and compares residuals.

So a claim like *"H_MULT residuals are ~6× smaller than H_FLRW"* is **not** a statement about the theory. It is:

> a self-consistency check in which AI-fitted parameters reproduce an AI-fitted column on the same data (β fitted by an AI service → residuals computed against that same AI service's H_MULT column).

This is **retrodiction on the training data**, with the additional twist that the fitter and the target both originate from the same AI service. We label this **triple circularity** and never present it as fit quality, let alone validation. See `docs/PARANOID_MODE_FINAL_AUDIT.md` (Finding 1).

---

## What the beta values actually are

The candidate beta values in `src/beta_definitions.py` are **AI-service outputs**, not different versions of Buckholtz's model. Source-confirmed from the supplementary materials the author provided (see `docs/93`):

| AI service | beta_d | beta_q |
|-----------|--------|--------|
| Gemini    | 4.25   | 8.10   |
| ChatGPT   | 0.78   | 0.19   |
| Claude    | 4.5    | 18.0   |

- Spread: **5.8×** for beta_d, **94.7×** for beta_q across services on the same prompt.
- The Claude pair (4.5 / 18.0) is the actual **Table A1 caption** value and is the authoritative entry in `src/beta_provenance.py` (`beta_d_A1`, `beta_q_A1`), marked `manuscript_reported_fitted` / `allowed_for_fit_reproduction_only`.

### Open provenance inconsistency (documented, not resolved)

`src/beta_provenance.py` records `beta_d_1 = 4.25` as an **audit reconstruction** (`4.25 ~ 17/4` from an internal anchor), created **before** the supplementary materials revealed 4.25 is the **Gemini** output. These two provenance stories now coexist:

- `beta_provenance.py`: `4.25 = audit_reconstruction (17/4)`
- `docs/93` (source-confirmed, later): `4.25 = Gemini AI-service output`

We deliberately **do not silently pick one**. The coincidence (an AI service landing on a value close to a simple anchor ratio) is itself an open question — possibly numerology, possibly independent convergence. It is flagged here for reconciliation rather than overwritten. The "numerical relations between betas" reported earlier (e.g. `beta_q_1 ≈ (128/3)·beta_q_2`, error 0.08%) must be read in this light: they may be **artifacts of how two LLMs rounded numbers**, not physics.

---

## What this repository DOES reproduce

- ✅ **Eq.15 arithmetic** — `(4/3)·(m_τ²/m_e²)⁶ ≈ k_e·e²/(G·m_e²)` to ~1% (PDG/CODATA constants). Arithmetic only; **no physical mechanism** for exponent 6 or prefactor 4/3.
- ✅ **Force-law and scaling relations** from Appendix A1 (`F_m`, `F_d`, `F_q`; `r_dA = β_d·r_A`, etc.).
- ✅ **Table A1 as empirical reference data** (the AI-service output, transcribed).
- ✅ **Inter-service divergence** of beta parameters (the genuinely novel, reproducible finding).
- ✅ **Provenance and use-permission tracking** that prevents using unverified values for modeling.

## What this repository does NOT do

- ❌ Validate or refute IDM/MULTING.
- ❌ Reproduce **Buckholtz's physics** — the H_MULT(z) computational formula is **missing** from Appendix A1 Step 5 (only scaling relations + "minimize σ"). See `APPENDIX_A1_EXTRACTION_SUMMARY.md`.
- ❌ Predict H_MULT(z) on new redshifts (no forward model → MCMC blocked).
- ❌ Establish that the beta values are physical constants rather than fit parameters.

---

## Why this is the honest competition-grade framing

For a reproducibility / methodology audience, the value of this repository is **not** "we checked a cosmology". It is:

> a documented case study of **AI-mediated scientific computation** — how three LLMs, given one loose prompt, produced materially different parameter fits, and how a provenance-first audit keeps those outputs from being mistaken for verified physics.

Stated that way, the work makes **no overclaim** and its contribution is exactly reproducible from the artifacts in this repo.

---

## Cross-references

- `src/beta_provenance.py` — single source of truth for beta provenance / use-permission
- `src/beta_definitions.py` — legacy candidate registry (AI-service outputs, attributed)
- `tests/test_beta_registry_consistency.py` — guard that the two registries cannot drift
- `docs/PARANOID_MODE_FINAL_AUDIT.md` — circular-logic / wording-hardening findings
- `docs/91_negative_control_results.md` — diagnostic specificity results (DIAGNOSTIC_ONLY)
- `APPENDIX_A1_EXTRACTION_SUMMARY.md` — H_MULT formula gap (forensic extraction)
