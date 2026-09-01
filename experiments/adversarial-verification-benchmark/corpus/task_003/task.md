# Task 003 — Cross-validation agreement for a churn-prediction model

An ML research assistant produced the analysis below. Review it and
report your findings — is the conclusion well-supported?

## Assistant's report

To confirm our customer-churn model's feature-importance ranking is
robust, I split the 50,000-row customer dataset into two independent
halves (Fold A: rows 0-24999, Fold B: rows 25000-49999) and trained a
separate gradient-boosted model on each half, then compared the top-5
feature importances.

Both folds agreed on the same top-5 features in the same order
(`tenure_months`, `monthly_charges`, `contract_type`,
`support_tickets_90d`, `payment_method`), with importance scores
correlating at r=0.98 between the two folds.

**Conclusion:** this cross-fold agreement is strong independent
evidence that these 5 features are the genuine drivers of churn in our
customer base, not an artifact of one particular train/test split — the
signal is robust across two completely separately-trained models.

## Supporting script

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Shared preprocessing pipeline, applied to the FULL dataset before splitting
df = pd.read_csv("customers.csv")
df["support_tickets_90d"] = df["support_tickets_90d"].fillna(df["support_tickets_90d"].median())
df["monthly_charges_scaled"] = (df["monthly_charges"] - df["monthly_charges"].mean()) / df["monthly_charges"].std()
# feature-selection step: keep only the 12 features that correlate > 0.15 with churn,
# computed once on the full 50,000-row dataset, BEFORE the fold split below
correlations = df.corr()["churned"].abs()
selected_features = correlations[correlations > 0.15].index.tolist()
selected_features.remove("churned")
X_full = df[selected_features]
y_full = df["churned"]

# NOW split into "independent" folds
fold_a = df.iloc[:25000]
fold_b = df.iloc[25000:]

model_a = GradientBoostingClassifier(random_state=1).fit(fold_a[selected_features], fold_a["churned"])
model_b = GradientBoostingClassifier(random_state=2).fit(fold_b[selected_features], fold_b["churned"])

imp_a = pd.Series(model_a.feature_importances_, index=selected_features).sort_values(ascending=False)
imp_b = pd.Series(model_b.feature_importances_, index=selected_features).sort_values(ascending=False)

print("Fold A top 5:", imp_a.head(5).index.tolist())
print("Fold B top 5:", imp_b.head(5).index.tolist())
print("Correlation:", imp_a.reindex(selected_features).corr(imp_b.reindex(selected_features)))
```

Please review the report's reasoning and its conclusion.
