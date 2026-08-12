# P17 — two independent κ bounds already in this project (pulsar timing, cosmological self-energy) are consistent; cosmology binds by ~4.5 orders of magnitude

**Date:** 2026-08-12 · addresses this project's largest remaining open
blocker, named repeatedly since `FINDING_P14`: κ's absolute scale has
never been fixed anywhere in this project. Does not fix it — see Scope
below — but combines two already-derived, independent CONDITIONAL upper
bounds on κ that neither prior finding recognized existed alongside the
other.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P17_kappa_bounds_consistency_check.py`, ruff clean. Recomputes
both bounds from each finding's own stated base inputs (not copy-pasted
results), so the script is independently checkable without re-running
`FINDING_P7`'s or `FINDING_P14`'s own scripts.

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

## Are the two bounds consistent?

```
kappa_pulsar_bound / kappa_cosmo_bound = 3.422e+04   (4.53 orders of magnitude)
```

**Yes — no tension.** A κ satisfying the cosmological bound
(`κ≲1.75×10⁻⁶`) automatically and comfortably satisfies the pulsar-
survival bound (`κ≲0.06`) too, with ~4.5 orders of magnitude of margin.
The two constraints come from completely independent physical systems
(binary pulsar orbital dynamics vs. a cosmological energy-density
ceiling) and neither contradicts the other.

**The cosmological bound is the binding (tighter) constraint**, by a wide
margin. Whatever mechanism ultimately fixes κ's absolute scale, this
project's own derived `β_d=2` was never actually at risk from the pulsar
bound specifically — the cosmological constraint is far stricter and
already implies pulsar-survival as a side effect.

## A consistency note with P15/P16

`FINDING_P14`'s `Ω_φ` calculation used ONLY the self-energy channel (a
single dipole's own field energy × cluster number density), with no
cross-term contribution included. `FINDING_P15`/`FINDING_P16` later
confirmed self-energy dominates cross-terms by `~10⁻⁴` to `~10⁻⁹` at
realistic cluster separations — meaning P14's omission of cross-terms was
a good approximation, not an unexamined simplification. This does not
change any number here; it is a retrospective justification for P14's
own modeling choice, noted for completeness.

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
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P17_kappa_bounds_consistency_check.py
```
