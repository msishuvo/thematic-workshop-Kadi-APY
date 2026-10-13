"""Helper functions for reading and evaluating tensile test files.

You don't need to change anything here. In your own lab this file would
contain the code that reads YOUR instrument's output format.
"""

import csv


def read_curve(path):
    """Read a CSV with columns strain_percent, stress_MPa into two lists."""
    strain, stress = [], []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            strain.append(float(row["strain_percent"]))
            stress.append(float(row["stress_MPa"]))
    return strain, stress


def evaluate(path):
    """Return key results of a tensile test as a dictionary.

    - youngs_modulus (GPa): slope of the initial linear region
    - yield_strength (MPa): 0.2 % offset method
    - tensile_strength (MPa): maximum stress
    - elongation_at_break (%): last strain with non-zero stress
    """
    strain, stress = read_curve(path)
    tensile_strength = max(stress)

    # Fit the slope (least squares through the origin) on the initial loading
    # region, i.e. until the stress first exceeds 40 % of the maximum.
    pairs = []
    for e, s in zip(strain, stress):
        if s >= 0.4 * tensile_strength:
            break
        if e > 0:
            pairs.append((e, s))
    slope = sum(e * s for e, s in pairs) / sum(e * e for e, _ in pairs)  # MPa per %

    yield_strength = tensile_strength
    for e, s in zip(strain, stress):
        if e > 0.2 and s <= slope * (e - 0.2):
            yield_strength = s
            break

    elongation_at_break = max(e for e, s in zip(strain, stress) if s > 1.0)

    return {
        "youngs_modulus": round(slope * 100 / 1000, 1),  # MPa/% -> GPa
        "yield_strength": round(yield_strength, 1),
        "tensile_strength": round(tensile_strength, 1),
        "elongation_at_break": round(elongation_at_break, 1),
    }


if __name__ == "__main__":
    import sys

    for p in sys.argv[1:]:
        print(p, evaluate(p))
