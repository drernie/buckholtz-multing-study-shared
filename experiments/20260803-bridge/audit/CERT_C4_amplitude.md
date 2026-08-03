# Certificate C4 — amplitude bound

**Verdict: FAIL** — by the criterion frozen 2026-08-03, before the run.
**The claim's direction survives and is strengthened. Our implementation did not.**

**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

---

## The frozen criterion, and what happened

> **FAIL** — the independent implementation differs in sign, or by more than two
> orders at the central choice.

```
Path A (ours)   dipole at L_d = 8 Mpc :  3.9e-05  of rho_crit
Path B (indep.) dipole at L_d = 8 Mpc : ~3e-08

difference: 3.11 orders of magnitude   ->   FAIL
```

Sign agrees. Magnitude does not. The criterion says FAIL at more than two orders,
and this is three. It is recorded as FAIL.

## Why Path A was wrong

Path B's structural result makes the error immediately visible. Both extra terms
factorise as

```
rho_k = ½ G rho_eff² I_k ,   rho_eff = n<m>
```

Number density and mass never enter separately — only through `rho_eff`, **the
mass density locked in the clustered population**. That is a physically bounded
quantity, and it is checkable.

| | `rho_eff` [M☉/Mpc³] | as a fraction of `rho_m` |
|---|---|---|
| **Path A: `n = 1e-4`, `M = 1e15`** | **1.00e11** | **2.52 — i.e. 252 % of all matter** |
| Path B: Tinker mass function `> 1e14` | 4.03e9 | 0.102 |
| plain real abundance `n ~ 2e-5`, `M ~ 1e14` | 2.00e9 | 0.050 |

Our choice was described in the code and in the finding document as
"deliberately generous, so the result is a ceiling." **It was not a ceiling. It
was outside the mass budget of the universe.** Clusters above 10¹⁴ M☉ hold about
10 % of the matter; we assumed 252 %.

Since `rho ∝ rho_eff²`, a factor 24.8 in `rho_eff` is 615 in energy density —
2.79 dex of the observed 3.11. The remainder is accounted for by Path B's proper
mass-function weighting and correlation-length treatment.

**The lesson is specific, not general.** Calling an assumption "generous" is not
a substitute for checking it against a conservation law. A quantity that must be
bounded by the total matter density should be *expressed* as a fraction of the
total matter density, where the violation is visible. Path B did exactly that,
unprompted, and called it "the single most useful structural fact here."

## The claim's substance: strengthened, not weakened

The frozen claim was `Ω_pair ≲ 10⁻⁴`. Path B's answer is `10⁻⁷`, with a
defensible range of `10⁻⁸ to 10⁻⁶` and a firm ceiling of `10⁻⁶` across a
324–972-cell grid. That is **three orders further** from cosmological relevance
than we claimed.

So the conclusion drawn in NR-018 holds and is more secure. What fails is our
number, and NR-018's Ground 2 must be restated with Path B's values.

## Path B's independent validation of its own result

Not taken on trust; it anchored the calculation two ways that share no code path
with the main computation:

- **Fourier route.** `∫d³s ξ(s)/s = (2/π)∫P(k)dk`, giving
  `W/V = −(G/π) ρ̄_m² ∫P(k)dk` — no power law, no `r0`, no `γ`, no cutoffs,
  convergent at both ends. Result for all matter in linear theory:
  `−8.1 × 10⁻⁷ ρ_crit`. The real-space route from the same `P(k)` agrees to 2 %.
- **Dimensional expectation stated before computing.** The monopole must be of
  order `Ω (v/c)²`, i.e. `10⁻⁷–10⁻⁶` for peculiar velocities of 300–1000 km/s.
  It landed there.
- The cluster-pair monopole, `−8 × 10⁻⁸`, sits a factor ~10 below the
  all-matter value — as it must, since clusters carry 10 % of the mass.
- **Three unit systems** (SI, astronomical, an independently hand-rolled cgs
  pass), agreeing to 1 part in 10¹⁵, with `G` in astronomical units *derived*
  from SI rather than looked up.
- `σ₈` reproduced to the target; `σ(10¹⁴) ≈ 1.0`, `σ(10¹⁵) ≈ 0.6`;
  `n(>10¹⁴) ≈ 2×10⁻⁵ Mpc⁻³`; ~10 % of matter in halos above 10¹⁴ M☉ — all
  textbook values, reproduced from a mass function built from scratch.

## Three findings Path B raised that change the record

**1. Every requested `s_min` is inside the halo exclusion radius.** Two clusters
cannot be closer than the sum of their radii; below that they are one object and
the point-mass pair potential does not apply.

```
M = 1e14 : R_200m = 1.44 Mpc  ->  minimum separation 2.89 Mpc
M = 1e15 : R_200m = 3.11 Mpc  ->  minimum separation 6.22 Mpc
```

All of 0.5, 1 and 2 Mpc lie inside 2.89 Mpc. This matters because the quadrupole
is controlled entirely by `s_min`. Imposing exclusion drops it by a factor 8–30
and changes its cutoff dependence from `s_min^-1.8` to logarithmic. **The naive
quadrupole numbers — ours and the envelope's — are overestimates by about an
order of magnitude.**

**2. The `ξ` versus `1+ξ` choice is load-bearing, and it connects to C3.** For
gravity the homogeneous piece is removed by the Jeans swindle. For the extra
terms no such removal is established, and the homogeneous pieces diverge:

```
monopole   ~ −2π G ρ² s_max²          quadratic
dipole     ~ +π  G ρ² L_d s_max       LINEAR — exceeds its clustering term at ~2 Gpc
quadrupole ~ −(2π/3) G ρ² L_q² ln s_max
```

> "The dipole energy density of the universe is not a well-defined quantity
> unless something removes the homogeneous piece."

This is the same caution the C3 analyst raised independently — that `rho` and `p`
are separately cutoff-dependent and only their ratio is clean. Two blind readers,
on different questions, reached the same structural point.

**3. A self-consistency failure in the stated inputs.** `r0 = 15–25 Mpc` implies
a bias of 1.70–2.74, while mass-selected samples above 10¹⁴ M☉ have
`b_eff = 3.29`. The `r0` and the mass we specified are not a consistent pair;
using them together understates clustering by 1.4× to 14.8×.

## A new structural result: the dipole and quadrupole are not alike

Ours considered only the dipole. Path B's inverse question separates them
sharply, because `rho_3 ∝ L_d` is linear while `rho_4 ∝ L_q²` is quadratic:

| term | length needed to reach `rho_crit` | in Hubble radii |
|---|---|---|
| dipole `L_d` | 10⁸–10⁹ Mpc | **10⁴–10⁵** |
| quadrupole `L_q` | 1–4 × 10⁴ Mpc | **3–100, and ~5–15 centrally** |

Closing a 10⁷ energy gap costs a factor 10⁷ in length for a linear term and only
its square root for a quadratic one. **A steeper extra term is far cheaper to
make cosmologically relevant, because its ultraviolet divergence does the work.**
Neither is viable — but they fail by different amounts, and our earlier
"46× the Hubble radius" figure was an artefact of the same unphysical abundance.

## What this certificate changes

| record | action |
|---|---|
| NR-018 Ground 2 | replace all Path A numbers with Path B's; note the abundance error |
| `FINDING_effective_fluid_energy_scale.md` | numbers superseded; the direction stands |
| the "207 Gpc = 46× Hubble radius" figure | withdrawn — replace with 10⁴–10⁵ Hubble radii for the dipole |
| the "generous ceiling" framing | withdrawn — it was not a ceiling |
| C4 status | **FAIL**, claim direction confirmed, amplitude restated at `10⁻⁷` |

## Scope

Path B's own limits, in its words: everything is at `z = 0`; whether a
non-relativistic pair-potential energy density gravitates as `ρ` or as `ρ + 3p`
is unspecified; and the abundance choice, not the numerics, dominates the
uncertainty at roughly ±0.5 dex. Numerical error is 10⁻¹⁵.

It also declined to quote figures from Fukugita & Peebles (2004) while flagging
it as the right published cross-check, on the ground that it could not verify the
values in session. That is the correct call and the reference stands as a
pointer, not as a confirmation.
