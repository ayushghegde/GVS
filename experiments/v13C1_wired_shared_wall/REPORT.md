# Neural Glyph v13C1 — Wired Shared Wall / Service Spine

**Verdict: PASS as a current-process physical proxy. Wires/services can occupy a shared structural wall, but they must be electrically isolated and shielded from the weak capacitor faces. An unshielded service line in the wall can inject a disturbance comparable to the entire ~25 mV Tri-Wall decision margin; a shielded service spine removed the direct extracted service-to-evidence coupling term in the tested 100 um SKY130 slice.**

## Terms

- **Service Spine Wall (SSW):** a shared wall whose two outer faces belong to neighboring analog cells while its protected middle carries power/config/recovery/event wires and reference shields.
- **TSV (through-silicon via):** a conductor formed through silicon, normally isolated from the silicon by dielectric/barrier layers.
- **Shield rail:** a robust reference/ground conductor placed between a noisy service wire and a weak analog node to intercept electric-field coupling.
- **Service lane:** one embedded robust wire for power, configuration, recovery, pilot/PVT state, or robust events; it is not a weak high-impedance Grammar wire.

## 1. Can wires physically be placed in a silicon/shared wall?

Yes in principle. Existing semiconductor technology already puts conductors through silicon using TSVs, and advanced interconnect research also uses buried power rails/nano-TSVs inside the front-end structure. The conductor cannot simply be bare metal touching active silicon: it needs dielectric isolation/barrier structures to prevent leakage/contamination and to control stress.

The present SKY130 open PDK does not provide a process module for true TSV/buried-wall fabrication, so v13C1 does not claim a fabricated literal vertical wall. Instead, it tests the electrical rule using a real SKY130 metal/extraction proxy: two weak analog faces with a service conductor inside the shared-wall cross-section, first unshielded and then shielded.

## 2. Physical proxy: unshielded service wire

A 100 um-long SKY130 M4 slice was drawn as:

`A_EVID | SERVICE | B_EVID`

All three conductors are parallel and the overall analog-face separation is kept large enough for a wall-like cross-section.

Result:

- DRC: **0**
- SERVICE -> A_EVID extracted mutual capacitance: **1.18388 fF**
- SERVICE -> B_EVID: **1.18388 fF**
- SERVICE ground-referenced capacitance: **2.79459 fF**

Using the present ~72 fF Tri-Wall evidence-node proxy, a full 1.8 V service transition can produce roughly **29.1 mV** of charge-sharing kick on an unshielded evidence node.

That is larger than the useful ~24-25 mV transferred exact/partial separation of v13B3/B4.

**Decision: an unshielded switching wire inside the shared wall is rejected next to weak analog capacitor faces.**

## 3. Physical proxy: shielded service spine

The same 100 um slice was redrawn as:

`A_EVID | SHIELD_A | SERVICE | SHIELD_B | B_EVID`

Both shield conductors are intended to be tied to a robust reference/ground elsewhere. They do not need to short together locally.

Result:

- DRC: **0**
- extracted SERVICE <-> SHIELD terms: about **2.27 fF** and **2.51 fF**
- extracted A_EVID <-> its shield: **2.27 fF**
- extracted B_EVID <-> its shield: **2.51 fF**
- **no direct SERVICE <-> A_EVID or SERVICE <-> B_EVID capacitor term appears in the extracted network** at this geometry/extractor resolution.

This does not prove mathematically zero coupling; it means the shielding pushed direct coupling below the extraction reporting level in this physical proxy.

The cost is extra service-line capacitance. Effective service-line load proxy rises from about **5.16 fF** unshielded to about **6.23 fF** shielded when mutual terms are included.

Ideal full charge/discharge source-work proxy:

- shielded 100 um service lane at 1.2 V: **~8.97 fJ/cycle**
- at 1.8 V: **~20.19 fJ/cycle**

This is acceptable for slow configuration, pilot/PVT state, recovery control, or robust regional events; it is not a reason to toggle the wall spine for every sub-fJ local analog event.

## 4. Two wires inside one wall

A second physical extraction used:

`A_EVID | SHIELD_A | SERVICE0 | SERVICE1 | SHIELD_B | B_EVID`

Result:

- DRC: **0**
- direct service-to-evidence terms again did not appear in extraction;
- SERVICE0 <-> SERVICE1 mutual capacitance: **2.38579 fF / 100 um**;
- each service line couples strongly to its adjacent shield (~2.166 fF / 100 um).

Therefore multiple robust wires can share the protected middle of the wall, but two high-activity service wires can couple to each other. If they carry timing-sensitive signals, interleave extra shields or use orthogonal/different-layer routing. If they carry slow configuration/recovery/power, the coupling is much less problematic.

## 5. Selected shared-wall stack

Conceptual cross-section:

```
CELL A weak state
    |
capacitor face A
    |
dielectric
    |
SHIELD / REF A
    |
robust service lanes:
  - static/promoted fourth-face enable
  - validated-use / environment-pilot line
  - recovery rail
  - power/ground
  - robust Myelin/event lane when required
    |
SHIELD / REF B
    |
dielectric
    |
capacitor face B
    |
CELL B weak state
```

The shared wall is therefore not just structural silicon. It becomes protected infrastructure, like a building wall carrying utilities.

## 6. What must NOT be put in the service spine by default

- raw GC/GR Grammar candidate/reference nodes;
- tiny dendrite voltages;
- regenerative-latch internal nodes;
- raw analog lease storage;
- any other high-impedance state whose information is only a few millivolts.

Those stay on the cell side of the shield.

## 7. What SHOULD use the wall

- static or slowly changing fourth-face promotion/configuration;
- shared v12A-style PVT/environment pilot state;
- one-way expired-charge recovery rail from v11V/W/v12I;
- VDD/GND/reference distribution;
- robust full-swing winner/event signals;
- sparse Myelin-chord landing/control;
- exact-computer request/result if the physical wall is the nearest route.

## 8. v13C architecture consequence

The shared wall now has three roles simultaneously:

1. **structure** — removes duplicate cell shells/framework;
2. **computation surface** — capacitor face for cell A and a separate capacitor face for cell B;
3. **protected infrastructure** — wires, recovery, reference, power and slow configuration in the middle.

This is materially better than giving each cell an independent shell plus separate routing channels.

## 9. Acceptance / limits

PASS for the electrical-layout proxy:
- 0 DRC in unshielded, one-service shielded, and two-service shielded slices;
- unshielded service coupling is large enough to threaten the analog margin;
- shielded geometry suppresses direct extracted service/evidence coupling;
- two service lanes are physically plausible but couple to each other and should be treated as robust/slow lanes.

NOT YET PROVEN:
- literal vertical sidewall fabrication in SKY130;
- mechanical strength of a real hollow framework;
- TSV stress/thermal effects next to analog cells;
- maximum safe number/density of service lanes;
- full 3D package manufacturing cost/yield.

## 10. Next v13C experiment

Build one eight-cell framework slice where four shared walls carry:

- two v12A-style environment-pilot/service lanes;
- one validated residual/recovery lane;
- one static/promoted fourth-face enable lane;
- local Tri-Wall evidence on the protected faces;
- one direct Myelin-chord endpoint.

Then compare against the same eight cells with separate walls + separate routing. Measure framework material/area proxy, extracted wall-wire capacitance, evidence crosstalk, promotion energy, recovered cleanup charge, and total local-region energy.
