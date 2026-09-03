# Neural Glyph v14S — Self-Protected Polarity-Guided Choice Cell

**Status: MODEL/ARCHITECTURE PASS; PHYSICAL COMPOUND-DEVICE PARTIAL.**

## What happened

v14S closes the biggest chip-level conflict left by v14R: the HZO route memory wants a much larger programming voltage than the guided-gap firing path. Driving the same two terminals at the learning voltage would force the volatile diffusive gap far above its ~0.25-V inference regime and could destroy the transistor-replacement advantage.

v14S therefore separates the two electrical jobs while keeping them co-located in one branch footprint:

- **signal terminals:** low-voltage v14O guided-gap firing plus intrinsic passive ballast;
- **program terminals:** HZO polarity collar driven by a separate local BEOL row/column plane;
- **nonlinear inhibit:** a passive two-terminal nonlinear layer in series with the HZO collar so half-selected collars receive little internal FE voltage;
- **polarization aperture shield:** grounded metal around the collar with only a small aperture facing the guided gap, concentrating the useful fringe field and suppressing field leakage to neighboring branches;
- **eligibility:** the volatile guided-gap residue itself marks recent use, so v14Q does not require another physical memory element.

The ordinary semantic cell has **zero MOS transistors**. MOS is allowed only in a shared local programming porch until a cheaper passive regional driver is demonstrated.

## New selected cell

**SP-PGCC — Self-Protected Polarity-Guided Choice Cell:** one tiny choice node feeding six passive compound branches. Four branches are ordinary learned relations and two are uncommitted repair spares.

**Compound Polar Branch:** one low-voltage guided-gap signal path physically beside, but electrically separate from, one HZO polarity collar and its passive nonlinear inhibit/program stack.

The extra two branch mouths are cheaper than duplicating every learned relation and let training route around defective devices.

## Physical evidence inherited from v14R

The copied Magic/SKY130 extraction gives:

- CHOICE self capacitance: 112.362 aF;
- five explicit branch couplings: 7.95455 aF each;
- represented five-way CHOICE load: 152.13475 aF = 0.152135 fF.

v14S adds six 10×10 nm, 5-nm-thick, k≈25 HZO capacitance proxies. The combined choice + six-collar load is ~0.1787 fF. With the inherited 2.3-MΩ winner-path model, a 20% choice-node collapse takes ~0.0917 ns. Node charging energy at 0.25 V is only ~0.00558 fJ.

These CHOICE parasitics are extracted. The HZO collar capacitance is a geometry estimate.

## Aperture-field screen

A finite dipole-patch electrostatic envelope was combined with a 2-D Poisson shield/aperture screen. The selected target is:

- 10-nm polarization patch;
- 16-nm shield aperture;
- 20-nm neighbor observation/pitch screen;
- nominal polarization `P = 0.16 C/m²`.

The model retains ~92.8% of the target field while reducing the neighboring observed field to ~0.45% of target. The resulting target fringe envelope is ~0.441 V before a calibrated 3-D metal/material solution. Four independent external neighboring collar states were then injected into every branch race as crosstalk stress.

## Six-way branch race

300,000 deterministic Monte Carlo trials, including inherited gap/focus variation and the added four-neighbor aperture crosstalk:

- correct winner: **99.9937%**;
- correct winner with enough first/second margin to quench the shared node: **99.9937%**;
- mean winning delay: **~7.96 ns**;
- p95 winning delay: **~9.92 ns**.

This is a model result, not a fabricated switching measurement.

The polarization floor screen is important. At the selected geometry:

- P=0.12 C/m² -> ~99.922% correct+quenched;
- P=0.14 C/m² -> ~99.981%;
- P=0.16 C/m² -> ~99.993%;
- P=0.18 C/m² -> ~99.998%.

Therefore v14S now has a material acceptance target: **effective retained polarization should stay at or above roughly 0.14 C/m² if we want >99.98% single-cell modeled route selection without adding active correction.**

## Learning-program protection

The selected array scheme is V/3-like:

- chosen collar terminal differential target: 1.2 V;
- half-selected terminal differential: 0.4 V;
- 100-ns screening pulse.

With a 4.43-aF HZO proxy and an example passive nonlinear element (`Ron=100 MΩ`, `Roff=100 GΩ`), the RC envelope gives:

- selected HZO: ~1.2 V;
- half-selected HZO: ~0.081 V.

More importantly, the device target derived from the equations is mild compared with ideal selector marketing numbers:

- Roff >= ~48.1 GΩ to keep a half-selected HZO proxy <=0.15 V in 100 ns;
- Ron <= ~12.6 GΩ to bring selected HZO >=1.0 V;
- required resistance-window ratio in this simple RC envelope: only ~3.81×.

This is not a calibrated selector model. Cumulative disturb, threshold dynamics, leakage, temperature, and HZO domain switching still need physical/compact-model testing.

## Repair-spare result

The selected cell uses **4 logical relations + 2 spare physical branches**.

If each branch has 98% independent usable-device probability:

- five physical branches with four required -> cell yield ~99.616%, but a 64-cell region would be only ~78.2%;
- six physical branches with four required -> cell yield ~99.985%, and a 64-cell region ~99.03%.

At 99% branch probability, six branches give ~99.875% 64-cell-region probability under this independent-fault proxy.

This is why v14S keeps six mouths despite the small extra capacitance. The extra passive branch is economically better than per-relation duplication or repair MOS.

## Shared programming porch

One **Program Porch** serves eight cells.

**Program Porch:** a slow, shared edge circuit that supplies the four V/3 programming levels to the HZO row/column rails; it is not in the inference signal path.

Current conservative structural count proxy:

- 16 program lines per eight-cell bank;
- 32 line-selection MOS proxy;
- 8 additional shared-level/isolation MOS proxy;
- total ~40 shared MOS per bank = **5 MOS-equivalents per semantic cell**;
- ordinary cell itself = **0 MOS**.

For a 64-cell region this proxy is 320 shared programming MOS, but they are slow, reused, and outside the reasoning path.

Program-line energy is dominated by metal, not the 4-aF HZO. For an 8-cell bank, modeled ideal V/3 line-transition energy ranges from ~0.64 fJ for a 5-µm/0.2-fF-per-µm case to ~64 fJ for a deliberately long 100-µm/1-fF-per-µm case. A pessimistic all-16-lines-to-1.2-V upper bracket spans ~11.5 fJ to ~1.15 pJ over the same range. Physical program-grid PEX is required before claiming a write-energy advantage.

## Comparison against transistor cells

### v14E physically closed MOS reference

v14E's real CFN used 15 MOS + 2 MIM. Its two MIM plate geometries alone total ~11.924 µm² before counting its MOS or routing. v14S therefore has an area acceptance ceiling: with six branches, **each complete branch could consume ~1.99 µm² before merely equaling v14E's MIM plate area alone**. This is a break-even ceiling, not a v14S area claim.

The current v14S programming-periphery proxy is 5 shared MOS-equivalents/cell, versus 15 MOS physically inside the v14E CFN. The functions are different, so this is a structural complexity comparison, not a direct benchmark score.

### v12S transistor-heavy route reference

The supplied v12S archive hashes to `0ab940fa...63878`. It contains 70 MOS + 14 MIM in the full tile. Re-parsing the section from `two repeated motif queries` through the `exact kernel` boundary gives 50 MOS + 12 MIM in the two-candidate route/competition/capture region. v14S does not claim equivalent functionality to that entire section; it uses it as evidence of how quickly robust CMOS route selection accumulates devices.

### Inference energy-delay model

v14S reuses the inherited v14O event-energy proxy and adds the now tiny choice-node energy:

- v14S model event: **~1.906 fJ**;
- mean selected-branch delay: **~7.96 ns**.

Against deliberately favorable simple CMOS switching controls at 1.8 V / 6 ns:

- 5 fF: 16.2 fJ -> v14S ~8.5× lower energy and ~6.4× lower EDP;
- 10 fF: 32.4 fJ -> ~17× lower energy;
- 20 fF: 64.8 fJ -> ~34× lower energy.

Those CMOS controls are analytical break-even references, not extracted old-cell energy measurements. The physical v14S compound branch still has to close before this advantage can be claimed in silicon.

## What was rejected

- programming the HZO through the same two terminals as the 0.25-V guided gap;
- a MOS selector at every branch;
- a separate v14Q eligibility capacitor/device;
- duplicating every relation for yield;
- a 64×64 dense learning crossbar;
- pretending nanometer HZO material area equals final routed-cell area;
- claiming the passive nonlinear layer is already a selected fabricated device.

## Current problem

Only one core problem remains, but it is a real one: **the complete compound branch has not been physically demonstrated or calibrated.** We need to know whether HZO polarization can shift the actual guided-gap switching statistics strongly enough after real electrode screening while the nonlinear inhibit protects half-selected collars over repeated writes.

The two most dangerous failure modes are:

1. HZO/program-stack fields disturb or electrochemically bias the Ag guided gap even though the terminals are separated;
2. the nonlinear inhibit/HZO stack does not preserve the required >=0.14 C/m² effective polarization under temperature, cycling, and half-select history.

## What is next

v14S1 must stop adding architecture and physically close one compound branch plus one eight-cell program-bank proxy:

1. calibrated HZO hysteresis/pulse model at 0.4/1.2-V terminal conditions;
2. calibrated nonlinear-inhibit dynamic model rather than static Ron/Roff;
3. 3-D electrostatic field extraction with real metal electrodes/shield/aperture;
4. coupled guided-gap threshold/delay shift versus both HZO polarities;
5. repeated inference read-disturb and half-select stress;
6. polarity reversal and endurance;
7. two adjacent branch stacks for crosstalk;
8. 8-cell program-grid physical layout/RC extraction and write-energy accounting;
9. compare final compound branch + shared porch against the v14E/v12S transistor references without hiding periphery.

If physical closure requires a MOS beside each branch, **v14S fails**. The next move would be a different passive nonvolatile field source, not adding CMOS back into the semantic cell.
