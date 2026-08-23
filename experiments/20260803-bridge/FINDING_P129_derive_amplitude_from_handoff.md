# FINDING P129 — Deriving A≈6679 from real hand-off states: **`POINTWISE FIDELITY EXTENDED TO k=0.5; AMPLITUDE MATCH IS A COROLLARY, NOT INDEPENDENT EVIDENCE`**

**Status:** built, ran cleanly, own draft verdict caught as an overclaim
by a context-asymmetric skeptic review before being reported; corrected.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P129_derive_amplitude_from_handoff.py`, `skeptic_review_p129.md`

> User-directed, following a detailed proposal: derive `A≈6679`
> (`FINDING_P126`) from real hand-off state, tested for `N_hand`-invariance
> BEFORE comparison to 6679 — with an explicit warning, raised by the user
> before this file was built, that `FINDING_P128`'s own "trajectories
> match exactly" result could be an expected closure/control rather than
> independent confirmation.

---

## The test

For each `N_hand ∈ {100, 300, 1000, 3000}`: extracted real hand-off states
from **both** the k=0.3 **and** k=0.5 full systems, ran both through
`FINDING_P127`'s reduced system (no `k` anywhere in it), and computed
`A_pred(N_hand)` — the ratio of their deviations at `FINDING_P120`'s own
14 regression-anchored N-points, exactly the construction
`FINDING_P126`/`P127` used for their own affine checks.

## Raw numbers (clean, no bugs)

`A_pred(N_hand)` = 6679.24, 6679.27, 6679.36, 6679.46 for
`N_hand=100,300,1000,3000` — relative spread `0.0033%` across `N_hand`
(comfortably invariant). Compared to `FINDING_P126`'s own regression
anchor `A_hat_mean=6678.998`: relative distance `0.01%`.

## The skeptic catch

This suspiciously clean result (matching `skeptic-triggers.md` Trigger 4)
was sent to a context-asymmetric skeptic — claim + code only, no
reasoning chain — before being reported. **Verdict: OVERCLAIM, high
confidence.**

The core point: this file *also* verified, for the first time, that
`FINDING_P128`'s own "reduced-forward matches full-system-actual exactly"
result extends from k=0.3 to k=0.5 (`0.0000%` relative difference at
every spot-checked N up to `3×10⁵`). But **once that pointwise
equivalence holds for both k values, any ratio-of-deviations statistic
computed on the reduced trajectories must equal the same statistic
computed on the full trajectories, to the same precision — as a matter
of arithmetic, not physics.** `A_pred` matching `FINDING_P126`'s own
`A_hat` (measured independently, from full-system data alone) is
therefore a **corollary** of the pointwise-equivalence extension, not a
separate confirmation via "an entirely different method." The hand-off
states `ic03`/`ic05` were themselves extracted *from* the full system, so
the match inherits the full system's own information content rather than
predicting it independently.

Full review: `skeptic_review_p129.md`.

---

## Verdict — **two claims, kept separate**

1. **`[NEW]`** The pointwise reduced-forward-vs-full-actual fidelity
   `FINDING_P128` established for k=0.3 also holds for k=0.5 — genuinely
   new, not guaranteed a priori, and not previously tested.
2. **`[COROLLARY, not independent evidence]`** `A_pred` matching `6679`
   to `0.01%` follows near-arithmetically from claim 1. It does **not**
   independently confirm the amplitude value — a genuinely independent
   test would require a hand-off state *not* derived from the full
   system's own trajectory (e.g. an analytic low-k asymptotic estimate),
   not attempted here.

### Not established

- That the amplitude match is independent evidence beyond claim 1 — per
  the skeptic review, it is not.
- A closed-form (symbolic) expression for `A` in terms of `Λ, G_N,
  C_MATTER, k` — this remains a numerical cross-check, not an analytic
  derivation.
- *Why* the specific hand-off states carry the amplitude they do — traces
  to the early, k-dependent transient the reduction excludes, exactly as
  `FINDING_P127`/`P128` already stated.
- Pointwise fidelity for k=0.5 beyond the `N=3×10⁵` spot check —
  `N_ANCHORS` includes points up to `920067`, near the full system's own
  `T_END=1e13` reach; not independently spot-checked there.
- Anything at Lambda values, or `(k, IC)` combinations, other than
  k=0.3/k=0.5's main case tested throughout `FINDING_P119`–`P128`.
- Anything about MULTING itself (Gate 1). Any `k[h/Mpc]`.
