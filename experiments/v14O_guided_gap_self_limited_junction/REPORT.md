# v14O Experiment Report — Guided-Gap Self-Limited Junction

## What happened
v14N's seeded device still depended on creating too much temporary filament from scratch. v14O moved most of the conducting path into a permanent inert spine and left only a small controlled Ag switching gap. A sharpened tip supplies local field concentration and a passive resistive neck supplies intrinsic current compliance.

## Experiments
1. **Dynamic-gap sweep:** shorter gaps improved delay but produced a rapidly rising relative leakage/spontaneous-bridge risk proxy. A straight ~1.15 nm gap reached ~14.3 ns mean but was not selected as the final geometry.
2. **Field-focus sweep:** a safer ~1.3 nm gap plus ~1.45x local field focus reached ~11.85 ns mean / ~14.81 ns p95 in the engineering model while keeping a lower relative short-gap hazard than the 1.2 nm reference.
3. **Ballast variation:** 2.2 Mohm nominal passive ballast with 20% variation and 50% ON-gap-resistance variation gave ~112.7 nA mean firing current, ~70.9 nA p01, ~172.3 nA p99. The same ballast reduces a 25 nS STRONG relation by only ~5.2%.
4. **Coincidence-programming screen:** the selected relation receives full differential stress while neighboring half-selected links receive read-level stress. Under the assumed lognormal dose-threshold model, full-vs-half-select separation is large; three corroborating evidence events drive the rare half-select proxy extremely low. These probabilities are model assumptions, not measured device rates.
5. **Eight-layer cascade:** the selected geometry preserves the v14M population behavior. At 20% learned-link variation, mean final activity is ~98.65% and p05 ~95.31%.
6. **64-hop physical transport:** with sparse regeneration, selected mean transport is ~108.5 ns at ~11.4 fJ in the proxy, compared with ~111.36 ns / ~261.44 fJ for the deliberately favorable CMOS repeater control.
7. **Relearning with physical write faults:** under an independent 5% physical program-failure assumption, three copies are useful (~98.6% changed-relation correctness in the run). Two copies are not automatically useful because a 2-of-2 majority makes programming failures worse; redundancy topology matters.

## Problem
The strongest remaining uncertainty is now fabrication/device physics rather than system architecture. We do not know whether one real stack can hold a ~1.3 nm effective dynamic gap with the required distribution, maintain an inert sharp spine, provide ~Mohm intrinsic ballast, remain volatile at low stress, become reversible nonvolatile at stronger stress, and survive endurance/retention requirements.

The spontaneous-bridge/leakage hazard in the model is only a relative sensitivity proxy. It cannot be converted into a real false-fire rate without measured or calibrated atomistic/compact-device data.

## Decision
KEEP v14O at model level. It materially fixes the v14N speed mechanism without adding an active device. Physical promotion requires a compact/experimental device model or fabrication data for the guided-gap structure. If the inert spine cannot be fabricated with adequate gap control, fall back to v14N seeded nano-islands rather than compensating with transistors.
