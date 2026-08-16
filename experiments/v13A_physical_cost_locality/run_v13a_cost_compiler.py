#!/usr/bin/env python3
import math
import pandas as pd

WIRE_EVENT_FJ = 680.0
RESERVE = 0.10

DOMAINS = [
    ("image", 47555.555556, 26171.370756, 16),
    ("sound_raw", 1183200.0, 506700.257169, 480),
    ("sound_grammar", 1183200.0, 506700.257169, 160),
    ("code", 99200.0, 40.855933, 47),
    ("reasoning", 10800.0, 1060.596698, 12),
]

def min_burst(exact_fj, hybrid_fj, events, cost_factor):
    long_event = WIRE_EVENT_FJ * cost_factor
    max_comm = (1.0 - RESERVE) * exact_fj - hybrid_fj
    if max_comm <= 0:
        return None
    max_selections = max_comm / long_event
    for burst in range(1, events + 1):
        selections = math.ceil(events / burst)
        if selections <= max_selections:
            total = hybrid_fj + selections * long_event
            return burst, selections, total
    return None

rows = []
for domain, exact, hybrid, events in DOMAINS:
    for factor in (1, 2, 4, 8):
        naive = hybrid + events * WIRE_EVENT_FJ * factor
        selected = min_burst(exact, hybrid, events, factor)
        if selected:
            burst, selections, total = selected
            choice = "hybrid_local"
        else:
            burst, selections, total = None, None, exact
            choice = "exact_digital"
        rows.append({
            "domain": domain,
            "physical_cost_factor": factor,
            "events_before_locality": events,
            "exact_core_pJ": exact / 1000,
            "hybrid_core_pJ": hybrid / 1000,
            "naive_global_total_pJ": naive / 1000,
            "naive_global_saving_pct": 100 * (exact - naive) / exact,
            "min_local_burst_for_10pct_reserve": burst,
            "global_selections_after_locality": selections,
            "cost_aware_total_pJ": total / 1000,
            "cost_aware_saving_pct": 100 * (exact - total) / exact,
            "compiler_choice": choice,
        })

pd.DataFrame(rows).to_csv("physical_cost_screen.csv", index=False)
