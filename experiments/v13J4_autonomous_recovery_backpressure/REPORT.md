# Neural Glyph v13J4 — Autonomous Recovery Backpressure / Safe-Window Drain

**Verdict: KEEP.** The regional recovery reservoir can double as a decentralized pending-recovery buffer, but it cannot be allowed to rise indefinitely. The correct control is local and event-driven: live analog work blocks the facade drain; `CAPTURED/DONE + reservoir pressure` opens the chip-level recovery path in the next safe window.

## New terms
- **Recovery Backpressure:** the regional reservoir voltage itself represents how urgently accumulated expired charge should be drained.
- **Safe-Window Drain:** a local recovery valve that may open only after the active weak-analog result is captured.
- **Autonomic Recovery Gate (ARG):** `expired/recovery-present AND captured/done AND not weak-analog-active` controls the facade drain; no central per-event scheduler is required.

## 1. Why this is needed
v13J3 showed that multiple simultaneous high-swing facade transitions can consume weak analog margin. Therefore recovery should normally wait until the analog decision has completed.

But waiting creates another problem: the regional recovery reservoir fills.

Use the preserved v13P12 reference:
- 10 pF shared recovery reservoir across four tiles;
- initial/recovery-low state ~0.199 V in the quoted interval;
- ~220 fJ stored in one four-tile recovery interval.

Treat each ~220 fJ interval only as a first-order packet for the backpressure screen.

## 2. Backpressure model
For a 10 pF capacitor starting at 0.199 V, adding 220 fJ packets without draining gives approximately:

| packets waiting | reservoir voltage |
|---:|---:|
| 0 | 0.199 V |
| 1 | 0.289 V |
| 2 | 0.357 V |
| 4 | 0.464 V |
| 5 | 0.510 V |
| 8 | 0.626 V |
| 16 | 0.862 V |
| 18 | 0.912 V |

This is an energy-on-capacitor model, not a PDK transient of repeated complete tile lifecycles.

### Consequence
The 10 pF regional reservoir is a **short-term buffer**, not a long-term chip battery. If the next stage is not drained, its voltage will eventually move into a region that can interfere with the original recovery/lease behavior.

## 3. Selected decentralized control
Use existing robust lifecycle signals rather than inventing a central recovery controller.

Conceptual gate:

`ARG = RECOVERY_PRESENT & CAPTURED_OR_DONE & !WEAK_ANALOG_ACTIVE`

Operation:
1. weak analog evidence/Grammar/context is active -> facade recovery valve is forced closed;
2. result is captured -> live information no longer depends on that high-impedance state;
3. expired local charge reaches the regional reservoir;
4. regional voltage/backpressure rises;
5. in the first safe window, ARG opens the route to the facade/chip collector;
6. when the regional bank is back below its reset/low boundary, the valve closes.

The exact threshold/device is not selected yet; it must be PVT-tracked or self-referenced, not one fragile absolute threshold.

## 4. Why the reservoir itself is useful control
This reuses old v11/v12 thinking instead of adding a counter:
- charge amount represents accumulated recovery urgency;
- no digital count of expired events is required in the fast path;
- a large packet or several small packets naturally raises pressure faster;
- if no recovery arrives, the drain stays inactive;
- the local reservoir continues its original computational/recovery job.

The mechanism is analogous to the project's familiarity/lease philosophy: electricity stores the recent physical condition directly.

## 5. Interaction with facade quiet window
Preferred policy is **zero high-swing facade activity during weak analog integration**.

If an emergency robust utility must switch anyway, v13J3's conservative coupling screen says the present high-margin budget would tolerate roughly:
- up to four aligned 0.9 V utility transitions;
- up to three at 1.2 V;
- up to two at 1.8 V;

using the deliberately conservative ~0.124 fF per-line coupling proxy. These are stress-model limits, not permissions for the normal schedule.

Normal recovery still waits for `CAPTURED/DONE`.

## 6. Drain-frequency implication
Because ~2 stored packets already raise the 10 pF model above ~0.35 V, a small regional bank should normally be drained every one/few regional recovery episodes when a safe window is available. Large batching belongs **after** this stage in a bigger facade/chip collector, not by allowing the 10 pF regional bank to accumulate hundreds of packets.

Therefore the hierarchy is:

`tiny local expired states -> 10 pF-class regional buffer -> frequent safe-window drain -> much larger facade/chip collector -> infrequent efficient conversion`.

This resolves the apparent conflict between:
- v13J1: large batches improve converter efficiency;
- v13J3/v13J4: a small regional bank cannot hold a huge batch safely.

Batch **energy conversion** at the chip collector; do not batch **voltage accumulation** indefinitely in the local/regional bank.

## 7. Failure behavior
- stuck-open ARG is dangerous because it can load live/recent state -> branch isolation + `!WEAK_ANALOG_ACTIVE` gating required;
- stuck-closed ARG loses recovery efficiency but must not break correctness -> recovery is optional to correctness;
- overfull regional reservoir must trigger conservative drain/fallback, not modify inference thresholds;
- exact computation remains independent.

## 8. Next physical circuit
The next PDK target should combine existing real blocks rather than another abstract model:
1. one real Grammar/evidence node;
2. one local robust `VALID/CAPTURED` signal;
3. one 10 pF-class regional recovery node or scaled electrical equivalent;
4. one shielded service/recovery line with extracted coupling;
5. an ARG/recovery valve;
6. inject one/two recovery episodes while analog is active and verify valve remains closed;
7. repeat after capture and verify the recovery node drains without changing the already captured result;
8. TT/FF/SS + independent mismatch;
9. deliberately force facade switching during the weak window to measure the actual fallback boundary rather than rely only on the capacitance proxy.

Until that physical battery passes, v13J4 is an architecture/circuit-model KEEP, not physical closure.
