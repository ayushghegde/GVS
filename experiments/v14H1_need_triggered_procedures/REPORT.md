# v14H1 — Need-Triggered Transformation Selection

## Problem
A reasoning path should not require a stored global instruction sequence. The same learned transformation should be reusable whenever the current state needs it, including on numeric values never seen during training.

## Mechanism tested
**Need Potential:** local mismatch between active state and active goal.

**Need-Triggered Transformation Cell (NTTC):** reusable transformation selected by that mismatch rather than by a program counter or fixed step number.

The model uses six transformations for the rectangle trace:

1. bind unknown;
2. express dependent relation;
3. apply area relation;
4. expand/balance to zero form;
5. factor;
6. select feasible root.

Problems may arrive with any prefix already completed. Therefore the correct first transformation varies by current state.

## Dataset
All unique combinations of:

- width 1..50;
- offset 1..20;
- six starting stages.

Total: 6,000 unique problem states. 25% were placed in the exact full-state lookup control; 4,500 were held out.

## Result
- need-gated trace success on held-out numeric states: 100% nominal;
- exact full-state lookup first-action success on held-out states: 0%;
- blind fixed six-step trace success: 16.58%.

The need templates deliberately do not contain the numeric width/offset values. They match unresolved structural state.

## Population stress
The need-state feature population was replicated and independently corrupted before local competition.

Nine-copy population trace success:

- 5% feature flips: 99.99%;
- 10%: 99.71%;
- 15%: 97.64%;
- 20%: 90.48%.

This is an abstract fault-injection model, not measured physical reliability.

## Concrete trace
For width unknown, length five greater, area 84:

`unknown -> x`

`relation -> x+5`

`area relation -> x(x+5)=84`

`zero-form need -> x^2+5x-84=0`

`factor need -> (x+12)(x-7)=0`

`physical-dimension constraint -> x=7`

The selection experiment supports the **need-triggered control idea**, but it does not physically implement multiplication or factorization. Those are v14H2.
