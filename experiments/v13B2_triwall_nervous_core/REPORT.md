# Neural Glyph v13B2 — Tri-Wall Cell + Nervous-Core Screen

**Verdict: PARTIAL PASS — the user's 'three capacitor walls + one connection face' maps unusually well onto the existing 3-input Grammar physics; replacing the hollow interior with a continuous conductor is rejected, while a structured insulating core containing controlled sparse conductors is kept as a future architecture target.**

## New terms

- **Tri-Wall Glyph Cell (TWGC):** a 3D local cell whose three faces act as capacitive evidence/synapse walls and whose fourth face is a controlled electrical connection/output.
- **Nervous Core Scaffold (NCS):** a non-silicon interior support/fill containing electrically isolated controlled conductors or junctions, rather than one continuous conductive material.
- **Wall-Integrated Analog Steering (WIAS):** the fourth face of a TWGC directly uses the cell's analog evidence to steer a neighboring competition node instead of first generating a separate full-swing reader event.

## 1. Two interpretations tested

### Interpretation A — empty hollow shell

Active regions live on inner/outer surfaces. The cavity remains electrically empty except for sparse promoted Myelin chords.

Advantages:
- low unintended dielectric coupling;
- simple separation between regions;
- direct cross-cavity chords can shorten repeated routes;
- the cavity can be used as routing volume.

Weakness:
- if the shell only uses local surface neighbors, the routing improvement is modest.

For a 6x6x6 boundary model (152 surface cells):
- local shell: average 6.646 hops, p95 11, max 15, 300 local links.

### Interpretation B — replace unused interior silicon with something functional

The active semiconductor still has to exist where transistors are built, but non-active interior volume can in principle be replaced by a structural/insulating fill or package material containing controlled conductors.

Three variants were screened:

1. **continuous conductive fill — REJECT**
   - cells touching the same conductor tend toward the same potential;
   - analog states short/share charge;
   - selectivity is lost.

2. **ordinary orthogonal 3D neighbor mesh — REJECT as a density trade**
   - full 6x6x6 local 3D mesh: average shell-to-shell path 6.504 hops;
   - only ~2.1% better than the empty shell;
   - requires 540 links instead of 300 (~1.8x link inventory).

3. **structured controlled core — KEEP**
   - local shell plus one controlled inward connection per surface cell and a six-face core network:
   - average logical path ~3.358 hops (~49.5% fewer than shell local-only);
   - link inventory 458 (~1.53x shell).
   - however, when straight-line physical lengths are assigned to the inward/core links, average normalized geometric route is ~5.876 vs 6.646 for the shell: only ~11.6% shorter.

This means a generic central hub is not enough. The useful core must promote **sparse direct chords that approximate the Euclidean A-to-E direction**, rather than sending everything through one center.

The average straight-line lower bound between shell cells in this model is ~4.409 normalized units, ~33.7% below the local-shell route. That is the physical opportunity for learned/promoted cross-cavity chords.

## 2. Three capacitor walls map directly onto Grammar

The current legal 2x2 um SKY130 MIM is approximately 9.52 fF typical.

If three equal wall capacitors feed one 40 fF local dendrite and each active wall receives a 0.2 V event, first-order charge division gives:

- three active walls: 0.523314 V from a 0.44 V baseline;
- two active walls: 0.495543 V;
- exact-partial separation: 27.77 mV.

This is strikingly close to the historical v12N 3-input Grammar behavior (~0.522 V exact, ~0.495 V partial).

So the user's geometry is not merely packaging decoration: **three capacitive faces can literally implement the three-input Grammar evidence structure.**

A three-wall cell using 2x2-equivalent wall area has about:
- 28.56 fF total coupling area-equivalent;
- three physical input surfaces;
- one remaining face for local output/contact.

Literal vertical sidewall MIM is not available in the present SKY130 PDK. v13A7 only proved ordinary MIM-over-transistor vertical overlap. The TWGC is therefore a future/custom-process geometry target; in SKY130 it can be emulated using three planar MIMs arranged above/around the local logic.

## 3. Raw touching is not sufficient

A passive chain of equal 28.56 fF cells shows why uncontrolled contact propagation is unsafe.

Starting from a stored 0.2 V charge packet and sequentially charge-sharing through equal cells:

- A: 200 mV
- B: 100 mV
- C: 50 mV
- D: 25 mV
- E: 12.5 mV

If five equal cells are all connected at once, the final common voltage is ~40 mV.

A direct A-to-E connection shares between only two equal cells and gives ~100 mV.

Therefore the user's diagonal shortcut intuition is electrically useful: **fewer passive contacts means less charge dilution.** But it also proves that a long raw-touch chain cannot replace Myelin/regeneration.

Selected rule:
- 1 short analog contact: allowed if margin is characterized;
- repeated deep touch chain: regenerate or promote a direct chord;
- robust/exact information: use full-swing routing.

## 4. Wall-Integrated Analog Steering — analog reader interpretation

The closed v13A5/v13A6 dual-pair reader remains the safe robust boundary.

For local analog destinations, the TWGC can avoid a separate reader:

```
three capacitor walls
        |
        v
  local evidence node
        |
 fourth-face weak MOS/contact
        |
        v
neighbor inhibition/competition
```

The fourth-face device does not digitize the voltage. Its conductance is directly changed by the stored wall evidence, reusing the v12G direct-electricity principle.

The v13B1 screen already showed the present Grammar GC/GR polarity can directly steer a compact 100 fF destination competition at TT/FF/SS using weak W=0.42 um / L=12 um shunts. v13B2 therefore keeps WIAS as the default first attempt when the destination already contains an analog membrane/competition node.

Do not add a new membrane only to avoid the ~80-100 fJ robust reader. If a robust event is needed, use the closed dual-pair reader.

## 5. What should fill the interior?

### Empty/air/vacuum cavity
KEEP as the lowest-coupling reference architecture, but do not claim thermal benefit without an actual heat path.

### One conductive material
REJECT. It creates common-potential/shorting behavior.

### Random touching nanowire material
KEEP only as an experimental reservoir/associative layer. Published 3D nanowire networks demonstrate multiple current paths and history-dependent neuromorphic dynamics, but not deterministic exact routing.

### Insulating structural fill with embedded controlled conductors
SELECT as the most practical interpretation of the user's 'put something inside and connect it' idea.

Packaging technologies already demonstrate copper vertical interconnects embedded in non-conductive mold/epoxy material (through-mold vias). GVS would need a much finer/custom implementation for cell-scale routing, but the material concept is physically established: **mechanical/insulating bulk plus isolated conductors**, not a solid conductor.

Preferred NCS contents:
- insulating structural matrix;
- sparse copper/metal or future programmable conductors;
- controlled junction at each cell boundary;
- promoted Myelin chords for hot long-range routes;
- optional thermally useful electrically insulating filler if packaging requires it.

## 6. Selected combined architecture

```
          outer surface
  [C][C][C][contact]
        TWGC
          |
          | controlled local contact
          v
  ===========================
  insulating Nervous Core Scaffold
      \        |        /
       \   Myelin      /
        \   chord     /
         \     |     /
  ===========================
          ^
          | controlled contact
  [C][C][C][contact]
        TWGC
          inner surface
```

Here `[C]` is a capacitor wall.

The shell is still 'hollow' in the sense that it does not contain a solid active silicon block. The interior is instead a structured routing/support volume.

## 7. Decision

KEEP:
- three capacitor walls + one controlled connection face;
- analog fourth-face steering for already-analog local destinations;
- sparse diagonal/cross-cavity Myelin chords;
- insulating/structural core with isolated conductors;
- exact/global routing for cold/changeable/precise state.

REJECT:
- continuous conductive fill;
- unlimited passive touch propagation;
- dense all-to-all diagonals;
- replacing the closed robust reader everywhere before independent mismatch of the readerless path is proven.

## 8. Next physical experiment

Do not fabricate a hollow package yet.

First emulate one TWGC in the existing SKY130 flow:
1. use three legal 2x2 MIMs as the three capacitor walls;
2. place the three MIMs directly above/around a compact local evidence node using the v13A7 vertical-overlap rule;
3. make the fourth logical face a weak controlled MOS output/contact;
4. connect it directly to an existing local competition node;
5. compare readerless analog steering versus the closed dual-pair robust reader;
6. measure PVT, independent mismatch, crosstalk, area, and event energy;
7. if one-hop analog contact passes, place two cells with one promoted direct chord and compare against two sequential contacts.

Only if that emulation wins should v13B move toward a true hollow/filled-core package.