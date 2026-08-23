# Current Next Experiment — v13L1 Physical Differential Neurovascular Slice

## What changed in v13L0
v13L0 did not replace the v13K architecture. It refined the physical signoff question.

The selected Grammar path is a differential 10-MIM candidate/reference structure feeding the physically selected 10-MOS two-phase self-check reader. Therefore service disturbance must be measured on **both** evidence sides.

**Differential Service Coupling (DSC):** unequal Nerve/Charge-Artery coupling into candidate versus reference; common-mode coupling is less dangerous than unequal coupling because the Grammar decision depends on their difference.

v13L0 reused the conservative v13K values:
- weak node ~72 fF per side;
- useful differential ~25 mV;
- high-margin target ~18 mV;
- average service coupling reference ~0.124 fF;
- Nerve swing ~0.200 V;
- Charge-Artery swing ~0.0903 V.

Worst-direction deterministic stress found:
- at 1x average coupling, 8 Nerve + 32 Artery aligned transitions retain the 18 mV target until normalized candidate/reference coupling asymmetry exceeds ~45.3%;
- at 2x average coupling, the same stress allows ~22.6% asymmetry;
- at 2x coupling with 32 Nerve + 32 Artery aligned transitions, tolerance falls to ~10.9%.

**Decision:** low-swing neurovascular separation remains worth physicalizing, but v13L1 must sign off extracted differential coupling, not only absolute coupling into one weak node. No new scheduler, ADC, calibration loop or per-cell controller is added.

## v13L1 physical goal
Build the first same-die electrical **Differential Neurovascular Cell Slice** around the selected robust Grammar path.

### Required physical/electrical elements
1. real legal 10-MIM Grammar candidate/reference structure;
2. selected body-tied 10-MOS dual-input-pair two-phase self-check reader;
3. direct fourth-face path or ~0.2 V local Nerve;
4. separate low-voltage Charge Artery;
5. simple one-way recovery contact driven by the existing cleanup/expired-state lifecycle signal;
6. regional recovery branch / scaled reservoir equivalent;
7. shield/service-face geometry between weak pair, Nerve and Charge Artery;
8. at least two deliberately asymmetric service-placement variants so candidate/reference coupling imbalance is actually tested;
9. exact/robust result capture independent of recovery.

### Physical extraction measurements
For Nerve and Charge Artery separately measure:
- coupling to Grammar candidate side;
- coupling to Grammar reference side;
- average coupling;
- differential coupling;
- normalized asymmetry `(Ccand-Cref)/(Ccand+Cref)`;
- local RC and added weak-node capacitance.

Do not call a layout safe merely because each absolute coupling term looks small.

### Electrical battery
1. DRC and extracted connectivity first;
2. nominal TT/FF/SS;
3. independent MIM + MOS mismatch launches;
4. exact and partial Grammar motifs;
5. Nerve active alone;
6. Charge Artery active alone only after expiry;
7. Nerve + Charge Artery simultaneous;
8. aligned multi-line low-voltage service stress;
9. candidate-side-near service placement;
10. reference-side-near service placement;
11. swap physical orientation and repeat the two-phase self-check;
12. deliberately inject 0.9/1.2/1.8 V high-swing facade-equivalent activity for comparison;
13. verify unsafe high-swing/asymmetric disturbance becomes fallback before any wrong robust acceptance;
14. stuck-closed recovery contact -> efficiency/energy failure only, never wrong computation;
15. attempted live-state recovery -> topologically blocked or safely rejected/fallback.

### Measurements
- exact/partial margin before and during service activity;
- phase-0 and phase-1 logical consistency;
- physical-side preference count;
- false robust-result count;
- fallback count;
- regional recovery voltage and recovered/stored-energy change;
- Nerve event energy;
- added area/parasitic load versus direct fourth-face baseline;
- differential-coupling budget versus the v13L0 model.

## Hollow / inside-out mapping screen
Keep this separate from SKY130 electrical signoff.

Map the verified planar slice onto the practical hollow interpretation:
- protected weak/local computation skin;
- matched/shielded Nerve + Charge-Artery framework paths;
- robust high-swing facade/backside services farther from weak evidence;
- passive Thermal Capillary paths toward shared collectors;
- optional optical routes only after distance/reuse/source-idle break-even.

Literal active inner cavity walls remain FUTURE_PROCESS until a credible fabrication stack exists.

## Acceptance
v13L1 passes only if:
- zero wrong robust Grammar accepts across nominal PVT + the preserved mismatch battery;
- normal low-swing Nerve/Charge-Artery activity does not require a global quiet window;
- extracted differential service coupling stays within measured margin or causes safe fallback;
- the two-phase reader catches deliberately induced physical-side preference;
- recovery cannot load a live information node;
- exact fallback stays independent of Nerve/recovery state;
- direct neighbor remains cheaper/simpler than unnecessary spine traversal;
- high-swing exceptional utilities remain sufficiently isolated or fail safely.

## After v13L1
If v13L1 physically passes, promote the DSC geometry/signoff rule into `MAIN_ARCHITECTURE.md`, update the decision ledger/lineage, then build a multi-primitive local region behind the eight-way Regional Event Lease. If it fails, inspect extracted asymmetry and weak-node loading before changing Grammar or adding control logic.
