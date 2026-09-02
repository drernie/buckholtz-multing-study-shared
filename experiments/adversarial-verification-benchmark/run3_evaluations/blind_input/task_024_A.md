# Task 024 — baseline arm output

## Findings

**Verdict: not well-supported.** Conflates "rarely fires" with "well-calibrated"; headline number is contaminated by an unhandled data-quality issue the report itself discloses.

1. **Silent NaN swallow (verified):** `np.sqrt(np.nanmean(all-NaN window ** 2))` = nan; `nan > 0.15` = False. Every dropped window (known network-hiccup issue, per report's own context) is silently classified "not drifting," identical to a genuinely healthy reading. No exception, no log line distinguishing "confirmed quiet" from "instrument didn't report."
2. **No positive control:** report never demonstrates the detector fires on a real/synthetic drift event. A detector that never fires (miscalibrated threshold, broken comparison) would produce an equally low flag rate.
3. **Unjustified threshold=0.15**, no derivation shown.
4. **No visibility into dropout fraction** — the printed summary reports only flag rate, not how much of the 6 months was actually usable data.
5. Terminology issue: calling it a "false-alarm rate" presumes ground truth (no real drift occurred) that's never checked.

---

**DRAFT CLAIM:** The claim that a 0.02% flag rate over 6 months proves the sensor-drift detector is "well-calibrated and ready for deployment" is not supported. The code has a silent-failure bug: known network-hiccup dropouts arrive as all-NaN windows, nanmean of an all-NaN array returns NaN, and NaN > threshold evaluates False — so every dropped window is silently counted as "not drifting" with no visibility into how many windows this affected. More fundamentally, the report demonstrates only a low flag rate with no positive control (no injected/historical drift event confirmed detected), so an arbitrarily-high threshold would produce the same reassuring statistic while being useless. The claim should be downgraded from "ready for deployment" to "not yet validated" pending NaN-handling fixes and an explicit sensitivity test.
