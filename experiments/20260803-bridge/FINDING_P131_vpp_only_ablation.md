# FINDING P131 — Vpp-only mechanistic ablation: **`VPP-ONLY-REFUTED`**

**Status:** built, ran cleanly, one search-window artifact ruled out
directly before trusting the verdict.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P131_vpp_only_ablation.py`

> User-directed, in detail: a single, tightly-scoped **causal ablation**
> — keep the real background, real N=1 initial conditions (including
> their real k-dependence), and real couplings; delete only
> `kk²·exp(-2N)` from the ongoing perturbation dynamics — plus a mirror
> negative control (drop `Vpp` instead, keep `kk²·exp(-2N)`). Three
> outcomes specified in advance. **Close this line after this file,
> regardless of result.**

---

## Why an ablation, not another reformulation

`FINDING_P129`'s skeptic review established that an *exact* reformulation
of the same physics reproduces the same numbers as a matter of
arithmetic — not independent evidence. A first plan this session (solve
`pb(N)` independently, since it provably decouples, then solve the
linear `psi`/`dph`/`drA_hat`/`qm_hat` sector driven by that known `pb(N)`)
was recognized, before being built, as the same circularity in a new
disguise: it would reproduce `A_hat` exactly, telling us nothing new.

An **ablation** is different in kind: it deliberately *removes* real
physics from the dynamics. If the resulting, genuinely different numbers
still land near `6679`, that is real information — not guaranteed by
construction.

## The ablation

Term-by-term reconnaissance (this session) found the dominant
*instantaneous* driver of the resonance is usually `Vpp=3λφ̄²` (the
field's own quartic self-interaction), not `kk²·exp(-2N)` — though the
latter periodically exceeds `Vpp` (e.g. at N≈13). `P131` tests directly
whether `Vpp` alone is *sufficient*: `kk²·exp(-2N)` is zeroed everywhere
it appears in the dynamics (both `dphdd`'s own term and `drA_hat_d`'s),
while the real, k-dependent N=1 seed (via `psid0`'s own `kk²/a0²`
constraint term) is kept untouched. A mirror negative control does the
reverse: drop `Vpp` from that same term, keep `kk²·exp(-2N)`.

## Result

| Variant | peak `|psi|`(k=0.3) | peak `|psi|`(k=0.5) | ratio |
|---|---|---|---|
| unablated (positive control) | 2.6436 | 11231.95 | 4248.7 (matches `FINDING_P130`) |
| Vpp-only | 3.005×10⁻⁵ | 3.011×10⁻⁵ | **1.00** |
| k²-only | 6.769×10⁻⁵ | 6.037×10⁻⁵ | **0.89** |

`FINDING_P126`'s own `A_hat=6678.998`, for reference.

**One check before trusting this:** the first pass's Vpp-only peak sat
exactly at the search window's own lower edge (N=9.0) — indistinguishable
from a genuine peak vs. an under-sized search. Widened the window
(N=1.5–30, 2851 points) directly rather than assuming: the peak moved to
a genuine interior point (N=3.5, not at either new edge), with the
**same** ratio (1.00, unchanged). The k²-only peak was completely
unchanged (N=10.71 exactly). Confirms the result is robust, not a
search-boundary artifact.

---

## Verdict — **`VPP-ONLY-REFUTED`**

Neither ablated variant reproduces anything close to `A_hat=6679`
(`|log10(ratio)−log10(A_hat)|≈3.8` for both — nowhere near the same
order of magnitude). The dominant *instantaneous* term (`Vpp`, found by
term-by-term magnitude comparison) is **not** the dominant *integrated*
mechanism. The amplification genuinely requires the coupled
`kk²`-and-`Vpp` dynamics together — neither piece in isolation comes
anywhere close, confirming the user's own red-team point directly: an
oscillating system's largest-magnitude term at any given instant is not
automatically what drives its accumulated, integrated behavior.

**This mechanistic-ablation line is closed here**, per the user's own
explicit instruction, regardless of outcome — no further ablation
variants were attempted in response to this result.

### Not established

- A closed-form transfer/gain formula for the coupled system — not
  attempted, and this result shows a Vpp-only formula specifically would
  have been the wrong target regardless.
- Anything at Lambda values, or `(k, IC)` combinations, other than
  k=0.3/k=0.5's main case tested throughout `FINDING_P119`–`P130`.
- Anything about MULTING itself (Gate 1). Any `k[h/Mpc]`.
