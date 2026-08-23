# FINDING P122 — True forward extrapolation: **`Q-STABLE, MODEL-AMBIGUOUS-ON-DEVIATION-ENERGY, G_E-UNAFFECTED`**

**Status:** built to a user-proposed design responding to a critique of
`FINDING_P121`, ran, and went through two rounds of self-correction before
commit — a mathematical error in the decisive threshold's own meaning
(caught with a tool before the first write-up), and a numerical-precision
bug in the divergence check itself (caught by an impossible negative value
for a squared integrand, fixed with a closed-form criterion instead).
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P122_forward_extrapolation_test.py`

> User-proposed design, correctly diagnosing a gap in `FINDING_P121`:
> P121's "extension" grid sat entirely *inside* the power-law fit's own
> point-level calibration domain — a strong held-out **interpolation**
> test, not a genuine **extrapolation** test. Proposed fix: fit the tail
> law on an early part of the range only, hold out a late part no fit ever
> sees, check whether the fitted exponent `q` is stable across growing fit
> windows, and test against competing forms (exponential, power-law-with-
> log-correction) — with the decisive question being whether `q` sits
> reliably above or below `q=1/2`.

---

## Correction 1 — the q=1/2 threshold does not gate G_E, verified with a tool

The user's proposed criterion — `|δ|~N^-q` ⟹ `∫δ²dN` converges iff `q>1/2`
— is correct for a quantity that itself decays to zero. `contrast_coupled(N)`
does **not**: it approaches a finite **nonzero** constant `c_inf`
(`FINDING_P120`'s own result). For this system, `∫contrast(N)²dN` diverges
**linearly** in `N` for *both* branches (since `contrast→c_inf≠0`), and
`G_E := E_coupled/E_reference` converges because it is a **ratio** of two
linearly-diverging integrals with the same leading-order structure — not
because either integral converges on its own.

Checked directly with `scipy.integrate.quad`, not asserted: `G_E(N)` was
computed at `N` up to `1e12` for `q ∈ {0.1, 0.2, 0.502, 0.9}` — spanning
*both* sides of `1/2` — and it converges to the **same** finite target
`(c_c/c_r)²` in every case. `q` only changes the *rate*: `q=0.1` needs a
vastly larger `N` to get close; `q=0.9` gets there almost immediately.
**`G_E`'s own finiteness does not hinge on `q` crossing `1/2`.**

The `q=1/2` threshold *does* gate a real, different, well-posed quantity:
the **deviation/excess energy** `∫(contrast(N)-c_inf)²dN = ∫A²N^-2q dN`,
which converges iff `q>1/2` exactly as classically stated. This file's `q`
results are reported against *this* corrected target.

## Design, exactly as proposed

Fixed the fit window's lower edge at the domain start; grew its upper edge
(`N_cut`) through `{50000, 100000, 150000, 200000, 250000, 300000}`
decades, all held comfortably below a fixed hold-out region
(`{360000, 375000, 390000}` decades) no fit window ever touches. At each
`N_cut`, fit three competing tail laws — power law
(`c_inf - A·N^-q`), exponential (`c_inf - A·e^-N/τ`), and power-law-with-
log-correction (`c_inf - A·N^-q·(ln N)^r`) — on data with `N ≤ N_cut` only,
then predict `contrast(N)` at the untouched hold-out probes and compare to
the real measured value there.

**Positive control**: the identical pipeline on the reference branch
(independently known to be exactly constant) — every window trivially
predicts the hold-out probes to `0.0000%`. Passes cleanly.

## Results

**`q` is remarkably stable.** Across the growing fit windows:
`0.5024 → 0.5021 → 0.5020 → 0.5019 → 0.5019 → 0.5018`. Later-half relative
spread: `0.01%`. This is a genuine, non-trivial confirmation that
`FINDING_P120`/`P121`'s single full-domain estimate (`q≈0.503`) was not an
artifact of fitting all the data at once.

**But the plain power law does not win.** `power_law_log` beat plain
`power_law` on held-out prediction at **every one of 6 windows**, by a
consistent `~2.6–3×` margin (e.g. at the largest window: `power_law`
`0.0006%` vs `power_law_log` `0.0002%`). Not noise — a real,
extrapolation-level discrimination, exactly the kind `FINDING_P121`'s own
interpolation-level spline test could not provide.

**The winning model's own exponent sits on the *other* side of `1/2`.**
`power_law_log`'s fitted `q` is `0.4847 → 0.4900` across windows —
systematically *below* `1/2`, with a negative log-correction
(`r: -0.131 → -0.094`, drifting toward `0` as the window grows).

## Correction 2 — a numerical-precision bug in the divergence check, caught before commit

A first attempt at checking each model's own implied deviation-energy
behavior integrated `(model(n)-c_inf)²` numerically out to `n_start·1e200`
(`N` up to `~1e205`). `scipy.integrate.quad` returned a **negative** value
for this manifestly non-negative squared integrand once the domain spanned
`190+` orders of magnitude — an unambiguous numerical-precision breakdown,
not a result. Caught before being reported. Fixed by applying the
**closed-form** criterion (`p=2q<1` diverges regardless of the log
exponent `s`; `p>1` converges regardless of `s` — the standard result for
`∫N^-p(ln N)^s dN`, itself verified numerically at a *safe*, moderate range
`[1e6, 1e60]` before being trusted) directly to each model's own fitted
`q`, cross-checked against `quad` at a numerically-safe range
(`[n_start, n_start·1e6]`) as a sanity spot-check only, not as evidence
about the infinite limit.

**Result: the two best-fitting models disagree.**

| Model | fitted `q` | closed-form deviation-energy verdict |
|---|---|---|
| `power_law` | `0.5018` | **converges** (finite) |
| `power_law_log` (better held-out fit) | `0.4900` | **diverges** |

---

## Verdict — **`Q-STABLE, MODEL-AMBIGUOUS-ON-DEVIATION-ENERGY, G_E-UNAFFECTED`**

Three separate, honestly-reported results:

1. **`q` genuinely stabilizes under forward extrapolation** — not drifting,
   consistent to `0.01%` across a 6× growth in fit-window size. A real,
   validated confirmation of `FINDING_P120`/`P121`'s earlier estimate.
2. **The deviation/excess-energy convergence question is model-dependent
   and *not resolved* by this file.** The plain power law says finite; a
   measurably-better-fitting log-corrected variant says divergent. The
   better-fitting model favors divergence. This tension is reported, not
   smoothed over.
3. **`G_E` itself — the actual quantity of interest throughout
   `FINDING_P114`–`P121` — is unaffected by any of this.** Its convergence
   was independently established (`FINDING_P120`'s L'Hôpital argument) for
   any `q>0`, confirmed here by direct numerical check spanning `q=0.1` to
   `0.9`. The `q`-vs-`1/2` question this file investigates is a real,
   separate, interesting question — but not a precondition for `G_E`'s own
   finiteness.

### Not established

- That `G_E` hinges on `q` vs `1/2` — it does not (see Correction 1).
- Which of `power_law` / `power_law_log` correctly describes the true
  asymptotic tail law — they disagree on the deviation-energy question,
  and this file does not adjudicate between them.
- That `power_law_log`'s extra parameter `r` reflects real physics rather
  than fitting flexibility from one more free parameter.
- A rigorous asymptotic theorem — a stable, well-predicting `q` over the
  tested windows and hold-out region is evidence on a finite domain, not a
  proof as `N→∞`.
- The true functional form beyond the three tested candidates.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).

### Where this could go next

Not named as commitments — options only. (a) Extend the fit-window/hold-
out protocol to test whether `r`'s drift toward `0` as the window grows
suggests `power_law_log` itself converges to plain `power_law` in some
limit, which would resolve the tension in `power_law`'s favor. (b) Test
additional (k, IC) combinations from `FINDING_P109`/`P110`'s own lever-gate
set with the same protocol to see whether this exact ambiguity (stable but
disputed `q`, log-correction winning) is generic or specific to `k=0.3`.
