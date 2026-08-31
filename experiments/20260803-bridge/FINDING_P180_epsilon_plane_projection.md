# FINDING P180 — comparing FINDING_P165's predicted direction to the
# FULL 2D near-degenerate plane, not just one eigenvector, per the
# user's explicit request and FINDING_P178's own named gap

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (geometric decomposition of an
already-computed real fit quantity — not a new physics claim)
**Continues/answers:** `FINDING_P178`'s "what this file does NOT
establish" §2.4 ("comparing `FINDING_P165`'s predicted direction to
the near-degenerate plane the small eigenvalues span, not to one
arbitrary vector picked from within it"), and the user's direct
request to try exactly this.
**Script:** `P180_epsilon_plane_projection.py` (numpy/scipy, 5 tests
incl. 2 skeptic-requested checks, ruff clean, project test suite still
passes).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** the geometric decomposition is exact (an
> orthonormal eigenbasis, no approximation) and positive-controlled
> against `FINDING_P177`/`P178`/`P179`'s own already-verified angles.
> One of the two originally-claimed findings is RETRACTED (see
> Correction); one survives.
> **Ontological/mechanistic interpretation status:** OPEN, unchanged
> from `FINDING_P177` — genuine correspondence vs. Taylor-truncation
> leverage remains unresolved.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing)

**Process note:** the skeptic dispatch for this file's first draft had
a prompt-construction error on this project's side — the actual source
code was accidentally omitted and replaced with a placeholder, so the
review worked from the claim and the reported numbers only, not the
code. Despite this, the review's central mathematical critique did not
depend on the code at all — it was a pure geometric argument, and it
was correct. This is recorded here because it is itself informative
about the protocol: a genuinely well-posed adversarial critique can be
constructed and verified purely from a claim's own reported numbers,
without needing the implementation.

**Retracted in full:** the first draft's claim that a separately-computed
"mixing_angle" (how far `V_PRED`'s projection onto the flat `(v1,v2)`
plane sits from the `v1` axis versus the `v2` axis) provided evidence,
independent of `angle_to_plane`, that `V_PRED` is "specific to `v1`,
not generic anywhere in the plane." **Independently re-derived and
numerically verified**: for the orthogonal decomposition
`V_PRED = a1·v1 + a2·v2 + a3·v3`, the three angles satisfy the
**exact** spherical-right-triangle identity
`cos(full_angle) = cos(angle_to_plane) · cos(mixing_angle)` — not
merely a small-angle approximation. Checked directly:
`sqrt(angle_to_plane² + mixing_angle²)` matches `full_angle` to
`~10⁻¹¹` degrees (floating-point noise) in all three samples. This
means `mixing_angle` is **exactly** determined by `full_angle` and
`angle_to_plane` — it is not a second, corroborating measurement, and
presenting it as separate evidence double-counts one geometric fact in
two coordinate systems. The "specific to `v1` vs. generic in-plane"
interpretation built on it is dropped.

**Checked and addressed — λ1/λ2 for the actual base samples.** The
skeptic (working blind, without the code) correctly noted the claim's
soundness depends on whether `λ1` and `λ2` are themselves well
separated for the samples this file uses — `FINDING_P179` only checked
this for the 7-point leave-one-out variants, not the 8-point/33-point
base samples `P180` actually decomposes `V_PRED` against. **Checked
directly, added as a formal test**: `λ1/λ2` is `~1.6×10⁻⁸` (full),
`~5.6×10⁻⁹` (low-z), `~1.2×10⁻⁸` (high-z) — well separated in all
three. `v1` is not an arbitrary pick within a near-degenerate pair here
either.

**Accepted as an honest caveat, not previously stated explicitly:**
`V_PRED`'s coordinate *normalization* uses the fitted `β1_0, β2_0` (to
express it in the same rescaled coordinates the Hessian is computed
in), even though its underlying constant `C_IDEALIZED_LOCAL`
(`FINDING_P175`) comes from independent `z=0` baseline quantities, not
from `β1`/`β2` fitting. `V_PRED` was never claimed to be *fully*
unrelated to the real fit, but this file's earlier framing did not say
so explicitly; it does now.

**Accepted as an honest caveat:** no rigorous statistical null
distribution is offered for "how surprising" a given `angle_to_plane`
value is. The comparison here is descriptive (`angle_to_plane` relative
to the already-known `full_angle`), not a calibrated significance test.

**Net result:** the file's ONE genuinely new, non-redundant finding
survives: `angle_to_plane` — how much of `V_PRED` points into the
stiff (well-constrained) `v3` direction versus staying within the flat,
poorly-constrained `(v1,v2)` plane. `mixing_angle` is retained in the
output only as an exact-identity sanity check on the code, not as
independent evidence.

## 0. Premise — `NO_AUTHOR_ERROR`

Every function and constant is TJB's own, reproduced verbatim; the
decomposition and comparison are this project's own geometric analysis
of an already-computed real quantity, not a claim about v82's own
theory.

## 1. Method

For each of three real chi2 Hessians (full 33-point sample, low-z 8pt
subsample, high-z 8pt subsample — same construction as
`FINDING_P177`/`P178`/`P179`), decompose `V_PRED` (`FINDING_P165`'s
idealized-mechanism prediction) exactly in the orthonormal eigenbasis
`(v1, v2, v3)`:

```
V_PRED = a1*v1 + a2*v2 + a3*v3     (exact, since {v1,v2,v3} orthonormal)

angle_to_plane = arcsin(|a3| / |V_PRED|)     -- deviation into the stiff v3 direction
mixing_angle   = arctan2(|a2|, |a1|)         -- in-plane position (NOT independent, see Correction)
```

## 2. Results

```
FULL-33pt:  eigvals=[-1.14e-6, 70.6, 5.88e5]   lambda1/lambda2=1.61e-08
  full_angle(V_PRED,v1)=0.01723 deg   angle_to_plane=0.00082 deg   (~4.8% of full)

LOW-z:      eigvals=[-8.87e-11, 0.0157, 1.01e4]  lambda1/lambda2=5.63e-09
  full_angle(V_PRED,v1)=0.00624 deg   angle_to_plane=0.00006 deg   (~1.0% of full)

HIGH-z:     eigvals=[-2.20e-8, 1.838, 5.29e5]   lambda1/lambda2=1.20e-08
  full_angle(V_PRED,v1)=0.01946 deg   angle_to_plane=0.00088 deg   (~4.5% of full)
```

`angle_to_plane` is 20–100× smaller than `full_angle` in all three
samples — `V_PRED`'s already-tiny deviation from `v1` lies almost
entirely within the flat `(v1,v2)` subspace, essentially none of it
points toward the stiff, well-constrained `v3` direction. `λ1/λ2` is
`8`–`9` orders of magnitude below 1 in all three base samples,
confirming `v1` is a well-isolated, non-arbitrary direction to compare
against in the first place. The exact spherical identity
`cos(full)=cos(plane)·cos(mixing)` is verified to hold to `~10⁻¹¹`
degrees.

## 3. Verdict

1. **RETRACTED**: `mixing_angle` as independent evidence of
   "specificity to `v1` over `v2`." It is exactly determined by
   `full_angle` and `angle_to_plane`; presenting it as a second,
   corroborating measurement double-counted one geometric fact.
2. **SUPPORTED**: `V_PRED`'s tiny deviation from `v1` sits almost
   entirely in the direction the real 33-point data barely constrains
   at all (the flat `(v1,v2)` plane), not in the direction the data
   measures well (`v3`) — a genuine, exact, non-redundant geometric
   fact about the real fit surface, verified across all three samples.
3. **SUPPORTED (addressed gap)**: `v1` is confirmed well-isolated from
   `v2` (`λ1/λ2 ~10⁻⁸`–`10⁻⁹`) in the actual base samples this file
   uses, not just in `FINDING_P179`'s leave-one-out variants.

**What this means for the open question**: `FINDING_P177`'s original
question (genuine physical correspondence vs. Taylor-truncation
leverage) remains **unresolved**. This file adds one honest, narrow
geometric fact — the disagreement between `V_PRED` and `v1` lives in
the data's blind spot, not its strength — without resolving what that
fact ultimately means.

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not resolve `FINDING_P177`'s open question** — genuine
   correspondence vs. Taylor-truncation leverage remains unresolved.
3. **`mixing_angle` is not independent evidence** — see Correction;
   kept in the output only as a code-correctness sanity check.
4. **No rigorous statistical null/significance test** is offered for
   `angle_to_plane`'s smallness — the comparison is descriptive
   (relative to `full_angle`), not a calibrated p-value.
5. **`V_PRED` is not claimed to be fully independent of the real fit**
   — its coordinate normalization uses the fitted `β1_0, β2_0`, even
   though its underlying constant comes from independent `z=0`
   baseline quantities (`FINDING_P175`).
6. **Does not attempt a genuine joint 3-parameter re-optimization** of
   `(β1,β2,ε)` — inherited limitation from `FINDING_P177`, unchanged.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
