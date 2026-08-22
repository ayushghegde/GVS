# Neural Glyph v13G2 — Optical Dendrite / Long Fanout-Fan-in Screen

**Verdict: PROMISING FUTURE_PROCESS. The strongest optical use is not merely replacing one wire. A promoted hollow-cavity optical relation can deliver photons directly into a local charge-integrating receptor, allowing long-range fan-in/fanout while removing conventional receiver amplifiers and some routing stages. This is useful only for long sparse/hot relations and must use self-referenced/differential safeguards for analog evidence.**

## New terms

- **Optical Dendrite:** several promoted long-range optical sources deposit charge onto one local photodiode/receptor; the receptor sums charge physically and local competition decides the result.
- **Optical Fanout Tree:** one promoted modulated optical source is split/steered to several direct-photocharge receptors; photon energy scales with number of receivers but the modulator/router can be shared.
- **Differential Photocharge Pair:** signal and matched reference photocharge are compared locally so optical drift/coupling changes do not become a fixed absolute threshold error.

## 1. Long fanout model

Use the v13F 3 fF receptor at 0.2 V and 80% detector QE. Required detector-incident energy is ~0.600 fJ per receiver.

Moderate path/source assumptions:
- path efficiency 30%;
- laser wall-plug efficiency 15%;
- one published 5.9 fJ modulator action shared by the fanout event.

Then total optical source/modulator work is approximately:

`5.9 fJ + N * 13.33 fJ`

for N receivers.

At 10 mm, compare with the present ~3.74 fJ/mm electrical route proxy plus ~0.15 fJ endpoint per branch:

| fanout | optical moderate | N dedicated electrical 10 mm routes | modeled reduction |
|---:|---:|---:|---:|
| 1 | ~19.23 fJ | ~37.53 fJ | ~48.8% |
| 2 | ~32.56 fJ | ~75.06 fJ | ~56.6% |
| 4 | ~59.23 fJ | ~150.11 fJ | ~60.5% |
| 8 | ~112.55 fJ | ~300.22 fJ | ~62.5% |
| 16 | ~219.21 fJ | ~600.44 fJ | ~63.5% |

This ignores splitter/switch loss, additional apertures, detector reset, dark current and alignment. It is a compiler screen, not a photonic measurement.

### Consequence
Optical fanout is not free because photon energy scales with receiver count, but **endpoint sharing can still make it more attractive than N long material wires**.

## 2. Optical Dendrite: direct long-range fan-in

For analog/context use, one distant source need not create a full 0.2 V robust event. It can deposit a smaller charge increment into a local membrane/receptor.

For the ideal 3 fF receptor:
- one 20 mV contribution needs ~0.060 fJ incident optical energy at 80% QE;
- simple kT/C noise is ~1.18 mV RMS.

With the same moderate path/source assumptions, one source costs roughly:

`5.9 fJ modulator + 0.060/(0.30*0.15) = ~7.23 fJ`

Four promoted sources depositing 20 mV each:
- nominal summed local state: ~80 mV;
- simple signal/kT/C ratio: ~68;
- optical source/modulator work: ~28.93 fJ;
- four dedicated 10 mm electrical routes: ~150.11 fJ first-order;
- four old long-coordinate events: ~2720 fJ proxy.

This is potentially powerful because the destination performs **communication + summation** in one physical state.

## 3. Why this is not a normal optical neural network

GVS should not send every synapse through photonics. The Optical Dendrite is only for sparse long relations that have earned promotion.

Normal local weights remain capacitive/electrical because they are much cheaper.

The optical route is valuable when it removes:
- long electrical wire capacitance;
- repeated coordinate routing;
- receiver amplifier/full-swing reconstruction;
- separate digital fan-in bookkeeping.

## 4. Identity limitation

One shared photodiode sums charge but does not preserve which source contributed after the fact.

That is acceptable only when the promoted relation semantically represents pooled evidence, exactly like a dendrite.

If source identity is required, use:
- separate receptors;
- time slots;
- wavelength/spatial channels;
- or exact/electrical routing.

Do not force identity-sensitive code/pointers through a pooled optical dendrite.

## 5. Absolute optical amplitude is unsafe

Laser power, alignment, contamination, detector responsivity and thermal drift can all change received charge.

Reuse the v13A5 lesson: **do not sign off analog optical evidence against one absolute voltage threshold.**

Future analog optical cell should use one of:

### Differential Photocharge Pair
`signal detector/receptor versus matched reference detector/receptor`

### Two-phase optical self-check
Replay the promoted local optical evidence with swapped physical comparator sides when margin is low.

### Local pulse-count reference
Use a known reference pulse on the same source/path family to estimate current transfer gain before trusting weak analog optical weight.

High-margin robust 0.2 V optical events need less of this complexity; weak analog Optical Dendrite mode requires it.

## 6. Weighting

Do not begin with precision optical analog weights.

Selected first representation:
- no chord = 0;
- one calibrated pulse/contribution = +1;
- optional paired inhibitory/reference contribution = -1 or context suppression;
- exact residual handles exceptions.

This mirrors v12K ternary physical synapses and avoids making optical attenuation precision the new weak point.

Future attenuation/phase-change weights are allowed only if measured stability beats pulse-count/coarse structural weighting.

## 7. Route configuration

A long optical dendrite connection should be configured rarely:

`validated electrical repetition -> familiarity -> Use/Lease -> exact/conservative validation -> optical route consolidation`

Nonvolatile MEMS/PCM optical switching is attractive because the route can hold with zero static power while runtime photons pass.

No raw/noisy event may permanently create an optical synapse.

## 8. Failure and fallback

If photocharge margin falls below the locally characterized safe region:
- do not guess;
- mark optical route uncertain;
- fall back to electrical/exact path;
- use repeated successful recalibration before re-promotion.

Thermal Brake state may also lower optical-route confidence when source/switch temperature becomes high.

## 9. Decision

### KEEP for future photonic process
- direct-photocharge long fanout;
- Optical Dendrite long fan-in;
- coarse pulse/ternary optical weights;
- differential/reference optical evidence;
- nonvolatile optical route consolidation.

### REJECT as normal mode
- optics for every synapse;
- precision absolute optical weights without reference;
- pooled optical receptor when source identity is required;
- assuming beam splitting is energy-free.

## 10. Next

The next physical/system experiment should integrate this with the heterogeneous void layout:
- one regional optical source bank;
- two or four promoted long optical relations;
- one direct-photocharge fanout group;
- one Optical Dendrite fan-in receptor;
- electrical service walls and fallback routes;
- Thermal Artery near the source/switch block;
- compare against all-electrical long routes on energy, area/aperture, thermal load and failure recovery.
