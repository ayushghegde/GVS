# Neural Glyph v13Q1b — Real MOS Contact-Aperture Placement

**Verdict: PHYSICAL PLACEMENT PASS / TRANSIENT PVT OPEN.** A real SKY130 NFET can implement the selectable `NEIGHBOR <-> CELL` contact, but it must live at the cell boundary rather than beside the weak Grammar evidence core.

## Contact Aperture switch
The experiment reuses the recovered real `nf_cross` SKY130 `sky130_fd_pr__nfet_01v8` layout as a single pass/isolation device. Its source is routed to `NEIGHBOR`, drain to `CELL`, and gate to `AP_GATE`.

This is not a new transistor invention; it is a new placement/use of a preserved physical device.

## Variant A — switch beside weak evidence
The switch body and short routes were placed between nearby GC/GR weak rails.

Result:
- DRC: **0**;
- one real NFET instance extracted;
- `NEIGHBOR -> GC`: **0.00622776 fF** reported while the corresponding `NEIGHBOR -> GR` term was below the reported coupling list;
- `AP_GATE -> GC`: **0.0108039 fF**;
- `AP_GATE -> GR`: **0.00970849 fF**;
- additional child source/drain/gate couplings were also unequal because the device itself has left/right orientation.

**REJECT this placement.** A DRC-clean switch near the weak differential core can introduce physical-side preference.

## Variant B — switch moved to the cell wall
The same real NFET and same logical `NEIGHBOR <-> CELL` function were moved above/outside the GC/GR weak-evidence region. The weak rails remained unchanged.

Result:
- DRC: **0**;
- one real NFET instance extracted;
- source merged correctly to `NEIGHBOR`;
- drain merged correctly to `CELL`;
- gate merged correctly to `AP_GATE`;
- Magic reported **no direct aperture-switch/route coupling terms to either GC or GR at extraction precision**;
- the local `NEIGHBOR <-> CELL` route still has a reported direct geometric coupling term of **0.016098 fF**, in addition to the preserved NFET intrinsic source/drain/gate parasitics.

**KEEP this placement for switch-level transient testing.**

## What happened
The first switch implementation found exactly the risk predicted by v13L: even a tiny legal device can bias a weak differential pair when the device orientation is physically close to only one side.

The problem was solved by anatomy rather than control logic:

`weak evidence core in cell interior -> local robust/regenerated state -> aperture switch at boundary -> neighbouring cell`

That is compatible with the user's cell-as-wire idea because the communication hardware becomes part of the cell wall while the sensitive computation remains deeper inside the cell.

## Architectural consequence — computational core and conductive skin
An Embodied Conduction Cell should be internally compartmentalized:
- **core:** Grammar/template/constraint/analog confidence state;
- **wall compartment:** local integration/regeneration;
- **boundary aperture:** selectable MOS contact to neighbour;
- **separate service anatomy:** Charge Artery and Thermal path.

A cell can therefore communicate from any useful face/edge/vertex in a future 3-D implementation without placing every switch directly on top of the weak analog state.

## What remains open
- flattened full aperture parasitics;
- actual off leakage;
- on resistance and propagation delay;
- low-swing event energy;
- TT/FF/SS and mismatch;
- multi-aperture simultaneous switching;
- physical quorum/population-confidence circuit;
- real 3-D edge/vertex contact process.

## Next
Build v13Q1c using the remote-wall aperture:
1. flatten/extract the NFET + routes;
2. run a low-swing neighbour event through the switch;
3. measure on/off behavior and energy;
4. stress one aperture, several apertures, and skewed activity near the weak pair;
5. compare against a dedicated short Nerve;
6. keep unresolved population state local until confidence is strong enough for boundary regeneration.

Do not move the switch back toward GC/GR merely to save route length.
