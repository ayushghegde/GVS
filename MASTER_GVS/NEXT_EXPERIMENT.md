# Current Next Experiment — v13R4 Physical Slow-Egress Closure

## Why v13R4 is next
v13R has reduced the new recovery/differentiation ideas to one remaining transistor-level question rather than another architecture rule.

### v13R0 — Slow Charge Egress model
After normal cleanup/expiry invalidates a cell state, residual charge is released through a weak path over several local event intervals instead of being dumped abruptly.

At the selected model screen `tau = 8` local event intervals:
- uniform expiry: peak Charge-Artery influx ~52.9% lower;
- bursty expiry: ~74.2% lower;
- aligned 128-cell stress: ~86.9% lower;
- modeled eventual transfer remains ~100% after sufficient drain time.

**Decision:** keep `cell -> weak post-expiry egress -> Charge Artery -> regional reservoir -> larger battery/collector`. The reservoir is retained as buffer, decoupler, surge absorber, isolation/fault boundary and staged-transfer element. `tau=8` is only a model screen; real RC/device timing must choose the physical value.

### v13R1 — Cell differentiation
A 64-cell differentiated region with 20 relay, 12 Grammar, 10 template, 8 binding/context, 8 constraint/competition, 2 exact-patch and 4 General Reserve Cells:
- removes ~81.25% of optional module copies versus universal full-feature cells;
- adds ~1.8456 cell hops per tested 2-5-stage mixed operation on average;
- ~0.277 fJ at the preserved 0.15 fJ/local-hop proxy;
- retained all tested module classes in 100% of 10,000 independent 10%-cell-failure trials.

**Decision:** every ECC does not need every optional module. Keep a small general reserve rather than either one universal cell everywhere or zero flexible cells.

### v13R2 — Differentiation granularity
Fine seven-type differentiation beats coarse four-type and universal cells while type-specific design/test/yield overhead remains moderate, but the model finds a finite break-even (~38 abstract penalty units per extra type for fine versus coarse).

**Decision:** build a compact reusable standard-cell family. Do not create unlimited one-off cell types.

### v13R3 — Real physical differentiated pair
Real SKY130A Magic geometry with two recovered NFETs:
- communication aperture: `NEIGHBOR <-> CELL`, gate `AP_GATE`;
- recovery candidate: `CELL <-> ARTERY`, gate `EXPIRE`;
- devices placed at opposite cell boundaries around weak GC/GR rails;
- 0 DRC;
- direct service-to-weak-rail coupling ~0.00403226 fF on the respective side;
- simple 72 fF screening proxy gives ~0.0112 mV for a 0.2 V neighbour event and ~0.00506 mV for a 0.0903 V artery swing.

**Decision:** physical differentiation does not require putting recovery hardware over the weak core. Keep communication and recovery apertures at cell/service boundaries.

## Tool constraint inherited from v13Q/v13R3
The supplied ngspice source builds revision 26 and cannot parse the current SKY130 combined model deck even on the PDK's own parser test. Therefore no TT/FF/SS aperture or recovery transient from that binary is accepted.

v13R4 must use a SKY130-compatible modern ngspice/simulator. If that simulator is not available, preserve the tool block; do not substitute a toy MOS model and call it physical closure.

## v13R4 goal
Physically close one differentiated two-cell slice with a deliberately weak, one-way post-expiry recovery device.

### Required elements
1. one relay/conduction ECC with communication aperture but no recovery tap unless its recovered-energy budget justifies one;
2. one stateful/Grammar-side ECC with local state/evidence and a Slow Charge Egress tap;
3. wall-mounted communication aperture;
4. wall/service-boundary post-expiry recovery device;
5. separate low-voltage Charge Artery;
6. real regional reservoir or scaled equivalent;
7. staged battery/collector load beyond the reservoir;
8. GC/GR weak-evidence geometry protected by the v13L orthogonal/matched rule;
9. robust output capture independent of recovery state.

## Recovery behavior to test
`live state -> useful computation -> cleanup/expiry -> weak one-way drain -> Charge Artery -> regional reservoir -> slower battery/collector transfer`

The recovery path must be inactive or sufficiently isolated while information is live.

## Electrical/physical battery
1. DRC = 0 and extracted connectivity correct;
2. communication aperture ON/OFF characterization;
3. post-expiry egress ON resistance / effective time constant;
4. OFF leakage while the cell is live;
5. residual cell charge versus time after expiry;
6. peak Charge-Artery current versus abrupt-drain baseline;
7. regional-reservoir ripple/occupancy;
8. battery/collector-side transfer smoothness;
9. reservoir-to-cell backflow stress;
10. attempted live-state recovery;
11. simultaneous communication event + SCE on neighboring/different cells;
12. GC/GR coupling and normalized DSC;
13. TT/FF/SS;
14. independent relevant device mismatch;
15. stuck-open and stuck-closed recovery faults;
16. communication/recovery energy;
17. area/parasitic comparison of differentiated relay + stateful cells versus two universal full-feature cells.

## Measurements
### Slow Charge Egress
- cell residual voltage/charge at 50/90/95/99% release points;
- effective physical tau/time constant;
- peak and RMS artery current;
- reservoir peak/ripple;
- collector/battery transfer current;
- recovered-energy fraction;
- charge retained too long for next useful cell activation.

### Correctness/isolation
- wrong robust accepts (must remain zero);
- live-state evidence disturbance;
- GC/GR differential service coupling;
- backflow into expired and live cells;
- recovery fault effect on computation result.

### Differentiation
- real area and extracted capacitance of relay versus stateful/recovery cell;
- omitted-device/module count;
- routing cost created by specialization;
- whether a recovery tap materially repays its device/parasitic cost for each cell class.

## Acceptance
v13R4 passes only if:
- zero wrong robust accepts in the tested battery;
- no normal recovery current loads a live information state enough to change its result;
- reservoir/battery voltage cannot back-drive the information cell during the tested states;
- Slow Charge Egress materially reduces peak artery/reservoir stress versus abrupt drain;
- the selected physical drain is not so slow that dead charge prevents useful reuse;
- the regional reservoir still provides buffering/decoupling/staged transfer and is not bypassed;
- a recovery-device fault may lose recovery energy but may not create a wrong robust computation;
- differentiated relay/stateful cells provide a material area/capacitance/lifetime-cost advantage over universal full-feature cells, or the library is coarsened;
- no per-cell recovery scheduler, ADC, calibration computer or microcontroller is introduced.

## If v13R4 passes
Promote the validated v13R rules into `MAIN_ARCHITECTURE.md`, then build **v13R5 Differentiated Tissue**: a multi-cell region containing real relay, Grammar/template/context/constraint roles, cell-as-wire communication, Population Confidence, and Slow Charge Egress taps only on the cell classes that earn them.

Replay mixed reasoning/locality/recovery traffic and compare total area, event energy, peak recovery disturbance, robustness and useful operations per hardware unit against an equivalent universal-cell region.

## If v13R4 fails
Classify the failure before changing architecture:
- excessive live-state leakage -> weaken/move/isolate recovery device;
- excessive backflow -> add the minimum one-way physical isolation justified by measurement;
- excessive retained dead charge -> speed the passive egress rather than adding a scheduler;
- recovery tap costs more than it recovers for a cell class -> remove it from that differentiated class;
- differentiation routing dominates -> merge/coarsen cell classes;
- weak-core asymmetry -> fix physical placement first, not Grammar.

The objective is minimum total lifetime cost with correctness, not maximum recovery or maximum specialization.
