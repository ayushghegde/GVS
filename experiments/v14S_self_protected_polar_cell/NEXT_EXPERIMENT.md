# v14S1 — Physical Compound Polar Branch + 8-Cell Program Porch

## Goal

Close the only remaining v14S question: can the same physical branch footprint combine low-voltage guided-gap inference with a separately programmed HZO field memory and passive half-select protection without requiring a MOS transistor beside the branch?

## Required evidence

1. Calibrated ferroelectric pulse/hysteresis model for the selected HZO candidate, including 0.4-V half-select history and ~1.2-V selected pulses.
2. Dynamic compact model for the passive nonlinear inhibit element; static Ron/Roff is no longer sufficient.
3. Real 3-D electrostatic field solution for HZO + electrodes + grounded aperture shield + guided-gap metals.
4. Coupled guided-gap Monte Carlo using the extracted polarity-induced threshold shift rather than the current equivalent-charge proxy.
5. Repeated 0.25-V inference read-disturb test.
6. Repeated half-select stress, polarity reversal, imprint/fatigue and temperature variation.
7. Two neighboring compound branches to measure crosstalk and common-electrode interaction.
8. Physical 8-cell program-porch layout with line RC extraction. Compare 5/20/100-µm model brackets with the actual routed value.
9. Count final active/passive devices and routed footprint. Include shared level-generation and write drivers.
10. Compare against the physically closed v14E 15-MOS/2-MIM reference and the preserved v12S transistor-heavy route without treating different functions as identical.

## Acceptance

KEEP v14S only if all are true together:

- no MOS/transistor in the ordinary semantic cell or branch;
- effective retained collar polarization >=0.14 C/m² or equivalent field effect under worst relevant corner;
- six-way correct+quenched route probability >=99.9% using calibrated device statistics;
- half-select/inference disturb does not create a durable wrong-route bias;
- four-active-plus-two-spare scheme gives acceptable region yield;
- shared program porch remains <=5 MOS-equivalent/cell or proves a materially better area/energy trade;
- final branch routed footprint stays below ~1.99 µm²/branch, the conservative break-even against v14E MIM plate area alone, unless a larger branch still wins total cell area after full accounting;
- inference energy/delay remains better than the favorable CMOS break-even controls after extracted line/device parasitics;
- no hidden always-on bias or refresh is required.

## Failure rule

If the passive inhibit or HZO field coupling fails, do **not** repair the branch with a per-branch MOS selector. Keep the low-voltage guided-gap result and test another passive nonvolatile field source/selection stack. If every viable memory source requires per-branch active selection, mark the v14S transistor-replacement path FAIL rather than disguising CMOS as shared physics.
