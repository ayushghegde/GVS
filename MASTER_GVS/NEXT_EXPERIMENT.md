# Current Next Experiment — v14J1 Plastic-Link Physical Closure

## Goal
Determine whether a self-plastic capacitive connection can remain cheaper than transistor memory after the full programming problem is counted.

## Required tests
1. Obtain or construct a credible compact model for a reversible two-terminal ferroelectric/memcapacitive link with separate read and program regimes.
2. Replay weak/strong charge transfer using actual device capacitance windows, not the abstract 0.25/0.85 fF model.
3. Test bidirectional learning with positive/negative local differential pulse pairs, including reversal after a relation changes twice.
4. Sweep coercive/program threshold variation, read disturbance, retention drift, program failure, and partial-state saturation.
5. Test half-selected links in a sparse connection bundle so learning one relation does not rewrite neighbors.
6. Count complete write infrastructure: pulse rails, selectors/isolation if required, routing, write energy, and process steps. Do not compare only the two-terminal device footprint with one transistor.
7. Compare three hardware options: fixed compiled MIM, programmable ferroelectric memcapacitor, and a transistor-memory baseline on total inference+learning cost.
8. Retain two/three parallel link copies only if they repay their added area in fault tolerance.
9. Feed the physical link model into the v14H2 seven-domain connection-memory benchmark and verify that continual learning does not destroy multi-hop reasoning.
10. Keep specialized node-memory structures such as Role Pressure and CFN sparse; do not reintroduce persistent memory into every semantic cell.

## Acceptance
Promote SPCL only if it provides reversible nonvolatile coupling, negligible read disturb, adequate retention/endurance, and a total system cost below the transistor-based memory/routing it replaces. If programming/select infrastructure dominates, keep fixed MIM for inference-only connection planes and reject on-chip plastic SPCL until a cheaper material/process appears.
