# Reproduction

## Physical branch-mouth proxy

The Magic command file is `physical/choice5_m2.cmd` and generated `physical/v14r_choice5_m2.mag` / `.ext`.

Example command used from the physical working directory:

```bash
/mnt/data/gvs_v14r_tools/magic/install/bin/magic \
  -d null \
  -T /mnt/data/gvs_v14r_tools/common/sky130A/libs.tech/magic/sky130A.tech \
  < choice5_m2.cmd > choice5_m2.log 2>&1
```

The log must report `Total DRC errors found: 0`. The `.ext` file contains the CHOICE node and five explicit CHOICE-to-branch capacitances used by `source/run_v14r.py`.

## Combined model

```bash
python source/run_v14r.py
```

This writes `results/results.json`. The model uses deterministic seed families recorded directly in the script.
