# GVS v15FG — Fragment Scratch Screen + Same-AI Dialogue

Status: **PARTIAL PASS**

## What happened
v15E misunderstood the optical idea as a destination-address plane. v15FG corrects it. The optical surface is a shared scratch screen that holds only an intermediate fragment/sub-question/result for at least 1 us. It is visible to the same AI fabric across chips. Power delivery to a specialist remains a separate common-supply action; content does not ride the power rail.

The earlier literal idea that the mathematical value should equal an electrical voltage was also tested and rejected. A number such as 10 must not require a 10 V logic state. Every light dot may use a fixed 5 V emitter domain while the value is encoded spatially (for example two 5-unit dots or a binary/Hamming pattern). This preserves the screen concept without making electrical stress scale with the number being represented.

## Problem 1 — Can the screen hold only the needed fragment reliably for >=1 us?
A 12-dot Hamming(12,8) screen was tested on 300,000 random 8-bit fragments with emitter/detector variation, Poisson photon noise, dark current, and adjacent optical crosstalk. The receiver samples only inside the guaranteed 1 us visible interval.

Result:
- decoded fragment success: 100% observed in 300,000 trials
- raw optical bit error rate: ~2.78e-7
- guaranteed-window observation success: 100%
- average active dots: ~5.995

This is a device/package model, not a fabricated microLED screen.

## Problem 2 — Does the optical screen automatically save energy?
No. At fixed 5 V drive, energy is strongly emitter-current dependent. Median 12-dot-fragment energy for the modeled 1 us hold:
- 0.05 uA/dot: ~1.5 pJ
- 0.10 uA/dot: ~3.0 pJ
- 0.20 uA/dot: ~6.0 pJ
- 0.50 uA/dot: ~15 pJ
- 1.00 uA/dot: ~30 pJ

The simple 12-bit electrical-bus proxy is ~0.768/1.92/3.84/7.68 pJ for 2/5/10/20 mm respectively. Therefore the scratch screen is not selected as a universal short-link replacement. Its value is a shared physical scratch surface that can reduce repeated point-to-point data wiring and can become competitive when the emitter is efficient and/or links are long or congested.

## Problem 3 — Should the same AI be allowed to talk to itself?
Yes as an **optional high-compute inference mode**, not as a default architecture claim. A 500,000-task correlated-error stress model was used because this runtime cannot launch multiple identical LLM instances.

- single-instance accuracy proxy: 90.7684%
- two copies with no discussion: 90.7864%
- one exchange + reconciliation: 95.4066%
- initial disagreement rate: 12.3086%
- fixed discussion compute proxy: 2.45x
- adaptive discussion (exchange only when the two copies disagree): ~2.055x

This does not prove an LLM benchmark result. External research on same-/multi-model debate is mixed; therefore v15G exposes the mode only when a user selects extra compute.

## Problem 4 — Are extra learning capacitors still needed after v15D positive/negative charge learning?
No additional learning capacitor is selected. Charge cannot exist at a voltage node without capacitance, but the capacitance is already intrinsic to the dendrite/HZO electrode and wiring. v15D uses that unavoidable capacitance as the fast charge store. The architecture should not add a separate capacitor merely to hold the positive/negative learning residue.

## Problem 5 — Can emotion-like state be applied directly?
A 250,000-task generic decision simulation tested three direct global modulatory biases: caution, urgency, and curiosity. They directly shifted the same competitive decision fabric rather than creating a separate emotion processor.

- static-threshold agreement with the generic optimum: 56.44%
- direct-modulation agreement: 61.94%

This is only a functional modulation result. It does **not** imply subjective emotion, consciousness, or human feeling. The modest gain is not strong enough to make this a required architectural block, but it supports keeping a very small number of global bias signals as an optional state-control mechanism.

## Problem 6 — What should trigger a request to the maker for a hardware revision?
Only persistent physical evidence: leakage, repeated timing loss, thermal excess, exhausted repair resources, or recurring electrical margin failure. Knowledge uncertainty does not request a new chip.

100,000-region persistence test:
- injected fault prevalence: ~5.53%
- fault detection: ~98.16%
- false revision request rate: ~1.06e-5

## Selected architecture
1. Inherit v15D charge-gradient dendrites, natural decay, HZO consolidation, guided-gap firing, repair branches, hollow shared infrastructure, and zero-MOS ordinary semantic cells.
2. Replace v15E destination-address optical routing with the **FSS — Fragment Scratch Screen**.
3. Use fixed-voltage optical dots; encode fragment values spatially/pulse-wise. Do not map mathematical magnitude to device voltage.
4. Keep self-dialogue as a user-selected high-compute software/inference mode. Same prompt, same model family, multiple instances, compact exchange, one final answer.
5. Keep emotion-like global modulation optional and functional only.
6. Keep hardware revision requests strictly diagnostic.

## Remaining problems
- Fabricated microLED/photodetector package test of 1 us hold, optical crosstalk, and energy at sub-uA dot current.
- Real same-model dialogue benchmark in the final model stack; the current result is only a correlated-error stress model.
- Real v15D dendrite charge-capture/HZO consolidation coupon remains necessary.

## Next
v15FG1 should build a 4x4 physical Fragment Scratch Screen coupon and benchmark same-model dialogue on real reasoning tasks. If the screen requires >~0.2 uA/dot for reliable 1 us observation at the intended package geometry, keep electrical interconnect for short links and use the screen only where wiring topology justifies it.
