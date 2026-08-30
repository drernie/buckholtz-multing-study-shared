# FINDING P166 — AIC/BIC computed on v82's own published χ² numbers
# (Phase 1 of the AIC/BIC calibration plan, 2026-08-30)

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (pure arithmetic on already-published
numbers, no new data, no new fitting)
**Script:** `P166_aic_bic_from_v82_own_table_ii.py` — positive control
(v82's own admittedly-handicapped benchmark reproduces v82's own claimed
large win, confirming the arithmetic itself is correct) + negative
control (BIC's own N-scaling behaves correctly on synthetic values,
independent of any real data).
**Verdict:** `ON v82's OWN TWO "FAIRER" BENCHMARKS (its own words) — NOT
THE ADMITTEDLY-HANDICAPPED FIXED-PLANCK ONE — MULTING's RAW χ² EDGE IS
CONSUMED ALMOST ENTIRELY BY THE STANDARD PARAMETER-COUNT PENALTY. `ΔAIC≈
+1.2` to `+1.4` (Burnham-Anderson convention: <2 means the two models are
statistically indistinguishable — neither is preferred). `ΔBIC≈+2.7` to
`+2.9` (Kass-Raftery convention: 2–6 is "positive," not "strong," support
for the simpler model — i.e. mild, not decisive, favor toward ΛCDM). This
is the FIRST time this specific arithmetic has been done, by anyone,
including this project and TJB himself — TJB explicitly declines to
report AIC/BIC (Sec. IV.I), for a substantive, non-trivial reason he
states himself (see §1): ΛCDM's fixed parameters carry decades of
independent external scrutiny that MULTING's own fixed inputs have not
yet had, making a naive parameter-count penalty potentially UNFAIR TO
ΛCDM in the other direction (crediting MULTING's currently-fixed,
first-pass, unscrutinized choices as "free," when its TRUE effective
flexibility may be higher than the nominal k=2/3 used here). This means
the result below, if anything, is GENEROUS to MULTING, not harsh — a
floor, not a ceiling, on how unfavorable a fuller accounting could be.`
**Continues:** the AIC/BIC calibration plan from today's causal audits
("Measurement Shadow," "Identifiability Breaker," `negative-space-miner`)
— Phase 1 (this file, cheap, done): AIC/BIC on already-published numbers.
Phase 2 (not attempted here): fit a physically-empty dummy model of the
same flexibility to real H(z) data, as an independent calibration check.

## 0. Premise — `NO_AUTHOR_ERROR`, and why this is not a criticism

This file computes numbers TJB himself chose not to compute, and reports
them honestly — it is not a claim that his choice was wrong. v82's own
Sec. IV.I gives a substantive, carefully-reasoned argument for that
choice, quoted here in full because it materially bears on how to read
the result below:

> "Given this asymmetry, we do not report AIC or BIC anywhere in this
> paper... A penalty for the number of free parameters presupposes that
> those parameters were fixed independently of the data under test, an
> assumption that holds far more securely for ΛCDM, given its history,
> than for a framework still in active development; reporting a single
> AIC or BIC number would present that asymmetry as a resolved,
> symmetric statistical contest, which it is not."

TJB's own argument: ΛCDM's *nominally fixed* parameters (Ωk=0, Neff,
w=−1) represent decades of independent, adversarial, external scrutiny
across multiple collaborations and datasets — the "often-quoted parameter
count understates how much empirical work stands behind each fixed...
value" (his own words). MULTING, by contrast, has several *currently-
fixed* inputs (the coherence fraction `f_coh`, the sign of the accretion
correction, the temperature normalization `T_0`) that were, in his own
words, "adopted as first-pass modeling choices during this project's own
development, not validated by independent analyses external to it."

**This is a serious, correct point, and this file does not dispute it.**
Its consequence for reading the numbers below: the nominal parameter
counts used here (`k=3` for MULTING's unconstrained fit, `k=2` for its
SH0ES-anchored fit) are almost certainly an *undercount* of MULTING's
true effective flexibility, since they penalize only the three explicitly
varied parameters, not the several first-pass fixed choices TJB himself
flags as not yet independently scrutinized. A fuller accounting would
likely make MULTING's position *less* favorable under AIC/BIC, not more
— so this file's own result should be read as a floor, not a ceiling.

## 1. Method — pure arithmetic on v82's own already-published numbers

No new data, no new fitting. All six numbers (three MULTING rows, three
ΛCDM benchmarks) are quoted directly from v82's own Sec. III / Table II
(p.13):

`[VERIFIED-PDF]`:

| Model | `χ²₃₃` | `k` (free params) | Source |
|---|---|---|---|
| MULTING, unconstrained (`H0,anchor=73.22`) | 15.75 | 3 | Table II row 1, "the spotlighted solution" |
| MULTING, SH0ES-anchored (`H0,anchor=73.04`) | 15.78 | 2 | Table II row 2 |
| ΛCDM Benchmark 1 — fixed Planck (`H0=67.4, Ωm=0.315`) | 36.96 | 0 | "not a demanding benchmark... not permitted to respond to SH0ES at all" |
| ΛCDM Benchmark 2 — `H0, Ωm` both refit (`71.83, 0.2724`) | 16.31 | 2 | "the more meaningful comparison, because it does not handicap ΛCDM" |
| ΛCDM Benchmark 3 — `H0` fixed at 73.04, `Ωm` refit (`0.2679`) | 16.60 | 1 | "perhaps the fairest single comparison in this paper" |

`AIC = χ² + 2k`, `BIC = χ² + k·ln(N)`, `N=33` — the standard forms, both
already correctly identified in v82's own text (Sec. IV.I) even though
not applied there.

**Why Benchmarks 2 and 3, not Benchmark 1, are the relevant comparators:**
v82's own text explicitly calls Benchmark 1 "not a demanding benchmark"
because fixed-Planck ΛCDM "is not permitted to respond to SH0ES at all"
— i.e., TJB himself identifies it as a handicapped comparison, not a fair
one. He explicitly nominates Benchmarks 2 and 3 as the meaningful,
"fairest" comparisons. This file follows his own stated preference, not
an independent judgment call — an apples-to-apples reading of his own
paper on his own terms.

## 2. Result — `[VERIFIED-python, positive+negative control]`

**Comparison A** (MULTING unconstrained, `k=3` vs. ΛCDM Benchmark 2,
`k=2` — v82's own "more meaningful comparison"):

```
Δχ²  = −0.560   (MULTING's raw fit is better, by v82's own numbers)
ΔAIC = +1.440   (Burnham-Anderson: <2 → statistically indistinguishable)
ΔBIC = +2.937   (Kass-Raftery: 2–6 → "positive," not "strong," toward ΛCDM)
```

**Comparison B** (MULTING SH0ES-anchored, `k=2` vs. ΛCDM Benchmark 3,
`k=1` — v82's own "fairest single comparison"):

```
Δχ²  = −0.820
ΔAIC = +1.180
ΔBIC = +2.677
```

**Sanity check (Comparison C, MULTING unconstrained vs. the admittedly-
handicapped Benchmark 1)**, run purely as a positive control on the
arithmetic itself: `Δχ²=−21.21, ΔAIC=−15.21, ΔBIC=−10.72` — a large,
unambiguous win for MULTING, exactly reproducing v82's own qualitative
narrative about that specific (handicapped) comparison. This confirms
the AIC/BIC formulas are implemented correctly, independent of anything
about the fairer benchmarks above.

## 3. Interpretation

On the two comparisons TJB himself identifies as the meaningful, fair
ones, MULTING's raw `χ²` edge over ΛCDM — which his own text already
describes as narrow ("MULTING still edges ΛCDM out, though narrowly,
rather than substantially") — is almost entirely consumed by the standard
parameter-count penalty once it is actually computed. `ΔAIC` stays under
the conventional indistinguishability threshold of 2 in both comparisons;
`ΔBIC` reaches only "positive" (weak-to-moderate), not "strong," support
for the simpler ΛCDM comparator, per the standard Kass-Raftery scale.

**This is not a claim that MULTING is falsified, or that World B
(curve-fitting artifact, from today's earlier causal audits) is
confirmed.** It is a specific, narrow, arithmetic fact: the raw `χ²`
advantage TJB himself already characterizes as modest does not survive
the standard information-criterion penalty for MULTING's own extra
parameter, on the two benchmarks TJB himself calls fairest. Given §0's
point — that the true parameter-count gap may be larger than the nominal
one used here — this result is, if anything, an optimistic floor for
MULTING's position under this kind of comparison, not a worst case.

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory being wrong** (`NO_AUTHOR_ERROR`,
   §0) — TJB's own stated reason for omitting AIC/BIC is a substantive
   argument this file does not dispute; it only computes the number he
   declined to compute, using his own published data, and reports it.
2. **Does not use the more rigorous Bayes-factor / Bayesian evidence
   machinery** that today's earlier literature search (`negative-space-
   miner` run) found is the field's own preferred tool for exactly this
   kind of question (e.g. the `Λ_ωsCDM` case with `Δlog B=+6.2`, or the
   EDE Bayesian-vs-frequentist split) — AIC/BIC are simpler, cruder
   proxies; a full Bayesian treatment would need priors this file does
   not attempt to specify.
3. **Does not attempt Phase 2** of the calibration plan (fitting a
   physically-empty dummy model of the same flexibility to real H(z)
   data) — a separate, more expensive next step.
4. **Does not adjudicate §0's own asymmetry argument** — whether
   MULTING's currently-fixed inputs (`f_coh`, accretion sign, `T_0`)
   should, in fact, count as additional effective parameters, and by how
   much, is TJB's own open question (his own words: "this leaves open,
   plainly, how many degrees of freedom this framework will ultimately
   be found to have"), not resolved or estimated here.
5. **Does not use the free-floating fit's own uncertainty** on `β1, β2,
   H0,anchor` — a full treatment would also need the covariance/
   confidence region around the best-fit point (touching `FINDING_P165`'s
   own still-open magnitude question), not just the point χ² value.
