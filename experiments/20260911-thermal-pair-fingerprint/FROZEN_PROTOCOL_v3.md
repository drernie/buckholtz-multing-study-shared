# FROZEN PROTOCOL v3 — split-label verdict vocabulary, mechanically
# verified against v1's and v2's own already-frozen numbers

**Written and committed BEFORE `apply_v3_relabeling.py` is run.** Per
this project's own Falsification Ladder (Step 2b) discipline, the
RELABELING LOGIC below is fixed in writing first, so its mechanical
application cannot be tuned after seeing whether it reproduces the
pearl_registry's own falsifiable prediction.

**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

---

## 0. Honest framing — what kind of test this is and is not

**This is NOT a new blind real-data test.** v1's and v2's own numbers
are already known to this session (`FINDING_frozen_test_v1_result.md`,
`FINDING_frozen_test_v2_result.md`) — the "freeze before look" property
that made v1/v2 genuine evidence about the raw data does not apply here
in the same way, because the raw data outcome is not unknown.

**What IS a genuine pre-commitment here:** the split-label RELABELING
SCHEME itself (§2 below), fixed in writing and committed before
`apply_v3_relabeling.py` runs. That script recomputes v1's and v2's
conditions directly from each test's own cached real-data extraction
(`data_cache/extracted_temperatures_srcfree_cache.npz`,
`data_cache/extracted_temperatures_desi_v2_cache.npz`) — not by
retyping numbers from the FINDING files — so the check is a genuine
mechanical consistency check on the METHODOLOGY, not a hand-verified
claim.

**L0 (EstimandOps) classification: descriptive.** The question is "does
this corrected label scheme, applied mechanically and without
reinterpretation to two already-known cases, discriminate them the way
it was designed to?" — not a causal or predictive claim about kSZ
physics or MULTING. Nothing here changes v1's or v2's own verdicts,
which stand exactly as frozen.

## 1. Motivation — the two pearl_registry entries this closes

- **2026-09-12, source `FINDING_frozen_test_v1_result.md`:** the v1
  skeptic proposed a joint REJECT clause (`peak at largest-r bin AND
  detrended |z| < 2`) — already adopted into `FROZEN_PROTOCOL_v2.md`
  §2's systematic-detector, not repeated here.
- **2026-09-12, source `FINDING_frozen_test_v2_result.md`:** the v2
  skeptic (independently, and matching what I had already noticed
  before asking) flagged that `REJECT-MEASUREMENT-SUBSTRATE` conflates
  two logically different findings under one label: "a positively-
  detected systematic pattern" (v1's own case — the joint detector
  fires) vs. "no significant signal anywhere" (v2's own case — raw
  condition 1 fails outright). **This entry's own falsifiable
  prediction is what §3 below tests.**

## 2. The split-label scheme (replaces v2 §2's single
## `REJECT-MEASUREMENT-SUBSTRATE` label; conditions 1, 2, the joint
## systematic-detector, and 4' are UNCHANGED from `FROZEN_PROTOCOL_v2.md`)

```
IF NOT (condition 1 AND condition 2):
    VERDICT = NULL-BELOW-DETECTION-THRESHOLD
    (no significant, correctly-signed raw small-r signal at all --
    a plain non-detection, independent of whether the data shows any
    particular shape)

ELIF joint systematic-detector fires
     (peak |p_pair| bin == largest-separation bin
      AND detrended |z| < 2 in the 2 smallest-r bins):
    VERDICT = REJECT-SUBSTRATE-SYSTEMATIC
    (a genuine detection is not established, AND the shape positively
    matches a known systematic signature -- distinct from a plain
    non-detection)

ELIF condition 4' (detrended |z| >= 2 in the 2 smallest-r bins) passes:
    VERDICT = PROMOTE
    (unchanged from v2 -- conditions 1, 2 pass, the systematic-detector
    does not fire, and the signal survives detrending)

ELSE:
    VERDICT = INCONCLUSIVE
    (conditions 1-2 pass, the systematic-detector does not fire, but
    the signal does not yet clear the post-detrend floor either --
    unchanged from v2)
```

Conditions 1, 2, the systematic-detector, and 4' are copied verbatim
from `FROZEN_PROTOCOL_v2.md` §2 — no threshold, bin count, or pipeline
step is changed. The only change from v2 is that the single fused
`REJECT-MEASUREMENT-SUBSTRATE` outcome is now split into two outcomes
depending on WHICH branch fired.

## 3. Falsifiable prediction (verbatim from pearl_registry 2026-09-12)

> A v3 protocol that splits the fused verdict into two labels...
> should, applied retroactively as a pure re-labeling (no new data, no
> criteria-value change) to both v1's and v2's already-frozen numbers,
> produce v1=REJECT-SUBSTRATE-SYSTEMATIC and v2=NULL-BELOW-DETECTION-
> THRESHOLD — two visibly different, more informative labels instead of
> the same fused one both currently share.

**CONFIRMED** if `apply_v3_relabeling.py`, recomputing both cases
mechanically from their own cached extractions, produces exactly this
pair. **REFUTED** if it does not (e.g. both get the same label, the
labels are swapped, or either case's underlying conditions 1/2/detector
recompute differently from the values already published in the two
FINDING files — which would itself indicate the pipeline is not as
reproducible as assumed, a separate and more serious finding).

## 4. What this protocol does going forward

If CONFIRMED, this split-label vocabulary (§2) replaces
`FROZEN_PROTOCOL_v2.md` §2's single `REJECT-MEASUREMENT-SUBSTRATE`
label as the standard for any future real, blind frozen test on this
branch (a hypothetical v4) — the underlying pipeline, thresholds, and
bin logic are unchanged; only the REJECT-side vocabulary is split.

## 5. Skeptic pass

Same discipline as v1 §4 / v2 §5 — an independent context-blind
`Agent(skeptic)` review of `apply_v3_relabeling.py`'s actual output
against this file's own §2/§3, before the CONFIRMED/REFUTED verdict is
reported as final.
