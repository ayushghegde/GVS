# GVS v13P1 — Two-Edge Physical Crosstalk

**Status: PASS for the measured physical question; overall extracted-tile validation remains open.**

## What happened

Two copies of the DRC-clean v13P0 physical Myelin edge were placed on a 4.5 um vertical pitch. The second edge is an exact geometric translation of the first; no circuit/device dimensions were changed.

Each edge contains:

- one 2.00 um x 2.00 um SKY130 MIM capacitor;
- one 0.42 um / 0.15 um SKY130 NFET;
- legal source/drain/gate contacts;
- M4 -> M3 -> M2 -> M1 routing;
- independent G/MX/H/Q labels for extraction.

The pair passed Magic DRC with **0 errors** and extracted as two intended MIM devices plus two intended NFET devices.

## Measured inter-edge coupling

Magic capacitance output is converted from attofarads to femtofarads.

- G0 <-> G1: 0.112633 fF
- MX0 <-> MX1: 0.060883 fF
- H0 <-> H1: 0.0170647 fF
- Q0 <-> Q1: 0.00534327 fF

Additional mixed cross-edge terms were smaller:

- G1 <-> MX0: 0.00346465 fF
- MX1 <-> G0: 0.00346465 fF
- H1 <-> Q0: 0.000422403 fF
- MX1 <-> Q0: 0.000254 fF

The largest measured neighbor coupling is therefore about **0.113 fF**.

## Interpretation against v12S

The fixed v12S moderate stress profile added +3 fF to each local dendrite and still passed its electrical acceptance battery. The measured 4.5 um-pitch edge-to-edge coupling is more than an order of magnitude below 3 fF, including the H0/H1 coupling that is most directly relevant to competing local dendrites.

This does not prove a complete dense tile will have negligible crosstalk, because larger shared buses and many-neighbor accumulation are not represented by a two-edge pair. It does show that two adjacent physical Myelin slots at this pitch do not create an immediate coupling problem.

## Problem

The unresolved physical risk has moved upward in hierarchy: single-edge RC and nearest-neighbor Myelin coupling are now small. The next meaningful physical risks are shared-node loading (especially run/capture), accumulation from several neighboring edges, and the complete extracted lifecycle.

## What is next

1. Build a small multi-edge cluster around a shared local dendrite/shared-control geometry rather than isolated pairs.
2. Extract cumulative loading on H/run/capture-like nodes.
3. Compare those values to the v12S +3 fF / +20 fF / +20 fF stress envelope.
4. Only if cumulative extraction approaches or exceeds that envelope, run focused physical redesign/spacing experiments.
5. Continue toward the unchanged v12S full extracted transient battery.

No GVS architecture change is supported by v13P1.

## Provenance

- Branch: `experiment/v13P0-physical-rc`
- Magic: 8.3.681
- PDK: supplied SKY130A Magic technology
- Base layout: v13P0 `myelin_edge0_v2.mag`
- Pair pitch: 4.5 um in Y
- Generated pair layout SHA-256: `44d168e3fcd31e6187f171bc5090cb73933a3093b6b2c743220dc98d545623a7`
- Generated capacitance extraction SHA-256: `f77bb9239d7f701b670d86df7bd4762773ec4160c234509169ca90f6ac5ea5bc`
- Generated resistance extraction SHA-256: `6209d10b49edaa0fb523c7759e7221b150a54104c41f59f17a84175dd0a44b3b`
