# FINDING — beam-blending check (estimand.md Consistency (d)): the 5
# named Positivity-driving pairs are safe; the broader population is not
# fully cleared

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

## 3. The broader population: NOT fully cleared, stated honestly

This is not a blanket result — it is specific to the 5 illustrative
pairs. The real population at small `s` tells a different, more mixed
story:

| `s` cut | N pairs | median ang. sep | min ang. sep | frac. `<1×` beam | frac. `<2×` beam |
|---|---|---|---|---|---|
| ≤11 Mpc | 22 | 11.02' | 1.43' | 18.2% | 22.7% |
| ≤12 Mpc | 27 | 12.24' | 1.43' | 14.8% | 18.5% |
| ≤15 Mpc | 40 | 13.98' | 1.43' | 12.5% | 15.0% |
| ≤20 Mpc | 63 | 15.96' | 1.43' | 9.5% | 11.1% |

**Roughly 1-in-5 real pairs at `s≤11` Mpc has a real angular
separation below the beam FWHM** — genuine blending-risk pairs DO exist
in this regime; they simply were not among the 5 pairs the earlier
report happened to print (which were selected by highest `ξ_pred`, not
checked against this threat at the time). `FINDING_power_analysis_s_
dependent.md`'s own `3.978%` Positivity fraction (`306` real pairs
total, not just 5) has **not** been individually vetted against this
check — this script covers the 5 named illustrative pairs plus the
population-level base rate, not all 306.

## 4. What this does NOT establish

1. Does **not** clear `estimand.md`'s Consistency (d) threat in
   general — it resolves it for the 5 specific pairs already printed
   elsewhere, and gives a real base rate (`~9-18%` risk fraction
   depending on the `s` cutoff) for the wider small-`s` population.
2. Does **not** re-run the Positivity fraction with blending-risk pairs
   excluded — the `3.978%`/`306` number in `FINDING_power_analysis_s_
   dependent.md` still includes an unknown number of pairs that this
   check would flag if run on the full set.
3. Is a real angular-separation check, not a simulated CMB-map check —
   it establishes GEOMETRIC proximity to the beam scale, not that
   blending actually corrupts the source paper's own `τ_ML`/velocity
   pipeline at that separation (that pipeline's own handling of close
   pairs, if any, has not been read).
4. Not a claim about MULTING (`NO_AUTHOR_ERROR`) — entirely about
   whether this project's own real-position analysis is contaminated by
   an instrumental effect.

## Status

**Partial resolution — the specific risk named is cleared for the
illustrative pairs, not for the full Positivity population:**

```
5 named Positivity-driving pairs: CLEARED, 5.6x-10.7x beam FWHM
Population at s<=11 Mpc:          ~18-23% at real blending risk (<2x beam)
Full 306-pair Positivity set:     NOT individually checked
```

Next, if this branch continues: extend this exact script (its
`angular_sep_arcmin` function is already general) to all `306` real
pairs behind the `3.978%` Positivity fraction, and report a
blending-risk-excluded Positivity number directly, rather than the
current base-rate estimate. Not done here — the user's request was the
named closest pairs specifically, and this file answers that request in
full.
