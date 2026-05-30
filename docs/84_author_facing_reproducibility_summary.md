# Author-Facing Reproducibility Summary

**Status labels:**
```
AUTHOR_FACING_DRAFT
PRIVATE_NOT_SENT
NO_VALIDATION
NO_REFUTATION
NO_MCMC
NO_PUBLIC_CLAIMS
AUTHOR_REVIEW_REQUIRED
```

## 1. Purpose

This is a concise private summary of an internal reproducibility/provenance check of the three AI-service outputs in the Supplementary Material.

It is not a validation or refutation of FLRW, MULTING, or w_eff. The purpose is narrower: to clarify table provenance, table-construction choices, and the information needed before making any stronger comparison among FLRW, MULTING, and w_eff.

## 2. What Was Reviewed

The Supplementary Material was located and reviewed.

The ChatGPT, Claude, and Gemini outputs were reviewed, with emphasis on the tables involving H-data, H-FLRW, H-MULT, fitted beta values, w_eff, and future-projection text.

The tables were extracted into a structured internal format and checked for consistency of row counts, source pages, service labels, and basic transcription/provenance.

A second independent audit was performed before revising the internal comparison, specifically to reduce overstatement and keep the conclusions limited to reproducibility and provenance.

## 3. Main Preliminary Observations

The three AI-service outputs are useful, but they are not numerically identical. They appear to reflect different table-construction choices, including time/redshift grids, H-data choices, H0 anchors, and fitted parameter values.

The fitted beta values differ materially across the three service outputs:

| Service | beta_d | beta_q |
|---|---:|---:|
| ChatGPT | 0.78 | 0.19 |
| Claude | 4.5 | 18.0 |
| Gemini | 4.25 | 8.10 |

H_FLRW provenance remains unresolved from the extracted table values. The extracted H_FLRW columns do not yet confirm a single shared construction across all three services.

H_MULT table values are close to each service's own H-data in the extracted tables, but this does not establish cross-service robustness of the framework. A common data source, common z/time grid, and documented fitting protocol would be needed before making a stronger statement.

w_eff should be treated as table output or a phenomenological comparison unless its derivation is clarified. In particular, it would be useful to distinguish whether w_eff is analytic, fitted, or diagnostic.

## 4. What This Suggests Methodologically

The next useful step is not model judgment, but a reproducibility protocol that explicitly records:

- data source choices;
- H_FLRW construction;
- H0 anchor;
- z/time grid;
- beta fitting protocol;
- optimization objective;
- whether w_eff is analytic, fitted, or diagnostic.

Such a protocol would make it easier to compare AI-service outputs without treating exploratory table values as model-comparison conclusions.

## 5. Questions for Dr. Buckholtz

1. Which beta set, if any, should be treated as primary?
2. What fitting protocol was intended for beta_d and beta_q?
3. What exact H_FLRW construction should be used?
4. Should H_MULT(z) be interpreted as standard H(z), an effective kinematic quantity, or something else?
5. Should the three AI outputs be treated as alternatives, an ensemble, or exploratory examples?

## 6. Proposed Next Step

Prepare a small reproducibility table/protocol before any stronger comparison among FLRW, MULTING, and w_eff.

The table could record, for each AI-service output, the data source choices, H0 anchor, H_FLRW construction, z/time grid, beta values, fitting objective, and the status of w_eff. This would provide a shared basis for further discussion before any model-comparison work.

## 7. Boundaries

No MCMC yet.

No validation or refutation.

No public claim.

No model-comparison conclusion.

Author clarification is needed before moving from provenance/reproducibility checking to stronger comparison among FLRW, MULTING, and w_eff.

## Internal Note

For internal use only: the beta values above are reported neutrally as extracted table values. This draft does not treat any beta set as the correct or preferred one.
