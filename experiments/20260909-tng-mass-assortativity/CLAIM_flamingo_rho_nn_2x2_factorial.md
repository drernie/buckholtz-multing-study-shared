# CLAIM — complete the 2x2 factorial: separate "which halos are
# selected" from "which mass values are correlated" as the driver of
# the N=50 rho_NN shift

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b. Kept lean — fully specified by Step 8a skeptic review of
`FINDING_flamingo_rho_nn_m200c_vs_m500c_selection.md` (item 2, the
named factorial-completion gap).
**Continues:** the prior test measured only the diagonal cells
(select-`M200c`/correlate-`M200c` `=0.3197`; select-`M500c`/correlate-
`M500c` `=0.0826` at `N=50`). **User-requested.**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## Method

Reusing the SAME shared top-`5000`-by-`M200c` FLAMINGO pool. For each
`N in {35, 50, 1200}`, compute all FOUR cells of the factorial:

```
             correlate via M200c   correlate via M500c
select M200c   A (already known)    B (NEW)
select M500c   C (NEW)               D (already known)
```

`A` and `D` are already established. `B`: select the top-`N`-by-
`M200c` halos (same set as `A`), find each one's true nearest neighbor
by POSITION within that same set (unchanged from `A`'s own NN pairing
— selection and pairing depend only on `M200c`-ranking and position,
never on `M500c`), then correlate using `M500c` VALUES for both self
and partner. `C`: the mirror — select by `M500c` (same set as `D`),
same NN pairing as `D`, correlate using `M200c` values.

**Decomposition**: pure selection effect at fixed correlation-
convention = `C-A` (at `M200c` convention) and `D-B` (at `M500c`
convention); pure value effect at fixed selection = `B-A` (at `M200c`
selection) and `D-C` (at `M500c` selection). If `|C-A|` and `|D-B|`
are small while `|B-A|` and `|D-C|` are large, the value convention
(which mass number is plugged into the correlation) is the driver, not
which specific halos were chosen. If the reverse, selection is the
driver.

## What this would and would not settle

- **Directly separates** the two effects the prior test's own skeptic
  review found entangled in the `N=50` delta (`-0.2371`).
- **Does NOT** provide a rigorous significance level for any of the
  four cells or their differences — the prior test's own honest
  `z~0.7-1.6` framing for the total effect stands; this decomposes
  WHAT is shifting, not how confidently.
- **Does NOT** resolve the separate, larger `docs/162` item 9 question
  (2PCF-style estimand vs. nearest-neighbor).
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked: (a) is the
decomposition itself correctly implemented (same NN pairing reused
correctly for the mixed cells, no accidental re-pairing by the
alternate mass); (b) does the resulting decomposition change the
honest significance assessment from the prior test, or only its
mechanistic interpretation; (c) is the practical conclusion for
`docs/162` honestly scoped either way.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
