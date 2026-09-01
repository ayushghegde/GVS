# Neural Glyph v14M — Bimodal Diffusive Junction Tissue

**Status:** model-level device-consolidation candidate. v14M does not claim a fabricated device meeting all selected targets simultaneously.

## Central goal
Use one simple two-terminal device type across the transistor-free semantic core so a population can collectively replace transistor thresholding, per-cell state machinery, and programmable connection memory.

## Primitive — Bimodal Diffusive Junction (BDJ)
A BDJ is a two-terminal metal/oxide/metal-like diffusive junction, targeted around Ag or Ag-alloy / ultrathin HfO2-class dielectric / Pt-class bottom electrode.

The same physical device type is used in two regimes:

1. **Volatile firing regime** — low compliance forms a weak temporary filament. Repeated incoming pulses increase the internal filament/ionic state; insufficient activity relaxes; sufficient activity crosses threshold and produces a current pulse; the filament then self-relaxes.
2. **Nonvolatile connection regime** — stronger, infrequent programming produces a stable filament state used as an OFF / WEAK / STRONG learned relation. Opposite programming can depress or reset the relation.

The two regimes need not occur simultaneously in one instance. A group is fabricated from one device type; some instances are local firing junctions and others are learned links.

## Why this is simpler than v14L
v14L required a membrane capacitor plus leak plus volatile release switch for the common firing cell. v14M asks whether the device's own ionic/filament state can perform integration/leak/fire, eliminating the ordinary membrane capacitor from the common semantic cell.

## Evidence basis
Published work separately demonstrates:
- Ag/HfO2/Pt diffusive memristors with abrupt volatile threshold switching around 0.2–0.3 V at 100 nA compliance;
- HfO2-family diffusive devices that change between volatile threshold and nonvolatile memory behavior when current/programming conditions change;
- a 2025 AgSn/SiO2/Pt alloyed memristor that experimentally performs integrate-and-fire in a volatile regime and synaptic-weight potentiation/depression in a nonvolatile regime using one device type;
- recent Ag/HfOx-family filament devices with sub-100-ns switching in optimized thin-electrode/heterointerface structures.

No cited device has yet demonstrated the complete selected v14M target simultaneously. The selected target is therefore an engineering envelope, not a fabricated measurement.

## Selected group topology
A 64-cell local region uses:
- one volatile BDJ per semantic cell;
- three STRONG + two WEAK learned BDJ inputs per receiving cell in the selected reliability screen;
- sparse links only; no dense all-to-all array;
- Population Confidence, Goal Echo, v14K teacher-free self-test, and provisional understanding remain architectural rules.

The semantic core contains zero MOS by requirement.

## Selected target envelope
Initial model target:
- reasoning/read pulse: 0.20 V, 20 ns;
- volatile threshold target: about 0.25 V;
- volatile current target: about 100 nA;
- logical connection conductance: OFF 0.25 nS, WEAK 2.5 nS, STRONG 25 nS;
- desired firing delay: <= 30 ns for the strongest energy-delay claim;
- two-terminal instances only in the common semantic fabric.

The 30 ns number is a target, not a measured property of a fabricated v14M device.

## Group result
In the selected eight-layer 64-cell synthetic cascade with 1% link failures and 1% firing failures:
- 20% link variation: mean final activity ~98.57%, p05 ~95.31%;
- 30% link variation: mean ~98.00%, p05 ~93.75%;
- 40% link variation: mean ~95.41%, p05 ~89.06%;
- one million background-only node decisions at 30% variation produced zero modeled false fires.

## Energy-delay result
Using a deliberately simple event-energy proxy, a 30 ns BDJ target consumes about 2.31 fJ/event including link read and 1.5 fJ line/bias overhead.

Against a deliberately lean CMOS-control reference of C*1.8^2 with 6 ns delay:
- 5 fF CMOS: v14M energy ratio ~0.143, EDP ratio ~0.714;
- 10 fF CMOS: energy ratio ~0.071, EDP ratio ~0.357;
- 20 fF CMOS: energy ratio ~0.036, EDP ratio ~0.179.

The corresponding BDJ delay limits for equal EDP are about 38.5 ns, 62.3 ns, and 97.3 ns respectively.

These are model break-even targets, not measured processor comparisons.

## Structural proxy
For 64 cells and five learned links/cell:
- v14M: 64 volatile junctions + 320 connection junctions = 384 two-terminal devices;
- conservative reference: six MOS per threshold/hysteresis cell + one unrealistically-cheap element per learned link = 704 elements.

This is about 45.5% fewer counted active/memory elements, but it is not an area result. Rails, compliance limiting, forming, selectors, routing, yield, and process steps remain to be counted.

## Learning compatibility
A separate relation-revision screen using the same OFF/WEAK/STRONG junction states showed that device redundancy helps failed writes but not semantically wrong teaching. With 20% read variation and 5% program failures, changed-relation correctness rose from ~93.1% with one copy to ~99.1% with two and ~99.8% with three. Common-mode bad feedback remained the dominant error, so v14K provisional understanding remains required.

## Keep / reject
KEEP:
- one two-terminal device type across neuron-like and connection-like roles;
- volatile internal-state integration instead of a permanent voltage memory in semantic cells;
- nonvolatile OFF/WEAK/STRONG connection state;
- sparse population redundancy;
- v14K self-revision and self-test;
- whole-group energy/device-count comparison rather than one-device marketing.

REJECT:
- claiming the existing slow AgSn demonstration is already fast enough;
- claiming separate literature numbers prove one fabricated stack meets v14M;
- dense crossbars by default;
- transistor fallback inside the semantic core;
- ignoring nonvolatile write energy or compliance/selection infrastructure.
