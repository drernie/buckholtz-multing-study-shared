# FINDING P112 — Envelope/RMS observable built and controlled exactly as specified; **`PHASE-SHIFT CONTROL FAILS`**, traced to the `a1` anchor sitting inside `P111`'s own transient — correctly stopped, not forced

**Status:** built, run, own reconnaissance done before building (one correction
made to `FINDING_P111`'s characterization), two real design flaws found and
fixed by the file's own controls, one control still fails for a diagnosed
reason — the file correctly stops rather than reporting an unvalidated
GAP-CLOSES/STILL-OPEN verdict.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P112_envelope_rms_growth_observable.py`

> User-directed build: a phase-robust Envelope/RMS growth observable to
> replace point-sampled `G_growth`, per a detailed decisive-experiment design
> (RMS/peak amplitude in a window, positive control at k=10, phase-shift
> control, amplitude-scaling control, RMS-vs-peak comparison). Three real
> problems were found along the way — one refining `FINDING_P111`'s own
> premise before any code was written, two caught by the file's own
> pre-registered controls after code was written. All three are reported
> here, not smoothed over.

---

## Step 0 — reconnaissance before building, refining `FINDING_P111`

A dense 10,000-point log-spaced scan of the coupled contrast for
`(Λ=1e-15, k=0.3, φ̄̇(1)×0.1)` over `lna∈[-10.6, 91.1]` found only **two** sign
changes total — one at `lna=-8.16` (`a/a_star=2.8×10⁻⁴`, indistinguishable
from numerical noise at the very start of integration) and **one** genuine
transition at `lna=8.84` (`a/a_star≈6934`). After that crossing, contrast
stays negative and its *magnitude* keeps changing — not settling quickly.
Widening `T_END` further (mirroring `FINDING_P108`'s own precedent):
`|G_growth|` grows from `722516` (`T_END=1e9`) to `811964` (`T_END=2e9`,
`+12%`) before the integrator overflows at `T_END≥3e9`.

**This refines, not reverses, `FINDING_P111`'s conclusion.** Not literally
repeated multi-period oscillation — a single dominant transition followed by
either very slow convergence or genuinely unbounded growth, reach-limited
before either can be distinguished by point-sampling. Point-sampled
`G_growth` is still the wrong tool; a window-based observable is still the
right next move.

## The observable, exactly as specified

`A_RMS := √⟨contrast²⟩` and `A_peak := max|contrast|`, both over a window
`[a_center/W, a_center×W]`, sampled densely (400 points, log-spaced in `t`).
`G_RMS := (A_RMS,coupled(a2)/A_RMS,coupled(a1)) / (A_RMS,reference(a2)/A_RMS,reference(a1))`
— the same `a1→a2` double-ratio structure `growth_a_matched` was built to
measure, with RMS/peak amplitudes replacing single point values.

## Bug 1 — caught before any run: signature mismatch left mid-edit

The file was interrupted mid-redesign (a first, single-window design had
already failed its own positive control by 35%, diagnosed as not preserving
`G_growth`'s `a1`-normalized double-ratio structure, and was being rewritten
to take both `a1` and `a2`). Three `main()` call sites still used the old
one-argument signature. Fixed mechanically — no physics content, just
finishing an interrupted edit — verified by `ruff check` and a clean run.

## Bug 2 — caught by the file's own amplitude-scaling control: the control's own design was wrong

First run: **positive control passed** (`RMS`: `6.1%` off, `peak`: `8.0%` off,
both under the `10%` tolerance) — but the **amplitude-scaling control failed**
badly: scaling `dph0` alone by `3×` gave an observed ratio of `1.013`, not the
predicted `3.0`.

Traced directly, not assumed: `P105`'s own `initial_data()` has **three**
nonzero-default perturbation ICs — `psi0=1e-5, dph0=1e-6, drA0=1e-5` — all
entering `psid0`/`qm0` *linearly*. Scaling only `dph0` while `psi0`/`drA0`
stay fixed doesn't rescale the trajectory by `3×`; it changes which mix of
linear modes gets excited, which is a different (and untested) claim. Fixed
by scaling all three ICs together by the same factor — ratio came back
**exactly `3.0000`**, confirming both that the fix was correct and that the
RMS/window machinery itself is linear, as designed.

## Bug hypothesis 3, tested and refuted: window extrapolation

`PHASE-SHIFT CONTROL` still failed by a huge margin (`286%` spread across
`W=5,10,20`, vs. a `50%` tolerance). First hypothesis: `t_hi = t_center ×
W²` could exceed `t_end`, putting `sol.sol()` into scipy's unreliable
dense-output extrapolation region. **Checked directly**: at `W=5`, `t_hi` was
already `2.6×` `t_end` before any fix. Clipped `t_hi` to `min(t_end, ...)`.
**Result barely changed** (`352→352`, `12.2→12.2`, `2.27→2.27`) — this
hypothesis was wrong, and is reported as refuted, not silently dropped.

## The real cause, found by direct testing: the `a1` anchor sits inside `P111`'s own transient

Tested whether the instability tracked the `a2≈6934×a_star` transition found
in Step 0 — anchored the phase-shift probe at `a2=1e3×a_star` (well before)
and `a2=5×10⁴×a_star` (well after). **Both showed the same order-of-magnitude
instability** (`~1255→40→6` and `~635→16→2` across `W=5,10,20`) — this
hypothesis was also wrong.

Held `a2` and `W` fixed, varied only `a1` (established convention:
`a1=a_star×X_LO`, `X_LO=0.2`): `G_RMS` at `a1/a_star=0.2` is `12.2`; at
`a1/a_star=1,2,5,10` it drops to `0.45, 0.32, 0.25, 0.22` — a completely
different regime. Then, holding `a1/a_star=5` fixed and varying `W=5,10,20`:
`G_RMS = 0.20, 0.25, 0.33` — a `~60%` spread, down from `286%`, though still
short of a clean pass.

**Diagnosis, directly confirmed:** `a1 = a_star×0.2` — the established
convention carried over from every earlier file in this arc, where it worked
fine for smooth cases — sits inside the *same* steep transient
`FINDING_P111` already found in the coupled run's own `δφ` (changing by
`~4` orders of magnitude between `x=0.2` and `x=1`). The RMS/window
machinery itself is not broken (the positive control, at the same `a1`
convention but a smooth `k=10` case with no such transient, already passed);
the anchor choice is wrong specifically for this extreme-IC, low-`k` case.

---

## Verdict — **`PHASE-SHIFT CONTROL FAILS`; correctly stopped, not forced**

Per this file's own pre-registered discipline (the same discipline already
applied to the positive control): a required control failing means any
downstream `GAP-CLOSES`/`STILL-OPEN` verdict would rest on an unvalidated
observable. The file stops (`return 1`) before the main test rather than
printing a verdict that looks decisive but isn't. **The main test's raw
numbers were inspected during debugging** (not hidden) and were themselves
inconclusive either way — still changing by double digits of percent at both
the earliest and latest measured windows — so nothing was suppressed by
stopping here.

This is not a dead end for the underlying question. It is a precise,
directly-verified diagnosis of *why* the specified design doesn't yet work
at the established anchor, one level more specific than `FINDING_P111`'s own
transient diagnosis: the transient isn't just a nuisance for point-sampling,
it also contaminates any window-based average anchored inside it. Two real
bugs were found and fixed along the way (the amplitude-scaling control's own
design, and a refuted-but-worth-recording extrapolation hypothesis); neither
explains the remaining failure, which is squarely the anchor.

### Not established

- Whether an adaptively-chosen `a1` (placed by a principled rule tied to
  where the transient structurally settles, not by picking whichever value
  happens to pass) would let the phase-shift control pass and the main test
  proceed to a trustworthy `GAP-CLOSES`/`STILL-OPEN` verdict — not attempted
  here, since doing so post-hoc, after seeing which `a1` values "worked,"
  would be exactly the "picking a lucky moment" the user's own design
  explicitly ruled out.
- Whether `G_RMS`/`G_peak`, once properly anchored, would converge as `a_end`
  moves later — the main test never ran to a trusted conclusion.
- Anything at `Λ` values other than `1e-15`.
- Any numeric value of `eps(k)`, `G_growth`, `G_RMS`, `G_peak`, or `f(k)` in
  physical units, or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
