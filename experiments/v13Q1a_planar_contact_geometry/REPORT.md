# Neural Glyph v13Q1a — Planar Contact-Aperture Geometry Precheck

**Verdict: PHYSICAL GEOMETRY PASS / SWITCH-LEVEL CLOSURE OPEN.** A repeated-cell contact field can be placed near the selected Grammar weak-pair geometry with zero DRC and symmetric extracted coupling, but this experiment does not yet contain the MOS switch that makes an aperture electrically open/closed.

## New term
**Planar Contact-Aperture Proxy:** a SKY130 metal geometry representing the conductor/pad portion of a future selectable cell-to-cell Contact Aperture. It measures layout loading and asymmetry before adding the aperture transistor/state device.

## Tools
- Magic 8.3.681 built from the uploaded source archive;
- SKY130A `sky130A.tech` from the uploaded PDK files;
- real Magic DRC and parasitic extraction;
- capacitance values below are `.ext` coupling values converted from aF to fF.

## Weak-pair geometry
The precheck reuses the selected reader-terminal class:
- GC metal2 weak rail on the left;
- GR metal2 weak rail on the right;
- symmetric local CELL metal2 state plate between them.

The point is not to recreate the complete 10-MOS/10-MIM Grammar circuit in this subexperiment. It is to measure whether dormant neighbour-contact conductor geometry can exist around a weak local state without creating immediate differential asymmetry.

## Variant A — four independent face-like pads
Four metal3 pads overlap narrow strips of the CELL plate and remain mutually independent.

Result:
- DRC: **0**;
- total direct contact-pad -> CELL coupling: **0.431792 fF**;
- aggregate contact-pad -> GC: **0.01765768 fF**;
- aggregate contact-pad -> GR: **0.01765768 fF**;
- aggregate contact DSC: **0% at extraction precision**.

This establishes the ordinary face-contact geometry baseline.

## Variant B — four compact corner/diagonal pads
Four smaller metal3 pads occupy the four corners around the CELL plate.

Result:
- DRC: **0**;
- total direct corner-pad -> CELL coupling: **0.1792772 fF**;
- aggregate corner-pad -> GC: **0.012549754 fF**;
- aggregate corner-pad -> GR: **0.012549754 fF**;
- aggregate contact DSC: **0% at extraction precision**.

The smaller corner pads have lower geometric loading than the larger face pads in this particular planar proxy. That does **not** prove a real 3-D vertex contact is cheaper: the future switch, via/bond geometry and manufacturing tolerance are not present here.

## Variant C — eight contacts plus services
Four face-like + four corner-like contacts were placed around the same CELL plate. A metal4 low-swing Nerve and separate Charge Artery were added as nearby service lines.

Result:
- DRC: **0**;
- eight-contact total direct coupling to CELL: **0.4226104 fF**;
- aggregate eight-contact -> GC: **0.022550324 fF**;
- aggregate eight-contact -> GR: **0.022550324 fF**;
- contact DSC: **0% at extraction precision**;
- NERVE -> GC: **0.01448 fF**;
- NERVE -> GR: **0.01448 fF**;
- ARTERY -> GC: **0.0123103 fF**;
- ARTERY -> GR: **0.0123103 fF**.

The service and contact field therefore remain common-mode with this symmetric placement.

## Important individual-contact observation
Individual left/right contacts are not common-mode by themselves. For example, in the combined layout the closest face contact has about **0.00862081 fF** direct coupling into its nearby weak rail while the opposite-side term falls below the extractor's reported coupling list.

That means the architecture must not reason:
`total symmetric layout -> every possible contact event is harmless`.

A single asymmetric aperture transition can still create local differential injection. The next switch-level experiment must stress one contact at a time and skewed contact activity, not only all-contact averages.

## What happened
The physical geometry supports the basic v13Q idea better than expected: eight candidate neighbour pads plus Nerve + Artery fit around a compact local state while preserving zero aggregate weak-pair asymmetry in the symmetric layout.

## Problem still open
This is **not** the final off-state capacitance of a Contact Aperture because no MOS pass/isolation transistor has been inserted. A real switch will add gate/drain/source and diffusion parasitics. On-state propagation delay/energy and PVT/mismatch are also still unknown.

The geometry therefore proves only:
- the contact conductor topology is legal;
- symmetric placement can keep aggregate service/evidence coupling matched;
- contact-count loading is in a sub-fF direct-coupling range at this scale;
- diagonal/corner conductor geometry is not automatically worse than face geometry.

## Decision
### KEEP
- four face contacts as physical baseline;
- compact corner/diagonal contacts as candidates;
- symmetric placement around weak differential state;
- separate Nerve and Charge Artery;
- sign off individual-contact coupling, not just the aggregate.

### Do not claim yet
- 26 physical 3-D contacts/cell are practical;
- these pads are electrically selectable apertures;
- dormant switch loading is closed;
- quorum/confidence transistor cost is negligible;
- this layout is the final ECC.

## Next — v13Q1b switch-level aperture
Insert the smallest real body-tied SKY130 MOS isolation device between one external neighbour pad and one local regenerated event/state node. Compare:
1. face aperture;
2. compact corner aperture;
3. aperture absent / dedicated short Nerve baseline.

Measure off leakage/capacitance, on resistance/delay/event energy, individual GC/GR disturbance, TT/FF/SS and mismatch. Then scale the physically selected aperture to a four/eight-contact repeated cell before considering a larger 3-D contact count.
