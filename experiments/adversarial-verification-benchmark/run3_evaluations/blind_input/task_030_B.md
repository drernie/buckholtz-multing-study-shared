# Task 030 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 030 (delivery-time hyperparameter sweep)

### 1. Falsifiable claim
`learning_rate=0.03, max_depth=7` (CV RMSE=4.21 min, test RMSE=4.35 min) is a "reasonable, non-overfit choice whose CV estimate is a trustworthy proxy for real-world generalization" -- supported by (a) interior grid optimum, (b) close CV/test agreement. Checkable: rests on CV/test RMSE estimating error on NEW deliveries, not ones sharing a driver/route/customer with training data.

### 2. Controls
**Neither present.** No positive control (naive/simple baseline). No negative control (what CV/test RMSE would look like if the group-independence assumption were violated) -- built one below.

### 3. Red flags
**(a) Non-sequitur justification for skipping grouped CV:** "grouped by order ID, which is independent of driver/route/customer identity" -- order-ID uniqueness says nothing about whether driver/route/customer VALUES repeat across rows. In real delivery data a driver makes many deliveries -- ordinary random k-fold on rows will almost certainly place the same driver's other deliveries in both train and validation, the OPPOSITE of the report's claim.

**(b) CV/test "agreement" isn't independent evidence against overfitting if both splits share the same bias.** Test set carved out the same way (random row split). If driver identity leaks between train/val in CV, the same mechanism leaks between train/test -- agreement is consistent with BOTH "true generalization" AND "both estimates share the same optimism." The report treats a non-discriminating check as if it discriminates.

**(c) Silently-fixed parameter interacting with the swept one:** `n_estimators=200` fixed across the entire `learning_rate` sweep -- lower learning rates need more boosting rounds; structurally handicaps low-lr settings, weakening "interior optimum ⇒ real sweet spot" `[INFERRED]`.

**(d) Unexamined CV mechanics** `[VERIFIED via sklearn docs]`: `KFold` defaults `shuffle=False`. Report never states whether rows were pre-shuffled -- if sorted by date/route/driver, fold composition is an accident of file order, not controlled sampling.

**(e) Target leakage:** unknown, no feature list given -- `[UNKNOWN]`, not claimed as a finding.

### 4. Executed check
sklearn unavailable in sandbox; built pure-Python synthetic mirror via `mcp__mcp-run-python` (6,020 rows / 60 drivers, driver effect σ=3min, noise σ=2min, target-encoded driver adjustment):
```
[A] Standard non-grouped 5-fold CV RMSE = 2.011 min
[A] Fraction of val rows whose driver ALSO appears in that fold's train set: [1.0, 1.0, 1.0, 1.0, 1.0]
[B] Grouped (by-driver) 5-fold CV RMSE = 3.194 min
[C] Non-grouped held-out TEST RMSE (mirrors report's test) = 1.944 min
[D] Grouped held-out TEST RMSE (unseen drivers) = 2.747 min
```
100% of validation rows in every fold have their driver already in that fold's training data -- the direct opposite of the report's claim. Standard CV and non-grouped test agree closely (~3.4% relative diff -- same order as the report's 4.21 vs 4.35, ~3.3%) WHILE both underestimate true generalization error to an unseen driver by 40-59% (grouped CV 3.194, grouped test 2.747). `[VERIFIED-SYNTHETIC]`: demonstrates the mechanism is real and serious when present; whether present in the report's actual dataset remains `[UNKNOWN]`.

### 5. Verdict
**REJECT the conclusion as currently supported** -- not because the hyperparameters are necessarily wrong, but because both pieces of evidence offered (interior optimum, CV≈test agreement) are compatible with substantial overfitting to driver/route/customer identity. Standard-Ladder REJECT pending a grouped-CV/grouped-test rerun -- cheap fix (`GroupKFold`/`GroupShuffleSplit` keyed on driver/route/customer), report's own pipeline already has what's needed.

---

### DRAFT CLAIM
A gradient-boosted delivery-time regressor was tuned via standard (non-grouped) 5-fold CV, concluding `lr=0.03, max_depth=7` is reasonable/non-overfit because the CV optimum is interior and CV RMSE (4.21) closely matches test RMSE (4.35). The report's justification for skipping grouped CV -- "grouped by order ID, independent of driver/route/customer identity" -- does not follow: order-ID uniqueness only guarantees distinct deliveries, not that driver/route/customer is unique across the dataset, and delivery datasets typically have each driver appear in many orders. If driver identity carries real predictive signal and repeats between train/validation/test under random splitting, both CV and test estimates would be optimistically biased by the SAME mechanism, so their close agreement is consistent with hidden overfitting, not evidence against it. A synthetic simulation reproducing the report's stated splitting logic confirms the mechanism is real and large when present: standard CV/test RMSE agree closely (as in the report) while driver-grouped CV/test (unseen drivers) show 40-59% higher RMSE -- the true generalization gap the reported numbers cannot detect. Verdict: REJECT-pending-rerun with group-aware splitting keyed on driver/route/customer before treating the current RMSE numbers as representative of real-world performance. Secondary, lower-priority: `n_estimators` held fixed across the `learning_rate` sweep structurally disadvantages low learning rates, weakening the "interior optimum" evidence independent of the grouping issue.
