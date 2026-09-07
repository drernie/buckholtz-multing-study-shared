# FINDING — Stage 3d: BAO wiggles do **not** break the one-sign-change
# premise. The BAO branch is closed.

**Date:** 2026-09-07
**Artifact:** `stage3d_bao_wiggle_signchanges.py`
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Closes:** the `OPEN` item recorded by `FIX 4` / `FIX 5` in
`AMENDMENTS_after_step8a_skeptic.md`.

---

## 1. What was open

The Step 8a skeptic showed that C4's conclusion (no finite compensation
radius) needs `ξ` to have **exactly one sign change** — and that `stage3c`
never measured it. `FIX 5` added the measurement and got **1** for the two
smooth transfer functions.

But `FIX 4` had also found that the promised BAO variant was never
implemented, and that **this is precisely the case where the premise is
not guaranteed**: baryon acoustic oscillations put a real feature at
~105 Mpc/h, right where `ξ` is small and approaching its zero.

That was the one case that could have broken the argument. It is now run.

## 2. Two independent routes, because one implementation cannot audit itself

Transcribing the full Eisenstein & Hu 1998 fitting formula is ~40 lines of
specific constants and is error-prone.

- **W1** — full **EH98 with wiggles**: `z_eq`, `k_eq`, `z_d`, `R_d`/`R_eq`,
  sound horizon `s`, `k_silk`, `α_c`, `β_c`, `α_b`, `β_b`, `β_node`, node
  shift `s̃`, and `T = f_b·T_b + f_c·T_c`.
- **W2** — a **BAO template** with tunable amplitude:
  `T_nw·√(1 + A·j₀(ks)·exp(−(kΣ)²))`, `s ≈ 150` Mpc, `Σ = 7` Mpc/h. Its
  amplitude ladder answers what a single yes/no cannot: *how large would
  the wiggle have to be to break the premise at all?*

## 3. Controls on W1 — the transcription is sound

| control | result |
|---|---|
| `T(k) → 1` as `k → 0` | **1.00000** — PASS |
| wiggle amplitude `max\|T_full/T_nw − 1\|` | **0.0328** — 3.3%, the right order for real BAO |
| oscillatory structure | **14 sign changes** of the ratio about its mean — PASS |

The second and third are the discriminating ones: almost any typo in
`α_b`, `β_b` or `k_silk` would shift or kill the amplitude while leaving
the curve smooth. Fourteen alternating signs is not something a
transcription error produces by accident.

## 4. The measurement

| spectrum | **#sign(ξ)** | **#sign(δ̄)** | `R_xi0` [Mpc] | `R_comp` |
|---|---|---|---|---|
| EH98 no-wiggle (FIX 5 baseline) | **1** | 0 | 180.2 | **NONE** |
| **W1 — EH98 FULL, real wiggles** | **1** | 0 | **172.8** | **NONE** |
| W2 template, `A=0.05` (realistic) | **1** | 0 | 188.9 | **NONE** |
| W2 template, `A=0.20` (4× real) | **1** | 0 | 203.2 | **NONE** |
| W2 template, `A=0.60` (12× real) | **1** | 0 | 220.0 | **NONE** |
| W2 template, `A=0.95` (≈19× real) | **1** | 0 | 227.3 | **NONE** |

**W1 and W2 agree on the count.**

## 5. Why the invariance is not trivial

The wiggle demonstrably *does* something: `R_xi0` moves from 172.8 to
227.3 Mpc across the table — a **31% spread**. The spectra genuinely
differ. What is invariant is the **count**, not the curve.

**An honest difference between the two routes, worth stating:** W1 moves
`R_xi0` **down** (180.2 → 172.8) while the template moves it **up**
(→ 188.9 at realistic amplitude). They are not the same spectrum — the
template is a crude `j₀` modulation, W1 carries Silk damping and the node
shift. That they disagree on the *direction* of the shift while agreeing
on the *count* is what makes the agreement a real cross-check rather than
two views of one object.

## 6. Verdict

> **BAO does not break the premise.** With real acoustic oscillations
> present, `ξ` still has exactly one sign change and `δ̄` still never
> crosses zero. Pushed to ~19× the real amplitude, the count does not
> move.

C4's conclusion survives the one case `FIX 4` identified as capable of
breaking it, and now rests on a premise **measured under wiggles**, not
only under smoothed spectra.

## 7. What this does NOT establish

1. **Linear theory only**, as before. Non-linear evolution, redshift-space
   effects and sample selection are not modelled.
2. **Two transfer-function families, not the space of all spectra.** The
   band-limited counterexample from `FIX 5` (`δ̄` reaching `−0.0862`)
   still stands: spectra with a *narrow* spectral peak do break the
   premise. BAO is a broad, damped modulation on a broadband spectrum,
   which is why it does not.
3. **The amplitude ladder is a template ladder.** `A = 0.95` is not a
   physical universe; it bounds the template's sensitivity, not nature's.
4. **Nothing about MULTING** (`NO_AUTHOR_ERROR`).

## 8. What remains open in the amendments

One item only, unchanged: `stage3c`'s convergence block varies solely
`damp` (0.10 / 0.15 / 0.25 Mpc/h); `kmin`, `kmax`, `nk`, `rmax` are still
never varied, despite `xi_of_r`'s docstring promising a convergence check.
