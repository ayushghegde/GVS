# Current Next Experiment — v13C3 Physical Shared-Service Eight-Cell Slice

## What is already solved

The physical locality path remains:

`orthogonal coordinate -> compact coordinate release -> Regional Event Lease -> 8 isolated local event paths`.

New v13C results now add:

- **v13C0 exclusion audit:** 29 distinct explicit rejected/not-default idea families were identified in the two master audit files after merging obvious duplicates; v13C now separates principle rejection from implementation/mode/process rejection so useful old mechanisms are not accidentally discarded;
- **v13C1 wired shared wall:** a 100 um SKY130 M4 wall proxy shows an unshielded service line couples ~1.184 fF into each weak analog face, enough for a ~29 mV worst charge-sharing kick on the present ~72 fF evidence-node proxy; adding reference shields removes direct extracted service-to-evidence capacitor terms in the tested geometry;
- **v13C1 two-service proxy:** two robust service wires can coexist between outer shields; direct service-to-evidence terms remain absent in extraction, while service-to-service coupling is ~2.386 fF/100 um and therefore must be treated as robust/slow routing;
- **v13C2 eight-cell service-spine model:** a 2x2x2 cell block reduces independent wall-panel count from 48 to 36 by sharing common walls; a simple shared 100 um trunk + eight 10 um branches reduces protected control-wire length/capacitance proxy by ~77.5% versus eight separate 100 um protected routes.

## Architecture rule added by v13C

Every old rejection is classified as one of:

- `PRINCIPLE_REJECTED` — keep rejected unless fundamentally new evidence changes the need;
- `IMPLEMENTATION_REJECTED` — underlying physics remains available with a different topology/control;
- `MODE_ONLY` — use only when workload/area/margin makes it win;
- `FUTURE_PROCESS` — unavailable/uneconomic in current SKY130, not physically impossible.

This protects mechanisms such as stored-leak adaptation, one-way recovery, direct analog context, selective Grammar, and targeted 3D from being lost merely because one earlier implementation failed.

## Selected shared wall

Use a **Service Spine Wall**:

`cell-A capacitor face -> dielectric -> robust shield/reference -> protected service lanes -> robust shield/reference -> dielectric -> cell-B capacitor face`

Preferred service lanes:

- v12A-style shared environment/PVT pilot state;
- validated-use promotion/demotion control;
- one-way expired-charge recovery;
- VDD/GND/reference;
- static/burst-amortized fourth-face enable;
- robust winner/event/Myelin-chord landing.

Do not route tiny GC/GR/dendrite/latch-internal analog state through the shared service spine.

## Next physical experiment — v13C3

Build one physically extracted eight-cell service slice in ordinary SKY130 geometry before any literal hollow-package claim.

Required:

1. two weak analog evidence traces on opposite sides of at least four shared wall sections;
2. two robust service lanes inside the protected spine;
3. one reference/recovery shield structure;
4. two v12A-style replica pilot inputs shared across the eight local contacts;
5. at least two physical Use Reservoir / validated residual-tap paths;
6. one fourth-face gate branch;
7. three timed phases: configure before evidence, hold service lines static during weak evidence, then cleanup/recovery after decision;
8. TT/FF/SS plus independent mismatch;
9. measure analog kick, service/service crosstalk, evidence margin, promotion/demotion correctness, recovered charge, wire/source energy and area;
10. compare against separate walls + separate protected routes;
11. if this passes, populate the same region with real Grammar/template/Myelin structures behind the eight-way lease.

## Acceptance

The shared service framework survives only if:

- no service transition during the protected evidence phase creates a false decision;
- raw/noisy events cannot train a contact;
- validated repeated use can train it;
- cleanup/recovery never loads live evidence;
- shield/service overhead is smaller than the routing/reader/framework it removes;
- exact fallback remains independent.
