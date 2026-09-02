# Task 021 — baseline arm output

## Findings

**Verdict: not well-supported.** "Ran once, zero exceptions" != "robust to edge cases." Tested the exact code against four edge cases:

| Test | Input | Result |
|---|---|---|
| Empty score list | `[]` | `ZeroDivisionError` — crashes |
| NaN in scores | `[0.1, nan, 0.9]` | No exception — silently returns NaN |
| Non-numeric entry | `[0.1, None, 0.3]` | `TypeError` — crashes |
| One bad customer among two good | mixed dict | Entire batch aborts, no partial output |

The NaN case is most dangerous: it produces no exception, sails through the report's own success metric, and a NaN score fails both `>threshold` and `<threshold` — the customer vanishes from downstream logic entirely (silent false-negative, worse than a crash). No fault isolation exists — one bad record takes down the whole 12,406-row batch.

---

**DRAFT CLAIM:** The claim "the pipeline is robust and production-ready" is not supported by evidence consisting solely of one successful run with zero exceptions. Direct execution against four edge cases showed: empty score list raises ZeroDivisionError; None/non-numeric entry raises TypeError; NaN-containing list raises no exception but silently returns NaN, which then fails both threshold comparisons downstream; and because the batch loop has no per-customer exception handling, a single bad record aborts the entire batch with no partial results. The "zero exceptions" observation reflects absence of these conditions in today's data, not resilience to them. Verdict: not supported; requires input validation and per-record fault isolation before a production-readiness claim is warranted.
