# FINDING E5 — switching only the stellar-population model shifts cosmic
# chronometer `H(z)` by a tight, uniform `~+6.8%`; the shift sits INSIDE
# the CC community's own published modelling budget, and neither v82 nor
# this project propagates that budget at all

**Date:** 2026-09-06
**Continues:** `FINDING_E1`-`E4`. Executes option 1 of five development
options ("trace one input to the bottom"), explicit go-ahead given.
**Verification:** every number computed this session from Moresco's own
published tables, fetched live from `gitlab.com/mmoresco/CCcovariance`.

## ⚠️ CORRECTION — this file's first draft over-reached; corrected
## before ever being presented as settled

The first draft led with **"up to `26.5%`"** and **"exceeds its own
`1σ` at `4` of `15` points."** A Step 8a context-blind skeptic pass
attacked both, and **my own follow-up checks confirmed the skeptic on
both counts**:

1. **The `26.5%` headline is carried by two high-`z` points.** The real
   structure is `12` points at a tight, uniform `+6.80%` (spread only
   `0.99` percentage points, range `+4.93%` to `+7.64%`) plus `3`
   negative ones, of which two are large (`z=0.7812`, `z=1.037`).
   Leading with the maximum was cherry-picking the tail.
2. **"Exceeds `1σ`" was a σ-scope error and is WITHDRAWN.** BC03's
   quoted `errHz` is `sqrt(stat² + met²)` — verified directly, matching
   to within `2%` for `13` of `15` points — i.e. it **excludes the
   SPS/modelling systematic by construction**, because that term lives
   separately in `Cov_model`. Comparing an SPS-induced shift against a
   σ that omits SPS is incoherent. Recomputed against an SPS-inclusive
   σ, the count drops from `4/15` to `2/15`.

The corrected result below is **stronger, not weaker**, than the
original headline — a tight directional bias is a better finding than a
large outlier.

## L0 (EstimandOps)

**Question type: descriptive.** What model dependence does the
*cleanest* available cosmological input carry, and is it propagated by
v82 or by this project? Chosen because `FINDING_E4` put the 31-point
cosmic chronometer `H(z)` compilation at **Class I, data-proximate** —
v82's own label, and defensible: the method (Jimenez & Loeb 2002)
measures differential galaxy ages and genuinely assumes no expansion
history. The question is what it assumes *instead*.

## Result 1 — the CC community published its own systematic budget

Moresco et al., **"Setting the Stage for Cosmic Chronometers"**
I (`[VERIFIED-arXiv:1804.05864]`, 2018) and II (`[VERIFIED-arXiv:
2003.07362]`, 2020). The accompanying repository decomposes:

```
Cov = Cov_stat + Cov_syst
Cov_syst  = Cov_met + Cov_young + Cov_model
Cov_model = Cov_SFH + Cov_IMF + Cov_stlib + Cov_SPS
```

**Moresco's own README:** `Cov_met` and `Cov_young` are purely
diagonal, but `Cov_model` "has been conservatively estimated as the
contribution from different redshifts are **fully correlated**." The
modelling part is therefore `100%` correlated across bins — exactly the
regime where treating errors as independent is most wrong.

**His own per-component budget** (`data_MM20.dat`, 29 bins,
`z=0.075-1.475`, percent of `H(z)`):

| component | mean | max |
|---|---|---|
| initial mass function | `0.36%` | `0.47%` |
| stellar library | `6.57%` | `7.40%` |
| **total modelling (SPS incl.)** | **`8.91%`** | `15.86%` |

## Result 2 — the corrected measurement: a tight, uniform SPS offset

Moresco's repository ships **two** `H(z)` tables built from the *same*
galaxy observations (positive control run: all `15` rows carry
**identical** source-paper references and identical redshifts),
differing only in the SPS model: `HzTable_MM_BC03.dat` (Bruzual &
Charlot 2003) vs `HzTable_MM_M11.dat` (Maraston & Strömbäck 2011).

| | n | mean shift | range | spread |
|---|---|---|---|---|
| **positive (M11 > BC03)** | **12** | **`+6.80%`** | `+4.93%` to `+7.64%` | `0.99` pp |
| negative | 3 | `-14.29%` | `-0.64%` to `-26.48%` | — |

**The load-bearing result is the first row:** a `~7%` *directional*
offset, uniform to within one percentage point across `z=0.18-1.97`,
produced by a pure modelling choice with no new observation. That is a
systematic bias, not model noise.

**And it confirms rather than contradicts the community's own numbers:**
`13` of `15` shifts fall inside Moresco's own `8.91%` mean modelling
budget. The two that don't are `z=0.7812` and `z=1.037`.

**The two excursions carry a named, unverified caveat** (raised by the
skeptic, not checked here): both sit at high `z` where the CC method's
own calibration is weakest, and it was not verified from the artifacts
that the fit method was held fixed between the BC03 and M11 re-analyses
at `z>0.7`. If it was not, part of those excursions is method
difference, not pure SPS choice. **The cheap check named but not run:**
read §3-4 of `arXiv:2003.07362` on how the M11 re-analysis was
performed at high `z`.

## Result 3 — neither v82 nor this project propagates any of it

**v82** `[VERIFIED-BASH]`: cites Moresco 2016 `[7]`, Moresco 2015 `[9]`,
Jimenez & Loeb 2002 `[10]` — the *measurement* papers — but has **zero**
occurrences of "covariance", **zero** of "Setting the Stage", and cites
neither systematics paper.

**This project** `[VERIFIED-BASH+code-read]` — and this matters more,
because it is ours to fix:
- `src/cluster_data_pipeline.py:379` fetches from
  `gitlab.com/mmoresco/CCcovariance` — **the covariance repository
  itself** — then reads only `(z, H, σ)` (lines 388-391). We download
  from the covariance source and discard the covariance.
- `src/cluster_data_pipeline.py:402` hardcodes
  `df_hz["FLRW_independent"] = True`, unqualified. True in the sense
  that matters (no assumed expansion history); reads as
  "assumption-free", which Results 1-2 show it is not.
- No covariance handling anywhere in `src/` — every `χ²` uses a scalar
  `sigma_H` sequence.
- **Live-fetch bug found in passing:** the hardcoded path
  `data/CC_Hubble.dat` returns **HTTP 404**; the real files are
  `HzTable_MM_BC03.dat`, `HzTable_MM_M11.dat`, `data_MM20.dat`.
  `raise_for_status()` catches it and the code silently falls back to
  its hardcoded table — nothing visibly breaks, but the "live" path has
  been dead and the fallback is what actually runs.

## What this establishes

The `evidence` / `authority` split is **not binary even for the best
input in the construction.** CC genuinely escapes the assumption it was
designed to escape — Class I is the right label — while carrying a
different, published, `~7%` systematic from stellar-population
modelling that is `100%` correlated across redshift and invisible if
only `errHz` is used. The practical statement, which needs no headline
number: **any analysis treating CC points as independent measurements
with only the `errHz` column is under-quoting model uncertainty by
roughly the size of the point errors themselves.**

## What this does NOT establish

1. **Does not show any v82 result is wrong.** Whether propagating the
   full covariance changes v82's conclusions is a separate, unrun
   computation. Direction is predictable (larger correlated errors
   weaken *all* `χ²`-based discrimination, ΛCDM's included); magnitude
   is not, and it cuts both ways rather than favouring either model.
2. Does not establish that our own `P191`-`P194` Fisher forecasts
   (which assumed `σ=10%`) change materially — flagged, not rerun.
3. **Does not show the CC community is hiding anything** — the opposite.
   Every number here is theirs, published, and this project found it by
   reading their own repository. The finding is "use the covariance
   they told you to use."
4. Does not resolve the two high-`z` excursions' attribution.
5. `NO_AUTHOR_ERROR` — the failure to propagate is documented here for
   **this project's own code first**, where it is directly fixable.
