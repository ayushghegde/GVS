# Neural Glyph v13O0 — Constraint Membrane Reasoning

**Verdict: MODEL PASS / PHYSICAL PRESSURE-CELL OPEN.**

## New terms
- **Constraint Membrane Fabric (CMF):** recurrent local state cells whose physical relations continuously push violated constraints toward satisfaction instead of executing a central search program.
- **Constraint Pressure:** persistent local analog state representing how long/strongly a relation has remained violated.
- **Pressure Pulse:** a regional analog escape event triggered by accumulated violation pressure; it weakens stuck states so local constraints can settle again, without an exact solver choosing the new assignment.
- **Parallel Attractor Colony (PAC):** several cheap copies of the same fabric using different initial charge states; the first valid attractor wins.

## What happened
Held-out planted satisfiable 3-SAT instances near 4.2 clauses/variable were solved using only local recurrence. Parameters were chosen on separate exploratory seeds; reported evaluation uses 50 held-out instances per size.

The plain recurrent mesh increasingly locks into bad attractors as problem size grows. Reusing GVS-style fatigue/homeostasis plus persistent constraint pressure materially improves escape without inserting a CPU search loop.

| variables | plain single-fabric | adaptive single-fabric |
|---:|---:|---:|
|16|66%|94%|
|24|44%|82%|
|32|32%|84%|
|48|14%|66%|
|64|8%|62%|

On the 64-variable/269-clause case, a pressure-pulse variant reached **84%** single-fabric success. Independent adaptive replicas reached 62/72/88/90/98% success for 1/2/4/8/16 replicas respectively.

## Energy boundary
A deliberately incomplete capacitive switching proxy uses the preserved 72 fF weak-node reference and 9.52 fF 2x2 MIM reference at 0.2 V. It excludes MOS loss, wire loss and physical parasitics and therefore is **not** a physical energy claim. More replicas improve coverage but multiply switched capacitance; pressure escape is therefore preferred before brute-force replication.

## Problem
This is a physics-inspired algorithmic model, not transistor/PEX proof. It also solves a constraint family, not general AI. The next question is whether relation retrieval and exact operations can also be embodied without a processor.

## Reproduce
`python3 experiments/v13O0_constraint_membrane_reasoning/source/run_v13o0.py`
