# Neural Glyph v14P — Polarized Trail Branch Fabric

**Status:** model-level branch-selection / reversible-learning architecture. No fabricated polarized trail collar or extracted <=1 fF choice node exists yet.

## Central physical idea

A semantic cell does not retain long-term meaning as node voltage. It emits only temporary excitation. Several sparse candidate branches leave a tiny shared choice node. Each branch uses the v14O guided-gap volatile junction for fast conduction, but long-term route preference is stored in a local reversible electrostatic polarization/trapped-charge region surrounding the branch tip.

## New primitive — Polarized Trail Collar (PTC)

**PTC:** a nanoscale polarizable/trap-rich dielectric collar around a guided-gap branch tip that shifts the local electric field without carrying the main inference current.

- confirmed/favored state lowers the local bridge-formation barrier;
- neutral state leaves the branch near baseline;
- contradicted/reversed state raises the barrier;
- ordinary reasoning pulses stay below the programming condition;
- later learning can reverse the polarization again.

The preferred collar is dipolar/compensated rather than a bare patch of net charge. A nearby positive/negative pair gives strong local field at its own tip while the field falls faster at neighboring branch tips.

## Interpretation of the drawn branch idea

The useful physical abstraction is not that electrons are pulled around a wire bend like particles following a sign. Instead, the trail field changes the local barrier / effective gap field. Under the same transient source excitation, the branch with the favorable trail forms its temporary bridge earlier.

## Learning rule

Traffic alone does **not** permanently strengthen a path.

1. use creates eligibility;
2. confirmation / successful self-test strengthens the active correct PTC;
3. contradiction reverses or neutralizes the active wrong PTC;
4. uncertain new knowledge remains provisional and requires corroboration;
5. later evidence may reverse the same physical relation again.

This preserves v14K's rule that effort/usage is not truth.

## Branch competition

The selected ordinary cell uses about 4–5 local candidate branches.

Integrated v14O + v14P guided-gap race model, effective favored/reversed trail states, 15% trail variation, v14O gap variation:

- 4 branches: ~99.11% correct first bridge;
- 5 branches: ~98.65%;
- 8 branches: ~97.61%;
- 16 branches: ~94.60%.

Therefore wide local fanout is rejected. Larger logical fanout is reached through shared relay/hierarchical small branch bundles.

## Tiny choice node

A hidden timing problem appears if the whole semantic cell capacitance must discharge after the first branch fires. v14O's ON path is roughly 2.3 Mohm in the model, so a large node would quench competing branches too slowly.

v14P therefore adds a **Choice Node**: a very small local metal/output node that only feeds the branch mouths.

At 0.25 V and 2.3 Mohm:
- 1 fF choice node: ~0.51 ns to fall by 20%, ~0.031 fJ stored-energy scale;
- 0.5 fF: ~0.26 ns, ~0.016 fJ.

With a 1 fF node in the current race model:
- 4-way correct + quenched before second branch: ~98.15%;
- 5-way: ~97.52%.

The <=1 fF value is a physical extraction target, not an achieved layout result.

## Hierarchical sparse routing

Direct 16-way local branching is weaker than two 4-way stages in the model:
- direct 16-way first-bridge correctness: ~94.8%;
- two 4-way stages: ~98.1% first-order winner probability.

The architecture therefore scales by small branch bundles / relay tissue rather than dense local stars. Semantic transformation nodes may not be skipped merely to improve transport statistics.

## Retention and reconsolidation

A PTC need not have perfect forever-retention if confirmed use reconsolidates it.

Sensitivity examples over ten years:
- 1-year intrinsic trail decay + monthly confirmed use: ~98.3% mean query accuracy;
- 2-year decay + ~6-month use: ~95.3%;
- 5-year decay + yearly use: ~96.5%;
- 20-year decay + ~2-year use: ~98.2%.

Rare unused knowledge can fade; this is an explicit design trade, not a claim about human memory.

## Relearning

Across 12 rounds where 20% of relations are remapped per round, with 5% physical program failures and 3% wrong feedback, three corroborated updates per changed relation gave at the final round:
- ~98.34% overall accuracy;
- ~97.65% accuracy on just-changed relations;
- ~1.42% selection of the old relation;
- 100% accuracy on never-changed relations in this model.

## Relationship to v14O

v14O supplies:
- guided short dynamic gap;
- field-focus inert spine;
- passive ballast/current self-limiting hypothesis;
- volatile temporary bridge;
- sparse long-distance regeneration.

v14P supplies:
- persistent reversible route preference outside the main current path;
- branch competition through local field bias;
- decoupling of fast volatile firing from long-term learned state.

This means v14P no longer requires the main firing filament itself to provide both nanosecond volatility and long-retention semantic memory.

## Cost rule

The PTC is worthwhile only if it is integrated into the branch dielectric/sidewall without a per-branch MOS gate or expensive selector. A 10 nm x 10 nm, 5 nm-thick, k~20 electrostatic geometry has only an attofarad-scale capacitance floor, but that is **not** a programming-energy claim; real trap injection/ferroelectric switching/peripherals may dominate.

## Keep / reject

KEEP:
- temporary excitation in cells;
- persistent route state in local connection polarization;
- 4–5-way local branch bundles;
- reversible confirmation/contradiction learning;
- v14O guided-gap volatile conduction;
- tiny choice node and hierarchical/shared relay expansion.

REJECT:
- bare free positive charge sitting indefinitely on metal;
- traffic-only permanent strengthening;
- dense 16+ way local fanout by default;
- assuming the first branch automatically suppresses others without a sub-fF/few-fF quench-node analysis;
- claiming charge-trap / ferroelectric retention or write energy before calibrated device evidence.
