# Neural Glyph v13O2 — Morphological Exact Patch

**Verdict: FUNCTIONAL MODEL PASS.**

## New term
**Morphological Exact Patch (MEP):** a repeated exact operation compiled into fixed spatial dataflow, so runtime execution is propagation through hardware rather than instruction fetch/decode/program-counter control.

## Experiment
An 8-bit unsigned ripple-carry adder was constructed entirely from NAND composition. Each full-adder bit uses nine NAND cells, so the complete patch uses 72 NAND cells.

Every one of the **65,536** possible 8-bit input pairs was exhaustively checked.

## Result
- 65,536 / 65,536 correct;
- 0 wrong results;
- 72 NAND cells;
- maximum logical depth 20;
- runtime instruction fetches: 0;
- runtime program-counter steps: 0.

## Interpretation
This does not claim 72 NAND cells replace a general computer. It proves that exact operations which are useful/repeated can remain exact while being embodied as local morphology. Generality must come from a fabric capable of selecting/combining learned structures, not from pretending analog relaxation should do exact arithmetic.

## Reproduce
`python3 experiments/v13O2_morphological_exact_patch/source/run_v13o2.py`
