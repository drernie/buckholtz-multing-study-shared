# FINDING P127 — Attempting to derive `A≈6679` from first principles: **`AFFINE-MECHANISM-CONFIRMED, SLOW-TAIL-MECHANISM-STILL-MISSING`**

**Status:** built, ran, gave a mixed result; user asked to verify before
accepting it ("подожди, проверь результат") — re-investigated directly
rather than left as an open "derivation error or IC artifact?" question,
and resolved that specific ambiguity.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P127_reduced_system_first_principles.py`

> User-directed: "попробуй вывести A из первых принципов" (try to derive A
> from first principles) — the exact gap `FINDING_P125`/`P126` both named
> under Not Established: neither derived *why* the affine constant
> `A≈6679` exists, only measured that it does.

---

## The derivation attempted

`FINDING_P118`'s full ODE system, at late `N`, has exactly one source of
`k`-dependence: the `k²·exp(-2N)` terms in `dphdd` and `drA_hat_d`. Both
decay to zero. Dropping them (along with `ρ_A=C_MATTER·exp(-3N)→0`) and
setting `H=H_Λ` constant gives a **reduced, provably `k`-independent**
6-variable system (`pb, pb_N, psi, psi_N, dph, dph_N`, sourcing two linear
integrators `drA_hat, qm_hat`) — derived explicitly by converting
`t`-derivatives to `N`-derivatives, shown in full in the file's own
docstring.

**Positive control, clean pass**: `pb`'s own reduced equation, solved in
isolation, reproduces `FINDING_P125`'s already-validated slow-roll law
almost exactly (ratio to prediction: `1.0029` at `N=1000` → `1.000001` at
`N=10⁶`).

## First pass — a mixed result flagged for verification

Solving the full 6-variable system from two arbitrary initial conditions
gave: the affine relationship held (`0.0094%` spread), but `q_local`
stayed near zero, and one IC's raw deviation reached `~9×10²²` by
`N=10⁶` — astronomically large. The original draft left open whether this
was a derivation error or an IC artifact, without distinguishing them.

## Verification round — the ambiguity resolved directly

**Checked the initial conditions themselves first.** `pb0=1e-3/2e-3` at
`N=1` sit **four orders of magnitude** off the slow-roll attractor at
`N=1` (`pb_attractor≈1.12×10⁻⁷`) — an enormous, unphysical initial
displacement (`μ·pb0³ ~ 10⁵–10⁶`). Rerunning with `pb` started exactly on
its own attractor at `N=100`: **the astronomical blow-up is gone**
(deviations now `≈-10`, not `~10²²`). This directly rules out a
derivation error as the explanation for *that* symptom — it was IC
pathology.

**The affine relationship held again, even more cleanly** (`0.0026%`
spread) from the corrected ICs — further, independent confirmation of the
dominant-mode mechanism.

**But `q_local` still didn't show `≈0.466`.** Diagnosed directly, not
guessed: `psi`'s own homogeneous solution decays as `exp(-N)` or
`exp(-3N)` (roots of `psi_NN+4·psi_N+3·psi=0`, this file's own reduction).
Checked numerically — `exp(-N)` is **exactly `0.0`** in float64 by
`N≈500`, well before this file's own probe range (`N≥1000`) even starts.
Starting `psi`/`dph` "fresh" with small values at `N=100` means their free
component has fully vanished before any probe point — only a *particular*
solution, sourced continuously through the `pb`-dependent coupling terms,
could survive, and a small arbitrary IC doesn't excite enough of it to be
visible.

---

## Verdict — **`AFFINE-MECHANISM-CONFIRMED, SLOW-TAIL-MECHANISM-STILL-MISSING`**

Three claims, kept separate:

1. **The existence of *an* affine relationship is genuinely explained**,
   confirmed twice, independently, on arbitrary (then attractor-corrected)
   initial conditions unrelated to `k=0.3`/`k=0.5`.
2. **The earlier astronomical blow-up was IC pathology, not a derivation
   error** — directly verified, not left as an open question.
3. **The specific value `q≈0.466` still was not reproduced** — but the
   reason is now precise, not vague: small, arbitrary `psi`/`dph` initial
   values decay via their own fast homogeneous modes long before the probe
   range, so they cannot show the slow tail. The real system's slow tail
   most likely requires *substantial* `psi`/`dph`/`drA_hat`/`qm_hat`
   values, carried over from the early, `k`-dependent transient this
   reduction deliberately excludes — not a small-IC artifact, and (as far
   as tested) not a sign of an error in the reduced equations themselves.

### Not established

- The specific numeric value `A≈6679` — this file confirms the mechanism
  that guarantees *some* affine relationship exists; it does not compute
  what `k=0.3`/`k=0.5`'s own early transients hand off to it.
- A closed-form or correctly-reproduced numerical value for `q` from the
  reduced system — not achieved with small arbitrary ICs.
- That `H=H_Λ=const` is an exact approximation rather than a very good
  one — only the `pb`-only positive control directly checked this.
- Whether *substantial* (non-arbitrary) `psi`/`dph`/`drA_hat`/`qm_hat`
  values, carried over from a real early transient, would make this
  reduced system reproduce `q≈0.466` — named as the concrete next step,
  not attempted.
- Anything about MULTING itself (Gate 1). Any `k[h/Mpc]`.

### Where this could go next (named, not committed)

Extract the real system's own state vector at some intermediate `N`
(where `k²/a²` is already small but not yet negligible over the full
range) and use *that* as the reduced system's initial condition, rather
than a small arbitrary guess — this file's own verification round makes
this the clear next step, not one option among several.
