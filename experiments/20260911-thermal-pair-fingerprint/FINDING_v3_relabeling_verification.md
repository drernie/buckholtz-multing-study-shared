# FINDING — v3 split-label relabeling: CONFIRMED mechanically,
# WEAKENED by skeptic (the test is close to trivial for its stated purpose)

**Continues:** `FROZEN_PROTOCOL_v3.md` (relabeling logic committed at
`2fb0632`, BEFORE `apply_v3_relabeling.py` was run) → the script's
actual run, recomputing v1's and v2's conditions directly from each
test's own cached real-data extraction.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## 0. What kind of result this is

Per `FROZEN_PROTOCOL_v3.md` §0: this is **not** a new blind real-data
test — v1's and v2's numbers were already known. What was genuinely
pre-committed was the split-label RELABELING LOGIC itself, fixed in
writing and git-committed before the mechanical recompute script ran.

## 1. Reproducibility check (a free byproduct, not the main result)

`apply_v3_relabeling.py` recomputed both cases' raw and detrended
pairwise tables directly from `data_cache/extracted_temperatures_
srcfree_cache.npz` and `data_cache/extracted_temperatures_desi_v2_
cache.npz` — independently of `final_frozen_test.py` / `final_frozen_
test_v2.py` (no shared code, only shared library imports). Every number
reproduced **exactly** to the printed precision against `FINDING_
frozen_test_v1_result.md` and `FINDING_frozen_test_v2_result.md`'s own
tables (e.g. v1 r=592.9: -13.2449/-4.23 both places; v2 r=3849.1:
-173.2238/-2.23 both places). This is a real, if minor, confirmation
that the pipeline is deterministic and the two original FINDING files'
published numbers were not transcribed incorrectly.

## 2. The relabeling result

```
v1: cond1=True  cond2=True  peak_at_max_r=True  detrend_below_floor=True
    -> REJECT-SUBSTRATE-SYSTEMATIC
v2: cond1=False cond2=True  peak_at_max_r=False detrend_below_floor=True
    -> NULL-BELOW-DETECTION-THRESHOLD

predicted (pearl_registry, 2026-09-12): v1=REJECT-SUBSTRATE-SYSTEMATIC,
                                         v2=NULL-BELOW-DETECTION-THRESHOLD
actual:                                 v1=REJECT-SUBSTRATE-SYSTEMATIC,
                                         v2=NULL-BELOW-DETECTION-THRESHOLD
MECHANICAL VERDICT: CONFIRMED
```

## 3. Independent skeptic review (Step 8a, context-blind)

Given only `FROZEN_PROTOCOL_v3.md` §2/§3's criteria and the actual raw
script output (no session reasoning). **Verdict: WEAKENED.**

The skeptic independently re-derived all four condition values for both
cases from the raw numbers and confirmed the labels follow correctly
from §2's logic as written, with no bin-indexing ambiguity — the
mechanical CONFIRMED verdict itself is not in question.

**The substantive point:** the test is close to trivial for what it
claims to validate. v1 and v2 diverge already at the very first gate
(condition 1: raw |z| ≥ 3) — v1's small-r bins are |z|≈4, v2's are
|z|<2, a ~2× gap. Because of this, **v2's verdict is decided entirely
by the first `if` branch** (`NOT(cond1 AND cond2)`) — the peak-bin
identification and detrend-below-floor computation are printed for v2
but never actually influence its label, since the function returns
before reaching that branch. Independently re-checked in
`apply_v3_relabeling.py`'s own `apply_v3_label()`: confirmed true — v2
short-circuits on the first line.

So the "artifact-shape" half of §2's logic (the joint systematic-
detector: peak-at-max-r AND detrend-below-floor) was exercised by
exactly **one** case (v1), and never had to discriminate
`REJECT-SUBSTRATE-SYSTEMATIC` from a counter-example — a hypothetical
case where condition 1 passes (real raw signal) but the shape is NOT
the specific artifact pattern (peak not at the largest bin, or detrend
does not collapse it). No such case exists yet in this branch's own
real-data results. The skeptic's own words: *"'CONFIRMED' here
demonstrates that (i) v1 and v2 land on opposite sides of a signal/
no-signal cut, and (ii) SS2 doesn't crash. It does not test whether the
artifact-shape half of SS2 ... correctly discriminates a case-A from a
case-B when the raw |z| levels are comparable. That test hasn't been
run."*

**Response (Step 8a matrix):** this concern is **accepted as a
documented limitation**, not dismissed and not fixed by fabricating a
third case. It is genuinely true given only the two real-data results
this branch has produced so far, and it correctly narrows what
"CONFIRMED" can be read to support.

## 4. What this DOES support

- The split-label scheme (`FROZEN_PROTOCOL_v3.md` §2), applied
  mechanically and without reinterpretation, correctly separates a
  clean non-detection (v2) from a case with real raw signal that
  matches a known systematic shape (v1) — the two labels are honestly
  named for what actually happened in each case, not just mechanically
  self-consistent.
- The underlying pipeline (beam correction, MAD outlier flag, pairwise
  estimator, quadratic detrend) is independently confirmed reproducible
  byte-for-byte from each test's own cached extraction.

## 5. What this does NOT support

- **Does not validate the joint systematic-detector's discriminating
  power** — whether it correctly separates `REJECT-SUBSTRATE-SYSTEMATIC`
  from `PROMOTE`/`INCONCLUSIVE` when condition 1 genuinely passes but
  the shape is NOT the known artifact pattern. No case in this branch's
  real data has tested that branch of the logic against a
  counter-example.
- **Does not change v1's or v2's own frozen verdicts** — those stand
  exactly as recorded in their own FINDING files.
- **Not a new physics or MULTING claim** — per `FROZEN_PROTOCOL_v3.md`
  §0, this is a methodology consistency check, L0 descriptive.

## 6. Status

**v3 relabeling: CONFIRMED mechanically, WEAKENED by skeptic — accepted
as a documented limitation.** The split-label vocabulary
(`FROZEN_PROTOCOL_v3.md` §2) is adopted as the standard for any future
real, blind frozen test on this branch (a hypothetical v4), with the
explicit caveat that the artifact-shape-discriminating branch remains
genuinely untested against a counter-example — recorded as a new
pearl_registry entry (below) rather than left implicit.
