# v14S — Shared-Threshold Polarized-Link Cell

**Status: PARTIAL PASS (chip-level architecture/model screen; not fabricated device closure).**

## What happened
v14R still placed an active guided-gap firing junction on every candidate outgoing branch. v14S removes that replication. A cell fires once through one shared volatile threshold junction; sparse two-terminal polarized links carry persistent relation strength to receiving cells. Receiving cells perform the next competition by integrating convergent weighted evidence.

The common semantic cell becomes:
- 1 shared volatile two-terminal threshold junction per cell;
- about 5 two-terminal polarized relation links per cell;
- one ~0.20 fF receive node, using the v14R real ~0.152 fF SKY130/Magic node as the physical metal floor plus device allowance;
- no MOS transistor in the semantic cell.

## New primitive
**STPLC — Shared-Threshold Polarized-Link Cell:** persistent relation state is held in sparse two-terminal polarized links and all incoming evidence is integrated onto one tiny node that drives a single volatile threshold junction.

The important simplification is that outgoing branches do not each decide whether to fire. One cell event fans out through weighted links. The next cells decide from the combined incoming evidence.

## Selected model point
- inference pulse: 0.25 V, 20 ns
- node capacitance target: 0.20 fF
- STRONG link conductance target: 7 nS
- WEAK link conductance target: 0.5 nS
- STRONG/WEAK ratio: 14:1
- local leak: 2 nS
- shared threshold target: 0.16 V
- shared threshold event target: 100 nA, 12 ns
- 4 convergent active sources, 5 candidate receiving cells
- link variation: 30% CV
- independent link failure: 1%

200,000-trial result:
- correct receiver: 99.9595%
- any distractor firing: 0 in the selected run
- mean correct-node voltage: ~0.2198 V
- mean maximum distractor voltage: ~0.04685 V
- independent eight-stage route proxy: ~99.6765%

At 50% link variation + 5% failed links, the same topology remains ~98.6% single-stage correct in the reproducible sweep.

## Why the first attempt failed
The first v14S point used 5 nS STRONG links and a 0.18 V threshold. It reached only ~88.6% because the correct receiver was too near threshold. Distractors were not the problem. The fix was not more circuitry: STRONG was moved to 7 nS and the threshold to 0.16 V, widening the voltage margin.

## Energy target
Conservative full-pulse conductance accounting plus one shared 100 nA / 0.25 V / 12 ns threshold event gives:
- four-source link energy: ~0.045 fJ
- shared threshold event: ~0.300 fJ
- node charge: ~0.00625 fJ
- selected event total: ~0.35125 fJ

This is an engineering target, not measured combined hardware. Against the deliberately lean inherited CMOS switching proxy C*1.8^2, this is ~2.17% of a 5 fF event and ~1.08% of a 10 fF event before driver/interconnect/process overhead.

## Chip-level structural screen
For a 4096-cell degree-5 region:
- v14S: 4096 shared threshold junctions + 20,480 polarized links = 24,576 two-terminal devices;
- inherited lean reference: 24,576 MOS for six-MOS threshold/hysteresis blocks + 20,480 memory elements;
- counted-element reduction: ~45.45%;
- MOS removed before shared periphery: 20,480.

An illustrative 20-MOS programming/verification driver shared by 64 cells amortizes to 0.3125 MOS/cell, well below the five-MOS/cell structural margin. This is a budget example, not a selected circuit.

The physically closed v14E contradiction cell remains the proven transistor baseline at 15 MOS + 2 MIM, but it is a specialized contradiction/restart cell, not an apples-to-apples semantic cell.

## Learning simplification
v14Q's useful rule is retained without a separate per-link eligibility device.

**Pulse-overlap eligibility:** recently active source/target nodes retain a short electrical/ionic trace, so a later confirmation pulse overlaps more strongly on the relation that was actually used. Long-term state changes only with confirmation/contradiction. Traffic alone never becomes truth.

## Device direction
1. **Polarized link:** compact two-terminal HZO/FTJ-like relation element with reversible OFF/WEAK/STRONG conductance.
2. **Shared threshold junction:** one Ag/HfO2-class volatile diffusive switch at the receiving cell, preferably improved with the useful v14N/v14O seed/guided-gap/self-limiting ideas.

Literature supports these ingredients separately, but no cited device is treated as a fabricated v14S cell.

## Rejected
- active guided-gap firing junction on every ordinary outgoing branch;
- separate eligibility memory per link;
- one MOS selector per link;
- dense all-to-all relation matrices;
- forcing firing and long-term memory into the same filament just to claim one device type;
- accepting the first low-margin v14S operating point.

## Current problem
Architecture-level margin is now good enough. Device/process closure remains:
- physical polarized link must reach about the selected 7 nS / 0.5 nS read classes or an equivalent margin;
- 0.25 V inference must not disturb long-term state;
- selected programming must remain reliable after cumulative half-select exposure;
- the shared threshold junction needs low variation and high endurance;
- shared programming rails, masks, routing and yield must not erase the MOS savings.

## Decision
**KEEP v14S as the preferred transistor-replacement cell direction.** It is materially simpler than v14R because a degree-5 cell removes four of five active firing junctions. It is not yet a fabricated-device PASS.

## What is next
v14S1 physically/calibrationally closes one 64-cell tile: calibrated polarized-link model, calibrated volatile threshold model, extracted node/interconnect, transient cascades, read/half-select disturb, shared driver amortization, and a physically laid-out MOS reference implementing the same function.
