# FINDING P108 — **`SIX-BRANCH-CONVERGES` at every tested `k`.** The complete picture, no gaps left

**Status:** built, run, regression control exact, verdict against
pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P108_wide_tend_reach_limited_branches.py`

> `FINDING_P107` reached `CONVERGES-CONFIRMED` for 4 of 6 `Λ` branches;
> the two smallest `Λ` couldn't be pushed far enough past their own
> crossing within `T_END=1e8` to test. `P107`'s own overflow-risk caveat
> was specific to the *large*-`Λ` branches — this file tests whether it's
> safe to widen `T_END` for the small-`Λ` ones instead, and completes the
> picture.

---

## Reconnaissance first

Probed `a(T_END)` for both reach-limited branches at `T_END ∈ (1e8, 3e8,
1e9, 3e9, 1e10)` before choosing anything. Growth is exponential once
`Λ` dominates (de Sitter), so small `T_END` increases overshoot fast:

| `Λ` | `T_END=1e8` | `T_END=3e8` | `T_END=1e9` |
|---|---|---|---|
| `2e-17` | ratio `2.3` | ratio `31` | ratio `2.6×10⁵` |
| `1e-16` | ratio `11` | ratio `3719` | ratio `2.3×10¹²` |

`Λ=2e-17` is the binding constraint (slowest growth). Narrowed
empirically to `T_END=4.5e8` — the smallest value that safely clears
`x=100` for the harder branch (ratio `~213`, comfortable margin), rather
than a much larger value that would overshoot without adding anything.

## Regression control — exact

Re-evaluated `G_growth` at the exact `(Λ, k, x)` points `FINDING_P107`
already published, now at `T_END=4.5e8` instead of `1e8`:

| point | `P107` | this file | rel diff |
|---|---|---|---|
| `Λ=2e-17, k=1, x=2` | `1.046447` | `1.046447` | `1.0×10⁻⁷` |
| `Λ=1e-16, k=1, x=2` | `1.046415` | `1.046415` | `9.1×10⁻⁸` |
| `Λ=1e-16, k=1, x=5` | `1.050206` | `1.050206` | `4.5×10⁻⁷` |
| `Λ=1e-16, k=1, x=10` | `1.050877` | `1.050877` | `1.2×10⁻⁸` |

Essentially exact — widening `T_END` doesn't change the trajectory up to
where it was already computed, exactly as expected (integrating further
doesn't rewrite the earlier path).

## Results — both branches converge cleanly at every `k`

Final-step changes (`x=50→100`) between `0.0001%` and `0.0014%` — far
inside `P76`'s own `2%` threshold, for both branches, all three `k`.

## The complete 6-branch picture

| `k` | full 6-branch `G_∞` range | relative spread |
|---|---|---|
| `0.1` | `[0.996876, 1.004086]` | `0.72%` |
| `1.0` | `[1.050046, 1.051153]` | `0.11%` |
| `10.0` | `[1.095357, 1.095798]` | `0.04%` |

---

## Verdict — **`SIX-BRANCH-CONVERGES` at every tested `k`**

Both reach-limited branches individually T-converge on `G_growth`, and
joining them to `FINDING_P107`'s own four converged values gives a
**complete, gap-free 6-branch picture**: every branch tested in this arc
supports M1 (scale-degeneracy-only), at every `k` tested, with spreads
under `1%` everywhere. This is the strongest and most complete form of
this result the arc has produced — no untested `Λ` values remain in the
range this arc has explored.

### Not established

- That `T_END` could not be pushed even further for these two branches —
  `4.5e8` was chosen as the smallest value clearing `x=100`, not tested
  beyond that.
- Anything about the four already-converged branches from
  `FINDING_P107` — not re-run, re-quoted only.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
