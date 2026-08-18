# Neural Glyph v13A6 — Margin-Tiered Grammar Readout

**Verdict: PARTIAL PASS — re-analysis shows the final 3-step sound Grammar ratio does not need the expensive two-phase self-check on the normal high-margin path; physical one-phase reader layout/PEX remains.**

## Why this experiment exists

v13A5 solved the old fixed-0.500-V Grammar threshold problem with a PVT-tracking equal-total legal-MIM ratio and a two-phase polarity-swapped regenerative latch.

That safe baseline was intentionally conservative because the latch stress battery showed that a simple one-phase decision can be offset-sensitive when evidence is only about +/-11 mV.

The final physical Grammar ratio, however, produces much larger evidence than that harsh stress case. v13A6 asks whether the second phase/swap network is still needed for the normal 3-bit sound Grammar primitive.

## Existing evidence re-analyzed

### Final real-swap Grammar mismatch screen

The v13A5 real-swap screen has 24 exact/partial cases across TT/FF/SS with MIM mismatch and transistor mismatch active together.

Observed physical-ratio margins:
- exact: approximately +27.35 to +29.51 mV in the preserved 24-case file
- partial: approximately -25.37 to -28.89 mV

**Phase 0 alone was correct in all 24/24 cases.**

Two full two-phase runs declared fallback:
- FF exact seed 202: phase 0 was already correct; phase 1 resolved too weakly
- SS partial seed 202: phase 0 was already correct; phase 1 preferred the same physical side

So the only observed failures in that screen were created by the extra safety phase, not by the normal first decision.

### Deliberate latch stress battery

The separate selected latch-D stress battery used +/-31, +/-18 and +/-11 mV evidence.

Single-phase phase-0 result:
- +/-31 mV: 24/24 correct across both signs
- +/-18 mV: 24/24 correct across both signs
- +/-11 mV: 22/24 correct; the low-margin region is not safe for unconditional one-phase use

Therefore the current data has a clear margin boundary:
- >=18 mV tested region: no observed phase-0 errors in this mismatch set
- 11 mV stress region: one-phase errors can occur

This is not a fabrication-yield claim. The unique mismatch sample count is still small.

## Architecture decision

For the discrete 3-step sound Grammar primitive, the physical ratio itself guarantees a large nominal separation between an exact 3/3 motif and a 2/3 partial motif. The current MIM mismatch screen also retained more than about 23 mV absolute margin.

Therefore the selected normal readout is simplified to **one direct regenerative comparison**.

### Normal high-margin Grammar path

`physical MIM candidate/reference -> direct PFET input pair -> regenerative latch -> robust local Grammar event`

No input polarity-swap matrix is required on the normal path.

The 13-MOS v13A5 reader can therefore be reduced conceptually to:
- 3 PFET latch-core devices
- 2 cross-coupled NFET devices
- 2 output-reset NFETs

**7 MOS** before any later physical optimization.

Removed from the normal path:
- 4 input-swap NFETs
- 2 input-reset NFETs
- second comparison phase
- second local motif replay
- PH1 routing
- X0/X1 swap-sample network

This is a **6-MOS / ~46% reader-transistor reduction** versus the 13-MOS two-phase implementation, before layout.

## Safety rule

The two-phase self-check is **not deleted**. It becomes a margin-tiered safety mode.

Use one phase only when the representation compiler/characterization proves the physical evidence class has adequate margin.

Use two-phase self-check or exact fallback when:
- physical evidence margin is low/unknown;
- the representation is not a discrete motif with characterized separation;
- drift/aging/layout extraction moves margin toward the unsafe band;
- calibration/health check requests a conservative re-test.

This follows the existing hybrid rule: spend precision only when uncertainty requires it.

## Why this is better than slow offset calibration right now

v11U-style slow condition memory remains interesting, but it is no longer the first optimization required here.

The final 3-step Grammar ratio already gives enough physical margin that the observed first-phase decisions are correct in the current combined mismatch screen. Adding calibration state before physically testing the simpler direct reader would add unnecessary hardware and another correctness dependency.

Calibration remains an optional future optimization for genuinely low-margin analog representations.

## Energy consequence

The measured v13A5 two-phase total readout energy is about 33-64 fJ depending on corner/case.

The one-phase energy has **not yet been directly re-measured** and is therefore not claimed as an exact number here.

However the second regenerative phase, swap/reset activity and second motif replay are removed. Because regenerative latch VDD work dominated the two-phase total, a substantial reduction is expected. Exact energy must be measured on the physical one-phase reader PEX before promotion.

## Physical-layout consequence

This simplification directly attacks the failure seen in the roomy 13-MOS reader layout:
- high-impedance GC/GR no longer pass through a four-NFET swap matrix;
- there are no X0/X1 sampling tracks on the normal path;
- candidate/reference only need short, symmetric routes into the PFET differential gates;
- PH1 and second-phase reset/swap routing disappear;
- evidence is no longer intentionally disturbed and replayed for normal decisions.

This should make the physical reader much easier to keep symmetric and low-capacitance.

## What is solved

- the current final 3-step sound Grammar physical-margin class does not show a need for unconditional two-phase self-check in the existing mismatch data;
- the previous physical swap-layout problem can be removed architecturally rather than fought with ever-more-complicated routing;
- two-phase self-check remains available only where it adds real correctness value;
- the readout policy is now compatible with the v12O/v13A physical-cost-aware compiler: confidence precision itself becomes adaptive.

## Remaining problem / next

1. lay out the 7-MOS direct one-phase reader with GC/GR connected only to short matched PFET-gate routes;
2. DRC and extract it;
3. attach the full extracted 10-MIM candidate/reference array;
4. verify exact/partial evidence margin after reader PEX;
5. run TT/FF/SS plus transistor + MIM mismatch;
6. require zero wrong accepted decisions in the tested high-margin class;
7. measure real one-phase energy;
8. compare area/capacitance against the 13-MOS compact/two-phase reader attempt;
9. place one shared reference/readout behind the selected eight-way Regional Lease;
10. keep two-phase self-check as the compiler-selected low-margin mode, not the default.

If the one-phase physical reader creates a new systematic layout offset large enough to threaten the >23 mV physical ratio margin, fix layout symmetry first. Do not immediately add a precision digital comparator.