# CLAIM P196 Addendum 2 — substituting real, X-ray-measured
# concentration-mass relations (Buote et al. 2007, Schmidt & Allen
# 2007) for Duffy et al. (2008)'s simulated median

**Date:** 2026-09-06
**Continues:** `FINDING_P196_ADDENDUM`, which ruled out concentration
*scatter* as an explanation for `P196`'s own `1.47×` residual, and
explicitly named Duffy et al. (2008)'s own documented, one-directional
finding — real X-ray-observed cluster concentrations run systematically
*higher* than their simulated median — as the concrete, untested next
candidate.
**Authorization:** explicit user go-ahead ("да, проверь Buote и
Schmidt & Allen"), 2026-09-06.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive.

## What is newly verified before this file (primary sources, this
## session, not memory)

**`[VERIFIED-arXiv:astro-ph/0610135]` Buote et al. (2007)**, 39 real
X-ray systems ((0.06-20)×10¹⁴ M☉), BCES power-law fit to the full
sample:
```
c₀ = c₁₄ · (M/M₁₄)^α,   c₀ ≡ (1+z)c,   M₁₄ = 10¹⁴ h⁻¹ M☉
α = −0.172 ± 0.026,   c₁₄ = 9.0 ± 0.4   (1σ)
intrinsic scatter in log₁₀ c₀ = 0.102 ± 0.004
```
`M` and `c` are defined at Buote's own **virial** overdensity
`Δ_vir(z)`, computed via the **Bryan & Norman (1998)** fitting formula:
`x = Ωm(1+z)³/E(z)² − 1`, `Δ_vir(z) = 18π² + 82x − 39x²`. Independently
re-derived by hand and cross-checked: at `z=0`, this formula gives
`Δ_vir(0) = 101.14`, matching Buote's own quoted `Δ=101.1` conversion
reference exactly — confirms the formula (recalled, not looked up in
this exact paper) is correctly applied.

**`[VERIFIED-arXiv:astro-ph/0610038]` Schmidt & Allen (2007)**, 34 real
Chandra-observed massive relaxed clusters (`0.06<z<0.7`), full free-fit
(`c₀, a, b` all free):
```
c_vir(z) = c₀/(1+z)^b · (M_vir/(8×10¹⁴ h⁻¹ M☉))^a
c₀ = 7.55 ± 0.90,   a = −0.45 ± 0.12,   b = 0.71 ± 0.52   (95% CL)
```
`M_vir` and `c_vir` are defined at **their own** virial overdensity,
`Δc(z) = 178·Ωm(z)^0.45` (Lahav et al. 1991) — a **third**, distinct
convention, different from both Buote's Bryan-Norman `Δ_vir(z)` and
Duffy et al.'s fixed `Δ=200`.

**A real, load-bearing tension between the two real observational
studies, not resolvable within this file**: Buote's own slope
(`α=−0.172±0.026`) and Schmidt & Allen's (`a=−0.45±0.12`) disagree by
roughly a factor of 2.6 in log-slope — the two real X-ray studies do
not agree with each other, not just with N-body simulations. This is
reported honestly as a real source of model uncertainty this file
cannot resolve, not smoothed over.

## New estimand element specific to this file

**Population**: same 123 HeCS-SZ clusters, same `M200c`, same
`Δ=178→500` NFW shape-correction target as `P196`.

**Method**: for each cluster and each of the two real relations
separately, solve (via `brentq`, reusing this project's own existing
NFW machinery) for the `(M_vir, c_vir)` pair such that (a) `c_vir` is
given by that paper's own fitted formula at that `M_vir`, and (b)
converting `(M_vir, c_vir)` at that paper's own `Δ(z)` to `Δ=200` gives
`M200 = M200c` (the real, catalog value) — i.e., find the halo whose
real `M200c` is consistent with that paper's own predicted
concentration, rather than assuming `M200c ≈ M_vir` (an approximation
this file explicitly avoids). Once anchored, recompute `R500`, `R178`,
and the final `ratio_2b` exactly as in `P196`, substituting this
concentration source for Duffy et al. (2008).

**Positive control (mandatory before trusting either substitution)**:
round-trip Duffy et al. (2008)'s own relation through this NEW
root-finding machinery (at `Δ=200`, where the round-trip should be the
identity, since Duffy's own `c` is already defined at `Δ=200`) and
confirm it reproduces `P196`'s own original `nfw_from_m200c`-based
numbers — validates the new machinery against a known-correct baseline
before applying it to the two real, differently-`Δ`-conventioned
relations.

**Falsifiable predicate**: if substituting either real relation moves
the mean ratio meaningfully toward `1.0` (using `P196`'s own MCID band
`[0.95,1.05]`), that specific mechanism (real concentrations run
higher than simulated) is confirmed as a material contributor to the
residual. If it does not move the ratio into that band — or moves it
in the *opposite* direction — the mechanism is not confirmed by this
specific test, reported honestly either way.

**MCID**: reused from `CLAIM_P196` unchanged (`[0.95,1.05]` band, or a
scatter reduction `>5` percentage points).

## What this does NOT establish

1. Does not resolve the real Buote-vs-Schmidt&Allen slope disagreement
   — both are used and reported separately, not averaged or
   arbitrarily preferred.
2. Approximates `M_vir≈M200c` is explicitly avoided (the root-finding
   procedure), but the Δ-conversion itself still assumes a single NFW
   profile shape holds exactly between the paper's own `Δ(z)` and
   `Δ=200` — the same category of approximation `P196`'s own Step 2b
   already carries, not a new, additional assumption.
3. Does not attempt a from-scratch reanalysis of either paper's own
   Chandra/XMM data — their published fit parameters are used as
   given.
4. Does not draft or send anything to TJB.
5. `NO_AUTHOR_ERROR`.
