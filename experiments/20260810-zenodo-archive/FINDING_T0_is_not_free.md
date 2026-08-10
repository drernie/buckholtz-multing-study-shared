# T₀ is not a free parameter, and the tension is between two external calibrations

**Date:** 2026-08-10 · **Target:** Zenodo 10.5281/zenodo.21204955
**L0:** Descriptive — comparison of the archive's own quantities against externally
measured relations. No causal claim.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

---

## What the archive says

`assumptions.yaml`:

> `T0_note: "Temperature normalization, RECALIBRATED from an earlier value of 6.0
> keV. Chosen so implied gas fraction is realistic (~0.13 at z=0); this in turn
> implies cluster temperatures ~3.3-3.6 keV, noticeably below independent
> weak-lensing-calibrated M-T relations (~7 keV) for the same mass. See paper
> Sec. II.C for full discussion of this unresolved tension."`

Flagged by the author as unresolved. Verified reproduction of the archive's own
numbers `[VERIFIED-BASH]`:

| quantity | archive value |
|---|---|
| M₀ | 1.193082e45 kg = **6.000 × 10¹⁴ M☉** (exactly 6.0) |
| T₀ | 3.7163 keV |
| f_gas(z=0) | **0.1307** — matches the stated "~0.13" |
| T range over 0 ≤ z ≤ 2.33 | 3.287 – 3.716 keV (the note's "3.3–3.6" understates the z=0 end) |
| R₅₀₀(z=0) | 1.315 Mpc |

---

## Finding 1 — T₀ was not chosen; it was forced

The note reads as though T₀ were tuned. It is not a free parameter. Three inputs
determine it uniquely:

1. `M₀ = 6 × 10¹⁴ M☉` — **chosen**, and a round number
2. `f_gas ≈ 0.13` — required by observation
3. `M_gas(T)` from Ramos-Ceja et al. 2025 — external: `B = 2.24`, pivot
   `2.28 × 10¹³ M☉` at `T = 2.27` keV

Solving (2) and (3) at (1) for T gives **T₀ = 3.7160 keV** against the archive's
**3.7163** — agreement to four figures. `[VERIFIED-BASH]`

So the recalibration was not a choice among options. At the original T₀ = 6.0 keV
the Ramos-Ceja relation gives M_gas larger by a factor **2.92**, hence

```
f_gas = 0.382     vs     cosmic baryon fraction Ω_b/Ω_m = 0.157
```

— more than twice the cosmic ceiling, and therefore unphysical. The move to
3.7163 keV was the only way to keep f_gas admissible **given M₀ and the
Ramos-Ceja relation**.

This reframes the note: the free choice was never T₀. It was **M₀**.

---

## Finding 2 — the tension is between two external calibrations, not with MULTING

Ask whether any mass exists at which all three hold simultaneously: standard
self-similar M–T, the Ramos-Ceja M_gas–T, and a realistic f_gas.

Taking the archive's own (unverified, see below) anchor `T_std(M) = 7 keV ×
(M/6×10¹⁴)^{2/3}`:

| M [M☉] | T_std [keV] | implied f_gas |
|---|---|---|
| 1 × 10¹⁴ | 2.12 | 0.223 |
| 3 × 10¹⁴ | 4.41 | 0.384 |
| **6 × 10¹⁴** (archive) | **7.00** | **0.540** |
| 1 × 10¹⁵ | 9.84 | 0.695 |
| 3 × 10¹⁵ | 20.47 | **1.194** |

Cosmic baryon fraction: **0.157**.

`[VERIFIED-BASH]` The only solution with f_gas = 0.1307 lies at
**M ≈ 3.4 × 10¹³ M☉, T ≈ 1.03 keV** — a galaxy group, not a cluster.

Across the entire cluster range the two external relations, combined at the
self-similar slope, imply gas fractions above the cosmic baryon ceiling; at
3 × 10¹⁵ M☉ they imply more gas than total matter.

**The incompatibility is therefore a property of the two published calibrations
at the self-similar slope, not of MULTING.** Any model adopting that pair meets
it. The author met it, resolved it the only way available — lower T₀ until f_gas
is admissible, accept the M–T offset as the cost — and labelled the residue
unresolved. Labelling it was correct.

---

## Finding 3 — the slope is right; only the normalization is in dispute

The archive uses `T ∝ M^{2/3} E^{2/3}`, equivalently `M₅₀₀ ∝ T^{1.5} E^{-1}` —
the standard self-similar form.

Arnaud, Pointecouteau & Pratt 2005 ([astro-ph/0502210](https://arxiv.org/abs/astro-ph/0502210),
A&A 441, 893), abstract verified: at δ = 500 the slope for hot clusters
(kT > 3.5 keV) is **α = 1.49 ± 0.15**, "consistent with the standard self-similar
expectation"; for the whole sample **α = 1.71 ± 0.09**.

The archive's implicit α = 1.5 sits inside the hot-cluster measurement. Nothing
in the functional form is anomalous — the entire dispute is the normalization.

---

## Finding 4 — the direction of the weak-lensing correction is worth checking

The note attributes the ~7 keV comparison to **weak-lensing-calibrated** M–T
relations. Weak-lensing masses run systematically **above** hydrostatic masses for
the same cluster (hydrostatic mass bias). A relation calibrated on WL masses
therefore assigns a **larger** mass to a given temperature, equivalently a
**lower** temperature to a given mass, than a hydrostatically calibrated one.

So moving from hydrostatic to weak-lensing calibration should move the comparison
value **toward** the archive's 3.72 keV, not away from it. If the quoted ~7 keV
came from a hydrostatically calibrated relation, or if the bias direction was
applied the other way, the stated size of the tension would be an overstatement —
against the author's own interest.

`[UNKNOWN]` — **not established.** The normalization could not be retrieved:
A&A returns HTTP 403 to automated requests and the arXiv abstract carries slopes
only. The "~7 keV" figure remains the archive's own unverified claim, and this
finding is a direction-of-effect argument, not a recomputation.

---

## Coupling to the closed bridge candidate

`T(z)` is computed from `M(z)` through the self-similar relation, so the question
left open there — **does `M(z)` track one node's growth, or the characteristic
mass of the node population?** — propagates here unchanged. Under the second
reading the whole f_gas argument would need restating, because a population
characteristic mass and a single halo's gas fraction are different objects.

And Finding 1 sharpens that question: with T₀ shown to be dependent,
`M₀ = 6 × 10¹⁴ M☉` — round, and labelled in the archive itself as "Theoretical
input; not independently data-grounded" — is now the least constrained quantity in
the chain, not T₀.

---

## Epistemic summary

| statement | status |
|---|---|
| T₀ is determined by M₀ + f_gas + Ramos-Ceja, to four figures | **[VERIFIED-BASH]** |
| At T₀ = 6.0 keV the implied f_gas is 0.382, above the cosmic ceiling 0.157 | **[VERIFIED-BASH]** |
| The two external relations admit f_gas ≤ 0.157 only at group scale (~3.4 × 10¹³ M☉) | **[VERIFIED-BASH]** |
| The archive's M–T slope matches APP05's hot-cluster measurement | **[VERIFIED]** — α = 1.5 vs 1.49 ± 0.15 |
| A WL-calibrated relation gives a *lower* T at fixed M than a hydrostatic one | **[INFERRED]** from the sign of hydrostatic bias |
| The "~7 keV" comparison value | **[UNKNOWN]** — normalization not retrievable from accessible sources |
| The tension is intrinsic to MULTING | **[FALSIFIED]** — it is a property of the two external calibrations |

---

## What would resolve it

Not a computation. Two questions, in order of how much they would change:

1. **Which M–T normalization is the ~7 keV from**, and is it hydrostatic or
   weak-lensing calibrated? If hydrostatic, the stated tension is larger than the
   consistent comparison warrants.
2. **What is `M₀` supposed to be?** With T₀ shown to be dependent, the round
   6 × 10¹⁴ M☉ carries the freedom that the note attributes to T₀.

Both are for the author, when the standing pause ends. Neither is a run.

## Artifacts

Computations inline in this session against the archive's unmodified
`multing_core.py`; the f_gas inversion uses `scipy.optimize.brentq` on the
archive's own `Mgas_of`.
