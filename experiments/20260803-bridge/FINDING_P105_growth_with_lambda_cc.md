# FINDING P105 — **`G_growth` extended, regression-perfect. `CONVERGES (M1)` at P76's own certified k — `FINDING_P104` extends to the perturbation level**

**Status:** built, run, regression control exact, verdict corrected before
finalizing (a naive relative-spread metric was caught overclaiming
divergence at a mode `P76` itself already disowns).
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P105_growth_with_lambda_cc.py`

> User-directed: "extend `G_growth` to accept `lam_cc`." `FINDING_P104`
> found the background's dimensionless shape survives `Λ_internal`'s
> freedom, but could not test the user's original proposal (`k_J/(aH)`,
> `f(k)` growth-difference ratios) — `G_growth`/`contrast` never accepted
> `lam_cc` anywhere in `P76`–`P92`. This file builds that extension and
> runs the same test one layer down.

---

## The analytic argument for where `lam_cc` goes, before any code

`P76`'s `bg_quantities` computes `V = λφ̄⁴/4` and `H = √((8πG/3)(ρ_phys +
φ̄̇²/2 + V))`. Does adding `lam_cc` to `V` change `Hdot = -4πG(ρ_phys +
φ̄̇²)`? Derived directly: `2H·Ḣ = (8πG/3)·d/dt(ρ_phys + φ̄̇²/2 + V)`. Working
through each term's time derivative — the `ĝρ_A φ̄̇` cross-terms cancel
against each other, the `V'φ̄̇` cross-terms cancel against each other —
what survives is exactly `-3H(ρ_phys+φ̄̇²)`, **identical to the existing
`Hdot` formula, with no `lam_cc` term at all**. `Λ`'s equation of state
(`w=-1`) makes its `(ρ+p)` contribution to `Ḣ` exactly zero by
construction. So: `H`'s formula is the *only* place `lam_cc` enters;
`Hdot` and every perturbation equation (`ψ̈`, `δφ̈`, `δρ̇_A`, `q̇_m`) need no
new term — they already depend on `lam_cc` correctly, purely through `H`
and `Hdot`, once those two are computed right.

## Not touched: `P76_growth_observable.py` itself

Every file in this arc extends or wraps a prior file rather than editing
it in place — `P76` is loaded by many later reconstructions (`P88`–`P92`),
so editing it would be a blast-radius risk. This file **reimplements** the
9-state background+perturbation system with `lam_cc` threaded through
exactly where the analytic argument says it must go, verified identical
to the original at `lam_cc=0`.

## Regression control — exact

| `k` | `P76` `G_growth` | this file `@lam_cc=0` | rel diff |
|---|---|---|---|
| `0.1` | `1.008547386400` | `1.008547386400` | `0.0` |
| `1.0` | `1.160141080499` | `1.160141080499` | `0.0` |
| `10.0` | `1.314850304498` | `1.314850304498` | `0.0` |

Same exact match on `eps(k)`. **`0.000e+00` relative difference at every
tested `k`** — the extension changes nothing at `lam_cc=0`, exactly as the
analytic argument required. Sanity check: `G_growth(k=1, lam_cc=1e-13) =
1.0833` vs `G_growth(k=1, lam_cc=0) = 1.1601` — `lam_cc` genuinely changes
the result, not a silent no-op.

## The Predictive Quotient test, one layer down from `FINDING_P104`

Same anchor-free branches as `P104` (`a_star(Λ):=(C_MATTER/Λ)^(1/3)`), same
6 `Λ` values, window `[a_star·0.2, a_star·2.0]` per branch, comparing
`eps(k;Λ)` — `P76`'s own established, window-free growth-index-shift
observable (Part G).

| `k` | status | eps range | rel spread | abs spread |
|---|---|---|---|---|
| `0.1` | `P76`-flagged-noisy | `[-0.001017, 0.001552]` | `5.79×` | `2.569×10⁻³` |
| `1.0` | `P76`-certified | `[0.019282, 0.019717]` | `2.22×10⁻²` | `4.348×10⁻⁴` |
| `10.0` | `P76`-certified | `[0.035986, 0.036155]` | `4.70×10⁻³` | `1.697×10⁻⁴` |

## Catching my own overclaim before writing a verdict

A naive threshold check (`>30% ⇒ DIVERGES`) fires on `k=0.1`'s `579%`
relative spread. Before accepting that: `eps(0.1)` **crosses zero** across
branches, and `P76`'s *own* file — a prior, independent experiment —
already established that `k=0.1` fails its own T-convergence/lever gates
("anyone quoting eps at k≤1 from this file would be quoting noise").
Excluding `k=0.1` from the headline verdict is not a rescue invented here
to save M1 — checked explicitly against this project's Anti-Overfitting
Gate: **5/5 pass** (pre-registered in a prior experiment, more specific
not less, still falsifiable, independently motivated by `P76`'s own
gates, not this file's convenience). `k=0.1`'s absolute spread is
genuinely the largest of the three, so it isn't dismissed as pure
zero-crossing noise either — it's reported separately, honestly
unresolved, since this file never re-verified T-convergence per branch
there.

---

## Verdict — **`CONVERGES (M1)` at `P76`'s own certified `k` (`1`, `10`)**

`eps(k;Λ)` agrees across independently-chosen, unanchored `Λ` branches to
within `2.2%` at `k=1` and `0.5%` at `k=10` — both comfortably inside even
`FINDING_P104`'s stricter `5%` background-level threshold. **The
perturbation-level dimensionless growth also survives `Λ`'s structural
freedom**, at the `k` values where the underlying measurement is reliable
in the first place — extending `FINDING_P104`'s background-level result
to the layer the user's original proposal (`k_J/(aH)`, `f(k)` ratios) was
actually about.

`k=0.1` is reported separately, not folded into the headline: already
known-unreliable before this file ran, genuinely larger absolute spread
there than at `k=1`/`k=10`, but whether that reflects real
`Λ`-dependence or accumulated noise on an already-noisy baseline is not
resolved here.

### Not established

- That `eps(k;Λ)` is T-converged per branch the way `P76`'s own Part D
  gate required — this file measures one window per branch, not across
  the four-decade convergence check `P76` itself used.
- That `[0.2, 2.0]·a_star` is the right window — a different window could
  give a different spread; not scanned.
- Anything at `k` outside `{0.1, 1.0, 10.0}`.
- Whether `k=0.1`'s larger absolute spread reflects real `Λ`-dependence —
  genuinely open, not resolved by this file.
- Any numeric value of `ε(k)`, `f(k)`, or `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
