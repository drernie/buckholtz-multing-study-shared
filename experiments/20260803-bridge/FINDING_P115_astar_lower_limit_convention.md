# FINDING P115 — The `a_star` lower-limit convention agrees with `FINDING_P114`'s `a0`-anchored result to within `0.6%`

**Status:** built, all three controls pass, main test converges even more
tightly than `FINDING_P114`'s own. Directly answers an item `FINDING_P114`
left open and a concern its skeptic review raised.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P115_astar_lower_limit_convention.py`

> User-directed: "try the `a_star` lower-limit convention instead."
> `FINDING_P114`'s skeptic review found `a0 = A3_INIT**(1/3)` is a fixed
> convention inherited from `P76` — tied to this arc's shared ODE start time
> — not a physically privileged epoch, and its sensitivity was never
> independently tested. This file tests it directly.

---

## The alternative convention

`a0` answers "wherever this arc's solver happens to start integrating".
`a_star` answers a different, already load-bearing question in this
sub-arc: `a_star(Λ) := (C_MATTER/Λ)^(1/3)`, the `ρ_Λ = ρ_matter` crossing,
first defined in `FINDING_P104` and used as the reference scale by every
file since. Using it as the integral's lower limit substitutes a genuinely
physical anchor for a purely infrastructural one:

```
E'(a_reach)   := integral[a_star, a_reach] contrast(a)^2 d(ln a)
G_E'(a_reach) := E'_coupled(a_reach) / E'_reference(a_reach)
```

## Results

- **`k=10` baseline**: resolution-checked (`n=4000…32000` agree to 6 decimal
  places — tighter than `FINDING_P114`'s own check), converges to
  `√G_E'=1.476668` — essentially the same as `FINDING_P114`'s `a0`-anchored
  value (`1.474`, `~0.2%` apart).
- **`k=0.3`, `φ̄̇(1)×0.1`**: converges *even more tightly* than
  `FINDING_P114`'s own main test — final-step change `0.042%` (vs.
  `FINDING_P114`'s `0.22%`) — to `√G_E'=389,236`.
- **Positive control (convergence)**: passes.
- **Amplitude-scaling** (`ICs×3 → G_E'×9`): observed `9.0000` exact — kept
  here for internal-consistency checking only, per the skeptic-corrected
  framing (it verifies the linear-ODE machinery, not the domain choice's
  physical meaning).
- **Crossing-robustness** (excise the real transition): `0.14%` change —
  passes threshold `2%`.

## The key comparison

`√G_E' = 389,236` vs. `FINDING_P114`'s `√G_E = 386,921` (`a0`-anchored) —
a **`0.60%` relative difference**. The specific concern the skeptic raised
— that `a0`'s arbitrariness was untested and could matter — is now directly
tested, not assumed away: switching to a genuinely different, independently
principled lower-limit convention moves the converged value by well under
`1%`.

**This is not the same finding as the already-documented `~40%`
sensitivity.** `FINDING_P114`'s own follow-up check found `√G_E` moves by
`~40%` between `x_lo=1` (`≈a_star`) and `x_lo=100` (past the transient) —
that sensitivity is real, unaffected by this result, and not re-tested
here. What this file shows is narrower and different: the `a0`-vs-`a_star`
axis specifically — the one the skeptic flagged as untested — is *not*
where that sensitivity lives. `a0` (deep in the matter-dominated era) and
`a_star` (the `Λ`-matter crossing) give almost the same answer; the
transient stretch between `x=1` and `x=100` is where the real sensitivity
concentrates.

---

## Verdict — the `a0`-arbitrariness concern is resolved; the transient-inclusion sensitivity stands

The skeptic-raised concern about `a0` specifically is answered: it is not a
major source of `FINDING_P114`'s uncertainty. `FINDING_P114`'s own
already-reported `~40%` sensitivity to the transient stretch remains real
and is not addressed by this file.

### Not established

- The already-documented `~40%` sensitivity to including/excluding the
  `x=1`-to-`100` transient stretch — not re-tested or resolved here.
- That `G_E'` matches `G_growth` numerically — it does not, for the same
  reasons `FINDING_P114` documented.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units, or
  any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
