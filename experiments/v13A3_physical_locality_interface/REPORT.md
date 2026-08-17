# Neural Glyph v13A3 — Compact Physical Locality Interface

**Verdict: PARTIAL PASS — co-placed physical coordinate-release + Regional Event Lease passes DRC, extraction, PVT, incomplete-coordinate tests, and 12/12 combined mismatch. Full historical-v12S signoff still waits for a compatible continuous-model simulator path.**

## What this experiment combines

The selected physical chain is now one layout, not two separately extracted blocks:

`ROWB/COLB -> 4T active-low coordinate release -> physical M4 PRE handoff -> 5-NFET Regional Event Lease + 2x2 MIM -> local 0.2 V event`

The coordinate cell is a 4-transistor active-low NOR-style release:
- 2 series PFETs, W=0.84 um / L=0.15 um;
- 2 parallel NFET clamps, W=0.42 um / L=0.15 um.

The Regional Lease retains the v13A1 topology:
- min write NFET;
- min validated-success refresh NFET;
- W=1/L=8 um weak-leak NFET;
- min DONE/CLEAN clear NFET;
- min local event-gate NFET;
- one 2x2 um M3 MIM plus useful extracted WAKE parasitics.

## Physical construction lessons

Two DRC-clean coordinate layouts were rejected before the final routing was accepted:

1. a VDD/body-tap M2 route crossed PRE, electrically collapsing the PFET chain;
2. the second-PFET M1 route crossed its opposite diffusion terminal, collapsing the PMOS midpoint into PRE.

Both were legal geometries from a spacing-rule perspective. Extraction, not DRC, exposed the topology errors.

The selected fix routes the second-PFET PRE connection on M3, preserving a distinct PMOS midpoint while keeping the cell at four transistors.

Selected coordinate cell:
- DRC errors: 0;
- extracted devices: exactly 2 NFET + 2 PFET;
- separate VDD, PRE, ROWB, COLB, GND and PMOS midpoint.

## Co-placement

The first correct co-placement intentionally left roughly a 10 um gap between coordinate and lease cells. It passed, but was unnecessarily large.

The selected tighter placement reduces the gap to roughly 2 um and routes PRE on M4 so it can cross the lease's M2 WAKE and M3 GND structures without touching them.

Bounding boxes:
- roomy combined interface: ~38.02 um x 22.0 um = **~836.44 um^2**;
- selected compact interface: ~30.02 um x 22.0 um = **~660.44 um^2**;
- combined bounding-box reduction: **~21.0%**.

The extracted PRE-to-substrate capacitance also drops from roughly 4.94 fF in the roomy placement to roughly 4.19 fF in the selected compact placement.

## Physical extraction

Selected compact combined layout:
- DRC errors: 0;
- extracted intended devices: 9 NFET + 2 PFET + 1 MIM = the expected 4T coordinate + 5T lease + capacitor;
- physical PRE route connects the coordinate release to the lease diode-write device;
- WAKE remains a separate storage node;
- ROWB/COLB remain separate;
- no accidental coordinate-to-WAKE short.

Coordinate and lease grounds are exposed as separate local ground shapes in the extraction and are tied to the same external ground in the transient bench. A future regional power-grid layout should make that shared ground connection physical rather than relying on an external common node.

## PVT result — selected compact combined PEX

12-event refreshed local burst:

- TT: PRE peak ~1.81222 V; WAKE at event 12 ~1.12060 V; minimum event ~0.200245 V; PASS.
- FF: PRE peak ~1.80631 V; WAKE ~1.20183 V; minimum event ~0.200065 V; PASS.
- SS: PRE peak ~1.81649 V; WAKE ~1.03028 V; minimum event ~0.200142 V; PASS.

DONE/CLEAN clears the lease after the burst.

## Incomplete-coordinate screen — selected compact combined PEX

At the slow SS corner, with **no validated refresh**:

- row-only: PRE peak ~0.901 mV; WAKE peak ~0.691 mV; local event only ~0.345 mV;
- column-only: PRE ~2.54 mV; WAKE ~1.41 mV; local event ~0.349 mV;
- none: PRE essentially zero; WAKE ~0.465 mV; local event ~0.345 mV;
- deliberately partial coordinate: PRE ~55.5 mV; WAKE ~0.844 mV; local event ~0.345 mV.

None approaches the intended ~0.2 V local event.

## Combined mismatch result

Mismatch is applied to coordinate and lease transistors in the same PEX system.

Four launches per corner: **12/12 PASS**.

Weakest event-12 WAKE:
- TT mismatch: ~1.1035 V;
- FF mismatch: ~1.1817 V;
- SS mismatch: **~0.99049 V**.

All twelve local events remain essentially full ~0.2 V. DONE clear remains inside the existing +/-30 mV cleanup screen.

## Architecture invariant retained

Only **validated local success/winner state** may refresh the lease. Raw sensory/event activity, noise, incomplete coordinates and unselected regions may never refresh it.

This is important because the lease is a locality state, not a confidence detector. Confidence/winner validation remains in the existing Glyph computation.

## What this solves

The v13A locality idea now has a physically extracted interface:

- one real coordinate selection can open a local region;
- the physical region can remain useful across at least 12 validated local events;
- incomplete coordinates remain blocked;
- no digital event counter/scheduler is required;
- the coordinate and lease can be compacted without giving up PVT/mismatch behavior;
- long-wire activity can be amortized before local Grammar/template/Myelin work.

## Current problem

The next bottleneck is no longer the coordinate/lease interface itself. It is **what local work should sit behind one lease, and how cheaply several such interfaces share power/event wiring in a real region**.

The next experiment should build a small physical region rather than another isolated interface:

1. one orthogonal row/column coordinate enters the selected compact locality interface;
2. the lease feeds multiple local Grammar/template/Myelin event paths;
3. validated local winners refresh the lease;
4. inactive local paths remain physically quiet;
5. measure whether sharing one interface across 4-8 local event structures saves more wiring/area than duplicating an interface per structure;
6. keep exact fallback independent;
7. extract real local fanout/coupling and compare against v13A communication-cost thresholds.

A complete historical-v12S lifecycle rerun remains a separate simulator/tooling task: do not redesign v12S to compensate for the current ngspice build's inability to parse the continuous SKY130 model deck used by the historical baseline.
