# P30 — a schematic universal-coupling growth equation, honestly definitional where it needs to be, with a corrected time-convention factor

**Date:** 2026-08-13
**Origin:** user-specified, following the P22 `4π` correction and the P29
skeptic correction. P29's own withdrawn linkage to P28 left a genuine gap:
this project has never derived what a truly *universal* coupling (P23's
reading of MULTING's `g`) actually does to the linear growth equations —
only a schematic toy (P28) and Archidiacono's own *DM-only* equations
(P29). This finding closes that gap directly, before asking what real
growth-of-structure bounds constrain `ΔG/G_N` (the next, separate step).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P30_universal_coupling_linear_growth.py`

**[CORRECTED after skeptic review, same day.]** Two real issues, not just
framing overreach. **(1)** The original script's Step 2/3 called the *same*
function with *identical* arguments to compute both `S_χ` and `S_b`, then
"verified" they were equal — a syntactic tautology (`f(x)−f(x)==0`), the
exact same overclaim pattern P29's own script was corrected for earlier the
same day. **(2)** `FINDING_P29`'s own quoted baryon equation uses conformal
time (primed derivatives, single-`ℋ` friction) — the correct identity for
that convention is `(3/2)Ω_m·ℋ²=4πG_N·ρ_m·a²` (*with* a scale-factor
factor), not `4πG_N·ρ_m` (the *cosmic*-time identity), which is what the
original version used. Both fixed below: the script now makes the
definitional nature of "universal coupling" explicit rather than dressing
it as a discovered result, adds a genuinely non-trivial check (that
Archidiacono's own DM-only model gives an *asymmetric* `G_eff` between
species), and keeps `a²` explicit throughout. §3's "re-confirms P28" and
"well-posed, literature-searchable" claims are also corrected — see the
Skeptic Verdict section for the full 6-sub-verdict breakdown.

## 0. Honest scope, stated before anything else

This finding derives equations, not bounds. It does **not** search for or
apply any real CMB/BAO/growth-rate observational constraint on `ΔG/G_N` —
that is explicitly the next step this finding sets up, not something it
attempts. It also does **not** re-derive the friction (Hubble-drag) term
of the growth equation from first principles — that term is carried
through unmodified from the standard sub-horizon form, by convention, not
verified symbolically here (only the *source* term, which is what actually
changes between the DM-only and universal cases, is derived and checked).

## 1. Method

Starts from `FINDING_P29`'s own quoted baryon growth equation (the one
concrete, WebFetch-verified piece of Archidiacono's actual perturbation
system this project has). **[CORRECTED after skeptic review]** ~~rewritten
via the standard Friedmann-equation identity `(3/2)Ω_mH²=4πG_N·ρ_m`~~ —
P29's own quote uses conformal time (primed derivatives, single-`ℋ`
friction), for which the correct identity is `(3/2)Ω_m·ℋ²=4πG_N·ρ_m·a²`
(with the scale-factor `a²`, `ℋ=aH` the conformal Hubble parameter). The
original version conflated conformal `ℋ` with cosmic-time `H`, silently
dropping `a²`. Fixed below with `a²` kept explicit throughout:

```
S_baryon (Archidiacono, DM-only model, UNMODIFIED) = 4π·G_N·ρ_m·a²·(f_χδ_χ+(1−f_χ)δ_b)
```

**Replaces the DM-only topology with a universal one**, per the user's
explicit instruction. **[CORRECTED after skeptic review]** This step's
description is now split honestly into a *checked* part and a *definitional*
part, which the original blurred together: Archidiacono's own DM-only model
gives `G_eff,χ=G_N+ΔG` (their eq. 4.2's fifth-force term) but `G_eff,b=G_N`
(P29's own quoted baryon equation has no fifth-force term at all) — a
genuine, checkable **asymmetry**, verified in §2 below. A universal
coupling, by contrast, means both species get the *same* `G_eff=G_N+ΔG` —
this is the **definition** of "universal" (matching P23's established
reading of MULTING's `g`), not something derived from anything downstream;
presenting it as a "result" in the original version was the source of the
tautology issue below.

## 2. Result (sympy-verified, corrected)

**(a) Archidiacono's own DM-only model has a genuine, checked asymmetry:**

```
G_eff,χ (DM-only) = G_N + ΔG
G_eff,b (DM-only) = G_N
G_eff,χ − G_eff,b = ΔG ≠ 0   (verified, non-trivial — a real check)
```

**(b) Under universal coupling, both species' `G_eff` are equal — by
definition, not by derivation:**

```
G_eff,χ = G_eff,b = G_N + ΔG    (this IS the definition of "universal")
```

**[CORRECTED after skeptic review]** ~~S_χ − S_b = 0 (verified, not
assumed)~~ — the *original* version of this section called the same
source-term function with identical arguments for both species and
"verified" the results were equal, a syntactic tautology carrying zero
information (`f(x)−f(x)==0` is always true regardless of physics). Fixed:
the source terms *do* follow algebraically from (b)'s definition —
`S_χ=S_b=4π·(G_N+ΔG)·ρ_m·a²·(f_χδ_χ+(1−f_χ)δ_b)` — but this is a
consequence of the definition, not an independent discovery, and is
labeled as such in the corrected script.

Given matched (adiabatic) initial conditions, identical linear ODEs with
identical sources have identical solutions: `δ_χ(t)=δ_b(t)` for all time.
**[CORRECTED after skeptic review]** ~~This re-confirms P28's earlier
result... now derived within a fuller equation structure — an independent
cross-check.~~ It does **not** independently re-confirm anything. P28's
own result and this one **encode the identical load-bearing assumption**
(universal = same `G_eff` for both species) — P28's toy model set
`G_eff,c=G_eff,b` directly; this finding does the same, only via a
different-looking template. Two derivations sharing their defining
assumption cannot cross-verify each other on that assumption — agreement
was close to definitionally guaranteed, not a discovery. Honest
restatement: *the same conclusion follows here from encoding the same
defining assumption in a construction closer to Archidiacono's own quoted
equations* — not an independent confirmation.

**(c) The combined single-species equation for total matter reduces
exactly to the user-specified target form (with the corrected `a²`
factor).** Defining `δ_m:=f_χδ_χ+(1−f_χ)δ_b` and substituting
`δ_χ=δ_b=δ_m` (licensed by (b)):

```
δ_m'' + ℋδ_m' = 4π·G_eff·ρ_m·a²·δ_m,   G_eff = G_N + ΔG
```

Verified symbolically that the derived source term matches this target
exactly (`sp.simplify` confirms zero difference). **[CORRECTED after
skeptic review]** ~~This is the standard, textbook single-species linear
growth equation~~ — this is a *schematic* target equation, valid only in
the sub-Compton (`r≪m_φ⁻¹`), scale-independent, time-independent-`ΔG`
regime (§4 spells out the full list of restrictions); calling it "the
standard textbook equation" without those qualifications overstated how
directly it maps onto real modified-gravity literature.

## 3. Why this matters, corrected scope

This closes the gap `FINDING_P29`'s own corrected §3 flagged explicitly:
deriving the universal-coupling analogue of Archidiacono's equations "from
scratch (baryons sourcing and receiving the fifth force too, not just
gravity)" — done here, within the stated regime. **[CORRECTED after
skeptic review]** ~~a well-posed, literature-searchable question~~ — the
honest next question is: *what real growth-of-structure observational
bounds exist on `ΔG/G_N`?* — but this is **not** a straightforward lookup.
Standard modified-gravity growth-rate literature (Planck MG constraints,
DES-Y3, ISiTGR, MGCAMB) typically parametrizes deviations via
time-and-scale-dependent functions `μ(a,k)`/`Σ(a,k)`, not a single constant
`ΔG`. A constant, scale-independent `ΔG/G_N−1` is the *simplest special
case* of these parametrizations, and existing tools can in principle
constrain it — but translating a reported bound into a number for `ΔG/G_N`
requires real, non-trivial modeling choices (pivot redshift, marginalizing
over background parameters, degeneracy with the structure-growth
amplitude itself) not previewed or attempted here. This remains a better-
posed question than force-fitting Archidiacono's own DM-only-specific `β`
bound onto a structurally different coupling (P23, P28, P29's
now-three-times-recorded caveat on `FINDING_P22`'s original mapping) — but
"well-posed" should not have been read as "easy."

## 4. What this does NOT establish

1. **Any numeric bound on `ΔG/G_N`.** No literature search performed, no
   CMB/BAO/growth-rate data consulted. This is a **derivation-only**
   finding — the natural next step (a real bound search) is explicitly
   deferred, not attempted, and per §3 (corrected) is real, non-trivial
   work, not a simple lookup.
2. **A re-derivation of the friction/Hubble-drag term.** Carried through
   unmodified from the standard sub-horizon growth-equation form, by
   convention; only the *source* term (what changes between DM-only and
   universal coupling) was derived and verified here.
3. **That this fully replaces Archidiacono's own eq. 4.2/4.4 mechanism.**
   Those equations describe a specific, screened/mediator-field
   construction (a genuine field `s` with its own dynamics, Compton
   wavelength, etc.). This finding uses their *net effect on the growth
   equations* (a `G_N→G_eff` shift) as the target form, which is the
   standard leading-order behavior expected for `r≪m_φ⁻¹` (per the same
   short-distance regime Archidiacono's own text — quoted in `FINDING_P22`
   — states directly), but does not re-derive the full field-theoretic
   machinery behind it.
4. **[Added after skeptic review] Scale-independence of `ΔG`.** The target
   equation implicitly assumes `k≪a·m_φ` throughout (the sub-Compton limit
   where the scalar's own gradient/mass term is negligible next to the
   source). Near or beyond `k~a·m_φ`, Yukawa-type suppression sets in and a
   constant `ΔG` is no longer the right description — not modeled here.
5. **[Added after skeptic review] Time-independence of `ΔG`.** Treated as a
   constant throughout; Archidiacono's own mediator field `s(a)` in general
   evolves with the background, which could make `ΔG` itself time-dependent
   — not addressed.
6. **[Added after skeptic review] The adiabatic-initial-condition
   assumption.** `δ_χ(t)=δ_b(t)` under universal coupling follows only if
   the two species start with matched (adiabatic) initial perturbations —
   stated in §2 but not elevated to a full caveat until now; a genuinely
   different (isocurvature) initial condition would not give this result
   even under a universal coupling.
7. **A resolution of what value `ΔG` actually takes.** Only its
   *functional role* in the growth equation — connecting it to a number
   still requires either (a) the direct-`G`-measurement route flagged as
   open in P28, or (b) the growth-of-structure bound route this finding
   sets up, neither pursued to a number here.
8. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   built by generalizing a published external paper's own equations — not
   a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P30_universal_coupling_linear_growth.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `FINDING_P29_archidiacono_own_equations_absolute_growth.md`
(corrected), `FINDING_P28_archidiacono_differential_blindness.md`
(corrected), and `FINDING_P23_target_population_confirmed_universal.md`
(corrected) — no session history. 6 sub-verdicts, per Step 8a (not merged):

- **A** (Friedmann-identity substitution): **WEAKENED** — the identity
  `(3/2)Ω_mH²=4πG_Nρ_m` is correct for *cosmic*-time `H`, but P29's own
  quoted equation uses conformal-time `ℋ` (primed derivatives, single-`ℋ`
  friction); the correct identity for that convention carries a scale-factor
  `a²` this finding's original version silently dropped, mixing conventions.
  Independently re-derived by hand before accepting: confirmed `(3/2)Ω_mℋ²
  =4πG_Nρ_m·a²` (with `a²`), not `4πG_Nρ_m`. *Applied: FIXED — `a²` kept
  explicit throughout §1–§2 and the script.*
- **B** (the "universal coupling" `G_N→G_eff` construction and its implicit
  regime): **WEAKENED** — physically well-motivated in the sub-Compton,
  Newtonian-limit regime (`k≪a·m_φ`), but §2's original "CONFIRMED"/
  "standard textbook" language did not inherit the regime restriction §4
  already (correctly) stated. *Applied: FIXED — §2's confidence language
  pulled back, §4 gains two new explicit caveats (scale- and
  time-independence of `ΔG`).*
- **C** ("re-confirms P28... within a fuller equation structure"):
  **FALSIFIED** — the two derivations share the identical load-bearing
  assumption (universal = same `G_eff` for both species); agreement between
  them is close to definitionally guaranteed, not an independent
  cross-check. Same overclaim pattern already caught in this session's own
  P22 and P29 corrections ("independent" claims that turn out to share their
  premise or their source). *Applied: FIXED — §2 corrected to state the
  honest relationship: the same conclusion follows from encoding the same
  assumption in a different template, not an independent confirmation.*
- **D** (§3's "well-posed, literature-searchable" framing): **WEAKENED** —
  broadly directionally right but glossed over real translation work.
  Standard modified-gravity growth-rate literature (Planck MG, DES-Y3,
  ISiTGR, MGCAMB) parametrizes deviations via time-and-scale-dependent
  `μ(a,k)`/`Σ(a,k)` functions, not a single constant `ΔG` — a constant `ΔG`
  is the simplest special case, but translating a reported bound into a
  number requires real modeling choices not previewed. *Applied: FIXED —
  §3 corrected, "well-posed" retained but "easy"/implied-lookup framing
  removed.*
- **E** (§4 disclaimer completeness relative to §2's original confidence):
  **WEAKENED** — real gap; scale-independence, time-independence, and the
  adiabatic-initial-condition assumption were not elevated to explicit
  caveats. *Applied: FIXED — three new caveats added to §4.*
- **F** (is the sympy verification substantive or tautological — **the
  single most consequential catch**): **FALSIFIED as substantive
  verification.** The original script's Step 2/3 called the *same* function
  (`universal_coupling_source`) with *identical* arguments to compute both
  `S_χ` and `S_b`, then checked `S_χ−S_b==0` — a syntactic tautology
  (`f(x)−f(x)` is always `0`), carrying zero information about physics.
  Independently confirmed by direct re-reading of the script's own source
  before accepting (lines calling the identical function twice with
  identical arguments). Exactly the same class of error P29's own script
  was corrected for earlier the same day (sympy verifying transcription
  arithmetic, not physics). *Applied: FIXED — script rewritten to (1) make
  the "universal" case's equal-`G_eff` explicit as a *definition*, not a
  "check," and (2) add a genuinely non-trivial verification instead: that
  Archidiacono's own DM-only model gives an *asymmetric* `G_eff` between
  species (`G_eff,χ−G_eff,b=ΔG≠0`), a real, checkable fact from P29's own
  quoted equations.*

**Not a core-predicate-false kill of the underlying physical claim** — a
universal coupling genuinely does mean identical `G_eff` for both species,
and the resulting single-species equation is a real, correctly-derived
consequence of that definition. **This is a framing/scope issue compounded
by one genuine construction error** (the tautological sympy "check," sub-
verdict F) and one genuine notational error (the `a²`-dropping, sub-verdict
A) — neither invalidates the qualitative conclusion, both required real
fixes, not mere softening. The skeptic's own one-line summary: *"What
survives: universal coupling is source-symmetric under matched adiabatic
ICs (already known from P28), and reducing to the standard growth-equation
form in the sub-Compton limit is the right structural target for a future —
non-trivial — MG bound search on constant ΔG."*
