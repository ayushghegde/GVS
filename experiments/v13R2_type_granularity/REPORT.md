# Neural Glyph v13R2 — Differentiation Granularity / Manufacturing Screen

**Verdict: MODEL PASS WITH A LIMIT.** Differentiation can remain worthwhile after charging an explicit cost for more standard-cell variants, but very fine specialization is rejected if design/test/yield/library overhead becomes too high.

## Three libraries
All cases use 64 cells and the same common conduction/body unit.

1. **Universal 1-type:** every cell contains all five optional module classes.
2. **Coarse 4-type:** relay, combined cognitive, exact, general reserve.
3. **Fine 7-type:** relay, five module-specific classes, general reserve.

Optional module copies:
- universal: 320;
- coarse: 174;
- fine: 60.

The model assigns one abstract cost unit to the common cell body and one to each optional module copy, then sweeps an added amortized penalty per extra cell type. These units are not dollars or mm^2.

## Results
With zero type penalty:
- coarse reduces abstract cost ~38.0%;
- fine ~67.7%.

At 16 units per extra type:
- coarse ~25.5% lower;
- fine ~42.7% lower.

At 32 units/type:
- coarse ~13.0% lower;
- fine ~17.7% lower.

Fine differentiation becomes more expensive than coarse at about **38 penalty units per extra type**. Fine reaches the universal-cell cost at ~43.3 units/type; coarse reaches it at ~48.7 units/type.

## Interpretation
v13R should not make a unique transistor layout for every learned concept. The manufacturing target is a **small reusable standard-cell family** sharing the same process layers and interface geometry.

Differentiation means different standard-cell contents/placement, not a new semiconductor process for every role.

## Decision
- SELECT a compact differentiated library as the current direction.
- KEEP a coarse fallback if physical characterization shows large type-specific verification/yield cost.
- REJECT both extremes: one universal bloated cell everywhere, and unlimited one-off cell types.

## Reproduce
`python3 experiments/v13R2_type_granularity/source/run_v13r2.py`

Evidence class: deterministic abstract manufacturing/design-cost sensitivity model.
