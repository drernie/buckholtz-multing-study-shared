# Task 010 — Combined reliability claim for a pump assembly

A reliability-engineering research assistant produced the analysis
below. Review it and report your findings — is the conclusion
well-supported?

## Assistant's report

Our pump assembly's failure modes were assessed independently across
three subsystems:

1. **Bearing wear**: independently modeled, found to survive 50,000
   operating hours with 95% confidence, assuming nominal lubrication
   and load.
2. **Seal degradation**: independently modeled, found to survive 45,000
   operating hours with 95% confidence, assuming nominal temperature and
   chemical exposure.
3. **Impeller fatigue**: independently modeled, found to survive 60,000
   operating hours with 95% confidence, assuming nominal flow rate and
   cavitation-free operation.

**Combined conclusion:** since each subsystem independently clears our
40,000-hour design requirement with 95% confidence, and all three
subsystems must fail together for the pump to fail catastrophically
before 40,000 hours, the overall assembly's reliability at 40,000 hours
is at least 95% x 95% x 95% ≈ 85.7% — comfortably meeting our 80%
program requirement.

## Supporting script

```python
p_bearing = 0.95   # survives 50,000h
p_seal = 0.95       # survives 45,000h
p_impeller = 0.95   # survives 60,000h

# each subsystem's own model assumed the OTHER subsystems were operating
# at nominal conditions (nominal load, nominal temperature, nominal flow) --
# these nominal-condition assumptions were not independently re-derived per
# subsystem, they were shared across all three models as a common baseline
# operating-condition assumption

p_combined_naive = p_bearing * p_seal * p_impeller
print(f"Naive combined reliability (independence assumed): {p_combined_naive:.3f}")
print("Program requirement: 0.80")
print(f"Margin: {p_combined_naive - 0.80:.3f}")
```

Please review the report's reasoning and its conclusion.
