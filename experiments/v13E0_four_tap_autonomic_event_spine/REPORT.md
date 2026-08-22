# Neural Glyph v13E0 — Four-Tap Autonomic Event Spine Closure

**Verdict: PASS for the current four-tap physical/electrical battery at a 0.9 V promoted-tap gate. The earlier 0.8 V point is rejected as insufficiently robust for four simultaneous taps under mismatch. Direct fourth-face routing remains the preferred true-neighbor path; the shared spine is selected for regional/fanout routing.**

## Terms

- **Autonomic Event Spine:** a protected regional wire carrying a robust local event to several self-configured taps rather than broadcasting fragile analog evidence.
- **Promoted tap:** a local pass device whose configuration state has earned a persistent/slow enable from repeated validated use.
- **Source-work proxy:** source charge integrated over the charging/hold interval multiplied by the source voltage; it is a comparison proxy, not total region energy.

## 1. Physical routing slice

A shielded ~180 um spine with four isolated local branches was used. An earlier layout accidentally connected the branches directly to the spine; extraction caught the error and that topology was rejected.

Corrected routing properties used in the closure bench:

- protected spine effective load: ~11.26 fF;
- each branch output includes ~4.8 fF local physical/receiver loading in the transistor bench;
- branch-to-protected weak-evidence coupling proxy: ~0.124 fF;
- protected weak evidence state: ~72 fF;
- resulting 0.2 V branch event produces only ~0.344 mV disturbance on the protected weak state.

This preserves the v13C rule: robust event/control may use the service spine while millivolt-class evidence stays behind shielding.

## 2. Promoted-gate sweep

A minimum SKY130 NFET W=0.42/L=0.15 transfers a 0.2 V local event. Nominally, ~0.8 V gate looks nearly full-strength, but mismatch exposed insufficient four-tap headroom.

A TT/FF/SS mismatch sweep with seeds 101/202/303/404 found the global minimum four-active output approximately:

- 0.80 V gate: ~0.18835 V;
- 0.82 V: ~0.19603 V;
- 0.85 V: ~0.19722 V;
- 0.88 V: ~0.19960 V;
- **0.90 V: ~0.1999991 V**;
- 0.95 V: ~0.1999998 V;
- 1.00 V: ~0.1999999 V.

**Decision: select 0.9 V as the first conservative promoted-tap operating point for the present 0.2 V event-spine topology.**

The old 0.8 V recommendation is superseded for four-active mismatch operation.

## 3. Final 0.9 V mismatch battery

Full battery:

- TT mismatch: seeds 101/202/303/404;
- FF mismatch: seeds 101/202/303/404;
- SS/85 C mismatch: seeds 101/202/303/404.

Result: **12/12 PASS**.

Across the final combined battery:

- the selected one-tap output remains essentially 0.2 V;
- inactive taps remain microvolt-class;
- all four simultaneously selected outputs remain essentially full 0.2 V;
- the weakest four-active output is ~0.199998 V class;
- protected-evidence kick remains ~0.344 mV.

This is a small mismatch screen, not fabrication-yield signoff.

## 4. Nominal event-source work at 0.9 V

Charge/hold source-work proxy, 0-100 ns integration interval:

| Corner | shared spine, one tap | shared spine, four taps | direct fourth-face neighbor |
|---|---:|---:|---:|
| TT | ~0.6728 fJ | ~1.3400 fJ | ~0.1505 fJ |
| FF | ~0.6745 fJ | ~1.3467 fJ | ~0.1522 fJ |
| SS | ~0.6714 fJ | ~1.3344 fJ | ~0.1489 fJ |

The direct fourth face is therefore roughly 4.4x cheaper than the full shared spine for one true neighboring destination in this event-source comparison.

**Decision: do not replace direct neighbor fourth-face links with the regional spine.**

The shared spine earns its place when it replaces longer/repeated regional routing, supports fanout, or provides post-fabrication reconfigurability.

## 5. Tap configuration cost

A nominal full-PDK gate ramp to 0.9 V gives a one-time/slow promotion work proxy:

- TT: ~0.333 fJ;
- FF: ~0.353 fJ;
- SS: ~0.316 fJ.

This is not paid per event when a promoted tap remains static over a burst. Static promotion is therefore essential to the event-spine energy argument.

## 6. Recovery

The prior post-capture recovery bench at the earlier 0.8 V gate point showed the correct sequencing principle: do not touch the configuration charge while the event is live; after capture, a one-way recovery rail can accept part of the expired state without disturbing the event. That special bench recovered roughly 53% of removed gate-state energy.

The recovery fraction has not yet been re-signed at 0.9 V, so v13E keeps the **principle** but does not copy the old percentage onto the selected 0.9 V point.

## 7. Architectural decision

Selected routing hierarchy after physical closure:

1. **direct fourth face** — true neighboring weak-analog or event link; lowest load/energy;
2. **short segmented analog tap** — nearby non-neighbor weak analog relation with only a small active segment;
3. **0.2 V protected Autonomic Event Spine** — regional/fanout route with promoted static taps;
4. **Myelin chord** — stable hot long-range direct relation;
5. **exact/global fabric** — cold, changing, exact, or ambiguous relation.

Do not distribute raw ~25 mV analog Grammar evidence over the whole regional trunk. Carry a robust event and recreate local analog evidence at the destination.

## 8. Closure

v13E0 is closed for the defined four-tap battery:

`shielded physical spine -> isolated branches -> minimum tap NFETs -> promoted-gate sweep -> TT/FF/SS -> 12 mismatch launches -> crosstalk -> nominal source-work -> fourth-face comparison`

Next work moves to the hollow/framework volume itself: test whether the empty interior can become a useful communication medium, especially with light, without displacing the electrical mechanisms that already win locally.
