# Neural Glyph v15E — Charge-Captured Dendrites + Luminous Need Plane

**Status: MODEL PASS — CHARGE CAPTURE SUPPORTED; OPTICAL NEED PLANE PASSES CURRENT ROUTING MODEL; PHYSICAL COMPOUND DEVICE/PACKAGE COUPONS STILL REQUIRED.**

## What happened
v15E first closed the narrow v15D question: whether one guided-gap event can leave a useful signed charge packet for microsecond-scale natural forgetting. It then tested the user's cross-chip "emitter screen" idea as a sparse internal optical need/response plane.

The first optical implementation failed because one bright destination pixel produced a ~2.8% false-wake rate under package crosstalk variation. That version was rejected. The improved design uses a 2-of-3 spatial destination signature and a modest dark-zone optical isolation requirement.

## v15D charge-capture closure
### Actual ngspice transient
The existing guided gap was modeled as the volatile sample switch. A ~0.23 V local event charges the existing 24 aF dendrite/HZO node. When the gap resets OFF, the node is isolated and decays through the OFF gap plus natural collar leakage.

Measured by ngspice:
- captured voltage: **0.229992 V**;
- corresponding charge at 24 aF: **34.45 electrons**;
- 100 ns: **0.221221 V**;
- 1 us: **0.155892 V**;
- 5 us: **0.032904 V**;
- 10 us: **0.004708 V**.

### 500,000-trial variation model
The event voltage is derived from varied guided-gap current × ON resistance and capped at the inherited local inference envelope; node C, OFF resistance and leakage all vary.

Result:
- median initial capture: **33.32 electrons**;
- p1: **16.10 electrons**;
- p99: **45.79 electrons**;
- capture >=15 electrons: **99.4514%**;
- initial 15–45 electron band: **97.9352%**;
- median decay time constant: **2.535 us**;
- after 1 us, >=5 electrons remain: **99.8706%**;
- after 5 us, >=5 electrons remain: **43.8516%**.

Therefore the old fixed 22.5-electron assumption is rejected. The selected design uses event-derived Q=C*V; the correct target is "tens of electrons," with natural microsecond forgetting.

This is still circuit/device modeling, not a fabricated compound-device measurement.

## Luminous Need Plane — first failure
A single spatial route pixel was tested over 16 specialist receivers. Under emitter, coupling, detector, shot-noise and crosstalk variation, false wakes were ~2.8%. The design was rejected.

## Improved optical route code
Each specialist has a three-pixel spatial signature. A receiver wakes only if at least two of those three separated pixels cross threshold.

1,000,000-trial photon-statistics model:
- correct wake: **99.9993%**;
- miss rate: **0.0001%**;
- false-wake rate: **0.0006%**;
- target photoelectron median per route pixel: **479**;
- wrong-zone maximum median: **16**;
- route threshold: **45 photoelectrons/pixel**.

The model assumes median wrong-zone coupling <=1.5e-4. That number was separately checked with a scalar diffraction geometry model.

## Optical geometry check
A 500,000-sample scalar Airy-field model used roughly 590 nm wavelength, 20 um optical aperture, 2 mm inter-plane distance, 305 um receiver pitch, aperture/distance/alignment variation, and only 2x stray-light reduction from a dark isolation zone.

Median post-isolation adjacent intensity ratio: **1.45e-4**. This is not FDTD and excludes package scattering/multi-reflection; a physical package coupon remains required.

## Direct light-to-energy activation — actual ngspice
A conservative received photocurrent pulse (0.2 uA for ~5 ns) charges a 2 fF need node. That node directly controls a shared package power gate.

ngspice:
- detector-node peak: **0.4986 V**;
- specialist load peak: **0.7960 V** from a 0.8 V shared source;
- gate-on interval: **45.1 ns**.

## Problem remaining
v15E has two prototype questions: reproduce the event-derived tens-of-electrons capture/microsecond leakage in the compound device, and verify the package optical crosstalk/energy on a real need-plane coupon.
