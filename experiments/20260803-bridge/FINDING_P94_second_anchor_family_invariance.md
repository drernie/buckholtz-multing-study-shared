# FINDING P94 — **STILL-DEGENERATE.** `Ω_m=0.315` does not resolve it either; the completion's `Λ` is a genuinely free scale

**Status:** built, control failed by its own construction and was sharpened
(not relaxed), re-run, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P94_second_anchor_family_invariance.py`

> `FINDING_P93` found `Ω_Λ=0.7` a tautology that cannot pick a reference epoch,
> and registered that a second anchor — `Ω_m` — used **with** `H₀` should break
> the degeneracy. It does not. The reason is more fundamental than a missing
> number: the completion's dark-energy term is a **free scale**, and no
> dimensionless ratio, however precisely measured, can pin a scale.

---

## A hand-derivation error, caught and not trusted

Before any code, working the unit algebra for how `Ω_m` and `H₀` jointly fix
`a_today` produced `Ω_m,int(a_today) = 8π·Ω_m` — nonsense, since `Ω` cannot
exceed `~1`. Rather than hunt the error by hand — demonstrably error-prone —
this file answers the question **numerically**, on machinery already verified
in `P86`/`P93`, per this project's own Compute-First discipline.

## The design

`P86`'s `lambda_for(a_today, frac)` ties `Λ` to `a_today` **by construction** —
reusing it would just repeat `P93`'s tautology. Instead: take `Λ_internal` as
**fixed**, using `P93`'s own four successfully-measured `Λ` values (from
`lambda_for(a_today_seed, 0.7)` at `a_today_seed = 1e4, 3e4, 1e5, 3e5`) as four
**independent** starting points — not re-derived per search. For **each** fixed
`Λ`, find the actual `a_today` where `Ω_m,int(a) = 0.315` **exactly** (Planck's
precise value, not the round `0.3` that `Ω_Λ=0.7` implies). If `H_int` at that
point agrees across all four `Λ` choices, `{H₀, Ω_m}` genuinely pin the bridge.
If it varies, the degeneracy survives.

## The control failed first, by its own construction — ninth this session

The first control checked **global monotonicity** of `Ω_m,int(a)` over
`[300, 3e6]` and failed on all four seeds. A finer 60-point scan found why:
small early-time bumps at `a < 5000`, `Ω_m ≈ 0.99–1.0` (order `1e-3`, far above
`0.315`) — likely residual oscillation-era scalar kinetic/potential energy.
**Global monotonicity was never what the root-find needs** — `brentq` needs a
**single sign change**, which the same 60-point scan confirmed on all four
seeds (`1` crossing each, `4–12` harmless early bumps reported alongside).
Sharpened, not relaxed: the control now checks exactly the precondition the
root actually requires.

## Results

| `Λ` seed | `Λ_internal` | `a_today` (`Ω_m=0.315` exactly) | `H_int` | `Ω_m` check |
|---|---|---|---|---|
| `1e4` | `2.3333e-12` | `9767.898792` | `5.342042e-06` | `0.314999995` |
| `3e4` | `8.6420e-14` | `29303.327613` | `1.028074743e-06` | `0.314999998` |
| `1e5` | `2.3333e-15` | `97678.960088` | `1.689285027e-07` | `0.315000002` |
| `3e5` | `8.6420e-17` | no root in range | — | not measured |

`3e5` is `BLOCKED-INFRASTRUCTURE`, excluded — not scored either way.

**`H_int(a_today_precise)` spread across the three measured branches:
`31.623095×`.** Pre-registered `STILL-DEGENERATE` threshold was `>1.10×`
(`10%`). This is not a marginal miss — it is three thousand percent over.

## The mechanism, confirmed rather than left as a bare number

```
a_today_precise / a_today_seed  =  0.976790 / 0.976778 / 0.976790   -- constant
H_int(a_today_precise)  ∝  a_today_precise^(-3/2)  to 4-5 significant figures
```

The correction from `Ω_m=0.3` (implicit in `Ω_Λ=0.7`) to the precise `0.315` is
a **near-constant multiplicative shift** (`≈0.9768`) applied to whichever
`a_today_seed` a branch started from — so the three-branch spread reduces to the
**same** `a^{-1/2}` power law in `a·H` that `FINDING_P93` already established to
five significant figures, now confirmed via a **structurally independent**
computational path: fixed `Λ`, exact root on `Ω_m`, rather than `P93`'s fixed
epoch with `Λ` derived from `Ω_Λ=0.7`.

**Why this is not circular.** `P93`'s family varied `a_today` along **one**
continuous curve `Λ(a_today) = lambda_for(a_today, 0.7)`. `P94`'s family holds
`Λ` **fixed** at four values taken from that curve and re-solves for `a_today`
under a **different** criterion (`Ω_m=0.315` exactly, not `Ω_Λ=0.7` at the
seed). That the same power law re-emerges from a different construction is
independent corroboration, not restatement — it shows the degeneracy is a
property of the **physics** (matter-domination scaling `H² ∝ a⁻³` near any
`Ω_m≈0.3` epoch), not an artifact of `P93`'s specific parametrization.

## Verdict — **STILL-DEGENERATE**

`{H₀, Ω_m}` do **not** pin the bridge. `Λ_internal` is a genuinely free knob of
the completion — `FINDING_P86` added it as *"a constant added to the
potential,"* with nothing in the model deriving its scale — and a **dimensionless
ratio** (`Ω_m`, however precisely measured) can only ever fix the **composition**
at whatever epoch you land on; it cannot fix the **absolute density scale**,
which is what actually determines `H_int(a_today)` and hence the bridge.

**No `k[h/Mpc]` number is quoted.** The situation is worse than `P93` left it:
not "one anchor short," but structurally short by an anchor that supplies an
**absolute scale**, not another ratio. The natural candidate is requiring the
completion's dark-energy term, once `κ` is fixed, to reproduce the actual
**physical** cosmological constant (`Λ_phys ≈ 1.1×10⁻⁵² m⁻²` or equivalently
`ρ_Λ ≈ 5.8×10⁻²⁷ kg/m³`) — but nothing in this model predicts that value; it
would have to be **imposed**, which is a different kind of step than sourcing a
dimensionless ratio and needs its own Gate 2 (Target Provenance) treatment
before being attempted.

### Not established

- Any numeric value of `ε(k)` or `f(k)` in physical units.
- That `Ω_m=0.315` is measured independent of `Ω_Λ` — flatness is assumed, as it
  already was in `FINDING_P86`'s construction.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file.
