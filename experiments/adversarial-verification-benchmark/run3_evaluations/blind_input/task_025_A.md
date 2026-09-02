# Task 025 — baseline arm output

## Findings — PCA on a directed co-purchase matrix

**Bottom line: the conclusion is not well-supported.** "PCA converged, explains 68% of variance, loadings look sensible -> genuine co-purchase patterns ready for production" does not follow from the evidence given.

### Core methodological flaw: popularity confound (mechanism identified, not just suspected)
`M` is a raw, unnormalized directed count matrix over 850 products; PCA is fit directly with no preprocessing. On a co-occurrence/adjacency-style count matrix, variance is dominated by marginal product popularity, not pairwise affinity -- same failure mode as spectral analysis on a raw (non-degree-normalized) adjacency matrix.

**Tested directly, not just asserted:** built a synthetic null model -- 850 products, power-law popularity, orders assembled by drawing items INDEPENDENTLY by popularity alone (zero genuine pairwise affinity by construction). Built the identical co-purchase matrix, ran identical `sklearn.decomposition.PCA(n_components=3)`.

| popularity skew | orders | basket size | top-3 explained variance | corr(PC1, row popularity) |
|---|---|---|---|---|
| 1.1 | 50,000 | 2-5 | 98.9% | 0.991 |
| 0.6 (flat) | 50,000 | 2-6 | 54.7% | 0.992 |
| 1.5 (skewed) | 50,000 | 2-4 | 99.7% | 0.995 |
| 1.1 | 20,000 | 3-8 | 98.1% | 0.994 |

Every variant -- across a >4x parameter range, none tuned to the report's data -- produces high-to-extreme "explained variance" with PC1 correlating >=0.99 with raw popularity. The report's own 68% sits inside this range, produced by a model with NO real co-purchase mechanism. Floor defect: the success criterion is met/exceeded by a construction with zero mechanism -- same structural failure as the H1 null-model case already on record in this stack's pearl registry.

### Independent problems (each sufficient alone)
1. "Loadings look sensible" -- unverified subjective eyeball, no negative control (shuffled/permuted matrix).
2. `n_components=3` arbitrary -- no scree plot, no parallel analysis threshold.
3. Row/column semantics conflated -- PCA centers columns only, row popularity never removed.
4. No held-out validation of the actual business objective (precision@k, A/B, lift over baseline).
5. No specified translation from PCA loadings to a recommendation rule.
6. Standard alternatives (PMI/lift-normalized co-occurrence, NMF, correspondence analysis, association-rule mining) not considered -- these are the actual industry tools for this exact problem because they avoid the popularity confound.

### What would fix it
Popularity-normalize before factorization (PMI/lift, or NMF/correspondence analysis); choose component count via scree/parallel analysis; run identical pipeline on a negative control and require real data to separate from that floor; validate against held-out purchases with precision@k / lift over popularity baseline.

---

**DRAFT CLAIM:** A report claims PCA on a raw, unnormalized directed product co-purchase count matrix (850x850), top-3 components explaining 68% of variance with "sensible-looking" loadings, demonstrates genuine co-purchase patterns suitable for production. Not supported: PCA on a raw co-occurrence matrix is dominated by marginal popularity rather than pairwise affinity, and an independently constructed null model (orders from power-law popularity alone, zero real co-purchase structure) reproduces comparable-to-higher "explained variance" (54.7%-99.7% across four settings, all >= the reported 68% at realistic skew) with PC1 correlating >=0.99 with raw popularity in every case. No negative control, no scree justification for 3 components, no held-out predictive validation, no defined loadings-to-recommendation procedure. Verdict: not ready for production; needs popularity normalization, principled component count, negative-control comparison, and out-of-sample validation.
