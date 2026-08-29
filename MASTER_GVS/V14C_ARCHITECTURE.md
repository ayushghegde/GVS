# Neural Glyph v14C — Heterogeneous Adaptive Reasoning Tissue

**Status: selected system candidate.** v14C keeps the accepted v13A–v13U computational, cell-as-wire, neurovascular, adaptive and consolidation ideas, but changes the reserve tissue after end-to-end workload testing.

## New organization
A 64-cell region is now modeled as:
- 18 Relay/Conduction ECCs;
- 12 Grammar ECCs;
- 10 Template ECCs;
- 8 Binding/Context ECCs;
- 8 Constraint/Competition ECCs;
- 2 Morphological Exact-Patch ECCs;
- 4 full General Reserve ECCs;
- 2 Critical Reserve ECCs.

**Critical Reserve Cell (CRC):** an adaptive reserve ECC that carries only Constraint and Exact Expression Patches, while retaining cell-as-wire conduction and physical Role-Pressure adaptation.

Two former relay-only positions become CRCs; region cell count remains 64. This is compatible with cell-as-wire because reserve cells can still relay local events.

## Physical Role Pressure carried forward
The selected adaptive-support primitive is:
- FAST pressure: two legal 2x2-um MIMs, ~19.04 fF nominal storage, PFET injector W/L 1.26/0.50 um;
- SLOW pressure: four legal 2x2-um MIMs, ~38.08 fF nominal storage, PFET injector W/L 1.38/0.50 um;
- one ~1x1-um MIM CHL bucket per pressure path (~2.38 fF screen);
- 6-MOS hysteretic selector: PFET 5.04/0.15 x2, PFET feedback 3.78/0.15, NFET feedback 2.52/0.15, NFET 1.26/0.15 x2.

**Capacitive Homeostatic Leak (CHL):** a small discharged MIM bucket removes a fraction of Role-Pressure charge by charge sharing, avoiding a process-sensitive subthreshold leak bias.

The selected 2-MIM FAST / 4-MIM SLOW physical timing table preserves SLOW-after-FAST in all 27 TT/FF/SS x supply x temperature points. The minimum matched timing gap is ~10.023 ns and mean gap ~24.86 ns. Preliminary independent TT mismatch runs (12 FAST + 12 SLOW) had non-overlapping observed ranges; even a 2x empirical half-span envelope still leaves ~0.30 ns ordering margin. This is supporting evidence, not a claim of a completed 48+48 PDK Monte-Carlo signoff.

Strict FAST-before-SLOW ordering is an adaptation-quality property, not a computation-correctness boundary: an extreme ordering crossover may alter response speed but may not authorize a wrong robust answer.

## Adaptive reserve rules
- four General Reserve ECCs may express Grammar, Template, Binding, Constraint or Exact patches;
- two CRCs may express only Constraint or Exact patches;
- reserve cells use mixed fast/slow Role Pressure;
- hysteresis, dwell/fatigue and a one-change developmental wave prevent role thrashing;
- patch handoff remains break-before-make;
- old patch state may drain through Dual-Key Egress -> Local Venule while the new patch operates.

## Confidence–Pressure Effort
**Confidence–Pressure Effort (CPE):** an unresolved reasoning state is allowed extra local settling only while constraint-tissue pressure is low; under congestion it remains unresolved rather than monopolizing cells.

In the selected model screen, a low pressure threshold is a Pareto improvement over a fixed four-attempt rule. It is not yet a fixed voltage threshold; physical Population Confidence/Role Pressure must implement the equivalent behavior without a scheduler.

## Recovery and persistent memory
Unchanged hierarchy:
`expired patch -> Dual-Key Egress -> Local Venule -> Charge Artery -> regional reservoir -> battery/collector`.

Thermal Capillary/Artery remains separate. Persistent SONOS/future MRAM remains a sparse consolidation tier only; FAST/SLOW Role Pressure and active Expression-Patch ownership stay volatile MIM/MOS.

## System evidence
The main 100-seed mixed multi-stage workload uses complete questions requiring Grammar/Template/Binding/Constraint/Exact stages, seven workload phases, burst noise and 10% specialized-cell loss.

Baseline four-full-reserve adaptive tissue:
- ~71.7% of questions complete within 20 epochs;
- fixed differentiation: ~52.0%;
- universal tissue: ~100%;
- fixed/adaptive optional module copies: 60 vs universal 320.

v14C reserve differentiation, using 4 General + 2 CRCs:
- 100% eventual completion in the selected 10% failure sweep;
- ~90.1% within 20 epochs;
- p95 latency ~22.36 epochs;
- 64 optional module copies.

This is ~4.5x the universal tissue's on-time decisions per optional-module copy in the model, while universal tissue remains much faster in absolute latency.

## Hard-reasoning boundary
The 96/128-variable stochastic constraint screen shows the remaining bottleneck is reasoning quality, not only hardware quantity. With four allowed attempts, eventual resolution is ~79%; allowing deeper settling raises resolution toward ~96% but increases queue delay. CPE gives a small Pareto improvement by spending extra settling only under low local pressure.

v14C therefore does **not** claim modern foundation-model capability. It demonstrates that a highly differentiated/adaptive physical organization can approach universal-hardware throughput on the tested multi-role workloads with far fewer optional module copies, while exposing reasoning dynamics as the next dominant limitation.
