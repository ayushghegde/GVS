# v13B continuity — reuse the old readerless electricity rule

## Historical finding

The older v12E/v12F/v12G line already attacked a reader-energy problem by avoiding the reader when possible. A live electrical trace was used directly as a MOS-gate control to steer inhibition/fatigue/context. v12H later showed that a small regenerative latch can be offset-sensitive; v12I therefore kept exact fallback for truly ambiguous cases. v12R generalized the boundary rule: weak analog evidence stays inside local dendritic/event processing, and only an already-robust soma/interneuron/full-swing event crosses into exact logic.

## Current v13B screen

The newly closed v13A5 co-placed Grammar block gives about 20-22 mV exact/partial candidate-reference separation. A direct-steering screen reused the v12G topology with two equal 88 pF local candidate membranes and equal 23 nA evidence. `GC` directly gates the weak shunt on the context-incompatible candidate, while `GR` gates the opposite shunt.

Naive minimum/short shunts are too strong at the Grammar common mode (~0.53-0.58 V): L=2 and L=4 suppress both candidates and are rejected.

With W=.42 um/L=12 um shunts at TT:

- exact-like GC>GR case: correct C crossed 0.5 V at ~4.584 ms; wrong E did not cross by 5 ms; Cmax ~0.555 V, Emax ~0.368 V.
- partial-like GC<GR case: correct opposite E crossed at ~3.982 ms; C crossed only at ~4.985 ms; Emax ~0.662 V, Cmax ~0.502 V.

So the physical differential can directly steer an existing local competition stage without a powered reader. However this is **not** adopted as a replacement for the v13A5 Grammar reader: the test uses the old large 88 pF membrane/time scale, and the ~0.55 V Grammar common mode makes simple direct shunts sensitive to device strength. It is useful only when a downstream local membrane/interneuron already exists and can absorb the steering function for free or nearly free.

## Architecture rule

For v13B:

1. keep weak evidence analog and local;
2. when a local membrane/interneuron already exists, first try direct differential inhibition/steering rather than adding a separate reader;
3. never add a large membrane just to avoid a ~0.08-0.10 pJ reader;
4. if no suitable physical competition stage exists, use the closed dual-pair v13A5 reader;
5. exact/full-swing state is used only after a robust local event or for ambiguity/fallback.

This preserves the old Glyph direction rather than making routing/reasoning globally digital.
