# Neural Glyph v13H0 — Mixed Hollow Region Qualification

**Verdict: CONDITIONAL PASS.** The hollow heterogeneous design is measurably better than the best current all-electrical hierarchy only for routes that are both physically long and reused enough to amortize optical endpoint/route-write cost. Local/short traffic remains electrical. The large thermal-exhaust concept is kept, but heat harvesting is moved to a shared external/top boundary rather than placed on every cell.

## New terms
- **Thin TIR Lightpipe:** a narrow high-index transparent guide through the hollow volume; ordinary total internal reflection keeps light inside the guide without reserving a component-sized free-space corridor.
- **Thermal Exhaust Plenum:** component-free hollow thermal route shared by many regions/chips, carrying heat toward a common package/rack exhaust.
- **Top Heat Harvester:** one large shared external heat-recovery module serving many chips; it may include a condenser/heat exchanger and optional thermoelectric stage.

## 1. Fair baseline
This experiment does not compare optics against the old intentionally expensive 0.68 pJ global coordinate event alone. The primary comparison uses the improved dedicated electrical-route proxy from v13E/v13G:

`E_electrical ~= 0.15 fJ + 3.74 fJ/mm * distance`.

Nearest-neighbor fourth-face and regional event-spine traffic remain electrical and are not replaced by optics.

## 2. TIR route instead of a large empty optical corridor
Ordinary TIR requires a higher-index core surrounded by lower-index material, so a truly empty/air-core route is not the simplest TIR implementation. The selected architecture uses a skinny transparent glass/polymer lightpipe inside the hollow framework.

Literature-backed proxy used here:
- propagation ~0.08 dB/cm;
- endpoint/facet coupling ~0.47 dB each;
- direct-photocharge target from v13F: ~0.6 fJ detector-incident energy for a 3 fF receptor at a 0.2 V event with 80% QE;
- laser wall-plug scenario: 15%;
- modulator proxy: 5.9 fJ/event.

This yields ~10.9-11.1 fJ runtime optical event work over 3-20 mm because propagation loss is small compared with endpoint cost.

## 3. Distance and reuse crossover
Including a 1 pJ rare nonvolatile route-write/switch cost:

| distance | electrical runtime | TIR optical runtime | reuses to repay 1 pJ write |
|---:|---:|---:|---:|
| 3 mm | 11.37 fJ | 10.89 fJ | ~2102 |
| 5 mm | 18.85 fJ | 10.91 fJ | ~126 |
| 10 mm | 37.55 fJ | 10.96 fJ | ~38 |
| 15 mm | 56.25 fJ | 11.01 fJ | ~23 |
| 20 mm | 74.95 fJ | 11.05 fJ | ~16 |

Decision: do not promote 1-3 mm routes optically. Around 5 mm, only very hot routes qualify. Around 10-20 mm, tens of repeated validated events can repay the route-write cost.

## 4. Eight-region 3D system test
Eight regions were placed at the corners of an illustrative 10 mm cube. The 28 pair distances are:
- 12 edge pairs at 10 mm;
- 12 face diagonals at 14.14 mm;
- 4 body diagonals at 17.32 mm.

Every pair is allowed the best dedicated electrical route; hollow optics is chosen only if lifetime cost is lower after the 1 pJ write.

### Lifetime results
At 16 uses per relation: no optical route is worth promoting.

At 32 uses:
- 25% hot candidates -> ~9.1% communication saving;
- 50% hot -> ~14.7%;
- all candidate routes -> ~16.3% because only the longest subset passes break-even.

At 64 uses:
- 25% hot -> ~17.3%;
- 50% hot -> **~31.0%**;
- all 28 routes hot -> **~44.7%** communication saving.

At 128 uses:
- 50% hot -> ~39.1%;
- all hot -> ~60.9%.

At 256 uses:
- 50% hot -> ~43.2%;
- all hot -> ~69.0%.

This is the first fair hollow-versus-best-electrical lifetime result: the hollow/TIR design wins strongly only after physical distance and reuse both become substantial.

## 5. Existing image/sound/code/reasoning workloads
The preserved v13A local-core and communication-event counts were reused. To avoid cherry-picking, the screen assumes 10 mm long relations, 50% of remaining long relations eligible for optical promotion, and 64 lifetime uses per promoted relation.

Per promoted optical event after amortizing 1 pJ/64 is ~26.58 fJ versus 37.55 fJ electrical.

Result versus the improved all-electrical hierarchy:
- image: ~0.12% total-energy improvement;
- sound: ~0.17%;
- code: **~14.0%**;
- reasoning: ~1.4%.

Why code benefits most: its local physical motif/dispatch core is already extremely small, so communication is a large fraction of total. Image and sound are still dominated by local computation; hollow optics helps their communication but barely changes whole-workload energy in this particular screen.

This corrects the earlier v13G comparison that used the old 0.68 pJ long-coordinate proxy: hollow optics still wins in the right regime, but the advantage is much smaller against the best dedicated electrical route.

## 6. Optical route volume
A demonstrated ~9 x 9 um single-mode glass-waveguide core occupies only ~0.00081 mm^3 over 10 mm. Even reserving a conservative 50 x 50 um lane uses ~0.025 mm^3 over 10 mm.

Therefore the selected optical path no longer reserves a large component-sized empty corridor. It behaves geometrically more like a wire/lightpipe through the hollow framework.

## 7. Large shared thermal artery / exhaust
A truly empty vacuum channel is a poor high-power heat conveyor: at modest chip temperature differences, radiation over 1 cm^2 is only tens of milliwatts. The useful interpretation is therefore **empty of components**, not empty of heat-transport physics.

Selected structure:

`hot chip/framework -> conductive spreader/wick -> hollow vapor/exhaust channel -> common top condenser/heat exchanger -> optional TEG -> outside/facility heat sink or useful heat loop`.

The closest real technology is a vapor chamber / heat pipe / microfluidic exhaust. Recent multi-chip vapor-chamber work has demonstrated high heat-flux transport, and 3D/microchannel research shows large reductions in hotspot temperature when coolant is brought near stacked hot regions.

## 8. Heat harvesting should be large-scale
Do not put a thermoelectric generator on every small Glyph cell. It adds area and thermal resistance for tiny recoverable power.

A 2025 rack-scale TEG + heat-pipe + PCM model reported:
- 25 kW server-rack heat;
- ~125 W electrical TEG output in one stage (~0.5% of heat);
- ~219 W in a dual-stage model (~0.876%);
- ~20.1 kW useful hot-water heating output.

Using those same ratios only as a scenario screen:
- 16 chips at 200 W each -> 3.2 kW heat -> ~16-28 W electrical recovery, ~2.57 kW useful heat;
- 64 chips -> 12.8 kW -> ~64-112 W electrical, ~10.29 kW useful heat;
- 128 chips -> 25.6 kW -> ~128-224 W electrical, ~20.58 kW useful heat.

These are scaled external-study models, not GVS measurements. They support the user's idea of one large harvester above many chips, while also showing that **useful heat export is far larger than electrical thermoelectric recovery**.

## 9. Final architecture decision
### KEEP
- hollow structural framework;
- local electrical Tri-Wall/fourth-face/event-spine nervous fabric;
- skinny TIR/glass lightpipes for long, repeatedly validated routes;
- direct photocharge endpoint for future optical process;
- rare nonvolatile optical route write;
- component-free thermal exhaust paths;
- shared vapor/heat-pipe/microfluidic collection to a top/outside heat harvester;
- large-scale heat reuse/harvesting, not per-cell TEGs.

### REJECT / MODE ONLY
- large free-space optical corridors when a thin lightpipe can do the job;
- optics below the distance/reuse crossover;
- ordinary TIR in an empty air core;
- literal evacuated thermal channels as the only heat-transport mechanism;
- per-cell thermoelectric harvesting;
- claiming recovered heat as free energy.

## 10. Next physical/system work
1. build an 8-region electrical mixed block using the closed lease/Grammar/template/Myelin/tap-spine components;
2. assign actual route lengths from a 3D floorplan;
3. promote only routes that pass measured lifetime break-even;
4. model thin TIR lightpipe endpoint area, bends, crossings and source sharing;
5. build a thermal network where component-free vapor/exhaust arteries take heat to one top manifold;
6. include pump/fan/source/TEG overhead rather than counting recovered heat alone;
7. replay real image/sound/code/reasoning traces and compare all-electrical vs hollow heterogeneous on energy, latency, package volume, thermal headroom and fallback correctness.
