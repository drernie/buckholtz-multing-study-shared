# FINDING — Stage 3b: the standard picture's "reversal" is a **different
# derivative**, and MULTING's own lands outside its own construction

**Date:** 2026-09-07
**Artifact:** `stage3b_standard_web_reversal_scale.py`
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Status:** Stage-3b result, **not promoted**, no Step 8a pass.

---

## 1. The obvious comparison is a category error — stated before making it

The natural move is to compare MULTING's `d_flip = 92.67 Mpc` against the
**turnaround radius**, *"the scale where the attraction due to its mass is
balanced by the repulsion due to dark energy"* (Bhattacharya,
Dialektopoulos, Romano, Skordis & Tomaras, arXiv:**1611.05055**, abstract,
`[VERIFIED-arXiv-abstract]`).

**That would be wrong**, and the reason is the same conflation this
project has been catching all day:

| | what reverses |
|---|---|
| MULTING `d_flip` | `∂(ä/a)/∂k` — the **response** to thermal energy |
| turnaround `r_ta` | `ä/a = 0` — the **quantity** itself |

Different derivatives. Reported for context only:

| quantity | value |
|---|---|
| `M0` (TJB's node) | `1.1931e45` kg = `6.000e14` solar masses |
| `R500` | 1.315 Mpc |
| `r_ta,max` (one node) | **9.40 Mpc** |
| `r_ta,max` (pair, `2M0`) | **11.84 Mpc** |
| MULTING `d_flip` | **92.67 Mpc** — `7.8x` larger |

**Do not quote the 7.8x as the discriminant.** It compares two different
questions.

## 2. The correct comparison: the standard *response* has no reversal

Point mass `M` in a `Lambda` background, test particle at `r`:

```
rddot/r        = -GM/r^3 + Lambda c^2/3   ->  reverses at r_ta
d(rddot/r)/dM  = -G/r^3                   ->  NEGATIVE FOR ALL r, NEVER FLIPS
```

The response decays as `1/r^3` and stays negative at every radius. **In the
uncompensated point-mass + Lambda picture there is no standard reversal at
any scale to compare `d_flip` against.**

## 3. Why MULTING has one and the point mass does not — structural

```
dipole      + b1 R    /(c^2 d^4)     ~ d^-4   repulsive
quadrupole  - b2 k R^2/(M c^4 d^5)   ~ d^-5   attractive
```

The attractive term falls **faster**, so it dominates at small `d` and
loses at large `d` — **exactly one crossing**. The standard response is a
single term and therefore has none. The reversal is a structural
consequence of two tiers with different powers of `d`, not a tuned
coincidence.

**On this reading the shape IS discriminating.**

## 4. The live `[UNKNOWN]` — compensation

A real cosmic-web overdensity is **compensated**: mass gathered into a
knot leaves its surroundings underdense, and underdense regions expand
faster than average (Bolejko, Nazer & Wiltshire, arXiv:**1512.07364**).
A compensated perturbation can therefore give a **positive**
`dH_local/dM` outside its compensation radius — a reversal of its own,
from ordinary physics.

`[UNKNOWN]` at what scale. **That** scale, not `r_ta`, is the number to
compare with 92.67 Mpc. `[INFERRED]` it cannot exceed roughly half the
mean separation to neighbouring structures — past that you are inside the
next cell — i.e. `<= d0/2 = 22.5 Mpc` on TJB's own geometry.

## 5. The sharpest result — and it cuts against MULTING

| | |
|---|---|
| TJB's own node separation `d0` | 45.00 Mpc |
| implied node density `1/d0^3` | `1.10e-05 Mpc^-3` |
| MULTING `d_flip` | 92.67 Mpc |
| **`d_flip / d0`** | **2.06x** |

(Internal check: `Q(d0) = 2.059` and `d_flip/d0 = 2.06` are the same
number — `Q ~ 1/d` by construction. Consistent.)

> **MULTING's reversal sits at more than twice the model's own node
> separation.** At that distance a "representative pair" has other nodes
> between its members. `FINDING_P157` already established that v82
> evaluates **one representative pair**, not a population — so the
> single-pair construction the `d^-4`/`d^-5` competition is derived from
> **does not hold where its own reversal happens.**

The two reversals plausibly sit on opposite sides of `d0` — standard
compensation `<= 22.5 Mpc`, MULTING `~ 92.7 Mpc` — which would separate
them cleanly. But MULTING's lands in a regime its own construction does
not cover, so the separation cannot be claimed as a physical prediction.

## 6. Verdict

- Stage 3's **`CRITERION_INVALID` on the monotone test stands.**
- The **shape test is neither criterion-invalid nor valid**: the standard
  uncompensated response has no reversal (favourable), the compensated one
  has an `[UNKNOWN]` scale (undecided), and MULTING's own reversal is
  outside its own domain of validity (unfavourable).
- **The weakening now comes from MULTING's side, not the floor's.** That
  is a different situation from Stage 3 and should not be merged with it.

## 7. What this does NOT establish

1. Not that the compensated standard reversal is at 22.5 Mpc — that is
   `[INFERRED]` from a geometric argument, not computed or measured.
2. Not that MULTING is wrong. The single-pair limitation is a limit on
   **what this project can derive from the published construction**, not
   a defect claim (`NO_AUTHOR_ERROR`).
3. Not a full-text reading of either cited paper — abstracts only.
4. `d_flip` inherits everything Stage 1 section 6 already listed:
   conditional on one published fit, `beta`-blocked, `d`-as-free is an
   extension beyond the kernel.
