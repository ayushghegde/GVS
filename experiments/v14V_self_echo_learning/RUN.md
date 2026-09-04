# v14V exact run

## Main engineering experiment

```bash
python3 experiments/v14V_self_echo_learning/source/run_v14v.py > experiments/v14V_self_echo_learning/run.log
```

The script writes `results/results.json`. Dependencies: Python 3 and NumPy. Random seeds are fixed in source. The self-tag and ETG screens use 1,000,000 Monte Carlo trials; the sequential learning screen uses deterministic seeds.

## Physical evidence

The persisted `.mag`, `.ext`, and extraction logs under `physical/` are the rerun Magic/SKY130A TEACH-mesh proxies. Their DRC/extraction results are parsed by the report/results. They do not model HZO or the custom ionic devices.
