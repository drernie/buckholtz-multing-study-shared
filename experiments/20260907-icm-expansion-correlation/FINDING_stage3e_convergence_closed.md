# FINDING — Stage 3e: convergence swept, oracle anchored, integrator
# cross-checked. Status → `C4-NUMERICALLY-CLOSED-WITHIN-THIS-LINEAR-FAMILY`

**Date:** 2026-09-07
**Artifact:** `stage3e_convergence_and_oracle.py`
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Closes:** the last open item of `AMENDMENTS_after_step8a_skeptic.md`.

---

## 1. Three criticisms, three answers

### A. The transcription claim was too strong — WITHDRAWN

`stage3d` said *"14 alternating signs is not a transcription accident."*
**Too strong.** A typo can preserve oscillatory character while corrupting
phase, acoustic scale, damping, or the baryon/CDM amplitude ratio. Honest
status of the internal controls: **"not obviously broken"**, not *"proven
correct"*. Proving it needs CLASS/CAMB, unavailable here.

What is available — a **partial** external anchor, EH98's own derived
quantities against published cosmology:

| quantity | computed | published | deviation |
|---|---|---|---|
| `z_eq` | 3445.408 | ~3400 | **+1.34%** |
| `z_d` | 1020.781 | ~1060 | **−3.70%** |
| `s` (sound horizon) | **150.865 Mpc** | `r_d ≈ 147.1` | **+2.56%** |
| `k_eq` | 0.01048 Mpc⁻¹ | — | — |

The `+2.56%` on `s` is **the known systematic of the EH98 fitting
formula** (documented ~2–3% high vs the exact integral). A deviation of
the right sign and size is stronger evidence of correct transcription than
an exact hit would be — an exact hit on a fitting formula would suggest
two errors cancelling.

**Explicitly NOT verified by this anchor:** `α_c`, `β_c`, `α_b`, `β_b`,
`β_node`, the Silk term.

### B. W1/W2 were only partially independent — separate integrator added

Criticism accepted: `stage3d`'s two routes differ in the **wiggle model**
but share `P(k) → ξ(r) → δ̄(r) → sign counter`. Their agreement therefore
tested the wiggle physics, **not the integrator**.

`ξ(r)` recomputed by a structurally different method — **linear grid +
Simpson** on `k·P(k)·sin(kr)/r`, instead of **log grid + trapezoid** on
`P·k²·sinc` — on a different `k`-range as well:

| r [Mpc/h] | log-trapezoid | linear-Simpson | rel. diff | sign |
|---|---|---|---|---|
| 10 | +3.496929e-01 | +3.495923e-01 | 2.88e-04 | OK |
| 50 | +7.037092e-03 | +7.041409e-03 | 6.14e-04 | OK |
| 100 | +1.630788e-03 | +1.630099e-03 | 4.22e-04 | OK |
| **150** | **−2.569872e-04** | **−2.569256e-04** | 2.40e-04 | OK |
| 200 | −1.485744e-04 | −1.484638e-04 | 7.44e-04 | OK |

Worst relative difference **7.4e-04**, across four orders of magnitude in
`ξ` and **on both sides of the zero crossing**.

### C. The convergence sweep — the item `stage3c` promised and never ran

**Kill criterion, written into the docstring BEFORE the run:** if a
reasonable refinement changes the **crossing count**, the branch is NOT
closed; if only `R_xi0` moves, it is.

**WIGGLE (W1), 13 configs:**

```
        config  #sign(xi)  #sign(db)   R_xi0[Mpc]   R_comp
      BASELINE          1          0        172.8     NONE
     kmin x0.1          1          0        172.8     NONE
      kmin x10          1          0        172.8     NONE
     kmax x0.5          1          0        172.8     NONE
       kmax x2          1          0        172.8     NONE
     nk   x0.5          1          0        172.8     NONE
       nk   x2          1          0        172.8     NONE
     rmax x0.5          1          0        172.8     NONE
       rmax x2          1          0        172.8     NONE
     n_r  x0.5          1          0        172.8     NONE
       n_r  x2          1          0        172.8     NONE
  WORST coarse          1          0        172.8     NONE
    WORST fine          1          0        172.8     NONE

  distinct (n_xi, n_db): [(1, 0)]      COUNT STABLE: True
```

**SMOOTH:** identical structure, `R_xi0 = 180.2` in all 13,
`distinct: [(1, 0)]`, `COUNT STABLE: True`.

**26 of 26 points give `(1, 0)` and `R_comp = NONE`.**

---

## 2. VALIDATION CONTROL — the destructive mutation test

**Read this before concluding anything from §1C.** `R_xi0` did not move by
a single digit across 26 configurations. That is *suspiciously* clean —
the external review had predicted small movement. Perfect stability has an
obvious alternative explanation: **the swept parameters never reach the
computation.**

So they were deliberately broken:

| config | `R_xi0` [Mpc] | **#sign(ξ)** |
|---|---|---|
| **baseline** | **172.8008** | **1** |
| `kmax=0.5` (truncates power) | 110.8817 | **51** |
| `kmax=0.05` (severe) | 144.8264 | **5** |
| `kmin=0.02` (kills large scale) | 95.7002 | **3** |
| `nk=300` (absurdly coarse) | 72.8082 | **147** |
| `nk=2000` (coarse) | 169.9060 | **279** |
| `rmax=120` (just past the zero) | 172.7941 | 1 |

**The parameters are wired, and violently so.** Break them and the count
explodes to 279. The sweep's stability is therefore *convergence*, not
*dead plumbing*.

**Two secondary observations worth keeping:**

1. **The crossing count is far more fragile than `R_xi0` under
   under-resolution.** At `nk=2000` the count is 279 while `R_xi0 = 169.9`
   is still within 2% of the truth. The quantity C4 rests on is the one
   that breaks *first* on a bad grid — which is precisely why its
   stability in the converged regime carries information.
2. **`rmax=120` barely perturbs anything** (172.7941 vs 172.8008) because
   the zero at ~116.5 Mpc/h still sits inside that window. Consistent.

**Do not, at a later reading, interpret §1C's uniformity as a dead
parameter. It was tested. This section is the test.**

---

## 3. Status

**`C4-NUMERICALLY-CLOSED-WITHIN-THIS-LINEAR-FAMILY`.**

Within linear ΛCDM with smooth and BAO transfer functions:
`ξ(r)` has exactly one sign change, and `δ̄(r)` does not cross zero at any
finite `r`. Survived: smooth spectra · full EH98 wiggles · independent BAO
template · BAO to ~19× realistic amplitude · `kmin` · `kmax` · `nk` ·
`rmax` · radial resolution · coarse/fine combinations · deliberate
destructive mutation.

## 4. What this does NOT do — and this is the point

**It does not revive Ernest's test.** The comparator stopped being the
bottleneck several stages ago:

```
standard model : no flip   (Stage 3c/3d/3e, now numerically closed)
current MULTING: no flip   (Stage 4: Q(z) > 1 globally)
```

A perfect standard comparator cannot create a discriminating test when
neither side has the feature. **This branch was a repair of C4's proof,
not a rescue of the physical test.**

## 5. Three caveats, of different kinds

1. **Conditional on the published fit.** Everything about the negative
   thermal response is at the published `β₂/β₁`. Touching `Q = 1` needs
   that ratio ~1.75× smaller. A claim about *all admissible fits* would
   need a separate sweep over the fit valley — not required for the
   standing `REFUSE`.
2. **Acceleration ≠ local Hubble rate.** Established:
   `∂(ä/a)/∂k < 0`. **Not** established: `∂H_local/∂E_th < 0`. That needs
   a dynamical bridge `δ(ä/a) → δH_local(t)` which does not exist. Until
   it does, Ernest's observational claim cannot honestly be issued as a
   prediction of current v82.
3. **C4 is not a theorem about non-linear ΛCDM.** A specific linear family
   was closed. Real halo environments, non-linear bias, exclusion and
   selection are wider — and there is no practical reason to go there,
   because the MULTING-side flip is already absent.

## 6. Branch verdict, unchanged

`claim.md`'s **`REFUSE(no_falsifiable_predicate_yet)` stands.** The whole
ICM–local-expansion thread remains REFUSE.

**Strongest surviving physics statement:** *at the published fit the
thermal-source response of pair fractional acceleration is negative; the
corresponding observable prediction for `H_local` has not been derived.*

**This branch is stopped here.** What remains are new, separate research
questions, not further arithmetic on this one.
