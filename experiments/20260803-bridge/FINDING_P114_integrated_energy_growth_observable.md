# FINDING P114 — A fundamentally different observable: **`OBSERVABLE-CONVERGES`** (revised from an initial `GAP-CLOSES` overclaim after context-asymmetric skeptic review)

**Status:** built, all four controls pass, main test converges cleanly
(`0.22%` final-step change). An adversarial self-check before reporting
found a real caveat (lower-limit sensitivity). A subsequent
**context-asymmetric skeptic review** (claim + code only, no reasoning
chain — per this repo's Step 8a discipline) went further and found the
original `GAP-CLOSES` framing itself overclaimed. Verdict revised
accordingly, not smoothed over.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P114_integrated_energy_growth_observable.py`

> `FINDING_P113` fixed a real anchor bug in the windowed RMS/peak
> observable, but the underlying construction — a *local* average — still
> failed: no power-law plateau wide enough to support a window at any width
> tested. User-directed: try something genuinely different, not another
> window.

---

## The observable

Integrate the **squared** contrast over the entire trusted trajectory, from
the actual start of integration (`a0`) out to a chosen reach — no anchor
point needed at all:

```
E(a_reach)   := integral[a0, a_reach] contrast(a)^2 d(ln a)
G_E(a_reach) := E_coupled(a_reach) / E_reference(a_reach)
```

A local zero-crossing contributes a *small* amount (`|contrast|²` is itself
small there) instead of blowing up a ratio. Convergence is tested by pushing
`a_reach` further, the same way `FINDING_P107` tested `G_growth`.

## Reconnaissance and controls — all pass

- **`k=10` baseline**: `G_E` converges almost immediately (`√G_E=1.474` by
  `x=100`), but **not** to `G_∞=1.095773` — expected, since `G_E` integrates
  the whole history, a genuinely different quantity from `G_growth`'s
  late-time point ratio.
- **`k=0.3`, `φ̄̇(1)×0.1`**: `√G_E` peaks near `x=100` then declines smoothly
  toward `~386,000–387,000` by `x=1e6–1e8` — resolution-checked
  (`n=4000…32000` agree to 5 decimal places) and reach-checked
  (`T_END=3e9`).
- Positive control (convergence): `0.16%` final-step change — passes.
- Amplitude-scaling (`ICs×3` → expect `G_E×9`): observed `9.0000` exact.
- Crossing-robustness (excise noise crossing / real transition, narrow
  windows): `0.00%` / `0.14%` — passes threshold `2%`.
- Main convergence (`k=0.3`): final-step `0.22%` — passes threshold `5%`.

## Self-found caveat, before the skeptic even ran

Adversarial self-check: restricting the integral's *lower* limit from `a0`
to `x_lo=100` (excluding the transient stretch) gives a converged
`√G_E≈260,000–270,000` — vs. `~400,000–430,000` at `x_lo=1`. Each is
internally stable, but they genuinely differ by `~40%`. The transient is not
diluted away; it leaves a real, persistent imprint on the total. Reported in
the first version of this finding as a caveat that "does not overturn the
verdict, but sharpens what it means" — the skeptic review below found that
framing itself needed correcting.

---

## Skeptic review — context-asymmetric (claim + code only), verdict `WEAKENED`

Five concrete lines of attack, each resolved explicitly (per Step 8a's
response matrix — `WEAKENED` is not a veto, each concern gets a response):

| # | Concern | Resolution |
|---|---|---|
| 1 | `"a0 is the unique, non-arbitrary starting point"` is false — `a0 = A3_INIT**(1/3)`, and `A3_INIT` is a fixed constant *imported from `P76`*, tied to this arc's shared ODE start time `t=1`, not a physically privileged epoch. Its sensitivity was never tested. | **Accepted.** Verified directly: `P105_growth_with_lambda_cc.py:131` imports `A3_INIT = p76.A3_INIT`, used at line 183 as `a0 = A3_INIT**(1/3)`. The claim is corrected — `a0` is a convention inherited unchanged from every earlier file in this arc (not introduced or tuned here, unlike `X_LO`), but calling it "non-arbitrary" overstated what was established. Not independently stress-tested (would require re-running with a different `A3_INIT` convention — not attempted). |
| 2 | The amplitude-scaling control (`ICs×3 → G_E×9`) is guaranteed to pass by the linear-ODE construction of the perturbation system itself — it tests `scipy`'s IVP linearity, not whether the anchor/domain choice is physically meaningful. | **Accepted, reclassified.** The control genuinely does verify implementation correctness (it *did* catch a real bug in `FINDING_P112`'s first attempt, where scaling only `dph0` alone broke the prediction) — but it is not evidence about domain-choice validity, and this finding no longer cites it as such. |
| 3 | The narrow crossing-robustness excision (`~0.6` decades) is much narrower than the `~2`-decade lower-limit shift that produced the `~40%` sensitivity already found — its clean pass gives false comfort about the wider, already-known sensitivity. | **Accepted.** This is the same caveat already reported above, now stated more sharply: the control's narrow scope should not be read as evidence of robustness to the *wider* region's cumulative contribution, which is demonstrably real. |
| 4 | `"GAP-CLOSES"` overclaims: `FINDING_P110`'s original question was about `G_growth`'s convergence; `G_E` is a provably different quantity (`34%` off `G_∞` even on the smooth `k=10` case) — reporting its convergence as "the gap closes" swaps the question rather than answering it. | **Accepted — the core correction.** Verdict relabeled `OBSERVABLE-CONVERGES` throughout this document and in `P114_integrated_energy_growth_observable.py`'s own printed output. What is established: a well-defined, numerically stable, control-passing quantity exists for this branch where every earlier attempt could not produce one. What is *not* established: that `G_growth`'s own divergence/instability has been resolved or explained. |
| 5 | Quadrature over a sharp transient (`δφ` reaching order `1–5` from `~1e-7`) could carry large local error even if the reported number "looks converged" under reach extension, since reach-convergence proves the *tail* is small, not that the *peak* was integrated accurately. | **Dismissed as already adequately addressed**, not ignored: the resolution check (`n=4000→32000`, agreeing to 5 decimal places) directly tests peak-integration accuracy — increasing sample density resolves the peak better regardless of reach, and the value didn't move. A distinct concern from tail-convergence; already covered by an existing control, not a new gap. |

---

## Verdict — **`OBSERVABLE-CONVERGES`** (not `GAP-CLOSES`)

A well-defined, numerically stable, fully-controlled quantity — genuinely
different in construction from every point-sampled or windowed attempt in
this sub-arc — converges cleanly for `(k=0.3, φ̄̇(1)×0.1)`: `G_E→1.497×10¹¹`
(`√G_E≈386,921`), surviving resolution checks, reach extension, amplitude-
scaling, and narrow crossing-robustness. **This is real progress**: it is
the first time in the entire `k<1` investigation that a controlled,
converging number has been produced for this branch. **It is not** a
resolution of `FINDING_P110`'s original `G_growth`-convergence question —
`G_E` is a different, adjacent quantity, and its convergence does not, by
construction, tell us that `G_growth` itself would converge or what it
would converge to.

### Not established

- That `G_E` and `G_growth` measure the same physical quantity — they do
  not.
- That `FINDING_P110`'s original `k<1` growth-**ratio** question is
  resolved — it is not.
- That `a0` (the arc's shared `A3_INIT` convention) is a physically
  privileged epoch rather than simply where integration happens to start —
  not independently stress-tested.
- Whether a different, equally-principled lower-limit convention (e.g.
  starting at `a_star`) would give a more physically interpretable
  quantity — not attempted here.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units, or
  any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
