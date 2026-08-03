# DRAFT SPECIFICATION v7 — kSZ dipole conditional upper limit

**STATUS: DRAFT. NOT FROZEN.**

**This document is explanatory. It does not govern.** Four machine-readable
files are normative, and where this text and one of them differ, the file wins:

| File | Governs |
|---|---|
| `state_machine.yaml` | terminal states, transitions, tie resolution, empty sets, terminal verbs |
| `reference_config.yaml` | every constant, every library call and its options |
| `output_schema.json` | every reported output: name, shape, dtype, mask, suppression |
| `test_vectors.json` | one regression witness per registered ambiguity |

Every change from v6 is a registered entry in `ambiguity_ledger_v7.md`. No
method, derivation or interpretation is added. Reasoning stays in
`derivations.md`, which is not gated.

**Freeze gate.** A finding blocks the freeze if and only if two implementations,
both compatible with the normative files, could differ in the simulated data, a
kernel, the likelihood, a terminal state, or a reported output. A reader must
supply `Reading A` / `Reading B` / `Affected output`. A reading contradicted by
a normative file is not blocking.

Path: `DRAFT_v7 → LOCAL_STATIC_LINT → SPEC_GATE → DUAL_READER_REVIEW →
COMPUTATIONALLY_FROZEN_v7 → BLIND_C`.

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0: descriptive

---

## 0. Product

A conditional, stat-only, fixed-template 95% upper limit on
`ℓ_d = A₃/A₂ = μ`, in physical Mpc, within one continuum pairwise-kSZ forward
model.

Out of scope and not inferable from any output: any limit on `β_d`; any test of
any preprint figure; any claim about the physical correctness of the principal
value; template-uncertainty propagation; any data-based determination of
`r_lo`; `CL_s` protection; any statement about `μ > mumax`; the absolute unit of
`r_mp`.

Two annotations are attached to reported items — `stat_only_fixed_template` and
`model_support_conditional`. They are **report fields**, declared in
`output_schema.json`, and are never outcome labels.

## 1. Symbols

As v6, with `jj` now running `0 … 600` and the counters re-indexed by stage.
The full list is unchanged in kind; the normative shapes are in
`output_schema.json`.

## 2–8. Inputs, units, ξ, kernels, models, fit, Monte Carlo

Unchanged from v6 in substance, with these registered edits:

- **`gcurve`** (INP-01): column 0 is the abscissa in h⁻¹Mpc and is multiplied by
  `1/hdata`; column 1 is `g`, not `√g`; interpolation is `numpy.interp` onto the
  15 fitted `r_mp` with end-value clamping. See `reference_config.yaml`.
- **Quadrature** (QUAD-01): `IntGK` is `scipy.integrate.quad` with the epsabs,
  epsrel, `limit` and `points` given in `reference_config.yaml`.
  Non-convergence is a computable criterion, not a judgement:
  `ier != 0 or abserr > max(epsabs, epsrel·|result|)`.
- **Counters** (IDX-01): `edge_count[model, rlo, stage, boundary]` and
  `degen_count[model, rlo, stage]`. Every fit increments the bucket of its own
  stage. The `jj` axis is not used off the coarse grid.
- **`mu = 0`** (ZERO-01): evaluated, not assumed. `Qobs(0) = Q95(0) = 0`
  analytically — `Qstat(0)` is zero for every dataset, so no simulation is run
  at that node. `acc(0)` is true. See `state_machine.yaml → zero_node`.

## 9. r_lo scan

Grid and conditional node as v6, in `reference_config.yaml`.

**Monotonicity pairing** (PAIR-01), stated once and only once:

> Excluded nodes remove both comparisons that involve them. The gap is **not**
> closed: if node `kk = 5` is excluded, `kk = 4` and `kk = 6` are not compared.

Exclusion is keyed on whether `L95` is numeric, not on whether a label was
raised. Two lists are reported (LIST-01): `excluded_from_range` and
`excluded_from_monotonicity`.

`range`, `maxViolation` and their empty-set behaviour are governed by
`state_machine.yaml → empty_set_contract`.

## 10. Upper endpoint

**Governed entirely by `state_machine.yaml`.** This section explains it and
adds nothing.

The acceptance vector runs `jj = 0 … 600` with `acc(0)` true by evaluation. Four
states partition every possible vector:

| Condition | State | `L95` |
|---|---|---|
| `acc(600)` true | `RANGE_INSUFFICIENT` | none |
| `acc(600)` false, no positive node accepted | `FINITE_LIMIT_NEAR_ZERO` | bisection on `[0, 0.1]`, may be 0.0 |
| `acc(600)` false, some accepted, one falling transition | `FINITE_LIMIT` | interpolated crossing |
| `acc(600)` false, some accepted, several falling transitions | `FINITE_LIMIT_MULTICROSS` | supremum of the acceptance set, i.e. the crossing at the **last** falling transition |

Refinement may report `REFINEMENT_LOST_CROSSING`. `RANGE_INSUFFICIENT` makes no
claim about `μ > mumax`; a state asserting the absence of a crossing anywhere
would require evaluating beyond `mumax`, which §0 places out of scope.

**Ties** resolve by `argmax_left` — the smallest index among all maximisers —
everywhere in the specification. A total tie over all 601 nodes is reachable
when `muhat = mumax`; witness TV02.

`SdMC` is unchanged from v6 in form. Its bandwidth is written out in
`reference_config.yaml → libraries.kde`, not cited by name.

## 11. Branches

As v6. A branch whose endpoint state carries no numeric `L95` raises
`STOP_BRANCH`: its row stays in the table with the state label in place of
`L95` and `SdMC` (BRANCH-01). The table is always five rows, ordered
`primary, branch_1, branch_2, branch_3, branch_4`.

## 12. Controls

Deviation measures, tolerances and terminal verbs are in
`reference_config.yaml` and `state_machine.yaml`.

**All nine controls run to completion and emit their measured values before any
terminal verb is honoured** (CTRL-02), so output item 8 is always complete.

Two rows changed:

- **Control 5** (CTRL-03) now names both operand pairs explicitly —
  `Kraw3` at 1e-12 against `Kraw3` at 1e-10, and `Kw3` at 1e-12 against `Kw3` at
  1e-10 — so the "second-named quantity" rule of §12.0 does not apply to it. It
  emits **two** values; the verdict is taken on their maximum.
- **Control 6** emits **four** values, one per (kernel, ε) pair, verdict on the
  maximum (CTRL-01).

## 13. Coverage study

As v6, with one registered edit: the threshold `Q95(muTrue)` is **recomputed
under `rootVal`** at `keyStage = 0`, `nsim = 100000` (RNG-01). It is not reused
from the §10 scan. The study owns its threshold.

## 14. Dual-unit run

As v6. Re-expression means the same physical length written in h⁻¹Mpc. Key
fields are index arithmetic and are never re-expressed.

## 15. Outputs

**Governed entirely by `output_schema.json`** — names, shapes, dtypes, validity
masks, row order, and which terminal verb suppresses which item. A label is
never stored inside a float array; every value array has a parallel `state`
array of strings (SHAPE-01).

Item 9's observed-boundary array keeps shape `(2, 11, 2)` and gains
`observed_valid (2, 11)`; slots where a model was not run at an `r_lo` are
masked false and must not be read (MASK-01).

## 16. Standing scope statements

Unchanged from v6. In particular: all eleven `r_lo` values lie strictly between
the first and second tabulated separations of `ξ`, so the `r_lo` dependence is a
dependence on the §4 interpolant over an interval containing no measurement.

**Even a successful review and a successful Blind C establish only:**

```
COMPUTATIONALLY FROZEN
INDEPENDENTLY REPRODUCED
```

The physical status remains **SUPPORT-CONDITIONAL**, and no output of this
procedure changes that.

---

## Appendix — static review questions

Two independent readers answer these from this document **and the four
normative files**, pseudocode only, no numbers, applying the freeze gate above.

1. Which kernels enter which model, and how is `Kraw2` integrated?
2. Where is `1/(1+xi)` applied?
3. Which lengths are converted, where, and which are not?
4. How is the pole integrated, how is the logarithm integrated, and what makes
   the quadrature reproducible?
5. How is a simulated dataset formed — covariance, amplitude, and the exact
   order in which the stream is consumed?
6. What is `Wt`?
7. What is `muhat`, which candidates enter, and how are ties resolved?
8. What is `Qstat`, what is `acc(0)`, and what do the two counters count?
9. Which of the four states applies to a given `acc` vector, and what does each
   report? Is the classification total?
10. What is `SdMC`, in which states is it `NOT_DEFINED`, and what happens to an
    empty `range` or an empty violation set?
11. What are the nine controls, which verb does each raise, in what order do
    they run, and how many values does each emit?
12. What is reported, with what shape, dtype and mask, and what is out of scope?
