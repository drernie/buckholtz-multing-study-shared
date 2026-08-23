# FINDING P127 — Attempting to derive `A≈6679` from first principles: **`MECHANISM-PARTIALLY-CONFIRMED`** (the affine relationship is genuinely explained; the specific exponent is not)

**Status:** built, ran, gave an honest mixed result — not forced into either
a clean success or restated as a failure.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P127_reduced_system_first_principles.py`

> User-directed: "попробуй вывести A из первых принципов" (try to derive A
> from first principles) — the exact gap `FINDING_P125`/`P126` both named
> under Not Established: neither derived *why* the affine constant
> `A≈6679` exists, only measured that it does.

---

## The derivation attempted

`FINDING_P118`'s full ODE system, at late `N`, has exactly one source of
`k`-dependence: the `k²·exp(-2N)` terms in `dphdd` and `drA_hat_d`. Both
decay to zero. Dropping them (along with `ρ_A=C_MATTER·exp(-3N)→0`) and
setting `H=H_Λ` constant gives a **reduced, provably `k`-independent**
6-variable system (`pb, pb_N, psi, psi_N, dph, dph_N`, sourcing two linear
integrators `drA_hat, qm_hat`) — derived explicitly by converting
`t`-derivatives to `N`-derivatives, shown in full in the file's own
docstring.

**Positive control, clean pass**: `pb`'s own reduced equation, solved in
isolation, reproduces `FINDING_P125`'s already-validated slow-roll law
almost exactly (ratio to prediction: `1.0029` at `N=1000` → `1.000001` at
`N=10⁶`).

**Main test**: solve the full 6-variable reduced system from **two
arbitrary, non-`k`-tied initial conditions** (not derived from solving the
real system at any specific `k`). If the mechanism is right, both should
converge onto the same dominant mode, up to affine rescaling — a genuine,
independent test, not an inference from the already-observed match.

## Mixed result — reported honestly, not forced

**The affine relationship held, cleanly**: `A_hat` (the ratio of the two
solutions' deviations from their own optimal `c_inf`) was constant to
`0.0094%` across 3 decades of `N` — even tighter than the real system's
own `0.0063%`. This is genuine, independent confirmation that *some*
affine relationship is structurally guaranteed by this reduced system,
from ICs that have nothing to do with `k=0.3` or `k=0.5`.

**But `q_local` did not reproduce `≈0.466`.** Both ICs' `contrast(N)`
showed near-degenerate, essentially-zero `q_local` values, and the
optimal-`c_inf` search for IC_B returned an absurd `c_inf≈-6.3×10¹⁹` —
a sign the search was chasing a genuinely unconverged quantity. Checking
the raw deviations directly: `dev_B` reached `~9×10²²` by `N=10⁶` —
**astronomically large**, not the small, converging residual the real
system shows. Something in the `psi`/`dph`/`qm_hat` sector is growing
without the stabilizing behavior the full system exhibits.

**Likely cause, not confirmed**: the `qm_hat_N` equation carries a
`1/H_Λ` amplification factor (`H_Λ≈9.15×10⁻⁸`, so `1/H_Λ≈1.09×10⁷`) — even
a tiny residual in `dph-(1-pb)·psi` gets amplified enormously. Either (a)
this reduction dropped a term that provides real stabilization in the full
system (plausible — the `(1-gh·pb)` denominators and sub-leading `pb`
corrections were kept in some places and simplified in others, and a
by-hand derivation of a 6-variable coupled system carries real error
risk), or (b) the arbitrary initial conditions chosen excite a mode that
real trajectories, arriving via the actual early `k`-dependent transient,
never reach.

---

## Verdict — **`MECHANISM-PARTIALLY-CONFIRMED`**

Two different claims, kept separate rather than merged into one verdict:

1. **The existence of *an* affine relationship between any two solutions
   reaching this regime is genuinely explained** — confirmed independently
   on arbitrary initial conditions, not inferred from `FINDING_P126`'s own
   observation. This is real progress: not "k=0.3 and k=0.5 happen to
   match," but "any two late-time trajectories of this reduced system are
   forced into an affine relationship by construction."
2. **The specific value `q≈0.466` (and therefore the path to computing
   `A≈6679` itself) was not reproduced.** The reduction either has an
   error, or is missing a stabilizing term, in the `psi`/`dph`/`qm_hat`
   sector specifically — the same sector `FINDING_P125`/`P126` already
   flagged as not independently re-derived.

This is not a clean resolution of the user's request, and is reported as
such rather than dressed up as one.

### Not established

- Why the specific value `A≈6679` exists — this remains genuinely open;
  this file's own attempt at the mechanism did not get far enough to
  compute it.
- A closed-form or even a correctly-reproduced numerical value for `q`
  from the reduced system — the reduction as built here does not converge
  the way the real system does.
- Whether the discrepancy is a derivation error or a genuine IC-selection
  issue — not distinguished here; would need either careful re-derivation
  (ideally cross-checked symbolically, not by hand) or initial conditions
  actually extracted from the real system's own early transient at a
  matching point.
- Anything about MULTING itself (Gate 1). Any `k[h/Mpc]`.

### Where this could go next (named, not committed)

Extract the real system's own state vector at some intermediate `N`
(where `k²/a²` is already small but not yet negligible over the full
range) and use *that* as the reduced system's initial condition, rather
than an arbitrary guess — this would test whether the reduction is
correct given a realistic hand-off point, isolating whether the gap found
here is a derivation error or an IC artifact.
