# FINDING P140 — positivity does not discriminate the two completions
# on this campaign's own trajectory range: BOTH-SAFE, honest NULL

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verdict:** `BOTH-SAFE` (NULL result — positivity is not a discriminant
here)
**Bottleneck:** 2 (Unique completion) — a self-directed selection-
principle check, does not touch bottleneck 4's own IC-sensitivity work
**Script:** `P140_completion_positivity_check.py`, positive-control-tested

---

## 1. Why this file

User-proposed self-directed search option for bottleneck 2: does the
linear completion `M(φ)=1-g·φ` go unphysical (`M<0`, implying a negative
effective matter density) on trajectories this campaign has already
computed? The exponential completion `M(φ)=exp(-g·φ)` is positive by
construction for all `φ`; the linear one only for `φ<1/g`. If the
project's own already-explored trajectories exceed `1/g`, the linear
completion would already be excluded on existing ground — no new
mechanism, external fact, or literature search needed.

## 2. Result

Scanned all `(k, lever)` combinations already used across `P78`-`P139`
(`k∈{1,2,3,10}`, lever `∈{0.1,0.5,1,2}`, both mass laws, `ĝ=1` branch),
sampling `φ̄(t)` at 2000 points per trajectory:

| law | worst `max(φ̄)` | at | threshold `1/ĝ` |
|---|---|---|---|
| linear | `0.1685` | `k=10, lever=×2` | `1.0` |
| exponential | `0.1645` | `k=10, lever=×2` | — (safe for all `φ`) |

**`φ̄` never exceeds `~0.17`, well below the `1.0` threshold** — the
linear completion stays comfortably physical (`M>0`) everywhere this
campaign has already explored. Positive control (`ĝ=0` branch, `M≡1`
for both laws) passes exactly.

## 3. Verdict

**`BOTH-SAFE`.** Positivity does not discriminate the two completions on
the range this project's own reconstruction actually uses — an honest
NULL, not a null-because-untested result. The general theoretical
asymmetry (exponential positivity-safe for *any* `φ`; linear only on a
bounded range) still stands as a structural fact, but it is moot for
this campaign's own trajectories: both candidates remain equally
physical here.

## 4. What this does NOT establish

1. **That the two completions are physically equivalent in general** —
   only that neither is excluded by positivity on the range explored.
2. **Anything about a wider trajectory range** than `P74`-`P139` already
   used — a different parameter regime could behave differently, not
   checked here.
3. **Anything about bottleneck 4** (IC-sensitivity) — this file is
   entirely about bottleneck 2 (Unique completion) and does not touch
   the IC-sensitivity workstream.
4. **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in
   force.
5. **Anything about MULTING itself** (Gate 1). Both completions are
   ours.

## 5. Controls

- **Positive control**: `ĝ=0` branch, `M≡1` identically for both laws —
  passes exactly (`min(M)=1.000000000000`).
- **Reuse, not re-derive**: `run`/`mass_law` imported directly from
  `P79`'s own module.
