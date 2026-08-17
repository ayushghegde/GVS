# Experiment Lineage — What Each Stage Added

This is a continuity map, not a replacement for the original reports. Keep original reports/results as source of truth.

## v11 natural-firing / self-correction line
- **v11N** — selective persistence reset. Preserve useful persistence while resetting fast soma.
- **v11O** — moved to real SKY130 devices; reset NMOS had to be legally fingered.
- **v11P** — mismatch exposed stale-route spikes; confirmed falling-edge clear solved much of it without destructive always-clear.
- **v11Q** — reduced huge membrane/persistence capacitors; conservative 88 pF / 132 pF direction survived broader screens better than more aggressive scaling.
- **v11R** — replaced giant ideal leaks with long-channel MOS weak leaks; fixed bias failed across PVT.
- **v11S** — stored leaked charge as physical negative-feedback memory; useful at hot corner but always-active storage became sticky.
- **v11T (historical summary label)** — moved toward one shared self-thresholding charge bucket; keep provenance separate from repository `v11T_unfinished`.
- **v11U** — separated PVT sensing from route activity with slow replica leak; added reset-charge recovery concept.
- **v11V** — whole-fabric one-way recovery bus; rejected too-small rail that fed back into firing.
- **v11W** — combined global recovery with shared memory/adaptation; recovery could support adaptation subsystem under modeled activity budgets.
- **v11X** — shared analog self-correcting regional core; one shared adaptation node for multiple routers; architecture-level pass/model screen.

## v12 self-correction compression -> memory/context -> hybrid
- **v12A** — two-pilot regional self-corrector; rejected direct whole-region leak bucket; kept pilot architecture.
- **v12B** — real-PDK preparation/mismatch-compression search; kept regional approach while toolchain was incomplete.
- **v12C** — restored real SKY130 mismatch simulation; real BSIM changed which leak-stack topology was best.
- **v12D** — recycled firing charge into row/column electrical route memory; MOS intersections decoded prior route.
- **v12E** — same trace used for recency, repetition confidence and compute-skip; self-reference reduced PVT sensitivity.
- **v12F** — routerless winner-take-all, fatigue, multimodal/event fabric direction.
- **v12G** — electrical-context reasoning without explicit router; firing context inhibits/steers next choice.
- **v12H** — shared inhibitory interneuron hierarchy + ambiguity escalation; passive pooled inhibition and direct tie-breaking shunts rejected.
- **v12I** — recycle ambiguous finalist charge, then use compressed exact tag only after ambiguity; robust hybrid fallback.
- **v12J** — stop context-wrong evidence at the source; important energy correction. Brain/event and computer compared fairly on sparse workloads.
- **v12K** — stable ternary connection becomes a physical MIM capacitor; exact fallback protects uncertainty. Image/sound/multimodal avoided most repeated weight reads in tested workloads. Analog exact ALU direction not supported.
- **v12L** — repeated stable weight patterns promoted into shared capacitive templates with exact digital residuals.
- **v12M** — template-ID SRAM reads removed from event path; static binary pass tree chosen. Sound 1x3 sharing useful with inactive-source isolation. One-hot and naive decoder rejected.
- **v12N** — Grammar Cells create high-level events directly from common local patterns. Sound strong, vision selective first-look, code structure recognition useful, exact arithmetic stays computer-like. Ambiguity escalates.
- **v12O** — autonomous representation/morphogenic compiler chooses digital, sparse exact, template, Grammar/event, etc. based on measured reuse/stability/cost/error.
- **v12P** — continuous reuse bookkeeping reduced with physical lease capacitors and speculative exact fallback.
- **v12Q** — mini complete-system integration; repeated execution plans become Myelin paths; 28k-query trace establishes regional reuse structure.
- **v12R** — passive and full-swing Myelin physically demonstrated; compressed reasoning/control storage refined; tiny-dendrite direct digital bridge rejected.
- **v12S** — complete autonomous tile lifecycle integrated: lease/request, VALID, Grammar, programmable passive Myelin, capacitive template evidence, dendrites, robust somas, competition, full-swing route capture, exact kernel, automatic recovery, error invalidation and exact fallback. Historical verdict PARTIAL PASS because real placed/routed extraction was missing at that point.

## v13 physicalization / scaling
- **v13P0** — first real SKY130 route/MIM/NFET extraction; connected Myelin edge became DRC-clean with small parasitics and sub-ohm routing. No architecture change justified.
- **v13P1** — two-edge crosstalk at compact pitch remained small.
- **v13P2** — four-edge cluster showed accumulated local Myelin coupling still tiny.
- **v13P3** — long shared-spine/fan-in extraction found that wire length can dominate control capacitance.
- **v13P4** — real terminal/contact loading quantified; reinforced use of short local segments.
- **v13 GTI/receiver sequence** — long parallel event wires showed dangerous coupling; orthogonal M4/M5 event geometry reduced coupling drastically. Coordinate receiver evolved through physical/extracted tests; cheaper 4T active-low coordinate-release cell later passed PVT/mismatch/full-lifecycle screens in the working experiments.
- **v13P10** — physical ~1 mm x 1 mm 16x16 orthogonal event grid, 256 crossings, 0 DRC; selected row+column physical charge about 0.68 pJ including receiver-loading estimate.
- **v13P11** — selection interface inserted into complete v12S lifecycle in a differential integration screen; local tile behavior remained transparent relative to same compact baseline. Later working-session real-model receiver/full-lifecycle tests further strengthened this direction.
- **v13P12** — old one-way/shared-recovery idea revisited for modern tiles; four tiles sharing one 10 pF reservoir passed nominal PVT and a 12-launch four-tile mismatch screen in the working experiments, reducing the modeled recovery-cap target from 40 pF to 10 pF. Dense nonlinear varactor reservoir rejected for now.
- **v13A** — representation compiler becomes physical-cost/locality aware using extracted 16x16 event-fabric cost. Result: hybrid still wins only if several low-level operations stay local before another long-distance selection is paid.

## Directional conclusion from the full history
The experiments repeatedly converge on the same architecture:

1. use physics for stable/reused/local computation;
2. use exact computer logic for changing/precise/unusual work;
3. detect uncertainty instead of guessing;
4. move only high-level events over long distances;
5. store short-lived control/history as charge when that removes metadata;
6. share expensive support hardware regionally when local decisions remain isolated;
7. let an autonomous compiler promote/demote representations as reuse, drift and physical cost change.
