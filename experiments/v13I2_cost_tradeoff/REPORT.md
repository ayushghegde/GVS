# Neural Glyph v13I2 — Manufacturing Cost, Running Cost and Tradeoff Decision

**Verdict: choose Hollow-Electrical Base as the default architecture. Add the Optional Photonic Layer only for long/hot route-heavy products or regions that pass measured lifetime break-even.**

## 1. Manufacturing cost ranking

### Lowest current manufacturing burden: Hollow-Electrical Base (HEB)
HEB already requires nontrivial hollow/3D packaging, but its active computation and communication remain electrical/CMOS/MIM plus thermal infrastructure.

### Higher manufacturing burden: Hollow-Heterogeneous Extension (HHE)
HHE adds:
- photonic emitters/modulators/detectors;
- transparent TIR/lightpipe structures;
- optical alignment/registration;
- optical testing;
- source coupling/distribution;
- possibly nonvolatile MEMS/PCM route switches.

A 2024/2025 review of 3D photonic packaging reports that packaging, assembly and test are commonly estimated at ~70-80% of PIC manufacturing cost versus ~20% for electronic IC counterparts, and identifies active optical alignment as a major cost/throughput barrier.

This does not map directly to GVS dollars, but it makes the direction clear: **with current manufacturing, HHE is more expensive to build.**

## 2. Running-energy ranking

### Low reuse / local-dominated workload
HEB wins or ties. At 16 lifetime uses in the 8-region route model, no optical route is economic.

### Medium long-route reuse
At 64 uses/relation and 50% long/hot routes:
- HEB communication lifetime ~86.20 pJ;
- HHE expected ~66.94 pJ;
- HHE communication advantage ~22.34%.

### Very hot long-route fabric
At 256 uses and 50% hot routes, the communication advantage grows to ~34.52%.

### Whole mixed workload
At the 10 mm / 64-use / 50%-eligible screen using one preserved image, sound, code and reasoning operation each:
- HEB summed dynamic proxy ~541.22 pJ;
- HHE ~540.16 pJ;
- only ~0.196% reduction.

The tiny whole-mix change occurs because image/sound local compute dominates. Code, whose core is already very cheap, gains ~14% total energy.

## 3. Optical idle/source constraint

At 10 mm and 64 lifetime uses, HHE has only ~10.97 fJ/event of remaining advantage after route-write amortization.

At a 1 GHz promoted-event rate, shared optical idle overhead must therefore remain below roughly ~11 uW to preserve that particular win. Lower utilization makes the allowed idle power even smaller.

This means a continuously biased/tuned optical source can make HHE cost more to run even when per-event optical energy is attractive.

**Requirement:** source sharing + burst power gating or another low-idle source strategy is mandatory before HHE can be called lower-running-cost hardware in a real implementation.

## 4. Thermal cost

Both HEB and HHE may use the same large shared Thermal Exhaust Plenum and top harvester. Do not give HHE a special energy credit just because it produces heat.

Low-grade thermoelectric recovery is modest. Published studies include ~1.92% conversion at a 70 C temperature difference in one optimized modular heat-exchanger/TEG study and ~125 W from a modeled 25 kW data-center rack (~0.5%) in a heat-pipe/PCM/TEG system. Useful heat export can be much larger than electrical recovery.

Therefore:
- thermal exhaust can lower cooling operating cost for both architectures;
- heat reuse is useful at machine/rack scale;
- TEG electrical recovery is a secondary credit, not the reason to select HHE.

## 5. Volume / package trade

The TIR route itself can be small. In the 10 mm-cube model, 14 conservative 50 x 50 um optical lanes occupy only ~0.449 mm^3 (~0.045% of the 1000 mm^3 illustrative volume). All 28 lanes are still below ~0.1% route-lane volume.

The real area/cost is therefore more likely to come from endpoints, source distribution, switches, alignment structures and test than from the transparent line itself.

## 6. Reliability / repair trade

HEB:
- fewer physical technology classes;
- simpler electrical diagnosis;
- existing exact fallback;
- no optical alignment/source failure mode.

HHE:
- lower runtime cost on qualified long routes;
- more failure modes: source, coupler, detector, alignment, optical switch, contamination/thermal drift;
- must retain electrical fallback, so optics does not eliminate the electrical network.

The electrical fallback duplication weakens manufacturing savings from replacing wires with light.

## 7. Best product strategy

### Default / cheapest product
**HEB**.

### High-end route-heavy product
**HEB + Optional Photonic Layer**.

The base hollow framework should reserve narrow service/optical conduits and endpoint sites so the same mechanical concept can support both variants. Do not manufacture the expensive photonic subsystem for workloads that will not repay it.

This is the current lowest-risk way to honor both costs:
- one common electrical architecture;
- optional optical extension;
- same thermal exhaust and component bays;
- compiler decides whether installed optics is used.

## 8. Current direct answer

### Lower manufacturing cost today
**Hollow-Electrical Base.**

### Lower running cost for typical mixed/local workloads
**Hollow-Electrical Base or near tie.**

### Lower running cost for long, hot, repeatedly used multi-mm relations
**Hollow-Heterogeneous Extension, if the source-idle/alignment overhead remains below break-even.**

### Best overall architecture today
**HEB as the universal architecture + optional photonics as a package/region upgrade.**
