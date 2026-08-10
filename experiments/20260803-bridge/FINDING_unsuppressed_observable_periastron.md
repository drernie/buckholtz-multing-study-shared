# The unsuppressed observable: periastron advance — where the k-tiers enter at full strength

**Date:** 2026-08-10 · answers the closing question of `FINDING_xi2_and_forecast.md`:
find an observable where the `k·k` tier is not suppressed by `ℓ_d/r`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verification:** two positive controls (Newton → 0 exactly; GR → `6πGM/(ac²)` exactly);
J0737-3039 GR prediction reproduced to 0.04 %

---

## 1. Why the suppression exists, and what it selects

In every isotropically-smoothed cosmological observable the k-tiers appear as
`ℓ_d/r` and `ℓ_q²/r²` corrections to the monopole. With
`ℓ_d/r = 2β_d(k/mc²)(r_A/r_sep)`, the suppression is the product of two small
numbers — internal-kinetic fraction and compactness. Scanned across systems
(clusters measured from this project's own 548-cluster sample):

| system | `k/(mc²)` | `r_A/r_sep` | `ℓ_d/r` per `β_d` |
|---|---:|---:|---:|
| cluster pair, cosmological | 1.7e−6 | 1.0e−2 | **3.5e−8** |
| Sun–Earth | 1.0e−6 | 4.7e−3 | 9.3e−9 |
| galaxy pair | 4.5e−7 | 2.0e−2 | 1.8e−8 |
| binary pulsar B1913+16 | 0.10 | 5.1e−6 | 1.0e−6 |
| double NS, 100 km | 0.10 | 0.10 | 2.0e−2 |
| BBH at ISCO | 0.25 | ~1 | **0.5** |

Nine decades of range, and **cluster pairs — the system the whole MULTING corpus is
built on — are the worst case in the list.** Compact binaries are the best.

## 2. The observable: apsidal precession, where the dipole is *not* suppressed

For a near-circular orbit under `F = GM/r² − GA₃/r³ + GA₄/r⁴` (MULTING's own signs),
the Binet stability frequency gives, linearised:

```
Delta_phi_MULTING = (pi/a) * ( -ell_d + 2 ell_q2 / a )        per orbit
```

**Controls, both passing exactly:** pure Newton gives `Δφ = 0` (closed ellipse), and
the GR term `3(GM)²L²/(c²r⁴)` with `L² = GMa` gives `6πGM/(ac²)` — the textbook
periastron advance, reproduced symbolically after fixing an error the control itself
caught (the first attempt omitted the `L²` factor and failed on dimensions; a numeric
cross-check isolated the fault to the symbolic `limit()` step, not the physics).

The structural point: `Δφ_GR = (π/a)·6GM/c²` and `Δφ_dipole = −(π/a)·ℓ_d`. **Both
scale as `1/a`.** The dipole competes with the *leading relativistic effect* on equal
footing, not with the Newtonian monopole through a `ℓ_d/r` handicap. That is the
answer to the question posed: the suppression is absent because precession responds to
the *shape* of the force law, not to its magnitude, and the `k·k` tier enters at
`2ℓ_q²/a` — only one power down, with its coefficient measured by the same observable.

## 3. Real data: the double pulsar

J0737-3039 (Kramer et al. 2021, arXiv:2112.06795): `ω̇ = 16.89947(4)` deg/yr —
fractional precision **2.4×10⁻⁶**. My formula reproduces the GR value to 0.04 %
(16.906 vs 16.8995; the residual is the `e²` and higher-PN terms the near-circular
formula drops — adequate for a bound, not for parameter estimation).

Attributing at most the measurement precision to a MULTING term:

| system | a [km] | ω̇ precision | bound on `\|ℓ_d\|` | `ℓ_d/a` |
|---|---:|---:|---:|---:|
| **J0737-3039** | 8.79e5 | 2.4e−6 | **5.5 cm** | **6.2e−11** |
| B1913+16 | 1.95e6 | 7.1e−5 | 2.9 m | 1.5e−9 |

Compare: the kSZ quadrupole forecast gave `σ(ℓ_d) ≈ 18 Mpc` at `r = 100` Mpc — the
double pulsar is **~24 orders of magnitude more constraining in absolute length**, and
9 orders in the dimensionless `ℓ_d/a`.

## 4. What the bound means — and the one honest ambiguity

`ℓ_d = 2β_d(u_A+u_B)` with `u = (k/c²m)·r_A`. For a neutron star the natural analogue
of the cluster's thermal `k` depends on which internal energy plays the role:

| choice of k | `u_NS` | `β_d` bound from 5.5 cm |
|---|---:|---:|
| virial/binding energy (`E/Mc² ≈ 0.105`) | 1.15e3 m | **1.2×10⁻⁵** |
| rotational energy only (P = 22.7 ms) | 0.23 m | 6.0×10⁻² |

Under either reading the bound is **orders of magnitude below** Table A1's fitted
`β_d = 4.5`, and ~12 orders below the `β_d ~ 10⁷` that the cluster-signature estimate
(`build_report_ru.py`) says a cosmological dipole effect would need.

**Stated with the required care:** this is a constraint on `β_d·u_NS` as a product.
An advocate's escape is that `k` is *specifically* thermal-kinetic energy and cold
neutron stars have almost none — then `u_NS → 0` and the bound evaporates. The corpus
does not define `k` sharply enough to close that escape (it says "kinetic energy of
sub-objects"); a NS interior is degenerate, not thermal, so the escape is live. What
the bound does establish, cleanly: **any version of MULTING in which `k` includes
bulk internal energy (binding, rotational, degeneracy) is excluded at the 10⁻⁵ level
in `β_d` by the double pulsar.** The theory can only survive in the reading where `k`
is strictly thermal — which should be checked against how the cluster analysis uses
`E_thermal/c²`, where it manifestly *is* thermal. The two uses are consistent only if
`k` = thermal kinetic energy specifically; that is now a sharp definitional question
for the corpus rather than a vague one.

## 5. Verdict

```
Unsuppressed observable                : FOUND -- apsidal/periastron precession.
                                         Dipole enters at (pi/a) ell_d, the same 1/a
                                         order as GR's leading term; no ell_d/r penalty
Controls                               : Newton -> 0 exact; GR -> 6 pi GM/(a c^2) exact;
                                         J0737-3039 omega_dot reproduced to 0.04 %
Best real system                       : double pulsar J0737-3039, omega_dot to 2.4e-6
Bound                                  : |ell_d| < 5.5 cm  (ell_d/a < 6e-11)
In beta_d, k = bulk internal energy    : beta_d < 1.2e-5  -- excludes Table A1's 4.5
                                         and the cosmological ~1e7 by 5-12 orders
In beta_d, k = strictly thermal        : bound evaporates (cold NS); the theory
                                         survives only in this reading
New sharp question for the corpus      : is k defined as THERMAL kinetic energy
                                         specifically? Cluster usage says yes;
                                         nothing in the text pins it down.
ell_q^2 term                           : enters at 2 ell_q2/a^2 -- constrained by the
                                         same data once ell_d is bounded; not yet
                                         separately extracted here
```

## What this does NOT establish

1. **Not a refutation of MULTING.** The thermal-k reading survives untouched, and
   that reading is consistent with how the cluster analysis actually computes `k`.
2. The near-circular formula drops `O(e²)` and higher-PN cross terms; for B1913+16
   (`e = 0.617`) the bound is indicative only. J0737's `e = 0.088` makes the 5.5 cm
   figure robust at the ~1 % level.
3. Attributing the full measurement precision to MULTING assumes no conspiracy with
   other PN parameters; a joint fit would weaken the bound by an O(1) factor.
4. The `u_NS` estimates use a uniform-density NS; realistic structure changes them
   by factors of order unity, nothing more.

## The one-line summary for the bridge track

The programme asked for an observable where the k-sector is unsuppressed. It exists,
it is already measured to 2.4×10⁻⁶, and it converts MULTING's vaguest definition —
what exactly is `k`? — into the single load-bearing question on which the theory's
compact-object viability now rests.
