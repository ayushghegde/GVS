# Neural Glyph v13C2 — Eight-Cell Shared-Service Framework Screen

**Verdict: KEEP — a shared-wall framework can reduce both duplicated structure and duplicated control-wire length, but the energy win comes only if service trunks are shared and mostly static/slow. This is an architecture model using v13C1 extracted wire capacitance, not a full eight-cell PEX.**

## 1. Eight-cell geometry

Use a simple 2x2x2 block = 8 framework cells.

If every cell owns six independent wall panels:
- wall panels = 8 x 6 = **48**.

If neighboring cells physically share their common wall:
- unique wall panels = `(nx+1)ny nz + nx(ny+1)nz + nx ny(nz+1)`;
- for 2x2x2 = **36** unique panels.

So even this tiny finite block removes **12 duplicated wall panels = 25% fewer wall panels**. As the region becomes larger and boundary walls become a smaller fraction, the duplication saving tends toward ~50% for interior walls.

This is consistent with the v13B4 periodic-thickness screen, where `t/p=0.1` reduced framework material by ~44.5% versus independent shells.

## 2. Service-wire sharing model

From v13C1, the shielded 100 um service-lane proxy has about **6.231 fF** effective capacitance when its ground/shield mutual terms are counted.

Naive separate-control model:
- eight cells each require one separate 100 um protected control lane;
- total routed service length = **800 um**;
- capacitance proxy = **49.85 fF**;
- ideal 1.2 V full charge/discharge source-work proxy = **~71.8 fJ**.

Shared-spine model:
- one 100 um shared wall trunk;
- eight 10 um local protected branches;
- total routed length = **180 um**;
- capacitance proxy, assuming first-order linear length scaling = **11.22 fF**;
- 1.2 V source-work proxy = **~16.2 fJ**.

Proxy reduction in this deliberately simple configuration:
- wire length: **77.5%**
- control-line source-work: **~77.5%**

This is not a whole-region energy claim. Local gate charge, reservoir write energy, branch vias, drivers, shields and recovery circuitry must still be added in physical PEX.

## 3. What should be shared on the service spine

Best candidates:
- two v12A-style PVT/environment pilot lines shared across the eight-cell region;
- robust reference/ground shields;
- regional expired-charge recovery rail;
- slow promotion/demotion control;
- static or burst-amortized fourth-face configuration;
- robust region winner/event lines.

Do not share one sensitive analog evidence node among cells. Each Tri-Wall evidence state and Contact Receptor remains local.

## 4. Architecture consequence

The framework now mirrors the old successful regional-sharing rule:

`local sensitive state -> private`

`slow environment/support/recovery -> shared`

`validated robust meaning -> may travel`

This is the same reason v12A used two pilot devices for eight routers rather than duplicating a PVT sensor per neuron, and the same reason the current Regional Lease shares long selection while keeping eight event outputs isolated.

## 5. Next physical closure

The next v13C physical layout should place two analog evidence traces on opposite sides of a real shared service spine containing at least:

- two service wires;
- one reference/recovery shield;
- one local branch to a fourth-face MOS gate;
- one branch to a small Use Reservoir;

then run full extraction and transient switching during three phases:

1. service/config changes before evidence capture;
2. weak analog evidence capture with service lines static;
3. post-decision cleanup/recovery activity.

Acceptance requires no false analog decision, no raw/noisy promotion, and a material energy/area reduction versus separate protected service routes.
