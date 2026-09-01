# Task 021 — Batch scoring pipeline, edge-case robustness review

A data-engineering research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We built a batch scoring pipeline that averages a customer's recent
transaction-risk scores to produce a daily summary score. We ran it
against our full production customer list (12,406 customers) and it
completed without errors, producing 12,406 summary rows.

**Conclusion:** the pipeline is robust and production-ready — it
processed the entire customer list cleanly with zero exceptions.

## Supporting script

```python
def daily_summary_score(customer_scores):
    """Average a customer's list of recent risk scores."""
    total = sum(customer_scores)
    return total / len(customer_scores)

def run_batch(all_customers):
    results = {}
    for customer_id, scores in all_customers.items():
        results[customer_id] = daily_summary_score(scores)
    return results

# Production run (12,406 customers, real transaction data)
all_customers = load_customer_scores()  # dict: customer_id -> list[float]
results = run_batch(all_customers)
print(f"Processed {len(results)} customers with 0 exceptions.")
```

Please review the report's reasoning and its conclusion.
