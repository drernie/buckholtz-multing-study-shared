# Task 030 — baseline arm output

## Findings

**Verdict: not well-supported.** The central safeguard claim -- grouping "by order ID" protects against driver/route/customer leakage -- is self-contradicting and confirmed empirically wrong.

### Finding 1 (HIGH) -- grouping justification self-contradicting, mechanism-verified
The report says order ID is unique per row AND "independent of" driver/route/customer identity, yet concludes grouping by it prevents driver/route/customer overlap across folds. If the grouping key is independent of those identities, grouping by it provides ZERO protection. Verified with sklearn 1.7.2:
- `cross_val_score(cv=5)` resolves to plain KFold -- no grouping at all.
- Plain KFold split on synthetic data matching the report's description: 100% of drivers in every validation fold also appear in that fold's training partition (20/20, all 5 folds).
- GroupKFold(groups=driver_id): 0 overlapping drivers -- clean separation, the actually-correct approach.
- GroupKFold(groups=order_id) [literally "grouped by order ID"]: IDENTICAL driver overlap to plain KFold, because every group has size 1 when the key is unique per row -- grouping by a unique-per-row key is mathematically indistinguishable from no grouping.

The report's stated safeguard does not exist.

### Finding 2 (MEDIUM) -- consequence plausible but unquantified
If driver/route/customer identity correlates with features in X, leakage lets the model partially memorize per-entity behavior. Report never checks for this -- asserts protection instead of testing for its absence.

### Finding 3 -- "interior optimum => non-overfit" is a non-sequitur
Interior optimum means the search range was wide enough, says nothing about whether that combination's CV RMSE is signal or noise -- no per-fold variance reported across the 25 combinations (optimizer's-curse concern).

### Finding 4 -- "CV ~= test" doesn't discriminate the hypothesis
4.21 vs 4.35 could mean both share the same undetected leakage bias, since the test split's own entity-disjointness from train is never established.

---

**DRAFT CLAIM:** The claim that learning_rate=0.03, max_depth=7 is a "reasonable, non-overfit" choice is not well-supported. The central safeguard against entity leakage -- "grouped by order ID... so standard k-fold is appropriate" -- is self-contradicting (order ID is also stated to be independent of driver/route/customer identity, meaning grouping by it protects nothing), confirmed mechanically: cross_val_score(cv=5) resolves to plain KFold, 100% of drivers in each validation fold also appear in that fold's training data, and grouping by a unique-per-row key is mathematically identical to no grouping. The remaining arguments (interior optimum, CV~=test) are each independently weak -- no per-fold variance reported, and CV/test agreement can't distinguish "no overfitting" from "both share the same undetected bias." Fix: re-run with GroupKFold on driver_id and report per-fold variance before concluding on generalization.
