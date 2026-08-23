#!/usr/bin/env python3
"""v13L0 differential neurovascular isolation stress model.

Evidence class: architecture/circuit proxy only. This script does not claim PEX.
It reuses v13K's conservative values and asks how *asymmetric* service coupling
changes the differential Grammar margin.
"""

import csv
from pathlib import Path

C_NODE_FF = 72.0
COUPLING_FF = 0.124
V_NERVE = 0.200
V_ARTERY = 0.0903
BASE_MARGIN_V = 0.025
HIGH_MARGIN_V = 0.018

OUT = Path(__file__).with_name("differential_stress.csv")


def differential_kick_v(scale, n_nerve, n_artery, asymmetry):
    """Worst-direction differential kick.

    asymmetry = (C_candidate - C_reference) / (C_candidate + C_reference)
    when the pair average equals COUPLING_FF * scale.
    """
    c_avg = COUPLING_FF * scale
    service_volt_seconds = n_nerve * V_NERVE + n_artery * V_ARTERY
    return 2.0 * asymmetry * c_avg / C_NODE_FF * service_volt_seconds


def max_asymmetry_for_high_margin(scale, n_nerve, n_artery):
    budget_v = BASE_MARGIN_V - HIGH_MARGIN_V
    c_avg = COUPLING_FF * scale
    service_volt_seconds = n_nerve * V_NERVE + n_artery * V_ARTERY
    return budget_v * C_NODE_FF / (2.0 * c_avg * service_volt_seconds)


def main():
    rows = []
    for scale in (0.5, 1.0, 1.5, 2.0):
        for n_nerve, n_artery in ((1, 1), (4, 4), (8, 8), (8, 32), (16, 16), (32, 32)):
            max_a = max_asymmetry_for_high_margin(scale, n_nerve, n_artery)
            for asym in (0.0, 0.1, 0.2, 0.3, 0.5, 1.0):
                kick = differential_kick_v(scale, n_nerve, n_artery, asym)
                remaining = BASE_MARGIN_V - kick
                rows.append({
                    "coupling_scale": scale,
                    "nerve_transitions": n_nerve,
                    "artery_transitions": n_artery,
                    "normalized_asymmetry": asym,
                    "differential_kick_mV": 1000.0 * kick,
                    "remaining_margin_mV": 1000.0 * remaining,
                    "high_margin_pass": remaining >= HIGH_MARGIN_V,
                    "max_asymmetry_for_18mV": max_a,
                })

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
