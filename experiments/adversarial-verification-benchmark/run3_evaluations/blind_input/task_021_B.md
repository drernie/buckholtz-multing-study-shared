# Task 021 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 021

### 1. Falsifiable claim
"This pipeline correctly handles the range of inputs it will encounter in production" (implicit behind "robust and production-ready").

### 2. Controls
Positive control weak-to-absent (no independently-verified expected output). Negative control absent entirely — no deliberately-bad input tested.

### 3. Failure modes found
- Silent assumption never stated: every customer has >=1 recent score.
- "0 exceptions on real data" conflated with general robustness — only certifies THIS day's data draw had no edge cases.
- Silent-corruption blind spot: NaN in scores does NOT raise an exception, silently returns NaN as the summary — worse than a crash, since "0 exceptions" would report the same success message even with corrupted output.

### 4. Executed checks
- Empty list: `ZeroDivisionError`, confirmed by execution.
- NaN probe: returns nan, no exception.
- Synthetic 12,406-customer population with realistic ~0.5% dormant-customer rate (61 zero-transaction customers): crashed with the identical ZeroDivisionError — proving "0 exceptions on the real run" was a property of that day's data, not evidence of tolerance to the full input space.

### 5. Verdict
**FALSIFIED / REJECT** for "robust and production-ready" as stated. Two concrete, demonstrated failure modes, neither hypothetical.

---

### DRAFT CLAIM
A batch scoring pipeline computes sum(scores)/len(scores) per customer, ran once against 12,406 real customers with zero exceptions, and the report concludes "robust and production-ready." Independent execution shows two failure modes the single run never exercised: any customer with zero recent scores causes an unhandled ZeroDivisionError (reproduced directly and in a synthetic population with a realistic ~0.5% dormant-customer rate); and a NaN value anywhere in a customer's scores is silently averaged into a NaN output with no exception, meaning "0 exceptions" cannot distinguish a healthy run from one with silently corrupted rows. No positive or negative control was present in the original validation. Reviewer should confirm by running daily_summary_score([]) and daily_summary_score([0.2,0.5,nan,0.3]) against the actual source before accepting "production-ready."
