# Neural Glyph v13F0 — Hollow Photonic Void Screen

**Verdict: MODE-DEPENDENT KEEP. Light is rejected as a replacement for the present local fourth-face and electrical event-spine links, but the hollow/framework interior creates a credible new use: sparse pre-aligned optical chords for long robust events/bursts across otherwise empty 3D volume. A direct photocharge receptor is the most GVS-like optical receiver candidate and is kept for future photonic-process testing.**

## New terms

- **Optical Void Chord (OVC):** a pre-aligned line-of-sight optical path across the hollow/framework cavity that carries robust events or bursts between distant surfaces without a material wire along the entire route.
- **Photocharge Receptor:** a photodiode that charges a local receptor/membrane directly, avoiding a conventional transimpedance/receiver amplifier when the required signal margin is small enough.
- **Optical Corridor:** reserved clear cavity volume between optical endpoints; components may occupy the rest of the cavity but must not block or scatter a promoted line-of-sight route.

## 1. First correction: light is not useful merely because it travels fast

An electrical signal in a conductor is also an electromagnetic disturbance; the useful advantage of optics is not a magical orders-of-magnitude propagation-speed gain over a short wire. In free space, light takes about 3.34 ps/mm, so even a 20 mm cavity crossing is only ~66.7 ps. Electrical interconnect may have additional RC/repeater delay, but local GVS wires are already extremely short.

The more important potential optical advantages are:

- no conductor capacitance along a free-space chord;
- many beams may cross geometrically without becoming electrically shorted nodes;
- a diagonal A-to-E path can use the cavity directly instead of following wall routing;
- very high aggregate bandwidth is possible;
- distance-dependent electrical wire/repeater cost can be replaced by endpoint conversion cost.

The endpoint conversion cost is the main problem.

## 2. Current published photonic baseline versus GVS electrical links

A 2025 Nature Photonics 3D-integrated transceiver demonstrated 50 fJ/bit transmitter-front-end energy and 70 fJ/bit receiver-front-end energy, or ~120 fJ/bit combined front ends at 10 Gb/s/channel. The same work discusses possible laser energy around 30 fJ/bit for a scalable comb source and a best-case silicon-resonator thermal-tuning contribution around 176 fJ/bit in one scenario.

Screening sums:

- measured TX+RX front ends: ~120 fJ/bit;
- front ends + 30 fJ/bit laser estimate: ~150 fJ/bit;
- front ends + laser + 176 fJ/bit tuning scenario: ~326 fJ/bit.

Compare with current GVS electrical event-source proxies:

- direct fourth-face true neighbor: ~0.15 fJ;
- protected ~180 um event spine, one tap: ~0.67 fJ;
- same spine, four taps: ~1.34 fJ;
- old long-coordinate communication proxy: ~680 fJ/event.

Therefore conventional optics is **rejected locally**: even the 120 fJ front-end number is ~90x the four-tap regional spine and ~800x the direct neighbor source-work proxy.

At the long-route scale, the comparison changes. A ~150–326 fJ/bit research photonic link is numerically below the ~680 fJ GVS long-coordinate event proxy, but these are not identical interfaces or signoff conditions. This only justifies a crossover experiment, not replacing the long electrical fabric.

Critical architectural consequence: an optical route should be **pre-established/promoted**. If every event must transmit a multi-bit destination address, optical endpoint energy multiplies by the address width and can lose the advantage. A stable Optical Void Chord carries a one-bit-like `event on this already-known relation` or an amortized burst.

## 3. Hollow-cavity propagation / aperture screen

For a 1550 nm Gaussian beam, requiring Rayleigh range approximately equal to the path length gives the rough waist relationship `w0 = sqrt(lambda*L/pi)`.

| distance | free-space flight time | ~2*w0 optical diameter |
|---:|---:|---:|
| 0.1 mm | 0.334 ps | 14.0 um |
| 0.5 mm | 1.67 ps | 31.4 um |
| 1 mm | 3.34 ps | 44.4 um |
| 5 mm | 16.7 ps | 99.3 um |
| 10 mm | 33.4 ps | 140.5 um |
| 20 mm | 66.7 ps | 198.7 um |

This is a simple diffraction screen, not an optical design. It shows a key scale result: free-space optical chords are plausible at package/mm scale but consume tens-to-hundreds of micrometers of aperture/corridor unless lenses, metasurfaces or diffraction-free beam techniques improve confinement.

A 2024 Journal of Lightwave Technology demonstration supports the general route idea: diffraction-free on-chip wireless optical beams achieved millimeter-scale transmission, >20 dB reconfigurable switching extinction and a 3.2 Tb/s aggregate proof-of-concept rate per beam. This does not give GVS an energy number, but it demonstrates that intersecting/reconfigurable beam routes are physically credible.

## 4. 3D material waveguide option

The cavity does not have to be completely empty. A fixed optical route could use a free-standing 3D waveguide.

A 2024 Scientific Reports experiment demonstrated unsupported polymer 3D waveguides up to 900 um, including non-connected 3D crossings. Measured propagation loss was ~1.93 dB/mm at 635 nm and ~3.71 dB/mm at 830 nm.

Using those measured losses directly:

- 635 nm, 1 mm: ~64% optical power remains;
- 635 nm, 5 mm: ~10.8%;
- 635 nm, 20 mm: ~0.014%;
- 830 nm, 5 mm: ~1.4%.

**Decision:** this demonstrated polymer-waveguide technology is attractive for short fixed 3D connections/crossings, but rejected as the default multi-millimeter hollow-cavity link at those measured losses. Better C-band waveguides/processes could change the conclusion later.

## 5. Direct photocharge receiver model

The published 2025 3D receiver uses a ~17 fF photodiode plus ~10 fF pad capacitance and an electronic receiver amplifier. GVS has a different opportunity: the destination already understands charge.

Instead of:

`photodiode -> amplifier -> digital/full-swing -> analog cell`

try:

`photodiode -> local Contact Receptor / capacitor wall -> local competition`

This is **Photocharge Receptor** mode.

At 1550 nm, one photon has ~0.128 aJ of energy. The ideal photon count required merely to put charge `Q=C*dV` onto a node is small:

### Ideal 3 fF receptor

- 20 mV: ~374 electrons; ~0.048 fJ received optical energy at 100% quantum efficiency, ~0.060 fJ at 80%;
- 200 mV: ~3,745 electrons; ~0.480 fJ at 100%, ~0.600 fJ at 80%.

### Published 17 fF photodiode capacitance

- 20 mV: ~2,122 electrons; ~0.340 fJ at 80% quantum efficiency;
- 200 mV: ~21,221 electrons; ~3.40 fJ at 80%.

### 17 fF diode + 10 fF pad = 27 fF

- 200 mV: ideal received optical energy ~5.40 fJ at 80% quantum efficiency.

These numbers are an ideal charge/photon model only. They exclude source wall-plug efficiency, modulator/coupler loss, detector dark current, reset, alignment, scattering and routing loss.

## 6. Noise screen for direct photocharge

For a 3 fF receptor at 300 K, `sqrt(kT/C)` is ~1.18 mV RMS. A 20 mV photocharge state is therefore ~17x this simple thermal-noise amplitude. The ~374-electron shot-count scale has `sqrt(N)` ~19.4.

This suggests a 20 mV direct photocharge state is not obviously impossible on first-principles noise grounds, but a real detector introduces additional noise and capacitance. The correct next step is not to claim a sub-fJ optical receiver; it is to test an actual small photodiode/process model and determine the minimum robust charge margin.

## 7. Optical modulator is not necessarily the dominant cost

A 2025 Nature Communications silicon photonic-crystal modulator demonstrated 110 GHz electro-optic bandwidth, a 10 um^2 footprint and ~5.9 fJ/bit device power. This shows the modulator itself can be single-digit fJ/bit. However, a complete GVS optical link still needs light generation, routing/coupling and detection; the full link cannot be priced at 5.9 fJ/bit.

This strengthens the Photocharge Receptor direction: if GVS can remove the conventional receiver amplifier because the destination is already an analog charge-processing cell, endpoint cost may fall substantially.

## 8. The hollow volume becomes a routing resource, not merely empty space

Selected conceptual organization:

```text
active/framework wall                    active/framework wall
[local cell] [emitter/modulator]         [photodiode/receptor] [local cell]
        \                                       /
         \----------- Optical Void Chord ------/

          clear optical corridor through cavity

other cavity volume may still contain:
  memory / electrical service walls / power / cooling / exact logic /
  other non-blocking optical chords / sparse 3D waveguides
```

The framework/service walls still carry power, configuration, recovery and local electrical traffic. Light does not replace them.

The placement/compiler must reserve optical corridors. A random component placed in the cavity can physically block a line-of-sight chord.

## 9. Decentralized optical interpretation

Optics should follow the same GVS promotion policy as electrical Myelin:

1. new/cold relation uses existing exact/electrical routing;
2. repeated validated use creates electrical familiarity;
3. if distance/fanout/bandwidth makes optics cheaper, the relation may be promoted to a static/pre-aligned optical chord or optical switch state;
4. runtime sends only the robust event/burst through the chord;
5. inactivity or semantic invalidation removes/demotes the route;
6. exact fallback remains independent.

Do not use a central optical router for every local event if a static relation can configure itself slowly.

## 10. Fanout and crossings

Optical beams can geometrically cross without becoming the same electrical node, which is valuable in the hollow volume. But optical fanout is not free: splitting one beam reduces photon power per receiver, and coherent/scattered light can still create crosstalk. Wavelength/spatial multiplexing may provide large bandwidth but adds filters, sources and tuning.

Therefore the first optical target is **one-to-one hot chords and bursts**, not unlimited optical broadcast.

## 11. v13F decision

### KEEP / test further

- hollow cavity as an optical routing volume;
- sparse Optical Void Chords for long, stable, robust event/burst relations;
- reserved optical corridors and diagonal A-to-E paths;
- direct Photocharge Receptor as a future photonic-process receiver;
- short 3D waveguides when line-of-sight is blocked and measured loss is acceptable;
- electrical walls for power/config/recovery/local routing.

### REJECT as current default

- optics for nearest-neighbor/local fourth-face traffic;
- optics for the current ~180 um event spine;
- carrying weak analog Grammar voltages optically across the whole system;
- long multi-mm routes using the demonstrated 1.93–3.71 dB/mm polymer waveguide as if the loss were negligible;
- assuming light is automatically better solely because `c` is high;
- optical broadcast without paying photon splitting, source and receiver costs.

### FUTURE_PROCESS

Current SKY130 does not contain the photonic devices needed for a physical optical signoff. v13F is therefore a model + literature-backed architecture screen, not a fabricated/PEX optical result.

## 12. Next experiment

Build the first **electrical/optical crossover compiler** for the hollow framework. For each promoted relation it should compare:

- direct fourth face;
- electrical event spine;
- electrical Myelin chord;
- conventional photonic chord using measured full-link energy;
- direct-photocharge optical chord using conservative detector/coupling efficiency assumptions;
- distance, fanout, burst length, aperture/corridor area, and alignment/tuning overhead.

Then reserve optical corridors only for relations whose measured/modelled lifetime traffic repays the optical endpoints and occupied cavity aperture.

## References used for the external screen

- S. Daudlin et al., *Three-dimensional photonic integration for ultra-low-energy, high-bandwidth interchip data links*, Nature Photonics (2025).
- *Ultracompact and large-bandwidth silicon modulator in a CMOS-compatible foundry*, Nature Communications (2025).
- *On-Chip 3.2 Tb/s Wireless Optical Interconnects Using Diffraction-Free Beam and Microcomb*, Journal of Lightwave Technology (2024).
- A. Andrishak et al., *Free-standing millimeter-range 3D waveguides for on-chip optical interconnects*, Scientific Reports (2024).
