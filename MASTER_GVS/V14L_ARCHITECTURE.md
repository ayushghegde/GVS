# Neural Glyph v14L — Quantal Charge-Vesicle Tissue

**Status:** model-level architecture and Monte Carlo charge-sharing experiment built on v14K. The v14J fixed SKY130 MIM extraction is reused as the capacitance floor. The new volatile release element is a physical target, not yet a fabricated GVS device.

## Central idea

v14L turns the user's “leaky capacitor that gathers charge and sends energy” idea into a physically conservative primitive.

A capacitor does not literally clump electrons into a little ball. Excess charge accumulates collectively on its electrodes. A plain capacitor can store and leak charge, but it cannot provide unlimited fan-out or regenerate a long signal chain. v14L therefore separates **information accumulation** from **energy regeneration** while keeping the cell capacitor-centered.

## New primitive — QVC

**Quantal Vesicle Capacitor (QVC):** a leaky, pre-biased membrane capacitor that accumulates small incoming capacitive charge packets, forgets old excess charge by leaking back toward its bias, and triggers a regenerative release event when its voltage crosses threshold.

Target electrical form:

`local bias/replenishment -> high-impedance path -> Cmem || controlled leak || volatile release element`

The volatile release element should ideally share electrodes with the capacitive structure or sit directly beside it in BEOL so the cell does not become a transistor-sized control circuit.

## New primitive — VRS

**Volatile Release Switch (VRS):** a two-terminal nonlinear element that is high resistance during integration, snaps conductive above a threshold, and returns high resistance below a holding condition.

Candidate device classes include OTS, NbOx/VOx-type threshold devices, and other solid-state volatile memristive selectors. No material is selected yet.

## Why the cell is pre-biased

The first passive experiment was rejected. If a charged capacitor at voltage V simply shares charge with k equal empty capacitors, the common voltage is approximately V/(k+1). Even fan-out 1 halves the voltage. A passive one-reservoir chain therefore loses amplitude and cannot behave like a regenerative neural tissue.

v14L instead keeps each receiving cell locally biased below threshold. Incoming links carry only the **incremental evidence charge** needed to cross threshold. Most firing energy is already stored locally and is replenished slowly afterward. This is analogous to the useful energy-regeneration principle of neurons without reproducing neurotransmitter chemistry.

## Reuse of v14K connection memory

v14L does not add a second synapse fabric.

The same sparse OFF/WEAK/STRONG connection elements from v14K become the packet couplers:

- OFF: essentially no packet transfer;
- WEAK: small capacitive displacement packet;
- STRONG: larger packet;
- learned structural revision changes both understanding and future packet flow.

This is important because otherwise a separate communication synapse would erase the hardware savings.

## Current capacitance basis

The model uses the physically extracted v14J fixed-MIM proxy as a floor:

- WEAK effective coupling proxy: 2.73685 fF;
- STRONG effective coupling proxy: 9.34526 fF;
- membrane proxy: two STRONG-size MIMs = 18.69052 fF.

These values come from Magic/SKY130 extraction plus the current PDK MIM area model. They are not fabricated measurements and ordinary SKY130 MIM remains fixed, not plastic.

## Selected operating point

The current model uses:

- local resting bias: 0.60 V;
- firing threshold: 0.80 V;
- post-fire reset target: 0.15 V;
- source firing edge magnitude: 0.65 V;
- leak time constant: 100 ns;
- packet spacing: 5 ns;
- 1% release-miss stress;
- 5% capacitor variation, 2.5% threshold variation, 20% leak-time variation, and small bias/source-edge variation.

The resting bias is intentionally below threshold. Old evidence decays toward the bias; after firing, the same low-bandwidth replenishment path restores local energy.

## v14L experiments

### v14L0 — Passive fan-out conservation

Rejected the one-capacitor-only concept for general propagation. Passive charge sharing cannot provide gain. Regeneration must occur locally.

### v14L1 — Quantal packet accumulation

A voltage edge on a source is coupled through the persistent relation capacitor into a receiving QVC. Packet amplitude is approximately proportional to `Clink / Ctotal`, so a STRONG learned connection naturally transfers more evidence than a WEAK one.

### v14L2 — Cascaded tissue Monte Carlo

Eight layers of 64 cells were stressed for 500 deterministic Monte Carlo trials.

Selected 6-WEAK + 1-STRONG input structure:

- mean final active fraction: 0.994125;
- 5th-percentile final active fraction: 0.96875;
- minimum observed final active fraction: 0.921875;
- modeled shared coupling + replenishment energy: about 9.1334 fJ per firing before VRS firing energy.

Alternative 4-WEAK + 2-STRONG structure:

- mean final active fraction: 0.99884375;
- 5th-percentile final active fraction: 0.984375;
- modeled shared coupling + replenishment energy: about 9.8476 fJ per firing before VRS firing energy.

The stronger-link option is more robust but spends more coupling energy. This is a useful system-level tradeoff rather than a reason to maximize every weight.

### v14L3 — Idle false-fire screen

One million synthetic idle samples with the selected 0.60 V bias / 0.80 V threshold variation model produced zero false threshold crossings. This is only a statistical model screen, not transistor/device signoff.

### v14L4 — Transistor break-even target

The capacitive/replenishment part is not the unknown anymore; the VRS is.

For the selected 6W+1S model, common packet/replenishment cost is about 9.13 fJ/fire. Against a transistor control reference with effective switched capacitance `Clogic` at 1.8 V, v14L wins energy when:

`E_VRS < Clogic * 1.8^2`.

Examples:

- if transistor control switches 5 fF effectively, VRS must be <16.2 fJ/fire for energy advantage;
- 10 fF -> <32.4 fJ/fire;
- 20 fF -> <64.8 fJ/fire.

Delay matters too. Against a 10 fF control reference at 6 ns, if VRS firing energy is 5 fJ, the VRS should switch in roughly <=17.6 ns to beat energy-delay product. A ~10 ns VRS would pass this model target; a ~20 ns VRS would still save energy but would lose EDP against that lean reference.

These are **requirements for the device**, not measurements of an existing GVS switch.

## Chemistry decision

Do not reproduce literal neurotransmitter chemistry in v14L. Biological chemical synapses require chemical packaging/release/receptors and energy-consuming restoration. That complexity has no demonstrated cost advantage for this chip.

KEEP as research candidates:

- solid-state ionic threshold devices;
- OTS/chalcogenide selectors;
- oxide threshold switches;
- other BEOL two-terminal volatile switches.

They may involve ion or defect motion internally, but they do not require fluid neurotransmitter reservoirs or biological molecular machinery.

## Relationship to existing GVS recovery

The firing path and spent-charge recovery remain subordinate to correctness.

v14L should ultimately connect its post-fire spent charge to the existing hierarchy:

`cell -> Local Venule -> Charge Artery -> regional reservoir -> battery/collector`.

The low-bandwidth replenishment path is separate from the reasoning signal path. It must not become a hidden scheduler.

## Keep / reject

KEEP:
- capacitor-centered local integration;
- controlled leak / forgetting;
- sub-threshold local bias so small packets can trigger a regenerative event;
- local energy regeneration instead of requiring one packet to power the whole chain;
- reuse of v14K plastic relation capacitors as communication links;
- WEAK/STRONG link strength as physical packet amplitude;
- sparse strong links for robustness rather than making all links strong;
- system-level energy + delay + area + reliability accounting.

REJECT:
- claiming electrons literally clump into a compact particle packet inside a capacitor;
- a passive one-capacitor fan-out chain;
- literal neurotransmitter chemistry as the baseline;
- adding a second full synapse matrix just for communication;
- calling OTS/ionic devices cheaper than transistors before firing energy, selectors, process integration, endurance, leakage, variation, and delay are measured;
- declaring v14L collectively better than transistor logic before the VRS physical budget closes.

## Acceptance for physical promotion

Promote the QVC/VRS primitive only if a real device or credible compact model demonstrates all of the following together:

1. threshold/hold behavior compatible with the selected bias window;
2. controlled sub-threshold leakage that gives a useful integration time without a per-cell transistor;
3. VRS firing energy inside the break-even budget;
4. switching delay inside the target EDP window;
5. enough drive for the sparse capacitive fan-out without excessive voltage collapse;
6. acceptable device-to-device and cycle-to-cycle variation;
7. BEOL/process cost that remains favorable when counted across the whole region;
8. compatibility with v14K OFF/WEAK/STRONG plastic links and the existing recovery hierarchy.
