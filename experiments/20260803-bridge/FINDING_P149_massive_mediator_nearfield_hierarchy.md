# FINDING P149 — Q4: the near-field RATIO-INVARIANT survives μ~H₀/c at
# cluster scale; deviation grows only near the Hubble radius, and even
# there stays bounded, not runaway

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
**Verdict:** `MASSIVE-MEDIATOR-NEAR-FIELD-RATIO-INVARIANT-COMPATIBLE` —
corrected from an earlier draft's `...-NEAR-FIELD-COMPATIBLE`, per
independent skeptic review (§0 below): "the ladder survives" overclaimed
what was actually tested.
**Origin:** `P148`'s Q4 — the first, cheapest step of the user's
internal-consistency → observable-mapping → external-constraint order,
run before any fifth-force experimental mapping (`P150`).
**Script:** `P149_massive_mediator_nearfield_hierarchy.py` (3 positive
controls + 1 decisive numerical table, ruff clean, does not touch the
881-test suite)

---

## 0. Correction (same day, independent skeptic review) — read this first

Two real issues, both fixed in place:

1. **Math error, inherited from prior work.** The originally-quoted
   small-`(μs)` expansion `Λ = 3/2 − (3/4)(μs)² + O((μs)⁴)` is
   **incomplete** — it silently drops a real `+(μs)³` term. The skeptic
   independently rederived the full expansion by hand
   (`Λ = 3/2 − (3/4)x² + x³ − (5/8)x⁴ + O(x⁵)`, `x=μs`) and traced the
   omission to `two_field_action_closure.py`'s own truncated `sp.series`
   call, which cuts off before the cubic term appears — this file's first
   draft inherited the same incomplete quote without independently
   checking it. Independently re-verified here (not just accepted): a
   fresh symbolic expansion confirms the corrected series exactly.
   **Numerical impact: none** — at cluster scale `x~10⁻⁴`, the cubic term
   (`~10⁻¹²`) is utterly dominated by the quadratic term (`~10⁻⁸`); the
   decisive numerical table (§3) was already computed from the exact
   closed form, not the truncated series, so it required no correction.
2. **Verdict-label overreach.** "The near-field ladder survives" claimed
   more than what was tested. `P1`'s own finding is that *only the ratio*
   `β_q/β_d` (equivalently `Λ(s)`) is physical — individual tier
   coefficients depend on the lever-arm convention. For any `μ>0`, the
   individual power-law tiers `F_km~1/r³, F_kk~1/r⁴` are **not** preserved
   unmodified — each acquires its own `exp(−μr)×polynomial(μr)`
   deformation. What survives is specifically the convention-independent
   ratio invariant, not "the ladder" in the sense of the pure power laws
   themselves. Verdict renamed throughout to make this explicit.

**A genuine strengthening, not just a repair:** the skeptic's own
proposed stress-test — could `β_d(μ)` and `β_q(μ)` individually drift
substantially while *cancelling* in the ratio, making the ratio-only
check too weak? — was checked directly (§3a below) and resolved in the
strongest possible direction: the ratio `Λ` is actually the **most**
sensitive of the three natural quantities at leading order in `μs`
(`O(x²)` for `Λ`, vs. `O(x³)` for `β_d` alone and `O(x⁴)` for `β_q²`
alone). The ratio-only reduction is not a looser test hiding drift — it
is the strictest one available, confirmed rather than merely assumed.

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

**Three positive controls, all required to pass first:**
1. `Λ(μ=0) = 3/2` exactly (massless limit).
2. Small-`(μs)` expansion, corrected per §0:
   `Λ = 3/2 − (3/4)(μs)² + (μs)³ − (5/8)(μs)⁴ + O((μs)⁵)`, all four
   nonzero coefficients checked exact, not just the first two.
3. (Added post-correction, §3a) — the ratio-only reduction is checked
   against the individual tier coefficients' own drift, to directly test
   whether it could be hiding cancelling deviations.

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

## 3a. Does the ratio-only check hide individually-drifting tiers?

Per §0's strengthening: computed each tier's own Yukawa/massless ratio
directly, small-`x` expansion (`x=μs`):

```
β_d(μ)/β_d(0)   = 1 − x³/6 + x⁴/8 − x⁵/20 + O(x⁶)     leading drift O(x³)
β_q²(μ)/β_q²(0) = 1 − x⁴/24 + x⁵/30 + O(x⁶)            leading drift O(x⁴)
Λ(μ)/Λ(0)       = 1 − x²/2 + O(x³)                     leading drift O(x²)
```

`Λ`'s own drift (`O(x²)`) is **larger**, not smaller, than either
individual tier's drift (`O(x³)`, `O(x⁴)`) at leading order — the
opposite of the "ratio hides cancelling drift" concern the check was
designed to probe. Structurally, this is forced: the tier expansion gives
`F_mm∝K', F_km∝K'', F_kk∝K'''`, and `Λ=K'''K'/K''²` is the *unique*
dimensionless combination invariant under the lever-arm rescaling
`p→λp` that `P1` identified — there is no other convention-independent
quantity available to check instead. The ratio-only reduction is
therefore not a simplification of convenience; it is the only physically
meaningful quantity, and it is also the strictest one.

## 4. Verdict

**`MASSIVE-MEDIATOR-NEAR-FIELD-RATIO-INVARIANT-COMPATIBLE`** (label
corrected, §0). `P11`'s `μ~H₀/c` candidate does not break the one
convention-independent quantity this construction's near-field content
actually reduces to — the deviation from the exact-massless ratio is
negligible by many orders of magnitude at the scale where `β_d=2,
β_q=√6` was derived, and grows only near/beyond the Hubble radius, where
a cosmologically-relevant escape from the exact double-layer zero is
exactly what `P11`'s own separate calculation (breaking the double layer
for any finite `μ`) already requires. The two P11-named unresolved items
now stand as: (a) **resolved, precisely scoped** — the ratio-invariant
survives at cluster scale; the individual power-law tiers are formally
deformed for any `μ>0` but by even less than the ratio itself; (b)
**still open** — whether `μ~H₀/c` specifically gives an *observable*
magnitude (not attempted here; would need the actual double-layer-
breaking amplitude from `P11`'s own calculation combined with a real
observational forecast).

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
