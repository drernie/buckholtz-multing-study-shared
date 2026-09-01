# Task 023 — Churn classifier, perfect held-out performance

A machine-learning research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We built a classifier to predict customer churn from account features,
trained on 80% of the data and evaluated on a held-out 20% test split.

**Result:** F1 = 1.000 on the held-out test set. Precision = 1.000,
recall = 1.000.

**Conclusion:** the model generalizes perfectly to unseen customers —
this is a strong, deployable churn predictor.

## Supporting script

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score

df = pd.read_csv("customer_accounts.csv")

# Feature engineering: derive a few extra columns from the raw export
df["tenure_days"] = (pd.to_datetime(df["snapshot_date"]) - pd.to_datetime(df["signup_date"])).dt.days
df["days_since_cancellation"] = (pd.to_datetime(df["snapshot_date"]) - pd.to_datetime(df["cancellation_date"])).dt.days
df["is_active"] = df["days_since_cancellation"].isna().astype(int)  # 1 if never cancelled

features = ["tenure_days", "monthly_spend", "support_tickets", "days_since_cancellation", "is_active"]
X = df[features].fillna(-1)
y = df["churned"]  # target: 1 if customer churned

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
preds = clf.predict(X_test)

print(f"F1: {f1_score(y_test, preds):.3f}")
print(f"Precision: {precision_score(y_test, preds):.3f}")
print(f"Recall: {recall_score(y_test, preds):.3f}")
```

Please review the report's reasoning and its conclusion.
