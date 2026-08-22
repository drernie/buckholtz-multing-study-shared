# FINDING P118 — A derived, regression-verified rescaling gets past `FINDING_P117`'s numerical wall by ~180 decades — and the climb still doesn't plateau

**Status:** built, regression-verified against the original system (not
assumed), extension confirmed directly, main scan re-run at the vastly
extended reach. All controls pass.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P118_rescaled_density_reformulation.py`

> User-directed: "try a log-density reformulation to get past the wall."
> `FINDING_P117` traced the wall precisely: `rho_A = C_MATTER/a³`
> underflows to exactly `0.0` once `a³` overflows float64
> (`a > ~5.65×10¹⁰²`), making `contrast = delta_m/rho_phys` exactly `±inf`.

---

## The reformulation, derived not guessed

Track rescaled variables `drA_hat := drA·a³`, `qm_hat := qm·a³` instead of
`drA`, `qm` directly. Re-deriving their ODEs via the product rule and
`P105`'s own equations:

```
d(drA_hat)/dt = 3·psid·C_MATTER + k²·qm_hat/(a²·(1-gh·pb))   ← only a², not a³
d(qm_hat)/dt  = C_MATTER·[gh·dph - (1-gh·pb)·psi]              ← no a-dependence at all
```

Every appearance of `rho_A·a³` collapses to the exact constant `C_MATTER`
— never computed via a raw `a³` that can overflow. `contrast` is
reformulated the same way (`delta_m·a³` over `rho_phys·a³`, the `a³`
factors canceling exactly):

```
contrast = [drA_hat·(1-gh·pb) - gh·C_MATTER·dph - 3·H·qm_hat] / [C_MATTER·(1-gh·pb)]
```

## Controls, all pass

- **Regression** (the critical gate, checked before trusting anything
  else): reformulated `contrast` vs. the original system's, at four `x`
  values within both systems' valid range — agree to `7×10⁻¹¹`–`2×10⁻⁸`.
- **Smooth-case regression** (`k=10`): agrees to `10⁻¹²`–`10⁻¹⁴`.
- **Extension**: at the *same*, unchanged `T_END=7e9`, the reformulated
  `contrast` stays finite all the way to `x=1e278` (`a≈1e283`) — where the
  original system had already returned exactly `±inf` around `x≈1e98`.
  **~180 more decades of valid reach.**

## What did *not* change: `a` itself is a separate, absolute ceiling

An initial attempt to also push `T_END` further failed — `a` (unrescaled,
its own growth `da/dt = a·H` untouched by this reformulation) still hits
float64's absolute maximum at the same `t≈7.634×10⁹` `FINDING_P117` found.
The reformulation extends *contrast's* valid range within the existing
trajectory; it does not extend the trajectory itself. (A further
reformulation tracking `ln(a)` as the state variable, rather than raw `a`,
is the natural next step to push past *this* wall too — not attempted
here.)

## Main result — the climb continues, decelerating, no plateau

Re-running `FINDING_P117`'s own decisive `x_lo`-independence scan at
`a_reach=1e278·a_star`, `T_END=7e9` (unchanged):

```
x_lo=1       1,013,737
x_lo=1e30    1,050,098   (+3.6% over 30 decades)
x_lo=1e90    1,080,799
x_lo=1e200   1,107,517
x_lo=1e270   1,118,029   (+0.95% over the last 70 decades)
```

Still monotonic, still no plateau — total rise `10.29%` across the whole
extended range — but the **rate** of rise is visibly decelerating (`3.6%`
per 30 decades early on, down to `0.95%` per 70 decades late), consistent
with (though not proof of) a genuine asymptote existing somewhere far
beyond what even this reformulation can reach.

---

## Verdict — the reformulation works exactly as designed; `FINDING_P117`'s conclusion stands, now on much stronger ground

The user's request was answered directly and successfully: a log/rescaled-
density reformulation *was* built, it *does* get past the wall, by a
verified ~180 decades. What it reveals, honestly, is that `FINDING_P117`'s
`STILL-NOT-CONVERGED` verdict was correct — not merely because the reach
ran out, but because the value keeps climbing even across a domain 180
decades larger than anything tested before. This is a stronger result than
`FINDING_P117` could produce alone: the non-convergence is no longer just
"we hit a wall and stopped," it is "we pushed the wall back by 180 decades
and it's still not enough."

### Not established

- A value for `G_E`'s true asymptote, if the climb continues — only that
  the wall has been pushed much further out, and the rate of climb is
  slowing.
- Whether an even further reformulation (tracking `ln(a)` itself, to push
  past the *outer* `a`-overflow wall too) would eventually reveal a
  plateau — not attempted here.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
