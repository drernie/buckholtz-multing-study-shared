# P17 — two pre-existing κ upper bounds don't contradict each other (a near-tautology for one-sided bounds), and the tighter one's own units don't check out

~~two independent κ bounds already in this project (pulsar timing,
cosmological self-energy) are consistent; cosmology binds by ~4.5 orders
of magnitude~~ **[CORRECTED after skeptic review — retitled]**

**Date:** 2026-08-12 · corrected 2026-08-12 after context-blind skeptic
review · originally set out to address this project's largest remaining
open blocker, named repeatedly since `FINDING_P14`: κ's absolute scale
has never been fixed anywhere in this project.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P17_kappa_bounds_consistency_check.py`, ruff clean. Recomputes
both bounds from each finding's own stated base inputs (not copy-pasted
results), so the script is independently checkable without re-running
`FINDING_P7`'s or `FINDING_P14`'s own scripts.

**[CORRECTED after skeptic review — read before the rest of this file]**
A context-blind skeptic review found the arithmetic CONFIRMED-REAL but the
interpretive claim WEAKENED, for three independent reasons, all applied
below: (1) **a genuine dimensional-analysis catch, independently
re-verified**: `Ω_φ` (P14's quantity, reused here unchanged) has units
`kg/m`, not dimensionless — so `κ_cosmo_bound`'s absolute numeric value is
currently unverifiable, not just imprecise (propagated back to
`FINDING_P14` §6, new). (2) For two one-sided upper bounds, "consistent /
no tension" is logically equivalent to "the tighter bound is tighter" —
not independent information; the finding's own framing overstated this.
(3) **A citation error of my own, independent of the skeptic's search
limitations**: the "consistency note" below originally cited
`FINDING_P15`/`FINDING_P16`'s cross-term ratio as "~10⁻⁴ to ~10⁻⁹" — the
`~10⁻⁹` figure was P15's own already-retracted, misattributed number
(see `FINDING_P15`'s own correction); the correct range is `~4×10⁻⁵` to
`~1.4×10⁻⁴`. Fixed below.

## Scope limit, stated up front

**This does NOT fix κ.** Both bounds derived below are one-sided upper
bounds (`κ ≲ X`); neither provides a lower bound or a specific value. κ
could, for all either constraint says, be exactly zero — in which case
the entire k-sector dipole coupling this whole bridge track (P1–P16) has
been probing would simply vanish. `FINDING_P14`'s open problem (κ's
absolute scale is unfixed project-wide) remains open after this finding.
What this establishes is narrower: **the two independent bounds that
already existed in this project's own prior work do not contradict each
other**, and identifying which one is currently binding. Per
NO_AUTHOR_ERROR: entirely about this project's own reconstruction.

## The two bounds, each already present in prior work

**Bound 1 — `FINDING_P7`, binary pulsar J0737-3039, rotational-only `k`.**
`FINDING_P7`'s own caveat (added after the `FINDING_P14` skeptic review)
already states: *"at κ=1 (as computed), β_d≲0.12 excludes β_d=2 by ~1.2
orders; at κ≈0.06 instead, the bound becomes β_d≲2.0"* — i.e., **if**
this project's own derived `β_d=2` (`FINDING_two_charge_completion.md`,
zero free parameters after κ) is to survive the pulsar-timing bound on
`ℓ_d/r`, κ must be `≲0.06`. This script re-derives that number directly
from P7's own base inputs (`β_d=2`, `u_A=0.23m` at κ=1, pulsar bound
`0.055`), not by quoting it:

```
kappa_pulsar_bound = 0.055 / (2 * 2 * 0.23) = 0.0598
```

**Bound 2 — `FINDING_P14`, cosmological self-energy, Gate-4 cluster-
density ceiling.** `FINDING_P14`'s own caveat states: *"Omega_phi(kappa)
~3.3e11*kappa^2, so Omega_phi<=1 gives kappa<=1e-6"*. Re-derived here from
P14's own base physical inputs (same `(8π/3)p²/r_min³` self-energy
formula, same Gate-4 maximally-generous cluster-density bound,
`k/mc²=1.7×10⁻⁶`, cluster radius `1.5 Mpc`, mass `10¹⁵ M☉`):

```
Omega_phi(kappa=1) = 3.2773e+11
kappa_cosmo_bound = 1/sqrt(3.2773e11) = 1.7468e-06
```

Matches P14's own `~1e-6` figure — precise value not previously computed
to this many digits.

**[CORRECTED after skeptic review — read before trusting this number.]**
`Ω_φ` as computed by `FINDING_P14`'s own formula (reused unchanged here)
has units `kg/m`, not dimensionless — independently re-verified: `p_i` has
units `kg·m`, so `(8π/3)p_i²/r_min³` has units `(kg·m)²/m³ = kg²/m`, and
carrying that through `ρ_φ=n·E_self`, `Ω_φ=ρ_φ/ρ_crit` gives `kg/m`
overall, not a pure number. A missing normalization/coupling constant
(units `m/kg`) is silently assumed to be `1` in some unstated unit
system — its true value is unknown and could be many orders of magnitude
from `1`. **`κ_cosmo_bound=1.7468×10⁻⁶` is therefore not just imprecise —
its absolute scale is currently unverifiable.** Full detail added to
`FINDING_P14` §6 (new). The `κ²` scaling relationship itself remains
valid regardless of this issue (any fixed but unknown normalization
constant cancels out of the *scaling*, just not the specific number).

## Are the two bounds consistent?

```
kappa_pulsar_bound / kappa_cosmo_bound = 3.422e+04   (4.53 orders of magnitude)
```

~~Yes — no tension... The cosmological bound is the binding (tighter)
constraint, by a wide margin.~~

**[CORRECTED after skeptic review.]** The arithmetic ratio is correct, but
three things weaken what it can be said to establish:

1. **For two one-sided upper bounds, "consistent" carries no information
   beyond "the tighter one is tighter."** `κ≲A` and `κ≲B` never
   contradict each other — the only question is which of `A`, `B` is
   smaller. Presenting "consistent" and "cosmology binds" as two separate
   findings was double-counting one arithmetic fact.
2. **The two bounds rest on entirely non-overlapping assumption sets that
   never actually connect to each other.** Bound 1 is conditional on
   trusting `β_d=2` and the rotational reading of `k` (P7's own §4 flags
   a competing reading giving a very different number). Bound 2 is
   conditional on Gate-4's ceiling, `r_min=r_cluster`, P14 §1's still-
   unresolved self-energy-vs-cancellation tension, and — as just found —
   an unverified dimensional normalization. "Both conditionals hold and
   don't clash" says nothing about the actual physical κ; it describes
   two hypotheticals under their own separate premises.
3. **Given how differently-scaled the two source systems are** (a single
   pulsar's own measured spin period vs. an entire cosmological
   population's assumed self-energy budget, spanning `>20` orders of
   magnitude in the underlying physical quantities before any square
   root), **there was never a realistic parameter regime in which these
   two specific computations could have come out contradictory.**
   "Checked for consistency, found none" is not informative when the
   scale disparity structurally guarantees the outcome.

**Revised, defensible statement:** of the two pre-existing upper bounds on
κ in this project, the cosmological one (`FINDING_P14`) currently produces
the numerically smaller figure — but that figure's own dimensional
validity is unconfirmed (§ above), and "smaller" was close to guaranteed
by the vast difference in physical scale between the two source systems,
not a substantive cross-check. The precise "`4.53` orders of magnitude"
should not be read as a meaningful measurement — it inherits both the
dimensional uncertainty above and every modeling uncertainty already
flagged in `FINDING_P14` (cluster mass, `r_min` choice, Gate-4 looseness).

## A consistency note with P15/P16

**[CORRECTED after skeptic review — citation error, independent of the
skeptic's own search limitations.]** ~~self-energy dominates cross-terms
by ~10⁻⁴ to ~10⁻⁹~~ **The correct range, read directly from
`FINDING_P15`'s corrected §4 and `FINDING_P16`'s §Results, is `~4×10⁻⁵`
(P15's ring, Regime B) to `~1.4×10⁻⁴` (P16's sphere, Regime B')** — the
`~10⁻⁹` figure this section originally cited was P15's own already-
retracted number (that value belonged to a different regime, misattributed
in P15's first draft, and corrected there before this file was written —
citing it here anyway was this file's own error, not inherited).

`FINDING_P14`'s `Ω_φ` calculation used ONLY the self-energy channel, with
no cross-term contribution included. `FINDING_P15`/`FINDING_P16`
confirmed self-energy dominates cross-terms by `~4×10⁻⁵` to `~1.4×10⁻⁴` at
realistic cluster separations — meaning P14's omission of cross-terms was
a reasonable approximation. This does not change any bound derived above
(both bounds are already dominated by the dimensional-normalization issue,
which is a much larger source of uncertainty than the sub-percent
cross-term correction would be even if included).

## What this does NOT establish

1. **A value, or even a nonzero lower bound, for κ.** Both bounds here
   are upper bounds only. κ=0 (no k-sector coupling at all) satisfies
   both trivially.
2. **That the cosmological bound (`FINDING_P14`) is itself reliable
   beyond its own stated caveats** — Gate-4's maximally-generous
   cluster-density assumption, the `r_min=r_cluster` modeling choice, and
   the `Ω_φ`-vs-Archidiacono-`β` mapping gap (`FINDING_P14`'s caveats 2-3)
   are all unaffected by this finding.
3. **That the pulsar bound (`FINDING_P7`) is itself the tightest possible
   astrophysical constraint** — only that it is not the binding one
   *relative to* the cosmological bound specifically; other systems were
   not surveyed here.
4. **That `Ω_φ`'s absolute numeric value (hence `κ_cosmo_bound`'s absolute
   value) is currently trustworthy.** [Added after skeptic review.] A
   missing normalization constant, undiscovered by this or any prior
   finding, makes `Ω_φ` as computed dimensionally inconsistent with an
   energy-density fraction. See `FINDING_P14` §6.
5. **That comparing these two specific bounds constitutes a meaningful
   independent cross-check on κ.** [Added after skeptic review.] Given
   how differently-scaled and how differently-conditional the two source
   systems are, their numeric non-contradiction was close to structurally
   guaranteed, not a substantive finding in its own right.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic verdict (Step 8a, context-blind — claim + code + cited files only)

Two separate verdicts, not merged. The skeptic could not locate
`FINDING_P15`/`FINDING_P16` at the paths it searched (a tool-access
limitation on its own end, independently confirmed by re-listing this
directory — both files exist and are committed); its verdict on the
"consistency note" citation is therefore marked NEEDS-REAL-DATA in its
own report, but the citation error it flagged as unverifiable turned out
to be real anyway, caught independently by re-reading the actual files
directly (see correction above) — not by the skeptic's own search.

**(1) Math/numerical content: CONFIRMED-REAL, with one serious caveat.**
Both re-derived bounds (`0.0598`, `1.7468×10⁻⁶`) independently
hand-verified by the skeptic and match P7's/P14's own stated figures
exactly — the self-checking re-derivation from base inputs works as
designed. The serious caveat: `Ω_φ`'s dimensional inconsistency
(inherited from `FINDING_P14`, not introduced by this script, but not
re-flagged here either) means `κ_cosmo_bound`'s specific numeric value is
not verified to be physically meaningful, only arithmetically consistent
with P14's own (also-not-dimensionally-verified) formula.

**(2) Interpretive claim ("consistent, cosmology binds by 4.53 orders"):
WEAKENED, close to FALSIFIED for the "meaningful consistency check"
framing specifically.** The relative-ordering claim survives (cosmology's
number is smaller) but the "consistency check" framing is near-tautological
for one-sided bounds, the two source systems' assumption sets never
overlap, and the disparity in scale made contradiction essentially
impossible from the outset — none of which was acknowledged in the
original draft. Applied per Response Matrix: retitled (Fix), dimensional
caveat added prominently and propagated to `FINDING_P14` §6 (Fix), the
tautology and non-overlapping-conditionals points added explicitly (Fix),
precision claim downgraded (Fix), citation error corrected (Fix — my own
error, not the skeptic's finding, though flagged by the same review
pass). No response fell to core-predicate-false — the raw arithmetic
survives; only its physical meaningfulness and the strength of the
"consistency" framing are downgraded.

## Reproduction

```bash
python experiments/20260803-bridge/P17_kappa_bounds_consistency_check.py
```
