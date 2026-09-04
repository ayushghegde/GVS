# Neural Glyph v14V — Self-Addressed Polarity Fabric

**Status: PARTIAL PASS — physical TEACH-mesh rerun pass; self-addressing concept survives; original ETG/learning model does not meet final acceptance.**

## What happened

v14V tested the rule **activity becomes the address**. A winning branch creates a temporary local eligibility state and a regional TEACH mesh later broadcasts only confirmation or contradiction. Normal row/column learning decode is therefore removed from the ordinary cell path.

A fully reproducible rerun was performed after the earlier interrupted run. The rerun is the authoritative v14V result and is intentionally harsher than the earlier report.

## Physical TEACH-mesh rerun

Magic/SKY130A metal2 proxy extraction was rerun on fresh compact teaching meshes:

- 64-cell mesh: 0 DRC errors, **15.2122 fF** extracted TEACH-node capacitance.
- 256-cell mesh: 0 DRC errors, **46.6582 fF** extracted TEACH-node capacitance.

These are metal-routing proxies only. HZO, the guided gap and the volatile eligibility physics are not present in SKY130.

## Self-tag rerun

One-million-trial event-charge model:

- winner tag success: **100.000000%**
- loser false-tag fraction: **1e-06**
- winner charge p0.1: **2172.9 e**
- loser charge p99.9: **375.1 e**

The event-charge separation remains strong enough to continue self-addressing experiments.

## Original ETG model — problem found

The reproducible v14V ETG model assumed a ~5000x fresh conductance gain directly rather than deriving it from a device mechanism. At 100 ns it produces:

- tagged HZO >=1.0 V: **99.9511%**
- untouched HZO <=0.15 V: **100.000000%**
- 500-ns stale HZO <=0.15 V: **99.9835%**
- tagged p0.1 internal voltage: **1.058 V**

Therefore the old ETG abstraction is **not physically closed and does not meet the preferred >=99.999% tagged-write target at 100 ns**.

This is the dominant v14V device problem addressed by v14V1.

## Learning rerun — second problem found

The corrected one-causal-event-at-a-time learning model is less flattering than the interrupted result. At 3% feedback error:

- explicit-address reference final accuracy: **99.980%**
- raw self-addressed final accuracy: **97.227%**
- corroborated self-addressed final accuracy: **97.891%**

The reason is structural: self-addressing naturally changes the route that actually fired. It can weaken a wrong route or strengthen a correct one, but it cannot directly strengthen an alternative route that did not fire. This is not an ETG defect. It is a learning-level problem and motivates the later two-level thinking/neuron architecture.

## Energy rerun

Using extracted metal plus estimated HZO collar capacitance:

- 64 cells: ~**28.77 fJ** after the charge-recovery envelope plus launcher proxy.
- 256 cells: ~**48.27 fJ** on the same basis.

Only the metal capacitance is extracted. HZO loading, recovery fraction and launcher energy are models.

## What is the problem now?

There are two different problems and they must not be mixed:

1. **Neuron/device problem:** derive the temporary program-path conductance from a real physical mechanism instead of assuming a 5000x ETG gain.
2. **Thinking/learning problem:** decide which alternative path should be promoted when the currently selected path is wrong. A branch-local self-tag alone cannot know that.

v14V1 attacks problem 1. The future v15A thinking-layer experiment attacks problem 2.

## Decision

KEEP: activity-as-address, one TEACH mesh, polarity memory, guided volatile gap, field isolation, hollow charge recovery, 0-MOS semantic cells.

REJECT: treating a hard 5000x conductance ratio as a free device property; claiming the self-addressed local rule alone is sufficient for high-quality learning.

## What is next?

**v14V1 — Self-Emptying Echo Pocket.** Replace the arbitrary gain with an ion-populated side pocket that electrostatically lowers the orthogonal program barrier after firing and automatically empties. Then carry the surviving hardware into v15A's two-level learning architecture.
