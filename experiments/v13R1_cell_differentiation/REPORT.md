# Neural Glyph v13R1 — Cell Differentiation Screen

**Verdict: MODEL PASS.** A mixed GVS region should not make every Embodied Conduction Cell carry every optional computation block. A small number of general cells plus many specialized cells retains flexibility while removing most duplicated optional hardware.

## New terms
**Differentiated Embodied Tissue (DET):** a local region built from several ECC cell roles that share the same conduction/body rules but contain only the optional compute/state modules needed for their job.

**General Reserve Cell (GRC):** a small minority of broader-function ECCs kept for novelty, repair, remapping and workload imbalance.

## 64-cell test region
4 x 4 x 4 packed cells:
- 20 relay/conduction;
- 12 Grammar;
- 10 template;
- 8 transient-binding;
- 8 constraint/competition;
- 2 exact spatial-patch;
- 4 General Reserve Cells.

Every cell keeps the base conduction/body structure. Optional module copies are compared against a universal cell carrying all five module classes everywhere.

## Selected four-general-cell result
- optional module-copy reduction: **81.25%**;
- average extra movement for a 2-5-stage mixed operation: **1.8456 cell hops**;
- p95 extra movement: **4 hops**;
- existing 0.15 fJ local-hop proxy -> **~0.277 fJ average added route energy**;
- all five module classes remained available in **100% of 10,000 trials** with independent 10% random cell-failure probability.

Module-copy reductions:
- Grammar 75.0%;
- Template 78.125%;
- Binding 81.25%;
- Constraint 81.25%;
- Exact patch 90.625%.

## Cost sensitivity
Optional module costs were swept independently over 0.25x..8x a common conduction-body unit. The selected 4-general-cell fabric gave:
- mean total abstract hardware reduction: **73.38%**;
- 5th percentile: **65.74%**;
- median: **73.92%**;
- 95th percentile: **78.97%**.

These are abstract cost units, not mm^2 or dollars.

## Why four general cells
Zero general cells removes more copies (87.5%) but routes farther and is more brittle to loss of a scarce function. Four general cells were the first tested point with 100% module-class availability in the 10% independent random-failure stress while still removing >80% of optional copies.

## Hardware consequence
Relay ECCs should not carry Grammar MIM/readout merely because a neighbor does. Grammar, Template, Binding, Constraint, Exact and General cells each keep only the role-specific structures that repay their presence.

Recovery is differentiated too: a stateful/high-charge cell may earn a Slow Charge Egress tap; a tiny relay may omit it if recoverable energy does not repay device/coupling/area cost.

## Decision
- KEEP one common ECC interface/body standard;
- KEEP a small differentiated cell library;
- KEEP a small General Reserve population;
- OMIT unused optional modules;
- DO NOT create dozens of one-off cell types;
- SIZE role counts from workload and physical area/energy.

## Reproduce
`python3 experiments/v13R1_cell_differentiation/source/run_v13r1.py`

Evidence class: deterministic role-placement/reliability model plus abstract cost sensitivity.
