# v14N Experiment Report — Seeded Nodal Diffusive Relay

## What was tested
Two delay-reduction mechanisms were evaluated:
1. a Seeded Nucleation BDJ (SN-BDJ) device target that reduces stochastic filament path length / nucleation search;
2. a Sparse Regeneration Trunk (SRT) that uses active junctions only at spaced physical transport nodes.

## What causes the delay
Current device literature indicates that Ag-family diffusive memristor switching includes a finite incubation interval associated with filament/channel formation. Field-enhanced Ag+ drift and nucleation determine the delay; higher voltage reduces the delay and narrows its distribution. Embedded Ag nano-islands can localize filament formation and reduce threshold variability/electroforming burden.

## Device sensitivity result
The v14M hardest EDP limit is ~38.5 ns versus the lean 5 fF CMOS control. With a seeded-junction coefficient of variation target ~0.15:
- a 55 ns starting mean needs approximately a 0.55x mean-delay multiplier for its p95 to approach the 38.5 ns region;
- a 75 ns starting mean needs a stronger ~0.4x multiplier.

A simple half-distance sensitivity bracket gives 2x to 4x theoretical improvement depending whether delay behaves closer to linear path/drift or stronger field-drift scaling. This means a mid-gap field-focus seed is worth fabricating/testing; it does not prove that nucleation barriers will follow the simple bracket.

## Sparse transport result
64 physical transport hops, 10,000 trials, 30 ns mean regeneration junction:
- every-hop active regeneration: ~1.93 us mean delay, ~150.4 fJ;
- selected 22-hop spacing: 3 active nodes, 100% modeled success, ~172.2 ns mean, ~199.4 ns p95, ~9.19 fJ;
- spacing beyond the high-20s begins losing amplitude margin in the chosen proxy.

A favorable CMOS repeater control (5 fF, 1.8 V, 6 ns repeater every four hops) gives ~111 ns and ~261 fJ in the same simplified transport framework. Therefore current v14N is not yet a raw-delay winner at 30 ns/junction, but it has a strong model-level energy/EDP margin. Seeded junction delays around 10-15 ns make raw latency competitive in this proxy.

## Decision
KEEP both changes.

The architecture should not wait for a perfect 30 ns all-purpose device before improving transport. SRT reduces how often the slow ionic event is required for physical routing, while SN-BDJ attacks the ionic event itself.

## Evidence boundary
Everything in the transport/delay tables is an engineering model. Literature establishes relevant mechanisms and examples, not the complete v14N device. No fabricated v14N stack has been measured.
