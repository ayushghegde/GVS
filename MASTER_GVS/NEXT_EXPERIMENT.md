# Current Next Experiment — v13Q1 Physical Contact-Aperture Slice

## What v13Q0 established
v13Q0 changed the local communication substrate rather than adding another computer-like controller.

### Cell-as-wire result
In a 16 x 16 x 4 packed-cell model, selectable face/edge/vertex neighbour contacts reduced mean local relay count from ~11.877 to ~7.476 hops (~37.05%). With edge contacts modeled at 1.5x face-event cost and vertex contacts at 2x, the embodied cell path was ~18.53% lower energy than face-only. If edge/vertex costs rise to 2x/3x, the energy advantage disappears.

**Decision:** face contacts are default; diagonal contacts are optional shortcuts only after physical cost extraction.

### Population-confidence result
Uncertainty is represented as disagreement between competing cell populations. Robust output is allowed only when winner-minus-runner-up accumulated evidence crosses a confidence margin.

At the stronger tested evidence point, 20,000 trials produced 100% correct robust decisions and zero unresolved. At the moderate point, 99.8% were correct robust, 0.01% wrong robust and 0.19% remained uncertain.

**Decision:** low confidence means keep settling / remain non-robust, not automatic exact-computer fallback and not guessing.

### Quorum relay result
With 10% independent contact-event errors across a 16-hop modeled path, local multi-contact agreement dramatically reduced propagation error. Nine supporting contacts reduced the measured wrong end-to-end fraction to ~0.085% with only ~1.008 local attempts/planned hop.

**Decision:** local redundancy is a reliability knob, but physical area/capacitance must decide the useful quorum size.

## v13Q1 goal
Build the smallest real SKY130 planar proxy that can answer whether an Embodied Conduction Cell is physically economical near weak Glyph evidence.

### Required elements
1. one real/recovered Grammar candidate/reference weak pair or equivalent preserved physical weak-node geometry;
2. one repeated local cell body/state node;
3. four face-like selectable neighbour Contact Apertures;
4. at least one diagonal-shortcut geometry candidate;
5. normally-off contact state;
6. local regeneration/event output;
7. Nerve line retained as the dedicated-route comparison;
8. separate Charge Artery retained so information contacts do not become recovery paths.

## Measurements
- DRC and extracted connectivity;
- off-state aperture capacitance into the local state and GC/GR;
- on-state event energy and propagation delay;
- differential coupling into GC versus GR;
- face versus diagonal aperture area/capacitance;
- number of apertures that can surround one cell before loading becomes unacceptable;
- TT/FF/SS and mismatch for the local regeneration element;
- ambiguous/low-margin input behavior: must stay non-robust before a wrong accept;
- comparison with existing direct fourth-face and dedicated Nerve/event-spine proxies.

## Acceptance
v13Q1 passes only if:
- DRC/connectivity are correct;
- closed apertures do not materially destroy the preserved weak-evidence margin;
- ordinary active local contact events do not require a global quiet scheduler;
- ambiguous evidence can remain unresolved/non-robust;
- no per-cell router, ADC or microcontroller is introduced;
- face contact is physically competitive with a separate short local wire;
- diagonal contact is kept only if its reduced hop count repays its extra physical loading;
- recovery and thermal service remain isolated from weak information contacts.

## Failure response
If off-capacitance is excessive, reduce/contact-share/isolate apertures before changing Grammar. If diagonal contacts are expensive, delete them without rejecting the cell-as-wire concept. If local quorum requires too much hardware, use population agreement over time/nearby cells rather than duplicating a large voter inside every cell.

## After v13Q1
If physical contact apertures pass, build v13Q2: a multi-cell physical chain where the same repeated cells perform local computation, confidence accumulation and event regeneration. Compare total area/energy against compute-cell + separate local-router/wire organization.
