# FINDING P117 — A stiffer integrator doesn't help; and a "TRUE-ASYMPTOTE-FOUND" verdict drafted from this same investigation was **RETRACTED** after a skeptic-driven check proved it wrong

**Status:** built, all controls pass. An earlier draft of this file and its
own committed finding reported `TRUE-ASYMPTOTE-FOUND`; a context-asymmetric
skeptic review found the supporting evidence near-tautological, direct
follow-up testing confirmed the skeptic was right, and the verdict is
retracted here — not smoothed over, not left as a footnote — with the full
corrected picture.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P117_stiffer_integrator_and_true_asymptote.py`

> User-directed: "push a stiffer integrator to converge the deep-cut tail."
> `FINDING_P116`'s reach-sensitivity control had failed at `x_lo=100`
> (`17.79%` shift between `a_reach=1e7` and `1e8·a_star`).

---

## Part 1 — the literal request, tested directly: it does not work

`RK45` (already in use) vs `Radau`/`BDF`/`LSODA` at `T_END=1e10`:

| Method | Result |
|---|---|
| `Radau` | Crashes outright — Jacobian probe overflows float64. |
| `BDF` | Fails at the very first step. |
| `LSODA` | Reaches the same `t≈7.633×10⁹` `RK45` does, then fails *worse* (`a=nan`). |
| `RK45` | Cleanest: successful steps to `t=7.630×10⁹`, only failing at `t=7.634×10⁹` where `a` hits float64's actual maximum. |

**A stiffer integrator does not help.** The bottleneck is a genuine
floating-point *range* overflow of the scale factor `a`, not stiffness — no
method, however implicit, evades it.

## Part 2 — the diagnosis pointed at a real gap, first pursued too far

Every prior file in this arc used `T_END=3e9` as a conservative margin,
never pushed to its actual limit (`~7.634×10⁹`). Pushing `RK45` (unchanged)
to `T_END=7e9` reaches `a_reach/a_star` up to `~1e270` — vastly beyond
anything tested before, and at fixed `x_lo=1`, `√G_E` does keep rising
smoothly (dense-scanned, resolution-checked to `<0.001%`) from `389,259`
past `870,000`. This part of the investigation is solid and stands.

## Part 3 — where an earlier draft overclaimed, and how it was caught

That earlier draft cross-validated only `x_lo=1` and `x_lo=100` at a shared
`a_reach=1e270·a_star`, found them agreeing to `0.48%`, and reported
`TRUE-ASYMPTOTE-FOUND`.

**A context-asymmetric skeptic review (claim + code only) returned
`WEAKENED`, with a specific, sharp attack**: the two domains overlap over
`>99%` of their integrated length (`ln(a)` ranges `~622` units total; the
two lower limits differ by only `~4.6` units). Their `0.48%` agreement is
close to arithmetically guaranteed by that overlap, not independent
evidence of convergence — a genuine test needs a third lower limit *inside*
the dominant region.

**Tested directly, not just conceded**: `x_lo=1e50` (well inside the
"shared" region, still numerically clean) gives `√G_E=983,466` — `~12–17%`
*above* the `x_lo=1`/`100` values. A full scan from `x_lo=1` to `x_lo=1e90`
at a fixed, safe `a_reach=1e94·a_star` shows `√G_E` climbing
**monotonically, with no plateau, the entire way**:

```
x_lo=1      863,854
x_lo=1e10   902,197
x_lo=1e30   951,894
x_lo=1e60   990,921
x_lo=1e90 1,015,170     (+17.5% over x_lo=1, still rising)
```

**The `TRUE-ASYMPTOTE-FOUND` verdict is retracted.** The prior draft's
resolution and reach-sensitivity checks were real and correctly executed —
they just weren't the check that mattered. The skeptic named the actual gap;
testing it overturned the headline claim.

## Part 4 — the hard numerical wall

`rho_A = C_MATTER/a³` underflows to *exactly* `0.0` once `a³` itself
overflows float64 (`a > ~5.6×10¹⁰²`, i.e. `a/a_star > ~5.6×10⁹⁷`). Past that
point, `rho_phys=0` and `contrast = delta_m/rho_phys` becomes exactly
`±inf` — not an approximation artifact, a representability wall tied to the
observable's own definition. No integrator can push past this; it depends
only on float64's range, not on step size or method. Traced directly:
`rho_A`/`rho_phys`/`delta_m`/`contrast` are all individually finite and
well-behaved (no precision loss found) all the way to `a/a_star~1e97`,
confirming the climb found in Part 3 is real, not numerical noise — it
simply never plateaus before the wall.

## Part 5 — the decisive control

The **identical** `x_lo` scan on the smooth `k=10` baseline shows `√G_E`
essentially flat (`1.4798→1.4800`, `<0.02%` total variation) across the
*same* `90+`-decade range that drove `k=0.3` up by `17.5%+`. This rules out
a code bug: the same construction, same integration, same arithmetic gives
a tightly converged answer for the smooth case and a genuinely,
monotonically non-converging one for the extreme-IC case.

**A side-note, to avoid a false "new discovery" claim**: a sign change in
`contrast_coupled` located between `x=3000` and `x=10000` during this
investigation is *not* new — it lands inside `FINDING_P112`'s own original
dense-scan finding of a transition at `a/a_star≈6934`. Confirms, does not
contradict, `FINDING_P111`/`P116`'s single-dominant-transient diagnosis.

---

## Skeptic response matrix (Step 8a)

| Concern | Resolution |
|---|---|
| `"Two-lower-limit cross-validation is near-tautological"` | **Accepted, and confirmed decisive.** Tested directly with a third limit (`x_lo=1e50`) and a full scan — the original `TRUE-ASYMPTOTE-FOUND` claim was wrong, not just under-supported. |
| Resolution check possibly not run at the actual frontier | **Tested and refuted as a separate concern**: resolution at `a_reach=1e270` itself holds to `<0.001%` (`n=32000→512000`). Not the source of the problem — the problem was `x_lo`, not resolution. |
| `geomspace`-in-`t` might systematically under-sample the tail vs. genuinely log-uniform-in-`ln(a)` | **Tested and refuted**: an independent log-uniform-in-`ln(a)` sampler agrees with `geomspace`-in-`t` to `<0.1%` at matched `n`. Not the source of the problem either. |
| Smooth-case control uses a different `x_lo` convention (`0.2`) than the main test (`1`, `100`) | **Accepted**; this file's rewritten smooth-case control uses the *same* `x_lo` grid as the main scan, removing the asymmetry. |

---

## Verdict — **`STILL-NOT-CONVERGED, NUMERICAL-WALL-IDENTIFIED`**

The user's literal request (a stiffer integrator) does not help. The
investigation it triggered found real, verified progress (P114–P116's prior
values were premature) and then — via a skeptic-caught, self-corrected
overclaim — a more precise and more honest final picture: the Integrated
Energy Growth Observable, pushed to the absolute safe numerical limit in
*both* `a_reach` and `x_lo`, does not converge to a lower-limit-independent
value for `(k=0.3, φ̄̇(1)×0.1)`. It climbs monotonically the entire way to a
hard numerical wall where the construction itself becomes undefined.
`FINDING_P110`'s original `k<1` growth-ratio question remains genuinely
open for this observable — what this file adds is a precise characterization
of exactly why and where this specific construction hits its limit.

### Not established

- Any value for `G_E`'s asymptote — there is no evidence one exists within
  float64's representable range for this branch.
- What physically happens to the `k=0.3` branch beyond `a/a_star~1e97` —
  unknowable in float64 without a reformulation avoiding division by a
  density that must underflow (e.g. tracking `ln(ρ)` instead).
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units, or
  any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
