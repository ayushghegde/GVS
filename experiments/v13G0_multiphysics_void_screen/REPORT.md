# Neural Glyph v13G0 — Multi-Physics Hollow-Volume Screen

**Verdict: do not choose one universal carrier. Keep electricity for local computation, optics for promoted long/hot cavity chords, heat/fluidics for slow thermal control and cooling, mechanical/nonvolatile photonic switching for rare route configuration, and magnetic state only as a future persistent anchor. Capacitive/inductive/RF/acoustic carriers remain mode-dependent tools rather than the default nervous fabric.**

## New terms

- **Heterogeneous Void Fabric (HVF):** the hollow/framework interior is divided into functional volumes: optical corridors, cooling channels, internal component bays, structural ribs and service-wall infrastructure; the cavity is neither kept completely empty nor filled uniformly.
- **Thermal Artery:** a dedicated coolant/heat-removal channel placed near active framework walls or hot internal modules.
- **Consolidation switch:** a slowly reconfigured, near-zero-static-power device that remembers a promoted route while runtime events pass without paying reconfiguration energy.

## 1. Electrical remains the default local physics

Current GVS references:
- direct fourth-face neighbor ~0.15 fJ/event source-work proxy;
- protected ~180 um event spine ~0.67 fJ one tap / ~1.34 fJ four taps;
- v13E promoted event tap selected at 0.9 V after 12/12 TT/FF/SS mismatch closure.

No external communication technology screened here beats these local links. Therefore do not replace the electrical nervous fabric around a local intelligent region.

## 2. Contactless capacitive coupling

Older fabricated 3D capacitive interconnects demonstrated roughly 41 fJ/bit synchronous and 80 fJ/bit asynchronous operation with face-to-face electrodes. Literature describes the practical range as only a few micrometers.

### Use
- adjacent face-to-face tiers/modules where eliminating a galvanic bond/TSV materially helps assembly or yield;
- possible future removable/replaceable module interface.

### Do not use
- ordinary neighboring Glyph cells: the present direct fourth face is orders of magnitude cheaper;
- multi-mm hollow-volume routing.

**Decision: MODE_ONLY.**

## 3. Inductive near-field coupling

A fabricated 90 nm inductive inter-chip link reported ~65 fJ/bit with charge recycling; literature places practical contactless vertical ranges around tens of micrometers.

### Use
- vertical non-contact tier/module interface;
- possible clock/power/data bridge where bonding is undesirable.

### Problem
Large coils/receiver circuitry and magnetic crosstalk make it poor compared with direct electrical local GVS.

**Decision: MODE_ONLY.**

## 4. mmWave / RF cavity wireless

Published mmWave chip/inter-chip work is typically hundreds of fJ/bit to pJ/bit for complete transmitter/receiver classes; antennas and RF front ends consume meaningful area and power.

### Useful property
One transmitter can cover a region without an individual wire to every endpoint.

### GVS role
- rare global/regional broadcast, clock, discovery or emergency control if wiring/optical line-of-sight is physically blocked;
- not local reasoning/evidence traffic.

**Decision: MODE_ONLY / backup broadcast, not default.**

## 5. Optics

v13F showed two separate regimes:

### Conventional photonics
~120 fJ/bit published TX+RX front ends, ~150 fJ/bit when an optimistic ~30 fJ/bit laser screen is added. Too expensive locally, potentially competitive against the old ~680 fJ long-coordinate fabric.

### Direct-photocharge GVS optical chord
A 3 fF receptor at 0.2 V requires only ~0.600 fJ incident optical energy at 80% detector QE in the ideal photon/charge model. Combining this with a published 5.9 fJ/bit modulator produces scenario totals of roughly:
- good source/path: ~8.8 fJ;
- moderate: ~19.2 fJ;
- poor: ~65.9 fJ.

Against the present ~3.0-3.7 fJ/mm local robust-event wire slope proxies, these correspond to first-order crossovers of roughly **2-18 mm**.

This is exactly the hollow/package distance class.

**Decision: KEEP as FUTURE_PROCESS long-hot route.**

## 6. Mechanical / MEMS as route configuration, not data carrier

A 2025 nonvolatile silicon-photonic MEMS switch demonstrated ~0.23 dB excess loss, high extinction, zero static retention and ~1 pJ theoretical switching energy, including a 16x16 array.

That is too expensive to toggle per event but attractive for GVS promotion:

`electrical familiarity -> validation -> rare mechanical/photonic route write -> many fast optical events -> zero static route-hold power`

The first-order ~1 pJ write payback versus a ~680 fJ electrical global event is only a few reused events, consistent with v12E's third-use familiarity becoming strong.

**Decision: PROMISING FUTURE_PROCESS consolidation mechanism.**

Phase-change optical routers with zero static hold power are another future consolidation option, but write endurance/heat/process cost must be measured before selection.

## 7. Acoustic / phononic

A longitudinal acoustic wave in silicon is roughly kilometers per second, not hundreds of millions of meters per second. First-order delay:
- 0.1 mm ~11.9 ns;
- 1 mm ~118.6 ns;
- 10 mm ~1.19 us.

This is far slower than optical flight and ordinary electrical local events. Programmable GHz phononic circuits are becoming credible for filtering/synthesis, but that does not make sound the right general interconnect.

### Possible GVS use
- frequency-selective preprocessing;
- delay/resonance/time features;
- sensor front ends.

### Rejected use
- normal reasoning/routing across the hollow cavity.

**Decision: REJECT_NORMAL_ROUTING; MODE_ONLY signal processing.**

## 8. Heat

First-order thermal diffusion in silicon using a typical diffusivity is slow:
- 0.1 mm ~0.11 ms;
- 1 mm ~11 ms;
- 10 mm ~1.1 s.

So heat remains unsuitable for exact fast route identity.

But the hollow framework makes heat more useful structurally:
- inner surfaces shorten heat-removal paths;
- cooling channels can sit close to buried/hot modules;
- temperature-sensitive replica devices can implement the existing Thermal Brake automatically.

Recent 3D/chiplet studies continue to show embedded microchannels can reduce thermal resistance and cool high heat fluxes when placed near hot regions.

**Decision: KEEP for environment control + cooling, not information routing.**

## 9. Microfluidics / hollow-volume cooling

The cavity can carry coolant instead of treating all empty space as wasted air. This is not a logic carrier; it is infrastructure.

Selected rule:
- put **Thermal Arteries** close to hot exact-compute/memory/power blocks;
- keep weak analog cells away from large temperature gradients where possible;
- do not share one open optical corridor with turbulent coolant by default because refractive-index motion, bubbles/contamination and mechanical vibration can disturb alignment.

Therefore optical corridors and coolant channels are separate functional zones unless a future transparent-fluid optical experiment proves coexistence.

**Decision: KEEP.**

## 10. Magnetism

Magnetic/nonvolatile state is attractive for verified long-lived configuration but the current SKY130 flow has no MRAM device. It should not carry every runtime event.

**Decision: FUTURE_PROCESS persistent anchor only.**

## 11. Power transfer through the cavity

Wireless optical/inductive/capacitive power is possible, but GVS already has protected shared service walls where galvanic VDD/GND distribution is cheaper and more controllable.

Use wireless power only for physically isolated/removable modules where eliminating contacts solves a real packaging problem.

**Decision: REJECT as default power distribution.**

## 12. Selected physics hierarchy

```text
nearest/local computation       -> electricity/charge
neighbor communication          -> fourth face
regional fanout                 -> shielded electrical event spine
short contactless tier gap      -> capacitive or inductive only if packaging needs it
long hot line-of-sight relation -> Optical Void Chord
rare optical route change       -> nonvolatile MEMS/PCM consolidation switch
local frequency/delay function  -> optional phononic block
thermal health                  -> replica leak / Thermal Brake
cooling                         -> Thermal Artery / microfluidics
persistent verified state       -> CMOS now, magnetic future
exact/ambiguous semantics       -> exact computer
```

## 13. Main problem discovered

The hollow volume cannot be optimized by `fill as much as possible`. Components, coolant and optics compete for geometry:
- a component can block an optical chord;
- a coolant channel can create optical instability;
- a hot exact block can disturb analog thresholds and photonic resonances;
- an optical aperture consumes wall surface that might otherwise hold capacitors;
- extra routing/support material adds capacitance and thermal coupling.

Therefore v13G must make **volume allocation itself part of the compiler/architecture**.

## 14. Next

Build the Heterogeneous Void Fabric zoning architecture and then compare one eight-region system with:
1. no cavity use;
2. cavity filled with modules/wires only;
3. zoned cavity with electrical walls + optical corridors + cooling + component bays.

The selected version must win on useful computation/communication per package volume, energy and thermal margin, not on geometric novelty.
