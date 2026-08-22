# v13C Architecture Addendum

## Why v13C exists

v13C prevents useful physical ideas from being lost when one implementation fails, and turns the shared silicon/framework wall into active infrastructure rather than dead structure.

## Rejection taxonomy

- `PRINCIPLE_REJECTED`: underlying idea loses for the tested need.
- `IMPLEMENTATION_REJECTED`: keep the principle; this topology/sizing/control failed.
- `MODE_ONLY`: useful only under a measured workload/area/margin condition.
- `FUTURE_PROCESS`: not available/economic in current SKY130 but not physically forbidden.

The current master audit contains 29 distinct explicit rejected/not-default idea families after merging obvious duplicates. At least a dozen are implementation/mode/process rejections rather than reasons to discard the underlying principle.

## Shared-wall rule

Selected wall structure:

`weak cell-A capacitor face -> dielectric -> robust shield -> protected service lanes -> robust shield -> dielectric -> weak cell-B capacitor face`

The protected middle may carry:
- PVT/environment pilot state;
- promotion/demotion control;
- expired-charge recovery;
- VDD/GND/reference;
- static/burst-amortized fourth-face enable;
- robust event/Myelin-chord landing.

Do not put tiny GC/GR/dendrite/latch-internal analog state on the service spine.

## Physical evidence

v13C1 100 um M4 proxy:
- unshielded SERVICE-to-evidence mutual C: ~1.184 fF per side;
- ~29 mV worst charge-sharing kick on the present ~72 fF evidence-node proxy for a 1.8 V transition;
- shielded proxy: no direct SERVICE-to-evidence capacitance term extracted at the tested geometry/resolution;
- two-service shielded proxy: no direct service/evidence term extracted, service-to-service mutual ~2.386 fF/100 um.

Therefore wires in a shared wall are selected only with dielectric isolation + shielding and with weak analog evidence kept on the protected faces.

## Regional consequence

A 2x2x2 eight-cell framework has 48 independent wall panels but only 36 unique panels when neighbors share walls. A simple service-trunk model using v13C1 capacitance reduces protected control-route length/capacitance by ~77.5% versus eight separate 100 um routes when one 100 um trunk + eight 10 um branches is sufficient.

These are geometry/wire proxies, not whole-chip measurements.
