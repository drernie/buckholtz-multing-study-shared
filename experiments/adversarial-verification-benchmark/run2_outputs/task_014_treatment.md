# Task 014 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 014 (Optimizer bounds reused from a different problem instance)

### 1. Falsifiable claim in the report

> "The optimizer converged to x* = 5.0 cm... this is a valid result reflecting the genuine cost-minimizing thickness for this smaller, cooler pipe design," cost model `total_cost(x) = 12.0*x + 340.0/(x+1)`.

### 2. Positive / negative control

**Neither is supplied.** The report offers only `result.success == True` and "no error, no warning" as evidence.

### 3. Specific failure modes found

- **Silently-fixed parameter:** `bounds=(5.0, 45.0)` copied verbatim from a structurally different prior problem, never re-derived.
- **Boundary-solution blindness in the tool itself:** `minimize_scalar(method='bounded')` sets `success=True` identically whether the optimum is interior or truncated.
- **Self-contradiction:** the code's own comment predicts "a few cm, not tens of cm" — correct — but never checks whether that falls below the reused 5 cm floor.

### 4. Executed check

| Setup | x* | cost | success |
|---|---|---|---|
| Analytic unconstrained optimum | 4.32290 | 115.7498 | -- |
| As-reported (bounds (5.0, 45.0)) | 5.00000 | 116.6667 | True |
| Corrected bounds (0.01, 45.0) | 4.32290 | 115.7498 | True |

Boundary-sensitivity sweep:
```
bounds=(5,45)    -> x*=5.0000  success=True  AT_LOWER_BOUND=True   <- as reported
bounds=(0.01,45) -> x*=4.3229  success=True  AT_LOWER_BOUND=False
bounds=(4.5,45)  -> x*=4.5000  success=True  AT_LOWER_BOUND=True   <- artificial 2nd boundary hit
```

`success=True` fires identically whether the lower bound truncates the true optimum or not.

### 5. Verdict

**FALSIFIED.** The claim "x* = 5.0 cm is the genuine cost-minimizing thickness" does not hold — boundary artifact from reused search bounds.

Kill analysis — killed: the specific numeric conclusion (5.0 cm) and the general inference rule "optimizer returned success with no warning => trust the number." Not killed: the cost-function formula, minimize_scalar's correctness. Fix: re-derive bounds per problem instance, add explicit boundary-hit check as a standing guard.

---

### DRAFT CLAIM (self-contained, for blind handoff)

A `scipy.optimize.minimize_scalar(method='bounded')` call minimizing `total_cost(x) = 12.0*x + 340.0/(x+1)` over `x in [5.0, 45.0]` returned `x* ~= 5.0` with `success=True`, reported as "the genuine cost-minimizing thickness." The bounds `[5.0, 45.0]` were carried over unmodified from a different, larger-scale prior optimization and never re-derived. Recomputing the unconstrained analytic minimum (`x=sqrt(340/12)-1~=4.323`) and re-running with appropriate bounds both converge to x*~=4.323, differing from the reported x*=5.0 by ~16% in thickness. A bound-sensitivity sweep shows `success=True` is returned identically regardless of whether the lower bound truncates the true optimum, so "no error/warning, converged" is not evidence the box constraint is real rather than accidental. The reported x*=5.0 cm is a boundary artifact of stale search bounds, not a genuine optimum.
