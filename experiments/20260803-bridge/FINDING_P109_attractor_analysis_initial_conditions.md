# FINDING P109 — **Mixed: attractor-like at `k=0.1`/`k=10`, `IC-DOMINATED` at `k=1`.** Initial conditions are the new bottleneck — but only in a narrow, specific place

**Status:** built, run, regression control exact, verdict against
pre-registered outcomes, non-uniform across `k`.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P109_attractor_analysis_initial_conditions.py`

> User-proposed pivot after `FINDING_P108` closed the `Λ`-branch
> question: does the same asymptotic `G_∞(k)` also converge across
> **initial conditions**, at a fixed `Λ`? If both freedoms wash out, that's
> attractor-like universality — a stronger predictive-content claim than
> `Λ`-invariance alone. If not, IC selection becomes the next real
> bottleneck.

---

## Why this is a genuinely new question, checked before building

Two prior results touch IC sensitivity, and neither answers this file's
question. `FINDING_P76`'s own Part E "lever gate" tested `G_growth`'s
sensitivity to the same kind of IC variants, but at a **snapshot**
window with `Λ` not yet existing — and `FINDING_P107` itself proved
snapshot and asymptotic behavior can be qualitatively different (`eps`
looked fine at a snapshot but was structurally the wrong tool
asymptotically). `FINDING_P79` tested `φ̄̇(1)` sensitivity, but on a
**different quantity** (separation between two completions, not
`G_growth` itself) at low, non-asymptotic `k` — and found a real,
documented sign-flip there. Neither result substitutes for testing the
converged `G_∞` directly.

## Reconnaissance and regression control

At `Λ=1e-15` (one of `FINDING_P107`'s own full-reach branches), every IC
variant reaches `a(T_END)/a_star = 5948.0` to 4 significant figures,
matching baseline exactly — IC perturbations of this size don't shift
*when* `Λ` domination kicks in, so no `T_END` widening was needed
(unlike `FINDING_P108`). Regression control against `FINDING_P107`'s own
published `G_∞` at `Λ=1e-15`: relative diffs `~10⁻⁷`, essentially exact.

## Results — 7 IC variants × 3 `k`, T-convergence on `G_growth`

All 7 variants individually T-converge at all 3 `k` (final-step changes
`0.0000%`–`0.38%`, all inside `P76`'s own `2%` gate).

**Amplitude ICs are irrelevant.** `psi0×100`, `drA0×10`, `dph0×100` all
match baseline to within `~0.001%` at every `k` — unsurprising: `G_growth`
is a ratio of contrasts, and rescaling small linear-perturbation
amplitudes shouldn't move a ratio to leading order.

**`φ̄̇(1)` is the entire story:**

| `k` | converged `G_∞` range | relative spread | verdict |
|---|---|---|---|
| `0.1` | `[1.000046, 1.012746]` | `1.26%` | `ATTRACTOR-LIKE-UNIVERSALITY` |
| `1.0` | `[1.021908, 1.108586]` | `8.18%` | `IC-DOMINATED` |
| `10.0` | `[1.094957, 1.095980]` | `0.09%` | `ATTRACTOR-LIKE-UNIVERSALITY` |

At `k=1`, `φ̄̇(1)×0.1` gives `G_∞=1.1086` and `φ̄̇(1)×2` gives
`G_∞=1.0219` — both individually T-converged cleanly (`0.0015%` and
`0.0003%` final-step change respectively), so this is a real,
well-measured difference, not noise.

**One honesty flag, not swept under the verdict:** the `φ̄̇(1)×0.1` row
at `k=0.1` is *not* monotonic on its way to convergence
(`1.0113 → 1.0269 → 1.0109 → 1.0067 → 1.0166 → 1.0128`) — it wobbles
before settling, unlike every other row in this file, which approaches
smoothly. It still passes the `<2%` final-step gate (`0.38%`), but this
is measurably less clean than `k=10`'s convergence, and is reported as
such rather than presented with equal confidence.

---

## Verdict — **Non-uniform: robust at the extremes tested, IC-sensitive in between**

Late-time dimensionless growth is attractor-like at `k=0.1` and `k=10`,
but genuinely **IC-dominated at `k=1`**, driven specifically by the
background field's own initial velocity, not by any perturbation
amplitude. This is *not* the same finding as `FINDING_P79`'s (a
different quantity, low-`k` sign-flip) — but it is a second, independent
instance of `φ̄̇(1)` producing a large, k-localized effect in this
completion, worth keeping connected in mind rather than treated as
unrelated.

The user's own anticipated `IC-DOMINATED` outcome is confirmed — but
only in a narrow window, not uniformly. This is more informative than
either clean alternative would have been.

### Not established

- Anything at `Λ` values other than `1e-15` — a combined `Λ`-and-IC test
  was not attempted.
- Whether the `k=1` IC-sensitivity is itself a localized feature (a
  resonance-like effect near `k~1`) or the visible edge of a wider
  sensitive band — only `k=0.1, 1, 10` were tested.
- `φ̄̇(1)×10` (kination-dominated, excluded per `P77`/`P79`'s own
  precedent — not a legitimate IC variation).
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical
  units, or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
