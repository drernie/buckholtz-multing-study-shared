# Task 018 — baseline arm output

## Findings

**Verdict: not well-supported, and not even reproducible.**

1. g(x) is a sum of two squares, so g(x)>=0 everywhere (roots at 3 and 1 differ, cannot both vanish at once). By FTC, G(x) is monotonically non-decreasing, G(0)=0, so G(x)>=0 for all x>=0 by definition — a negative value is mathematically excluded, like a probability outside [0,1].
2. Root cause: float64 overflow, not an asymptotic phenomenon. Closed form G(x)=(1.1/3)x^3-3.1x^2+9.1x; at x=1e205 this is ~3.67e614, ~306 orders of magnitude past float64 max (~1.8e308). g(x) itself overflows once x gtrsim 1.34e154 (sqrt(float64_max)).
3. Ran the exact script unmodified: `OverflowError` raised before quad can even run — the reported -3.2e188 could not have been produced by this script in a standard current environment (scipy 1.16.3/numpy 2.3.4). A numpy-scalar variant that overflows silently instead returns `+inf`, not a spurious negative number.
4. Positive-control sweep of xmax from 1 to 1e102 (below float64-max^(1/3)) shows quad tracking the analytic integral to ~1e-16 relative error throughout — quad itself is trustworthy in-range; the failure is purely from testing ~100+ orders of magnitude past representability.

---

**DRAFT CLAIM:** The reported G(1e205)=-3.2e188 for the manifestly non-negative integrand g(x)=(x-3)^2+0.1(x-1)^2 is mathematically impossible — G is non-decreasing from G(0)=0, so G(x)>=0 for all x>=0 by definition. The true value (~3.7e614) exceeds float64 max by 300+ orders of magnitude, so the floating-point-correct answer is +inf. Running the exact script raises OverflowError and never returns the claimed number at all in a current environment; a numpy variant avoiding the crash correctly returns +inf. Separately, sweeping quad over xmax from 1 to 1e102 confirms the integrator is accurate to ~1e-16 in-range — the failure is a pure overflow artifact compounded by non-reproducibility, not a physical/asymptotic finding.
