# Neural Glyph v13D1 — Autonomic Tap Spine vs Fourth Face

**Verdict: HYBRID PASS. A dedicated fourth-face contact is better for one short private analog neighbor relation; a shared trunk with short cell subwires is better for repeated regional event/control fanout, provided the taps are electrically isolated, mostly static after promotion, and the weak analog state is regenerated locally rather than broadcast onto a heavily loaded analog trunk.**

## New terms

- **Autonomic Tap Spine (ATS):** a protected shared inter-cell trunk running in the service wall, with tiny local subwires/taps into cells; each tap can enable itself from local validated electrical familiarity rather than a central router.
- **Tap receptor:** the small local landing capacitance at the end of a subwire; it converts a shared event into local cell evidence without attaching the entire cell membrane to the trunk.
- **Segmented analog spine:** a weak-analog trunk divided by local isolation switches so only the nearby segment/tap capacitance is visible to the source.

## Inputs reused from measured/extracted earlier work

This is an architecture model using earlier physical measurements; it is not a new full 8-cell PEX.

- Tri-Wall evidence node proxy: ~72 fF.
- useful exact/partial differential: use 25 mV nominal screening value.
- Contact Receptor: 3 fF.
- v13C1 shielded service lane: ~6.231 fF / 100 um effective protected-wire capacitance.
- v13B4 promoted fourth-face gate work proxy: ~1.2 fJ at 1.2 V.
- local three-wall event source-work proxy: ~0.68 fJ for the exact case.

## 1. Direct fourth face

A source connected only to one 3 fF receptor retains, by first-order charge sharing:

`25 mV * 72/(72+3) = 24.0 mV`

This is excellent local analog fidelity.

Therefore **do not delete the fourth face**. For a directly adjacent private analog relation, it remains the smallest-capacitance path.

## 2. One selected subwire from a shared 100 um trunk

Model one 100 um protected trunk + eight 10 um physical branches. The wire inventory is 180 um total, corresponding to ~11.216 fF using the v13C1 extraction-per-length proxy.

If only **one 3 fF receptor is electrically active**, total extra load is ~14.216 fF and the 25 mV source differential arrives as:

**~20.88 mV**.

This remains above both the 18 mV screening boundary and a stricter 20 mV local target.

So a shared spine with subwires can carry weak analog state *if only a small selected portion is visible*.

## 3. All eight analog taps active — reject

If all eight 3 fF receptors are simultaneously attached to the same full analog spine:

- total load ~35.216 fF;
- transferred differential ~**16.79 mV**.

That falls below the present 18 mV high-margin screen.

**Decision: do not use one unsegmented weak-analog bus with all cell receptors continuously attached.**

## 4. Segmentation fixes most of the loss

One selected 25 um trunk segment + 10 um branch + 3 fF receptor:

- load ~5.181 fF;
- transferred differential ~**23.32 mV**.

One selected 50 um segment + 10 um branch:

- load ~6.739 fF;
- differential ~**22.86 mV**.

Therefore the right analog interpretation is not a global analog wire. It is **short segmented analog spines that self-isolate unused sections**.

## 5. Maximum simultaneous analog taps

For the full 180 um protected-wire inventory:

- >=20 mV target: at most **2** active 3 fF taps;
- >=18 mV target: at most **5** active taps.

For a 35 um selected segment:

- >=20 mV: up to **5** active taps;
- >=18 mV: all **8** can remain above the screen in the first-order model.

This creates a direct use for the old v12F electric-homeostasis principle: pooled tap activity should automatically raise inhibition/selection pressure when too many taps are simultaneously loading one analog segment.

## 6. Event spine is better than analog spine for regional fanout

A stronger architecture is to let the shared spine carry a local event pulse, then let each destination's capacitor wall turn that event back into local analog evidence.

The v13C2 180 um protected wire inventory is ~11.216 fF. A conservative `C*V^2` full-pulse proxy at a 0.2 V local event is only about **0.449 fJ** for the shared wire itself.

Assume a promoted tap is already static, so no per-event tap-gate transition is required.

Then:

`shared event spine energy proxy = ~0.449 fJ wire + 0.68 fJ per active destination wall`

Compare with independently toggling a 1.2 V fourth-face gate for every destination:

`dedicated fourth-face proxy = ~1.2 fJ gate + 0.68 fJ wall per destination`

At fanout 1 the static shared-spine proxy is ~1.13 fJ versus ~1.88 fJ; at fanout 8 it is ~5.89 fJ versus ~15.04 fJ, about **61% lower** in this simplified routing/control proxy.

This excludes drivers, source switches, vias and actual timing, so it is not a whole-region energy claim.

If every tap gate must switch dynamically each event, the advantage disappears. Therefore **self-setting/static promoted taps are essential**.

## 7. Old v12E repetition solves tap self-configuration better than a central counter

Preserved v12E self-referenced repetition:

- first validated firing: only ~1.3-1.6 mV differential;
- second: ~16.8-17.2 mV;
- third: ~28.2-28.6 mV across TT, SS/85C and one mismatch seed.

Selected v13D policy:

- first use: no structural change;
- second close use: probation;
- third validated close use: enough electrical familiarity for a **temporary tap** because the familiarity margin is now around 28 mV;
- longer-term repeated success writes the slower v12P/v13B4 lease/use state and may consolidate the tap/Myelin relation.

This gives two physical learning timescales without a software reuse counter.

## 8. Selected topology

```
         protected Service Spine Wall
================================================
 robust/local event trunk
================================================
      |        |        |        |
   short tap short tap short tap short tap
      |        |        |        |
   receptor receptor receptor receptor
      |        |        |        |
  capacitor  capacitor  capacitor  capacitor
    walls      walls      walls      walls
      |        |        |        |
   local competition / Grammar / template
```

Each tap owns local charge state. A central router does not decide each event.

### Local rule

`validated repetition -> local familiarity rises -> tap opens temporarily -> continued usefulness -> slow lease/use state promotes it -> inactivity/fatigue closes it`

### Congestion rule

`too many simultaneous taps -> shared electrical homeostat/inhibition rises -> fewer taps remain active`

## 9. Fourth face versus subwire: final decision

### Fourth face wins when

- A and E are direct physical neighbors;
- the signal is weak analog evidence;
- only one/few private destinations need it;
- minimum loading matters more than configurability.

### Subwire/tap spine wins when

- several cells share the same event/control source;
- the route is regional rather than face-to-face;
- a connection must be reconfigurable after fabrication;
- the trunk can be shielded and taps can remain static over a burst;
- local capacitor walls regenerate the event into local analog evidence.

### Segmented analog tap wins in the middle

For short local non-neighbor analog routes, a segmented spine with only one/few active taps preserves ~23 mV class margin while avoiding a dedicated long fourth-face-style point-to-point conductor.

## 10. v13D conclusion

The subwire is **not a replacement for the fourth face**. It is a second routing scale.

Selected hierarchy:

1. direct fourth face = nearest-neighbor analog synapse/contact;
2. segmented analog tap spine = short local non-neighbor analog relation;
3. protected event spine + local capacitor tap = regional shared event/control;
4. Myelin chord = stable hot long-range relation;
5. exact/global fabric = changing/cold/precise relation.

The next physical experiment must build one shielded trunk with at least four local taps, give each tap a v12E-style familiarity trace, and verify that only repeated validated use opens a tap while electrical homeostasis prevents excess simultaneous analog loading.
