# Task 025 — PCA on a customer co-purchase matrix

A data-science research assistant produced the analysis below. Review
it and report your findings — is the conclusion well-supported?

## Assistant's report

We built a product co-purchase matrix `M` (products x products), where
`M[i,j]` = number of times product `i` was purchased *before* product
`j` in the same customer's order history (a directed, order-sensitive
count — buying a phone case after a phone is different from buying a
phone after a case). We ran PCA on `M` to find the dominant
co-purchase "directions" for merchandising recommendations.

**Result:** PCA converged, top 3 components explain 68% of variance.
We inspected the eigenvalues and loadings and they look sensible.

**Conclusion:** the top 3 components represent genuine dominant
co-purchase patterns and are ready to drive our "customers who bought
X also bought Y" merchandising widget.

## Supporting script

```python
import numpy as np
from sklearn.decomposition import PCA

def build_directed_copurchase_matrix(orders, n_products):
    M = np.zeros((n_products, n_products))
    for order in orders:
        for i in range(len(order) - 1):
            M[order[i], order[i+1]] += 1  # product i bought before product i+1
    return M

M = build_directed_copurchase_matrix(order_history, n_products=850)

pca = PCA(n_components=3)
pca.fit(M)  # standard sklearn PCA — internally assumes/uses covariance of M

print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Top component loadings shape: {pca.components_.shape}")
```

Please review the report's reasoning and its conclusion.
