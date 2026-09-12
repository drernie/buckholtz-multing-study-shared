# CLAIM — direct before/after recompute of `rho_NN` on `M200c`-top-50
# vs. `M500c`-top-50 FLAMINGO selections: the actual test named by
# Step 8a skeptic review of the overlap result, replacing the overlap
# PROXY with the real statistic

**Date:** 2026-09-12
**Written and committed BEFORE the decisive script runs.** Per FL Step
2b. Kept lean (Structure-Bias Guard) — fully specified by the
skeptic's own named next step in `FINDING_flamingo_m500c_m200c_
overlap.md` item 3 / item 4 ("recompute a prior Pearson r on both
selections... instead of the indirect overlap surrogate").
**Continues:** `docs/162_ontology_spec_v82.md` item 3's sharpened
`[OPEN]` flag. **User-requested** (exact scope: top-50, the specific
`N` where overlap was the real anomaly, `74.0%`).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive

---

## The question

`FINDING_flamingo_m500c_m200c_overlap.md` established REAL top-`50`
overlap (`74.0%`) but explicitly could NOT answer whether this
membership difference actually SHIFTS `rho_NN` — overlap measures set
membership, not statistic stability, and the swap is systematically
biased (lowest-ratio halos swap out), not random. **This test replaces
the proxy with the real statistic.**

## Method

Reusing the SAME already-downloaded top-`5000`-by-`M200c` FLAMINGO
pool (deterministic, no new selection logic):

1. **`M200c`-top-`50`**: select the `50` most massive halos by `M200c`
   (identical to the prior overlap test's own selection). Compute
   `rho_NN` using each halo's true nearest neighbor WITHIN this same
   `50`-halo set, via FLAMINGO's real, full `1000` Mpc periodicity
   (matching this branch's own "definitive global estimand"
   methodology, not an artificial sub-cube wrap). Correlate `log
   M200c_self` against `log M200c_partner` — the population's own
   native mass definition.
2. **`M500c`-top-`50`**: select the `50` most massive halos by `M500c`
   (a DIFFERENT set, `74.0%` overlapping with #1, per the already-
   measured real overlap). Compute `rho_NN` the same way, on this
   population, correlating `log M500c_self` against `log
   M500c_partner` — again the population's own native definition
   (matching what a genuinely `M500c`/`R500`-convention-faithful
   selection, per v82's own text, would actually compute).
3. **Also report, for completeness (cheap, same data)**: the SAME
   comparison at `N=35` and `N=1200` (the other two `N` already tested
   for overlap), so this result sits alongside the full overlap
   picture rather than only the single anomalous point.

**Uncertainty**: given `N=50` is small, report the analytic
`1/sqrt(N-2)` SD alongside each point estimate as a first-pass scale
reference (matching this branch's own established practice at this
sample size) — NOT a claim this settles precision to the sigma-count
level (per this session's own standing corrections on that point).

## What this would and would not settle

- **If `rho_NN(M200c-top-50)` and `rho_NN(M500c-top-50)` are close**
  (within roughly one sample-scale SD of each other): the mass-
  definition choice did not materially matter for this specific
  statistic at this specific `N`, DESPITE the real, measured `74%`
  membership overlap — directly resolving the open question in
  `docs/162` item 3.
- **If they differ substantially**: confirms the skeptic's own
  concern — set overlap was hiding a real shift, and future tests in
  this branch should use `M500c` (the v82-faithful convention)
  directly, not `M200c` with an assumed-safe equivalence.
- **Either way**: this is ONE `N` (plus two bonus `N`s) on ONE
  simulation — does not generalize to every possible selection scale,
  and does not resolve the SEPARATE, larger `docs/162` item 9 question
  (2PCF-style estimand vs. nearest-neighbor).
- **Does NOT** validate or invalidate v82's own theory
  (`NO_AUTHOR_ERROR`).

## Skeptic pass

Mandatory (Step 8a), context-blind — specifically asked: (a) is
correlating each population against its OWN native mass definition the
right choice, or does mixing this with the ALTERNATE definition (e.g.
`M500c`-selected population but correlated via `M200c` values) matter
for isolating "does selection matter" from "does the correlated
quantity's own definition matter"; (b) is any observed
difference/similarity at `n=50` distinguishable from noise given this
branch's own already-established sample-size-dependent scatter floor
(`SD~0.17-0.23` at comparable `N` from every prior FLAMINGO test); (c)
is the practical conclusion for `docs/162` honestly scoped either way.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · NO_AUTHOR_ERROR
