# v14H0 — Transistor-Free Structural Operator Screen

## Problem
v14G associative reasoning failed completely when exact arithmetic transitions were deliberately withheld. This experiment compares reusable physical-structure models against sparse memorized lookup.

## Compared approaches
1. **Coprime residue/phase rings:** values are encoded on mod-3/mod-4/mod-5/mod-7 rings. Addition is local phase displacement. Five replicas per ring provide majority restoration.
2. **Reusable wave displacement:** one N-site displacement geometry computes `a+b` by position shift; three tracks provide voting.
3. **Sparse lookup:** 25% of all operand pairs are stored exactly.

## Domain
`Z_420` modular addition. The finite modular domain is intentional because the residue code is exact there. This experiment does not claim unbounded arithmetic.

## Unseen-pair result
There are 176,400 operand pairs. The sparse lookup stores 44,100 and 132,300 are held out.

- CRRO-5 nominal held-out exact: 100%.
- wave-3 nominal held-out exact: 100%.
- lookup-25 direct held-out exact: 0%.
- nearest memorized-pair interpolation: 6.8% on 1,000 held-out samples.

## Variation stress
Variation sigma combines static device offset and event noise in quadrature and is expressed as a fraction of one state pitch.

At sigma=0.20, 5,000 chains of 8 additions:

- CRRO-5 exact-chain rate: 99.98%.
- wave-3 exact-chain rate: 99.54%.

At sigma=0.20, 5,000 chains of 32 additions:

- CRRO-5: 99.76%.
- wave-3: 98.92%.

## Structural cost proxy
This is deliberately not called transistor count, area, energy, yield or cost.

- CRRO-5: 95 residue state sites; no programmable operand-pair links.
- wave-3: 1,260 state sites; no programmable operand-pair links.
- lookup-25: 44,100 programmable pair links and incomplete coverage.
- lookup-full: 176,400 programmable pair links.

## Confidence failure
The CRRO's simple population-disagreement flag is too blunt. At sigma=0.20 it flags 22.05% of operations while the actual per-operation error rate is only 0.0175%, and it identifies only part of the rare wrong states.

A separate coherence-check screen added mod-6, mod-10, mod-140 and mod-210 verification rings. None produced enough wrong-state recall for the added state sites under the selected noisy model, so they are rejected for now.

## Decision
**SELECT CRRO-5 as the v14H exact-addition operator candidate.**

Reason: it satisfies unseen-pair generalization, eight-plus-step composition, and structural economy better than the other candidates in this model.

Do not promote it to physical signoff. The transistor-free device implementation, energy, area, programming/restoration overhead, and confidence/error detector are still open.
