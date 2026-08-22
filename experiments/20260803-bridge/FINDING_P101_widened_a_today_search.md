# FINDING P101 — **RANGE-UNCHANGED (in fact, shrunk).** `P100`'s own hypothesis about the next lever is refuted

**Status:** built, run (twice — a design bug caught and fixed before trusting
the first result), regression control passed, verdict against pre-registered
outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P101_widened_a_today_search.py`

> `FINDING_P100` hardened the Lambda scan and named — but did not pull — a
> different lever: is the inner root's `a_today` search bracket
> (`[3×10², 3×10⁶]`, inherited unchanged from `FINDING_P94`) itself the
> reason the measurable `Λ` range stops where it does? This file pulls that
> lever directly.

---

## A design bug found and fixed before trusting anything

The first attempt took `P100`'s own wording literally — `a_today` floor set
to `a0·(1+10⁻⁴)`, right next to the trajectory's start
(`a0 = A3_INIT^(1/3) ≈ 2.6134`). **Every single Λ value came back "not
measured."**

Read before trusted, not reported as a result: `shape(a_today)` is not
evaluated at `a_today` alone — it needs `H` at `a_today/(1+z)` too, for the
largest `z` this file uses. With `a_today` sitting right at `a0`,
`a_today/(1+0.5) ≈ 1.74` — **below `a0`**, a point the trajectory never
reaches. `resid()` at that endpoint is `NaN`, so the bracket is rejected
before `brentq` ever runs. The all-`NaN` run was a bug in this file's own
bracket placement, not a physics result.

**Fixed floor:** `a_today ≥ a0·(1 + max(z_fit1, z_fit2, z_check…))·(1+10⁻³)
= a0·4.004 ≈ 10.46` — the smallest `a_today` for which `a_today/(1+z)` stays
reachable for *every* `z` this file ever evaluates, including the
out-of-sample `z_check = (1.0, 3.0)` reached only if a root is found. Still
`~29×` lower than the old `300` floor, now internally consistent rather than
merely close to `a0` in name.

## Step 1 — regression control (refactor only, old bounds)

| `Λ` | `P100` published `g` | this file's `g` | relative diff |
|---|---|---|---|
| `2.084e-16` | `2.905e-06` | `2.904817e-06` | `6.284e-05` |
| `3.000e-12` | `1.616e-05` | `1.615814e-05` | `1.151e-04` |

Both inside the `5×10⁻³` tolerance. The refactor into explicit-bound
functions changed nothing.

## Step 2 — same 40-point Λ grid as `P100`, corrected widened bracket

**New bracket `[10.46, 10⁸]`** — `29×` lower floor, `33×` higher ceiling
than `P100`'s `[300, 3×10⁶]`.

| | `P100` (old bracket) | this file (new bracket) |
|---|---|---|
| measurable count | `19/40` | `16/40` |
| measurable Λ range | `[1.194×10⁻¹⁶, 4.924×10⁻¹²]` | `[7.017×10⁻¹⁶, 4.924×10⁻¹²]` |
| sign changes | `0` | `0` |

**High end: unchanged**, to 4 significant figures (`4.9239×10⁻¹²` vs
`4.9240×10⁻¹²`) — the ceiling was never the constraint on that side, at either
bracket width.

**Low end: the measurable range did not extend — it *shrank*.** Three grid
points that resolved under `P100`'s narrower `[300, 3×10⁶]` bracket
(`Λ = 1.194×10⁻¹⁶, 2.154×10⁻¹⁶, 3.888×10⁻¹⁶`) come back `not measured` under
the wider `[10.46, 10⁸]` bracket. In the region where both runs *do*
resolve, the numbers agree closely (e.g. `Λ=7.017×10⁻¹⁶`: `P100`'s
`g=+3.880×10⁻⁶` vs this file's `+3.883×10⁻⁶`) — so this is not a different
physical answer, it is a difference in what the search can even see.

### Why three points were lost, not gained — read before writing the verdict

The bracket check used throughout `P94`–`P101` is coarse: `brentq` only
runs if `resid(a_lo)` and `resid(a_hi)` have opposite signs at the two
*endpoints* — the interior is never scanned for a hidden sign change. A
`29×`–`33×` wider bracket spans far more of `resid(a_today)`'s structure
between those endpoints. If `resid` is non-monotonic (plausible — every
`g(Λ)` scan in this whole arc has been), a wider span makes it *more*
likely, not less, that the two endpoints land on the *same* sign even when
a root exists somewhere between them — masking it rather than revealing it.
This is a **limitation of the two-endpoint bracket check itself**, present
in every file from `P94` onward, newly exposed here because this is the
first file to push the bracket width far enough to trigger it. Not fixed
in this file (a proper fix — scanning several interior points before
committing to `brentq`, or a coarse grid pre-scan — is a different, smaller
lever than the one this file was built to test) — named, not pulled.

## Verdict — **RANGE-UNCHANGED (high end), SHRUNK (low end); zero sign changes either way**

`P100`'s own named hypothesis — that the `a_today` search bracket was the
binding constraint on the measurable `Λ` range — is **refuted** by this
test, in the strongest form available: widening the bracket `29×`–`33×`
did not recover any of the region `P100` couldn't see, and lost ground on
the low end instead (for a diagnosed, non-physical reason — the coarse
bracket check, not the dynamics). The true wall on the high-`Λ` side is
confirmed to be something other than `a_today` bracket width; on the
low-`Λ` side, this file cannot cleanly separate "genuinely no root" from
"the bracket check is too coarse to see one" — both remain open.

Zero sign changes in the measurable region either way. No `k[h/Mpc]`
number is quoted.

### Not established

- Whether a genuine root exists in the `Λ` region the coarse two-endpoint
  bracket check now fails to resolve (`1.194×10⁻¹⁶`–`7.017×10⁻¹⁶`) — an
  interior-scanning bracket search, not built here, would be needed to
  rule this in or out.
- Whether `A_TODAY_HI_NEW = 10⁸` is the true maximum reachable `a(T_END)`
  for any given `Λ` — a round ceiling tied to the integration's own
  time-axis scale, not a computed one.
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file.
