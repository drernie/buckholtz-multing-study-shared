# Task 012 — treatment arm output (FL protocol)

## Falsification-Ladder Standard-Ladder Review — Task 012 (K_eq two-route cross-check)

### 1. Falsifiable claim being made

> "The exact numerical agreement between Route 1 (thermodynamic, `K_eq = exp(-ΔG/RT)`) and Route 2 (kinetic, `K_eq = k_forward/k_reverse`) constitutes independent confirmation of the measured `K_eq = 28.92`, validating both the free-energy measurement and the rate-constant framework."

This is checkable: if Route 2 is truly independent of Route 1, the two should be able to disagree given different (even synthetic) inputs, and Route 2's own free parameter (`k_forward`) should matter to the output.

### 2. Positive / negative controls

**None supplied.** No positive control (e.g., an ester with an independently, directly measured `k_reverse` where the two routes are known to converge for a real reason) and no negative control (e.g., a case engineered to make the two routes disagree, to show the comparison has power to fail). The report treats "the numbers matched" as self-validating, which is exactly the gap controls exist to close.

### 3. Specific defect found: circular/tautological validation

Route 2 is defined as `k_reverse = k_forward * exp(dG/RT)`, then `K_eq = k_forward / k_reverse`. Substituting:

```
K_eq_route2 = k_forward / (k_forward * exp(dG/RT)) = exp(-dG/RT) = K_eq_route1
```

`k_forward` cancels out of the formula identically — it never enters the final answer. Route 2 is not a second measurement; it is Route 1 rewritten in kinetic vocabulary, dressed up with a "measured" `k_forward` that is present in the code but does no work. This is the classic estimator-driven circularity: `dG` is used to manufacture the very quantity (`k_reverse`) that is then presented as confirming `dG`. There is no target leakage or silently-fixed nuisance parameter beyond this — the whole "cross-check" reduces to computing the same expression twice.

### 4. Executable checks (run, not described)

Ran `check_keq.py` (numpy + sympy) with six checks:

1. **Reproduction** — confirms the reported numbers: both routes give `28.919187`, diff `= 0.0` exactly (not "close," bit-for-bit identical).
2. **Symbolic simplification** (`sympy.simplify(k_f/kr_s)`) — proves `K_eq_route2` reduces algebraically to `exp(-dG/(R*T))`, with `k_f` cancelling completely and symbolically, not just for this numeric input.
3. **Ablation on `k_forward`** — swept `k_forward` over 4.2e-6 to 4.2e0 (6 orders of magnitude): `K_eq_route2` stayed at `28.919187` in every case. The "measured" rate constant carries zero information into the output.
4. **Sweep on `dG`** — varied `dG` over a wide range (-20000 to +5000 J/mol) and compared the two routes: correlation `r = 1.000000000000000`, slope `= 1.000000000000000`, max absolute difference `= 2.8e-14` (floating-point noise floor). Perfect agreement holds everywhere in the space, not just at the reported point — the signature of an identity, not of two measurements that happen to coincide.
5. **What a real negative control would need** — a genuinely independent Route 2 requires `k_reverse` from data `dG` was never used to produce.
6. **Synthetic negative-control simulation** — reran Route 2 with `k_reverse` perturbed by realistic 5% measurement noise (independent of the `dG`-derived value) across 8 trials: `K_eq_route2` scattered from 27.6 to 32.0, deviating from Route 1's 28.919 by up to ±3.1. This shows what an actually independent comparison would look like — and that the reported "exact" `0.000000` agreement is diagnostic of circularity, not of validation.

All checks were executed successfully; output confirms the algebraic argument numerically and shows the effect holds globally, not just at the reported operating point.

### 5. Verdict

**REJECT** — the "independent kinetic cross-check" is not independent. It is Route 1 restated through a substitution that makes the input parameter (`k_forward`) mathematically inert. The report's own admission — "we didn't have independent kinetic reverse-rate data... so we backed it out this way" — already discloses the circularity; the analysis then treats the resulting tautological match as if it were evidence. The `dG = -8.34 kJ/mol` measurement is not corroborated by anything in this report. What is actually validated is only that the code correctly implements `exp(-dG/RT)` twice and that `y/(y*c) = 1/c` in floating point — a true but scientifically empty fact.

**Kill Analysis:**
- **Killed:** the claim that "two routes converge precisely" constitutes independent confirmation of `K_eq` or of `dG`.
- **NOT killed:** the underlying `dG = -8.34 kJ/mol` measurement itself may well be correct — this review offers no evidence against it, only against the claim that Route 2 corroborates it.
- **What would fix it:** obtain `k_reverse` from an actual independent kinetic experiment (rate of the reverse esterification/hydrolysis under controlled conditions), not derived algebraically from `dG`. Only then would agreement (or its absence, within combined experimental error bars) carry evidential weight.

---

### DRAFT CLAIM (for blind independent-reviewer handoff)

A lab report computes an esterification reaction's equilibrium constant two ways and presents their exact numerical agreement (`K_eq = 28.92` both times) as independent cross-validation. Route 1 computes `K_eq = exp(-ΔG/RT)` from a measured Gibbs free energy. Route 2 computes `K_eq = k_forward / k_reverse`, but `k_reverse` was not independently measured — it was itself derived by rearranging the same thermodynamic equation using the identical `ΔG` value, i.e. `k_reverse = k_forward * exp(ΔG/RT)`. Algebraic substitution shows `k_forward` cancels exactly out of Route 2's formula, so Route 2 reduces identically to Route 1's expression regardless of what `k_forward` is; this was confirmed both symbolically (sympy) and numerically by varying `k_forward` over six orders of magnitude with no change in the output, and by sweeping `ΔG` over a wide range where the two routes tracked with correlation `r = 1.0` and slope `1.0` to machine precision. Claim to evaluate: does this two-route agreement provide independent evidence for the reported `K_eq`/`ΔG`? Verdict to reach: no — it is a tautological restatement of one input, not a cross-check, since Route 2 has no degree of freedom capable of disagreeing with Route 1; a synthetic simulation with genuinely independent (noisy) `k_reverse` shows the routes would scatter by several units if truly independent, which they do not.
