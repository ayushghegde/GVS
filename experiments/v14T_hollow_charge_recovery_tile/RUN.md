# v14T exact run

## Physical SKY130 program-grid proxy

```bash
cd experiments/v14T_hollow_charge_recovery_tile/physical
printf ':drc check\n:drc count total\n:extract do local\n:extract all\n:quit -noprompt\n' | \
  script -qec '/path/to/magic -dnull -T /path/to/sky130A.tech v14t_program_porch_proxy' extract_proxy.log
```

Tool used in this run: Magic 8.3.681 built from the supplied archive; SKY130A technology reports version `1.0.602-0-gf3c505b`.

## System/model sweep

```bash
python3 experiments/v14T_hollow_charge_recovery_tile/source/run_v14t.py \
  > experiments/v14T_hollow_charge_recovery_tile/run.log
```

The script parses the physical `.ext` file and writes `results/results.json`. No SPICE compact model is claimed for the hollow reservoir, recovery network, HZO, or guided-gap device.
