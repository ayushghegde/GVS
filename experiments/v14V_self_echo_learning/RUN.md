# v14V exact runs

## Main engineering experiment

```bash
cd experiments/v14V_self_addressed_polarity_fabric
python3 source/run_v14v.py > run.log
```

The script writes `results/results.json`. Dependencies: Python 3, NumPy and Numba. Random seeds are fixed in source. The selected self-tag and ETG screens use 1,000,000 Monte Carlo trials; the corrected sequential learning screen uses 20 deterministic seeds.

## Physical TEACH mesh extraction

The original run used Magic 8.3.681 built from the supplied archive and SKY130A technology version `1.0.602-0-gf3c505b`.

256-cell proxy:

```bash
cd physical
/mnt/data/gvs_v14v_tools/magic_install/bin/magic -dnull \
  -T /mnt/data/gvs_v14v_tools/common/sky130A/libs.tech/magic/sky130A.tech \
  v14v_teach_mesh
```

At the Magic prompt:

```text
:drc check
:drc count total
:extract do local
:extract all
:quit -noprompt
```

Repeat with `v14v_teach_mesh_8x8` for the 64-cell proxy.

Both original extraction logs and `.ext` files are persisted under `physical/`.
