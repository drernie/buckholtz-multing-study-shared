# The bridge cannot target Table A1 — and the reason is in the paper

**Date:** 2026-08-03 · **Stage:** B0, before any bridge construction
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## Summary

The bridge programme was to reconstruct the operator carrying the MULTING force
law into `H(z)`, using Table A1 and Figure 3 as the target. Before building it,
the target was audited.

**Table A1 is not a MULTING calculation.** It is the output of an AI service
responding to a prompt, and the author says so plainly in the caption and in the
surrounding text. Every column — including `H-MULT` and `H-FLRW` — was
*requested from the service*, not computed by a model.

That resolves the bridge question at the root: there is no operator to recover
from Table A1, because no operator produced Table A1. A candidate bridge, if
built, must not be validated against it — doing so would mean reproducing a
language model's output, not a physical theory.

The author is explicit and unambiguous about this. The finding concerns what the
object is, not how it was presented.

---

## What the source says — verbatim

Verified against `data/source_material/buckholtz_preprints202511.0598.v6_pymupdf-clean.md`
(PDF text layer, pages 38–39). Marked `[VERIFIED-SOURCE]`.

On the nature of the table:

> "Table A1 shows responses, to our prompt, by one online service that has bases
> in artificial intelligence."

The caption, in full agreement:

> "Table A1. Responses, to our prompt, by one online service that has bases in
> artificial intelligence."

On each column being prompted rather than derived:

> "Regarding H-FLRW, the prompt asked for a value that ΛCDM cosmology suggests."
> "Regarding H-MULT, the prompt asked for a value that MULTING suggests."
> "Regarding z, the prompt asked for a redshift that associates with the time."

On the author's own confidence in it:

> "the responses that Table A1 shows are not necessarily trustworthy or directly
> useful"

On where the β coefficients came from:

> "Regarding H-MULT, the online service reported choosing βd = 4.5 and βq = 18.0."

And, decisively for the `w_eff` column:

> "Regarding w_eff, the prompt did not define w_eff but did state 'Compute a
> sample w_eff(z) curve **from the H-data values** (of H(z)) that you already
> used.'"

---

## What the numbers independently confirm

Each item below was computed from the table before the caption was read, and
each agrees with what the caption says. `[VERIFIED-NUMERIC]`

### 1. `w_eff` reproduces the observations, not the model

The prompt asked for a curve fitted to the H-data. It is:

| `H-w_eff` compared against | max deviation | rms |
|---|---|---|
| `H-data` (observations) | 0.48 % | **0.29 %** |
| `H-MULT` | 1.28 % | 0.85 % |
| `H-FLRW` | 11.3 % | 7.91 % |

`w_eff` is a fit to the data by construction, and the numbers show it. Its first
six values are an exact arithmetic progression:

```
-1.30  -1.25  -1.20  -1.15  -1.10  -1.05      step exactly +0.05
-1.01  -0.98  -0.96  -0.95  -0.97  -1.00      the pattern then breaks
```

### 2. `H-FLRW` is not the expansion history of any standard cosmology

Fitting the column with four cosmologies:

| model | max residual | best-fit `Ω_m` |
|---|---|---|
| flat ΛCDM | 17.4 % | 0.040 |
| flat wCDM | 5.6 % | 0.035 |
| power law `H ∝ (1+z)^n` | 9.8 % | — |
| CPL `w₀–wₐ` | 3.3 % | 0.010 |

Every fit drives the matter density to 0.01–0.04, **below the baryon density
alone** (`Ω_b = 0.049`). At `z = 8.5` the column reads 398.5 km/s/Mpc against
Planck ΛCDM's 1109.

### 3. The `(z, t)` pairs are not a ΛCDM age relation

The time column is an exact integer-gigayear grid — 13.5, then 13, 12, …, 3.
The redshift assigned to each does not correspond to that time in ΛCDM:

| | table | flat ΛCDM |
|---|---|---|
| age at `z = 8.5` | 3.0 Gyr | 0.59 Gyr |
| maximum discrepancy | — | 3.01 Gyr |

### 4. The table's own `(z, t)` pairs generate an `H(z)` matching no column

Differentiating the tabulated pairs, `H = −(1+z)⁻¹ dz/dt`, gives values that
deviate from `H-data` by 71 %, from `H-FLRW` by 83 %, and from `H-MULT` by 69 %
in the median.

### 5. Four of twelve rows lie beyond any cosmic-chronometer measurement

The cosmic-chronometer compilation in this repository spans `z ∈ [0.070,
1.965]`, 27 points. Table A1 carries "H-data" values with uncertainties at
`z = 2.1, 3.2, 5.0, 8.5`.

---

## A transcription correction, made along the way

Our working file `data/table_a1_reported.csv` was checked field by field against
the source text layer: **104 of 108 numeric fields matched.** Four fields in the
first row did not, and are corrected in the new source-verified file:

| field at `z = 0` | our file | source |
|---|---|---|
| `sigma_H` | 1.1 | **1.0** |
| `H_MULT` | 71.1 | **73.0** |
| `sigma_MULT` | 1.3 | **0.0** |
| `w_eff` | absent | **−1.30** |

The corrected `H_MULT(0) = 73.0` is worth noting on its own: it equals the
observed value exactly, with `σ_MULT = 0`.

Use `data/table_a1_source_verified.csv` from here. The old file is left in place
as the record of what was previously assumed.

---

## Consequences for the bridge programme

**B0 — freeze the claim.** The claim as originally framed —

> at fixed `β_d`, `β_q`, `k_A`, `r_A`, `D`, without tuning to `H(z)`, the MULTING
> force law reproduces the published `H_MULT(z)`

— is **not testable against Table A1**, because the published `H_MULT(z)` is not
an output of the force law. It is an AI service's answer to a request for "a
value that MULTING suggests". Testing a bridge against it would test agreement
with generated text.

**Verdict: `BLOCKED_BY_TARGET_PROVENANCE`**, which is distinct from the three
outcomes the programme anticipated. It is not PASS, not FAIL, and not the
expected BLOCKED (author has not supplied `k_A`, `r_A`, `D`). The target itself
is of the wrong kind.

**What remains possible, and worth doing:**

1. **Build the candidate bridge anyway**, and evaluate it against *observations*
   — the cosmic-chronometer compilation — rather than against Table A1. That is
   a real test of the force law, and the target is then measured data.
2. **Ask the author the sharper question.** Not "what are `k_A(z)`, `r_A(z)`,
   `D(z)`" but first: *is there a MULTING calculation of `H(z)` that does not
   pass through an AI service?* If yes, that calculation is the object to
   reconstruct, and Table A1 is a distraction. If no, then the bridge does not
   exist yet in any form, and building one is new work rather than
   reconstruction.
3. **The kSZ constraint is unaffected.** It tests the force law directly against
   ACT+SDSS pairwise velocities and never touches Table A1.

**What must not be done:** quoting any Table A1 number as a MULTING prediction,
in either direction. That includes our own earlier reconstructions of `ε(z)`,
`q(z)` and `w_eff` from it — they characterise the AI output, and the labels on
those results must say so.

---

## Scope

This audits a published table for internal consistency and provenance. It
evaluates neither MULTING nor the author's other results, and nothing here
supports or refutes the model. The author labelled the table accurately; the
error was in our assumption that it was a model calculation.

Artifacts: `scripts/bridge_b0_table_a1_audit.py`,
`experiments/20260803-bridge/artifacts/b0_table_a1_audit.json`,
`data/table_a1_source_verified.csv`.
