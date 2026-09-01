# Task 011 — Discounted cash-flow valuation using a bond-yield constant

A financial-modeling research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We valued Project Meridian using a discounted-cash-flow model with the
risk-free rate set to the current 10-year Treasury yield.

**Section 3.2 (cash flow projection):** using `risk_free_rate = 4.15%`
(10-year Treasury, as of our Q1 data pull), the project's NPV comes out
to $9.2M, comfortably above our $8M approval threshold.

**Section 5.1 (sensitivity discussion):** we note that our NPV estimate
of $9.2M was computed using the current 4.15% risk-free rate, and
remains robust to a +/-0.5% swing in this rate (NPV stays above $8M
threshold across 3.65%-4.65%).

## Supporting script

```python
RISK_FREE_RATE = 0.0415  # 10-year Treasury, Q1 data pull

def npv(cash_flows, rate):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))

cash_flows = [-12_000_000, 4_200_000, 4_500_000, 4_800_000, 5_100_000, 5_400_000]

# Section 3.2's own NPV calculation
result_32 = npv(cash_flows, RISK_FREE_RATE)
print(f"Section 3.2 NPV (rate={RISK_FREE_RATE:.2%}): ${result_32:,.0f}")

# Section 5.1's sensitivity check -- rate updated after a later data refresh,
# variable name reused without updating the reference in the printed summary
RISK_FREE_RATE = 0.0398  # updated Q2 data pull, 10-year Treasury moved to 3.98%
for delta in [-0.005, 0.0, 0.005]:
    r = RISK_FREE_RATE + delta
    result = npv(cash_flows, r)
    print(f"Section 5.1 sensitivity, rate={r:.2%}: NPV=${result:,.0f}")
```

Please review the report's reasoning and its conclusion.
