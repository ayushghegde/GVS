# Current Next Experiment — v14P1 Physical Electrostatic Trail Tip

## Goal
Determine whether a nanoscale trapped-charge/polarization pocket can reversibly shift the firing barrier of a v14O guided-gap branch enough for sparse path selection without adding a transistor or persistent node voltage.

## Preferred simple structure
Start with:
1. v14O inert field-focus spine and dynamic gap;
2. a small trap-rich dielectric pocket adjacent to the branch tip, outside the main current path;
3. the same two branch terminals for ordinary read and differential coincidence learning pulses;
4. v14O passive ballast for firing current.

Do not add a third gate terminal unless the two-terminal structure fails and the complete three-terminal system still beats the transistor reference.

## Physical tests
- electrostatic/barrier shift versus trapped charge/polarization;
- read-disturb under billions-equivalent ordinary pulses;
- positive and reverse programming;
- retention and spontaneous detrapping;
- neighboring-tip electrostatic crosstalk;
- temperature dependence;
- cycle endurance;
- programming energy;
- half-select disturbance under local coincidence learning;
- branch competition for 4-8 candidate routes;
- integration with v14O transient bridge and self-reset.

## Acceptance
- at least ~50-70 mV usable reversible branch-bias window with enough margin to separate favored from contradicted paths under realistic variation;
- ordinary reasoning pulses must not materially program the trail;
- reversible relearning after route changes;
- sparse five-ish branch competition should exceed 99% winner accuracy after physical calibration or show a population-confidence correction whose total cost still wins;
- no per-branch MOS selector/current limiter in the semantic core;
- complete group cost must beat the transistor reference, not merely the trap footprint.

## Failure rule
If trapped-charge retention, crosstalk, or programming energy is poor, do not force the electrostatic idea. Compare:
A. ferroelectric polarization tip;
B. ionic polarization tip;
C. v14O nonvolatile filament weight;
D. v14J memcapacitive link.
Keep the simplest whole-system winner.
