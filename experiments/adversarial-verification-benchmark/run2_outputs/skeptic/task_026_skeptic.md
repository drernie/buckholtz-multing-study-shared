# Skeptic sub-call — task_026

**Note on provenance:** `Write`/`Edit` denied by the systemic
`agent-tool-scope-guard` block (see task_012/013/014/016/020/021/022).
This file transcribes the subagent's own chat-response text.

## Verdict

**CONFIRMED-REAL**

## Independent verification performed (subagent's own words, verbatim)

Checked directly against `task.md`: the report validates only on
same-distribution held-out data (its own comment says so) and deploys on
an explicitly different distribution (phone-camera crops from an
unreliable upstream service — also stated in the artifact's own
comment). `predict_digit`/`run_inference_service` have zero shape/dtype/
range validation (confirmed by reading the code — the "No input
validation" comment is verbatim in the source). Traced `.reshape(1,784)`
semantics manually (no code-execution tool was available in this
session): a size-mismatched crop raises an unhandled `ValueError`; a
size-matched but wrong-scale/dtype input passes silently through
`/255.0` with no error signal — exactly the two failure modes the claim
describes, and they're logically exhaustive.

**Caveat, stated by the subagent itself:** the specific "~49-point" drop
figure is unverifiable (no experiment artifact given to reproduce it)
and the claim itself labels it "stand-in" — not load-bearing for the
verdict.

Files read: `run2_outputs/skeptic_input/task_026_claim.md`,
`corpus/task_026/task.md`, `protocol_v1.0/falsification-ladder.md`.
