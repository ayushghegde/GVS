# Neural Glyph v13A7 — 3D Vertical Architecture Screen

**Verdict: PARTIAL PASS — same-die vertical MIM-over-transistor placement is physically demonstrated in SKY130; true die-stacked 3D remains a modeled architecture candidate, not a measured GVS result.**

## Why this experiment exists

The current GVS direction is increasingly limited by interconnect and physical placement rather than the local capacitive/event computation itself. The question tested here is whether GVS should deliberately use the third dimension instead of treating the chip as a flat plane.

This experiment does **not** change any completed v11/v12/v13 mechanism. It asks how to physically place those mechanisms more efficiently.

## Three meanings of 3D

### A. Same-die vertical BEOL stacking — selected now

Use the ordinary CMOS vertical structure more deliberately:

- transistors remain in the active device layer;
- MIM evidence/storage capacitors occupy upper metal layers directly above transistor logic when DRC/PEX allows it;
- short local sample/readout wiring stays in lower metals;
- robust/global event wiring uses the highest convenient metal.

This adds no die-to-die bonding step and is compatible with the current SKY130 physical flow.

### B. Hybrid-bonded die stack — promising future mode

Partition functions between directly bonded dies/tiers:

- local Glyph/event compute on one die;
- static template/configuration memory or event-distribution tier on another;
- robust full-swing events and slow/static configuration cross the vertical interface;
- weak candidate/reference/dendrite analog nodes stay inside one tier.

Modern 3D platforms such as TSMC SoIC and Intel Foveros Direct use fine-pitch direct/hybrid bonding. This is real manufacturing technology, but adds bonding, yield, thermal, power-delivery and cost concerns.

### C. Monolithic/CFET stacked device layers — research/future only

True vertically stacked active devices are increasingly demonstrated in research, but are not available in the current SKY130 PDK and should not be required for the first GVS hardware.

## Physical SKY130 experiment: MIM directly above NFET

A real W=0.42 um / L=0.15 um SKY130 NFET was drawn with a legal 2x2 um `sky130_fd_pr__cap_mim_m3_1` placed directly above it in XY.

Result:

- Magic/SKY130A DRC errors: **0**
- extraction sees exactly **1 NFET + 1 MIM**
- no accidental electrical short between the capacitor and the transistor
- correct NFET dimensions extracted
- correct 2x2 um MIM extracted

Extracted unwanted vertical coupling in this test is very small. Largest plate-to-transistor term:

- CAPBOT -> DRAIN: **59.0883 aF = 0.0591 fF**

Other examples:

- CAPBOT -> GATE: ~0.0149 fF
- CAPTOP -> DRAIN: ~0.00225 fF
- CAPTOP -> GATE: ~0.00191 fF

This proves that at least for this physical test, upper-metal capacitive state can occupy the same XY footprint as lower transistor logic without large unwanted coupling.

## Immediate GVS consequence

The next Grammar/readout layout should be **verticalized**, not simply placed side by side.

Preferred structure:

```text
M5        robust/global event routing
-------------------------------------
M4/M3     Grammar MIM candidate/reference
          short local evidence buses
-------------------------------------
M2/M1     reader / reset / lease local routing
-------------------------------------
FEOL      NFET/PFET reader + local event devices
```

The 10-MIM Grammar ratio array should be placed above as much of the direct reader/local logic as routing rules allow. This can reduce XY footprint and GC/GR wire length at the same time.

## True 3D die-stack energy screen

This part is **modeled**, not extracted GVS hardware.

GVS measured/model inputs:

- current long planar 16x16 coordinate selection: ~680 fJ
- selected 8-way Regional Lease write+refresh proxy: ~106.8 fJ for the tested burst
- measured minimum-width M4 capacitance: ~0.076106 fF/um
- VDD: 1.8 V

Literature screening inputs for hybrid-bond capacitance are used only to test architectural sensitivity, not as foundry guarantees:

- 10 um pitch: ~3 fF/interconnect
- 5 um pitch: ~0.1 fF/interconnect
- 1 um pitch: ~0.07 fF/interconnect

The model assumes two vertical coordinate/event links plus two local 50 um M4 landing wires.

### 10 um hybrid-bond screen

Ideal link-cap estimate:

- selection: ~44.1 fJ
- saving vs ~680 fJ planar selection: ~93.5%

With a 4x multiplier on the vertical-link energy to represent unmodeled driver/receiver/interface overhead:

- selection: ~102.4 fJ
- saving: ~84.9%

With 8x:

- ~180.2 fJ
- ~73.5% lower than the planar-selection proxy

### Deliberately conservative interface budget

Add 20 fF of extra interface capacitance to **each** of the two 10 um vertical links, far above the bare bond-capacitance input:

- modeled selection: ~173.7 fJ
- still ~74.5% below the 680 fJ planar-selection proxy

This does not prove a fabricated 3D GVS will achieve these values. It shows that the measured planar communication cost is large enough that true vertical integration has a substantial parasitic budget before losing its architectural advantage.

## What should cross a 3D die interface

### Allowed/preferred

- robust full-swing winner/event signals
- coordinate/region selection events
- slow static template/configuration bits
- exact-computer requests/results
- power/ground through an appropriate 3D PDN

### Keep inside one tier

- tiny dendrite/Grammar candidate voltages
- candidate/reference ratio nodes
- sensitive analog lease nodes if a local implementation exists
- regenerative-latch internal nodes

The rule is the same one already discovered in planar GVS: **weak analog information stays local; only robust meaning travels far.**

## Proposed 3D GVS partition

A useful future partition is:

### Local event/Glyph tier

- Regional Lease
- Grammar/template/Myelin local compute
- local MIM evidence/storage directly above its transistors
- local robust winner generation

### Memory/configuration tier

- static template assignment/configuration bits
- residual/exact metadata
- slow compiler state
- memory that benefits from dense vertical connection to local groups

### Exact-compute tier or neighboring chiplet

- ALU
- exact arithmetic/state
- fallback computer
- unusual/new/low-margin work

The hot exact-compute block should not automatically be sandwiched under temperature-sensitive analog logic; thermal placement must be co-designed.

## Power in 3D

Backside power delivery is attractive for a future advanced-node GVS because it separates power routing from signal routing and is particularly relevant to 3D systems. It is **not** available in the current SKY130 process and is therefore a future implementation option, not a baseline dependency.

## Cost/yield conclusion

3D is not automatically cheaper.

### Cheapest near-term path

1. keep the current mature/open process;
2. exploit same-die vertical BEOL overlap aggressively;
3. reduce long wires/local footprint first;
4. prototype GVS in 2D silicon with vertical metal/capacitor use.

### Use true hybrid-bond 3D when

- communication energy/area dominates enough to justify packaging cost;
- known-good-die partitioning improves yield or lets memory/logic use different cost-optimized nodes;
- thermal and power delivery are solved;
- vertical link density is actually used by the workload.

Do not use 3D merely because it is more advanced.

## Selected architecture decision

**KEEP 3D, but hierarchically:**

1. **NOW:** same-die vertical MIM-over-logic / metal-layer co-design;
2. **NEXT AFTER LOCAL SIGNOFF:** hybrid-bonded memory/event tier as a modeled/technology-target option;
3. **FUTURE ONLY:** monolithic/CFET stacked active device layers.

## Next experiment

Merge v13A6 and v13A7 instead of forking the architecture:

1. lay out the selected direct Grammar reader;
2. place the 10-MIM candidate/reference array directly **above** the reader where legal;
3. keep GC/GR vertical/local and symmetric;
4. keep O0/O1 routing short enough to satisfy the measured reader parasitic budget;
5. DRC + full extraction;
6. compare XY footprint against side-by-side placement;
7. compare GC/GR and O0/O1 parasitics;
8. rerun TT/FF/SS + mismatch;
9. only after this same-die vertical cell passes, model/place one vertical hybrid-bond event/config interface at the regional level.

## Provenance

### Measured/extracted GVS data

- SKY130 vertical MIM-over-NFET DRC/extraction in this experiment
- v13 physical M4 wire capacitance
- v13A Regional Lease/locality measurements
- v13A long-selection energy proxy

### External technology context / modeled inputs

- TSMC 3DFabric / SoIC public technology pages
- Intel Foveros Direct public technology material
- imec hybrid-bonding / backside-power / CFET research
- published architecture-level hybrid-bond capacitance values used only for sensitivity screening

No hybrid-bonded GVS silicon has been fabricated or extracted.