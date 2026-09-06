# FINDING E17 — closing E16's Pearl Registry gap took two Step 8a skeptic
# rounds, and the real answer split into two separate findings, not one

**Date:** 2026-09-06
**Claim:** `CLAIM_E17_mass_scatter_for_F0_Faccretion.md` (pre-registered)
**Script:** `E17_mass_scatter_for_F0_Faccretion.py`
**Continues:** `FINDING_E16`'s Pearl Registry Caveat Gate entry
(`F0`/`F_accretion` also nonlinear in `M(z)`, un-scoped by `E16`'s
`F1,F2`-only Jensen's-gap correction).

## What was asked

Measure a real, sourced population scatter for `M(z)` (v82's own assumed
mass-accretion law), to check whether `F0=-G·M²/d²` and `F_accretion`
(`∝M`, `∝√M`) carry their own Jensen's-gap corrections, un-scoped by
`E16`'s `F1,F2`-only work.

## Real sources found and used

- `v82.md`'s own bibliography (refs `[18]` Fakhouri, Ma & Boylan-Kolchin
  2010, `arXiv:1001.2304`; `[19]` Zhao, Jing, Mo & Börner 2009,
  `arXiv:0811.0828`) confirms `M(z)` is v82's own "Class II,
  retained-theoretical" input — a real mass-accretion-history (MAH)
  literature, not a fitted scaling relation. Neither cited paper gives a
  directly quotable `σ` (Zhao+2009 defers to an unlocatable "Zhao et al.
  2010, in preparation").
- **Correa, Wyithe, Schaye & Duffy (2015)**, `arXiv:1501.04382`, provides
  an N-body-validated analytic MAH model (their eqs 49-52) connecting
  Duffy et al. (2008)'s own concentration-mass scatter (`σ(log10
  c200)=0.15`, already used by this project's `P196_addendum_
  concentration_scatter.py`) to a formation-redshift and `M(z)` shape.

## What went wrong, twice, both corrected in place — no silent fixes

**Step 8a Pass 1 verdict: `FALSIFIED`.** The first version computed
`exp(n²σ_ln(M)²/2)` — i.e., `E[Mⁿ]/median(M)ⁿ` under a parametric
lognormal assumption, referenced against **Correa's own MAH-model
median**, not v82's own assumed `M_ref(z)=M0·(1+z)^{-1.1}` — the actual
quantity v82's force law evaluates `F0`/`F_accretion` at. The skeptic
found these differ by a real `6.5×` systematic offset at `z=2.33`,
conflated with scatter, flipping the reported sign at `z=1.0`. **Fixed:**
direct `E[Mⁿ]/M_ref(z)ⁿ` from raw Monte Carlo samples, no parametric
shortcut, correct reference throughout.

**Step 8a Pass 2 (on the fix) verdict: `WEAKENED`.** The corrected single
number still **conflated two physically distinct effects**: a real
systematic **offset** (`E[M]/M_ref`, v82's own assumed power law vs the
real MAH model — up to `~5×` at `z=2.33`, NOT a scatter effect) with the
actual **Jensen scatter correction** (`E[Mⁿ]/E[M]ⁿ` — the quantity `E16`'s
gap actually asked about, much smaller). The skeptic also flagged: (a)
`5.6%` of Monte Carlo draws excluded for unphysical formation redshift
biases the reported numbers to be an **upper bound**, not a neutral
estimate; (b) positive controls PC1-PC3 are structurally tautological —
no control cross-checks `mass_history_ratio` against Correa+2015's own
published values; (c) a real mathematical singularity in Correa's own
`α` formula as `z_{-2}→0` (verified: `α` range `[-6747, +0.26]` for
`z_{-2}∈[0,0.05)`) required switching from `np.std` to a direct-sample
mean (robust to the singularity, since `(1+z)^α→0` there, not `→∞`).
**Fixed:** the script now returns `offset(z)`, `jensen(n,z)`, and
`combined(n,z)=offset(z)ⁿ·jensen(n,z)` separately — a caller cannot
silently misattribute one for the other.

## Result — the two separated findings

| `z` | offset `E[M]/M_ref` | Jensen (`F0`, n=2) | Jensen (`F_acc`, n=1.5) |
|---|---|---|---|
| 0.07 | 0.9528 | 1.0149 | 1.0064 |
| 0.25 | 0.8655 | 1.0577 | 1.0245 |
| 1.00 | 0.5499 | 1.2813 | 1.1118 |
| 2.00 | 0.2653 | 1.7205 | 1.2601 |
| 2.33 | 0.2057 | 1.9122 | 1.3181 |

**Finding 1 — the Jensen scatter correction (what `E16`'s gap asked
about): MATERIAL at `z=1.00, 2.00, 2.33`.** `F0`'s correction reaches
`~1.9×` at `z=2.33`; `F_accretion`'s reaches `~1.3×`. Smaller than `E15`'s
own `F1,F2` corrections (`1.13×`/`1.62×` at fixed `σ=0.49`, no
`z`-dependence), but real, and growing with `z` (individual mass
trajectories diverge further the further back they're traced) — unlike
`E13`'s `M_gas` scatter, which was treated as `z`-independent.

**Finding 2 — a large, separate, un-asked-for systematic offset:** v82's
own simple assumed `M(z)=M0·(1+z)^{-1.1}` diverges substantially from
Correa+2015's real N-body-calibrated MAH model at this project's own
pivot mass (`M0≈6×10¹⁴ M_☉`) — down to `~21%` of v82's assumed value at
`z=2.33`. This is **not** a scatter/Jensen effect and is **not** what this
experiment was asked to measure — logged separately (Pearl Registry,
below), not folded into the Jensen result.

## What this does and does NOT establish

**Does establish:** a real, sourced, doubly-skeptic-reviewed Jensen
correction for `F0`/`F_accretion`, closing `E16`'s named gap — material at
higher `z`, though smaller than `F1,F2`'s own corrections.

**Does NOT establish:**
1. The full `M(z)` scatter — only the concentration-driven channel
   (Correa's own analysis finds real formation-time scatter not fully
   explained by concentration alone) — a lower-bound-flavored partial
   estimate on the Jensen component specifically.
2. Numerical calibration of `mass_history_ratio` against Correa+2015's
   own published figures/tables — named as an open verification gap by
   the 2nd skeptic pass, not closed here.
3. Whether the offset finding (Finding 2) reflects a real problem with
   v82's own assumed mass law, or a mismatch in what the two models are
   actually meant to describe (single-halo MAH vs population-level
   characteristic mass) — an open interpretive question, not resolved.
4. `NO_AUTHOR_ERROR` — a direct answer to a question this project itself
   posed (`E16`'s Pearl Registry entry), not a claim about v82's
   correctness.

## Pearl Registry entries

Two new rows in `pearl_registry/INDEX.md`: (1) the Jensen-correction
result itself (closing `E16`'s Caveat Gate entry); (2) the `M(z)`-vs-MAH
systematic-offset side-finding (Finding 2), a genuinely new, unexpected,
falsifiable observation this experiment was not designed to produce.

## Next step, named not done

Validate `mass_history_ratio` numerically against Correa+2015's own
published Fig 3/Table values at a comparable `M0`, before treating either
the Jensen correction or the offset magnitude as more than
order-of-magnitude-plausible.
