# Neural Glyph v13D2 — Decentralized Physics Screen

**Verdict: SELECT a multi-timescale physical hierarchy: electricity for fast computation and routing state, temperature/leak physics for slow local health/congestion adaptation, and magnetic nonvolatile state only as a future-process consolidation anchor. Do not use heat or magnetism as the normal carrier of weak per-event reasoning.**

## New terms

- **Autonomic State Ladder:** different physical mechanisms are assigned to the time scale they naturally handle best rather than forcing one mechanism to do everything.
- **Thermal Brake:** local temperature-sensitive replica/leak devices automatically increase inhibition, tap decay, or promotion difficulty when a region becomes hot; no software temperature table is needed in the fast path.
- **Magnetic Anchor:** a future nonvolatile magnetic bit/device stores a fully verified long-lived route/promotion state so it survives power loss without continuous refresh.

## 1. Electricity — SELECT for fast and medium state

This remains the strongest GVS mechanism because old experiments already showed one electrical state can represent several useful meanings.

Recovered roles:

- event/evidence;
- repetition/familiarity (v12E);
- fatigue/homeostasis (v12F);
- short context (v12G);
- ambiguity/recycle state (v12H/I);
- physical lease/hotness (v12P);
- validated cleanup -> recovery (v11V/W, v12I).

v13D adds tap configuration:

`validated repeated use -> familiarity charge -> temporary tap -> slow lease/use charge -> promoted tap/Myelin`

This is decentralized because the cell/tap's own charge determines its state.

## 2. Heat — SELECT only as slow environment feedback

Heat is spatially diffuse and slow compared with local electrical events. That makes it poor for encoding exact route identity or fast reasoning, but useful for **regional health state**.

Old v11U/v12A already gives the implementation direction: use small replica leak devices whose current naturally depends on process and temperature but does not see route activity.

### Thermal Brake behavior

`local temperature/leak rises -> replica current rises -> Environment Reservoir changes -> promotion threshold rises / tap retention shortens / inhibition increases`

When the region cools, the replica state decays and normal thresholds return.

This is more useful than adding a digital thermal-management lookup into every cell.

### What heat must not do

- select the exact destination of a fast event;
- encode a few-millivolt candidate/reference decision;
- directly train a route merely because a hot neighboring block warmed it;
- be counted as recovered energy without an actual temperature gradient and thermoelectric device.

A future package-level thermoelectric element can be considered only after a measured thermal gradient exists. v11W correctly counted heat recovery as zero in its pass.

## 3. Magnetism — FUTURE_PROCESS for persistent verified structure

Magnetic memory is attractive for a different reason: nonvolatility. A promoted relation that is stable over very long times does not need to leak away and be rebuilt after power loss.

### Magnetic Anchor policy

The magnetic state is **not** trained directly from raw events.

Sequence:

1. electrical familiarity/lease learns locally;
2. exact/conservative validation confirms the relation during rare consolidation;
3. only then a magnetic/nonvolatile anchor may store `PROMOTED/VALID` or a small route/config state;
4. runtime events still move electrically/capacitively.

This avoids trying to use a relatively expensive magnetic write for every inference event.

### Why it is future-only

The current SKY130 flow has no MRAM device module. Adding STT/SOT/other magnetic devices changes the manufacturing process and write/read circuitry. Therefore magnetic anchoring is a `FUTURE_PROCESS` option, not a dependency of v13D silicon.

## 4. Selected decentralized hierarchy

```
FAST, LOCAL
  electrical event/evidence
        |
        v
  local capacitor wall / receptor
        |
  familiarity + competition + tap
        |
        v
MEDIUM
  electrical lease / use / fatigue
        |
        +---- local Thermal Brake changes thresholds/decay
        |
        v
RARE CONSOLIDATION
  exact verification
        |
        +---- static CMOS config now
        |
        +---- future Magnetic Anchor if process supports it
        v
EXPIRED CHARGE
  one-way recovery rail
```

No central scheduler needs to decide each tap, threshold, fatigue state or recovery event.

## 5. Decentralization boundaries

Decentralization is useful only when local physics has enough information to make the decision safely.

### Fully local/physical

- short event routing;
- repetition/familiarity;
- tap temporary enable;
- homeostatic congestion suppression;
- PVT/thermal threshold adjustment;
- lease decay;
- expired-charge collection.

### Rare exact support remains

- semantic validity after learning changes;
- exact arithmetic/code/state;
- resolving low-margin ambiguity;
- verifying a route before permanent/nonvolatile consolidation.

This is not central control of every event. It is an occasional correctness boundary.

## 6. v13D architectural decision

Do not choose between electricity, heat and magnetism as if only one is allowed.

Use each for what it naturally does well:

- **electricity/charge:** fast information and local adaptation;
- **heat/leak:** slow local environmental feedback;
- **magnetism:** future persistent verified configuration;
- **exact computer:** rare precision/semantic correction.

The next physical work remains electrical because it is manufacturable in the current flow: a four/eight-tap Autonomic Tap Spine with familiarity, homeostatic loading control, replica-PVT thresholding and post-decision recovery. Thermal effects are injected through the real corner/temperature-dependent replica devices. Magnetic anchoring stays a later technology option.
