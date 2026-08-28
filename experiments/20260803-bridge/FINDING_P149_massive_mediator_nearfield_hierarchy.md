# FINDING P149 — Q4: the near-field ratio survives μ~H₀/c at cluster
# scale; deviation grows only near the Hubble radius, and even there
# stays bounded, not runaway

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
**Verdict:** `MASSIVE-MEDIATOR-NEAR-FIELD-COMPATIBLE`
**Origin:** `P148`'s Q4 — the first, cheapest step of the user's
internal-consistency → observable-mapping → external-constraint order,
run before any fifth-force experimental mapping (`P150`).
**Script:** `P149_massive_mediator_nearfield_hierarchy.py` (2 positive
controls + 1 decisive numerical table, ruff clean, does not touch the
881-test suite)

---

## 1. What's being tested

`P11` proposed a fixed-mass Yukawa mediator (`μ~H₀/c`) as a candidate
mechanism that could give `two_field_action_closure.py`'s exact-massless
cosmological double-layer zero a nonzero cosmological escape, while
staying negligibly different from massless at cluster scale — but named
two unresolved items: whether the near-field ladder (`β_d=2, β_q=√6`)
actually survives a nonzero `μ` at cluster scale, and whether `μ~H₀/c`
gives an observable magnitude. This file resolves the first.

## 2. Method — reuse the already-verified kernel invariant, don't
## re-derive from scratch

`P1` (`two_field_action_closure.py`) already established, for a general
exchange kernel `K(s)`, that `β_q/β_d` is fixed entirely by the kernel
invariant `Λ(s) = K'''(s)K'(s)/K''(s)²` — and that **only this ratio is
physical**; individual `β_d, β_q` values depend on the lever-arm
convention (`d=r_A`), a modelling choice, not physics. For massless
`K=1/s`, `Λ=3/2` exactly at every `s`. This file evaluates `Λ(s)` for
Yukawa `K=exp(−μs)/s` at realistic `μ=H₀/c` and separations `s` from
cluster to super-Hubble scale — reusing the established machinery rather
than re-deriving the full lever-arm ladder (a first draft attempted a
from-scratch lever-arm re-derivation and hit an unrelated
separation-vs-lever-arm variable-naming bug; discarded in favor of this
simpler, more directly verifiable route once the redundancy with `Λ(s)`
was recognized).

**Two positive controls, both required to pass first:**
1. `Λ(μ=0) = 3/2` exactly (massless limit).
2. Small-`(μs)` expansion `Λ = 3/2 − (3/4)(μs)² + O((μs)⁴)` matches
   `P1`/`P11`'s own hand-derived expansion, coefficient by coefficient.

## 3. Result

| `r` [Mpc] | `μr` | `Λ(μr)` | deviation from `3/2` |
|---:|---:|---:|---:|
| 0.5 | `1.2×10⁻⁴` | 1.4999999898 | `6.8×10⁻⁷`% |
| 1.0 | `2.3×10⁻⁴` | 1.4999999591 | `2.7×10⁻⁶`% |
| 3.0 | `7.0×10⁻⁴` | 1.4999996324 | `2.5×10⁻⁵`% |
| 10.0 | `2.3×10⁻³` | 1.4999959239 | `2.7×10⁻⁴`% |
| 100.0 | `2.3×10⁻²` | 1.4996036651 | `2.6×10⁻²`% |
| 1000.0 | `0.23` | 1.4700381332 | `2.0`% |
| 4283.0 (`≈c/H₀`) | `1.00` | 1.2799930621 | `14.7`% |
| 8566.0 | `2.00` | 1.1399941296 | `24.0`% |
| 42830.0 | `10.0` | 1.0095398363 | `32.7`% |

**At cluster scale (`r~0.5–10` Mpc — where `β_d=2, β_q=√6` was actually
derived and where it would need to be measured), the deviation is
`10⁻⁷`–`10⁻⁴`%: utterly negligible.** It only becomes noticeable
(`~2%`) around `r~1000` Mpc and reaches `~15%` at the Hubble radius
itself. Beyond that, the deviation does **not** run away — `Λ→1` as
`μs→∞` (checked analytically: `Λ(s)=(μs+1)(μ³s³+3μ²s²+6μs+6)/(μ²s²+2μs+2)²
→ (μs)⁴/(μs)⁴ = 1`), so the deviation asymptotes toward a bounded
`~33%`, not divergence.

## 4. Verdict

**`MASSIVE-MEDIATOR-NEAR-FIELD-COMPATIBLE`.** `P11`'s `μ~H₀/c` candidate
does not break the near-field ladder it needs to preserve — the
deviation from the exact-massless ratio is negligible by many orders of
magnitude at the scale where `β_d=2, β_q=√6` was derived, and grows only
near/beyond the Hubble radius, where a cosmologically-relevant escape
from the exact double-layer zero is exactly what `P11`'s own separate
calculation (breaking the double layer for any finite `μ`) already
requires. The two P11-named unresolved items now stand as: (a)
**resolved** — near-field ladder survives; (b) **still open** — whether
`μ~H₀/c` specifically gives an *observable* magnitude (not attempted
here; would need the actual double-layer-breaking amplitude from `P11`'s
own calculation combined with a real observational forecast).

## 5. What this file does NOT establish

1. **Not a confirmation that a cosmological signal actually exists at
   observable magnitude.** This checks internal consistency (does the
   local structure survive) — `P11`'s (b) is untouched.
2. **`μ=H₀/c` is still a specific choice, not derived from anything in
   this project's own construction.** The test shows this choice is
   *compatible* with the near-field ladder — it does not show this
   choice is *required* or *natural* beyond the qualitative
   "cosmologically relevant scale" motivation `P11` already gave.
3. **Does not touch Q3a/Q3b** (`P150`/`P151`) — the fifth-force
   experimental-mapping question is untouched by this purely internal
   consistency check, per the user's own explicit ordering.
4. Nothing about MULTING itself (Gate 1) — entirely this project's own
   reconstruction cluster.
