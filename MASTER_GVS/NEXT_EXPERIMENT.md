# Current Next Experiment — v13L1b Integrated Grammar + Neurovascular Slice

## What v13L1a physically established
The geometry-only differential-service problem is now closed enough to choose a physical routing baseline.

Using real SKY130A Magic layout/DRC/extraction:
- deliberately one-sided parallel service routing was 0-DRC but electrically bad;
- parallel NERVE over GC extracted ~4.3095 fF to GC and no comparable NERVE->GR term at extractor resolution;
- orthogonal NERVE/ARTERY crossing extracted ~0.127589 fF to GC and ~0.127589 fF to GR for each service, giving zero reported differential asymmetry;
- an intervening metal3 shield with services on metal4 produced no direct service->GC/GR capacitance terms at extractor resolution;
- all three geometry variants were 0 DRC.

**Decision:** use orthogonal routing as the ordinary low-cost service baseline; use shielding when parallel run length/service density or extracted DSC is too high. Reject long one-sided parallel service routing near weak Grammar evidence even when DRC-clean.

## New term retained
**Differential Service Coupling (DSC):** unequal extracted coupling into Grammar candidate GC versus reference GR. Sign off both sides separately; do not rely only on one-node disturbance or total/common coupling.

## v13L1b goal
Attach the real selected Grammar path to the winning service geometry and close the first complete physical Neurovascular Cell Slice.

### Required physical elements
1. legal physical 10-MIM Grammar candidate/reference network;
2. selected body-tied 10-MOS dual-input-pair two-phase self-check reader;
3. orthogonal ~0.2 V Nerve as baseline;
4. separate low-voltage Charge Artery;
5. shielded variant retained as a comparison/protection option;
6. simple one-way recovery contact controlled only by existing cleanup/expiry lifecycle;
7. regional recovery branch or scaled reservoir equivalent;
8. robust/exact result capture independent of recovery.

## Physical placement rules from v13L1a
- keep GC/GR local and matched;
- no long one-sided parallel Nerve/Artery run beside only GC or only GR;
- ordinary crossing should be orthogonal where routing permits;
- if service must run parallel near weak evidence, interpose a real shield and extract it;
- measure C(NERVE,GC), C(NERVE,GR), C(ARTERY,GC), C(ARTERY,GR) separately;
- compute normalized DSC `(Ccand-Cref)/(Ccand+Cref)`;
- inspect added GC/GR absolute capacitance because common loading can slow the reader even when differential asymmetry is zero.

## Electrical battery
1. DRC = 0 and extracted connectivity correct;
2. full RC/capacitance extraction of MIM + reader + service geometry;
3. fresh motif replay into the physical candidate/reference network;
4. two-phase self-check using the selected 10-MOS reader;
5. TT/FF/SS exact + partial motifs;
6. independent MIM + MOS mismatch launches;
7. Nerve active alone;
8. Charge Artery active alone only after expiry;
9. Nerve + Charge Artery simultaneous;
10. aligned multi-service stress;
11. deliberately skew service placement to create DSC and verify side-bias rejection/fallback;
12. high-swing 0.9/1.2/1.8 V comparison line;
13. stuck-closed recovery fault -> energy loss only;
14. attempted live-state recovery -> blocked or fallback, never a wrong robust accept.

## Measurements
- GC/GR total capacitance after full integration;
- reader-side and service-side parasitic contributions;
- all four service-to-evidence coupling terms;
- normalized DSC;
- phase-0 / phase-1 outputs and physical-side preference;
- exact/partial robust margin;
- wrong accepts and fallbacks;
- readout energy;
- Nerve event energy;
- recovery voltage/energy;
- area overhead of orthogonal versus shielded service protection.

## Acceptance
v13L1b passes only if:
- zero wrong robust Grammar accepts across nominal PVT + preserved mismatch battery;
- the two phases preserve the logical result while reversing physical latch side;
- orthogonal low-swing service activity does not require a global quiet window;
- any deliberately excessive DSC becomes fallback before wrong acceptance;
- recovery never loads live information;
- exact fallback remains independent;
- shield use is justified only where it materially improves extracted margin, not added by default.

## After v13L1b
If this passes, promote the v13L DSC/orthogonal-or-shield service rule into `MAIN_ARCHITECTURE.md`, update `DECISION_LEDGER.md` and `EXPERIMENT_LINEAGE.md`, then stop studying isolated service wires and build a multi-primitive local intelligent region behind the eight-way Regional Event Lease.

If it fails, inspect added GC/GR loading and extracted asymmetry first. Do not revert to a fixed digital threshold or redesign Grammar solely to accommodate a poor service layout.
