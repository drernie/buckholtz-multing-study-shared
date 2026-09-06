# FINDING E9 — the provenance-audit tool applied to v82's full input
# chain: of 10 inputs, 1 has a quantified, propagatable systematic,
# 2 are circular (both TJB's own diagnoses), 6 are declared but
# unmeasured, 1 is clean

**Date:** 2026-09-06
**Script:** `E9_provenance_audit_v82_chain.py` (runs `src/provenance_audit.py`
over the chain mapped in `FINDING_E4`)
**Option 3 of the second option set**, explicit go-ahead given.

## What this is and is not

An *application* of the tool built in the first option set to the real
chain — not a new measurement. Every `incurred` entry is sourced to a
`FINDING` (`E2`, `E5`, `E6`, `E8`) or to a v82 line number. Where v82
names a dependency but no one has measured it, `magnitude_pct=None` is
deliberate: the tool's `UNQUANTIFIED` verdict *is* the honest state.

The model under test is `H(z)` — the bridge exists to produce it
bottom-up — so any input that already assumes an expansion history is
circular with respect to it.

## Result

```
Steps: 10        ISSUES: 9        undeclared: 0
  CIRCULAR      = 2
  OUTSIDE_SIGMA = 1
  UNQUANTIFIED  = 6
  clean         = 1  (SH0ES: dependency quantified AND in its quoted sigma)
```

| input (v82's own class) | verdict | basis |
|---|---|---|
| cosmic chronometer `H(z)` (Class I) | **OUTSIDE_SIGMA** — SPS `8.91%`, correlated, not in `errHz` | `E5` measured, `E8` propagated |
| gas mass `M_gas` (Class I) | UNQUANTIFIED — X-ray scaling calibration | v82 grounds it in data, gives no budget |
| ICM thermal energy `k_X` (Class I) | UNQUANTIFIED — same calibration | v82.md:566-569 |
| temperature `T_keV`, Eq.14 (Class II) | UNQUANTIFIED — self-similar assumption | v82.md:569, "purely theoretical" |
| mass evolution `m_X(z)`, Eq.10 (Class II) | UNQUANTIFIED — assumed accretion law | v82.md:586-587 |
| separation law, §II.C (Class II) | UNQUANTIFIED — theoretical | v82.md:587-589 |
| node radius `r_X(z)` via `ρ_crit(z)` (Class III) | **CIRCULAR** | TJB's own §II.F; `P199` |
| `H₀,anchor` via peculiar velocities (§IV.M) | **CIRCULAR** | TJB's own §IV.M; `E2` |
| SH0ES anchor | **clean** — `1.4%`, in quoted `σ` | `E8`: carries `+22.03` of the `21.2` gap |
| DESI Ly-α BAO | UNQUANTIFIED — `r_d` provenance not stated in v82 | `E6` example 3 |

## What the table shows that the hand-mapping in `E4` did not make visible

`E4` sorted inputs into TJB's three classes. This run adds the second
field, and the second field is where the information is:

1. **Class I is not one thing.** Three inputs share the label. One (CC)
   has a *measured, published* dependency that is `100%` correlated
   across bins and absent from its error bar — and `E8` showed it
   changes a conclusion (`4-7.6×` on the degeneracy). Two (gas mass,
   thermal energy) have a *declared* dependency nobody has sized. The
   label "data-proximate" is true of all three and says nothing about
   this difference.
2. **"Unquantified" is the modal state.** Six of ten inputs carry a
   dependency v82 itself names and no one — v82 or this project — has
   put a number on. That is not a criticism of v82, which is unusually
   explicit about naming them; it is a statement about where the work
   is. `E5` sized exactly one of these (CC) and it took Moresco's
   published tables to do it.
3. **The two CIRCULAR verdicts are re-derivations, not discoveries.**
   Both were found, named, and published by TJB. The tool reproducing
   them from declared inputs is a positive control on the tool, and
   nothing more.
4. **The one clean input carries the model gap.** SH0ES is the only
   step whose dependency is both quantified and inside its quoted
   uncertainty — and `E8` found it supplies `+22.03` of the `21.2` χ²
   gap versus fixed Planck ΛCDM. Cleanest input, largest lever.

## What this does NOT establish

1. Does not size any of the six `UNQUANTIFIED` dependencies. Each is a
   separate, real piece of work; the tool's job is to keep them visible
   as blanks, not to fill them.
2. Does not assert v82 *should* have quantified them — v82 names them,
   which is more than most bottom-up constructions do.
3. The DESI `r_d` entry reflects that v82 does not state the sound-
   horizon provenance, not that it is wrong to use the point.
4. `NO_AUTHOR_ERROR`. Both circular items are TJB's own published
   findings; the tool's output on them is a check on the tool.
