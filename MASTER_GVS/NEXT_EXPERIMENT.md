# Current Next Experiment — v14M1 Physical Bimodal Junction Closure

## Goal
Determine whether one fabricated two-terminal diffusive junction stack can satisfy both v14M roles and beat the complete transistor reference at group level.

## Candidate stack
Start with the simplest CMOS-compatible family supported by current evidence:
- Ag or thin Ag-alloy active electrode;
- ultrathin ALD HfO2, optionally with one control/interfacial layer only if it materially improves speed/variation;
- Pt/TiN-class bottom electrode.

Do not add more layers merely to chase one metric.

## Required device evidence
1. Volatile low-current mode: threshold voltage, delay, off leakage, on current, self-relaxation, refractory time, cycle variation, endurance.
2. Nonvolatile mode on the same stack: reversible OFF/WEAK/STRONG states, retention, potentiation/depression, program energy, program failure.
3. Demonstrate clean separation between read/reason pulses and nonvolatile programming.
4. Quantify forming requirement; reject if forming/per-cell initialization becomes dominant.
5. Quantify current-compliance implementation. A hidden transistor/current-limiter per BDJ invalidates the transistor-elimination claim.
6. Measure/simulate fan-out through 3 STRONG + 2 WEAK links and background-only false firing.
7. Count shared bias rails, drivers, half-select/sneak paths, routing, and write peripherals.
8. Compare total group energy-delay and area/process complexity against 5 fF, 10 fF, and 20 fF CMOS-control references.

## Hard acceptance targets from v14M0
- preferred firing delay <=30 ns;
- absolute EDP break-even: <=38.5 ns versus 5 fF CMOS, <=62.3 ns versus 10 fF, <=97.3 ns versus 20 fF under the current energy proxy;
- no semantic-core MOS/compliance transistor per junction;
- at least 95% p05 eight-layer propagation at 20% link variation, or a demonstrated system-level trade that repays any extra redundancy;
- learning write energy must amortize under realistic continual-learning rates.

## If the exact same device cannot satisfy both regimes
Do not hide the failure. Compare:
A. one BDJ device type;
B. v14L capacitor + OTS two-device cell;
C. fixed MIM connection + separate OTS;
D. CMOS reference.
Keep the architecture that wins total system cost, not the one with the fewest named device types.
