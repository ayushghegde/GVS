# Neural Glyph v13A6 — 10-MOS Dual-Input-Pair Grammar Reader

**Verdict: PARTIAL PASS — direct physical-ratio electrical model passes PVT and 96 combined MIM+MOS mismatch cases with 0 wrong accepts; physical reader layout/PEX remains.**

## Analysis target
v13A5 solved the old fixed 0.5 V Grammar threshold with a legal-MIM PVT-tracking candidate/reference ratio, but the sequential 13-MOS analog-swap reader became physically asymmetric and parasitic. The goal here is to remove the analog swap crossbar without returning to a conventional ADC/comparator.

## Selected topology
Use one shared regenerative latch and two mirrored PMOS differential input pairs:

- shared core: 2 cross-coupled NFET + 2 output-reset NFET
- phase-0 tail PFET + normal PMOS pair
- phase-1 tail PFET + crossed PMOS pair
- total: **10 MOS**

Weak candidate/reference evidence never moves through an analog switch crossbar. Phase selection occurs by enabling one of the two PMOS input pairs. Fresh local capacitive evidence is replayed before phase 2; the replay stays inside the already-selected Regional Lease and does not repay the long coordinate event.

Acceptance is strict: phase 0 and phase 1 must resolve to opposite physical sides corresponding to the same logical answer. Same-side preference or weak resolution is **fallback**, never accepted.

## Important transistor optimization
The original W=1 um / L=1 um PMOS input devices were too slow when connected directly to the real ratio network, whose common-mode is ~0.57-0.60 V.

Tail-strength sweeps did not solve this efficiently.

The useful solution was to preserve approximately the same PMOS input gate area while changing aspect ratio:

- old: W=1 um, L=1 um
- selected: **W=2 um, L=0.5 um**

This keeps first-order device area/mismatch scale similar while increasing W/L by about 4x. The direct capacitor-ratio network then resolves robustly in the original 1.5 ns/phase window.

More aggressive devices (e.g. much wider/shorter) increased energy without enough benefit and were not selected.

## Direct physical-ratio nominal result
Candidate/reference use the v13A5 legal 2x2 MIM ratio model including physical series-pair midpoint parasitic and ~0.055 fF candidate-reference cross-coupling.

At TT/FF/SS, exact and partial motifs both resolve correctly in two 1.5 ns phases. Typical evidence margins remain roughly +/-24 to 27 mV.

VDD decision energy is approximately:
- FF: ~50-57 fJ
- TT: ~54-60 fJ
- SS: ~58-64 fJ

The local capacitive evidence replay remains sub-fJ class and is not the dominant cost.

## Combined mismatch
Both independent MIM mismatch and SKY130 MOS mismatch are active.

Two batches, 8 seeds per corner/motif each, total **96 exact/partial cases** across TT/FF/SS:

- correct accepts: **95**
- deliberate fallback: **1**
- wrong accepts: **0**

The single fallback was a TT partial case where both phases fully resolved to the same physical latch side despite a ~-24 mV physical evidence margin. The self-check therefore detected input-pair offset and refused the analog answer.

Across the screen, evidence remained approximately:
- exact: +24 to +29 mV
- partial: -21 to -27 mV

## Comparison to rejected/less-useful points
- W=1/L=1 input pairs: lower energy but much higher SS fallback rate under mismatch.
- W=1.25/L=1: insufficient reliability improvement.
- W=1.5/L=1: lower fallback than W=1, but slower and ~60 fJ class; still occasional offset fallback.
- W=2/L=1: added capacitance and did not improve the trade.
- stronger tail only: did not restore robust direct-ratio resolution efficiently.

## Conclusion
The architecture problem from v13A5 is now electrically improved without adding a conventional digital threshold:

`legal-MIM Grammar ratio -> phase0 PMOS pair -> shared latch -> reset/replay -> phase1 mirrored PMOS pair -> accept or fallback`

The key improvement is **same-area faster input transistor geometry**, not more tail current or a larger comparator.

## Remaining problem / next
1. physically lay out the exact 10-MOS reader with W=2/L=.5 PMOS input devices;
2. keep GC/GR routes short and geometrically symmetric;
3. DRC + extraction; reject any DRC-clean topology with wrong connectivity;
4. co-place beside the extracted 10-MIM ratio array;
5. rerun direct PEX ratio -> reader at TT/FF/SS;
6. rerun combined MIM+MOS mismatch;
7. measure full event energy including reset/tail controls and local evidence replay;
8. only after physical PEX passes, connect the robust Grammar winner to the selected eight-way Regional Lease refresh/event path.
