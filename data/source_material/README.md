# Author Source Material — Handling Manifest

**Status:** Local reference copy. Content files (PDF + MD) are **NOT tracked in git**
(only this README is tracked).
**Date:** 2026-06-01

## What lives here (locally)

A 1:1 copy of Dr. Thomas J. Buckholtz's preprint, kept so the audit can reference
the primary source when needed:

| File (local only) | What it is |
|---|---|
| `buckholtz_preprints202511.0598.v6.pdf` | Original preprint, verbatim (the 1:1 source) |
| `buckholtz_preprints202511.0598.v6.md` | Markdown conversion (via `markitdown`) for token-efficient reading |
| `buckholtz_supplementary202511.0598.v6.md` | **Supplementary Material** — the A.1 prompt + 3 full AI-service transcripts (ChatGPT / Claude / Gemini). Markdown via `markitdown`. **Canonical reference for the bridge-improvisation + β-divergence findings.** Added 2026-06-05. |

**Fidelity verified (2026-06-05):** Table A1 12-row structure + all numeric values
(67.4 … 398.5, β=4.5/18.0) survived conversion intact. Main `.md` re-converted and
confirmed byte-identical to the existing copy (2773 lines / 187987 chars).

**Source:**
> Thomas J. Buckholtz, *Gravitational and Dark-Matter Concepts that Can Help Explain
> and Predict Cosmic Data*, Preprints.org, posted 21 May 2026,
> doi:[10.20944/preprints202511.0598.v6](https://doi.org/10.20944/preprints202511.0598.v6)

## Licensing

The preprint is published under **Creative Commons CC BY 4.0**, which permits free
download, distribution, and reuse **provided the author and preprint are cited**.

So redistribution is *legally* allowed with attribution. We nonetheless keep the
content **untracked** here because:

- During an **active collaboration**, we do not republish the author's work on his
  behalf; he asked to retain pre-publication control.
- Consistency with the project's publication-hygiene posture (see
  `data/supplementary_extracted/README.md`).

If the repository is ever published and you choose to include the preprint, you may
do so under CC BY 4.0 — just keep the citation above and remove the gitignore rule
`data/source_material/*` for the chosen file. That is a deliberate, attributable
decision, not a default.

## How to recreate the markdown

```bash
python -m markitdown "data/source_material/buckholtz_preprints202511.0598.v6.pdf" \
  -o "data/source_material/buckholtz_preprints202511.0598.v6.md"
```

No code in `src/` or `tests/` depends on these files; their absence does not affect
the test suite or CI. This is reference material, not analysis input.

## Scope note

Storing the source here does **not** change any analysis status: no validation, no
refutation, no MCMC, no outreach. It only makes the primary source available for
careful reference during the reproducibility work.
