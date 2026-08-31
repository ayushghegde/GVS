# v14L Experiment Report — Quantal Charge-Vesicle Tissue

## What was tested

The user proposed a capacitor that loses old energy, gathers charge, and then sends energy to other cells. The first interpretation—a single passive capacitor that accumulates and then shares its stored charge downstream—was tested and rejected by charge conservation: with equal capacitors, one receiver already halves the source voltage, and fan-out reduces it further.

The retained v14L architecture instead pre-biases every receiving cell below threshold. Incoming relation capacitors deliver only incremental evidence charge. A local volatile threshold event releases the cell's already stored energy; a slow replenishment path restores it after firing. This preserves local regeneration without copying biological chemistry.

## Physical basis reused from v14J

The model did not invent arbitrary link capacitances. It reused the v14J Magic/SKY130 fixed-MIM extraction proxies:

- WEAK = 2.73685 fF;
- STRONG = 9.34526 fF;
- QVC membrane = 18.69052 fF (two STRONG-size MIM proxies).

Ordinary SKY130 MIM is still fixed and cannot implement v14K plasticity. These values are only the current physical capacitance floor.

## Selected QVC operating point

- resting bias: 0.60 V;
- threshold: 0.80 V;
- reset: 0.15 V;
- source firing edge: 0.65 V;
- leak tau: 100 ns;
- packet spacing: 5 ns;
- release miss probability: 1%;
- capacitance sigma model: 5%;
- threshold sigma model: 2.5%;
- leak-time sigma model: 20%.

A source voltage edge couples into the receiver in proportion to `Clink / Ctotal`. Therefore the same v14K WEAK/STRONG connection state becomes packet strength.

## Main cascade result

Eight layers x 64 cells, 500 deterministic Monte Carlo trials:

### 6 WEAK + 1 STRONG inputs/cell
- mean final active fraction: 0.994125;
- p05 final active fraction: 0.96875;
- minimum final active fraction: 0.921875;
- coupling + replenishment energy: 9.1334 fJ/fire before VRS energy.

### 4 WEAK + 2 STRONG inputs/cell
- mean final active fraction: 0.99884375;
- p05 final active fraction: 0.984375;
- minimum final active fraction: 0.984375;
- coupling + replenishment energy: 9.8476 fJ/fire before VRS energy.

The 4W+2S form is more robust but spends more energy. The 6W+1S form is the current efficiency candidate.

## Idle screen

1,000,000 synthetic idle samples with the selected bias/threshold variation produced zero threshold crossings. This only verifies model margin; it is not device/PVT signoff.

## Collective transistor comparison

The user requested that the system be better collectively even if one element is individually expensive. v14L therefore compares complete per-fire cost rather than device count.

For the 6W+1S candidate, the part shared by the capacitive network is ~9.13 fJ/fire. If a transistor control implementation has effective switched capacitance `C_logic` at 1.8 V, its added dynamic energy is approximately `C_logic * VDD^2`.

This gives a direct VRS firing-energy budget:

- 5 fF transistor control -> VRS must be <16.2 fJ/fire;
- 10 fF -> <32.4 fJ/fire;
- 20 fF -> <64.8 fJ/fire.

Energy alone is insufficient. With a 10 fF, 6 ns transistor reference and a 5 fJ VRS event, the VRS must switch in <=17.63 ns to match energy-delay product. A ~10 ns-class switch is therefore interesting; a ~20 ns switch could still save energy but would lose EDP against that lean reference.

## Decision

KEEP:
- pre-biased leaky membrane capacitor;
- local regeneration;
- existing v14K relation capacitance as packet coupling;
- sparse STRONG links for robustness;
- system-level energy and EDP acceptance.

REJECT:
- passive one-capacitor propagation;
- literal neurotransmitter chemistry as the baseline;
- extra synapse hardware that duplicates v14K;
- claiming transistor superiority or v14L superiority before the VRS physical numbers close.

## Current blocker

The volatile release device is now the dominant unknown. The next experiment must obtain or construct a credible compact model and test threshold, hold voltage, off leakage, firing energy, switching time, drive current, variation, endurance, and BEOL/process burden together with the real QVC capacitance and fan-out load.
