# v13P8 physical screen — SKY130 metal membrane

## What was physically tested

Magic 8.3.681 was rebuilt from the supplied source and run with the supplied SKY130A technology. The candidate membrane was implemented as:

- ROW coupling conductor on M2;
- one continuous membrane conductor on M3;
- COLUMN coupling conductor on M4;
- ROW and COLUMN placed over separate parts of the membrane so they do not directly overlap each other;
- the two M3 membrane pads joined by a narrow M3 neck.

This is intentionally a physical metal membrane, not an ideal lumped capacitor.

## Extracted sweep

All listed geometries had 0 DRC errors.

| square input pads | Cmem->substrate | ROW->MEM | COL->MEM | ROW<->COL |
|---|---:|---:|---:|---:|
| 1.5 um | 0.497622 fF | 0.215424 fF | 0.223404 fF | ~0 |
| 2.0 um | 0.648568 fF | 0.372559 fF | 0.380659 fF | ~0 |
| 2.5 um | 0.805699 fF | 0.573111 fF | 0.580455 fF | ~0 |
| 3.0 um | 0.969016 fF | 0.816962 fF | 0.822597 fF | ~0 |
| 3.5 um | 1.138520 fF | 1.104040 fF | 1.106980 fF | ~0 |

The result is useful because the membrane's own substrate capacitance and its two synaptic couplings scale together naturally. The physical geometry therefore performs both storage and evidence accumulation without a separate MIM capacitor.

## Compact candidate

For 2.0 um pads:

- Cmem = 0.648568 fF
- Crow = 0.372559 fF
- Ccol = 0.380659 fF
- direct row/column coupling was not reported by extraction

At 1.8 V ideal charge sharing gives approximately:

- row only = 0.478 V
- column only = 0.489 V
- row+column = 0.967 V

With independent +/-20% stress applied to Cmem, Crow and Ccol, the worst capacitor-only discrimination band is approximately:

- maximum one-input level = 0.646 V
- minimum two-input level = 0.785 V
- remaining sensing window = about 140 mV

This is the current best area-oriented candidate.

## Centered-threshold candidate

Starting from 2.5 um pads, a narrow M3-only tail was added to raise membrane capacitance without substantially increasing input coupling. A 2.0 um long, 0.5 um wide tail produced:

- Cmem = 0.9820 fF
- Crow = 0.5739 fF
- Ccol = 0.6092 fF
- Cm/Csyn(avg) = ~1.66
- DRC = 0

Ideal levels:

- row only = ~0.477 V
- column only = ~0.506 V
- row+column = ~0.984 V

With +/-20% capacitor stress:

- maximum one-input level = ~0.666 V
- minimum two-input level = ~0.802 V
- remaining sensing window = ~136 mV

This geometry centers the window near the previously recorded ~0.73 V nominal standard-NFET threshold, but uses more metal area than the compact version.

## Important result

The original concern in v13P7 was that a capacitive receiver might require a large intentional MIM at every tile. This physical experiment shows that is not necessary: ordinary M2/M3/M4 geometry can generate sub-fF synaptic coupling and membrane storage with zero DRC errors.

So the capacitance idea is physically credible enough to continue.

## What is still unsolved

Do not call the receiver solved yet. We still need:

- sensing NFET/inverter threshold across TT/FF/SS;
- mismatch screen;
- leakage and membrane decay versus event-pulse spacing;
- reset/bleed implementation;
- receiver output regeneration;
- area/energy comparison against the v13P7 two-key MOS receiver.

If threshold spread cannot be kept inside a practical membrane window, the capacitive receiver should remain an optional prefilter and the conventional two-key MOS receiver should remain the exact inter-tile selector.
