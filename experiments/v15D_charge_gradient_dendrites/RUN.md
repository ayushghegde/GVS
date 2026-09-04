# Run v15D

Required local tools for the recorded run:
- Python 3 + NumPy
- ngspice built from the supplied `ngspice-master.zip`

Commands:
```bash
NGSPICE_BIN=/mnt/data/ngbuild/install/bin/ngspice \
python /mnt/data/v15D_charge_gradient_dendrites/source/run_v15d.py
```

The script reruns the ngspice decks in `spice/` and writes `results/results.json`.

The coupled charge/HZO helper is `source/coupled_charge_hzo.py`.
