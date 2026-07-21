# Lessons Learned — Process & Tooling

**Scope note:** this file is for *workflow/tooling* lessons — how we work, not what we
found. Falsified *scientific* claims belong in `null_results/` with the full FL template
(Claim / Why falsified / Kill Analysis / Relaxation Map / Forbidden use) — do not put a
scientific null result here just because it "felt like a lesson." Cross-reference instead.

---

## 2026-07-22 — "Narrow test, class claim" — over-generalizing one branch to a theory family

The P3 fσ8 test (docs/128) modeled ONE dipole channel (intrinsic-random orientation),
ONE parametrization (scale-independent constant), ONE data point (z=0.07), at FIXED
Ωm — and the draft conclusion generalized to "MULTING dipole is degenerate with ΛCDM
at linear order." A context-asymmetry skeptic FALSIFIED it on five independent holes,
the strongest being an untested SECOND physical channel (induced/tidal polarization,
Blanchet DDM) that the isotropic-averaging argument simply does not cover. The clean
0.06σ data match and a working positive control made the draft LOOK solid — the gap
was in physics *scope*, not numerics.

**Takeaway:** when a test fixes a branch/parametrization/dataset/nuisance-parameter,
the licensed claim is scoped to exactly those choices — generalizing to "the theory
class is degenerate" silently asserts the untested branches behave the same. The
tell: a clean result with a working control still deserves a skeptic pass on
*coverage* ("what did I hold fixed, and does a real alternative violate it?"), not
just on correctness. This is the 4th skeptic catch this session and the first on
physics-modeling scope rather than an internal error — and it re-routed P3 into Q006
(the Lagrangian), turning an "interesting theory question" into a load-bearing
kill-condition.

## 2026-07-21 — "Algebraic revival of a physical null" — a named failure mode the skeptic caught

Ran the P1 Factorization Gate to test whether NR-016's obstruction could be lifted.
Found (sympy-exact) that `F_oP` factorizes into a global 2×2 matrix kernel with
per-object charge `(m_i, k_i r_i)` — cleanly escaping the *algebraic* single-kernel
problem NR-016 hit. It was tempting to read this as "NR-016's obstruction is
non-fatal, Shtanov is revived." A context-asymmetry skeptic pass (given only the
algebra + the interpretation, not the reasoning) named the exact error: **the
obstruction is not algebraic but about cosmological CLOSURE — the evolution law for
`k_i r_i` is missing from the corpus, so resolving the algebra leaves the closure
question fully open.** The factorization was itself motivated by wanting to rescue
the mapping (AOG-5 fail). (Second-order lesson, added same day after user review: the
skeptic itself over-stated this as "no conserved background *exists*" — a same-model
pass is Weak-Medium independence and cannot certify non-existence; the honest label
is "MISSING from corpus," and the robust check is the `docs/126` counterexample. Even
the tool that catches overclaims can overclaim.)

**Takeaway (the pattern, worth naming):** when a killed result gets "revived" by a
cleaner equation-level rewrite, check whether the rewrite touches the *reason* it was
killed or only the *symptom*. If the original kill was physical (conservation,
symmetry, dimensionality) and the revival is algebraic (factorization, change of
variables, reparametrization), the revival is cosmetic — the null stands. This is the
**third** skeptic catch this session (NR-015 statistical, NR-016 universality
assumption, this one algebraic-vs-physical) and the cleanest illustration that the
context-asymmetry pass earns its cost specifically on *self-authored* results that
look too tidy. Full content: `docs/125`; the surviving algebraic fact is a pearl
(2026-07-21), not a bridge.

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
