# Neural Glyph v14S — Shared-Threshold Polarized-Link Cell

**Status:** preferred transistor-replacement architecture at model/chip-structure level; physical combined-device closure remains.

## Core invention — STPLC
**Shared-Threshold Polarized-Link Cell (STPLC):** one tiny receive node and one volatile two-terminal threshold junction are shared by all sparse relations terminating at a semantic cell; persistent relation strength lives in two-terminal polarized links.

Topology:

`source firing -> sparse polarized links -> tiny receiving node -> one shared volatile threshold junction -> one new firing event`

The source does not need an active winner device on each outgoing branch. Its event can fan out over sparse weighted links. Receiving cells decide from convergent evidence.

## Common cell target
- 0 MOS inside semantic cell
- 1 shared volatile threshold junction
- ~5 two-terminal polarized links at degree 5
- ~0.20 fF receive node target
- 0.25 V inference pulse
- ~0.16 V receive threshold
- STRONG ~7 nS, WEAK ~0.5 nS initial target

## Physical device roles
**Polarized Link:** HZO/ferroelectric-tunnel-junction-like two-terminal element storing reversible relation strength as polarization-modulated conductance.

**Shared Threshold Junction:** Ag/HfO2-class volatile diffusive switch that performs local nonlinear firing once combined input evidence is high enough. v14N seed guidance, v14O guided gap and passive ion/current limiting remain candidate geometry improvements for this single shared switch.

## Learning
Use + confirmation overlap creates selected differential programming stress. Contradiction reverses it. Recent-use eligibility should be implemented by transient pulse/ionic overlap if physically possible, not a separate per-link memory device.

## Why this is better than v14R
v14R had one active guided-gap race device per candidate branch. v14S shares the nonlinear firing function once per receiving cell. For five relations this changes active firing count from roughly five to one while keeping persistent relation state in simple two-terminal links.

## Selected evidence
At 30% link variation and 1% independent link failures, a four-source/five-target model gives ~99.96% correct receiver selection and no modeled distractor fires in 200,000 trials. The first lower-margin point failed (~88.6%) and was rejected.

Modeled selected event energy is ~0.351 fJ, dominated by the shared volatile threshold event. This is a target envelope, not measured silicon.

## Keep
- one nonlinear firing element per semantic cell, not per branch;
- persistent memory in sparse two-terminal polarized links;
- low-voltage inference;
- local coincidence programming;
- confirmation/contradiction-gated long-term learning;
- v14R real tiny-node result;
- v14N/v14O guidance/self-limiting ideas applied only to the single shared threshold switch;
- v14K self-test/corroboration for uncertain teaching.

## Reject
- MOS inside the common semantic cell;
- branch-local active selector/firing devices by default;
- separate UET hardware per relation;
- a complex compound device solely to reduce nominal device-type count;
- claiming area advantage before physical BEOL footprint and shared periphery are counted.
