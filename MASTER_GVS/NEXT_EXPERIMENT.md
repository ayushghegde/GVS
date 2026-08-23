# Current Next Experiment — v13K5 Physical Neurovascular Cell Slice

## What v13K has established

### v13K0 — Neurovascular cell anatomy
Each cell/cluster now has physically separate service roles:
- **Nerve** for firing/events;
- **Charge Artery** for expired-charge collection;
- **Thermal Capillary** for passive heat removal;
- optional **Light Nerve** for long/hot/reused relations;
- direct fourth-face contact for paired neighbors.

Cells/support may occupy outer, inner, underside and side surfaces when fabrication and total cost justify it. Shared controller/memory/exact functions live in Component Bays / Exact Service Cores rather than one microcontroller per cell.

Illustrative 10x10x2 mm shell with 0.2 mm framework gives 1.878x inner+outer surface versus outer alone; after 30% service reserve the geometry still leaves ~1.31x outer-only usable surface.

### v13K1 — low-swing artery disturbance
Using the existing conservative 0.124 fF coupling proxy to a 72 fF weak node:
- 1.8 V high-swing utility step -> ~3.09 mV kick;
- actual regional-recovery swing ~0.1990 -> 0.2893 V -> only ~0.155 mV per artery.

Even 32 perfectly aligned low-voltage artery transitions leave about 20.0 mV from a 25 mV differential in the first-order model, still above the 18 mV high-margin screen.

Normal recovery therefore should not need a universal global quiet window. High-swing exceptional power/config/test traffic remains separately shielded/staggered only when measured coupling requires it.

### v13K2 — recovery/thermal scaling
Using the v13C line-capacitance proxy:
- one 0.5 mm Charge Artery ~31.16 fF;
- four branches ~124.62 fF = ~1.25% of a 10 pF regional reservoir;
- branch-capacitor energy over the preserved 0.1990 -> 0.2893 V recovery rise ~2.75 fJ versus ~220 fJ regional stored-energy reference.

Thermal collection is passive: every cell/small cluster gets a thermal capillary into a larger shared Thermal Artery/Exhaust; no per-cell pump/controller.

### v13K3 — integrated architecture
Direct fourth-face neighbor remains the shortest private electrical route (~0.15 fJ event proxy), ~77.6% below the one-tap event-spine proxy (~0.67 fJ).

The complete existing GVS core remains: Coordinate Release, 8-way Lease, Grammar, templates, Myelin, context, familiarity, homeostasis, event spine, shared recovery and exact fallback.

### v13K4 — component placement
Illustrative 32-region placement model:
- central interior Exact Service Core: average Manhattan route ~5.5 mm;
- top/bottom center: ~6.0 mm;
- side center: ~8.0 mm;
- top corner: ~11.0 mm.

Using the existing 3.74 fJ/mm route proxy only for comparison, frequently accessed exact/memory support favors central/interior placement, while large/hot/slow/test-facing support favors exterior/backside placement.

## v13K5 physical goal
Build the first same-die electrical **Neurovascular Cell Slice**. Do not add more control logic unless a measured failure requires it.

### Required physical/electrical elements
1. one real weak Grammar/Tri-Wall evidence node from the existing SKY130 family;
2. one direct fourth-face or ~0.2 V local Nerve;
3. one separate low-voltage Charge Artery;
4. one simple recovery contact driven by the existing cleanup/expired-state lifecycle signal;
5. one regional recovery branch / scaled reservoir equivalent;
6. shield/service geometry between weak node, Nerve and Charge Artery;
7. exact/robust result capture independent of recovery.

### Battery
8. nominal TT/FF/SS;
9. independent mismatch launches;
10. Nerve active alone;
11. Charge Artery active alone after expiry;
12. Nerve + Charge Artery simultaneous;
13. multiple aligned low-voltage arteries as stress;
14. deliberately inject a high-swing 0.9/1.2/1.8 V facade-equivalent line for comparison;
15. verify unsafe high-swing disturbance causes fallback before wrong acceptance;
16. stuck-closed recovery contact -> energy loss only, no correctness loss;
17. stuck-open recovery contact during live state -> blocked by lifecycle/topology or converted to fallback, never silently accepted.

### Measurements
- extracted Nerve-to-evidence and Artery-to-evidence coupling;
- exact/partial margin before and during simultaneous low-voltage service activity;
- false robust-result count;
- fallback count;
- regional recovery voltage and energy;
- Nerve event energy;
- added area/parasitic load versus direct fourth-face baseline.

### Separate manufacturability screen
18. map inner+outer+underside+side cell skins to practical stacked/backside technology;
19. reserve area for Nerve/Charge/Thermal/Optical services;
20. keep literal full inside-out active framework FUTURE_PROCESS until a credible fabrication stack exists.

## Acceptance
v13K5 passes only if:
- low-voltage Charge Artery operates without a global quiet window across PVT + mismatch;
- direct neighbor remains cheaper/simpler than routing through a shared spine;
- recovery cannot corrupt live information;
- thermal path remains electrically passive;
- exact fallback remains independent;
- high-swing utilities remain isolated enough or fail safely.
