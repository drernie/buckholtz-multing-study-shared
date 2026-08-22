# FINDING P91 — **B-CONFIRMED.** The boundary reconstructs, my prediction about it did not, and P81's predicate turns out to be grid-sensitive

**Status:** built, run, withdrawn, probed, revised, re-run. Verdict against
pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifacts:** `P91_boundary_through_the_reconstruction.py` (rev 2),
`p91_tightness_probe.py`

> The last registered reconstruction target. It took two revisions, and the
> reason for the second is the more useful half of this finding.

---

## Revision 1 withdrew itself, correctly

It returned **`B-SUSPICIOUS-TIGHT`** — agreement of `2.220e-16` and `0.000e+00`
between two bisections deliberately given different brackets. Its own
pre-registered rule said that two independent searches cannot do that, and
withdrew the result. `p91_tightness_probe.py` then measured the cause, and there
were **two**, one a real result and one a defect in my own control.

### (a) The agreement was real

Re-locating each flip at `tol 1e-13` instead of `1e-4`:

| edge | recon | P81 | relative |
|---|---|---|---|
| `λ=0` | `0.7382122147416424` | `0.7382122147462467` | `6.24e-12` |
| `λ=0.1` | `2.751764836587313` | `2.7517648365591185` | `1.02e-11` |

The `2.220e-16` was **alignment luck between two dyadic grids** — bracket
`(1.0, 0.1)` lands on a grid of spacing `5.493e-05`, bracket `(0.9, 0.2)` on
`4.272e-05`, and after 14 halvings two of their points happened to fall within
one ulp of each other. Not shared state.

### (b) My "different brackets" control failed by its own construction

Revision 1 chose them **by eye**: `(3.5, 1.5)` against P83's `(3.0, 2.0)`. But

```
(3.5 + 1.5)/2 = 2.5 = (3.0 + 2.0)/2
```

Same first midpoint. One extra step later the reconstruction sits at bracket
`(3.0, 2.5)` — exactly where P81 already was — and from there the paths
**coincide**: 12 of 13 midpoints shared, identical final bracket, bitwise
identical answer. That edge's "perfect agreement" demonstrated only that
**bisection is deterministic**.

**Eighth control this session to fail by its own construction, and this one
entirely mine.** The docstring had warned about exactly this failure mode; the
bracket choice simply failed to prevent it.

---

## What revision 2 changed — four sharpenings, no relaxations

**1. Independence is measured, not chosen.** Every bisection records its path.
*"The brackets look different"* is not a measurement; *"the paths diverged"* is.

**2. Measured on the searches that are actually scored.** This is the subtle one.
The merge is a **coarse-tolerance** phenomenon: once midpoints come within
`1e-11` of the flip the two predicates disagree and the paths separate
regardless of where they started — which is precisely why the tight run returned
two *different* numbers on the merged edge. So the post-condition applies to the
tight searches. Applying it to the coarse paths would have discarded a valid
measurement over a defect in a number that is not being scored.

**3. The scored quantity changed.** Revision 1 scored the `tol=1e-4` answers.
Each lands within `tol` of its own flip, so their mutual difference can be
anything from `1e-16` to `1e-4` depending on grid alignment — **it measures
alignment, not agreement.**

**4. Part C was aimed at the wrong object.** The reconstruction classifies via a
**terminal event** on the continuous trajectory: if the event never fires, no dip
below `FLOOR` occurred *anywhere*, on any grid. So its answer is grid-free **by
construction**, and revision 1's exact `0.000e+00` came from varying something
the answer does not use. The real question was always whether **P81's sampled
min steps over a dip.**

---

## Results

### Part A — the flips, at `tol 1e-12`, independence measured

| edge | flip recon | flip P81 | midpoints separated | relative |
|---|---|---|---|---|
| `λ=0` | `0.738212214741861` | `0.738212214746068` | `35` | `5.698e-12` |
| `λ=0.1` | `2.751764836589718` | `2.751764836558323` | `36` | `1.141e-11` |

The tight paths diverged over 35 and 36 midpoints — genuinely independent
searches, measured.

**The coarse numbers, kept for the record and explicitly uninformative:**

| edge | coarse relative |
|---|---|
| `λ=0` | `2.220e-16` |
| `λ=0.1` | `5.146e-05` |

This pair is itself the demonstration. **The same quantity moved from
`0.000e+00` to `5.146e-05` purely because the bracket was repaired**, while the
underlying flips agree at `1e-11` either way. The coarse comparison tracks
bracket alignment; it is not a measure of agreement.

### Part C — P81's boundary **is** grid-sensitive at `λ≠0`

| edge | `n_probe=300` | `n_probe=3000` | `n_probe=30000` | movement |
|---|---|---|---|---|
| `λ=0` | `0.738223267` | `0.738223267` | `0.738223267` | `0.000e+00` |
| `λ=0.1` | `2.752319336` | `2.751831055` | `2.751831055` | `1.774e-04` |

**Both halves of the pre-registration confirmed.** At `λ=0`, `φ̄` is monotone
(diamond D1) and the sampled minimum is the endpoint — exactly zero movement,
which independently corroborates D1. At `λ=0.1` the scalar oscillates, and a
coarse grid **steps over dips**: the boundary moves by `1.774e-04`.

**The practical reading, stated as a margin rather than a reassurance.** P81's
default `n_probe=3000` is adequate — `3000 → 30000` moves it by *exactly* zero.
But the margin is about **one order**: at `300` the boundary shifts by
`1.8e-04`, which is **above** the `1e-4` bisection tolerance the boundary is
quoted at. The predicate is grid-sensitive; its default merely sits on the safe
side of the sensitivity.

---

## Verdict

**B-CONFIRMED.** Worst tight-tolerance flip agreement `1.141e-11 < 1e-8` on
every independent edge. The two implementations locate the **same** boundary.

### This refutes a prediction I registered myself

`FINDING_P89` predicted the boundary would reproduce **only** to its bisection
tolerance (`≈1e-4`) and **not better**. It reproduces about **eight orders
better**. The prediction confused the **precision of the search** with the
**accuracy of the answer**: the bisection tolerance is a property of the search,
and tightening it keeps improving the agreement down to `1e-11`.

`FINDING_P90`'s sharpening inherited the same error — *"if it agrees much better
than `1e-4` while both use `1e-4`, the two searches are sharing state."* Also
wrong, and it is what caused revision 1's spurious withdrawal. Both are recorded
as refuted rather than quietly dropped.

### Perelman condition 5

Now covers **`ε(k)`, `f`, `μ`, and the viability boundary** — all four at the
**independently-written code** rung, and no higher. Same person wrote both
implementations; a different **model**, a **blind replication**, and a **new
physical experiment** remain absent. **Strong**, not *Very strong*.

### Scope and what is not established

- **Only the `min(1−ĝφ̄)` clause is reconstructed.** Part 0 measured that this is
  what binds at both boundaries; `a ≤ 0` is vacuous when `a` is the axis, and
  `H` non-monotone is not surveyable where `H → 0`. The comparison is licensed
  there **and nowhere else**.
- Only edges whose tight searches were **measured** to separate are scored.
- A reconstruction tests the **implementation**, never the **specification**.
- Nothing observational. `NO_BRIDGE_FITTING` untouched. Gate 1 holds.
