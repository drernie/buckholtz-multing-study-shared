# Task 029 — treatment arm output (FL protocol)

## Falsification-Ladder Review — Task 029 (Reservoir Inflow Integral)

### 1. Falsifiable claim
Two bundled claims: **A (numerical)** -- `quad` correctly computes the integral with the stated tiny error; **B (physical)** -- because A's error bound is tiny, the resulting 1,638,600 m^3 is a reliable estimate of ACTUAL reservoir inflow, corroborated by a historical range. Report treats B as following from A.

### 2. Controls
**None genuine.** No positive control (synthetic data with known parameters through the same gauge-fit procedure), no negative control (a wrong model shown to fail the historical-range check). `quad`'s internal error estimate is not a scientific control -- it bounds quadrature error given q(t), not model error of q(t) itself.

### 3. Circularity / provenance issues
Six defining constants (peak1=25000, center1=30, width1=12, peak2=18000, center2=75, width2=20) are hard-coded with no cited source, no gauge station ID, no uncertainty -- "individually validated against historical gauge data" is asserted, not shown. Possible circularity: if peak/width were fit from the SAME historical records used for the "1.5-2.0M m^3" comparison, the two checks aren't independent -- flagged `[HYPOTHESIS]`, not confirmed.

### 4. Executed checks
Reproduced the script + ran an ablation and a discriminating-power/negative-control sweep:
```
Q_total = 1,638,594.08 m^3 (script's own stdout -- report's "1,638,600" is a mismatch, ~6 m^3, ~900x larger than the claimed 6.7e-3 error bound)
quad error = 6.678e-3 m^3 (relative 4.08e-9) -- matches report

Analytic full-line total: 1,654,374.66 m^3; [0,120] truncation excludes ~0.95% of modeled process

Sensitivity (uniform peak scaling): -20% -> 1,310,875 | -10% -> 1,474,735 | +10% -> 1,802,453 | +20% -> 1,966,313
  -- Q_total moves ~1:1 with a uniform parameter shift, no damping

Discriminating-power sweep against "1.5-2.0M" historical range:
  baseline                    1,638,594  PASSES
  peak1 -30%                  1,414,398  fails
  peak1 +30%                  1,862,790  PASSES  <- wrong-by-30% still "validates"
  width1 +30%                 1,842,236  PASSES  <- wrong-by-30% still "validates"
  peak2 +30%                  1,905,977  PASSES  <- wrong-by-30% still "validates"
  width2 +30%                 1,869,149  PASSES  <- wrong-by-30% still "validates"
```
Any single one of the 4 amplitude/width parameters can be wrong by 30% ALONE and the total still lands inside "historical range" -- the check has almost no discriminating power. No parameter uncertainty is propagated anywhere in the report despite realistic gauge-fit uncertainty (+/-10-20%) dwarfing the quoted 4e-9 relative numerical error by many orders of magnitude.

### 5. Verdict
**REJECT** the conclusion "the estimate is numerically reliable [therefore trustworthy]." Claim A -> CONFIRMED-REAL; Claim B -> FALSIFIED as stated (downgradeable to NEEDS-REAL-DATA if gauge-data provenance/independence is disclosed). Textbook precision theater: a real, correctly-computed ultra-precise number (quadrature) is used to imply confidence about a completely different, unverified question (whether the function models real inflow). The one physical-plausibility check passes for many substantially wrong parameter sets, so it doesn't discriminate correct from incorrect models, and its independence from the fitting data is undisclosed and plausibly circular.

---

### DRAFT CLAIM
A hydrology report claims 120-day cumulative inflow of 1,638,600 m^3 via `scipy.integrate.quad` on a two-Gaussian model, calling it "numerically reliable" because quad's own error bound is ~6.7e-3 m^3, which also roughly matches a cited 1.5-2.0M m^3 historical range. Independent recomputation confirms the integral and error bound, but the reliability conclusion does not follow: quad's bound only certifies integration precision of the GIVEN function, not whether that function models real inflow, and no positive or negative control is provided. A parameter-sensitivity sweep shows any single one of 4 amplitude/width parameters can be wrong by 30% in isolation and the total still lands inside the "historical range," meaning that check has very weak power to distinguish correct from incorrect models; the six defining constants are unsourced, and it cannot be ruled out the "historical range" derives from the same gauge data the parameters were fit to (circular). Verdict: arithmetic correct, reliability conclusion unsupported -- reject as stated pending disclosed provenance, an actual independent control, and propagated parameter uncertainty.
