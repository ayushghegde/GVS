# v14J Report — Reversible Electrical Connection Plasticity

## Problem
v14H showed that broad synthetic reasoning does not require persistent semantic voltage at every node. Knowledge can live in sparse connections, but fixed capacitors cannot update when a learned relation changes.

## Hypothesis
A two-terminal memcapacitive connection can use its own electrical history as the nonvolatile weight state. Low read excitation does not rewrite it. A local learning echo changes capacitance: one polarity strengthens a useful relation and the opposite polarity weakens a contradicted relation.

## Main result
Reversible plasticity is required. In the continual-learning model, strengthen-only learning accumulates obsolete paths and falls to roughly 60-69% final accuracy. Reversible strengthen/weaken learning stays near 99.5-100% under clean feedback and remains ~98% with two/three copies under a harsh combination of 10% false feedback and 5% program-event failures.

The key architectural result is therefore not merely 'capacitors can be weights'. It is:

**the connection must be electrically erasable/reversible as knowledge changes.**

## Automatic local update interpretation
Inference does not call a digital weight-update routine in the hardware hypothesis. Pre/post electrical activity establishes an eligibility path. If a compatible Goal/Population-Confidence echo returns, the differential voltage across that active two-terminal link has the potentiating polarity. If contradiction evidence returns, polarity reverses and the same physical connection depresses.

A learning signal remains necessary. Repeated activity by itself cannot prove truth.

## Physical floor
Two fixed SKY130 MIM connections were generated and extracted:

- weak 1x1 um: 0 DRC;
- strong 2x2 um: 0 DRC;
- both extract as real `sky130_fd_pr__cap_mim_m3_1` devices;
- effective nominal+direct-parasitic coupling proxy is ~2.737 fF versus ~9.345 fF, ratio ~3.415x.

This validates the cheap charge-transfer inference principle. It does not implement learning because ordinary MIM geometry is immutable.

## External process screen
Current ferroelectric memcapacitor literature makes the plastic-link hypothesis plausible but not closed. HZO devices have demonstrated reversible high/low capacitance states, non-destructive sub-coercive read, multilevel capacitance, long retention, and high endurance. Published programming voltages are still often around 2-4 V, so programming infrastructure may dominate cost. v14J therefore keeps ferroelectric/memcapacitive links as a future-process candidate only.

## Limitations
- The SPCL state equation is an abstract device model.
- The experiment is not a fabricated measurement or a foundation-model benchmark.
- No current SKY130 device provides the required nonvolatile reversible capacitance.
- Learning polarity currently assumes a local correctness/contradiction echo from existing GVS confidence mechanisms.
- Program-driver area, write energy, half-select disturbance, sneak paths, endurance under actual learning frequency, and fabrication yield remain open.
