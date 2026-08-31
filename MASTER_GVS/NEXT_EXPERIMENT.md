# Current Next Experiment — v14H2 Structural Product / Factor Relation

## Problem
v14H0 now has a model-level reusable exact addition candidate in `Z_420`, and v14H1 has a need-triggered transformation-selection model. The remaining gap in the user's rectangle example is physical structural multiplication/factorization.

## Goal
Create a transistor-free reusable product/factor relation that does not store one link for every `(a,b)->a*b` pair and that can stay compatible with residue-coded values.

## Candidates to test
1. residue-domain product coupling: each residue ring performs local modular multiplication and a coherent population reconstructs the product state;
2. logarithmic/phase product transform: multiplication becomes additive phase displacement where representation permits it, with explicit handling of zero/sign and finite-domain limits;
3. factor-constraint membrane: candidate factor populations co-fire only when their structural product relation satisfies the target residue tuple;
4. sparse pair lookup as the control.

## Acceptance
Keep a candidate only if it:
- solves held-out operand pairs;
- supports the `x(x+5)=84` factor relation without a CPU;
- composes for at least eight operations/transformations under modeled variation;
- has a materially better confidence/error boundary than the current CRRO replica-disagreement signal;
- uses far fewer programmable pair links than a full product table;
- has a plausible two-terminal/passive + sparse-restoration physical path.

If no candidate passes, keep CRRO for exact modular addition and mark multiplication/factorization unresolved.
