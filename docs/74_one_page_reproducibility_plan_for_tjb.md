# One-Page Reproducibility Plan — AI-Assisted FLRW / MULTING Tables

**Date:** 2026-05-30  
**For:** Dr. Thomas J. Buckholtz  
**Status:** DRAFT_FOR_AUTHOR_REVIEW

---

## Purpose

This plan outlines a focused effort to make the AI-assisted table generation workflows reproducible and comparable across services.

**Goal:** Understand which assumptions and data sources reproduce the tables, and which choices lead to differences.

**Not the goal:** Validation or refutation of any framework. This is an assumption-recovery and comparison exercise, not a physics decision.

---

## Scope

We propose to examine and compare:

1. **Anthropic Claude Table A1** (from manuscript)
2. **OpenAI ChatGPT supplementary table** (mentioned in your response)
3. **Google Gemini supplementary table** (mentioned in your response)

For each table, we will focus on:

- H_FLRW column (ΛCDM expansion rate)
- H_MULT column (MULTING expansion rate)
- w_eff-related values (if present)
- Residuals and sigma values
- Reported uncertainties

---

## Method

### Step 1: Transcribe Tables

Convert all AI-service tables into machine-readable CSV format with explicit column headers and units.

### Step 2: Track Provenance

For each table, document:

- **Data source:** published summary / published table / AI extrapolation / unknown
- **Statistical handling:** averages / ranges / uncertainty propagation / AI-inferred method
- **Parameter status:** source-confirmed / AI-inferred / fitted / unknown

This creates an **assumption registry** that tracks what each service may have chosen when details were not specified.

### Step 3: Recompute Simple Columns

Verify arithmetic:

- Residuals: H_MULT - H_obs, H_FLRW - H_obs
- Sigma values (standardized deviations)
- Any derived quantities that can be checked independently

### Step 4: Compare AI-Service Outputs

Check for:

- **Agreement:** which columns are stable across ChatGPT / Gemini / Claude?
- **Disagreement:** which columns differ, and by how much?
- **Sensitivity:** small assumption changes → large output changes?

### Step 5: Classify Reproducibility

For each table element, label:

- **Reproduced exactly:** our recomputation matches reported value
- **Reproduced under recovered assumptions:** we identified which convention makes it match
- **Partially reproduced:** close but not exact
- **Not reproduced:** we cannot match the reported value
- **Under-specified:** insufficient information to attempt reproduction

---

## Requested Inputs

To proceed efficiently, we would appreciate:

1. **Supplementary tables:**
   - ChatGPT version of Table A1
   - Gemini version of Table A1
   - (These were mentioned in your response; we have not yet located them in the Supplementary Materials)

2. **Prompts (if available):**
   - What instructions were given to each AI service?
   - Were the prompts identical, or did each service receive different guidance?

3. **AI service metadata (if available):**
   - Service dates / versions (e.g., ChatGPT-4, Gemini 1.5, Claude Sonnet 3.5)
   - Any settings or preferences that were specified

4. **H_FLRW convention (if known):**
   - Which H₀, Ωₘ, ΩΛ values were intended for the H_FLRW column?
   - Was a specific cosmology calculator used, or were AI services asked to compute this themselves?

5. **β parameter status:**
   - Are β_d and β_q intended as:
     - fitted phenomenological parameters?
     - candidate fundamental constants?
     - derived from other principles?
   - Should they be treated as fixed, or as quantities to be estimated?

6. **H_MULT operational meaning:**
   - Is H_MULT(z) intended as:
     - a metric expansion rate (like H_FLRW)?
     - an effective kinematic quantity from force-law fits?
     - something else?

**Note:** If some of these are unknown or were left to AI discretion, that itself is useful information — we can document it as "AI-inferred" in the provenance registry.

---

## Output

We will produce:

1. **Machine-readable tables** (CSV)
   - All three AI-service tables in standardized format

2. **Assumption registry**
   - Data source: where each number came from
   - Statistical method: how uncertainties were handled
   - Parameter status: which values are source-confirmed vs AI-inferred

3. **Comparison matrix**
   - Which columns agree across services
   - Which columns diverge, and by how much
   - Sensitivity analysis: assumption changes → output changes

4. **Reproducibility notes**
   - What we reproduced exactly
   - What we reproduced under recovered assumptions
   - What remains under-specified

5. **Short clarification question list**
   - Focused questions for any unresolved ambiguities
   - No more than 5-10 questions total
   - Respectful, assumes we may have missed something

**Format:** Private report, shared with you for review before any further use.

---

## Boundaries (What This Does Not Include)

To keep the scope manageable and respectful, this plan explicitly excludes:

1. ❌ **No validation claim**
   - We will not claim that MULTING is "validated" by table reproduction
   - Reproducing a table ≠ confirming the underlying physics

2. ❌ **No refutation claim**
   - We will not claim that MULTING is "refuted" if tables are not fully reproducible
   - Under-specification ≠ error

3. ❌ **No public release without approval**
   - All outputs remain private unless you explicitly approve public release
   - No blog posts, no preprints, no social media about your work

4. ❌ **No MCMC comparison yet**
   - This plan does NOT include Bayesian model comparison (MCMC)
   - MCMC requires:
     - clarified bridge method (F_oP → H_MULT formula)
     - independent out-of-sample data (not the same data used for fitting β)
     - explicit complexity penalty (number of free parameters)
   - These are not yet resolved, so MCMC is deferred to a possible future phase

5. ❌ **No premature physics conclusions**
   - This is assumption-recovery work, not a final decision about FLRW vs MULTING
   - The goal is to make table workflows comparable, not to "pick a winner"

---

## Timeline (Tentative)

**Phase 1 (1-2 weeks):** Table transcription + provenance registry setup

**Phase 2 (1 week):** Recomputation + comparison across services

**Phase 3 (1 week):** Documentation + clarification question list

**Total:** 3-4 weeks from receipt of supplementary tables

**Pause points:**
- After Phase 1: share preliminary registry for your review
- After Phase 2: share comparison matrix before finalizing
- After Phase 3: share full report, wait for your feedback

At each pause point, you can redirect, request changes, or decide to stop.

---

## Why This May Be Useful

This work may help in several ways:

1. **Near-term:** Identify which assumptions make tables reproducible
   - If H_FLRW depends on specific conventions, document them
   - If AI services made different choices, document the differences
   - If some choices are more stable than others, note that

2. **Methodological:** Develop techniques for comparing AI-assisted table workflows
   - Provenance registry can be reused for other AI-generated scientific outputs
   - Comparison framework can help others assess AI-service stability

3. **Long-term (speculative):** If table workflows become robust and well-documented, they may eventually contribute to fair comparisons of FLRW, MULTING, and w_eff approaches
   - But this is a future possibility, not a current claim
   - Many steps remain (out-of-sample data, model specification, peer review)

---

## Request for Feedback

Before proceeding, we would appreciate your feedback on:

1. **Scope:** Is this focus appropriate, or should we narrow/broaden?
2. **Inputs:** Which of the requested inputs are available?
3. **Output format:** Would you prefer different deliverables?
4. **Timeline:** Is 3-4 weeks reasonable, or is there urgency?
5. **Boundaries:** Are the exclusions (no validation, no MCMC yet) acceptable?

We are happy to adjust this plan based on your guidance.

---

## Collaboration Philosophy

We approach this work with the following principles:

- **You are the expert** on the IDM/MULTING framework; we are learners attempting to understand the computational workflow
- **Assumptions first, conclusions later:** we focus on documenting what was assumed before drawing any physics conclusions
- **Transparency:** all methods, code, and intermediate outputs can be shared
- **Respectful uncertainty:** if we cannot reproduce something, we assume we missed an assumption rather than concluding there is an error

This is intended as a **collaborative clarification exercise**, not an adversarial audit.

---

**Next step:** Awaiting your response on whether this plan is appropriate, and whether supplementary tables (ChatGPT, Gemini) are available.

**Contact method:** (User will specify — email / meeting / other)

---

**Prepared by:** Reproducibility audit team  
**Date:** 2026-05-30  
**Version:** 1.0 (draft for author review)  
**Status:** PRIVATE / NOT_SENT / AWAITING_USER_APPROVAL

**Related documents (internal, not shared with author unless requested):**
- docs/71_author_response_analysis.md (detailed analysis of your response)
- docs/72_reproducibility_plan_outline_for_tjb.md (full 4-phase plan with technical details)
- docs/73_multi_ai_table_comparison_plan.md (detailed comparison workflow)
