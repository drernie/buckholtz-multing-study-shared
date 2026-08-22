# FINDING P102 — **RECOVERS-P100, with room to spare.** The coarse endpoint check really was masking roots — fixed, and the measurable range now extends further than any prior file in the arc

**Status:** built, run, both controls passed, verdict against pre-registered
outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P102_interior_scanning_bracket_search.py`

> `FINDING_P101` diagnosed, but did not fix, a limitation in every root
> search this arc has used since `FINDING_P94`: checking only the two
> bracket *endpoints* for a sign change before running `brentq`, never
> scanning the interior. `P101`'s own widened bracket lost 3 previously
> -measurable `Λ` values to exactly this blind spot. This file builds the
> fix and applies it.

---

## The fix

`interior_scan_roots(lam_cc, a_lo, a_hi, n)` replaces the 2-point check
with `n` log-spaced evaluations of `resid(a_today)` across the bracket,
finds every adjacent-point sign change among the *finite* evaluations, and
hands each detected sub-interval to `brentq` independently — can find
**zero, one, or several** roots per `Λ`, where the old check could find at
most one (and, as `P101` showed, sometimes missed the one that was there).

## Controls, both passed before trusting a different answer than `P101`'s

| Control | Check | Result |
|---|---|---|
| 1 | `n=2` (degenerate, endpoints only) reproduces `P101`'s own "not measured" for a lost `Λ` | **PASSES** — same algorithm, same answer at the degenerate limit |
| 2 | Fine resolution still reproduces the long-standing regression targets (`Λ=2.084e-16`, `3.000e-12`) | **PASSES** — `6.26e-05` and `4.73e-05` relative, both inside `5×10⁻³` |

## Stage A — deep dive on `P101`'s 3 "lost" `Λ` values, 3000 points (~430/decade)

| `Λ` | valid points | roots found | root `a_today` | `g(Λ)` |
|---|---|---|---|---|
| `1.194×10⁻¹⁶` | `2347/3000` | **1** | `263117.83` | `+2.3975×10⁻⁶` |
| `2.154×10⁻¹⁶` | `2513/3000` | **1** | `216115.32` | `+2.7404×10⁻⁶` |
| `3.888×10⁻¹⁶` | `2748/3000` | **1** | `177505.46` | `+3.1902×10⁻⁶` |

**HIDDEN-ROOT-CONFIRMED for 3/3.** `P101`'s masking hypothesis was correct.
And notably: these recovered values match `FINDING_P100`'s own *original*
numbers for the same `Λ` almost exactly (`P100` had `+2.397009e-06`,
`+2.740912e-06`, `+3.189133e-06` at these same three points) — the roots
were never lost to the physics. `P100`'s narrower `[300, 3×10⁶]` bracket
happened, by luck of placement, to have these roots between its two
endpoints; `P101`'s wider `[10.46, 10⁸]` bracket did not, purely because a
wider span made the endpoint-only check more likely to land same-signed.

## Stage B — full 40-point grid, 300 interior points/`Λ` (~43/decade)

| | measurable | low end | high end |
|---|---|---|---|
| `P100` (old bracket, endpoint-only) | `19/40` | `1.194×10⁻¹⁶` | `4.924×10⁻¹²` |
| `P101` (new bracket, endpoint-only) | `16/40` | `7.017×10⁻¹⁶` | `4.924×10⁻¹²` |
| **this file** (new bracket, interior scan) | **`23/40`** | **`1.125×10⁻¹⁷`** | `4.924×10⁻¹²` |

**High end unchanged** across all three — confirms `P101`'s own conclusion
that the ceiling was never a bracket-check artifact. **Low end extends
`~10.6×` past even `P100`'s best result** — `Λ=1.1253×10⁻¹⁷` resolves here
and never resolved in *any* prior file in this arc, `P100` included.

**No degenerate (multi-root) `Λ` values found** — every measurable point
has exactly one `a_today` root, not several. **Zero sign changes of
`g(Λ)`** across all 23 measurable points — the two-epoch shape match
still does not exist anywhere in this now much more thoroughly searched
domain.

---

## Verdict — **RECOVERS-P100, and extends past it**

The coarse two-endpoint bracket check, present in every file since `P94`,
really was masking real roots — confirmed directly, not inferred. Fixing
it recovers `P100`'s own count with `4` points to spare (`23` vs `19`) and
extends the measurable `Λ` floor an order of magnitude further than any
prior step in the `P93`–`P102` arc has reached. **Still zero sign changes
of `g(Λ)`.** The two-epoch `H(a)` shape match this whole arc has been
looking for since `FINDING_P99` still does not exist anywhere the search
can now see — but the search itself is, for the first time, no longer the
limiting factor on the low-`Λ` side.

No `k[h/Mpc]` number is quoted.

### Not established

- That `3000`/`300`-point resolution is fine enough to catch *every*
  possible hidden root — a sufficiently pathological `resid(a_today)`
  could still hide a feature narrower than the scan spacing. Not ruled
  out, not assumed away.
- Whether the SAME two-endpoint limitation affects the joint `Ω_m`/`Λ` or
  `Ω_m`/age searches in `FINDING_P96`–`P98` (their own `NO-ROOT` verdicts
  used the identical bracket-check pattern this file just showed can miss
  real roots). Not tested here — `FINDING_P95`'s own `NO-ROOT` is exempt,
  since it is a *structural* proof (`Ω_φ≥0` identically), not a numerical
  bracket search, but `P96`–`P98` are not. Worth a note for anyone
  revisiting those findings; out of scope for this file, which was built
  specifically for `P100`/`P101`'s `a_today` lever.
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file.
