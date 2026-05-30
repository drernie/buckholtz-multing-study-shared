# docs/81 Revision Verification After Codex Audit

**Date:** 2026-05-31
**Verifier:** Codex
**Latest commit inspected:** `ea1e896` (`docs: revise multi-AI comparison after Codex audit`)
**Audit baseline:** `docs/82_codex_independent_audit_of_multi_ai_comparison.md`
**Status:** INTERNAL_VERIFICATION_ONLY

**Safety labels:**
```
DOCS81_REVISION_VERIFICATION
INTERNAL_ANALYSIS_ONLY
NO_VALIDATION
NO_REFUTATION
NO_MCMC
NO_PUBLIC_CLAIMS
NO_EMAIL_SENT
```

## Evidence Checked

[VERIFIED] Commands/artifacts checked:
- `git log --oneline -5`
- `git show --stat ea1e896`
- `git show -- docs/81_multi_ai_reproducibility_comparison.md`
- `docs/81_multi_ai_reproducibility_comparison.md`
- `docs/82_codex_independent_audit_of_multi_ai_comparison.md`

[VERIFIED] `ea1e896` changes only `docs/81_multi_ai_reproducibility_comparison.md` and is explicitly a revision after the Codex audit.

## Requirement Verdicts

| # | Requirement | Verdict | Evidence / Notes |
|---:|---|---|---|
| 1 | H_FLRW overclaim removed | PASS | `docs/81` now says H_FLRW provenance remains unclear and NOT YET STABLE from CSV evidence. It no longer presents a shared Planck-2018 baseline as established. |
| 2 | Beta statistics corrected | PASS | `docs/81` now reports beta_d mean `3.18` with arithmetic value `3.1767`; beta_q mean `8.76` with arithmetic value `8.7633`; no active beta_d mean `1.84` remains except in revision history noting the correction. |
| 3 | H_MULT robustness softened | WARN | Main conclusion is softened: H_MULT is close to each service's own H-data and cross-service robustness is not established. However, line in "What this does NOT claim" still says H_MULT variation is "suggesting the framework has some robustness." This should be softened or removed. |
| 4 | Unsupported optimization/local-minima claims softened | PASS | "valid optimization methods" and hard "different local minima" claims were replaced in the body with "optimization procedures not sufficiently documented" and "non-unique fitting, differing service assumptions, or undocumented table-construction choices." Remaining old phrases appear only in revision-history notes as replaced text. |
| 5 | "w_eff predictions" replaced | PASS | Current analytical wording uses "w_eff table values"; old phrase appears only in revision history as a replaced phrase. |
| 6 | Safety labels present | PASS | `REVISED_INTERNAL_ANALYSIS`, `NOT_AUTHOR_READY`, `NO_VALIDATION`, `NO_REFUTATION`, `NO_MCMC`, and `NO_PUBLIC_CLAIMS` are present in the document safety block/status. |

## Detailed Findings

### PASS: H_FLRW Downgrade Applied

[VERIFIED] The revised document now states:
- H_FLRW calculation method remains unclear from extracted CSV evidence.
- Numerical values do not confirm a single shared Planck-2018 baseline.
- H_FLRW provenance is NOT YET STABLE.

This satisfies the Codex audit requirement to remove the prior "stable/identical" overclaim.

### PASS: Beta Statistics Corrected

[VERIFIED] The revised beta statistics section now reports:
- beta_d mean: `3.18`, with arithmetic detail `(0.78 + 4.5 + 4.25)/3 = 3.1767`
- beta_q mean: `8.76`, with arithmetic detail `(0.19 + 18.0 + 8.10)/3 = 8.7633`
- beta_d sample standard deviation: `2.08`
- beta_q sample standard deviation: `8.92`
- beta_d sample CV: `65.5%`
- beta_q sample CV: `101.8%`

[VERIFIED] The previous erroneous `beta_d mean = 1.84` appears only in revision history as a correction note, not as an active result.

### WARN: H_MULT Robustness Still Has One Residual Overstatement

[VERIFIED] Most H_MULT wording is now appropriately limited:

> H_MULT remains close to each service's own H-data in the extracted tables. Cross-service robustness is not established without a common z-grid, common H-data, and documented H_MULT computation.

[WARN] One residual sentence remains in the "What this does NOT claim" section:

> H_MULT varies by ~5% at low z despite 42-95x beta differences, suggesting the framework has some robustness.

This is not as strong as the original overclaim, but it still implies robustness of the framework. Suggested replacement:

> H_MULT values remain relatively close to each service's own H-data in selected low-z rows, but this does not establish cross-service robustness.

### PASS: Unsupported Optimization Claims Softened

[VERIFIED] The current document no longer asserts that all services used valid optimization methods as a finding. It now says optimization procedures are not sufficiently documented to assess equivalence or validity.

[VERIFIED] The hard "different local minima" explanation was replaced with:

> non-unique fitting, differing service assumptions, or undocumented table-construction choices

This satisfies the Codex audit requirement.

### PASS: w_eff Wording Softened

[VERIFIED] The current document uses "w_eff table values" in the active analysis. The phrase "w_eff predictions" appears only in the revision history as a description of what was replaced.

### PASS: Safety Labels Present

[VERIFIED] Required safety labels are present:
- `REVISED_INTERNAL_ANALYSIS`
- `NOT_AUTHOR_READY`
- `NO_VALIDATION`
- `NO_REFUTATION`
- `NO_MCMC`
- `NO_PUBLIC_CLAIMS`

## Safe-Use Assessment

### Is docs/81 now safe as internal analysis?

**YES, with one WARN.**

`docs/81` now applies the core Codex audit corrections and is much safer for internal analysis. The remaining H_MULT robustness sentence should be softened before relying on it as a clean internal reference, but it does not invalidate the overall revision.

### Is docs/81 safe to share with Dr. Buckholtz?

**NO / NOT YET.**

The document itself is labeled `NOT_AUTHOR_READY`, and one H_MULT robustness phrase still needs softening. It also remains an internal CSV-level analysis and should not be shared externally until the remaining wording is fixed and the user explicitly approves external sharing.

## Remaining Required Edits

1. Soften or remove the sentence:
   > suggesting the framework has some robustness

2. Replace it with CSV-level wording:
   > H_MULT values remain relatively close to each service's own H-data in selected low-z rows, but this does not establish cross-service robustness.

3. Keep `NOT_AUTHOR_READY` until source-level verification and user approval.

## Overall Verdict

**docs/81 revision passes the main Codex audit requirements with one remaining WARN.**

The H_FLRW overclaim was fixed, beta statistics were corrected, unsupported optimization claims were softened, w_eff wording was corrected, and safety labels are present. The only remaining issue is one residual H_MULT robustness phrase that should be softened before considering `docs/81` clean.

## Compliance Confirmation

[VERIFIED] No email sent.

[VERIFIED] No public claims made.

[VERIFIED] No validation or refutation claim made.

[VERIFIED] No MCMC run.

[VERIFIED] `docs/81_multi_ai_reproducibility_comparison.md` was not edited by this verification pass.
