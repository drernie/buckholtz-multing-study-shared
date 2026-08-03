# The force law's repulsive regime, tested against 1742 real clusters

**Date:** 2026-08-03 · **Branch C** — the force law against data, no bridge involved
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Result: the constraint is real but weak. One structural relation survives.**

---

## Why this test exists

Every previous strand tested a *reconstruction* — Table A1, the emailed curve, an
effective-fluid mapping. This one tests the force law itself against a
measured catalogue, and needs neither a bridge nor kSZ.

The published law

```
F = -A2/s^2 + A3/s^3 - A4/s^4
  = -(A2/s^2) [ 1 - l_d/s + l_q^2/s^2 ] ,     l_d = A3/A2 ,  l_q^2 = A4/A2
```

changes **sign**. The bracket is negative — the net force between two clusters is
*repulsive* — whenever

```
s_-  <  s  <  s_+ ,      s_pm = ( l_d +- sqrt(l_d^2 - 4 l_q^2) ) / 2
```

and that window exists at all only if `l_d > 2 l_q`.

Galaxy clusters demonstrably cluster on exactly those scales. So the observed
population of close cluster pairs constrains the sign structure directly.

## Data and method

`data/mcxc.csv` — 1742 MCXC clusters with RA, Dec, `z`, `M500c`, `R500c`.
Comoving distances from flat ΛCDM (`H0 = 67.36`, `Ω_m = 0.3153`).

**Peculiar velocities are the trap here, and the first run fell into it.** A 3D
separation built from redshift is contaminated at exactly the scales that matter:
1000 km/s of peculiar motion is ~15 Mpc of apparent line-of-sight distance, so a
"5 Mpc pair" may be nothing of the kind. The first pass used 3D separations and
its numbers are withdrawn.

The corrected test uses **projected (transverse) separation `r_p`**, which
peculiar velocities do not affect, with a line-of-sight cut carrying a ±2000 km/s
allowance, and halo exclusion at `1.9 (R500,i + R500,j)`.

```
pairs with clean projected separation : 4051
r_p percentiles [Mpc]  1st 4.35   5th 8.70   25th 27.26   50th 43.80   min 1.76
```

**The inequality that makes this rigorous:** true 3D separation `s >= r_p`
always. Repulsion requires `s < s_+`. So counting pairs with `r_p < s_+` is a
strict **upper bound** on how many observed pairs can be repelled — no
selection-function modelling required to make the bound valid.

## Result

| `l_d` [Mpc] | `l_q` [Mpc] | pairs that *can* be repelled | upper bound | median dispersal time |
|---|---|---|---|---|
| 4 | 0 | 33 | 0.81 % | 15.4 Gyr |
| **8 — this project's kSZ bound** | **0** | **172** | **4.25 %** | **20.3 Gyr** |
| 8 | 2 | 151 | 3.73 % | 20.0 Gyr |
| 8 | 4 | **0** | **0.00 %** | — (no repulsive regime) |
| 16 | 0 | 477 | 11.77 % | 44.8 Gyr |
| 25 | 0 | 891 | 21.99 % | 82.7 Gyr |

Dispersal time estimated as `t ~ sqrt( s^3 / (G M_tot |bracket|) )` — an
order-of-magnitude free-expansion estimate, not an orbit integration.

## What this establishes

**Not a falsification, and it is worth saying so plainly.** At the kSZ bound, at
most 4 % of observed pairs sit in the repulsive window, and they would take
~20 Gyr to disperse — longer than the age of the universe. A repulsive term of
this size does not visibly contradict the observed clustering of clusters.

**One clean structural relation, from data rather than theory:**

```
l_q >= l_d / 2   removes the repulsive regime at every separation
```

This is not a fit and not an assumption. It follows from the discriminant of the
bracket, and the data's role is to show that the alternative — accepting a
repulsive window — is *tolerable* rather than excluded. So the two length scales
are not independent if one wants a strictly attractive law: the quadrupole must
be at least half the dipole.

**A constraint that scales.** The upper bound grows roughly linearly in `l_d`
(0.8 % at 4 Mpc, 4 % at 8, 12 % at 16, 22 % at 25). A future measurement that
established the true 3D pair distribution — kSZ pairwise velocities do exactly
this — would convert these upper bounds into two-sided constraints.

## What this does not establish

- Nothing about `H(z)`, about MULTING's cosmology, or about any bridge.
- Nothing about whether the force law is correct — a weak constraint that a model
  passes is not evidence the model is right.
- The MCXC selection function is not modelled. This does not invalidate the upper
  bound (the `s >= r_p` inequality holds regardless) but it does mean the
  *fraction* is a property of this catalogue, not of the cluster population.
- The dispersal time is a scaling estimate. It does not account for the
  surrounding mass distribution, which dominates at these separations.
- The first run's 3D-separation numbers are withdrawn, not merely superseded:
  redshift-space contamination makes them meaningless at the relevant scales.

## Reproduction

```
data/mcxc.csv, flat LCDM H0=67.36 Om=0.3153, G = 4.300917270e-9 Mpc (km/s)^2 / Msun
r_p = theta_ij * (D_i + D_j)/2 ;  keep |D_i - D_j| - 2*2000/H0 < 40 Mpc
halo exclusion  r_p > 1.9 (R500_i + R500_j)
bracket(s) = 1 - l_d/s + l_q^2/s^2 ;  s_pm = (l_d +- sqrt(l_d^2 - 4 l_q^2))/2
```
