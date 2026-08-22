# FINDING P92-probe — **MIN-M-ONLY.** The H-monotonicity hypothesis is refuted; the direction of P92's discrepancy stays unexplained

**Status:** built, run, verdict against pre-registered outcomes.
**Tier:** FL Micro (single hypothesis test on an existing predicate).
**L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `p92_which_clause_probe.py`

---

## The question

P92's `λ=0.1` `n_probe` ladder found that P81's boundary does **not** converge
to the event-located exact flip — it **crosses** it near `n_probe=3000` and
settles `4.136e-07` away, on the side of **smaller** `ĝ` (P81 rejects
*earlier*). The obvious explanation — "a coarse grid steps over a viability
dip" — was ruled out by direction: a sampled minimum is always `≥` the
continuous one, so that mechanism should shift the boundary the other way.

Hypothesis under test: P81's predicate has a **second** grid-dependent clause,
`H` monotonicity (`max(diff(H)) ≤ 1e-9·max(H)`), that a coarse grid cannot
resolve through an oscillation and a fine one can — so raising `n_probe`
**activates** a dormant clause.

## Result — refuted cleanly

**M1, the decisive window** (`λ=0.1`, `ĝ=2.7517642`, strictly between P81's
`n=100000` and `n=3000` boundaries):

| `n_probe` | ok | `min_M` | `H_monotone` | `worst_H_rise_rel` | why |
|---|---|---|---|---|---|
| `300` | True | `0.100351087` | True | `-6.017e-10` | viable |
| `1000` | True | `0.100005425` | True | `-1.762e-10` | viable |
| `3000` | True | `0.100000378` | True | `-5.834e-11` | viable |
| `10000` | **False** | `0.099999774` | True | `-1.746e-11` | `min(1-g*phibar)=0.1<=0.1` |
| `30000` | False | `0.099999712` | True | `-5.816e-12` | `min(1-g*phibar)=0.1<=0.1` |
| `100000` | False | `0.099999702` | True | `-1.744e-12` | `min(1-g*phibar)=0.1<=0.1` |

`H_monotone` is **True at every single point**. `"H not monotone"` never appears
in any `why` string — not at this window, not anywhere.

**M2** confirms it structurally: `worst_H_rise_rel` at every `λ ∈ {0, 0.1, 1, 10}`
is negative (`H` genuinely non-rising) at every `n_probe`, orders below the
`1e-9` threshold, and never crosses it.

**M3** was moot — with M1 and M2 both flat, the negative control had nothing to
discriminate.

→ **MIN-M-ONLY**, exactly the refutation outcome pre-registered in the probe's
docstring. The `min(1-g*phibar)` clause is what binds at every `n_probe`; a
second grid-activated clause is not the mechanism.

## What stays open, recorded rather than chased

Two regularities surfaced in the same run and are worth naming, though neither
is explained here — this was a single hypothesis probe, not a new registered
experiment, and neither thread is pursued further in this file.

1. **`min_M` in M1 decreases monotonically with `n_probe`**, converging to
   `≈0.0999997` — below `FLOOR` — at a `ĝ` that sits *below* the reconstruction's
   exact flip. Same direction as P92's ladder result, seen at a fixed point
   instead of via bisection. Consistent with, not a new explanation of, the
   discrepancy.
2. **M2's `worst_H_rise_rel` is numerically identical across all four `λ`** at
   every `n_probe`, independent of the measured turning-point count (`0`,
   `216`, `332`, `562`). A quantity that does not vary with the oscillation
   structure of the trajectory it is supposedly measuring looks like a
   discretization artifact of the `n_probe` grid itself, not a physical
   signal — but this was not tested here and is not claimed.

## Verdict

**Hypothesis refuted.** The direction of P92's discrepancy — P81's sampled
boundary converging to a *smaller* `ĝ` than the event-located exact flip —
remains **unexplained**. No substitute mechanism is offered.

### Consequence for P91

`FINDING_P91`'s Part 0 verified that `min(1-g*phibar)` is the binding clause
**at the default `n_probe`**. This probe shows that clause remains the binder
across the *entire* ladder, so Part 0's licence to compare is **not** narrowed
by a second clause switching on — that specific concern is closed. The
discrepancy itself, however, is a separate, still-open fact about `P81`'s
predicate that `FINDING_P91`'s `B-CONFIRMED` did not have in hand.

### Not established

- Why P81's sampled boundary crosses and settles past the exact flip.
- Whether the two open threads above share a cause.
- Anything about the shared equations, anything observational. Gate 1 holds.
