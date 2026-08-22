# FINDING P88 — **R-CONFIRMED.** `ε(k)` survives a second, independently written implementation

**Status:** built, run, attacked, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifacts:** `P88_independent_reconstruction.py`, `p88_independence_probe.py`

> Every finding from P73 onward ends with the same line: *"Perelman condition 5 —
> still not met."* The reason was structural, not lazy. **Every step imports
> `P76_growth_observable.py`.** P80, P81, P82, P84, P87 all call the same `run()`,
> the same `contrast()`, the same integrator. When `FINDING_P82` reproduced P77's
> anchor-free slope to `1.15e-04` it still had to scope that as *weak-to-medium*
> on the Independent Verification Strength Ladder — **same model, isolated
> context** — precisely because both numbers came out of one implementation.
>
> This step writes the campaign's most load-bearing number a **second time**,
> sharing no computational code with the first.

---

## What "independent" means here, concretely

Not "written again in different words." The **formulation** differs:

| | P76 | P88 |
|---|---|---|
| independent variable | `t` | `N = ln a` |
| the scale factor | a **state variable**, `ȧ = aH` | **the axis itself** |
| `H` | integrated alongside | solved from the Friedmann **constraint**, algebraically |
| state vector | 9 components | 8 components |
| matched-`a` comparison | needs `brentq` to invert `a(t)` | free — `a` *is* the coordinate |
| integrator | `RK45` | `DOP853` |

So the Friedmann constraint is satisfied **exactly by construction** rather than
approximately by integrating `a` beside it, and an entire root-finding layer
disappears. Those are *different sources of error*, which is the whole point.

**What is shared, and must be.** The **equations** and the **initial data** are
the claim's *specification*, not its implementation. A reconstruction that solved
different equations would be measuring something else. The physics is transcribed
from the findings; the code that solves it is not.

**The trap avoided.** `FINDING_P78`'s control A3 failed *falsely* because it
compared against P77's published values **rounded to six decimals**. So P88 does
not compare against the published `0.045688`. It picks its **own** anchors
(`a₁ = 1000`, `a₂ = 400000`, chosen here) and runs **P76's own public entry point**
`G_growth` at *those same two*, at full precision. Like-for-like, no rounding.

---

## Part A — the external lock mass, before any comparison

In matter domination the growing mode is `δ ∝ a`, so `d ln δ / d ln a = 1`.
Textbook, and owed to nothing in this project — a reconstruction that cannot
reproduce it is not a reconstruction.

| `a` | `d ln δ / d ln a` | deviation |
|---|---|---|
| `1000` | `1.000001004150` | `+1.004e-06` |
| `1e4` | `1.000000003182` | `+3.182e-09` |
| `1e5` | `1.000000000016` | `+1.582e-11` |
| `4e5` | `1.000000000005` | `+4.721e-12` |

Worst `1.004e-06` against a `1e-3` threshold → **L1 PASSES.**

---

## Part B — the two implementations, at identical anchors

`(ĝ, λ) = (1, 1)`, `a₁ = 1000 → a₂ = 400000`:

| `k` | reconstruction | P76 | relative diff |
|---|---|---|---|
| `3` | `0.039909712233` | `0.039909712238` | `1.351e-10` |
| `10` | `0.045662752907` | `0.045662752908` | `1.728e-11` |
| `30` | `0.046612234153` | `0.046612234153` | `2.401e-13` |

## Part C — negative control: a corrupted reconstruction must disagree

If the comparison passes even with a deliberate bug, it proves nothing. The Euler
exchange term's sign is flipped **in the reconstruction only**:

| `k` | corrupted recon | P76 | relative diff |
|---|---|---|---|
| `10` | `0.040040431722` | `0.045662752908` | `1.231e-01` |

`12.3 %` — the comparison **discriminates**.

---

## The number was too good, so it was attacked before it was quoted

`2.401e-13` at `k=30` is **better than either code's integrator tolerance**
(`1e-11` here, `1e-10` in P76). A result more accurate than the machinery that
produced it is the exact shape this campaign has caught repeatedly: *the gate
measuring something other than what the claim asserts.* So `p88_independence_probe.py`
tried to break the verdict first. Both attacks were pre-registered.

### Attack 1 — is the agreement tolerance-limited, or **pinned**?

If both files really integrate independently, the difference is a
**discretization** difference and must degrade when either side is loosened. If
it stays near `1e-13` regardless, the numbers are not independent.
Pre-registered: `≥100×` growth → TOL-LIMITED; `<10×` → SUSPICIOUS, verdict withdrawn.

Loosening the **reconstruction** (P76 fixed at `1e-10`):

| recon `rtol` | recon `ε` | relative diff |
|---|---|---|
| `1e-12` | `0.04566275290719` | `1.728e-11` |
| `1e-10` | `0.04566275290719` | `1.739e-11` |
| `1e-08` | `0.04566275290752` | `1.017e-11` |
| `1e-06` | `0.04566275296158` | `1.174e-09` |

**This ladder is not monotone, and that is expected rather than noise.** The first
three rows sit on a **floor at `≈1.7e-11` set by P76's own fixed `rtol=1e-10`** —
tightening the reconstruction below that floor cannot help, because the *other*
side's error dominates. Only `1e-6`, where the reconstruction's own error finally
exceeds the floor, moves. Spread `115×`, carried entirely by that last row.

Loosening **P76** instead (reconstruction fixed at `1e-11`) is the clean half:

| P76 `rtol` | P76 `ε` | relative diff |
|---|---|---|
| `1e-10` | `0.04566275290798` | `1.728e-11` |
| `1e-08` | `0.04566275292098` | `3.021e-10` |
| `1e-06` | `0.04566275405624` | `2.516e-08` |

Monotone, `1460×`. **The difference is set by whichever side is looser** — the
signature of two independent discretizations converging on the same solution.
→ **TOL-LIMITED.**

### Attack 2 — execute the independence claim instead of asserting it

"Shares no computational code" was **prose**. The file draws a boundary comment at
its midpoint; that line had never been tested. The probe splits the file at its
**own** marker, `exec`s only the text **above** it into a bare namespace, and
recomputes `ε` from that fragment alone.

- marker sits at **49 %** of the file;
- fragment **runs standalone** and reproduces `0.04566275290719` — **bitwise identical**;
- mentions of P76 in the fragment's **executable text: 0**.

→ **INDEPENDENCE HOLDS.**

**This control failed on its first run, by its own fault.** The criterion was
`0 mentions of P76 in the raw text`, and the raw text has **3** — all in the module
docstring, at lines 9, 22 and 43, which *describe the comparison in prose*. The
control was measuring "does this file **talk about** P76 above the line", not
"does the code above the line **use** it."

The obvious repair — strip all string literals — would have made the test
**weaker, not sharper**: a dynamic load hides its target inside a *string*
(`spec_from_file_location("x", "P76_growth_observable.py")`), and the fragment
inherits `import importlib.util` from the file's import block, so that escape
route is genuinely open. The fix removes **only the module docstring**, located by
AST position, and comments by tokenizer. Every other string stays visible.
Fifth control this session to fail by the control's own construction; recorded
rather than quietly retuned.

---

## Verdict

**R-CONFIRMED.** Worst relative difference `1.351e-10`, against a pre-registered
`< 1e-4`. Two implementations sharing no computational code — different
independent variable, different state vector, different integrator, Friedmann
exact by construction versus integrated — agree on `ε(k)`.

**Perelman condition 5 is met at the "independently-written code" rung, for
`ε(k)` only.**

### And not above it

- The **same person** wrote both implementations. A different **model**, a **blind
  replication** by another group, and a **new physical experiment** all remain
  absent. On the campaign's own Independent Verification Strength Ladder this is
  **Strong** — not *Very strong*, not *Strongest*.
- It reconstructs **`ε(k)` only**, at `(ĝ, λ) = (1, 1)`. `μ_tot == 1`, the viability
  boundary, the growth rate `f`, the scaling group — **untouched**, each needing
  its own reconstruction.
- **A reconstruction tests the implementation, never the specification.** If both
  files solve the same *wrong* equations they will agree beautifully. Nothing here
  says the shared equations are right.
- Nothing observational. `NO_BRIDGE_FITTING` untouched. Nothing about MULTING
  itself (Gate 1).

### Left unexplained, deliberately

Why `k=30` agrees to `2.4e-13` while `k=10` sits at `1.7e-11` — i.e. why the error
cancellation in the double ratio improves with `k` — was **not measured**. The
probe establishes that the difference is tolerance-limited and floor-set; it does
not establish the `k`-dependence of the floor. Per P87's lesson, no mechanism is
narrated for a direction that was merely observed.
