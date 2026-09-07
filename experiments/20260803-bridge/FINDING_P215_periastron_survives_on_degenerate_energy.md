# FINDING P215 — the periastron bound **survives** on the one internal
# energy the corpus actually admits: degenerate kinetic energy

**Date:** 2026-09-07
**Artifact:** `P215_degenerate_kinetic_periastron.py`
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Answers:** the `NEEDS-REAL-DATA` item raised by the Step 8a skeptic on
`P214` — *which energy did the periastron calculation substitute for
`u_NS`?*

---

## 1. The gap

`FINDING_unsuppressed_observable_periastron` computed the double-pulsar
bound for two choices, and concluded that *"any version of MULTING in
which `k` includes bulk internal energy (**binding, rotational,
degeneracy**) is excluded at the `10⁻⁵` level."*

Cross-checked against what the sources actually say (`P214` retraction,
2026-09-07):

| energy | computed there? | v6 | v82 |
|---|---|---|---|
| **binding** | yes — the `1.2×10⁻⁵` row | **excluded** (v6:601-602, *"potential energies that … bind sub-objects into objects"*) | **excluded** (v82:1381-1383, *"de-emphasize … potential energies within objects"*) |
| **rotational** | yes — the `6.0×10⁻²` row | **excluded by its own definition** (v6:640, *"energies of **linear motion**"*) | not addressed |
| **degeneracy** | **named in the conclusion, never computed** | not addressed | not addressed |

**Both computed rows used energies the corpus excludes. The one that could
survive had no row.** Degenerate kinetic energy is *kinetic* (Fermi motion
of neutrons) — not potential, not bulk, not rotational — so nothing in
either document rules it out.

## 2. Controls — the arithmetic is pinned to the existing finding, not to my constants

| control | result |
|---|---|
| **PC1** reproduce the binding row | `u = 1.155×10³` m vs its `1.15e3`; `β_d < 1.190×10⁻⁵` vs its `1.2e-5` — **PASS** |
| **PC2** reproduce the rotational row | `u = 0.2269` m vs its `0.23`; `β_d < 6.059×10⁻²` vs its `6.0e-2` |
| **NC1** relativistic Fermi formula → non-relativistic limit | `x=0.065` → 0.1%, `x=0.140` → 0.3%, `x=0.302` → 1.6% — converges as required |

PC1 also back-solves the finding's unstated `R_NS`: **11 km**, since
`0.105 × 11 km = 1.155 km` reproduces its `u`.

## 3. The missing row

Cold relativistic ideal degenerate neutron gas, uniform density — the same
approximation the original used:

```
x   = p_F/(m_n c),  p_F = ħ(3π²n)^(1/3)
ε   = (m⁴c⁵/π²ħ³)·(1/8)[ x√(1+x²)(1+2x²) − asinh(x) ]
K   = ε − n m_n c²
```

| `R_NS` [km] | `n` [m⁻³] | `x = p_F/m_n c` | `f_deg` | `u_NS` [m] | **`β_d <`** |
|---|---|---|---|---|---|
| 10.0 | 3.792e44 | 0.4703 | 0.0639 | 639.3 | **2.198e-05** |
| 11.0 | 2.849e44 | 0.4275 | 0.0532 | 584.8 | **2.404e-05** |
| 12.0 | 2.195e44 | 0.3919 | 0.0449 | 538.6 | **2.610e-05** |
| 13.0 | 1.726e44 | 0.3618 | 0.0384 | 499.0 | **2.817e-05** |
| 14.0 | 1.382e44 | 0.3359 | 0.0332 | 464.8 | **3.025e-05** |

## 4. Verdict

> **`β_d < 2.2×10⁻⁵ – 3.0×10⁻⁵`** — **5.2 to 5.3 orders of magnitude below
> Table A1's fitted `β_d = 4.5`.**

The bound is 2–3× weaker than the binding-energy version, **but at the
same order of magnitude**. Restricting the calculation to the energy the
corpus actually admits does **not** rescue the fitted value.

`x = 0.34–0.47` puts the neutron gas mildly relativistic, so the
relativistic treatment matters at the ~2–5% level — not at the level that
would change a five-order conclusion.

## 5. What this does and does not change

**Changes:** the periastron test is **restored on a legitimate footing**.
`P214`'s retraction left it in limbo — the two computed rows used excluded
energies, so the constraint had no admissible basis. It now has one.

**Does not change:** the corpus still does not *state* that `k` includes
degenerate energy. This computes what the bound would be **if** it does.
The scope question raised by the retraction stands: v82 gives the domain
of Eqs. (1)–(4) inconsistently — node at line 188, object at 1354-1355 and
1449-1452 — and a neutron star is an *object* on the second reading.

**Does not establish** that MULTING is refuted. It establishes that **if**
`k` extends to compact objects at all, in the one form the corpus admits,
then `β_d` is bounded ~5 orders below the value Table A1 fits.

## 6. Caveats, both real, neither load-bearing

1. **Uniform density is crude.** A realistic profile concentrates mass
   centrally, **raising** the mean Fermi momentum and therefore `f_deg` —
   so this estimate is, if anything, **conservative** in the direction
   that matters.
2. **Ideal Fermi gas ignores strong-interaction corrections**, which at
   these densities are not small. They shift `f_deg` by tens of percent,
   not by the ~5 orders needed to matter.
3. `M_A`, `M_B`, `P_spin` are `[MEMORY]` textbook values for J0737-3039.
   PC1/PC2 pin the *arithmetic* to the original finding rather than to
   these being exact; the order of magnitude is what is claimed.
4. No Step 8a pass on `P215` itself.
