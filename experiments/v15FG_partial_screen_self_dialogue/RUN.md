# Run v15FG

```bash
NGSPICE=/path/to/ngspice python source/run_v15fg.py
```

Selected local run used ngspice built from the supplied `ngspice-master.zip` plus Python 3 / NumPy / SciPy.

The script writes `results/results.json` and reruns `spice/screen_10.cir` when ngspice is available.
