# Do Not Reinvent These Problems

Search the source history before reopening any item below.

## Solved or substantially solved mechanisms
- selective persistence reset: v11N
- real SKY130 legal reset fingering: v11O
- stale-route confirmed falling-edge clear: v11P
- membrane capacitor scaling direction: v11Q
- MOS weak-leak physical direction: v11R
- stored leak-charge negative feedback concept: v11S
- regional/shared adaptation idea: v11T-U / v11X / v12A-C
- one-way shared energy recovery concept: v11V-W
- electrical row/column firing memory: v12D
- recency/repetition/confidence from firing charge: v12E
- routerless competition/fatigue: v12F
- context-dependent routerless reasoning: v12G
- shared inhibitory ambiguity detection: v12H
- charge-recycled exact ambiguity fallback: v12I
- upstream source gating of wrong evidence: v12J
- stable capacitive ternary synapse + exact fallback: v12K
- template promotion + exact residual: v12L
- static binary selector tree; one-hot/naive decoder rejected: v12M
- Grammar/escalation for local patterns; analog exact ALU rejected: v12N
- autonomous representation/compiler layer: v12O
- physical lease/speculative exact fallback: v12P
- Myelin execution paths and mini complete-system usage: v12Q
- passive/full-swing Myelin hardware: v12R
- integrated autonomous tile lifecycle, self-locking/self-clearing Myelin, invalidation/fallback/recovery: v12S
- real Myelin edge layout/extraction and short-range crosstalk: v13P0-P2
- shared-spine/terminal physical loading measurements: v13P3-P4
- inter-tile orthogonal event-fabric direction and coordinate selection: v13 physical GTI/receiver experiments
- physical 16x16 event-grid scaling: v13P10
- full-lifecycle selection-interface integration screen: v13P11
- four-tile regional shared recovery: v13P12
- physical-cost-aware locality compiler: v13A

## Known false starts / rejected ideas
- clear memory on every sharp falling edge: damaged severe-noise operation (v11P)
- 22/33 pF membranes: too aggressive across mismatch; 44/66 pF had extreme-corner failure (v11Q)
- fixed weak-leak bias across PVT: failed SS/hot (v11R)
- always-active leak-storage feedback: too sticky during normal activity (v11S)
- too-small shared recovery rail in v11V: changed firing
- passive pooled inhibition: too weak (v12H)
- direct 10 mV context shunt/regenerative latch for exact tie: rejected (v12H)
- analog neural exact arithmetic: rejected (v12N)
- one-hot template selector: little energy benefit, excessive configuration bits (v12M)
- naive binary decoder selector: more devices/energy (v12M)
- sharing sensory sources without isolation in sound selector: pJ-range contention (v12M)
- forcing Grammar processing onto all vision: accuracy loss (v12N)
- MOS varactor as stable capacitive synapse: weaker/nonlinear (v12K)
- HVT varactor recovery reservoir: dense but unstable/nonlinear full-tile FF simulation; rejected for now (v13P12 follow-on)
- naive global per-event long-fabric communication: can erase hybrid advantage (v13A)
- dynamic-config selector sharing as normal mode: saves area but loses static-tree event-energy advantage; area-constrained option only (v13A)

## Important correction
Do not treat v12S local `run/capture` as a millimeter-scale global bus problem. Those local analog control nodes were already solved and stress-tested. Long-distance scaling should happen around local tiles/regions, not by stretching their sensitive internal nodes globally.
