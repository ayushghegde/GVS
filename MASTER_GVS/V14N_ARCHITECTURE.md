# Neural Glyph v14N — Seeded Nodal Diffusive Relay

**Status:** model-level speed/transport experiment derived from v14M. No fabricated v14N device is claimed.

## Problem inherited from v14M
v14M simplified the semantic core to one Bimodal Diffusive Junction (BDJ) device type, but its hardest physical target is switching delay. In Ag/HfO2-class electrochemical-metallization devices, the delay is dominated by stochastic ionic/atomic filament nucleation and growth rather than electron transit through metal wiring.

## New device target — Seeded Nucleation BDJ (SN-BDJ)
The simplest speed intervention is to predefine a preferred filament birthplace/path.

Target concept:

Ag / very thin HfO2-class dielectric / sparse embedded Ag seed-island / Pt or TiN-class bottom electrode

The seed island is not a stored bit. It is a permanent geometric/material field-focus point intended to:
- reduce the effective Ag migration distance;
- reduce the nucleation search volume;
- increase local electric field at the intended filament path;
- reduce switching-delay and threshold dispersion;
- retain the v14M low-current volatile regime and higher-stress nonvolatile regime if physically possible.

A thin diffusion-limiting barrier may be added only if endurance requires it. It is not part of the minimum first stack.

## Why this is physically motivated
Recent HfO2 threshold-switching experiments report that embedded Ag nano-islands facilitate and constrain filament formation, can remove electroforming, and improve threshold consistency. Other current work attributes switching delay to field-lowered nucleation and Ag+ drift. This supports pre-seeding as a relevant speed/variation lever, but does not prove the v14N delay target.

## Path-length screen
A deliberately simple physical sensitivity bracket was used. If effective ionic travel distance is reduced from d to d/2:
- a path/drift-limited delay model gives about 2x speedup;
- a stronger field-drift sensitivity gives up to about 4x speedup.

Thus a 55-75 ns starting device could land in roughly 14-38 ns if the effective active distance is halved. This is an engineering target range, not a measured result.

## Nodal transport — Sparse Regeneration Trunk (SRT)
Nodes of Ranvier inspire one architectural rule only: do expensive active regeneration at sparse points while passive current travels through low-loss segments between them.

v14N applies this only to **physical transport hops inside a long relation wire**, not to semantic reasoning transitions. A semantic decision cell still fires whenever the reasoning graph requires a decision.

A 64-physical-hop transport proxy used:
- passive segment delay proportional to segment_length^2 (Elmore-like proxy);
- passive amplitude loss per hop;
- one BDJ regeneration event at the end of each segment;
- current v14M event-energy proxy of 2.315 fJ/regeneration.

With a 30 ns junction mean, the selected robust point was about 22 physical hops between regeneration sites:
- 3 regeneration junctions across 64 physical hops;
- 100% success in 10,000 model trials;
- mean transport delay ~172 ns;
- p95 ~199 ns;
- modeled transport energy ~9.19 fJ.

An active-junction-at-every-hop control in the same proxy takes ~1.93 us and ~150 fJ. This is not a silicon interconnect measurement.

## Favorable CMOS transport control
A deliberately favorable control used a 5 fF, 1.8 V, 6 ns CMOS repeater every four physical hops, with the same passive-link proxy and no SRAM/clock/decoder overhead:
- delay ~111 ns;
- energy ~261 fJ.

At the current 30 ns BDJ target, v14N is slower in raw transport latency but has much lower modeled energy and energy-delay product. If seeded junction delay reaches ~10-15 ns, the same sparse-regeneration proxy approaches or beats this favorable raw-latency control while retaining much lower modeled energy.

## Important separation
SRT solves transport overhead. It does NOT make an eight-step reasoning chain become one step. Each semantic transformation still requires its own physical state transition. Device-level SN-BDJ speed remains necessary.

## Keep / reject
KEEP:
- v14M one-device-type goal;
- pre-seeded field-focused filament formation as the simplest speed target;
- sparse active regeneration on long physical trunks;
- v14K provisional understanding and self-test;
- semantic connection state in sparse two-terminal links.

REJECT:
- active BDJ repeaters on every physical routing hop;
- claiming Nodes of Ranvier means skipping semantic reasoning cells;
- adding complex multilayers before the simple seed-island stack is tested;
- combining speed numbers from different papers as if one v14N device were measured;
- per-device MOS current compliance.
