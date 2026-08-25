# Neural Glyph v13M1 — Hollow Surface Route Compiler

**Verdict: MODEL PASS, with one architecture rejection: REJECT mandatory surface-only signal routing.** Cells and service networks may occupy the hollow surfaces, but a signal relation may use a direct fourth-face link, short nerve, interior electrical/Myelin chord or optional optical route when that is cheaper/shorter.

## Why this experiment
The hollow chip idea is useful only if it reduces total cost. A tempting but dangerous interpretation is that, once cells occupy outer/inner/side/underside surfaces, every signal should also travel around those surfaces.

v13M1 tests that assumption directly.

## Geometry
Illustrative 10 x 10 x 2 mm cuboid, matching the preserved v13K geometry class. Boundary locations are sampled on a 2 mm x/y and 1 mm z grid.

For every pair of boundary locations, compare:
- unrestricted Manhattan route through the package/interior;
- shortest route constrained to the cuboid boundary surface.

The existing electrical runtime proxy is applied only as a relative communication comparison:
`E ~= 0.15 fJ + 3.74 fJ/mm * distance`.

This is a geometry/model experiment, not PEX.

## Result over 4,186 boundary-location pairs
| pair class | mean surface detour | p95 | max | mean electrical penalty |
|---|---:|---:|---:|---:|
| all pairs | 1.049x | 1.40x | 5.0x | **2.98%** |
| share a face | 1.00x | 1.00x | 1.00x | 0% |
| different non-opposite faces | 1.00x | 1.00x | 1.00x | 0% |
| opposite faces | **1.137x** | 1.667x | **5.0x** | **6.88%** |

The mean penalty looks small, but the tail matters.

### Worst case
Two cells directly opposite across the 2 mm thickness near the center:
- direct/interior distance: 2 mm;
- surface-constrained distance: 10 mm;
- electrical proxy: ~7.63 fJ direct versus ~37.55 fJ around the surface;
- **5x route-length penalty**.

Forcing that relation around the shell would throw away the benefit of the hollow structure.

## v13M routing decision
The architecture should use a **surface service fabric**, not a surface-only data fabric.

### Keep on or near surfaces
- weak/local computation skins;
- low-swing Nerve trunks/taps where convenient;
- Charge Arteries and regional recovery branches;
- passive Thermal Capillaries/Arteries;
- robust power/config/test service domains;
- optional optical lightpipes where the lifetime break-even is satisfied.

### Allow direct/interior crossings when they materially win
- touching cells -> direct fourth-face relation;
- opposite inner/outer cells with short physical separation -> short protected bridge/chord rather than a long surface detour;
- stable medium-distance relation -> promoted electrical/Myelin chord;
- long/hot/reused relation -> optional optical Light Nerve after break-even;
- ambiguous/cold/changing relation -> normal exact/global fabric.

No new global router/controller is needed. The placement/compiler can make this choice from geometry, reuse and confidence class.

## What happened
The hollow surface is excellent for organization and service separation, but it is not always the shortest communication manifold. Same-face and many adjacent-face routes pay no model penalty; opposite-face relations can be much worse if forced to remain on the boundary.

## Problem solved
v13M now avoids a new failure mode: turning the hollow architecture into an artificial long-wire network just because the surfaces exist.

## Next physical experiment
Build one **two-octet v13M region**:
- two eight-cell intelligent octets behind separate leases;
- direct fourth-face edges inside each octet;
- one shared low-swing Nerve spine;
- one shared Charge-Artery branch to a regional reservoir;
- thermal attachments represented physically/thermally where possible;
- one deliberately opposite-surface promoted electrical chord;
- optional optical route left unpopulated unless its expected reuse crosses the preserved break-even.

Replay a mixed local workload and measure how often work remains inside one octet, how often it crosses to the second, communication/selection energy, service coupling and exact fallbacks.

## Reproduce
From repository root:
`python3 experiments/v13M1_surface_route_compiler/source/run_v13m1.py`

Tool class: deterministic Python 3 geometry model using only standard-library code. No PDK/PEX claim is made by this experiment.
