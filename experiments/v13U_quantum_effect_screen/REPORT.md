# v13U — Quantum-Effect Memory and Stochasticity Screen

**Verdict: MODEL/PROCESS-DATA PASS for a sparse consolidation layer; REJECT coherent quantum memory for current GVS.**

## What was tested
1. technology-role fit for volatile MIM/MOS, SKY130 SONOS, future MRAM, coherent quantum memory and single-electron/quantum-dot ideas;
2. SONOS endurance versus v13T adaptive-role switching and delayed consolidation;
3. conservative SONOS read-state margin using official SKY130 e-test limits;
4. whether stochastic escape helps local constraint search.

## Main findings
- v13T's measured adaptive rate (~121.5 role changes / 840 epochs across four reserve cells) would consume a 100k-write endurance budget after only ~2.77M local epochs if every active role were persisted.
- Delayed consolidation reduces writes but makes the durable copy stale: at 64 epochs, writes fall ~78.5% but live-role match is only ~31.3%; at 128 epochs writes fall ~97.2% but live-role match is ~21.1%.
- Therefore SONOS must store deep morphology/boot priors, not active Role Pressure or current Expression-Patch ownership.
- SKY130's conservative erased/programmed read-current limits (>=20 uA versus <=2 nA at the documented read condition) give a 10,000x gap. A 200 nA geometric-mid threshold has ~100x margin from either bound. A 1,000,000-sample severe sensor-noise stress produced zero modeled read classification errors.
- Small stochastic escape improves the tested local constraint solver, especially at 96/128 variables. This supports a cheap noise source but gives no evidence that quantum coherence is required.

## Decision
Keep fast live state in ordinary MIM/MOS. Add persistent memory only as a sparse, shared, slow consolidation tier when lifetime benefit repays special-process/high-voltage infrastructure. SKY130 SONOS is the current-process candidate in supported technology options; STT/SOT MRAM is a future-process comparison. Coherent qubit memory is rejected for the cheap GVS fabric.

All results are deterministic/seeded model or process-data screens, not fabricated measurements.
