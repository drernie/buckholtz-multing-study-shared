# FINDING P106 — **CONTROL-FAILS, twice.** The k=0.1 ambiguity was not resolved — a deeper, more general gap was found instead

**Status:** built, run twice (a design flaw caught and fixed mid-build did
not save the result — the corrected version failed for a different,
more informative reason), pre-registered `CONTROL-FAILS` outcome reached
honestly, not relaxed to force a pass.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P106_k01_window_vs_lambda_spread.py`

> `FINDING_P105` left `k=0.1`'s larger cross-branch spread honestly
> unresolved — real `Λ`-dependence, or window-choice noise on a mode
> `P76`'s own prior gates already found unreliable? This file tried to
> resolve it and instead found a **more general** methodological gap that
> makes the original question temporarily unanswerable with this
> approach.

---

## Attempt 1 — caught and diagnosed by its own control

First design: fix `a1 = a_star·0.2`, vary `a_end = a_star·{0.5, 1.0,
2.0}` — spanning `x=1`, the `Λ`-crossing itself. The control (checking
`k=1`/`k=10` within-branch window-spread against `FINDING_P105`'s own
cross-branch spread) **failed badly** — ratios of `10.9×` and `51.0×`.

Read before reported as a result: this window doesn't test window-choice
noise at all — it spans the matter-to-`Λ` **transition**, where `eps`
changing *is the physics*, not instability. `P76`'s own original
convergence check never crossed any such transition (`lam_cc` didn't
exist when it ran). Comparing "variation across a real transition" to
"variation across independent branches" was never a fair test. Corrected.

## Attempt 2 — narrowed to a local perturbation, control still fails

Corrected design: `a_end = a_star·{1.8, 1.9, 2.0}` — an `11%` local
perturbation right around `FINDING_P105`'s own comparison point
(`x_end=2.0`), testing whether *that specific choice* sits in a locally
stable part of the function.

| `k` | worst within-branch spread | `P105`'s cross-branch spread | ratio |
|---|---|---|---|
| `1.0` | `5.540×10⁻⁴` | `4.348×10⁻⁴` | `1.27×` |
| `10.0` | `1.014×10⁻³` | `1.697×10⁻⁴` | `5.97×` |

**Control still fails** — smaller ratios than attempt 1, but both still
well above the `0.10` threshold. This is **not** a bug to patch by
relaxing the threshold (that would be exactly the goalpost-moving this
project's own Anti-Overfitting discipline exists to catch) — it's a real
result.

---

## What this actually shows

Even at `k=1`/`k=10` — `P76`'s own certified, "clean corner" `k` — `eps`
is **still measurably window-length-dependent** at even an `11%`
perturbation near `x=2·a_star`. `P76`'s original convergence check found
these `k` stable, but over a completely different regime: `4` orders of
magnitude larger absolute `a`, deep into an established late-time state,
at `lam_cc=0` with no transition ever crossed. `FINDING_P104`/`P105`'s own
comparison window (`[0.2, 2.0]·a_star`, a factor of `10` in `a`) is
**modest** by comparison — evidently not deep enough into any asymptotic
regime for `eps` to have genuinely settled, at any `k`, not just `k=0.1`.

**This means:** `FINDING_P105`'s `CONVERGES (M1)` result at `k=1`/`k=10`
should be read precisely as what it measured — branch-to-branch agreement
of the eps **snapshot** at that specific window — not as evidence that a
fully asymptotically-converged growth-index-shift is `Λ`-independent.
Whether `eps` keeps converging to the *same* cross-branch-agreeing value,
or drifts apart, as the window is pushed deeper into an established
regime, is genuinely untested by anything in `P104`–`P106`.

---

## Verdict — **`CONTROL-FAILS`, the pre-registered outcome, reached honestly**

The `k=0.1` ambiguity is **not resolved** by this file. Not because the
test broke, but because the more fundamental prerequisite it needed —
confirming `eps` is window-converged at *all*, at any tested `k` — does
not hold at the window scale `P104`/`P105` used. Pushing the window
further to actually test asymptotic convergence (mirroring `P76`'s own
much larger relative reach) is a **different, larger** next step than
this file attempted, not a small patch to it.

### Not established

- Whether `k=0.1`'s cross-branch spread is real `Λ`-dependence or window
  noise — the original question, still open.
- Whether `FINDING_P105`'s `k=1`/`k=10` `CONVERGES` result would survive
  a genuine asymptotic-convergence test at much larger relative `a` — not
  refuted here, but not confirmed either.
- Any numeric value of `ε(k)` or `f(k)` in physical units, or any
  `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
