# Neural Glyph v14O — Guided-Gap Self-Limited Diffusive Junction

**Status:** model-level physical-device invention and sensitivity closure. No fabricated v14O junction or calibrated compact model exists yet.

## Problem inherited from v14N
v14N identified the dominant delay in Ag/HfO2-class diffusive firing elements as stochastic filament nucleation and ionic migration. A seeded junction plus sparse transport regeneration helped, but the preferred 10–15 ns device target was still not physically closed. A second unresolved problem was current compliance: if every junction needs a MOS limiter, transistor elimination fails.

## v14O invention — GG-SLDJ
**Guided-Gap Self-Limited Diffusive Junction (GG-SLDJ):** a two-terminal diffusive junction with an inert conductive nano-spine rising through most of the switching dielectric, a sharpened field-focus tip that stops short of the active Ag reservoir, and an intrinsic passive ballast neck in the spine/electrode.

The important idea is not to make the entire dielectric thinner. Instead, leave only a short **dynamic gap** at one predetermined location. The inert spine is permanent and does not encode a semantic state.

Target geometry in the current model:
- total switching dielectric scale: ~4 nm;
- dynamic Ag bridge gap mean: ~1.3 nm;
- dynamic-gap sigma target: ~0.12 nm;
- local field-focus factor target: ~1.45x;
- intrinsic ballast target: ~2.2 Mohm;
- firing voltage target: ~0.25 V.

## Physical behavior
### Volatile firing instance
Incoming evidence increases the transient ionic/filament state near the spine tip. If evidence is insufficient, the atomic bridge dissolves. If sufficient, only the final short gap must bridge, producing a firing current. The passive ballast neck limits the current intrinsically and the bridge then self-relaxes.

### Learned relation instance
Other instances of the same geometry operate as persistent OFF / WEAK / STRONG relation junctions. Stronger or repeated learning stress grows a more stable conductive state. Opposite-polarity learning depresses it.

The two roles are instances of one device type; one physical instance does not need to be volatile and nonvolatile simultaneously.

## Local coincidence programming
v14O removes a separate addressed selector from the conceptual learning path. A normal reasoning pulse appears on one side of an active relation. When confirmation or contradiction returns from the other side, it arrives with the opposite polarity. Only the active relation sees the full differential learning stress.

Current screening example:
- ordinary read: ~0.20 V, 20 ns;
- half-selected local learning exposure: ~0.20 V equivalent;
- selected relation: ~0.40 V differential, 100 ns;
- uncertain understanding requires three corroborating coincidence events before hard consolidation, reusing the v14K provisional-understanding rule.

This is an addressing hypothesis, not a measured programming law.

## Current model result
Selected guided-gap target:
- mean firing delay ~11.85 ns;
- p95 ~14.81 ns;
- p99 ~16.31 ns;
- 100% of the current Monte Carlo delay population below the old 38.5 ns minimum EDP gate;
- ballast-limited current mean ~112.7 nA, p01 ~70.9 nA, p99 ~172.3 nA;
- strong learned-link conductance penalty from the ballast ~5.2%.

Eight-layer 64-cell cascade with 1% link failure + 1% firing failure:
- 20% link variation: mean final activity ~98.65%, p05 ~95.31%;
- 30% variation: mean ~97.96%, p05 ~93.75%;
- modeled total event energy proxy around ~1.90 fJ/fire at the 20% condition.

64-hop sparse transport with the selected device:
- one regeneration about every 13 physical hops in the selected sweep;
- five regeneration junctions;
- mean ~108.5 ns, p95 ~115.0 ns;
- ~11.4 fJ transport-energy proxy;
- deliberately favorable CMOS transport control: ~111.36 ns and ~261.44 fJ in the inherited proxy.

This is the first GVS transport sensitivity point where the new-junction model is both slightly faster and dramatically lower-energy than that favorable control, but it is not a silicon comparison.

## Why the geometry is different from simply copying nano-island literature
Published nanotips/nano-islands support the general facts that geometric field concentration can localize filament formation and that passive/interface resistance can provide self-compliance. v14O combines those facts into a different system target: one inert starter spine, one short dynamic gap, one passive ballast neck, and local differential coincidence programming for the GVS sparse semantic fabric.

## Keep / reject
KEEP:
- predetermined final bridge location;
- speed from path guidance + field focus rather than aggressively thinning the whole oxide;
- intrinsic passive current limiting;
- same two-terminal device family for firing and relation memory;
- three-evidence provisional consolidation for uncertain lessons;
- sparse regeneration only for physical transport.

REJECT:
- shrinking the entire oxide until leakage becomes the speed solution;
- per-device MOS compliance;
- a selector transistor at every learned relation;
- claiming the assumed 1.45x field factor or 1.3 nm gap distribution is measured v14O silicon;
- skipping semantic nodes under the name of Ranvier-style transport.
