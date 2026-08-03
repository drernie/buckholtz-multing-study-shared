# The effective-fluid bridge fails by four to five orders of magnitude

**Date:** 2026-08-03 · **Stage:** B3, the decisive order-of-magnitude test
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## The question this answers

The proposed bridge was:

```
MULTING pair potential → generalized Layzer–Irvine energy → rho_pair, p_pair → Friedmann H(z)
```

Before building any of it, one number decides whether it can work at all: does the
interaction energy of a realistic cluster population, under the published
potential, reach the critical density?

It does not. It falls short by four to five orders of magnitude, with every
uncertain choice pushed in its favour.

This does **not** evaluate MULTING. It bounds one candidate mechanism — the
effective-fluid route — and the bound is a property of pair-interaction energy in
a clustered universe, not of the force law's correctness.

---

## Setup

```
U_2(s) = -A2/s                 from F = -A2/s^2      ordinary gravity
U_3(s) = +A2·ell_d/(2 s^2)     from F = +A3/s^3      dipole,     ell_d = A3/A2
U_4(s) = -A2·ell_q^2/(3 s^3)   from F = -A4/s^4      quadrupole, ell_q^2 = A4/A2

rho_k = (1/2) n^2 · 4π ∫ ξ_hh(s) s^2 U_k(s) ds
```

`ell_d` is exactly the quantity the kSZ strand of this project constrains, so the
two lines of work meet here.

**Every choice made to maximise the result:**

| quantity | used | reality |
|---|---|---|
| cluster number density | 1e-4 Mpc⁻³ | ~1e-5 above 1e14 M☉ |
| cluster mass | 1e15 M☉ | rich-cluster upper scale |
| correlation length `r0` | 25 Mpc | 15–25 Mpc observed |
| separation range | 1–200 Mpc | halo exclusion cuts the low end harder |

Halo exclusion, finite-size profiles and a proper mass function all **reduce**
the answer further. The number below is a ceiling.

---

## Result

`ρ_crit` as an energy density = 1.1318e22 M☉(km/s)²/Mpc³

| term | condition | ratio to ρ_crit |
|---|---|---|
| monopole (ordinary gravity) | — | **7.39e-05** |
| dipole | `ell_d` = 0.1 Mpc | 4.83e-07 |
| dipole | `ell_d` = 1 Mpc | 4.83e-06 |
| dipole | **`ell_d` = 8 Mpc — this project's kSZ bound** | **3.86e-05** |
| dipole | `ell_d` = 100 Mpc | 4.83e-04 |
| dipole | `ell_d` = 1000 Mpc | 4.83e-03 |
| quadrupole | `ell_q` = 8 Mpc | 9.29e-05 |

**Shortfall at the kSZ bound: 2.6 × 10⁴.**

To make the dipole term reach the critical density:

```
ell_d required = 2.07e5 Mpc = 207 Gpc = 46.5 × the Hubble radius (c/H0 = 4451 Mpc)
```

A length scale forty-six times the observable universe, against a kSZ bound of
order ten megaparsecs.

### Sanity check on the machinery

The monopole term is nothing but the gravitational binding energy of cluster
clustering, a quantity with a known scale. It comes out at 7.4e-5 of the critical
density — small, positive, and of the right order for large-scale structure. The
calculation is not obviously broken, and the dipole term sits in the same family.

---

## An error made and caught

The first run of this calculation mis-indexed the potential terms: the dipole was
integrated as `A2·ell_d/s` rather than `A2·ell_d/(2 s²)`, which overstated it by a
factor of `⟨s⟩/2` — roughly 4. The verdict did not change, but the numbers did,
and the corrected ones are the ones above. Recorded because the shortfall is now
2.6e4 rather than the 1.7e3 the first run printed.

---

## What this establishes, and what it does not

**Established.** An effective fluid built from MULTING pair-interaction energy
cannot drive cosmic expansion. Level 2 of the bridge programme — pair potential to
`rho_pair, p_pair` — is dead by four to five orders of magnitude, and no
refinement of halo statistics recovers that.

**Not established.** Nothing here says the force law is wrong, that MULTING is
wrong, or that no bridge exists. It says a *specific class* of bridge does not.
Energy exchange `Q` between sectors does not rescue it either: `Q` redistributes
energy, it does not create it, so if the microscopic reservoir is 10⁻⁴ of `ρ_crit`
the redistribution cannot exceed that.

**What a working bridge would have to be.** Not an effective fluid. It would have
to modify the gravitational response itself, or introduce a field carrying its own
energy density independent of the pair interactions — the covariant-action route
of level 3, not the statistical-mechanics route of level 2.

---

## How this closes the bridge programme

Together with the B0 finding that Table A1 is an AI service's output rather than a
MULTING calculation:

| level | status |
|---|---|
| B0 target | `BLOCKED_BY_TARGET_PROVENANCE` — Table A1 is generated text |
| B1 target reconstruction | cannot be done in the author's background; his `H_FLRW` column is not any standard cosmology |
| B2/B3 effective fluid | **falsified by 4–5 orders of magnitude** |
| level 3 covariant action | untouched, and now the only surviving route |

The programme's own B0 phrasing anticipated this branch: *"масштаб меньше на много
порядков — нужен отдельный механизм усиления, дополнительное поле или модификация
гравитационного отклика."* That is the branch we are on.

---

## Reproduction

The calculation is short enough to state completely. Units Mpc, M☉, km/s;
`G = 4.300917270e-9`; `c = 2.99792458e5`; `H0 = 67.36`.

```
rho_crit_energy = 3 H0^2 /(8 π G) · c^2
xi(s)  = (s/25)^-1.8
A2     = G M^2,  M = 1e15
rho_k  = 0.5 · n^2 · 4π · ∫_1^200 xi(s) s^2 U_k(s) ds,  n = 1e-4

∫ξ s ds = 3095 Mpc^2    ∫ξ ds = 404.5 Mpc    ∫ξ/s ds = 182.4
```
