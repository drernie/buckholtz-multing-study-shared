# Blind A — external provisional artifact

**Status: CROSS-IMPLEMENTATION-REPLICATED (stat-only endpoints). NOT independently
reproduced — see "On independence" below.**

An agent implemented the analysis from a written specification, in an isolated
directory containing ONLY public data — no local code, no local results. It was
explicitly NOT told: whether to include mass at r' > R, which UV prescription to
use, where to truncate, or which pair-weighting convention to adopt. Those four
decisions were left to it.

## What this experiment is, and is not

This is **NOT a reproduction test**. Because the specification was deliberately
incomplete, it measures ANALYST VARIATION: would two independent implementations
reach compatible conclusions when the model is under-specified? A different
number from this run does not by itself indicate a coding error — the agent may
have chosen a different admissible model.

A true reproduction (Blind B) requires freezing: bin policy, distance units,
kernel completeness, pair-weighting convention, UV prescription and scale, outer
tail closure, parameter domain, amplitude domain, covariance definition, Neyman
construction, seeds and simulation count.

## Files

- `report_original.md` — the agent's report, VERBATIM, unedited
- `specification_received.md` — exactly what it was given

## Its headline numbers (NOT yet accepted)

| quantity | value | status |
|---|---|---|
| weighted 95% upper limit | 8.25 Mpc | PENDING-INDEPENDENT-RECHECK |
| raw 95% upper limit | 11.25 Mpc | PENDING-INDEPENDENT-RECHECK |
| K_3(100) principal value | 0.0155930 | PENDING |
| best fit, weighted | 0.0 Mpc | PENDING |
| best fit, raw | +3.2 Mpc | PENDING |

## What it established that IS accepted

These are qualitative and were independently confirmed on our side:

- C_2 = 1 inside / 0 outside (shell theorem) — control passes both implementations
- mass at r' > R is REQUIRED for p > 2; one-sided truncation is log-divergent
- K_3 exists only as a Cauchy principal value; the pole is simple and antisymmetric
- K_4 has a double pole — no PV exists, the quadrupole is not constrainable this way
- no statistically significant 1/r^3 signal
- incomplete specification changes the numerical limit

## Why our earlier limit was wrong

We used a TWO-SIDED profile statistic q_mu = chi2(mu) - chi2(mu_hat) to build a
ONE-SIDED upper limit. The correct object sets q = 0 when mu_hat > mu. Our
15-17.5 Mpc bracket is INVALIDATED for that reason — wrong test statistic, not
a coding bug.

## Caveats the supervisor attached to this artifact

1. "PV is mathematically natural" is SUPPORTED; "PV is the unique physical UV
   completion" is NOT ESTABLISHED. Halo exclusion, finite-size convolution,
   softening, or a form factor may be what the physics requires instead. Also
   unfixed: whether the symmetric removal is in |r'-R|, in |s|, or in the
   dimensionless rho — the Jacobian makes these differ at finite epsilon.
2. The pair-weighting convention is PROVISIONALLY resolved in favour of the
   weighted form. "It is more conservative" carries no weight in choosing a
   definition. Final closure needs a derivation from the estimator itself, and a
   check that the denominator is not ALREADY in the published data vector
   (double-counting risk).
3. r_lo (the lower integration limit, 6 Mpc) is a MODEL-SUPPORT UNCERTAINTY, not
   an ordinary numerical systematic, until it is established what it represents.
   It must not be conflated with s_min, the exclusion around the singularity at
   r' = R — these are different objects.

---

## Outcome of the re-check (2026-08-02)

An independently written implementation (`../recheck_onesided.py`) reproduced
the stat-only endpoints EXACTLY:

| convention | Blind A | re-check | diff |
|---|---|---|---|
| raw | 11.00 | 11.00 | +0.00 Mpc |
| pair-weighted | 8.00 | 8.00 | +0.00 Mpc |

Kernels differ slightly (K3(100): 0.015593 vs 0.015754, 1.0%) because of the
finite PV epsilon and interpolation details — yet the endpoints coincide,
because the limit depends on shape and statistics, not kernel normalisation.

## On independence — read this before citing

The re-check did NOT import or read Blind A's scripts, and rebuilt the
statistic from scratch. But it **knew Blind A's numbers**: they were written
into its PASS criterion before it ran. So the correct status is

> **cross-implementation numerical replication**
> (independent-code reimplementation AFTER result disclosure)

which is stronger than a re-run and weaker than blind reproduction.
`INDEPENDENTLY REPRODUCED` is reserved for **Blind B** — a frozen specification
handed to an implementer with no knowledge of the expected values.

Full statistical specification: `docs/133`. Claim registry: `docs/134`.
