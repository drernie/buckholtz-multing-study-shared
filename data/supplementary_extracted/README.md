# Supplementary-Extracted Tables — Handling Manifest

**Status:** Intentionally **NOT tracked in git** (public-safety / publication hygiene).
**Date:** 2026-06-01

## What these files are

This directory holds CSV tables (`*.csv`) **derived from Dr. Thomas J. Buckholtz's
author-provided Supplementary Material** — specifically the per-service outputs
(ChatGPT / Claude / Gemini) extracted during the reproducibility audit
(parameters, approximate-match tables, w_eff comparisons, recap parameters).

## Why they are not in git

- They are **derivative tables of unpublished, author-provided material**.
- The author has indicated he wants to edit/delete material before any publication.
- The maintainer has committed not to publish anything that mentions the author's
  work without his input first.

Tracking these tables would risk redistributing them if the repository ever becomes
public. They are therefore listed in `.gitignore`
(`data/supplementary_extracted/*.csv`) and excluded from version control.

**This is a hygiene measure only. It does NOT change any analysis result, status,
or scientific claim.** Local copies are preserved on the maintainer's machine.

## How to recreate locally

These tables are reconstructed **only from the source Supplementary Material, with
appropriate permission**, using the extraction workflow documented in:

- `docs/76_supplementary_materials_inventory.md` — inventory of source materials
- `docs/77_multi_ai_table_extraction_summary.md` — extraction summary
- `docs/78_csv_integrity_audit.md` — CSV integrity checks
- `docs/41_table_a1_transcription_notes.md` — transcription notes

Place the recreated CSVs back in this directory. No code in `src/` or `tests/`
depends on these files, so their absence does not break the test suite or CI.

## What MAY be shared

Repository docs may **describe** the extraction workflow and report aggregate,
non-redistributive observations (e.g. "inter-service beta spread was 94.7×").
The **derived tables themselves are not redistributed by default**.
