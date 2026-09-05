# Neural Glyph v15FG — Partial-Thought Luminous Screen + Same-Model Dialogue

**Status: PARTIAL PASS.** The corrected partial-result optical screen passes the present ngspice + Monte Carlo model. Same-model self-dialogue and direct affect are protocol/behavior models only; they are not claimed as measured LLM-quality results or conscious emotion.

## What happened
The earlier v15E screen was misunderstood. It treated light mainly as a destination address. v15FG replaces that with the user's actual idea: the screen is a short-lived optical working surface for the same AI. It carries only an intermediate fragment needed to continue the same question.

Example used for closure:
- Math computes `5 × 2 = 10`.
- The partial result `+10` is represented by **two positive dots**, each driven from a **5-V branch** for at least **1 us**.
- Another active specialist region of the same AI sees the two dots, reconstructs `+10`, and continues the existing question.
- The shared supply powers the next specialist at its normal core voltage. `10` is a representation/need magnitude, **not 10 V applied across the chip core**.

Negative values use a negative-dot bank. This preserves the accepted positive/negative-charge direction.

## Why there is still capacitance
v15D/v15FG does **not add a separate learning capacitor**. The existing HZO/dendrite electrode has unavoidable capacitance. Signed charge can only exist on an electrical node because that node has capacitance. The architecture uses that intrinsic capacitance as the fast residue store and HZO polarization as the slow consolidated memory.

A photodetector also has unavoidable input/junction capacitance; using it to integrate light is not a new semantic memory device.

## v15F screen Monte Carlo
500,000 trials varied 5-V dot branch current, 1.0–1.6 us visible duration, optical efficiency/coupling, detector efficiency, dark counts and crosstalk.

Selected signed-unary rule: one lit dot = 5 units. `+10` = two positive dots.

Results:
- exact partial-value read pass: **99.9998%**;
- misread rate: **0.0002%**;
- false-dot event rate: **0 observed** in the present 500k run;
- missed-lit-dot event rate: **0.0002%**;
- lit-dot photoelectrons, median: **~655**;
- `+10` exact read pass: **100% observed** in its trial subset;
- `+10` median screen electrical energy proxy: **~3.03 pJ**.

This is a model target, not a fabricated microLED/display measurement.

## Actual ngspice screen test
A two-dot `+10` screen was run in ngspice. At ~1 us:
- detector 1: **17.964 mV**;
- detector 2: **17.964 mV**;
- dark/crosstalk detector: **7.19 uV**;
- combined partial-result/need node: **35.928 mV**;
- selected specialist's normal 0.8-V load: **0.7996 V**;
- load peak: **0.8003 V**.

This verifies the circuit interpretation: two 5-V-controlled optical dots can be seen for >=1 us and can enable a shared normal-voltage specialist supply. It does not mean a 10-V core rail.

## Screen energy boundary
For the deliberately long >=1-us hold, the selected `+10` two-dot proxy is ~3 pJ. A simple five-transition 0.8-V electrical-link capacitance proxy gives ~0.64 pJ at 2 mm, 1.6 pJ at 5 mm, 3.2 pJ at 10 mm and 6.4 pJ at 20 mm.

Therefore the screen is **not** automatically better than short electrical wires. Keep it only where reduced cross-chip wiring, persistent visible working state, or parallel observation justifies it.

## v15G optional same-model self-dialogue
This is **software behavior for users who enable it**, not another chip device. Two instances use the same model weights and same user prompt, but independent inference state/sampling. They exchange compact candidate answers/critiques and continue only while disagreement or low confidence remains.

A critical boundary was found: if both contexts are fully deterministic/correlated, self-dialogue adds **zero** perspective.

300,000 synthetic protocol trials per correlation point gave modeled gains over one context of +3.76 pp at correlation 0.0, +3.35 pp at 0.3, +2.63 pp at 0.6, +1.58 pp at 0.85 and **0 pp** at 1.0.

This is not an LLM benchmark. It tests the protocol principle only.

## Direct affect / emotion input
v15FG does not claim subjective emotion or consciousness. It tests affect-like signals as **direct signed modulatory state** in the reasoning fabric: caution, urgency and curiosity/uncertainty. They change thresholds and search/replay depth; they do not contain a hard-coded action.

In 250,000 generic synthetic contexts, switching from neutral to high-caution affect changed the selected action in **~27.49%** of cases rather than forcing one fixed response.

For the user's vehicle-style ambiguity, the model selected immediate allow ~0.004%, verify/challenge ~90.23%, and immediate block ~9.77%. The car scenario is only a test example.

## Hardware revision requests
Retain the corrected v15D meaning:
- unknown knowledge -> remain unknown / reason / ask another specialist;
- persistent physical chip fault -> accumulate hardware doubt and report a maker-facing revision request.

## Problem remaining
1. A real 5-V-branch micro-emitter screen must verify the 1-us read margin, optical crosstalk, and ~pJ-per-small-fragment energy.
2. Unary 5-unit dots are efficient only for small partial values.
3. Same-model self-dialogue must be tested on a real model runtime.
4. Direct affect must be calibrated so it modulates reasoning without overriding evidence.

## What is next
**v15FG1 — 8-dot signed partial-thought screen + real same-model dialogue A/B protocol.**
