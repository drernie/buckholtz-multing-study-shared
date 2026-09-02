# Statistical protocol — formalizing H1' (DoF-ratio criterion) from NR-020

**Date:** 2026-09-02
**Skill:** `/stat-validate`, requested by user, adapted (its 4 built-in
tests — McNemar/Wilcoxon/paired-t/von Mises — are all PAIRED-comparison
designs; H1' needs a cross-sectional regression across N independent
historical cases, which is a different design stat-validate's own
canned tests don't cover).
**Status:** PROTOCOL ONLY — no data collection performed yet, per
explicit scoping this session.
**Labels:** L0 descriptive/methodological (designing a test, not yet
running one)

---

## Design

Cross-sectional **logistic regression** (or Firth's penalized logistic
regression, given real risk of quasi-complete separation at the N this
analysis is likely to use) across N independent historical "numerical
coincidence" physics claims.

**Outcome (binary):** did the claim survive its first genuinely
independent, out-of-sample test (1) or fail it (0)?
**Primary predictor:** DoF-ratio = free parameters fixed in the formula
÷ independent data points genuinely fit BEFORE the first new prediction.
**Controls:** (1) author prestige proxy (e.g., established researcher at
time of publication vs. not), (2) ansatz-space-size proxy (how large was
the space of plausible functional forms the formula was chosen from) —
this second covariate is the weakest, most subjective part of the design
and should be flagged as such in any write-up.

**Primary test:** likelihood-ratio (or Wald) test on the DoF-ratio
coefficient, controlling for both covariates. Effect size reported as
odds ratio per 1-SD change in (standardized) DoF-ratio.

## Correction to the skeptic's own "≥30 cases" figure

The skeptic (today's negative-space-miner attack) specified "≥30
historical cases" as a validity requirement. That number is **too low**
for what it needs to do. Per Peduzzi et al. (1996)'s Events-Per-Variable
(EPV) rule for stable logistic regression, 3 predictors need ≥10 EPV
→ ≥30 events of the RARER outcome, not 30 cases total. With a
plausible ~50/50 survive/fail split, that already implies **N≈60 total**,
not 30 — and more if the true split is skewed (plausible, since most
historical numerology claims are believed to fail).

## Minimum Detectable Effect (MDE), simulation-based

Closed-form power formulas for multivariable logistic regression assume
independent covariates, which prestige/ansatz-size and DoF-ratio are not
expected to be here (a complex ansatz often also has more free
parameters — a realistic confound built into the simulation). Simulation
(500 draws per N/OR combination, `scratchpad/h1_prime_mde.py`, seed
20260902) is the more honest approach — same logic Peduzzi's own rule
was originally derived from.

| N | MDE (smallest reliably-detectable odds ratio, 80% power, α=0.05) |
|---|---|
| **30** (skeptic's own suggested floor) | **OR ≈ 5.0** — only a LARGE effect is detectable |
| 45 | OR ≈ 3.0 |
| **60** (EPV-rule-implied target) | **OR ≈ 2.5** |
| 90 | OR ≈ 2.5 (diminishing returns past 60 at this grid resolution) |

**Reading:** at the skeptic's own suggested N=30, this design could only
reliably detect a DoF-ratio effect that increases the odds of survival
5-fold per standard deviation — a genuinely small-to-moderate effect
(OR≈2-3, still practically meaningful) would likely be missed entirely.
**N≈60 is the honest target**, not 30 — this is itself a real, useful
correction surfaced by actually running the power analysis rather than
accepting the skeptic's number at face value.

## Blind coding

Single-coder (this session) is not "blind coders" in the strict sense
the skeptic asked for. The realistic approximation available in this
project: delegate a subsample to a fresh `Agent(skeptic)` or similar,
with no context from this session, to independently code the same
cases, then compute Cohen's κ on the overlap — matches the Context
Asymmetry Rule already used for the Step 8a skeptic dispatch elsewhere
in this project. Not yet done.

## What this protocol does NOT establish

1. Does not itself test H1' — no data has been collected.
2. Does not guarantee N≈60 real, well-documented historical cases are
   even findable in the literature at the needed quality/detail to code
   reliably — this is a real feasibility risk, not assessed here.
3. The ansatz-space-size covariate has no principled operationalization
   proposed yet — likely the weakest link in the whole design.
4. Does not replace or supersede NR-020's own qualitative application of
   H1' to Eq.32 (5-case, non-regression) — that stands as a provisional,
   unattacked-in-its-final-form read, separate from this heavier design.

## Next step (not started)

If pursued: literature search for ≥55 additional real, citable historical
"numerical coincidence" physics cases (beyond the 5 already in NR-020),
coding scheme finalized, delegated blind sub-coding, then the actual
regression. A substantial, multi-session undertaking — not attempted
without an explicit go-ahead given the real cost this protocol has now
quantified.

## Artifacts

- `scratchpad/h1_prime_mde.py` — MDE simulation (session-local, not
  committed; reproducible from this file's own docstring + seed).
