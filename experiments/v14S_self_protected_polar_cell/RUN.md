# v14S exact run

## Main experiment

```bash
python3 experiments/v14S_self_protected_polar_cell/source/run_v14s.py > experiments/v14S_self_protected_polar_cell/run.log
```

The script writes `results/results.json` itself. Random seeds are fixed in the source; the main six-way race uses seed `141506` and 300,000 trials. Polarization-floor screens use deterministic seeds derived from the polarization point.

Dependencies: Python 3, NumPy, SciPy. No SPICE compact model is used for the new HZO/inhibit/guided-gap compound device. The real capacitance input is the inherited v14R Magic/SKY130 extraction copied under `inherited/`.

## Optional v12S reference recount

```bash
python3 experiments/v14S_self_protected_polar_cell/source/count_v12s_reference.py /path/to/v12s_complete_autonomous_tile.cir
```
