# FINDING P181 — joint (β1,β2,ε) re-optimization, a genuine 3D
# critical point, per the user's direct request

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (real numeric optimization of TJB's
own real chi2 — not a new physics claim)
**Continues/answers:** `FINDING_P177`'s "what this file does NOT
establish" §4 ("Does not attempt a genuine joint 3-parameter
re-optimization of `(β1,β2,ε)`... the only way to properly test
whether a real, practical `ε`-degeneracy exists near the true minimum")
and the user's direct request. `FINDING_P176` attempted a short version
and did not converge within a reasonable wall-clock budget.
**Script:** `P181_joint_3d_reoptimization.py` (numpy/scipy, 7 tests
incl. skeptic-requested checks, ruff clean, project test suite still
passes).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** MIXED — a genuine local minimum was
> found, but several of the first draft's convergence claims were
> shown to rest on numerically unreliable machinery and are downgraded
> (see Correction). The core finding survives on independent,
> derivative-free evidence.
> **Ontological/mechanistic interpretation status:** the found minimum
> is explicitly NOT physically meaningful (wildly unphysical
> parameters) — it is offered only as a demonstration of parameter
> degeneracy, not a competing physical fit.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing — this dispatch included the actual source code,
per the lesson from `FINDING_P180`'s prompt-construction error)

A skeptic review raised 7 attacks. Each independently checked before
accepting or rejecting.

**Confirmed by direct numerical check — finite-difference gradient/
Hessian at the solution point is unreliable.** Sweeping step size at
`x_sol` (where `|x1|~15`, `|ε|~7615`) from relative `1e-6` to `1e-2`
gave `|grad|` estimates ranging from `9.1e-3` to `3.4e12` with **no
stable plateau** — contrast `X0`, where the same sweep gives a stable
`9.6`–`10.4`. The first draft's "`|grad|` shrank 7 orders of magnitude"
and "solution is a stable fixed point under re-optimization" claims,
both computed with step sizes validated only at `X0`'s scale, are
**downgraded to unreliable diagnostics**, not trusted evidence. BFGS's
own reported `success=False` ("precision loss") corroborates this same
numerical problem surfacing mid-optimization — not something to wave
away as "same basin, so it doesn't matter."

**What survives, re-evidenced without unreliable finite differences:**
Nelder-Mead (derivative-free, immune to this problem) converges to
`χ²=14.168`, matching trust-exact's `χ²=14.169` to 3 significant
figures. A direct 1D line-scan along `v1` (pure function evaluations,
no derivatives) shows a clean, unambiguous U-shaped minimum around
`t=-7500` to `-8000` (`χ²` dips to `~14.23`, rises on both sides). These
two **independent, derivative-free** lines of evidence are what
actually support "a genuine local minimum exists here" — not the
gradient-based convergence certificates.

**Accepted — "shallow saddle" framing was geometrically imprecise.** A
saddle is a *critical point* (zero gradient) with mixed-sign Hessian
eigenvalues; `|grad(X0)|=10.4` means `X0` is not a critical point at
all. **Checked and corrected — the skeptic's own proposed mechanism
for this was checked directly and found wrong**: the large residual
gradient at `X0` is **not** "essentially `grad_ε` because `ε` is
unconstrained" (`grad_ε` is tiny, `-0.0078`) — it is dominated by
`grad_x1, grad_x2` (`7.76, -6.98`), consistent with `FINDING_P176`'s
own established finding that the `(β1,β2)` 2D Hessian at `ε=0` has
condition number `~8300`: a Nelder-Mead-style optimizer converging by
function-value tolerance on an ill-conditioned surface can appear
"converged" while leaving real residual gradient along the
near-degenerate direction *within* `(β1,β2)` itself, independent of
`ε`.

**Accepted, then checked — the full-3D alignment angle (`0.0003°`) is
influenced by `ε`'s dominant magnitude, but is NOT an artifact.** The
skeptic's own proposed test (project both vectors onto just the
`(x1,x2)` plane) was run directly: the projected angle is `0.044°` —
still remarkably tight, not "tens of degrees" as it would be if the
full-3D number were purely an artifact of one dominant component. The
three independently-implied "distance traveled" ratios (from `ε`,
`x1`, `x2` separately) agree to within `0.4%` of each other, confirming
genuine proportionality across all three coordinates. The skeptic's
specific claim that the alignment is "arithmetically forced by
normalization" is **refuted** by this check. A softer, valid point
survives: near a point with one small/negative eigenvalue, local
descent naturally favors that eigendirection initially — some of this
alignment is expected from `X0`'s own local geometry, not a fully
independent confirmation. What remains genuinely informative: the
direction stays this tight over a `~7615`-unit excursion, far beyond
any local quadratic approximation's validity radius.

**Added, per skeptic request:** a densified, ceiling-aware `+v1` scan
(40 points) confirms no missed secondary minimum — `χ²` increases
monotonically the entire range, hitting the unphysical `H²≤0` ceiling
around `t~100000`–`150000`.

**Added, not requested — an honest additional finding surfaced while
investigating the alignment attack:** Nelder-Mead's convergence to this
trough is **sensitive to which single coordinate of `X0` is perturbed**
before starting — a `1%` perturbation in `x1` alone converges back near
`X0` (`χ²~15.75`, does not find the trough); a `1%` perturbation in
`x2` or `ε` alone *does* find the trough (`χ²~14.17`). The trough is
real and found consistently from `X0` by 2 independent, reliable
methods, but is **not** a trivially-discoverable global feature
independent of starting point — an additional demonstration of the
severity of the ill-conditioning already established.

**Added — null-Δχ² context.** Going from 2 effectively-fit parameters
to a genuine 3-parameter fit adds one degree of freedom; a naive null
expectation for `χ²` reduction from one additional free parameter is
of order 1. The observed reduction (`15.75-14.17=1.58`) is about
`1.5×` this null expectation — modest, not a discovery-scale
improvement, especially set against a `~7615`-unit parameter excursion.

**Merged, per the skeptic's Attack 7:** "a genuine critical point was
found" and "it aligns with `v1`" are reported as **one finding with two
facets**, not two independently-confirming results.

## 0. Premise — `NO_AUTHOR_ERROR`

Every function and constant is TJB's own, reproduced verbatim; the
optimization and interpretation are this project's own numerical
investigation, not a claim about v82's own theory.

## 1. Method

Starting from TJB's own real reference point `(β1_0, β2_0, ε=0)` —
rescaled to `X0=(1,1,0)` — minimized the real `χ²` (same construction
as `FINDING_P177`–`P180`) jointly over all three parameters, at fixed
`H0,anchor=73.22` (TJB's "unconstrained_spotlighted" row). Positive
control: `χ²(X0)=15.75` matches TJB's own Table II value.

## 2. Results

```
Reliable (derivative-free) evidence:
  1D line-scan along v1: U-shaped, min ~14.23 near t=-7500 to -8000
  Nelder-Mead:            chi2=14.168 at x=(-14.9, -7.6, -7759)
  -> AGREE

Unreliable (gradient-based) diagnostics:
  |grad| at x_sol across step-size sweep: 2.4e-4, 1.6e-2, 1.6, 164
  -> no stable plateau; trust-exact/BFGS certificates NOT trusted

Alignment with established v1 (from Nelder-Mead's x_sol):
  Full 3D angle:            0.00030 deg
  (x1,x2)-projected angle:  0.04375 deg

+v1 direction: no improvement anywhere in dense scan; hits H^2<=0
  ceiling around t~100000-150000 (asymmetric trough, confirmed)

Nelder-Mead basin sensitivity: perturbing X0 by 1% in x1 alone does
  NOT find the trough (chi2~15.75); perturbing x2 or eps alone DOES
  (chi2~14.17)
```

## 3. Verdict

**One finding, two facets, both real:** a genuine local minimum exists
at approximately `(β1≈-14.9×β1_fit, β2≈-7.6×β2_fit, ε≈-7759)`,
established by two independent derivative-free methods (Nelder-Mead,
line-scan) — not by the originally-cited gradient/Hessian-based
convergence certificates, which are numerically unreliable at this
parameter scale. Its direction from `X0` matches the already-established
near-null eigenvector `v1` tightly, even after removing `ε`'s dominant
magnitude (`0.044°` projected) — though this alignment is partly
expected from `X0`'s own local geometry, not a fully independent
confirmation. The `χ²` improvement (`10%`, `~1.5×` the null expectation
for one added parameter) despite an enormous parameter excursion is a
concrete, real-optimization demonstration of the severity of the
rank-deficiency/ill-conditioning already established in
`FINDING_P133`/`P176` — though the trough is not trivially/robustly
discoverable from arbitrarily nearby starting points (Nelder-Mead
basin-sensitivity finding).

## 4. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Not a claim of a better physical fit** — the found parameters
   (`β1≈-14.9×`, `β2≈-7.6×`, `ε≈-7759`) are wildly unphysical relative
   to TJB's own real model.
3. **Full 3D positive-definiteness of the Hessian at the solution is
   NOT certified** — the finite-difference machinery is demonstrably
   unreliable at this scale; reliance is on derivative-free convergence
   instead (§ Correction).
4. **Does not establish the trough is a robust, globally-discoverable
   feature** — Nelder-Mead's basin sensitivity to which coordinate is
   perturbed first shows the opposite.
5. **Does not resolve `FINDING_P177`'s open question** (genuine
   correspondence vs. Taylor-truncation leverage) — this file addresses
   a different question (does a genuine 3D critical point exist away
   from `ε=0`), not that one.
6. **Does not attempt the same joint re-optimization for the low-z/
   high-z subsamples** — scope limited to the full 33-point sample,
   TJB's primary reported target.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
