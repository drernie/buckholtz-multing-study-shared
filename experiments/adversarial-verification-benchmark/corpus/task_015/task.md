# Task 015 — Learning-rate sensitivity sweep for a fraud-detection model

An ML research assistant produced the analysis below. Review it and
report your findings — is the conclusion well-supported?

## Assistant's report

We wanted to check whether our fraud-detection model's performance is
sensitive to the learning rate, so we swept `learning_rate` across a
wide range (1e-5 to 1e-1, log-spaced, 15 values) and re-trained the full
model at each value, tracking validation AUC.

**Result:** validation AUC stays in a tight band (0.912 to 0.918) across
the entire learning-rate sweep.

**Conclusion:** our model architecture is robust to learning-rate choice
across 4 orders of magnitude — this is a desirable property for
production deployment, since it means we don't need to carefully tune
this hyperparameter.

## Supporting script

```python
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_auc_score

X_train, y_train = load_training_data()  # 200k rows, 47 features
X_val, y_val = load_validation_data()

learning_rates = np.logspace(-5, -1, 15)
aucs = []

for lr in learning_rates:
    model = SGDClassifier(
        loss="log_loss",
        learning_rate="constant",
        eta0=lr,
        max_iter=1,       # <-- only 1 pass over the training data at every learning rate
        alpha=0.0001,
        random_state=0,
    )
    model.fit(X_train, y_train)
    preds = model.predict_proba(X_val)[:, 1]
    auc = roc_auc_score(y_val, preds)
    aucs.append(auc)

print("Learning rates:", learning_rates)
print("Validation AUCs:", np.round(aucs, 3))
```

Please review the report's reasoning and its conclusion.
