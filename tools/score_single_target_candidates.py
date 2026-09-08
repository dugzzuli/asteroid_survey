"""Rank single-asteroid study candidates from a user-curated CSV.

Required columns: designation, period_status, shape_model, baseline_years,
multiband, thermal_data, special_case, observable

Use yes/no for boolean fields. period_status accepts unknown, ambiguous, or known.
This prioritises follow-up value; it does not establish scientific merit by itself.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED = {"designation", "period_status", "shape_model", "baseline_years", "multiband", "thermal_data", "special_case", "observable"}


def yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "1"}


def score(row: dict[str, str]) -> tuple[int, list[str]]:
    value, reasons = 0, []
    period = row["period_status"].strip().lower()
    if period == "unknown": value, reasons = value + 3, reasons + ["period unknown"]
    if period == "ambiguous": value, reasons = value + 4, reasons + ["period ambiguous"]
    if not yes(row["shape_model"]): value, reasons = value + 4, reasons + ["no shape model"]
    if float(row["baseline_years"]) >= 10: value, reasons = value + 3, reasons + ["YORP-capable baseline"]
    if yes(row["multiband"]): value, reasons = value + 2, reasons + ["multiband surface constraints"]
    if yes(row["thermal_data"]): value, reasons = value + 2, reasons + ["thermal constraint available"]
    if yes(row["special_case"]): value, reasons = value + 3, reasons + ["special physical case"]
    if yes(row["observable"]): value, reasons = value + 2, reasons + ["currently observable"]
    return value, reasons


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    with args.input.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows or not REQUIRED.issubset(rows[0]):
        raise SystemExit("CSV is missing one or more required columns")
    ranked = sorted(((score(row), row["designation"]) for row in rows), reverse=True)
    for (value, reasons), designation in ranked:
        print(f"{designation}: {value} — {', '.join(reasons) or 'no positive flags'}")


if __name__ == "__main__":
    main()
