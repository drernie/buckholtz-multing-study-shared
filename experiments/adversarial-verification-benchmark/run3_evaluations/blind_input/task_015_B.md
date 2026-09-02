# Task 015 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 015

### 1. Falsifiable claim
"Model architecture is robust to learning-rate choice across 4 orders of magnitude — therefore no careful tuning needed for production deployment."

### 2. Controls
**Neither supplied.** No positive control (LR known to blow up), no floor reference, no baseline trained to convergence.

### 3. Red flags
- Silently-fixed `max_iter=1` across every LR value, never discussed — caps training at exactly one pass, structurally preventing divergence/underfitting from ever appearing.
- AUC is rank-based/scale-invariant — a LR that scales the weight vector without flipping direction can leave AUC unchanged while calibration degrades; never checked.
- Train/val provenance opaque (temporal leakage risk for fraud detection) — flagged [UNKNOWN].

### 4. Executed check (synthetic fraud-like proxy, 60k rows, 47 features)
| Setup | AUC range | Spread |
|---|---|---|
| Floor (dummy) | 0.5000 | — |
| Report replica (max_iter=1) | [0.6972, 0.7749] | 0.0777 |
| Converged ablation (max_iter=200) | [0.6602, 0.7834] | 0.1233 |

Coefficient-norm growth across the sweep at max_iter=1: 0.35→12.88 (36.5x) — LR is visibly destabilizing the raw weight vector even within one epoch, just damped by the rank-based metric. Relaxing max_iter to let SGD converge makes LR sensitivity WORSE, not better — AUC degrades at high LR once training runs long enough for divergence to manifest. This directly falsifies the generalization step: production isn't capped at 1 epoch, and the two regimes disagree.

### 5. Verdict
**REJECT** the generalization to production. The narrower claim ("at exactly 1 epoch, AUC is insensitive to LR on this dataset") may be true but is much weaker than what's claimed, and still lacks a control confirming the test could detect sensitivity if present.

---

### DRAFT CLAIM
A report claims a fraud-detection SGDClassifier is "robust to learning rate across 4 orders of magnitude" (AUC in [0.912,0.918]) and concludes no tuning is needed in production. The sweep fixes max_iter=1 identically at every LR, with no positive/negative/floor control. An independent ablation on synthetic fraud-like data reproduced the max_iter=1 setup then reran with training allowed to converge (max_iter=200): the converged version showed AUC degrading substantially at high LR (peak ~0.78 down to ~0.66-0.70), the classic LR-instability failure mode the single-epoch design never lets manifest. This suggests the "robustness" finding is an artifact of the frozen max_iter=1 parameter, not a genuine architecture property, and the production conclusion does not follow. Reviewer should re-run the original sweep with max_iter varied jointly with LR on the real data, and check whether AUC is masking calibration/numerical instability a log-loss metric would reveal.
