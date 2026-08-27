# Neural Glyph v13S2 — Shared Venule Physical Geometry

**Verdict: PHYSICAL GEOMETRY PASS; slow-transient closure open.** A shared eight-cell venule and one real SKY130 NFET outlet can be placed at the cell boundary without adding reported direct coupling into the preserved weak GC/GR pair.

## Physical construction
Magic 8.3.681 with the repository SKY130A technology (`1.0.602-0-gf3c505b`). The weak pair reuses the selected reader terminal geometry. The slow outlet instantiates the recovered `nf_reset` SKY130 NFET geometry from the preserved v13A6 recovery baseline.

Two placements were extracted:
1. deliberately near the weak pair;
2. cell-boundary placement far below the weak pair.

Both are **0 DRC** and extract the intended `VENULE -> NFET source`, `ARTERY -> drain`, `SLOW_GATE -> gate` connectivity.

## Coupling result
Near placement:
- VENULE -> GC: **0.00604839 fF**;
- VENULE -> GR: **0.00604839 fF**;
- normalized differential asymmetry: 0 at extractor precision;
- using the preserved 72 fF screening node and 0.0903 V recovery swing, simple common-mode kick proxy is ~**0.0076 mV per side**.

Boundary placement:
- no direct VENULE/ARTERY -> GC/GR capacitance term is reported in the extracted file at Magic's reporting precision;
- GC-GR remains 0.040625 fF in this geometry proxy.

## Decision
The slow shared venule/outlet belongs at the **cell boundary**, the same anatomy rule learned for v13Q communication apertures. Do not route the shared recovery line through the weak differential core merely because the near placement is symmetric.

No shield is required by this geometry precheck because boundary separation already removes the direct term. Add a shield only if denser future placement extraction demonstrates a need.

## What this does not prove
- slow outlet ON current or time constant;
- OFF leakage/backflow;
- TT/FF/SS/mismatch;
- real reservoir capacitance sizing;
- absolute recovered energy.

The supplied ngspice revision 26 is too old for the current SKY130 combined model deck. The current official ngspice release is newer, but this runtime could not transfer the external archive into the local sandbox; no toy MOS model is substituted.
