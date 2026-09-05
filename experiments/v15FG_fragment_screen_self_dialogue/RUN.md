# Run

```bash
python source/run_v15fg.py
```

The script uses NumPy only and writes `results/results.json`.

Recommended reproducibility check:
```bash
python source/run_v15fg.py > run.log
sha256sum results/results.json
```
