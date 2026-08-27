# GVS v13U — Quantum-Effect Consolidation Memory

**Status: architecture/model pass; current-process SONOS is useful only as slow persistent consolidation, not as live adaptive state. Coherent quantum memory rejected for the cheap GVS fabric.**

v13U keeps v13T adaptive tissue, v13S venous recovery, v13Q cell-as-wire communication, the accepted Grammar reader, Population Confidence, and the hollow/all-surface placement architecture. It does not replace them with a quantum computer.

## 1. Question tested
Can quantum physics materially improve GVS memory or reasoning without making the chip expensive?

The answer is **yes, but only in narrow device roles**.

Quantum coherence is not the useful part for the present GVS target. The useful effects are ordinary solid-state phenomena such as charge tunneling and magnetic tunneling/spin that can provide persistent memory without requiring a runtime quantum algorithm.

## 2. Three memory timescales
### Working Membrane State
MIM/MOS state remains the fast local memory for evidence, context, Role Pressure, fatigue and adaptation. It can change constantly and is physically colocated with computation.

### Homeostatic State
Fast/slow Role Pressure from v13T remains analog/volatile. It deliberately forgets and should not spend nonvolatile endurance on transient workload pressure.

### Consolidated Morphology
**Quantum-Effect Consolidation Memory (QECM):** a sparse nonvolatile memory layer that records only relations, role priors or morphology that have remained useful/stable long enough to justify a durable write.

Candidate current-process device: SKY130 SONOS flash in the process options that support it.

Future-process candidate: STT/SOT MRAM if an integrated process or memory chiplet provides a measured cost advantage.

## 3. SKY130 SONOS result
Official SKY130 documentation supports SONOS nonvolatile cells in special technology options and provides beginning/end-of-life programmed/erased models.

Important process facts used in v13U:
- nominal program pulse: ~2 ms;
- nominal erase pulse: ~6 ms;
- guaranteed endurance shown to 100k cycles;
- conservative read-current limits at 1.8 V: erased >=20 uA and programmed <=2 nA.

The current local PDK installation also contains `sky130_fd_bs_flash__special_sonosfet_star` ngspice model files for programmed/erased beginning/end-of-life conditions.

### v13U2 read-margin screen
The conservative process-limit erased/programmed current ratio is **10,000x**.
A geometric-mid current threshold is ~200 nA, leaving ~100x margin from either guaranteed bound.
A 1,000,000-sample stress with intentionally severe multiplicative sensing noise produced zero modeled classification errors.

**Decision:** reading consolidated SONOS state is not the main architectural problem. Write latency, high-voltage support, endurance and special-process cost are the limiting terms.

## 4. Do not persist live adaptive roles
v13T's measured dual-timescale model produced about 121.5 reserve role changes over 840 epochs across four reserve cells, or ~0.03616 role writes per cell-epoch if every change were made nonvolatile.

At 100k guaranteed SONOS cycles, that corresponds to only ~2.77 million local epochs before spending the guaranteed cycle budget.

v13U1 therefore tests a consolidation delay. On a fast-changing 200k-epoch reserve-role trace:
- 32-epoch stability window: ~58.1% fewer NVM writes, but NVM matches current live role only ~50.6% of the time;
- 64 epochs: ~78.5% fewer writes, but only ~31.3% live-role match;
- 128 epochs: ~97.2% fewer writes, ~21.1% live-role match;
- 256 epochs: ~99.94% fewer writes, ~19.7% live-role match.

This means a slow NVM copy becomes stale if it is treated as a mirror of the live adaptive cell.

**Decision:** SONOS does not store the active Role Pressure/Expression-Patch selection. It stores only a deep prior or morphology state that is allowed to be stale and is overridden by live tissue after power-up.

## 5. Consolidation rule
A relation/role may be written into QECM only after all of these are true:
1. it has remained stable beyond a long consolidation window;
2. its repeated usefulness exceeds a promotion threshold;
3. expected future reuse repays the NVM write/high-voltage cost;
4. losing or staling the NVM copy cannot create a wrong robust answer;
5. live MIM/MOS state remains the correctness authority during operation.

This creates:
`fast adaptation -> familiarity/promote -> long persistence -> optional NVM consolidation`.

## 6. Boot behavior
On power-up, QECM supplies **priors**, not commands.

`consolidated morphology -> seed local role/relation -> Role Pressure/Grammar/context immediately allowed to override`.

A stale durable memory therefore costs adaptation time, not correctness.

## 7. Where quantum coherence was rejected
Coherent quantum memories can store quantum states and room-temperature demonstrations exist in specialized optical systems, but practical solid-state quantum computing/memory stacks still require specialized control, isolation and often cryogenic infrastructure. That overhead conflicts with the current GVS objective of negligible-cost repeated classical intelligent tissue.

Therefore v13U rejects:
- qubits per ECC;
- cryogenic quantum-memory blocks;
- entanglement/coherence as a requirement for Grammar/context/reasoning;
- quantum error-correction hardware in the local fabric.

## 8. MRAM future option
Magnetic tunnel junction memory uses electron spin and quantum tunneling. Modern STT-MRAM is a practical nonvolatile technology with strong speed/endurance/density characteristics and is being adopted as embedded NVM in advanced processes.

It is **not** in the current GVS SKY130 physical baseline, so v13U does not count hypothetical MRAM savings as current evidence.

If a future GVS process/chiplet exposes MRAM, it should be compared against SONOS for more frequently updated consolidated relations and reserve-role priors.

## 9. Stochastic physics for reasoning
v13U3 tested a local planted-constraint solver with occasional stochastic escape.

Representative results within a fixed 700-step budget:
- 64 variables: deterministic 25%; best tested noise point 41.7%;
- 96 variables: deterministic 8.3%; 20% stochastic escape 50%;
- 128 variables: deterministic 0%; tested 10-20% stochastic escape 16.7%.

This supports a small physical noise/entropy source for escaping local attractors.

It does **not** establish a quantum advantage. MOS thermal noise, mismatch, metastability or a future stochastic magnetic device may provide the randomness. Use the cheapest measured source.

## 10. Physical organization
QECM is sparse and shared. Do not put a high-voltage SONOS program circuit in every ECC.

Preferred organization:

```text
fast ECC tissue
  |  MIM/MOS evidence, context, RPF, active role
  |
  +-- familiarity / stability accumulator
             |
             | only after deep promotion
             v
      shared consolidation interface
             |
       SONOS / future MRAM bank
             |
       persistent morphology
```

The NVM bank belongs in a Component Bay / support region where high-voltage programming and isolation can be shared. Readback may seed nearby regions through ordinary low-voltage information paths.

## 11. KEEP / REJECT
### KEEP
- fast MIM/MOS memory for live thought/adaptation;
- slow nonvolatile consolidation for truly stable morphology;
- SKY130 SONOS as a real current-process candidate only where its special option is available;
- future MRAM comparison;
- low-cost stochastic exploration when it improves hard search;
- live tissue overriding stale persistent priors.

### REJECT
- SONOS writes on every role change;
- SONOS as Role Pressure memory;
- one NVM/high-voltage block per cell;
- coherent quantum memory as the main GVS memory;
- assuming stochastic benefit implies quantum advantage;
- changing accepted Grammar/neurovascular hardware merely to include a quantum device.

## 12. Evidence boundary
v13U0/U1/U2/U3 are architecture/model/process-data screens. The SONOS current separation uses official SKY130 e-test bounds, not a new fabricated measurement. A full SONOS layout/program/erase PEX has not been produced in this open GVS flow.

## 13. Next — v13U4 Consolidation Interface Closure
Test one shared persistent-memory interface behind the adaptive tissue:
1. volatile fast role/Relation state;
2. familiarity/stability accumulator;
3. deep promotion decision;
4. persistent SONOS model readback using BOL/EOL programmed/erased corners if a compatible simulator is available;
5. shared high-voltage programming cost model;
6. power-cut/restart with stale-prior override;
7. compare no-NVM, SONOS, and future-MRAM parameter envelopes.

Promote QECM only if lifetime energy/area/restart benefit repays special-process and programming infrastructure.
