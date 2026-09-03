# v14U reproducible run

```bash
python3 experiments/v14U_sparse_active_spine/source/run_v14u.py > experiments/v14U_sparse_active_spine/run.log
```

The script writes `results/results.json`. It preserves the previously recorded 8x8/16x16 SKY130 extraction summaries and reruns the HZO inhibit pulse sweep, hollow-rib elastic screen, DPD energy proxy and transistor accounting. Raw 16x16 extraction files are not claimed to be regenerated.
