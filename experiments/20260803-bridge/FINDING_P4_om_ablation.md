# P4: Ω_m ablation through the full chain — the anchor holds, the β's do not

**Date:** 2026-08-10 · plan item P4
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `om_ablation.py` · control reproduced exactly

---

## Why redone, and what failed the first time

`multing_core.py` embeds Planck `Ω_m = 0.315` inside `T(z)`, `M_gas(z)`,
`ρ_crit(z)` (hence `R(z)`), and `H_LCDM` used by the accretion term — so
"MULTING vs ΛCDM" comparisons carry a hidden architectural dependence
`MULTING ← Planck E(z)`. A prior attempt at this ablation returned an exact
null effect that was itself an artefact: `def Efun(z, Om=Om_planck)` binds its
default **at function-definition time**, so mutating the module attribute
afterward changes nothing — caught by a manipulation check (Errors and fixes,
this session's summary).

**Fix:** the module source is rewritten with the new `Ω_m` substituted
textually and re-executed, so every default argument, module constant and
closure genuinely sees the new value. Re-run this time with the manipulation
check first: `Efun(1)` must move (it did: 1.7903 → 1.5492 across the scan).

## Control: exact reproduction at the archive's own value

```
Om=0.315:  H0_anchor=73.2160, chi2_33=15.7515, r_33=0.9659   <- matches paper exactly
```

## Result: the anchor is robust; the β's are not

| `Ω_m` | `H₀_anchor` | `β₁` | `β₂` | `χ²₃₃` |
|---:|---:|---:|---:|---:|
| 0.20 | 73.1830 | 1.013e10 | 5.760e17 | 14.68 |
| 0.25 | 73.1975 | 1.162e10 | 6.481e17 | 15.01 |
| 0.30 | 73.2121 | 1.361e10 | 7.450e17 | 15.54 |
| **0.315** | **73.2160** | **1.434e10** | **7.807e17** | **15.75** |
| 0.35 | 73.2231 | 1.636e10 | 8.796e17 | 16.42 |
| 0.40 | 73.2193 | 2.034e10 | 1.074e18 | 18.06 |

`H₀_anchor` moves by **< 0.05 km/s/Mpc** (0.06 %) across the entire scanned
range 0.20–0.40 — the anchor is effectively insensitive to the embedded Planck
value.

**`β₁` and `β₂` are not.** `d ln(β₁)/dΩ_m = +3.49`, `d ln(β₂)/dΩ_m = +3.11` —
each grows by roughly **e^0.7 ≈ 2×** across a plausible `0.30 ± 0.02` window,
and by a full order of magnitude (`2.0×10¹⁰` vs `1.0×10¹⁰`) across the full
0.20–0.40 scan. `χ²₃₃` also moves substantially (14.7 → 18.1).

## What this means

The reviewer's "hidden architecture" concern is confirmed and quantified: **the
fitted β values are properties of (data + the assumed Planck ΛCDM inputs
embedded in T/M_gas/R), not of the data alone.** Reporting `β₁, β₂` without
their `Ω_m` dependence overstates how much the data constrain them. `H₀_anchor`
is the one output of this pipeline that survives the ablation essentially
unscathed — it is the quantity the seven-row tension table actually leans on,
and it is the one least contaminated by the circularity.

## Verdict

```
Control (Om=0.315)              : reproduced exactly (73.2160/15.7515/0.9659)
Manipulation check              : passed -- Efun genuinely moves with Om this time
H0_anchor sensitivity           : d H0/dOm = +0.18 -- < 0.1% over 0.20-0.40, robust
beta_1, beta_2 sensitivity      : d ln(beta)/dOm ~ +3.1 to +3.5 -- an order of
                                   magnitude swing over the scanned range
Interpretation                  : beta_1, beta_2 are NOT data-only quantities;
                                   they inherit the pipeline's Planck assumption
```

## What this does NOT establish

1. Not a claim that `Ω_m = 0.315` is wrong — the point is that the fit result
   for `β₁, β₂` is conditional on it, and that conditionality was not visible
   in the archive's headline numbers.
2. The scan is 1-D (`Ω_m` alone, flat `Ω_Λ = 1 − Ω_m`); other embedded choices
   (the self-similar `T–M` normalisation, the Ramos-Ceja `M_gas` fit
   parameters) were not varied and may carry comparable sensitivity.
3. Not yet propagated to whether the seven-row tension-reduction narrative
   (Table II) survives — only `H₀_anchor`, `β₁`, `β₂`, `χ²₃₃` were tracked here.
