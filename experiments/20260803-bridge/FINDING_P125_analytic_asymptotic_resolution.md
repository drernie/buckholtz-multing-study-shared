# FINDING P125 — Analytic resolution of `FINDING_P122`'s model ambiguity: **`DEVIATION-ENERGY-DIVERGES`** (q≈0.466, a genuine power-law divergence — resolved, but not as the guiding hypothesis predicted)

**Status:** built, ran, and its own verdict threshold was too loose on the
first pass — printed "RESOLVED: q→1/2" when the actual self-consistent
result sat 6.8% away from 1/2, on an extremely tight plateau. Caught by
directly computing the plateau's distance from 0.5 before trusting the
printed verdict, threshold tightened, rerun, corrected.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P125_analytic_asymptotic_resolution.py`

> User-directed: "реши научную неопределённость из P122 до конца" (resolve
> P122's scientific uncertainty completely). `FINDING_P122` found two
> fitted models disagreeing on whether the deviation-energy integral
> converges (`q≈0.502`, plain power law) or diverges (`q≈0.485–0.49`,
> log-corrected). `FINDING_P123` could only "lean" toward one side using
> more curve-fitting on the same finite domain — a structural ceiling: a
> genuine power law and an exponential with a tiny rate are nearly
> indistinguishable by fitting alone on any finite domain. Resolving this
> for real required an argument that doesn't depend on curve-fitting.

---

## The analytic argument

At late times (`N` large), `FINDING_P118`'s ODE system simplifies:
`ρ_A→0`, the `k²/a²` term `→0` (matching `FINDING_P124`'s own exact
`q`-match across `k=0.3`/`k=0.5` — the late-time dynamics is
`k`-independent), `H→H_Λ` (constant). The background field `pb`'s own
late-time equation reduces, in `N`-derivatives, to
`pb_NN + 3·pb_N + (λ/H_Λ²)·pb³ = 0` — a **quartic-potential oscillator
under constant friction**, with friction coefficient **exactly 3**,
independent of `H_Λ`, `λ`, or `k`.

Numerically integrating this reduced toy equation shows it is
**overdamped** (friction dominates inertia, no oscillation), giving the
slow-roll approximation `3·pb_N ≈ -λ·pb³`, which integrates exactly to
`pb(N) ~ √(3/(2λN))` — a power law with exponent **exactly 1/2** —
confirmed against the full nonlinear toy ODE to 6 significant figures by
`N=10⁶` (amplitude ratio to the slow-roll prediction: `0.983` at `N=100`
→ `0.999996` at `N=10⁶`).

## The decisive, form-agnostic test

Rather than fit another competing curve, built `q_local(N) := -N·d/dN[ln|contrast(N)-c_inf|]`
— a **local logarithmic derivative**, computed via secant slopes on the
already-computed dense trajectory, with no assumption about the global
functional form. For a true power law, `q_local(N)→q`; for a true
exponential, `q_local(N)→∞`. Validated first on the toy ODE (known
`q=1/2`): `q_local` rises `0.464→0.475→0.476→0.477` toward `0.5` — the
method works.

## A real confound found, and fixed

Applying `q_local` to the real `k=0.3` data using `c_inf` from
`FINDING_P122`'s two fits — differing by only `~0.006%` — gave
**qualitatively opposite** large-`N` trends (one rising back toward `0.5`,
the other drifting monotonically away). `q_local` at large `N` is
dominated by `c_inf`'s own imprecision, not signal.

**Fixed** with a self-consistent construction: search for the `c_inf`
that makes `q_local(N)` **flattest** across the large-`N` range — this
pins down both `c_inf` and the true exponent together, without borrowing
either from a competing fit. Result: `c_inf=-38569.179` (between the two
fitted values), giving `q_local` flat to **`0.011%`** relative spread
across nearly a decade of `N` (`0.4662→0.4659→0.4660`).

## A verdict-logic bug, caught before commit

The first run's own printed verdict said `RESOLVED: q→1/2 EXACTLY` — the
threshold used was `|q_plateau - 0.5| < 0.05`. Directly computing the
plateau's mean (`0.465960`) and its distance from `0.5` (`0.034`, `6.8%`
relative) before trusting that verdict showed it was **not actually close
to `0.5`** — an extremely tight, stable plateau sitting decisively
*below* it. The `0.05` threshold was far too loose relative to the
plateau's own demonstrated `0.011%` precision. Tightened to `<0.01`,
rerun, corrected.

---

## Verdict — **`DEVIATION-ENERGY-DIVERGES`** (q≈0.466, genuine power-law divergence)

`q` converges to a **tight, stable plateau at approximately `0.466`** —
clearly and decisively below `1/2`, not marginally close to it. Two
things are true simultaneously, and both matter:

1. **The analytic *mechanism* is corroborated**: friction-dominated,
   `k`-independent, universal-in-`N` asymptotics — supported by
   `FINDING_P124`'s own exact `q`-match across two different `k` values,
   which only makes sense if the late-time dynamics really is generic
   across `k` as this mechanism predicts.
2. **The specific predicted *value* (`q=1/2`) is not confirmed.** The
   true tail law evidently has additional structure beyond what the
   background field `pb`'s own reduced equation alone captures — plausibly
   from the linearly-sourced `psi`/`dph`/`drA_hat`/`qm_hat` sector, which
   this file did not independently re-derive from first principles.

**Consequence for the deviation-energy question**: with `q≈0.466`
strictly below `1/2`, `∫N^{-2q}dN` **diverges as a genuine power law**
(not merely logarithmically as the `q→1/2` hypothesis would have implied)
— this decisively resolves `FINDING_P122`'s tension toward the
**divergent** reading. Notably, it favors `power_law_log`'s own
*qualitative* conclusion (divergent) without confirming its *specific*
point estimate either (`q≈0.485–0.49` — the self-consistent value differs
from both `FINDING_P122` fits). This does not affect `G_E`'s own
convergence, independently established (`FINDING_P120`/`P122`) for any
`q>0`.

### Not established

- A rigorous proof that `q_local(N)→0.466` continues all the way to
  `N→∞` — this file tests a wide but still finite domain, like every file
  before it in this sub-arc.
- That the full coupled `(psi, dph, drA_hat, qm_hat)` system's own
  asymptotic law was independently re-derived from first principles —
  only the background field `pb`'s reduced equation was solved
  analytically; `contrast(N)`'s own inheritance of a related law is a
  plausibility argument checked against real data, not a first-principles
  derivation of `contrast(N)` itself.
- Why the true exponent is specifically `≈0.466` rather than some other
  value below `1/2` — this file measures it precisely, it does not derive
  it from the full system.
- Anything at `Λ` values, or `(k, IC)` combinations, other than `k=0.3`
  (this file) and `k=0.5` (`FINDING_P124`, consistent with this file's
  own universal-friction-coefficient argument).
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
