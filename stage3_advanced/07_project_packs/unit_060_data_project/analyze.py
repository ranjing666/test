import csv
from collections import Counter, defaultdict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sample_learning_minutes.csv"
OUTPUT_FILE = BASE_DIR / "output" / "report.md"


def load_rows():
    with DATA_FILE.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def analyze(rows: list[dict]) -> dict:
    subject_minutes: dict[str, int] = defaultdict(int)
    daily_minutes: dict[str, int] = defaultdict(int)

    for row in rows:
        minutes = int(row["minutes"])
        subject_minutes[row["subject"]] += minutes
        daily_minutes[row["date"]] += minutes

    total_minutes = sum(subject_minutes.values())
    total_sessions = len(rows)
    average_minutes = round(total_minutes / total_sessions, 2) if total_sessions else 0
    top_subject = Counter(subject_minutes).most_common(1)[0]
    top_day = Counter(daily_minutes).most_common(1)[0]

    return {
        "total_minutes": total_minutes,
        "total_sessions": total_sessions,
        "average_minutes": average_minutes,
        "subject_minutes": dict(sorted(subject_minutes.items())),
        "daily_minutes": dict(sorted(daily_minutes.items())),
        "top_subject": top_subject,
        "top_day": top_day,
    }


def build_report(result: dict) -> str:
    subject_lines = "\n".join(
        f"- {subject}: {minutes} minutes" for subject, minutes in result["subject_minutes"].items()
    )
    day_lines = "\n".join(
        f"- {day}: {minutes} minutes" for day, minutes in result["daily_minutes"].items()
    )

    return f"""# Learning Data Report

## 1. Project Goal

Use a small dataset to understand study time distribution.

## 2. Key Numbers

- Total minutes: {result["total_minutes"]}
- Total sessions: {result["total_sessions"]}
- Average minutes per session: {result["average_minutes"]}

## 3. Subject Summary

{subject_lines}

## 4. Daily Summary

{day_lines}

## 5. Insights

- The top subject is **{result["top_subject"][0]}** with **{result["top_subject"][1]}** minutes.
- The busiest day is **{result["top_day"][0]}** with **{result["top_day"][1]}** minutes.
- You can now replace the CSV with your own data and compare patterns.
"""


def main() -> None:
    rows = load_rows()
    result = analyze(rows)
    report = build_report(result)
    OUTPUT_FILE.write_text(report, encoding="utf-8")

    print("Analysis complete.")
    print(f"Total minutes: {result['total_minutes']}")
    print(f"Top subject: {result['top_subject'][0]}")
    print(f"Report saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
