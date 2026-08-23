# Neural Glyph v13K1 — Low-Swing Charge-Artery Disturbance Screen

**Verdict: PASS at model/proxy level. Separating recovery into a low-swing artery removes most of the reason for the heavy Facade Quiet Window around recovery traffic. High-swing power/configuration still stays in the robust outer service layer.**

## Problem
v13J3 showed that a shielded but high-swing facade line can still disturb a ~72 fF weak evidence node. Using the conservative existing protected-branch coupling proxy ~0.124 fF:
- 0.9 V transition -> ~1.55 mV kick;
- 1.2 V -> ~2.06 mV;
- 1.8 V -> ~3.09 mV.
Several aligned transitions can eat the ~25 mV useful separation.

## v13K change
Do not use the high-swing facade as the normal recovery artery. Give each cell/group a dedicated **low-voltage Charge Artery** whose voltage follows the regional recovery system.

The preserved v13P12 regional reservoir example moved roughly 0.1990 V -> 0.2893 V in the quoted recovery interval, only about **90.3 mV of actual recovery swing**.

## Disturbance model
Use:
- weak evidence capacitance ~72 fF;
- useful differential ~25 mV;
- high-margin target ~18 mV;
- conservative coupling per artery/utility ~0.124 fF.

Estimated one-line kick:
- 90.3 mV recovery swing -> **~0.155 mV**;
- 0.2 V nerve event -> ~0.344 mV;
- 0.3 V service swing -> ~0.516 mV;
- 0.5 V -> ~0.860 mV;
- 0.9 V -> ~1.55 mV;
- 1.8 V -> ~3.09 mV.

At the actual ~90.3 mV recovery swing, about **45 perfectly aligned equivalent transitions** would be required to reduce 25 mV to the 18 mV high-margin screen in this first-order model.

Even 32 aligned 90.3 mV artery transitions leave roughly **20.0 mV** of the original 25 mV differential.

This is intentionally conservative because it reuses the previous coupling proxy rather than assuming the new physical separation magically creates lower coupling.

## Consequence
For the Charge Artery itself, v13K can simplify v13J's timing rules:

Old tendency:
`weak analog active -> freeze facade recovery -> capture -> recover`.

New selected tendency:
`live information isolated from recovery valve; expired low-voltage charge may flow on its dedicated artery without requiring global facade silence`.

The fundamental rule remains: a live high-impedance information node cannot be connected to recovery. But the **network no longer needs a global quiet-window scheduler for ordinary low-voltage recovery movement**.

High-swing VDD/config/test lines remain physically separated on robust service layers and may still need shielding/staggering if their measured coupling is large.

## Direct nerve coexistence
The normal regional Nerve is ~0.2 V. At the same conservative coupling, eight unrelated aligned 0.2 V transitions would leave about **22.25 mV** of a 25 mV weak differential. This gives much more coexistence headroom than 0.9–1.8 V utility traffic.

## Status
This is not a new physical PEX. It is a new system/circuit screen using previously extracted capacitance and previously measured/modelled voltage classes. The physical v13K target must lay out a Nerve + Charge Artery + weak node together and extract their real coupling.

## Selected rule
**Solve disturbance by voltage/domain/geometry separation first; use timing rules only for residual measured conflicts.**
