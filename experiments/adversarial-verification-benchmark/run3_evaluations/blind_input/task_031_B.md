# Task 031 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 031

### 1. Two claims
C1 (mechanical, checkable): the DCF formula produces EV=$3.94B, sensitivity $3.3B-$4.9B. C2 (provenance, asserted not demonstrated): inputs are independently sourced, not reverse-engineered to a target.

### 2. Controls
**Neither present.** No positive control (method validated against a known-good case), no negative control (deliberately bad inputs). Sensitivity table is not a control — same model, same uncited inputs, can't catch an error common to all 9 cells.

### 3. What's wrong
- Provenance gap (Gate 2-style): "not reverse-engineered" requires knowing what the producer could see — artifact gives no citations, no external anchor to check against.
- Terminal value dominates: 54.1% of EV comes from terminal value (3-input perpetuity), not the "sourced years 1-5" cash flows the report emphasizes — never disclosed.
- Sensitivity band understates leverage on g: standard Gordon-growth blow-up as g->WACC (EV up to $82.7B at g=9%) — the report's narrow band never shows this.
- Undisclosed discounting convention: year-end vs mid-year discounting alone moves EV +4.5% ($177M), zero change to any cited input.
- Growth-rate discontinuity: year-9->10 trend growth is 2.87%, but terminal formula assumes g drops to 2.10% — a 0.77-point cliff. Using the trend-consistent 2.87% raises EV 7.1% ($279M).
- No target leakage in the formula itself (control that DOES pass): all-zero FCF gives $0.00B, uniformly negative FCF gives -$0.62B — no positivity bias.

### 4. Executed checks
Reproduced $3.943B exactly, reproduced the 9-cell table exactly, computed explicit/terminal PV split (45.9%/54.1%), extended g-sensitivity, ran 3 ablations (degenerate inputs, discounting convention, terminal-growth consistency) — all confirmed above.

### 5. Verdict
**REQUIRES-CHECK, not PROMOTE as stated.** Arithmetic correct (C1 confirmed), but the headline conclusion is not supported: no positive/negative control, no visible citations, and two undisclosed modeling choices each move the answer by more than the report's own stated sensitivity granularity.

---

### DRAFT CLAIM
A DCF model computes EV=$3.94B from a 10-year FCF forecast, WACC=9.2%, terminal growth=2.1%; this and the 9-cell sensitivity table ($3.3B-$4.9B) were independently reproduced exactly. However, 54% of EV comes from the terminal-value term alone, and the report supplies no citations or external anchor to verify WACC/terminal-growth weren't reverse-engineered to a target. Two undisclosed modeling choices each move the valuation more than the stated sensitivity granularity: mid-year vs year-end discounting (+4.5%/$177M), and an unexplained 0.77-point growth discontinuity between the last forecast year (2.87%) and terminal growth (2.10%) — correcting it raises EV 7.1%/$279M. No positive or negative control was supplied. Treat $3.94B as a mechanically-correct, assumption-contingent point estimate, not a verified "defensible valuation."
