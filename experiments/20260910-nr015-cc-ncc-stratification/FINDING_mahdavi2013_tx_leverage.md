# FINDING — NR-015's Relaxation Map row 1: no analytic T_X-leverage
# exists in Mahdavi et al. 2013's own pipeline; the empirical M_hydro-T_X
# scaling is strong and consistent with standard self-similar physics

**Date:** 2026-09-10
**Continues:** `null_results/20260718-nr015-tx-shared-variable-artifact.md`'s
Relaxation Map row 1 ("Quantify M_hydro's actual T_X sensitivity — read
Mahdavi et al. 2013's exact HSE derivation, extract effective
`∂ln M_hydro/∂ln T_X` for their specific pipeline").

`NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive`
`NO_AUTHOR_ERROR`

## Primary-source finding that reframes the question

Read arXiv:1210.3689 (Mahdavi, Hoekstra, Babul, Bildfell, Jeltema, Henry
— "Joint Analysis of Cluster Observations II," the real, actual source
paper for the CCCP N=50 catalog used throughout the H1 program) §2.5-2.6
directly. **No algebraic HSE formula (`M_HE ~ -r·kT(r)/(G·μ·m_p)·[...]`)
is used to compute `M_hydro` from a separately-measured `T(r)` in this
pipeline.** Their own words: *"the unprojected temperature profile is
calculated self-consistently assuming hydrostatic equilibrium of assumed
gas and dark matter density profiles... temperature is merely an
intermediate 'dummy' quantity."* The actual free parameters, jointly fit
via MCMC ("Hrothgar") directly to the X-ray spectra, are the gas density
profile (triple-beta model, ~10 parameters), the metallicity profile (3
parameters), and the total-mass NFW profile (`M_Δ`, concentration `c`).
`T_X` is not among the fitted parameters — it is a derived summary of
the same joint posterior that also yields `M_hydro`.

**Consequence for NR-015's own question:** a single, fixed analytic
"leverage" coefficient (as if `M_hydro = f(T_X)` via a known formula)
does not exist for this specific pipeline. `T_X` and `M_hydro` are
correlated PROJECTIONS of one multi-parameter joint fit to the same
spectral data — an even more direct kind of shared-origin relationship
than the simple algebraic-substitution story NR-015 originally
hypothesized, not a weaker one.

## What was actually computed instead: the empirical scaling

Since no formula exists to differentiate, computed the closest available
answer directly from the real catalog (`mahdavi2013_tx_leverage.py`,
`N=50`, positive control: `Abell2390` `M_hydro=11.0` matches the paper's
own published Table 1 value `11.0±0.9` exactly):

| Quantity | Value |
|---|---|
| Raw log-slope `γ = d(ln M_hydro)/d(ln T_X)` | `1.385 ± 0.118` (`r=0.861, p=1.0e-15`) |
| Deviation from standard self-similar (`γ=1.5`, Kaiser 1986) | `z=-0.97, p=0.330` — **consistent with self-similar** |
| Same slope, controlling for `M_WL` (partial) | `γ=1.088 ± 0.135` (`r_partial=0.759, p=1.7e-10`) |

**Reading:** the empirical `M_hydro`-`T_X` relationship in this real
50-cluster sample is strong (raw `r=0.86`) and statistically
indistinguishable from the standard self-similar cluster-scaling
expectation. Even after removing the trivial "more massive clusters have
both higher `T_X` and higher `M_hydro`" confound (controlling for
`M_WL`), a substantial, highly significant relationship remains
(`γ≈1.09`, `r_partial=0.76`).

## What this does and does NOT establish

1. **Does** establish that the `T_X`-`M_hydro` relationship in this
   pipeline is strong and well-quantified, not a weak or marginal
   effect — directly relevant to why `NR-015`'s original partial
   correlation (`r≈-0.70` to `-0.81`) came out as large as it did.
2. **Does NOT** distinguish reading (1) (shared-fit/definitional origin)
   from a genuine, independent self-similar cluster-physics scaling —
   both predict a strong, self-similar-consistent `M_hydro`-`T_X`
   relationship, and per §2.5-2.6 they are not mutually exclusive in
   this pipeline: the joint-fit machinery is *built to reproduce* real
   cluster physics, so a real self-similar relationship and a
   shared-origin statistical entanglement are two descriptions of the
   same underlying fact here, not competing alternatives.
3. **Does** narrow NR-015's own Relaxation Map row 1 from "unrun" to
   "run, and the originally-imagined analytic-formula version of the
   question does not apply to this specific pipeline" — a real,
   substantive answer, not a null result.
4. Does not change `NR-015`'s own CC/NCC-stratification verdict
   (`experiments/20260910-nr015-cc-ncc-stratification/decision.md`) —
   that test's own favoring of reading (1) over reading (2) stands
   independently of this one.
5. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   of Mahdavi et al.'s real, published methodology and the CCCP catalog;
   no claim about MULTING/TJB's own theory.

## Files

- `mahdavi2013_tx_leverage.py` — full computation, positive control,
  `ruff check` clean.
