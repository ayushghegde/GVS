# Neural Glyph v13G1 — Heterogeneous Void Fabric / Volume-Zoning Architecture

**Verdict: KEEP. The hollow volume should not be maximally filled and should not be maximally empty. It should be zoned by function. Electrical walls serve local computation/power/control, intentionally empty optical corridors serve long hot links, Thermal Arteries cool hot modules, and component bays host memory/exact/support hardware. A physical-cost compiler chooses which resource each relation occupies.**

## 1. Why one uniform interior fails

Three previously tested extremes are all wrong as a universal architecture:

1. **empty only** — wastes volume that can hold memory, power, cooling or exact logic;
2. **filled conductor/network** — couples states and destroys selectivity;
3. **filled with components/wires everywhere** — blocks optical diagonals, increases heat density and leaves no reserved low-capacitance long-range path.

Therefore the interior is treated like a building/service volume: some space contains equipment, some carries utilities, some must remain clear for transport.

## 2. Functional zones

### A. Active framework / wall zone
- Tri-Wall capacitors;
- local transistors and receptors;
- direct fourth-face neighbor links;
- shielded Service Spine wires;
- power/reference/recovery/configuration.

### B. Optical Corridor
Intentionally clear line-of-sight volume reserved for promoted Optical Void Chords. Do not place memory, coolant pipes or support ribs across a committed corridor unless the route is first demoted/re-routed.

### C. Thermal Artery
Dedicated microfluidic/thermal route near hot exact compute, dense memory, optical sources or power conversion. It is electrically isolated and does not share the same open volume as precision free-space optics by default.

### D. Component Bay
Interior mounting volume for package-scale memory, exact-compute chiplets, local controllers, recovery capacitors, sensor interfaces or other useful hardware. Components attach to the framework/service infrastructure rather than floating as unserviceable islands.

### E. Structural / alignment rib
Mechanical support and optical alignment reference. These ribs may also carry shielded robust services, but weak analog state remains on protected cell surfaces.

### F. Reserve / bypass corridor
Some routing/volume remains uncommitted so a failed or invalidated long path can be bypassed without redesigning the whole package.

## 3. Distance-dependent carrier compiler

Use the current v13E event-spine slope (~3.74 fJ/mm first-order) plus ~0.15 fJ endpoint term only as a route-length proxy. Compare with v13F direct-photocharge scenarios:

- good optical ~8.76 fJ/event;
- moderate ~19.23 fJ/event;
- poor ~65.89 fJ/event.

First-order crossover in the generated distance table:
- good optical becomes lower-energy than the electrical proxy at about **2.5 mm**;
- moderate optical at about **5.5 mm**;
- poor optical only around **18 mm**.

This is a model, not a process signoff. It shows why the compiler needs measured endpoint/path quality: the same 10 mm relation can be clearly optical under a moderate link and clearly electrical if the optical path is very poor.

Conventional ~150 fJ photonics still does not beat this simple dedicated electrical-wire proxy inside a normal ~20 mm package; it only becomes attractive when it replaces a much more expensive global routing/fabric function or carries a high-bandwidth burst.

## 4. Optical source placement

Do not put a laser in every tiny cell.

Selected future structure is **regional source sharing**:
- one/few optical sources serve a local group or package region;
- small local modulators select promoted chords;
- endpoints remain local photodiode/receptor structures;
- a source failure affects a region, not the whole architecture;
- long idle periods may power down the regional source unless startup/tuning cost makes that worse.

This mirrors old successful GVS sharing: share expensive support, keep local decisions isolated.

## 5. Optical switching / route consolidation

For a route that changes rarely, a zero-static nonvolatile optical switch is more compatible with GVS than a continuously powered optical router.

Candidate future sequence:

`v12E familiarity -> Use/Lease state -> exact/conservative validation -> nonvolatile photonic switch/MEMS/PCM write -> many runtime optical events`

The route write is slow/expensive relative to an event, but its cost is amortized over reuse. Runtime does not need a central destination lookup.

## 6. Cooling and optics must be co-designed

The hollow package can improve cooling because coolant may approach internal hot surfaces, but photonics is temperature/alignment sensitive.

Rules:
- place optical sources/switches close to Thermal Arteries;
- keep weak analog Grammar/receptor nodes away from strong temperature gradients;
- keep moving liquid, bubbles and high-vibration pump structures out of free-space optical corridors unless a future experiment explicitly proves optical stability through the fluid;
- use the existing Thermal Brake to reduce promotion/activity when a region becomes hot;
- prefer nonvolatile photonic routing when it avoids continuous thermal tuning.

## 7. Internal memory/exact modules

The cavity should host exact hardware only where it reduces communication enough to repay its area/thermal cost.

Good candidates:
- local memory for region-specific residuals/exceptions;
- exact arithmetic/code engine near regions that frequently escalate;
- shared recovery/storage support;
- I/O/sensor conversion.

Bad default:
- placing a large hot controller in the center merely because space exists;
- routing every local event through that controller.

## 8. Decentralized self-healing

The reserve volume enables a physical fault policy that reuses old GVS learning mechanisms:

`route success -> familiarity/lease maintained`

`repeated failure/timeout -> route state decays or is invalidated`

`alternative electrical/optical path succeeds -> its familiarity rises`

`stable replacement -> promoted`

The exact fallback verifies correctness during transition but does not schedule every event. A failed optical chord can fall back to electrical routing; a failed electrical wall lane may use a redundant spine or long optical chord if physically available.

## 9. Current carrier hierarchy inside the framework

1. direct fourth face — adjacent weak analog/event;
2. short segmented electrical tap — nearby non-neighbor;
3. shielded regional event spine — regional fanout;
4. dedicated electrical/Myelin chord — stable short/medium route when wire is still cheapest;
5. Optical Void Chord — stable long/hot relation when endpoint/path cost beats wire/global fabric;
6. contactless capacitive/inductive link — only across tiny assembly gaps where a physical bond is undesirable;
7. RF/mmWave — rare broadcast/discovery/backup where wired/optical routes are physically impractical;
8. exact/global fabric — cold/changing/ambiguous relation.

## 10. Architectural consequence

The compiler no longer assigns only `representation` and `route`. It must also assign **volume**:

`relation/workload -> physical representation -> carrier -> wall/corridor/bay allocation -> thermal budget -> fallback path`

A promoted route is accepted only if its lifetime energy + occupied volume + cooling/alignment overhead beats the alternatives.

## 11. Next

Test two newly promising consequences:
1. direct-photocharge **long fanout/fan-in**, because removing eight conventional receiver amplifiers may change the economics of optical broadcast;
2. differential/ratio optical evidence, reusing the v13A5 lesson so analog optical signals are not judged by an absolute light level.
