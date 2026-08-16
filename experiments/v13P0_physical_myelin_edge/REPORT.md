# GVS v13P0 — Connected Physical Myelin Edge

**Status: PARTIAL PASS**

## What happened

The v12S programmable Myelin edge was laid out as a real SKY130A structure without changing its circuit architecture:

- 2.00 um x 2.00 um `sky130_fd_pr__cap_mim_m3_1` MIM capacitor;
- 0.42 um / 0.15 um `sky130_fd_pr__nfet_01v8` switch;
- legal source, drain and gate contacts;
- M4 -> M3 -> M2 -> M1 access stack;
- named `G0`, `MX0`, `Q`, and `H0` ports.

The first connected draft had 21 DRC violations around the gate-contact landing. Those were layout/contact-enclosure problems, not an observed failure of the GVS architecture. The gate landing was moved away from diffusion and given a wider poly dogbone plus legal LI/M1 enclosure.

The resulting `myelin_edge0_v2.mag` has **0 DRC errors**.

Magic extraction recognizes exactly the intended devices:

- `sky130_fd_pr__cap_mim_m3_1`, w=2.00 um, l=2.00 um;
- `sky130_fd_pr__nfet_01v8`, w=0.42 um, l=0.15 um.

## Extracted parasitics

Magic capacitance values are converted from attofarads to femtofarads.

Node-to-substrate capacitance:

- G0: 1.279300 fF
- MX0: 0.707921 fF
- Q: 0.403547 fF
- H0: 0.319232 fF

Inter-node coupling:

- MX0 <-> G0: 0.397983 fF
- MX0 <-> Q: 0.009880 fF
- Q <-> G0: 0.005022 fF
- H0 <-> MX0: 0.033136 fF
- H0 <-> Q: 0.006655 fF

Magic extresist reports resistance in milliohms. The useful end-to-end values are approximately:

- MIM top plate to NFET source: 261.854 mOhm = 0.261854 ohm;
- NFET drain to H0 route port: 247.529 mOhm = 0.247529 ohm.

These interconnect resistances are much smaller than the transistor's electrical impedance and are not presently the dominant risk.

## Comparison with the fixed v12S stress battery

The historical v12S moderate parasitic profile deliberately added +3 fF to each 10 fF local dendrite, +20 fF to the shared run node, and +20 fF to capture. It passed TT/FF/SS and mismatch screens.

The physically extracted H0 capacitance of this single connected edge is about 0.319 fF, with only about 0.040 fF combined explicit coupling from H0 to MX0/Q. The measured connected-edge parasitics are therefore below the prior +3 fF local-dendrite stress envelope.

This comparison is evidence that the current physical edge is not obviously outside the v12S robustness envelope. It is **not** yet a replacement for rerunning the complete v12S transient lifecycle with the extracted network.

## Current problem

A complete extracted-layout transient rerun is still missing. The edge itself is now physically valid, but the acceptance battery must be rerun after replacing the schematic `XMY0 + XMYS0` pair with the extracted-RC equivalent in the unchanged v12S lifecycle.

The experiment therefore remains PARTIAL PASS rather than being promoted to a full physical validation.

## What is next

1. Insert `extracted_rc_overlay.spice` for route 0 into an unchanged v12S lifecycle copy.
2. Repeat the same physical edge for route 1/template paths or mirror the verified geometry where symmetry is exact.
3. Run TT/FF/SS and mismatch lifecycle tests.
4. Check dendritic margin, one-hot route capture, output correctness, recovery and invalidation against the existing v12S acceptance battery.
5. Only redesign a local physical structure if the extracted simulation exposes a measured failure.

No GVS architecture change is justified by v13P0 so far.
