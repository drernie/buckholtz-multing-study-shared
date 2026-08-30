# FINDING P168 — does the Cosmic Chronometer sample's known systematic
# covariance close FINDING_P167's own ~1.7-χ² margin?

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 predictive (real numerical GLS fit against a
documented systematic-covariance structure)
**Script:** `P168_cc_covariance_sensitivity_check.py` — positive control
(zero systematic amplitude exactly recovers `FINDING_P167`'s own
diagonal-only `χ²` values, to `<0.01` tolerance) + two variants bounding
a genuine, disclosed scope ambiguity.
**Covariance source:** Moresco, Jimenez, Verde, Cimatti & Pozzetti,
"Setting the Stage for Cosmic Chronometers II," ApJ 898, 82 (2020),
`arXiv:2003.07362` — abstract fetched and quoted directly
`[VERIFIED-arXiv]`, not accepted from an agent report alone.
**Verdict (final, post-skeptic — see "Correction" below, this fixes a
real code bug and a real conceptual mischaracterization, not just
wording):** `WITHIN THE SPECIFIC, DOCUMENTED SYSTEMATIC COMPONENT THIS
FILE CAN ACTUALLY CONSTRUCT (SPS-model/IMF choice, the paper's own
headline "5.4% at z=0.2 to 2.3% at z=1.5" additional systematic, applied
ONLY to the 31 actual Cosmic Chronometer points as the paper's own rank-1
fully-correlated structure, Eq. 9), THE DUMMY MODEL'S OWN ACHIEVABLE `χ²`
DECREASES (`14.073`→`13.99` unconstrained, `14.107`→`14.01` anchored,
Variant A; `13.64` both regimes, Variant B) — but THIS DECREASE IS
LARGELY A GENERIC MATHEMATICAL FACT ABOUT ENLARGING A COVARIANCE MATRIX
(Loewner ordering: for ANY fixed residual vector, adding a positive-
semi-definite term to a covariance can only lower `rᵀCov⁻¹r`, whether or
not the model is refit), NOT SPECIFICALLY EVIDENCE THAT THE DUMMY MODEL'S
OWN FLEXIBILITY IS "ABSORBING" THE SYSTEMATIC. THIS FILE CANNOT TELL
WHETHER MULTING'S OWN `χ²=15.75/15.78` WOULD DECREASE BY A COMPARABLE OR
LARGER AMOUNT UNDER THE SAME TREATMENT — it only refits the dummy side;
recomputing MULTING's own number under this covariance would need
numerically integrating v82's own full trajectory across the entire
fitted range, not attempted here. Given the Loewner-ordering fact above,
THIS IS PLAUSIBLE, NOT UNLIKELY. The honest state, corrected: this file
does NOT show the `FINDING_P167` margin "widens" in any meaningful sense
— it shows the dummy model's own `χ²` doesn't get worse under one
specific, partially-scoped systematic, which is weaker information than
originally stated. A second, separately-disclosed scope gap (whether
this Moresco-group-specific systematic should even apply to the ~16
non-Moresco points in the standard 31-point compilation) also remains
open. This file narrows the space of remaining explanations only
slightly; it does not close `FINDING_P167`'s own named residual gap.`
**Correction (2026-08-31, context-asymmetric skeptic-caught, two points,
both independently re-verified before applying):** the first draft (a)
contained a real code bug, not just a wording issue: `_build_covariance`
applied the Cosmic-Chronometer-specific SPS/IMF systematic to ALL of
`FULL_33`, including the SH0ES and DESI points — neither is a Cosmic
Chronometer measurement (SH0ES is Cepheid-calibrated distance-ladder,
DESI is BAO), and neither has any documented connection to Moresco et
al. 2020's own stellar-population-synthesis analysis. Fixed by restricting
the systematic construction to the first `len(CC_DATA)=31` entries only
(`_build_covariance`'s new `n_cc` parameter); Variant A's numbers changed
as a result (Variant B's did not, since SH0ES/DESI happened to fall
outside its `[0.2,1.5]` restriction anyway — the bug was silently masked
there, not absent). (b) The original mechanistic explanation for the
`χ²` decrease ("a model with free parameters can partially absorb a
fully-correlated systematic through its own fit") was imprecise to the
point of misleading: independently re-derived via the Sherman-Morrison
identity, `(D+vvᵀ)⁻¹ = D⁻¹ − (D⁻¹v)(D⁻¹v)ᵀ/(1+vᵀD⁻¹v)`, confirming that
for **any fixed residual vector**, `rᵀ(D+vvᵀ)⁻¹r ≤ rᵀD⁻¹r` — the
covariance-enlargement effect exists independent of refitting or model
flexibility; only the *additional* margin beyond this generic baseline
could plausibly reflect fit flexibility, and this file does not isolate
that additional margin from the generic effect. Consequently, the
skeptic's own sharpest point stands: since this Loewner-ordering effect
is generic, MULTING's own `χ²` would plausibly also decrease under the
same covariance treatment, by a comparable or larger amount — making
this file's own one-sided comparison much weaker evidence than the
original draft's "margin widens" framing implied. Corrected throughout.
**Continues:** `FINDING_P167`'s own "does NOT establish" point 6 — "v82
never states diagonal vs. full-covariance weighting... the natural next
check, not attempted in this session."

## 0. Premise — `NO_AUTHOR_ERROR`

This file investigates a property of the *reference dataset* (the public
Cosmic Chronometer compilation) and this project's own dummy-model
comparison — not v82's own theory or TJB's own methodology, which
remains unaddressed either way by this file.

## 1. What was actually found and checked — `[VERIFIED-arXiv]`

A background research pass located the actual paper that quantifies
Cosmic Chronometer systematic covariance: `arXiv:2003.07362`. Its own
abstract, fetched and read directly (not from an agent's paraphrase):

> "For current H(z) measurements, where the uncertainties due to
> metallicity and star formation history were already included... the
> additional systematic uncertainty is between 5.4% (at z=0.2) and 2.3%
> (at z=1.5)."

This confirms two structural facts used directly in this file: (a) the
*already-published* CC `σ_H` values (the ones `FINDING_P167` already
used, diagonal) already incorporate metallicity and star-formation-
history systematics — so the *additional*, not-yet-incorporated
systematic is specifically the stellar-population-synthesis-model/IMF
choice; (b) the paper's own Eq. 9 constructs this component as a rank-1
outer product, i.e. **fully correlated across all redshift points**, not
restricted to same-survey pairs — confirmed independently by the
background agent reading the paper's own public code repository
(`gitlab.com/mmoresco/CCcovariance`) directly, not just its prose.

## 2. Honest scope limitations of this specific file — stated up front, not discovered post hoc

1. **Only two anchor points, not the full curve.** The paper's own
   Table 3 gives this fraction at 29 discrete redshift bins; this file
   has only the abstract's two headline values and interpolates linearly
   between them. This is a rough approximation of the true `η̂(z)` shape.
2. **Genuine, unresolved applicability gap.** The paper's own covariance
   construction is built specifically from the Moresco group's own
   D4000-method measurements. The standard 31-point compilation also
   includes points from Simon et al. (2005), Stern et al. (2010), Zhang
   et al. (2014), and Ratsimbazafy et al. (2017) — different
   measurement methodology (full spectral fitting, not the D4000-slope
   technique this systematic analysis is built around). Neither the
   paper nor this file establishes whether the SAME systematic fraction
   should apply to those points. **Two variants are run to bound this**:
   Variant A (apply to all 31 points, a conservative sensitivity bound)
   and Variant B (apply only within the paper's own analyzed range,
   `0.2≤z≤1.5`, zero elsewhere).
3. **Flat extrapolation** outside `[0.2, 1.5]` in Variant A, rather than
   the paper's own actual (unknown, to this file) curve behavior there.

## 3. Result — `[VERIFIED-python]`, positive control passed

`test_positive_control_zero_systematic_recovers_p167_diagonal_result`:
setting the systematic amplitude to zero reproduces `FINDING_P167`'s own
diagonal-only `χ²` values (`14.073`, `14.107`) to within `0.01` —
confirms the GLS machinery is implemented correctly before trusting it
on the nonzero case.

```
Variant A (systematic on the 31 CC points only, corrected):
  Unconstrained: chi2=13.989  (was 14.073)   Delta vs MULTING = -1.761
  Anchored:      chi2=14.008  (was 14.107)   Delta vs MULTING = -1.772

Variant B (systematic only within [0.2,1.5], CC points only):
  Unconstrained: chi2=13.637  (was 14.073)   Delta vs MULTING = -2.113
  Anchored:      chi2=13.637  (was 14.107)   Delta vs MULTING = -2.143
```

In both variants and both comparison regimes, the dummy model's own
achievable `χ²` **decreases** relative to `FINDING_P167`'s diagonal-only
result. **This is expected, and largely uninformative on its own**
(skeptic-caught correction, above): via the Sherman-Morrison identity,
enlarging a diagonal covariance by any positive-semi-definite term
mechanically lowers `rᵀCov⁻¹r` for *any* fixed residual `r` — a model
does not need to be refit, or even be flexible, for this to happen. Only
the portion of the decrease *beyond* this generic floor could plausibly
reflect the dummy model's own flexibility tracking the systematic — this
file does not isolate that portion, so no claim about "the margin
widening" is actually licensed by this result.

## 4. Why this narrows, but does not close, the original question

This file only refits the **dummy** model under the covariance-aware
objective. It does **not**, and could not without substantially more
work, recompute MULTING's **own** `χ²=15.75/15.78` under the same
treatment — that would require numerically integrating v82's own full
coupled `(s,z,H)` dynamical system across the entire fitted redshift
range (`z∈[0.07,2.33]`), using its own reported best-fit `(β1,β2,
H0,anchor)`, not merely the near-`z=0` perturbative expansion this
project's own `P161`/`P165` machinery already has. Without that, this
file's comparison still implicitly holds TJB's own reported number fixed
under whatever convention he used (unconfirmed, per `FINDING_P167`) while
only the dummy side is corrected for a specific, documented systematic.

**What this file actually establishes, honestly (corrected, weaker than
first stated):** almost nothing about whether `FINDING_P167`'s own margin
survives. The observed `χ²` decrease for the dummy model is expected
under simple linear algebra (Loewner ordering, §3) regardless of which
model is being fit — so, absent a way to also recompute MULTING's own
`χ²` under the identical covariance, this file cannot distinguish
"the margin is robust" from "both models' `χ²` would drop by a similar
amount, leaving the margin roughly where `FINDING_P167` left it, or
worse." The one thing this file does establish is negative and narrow:
it found no sign that accounting for this ONE specific, documented
systematic makes the dummy model's own case *weaker* — but that is a
much smaller claim than "the margin widens," and does not by itself
support any directional conclusion about the comparison as a whole.

## 5. What this file does NOT establish

1. **Not a claim about v82's own theory or methodology**
   (`NO_AUTHOR_ERROR`, §0).
2. **Does not recompute MULTING's own `χ²` under this covariance
   treatment** — the central remaining gap, §4. A fuller test would need
   to numerically integrate v82's own full dynamical system across the
   whole fitted range, not attempted here.
3. **Does not resolve whether the Moresco-group-specific systematic
   applies to the ~16 non-Moresco points** in the standard compilation
   (§2 point 2) — Variants A/B bound this, do not resolve it.
4. **Does not reproduce the paper's own full 29-bin `η̂(z)` table** —
   only linearly interpolates between its two headline endpoint values
   (§2 point 1).
5. **Does not account for the OTHER systematic components** the same
   paper discusses (metallicity, star-formation-history) — these are
   stated to already be incorporated into the published `σ_stat` values
   this project's own `CC_DATA` already uses, per the paper's own
   abstract, and are not re-added here to avoid double-counting.
6. **Does not settle `FINDING_P167`'s own open question, and does not
   even narrow it as much as the first draft claimed** (skeptic-caught
   correction) — the observed `χ²` decrease is largely a generic
   consequence of covariance enlargement (Loewner ordering, §3), not
   specific evidence about the dummy model vs. MULTING comparison; a
   genuinely informative test would need to apply the same covariance
   treatment to MULTING's own `χ²` too (point 2 above), not attempted.
7. **Contained, and has since fixed, a real code bug** (Correction,
   above) — the first draft applied the CC-specific systematic to SH0ES
   and DESI as well, which are not Cosmic Chronometer measurements.
