# Neural Glyph v13B3 — Silicon Framework Hollow Cell + Fourth-Face Analog Link

**Verdict: PARTIAL PASS — the clarified 'building framework' interpretation is stronger than an empty hollow shell, and a real 3-MIM + fourth-face MOS physical emulation passes when the analog face is controlled with a full-swing/static enable. Directly using the ~1 V analog Regional-Lease state as the pass-gate control is rejected because NMOS threshold compression destroys most of the small exact/partial differential.**

## Terms

- **Silicon Framework Cell (SFC):** a volumetric cell where silicon is used as thin active/structural walls or ribs, while the cavity can contain other useful components, interconnect, power, cooling, memory, or chiplets at the appropriate scale.
- **Fourth-Face Analog Link (FFAL):** three capacitor faces accumulate evidence and a fourth face exports that analog state to another cell through a controlled contact rather than first digitizing it.
- **Contact Receptor:** a small landing capacitance at the receiving face so the source cell does not have to charge the receiver's entire membrane/state node.
- **Myelin Chord:** a sparse direct long-range connection through the interior that skips intermediate local cells when a relation is stable/reused enough to justify physical promotion.

## 1. Clarified architecture

The user did not mean an empty cavity with a few wires. The intended analogy is a building or subway system: silicon acts more like the steel/concrete framework, while the enclosed volume can host several different functions.

At a millimeter/package scale, cavity contents could include different chiplets or controller dies, memory, passive capacitors, power/clock distribution, thermal channels, optical/I/O structures, sensors, or local bridges. At micron/nano Glyph-cell scale, the cavity cannot contain a whole microcontroller; it would contain transistor/passive/interconnect structures appropriate to that scale. These two scales must not be confused.

## 2. Hypothetical framework geometry screen

The user's 20 mm / 5 mm / 0.5 mm dimensions are treated only as geometry examples, not proposed fabrication dimensions.

For a 5 mm cubic cell with 0.5 mm walls:

- 20 mm thickness allows 4 cell pitches;
- full six-wall shell leaves a 4 mm internal cube = **51.2% cavity volume**;
- a shared periodic 0.5 mm wall framework idealization leaves **72.9% cavity volume**;
- an edge-rib-only mathematical idealization leaves ~97.2% void, but this is not a mechanical/fabrication recommendation;
- full outer + inner surface area is 246 mm^2 versus a 25 mm^2 planar footprint = **9.84x theoretical surface/footprint**, before accounting for shared walls, keep-outs, assembly and thermal constraints.

The screen supports the main idea: if a package is deliberately volumetric, a solid inactive interior is not automatically the best use of volume. The cavity can host heterogeneous functions while thin silicon regions carry active devices where semiconductor is actually required.

## 3. Physical three-wall cell emulation

Because SKY130 does not provide literal vertical sidewall MIM cells, the three capacitor walls were emulated with three legal planar 2x2 um `sky130_fd_pr__cap_mim_m3_1` devices feeding one evidence node.

Two fourth-face implementations were physically drawn and extracted.

### A. Evidence-gated long weak MOS — REJECT as default

Physical cell:
- 3 legal 2x2 um MIMs;
- one W=0.42 um / L=12 um NFET whose gate is the evidence node;
- DRC = 0;
- extraction sees exactly 3 MIM + 1 NFET.

Extracted evidence-node routing parasitic is ~4.879 fF. The 12 um gate itself has an estimated oxide-area capacitance of ~42 fF (using the SKY130 1.8 V oxide thickness), which is comparable to the intentional 40 fF local membrane.

Including this gate-load estimate, first-order exact-vs-partial wall separation falls to approximately:
- low MIM corner: **13.75 mV**;
- typical: **16.72 mV**;
- high: **19.41 mV**.

This exposes a hidden problem in the earlier readerless screen: making a MOS weak by making it extremely long also turns its gate into a large capacitor. It can consume much of the small wall evidence before the analog decision is even made.

**Decision: do not use an evidence-driven L=12 MOS as the default fourth face.**

### B. Lease/config-gated minimum MOS pass face — selected physical candidate

Physical cell:
- 3 legal 2x2 um MIM walls;
- one W=0.42 um / L=0.15 um NFET pass device;
- evidence connects to source/drain, not the gate;
- separate `LEASE/ENABLE` controls the gate;
- DRC = 0;
- extraction sees exactly 3 MIM + 1 NFET.

Extracted parasitics:
- evidence-node ground parasitic: **~2.965 fF**;
- extra wall-to-evidence fringe: **~0.164-0.169 fF per wall**;
- EVID-to-LEASE coupling: **46.51 aF**;
- EVID-to-OUT coupling: **24.71 aF**.

With the intentional 40 fF local state, first-order three-wall vs two-wall separation remains approximately:
- low MIM corner: **22.95 mV**;
- typical: **26.90 mV**;
- high: **30.24 mV**.

## 4. Full SKY130 PVT transient — physical MIM + physical pass MOS

The extracted topology was replayed with the real SKY130 MIM model, real W=0.42/L=0.15 NFET model, 40 fF local state, extracted parasitic terms, and a 3 fF receiving Contact Receptor.

### Raw ~1.0 V lease gate — FAIL

At TT with the pass gate driven to only 1.0 V:
- exact receptor @1.30 us: ~0.47995 V;
- partial receptor: ~0.47670 V;
- separation: only **~3.25 mV**.

The NMOS is operating near its threshold and behaves like a source-follower limiter. It compresses the useful analog difference.

**Decision: do not connect the existing ~1 V analog WAKE directly to this fourth-face pass device and expect high-fidelity analog transfer.**

### Full-swing/static 1.8 V enable — PASS

With a 1.8 V enable held during the analog transfer:

| Corner | Exact receptor | Partial receptor | separation |
|---|---:|---:|---:|
| TT | 0.524486 V | 0.499492 V | **24.994 mV** |
| FF | 0.525296 V | 0.500272 V | **25.024 mV** |
| SS | 0.523704 V | 0.498738 V | **24.966 mV** |

The fourth face therefore preserves nearly all of the physical wall differential when the connection is strongly enabled.

This does not require a per-event digital conversion of the wall evidence. For a stable/local relation, the enable can be static or amortized over a lease/burst. A fixed capacitive/metal contact is also possible for a permanently promoted relation.

## 5. Independent full-PDK mismatch launches

`tt_mm`, `ff_mm`, and `ss_mm` were run with independent ngspice random seeds 101 and 404. Exact and partial stimuli were paired using the same seed to represent the same physical cell under the two input classes.

Receptor separation:

- TT seed101: 24.163 mV
- TT seed404: 24.699 mV
- FF seed101: 24.193 mV
- FF seed404: 24.729 mV
- SS seed101: **24.135 mV**
- SS seed404: 24.670 mV

Result: **6/6 paired mismatch launches preserve the correct sign; minimum receptor separation ~24.14 mV.**

This is a small mismatch screen, not a fabrication-yield claim.

A separate 200k-sample analytical stress using 1.4% wall-cap sigma and an extra non-PDK 5% membrane-cap stress also produced no sign reversals; the low-corner 0.1-percentile receptor separation was ~14.81 mV. This is a model stress only, not additional PDK signoff.

## 6. Crosstalk / switching injection

Using the extracted typical ~72 fF total evidence-node capacitance:

- a full 1.8 V transition coupled through the 46.51 aF EVID-LEASE term is ~1.16 mV worst-case charge-kick proxy;
- a full 1.8 V neighboring OUT transition through 24.71 aF is ~0.62 mV;
- aligned worst-case proxy is ~1.78 mV, far below the ~25 mV transferred class separation but not zero.

The full transient shows a common-mode kick at the 1.8 V enable edge, while exact-vs-partial separation remains ~25 mV.

**Rule: establish a static/promoted contact before analog evidence capture when possible. Avoid toggling the fourth-face control in the middle of a weak decision.**

## 7. Energy

From the full PDK runs, fourth-face 1.8 V gate-source work is about:
- TT: ~1.56-1.57 fJ;
- FF: ~1.64-1.65 fJ;
- SS: ~1.49-1.50 fJ.

Using the measured evidence rise to infer effective wall coupling, the three-wall event source-work proxy is ~0.68 fJ for an exact three-wall pulse and ~0.55 fJ for a two-wall partial pulse.

Combined local wall + fourth-face enable proxy:
- exact: roughly **2.18-2.32 fJ** across corners;
- partial: roughly **2.04-2.19 fJ**.

This excludes downstream competition/soma energy and is not a whole-cell energy number. It is nevertheless much smaller than the ~76-97 fJ robust dual-pair Grammar readout, so removing that conversion is attractive when the destination can consume analog evidence directly.

## 8. Two touching hops versus one chord

With the typical extracted cell capacitance ~72 fF and ~26.9 mV internal exact-vs-partial separation:

### Equal full-cell passive touching
- one equal-capacitance touch -> ~13.45 mV separation;
- two touches -> ~6.72 mV.

Two raw passive hops are therefore **rejected** for high-confidence reasoning without local regeneration.

### Small Contact Receptor
A 3 fF landing receptor receives approximately **25.82 mV** in the first-order charge-sharing model, preserving ~96% of the source separation.

This is the preferred fourth-face geometry: do not connect the source evidence node directly to the next cell's entire membrane. Land on a small receptor and let the receiving cell's own local dynamics consume/regenerate the signal.

### Chord load budget
Using the current ~26.9 mV typical source separation:
- to remain >=18 mV, total receptor+chord capacitance should stay below ~35.6 fF;
- using the earlier measured M4 ~0.076106 fF/um only as a comparison proxy, that equals ~468 um of such wire capacitance;
- to remain >=11 mV, the budget is ~104 fF (~1.37 mm of that M4 proxy).

These are capacitance budgets, not measurements of a future hollow-core conductor.

## 9. Architecture decision

The strongest interpretation of the user's idea is now:

`thin silicon framework -> three-wall capacitive Glyph cells -> small fourth-face receptors -> embedded heterogeneous utility volume -> sparse Myelin chords -> robust reader only at boundaries that actually require a full-swing result`

### Keep
- silicon as framework rather than unnecessary solid inactive volume;
- heterogeneous components in cavities at the scale where they physically fit;
- three capacitor walls as real evidence structures;
- small receptor on the fourth face;
- full-swing/static enable for a dynamic pass face;
- permanent capacitive/metal contact for stable promoted relations;
- sparse diagonal Myelin chords;
- robust v13A5/v13A6 reader only when a robust event is required.

### Reject
- a continuous conductive core;
- a giant evidence-gated long MOS on every cell;
- directly using the ~1 V analog lease as a high-fidelity pass-gate control;
- raw multi-hop equal-capacitance touching without regeneration;
- claiming the millimeter example is a real chip geometry.

## 10. Next experiment

Build the first mixed eight-way region using this interface rule:

1. two or more Tri-Wall/Grammar-like physical evidence cells;
2. at least one fourth-face analog link landing on a small receptor;
3. one local competition node that consumes that receptor without a separate Grammar reader;
4. one closed dual-pair reader boundary for comparison;
5. one two-hop local path and one direct Myelin-chord equivalent with matched source evidence;
6. measure receptor load, local competition correctness, lease/control injection, energy and route latency;
7. promote the analog link only if it removes reader/long-route energy without increasing wrong accepts.

The real hollow/framework package should remain a later packaging experiment until this ordinary-silicon emulation proves the local electrical rules first.
