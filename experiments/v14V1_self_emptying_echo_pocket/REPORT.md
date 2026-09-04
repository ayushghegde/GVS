# Neural Glyph v14V1 — Self-Emptying Echo Pocket

**Status: MODEL PASS / PHYSICAL COUPON OPEN.**

## What happened

The v14V blocker was stated as a need for a passive programming barrier to become about 5000x more conductive after a branch fired, remain useful for about 100 ns, and forget by about 500 ns. v14V1 shows that 5000x is not a fundamental material requirement.

For the current ~8 aF 4-nm HZO collar and a 1.2 V / 30 ns TEACH pulse, the fresh series path only has to be below about 2.1 Gohm to put >=1.0 V on HZO. An untouched/stale branch has to remain above about 28 Gohm to keep HZO <=0.15 V. The mathematical fresh/stale separation is therefore only about 14x. Starting from a ~1 Tohm OFF path, about 500x fresh enhancement already has nominal margin; 1000x is the v14V1 variation target.

## New mechanism

**SEEP — Self-Emptying Echo Pocket:** a shallow nanoscale side pocket made as part of the existing guided-gap/ETG geometry. It is not a transistor and not a durable memory. When the guided gap wins, the same local ionic event pushes a small fraction of mobile Ag ions into the pocket. The pocket is positioned next to the orthogonal TEACH-program barrier but field-isolated from HZO by the FIC aperture/shield.

Those temporary ions lower the TEACH barrier electrostatically. Conductance rises exponentially with barrier lowering, so a modest ~0.2–0.25 eV fresh barrier shift is enough to produce >500–1000x useful conductance gain. When inference ends, the ions diffuse back to the common Ag reservoir. The address therefore erases itself.

This is different from adding a second volatile memory device: the tag is a geometric side state of the same mobile-ion branch that already fires.

## Why the numbers are physically worth testing

The model uses an effective ~6 mV barrier shift per captured ion after screening. A point elementary charge 1.5 nm away in a dielectric with er~12 would produce roughly 80 mV before screening, so the model retains only about 7.5% of that simple electrostatic scale. The selected winner population still has >100 captured ions in its lower tail; modeled losers do not cross the pocket-loading onset in the 99.99th percentile.

Published Ag threshold switches are used only as feasibility anchors, not copied designs: Ag-containing volatile selectors have experimentally shown enormous HRS/LRS ratios and hundreds-of-nanoseconds relaxation/endurance scales. v14V1's architecture, geometry and use of the ionic state as a perpendicular learning address are GVS-generated.

## One-million-trial result

At 100 ns feedback delay:

- tagged HZO >=1.0 V: ~99.998%
- untouched HZO <=0.15 V: 100% observed
- 500 ns stale HZO <=0.15 V: ~99.9985%
- inference-only induced HZO voltage <=0.30 V: 100% observed
- fresh conductance-gain p0.1: >1000x
- fresh barrier-shift p0.1: ~0.232 eV
- stale barrier-shift p99.9: ~0.080 eV
- winner pocket ions p0.1: ~142
- loser pocket ions p99.99: 0 in the model

At 80 ns the fresh margin is stronger; at 500 ns the tag has effectively ceased to be useful. A future thinking-layer replay can deliberately recreate the tag immediately before TEACH, so a human or high-level reasoning process does not need to respond inside 100 ns.

## What problem is solved?

The arbitrary hard requirement for a special material that intrinsically changes by 5000x is removed. The gain can emerge from a modest transient ionic barrier shift in a side pocket, and the actual circuit only mathematically requires ~14x fresh/stale separation.

## What remains unsolved?

The remaining blocker is now a single physical coupon question, not architecture:

1. Does a guided-gap firing event reproducibly populate the side pocket with enough ions?
2. Does that occupancy shift the perpendicular program barrier by roughly >=0.2 eV at ~100 ns?
3. Does the pocket self-empty by ~500 ns across temperature/process variation?
4. Does it survive repeated cycles without permanent Ag trapping or HZO disturb?

If those measurements fail, v14V self-addressing is rejected and v14U's sparse regional decoder remains the fallback. No per-branch MOS rescue is allowed.

## What is next?

Fabricate/model-calibrate a two-path coupon: horizontal guided-gap inference path crossing an orthogonal TEACH barrier, with the SEEP pocket beside the crossing and the HZO FIC outside the ionic current path. Measure transient program conductance at 20/50/80/100/200/500 ns after firing, then repeated cycling and temperature.
