# v14P Experiment Report — Electrostatic Trail Selection

## Question
Can the user's 'positive charge at the useful wire tip' idea become a physically sensible transistor-free route-selection mechanism?

## Interpretation of the drawing
The useful abstraction is not that electrons are literally pulled around a bend like particles following a charged signpost. A local trapped charge/polarization changes the electrostatic potential and therefore the barrier/field at a branch mouth. The standard excitation then preferentially switches the easier branch.

## Experiment 1 — learning-rule failure control
Six candidate branches per node were given an electrostatic trail variable. Reading was noisy; trail coupling and base conductance varied by device; 5% of programming attempts failed. After initial learning, 25% of relations were remapped.

Result:
- use-only deposition: near chance before and after remapping;
- confirm-only: initial learning works but old positive trails remain competitive after knowledge changes;
- reversible confirmation/contradiction: initial learning works and remapped relations are relearned rapidly.

Selected deterministic aggregate (6 seeds):
- reversible pre-change accuracy: 100%;
- after 500 adaptation events: ~79.1% on changed relations;
- after 2,000: 100%;
- old-route selection after 2,000: 0%.

This is a model result, not measured hardware.

## Experiment 2 — branch-tip electrostatic selection
A branch barrier model was used with a 0.22-V reasoning pulse and 0.25-V baseline threshold. The selected path carried a favorable trail (+5 effective units); contradicted alternatives used -1. Threshold sigma was 16 mV, trail/coupling variation 25%, and electrostatic crosstalk 15%.

120,000 trials:
- correct branch winner ~98.06%;
- clean target-only threshold crossing ~87.17%;
- wrong-branch threshold crossing ~2.78%.

The winner metric matters because Population Confidence / local competition can tolerate weak subthreshold/secondary activity better than requiring every incorrect branch to be perfectly silent.

## Experiment 3 — fanout stress
The same model was swept across 4, 8, and 16 candidate branches and 8-20 mV threshold spread.

Very wide branching degrades first. The hardest 16-way / 20-mV case reached ~89.5% winner accuracy. This supports the existing sparse-connectivity rule instead of a dense crossbar.

## Physical interpretation
The preferred v14P device is a small charge-trap/electret/ferroelectric-like pocket adjacent to the v14O guided-gap tip. The trail should modulate the local field/barrier but not carry the full inference current.

A favorable learning pulse traps charge/polarization that lowers the branch barrier. A contradiction pulse detrapps, compensates, or reverses the field. Ordinary inference pulses stay below the programming condition.

## Literature boundary
Two-terminal HfO2 devices have experimentally shown electron-trapping-driven conductance changes and relaxation, so charge-controlled local fields are physically plausible. Charge-trap memories also demonstrate that trapped charge can shift device electrostatics. However, published charge-trap reliability work warns about migration, neighbor interference, and retention loss at small scales. v14P must therefore physically close those exact risks rather than assuming an ideal electret.

## Decision
KEEP the electrostatic-trail concept as a route-bias memory layer.

Do not replace v14O firing with it. Combine them:
- v14O guided-gap branch = fast transient conduction;
- v14P trail tip = persistent route preference.

This decoupling is currently more credible than demanding one filament state simultaneously optimize nanosecond firing, long retention, reversible learning, and low leakage.
