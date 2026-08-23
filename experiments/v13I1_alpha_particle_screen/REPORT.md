# Neural Glyph v13I1 — Alpha-Particle Carrier / Fault Screen

**Verdict: REJECT as a runtime communication/computation carrier. KEEP only as a radiation-fault model / future robustness test category.**

This report is intentionally high-level and safety-focused. It does not specify radioactive sources, handling, shielding procedures, or experimental setup.

## 1. Why test the idea at all

The hollow volume invites the question whether a particle could travel directly from one region to another and deposit charge at a destination. Alpha particles are charged helium nuclei and can create a very large charge pulse in semiconductor detectors.

The same property that makes them easy to detect makes them a poor normal GVS signal.

## 2. Energy scale

A representative 5 MeV alpha particle carries approximately:

`5e6 eV * 1.602e-19 J/eV ~= 8.01e-13 J ~= 0.801 pJ ~= 801 fJ`

Compare current GVS runtime proxies:
- direct fourth face ~0.15 fJ/event;
- 180 um electrical event spine ~0.67-1.34 fJ/event;
- 10 mm dedicated electrical route ~37.55 fJ/event;
- modeled 10 mm thin-TIR/direct-photocharge optical runtime ~10.96 fJ/event.

Even one representative alpha particle therefore carries ~21x the energy of the 10 mm electrical event and ~73x the modeled optical runtime event before including any particle-generation/detection overhead.

## 3. Charge deposition is far too large for tiny Glyph receptors

Silicon requires roughly 3.6 eV per generated electron-hole pair as a standard detector rule-of-thumb. If 5 MeV were fully deposited in silicon, the ideal count is roughly:

`5e6 / 3.6 ~= 1.39 million electron-hole pairs`

corresponding to about `2.2e-13 C` of generated charge before recombination/collection effects.

A 3 fF GVS receptor needs only:

`Q = C*V = 3 fF * 0.2 V = 6e-16 C`

for a full 0.2 V event, or only about 3.7 thousand electrons.

The alpha-induced charge scale is hundreds of times larger than the intended receptor event. Real devices would clamp/saturate rather than reaching the impossible ideal `Q/C` voltage.

**Decision:** alpha charge is not a naturally matched analog signal for the present low-charge architecture.

## 4. Range / routing problem

Authoritative radiation references show that alpha particles have short ranges in semiconductor material. Silicon alpha spectrometers use thin sensitive regions, and an IAEA example gives ~18 um range for a ~5.5 MeV alpha in SiC. NIST ASTAR provides stopping-power/range tables for helium ions.

This is the opposite of what GVS needs for an internal multi-millimeter reliable carrier: transparent, low-loss, repeatable routing with low endpoint disturbance.

## 5. Reliability problem

NASA/JPL radiation literature uses alpha particles specifically to study single-event upsets in CMOS latches and memories. A sufficiently large collected ionization charge can flip stored circuit state.

GVS contains many deliberately tiny high-impedance charge nodes, so introducing an ionizing particle carrier would create a new false-event and corruption mechanism near the very nodes that are intended to save energy.

## 6. Architecture consequence

Do not create an alpha-particle communication layer.

Instead, add a **Radiation Quarantine Rule** to the existing physical-safety policy:

- one uncorrelated physical transient cannot train a persistent route;
- raw activity cannot refresh the Regional Lease;
- persistent fourth-face/Myelin/optical promotion still requires repeated validated success;
- low-margin decisions retain two-phase/reference checking or exact fallback;
- a suspicious isolated high-amplitude event should be treated as invalid/noise unless normal source/timing/context validation confirms it.

This reuses the existing v12/v13 rule that noise cannot become structure.

## 7. Decision

### REJECT
- alpha particles for data routing;
- alpha particles for analog weighting;
- alpha particles as an energy-recovery mechanism;
- alpha particles as a substitute for optical diagonal paths.

### KEEP conceptually
- radiation-induced transient/upset as a future fault-injection/robustness class;
- architectural immunity through validation, non-training of raw events, reference/self-check and exact fallback.

The practical radioactive-source side is outside the GVS architecture and is not required for continuing the design.
