# Short Email Draft After Supplementary Audit

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

**Subject:** Follow-up on Supplementary Material reproducibility framing

Dear Dr. Buckholtz,

Thank you again for pointing me toward the Supplementary Material. I have now located it and performed a preliminary internal reproducibility/provenance check of the three AI-service outputs: ChatGPT, Claude, and Gemini.

My aim at this stage is narrow and cautious. I am not treating this as a validation or refutation of FLRW, MULTING, or w_eff. Instead, I am trying to understand the table-construction choices well enough to make any later comparison more reproducible.

The main preliminary observation is that the three AI-service outputs are useful but not numerically identical. In particular, they appear to use different time/redshift grids, H-data choices, H0 anchors, fitted beta values, and possibly different H_FLRW constructions. The fitted beta values I extracted are:

| Service | beta_d | beta_q |
|---|---:|---:|
| ChatGPT | 0.78 | 0.19 |
| Claude | 4.5 | 18.0 |
| Gemini | 4.25 | 8.10 |

I also found that the H_FLRW provenance is not yet clear from the extracted table values alone. The H_MULT table values are close to each service's own H-data, but I would not interpret that as cross-service robustness without a common data source, common z/time grid, and documented fitting protocol. Similarly, I am treating w_eff as a table output or phenomenological comparison unless its derivation is clarified.

Would this framing be acceptable to you: before making any stronger comparison among FLRW, MULTING, and w_eff, we first prepare a small reproducibility protocol that records the data source choices, H_FLRW construction, H0 anchor, z/time grid, beta fitting protocol, optimization objective, and whether w_eff is analytic, fitted, or diagnostic?

If that framing seems reasonable, I would be grateful for your guidance on five points:

1. Which beta set, if any, should be treated as primary?
2. What fitting protocol was intended for beta_d and beta_q?
3. What exact H_FLRW construction should be used?
4. Should H_MULT(z) be interpreted as standard H(z), an effective kinematic quantity, or something else?
5. Should the three AI outputs be treated as alternatives, an ensemble, or exploratory examples?

My goal is to preserve the exploratory value of the Supplementary Material while making the provenance and reproducibility assumptions explicit before doing any stronger model-comparison work.

Best regards,

[Your name]
