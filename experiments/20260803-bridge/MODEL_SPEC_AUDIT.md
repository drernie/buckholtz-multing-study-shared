# MODEL_SPEC_AUDIT — the bridge track's symbol and claim registry

**Date:** 2026-08-10 · proposed by an external reviewer's read of the bridge
track: *"для каждой формулы — четыре колонки: задано в MULTING / выведено нами
/ независимый вход, чтобы сразу видеть, где мы объясняем существующее, а где
добавляем новую физику."*
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Scope:** the covariant-completion programme (`experiments/20260803-bridge/`),
2026-08-03 through 2026-08-10. Not the whole MULTING/IDM corpus — Eq.31–32, the
6-isomer count and the cluster-only kSZ/Ω_m tracks are out of scope here.

This also closes, for this one track, a gap the project's own methodology has
flagged since 2026-06-24: `research-methodology.md`'s "gap #2 — Реестр
параметров/символов", a symbol-overload registry that existed only as a
manual protocol with no worked example. This is that worked example.

---

## How to read the columns

| Column | Meaning |
|---|---|
| **Given** | Stated in the MULTING preprint itself, as a postulate or definition |
| **Derived** | Obtained in this track from the given material — a real step, not asserted |
| **Independent input** | External data or literature the derivation needed |
| **Status** | Current epistemic status, one word: `HOLDS` / `DOWNGRADED` / `KILLED` / `OPEN` |
| **Evidence** | Which `FINDING_*.md` established it |

**Hard rule enforced while building this table** (Gate 1 of
`~/.claude/rules/artifact-provenance-gates.md`): a verdict for one symbol never
transfers to a same-named symbol in a different construction. `ℓ_d` means
something different in the single-field completion (§2) and the two-charge one
(§3) — both rows are kept, not merged, because they are not the same object
even though they share a name.

---

## 1. Force-law primitives — given by MULTING, not touched by this track

| Symbol | Meaning | Given as | Independent input | Status |
|---|---|---|---|---|
| `m_A, m_P` | monopole (mass) charge | postulate | cluster `M500` (MCXC-I/PSZ2) | HOLDS |
| `k_A, k_P` | "kinetic energy of sub-objects" charge | postulate, **not sharply defined** | none — the definition itself is the gap | **OPEN**, see §5 |
| `r_A, r_P` | object radius entering `r_dA = β_d r_A` | postulate | `R500` | HOLDS |
| `F_m, F_d, F_q` | monopole/dipole/quadrupole force terms | postulate, Eqs.(14)-(16) | — | HOLDS |
| sign rule (attract/repel/attract) | even tiers attract, odd repel | **postulate**, §2.2 | — | **DOWNGRADED to consequence** — see §3, row `sign rule` |
| `β_d, β_q` | dipole/quadrupole coupling constants | **free parameters**; only known values are AI-fitted (Table A1: `4.5`, `18.0`) | — | fitted values `BLOCKED_BY_TARGET_PROVENANCE`, `FINDING_table_a1_provenance.md` |
| `ℓ_d = A₃/A₂, ℓ_q² = A₄/A₂` | scale-free force-law ratios | postulate (defined in the technical memorandum used by the kSZ spec) | — | HOLDS as a definition; **value** is what every row below tries to pin down |

---

## 2. The single-field completion (R7) — mostly downgraded or killed

| Symbol / claim | Given | Derived | Independent input | Status | Evidence |
|---|---|---|---|---|---|
| `Φ(χ) = [(1+3εχ)^{2/3}−1]/(2ε)` | — | yes, exact field redefinition of `L=½f(Φ)(∂Φ)²` | — | HOLDS as one witness action | `FINDING_R7_collapses_to_one_action.md` |
| `ℓ_q² = 2ℓ_d²` | — | yes, from `Φ(χ)`'s own series | — | **DOWNGRADED**: shown to be the `f₂=0` (minimal) member of a one-parameter-per-order class, `ℓ_q²=2ℓ_d²−f₂/2`; not a consequence of covariance | `FINDING_lq2_test_outcome.md` §1 |
| `β_q/β_d = 2√2 = 2.8284` | — | yes, from the R7 map applied to MULTING's own β-definitions | — | **downgraded with the above**; not tested against fitted β (Gate 2: fitted target) | `FINDING_lq2_test_outcome.md` §2 |
| field eq. collapses to linear Poisson for `χ` | — | yes, `∇²χ=0` exact to all orders in vacuum, sympy-verified | — | HOLDS | `FINDING_field_equation_solved.md` §1 |
| `d ln ℓ_d/d ln M = +1` (point-source, single field) | — | yes, exact for `χ=M/r` | — | HOLDS as a prediction of *this construction* — but **KILLED as MULTING's own prediction**: measured `+0.555±0.041` on 548 clusters, 10.8σ off | `FINDING_field_equation_solved.md` §4 |
| kSZ constraint on `ℓ_d` via pairwise superposition | — | attempted | ACT DR6 + `xi_zbin2.dat` | **KILLED (method)**: `C₃,C₄` diverge at contact for a spherically-symmetric shell (isotropic average of a physical dipole); not a property of the theory | `FINDING_dipole_shell_is_a_double_layer.md` |
| kSZ constraint via the field-picture (`λ` parametrisation) | — | yes, one-parameter, finite everywhere | ACT DR6 | `λ = +0.05, 95% CI [−0.24,+2.08]`, not degenerate with amplitude — but this is a constraint on the **single-field** `ℓ_d=εM`, already killed by mass-scaling above | `FINDING_field_equation_solved.md` §2 |

**Net verdict, §2:** the single-field completion is internally consistent but
empirically excluded as MULTING's actual completion (mass-scaling, 10.8σ).
Superseded by §3.

---

## 3. The two-charge completion — current best candidate

| Symbol / claim | Given | Derived | Independent input | Status | Evidence |
|---|---|---|---|---|---|
| charge structure `m·m`, `k·m+m·k`, `k·k` | — | yes, forced by MULTING's own `\|r_qAB\|²=β_q²r_Ar_P` (product of *two* bodies' lever arms — a quadrupole moment of one body cannot produce that; two dipole moments do, automatically) | — | HOLDS — the structural clue was read from MULTING's own parametrisation, not assumed | `FINDING_two_charge_completion.md` §1 |
| **sign rule** (attract/repel/attract) | postulate in MULTING | **re-derived as a theorem**: `(m_A−κk_A)(m_P−κk_P)` binomial expansion | — | **DOWNGRADED from postulate to consequence** (a postulate becomes provably necessary — the strongest single result of this track) | `FINDING_two_charge_completion.md` §2 |
| construction (physical dipole, point charges, `1/r` kernel, derivative coupling) | — | yes | — | HOLDS, ghost-free, positive controls passed (3, one caught a real sign bug) | `FINDING_two_charge_completion.md` §6 |
| dipole **orientation** = mirror-symmetric (induced polarisation) | — | yes, **forced** by requiring `F_d`'s A↔B symmetry | — | HOLDS — not assumed, the only configuration matching MULTING's own form | `FINDING_two_charge_completion.md` §3, `FINDING_P1_two_field_closure.md` |
| sign of `k`-charge = opposite mass | — | yes, forced by requiring net repulsion | — | HOLDS | `FINDING_two_charge_completion.md` §3 |
| `ℓ_d = 2(u_A+u_P), ℓ_q²=6u_Au_P` | — | yes, exact | — | HOLDS, with `u≡κkr/(c²m)` | `FINDING_two_charge_completion.md` §4 |
| `β_d = 2, β_q = √6` | — | yes | — | HOLDS **as one convention's numbers** — depends on `lever arm = r_A` | `FINDING_two_charge_completion.md` §4 |
| `β_q/β_d = √6/2 = 1.2247` | — | yes | — | HOLDS **as the physical content**: convention-invariant (checked symbolically), equals a kernel invariant `Λ=K'''K'/K''²=3/2 ⟺ massless mediator` | `FINDING_P1_two_field_closure.md` §2-3 |
| `d ln ℓ_d/d ln M = +0.555` reproduced | — | yes, `ℓ_d=2(u_A+u_P)` is MULTING's own functional form | 548 clusters, `E_thermal/c²` (MCXC-I∩PSZ2) | HOLDS — the mass-scaling obstruction that killed §2 is closed here | `FINDING_field_equation_solved.md` §5, `FINDING_two_charge_completion.md` §5 |
| EP obstruction (CANDIDATE-L1: repulsive `1/r³` cannot come from a stable EP-respecting local action) | — | **resolved by reclassification**: `φ` is a fifth force, not gravity; EP constrains the gravitational sector only | — | HOLDS as a resolution of a previously open obstruction | `FINDING_P1_two_field_closure.md` §4.2 |
| cosmological background contribution | — | yes: radial-dipole average = double layer (zero off-shell); random average = zero by symmetry either way | — | this completion contributes **only a `G`-renormalisation** at first order — **cannot** supply MULTING's `H(z)` eras | `FINDING_P1_two_field_closure.md` §4.3, converges independently with the effective-fluid finding below |

**Net verdict, §3:** the strongest surviving construction. Reproduces the
sign rule as a theorem, the mass-scaling law, and gives a sharp, falsifiable,
convention-independent number (`1.2247`) — but that number remains
**untested**, because every route tried to test it independently failed for
reasons that are themselves informative (§4).

---

## 4. Attempts to test `β_q/β_d` independently — all inconclusive, informatively

| Route | Independent input | Outcome | Status | Evidence |
|---|---|---|---|---|
| pairwise-kSZ isotropic (`ℓ=0`) | ACT DR6 | shell factor diverges at contact — a contact term, not a long-range force | KILLED (structural, not a data limitation) | `FINDING_dipole_shell_is_a_double_layer.md` |
| pairwise-kSZ quadrupole (`ℓ=2`) | ACT DR6, `ξ₂` from `xi_zbin2.dat` (leading-order projection, no simulation) | kernels derived exactly, finite; but the three candidate ratios (1.2247 / 2.8284 / 4.0) differ by `<1 Mpc` at `ℓ_d~5` Mpc, deep inside the forecast `σ(ℓ_d)~18` Mpc | **OPEN, forecast says not worth pursuing without new data** | `FINDING_quadrupole_channel_kernels.md`, `FINDING_xi2_and_forecast.md` |
| double-pulsar periastron (unsuppressed observable) | J0737-3039 timing, `ω̇` to `2.4×10⁻⁶` | bound `\|ℓ_d\|<5.5` cm **if** `k` includes bulk internal energy; evaporates if `k` is strictly thermal | **OPEN — hinges entirely on the definition of `k`** | `FINDING_unsuppressed_observable_periastron.md` |
| cluster-pair sign constraint (branch C, `ℓ_d≥2ℓ_q` for attractive-everywhere) | MCXC-I, 1742 clusters, projected separation | weak but real: at the kSZ-bound `ℓ_d=8` Mpc, ≤4.25% of pairs *could* be in a repulsive window and would take ~20 Gyr to disperse — not excluded | HOLDS as a weak constraint, not a test of `β_q/β_d` | `FINDING_cluster_pair_sign_constraint.md` |
| effective-fluid route (pair energy → cosmic `H(z)`) | cluster number density, correlation length | falls short of `ρ_crit` by 4-5 orders of magnitude at every plausible `ℓ_d`; `ℓ_d` would need to be 46× the Hubble radius | **KILLED** as a mechanism for MULTING's cosmology (independent of `β_q/β_d`) | `FINDING_effective_fluid_energy_scale.md` |
| charge-space identifiability (is `k` even a second charge, empirically) | CHEX-MATE (`chexmate_real_TX.csv`, `chexmate_combined.csv`) | `ρ=+0.36` (n=25) between two independent `k`/`T` estimators at fixed `M`; implied intrinsic scatter (0.07 dex) does not clearly exceed the internal noise floor (0.11 dex) | **SUGGESTIVE, not decisive** | `FINDING_P2_charge_identifiability.md` |

**No route above delivers a measurement of `ℓ_q²/ℓ_d²`.** Two die
structurally (isotropic kSZ, effective fluid), two are forecast-blocked by
present data (quadrupole kSZ, charge-space), one is entirely gated on a
definitional question (periastron), and one is a weak consistency check, not a
discriminator (branch C).

---

## 5. The single load-bearing open question

**Every unresolved row above terminates at the same place: what is `k`?**

| Reading | Consequence | Consistency |
|---|---|---|
| `k` = thermal kinetic energy specifically | cold neutron stars carry `u_NS≈0`; periastron bound evaporates | **consistent** with the cluster analysis, which computes `k=E_thermal/c²` (`multing_core.py:90-91`) |
| `k` = "kinetic energy of sub-objects" broadly (binding, rotational, degeneracy) | periastron bound: `β_d<1.2×10⁻⁵`, five orders below Table A1's fitted `4.5` | contradicts the fitted value, but that value is itself `BLOCKED_BY_TARGET_PROVENANCE` |

The corpus's own text supports the broad reading in places and the narrow one
in the cluster analysis. Held as `P3_k_definition_question_DRAFT_HELD.md` —
not sent, per the standing pause.

---

## 6. Summary verdict card

```
GIVEN, unmodified                : m, k (undefined precisely), r_A, F_m/F_d/F_q,
                                   sign rule (until Sec 3), beta_d/beta_q (free)
DERIVED, HOLDS                   : two-charge structure, sign rule as theorem,
                                   forced orientation, forced k-sign, beta_q/beta_d
                                   = sqrt(6)/2 (convention-invariant), EP resolution,
                                   mass-scaling reproduction (+0.555)
DERIVED, DOWNGRADED              : single-field ell_q^2=2ell_d^2 (-> minimality,
                                   not covariance), its beta_q/beta_d=2.8284
DERIVED, KILLED                  : single-field mass scaling (10.8 sigma),
                                   isotropic kSZ route (structural), effective-fluid
                                   cosmology route (4-5 orders short)
INDEPENDENT INPUT, consumed      : 548-cluster catalogue (MCXC-I+PSZ2), CHEX-MATE
                                   (25+104 clusters), ACT DR6 pairwise kSZ, MCXC
                                   1742-cluster pair catalogue, J0737-3039 timing,
                                   Cen+Bahcall+Gramann 1994 (H0-anchor track, Sec.
                                   P5, adjacent not central to this table)
OPEN, and load-bearing           : the single definition of k -- every unresolved
                                   test in Sec 4 traces back to it
NEW PHYSICS ADDED beyond MULTING : the entire completion (kappa, the derivative
                                   coupling, the fifth-force reclassification) --
                                   MULTING itself specifies none of this; it only
                                   specifies the force law's low-energy shape
```

---

## What this audit does NOT do

1. It does not judge MULTING's cosmological claims (`H(z)`, the isomer count,
   Eq.31/32) — out of scope, tracked elsewhere in this project.
2. It does not resolve the `k` question — it names it as the single point on
   which every open row in §4 converges, which is the audit's actual product.
3. Rows marked HOLDS are internal-consistency and derivation-correctness
   verdicts, not claims that the two-charge completion *is* MULTING's actual
   physics — that remains untested, per §4's own summary.
