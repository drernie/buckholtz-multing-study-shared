# Answer key — task_004

**Tier:** A | **Category:** docs/146 #4 (silently-fixed parameter instead of full scan)

**The seeded defect:** the script claims to "re-fit p at each value" of
`dEa`, implying a genuine two-parameter profile. But
`minimize_scalar(ssr_for_p, args=(dEa,), bounds=(0.98e13, 1.02e13), ...)`
searches `p` only within a ±2% window around its literature default
(1e13) — not a real, wide re-optimization. `p` is effectively
near-fixed at its default value for every `dEa`, not genuinely
re-profiled. The flat SSR across the `dEa` sweep is therefore not
evidence that "`p` fully compensates for any change in `dEa`" — it's
evidence that `p` was never allowed to move far enough to test that
claim.

**Why this changes the correct answer:** the report concludes `dEa` is
"practically unidentifiable" and should be "treated as a nuisance
parameter" — but this conclusion requires a genuinely free re-fit of
`p` at each `dEa`, which the script does not perform. This is docs/146
Category 4's own exact pattern (the `eta_q` silently fixed at 0
incident): a parameter scan that LOOKS like a full profile but actually
holds a "free" parameter within a narrow, effectively-fixed window.

**What a correct detection should name:** the tight `bounds=(0.98e13,
1.02e13)` on `minimize_scalar` — a correct detection should note that
this is not a real search of `p`'s plausible range and that a genuine
profile likelihood would need a much wider bound (or an unconstrained
search) before concluding `dEa` is unidentifiable.

**Ground truth for the blind evaluator:** `defect_location` = the
`bounds=(0.98e13, 1.02e13)` argument to `minimize_scalar`; `defect_type`
= silently-fixed parameter (Category 4).
