# Neural Glyph v13I0 — Full Hollow Architecture Comparison

**Verdict: CONDITIONAL PASS for the heterogeneous version, PASS as the default for the hollow-electrical base.**

This experiment compares two versions of the same hollow/framework GVS architecture instead of comparing against a deliberately weak electrical baseline.

## New terms

- **Hollow-Electrical Base (HEB):** hollow/framework GVS using Tri-Wall cells, direct fourth faces, shielded service walls, subwires/event spines, electrical/Myelin chords, component bays, exact fallback and the shared thermal exhaust, but no optical runtime carrier.
- **Hollow-Heterogeneous Extension (HHE):** HEB plus thin optical/TIR lightpipes, direct photocharge endpoints and rare optical-route consolidation only for long/hot routes that pass lifetime break-even.
- **Optional Photonic Layer (OPL):** photonics is not mandatory in every package; it is a package/region option installed only where expected lifetime traffic can repay its manufacturing and operating overhead.

## 1. Fair comparison rule

Both architectures keep the same already-validated local electrical stack:
- Active-Low Coordinate Release;
- eight-way Regional Event Lease;
- real Grammar/template/Myelin local primitives;
- direct fourth face for neighbors;
- v13E 0.9 V four-tap electrical event spine;
- familiarity/homeostasis/Use state;
- post-capture electrical recovery;
- exact fallback;
- shared walls, component bays and thermal exhaust.

HHE is not allowed to replace a cheaper local electrical mechanism merely because optics is available.

Electrical long-route runtime proxy retained from v13H:

`E_electrical ~= 0.15 fJ + 3.74 fJ/mm * distance`

Thin-TIR/direct-photocharge runtime proxy:

`E_optical ~= 10.862 fJ + 0.0094 fJ/mm * distance`

Rare optical route-write/consolidation cost:

`~1000 fJ` per promoted route.

The optical values remain model + literature backed, not SKY130 physical signoff.

## 2. Eight-region geometry

Use eight regions at the corners of an illustrative 10 mm cube. Pair distances:
- 12 edge routes at 10 mm;
- 12 face diagonals at 14.14 mm;
- 4 body diagonals at 17.32 mm.

Every relation may remain electrical. Optical is used only if:
1. route is eligible/hot;
2. lifetime optical energy including route write is lower;
3. an optical lane/source exists;
4. exact/electrical fallback remains available.

## 3. Lifetime communication result

Expected communication energy was calculated over hot-route fractions of 25%, 50% and 100%.

| uses/relation | hot fraction | optical-economic routes if hot | HEB lifetime | HHE expected | saving |
|---:|---:|---:|---:|---:|---:|
| 16 | 50% | 0/28 | 21.55 pJ | 21.55 pJ | 0% |
| 32 | 50% | 16/28 | 43.10 pJ | 39.58 pJ | ~8.17% |
| 64 | 50% | 28/28 | 86.20 pJ | 66.94 pJ | **~22.34%** |
| 128 | 50% | 28/28 | 172.39 pJ | 119.88 pJ | **~30.46%** |
| 256 | 50% | 28/28 | 344.78 pJ | 225.75 pJ | **~34.52%** |

At 64 uses with every route hot, the communication reduction reaches ~44.68%. At 16 uses no route qualifies.

This is deliberately more conservative than the earlier candidate-selection result because it treats hotness probabilistically rather than giving the optical architecture only the longest routes.

## 4. Existing workload test

Reuse v13A local-core and remaining long-event counts. Screen at 10 mm, 50% optical eligibility and 64 lifetime uses.

| domain | HEB | HHE | total saving |
|---|---:|---:|---:|
| image | 26.397 pJ | 26.364 pJ | ~0.125% |
| sound | 512.708 pJ | 511.831 pJ | ~0.171% |
| code | 0.942 pJ | 0.810 pJ | **~13.97%** |
| reasoning | 1.173 pJ | 1.157 pJ | ~1.40% |

If one operation from each domain is simply summed, total energy changes from ~541.22 pJ to ~540.16 pJ: only **~0.196%**.

Therefore the heterogeneous extension is not automatically a whole-system energy win. It mainly helps route-dominated workloads/regions. Code is the strongest current example because local motif/dispatch work is already tiny.

## 5. Optical-source idle-power problem

The runtime optical comparison only includes energy associated with transmitted events. A continuously powered optical source can erase the advantage.

At 10 mm:
- HEB electrical event ~37.55 fJ;
- HHE optical runtime ~10.96 fJ;
- with route write amortized over 64 uses, optical total ~26.58 fJ;
- remaining advantage ~10.97 fJ/promoted event.

Therefore, at 64-use lifetime, any shared-source idle energy amortized onto each promoted event must remain below ~10.97 fJ.

Equivalent idle-power budgets:
- 1 MHz promoted event stream -> ~0.011 uW;
- 100 MHz -> ~1.10 uW;
- 1 GHz -> ~10.97 uW;
- 10 GHz -> ~109.7 uW.

At 128 uses, the 1 GHz budget rises only to ~18.8 uW.

**Decision:** optical source generation must be shared, burst-gated or otherwise near-zero-idle from the point of view of promoted traffic. If realistic source standby/tuning exceeds this budget, the carrier compiler must leave the route electrical.

## 6. Volume

A conservative 50 x 50 um lightpipe lane over the mean 12.82 mm route uses ~0.032 mm^3 per route.

For a 10 mm cube (1000 mm^3 illustrative volume):
- 7 lanes -> ~0.224 mm^3 (~0.022%);
- 14 lanes -> ~0.449 mm^3 (~0.045%);
- all 28 lanes -> ~0.897 mm^3 (~0.090%).

This counts only reserved lane volume, not emitters, detectors, switches or alignment structures.

The result supports thin TIR/lightpipe routing: the optical path itself need not reserve component-sized tunnels.

## 7. Manufacturing-complexity comparison

### HEB required integration classes
1. CMOS/MIM active framework;
2. metal/service-wall interconnect;
3. hollow/3D structural assembly;
4. component-bay attachment/exact memory/logic;
5. shared thermal exhaust / heat-spreader or vapor structure.

### HHE adds
6. optical emit/modulate/detect devices;
7. lightpipe/waveguide fabrication or placement;
8. optical alignment and test;
9. optical source coupling/distribution;
10. optional nonvolatile optical-route switch technology.

This is not a dollar cost ratio. It is a process/integration count.

Current integrated-photonics literature reports that packaging, assembly and testing can represent roughly 70-80% of PIC manufacturing cost, compared with about 20% in electronic IC packaging. Active alignment is specifically identified as a major cost/throughput barrier. Therefore **HEB has the lower manufacturing cost with current technology**.

The HHE manufacturing penalty could fall if passive self-aligned lightpipes, wafer-level optical testing and source integration become routine, but that is not assumed in v13I.

## 8. Thermal architecture is common, not an excuse for optics

Both HEB and HHE use the large shared Thermal Exhaust architecture:

`hot regions/chips -> spreader/wick -> component-free vapor/thermal channel -> common top condenser/heat exchanger -> optional large heat harvester -> outside/useful heat loop`.

Do not put TEGs at every cell.

Published low-grade TEG systems remain modest electrical converters. Examples include ~1.92% conversion at a 70 C temperature difference in one optimized modular study and ~125 W from a modeled 25 kW server-rack heat stream (~0.5%) in a heat-pipe/PCM/TEG study, while useful hot-water heat was much larger.

Therefore recovered thermal electricity is not allowed to rescue an otherwise inefficient architecture. Cooling and useful heat export are the primary roles; electricity harvest is secondary.

## 9. Running-cost decision

### Typical mixed local workloads
HEB wins or is effectively tied because local computation dominates and HHE's communication savings are too small to repay optical manufacturing/idle overhead.

### Long/hot route-dominated workloads
HHE can win materially:
- ~22% communication reduction at 64 uses, 50% hot routes in the eight-region model;
- ~30% at 128 uses;
- ~35% at 256 uses;
- code-domain total ~14% lower in the 10 mm/64-use screen.

### Low-use routes
HEB always wins because optical route-write/source overhead cannot be repaid.

## 10. Selected product architecture

Do not make every hollow chip heterogeneous.

Selected structure:

**Base chip/package:** HEB.

**Optional high-end/package extension:** OPL installed only when floorplan/workload analysis predicts enough long repeated traffic.

Conceptually this is like leaving conduits in a building: the structural design permits an optical service layer, but the expensive equipment is installed only when there is a reason.

## 11. Final v13I0 decision

### KEEP as universal/default
- hollow electrical framework;
- Tri-Wall/fourth-face local links;
- subwires/event spines;
- electrical Myelin chords;
- component bays;
- shared thermal exhaust;
- exact fallback.

### KEEP as optional
- thin TIR optical layer;
- direct photocharge endpoint;
- rare nonvolatile optical route consolidation;
- optical dendrite/fanout only for long sparse promoted relations.

### Reject as universal
- photonics in every cell/region;
- permanently powered optical source that cannot meet idle-energy break-even;
- optical route selected only because it is geometrically possible.

## 12. What remains uncertain

- photonic endpoint physical signoff in a compatible process;
- real source standby/startup/tuning energy;
- optical alignment/yield inside the proposed hollow package;
- real thermal-fluid dimensions and pumping pressure;
- actual manufacturing BOM/yield, not just process-complexity ranking;
- full real trace replay rather than preserved event-count workload proxies.
