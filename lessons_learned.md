# Lessons Learned — Process & Tooling

**Scope note:** this file is for *workflow/tooling* lessons — how we work, not what we
found. Falsified *scientific* claims belong in `null_results/` with the full FL template
(Claim / Why falsified / Kill Analysis / Relaxation Map / Forbidden use) — do not put a
scientific null result here just because it "felt like a lesson." Cross-reference instead.

---

## 2026-07-19 — Skeptic review caught a silent universality assumption in a literature-application claim

Applied Shtanov & Sahni (arXiv:1010.6205, real, verified) to `F_oP` — mapped the
two-body potential into their `φ(r)=-(G/r)f(r)` form via `φ≡V(r)/(m_A m_P)`, got a
clean, computer-algebra-verified `G_eff=G` result (dipole/quadrupole vanish from
background `H(z)`). Independent context-asymmetry skeptic review found the mapping
silently assumed `B`, `C` (dipole/quadrupole coefficients) were bilinear in
`(m_A,m_P)` alone — checking the primary source directly (not memory) showed `k_A`
is defined as "internal kinetic energy of object-A," a per-cluster physical
quantity, not something reducible to a mass product. The universal-kernel
requirement Shtanov & Sahni's whole derivation depends on was not actually met.
Full writeup: `docs/124`, formally registered as `null_results/20260719-nr016...`.

**Takeaway:** the same discipline that caught NR-015 (2026-07-18, a self-authored
statistical claim) also caught a self-authored *literature-adaptation* claim one day
later — a different failure mode (silent scaling assumption vs. a mis-dated
threshold) but the same fix: adversarial review before presenting a clean-looking
derivation as established, especially when the "clean" result is a symbolic limit
that looks too tidy to be wrong.

## 2026-07-18 — Skeptic review caught an inaccurate self-authored claim before it shipped

Wrote NR-015 ("T_X shared-variable artifact") with an "ARTIFACT-CONFIRMED" verdict and a
threshold I described as "pre-registered 2026-07-01." An independent context-asymmetry
skeptic review (no session history, just the file + code) caught two real problems: the
`<0.20` sub-threshold was actually written into the script the same day as the run, not
pre-registered a month earlier; and a genuine competing explanation (dynamical state as a
common physical driver) existed and wasn't distinguished from the "definitional artifact"
reading. Confirmed with a bootstrap CI that the point estimate was statistically fragile.
Rewrote the file, softened the verdict, corrected the paper.

**Takeaway:** running a skeptic pass on your OWN high-confidence conclusion — not just on
external documents — catches things a second read of your own work does not. This session
had already applied that discipline to *external* adversarial reviews several times; this
was the first time it caught something self-authored, and it worked. See
`null_results/20260718-nr015-tx-shared-variable-artifact.md` for the full scientific
content; this entry is about the *process* that caught the error, not the error itself.

## 2026-07-18 — Testing a new agent type against a known-solved problem is a cheap, real eval

Ran the new `boyko-agent` type against H1e without telling it the answer was already known
(NR-014 existed). It found the existing kill via `null_results/` first (did not blindly
redo the work), launched its own independent verifier sub-agent for a genuine re-execution,
and surfaced an overdue pearl (the M_gas-only retest, 3 days late) that led directly to
NR-015. This is a reusable pattern for evaluating any new tool/agent in this project: give
it a task with a known ground truth, don't reveal the answer, and check whether it
discovers existing state before acting.

**Caveat:** its final responses twice got cut off mid-synthesis and needed a follow-up
message to retrieve the full report — an infrastructure limitation of long-running
background agent calls in this environment, not a capability gap in the agent itself.

## 2026-07-17/18 — A hook that logs commits can create an infinite loop if it doesn't
## recognize its own output

`~/.claude/hooks/post_commit_memory.py` (global, not project-specific) fires on every
`git commit`, including a commit that contains only the auto-log line it wrote after the
*previous* commit. Without a guard, this loops: commit → hook appends a line → committing
that line triggers the hook again → repeat. Fixed with a diff-shape check (is this commit's
entire diff just auto-log-pattern additions to one file?) rather than a commit-message
check, so it's robust regardless of what message a human or agent uses for the follow-up
commit. Not specific to this project, but repeatedly hit *in* this project's sessions —
worth knowing if a session seems to be generating an unusual number of `chore: auto-log
entry for <hash>` commits in a row.

## 2026-07-17 — Obsidian-vault MCP's prompt-injection scanner has false positives on
## ordinary markdown

Writing a note containing inline-code backticks (`` `master` ``, `` `paper/main.tex` ``)
and bare `|` characters outside table syntax twice triggered a "command_injection"
false-positive block. Removing backtick-wrapped inline code and rewording bare pipes into
prose (not table cells) resolved it. If a vault write is rejected with a generic injection
warning and the content is plainly benign markdown, suspect this before assuming the
content itself is the problem.

## Standing gaps flagged but not yet acted on (tracked, not forgotten)

- `symbols.md` variable registry — flagged 2026-07-01 (research-methodology.md's own gap
  #2), still not created as of this entry.
- `activeContext.md`/`goals.md` memory bloat (auto-summarization hook stacking
  `[summarized]` tags without condensing) — flagged in the 2026-07-17 research-audit, not
  yet cleaned up.
- Bootstrap CIs not yet computed retroactively for H1a/c/d/e's own point estimates (only
  done for the new NR-015 test) — see `decisions.md`.
