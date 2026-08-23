# FINDING P126 — Checking `FINDING_P125`'s resolution at k=0.5: **`AFFINE-FACTORIZATION-CONFIRMED`** (a skeptic caught an overclaim before commit — the real result is sharper than "the exponent matches")

**Status:** built, ran, its own draft verdict called a near-exact match
"independent confirmation" — a context-asymmetric skeptic review caught
this as an overclaim before commit, identified the real mechanism, the
file was rebuilt around a direct test of that mechanism, rerun, corrected.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P126_k05_analytic_resolution_check.py`

> User-directed: "проверь на k=0.5" (check it at k=0.5) — the exact
> follow-up `FINDING_P125` itself registered as a falsifiable prediction
> but did not test: does k=0.5's own `contrast_coupled(N)` show the same
> tight, self-consistent `q_local` plateau (`≈0.466`) `FINDING_P125` found
> at `k=0.3`?

---

## The draft result — too clean to trust at face value

Applying `FINDING_P125`'s own self-consistent optimal-`c_inf` construction
to `k=0.5`'s data gave a plateau matching `k=0.3`'s to **6 decimal
places** (`0.465959` vs `0.465960`) — not just the asymptotic value, but
at **every one of 12 probe points** across the whole tested range. This
is exactly the kind of "suspiciously perfect" result `skeptic-triggers.md`
Trigger 4 exists for.

## Skeptic review — the real mechanism

Sent the claim, method, and data (no reasoning chain) to an independent
skeptic. Verdict: **`WEAKENED`** — the match is real ODE behavior, not an
optimizer artifact, but the physical content is narrower than claimed.
The key insight: `q_local(N) := -N·d/dN[ln|val(N)|]` is **invariant under
any affine transformation** `x ↦ A·x + B` of its input (subtracting
`c_inf` kills the offset, the log-derivative kills the scale). If
`contrast_k05(N)` and `contrast_k03(N)` are exactly affinely related —
plausible, since these are **linear** perturbation variables whose only
`k`-dependence, once `k²/a²→0`, is an overall amplitude — the `q_local`
match would be a **near-mathematical consequence** of that relation, not
independent physics confirmation.

## The direct test

Computed `A_hat(N) := (contrast_k05(N)-c_inf_k05) / (contrast_k03(N)-c_inf_k03)`
at `FINDING_P120`'s own regression-anchored 14 `N`-points (reusing
already-committed values, not re-derived):

| N | A_hat |
|---|---|
| 926.3 | 6679.02 |
| 13,141 | 6678.93 |
| 109,670 | 6679.02 |
| 915,300 | 6679.24 |

**Confirmed constant**: mean `6678.998`, relative spread `0.0063%` across
nearly 3 decades of `N`. `contrast_k05(N) = 6679.0·contrast_k03(N) + \text{const}`
— an exact affine relationship, holding across the entire tested domain.

---

## Verdict — **`AFFINE-FACTORIZATION-CONFIRMED, NOT INDEPENDENT-MATCH`**

The real, defensible result is sharper and more precise than "the
exponents happen to match": the two ODE solutions' late-time **shape** is
`k`-independent up to a `k`-dependent overall rescaling. This is
consistent with, and a *stronger* statement than, the `k²/a²→0` mechanism
`FINDING_P125` proposed — that argument predicted a common **exponent**;
this shows a common **full shape function**.

The `q_local` match is not independent evidence beyond the affine
relationship — it *follows* from it. But the deviation-energy conclusion
(`DIVERGES`, `q≈0.466<1/2`) still stands at `k=0.5`: it transfers directly
from `k=0.3` via this same affine relationship, which is itself the real
result here.

### Not established

- Why the affine constant is specifically `A≈6679` — this file confirms
  the factorization exists and measures `A`, it does not derive it from
  first principles (would require solving the linear perturbation
  equations' own `k`-dependent eigenvalue/amplitude).
- A rigorous proof that either plateau continues to `N→∞` — both are
  finite-domain measurements.
- Why the specific value is `≈0.466` rather than exactly `1/2` or some
  other value — `FINDING_P125` already flagged this as unresolved from
  first principles; this file does not resolve it either.
- Anything at `Λ` values, or `(k, IC)` combinations, other than `k=0.3`
  and `k=0.5`.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
