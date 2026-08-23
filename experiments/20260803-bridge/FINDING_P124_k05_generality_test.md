# FINDING P124 — Generality test at k=0.5: **`SAME-QUALITATIVE-PATTERN-CONFIRMED`** (a verdict-logic bug flipped the first result to its opposite, caught before commit)

**Status:** built, ran, its own verdict computation returned the wrong
answer on the first pass — a `numpy.bool_` vs Python `bool` identity-check
pitfall, not a physics or methodology error — caught by re-deriving the
verdict by hand against the printed component values, fixed, rerun.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P124_k05_generality_test.py`

> User-directed ("го все по очереди"), the second and larger of the two
> follow-ups named across `FINDING_P122`/`P123`: is the k=0.3 sub-arc's
> whole pattern — a float64-overflow masquerading as an "unmeasurable
> pole" (`FINDING_P110`), resolved by `ln(a)`-state tracking
> (`FINDING_P119`), tail law approximately power-law with `q≈0.5`
> (`FINDING_P120`), log-correction measurably better (`FINDING_P122`) —
> generic to this ODE system, or specific to that one `(k, IC)` point?
> `FINDING_P110` found a second, independently-flagged "unmeasurable
> pole" at `k=0.5`, `φ̄̇(1)×0.1`, never investigated further once
> `FINDING_P111` onward focused entirely on `k=0.3`.

---

## Reconnaissance first (Compute First discipline)

A quick `T_END=1e10` probe, before building anything elaborate, showed:
the reference branch has zero sign changes (well-behaved,
`[0.065, 0.085]`); the coupled branch has one sign change (a large early
transient — peak `~+3.4×10⁸` near decade 2, crossing zero between decades
50–100, then a smooth, monotonically-more-negative tail); and
`energy_ratio_lna` — the actual `G_E` computation — returns a **finite**
value (`~4.5×10⁸`–`~8.2×10⁸`, vs `k=0.3`'s own `~1.25×10⁶`), still visibly
`x_lo`-dependent at this modest reach. This strongly suggested
`FINDING_P110`'s "unmeasurable pole" was itself a symptom of the same
float64-overflow-in-raw-`a` pathology already diagnosed and fixed for
`k=0.3` — not a genuine physical divergence.

## Design

Reused `FINDING_P119`'s `ln(a)`-state system, `FINDING_P120`'s
`contrast_at_N`/`convergence_check`, and `FINDING_P121`'s
`fit_model_params` verbatim — no new mechanics, only a new `(k, IC)`
applied to already-validated tooling. Solved to `FINDING_P119`'s own
established `T_END=1e13` ceiling.

## A caught bug — not physics, a boolean-identity pitfall

The first run's own verdict printed `PATTERN DOES NOT FULLY MATCH k=0.3`
— despite every individually-printed component (`main_shrinking=True`,
`reference degenerate=True`, `power_law_log beats power_law=True`,
`q` within `0.1` of `0.5`) reading as a match. Re-derived the combined
condition by hand against those exact printed values before trusting the
script — it came out `True`, contradicting the script's own output.

**Root cause**: `pll_wins = ho_err_pll < ho_err_pow` compares two
`numpy.float64` values, producing a `numpy.bool_`. The verdict check used
`pll_wins is True` — and `numpy.bool_(True) is True` is `False` (an
identity check across different object types), even though the *value*
is true. Fixed by replacing the identity check with `bool(...)` and
direct truthiness. Confirmed the fix with a standalone reproduction
before rerunning the full (~5 minute) solve.

## Results, corrected

| | k=0.3 (`FINDING_P120`/`P122`) | k=0.5 (this file) |
|---|---|---|
| reference branch | exactly constant | exactly constant (`0.085214`) |
| coupled branch converges | via power-law tail | via power-law tail |
| `q` (power_law fit) | `0.502868`–`0.5024` | `0.502868` |
| `power_law_log` beats `power_law` (held-out) | yes (`FINDING_P121`/`P122`) | yes (`0.0069%` vs `0.0190%`) |

**The `q` match to 6 decimal places is striking, and has a plausible
structural explanation, not asserted as coincidence:** the ODE's
`k²/a²` term (in `drA_hat_d`, per `FINDING_P118`'s own derivation) decays
to zero at late times for *any* fixed `k`. If the late-time asymptotic
decay rate is governed by the `k`-independent remainder of the equations
once this term has decayed away, `q` could genuinely be a **universal**
exponent for this whole `(IDM-completion, k<1, extreme-φ̄̇(1))` family —
while the amplitude/normalization (`c_inf`, `amp` — which differ by
`~1000×` between `k=0.3` and `k=0.5`) depends on the full history
including the earlier `k`-dependent transient, and so is *not* universal.
Not proven here — a mechanistic hypothesis consistent with the data,
worth stating explicitly rather than passing over as an odd coincidence.

---

## Verdict — **`SAME-QUALITATIVE-PATTERN-CONFIRMED`**

`contrast_coupled(N)` approaches a finite constant via an apparent
power-law tail with `q` close to `1/2`; the reference branch is exactly
constant; a log-corrected model beats the plain power law on held-out
prediction — at **both** independently-chosen `(k, IC)` points. The
`k=0.3` sub-arc's own pattern is not an isolated artifact of that one
point.

### Not established

- That `FINDING_P110`'s own "unmeasurable pole" verdict was *wrong* for
  the old (pre-`ln(a)`) system — it was correct for that system; this
  file shows the pole resolves under a different, later-built system,
  which is a different claim.
- A full forward-extrapolation/hold-out characterization for `k=0.5` —
  this file runs `FINDING_P120`/`P121`'s fit protocol only, not
  `FINDING_P122`/`P123`'s own genuine-extrapolation refinement.
- Whether this pattern holds at `k=0.3`'s *other* pole point
  (`φ̄̇(1)×0.5`, per `FINDING_P110`'s own table) or any other `(k, IC)`.
- The mechanistic hypothesis above (`k`-independent asymptotic exponent)
  — plausible and consistent with the data, not independently derived or
  tested against a third `k` value.
- Anything at `Λ` values other than `1e-15`.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
