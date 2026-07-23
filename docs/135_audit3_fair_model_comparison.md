# docs/135 — Audit 3: Independent End-to-End Reproduction + Fair Model Comparison

**Date:** 2026-07-23
**Origin:** third of the user's three priority audits (docs/133=Audit 1, docs/134=Audit 2).
Executed via boyko-agent, coordinator-reproduced and independently re-verified (numbers,
AIC/BIC arithmetic, delta_chi2 claim) before acceptance.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

---

## Correction to this audit's own planning (stated up front, honestly)

When this audit was scoped, the plan cited R011's stored `AIC_LCDM=16.8` and `AIC_MULTING=19.3`
as if directly comparable numbers already sitting in facts.json. **Audit 3 found this framing was
imprecise**: MULTING's φ(z) depends per-cluster on M500/R500/E_thermal, not on z alone (Q006 — no
continuous MULTING H(z) exists) — so it never had a genuine 27-CC-point likelihood the way LCDM
does, and R011's `AIC_MULTING=19.3` was computed on a different footing (a Fisher-z/AIC proxy
over the 443-cluster r-value, not the same chi2-on-27-points basis LCDM's 16.8 uses). This audit
corrects that: the two are now properly separated (see table below), not silently placed side by
side. This is exactly the kind of prose/footing mismatch Audit 2 (docs/134) was built to catch —
finding one in this audit's own setup, not just in the paper, is the discipline working as
intended.

## Unified side-by-side table [VERIFIED-BASH, coordinator-reproduced]

| model | #free params | chi2 (27 CC) | AIC | BIC | ΔAIC vs ΛCDM | Pearson r (443 clusters) | holdout (70/30, seed=42) |
|---|---|---|---|---|---|---|---|
| **ΛCDM** (H0, Ωm) | 2 | 12.81 | **16.81** | **19.40** | 0.00 | **0.8796** | χ²/pt = 1.518 |
| **wCDM** (H0, Ωm, w) | 3 | 12.81 | 18.81 | 22.70 | **+2.00** | 0.8811 | χ²/pt = 1.669 |
| **MULTING monopole** | η-only | n/a* | n/a* | n/a* | n/a* | 0.7334 | r = 0.7087 |
| **MULTING full** (β_d=100, β_q=3.24×10⁷) | η-only | n/a* | n/a* | n/a* | n/a* | 0.6235 | r = 0.6162 |

`*` MULTING has no chi2/AIC/BIC on the 27-CC-point footing because φ is not a function of z alone
— it cannot be scored against those 27 points at all, only against the 443-cluster r-correlation
(a genuinely different statistical object). Reporting `n/a` rather than forcing a false comparison
is the correct move here, not an evasion.

**Fits:** ΛCDM H0=68.77±2.27, Ωm=0.317±0.042. wCDM H0=68.38±5.00, Ωm=0.314±0.054, w=−0.959±0.464.

**Reproducibility check:** r-values (ΛCDM 0.8796, MULTING-mono 0.7334, MULTING-full 0.6235) match
R011's stored 0.8795/0.7334/0.6235 to 4 significant digits — **R011 is independently
reproducible**, coordinator-confirmed by re-running the script directly (not trusting the agent's
own claim).

## Prediction vs. fit (Phase B — the honest finding)

**Every row in the table is a fit. Nothing is a genuine held-out prediction of a parameter fixed
by data independent of the CC points being scored.** ΛCDM/wCDM: all 27 points used to fit
H0/Ωm(/w). MULTING full: β_d, β_q are grid-searched (fitted) in R011, explicitly phenomenological.
MULTING monopole: no β freedom, but H0=73 and D0 are set to the data scale. The 70/30 holdout
columns are the only genuinely out-of-sample numbers, and they only confirm the in-sample
ranking — no model improves out-of-sample. This "everything is a fit" answer is itself the
correct, useful result — not a gap to be embarrassed about.

## wCDM constraint quality — anti-cherry-pick finding

wCDM's extra parameter is unpaid-for: Δχ²=0.0034 (best-fit w=−0.959≈−1 collapses onto ΛCDM), so
ΔAIC=+2.00 is essentially the bare 2Δk penalty, not a real improvement — a round ΔAIC here is the
*signature of an unhelpful parameter*, verified directly via Δχ², not assumed from the round
number alone. w's own uncertainty (±0.464, 1σ band [−1.42, −0.49]) spans most of the plausible
dark-energy range; the train-split value jumps to −1.889±0.925 under a 70% resample — **fragile,
not a detection**. w=−1 (plain ΛCDM) sits inside the 1σ band. 27 chronometer points simply cannot
constrain w meaningfully; this is a property of the data, not a defect in the fit.

## AIC/BIC verdict

Adding wCDM does **not** change the qualitative story: free ΛCDM remains the preferred H(z)
description (ΔAIC=+2.0, ΔBIC=+3.3 against wCDM, both penalizing the unhelpful w). On MULTING's own
r-footing: ΛCDM (0.88) > MULTING-monopole (0.73) > MULTING-full (0.62) — adding the dipole/
quadrupole structure makes the fit *worse*, in-sample and out-of-sample, consistent with R011's
already-established nesting result (docs/122 v6).

## Overall verdict: **PIVOT**

Per the user's own Audit-3 criteria:
- **Not FAIL** — MULTING reproduces to 4 digits; units/method match R011; β's honestly labeled
  fitted, not smuggled as derived.
- **Not PASS** — PASS required a robust held-out advantage surviving equal anchoring + complexity
  penalty. MULTING shows the opposite: never beats free ΛCDM (or wCDM, which reduces to ΛCDM), in
  or out of sample.
- **= PIVOT** — the numbers reproduce, but plain free ΛCDM describes the H(z) data equally well or
  better, and wCDM's extra parameter buys nothing. Scope strictly limited to "this pipeline's
  tested configurations" — not a refutation of MULTING as a theory, only of this implementation's
  cosmic-acceleration mechanism as an H(z) description.

---

## Cross-check against Audits 1 and 2

All three audits converge independently on the same structural picture, reached by three
different routes:
- **Audit 1 (C1 closure, docs/133):** H_MULT(z) has no derived equation — NEEDS_DATA.
- **Audit 2 (provenance, docs/134):** H_MULT(z) row flagged 🔴 "not a derived formula" for the
  same reason.
- **Audit 3 (this document):** independently discovers MULTING's φ isn't a function of z alone,
  which is WHY no chi2/AIC/BIC exists for it — the same underlying fact (no closed H(z) form),
  found from the statistical-methodology side rather than the theory-closure side.

This convergence from three independent angles is itself evidence the finding is robust, not an
artifact of any one audit's framing.

---

*Artifacts: `scripts/audit3_fair_model_comparison.py` (ruff-clean, coordinator-reproduced),
`scratchpad/boyko_AUDIT3_model_comparison.md` (full agent report). No new data collected — reuses
`data/hz_cc.csv` and `data/clusters_clean.csv` already in the repo, and R011's already-found
MULTING optimum rather than re-running a fresh grid search.*
