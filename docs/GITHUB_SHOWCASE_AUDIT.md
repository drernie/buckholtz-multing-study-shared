# GitHub Showcase Audit — buckholtz-idm-multing-mvp

**Date:** 2026-06-18 · **Mode:** read-only audit (no fixes applied, no push, not made public)
**Auditor evidence policy:** every metric below is `[VERIFIED]` by a tool run on this machine
(py3.13, branch `feature/appendix-a1-doc-updates`). CI numbers may differ slightly by environment.

---

## 1. Executive Verdict

> **UPDATE 2026-06-18 (post-fix):** Blockers 1 & 3 RESOLVED — ruff now clean (49→0, verified),
> the 3 drift-prone static badges replaced with a **live CI badge** + a dated quality snapshot
> (853 pass · 12 skipped · 0 failed · 78% cov), README "Project Structure" rewritten to a stable
> top-level tree, and `docs/INDEX.md` brought current (now covers docs 71–121). **Remaining
> blocker: #2** (tracked private correspondence / public-vs-private decision) — intentionally left
> to the author's call. Revised score **~8/10** — private-showcase ready; public still gated on
> correspondence handling + Dr. Buckholtz's approval. Original audit below is kept as the baseline record.

**Baseline (pre-fix): 5.9/10 → Target after fixes: ~8.5/10.**

The repository is **scientifically honest and well-disciplined** (pervasive NOT_VALIDATION framing,
evidence markers, explicit non-goals, robust `.gitignore`). Its showcase weakness is **not** the
science — it is **three false headline badges** and **tracked private correspondence**.

**Top 3 blockers:**
1. **All 3 status badges are wrong** (hand-set static shields.io, not live CI):
   tests `542`→**real 853**, coverage `91%`→**real 78%**, `ruff clean`→**real 49 errors**.
2. **Private author correspondence is git-tracked** — publishing the repo publishes letters,
   email drafts, call-confirmation, and Dr. Buckholtz's verbatim shared procedure.
3. **CI is currently red** — `ci.yml` runs `ruff check .`; 49 lint errors fail that step.

None of these touch the core value; all are fixable in ~1–2 hours.

---

## 2. Score Table

| Dimension | Score | Basis |
|---|---|---|
| First impression | 6/10 | Strong README, but the first thing a reviewer sees (3 badges) is all wrong |
| Truthfulness | 6/10 | Body claims honest & hedged; headline badges false |
| Reproducibility | 8/10 | Datasets now committed, scripts runnable, CI matrix, clear quickstart |
| Engineering hygiene | 6/10 | 853 tests pass, excellent gitignore; but ruff red + coverage badge inflated |
| Visual clarity | 6/10 | No diagram, no social preview; tables are good |
| Documentation structure | 6/10 | README solid but "Project Structure" badly stale; 119 docs, no index |
| Public-safety readiness | 4/10 | PDFs/supplementary/secrets protected; **correspondence tracked** |
| Portfolio value | 7/10 | Demonstrates rare epistemic rigor + real physicist collaboration |
| Reviewer confidence | 6/10 | Senior scientist respects discipline; loses trust on wrong badges |
| Adversarial robustness | 4/10 | Fails Stage-10.1 count-drift on all 3 badges |
| **Weighted average** | **5.9/10** | |

---

## 3. Best Positioning Sentence

> This repository is a **reproducibility & provenance-audit scaffold** that helps **research
> collaborators and senior scientists** **separate what is source-confirmed, fitted, inferred, and
> unknown** in Thomas J. Buckholtz's IDM/MULTING framework, by **executable epistemic registries +
> tool-verified numerical checks**, while explicitly avoiding **any claim that the theory is validated
> or refuted.**

Primary audience: **Research collaborator / senior scientist** (the author himself is the #1 reader).
Secondary: **employer/recruiter** (portfolio piece on epistemic engineering).

---

## 4. Audience-Specific First Impression

- **30 sec:** README hero + disclaimers + "what this actually reproduces" — *excellent*, already
  communicates honest scope. Undermined only by the 3 wrong badges directly above it.
- **3 min trust:** evidence markers, non-goals, Rosetta stone, status taxonomy — *strong*. A skeptic
  would then check the badges, find them wrong, and discount the rest. **Fix badges first.**
- **10 min run:** `pip install -r requirements.txt && pytest` works (853 pass). Datasets now present.
  `ruff check .` fails — a reviewer running the documented commands hits 49 errors.

---

## 5. Engineering Hygiene Findings (14-check matrix)

| Check | Result | Evidence |
|---|---|---|
| Tests pass | ✅ 853 passed, 12 skipped, 0 failed | `[VERIFIED]` exit=0; 865 collected − 12 skipped |
| Lint pass | ❌ 49 errors | `[VERIFIED]` `ruff check .` |
| CI exists | ✅ `.github/workflows/ci.yml`, py3.11–3.13 | `[VERIFIED]` |
| CI currently green | ❌ ruff step fails | `[INFERRED]` from 49 ruff errors on tracked files |
| LICENSE | ✅ MIT, ORCID attributed | `[VERIFIED]` |
| CITATION.cff | ✅ present, cites preprint DOI (CC BY 4.0) | `[VERIFIED]` |
| CHANGELOG.md | ✅ present; entry shows prior 533/72% | `[VERIFIED]` |
| No tracked `__pycache__` | ✅ clean | `[VERIFIED]` `git ls-files` |
| No tracked secrets/.coverage | ✅ clean | `[VERIFIED]` |
| No tracked PDFs | ✅ clean (gitignored) | `[VERIFIED]` |
| No third-party source material | ✅ only `source_material/README.md` tracked | `[VERIFIED]` |
| `.gitignore` correct | ✅ excellent (PDFs, supplementary, .env, correspondence notes) | `[VERIFIED]` |
| Version matches tag | ✅ pyproject `0.3.0` == tag `v0.3.0` | `[VERIFIED]` |
| Reproducibility scripts have data | ✅ fixed 2026-06-18 (`data/*.csv` committed) | `[VERIFIED]` |

### Real metrics vs badges (Stage 10.1 count-drift)
| Badge claims | Reality `[VERIFIED]` | Drift |
|---|---|---|
| `tests 542 passed` | **853 passed, 12 skipped** | +311 |
| `coverage 91%` | **78%** (3292 stmts, 711 missed, src/) | −13 pts |
| `lint ruff clean` | **49 errors** | false |

All three badges are **static hand-set shields.io URLs**, not live CI badges → they cannot self-update
and have drifted. This also violates the user's own global rule ("never hand-edit test/coverage badges").

### Ruff error breakdown (49)
| File | Count | Codes | Tracked |
|---|---|---|---|
| `audit/self_consistency_diagnostic.py` | 42 | 40×F541 (f-string no placeholder) | yes |
| `src/cluster_data_pipeline.py` | 4 | B905 (zip strict), I001 | yes (committed 2026-06-18) |
| `code/beta_cv.py` | 2 | B905 | yes |
| `src/pearson_fit.py` | 1 | F841 / B904 | yes (committed 2026-06-18) |

**41 of 49 auto-fixable** (`ruff check --fix`); ~8 need manual (`strict=` on zip, `raise ... from`).

---

## 6. Public-Safety Findings (Stage 7) — **BLOCKER for public release**

`.gitignore` correctly excludes the heavy-risk items (preprint PDF, supplementary CSVs, secrets).
**But private correspondence is tracked** and would go public on release:

| Tracked file | Risk |
|---|---|
| `docs/117_tjb_authored_procedure.md` | Dr. Buckholtz's **verbatim** shared AI-procedure — republishing without explicit permission |
| `docs/121_letter_to_tjb_draft.md` | Letters addressed to the author |
| `docs/103`, `104`, `26` | Author clarification drafts |
| `docs/75`, `85`, `93`, `98` | Email drafts |
| `docs/call_confirmation_draft_2026_06_10.md` | Call/Zoom logistics |
| `OUTREACH_TEMPLATE.md` | Outreach correspondence |
| `TJB_DIAGNOSTIC_BRIEF.md` | 32K brief containing call-derived findings (Q6/Q7) |

The preprint itself is CC BY 4.0 (DOI 10.20944/preprints202511.0598.v6) — redistribution-with-attribution
is *legally* fine, but **collaboration is active**, so courtesy + relationship risk dominate the legal status.

**Recommendation:** keep repo **PRIVATE** until (a) badges fixed, (b) correspondence untracked or
author-approved, (c) explicit go from Dr. Buckholtz on what may be public. Do **not** publish on his behalf.

---

## 7. Overclaim Gate (Stage 8)

The README claim-discipline is **strong** — no marketing language, explicit "does NOT validate/refute".
The only overclaims are the badges (Stage 10.1), classified `[UNSUPPORTED]` → must be regenerated, not hand-edited.
Body numerical results (Eq.32 0.17σ, N=5 5.8σ, ΔAIC +2.5, Pearson r) match the corrected source files `[VERIFIED]`.

---

## 8. Documentation-Structure Drift

README "Project Structure" section is **stale**:
- lists docs `01–22` (19 files) — repo actually has **119** docs.
- lists **6** test files — repo actually has **46**.
- `git ls-files docs/*.md` = 122 vs 119 on disk → a few tracked docs deleted from working tree (index drift).

119 docs with no index is **doc sprawl** — a reviewer cannot navigate it. Recommend a `docs/INDEX.md`.

---

## 9. Prioritized Fixes

### 30-minute fixes (high ROI)
1. **Fix ruff, then make badges true.**
   ```bash
   ruff check --fix .                 # clears 41
   ruff check .                       # fix remaining ~8 manually (zip strict=, raise from)
   pytest -q                          # confirm 853 pass
   pytest --cov=src --cov-report=term # read real % (78 now; will rise after ruff/test changes)
   ```
   Then edit `README.md:3-5` badges to the **real** numbers (or replace with a live GitHub Actions
   badge: `![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)`).
2. **Untrack private correspondence** (keeps local copies):
   ```bash
   git rm --cached docs/117_*.md docs/121_*.md docs/103_*.md docs/104_*.md \
     docs/75_*.md docs/85_*.md docs/93_*.md docs/98_*.md docs/26_*.md \
     docs/call_confirmation_draft_2026_06_10.md OUTREACH_TEMPLATE.md TJB_DIAGNOSTIC_BRIEF.md
   # add a correspondence/** ignore rule + a MANIFEST.md explaining exclusions
   ```
   (Only if heading toward public. If staying private, defer — but decide consciously.)

### 2-hour fixes
3. **`docs/INDEX.md`** — table of the 119 docs grouped by theme (audit / bridge / author / null-results).
4. **README "Project Structure"** — regenerate from real tree; or trim to top-level dirs + point to INDEX.
5. **Visual layer** — one Mermaid architecture diagram (inputs: PDG/CODATA + catalogs → registries →
   tests → epistemic verdicts → boundaries) in `docs/ARCHITECTURE.md`.

### Before-public-release checklist (mandatory gates)
- [ ] All 3 badges verified against a real CI run (not hand-set)
- [ ] CI green on all 3 Python versions
- [ ] Correspondence untracked OR author-approved for publication
- [ ] Explicit written go from Dr. Buckholtz
- [ ] `git log -p` scan for author quotes / private content in commit history
- [ ] Repo description + topics set; social preview image attached

---

## 10. Adversarial Audit (Stage 10) — verdict

- **10.1 count-drift:** ❌ FAIL — 3/3 badges drifted (tool-recomputed above).
- **10.2 hostile reviewer:** performed inline with tools (stronger than reasoning-only). A hostile
  reviewer's first move — "do the badges match?" — breaks immediately. After badge fix + correspondence
  handling, the repo's honest framing survives scrutiny well.
- **Verdict:** **NOT adversarial-ready today** (badge drift). **Public release: BLOCKED** (correspondence
  + badges). As a **private** collaborator/portfolio showcase it is already strong (≈7/10 ignoring badges).

---

## Final Report

- **Files changed by this audit:** 1 (this document). No fixes applied — read-only mode.
- **Tool results:** 853 passed / 12 skipped / 0 failed `[VERIFIED]`; coverage 78% `[VERIFIED]`;
  ruff 49 errors `[VERIFIED]`; sensitive-data scan clean except tracked correspondence `[VERIFIED]`.
- **Final score:** 5.9/10 (target ~8.5 after the 30-min + 2-hr fixes).
- **Public release readiness:** **BLOCKED** — fix badges, handle correspondence, get author approval.
