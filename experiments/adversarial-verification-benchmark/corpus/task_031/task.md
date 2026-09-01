# Task 031 — Discounted cash-flow valuation, constant provenance check

A financial-modeling research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We built a discounted cash-flow (DCF) valuation for a target company
using a 10-year explicit forecast plus a terminal value (Gordon growth
model). All inputs are sourced and labeled: forecast free cash flows
come from the company's own management guidance (cited, years 1-5) and
a straight-line convergence to industry-average growth thereafter
(years 6-10, per a cited industry report); the discount rate (WACC =
9.2%) is computed from the company's actual capital structure (market
cap, debt, current cost of debt/equity, all cited to recent filings/
market data); the terminal growth rate (2.1%) is set equal to the
cited long-run GDP-growth consensus forecast, explicitly *not* fitted
to make the valuation hit any target number.

**Result:** implied enterprise value = $3.94B. Sensitivity table shows
the result ranges from $3.3B to $4.9B across a WACC range of 8.2%-10.2%
and terminal growth range of 1.6%-2.6% (i.e., the paper explicitly
tests robustness to the two most uncertain inputs, and 2.1%/9.2% are
each within, not at the edge of, standard analyst ranges for this
sector).

**Conclusion:** the $3.94B point estimate is a defensible valuation
given the stated assumptions, with an explicit sensitivity range and
fully cited, non-circular inputs (no input was reverse-engineered from
a target valuation).

## Supporting script

```python
def dcf_valuation(fcf_forecast, wacc, terminal_growth, terminal_year_fcf):
    pv_explicit = sum(fcf / (1 + wacc) ** (i + 1) for i, fcf in enumerate(fcf_forecast))
    terminal_value = terminal_year_fcf * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal_value / (1 + wacc) ** len(fcf_forecast)
    return pv_explicit + pv_terminal

# All inputs cited: management guidance (yrs 1-5), industry-report convergence (yrs 6-10)
fcf_forecast = [210, 235, 258, 279, 298, 312, 325, 337, 348, 358]  # $M, cited sources
wacc = 0.092          # from company capital structure, cited market data
terminal_growth = 0.021  # cited long-run GDP consensus, independent of target valuation

ev = dcf_valuation(fcf_forecast, wacc, terminal_growth, fcf_forecast[-1])
print(f"Enterprise value: ${ev/1000:.2f}B")

# Sensitivity table
for w in [0.082, 0.092, 0.102]:
    for g in [0.016, 0.021, 0.026]:
        val = dcf_valuation(fcf_forecast, w, g, fcf_forecast[-1])
        print(f"WACC={w:.1%}, g={g:.1%}: ${val/1000:.2f}B")
```

Please review the report's reasoning and its conclusion.
