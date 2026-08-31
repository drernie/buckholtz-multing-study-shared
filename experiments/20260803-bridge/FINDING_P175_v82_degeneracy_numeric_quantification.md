# FINDING P175 — quantifying FINDING_P165's own unattempted next step: the
# numeric scale of the beta1-beta2-epsilon degeneracy, using v82's own
# real baseline values and Table II data

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (numeric evaluation of an already-derived
symbolic result against real published/archived numbers — not a new
physics claim)
**Continues/answers:** `FINDING_P165`'s own explicitly named unattempted
next steps ("does NOT establish", point 2): "does not compute the numeric
value of `C=d0·m0/(k0·r0)`... in v82's own actual units," and does not
determine whether the identified degeneracy is "practically dangerous or
practically negligible in magnitude."
**Script:** `P175_v82_degeneracy_numeric_quantification.py` (numpy,
1 positive control, verified against TJB's own cached run output).
**Data source:** TJB's own supplemental Zenodo archive (`zenodo_archive_
v17.zip`, DOI 10.5281/zenodo.22004287 — the same archive `FINDING_P169`
already used to recover `M0`) — `archive/code/multing_core.py` (functions
copied verbatim, cross-checked against a direct import of the real file,
identical output) and `archive/code/assumptions.yaml` (baseline constants
and Table II rows, copied verbatim, not re-derived).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** PARTIALLY SUPPORTED, narrowed after skeptic
> review — see Correction below. One clean numeric result survives fully
> (C's value, and its consequence at a physically small ε); one attempted
> comparison against v82's own real Table II data does NOT survive and is
> retracted, not merely softened.
> **Ontological/mechanistic interpretation status:** OPEN — whether v82's
> own real Table II degeneracy pattern is explainable by, or unrelated to,
> the β1-β2-ε absorption mechanism `FINDING_P165` identified is NOT
> resolved by this file (the attempted test was invalid — see below); a
> different, harder test would be needed.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing — this is a real retraction of half this file's
original claim, not a wording tweak)

A context-blind skeptic review of this file's first draft found two
substantive problems, both accepted after independent re-checking (not
taken on the skeptic's word alone):

1. **Category error (the load-bearing one).** The first draft inverted
   v82's own real Table II β1-span (`Δβ1=3.26×10⁹`, across all 7 rows) via
   `C` to compute an "implied epsilon ≈ 123," and concluded this
   unphysically large value meant Table II's real degeneracy is NOT
   caused by the ε-absorption mechanism. **This inversion is invalid.**
   `C`'s null direction `(C, C², 1)` was derived by `FINDING_P165` at
   **fixed** `H0,anchor` (Part B, explicitly conditional on that). Table
   II is the opposite: a **scan over** `H0,anchor` (67.40→73.22 km/s/Mpc)
   with `(β1,β2)` re-optimized at each value — a genuinely different
   slice of the same 3-parameter space. Dividing Table II's real `Δβ1`
   (produced by moving `H0,anchor` and refitting) by `C` (which relates a
   β1-shift to an ε-shift *at fixed `H0,anchor`*) does not compute
   anything about ε — it is a category error, not a physically
   meaningful number. **Retracted in full**, not reinterpreted.
2. **Overstated "comparable fit quality."** The first draft described
   Table II's `χ²₃₃` range (15.75→47.77, a factor of ~3.0) as "comparable
   fit quality" when framing the predicted-vs-empirical slope mismatch
   (2.644×10⁷ vs 6.157×10⁷, a factor of 2.33×) as expected/unconcerning.
   `FINDING_P165` itself only ever called `χ²₃₃≈15.75–34.14` "comparable"
   (excluding the two most extreme rows, `pct_90` and
   `planck_exact_100pct`) — this file's own span calculation used all 7
   rows, a broader range than `P165`'s own more careful framing. The
   2.33× slope mismatch is real and should not have been waved off.

**What survives, unretracted:**
- The positive control (this script's copy of TJB's own baseline
  functions reproduces his own reported/cached growth factors to <0.15%
  — see §1) — solid.
- `C = 2.644421×10⁷` (dimensionless), computed from TJB's own real z=0
  baseline values — a genuine, first-time numeric answer to `FINDING_
  P165`'s own explicitly flagged gap. Its correctness depends on `k0`
  being the mass-equivalent `k_x/c²`, not raw Joules — **verified
  structurally** (not assumed) by matching `P165`'s own symbolic force
  term `-G·β1·2·k_x·m_x·r_x/s³` against TJB's own numeric code term
  `beta_1·(-G)·2·M·(k/c²)·(R/d)/d²` — identical only if `k_x ≡ k/c²`.
- **The one clean, self-contained consequence of `C`**: at a physically
  small ε — specifically, at this project's own previously-established
  external growth-rate ceiling scale, `ε≤8.39×10⁻¹²` (`FINDING_P22`/
  `P132`) — `FINDING_P165`'s own mechanism predicts `δβ1 = C·ε ≈
  2.22×10⁻⁴`, about **14 orders of magnitude** below `β1`'s own fitted
  value (`≈1.4×10¹⁰`). This is a direct, valid application of `C` within
  its own domain (a hypothetical small ε, not Table II's real data) — it
  does **not** depend on the retracted Table-II comparison.
- **A genuine, notable empirical observation about v82's own Table II**,
  independent of the ε-mechanism question entirely: the real
  `(H0,anchor,β1,β2)` triples across all 7 rows trace an extremely tight,
  near-perfectly linear `(β1,β2)` relationship — pairwise `δβ2/δβ1`
  between every adjacent row agrees to under 1% (range 6.118–6.160×10⁷).
  This is a real fact about v82's own reported fit, worth flagging on its
  own terms (see §4), even though this file cannot say what causes it.

## 0. Premise — `NO_AUTHOR_ERROR`

Every numeric input here (baseline constants, Table II rows, code
functions) is copied verbatim from TJB's own supplemental Zenodo archive
— this file evaluates this project's own prior symbolic result (`P165`)
against those real numbers; it is not a claim about whether v82's theory
is correct, and ε remains this project's own hypothetical device (§0 of
`FINDING_P165`), not a claim about what v82's own theory contains.

## 1. Positive control

TJB's own cached run output (`archive/results/generate_all_results_
output.txt`) reports "ingredient growth factors z=1.965 → z=0.070":
`m_X=3.07, r_X=2.94, k_X=3.30`. Computing the same three ratios from
this script's own copy of his functions gives `3.0684, 2.9429, 3.2994` —
matching to <0.15% in every case. (A first attempt at this positive
control misread the label "z070" as `z=0.70` rather than `z=0.070` and
failed at ~82% error — caught immediately by the assertion itself, before
any downstream number was trusted; corrected by re-reading TJB's own
output file directly, which spells the step out in full.)

## 2. `C = d0·m0/(k0·r0)`, evaluated at v82's own real z=0 baseline

```
m0 = 1.193082e+45 kg      (TJB's own M0_kg)
d0 = 1.388555e+24 m       (TJB's own d0_m = 45.0 Mpc)
r0 = 4.056635e+22 m       (= 1.3147 Mpc; TJB's own R_of(0), overdensity-500 radius)
k0 (Joules) = 1.387964e+56 J     (TJB's own k_of(0), total ICM thermal energy)
k0 (mass-equiv) = k0/c² = 1.544319e+39 kg

C = d0*m0 / (k0_mass_equiv * r0) = 2.644421e+07   (dimensionless)
```

## 3. What this number implies at a physically small ε

`FINDING_P165`'s Part B: `δβ1 = C·δε` at fixed `H0,anchor`. At
`ε = 8.39×10⁻¹²` (this project's own external growth-rate ceiling):

```
δβ1 = C * ε = 2.644421e+07 * 8.39e-12 ≈ 2.219e-4
β1 (v82's own fitted value, unconstrained_spotlighted row) = 1.4335e+10
δβ1 / β1 ≈ 1.55e-14   (a fractional shift ~14 orders of magnitude below beta1's own value)
```

**Reading:** an unmodeled monopole-tier effect at the scale this
project's own external literature bound already permits would be
absolutely undetectable in v82's own fitting procedure via this specific
mechanism — nowhere close to a scale that could ever be confused with, or
show up in, any real feature of v82's own fit. This is the "negligible"
half of `FINDING_P165`'s own open dangerous-vs-negligible question,
answered for this one specific ε scale — **conditional on ε actually
being that small**, which this file does not establish independently.

## 4. What this file does NOT establish (expanded after correction)

1. **Does not determine whether v82's own real Table II degeneracy
   pattern is caused by, consistent with, or unrelated to the β1-β2-ε
   absorption mechanism.** The attempted test (inverting Table II's real
   `Δβ1` through `C`) was a category error — comparing a fixed-`H0,anchor`
   direction against an `H0,anchor`-varying one — and has been retracted,
   not softened (see Correction, point 1).
2. **Does not establish that Table II's own tight `(β1,β2)` linearity
   (§ "what survives," last bullet) has any connection to a monopole-tier
   effect** — it is reported as a real, independent observation about
   v82's own fit, not explained here.
3. **A genuinely decisive version of this test remains undone**: either
   (a) use TJB's own optimizer (`archive/code/generate_all_results.py`,
   present in the same Zenodo archive) to produce two or more fits at the
   *same* `H0,anchor` with different starting points, to empirically
   isolate the true fixed-`H0,anchor` `(β1,β2)` degeneracy direction and
   compare its slope directly against `C` — the skeptic review's own
   named cheapest next check; or (b) compute a real Fisher-information/
   Hessian rank at v82's own best-fit point against the full 33-point
   dataset — the direct analogue of `FINDING_P133`'s own formal method,
   applied to v82's real fit instead of this project's own `(A,g,κ)`.
   Neither is attempted here.
4. **Not a claim about v82's own theory being wrong or incomplete**
   (`NO_AUTHOR_ERROR`, §0).
5. **Does not verify `Mgas_of(z)` or the X-ray scaling-relation chain
   independently** — the positive control (§1) covers `M_of`, `R_of`,
   `k_of` end-to-end (since the growth-factor ratios depend on the full
   chain), but does not isolate `Mgas_of` on its own.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
