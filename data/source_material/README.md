# Author Source Material — Handling Manifest

**Status:** Local reference copy. Content files (PDF + MD) are **NOT tracked in git**
(only this README is tracked).
**Date:** 2026-06-01

## What lives here (locally)

1:1 copies of Dr. Thomas J. Buckholtz's own preprints, kept so the audit can
reference the primary source when needed. **Two separate documents, not two
versions of the same one** — see the `[CANONICAL VERSION, 2026-08-30]` note
below for why this distinction matters.

| File (local only) | What it is |
|---|---|
| `buckholtz_preprints202511.0598.v6.pdf` | Original preprint, verbatim (the 1:1 source) — **the version this project's own F_oP/dipole/quadrupole/S-S-background reconstruction (docs/124-127, P1-P155) is built on.** |
| `buckholtz_preprints202511.0598.v6.md` | Markdown conversion (via `markitdown`) for token-efficient reading |
| `buckholtz_supplementary202511.0598.v6.md` | **Supplementary Material** — the A.1 prompt + 3 full AI-service transcripts (ChatGPT / Claude / Gemini). Markdown via `markitdown`. **Canonical reference for the bridge-improvisation + β-divergence findings.** Added 2026-06-05. |
| `buckholtz_202608.0943v1.v82.pdf` | **[NEW, 2026-08-30]** "Multi-Tier Newtonian Gravity: A Cosmic-Node-Based Alternative to LCDM for the Hubble Tension," Preprints.org 202608.0943v1, dated August 2026 — TJB's own current/latest work (Zenodo record 22004287, filename ends `v82`). **Substantially expanded from v6** — see `docs/149_v82_preprint_study.md` for the full comparison. |
| `buckholtz_202608.0943v1.v82.md` | Markdown conversion via `markitdown`. **Fidelity caveat (unlike v6's byte-verified conversion): prose converted well and is reliably grep-able, but numbered equations (1)-(23) came through with scattered subscripts/table-fragmentation** — cross-check any exact equation against the PDF directly (page images), don't trust the `.md` for equation-level precision. |

**Fidelity verified (2026-06-05, v6 only):** Table A1 12-row structure + all
numeric values (67.4 … 398.5, β=4.5/18.0) survived conversion intact. Main
`.md` re-converted and confirmed byte-identical to the existing copy (2773
lines / 187987 chars).

**[CANONICAL VERSION, 2026-08-30]** This project's entire F_oP/dipole/
quadrupole/Shtanov-Sahni-background reconstruction was built on **v6**,
established many months before v82 existed. TJB's own 2026-08-29 reply to a
2026-08-27 progress-report email revealed he was referencing v82 (his
current work) and was unsure which version the letter's remarks addressed
— a real, confirmed version gap, not a false alarm (see `correspondence/
tjb_reply_20260829.md`, `lessons_learned.md`'s 2026-08-29 entry). **v82 is
now the project's reference point going forward** for anything touching the
force law, the F→H(z) bridge, or cluster-property evolution — see
`docs/149_v82_preprint_study.md`. v6 remains the correctly-cited source for
every already-completed finding (P1-P155); do not silently re-attribute
those to v82 without re-checking they still hold under v82's own equations.

**Sources:**
> Thomas J. Buckholtz, *Gravitational and Dark-Matter Concepts that Can Help Explain
> and Predict Cosmic Data*, Preprints.org, posted 21 May 2026,
> doi:[10.20944/preprints202511.0598.v6](https://doi.org/10.20944/preprints202511.0598.v6)

> Thomas J. Buckholtz, *Multi-Tier Newtonian Gravity: A Cosmic-Node-Based
> Alternative to LCDM for the Hubble Tension*, Preprints.org 202608.0943v1,
> dated August 2026; also archived on Zenodo, record 22004287
> (https://zenodo.org/records/22004287).

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

python -m markitdown "data/source_material/buckholtz_202608.0943v1.v82.pdf" \
  -o "data/source_material/buckholtz_202608.0943v1.v82.md"
```

No code in `src/` or `tests/` depends on these files; their absence does not affect
the test suite or CI. This is reference material, not analysis input.

## Scope note

Storing the source here does **not** change any analysis status: no validation, no
refutation, no MCMC, no outreach. It only makes the primary source available for
careful reference during the reproducibility work.
