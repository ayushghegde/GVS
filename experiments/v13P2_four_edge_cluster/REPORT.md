# GVS v13P2 — Four-Edge Physical Myelin Cluster

**Status: PASS for the measured cluster-coupling question; full extracted tile still open.**

## What happened

Four copies of the verified v13P0 physical Myelin edge were placed at 4.5 um vertical pitch. Each copy preserves the exact 2x2 um MIM, W=0.42 um/L=0.15 um NFET, contacts and routing geometry. No GVS architecture was changed.

Magic 8.3.681 with the supplied SKY130A technology reported **0 DRC errors** for the four-edge cluster and extracted all four intended MIM/NFET pairs.

## Accumulated coupling

The two middle edges each have neighbors above and below, so they expose the first accumulation effect that a two-edge test cannot show.

Measured total inter-edge coupling incident on the middle local-dendrite H nodes:

- H1: 0.034551803 fF
- H2: 0.034551803 fF

For the other middle nodes:

- G1/G2: 0.232195300 fF each
- MX1/MX2: 0.128949300 fF each

Nearest-neighbor terms remained the same as the pair experiment:

- H-H: 0.017064700 fF
- G-G: 0.112633000 fF
- MX-MX: 0.060883000 fF
- Q-Q: 0.005343270 fF

The middle H-node accumulation is about 87 times smaller than the +3 fF local-dendrite load used in the historical v12S moderate parasitic stress profile.

## What this changes

The evidence now says that the first physical limit is unlikely to be simple nearest-neighbor Myelin-slot density at 4.5 um pitch. A single edge, a pair, and a four-edge cluster all remain comfortably inside the old local-dendrite stress envelope.

The next more credible scaling risk is **shared-network fan-in**: run, capture and other control nets collect load from many structures and were stressed in v12S by +20 fF rather than +3 fF.

## Current problem

There is not yet a placed shared run/capture network to extract. The complete-tile transient lifecycle also has not yet been rerun with physical RC.

## What is next

1. Lay out a small representative shared-control spine with multiple attached edge/soma taps.
2. Extract capacitance and resistance on the shared node as fan-in increases.
3. Determine the fan-in/pitch where extracted shared-node load approaches the historical +20 fF v12S stress level.
4. Use that evidence to choose hierarchy/repeater/localization only if needed; do not redesign pre-emptively.
5. Feed the measured shared-network RC together with the v13P0 edge overlay into the unchanged v12S lifecycle simulation.

No architecture change is justified by v13P2.
