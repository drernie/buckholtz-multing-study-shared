# FINDING — mock-catalog power analysis: population definition decides
# whether the C1 kill-test is even runnable

**Date:** 2026-09-11
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Artifact:** `power_analysis_mock_catalog.py` — real code, real output,
`[VERIFIED-run]`. All inputs either directly cited (arXiv IDs given
inline) or explicitly flagged as an assumption; none invented silently.
**Continues:** `estimand.md`'s own MCID section ("not yet numeric... a
mock-catalog power analysis... before any real number is frozen") and
`data_acquisition_plan.md`'s Fork 2 (the 700-850 deg² footprint bound).

---

## 1. What this is, and what it is NOT

This answers the narrow, C1-scoped statistical question: **given a real
sample size and a real predicted signal shape, and assuming ONLY
measurement noise (no confounding, no measurement-validity threats), how
much data is needed to detect it?** It does **not** answer the C2 causal
question, and it does **not** run `estimand.md`'s own mandatory synthetic
four-world identifiability battery (MULTING / optical-depth-confounded /
merger-confounded / null) — that remains a separate, not-yet-built
artifact. This power analysis is a **best-case upper bound**: real power,
once confounding and measurement-validity threats are folded in, will be
lower than every number below.

---

## 2. The decisive finding: "the pair" definition changes N_pairs by 30x

Two honest ways to define the separation window: the real kSZ-literature
bin (`20-160 Mpc`, the general pairwise-kSZ convention this project's
`claim.md`/`estimand.md` inherited from `arXiv:2511.23417`) vs. v82's own
characteristic node scale (`s0~30 Mpc`, `pearl_registry`'s 2026-09-09
entry — itself only weakly sourced, v82's own text names it and then
rejects it):

| Window | N_pairs (Fork-2 mid footprint, 775 deg², LOWER BOUND) |
|---|---|
| 20-160 Mpc (kSZ literature convention) | **~585** |
| 20-45 Mpc (v82's own `s0~30 Mpc` region) | **~12** |

Both are computed the same way — a real `astropy.cosmology` comoving-
volume calculation applied to the real ACT-DR5 MCMF cluster density
(`6237` clusters, `[VERIFIED-arXiv:2406.14754]`) — not two different
methods giving different answers by accident. **The difference is purely
which physical separation range "the pair" is taken to mean**, and
`estimand.md`'s own Population section already flagged this as unresolved
(deferring to the source paper's own convention) without yet knowing it
carried a 30x cost.

---

## 3. Power results

**At the broad (585-pair) window** — Monte Carlo, `N_MC=4000` per cell,
`ΔAIC>6` + `|z|>1.96` as the PROMOTE criterion (matches this project's
own `FINDING_P166` AIC convention):

| N_pairs | noise = 1x signal RMS | 3x | 10x |
|---|---|---|---|
| 50 | 100.0% | 31.2% | 2.1% |
| 100 | 100.0% | 68.1% | 4.0% |
| **585 (Fork-2 estimate)** | **100.0%** | **100.0%** | **33.9%** |
| 5000 | 100.0% | 100.0% | 100.0% |

False-promote rate under the null stayed near the nominal `~0.5%`
throughout (below the `α=0.05` design level, since the `ΔAIC>6` bar is
stricter than the bare `z`-test alone) — the test is not spuriously
trigger-happy in this idealized setting.

**At the narrow (12-pair) window** — the same test collapses:

| noise | power | false-promote |
|---|---|---|
| 1x | 65.5% | 1.2% |
| **3x** | **5.9%** | 1.1% |
| 10x | 1.4% | 1.1% |

**At `n=12`, the test has essentially no power at any realistic noise
level** — 5.9% at 3x noise is barely above the false-promote rate itself,
meaning a PROMOTE verdict at that sample size would be nearly
uninformative regardless of whether MULTING is true.

---

## 4. What this means for the branch

**If "the pair" means the broad kSZ-statistic window:** the C1 kill-test
is well-powered at the Fork-2-estimated sample size, even under
pessimistic (3x) noise — a real, favorable result, *conditional on* the
marginal-to-joint `ξ`-scatter substitution (`claim.md` §3a's own flagged
`HYPOTHESIS`) holding up, and *conditional on* the confounding structure
being controlled well enough that the synthetic battery passes.

**If "the pair" means v82's own characteristic scale:** the branch is
**not viable as currently scoped** — 12 pairs cannot support this test
at any noise level this analysis considers realistic. The only way
forward in that case is enlarging the usable sky area (revisit Fork 1's
"request the collaboration data" option specifically for its potential
to cover much more sky than the from-scratch ACT+DESI construction can
reach), or accepting that this branch answers a question about the
kSZ-literature's own pairwise scale, not literally the scale in v82's own
text — a real, honest scope narrowing, not a technicality to paper over.

**This is now the single most consequential open decision in this
branch — more consequential than the data-acquisition cost itself.**

---

## 5. What this does NOT establish

1. Not a real power number — a best-case, confounder-free upper bound.
   The synthetic four-world battery (`estimand.md`'s own hard gate) has
   not run; real power is lower.
2. Not a resolution of the marginal-vs-joint `ξ`-scatter substitution
   (`claim.md` §3a) — still `HYPOTHESIS`, carried forward as an assumption
   into this analysis, not validated by it.
3. Not a resolution of which separation window is correct — both numbers
   stand, the decision is named, not made.
4. Not a claim about MULTING (`NO_AUTHOR_ERROR`) — this is entirely about
   whether *this project's own reconstruction* of a test is statistically
   viable.

## Status

**Computed, not decided.** Next: either (a) resolve the pair-definition
question (re-read `arXiv:2511.23417`'s own methods section for how it
defines pairs, and separately try to pin down v82's own intended
separation more precisely than the `s0~30 Mpc` proxy), or (b) proceed
provisionally under the broad-window definition, explicitly labeled as
such, while the narrow-window result stays on record as the honest
alternative. No code beyond this power-analysis script exists in this
folder; the synthetic four-world battery is still unbuilt.
