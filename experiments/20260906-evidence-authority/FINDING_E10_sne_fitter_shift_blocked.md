# FINDING E10 — turning `E6`'s SNe-Ia example from a citation into a
# measurement is BLOCKED on data, and the attempt caught a column
# misidentification that would have produced a wrong number

**Date:** 2026-09-06
**Option 4 of the second option set**, explicit go-ahead given.
**Verdict:** `BLOCKED-INFRASTRUCTURE` in the FL sense — the test could not
run on available data. **Not** evidence against the claim; the claim
(Bengochea 2010; Kessler et al. 2009) stays a citation, unchanged.

## Goal

`E6` grounds its two-field classification in three examples but only one
(`E5`, cosmic chronometers, `+6.80%`) was *measured here*; the other two
are cited. The plan: reproduce the SNe Ia case the same way — same
supernovae, two light-curve fitters, per-object distance-modulus shift.

## The right dataset exists, and its headline is exactly the structure

Kessler et al. 2009, *"First-year SDSS-II Supernova Results"*
(`[VERIFIED-arXiv:0908.4274]`, abstract read this session): the same
288 SNe Ia fit with MLCS2k2 and SALT-II give **`w = −0.76 ± 0.07`** and
**`w = −0.96 ± 0.06`** respectively — a `0.20` shift in the dark-energy
equation of state from the fitter choice alone, ~3σ(stat). The authors
trace it to "a difference in the rest-frame UV model combined with a
different luminosity correction from color variations," and state it
"mostly affect[s] the distance estimates for the SNLS and HST
supernovae" — i.e., **concentrated at high `z`**, where the method is
least calibrated. That is `E5`'s pattern (uniform low-`z` shift,
excursions where calibration is weakest) in a second observable.

## Why the per-object measurement could not be made — and the near-miss

The VizieR table `J/ApJS/185/32/fits` (288 rows, fetched live) merges
Kessler's MLCS2k2 (table10) and SALT-II (table14) fits into one row per
SN and carries **two** distance-modulus columns, `DM` and `DMe`. The
obvious reading — `DM` = MLCS2k2, `DMe` = SALT-II — would have given a
clean per-object shift: `DMe − DM` has mean `−0.110 mag` (`≈ −5%` in
luminosity distance, the same order as `E5`), std `0.162`.

**That reading is wrong, on two independent grounds:**

1. **The CDS ReadMe's own column definition** (fetched):
   `DMe  ?=-9  Distance modulus; LOWZ+SDSS+ESSENCE+SNLS+HST` — a
   distance modulus from a *sample combination*, with `−9` as a
   placeholder for SNe "not included in the sample combination." It is
   not labelled, and is not, the SALT-II modulus.
2. **The redshift trend is the opposite of Kessler's stated mechanism.**
   Kessler puts the fitter discrepancy at high `z`. `DMe − DM` is
   largest at *low* `z` and converges toward zero at high `z`:

   | `z` bin | n | mean `DMe−DM` |
   |---|---|---|
   | `[0.00, 0.10)` | 41 | `−0.200` |
   | `[0.10, 0.25)` | 59 | `−0.161` |
   | `[0.25, 0.50)` | 96 | `−0.128` |
   | `[0.50, 0.80)` | 50 | `−0.025` |
   | `[0.80, 2.00)` | 42 | `−0.010` |

   `corr(z, DMe−DM) = +0.39`. A near-constant low-`z` offset that decays
   at high `z` is the signature of a *different absolute-magnitude /
   `H₀` normalisation convention* between two analyses, not of a
   light-curve-fitter difference. The correlation test with fitter
   parameters was likewise inconclusive (`x1: +0.25`, `c: −0.16`,
   `Av: +0.17`, `Del: +0.02` — no clean SALT-vs-MLCS separation).

**And the reconstruction route is closed too:** deriving the SALT-II
modulus per object needs `m_B` (peak rest-frame `B` magnitude) plus
Kessler's fitted `(α, β, M)`. The 18-column VizieR table has `c` and `x1`
but **no `m_B`**. Without it, no per-object SALT-II μ can be built.

## What would unblock it (named, not run)

- Kessler's original table14 with `m_B`, or their published per-SN μ
  for both fitters (the paper's Fig./Table of Hubble residuals), from
  the journal supplement rather than the VizieR merge; **or**
- a modern equivalent with both fitters' per-object μ published
  side-by-side — Taylor et al. 2023, *"SALT2 versus SALT3"*
  (`[VERIFIED-arXiv:2301.10644]`, found this session), is the natural
  candidate and would also be a more current comparison.

## What this establishes

1. The SNe Ia example in `E6` remains a **citation, not a
   reproduction** — Kessler's own `w = −0.76` vs `−0.96` is the
   quantified statement, and it is theirs.
2. **The near-miss is itself the finding worth keeping.** Had `DMe−DM`
   been reported as "the fitter shift," it would have been a wrong
   number with the right sign and a plausible magnitude — the hardest
   kind of error to catch downstream. It was caught by reading the
   ReadMe's column definition and checking the `z`-trend against the
   source paper's own stated mechanism. This is the third time today
   the same discipline paid off (`E3`: kSZ's full pipeline; `E5`:
   `errHz` excludes SPS by construction; here: a column's actual
   identity), and each time the check was cheap and the mistake it
   prevented was not.

## What this does NOT establish

1. Nothing about the size of the SALT-II/MLCS2k2 per-object shift — not
   measured.
2. Nothing against Kessler et al.'s result, which is quoted from their
   own abstract and not challenged.
3. `BLOCKED-INFRASTRUCTURE` is not `REJECT`: the claim's status is
   unchanged, per `falsification-ladder.md` Step 2a's hard rule.
