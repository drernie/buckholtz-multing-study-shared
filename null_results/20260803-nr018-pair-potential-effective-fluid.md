# NR-018 — the naive pair-fluid virial mapping

> **Scope, stated first.** This closes ONE mapping: a positive-density
> effective fluid built by virial-averaging a pure inverse-power pair potential.
> It does NOT close the generalized Layzer-Irvine formalism, which remains a
> valid energy balance, and it does NOT close the space of MULTING -> H(z)
> bridges.

**Date:** 2026-08-03 · **Verdict:** REJECT · **Recurrence:** 4th bridge rejection
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## Claim rejected

> The MULTING pair force law, integrated over a realistic cluster population,
> yields an effective energy density and pressure that can source the Friedmann
> equation and reproduce the published `H(z)`.

Rejected on three independent grounds, any one of which is sufficient. The first
is exact and needs no data at all.

---

## Ground 1 — structural: the equation of state cannot be negative

For a pair potential `U(s) = C·s^(-n)` the virial pressure integral gives an
exact identity, because `s·dU/ds = -n·U`:

```
rho_pair = (1/2)  n_c^2 ∫ d³s ξ(s) U(s)
p_pair   = -(1/6) n_c^2 ∫ d³s ξ(s) s dU/ds  =  (n/3) · rho_pair

                    w = p/rho = n/3
```

**Independent of `ξ`, of the amplitude, and of any cutoff.** Verified
symbolically.

| term | `U ∝` | n | `w = n/3` | dark-energy-like? |
|---|---|---|---|---|
| monopole (gravity) | `1/s` | 1 | `+1/3` | no |
| dipole | `1/s²` | 2 | `+2/3` | no |
| quadrupole | `1/s³` | 3 | `+1` (stiff) | no |

A dark-energy component requires `ρ > 0` together with `p < 0`. Here `w = n/3 > 0`
for every term, so `p` carries the sign of `ρ`: the two can never be opposite.
**No positive-density fluid built this way is dark-energy-like**, and each term
dilutes at least as fast as radiation.

**The sign qualifier matters, and the first draft of this entry omitted it.**
`ρ + 3p = (1+n)ρ`, so when `ρ < 0` — which is exactly the case for the attractive
monopole, whose binding energy is negative — the acceleration inequality
`ρ + 3p < 0` is satisfied identically. Such a component does *not* behave as dark
energy: it carries negative energy density and **reduces** `H²`. The claim being
made here is about the dark-energy equation of state, not about the sign of
`ρ + 3p` in the abstract.

The consequence is the sharp one: any cosmological signal in a bridge of this
form comes **entirely** from the assumed time-dependence of `A₂(a), A₃(a),
A₄(a)`, and none from the force law. Fitting `A_n(a)` to a target `H(z)` fits a
free function to a curve; the force law contributes a label. That is the same
failure class as **NR-001** and **NR-002**.

## Ground 2 — magnitude: six to eight orders short

Two independent routes, plus a published measurement of the same quantity.

| estimate | `Ω_pair` at z = 0 |
|---|---|
| pair integral, `ξ = (s/5 Mpc)^-1.8` | `(5–17) × 10⁻⁷` |
| peculiar kinetic energy, `σ₁D = 200–500 km/s` | `(2–13) × 10⁻⁷` |
| our own generous ceiling (n 10× real, M = 10¹⁵ M☉, r₀ = 25 Mpc) | `7.4 × 10⁻⁵` monopole; `3.9 × 10⁻⁵` dipole at `ℓ_d = 8 Mpc` |
| Chiang, Makiya, Komatsu & Ménard, arXiv:2007.01679 (measured) | the `Ω_W`, `Ω_th` family sits at `10⁻⁸` |

The two independent estimates agree once our deliberate generosity is removed:
using a cluster abundance ten times the real one inflates `n²` by 100.

Reaching `Ω ~ 0.7` needs a boost of `~10⁶`, which in force terms means
`F_dipole/F_grav ~ 10⁶–10⁷` at 1–5 Mpc. That contradicts the model's own premise
— these are meant to be *corrections* to cluster-scale gravity — and contradicts
the observational bound on dark-sector fifth forces, currently **7–14 % of
gravity** from cluster data (arXiv:2209.03963).

For a length-scale statement: the dipole term reaches `ρ_crit` only at
`ℓ_d ≈ 2.1 × 10⁵ Mpc = 207 Gpc`, which is **46× the Hubble radius**, against a
kSZ bound of order ten megaparsecs from this project's own analysis.

## Ground 3 — the integrals are regulator-controlled

With `ξ ∝ s^-γ`, the integrand of `∫d³s ξ U` scales as `s^(2-γ-n)`:

```
γ = 1.8, n = 1:  s^-0.8   converges
γ = 1.8, n = 2:  s^-1.8   DIVERGES as s_min^-0.8
γ = 1.8, n = 3:  s^-2.8   DIVERGES as s_min^-1.8
```

So `ρ_pair` for the dipole and quadrupole is set entirely by a hand-chosen
small-separation cutoff. Our numbers used `s_min = 1 Mpc`; a different defensible
choice moves the quadrupole by an order of magnitude. **There is no literature
guidance, because the construction itself is unpublished** — see below.

---

## Kill analysis

**What this kills:** the positive-density virial mapping — pair potential ->
`rho_pair, p_pair` as an ordinary isotropic fluid -> Friedmann. Ground 1 is a
property of that mapping applied to pure inverse powers. Ground 3 constrains the
amplitude only, and is itself cutoff-dependent.

**What this does NOT kill:** the generalized Layzer-Irvine energy balance as a
formalism; comoving-separation or non-power-law variants; anisotropic-stress
mappings; and every covariant route.

**What survives, untouched:**

- The force law itself. Nothing here says it is wrong.
- **The covariant-action route.** A background density read off the stress-energy
  tensor of a field, rather than assembled from a pair sum, is the standard
  construction and the only one with published precedent. Template:
  **Skordis & Zlosnik, arXiv:2007.00082, PRL 127, 161302 (2021)** — the only
  verified paper carrying action → field equations → non-relativistic limit →
  FLRW background → perturbations in one place.
- **arXiv:1010.6205** (Shtanov & Sahni, generalised cosmic energy equation)
  remains valid literature. It was misapplied, not refuted.
- Cluster-scale virial dynamics as an observable signature.
- **The kSZ constraint**, which tests the force law directly against ACT+SDSS
  pairwise velocities and never passes through a cosmological bridge.

**Relaxation map** — one assumption at a time:

| assumption | relax how | survives ground 1? |
|---|---|---|
| potential is inverse-power in `s` | add an exponential or Yukawa factor | possibly — `w = n/3` is specific to pure powers |
| separation is physical | use comoving separation | changes the virial identity; must be re-derived |
| energy is pairwise | source from a field's stress-energy | **yes — this is the surviving route** |
| coefficients are constant | `A_n(a)` free functions | no — that is fitting, per NR-001/NR-002 |

**Energy exchange `Q` does not rescue it.** `Q` redistributes energy between
sectors; it does not create it. A reservoir at `10⁻⁶` of `ρ_crit` cannot be
redistributed into `0.7`.

---

## The construction is unpublished

Searched from three directions and not found: the combination of a two-body
potential integrated against `ξ_hh` over a halo mass function to source a
Friedmann background. The components are standard — the virial equation of state
(Hansen & McDonald), the halo model (Cooray & Sheth, arXiv:astro-ph/0206508),
halo exclusion, the Jeans-swindle background subtraction (Kiessling
astro-ph/9910247; Falco et al. arXiv:1210.3363) — but the assembly is not.

Every published long-range dark-force cosmology builds its background from a
mean-field Lagrangian and its stress-energy tensor, never from a pair-correlation
integral. Farrar–Peebles (astro-ph/0307316) and Gubser–Peebles (hep-th/0407097)
were constrained by structure formation and equivalence-principle violation, not
by a "too-small effective density" argument — because their backgrounds were
never built this way.

**The absence of a precedent is itself informative: nobody built this bridge, so
nobody had to kill it.**

---

## Process failure, recorded

This project's own rule requires grepping `null_results/INDEX.md` before starting
work. That was not done. **NR-016** (2026-07-19) had already rejected a bridge
from this force law via the same source paper, arXiv:1010.6205, on the ground
that the kernel is not universal — `B` and `C` depend on per-cluster `k_A/m_A`
rather than on the mass product.

Writing the coefficients as `A_n(a)` **assumes away** that obstruction rather
than solving it. That substitution is an assumption, not a result.

This is the **fourth** bridge rejection: NR-001 (constant ε), NR-002 (power law),
NR-016 (naive Shtanov mapping), NR-018 (effective fluid). The first structural
one — the earlier three rejected particular parameterisations; this rejects the
class.

---

## Do not retry without

1. A pair potential that is **not** a pure inverse power — ground 1 is specific
   to `s^-n`.
2. Or an independent principle forcing `A₃(a) ∝ a⁵`, `A₄(a) ∝ a⁶`, so that the
   terms do not dilute. Not fitting: a principle.
3. Or a published pair-integral → Friedmann construction, which would show the
   assembly is legitimate after all.
4. Or evidence that the measured `Ω_W` is orders of magnitude above `10⁻⁶`.

---

## Sources

Verified this session, marked as such by the research agent:
arXiv:1010.6205 · arXiv:2007.00082 · arXiv:2007.01679 · arXiv:astro-ph/0206508 ·
arXiv:astro-ph/9910247 · arXiv:1210.3363 · arXiv:0804.3518 (title:
"Model of Dark Matter and Dark Energy Based on Gravitational Polarization" —
the companion "Dipolar Dark Matter and Dark Energy" is arXiv:0901.3114) ·
arXiv:astro-ph/0403694 · arXiv:astro-ph/0511591 · arXiv:0804.0232 ·
arXiv:2504.17293 · arXiv:2209.03963 · arXiv:gr-qc/0509108 · arXiv:1407.8084 ·
arXiv:1505.07800 · arXiv:astro-ph/0307316 · arXiv:hep-th/0407097 ·
arXiv:astro-ph/0412586

Unverified and not to be quoted: the exact `Ω_W` value from arXiv:2007.01679;
the origin of the "doom factor"; equation numbers within arXiv:1010.6205 as of
this session; whether the double-counting objection (binding energy already
inside the measured lensing mass) is published anywhere.

Artifacts: `experiments/20260803-bridge/FINDING_effective_fluid_energy_scale.md`,
`experiments/20260803-bridge/FINDING_table_a1_provenance.md`.
