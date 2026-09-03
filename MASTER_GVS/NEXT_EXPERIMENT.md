# Current Next Experiment — v14R1 Calibrated Compound PGDB

## Goal

Close the only major unresolved ordinary-cell device in v14R: one two-terminal Polarity-Guided Diffusive Branch combining a v14O volatile guided gap with an edge-exposed reversible HZO polarity collar.

## Required sequence

1. Select one published 5–6 nm HZO stack with usable raw P-V / pulse-switching data and a realistic BEOL-compatible electrode/process candidate.
2. Fit a calibrated ferroelectric switching model or lookup table. Stop using the current simple Vc threshold sensitivity once calibrated data is available.
3. Build a 3-D electrostatic model including both metal electrodes, HZO polarization, the exposed collar edge, the guided-gap geometry and neighboring branches.
4. Measure the actual local gap-voltage/field shift in favored, neutral and reversed states.
5. Couple that field directly into the v14O guided-gap stochastic firing model.
6. Test 0.25 V inference disturb over a large pulse-equivalent count.
7. Test +0.6/-0.6 V selected coincidence, <=0.6 V half-select accumulation, reversal, imprint, retention, temperature and variation.
8. Add shallow eligibility only if the same collar produces a useful short-lived state without materially biasing inference.
9. Compare the final PGDB against the best retained v14J/v14M two-terminal alternatives on complete energy, area, program infrastructure, endurance and selection accuracy.

## Acceptance

Promote the compound PGDB only if:

- effective collar coupling >=12.5% equivalent in the current race model, >=15% preferred;
- five-way correct + quenched >=99% across calibrated variation or a cheaper physical correction achieves the same system target;
- ordinary inference does not materially rewrite deep polarity;
- half-select lifetime disturb is acceptable without a per-branch MOS selector;
- reversal works repeatedly;
- no standalone UET device is required;
- total compound branch plus shared programming infrastructure beats the retained transistor/two-terminal references.

## Failure rule

If HZO cannot retain enough fringe field or half-select/read disturb cannot close without per-branch active selection, reject the HZO collar implementation. Keep the physically closed tiny Choice Node and v14O guided firing core, then test the next two-terminal polarity/charge-trap candidate. Do not add transistors merely to preserve v14R's name.
