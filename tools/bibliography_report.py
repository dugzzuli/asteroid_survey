"""Validate papers.csv and render a compact Markdown method table.

Run: python tools/bibliography_report.py
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "bibliography" / "papers.csv"
OUTPUT = ROOT / "statistics" / "bibliography_quality.md"
REQUIRED = ("ID", "Year", "Title", "DOI", "arXiv", "Review_priority", "Main_question", "Limitation")


def main() -> None:
    with PAPERS.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
        fields = handle.seek(0) or next(csv.reader(PAPERS.open(encoding="utf-8-sig", newline="")))

    missing_headers = [field for field in REQUIRED if field not in fields]
    if missing_headers:
        raise SystemExit(f"Missing CSV headers: {', '.join(missing_headers)}")

    duplicate_ids = [item for item, count in Counter(row["ID"] for row in rows).items() if count > 1]
    missing_identifiers = [row["ID"] for row in rows if not row["DOI"].strip() and not row["arXiv"].strip()]
    incomplete = {
        row["ID"]: [field for field in REQUIRED if not row.get(field, "").strip()]
        for row in rows
        if any(not row.get(field, "").strip() for field in REQUIRED if field not in {"DOI", "arXiv"})
    }
    priorities = Counter(row["Review_priority"].strip() for row in rows)
    topics = Counter(topic.strip() for row in rows for topic in row["Research_topic"].split(";") if topic.strip())

    lines = [
        "# Bibliography quality report",
        "",
        f"- Records: {len(rows)}",
        f"- Priorities: " + ", ".join(f"{key}={value}" for key, value in sorted(priorities.items())),
        f"- Duplicate IDs: {', '.join(duplicate_ids) or 'none'}",
        f"- Missing DOI and arXiv: {', '.join(missing_identifiers) or 'none'}",
        f"- Records missing required analytical fields: {', '.join(incomplete) or 'none'}",
        "",
        "## Topic counts",
        "",
        "| Topic | Records |",
        "|---|---:|",
        *[f"| {topic} | {count} |" for topic, count in topics.most_common()],
    ]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} for {len(rows)} records.")
    if duplicate_ids or missing_identifiers or incomplete:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
