# CLAIM — M500c vs M200c top-N selection overlap: the concrete, cheap
# kill-criterion named by Step 8a skeptic review of P230 (docs/162's
# own item 3 / item 9)

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b. Kept lean (Structure-Bias Guard) — fully specified by the skeptic's
own kill-criterion in `FINDING_P230_what_physically_is_a_node.md`
Response Matrix item 2.
**Continues:** `docs/162_ontology_spec_v82.md` item 3's own `[OPEN]`
flag ("the practical size of the mismatch... plausibly modest but NOT
quantified"). **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## The question

`docs/162`'s own item 3 flags: v82's own mass/radius convention is
`M500c`/`R500`, but this project's entire prior simulation work
(TNG300, FLAMINGO, Magneticum, the full `27`-subcube saga) used `M200c`
throughout. The skeptic's own physics-based estimate (concentration-
mass scatter, `~0.10-0.15` dex in `log(c)`) predicted a top-`N`
selection overlap of `~90-95%`, not "nearly all" — but this was
`[WEAK]`/`[MEMORY]`-tier (general literature knowledge, not
independently checked against a primary source or real data). **This
test replaces that estimate with a real, direct measurement.**

## Method

FLAMINGO's own real SOAP halo catalog provides BOTH `SO/200_crit/
TotalMass` and `SO/500_crit/TotalMass` for the SAME halos (confirmed
live, `_explore_flamingo_so500_availability.py`) — the cleanest
possible cross-check, no cross-catalog matching needed. Download both
mass fields for a shared top-`5000`-by-`M200c` pool (same as every
prior FLAMINGO script this session). For each of several candidate `N`
(`35, 50, 1200` — spanning the TNG300-subcube scale and this branch's
own "definitive global estimand" `N=1200`): rank by `M200c`, take
top-`N`; separately rank by `M500c`, take top-`N`; compute the overlap
fraction (`|intersection|/N`). Also report the `M500c/M200c` ratio
distribution (mean, scatter) across the shared pool, as a direct,
real cross-check on the skeptic's own `[MEMORY]`-tier concentration-
scatter estimate.

## What this would and would not settle

- **If overlap is `>=95%`** at the `N` values actually used in this
  branch's own prior tests: the `M200c`-vs-`M500c` gap is confirmed
  practically minor for rank-based selection — prior top-`N` samples
  are a good proxy for what an `M500c`-based selection would have
  given, even though the exact mass VALUES differ.
- **If overlap is materially lower** (`<90%`, per the skeptic's own
  prediction, or lower): confirms a real, non-trivial selection-level
  sensitivity — any FUTURE test in this branch should select by
  `M500c` directly, not `M200c` with an assumed-safe rank-preservation.
- **Either way**: does NOT retroactively invalidate any already-
  reported correlation number (those remain what they measured) — only
  informs how much weight to place on "an `M500c`-based re-selection
  would likely give similar results."
- **Does NOT** address the separate, larger `docs/162` item 9
  question (2PCF-style estimand vs. nearest-neighbor) — this is
  narrowly scoped to the mass-DEFINITION sub-question only.
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked: (a) is the
overlap computation itself correct (no off-by-one/self-match bugs),
(b) does the reported ratio distribution's scatter roughly match the
`[MEMORY]`-tier literature estimate this test was designed to replace,
(c) is the practical implication for prior work honestly scoped either
way the result comes out.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
