# Neural Glyph v13F1 — Optical/Electrical Crossover Compiler Screen

**Verdict: KEEP a direct-photocharge optical mode only for long hot relations; conventional photonics remains too expensive for local GVS. The hollow cavity matters because it creates millimeter-scale line-of-sight routes where endpoint-dominated optics can eventually beat distance-dependent electrical routing.**

## Terms
- **Direct-photocharge chord:** modulated light is received directly as charge on a small local receptor; no conventional receiver amplifier is assumed in the model.
- **Crossover distance:** first-order distance at which the modeled incremental optical endpoint energy equals a linear electrical-wire energy proxy.
- **Optical consolidation:** rare promotion of a repeatedly validated relation into a static/nonvolatile optical route, analogous to Myelin promotion.

## 1. Electrical distance proxy

Two existing GVS measurements/models give similar local robust-event wire slopes:
- v13E protected event spine: ~0.6728 fJ over 0.18 mm for one tap -> ~3.74 fJ/mm first-order;
- measured M4 capacitance proxy: ~76.106 fF/mm at 0.2 V -> `C*V^2` ~3.04 fJ/mm.

These are local-wire proxies, not the old ~680 fJ coordinate/fabric event. The distinction matters: a dedicated wire is much cheaper than the full global selection machinery.

## 2. Direct-photocharge optical endpoint model

Use the v13F0 3 fF receptor, 0.2 V event and 80% detector quantum efficiency. Ideal incident detector energy is ~0.600 fJ.

Add the published 2025 ~5.9 fJ/bit silicon photonic modulator, then screen three source/path cases:

| case | path efficiency | laser wall-plug efficiency | modeled total incremental energy | crossover vs v13E event-spine slope |
|---|---:|---:|---:|---:|
| good | 70% | 30% | ~8.76 fJ | ~2.34 mm |
| moderate | 30% | 15% | ~19.23 fJ | ~5.15 mm |
| poor | 10% | 10% | ~65.89 fJ | ~17.63 mm |

This excludes reset, alignment control, tuning, source-sharing overhead, photodiode dark current, and a real optical switch. It is therefore a **scenario model**, not an optical signoff.

### Consequence
Conventional ~120–150 fJ photonic front ends do not beat a simple dedicated electrical wire at normal chip distances. A GVS-specific direct-photocharge receiver could create a crossover in the few-to-tens-of-mm range if the source/path efficiencies are good enough.

That is the hollow/package scale, not the nearest-neighbor cell scale.

## 3. Old long-coordinate fabric changes the comparison

The old long-coordinate communication proxy is ~680 fJ/event. A 150 fJ conventional photonic event is already numerically below that proxy, while a future direct-photocharge route could be much lower.

Therefore the compiler must compare **actual route classes**, not `light versus wire` in the abstract:

1. direct fourth face;
2. segmented local electrical tap;
3. regional electrical event spine;
4. dedicated electrical/Myelin chord;
5. long coordinate/global fabric;
6. optical chord.

Optics should only be promoted when it beats the cheapest physically available electrical route.

## 4. Nonvolatile optical route promotion matches old v12E familiarity

A 2025 nonvolatile silicon-photonic MEMS switch demonstrated zero-static-power retention and ~1 pJ theoretical switching energy. Treat 1 pJ only as a route-programming screening value.

If one long relation would otherwise cost ~680 fJ/event:
- 150 fJ optical event saves ~530 fJ/event -> ~1.9 events to amortize a 1 pJ switch write;
- 326 fJ conservative optical screen saves ~354 fJ/event -> ~2.8 events;
- 20–66 fJ direct-photocharge scenarios would amortize in ~1.5–1.6 events.

This is strikingly compatible with preserved v12E familiarity: the third closely repeated validated use produced ~28 mV familiarity. Therefore **three validated uses is a plausible earliest optical-promotion probation point**, not because three is magical, but because both the old physical familiarity margin and the first-order optical reconfiguration payback occur on the same small-reuse timescale.

A real compiler must still include route lifetime, aperture cost, switch endurance, alignment, and exact validation.

## 5. Analog optical evidence should be differential/ratio-based if attempted

Absolute optical amplitude is vulnerable to laser drift, coupling loss, dust/alignment, detector responsivity and path loss. Reusing the v13A5 lesson, a future weak-optical analog mode should not use a fixed absolute photo-voltage threshold.

Candidate future mechanism:

`candidate optical charge versus matched reference optical charge -> local ratio/differential decision`

This is only a design rule for a later photonic process. The normal optical chord remains a robust event/burst path.

## 6. Decision

### KEEP
- direct-photocharge optical chord as a future-process long-route candidate;
- conventional photonics for long high-bandwidth bursts when its full endpoint cost beats electrical global routing;
- v12E familiarity as one input to rare optical consolidation;
- nonvolatile optical switch state as a future static route memory.

### REJECT as default
- optics for direct fourth-face neighbors;
- optics for the ~180 um regional event spine;
- assuming a conventional 120–150 fJ transceiver beats a simple few-mm dedicated electrical wire;
- absolute analog optical thresholds.

## 7. Next

The next void experiment must screen all other physical carriers and then zone the hollow volume so optical corridors, cooling, service walls and internal modules do not conflict.
