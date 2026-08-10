# The two kinematic bridges want incompatible cluster mass histories

**Date:** 2026-08-10 · **Target:** Zenodo 10.5281/zenodo.21204955
**L0:** Mechanistic / counterfactual model comparison — the intervention is on a
rule inside the forward model, not on a physical variable of the observed
universe. `Δχ²` is a model-comparison contrast, **not** a causal effect estimated
from observations.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

---

## Question

`multing_core.addot_over_a` computes `A = F_total/((M/2)·d)` and declares it equal
to `−Ḣ`. Its own docstring is explicit that this is **not** `s̈/s`, and separately
records `s̈/s = H² − A`. So there is no bookkeeping error: the archive knows the
distinction.

What is missing is the derivation. Since `d(z) = d₀(1+z)⁻¹` is *exactly*
proportional to the scale factor (verified numerically), `ḋ/d ≡ H` and
`d̈/d = Ḣ + H²`. An object of the form `F/(μd)` is structurally `s̈/s` if
`F = μ s̈`. Identifying it with `−Ḣ` instead is an unstated dynamical postulate.
The project's reading of the archive's dialogue log records the author's own
note that the translation formula is "not independently derived and is a
rearrangement of FRW".

Two implementable bridges follow from the same force history:

```
Model K  (archive)        dH²/dz = 2·A/(1+z)              A = −Ḣ
Model M  (literal)        dH²/dz = 2·(H² − A)/(1+z)       A = d̈/d = Ḣ + H²
```

K is a quadrature; M is an ODE. Both are anchored identically at
`H(z_SH0ES) = H0_anchor`.

---

## Positive control on the implementation

Feeding Model M the analytic `ä/a` of flat ΛCDM must return flat ΛCDM `H(z)`.

| version | max relative error |
|---|---|
| first attempt, `atol = 1e-30` in SI | **1.0 × 10⁻³ — FAILED** |
| dimensionless `y = Y/Y_ref`, `atol = 1e-14` | **2.8 × 10⁻¹³ — passed** |

`Y = H²` in SI is of order `5 × 10⁻³⁶`, so the first absolute tolerance sat
2 × 10⁵ times **above** the quantity being integrated and the solver returned
plausible garbage. It was caught only by this control. The conclusions turned out
to be unchanged by the fix (χ² 51.94 → 52.02), but that could not be known before
fixing it, and is not a reason to have skipped it.

Both later anchors reproduce independently: χ²_M(p = −1.1) = **52.02** matches this
project's own earlier run, and χ²_M(p = −0.815) = **23.20** matches an external
reviewer's independent implementation to two decimals.

---

## Phase 1 — same force history, same β, no refit

| | Model K | Model M |
|---|---|---|
| q(0) | **−1.404** (accelerating) | **+0.437** (decelerating) |
| turning point | z = 0.096 | z = 0.442 |
| H(z = 1.07) | 136.4 | 38.5 |
| above z ≈ 1.14 | fine | **H² < 0, no solution** |

Identical forces, opposite cosmology. The translation rule is not a bookkeeping
convention.

## Phase 2 — refit β₁, β₂ under each bridge, p held at −1.1

| | χ²₃₃ |
|---|---|
| Model K, published fit | **15.78** |
| Model M, best refit | **52.02** |
| Δχ² | **+36.24** |

Confirmed by an independent 17×21 grid scan (best 54.18; 163 of 357 nodes
unphysical). Model K's own published region, β₁ ≈ 10¹⁰, admits no Model M
solution at all.

---

## Phase 3 — profile over the mass-evolution exponent, both bridges

`M(z) = M₀(1+z)^p`, archive value `p = −1.1`.

**A coupling the archive lists as two independent inputs.** `assumptions.yaml`
carries `scaling_law_parameters.mass_exponent = −1.1` and, in a separate section
with its own `grounding: theory`, `accretion_correction_parameters.mdot_coefficient
= 1.1`. These are one parameter: `M = M₀(1+z)^p ⟹ Ṁ = −p·H·M`, so the coefficient
**is** `−p`. Verified numerically against the archive's own `m_dot`: relative
difference `0.00e+00`. Any experiment that frees `p` without propagating it into
`Ṁ` is not a self-consistent model; this profile propagates it.

β constrained to be non-negative, as the archive's own fitter does. (A first run
of this profile omitted that guard and reported spurious improvements at negative
β₁ — outside the archive's parameter domain.)

| p | χ² Model K | χ² Model M | β₂/β₂⁰ under M |
|---|---|---|---|
| −0.500 | **unphysical** | 26.78 | 0.027 |
| −0.815 | **unphysical** | **23.20** | 0.150 |
| **−1.100** (archive) | **15.78** | 52.02 | 0.000 |
| −1.500 | 19.79 | 44.68 | 0.000 |
| −2.500 | 209.10 | 28.29 | 0.000 |
| −4.500 | 1019.78 | **19.76** | 0.000 |

### Recoverable fraction

```
R_p = (χ²_M[p=−1.1] − min_p χ²_M) / (χ²_M[p=−1.1] − χ²_K[p=−1.1])
    = (52.02 − 19.76) / (52.02 − 15.78) = 0.890
```

**89 % of the bridge penalty is recoverable by freeing one scaling exponent.**
The binary framing — "if no p reaches 16, the bridge is proven load-bearing" —
is therefore wrong and is withdrawn: most of the 36 units were a property of the
**fixed force-history shape**, not of the translation rule alone.

### The stronger result: the bridges want disjoint regions of p

This is what the two-model control adds, and it is sharper than R_p.

- Model K is narrowly peaked at its published `p = −1.1`, degrades fast away from
  it (19.8 → 209 → 1020) and is **unphysical for p > −1.1**.
- Model M is worst exactly at `p = −1.1` and improves both toward `p ≈ −0.8` and
  toward strongly negative p. Its good regions are where K cannot be evaluated.

The question therefore stops being "which bridge fits better" and becomes
**"what mass-growth history does each bridge require, and is it admissible?"** —
which independent cluster data can answer.

### Phase 4 — the literature bound, and it reverses the expected verdict

A first orientation guess written here — "`p = −4.5` implies a factor ≈ 23 growth
since z = 1, far above ordinary hierarchical assembly, while `p ≈ −0.8` is
unremarkable" — was **wrong**, and is recorded rather than deleted because the
way it was wrong is the finding.

Fakhouri, Ma & Boylan-Kolchin 2010 (MNRAS 406, 2267,
[arXiv:1001.2304](https://arxiv.org/abs/1001.2304)) give the mean halo mass
accretion rate from the two Millennium simulations:

```
<Mdot> = 46.1 Msun/yr · (M/1e12 Msun)^1.1 · (1 + 1.11 z) · E(z)
```

This converts into this archive's parameter directly, and `E(z)` cancels:

```
-p_eff(z) = Mdot/(H·M) = [46.1/(H0·M)] · (M/1e12)^1.1 · (1 + 1.11 z)
```

Integrating `d ln M/dz = p_eff/(1+z)` over the fitted range and fitting the best
single power law:

| M(z=0) | M(2.33)/M(0) | best constant p | RMS in ln M |
|---|---|---|---|
| 10¹⁴ M☉ | 0.099 | **−1.71** | 0.132 |
| 3×10¹⁴ M☉ | 0.078 | **−1.89** | 0.142 |
| 10¹⁵ M☉ | 0.059 | **−2.11** | 0.154 |

**Simulation-supported band: p ≈ −1.7 … −2.1.**

| p | position vs band | χ² Model K | χ² Model M |
|---|---|---|---|
| −0.815 | too shallow | unphysical | 23.20 |
| **−1.100** (archive) | **outside, shallow side** | **15.78** | 52.02 |
| **−1.7 … −2.1** | **← the band** | ~20 → ~100 | ~45 → ~35 |
| −2.500 | slightly steep | 209.10 | 28.29 |
| −4.500 | outside as a constant | 1019.78 | 19.76 |

**None of the three optima falls inside the band, and the archive's own value sits
outside it on the shallow side** — `p = −1.1` matches Fakhouri's z ≈ 0 value for a
light cluster, not the average over the fitted range. The direction in which
Model M improves is *toward* the band, not away from it: at `p = −2.5` Model M
gives 28.3 against Model K's 209.1.

The guess above failed because `p_eff` is **not constant in ΛCDM**: it runs from
−1.33 at z = 0 to −4.30 at z = 2 for a 10¹⁵ M☉ halo, a factor of three across the
very interval being fitted. `p = −4.5` is not exotic at high z; it is only exotic
as a *constant*.

**Therefore the questionable object is the functional form, not the value.**
`M(z) = M₀(1+z)^p` with a single p cannot represent what ΛCDM predicts to within
RMS 0.15 in ln M, so the p-profile compares two bridges on a family that neither
is obliged to fit well. That weakens both the original Δχ² = 36 and the R_p = 0.89
that replaced it.

### Three caveats without which the band must not be quoted

1. **Fakhouri is a ΛCDM N-body result.** Using it to bound a modified-gravity model
   is partly circular. Mitigated — not removed — by the fact that the archive
   already embeds Planck `E(z)` in its own scaling laws.
2. **`M(z)` is ambiguous in the archive.** Growth history of one halo (what
   Fakhouri measures) or characteristic mass of the cluster population at z? These
   are different quantities with different evolution. `assumptions.yaml` says only
   "Theoretical input; not independently data-grounded".
3. Fakhouri reports the **mean** accretion rate; the median is lower and the
   halo-to-halo scatter is large.

---

## Counterfactual: the embedded ΛCDM input

Changing **one** map element, `Ω_m` inside `Efun`, everything else fixed:

| Ω_m in Efun | χ² at published β |
|---|---|
| **0.315** (archive) | **15.78** |
| 0.300 | 32.10 |
| 0.2724 | 134.96 |
| 0.400 | 932.74 |

A 5 % change in `Ω_m` doubles χ² at fixed β. Refitting β at `Ω_m = 0.2724` returns
χ² = 15.24 with β down ≈ 13 %.

**No preference for a freely varying embedded Ω_m is claimed.** Two tested points
are not a likelihood profile, a free `Ω_m` is an extra parameter, and 0.54 units
of χ² would not pay for it under AIC. The finding is the *pattern*: strong
structural sensitivity, strong effective degeneracy after refit — the same shape
found one level down for β₁/β₂.

**Methodological note.** The first version of this counterfactual reported *zero*
effect at every Ω_m. That was a Python default-argument artifact:
`def Efun(z, Om=Om_planck)` binds the default at definition time, so reassigning
`mc.Om_planck` after import does nothing. The intervention had not occurred. Rule
extracted: **a null interventional result requires a manipulation check before it
is interpreted** — prove `X_actual = x₁` before reading `do(X=x₁) − do(X=x₀) = 0`.
Proposed for the causal-provenance gates.

---

## Causal map — terminology corrected

An earlier draft used three causal-inference terms too strongly. Corrected:

| earlier | correct |
|---|---|
| `Efun` is a **confounder** | **embedded ΛCDM-conditioned input / model dependence.** Confounding needs defined treatment and outcome with a common cause; this is upstream model dependence. |
| `A` is a **collider** | **deterministic intermediate.** The graph is forces → A → bridge → H, a mediator chain, not X → A ← Y. |
| anchor → z_min is **reverse causality** | **boundary-condition dependence / parameter coupling.** |

```
Planck ΛCDM E(z) ──► T, M_gas, ρ_crit, R, Ṁ ──► F₀,F₁,F₂,F_acc ──► A
                                                                    │
                                        ┌───────── POSTULATE ───────┴────────┐
                                   A = −Ḣ (K)                        A = d̈/d (M)
                                        └──────► H(z), q(z), z_min ◄─────────┘
```

---

## Corrected numeric claim about F₀

An earlier draft stated "F₀ ≤ 1 % of the net at every z". **That is wrong.**

| z | \|F₀\|/gross | \|F₀\|/\|net\| |
|---|---|---|
| 1.965 | 0.058 % | 0.96 % |
| 0.200 | 0.050 % | 3.31 % |
| **0.096** | 0.048 % | **941 %** |
| 0.070 | 0.048 % | 10.63 % |

The ratio to net is not a meaningful quantity: net passes through zero at the
turning point, so the ratio diverges there. Correct statement: **F₀ is ≲ 0.06 % of
the gross force budget** and is dynamically negligible against it.

The rhetorical companion — "the paper is called *Newtonian* but the Newtonian term
is vestigial" — is withdrawn. A title is not a physical test. The substantive
question is the correspondence principle: **is there a controlled limit of the
parameters or scales in which the theory recovers ordinary Newtonian dynamics?**

---

## Historical precedents

Internal analogies do not count; these are external.

| precedent | source | relation |
|---|---|---|
| Jordan vs Einstein frame in f(R): an accelerating solution in one conformal frame need not map to accelerating metric evolution in the other | [arXiv:1701.02381](https://arxiv.org/abs/1701.02381) | **illustration, not direct precedent** — there a definite conformal transformation exists and the dispute is over which metric matter couples to; here two candidate identifications are compared |
| Averaging / backreaction: local equations and averaged expansion dynamics cannot be identified without an explicit coarse-graining; Buchert's scheme yields extra backreaction terms rather than substituting local acceleration into Friedmann | [Buchert, gr-qc/9906015](https://arxiv.org/abs/gr-qc/9906015) | **closer precedent** — the same micro/meso → macro identification problem |
| Paranjape's review of the averaging problem, which finds the corrections **insufficient** to explain late-time acceleration | [arXiv:0906.3165](https://arxiv.org/abs/0906.3165) | cite for the *problem*, never as a successful backreaction explanation |

---

## Epistemic summary

| statement | status |
|---|---|
| The current H(z) implementation is highly sensitive to the choice of kinematic bridge; Δχ² = 36.24 at fixed p | **[VERIFIED-BASH]**, reproduced independently |
| The bridge is load-bearing **in the current architecture** | **[VERIFIED-BASH]** |
| Most of that penalty (R_p ≈ 0.89) is recoverable by one upstream structural change | **[VERIFIED-BASH]** |
| The two bridges require disjoint regions of the mass-evolution exponent | **[VERIFIED-BASH]** |
| `A = −Ḣ` is derived from the claimed mechanics | **[UNKNOWN]** — per the author's own log, not derived |
| A mechanically consistent MULTING is impossible | **[UNKNOWN]** — never tested; only one force form was varied |
| The ΛCDM-simulation band for a constant p is −1.7 … −2.1 | **[VERIFIED-BASH]** from Fakhouri+2010, subject to the three caveats above |
| The archive's p = −1.1 lies outside that band, shallow side | **[VERIFIED-BASH]** |
| p ≈ −4.5 is excluded by independent cluster data | **[FALSIFIED as stated]** — it is ordinary at z ≈ 2; only exotic as a *constant* |
| A single power law can represent ΛCDM mass growth over 0 < z < 2.33 | **[FALSIFIED]** — RMS 0.15 in ln M; p_eff runs −1.33 → −4.30 |
| What `M(z)` denotes — one halo's history, or the population's characteristic mass | **[UNKNOWN]** — **now the load-bearing question, and it is not a computation** |

---

## Next step — a question, not a calculation

The p-profile has gone as far as it usefully can. Both the original Δχ² = 36 and
the R_p = 0.89 that replaced it are conditioned on a one-parameter family that
ΛCDM itself does not obey over this redshift range, so pushing the profile finer
would refine a comparison whose baseline is the problem.

What decides the next move is a definition: **does `M(z)` track a single node's
mass growth, or the characteristic mass of the node population at redshift z?**
The two carry different literature and different admissible ranges, and the
archive does not say which is meant. Under the first reading Fakhouri+2010 applies
as above; under the second it does not, and the relevant comparison would be to the
evolution of the cluster mass function's characteristic scale.

This is a question for the author, to be raised when the standing pause ends —
not a further run. Recorded here so the p-profile is not repeated in the belief
that more compute will settle it.

## Status

**Candidate closed.** What the bridge question yielded: a measured, twice-reproduced
sensitivity of the published H(z) to an underived translation rule; a decomposition
of that sensitivity showing ~89 % of it is a property of the fixed force-history
shape rather than the rule; and a literature check that placed the archive's own
mass-evolution exponent outside the simulation-supported band while dissolving the
premise that a single exponent is the right object at all.

## Artifacts

`bridge_stress.py`, `p_profile.py` (this folder). Both run against the archive's
unmodified `multing_core.py` and reproduce the published χ² = 15.78 as an anchor
before anything else.
