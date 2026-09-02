# Task 029 — baseline arm output

## Findings

**Verification performed:** ran the exact script. Q_total = 1,638,594.08 m^3 (report's "1,638,600" is a round, not the script's literal own output — trivial provenance inconsistency). quad error estimate matches exactly: 6.678e-3 m^3, relative 4.08e-9.

**Core flaw: precision (numerical) conflated with accuracy (physical/model).** quad's abserr bounds only how well the algorithm integrated the GIVEN function — says nothing about whether the two-Gaussian model with hand-set peak/center/width correctly represents real inflow.

**Quantified the gap via sensitivity check:**
| Perturbation | Resulting Q_total | Delta |
|---|---|---|
| baseline | 1,638,594 | -- |
| +/-10% on peak params (routine gauge uncertainty) | 1,474,735 / 1,802,453 | ~164,000 m^3 |
| +/-20% | 1,310,875 / 1,966,313 | ~328,000 m^3 |

A plausible +/-10% parameter uncertainty moves the total ~164,000 m^3 -- roughly 24.5 MILLION times larger than quad's own quoted error (6.7e-3 m^3). The report emphasizes the astronomically negligible uncertainty source and is silent on the dominant one.

**Secondary flaw (Gate 2, target provenance):** "individually validated against historical gauge data" is asserted with no citation/data shown. If parameters were chosen with an eye toward matching the historical seasonal total, the reported "match" is circular, not confirmatory -- report gives no info to rule this out.

**Minor:** truncated window [0,120] discards ~0.96% of pulse mass (tails) -- two orders of magnitude smaller than the parameter-uncertainty effect, not the main issue.

---

**DRAFT CLAIM:** The report computes Q_total~1.64M m^3 via quad and argues reliability from quad's tiny error estimate. Reproduction confirms the integral and error are numerically correct. However, the central inferential move is invalid: quad's error characterizes integration accuracy of the GIVEN function, not whether that function correctly represents real inflow -- a category error between numerical precision and physical accuracy. A sensitivity check (+/-10% on peak parameters, plausible gauge uncertainty) shifts the total by ~164,000 m^3, ~24.5 million times larger than the quoted numerical error. The "individually validated against historical gauge data" claim is unsupported by any citation, and since the total is then claimed to match the same catchment's historical range, there's unresolved risk the parameters were tuned toward that target. Verdict: the report's stated justification for "reliable" does not support that conclusion -- it authenticates numerical convergence while leaving the actually load-bearing uncertainty source (model/parameters) completely unexamined.
