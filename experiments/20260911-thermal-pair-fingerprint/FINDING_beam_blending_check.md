# FINDING — beam-blending check (estimand.md Consistency (d)): checked
# for all 306 real Positivity pairs, not just the 5 illustrated ones —
# the threat is real but small (5/306 pairs, fraction moves 3.978%→3.913%)

**Date:** 2026-09-11
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Artifact:** `beam_blending_check.py` — real code, real output,
`[VERIFIED-run]`.
**Continues:** `FINDING_power_analysis_s_dependent.md` §2/§4's own named
open risk — the Positivity result's closest pairs sit at
`s≈10.5-11.6` Mpc, right against the small-`s` instrumental cut named
in `estimand.md`'s Consistency (d) (CMB-beam blending/deblending),
flagged there as untested.

---

## 1. The check

`ξ_pred(z,s)` uses each real pair's 3D **comoving** separation `s` — but
`s` alone does not say whether two clusters sit close together **on the
sky** (angular separation, what a CMB map / kSZ pipeline actually
resolves, and where blending risk lives) or close together **along the
line of sight** (small radial separation, large angular separation, no
blending risk at all). This script computes the REAL angular separation
(great-circle, from each pair's own real RA/Dec) for the 5 pairs
`FINDING_power_analysis_s_dependent.md` §2 named, and compares against
ACT-DR5's own stated beam FWHM — `2.2` arcmin (98 GHz) and `1.4` arcmin
(150 GHz), `[VERIFIED-arXiv:2406.14754]`, from the SAME catalog paper
this project's real-position pipeline is built on (fetched directly
from the paper's own text this session, not recalled).

## 2. The 5 named pairs: all safely resolved

| z | s (Mpc) | angular sep. (arcmin) | / 2.2' beam | verdict |
|---|---|---|---|---|
| 0.574 | 10.49 | 15.343 | 6.97× | resolved |
| 0.277 | 11.19 | 23.431 | 10.65× | resolved |
| 0.436 | 11.04 | 12.240 | 5.56× | resolved |
| 0.542 | 11.33 | 14.844 | 6.75× | resolved |
| 0.477 | 11.56 | 21.104 | 9.59× | resolved |

**All five sit at 5.6×-10.7× the conservative beam FWHM — no blending
risk for the specific pairs illustrated in the Positivity headline.**
A same-`s` diagnostic (§4 of the script) shows why: their real angular
separation is `56%-99%` of what it would be if their entire `10-11` Mpc
separation were purely transverse — these are not near-radial
alignments that only look close in projection; they are genuinely
separated on the sky by `10-11` Mpc worth of real transverse distance,
which subtends tens of arcminutes at `z~0.3-0.6`, comfortably above the
beam.

## 3. The nearby population base rate (§3 of the script) — a real,
## if slightly misleading, first look

Before checking all 306 pairs directly (§3a below), the script first
looked at the base rate among ALL real pairs at small `s` (not
restricted to the Positivity set) — a different, more mixed picture:

| `s` cut | N pairs | median ang. sep | min ang. sep | frac. `<1×` beam | frac. `<2×` beam |
|---|---|---|---|---|---|
| ≤11 Mpc | 22 | 11.02' | 1.43' | 18.2% | 22.7% |
| ≤12 Mpc | 27 | 12.24' | 1.43' | 14.8% | 18.5% |
| ≤15 Mpc | 40 | 13.98' | 1.43' | 12.5% | 15.0% |
| ≤20 Mpc | 63 | 15.96' | 1.43' | 9.5% | 11.1% |

**~1-in-5 real pairs at `s≤11` Mpc has real angular separation below
the beam FWHM.** This base rate is real, but — as §3a below shows
directly — it substantially OVERSTATES the risk to the actual
Positivity set, because it only looks at small `s`, and `s` alone
(as §4 already showed for the 5 illustrated pairs) does not determine
angular separation: many small-`s` pairs are mostly radial, not
transverse, and so pose no blending risk despite small `s`.

## 3a. [ADDED, full check] All 306 real pairs behind the Positivity
## fraction — checked directly, not estimated from a base rate

Rebuilt the exact `306`-pair Positivity set (`xi_pred(z,s) > ξ_crossing`,
full `s∈[10,160]` Mpc population, `7693`-pair pool) and computed real
angular separation for **every one of them**, not the 5 illustrated
ones — internal consistency check passed first: **`306/7693 = 3.978%`,
exactly matching `FINDING_power_analysis_s_dependent.md`'s own number.**

| | count | fraction of the 306 |
|---|---|---|
| angular sep `< 1×` beam (genuine blending risk) | 3 | 1.0% |
| angular sep `< 2×` beam (marginal or worse) | 5 | 1.6% |
| angular sep `≥ 2×` beam (resolved/marginal-safe) | 301 | 98.4% |
| angular sep `≥ 5×` beam (comfortably resolved) | 286 | 93.5% |

Angular separation across the 306: `min=1.804'`, `median=44.329'`,
`max=157.410'`.

**Blending-risk-excluded Positivity fraction: `301/7693 = 3.913%`**
(dropping pairs below `2×` beam) — versus the original, unfiltered
`3.978%`. **A `1.6%` relative reduction, not a collapse.** The
beam-blending threat is real (`5` real at-risk pairs exist) but small
in its actual effect on the headline Positivity result — the earlier
population base-rate (§3, `~18-23%`) was a real but substantially
over-pessimistic proxy, because it did not account for the
radial-vs-transverse split §4 (5-pair version) already demonstrated.

**The 10 closest-to-beam pairs among the 306**, for direct inspection:

| z | s (Mpc) | `ξ_pred` | ang.sep (arcmin) | / 2.2' beam |
|---|---|---|---|---|
| 0.450 | 16.19 | `9.362e-8` | 1.804 | 0.82 |
| 0.427 | 14.47 | `1.051e-7` | 1.933 | 0.88 |
| 0.399 | 29.14 | `5.241e-8` | 2.090 | 0.95 |
| 0.276 | 38.38 | `4.075e-8` | 2.998 | 1.36 |
| 0.490 | 37.17 | `4.055e-8` | 3.218 | 1.46 |
| 0.568 | 36.16 | `4.129e-8` | 5.232 | 2.38 |
| 0.599 | 15.54 | `9.577e-8` | 5.491 | 2.50 |
| 0.319 | 14.59 | `1.062e-7` | 7.035 | 3.20 |
| 0.547 | 34.93 | `4.284e-8` | 7.368 | 3.35 |
| 0.792 | 24.47 | `5.990e-8` | 7.399 | 3.36 |

Note the 3 genuinely at-risk pairs (ratio `<1`) are **not** among the 5
illustrated in §2 — the "5 closest by `ξ_pred`" and the "closest to
beam" sets are different, exactly because `ξ_pred` is driven by 3D `s`
alone while blending risk is driven by the angular (transverse-only)
component.

## 4. What this does NOT establish

1. `estimand.md`'s Consistency (d) threat is now checked directly
   against all 306 real pairs behind the Positivity fraction, not
   estimated from a base rate — but "checked" is not "zero risk": 5 of
   306 pairs (1.6%) remain genuinely at or near blending risk, and
   removing them changes the headline fraction only slightly
   (`3.978%→3.913%`).
2. Is a real angular-separation check, not a simulated CMB-map check —
   it establishes GEOMETRIC proximity to the beam scale, not that
   blending actually corrupts the source paper's own `τ_ML`/velocity
   pipeline at that separation (that pipeline's own handling of close
   pairs, if any, has not been read).
3. Not a claim about MULTING (`NO_AUTHOR_ERROR`) — entirely about
   whether this project's own real-position analysis is contaminated by
   an instrumental effect.

## Status

**Fully checked, not just partially — the threat is real but small:**

```
5 named Positivity-driving pairs:  CLEARED, 5.6x-10.7x beam FWHM
Population base rate at s<=11 Mpc: ~18-23% at real risk (over-pessimistic
                                     proxy, does not account for radial
                                     vs. transverse split)
Full 306-pair Positivity set:      CHECKED directly -- 5/306 (1.6%) at
                                     real risk (<2x beam), 3/306 (1.0%)
                                     genuinely below beam FWHM
Blending-risk-excluded fraction:   301/7693 = 3.913% (was 3.978%) --
                                     a 1.6% relative reduction, not a
                                     collapse of the Positivity result
```

Next, if this branch continues: no further action on THIS threat is
required before the sign-near-crossing PROMOTE sub-check and the
synthetic four-world battery — Consistency (d) is now a quantified,
small correction, not an open unknown.
