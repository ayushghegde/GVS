# Current Next Experiment — v14G1 Transistor-Free Structural Operator

## Problem
v14G can recall and compose learned semantic relations, but it cannot solve an exact relation that has never been physically embodied. The deliberate withheld-arithmetic screen scored 0%.

## Goal
Create a transistor-free physical operator that represents a reusable transformation rather than one memorized value-to-value edge.

## First target
Arithmetic addition is the clean acceptance task because the correct result is unambiguous and generalization can be measured exactly.

Test at least three approaches:
1. residue/phase-coded value rings where addition is a physical displacement or phase transform;
2. regular waveguide/coupler displacement that reuses one relation geometry across many values;
3. sparse learned lookup as the control.

## Acceptance
Keep an operator only if it:
- computes unseen operand combinations rather than recalling them;
- uses no MOS transistor in the reasoning core;
- needs substantially fewer programmable links than a value-by-value lookup table;
- composes for at least 8 sequential operations under device variation;
- retains an exact-error detector or Population Confidence boundary;
- has a credible fabrication path simpler/cheaper than recreating transistor logic.

If none passes, v14G remains an associative retrieval/reasoning fabric and exact arithmetic stays an unresolved hardware problem rather than being hidden behind a processor.
