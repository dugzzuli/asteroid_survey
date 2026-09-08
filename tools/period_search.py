"""Minimal weighted harmonic period search for asteroid lightcurves.

Input CSV columns: time, magnitude, error
Example:
    python tools/period_search.py observations.csv --min-period 1 --max-period 24

This is a transparent teaching implementation. Production work should inspect
window functions, aliases, phase-angle effects, and independent validation.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Solve a small linear system with partial-pivot Gaussian elimination."""
    size = len(vector)
    augmented = [row[:] + [value] for row, value in zip(matrix, vector)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-12:
            raise ValueError("singular design matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [a - factor * b for a, b in zip(augmented[row], augmented[column])]
    return [row[-1] for row in augmented]


def harmonic_chi2(times: list[float], magnitudes: list[float], errors: list[float], period: float, harmonics: int) -> float:
    design = [[1.0] + [term for order in range(1, harmonics + 1) for term in (math.sin(2 * math.pi * order * time / period), math.cos(2 * math.pi * order * time / period))] for time in times]
    width = 1 + 2 * harmonics
    normal = [[0.0] * width for _ in range(width)]
    rhs = [0.0] * width
    for row, magnitude, error in zip(design, magnitudes, errors):
        weight = 1.0 / (error * error)
        for left in range(width):
            rhs[left] += weight * row[left] * magnitude
            for right in range(width):
                normal[left][right] += weight * row[left] * row[right]
    coefficients = solve(normal, rhs)
    return sum(((magnitude - sum(value * coefficient for value, coefficient in zip(row, coefficients))) / error) ** 2 for row, magnitude, error in zip(design, magnitudes, errors))


def load_points(path: Path) -> tuple[list[float], list[float], list[float]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"time", "magnitude", "error"}
        if not required.issubset(reader.fieldnames or set()):
            raise ValueError("input CSV must contain time,magnitude,error columns")
        rows = [(float(row["time"]), float(row["magnitude"]), float(row["error"])) for row in reader]
    if len(rows) < 8:
        raise ValueError("at least eight observations are required")
    return tuple(map(list, zip(*rows)))


def main() -> None:
    parser = argparse.ArgumentParser(description="Grid-search a weighted harmonic lightcurve model.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--min-period", type=float, required=True, help="minimum trial period in the input time unit")
    parser.add_argument("--max-period", type=float, required=True, help="maximum trial period in the input time unit")
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--harmonics", type=int, default=2)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()
    if args.min_period <= 0 or args.max_period <= args.min_period:
        raise SystemExit("period bounds must satisfy 0 < min < max")
    times, magnitudes, errors = load_points(args.input)
    trials = []
    for index in range(args.steps):
        frequency = 1 / args.max_period + index * (1 / args.min_period - 1 / args.max_period) / (args.steps - 1)
        period = 1 / frequency
        try:
            trials.append((harmonic_chi2(times, magnitudes, errors, period, args.harmonics), period))
        except ValueError:
            continue
    for chi2, period in sorted(trials)[: args.top]:
        print(f"period={period:.8g} chi2={chi2:.5g}")


if __name__ == "__main__":
    main()
