# v14M Experiment Report — One Device Type, Two Regimes

## Question
Can a population built from one simple two-terminal diffusive junction type collectively beat a transistor-based control/memory fabric even if an individual junction is not always cheaper or faster than one MOS transistor?

## Device candidate
The selected model candidate is the **Bimodal Diffusive Junction (BDJ)**: an Ag/Ag-alloy + HfO2-class two-terminal filamentary device.

Low-current operation is volatile and self-relaxing, so the same device can act as a leaky integrate/fire element. Stronger programming creates nonvolatile conductance states so other instances of the same device type act as learned links.

This is grounded by separate published demonstrations of volatile/nonvolatile coexistence in HfO2 memristors, low-voltage Ag/HfO2 threshold switching, and single-device neuron/synapse reconfiguration. It is not yet one fabricated v14M stack with all selected speed/energy targets.

## Failure first
The first cascade used a threshold too close to full nominal incoming charge. Small early misses accumulated and the eight-layer network died. The architecture was not accepted.

A topology sweep showed that population margin is cheaper than demanding an unrealistically perfect threshold device. The smallest retained robust point was 3 STRONG + 2 WEAK useful incoming links per cell with a 0.50 nominal threshold factor.

## Reliability result
1000 trials, 8 layers, 64 cells/layer, 1% link failure, 1% firing failure:

- sigma=0.10 conductance variation: mean final active 0.9878; p05 0.9531.
- sigma=0.20: mean 0.9857; p05 0.9531.
- sigma=0.30: mean 0.9800; p05 0.9375.
- sigma=0.40: mean 0.9541; p05 0.8906.

A one-million-sample background-only screen at sigma=0.30 produced zero modeled false fires.

## Energy-delay screen
Model target values: Vth=0.25 V, Icomp=100 nA, 0.20 V / 20 ns link reads, 1.5 fJ fixed line/bias overhead.

At 30 ns target firing delay:
- fire proxy: 0.75 fJ;
- link-read proxy: ~0.065 fJ/fire;
- total: ~2.315 fJ/fire.

Conservative CMOS references count only C*VDD^2 at 1.8 V and 6 ns; they deliberately omit SRAM/decode/interconnect energy.

At 30 ns v14M still beats the EDP of 5 fF / 10 fF / 20 fF controls in this proxy. EDP break-even BDJ delays are ~38.5 / 62.3 / 97.3 ns respectively.

Published Ag/HfO2-family devices span a wide time range. Older/common volatile devices can be microseconds and would fail this target. Recent optimized filament devices are reported below 100 ns, and separate nonvolatile HfO2/MoS2 work reports ~55 ns SET. Therefore the physical target is difficult but not disconnected from current device research.

## Learning cost warning
Nonvolatile programming is the largest unresolved energy problem. The model does not assume a cheap write. If a write costs 10 pJ, the 30 ns candidate must amortize roughly 665 inferences per write for write cost to remain below half of saved inference energy versus the 10 fF CMOS reference. A 100 pJ write needs roughly 6,650 inferences/write.

So v14M only makes sense if learning is local and relatively sparse, or if future programming energy is greatly lower.

## Structural count
For a 64-cell region:
- v14M selected group: 384 two-terminal devices.
- conservative reference: 384 MOS for six-device threshold cells + 320 ideal one-element links = 704 counted elements.

This 45.5% count reduction is not a layout/process-cost result.

## Decision
**KEEP v14M at model level.**

The one-device-type idea is materially simpler than v14L and retains v14K learning semantics. But physical promotion is blocked on one exact question: can a single manufacturable diffusive junction stack simultaneously deliver a fast-enough low-current volatile regime and a useful reversible nonvolatile regime without expensive compliance/select peripherals?
