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

**Correction record (2026-08-10, same day, after first publication of this
file).** An independent adversarial audit of §3
(`adversarial_p1/ADVERSARIAL_AUDIT_P1.md`, context-blind per this project's
Context Asymmetry Rule — given only the target files, not this table's
reasoning) ran against this table's own claims and found real errors, not
merely gaps. Per this project's own no-silent-correction discipline, the
rows below are edited in place with the correction stated inline, rather than
the original wording being quietly replaced. **The single load-bearing
correction:** the claim that the two-charge completion "clears" MULTING's
mass-scaling obstruction (old row, §3) is **circular** — killed, not
survived. See the amended §3 rows and §6.

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
| construction (physical dipole, point charges, `1/r` kernel, derivative coupling) | — | the electrostatic sum: yes. "derivative coupling"/"local, ghost-free field theory": **not**, in this file alone | — | electrostatic identity HOLDS (independently reproduced, fresh code). Field-theoretic framing was **SPECULATIVE as originally stated** — `two_charge_completion.py` contains no Lagrangian, propagator or EOM; asserted, not derived. **Resolved separately**, not by this file: `two_field_action_closure.py` (§3 row below) supplies and independently re-verifies the actual action | `FINDING_two_charge_completion.md` §6; audit `adversarial_p1/ADVERSARIAL_AUDIT_P1.md` §4, §4a |
| dipole **orientation** = mirror-symmetric (induced polarisation) | — | yes, **forced** by requiring `F_d`'s A↔B symmetry **and** a nonzero dipole moment | — | HOLDS, refined — a 5-configuration sweep (not the original's 3, all collinear) found A↔B symmetry alone is **not** sufficient: a second symmetric configuration exists (transverse-parallel, `A₃=0`, `A₄` coefficient `3` not `6`). What uniquely selects the radial/mirror configuration is symmetry **conjoined with** MULTING's own stated nonzero dipole term. Practical conclusion (induced polarisation) survives; the original one-condition justification did not | `FINDING_two_charge_completion.md` §3, `FINDING_P1_two_field_closure.md`; audit §5 |
| sign of `k`-charge = opposite mass | — | yes, forced by requiring net repulsion | — | HOLDS | `FINDING_two_charge_completion.md` §3 |
| `ℓ_d = 2(u_A+u_P), ℓ_q²=6u_Au_P` | — | yes, exact | — | HOLDS, with `u≡κkr/(c²m)` | `FINDING_two_charge_completion.md` §4 |
| `β_d = 2, β_q = √6` | — | yes | — | HOLDS **as one convention's numbers** — depends on `lever arm = r_A` | `FINDING_two_charge_completion.md` §4 |
| `β_q/β_d = √6/2 = 1.2247` | — | yes | — | HOLDS, with a scoped caveat: an independent counterfactual found the number is convention-invariant only under a **shared** rescaling/kernel for both bodies (`γ_A=γ_B`); for `γ_A≠γ_B` the ratio moves off `3/8`. This is claimed (by the same audit that found the weakening) to be **subsumed** by `Λ=K'''K'/K''²=3/2⟺massless mediator`, which is invariant under *any* rescaling of the dipole moment and any kernel — reducing the residual assumption to "one `κ` for both bodies", physically reasonable but still unverified, not derived | `FINDING_P1_two_field_closure.md` §2-3; audit §3 (weakening), §4a (subsuming argument) |
| `d ln ℓ_d/d ln M = +0.555` "reproduced" | — | **NO — killed as circular.** `ℓ_d=2(u_A+u_P)` is exact algebra, but `u_i≡κk_ir_i/(c²m_i)` is not predicted by the theory; `k_i, r_i` are real cluster observables taken as-is, already carrying their own empirical scaling. The theory supplies only the bilinear rule `ℓ_d∝(u_A+u_P)`; it contributes no mechanism fixing how `u_i` scales with `M`. So "the exponent is reproduced" holds in the trivial sense that *whatever* exponent the data has, the theory inherits unchanged — indistinguishable from a theory making no mass-scaling prediction at all | 548 clusters, `E_thermal/c²` (MCXC-I∩PSZ2) | **KILLED** (Kill Analysis, audit §19). **Also corrects the number itself:** `+0.555±0.041` is the *marginal* exponent, confounded with this flux-limited sample's real M–z selection correlation (the same conflation P2 already flagged for `k` alone). Deconfounded against the physically-motivated `E(z)=H(z)/H₀` control: **`d ln(u)/d ln(M) = 0.393±0.055`** — *further* from `+1`, not closer. A from-scratch self-similar (pure-gravity + standard baryon physics) derivation independently predicts `+1` exactly too, for a reason unrelated to either completion — so the ~11σ departure from `+1` is ordinary baryonic-feedback astrophysics, and **neither** the single-field **nor** the two-charge comparison to real cluster data tests gravitational content until feedback is modelled explicitly | `FINDING_field_equation_solved.md` §5, `FINDING_two_charge_completion.md` §5 — **superseded by** audit §19, §19a |
| EP obstruction (CANDIDATE-L1: repulsive `1/r³` cannot come from a stable EP-respecting local action) | — | **resolved by reclassification**: `φ` is a fifth force, not gravity; EP constrains the gravitational sector only | — | HOLDS as a resolution of a previously open obstruction | `FINDING_P1_two_field_closure.md` §4.2 |
| cosmological background contribution | — | yes: radial-dipole average = double layer (zero off-shell); random average = zero by symmetry either way | — | this completion contributes **only a `G`-renormalisation** at first order — **cannot** supply MULTING's `H(z)` eras | `FINDING_P1_two_field_closure.md` §4.3, converges independently with the effective-fluid finding below |

**Net verdict, §3 (corrected).** The strongest surviving construction, but
narrower than first stated. **Survives** independent re-attack: the
algebraic derivation (`β_d=2, β_q=√6`), the sign rule as a theorem, the
attractive-everywhere margin, and the orientation argument (once repaired to
two conditions, not one). **Does not survive as stated:** the claim that it
"clears" MULTING's mass-scaling obstruction — that was circular, and is now
recorded as killed. What is left of `1.2247` is a sharp, falsifiable number
whose convention-freedom rests on one named, physically reasonable but
unverified assumption (same `κ` for both bodies) — and it remains
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
| charge-space identifiability — does `k` carry real info beyond `M`? | CHEX-MATE (`chexmate_real_TX.csv`, `chexmate_combined.csv`) | `ρ=+0.36` (n=25) between two independent `k`/`T` estimators at fixed `M`. **Independently re-derived to 4 decimals** (`ρ=+0.3611`, fresh matching code, not reusing P2's own) and **strengthened**: a bootstrap the original didn't run gives 95% CI `[−0.015,+0.674]` — barely touches zero, 97% of resamples give `ρ>0` | **SUGGESTIVE, and if anything slightly strengthened by independent re-check** | `FINDING_P2_charge_identifiability.md`; audit §8a |
| is the resulting `k`-charge **force** observable at all? — a separate, downstream question from the row above | same 548-cluster catalogue, population-wide (not just the median) | even at the single most extreme cluster and closest kSZ pair separation used anywhere in this project (`κ=1`, no further suppression): `ℓ_d/D~1.4×10⁻⁶`. Amplitude gap **5–7 orders of magnitude** at population level, up to `10⁵–10¹³×` across the full range of systems and separations tested. **[Note added 2026-08-12, per `FINDING_P14_kappa_normalization_unfixed.md`: `κ` is unfixed project-wide, and this row already correctly labels `κ=1` as the benchmark — but the "predicted effect is astronomically below..." framing in the status column reads as `κ`-independent. It is not fully: the gap scales as `κ²`, so `κ<1` only widens it further (unlike `FINDING_P7`'s exclusion, this conclusion is robust to `κ` uncertainty in the direction that matters — decreasing `κ` cannot rescue observability, only worsen it).]** | **BREAKS** — not a data-quality problem; the predicted effect is astronomically below any conceivable current detection floor at `κ≲1`, and worse for smaller `κ` | audit §8, independently re-run from raw data, not cited |

**No route above delivers a measurement of `ℓ_q²/ℓ_d²`.** Two die
structurally (isotropic kSZ, effective fluid), two are forecast-blocked by
present data (quadrupole kSZ, charge-space), one is entirely gated on a
definitional question (periastron), one is a weak consistency check rather
than a discriminator (branch C), and the charge-space route's own downstream
question — can the resulting force be *observed* even if `k` is real? —
breaks by 5–13 orders of magnitude regardless of the answer to the first
question. **These are two different questions and answering the first
(k carries information) does not answer the second (the force is
detectable).**

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

**One thing resolving this question would *not* fix, stated so it is not
mistaken for a fourth open item:** pinning down `k`'s definition does not
rescue §3's "mass-scaling cleared" claim. That claim died on circularity —
the theory not constraining how `u_i` scales with `M` at all — which is
independent of which reading of `k` is correct.

---

## 6. Summary verdict card

```
GIVEN, unmodified                : m, k (undefined precisely), r_A, F_m/F_d/F_q,
                                   sign rule (until Sec 3), beta_d/beta_q (free)
DERIVED, HOLDS                   : two-charge structure (algebra independently
                                   re-derived), sign rule as theorem, forced
                                   orientation (once repaired to 2 conditions),
                                   forced k-sign, beta_q/beta_d = sqrt(6)/2
                                   (convention-invariant under shared kappa; see
                                   caveat), the action itself (written in P1,
                                   independently re-verified), EP resolution,
                                   k carries real info beyond M (suggestive,
                                   independently re-confirmed + bootstrap)
DERIVED, DOWNGRADED              : single-field ell_q^2=2ell_d^2 (-> minimality,
                                   not covariance), its beta_q/beta_d=2.8284;
                                   beta_q/beta_d convention-freedom (shared-kappa
                                   assumption only, not fully general)
DERIVED, KILLED                  : single-field mass scaling (10.8 sigma, now
                                   ~11 sigma post-deconfound), isotropic kSZ
                                   route (structural), effective-fluid cosmology
                                   route (4-5 orders short), "two-charge clears
                                   the mass-scaling obstruction" (CIRCULAR --
                                   theory inherits u_i's exponent from data,
                                   predicts nothing about it), the specific
                                   figure "+0.555+-0.041" as a physical slope
                                   (superseded by the deconfounded 0.393+-0.055),
                                   k-charge force observability (5-13 orders
                                   below any detection floor -- distinct from,
                                   and does not follow from, k-identifiability)
INDEPENDENT INPUT, consumed      : 548-cluster catalogue (MCXC-I+PSZ2), CHEX-MATE
                                   (25+104 clusters), ACT DR6 pairwise kSZ, MCXC
                                   1742-cluster pair catalogue, J0737-3039 timing,
                                   Cen+Bahcall+Gramann 1994 (H0-anchor track, Sec.
                                   P5, adjacent not central to this table)
OPEN, and load-bearing           : the single definition of k -- every unresolved
                                   test in Sec 4 traces back to it. Resolving it
                                   does NOT rescue the killed mass-scaling claim
                                   (independent failure mode, see Sec 5 note).
                                   [PARTIALLY RESOLVED 2026-08-11, from the
                                   primary source directly, not from TJB --
                                   see FINDING_P7_k_definition_resolved_from_
                                   corpus.md. "k is strictly thermal" (the
                                   escape hatch that would zero the pulsar
                                   bound) has NO textual support -- the
                                   preprint explicitly discusses ROTATION as
                                   a candidate source of k, arguing only that
                                   thermal motion dominates for the CLUSTER
                                   case specifically. Using only the
                                   pulsars' OWN measured spin period (the
                                   least contestable component), beta_d=2
                                   (this project's own derived value) is
                                   excluded by the pulsar bound by ~1.2
                                   orders of magnitude [CORRECTED after
                                   skeptic review -- was misstated ~1.5,
                                   a factor-of-2 convention slip, see
                                   FINDING_P7's own correction note], with
                                   no dependence on any disputed physics.
                                   One narrower question remains open:
                                   whether TJB's "ground state" baseline is
                                   classical or quantum-mechanical (affects
                                   only whether the exclusion is ~1.2 or ~5
                                   orders, not whether beta_d=2 survives
                                   either way).]
UNKNOWN, precondition missing    : whether this is a covariant, cosmologically
                                   well-posed field theory beyond the action's
                                   flat-space, fixed-background form (audit S11)
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
4. This table's own first version (2026-08-10, same day) overstated §3's
   mass-scaling row and understated the k-charge/force-observability
   distinction. Both are corrected in place above, per this project's Context
   Asymmetry Rule: the correcting audit was given only the target files, not
   this table's reasoning, so its findings are an independent check rather
   than a self-review. Full detail: `adversarial_p1/ADVERSARIAL_AUDIT_P1.md`.
