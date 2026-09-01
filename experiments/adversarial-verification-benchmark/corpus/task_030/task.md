# Task 030 — Hyperparameter sweep for a delivery-time prediction model

A machine-learning research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We swept two hyperparameters (`learning_rate` in
`{0.001, 0.003, 0.01, 0.03, 0.1}`, `max_depth` in `{3, 5, 7, 9, 11}`) for
a gradient-boosted delivery-time regressor, using 5-fold cross-validation
on the training set only (test set untouched throughout the sweep). Each
row is one independent delivery from a distinct order; no driver, route,
or customer contributes more than one row to both a training fold and
its corresponding validation fold (grouped by order ID, which is
independent of driver/route/customer identity), so standard (non-grouped)
k-fold is appropriate here. For
each of the 25 combinations we recorded mean CV RMSE. We picked the
combination with the lowest mean CV RMSE (`learning_rate=0.03,
max_depth=7`, CV RMSE=4.21 min), then retrained a single final model on
the full training set with that combination and evaluated it once on
the held-out test set.

**Result:** best CV RMSE = 4.21 min (combination not at either edge of
either swept range — the minimum is interior to the grid in both
dimensions). Final test RMSE = 4.35 min, close to the CV estimate,
consistent with normal train/test variation rather than overfitting to
the validation folds.

**Conclusion:** the chosen hyperparameters (`learning_rate=0.03,
max_depth=7`) are a reasonable, non-overfit choice — the sweep's optimum
sits inside the searched grid rather than at a boundary, and the
close CV/test RMSE agreement supports the model's generalization.

## Supporting script

```python
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor

X_train, y_train, X_test, y_test = load_delivery_data_split()  # test set held out from the start

results = {}
for lr in [0.001, 0.003, 0.01, 0.03, 0.1]:
    for depth in [3, 5, 7, 9, 11]:
        model = GradientBoostingRegressor(learning_rate=lr, max_depth=depth, n_estimators=200, random_state=0)
        cv_rmse = -cross_val_score(model, X_train, y_train, cv=5, scoring="neg_root_mean_squared_error").mean()
        results[(lr, depth)] = cv_rmse

best_params = min(results, key=results.get)
print(f"Best params: learning_rate={best_params[0]}, max_depth={best_params[1]}, CV RMSE={results[best_params]:.2f}")

final_model = GradientBoostingRegressor(learning_rate=best_params[0], max_depth=best_params[1], n_estimators=200, random_state=0)
final_model.fit(X_train, y_train)
test_rmse = np.sqrt(np.mean((final_model.predict(X_test) - y_test) ** 2))
print(f"Test RMSE: {test_rmse:.2f}")
```

Please review the report's reasoning and its conclusion.
