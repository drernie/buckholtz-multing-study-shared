# FINDING P128 — Realistic hand-off ICs close FINDING_P127's own gap: **`HAND-OFF MECHANISM CONFIRMED`**

**Status:** built, ran, two bugs in this file's own diagnostic caught and
fixed before trusting the verdict; result is clean and decisive.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P128_realistic_handoff_ic_test.py`

> User-directed: "попробуй извлечь реалистичные IC из полной системы" (try
> to extract realistic ICs from the full system) — this is `FINDING_P127`'s
> own named "next step, not one option among several."

---

## The gap this closes

`FINDING_P127` built a reduced, provably `k`-independent late-time system
and confirmed *why an affine relationship must exist* between any two
`(k, IC)` trajectories. But seeded with small, **arbitrary** `psi`/`dph`
initial values, it could not reproduce the specific tail exponent
`q≈0.466` (`FINDING_P125`'s own established value) — diagnosed precisely:
those homogeneous modes (`exp(-N)`, `exp(-3N)`) decay to exact float64
zero well before the probe range starts, so a small arbitrary IC vanishes
before it can show a slow tail. `FINDING_P127`'s own "not established"
list named the fix: extract the REAL system's own state at some
intermediate `N` and use *that* as the hand-off, instead of a guess.

## The method

Solve the real, full `k=0.3` system once (`FINDING_P119`'s own `run_lna`,
`T_END=1e13`, the exact main case `FINDING_P120`–`P127` all used). At each
candidate hand-off `N_hand ∈ {100, 300, 1000, 3000}`: extract the full
state, recompute the **actual** `H(N_hand)` from the full system's own `H`
formula (not assumed to equal `H_Λ`), convert `t`-derivatives to
`N`-derivatives via `d(var)/dN = (d(var)/dt)/H`, and feed
`[pb, pb_N, psi, psi_N, dph, dph_N, drA_hat, qm_hat]` — `FINDING_P127`'s
own reduced-system state ordering — as its IC, integrated forward to
`N=2×10⁶`.

## Two bugs caught before trusting the result

1. **CONTROL 1's own regression check first failed.** `minimize_scalar`
   was given bounds of `K03_SELF_CONSISTENT_C_INF±200000` — copied from
   `FINDING_P126`'s own scan for the **unrelated** `k=0.5` case (whose
   `c_inf` is ~-49 million, a different scale entirely) — and wandered to
   the boundary instead of the known-correct optimum near `-38569`. Fixed
   with a tight `±50` window around the already-established anchor,
   matching `FINDING_P125`'s own original search-width discipline.
2. **With that fixed, the MAIN RESULT loop's own plateau search still gave
   a spurious near-zero result** — even though an *independent* check (the
   reduced-forward vs full-system-actual comparison, no optimizer
   involved) already showed **exact (0.0000%) agreement** at every matched
   `N` out to `3×10⁵`. That contradiction is what caught the bug, not a
   hunch: the loop's own `minimize_scalar` call used the same
   data-driven wide-bounds construction `FINDING_P127` used for its much
   smaller-magnitude arbitrary ICs, and — over this file's much
   larger-magnitude data — wandered to a different, spurious local
   minimum instead of the true one. Fixed by reusing the same tight,
   anchor-centered bounds Control 1 used, justified directly by the
   exact-match comparison. Both the naive and the fixed result are
   printed side by side in the script's own output, not just the one that
   "worked."

---

## Result

**Every one of the 4 tested `N_hand` values reproduces `q≈0.466` to within
`6×10⁻⁵` absolute** — an order of magnitude tighter than the already-strict
`0.01` threshold `FINDING_P125` established:

| `N_hand` | self-consistent plateau | `\|plateau − 0.465960\|` |
|---|---|---|
| 100  | 0.465928 | 3.19×10⁻⁵ |
| 300  | 0.465921 | 3.94×10⁻⁵ |
| 1000 | 0.465905 | 5.52×10⁻⁵ |
| 3000 | 0.465896 | 6.38×10⁻⁵ |

And **independently of that fit**, the reduced-forward trajectory matches
the real full system's own `contrast(N)` **exactly** (displayed
`0.0000%`) at every comparison point tested (`N` from `3×N_hand` out to
`3×10⁵`), for every `N_hand`. Reconnaissance also showed `H(N)/H_Λ`
already equals `1.00000000` by `N=30` — the reduction's own
`H=H_Λ`-constant approximation has effectively zero error at these `N`,
consistent with the exact match.

## Verdict — **`HAND-OFF MECHANISM CONFIRMED`**

The gap is closed. The real full system's own early, `k`-dependent
transient — handed off at *any* of the tested `N_hand` — carries enough
imprint on `psi`/`dph`/`drA_hat`/`qm_hat` to source the slow `q≈0.466`
tail once continued through `FINDING_P127`'s reduced, `k`-independent
system. The tail was never missing from the reduced equations; it was
missing from `FINDING_P127`'s own small-arbitrary-IC test, exactly as that
file's own diagnosis predicted.

### Not established

- The specific numeric value `A≈6679` (`FINDING_P126`) or a closed-form
  expression for `q` — this file confirms the *mechanism* that produces
  `q≈0.466` from a realistic hand-off; it does not derive `q`'s value in
  closed form, nor does it compute `A` from first principles.
- That `H=H_Λ` is asymptotically exact — the H-approximation-only check
  bounds its error at each *tested* `N_hand` (found to be ~0 there), not
  in the `N→∞` limit.
- Hand-off points earlier than `N_hand=100` (`kk²·exp(-2N)` is not yet
  fully negligible there for `kk=0.3`).
- Anything at Lambda values, or `(k, IC)` combinations, other than the
  `k=0.3` main case tested throughout `FINDING_P119`–`P127`.
- Anything about MULTING itself (Gate 1). Any `k[h/Mpc]`.
