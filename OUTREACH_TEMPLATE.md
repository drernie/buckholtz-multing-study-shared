# Email Template for Dr. Buckholtz

> ## ⚠️ DEPRECATED (2026-06-01)
>
> This template is **superseded** and kept for history only. Do **not** send it.
> - The beta values quoted below (4.25 / 0.78 / 8.10 / 0.19) are **AI-service outputs
>   (Gemini / ChatGPT), not the actual Table A1 caption pair** (β_d=4.5, β_q=18.0, Claude).
> - Author contact is already an **active two-way collaboration**; the current,
>   source-checked outreach lives in `correspondence/buckholtz-log` (vault) and
>   `docs/93_author_one_page_update.md`.
> - Current bottleneck is the **H_MULT(z) procedure**, not beta normalization.
>
> Use `docs/93` / the correspondence log instead.

---

**Status:** DEPRECATED draft template (historical) — do not send

**Purpose:** (historical) Request beta_d and beta_q clarification in respectful, non-threatening manner

---

## Subject Line (choose one)

- "Question about beta_d and beta_q definitions in IDM/MULTING"
- "Request for clarification: beta parameters in MULTING framework"
- "Reproducibility audit — beta_d / beta_q normalization question"

---

## Email Body

```
Dear Dr. Buckholtz,

I have been working through your IDM/MULTING framework and have built 
a small reproducibility-oriented audit for my own understanding. My goal 
is not to validate or challenge the theory, but to organize what is clear 
and what requires verification before proceeding with computational work.

The main point I would like to clarify is the status of beta_d and beta_q.

I have encountered several candidate values (4.25 / 0.78 for beta_d, 
8.10 / 0.19 for beta_q) and noticed some simple numerical relations 
between them. To avoid misrepresenting your framework, I wanted to ask:

1. Are these different normalizations of the same parameter, 
   or different parameters for different contexts?

2. What are the units (dimensionless, length, length²)?

3. Which values should be used for H(z, beta_d, beta_q) calculations?

If it would be helpful, I can share a short 2-page clarification brief 
summarizing the numerical patterns I observed.

I understand you may be busy, so no pressure to respond immediately. 
Any guidance would be greatly appreciated.

Respectfully,
[Your Name]
[Affiliation if applicable]
```

---

## Alternative: Shorter Version

```
Dear Dr. Buckholtz,

I am working on a reproducibility audit of IDM/MULTING for my own understanding.

Before implementing H(z) calculations, I would like to clarify the beta_d and 
beta_q definitions. I have encountered candidate values (4.25 / 0.78 for beta_d, 
8.10 / 0.19 for beta_q) and am unsure whether these represent different 
normalizations, model versions, or different physical quantities.

Could you clarify:
- Which values are current?
- What are the units?
- Are they derived from IDM structure or fitted to data?

Thank you for your time.

Best regards,
[Your Name]
```

---

## Attachment Options

### Option 1: No attachment (safest first contact)
Include brief summary in email body, offer to share more if interested.

### Option 2: Attach brief only
Send `docs/12_beta_clarification_brief.md` (2 pages, focused on question)

### Option 3: Link to repository (only if requested)
Provide GitHub/GitLab link after initial response

---

## Communication Principles (Review Before Sending)

### DO ✅

- Frame as "request for clarification to avoid misunderstanding"
- Acknowledge you may have missed something
- Emphasize goal is strengthening reproducibility
- Keep tone curious, not accusatory
- Be patient with response time

### DO NOT ❌

- Say "your model has problems"
- Say "we found inconsistencies"
- Say "AI/Claude helped me"
- Demand immediate response
- Send unsolicited repository dump
- Claim to have validated or refuted anything

---

## Expected Response Scenarios

### Scenario A: Quick clarification
"Oh, those are just different normalizations. Use 4.25 Mpc² for beta_d."

**Action:** Thank him, update repository, proceed with H(z)

---

### Scenario B: Detailed explanation
Sends paper draft, derivation, or longer explanation.

**Action:** Read carefully, update repository, send follow-up thanks

---

### Scenario C: "It's in the paper"
References publication you may not have access to.

**Action:** 
- Ask politely if he can share preprint or summary
- Check arXiv / ResearchGate
- If unavailable, document as "requires publication access"

---

### Scenario D: No response
No reply after 2-3 weeks.

**Action:**
- Send one gentle follow-up after 2 weeks
- If still no response, document blocker in repository
- Publish repository as "incomplete pending clarification"
- Move to other projects

---

### Scenario E: Defensive response
"Why are you questioning my work?"

**Action:**
- Reiterate you're trying to understand, not criticize
- Emphasize you reproduced Eq.15 successfully
- Offer to share positive findings (numerical relations)
- If still defensive, politely withdraw

---

## Follow-Up Protocol

### If he responds positively:

**Send within 48 hours:**
```
Dear Dr. Buckholtz,

Thank you for the clarification on [specific point].

I have updated my reproducibility audit accordingly and can now 
proceed with [next step]. If you would like to see the technical 
analysis, I am happy to share the repository.

Best regards,
[Name]
```

### If he asks for more details:

**Attach:** `docs/12_beta_clarification_brief.md`

**Or link to:** Repository (after making it public)

---

## Timeline

**Week 1:** Send initial email (short version preferred)

**Week 2-3:** Wait for response

**Week 3:** Send gentle follow-up if no response:
```
Dear Dr. Buckholtz,

I wanted to follow up on my previous email about beta_d and beta_q 
definitions. No rush — I understand you may be busy. Any guidance 
would be helpful when you have time.

Best regards,
[Name]
```

**Week 4+:** If still no response, document blocker and move forward with repository publication

---

## Pre-Send Checklist

Before clicking "Send":

- [ ] Reviewed email for respectful tone
- [ ] No claims of validation or refutation
- [ ] No mention of AI assistance
- [ ] Clear, specific question
- [ ] Polite, patient tone
- [ ] Correct email address
- [ ] Affiliation/context provided (if applicable)
- [ ] Attachment (if any) is appropriate
- [ ] No typos or grammar errors

---

## Contact Information Research

**Before sending, verify:**
- Latest email address (check recent publications, personal website, university page)
- Preferred contact method (some researchers prefer ResearchGate messages)
- Current affiliation (may have changed since older publications)

**Sources to check:**
- arXiv author page
- ORCID profile
- Google Scholar
- ResearchGate
- Personal/institutional website

---

**Status:** Template ready. Customize and send when appropriate.

**Recommendation:** Start with **shorter version**, offer brief as follow-up if interested.
