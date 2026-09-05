# FINDING P196 — independent rebuild of the Girardi-R_vir vs
# TJB-style R500(z) comparison: the prior chat's headline number could
# not be reproduced, and is very likely a units bug plus a wrong target

**Date:** 2026-09-06
**Claim:** `CLAIM_P196_girardi_r_vir_vs_r200_check.md`
**Script:** `P196_girardi_r_vir_vs_r200_check.py`
**Continues:** a prior, inaccessible chat session's handoff (Girardi
1998 `R_vir=0.002σ` vs TJB-style ρ_crit(z)-based radius, on 123 real
HeCS-SZ clusters, reported `r=0.883`, mean ratio `1.128±13%`, scatter
`±14%`). That session's own files (`kill_test_r200.py`, `table4.dat`,
`girardi1998.pdf`) exist only in its own scratchpad and are not
recoverable from this session.

## Headline result

**The correlation is real and reproduces robustly: `r≈0.88`**,
regardless of overdensity target (`R200`: `r=0.8832`; `R500`: `r=0.8804`).
Girardi's velocity-dispersion-only radius and a `ρ_crit(z)`-based
catalog radius track each other well across 123 real clusters — this
part of the prior finding is confirmed, independently, on freshly-
fetched data.

**The prior chat's headline "mean ratio 1.128±13%" could NOT be
reproduced and should not be treated as reliable.** This session's own
independent rebuild, on the same real catalog (HeCS-SZ, VizieR
`J/ApJ/819/63/table4`, re-fetched fresh this session, not copied from
the prior chat), gives:

| Comparison | Mean ratio | Scatter |
|---|---|---|
| vs `R200` (matching the prior chat's own stated method) | **1.61** | 12.0% |
| vs `R500` (v82's own actual Section II.F target — see below) | **2.49** (raw) → **1.47** (after both corrections) | 12.1% → 11.1% |

None of these reproduce `1.128`.

## `[HYPOTHESIS, strongly supported by exact arithmetic, not `[VERIFIED]`
## against the prior chat's own unavailable code]` — most likely
## explanation for the discrepancy

A context-blind Step 8a skeptic pass (given only this file's claim +
code, no access to the prior chat) audited this session's own script
for bugs across 6 specific checks (unit consistency, `h`-scaling
symbolic derivation, NFW normalization, Duffy et al. 2008 pivot-mass
convention, concentration sanity, other silent errors) — verdict
`CONFIRMED-OK`, no bug found in this session's code. Independently
re-verified by hand (not merely accepted): the symbolic `h`-scaling of
the ratio is `∝ h^(-1/3)`, and working the arithmetic backward:

```
This session's R200-target raw ratio (1.61) x h(0.7) = 1.127 ≈ 1.128
```

This matches the prior chat's reported number to 3 significant
figures. The most parsimonious explanation: Girardi's Eq. 11
coefficient (`0.002`) is stated in `h⁻¹Mpc` per km/s — a physical
radius requires dividing by `h` (`R_vir[Mpc] = 0.002σ/h`). If the prior
chat's script used `R_vir=0.002σ` **without** dividing by `h≈0.7`, its
`R_vir` values would be too small by exactly that factor — which
inflates the ratio's denominator effect and would produce exactly the
observed `1.128` from what should be `1.61` (this session's own,
correctly-`h`-handled `R200`-target number). **This is not proven
without the prior chat's own source** — flagged honestly as a strong,
arithmetic-backed hypothesis, not a confirmed fact about code this
session cannot read.

**A second, independent, more clearly established issue**: the prior
chat's own description used "`R200` через `M200` и `ρ_crit(z)`" —
`Δ=200`. But `v82`'s own Section II.F (lines 602-604 of this project's
markdown conversion, `[VERIFIED-arXiv]`, read directly, not from a
paraphrase) explicitly calls its `r_X(z)` construction **"the standard
`R500`-type definition"** — `Δ=500`, not `Δ=200`. This project's own
earlier work this same session (`P158_addendum2_real_mass_function.py`,
`OVERDENSITY=500`) already independently used `Δ=500` for exactly this
documented reason. The prior chat's comparison target itself does not
match what TJB's own text actually specifies.

## The scientifically correct comparison (this file's own contribution)

Retargeting to `R500` (converting HeCS-SZ's own tabulated `M200c` to an
`M500`-equivalent via an NFW profile + Duffy et al. 2008 `c200(M,z)`,
`[VERIFIED-arXiv:0804.2486]` coefficients used as published) and
applying two further, separately-reported corrections:

- **Step 2a — reference-density correction (EXACT, no free parameter)**:
  Girardi's own `R_vir` is referenced to `ρ_crit,0` (z=0, no `E(z)`),
  not `ρ_crit(z)`. Converting at fixed `Δ=178`:
  `R_vir,z-ref = R_vir/E(z)^(2/3)`. Moves the mean ratio `2.49→2.39` —
  a small effect at this sample's modest z range (`z≤0.29`, median
  correction factor `0.967`).
- **Step 2b — overdensity-shape correction (approximate, concentration-
  dependent)**: converts `Δ=178` (on the `ρ_crit(z)` reference, after
  2a) to `Δ=500` via the same NFW halo. Moves the mean ratio
  `2.39→1.47` — the dominant correction, as expected (`Δ=178→500` is a
  much bigger shape change than the `z`-reference step).

**Combined: `2.49→1.47`, a real, substantial 41% reduction — but not
enough to reach the pre-registered MCID band `[0.95,1.05]`, and
scatter barely moves (`12.1%→11.1%`, ~1 percentage point, MCID
required `>5pp`).** By the exact pre-registered rule in `CLAIM_P196`,
this correction is **NOT material** — it does not explain away the
finding, it substantially reduces but does not eliminate it.

**Endpoint 3 (z-trend, a real independent check of the mechanism)**:
the RAW ratio correlates positively with `z` (`r=0.50, p<0.0001`), and
the SIGN was predicted in advance from the mechanism (Girardi's `R_vir`
carries no `z`-dependence; `R500(z)` shrinks as `z` grows since
`ρ_crit(z)` grows) — observed sign matches. This is real, independent
support that the `z=0`-reference-density effect is genuinely present
in the data, not merely a plausible-sounding correction invented after
the fact.

## Corrections applied (no-silent-correction discipline)

1. **Caught mid-analysis, before any number was reported**: the first
   version of this file's own script used `Δ=200` (matching HeCS-SZ's
   own tabulated column and the prior chat's own stated method) and got
   a raw ratio of `1.61` — not close to `1.128`. Investigating this gap
   is what surfaced the `Δ=500` vs `Δ=200` target mismatch (v82's own
   text says `R500`) — the script was then rewritten to retarget `R500`
   properly via an NFW `M200c→M500` conversion, which is what produced
   the `2.49`/`1.47` numbers reported above.
2. **Step 8a skeptic pass (this session)**: `CONFIRMED-OK` on this
   file's own code across 6 specific probes (units, `h`-scaling, NFW
   normalization, Duffy pivot-mass convention, concentration sanity,
   other silent bugs) — no bug found. Independently re-verified by hand
   (the `h^(-1/3)` symbolic scaling and the `1.61×0.7=1.127` arithmetic)
   before accepting the skeptic's own report, per this project's
   `audit-verification-gate.md`.

## What this does NOT establish

1. **Does not prove the prior chat's script had a bug** — no access to
   their code. The `1.61×h≈1.128` match is strong circumstantial
   arithmetic, not a code diff. Marked `[HYPOTHESIS]`, not `[VERIFIED]`.
2. Does not resolve why the corrected ratio (`1.47`) still sits well
   above `1.0` — real, substantial, and NOT explained by the two
   corrections applied here. Candidate remaining explanations (none
   tested in this file): `M200c`'s own caustic-technique systematics
   (per the prior chat's own already-completed, separate investigation
   of the caustic method's N-body-calibrated filling factor); the
   Duffy et al. 2008 concentration relation's own real scatter
   (~0.1 dex, not propagated as an uncertainty band here); a genuine
   physical signal about the `ρ_crit(z)`-circularity TJB himself named.
3. Does not re-validate `M200c` itself, or attempt the caustic-
   technique reimplementation — same scope limits as `CLAIM_P196`.
4. Does not draft or send anything to TJB. Given the unresolved
   reproduction gap and the still-large (1.47×) residual offset, this
   result is **not ready** to characterize confidently in any form —
   the correct next step is understanding the residual, not writing up
   what is currently an unexplained, only-partially-corrected number.
5. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   attempts and a prior chat session's inaccessible, unverifiable
   pipeline; not a claim about MULTING, v82, or Dr. Buckholtz's work.

## Pearl / methodological carry-forward

Worth a `pearl_registry/INDEX.md` line: **a headline number from a
session whose code is not preserved cannot be trusted at face value,
even when the underlying data and general method are real** — this
session's independent rebuild, on the identical real catalog, gave a
raw ratio 1.4-2.2x higher than what was reported, traced (with strong
though not certain confidence) to a unit-conversion (`h⁻¹Mpc→Mpc`) slip
plus a wrong overdensity target. Reinforces, with a second concrete
instance this same broad session, why this project's own convention
(commit code + data alongside any reported number, never trust a
scratchpad-only result) exists.
