# Answer Key — Task 025

**Tier:** C (fresh synthetic, out-of-domain)
**Category:** Artifact Zoo Physics-adjacent — `non_hermitian` matrix treated as symmetric

## The seeded defect

`M` is explicitly built as a **directed** matrix: `M[i,j]` counts
"product `i` bought before product `j`," which is generally not equal
to `M[j,i]` ("product `j` bought before product `i`") — this is stated
directly in the report ("buying a phone case after a phone is different
from buying a phone after a case"). So `M` is asymmetric
(`M != M.T`) — the linear-algebra analogue of a non-Hermitian operator.
Standard PCA, as used here via `sklearn.decomposition.PCA`, implicitly
treats its input as if the relevant structure is captured by a
symmetric covariance-like matrix; running vanilla PCA on `pca.fit(M)`
does **not** correctly reflect the directional information in `M` — it
transforms `M` as if each row were a "sample" in a symmetric feature
space, discarding (or silently misinterpreting) the very asymmetry
(purchase order) that was the entire point of building a directed
matrix in the first place.

## Why this changes the correct answer

"PCA converged, eigenvalues/loadings look sensible, top 3 components
explain 68% of variance" is not evidence that those components
represent genuine *directed* co-purchase patterns. PCA run this way
(`fit` on the raw directed count matrix, treating rows as samples) does
not know or use the fact that `M[i,j]` and `M[j,i]` mean different
things — the order information the analysis is supposed to be built
around is not something ordinary PCA is designed to preserve or exploit
correctly. "It ran without error and the numbers look plausible" is not
the same as "the method is appropriate for asymmetric/directional
data" — a merchandising recommendation built on this misapplied
decomposition risks recommending symmetric associations
("X often co-occurs with Y") when the actual, more valuable signal is
directional ("X is bought before Y, not vice versa").

## What a correct detection should name

- `M` is built directed/asymmetric by construction (`M[i,j] != M[j,i]`
  in general) — the report itself explains why this matters.
- Standard PCA on the raw matrix does not respect or exploit that
  asymmetry; it's designed for symmetric covariance-like structure.
- A correct approach needs either symmetrizing `M` explicitly and
  analyzing the resulting undirected structure (losing the order
  information on purpose, with that tradeoff stated), or using a
  method actually designed for directed/asymmetric matrices (e.g.
  separate analysis of `M + M.T` and `M - M.T`, or a method built for
  directed graphs), not vanilla PCA presented as if it captures
  "dominant co-purchase directions."

## Ground truth for the blind evaluator

- **defect_location:** `pca.fit(M)` applied directly to the asymmetric
  directed co-purchase matrix `M`
- **defect_type:** asymmetric ("non-Hermitian-analogue") matrix
  processed with a method that implicitly assumes symmetric structure
  (Artifact Zoo Physics — `non_hermitian`)
