# FINDING — frozen test v2 (DESI LRG holdout): REJECT-MEASUREMENT-
# SUBSTRATE via plain non-detection, NOT via the v1 artifact pattern

**Continues:** `FROZEN_PROTOCOL_v2.md` (criteria + population swap
committed at `dd17f43`, executor at `c79074e`→`c7e040f`, both BEFORE
this result existed) → `final_frozen_test_v2.py`'s actual run.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## Result (real DESI DR1 LRG, N=3214 valid, z∈[0.4,0.8])

| r (Mpc) | raw p_pair | raw z | detrended z |
|---|---|---|---|
| 520.9 | -7.28 | -1.71 | +0.08 |
| 1412.0 | -14.96 | -1.80 | +0.16 |
| 2259.7 | -25.75 | -1.55 | +0.31 |
| 3150.0 | -52.94 | -1.40 | +0.30 |
| 3849.1 | -173.22 | -2.23 | -0.58 |
| 4381.8 | -221.63 | -1.25 | -0.18 |
| 5178.8 | +186.50 | +0.31 | +0.27 |

Raw T distribution: mean **-1.43 µK**, std 116.94 µK (contrast: v1's
ACT-DR5 MCMF gave mean **-49.25 µK** — see interpretation below).

**Mechanical evaluation of `FROZEN_PROTOCOL_v2.md` §2:**
- Condition 1 (raw |z|≥3 in the 2 smallest-r bins): **False** (1.71,
  1.80 — no significant raw signal at all)
- Condition 2 (correct sign): True (irrelevant — condition 1 already
  fails)
- Peak |p_pair| bin: index 5 (r=4381.8, 221.63) — **NOT** the largest-
  separation bin (index 6, r=5178.8, 186.50, which is actually
  *smaller* and even flips sign)
- Joint systematic-detector (peak-at-max-r AND detrended-below-floor):
  **False** — does NOT fire, because peak is not at the largest bin

**VERDICT: REJECT-MEASUREMENT-SUBSTRATE** — reached via the plain
"condition 1 fails outright" branch, **not** via the joint systematic-
detector that was the whole point of v2's design.

## Independent skeptic review

Context-blind `Agent(skeptic)` — criteria + raw numbers only.
**CONFIRMED**, every condition independently re-derived, no arithmetic
or logic error, no bin-identification ambiguity. Also independently
re-checked myself (`audit-verification-gate.md`) before trusting the
agent's own [VERIFIED] — matches.

**The skeptic raised, unprompted, the same imprecision I had already
noticed before asking for review:** the label `REJECT-MEASUREMENT-
SUBSTRATE` fuses two categorically different outcomes under one name —
(a) "a positively-detected systematic pattern invalidates the
measurement" (the joint-detector firing, v1's own shape) vs (b) "there
is no significant signal anywhere to begin with" (plain non-detection,
what actually happened here). The skeptic's own words: *"Case (a) is a
substrate diagnosis; case (b) is a plain null result — the substrate
as such has not been indicted, the effect just isn't there at this
precision."* This is a real naming imprecision in `FROZEN_PROTOCOL_v2.md`
itself, caught before being smuggled past as "the same kind of failure
as v1" — it is not.

## What this DOES support (precisely worded, learning from the v1
## correction earlier today)

- **v1's specific artifact signature (monotonic |p_pair| growth, peak
  at the largest-separation bin) does NOT reproduce on a structurally
  different, non-SZ-selected population.** This is real, structural
  evidence — obtained on genuinely independent data, not a re-diagnosis
  of v1's own numbers — that is **consistent with** (continues to
  support, does not independently prove) the SZ-selection-specific
  explanation for v1's own pattern.
- **The near-zero mean raw temperature (-1.43 µK vs v1's -49.25 µK)**
  is an independent, structurally different piece of corroborating
  detail: a population not selected via ACT's own tSZ decrement shows
  no large systematic offset, consistent with the SZ-selection
  mechanism (not proof — could also reflect other real differences
  between clusters and field galaxies, e.g. typical halo mass).

## What this does NOT support

- **Not a kSZ detection or non-detection in any physically meaningful
  sense.** DESI LRGs are individual field galaxies with typical halo
  masses far below the massive clusters real kSZ stacking analyses
  target (the real Gong/Bean-style detection used 456,803 objects;
  this holdout used 3214 — two orders of magnitude fewer, chosen to
  match v1's sample size for comparability, not for statistical power).
  A non-detection here is expected regardless of whether kSZ is real.
- **Not proof that v1's artifact is *specifically and only* caused by
  ACT-DR5 MCMF's own SZ-selection mechanism.** A structurally different
  population failing to reproduce the same pattern is consistent with
  that explanation, not a controlled isolation of it (no second,
  independent SZ-selected catalog was tested to confirm the pattern
  recurs there too).
- **The verdict label itself is imprecise**, per the skeptic's own
  point above — this REJECT is a null result, not a positive
  identification of a measurement-substrate problem. Future protocol
  versions should split these into separate verdict categories (e.g.
  `NULL-BELOW-DETECTION-THRESHOLD` vs `REJECT-SUBSTRATE-SYSTEMATIC`).

## Status

**v2 holdout complete.** Methodologically informative (v1's specific
artifact shape does not travel to a non-SZ-selected population — a real,
independently-obtained data point supporting, not proving, the earlier
explanation) but not a physics result (population too small, too
low-mass for a real kSZ test). The verdict-label imprecision is recorded
in `pearl_registry/INDEX.md` for a v3 protocol design, not corrected
retroactively here — same no-post-hoc-amendment discipline as v1.
