# Task 015 — baseline arm output

## Findings

**Verdict: not well-supported.** Report's own comment flags the flaw (`max_iter=1` — only 1 pass at every learning rate).

1. Reproduced the SGDClassifier call on synthetic fraud-like data: every fit raised `ConvergenceWarning`. None of the 15 "models" trained to anything resembling convergence — the report doesn't mention this.
2. Ran identical sweep with `max_iter=1` (as scripted) vs `max_iter=200` (converged): on synthetic data, the max_iter=1 sweep was NOT flat (AUC 0.567–0.727, spread ~0.16), including collapse at high LR — exactly the instability you'd expect. This shows a tight flat curve is not automatic from the bug alone; the report's suspiciously tight 0.912-0.918 band is likely a saturation effect specific to their strongly-predictive features, not evidence of architecture robustness.
3. No floor/ceiling arms: floor (zero-weight dummy) = 0.5 AUC, confirms real learning is happening, but no ceiling (fully-converged best model) exists to distinguish "robust in a meaningful middle range" from "task saturates the metric regardless of step size."

---

**DRAFT CLAIM:** The claim "robust to learning-rate choice across 4 orders of magnitude, no tuning needed for production" is not supported. The script trains every model for exactly one epoch (max_iter=1) regardless of LR — verified to reliably trigger ConvergenceWarning, none of 15 fits reaching convergence — and a flat AUC-vs-LR curve is not a generic consequence of this: on comparable synthetic data the same code produced a 0.16-point AUC swing including high-LR collapse. No ceiling comparison exists, so the reported band cannot be distinguished from a saturation effect. The experiment needs re-running under the actual production epoch budget, with floor/ceiling arms and a deployment-relevant metric, before "no tuning needed" can be supported.
