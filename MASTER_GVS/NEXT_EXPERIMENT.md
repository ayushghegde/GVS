# Current Next Experiment — v14L5 Physical Quantal Release Closure

## Problem
v14L now has a capacitor-centered communication architecture that survives the model-level cascade, but the decisive nonlinear release device is still abstract. A plain passive capacitor was rejected because charge sharing cannot regenerate a same-threshold chain. The remaining question is whether a real two-terminal volatile release element can provide threshold/hold behavior, controlled leak and a fast low-energy firing event cheaply enough that the **whole QVC cell** beats transistor control.

## Goal
Close one physically credible QVC/VRS unit using the v14J extracted MIM capacitance floor and a real or literature-grounded volatile threshold compact model. Do not tune the network further until this device budget is tested.

## Physical target
Selected QVC model:
- Cmem = 18.69052 fF;
- rest bias = 0.60 V;
- fire threshold = 0.80 V;
- reset target = 0.15 V;
- leak tau target = ~100 ns;
- source firing edge = ~0.65 V;
- v14K WEAK/STRONG relation capacitors remain the communication links.

Candidate VRS classes:
1. chalcogenide ovonic threshold switch;
2. oxide volatile threshold switch;
3. solid-state ionic/filamentary volatile selector;
4. a small CMOS threshold/reset circuit only as the cost reference, not as the preferred semantic-core implementation.

Literal neurotransmitter/fluid chemistry is not a baseline candidate.

## Required experiments
1. Build/import a compact VRS model with explicit Vth, Vhold, Ron, Roff/leak, switching delay and cycle energy.
2. Connect it to the real v14J MIM capacitance proxies and the selected 6-WEAK + 1-STRONG fan-out load.
3. Run transient integration -> threshold -> release -> reset -> replenishment.
4. Sweep temperature/device variation enough to test idle false firing, missed firing and threshold drift.
5. Measure complete firing energy, including the VRS, leak, replenishment and capacitive fan-out.
6. Compare against transistor controls at 5/10/20 fF effective switched capacitance and 6 ns reference delay.
7. Check the physical target budgets: VRS <16.2/32.4/64.8 fJ for 5/10/20 fF energy break-even; for the 10 fF reference and a 5 fJ VRS, delay should be <=17.63 ns for equal EDP, with ~10 ns preferred.
8. Test whether WEAK/STRONG v14K links preserve the predicted packet amplitude after extracted parasitics are included.
9. Test the post-fire charge path into Local Venule -> Charge Artery -> regional reservoir without allowing recovery to alter correctness.
10. Count BEOL material/process area, thermal budget, selectors and routing before calling the device cheaper than CMOS.

## Acceptance
Promote v14L only if the **complete QVC/VRS cell and sparse network**, not the isolated switch, beats the transistor reference on useful firing reliability plus energy and preferably energy-delay product while preserving v14K structural learning.

If no VRS candidate closes the budget, keep v14L as a system concept, retain capacitive packet coupling, and reject the nonlinear-device implementation rather than hiding the cost in uncounted peripherals.
