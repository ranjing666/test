import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_FILE = BASE_DIR / "learning_tasks.json"
SAMPLE_DATA_FILE = BASE_DIR / "sample_data.json"


def _normalize_tasks(tasks: list[dict]) -> list[dict]:
    normalized: list[dict] = []
    for task in tasks:
        normalized.append(
            {
                "title": str(task.get("title", "Untitled task")),
                "notes": str(task.get("notes", "No notes")),
                "done": bool(task.get("done", False)),
            }
        )
    return normalized


def load_tasks(file_path: Path = DEFAULT_DATA_FILE) -> list[dict]:
    source = file_path if file_path.exists() else SAMPLE_DATA_FILE
    if not source.exists():
        return []

    with source.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    return _normalize_tasks(data)


def save_tasks(file_path: Path, tasks: list[dict]) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as handle:
        json.dump(_normalize_tasks(tasks), handle, ensure_ascii=True, indent=2)
