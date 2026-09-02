# Task 025 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 025: PCA on Customer Co-Purchase Matrix

### 1. Falsifiable claim
"The top 3 PCA components represent genuine dominant co-purchase patterns and are ready to drive a merchandising widget." Predicate: loadings of PC1-PC3 encode pairwise product-affinity structure, not something else that happens to also produce high variance.

### 2. Controls
**None supplied.** Only evidence: "68% variance explained" + "loadings look sensible" (eyeballed). No negative control, no positive control (synthetic data with known injected structure), no held-out replication, no external/behavioral criterion (does a widget built from these actually lift conversion vs. "most popular" baseline).

### 3. Failure modes identified before running anything
- Popularity confound: raw co-occurrence count matrix on 850 products with heavy-tailed popularity; sklearn PCA centers columns but doesn't correct for marginals -- dominant variance direction is almost always "how often a product appears," not "which products pair."
- Tautological validation: PCA is guaranteed by construction to concentrate variance into a few components on any moderately structured matrix.
- Directionality claimed (order-sensitive matrix) but never exercised/tested against `M + M^T`.
- `n_components=3` unjustified (no scree/CV criterion).

### 4. Executed check
Reproduced the exact pipeline verbatim on two synthetic worlds (850 products, 120k orders, matched scale):
- **World A (negative control):** items drawn independently by Zipf popularity only -- zero genuine co-purchase affinity by construction.
- **World B (positive control):** popularity backbone + 5 real injected clusters (genuine structure).

| World | Top-3 explained variance | corr(PC1, popularity) |
|---|---|---|
| A -- pure popularity, no structure | 98.99% | 0.93 |
| B -- real 5-cluster structure injected | 97.51% | 0.94 |
| Report's actual number | 68% | not measured |

A world with ZERO genuine co-purchase pattern produces HIGHER top-3 variance (99%) than the report's 68%.

More decisively, in World B (true cluster structure known), measured how much each component tracks the injected clusters (eta^2) vs. popularity:
```
PC1: var=75.9% | corr_popularity=+0.93 | eta^2_with_TRUE_cluster=0.0051
PC2: var=15.6% | corr_popularity=+0.34 | eta^2_with_TRUE_cluster=0.0006
PC3: var= 5.3% | corr_popularity=+0.15 | eta^2_with_TRUE_cluster=0.0004
PC5: var= 0.65%| corr_popularity=-0.04 | eta^2_with_TRUE_cluster=0.1634  <- real signal appears here
PC7: var= 0.27%| corr_popularity=+0.02 | eta^2_with_TRUE_cluster=0.1803
Reference (random-label shuffle) eta^2: mean 0.0046, 95th pctile 0.011
```
PC1-PC3 -- exactly what the report proposes shipping -- are statistically indistinguishable from noise w.r.t. the real injected structure (eta^2 ~0.0004-0.005, at random-shuffle level), while being almost pure popularity (r up to 0.93). The real signal only appears at PC5/PC7, outside the report's window.

### 5. Verdict
**REJECT.** Sole evidence (68% variance + eyeballed loadings) fails to discriminate "genuine co-purchase pattern" from "nothing more than popularity." Executed negative control shows a null world with zero real signal reproduces/exceeds the reported result. Kill analysis: what's killed is that THESE top-3 components encode genuine structure; NOT killed: co-purchase mining itself, with popularity-correction (PMI/lift), held-out replication, and a justified component count, may still recover real structure (shown to exist further down the spectrum).

---

### DRAFT CLAIM
A team built an 850x850 directed product co-purchase count matrix and ran PCA(n_components=3), reporting 68% variance explained with "sensible-looking" loadings, concluding genuine co-purchase patterns ready for production. No positive/negative control or held-out validation was performed. Independent testing (identical pipeline on synthetic data at matched scale) shows a null world with ZERO genuine co-purchase structure (items drawn independently by popularity) produces HIGHER top-3 variance (99%) than the reported 68%, with PC1 correlating r~0.93 with raw popularity. In a second world with real 5-cluster structure injected, the top-3 components remain almost pure popularity (eta^2 with true clusters ~0.0004-0.005, indistinguishable from random shuffle), while the actual injected signal only appears at components 5+, outside the report's window. Strongly suggests the reported result is a popularity artifact. Recommend rejecting the conclusion; popularity-corrected matrix, held-out replication, and justified component count are minimum next steps.
