from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent


STAGES = [
    ("stage1_foundation", 1, 10),
    ("stage2_growth", 11, 30),
    ("stage3_advanced", 31, 60),
    ("stage4_expert", 61, 85),
    ("stage5_master", 86, 100),
]


def visible_markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if "tools" not in path.parts and "__pycache__" not in path.parts
    ]


def markdown_link_check() -> list[str]:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    missing: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            target_path = (path.parent / target).resolve()
            if not target_path.exists():
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
    return missing


def python_syntax_check() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        try:
            compile(source, str(path), "exec")
        except Exception as exc:  # pragma: no cover - diagnostic script
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    return errors


def count_check() -> dict[str, int]:
    return {
        "stage1_daily_guides": len(list((ROOT / "stage1_foundation" / "daily_guides").glob("day_*.md"))),
        "stage2_daily_guides": len(list((ROOT / "stage2_growth" / "daily_guides").glob("day_*.md"))),
        "stage3_daily_guides": len(list((ROOT / "stage3_advanced" / "daily_guides").glob("day_*.md"))),
        "stage4_daily_guides": len(list((ROOT / "stage4_expert" / "daily_guides").glob("day_*.md"))),
        "stage5_daily_guides": len(list((ROOT / "stage5_master" / "daily_guides").glob("day_*.md"))),
        "study_logs": len(list((ROOT / "study_logs").glob("day*.md"))),
        "unit_files": len(list(ROOT.glob("stage*_*/units/unit_*.md"))),
        "project_pack_roots": sum(
            1
            for stage in ["stage2_growth", "stage3_advanced", "stage4_expert", "stage5_master"]
            for child in (ROOT / stage / "project_packs").iterdir()
            if child.is_dir()
        ),
    }


def stage_dir_for_unit(unit_number: int) -> Path:
    for stage_dir, start, end in STAGES:
        if start <= unit_number <= end:
            return ROOT / stage_dir
    raise ValueError(unit_number)


def legacy_visible_term_check() -> list[str]:
    forbidden_terms = [
        "旧版",
        "旧计划",
        "一千天",
        "1000 天",
        "1000-Day",
        "压缩学习",
        "压缩后的",
        "压缩 Day 范围",
        "原 10 天",
    ]
    issues: list[str] = []
    for path in visible_markdown_files():
        text = path.read_text(encoding="utf-8")
        for term in forbidden_terms:
            if term in text:
                issues.append(f"{path.relative_to(ROOT)} contains legacy term: {term}")
    return issues


def unit_structure_check() -> list[str]:
    issues: list[str] = []
    heading_pattern = re.compile(r"^### Day \d{3}$", re.MULTILINE)
    for path in ROOT.glob("stage*_*/units/unit_*.md"):
        text = path.read_text(encoding="utf-8")
        if "- 单元结构：10 个学习步骤" not in text:
            issues.append(f"{path.relative_to(ROOT)} missing unit structure label")
        if "## 10 个学习步骤" not in text:
            issues.append(f"{path.relative_to(ROOT)} missing step section heading")
        if "- 对应天数：Day " in text:
            issues.append(f"{path.relative_to(ROOT)} contains legacy day-range label")
        if heading_pattern.search(text):
            issues.append(f"{path.relative_to(ROOT)} contains legacy day heading")
    return issues


def tracker_layout_check() -> list[str]:
    path = ROOT / "LEARNING_PROGRESS_TRACKER.md"
    if not path.exists():
        return ["LEARNING_PROGRESS_TRACKER.md is missing"]
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if "| 完成 | 学习日 | 主题 | 完成 | 学习日 | 主题 |" not in text:
        issues.append("LEARNING_PROGRESS_TRACKER.md missing compact progress table")
    if "- [ ] Day " in text:
        issues.append("LEARNING_PROGRESS_TRACKER.md still contains old long checklist layout")
    return issues


def placeholder_example_check() -> list[str]:
    generic_patterns = [
        "print('Unit ",
        "print(\"Unit ",
        "Keep going,",
    ]
    targeted_rules = {
        "stage2_growth/units/unit_020.md": ["## Project summary", "## Resume bullets"],
        "stage3_advanced/units/unit_033.md": ["import pandas as pd", "import matplotlib.pyplot as plt"],
        "stage3_advanced/units/unit_034.md": ["def find_max(", "def is_valid("],
        "stage3_advanced/units/unit_040.md": ["## Project summary", "## Resume bullets"],
        "stage3_advanced/units/unit_050.md": ["## Project summary", "## Resume bullets"],
        "stage4_expert/units/unit_070.md": ["import pandas as pd", "import matplotlib.pyplot as plt"],
        "stage4_expert/units/unit_079.md": ["CREATE TABLE students", "SELECT name, score"],
        "stage4_expert/units/unit_080.md": ["def find_max(", "def is_valid("],
        "stage4_expert/units/unit_085.md": ["def find_max(", "def is_valid("],
        "stage5_master/units/unit_090.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/units/unit_091.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/units/unit_092.md": ["requests.get(", '"status": "ok"'],
        "stage5_master/units/unit_093.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/units/unit_094.md": ["## Project log", "git status"],
        "stage5_master/units/unit_095.md": ["CREATE TABLE students", "SELECT name, score"],
        "stage5_master/units/unit_096.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/units/unit_098.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/units/unit_099.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/units/unit_086.md": ["def find_max(", "def is_valid("],
        "stage5_master/units/unit_097.md": ["import pandas as pd", "import matplotlib.pyplot as plt"],
        "stage5_master/units/unit_100.md": ["def find_max(", "def is_valid("],
    }
    targeted_daily_rules = {
        20: ["## Project summary", "## Resume bullets"],
        40: ["## Project summary", "## Resume bullets"],
        50: ["## Project summary", "## Resume bullets"],
        79: ["CREATE TABLE students", "SELECT name, score", "查数据前没想清楚要哪几列。"],
        90: ["## Project summary", "## Resume bullets"],
        91: ["## Project summary", "## Resume bullets"],
        92: ["## Project summary", "## Resume bullets"],
        93: ["## Project summary", "## Resume bullets"],
        94: ["## Project summary"],
        95: ["## Project summary", "## Resume bullets"],
        96: ["## Project summary", "## Resume bullets"],
        97: ["## Project summary", "## Resume bullets"],
        98: ["## Project summary", "## Resume bullets"],
        99: ["## Project summary", "## Resume bullets"],
        100: ["## Project summary", "## Resume bullets"],
    }
    issues: list[str] = []
    for stage in ["stage3_advanced", "stage4_expert", "stage5_master"]:
        for path in (ROOT / stage / "units").glob("unit_*.md"):
            text = path.read_text(encoding="utf-8")
            for pattern in generic_patterns:
                if pattern in text:
                    issues.append(f"{path.relative_to(ROOT)} contains placeholder pattern: {pattern}")
                    break
    for relative_path, patterns in targeted_rules.items():
        path = ROOT / relative_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in patterns:
            if pattern in text:
                issues.append(f"{path.relative_to(ROOT)} contains mismatched example pattern: {pattern}")
                break
    for unit_number, patterns in targeted_daily_rules.items():
        stage_dir = stage_dir_for_unit(unit_number) / "daily_guides"
        path = stage_dir / f"day_{unit_number:03d}.md"
        text = path.read_text(encoding="utf-8")
        for pattern in patterns:
            if pattern in text:
                issues.append(f"{path.relative_to(ROOT)} contains mismatched daily-guide pattern: {pattern}")
                break
    return issues


def print_section(title: str) -> None:
    print(f"\n[{title}]")


def main() -> None:
    failed = False

    print_section("markdown_links")
    missing_links = markdown_link_check()
    if missing_links:
        failed = True
        for item in missing_links:
            print(item)
    else:
        print("ok")

    print_section("python_syntax")
    syntax_errors = python_syntax_check()
    if syntax_errors:
        failed = True
        for item in syntax_errors:
            print(item)
    else:
        print("ok")

    print_section("counts")
    counts = count_check()
    for key, value in counts.items():
        print(f"{key}={value}")
    expected_counts = {
        "stage1_daily_guides": 10,
        "stage2_daily_guides": 20,
        "stage3_daily_guides": 30,
        "stage4_daily_guides": 25,
        "stage5_daily_guides": 15,
        "study_logs": 100,
        "unit_files": 100,
        "project_pack_roots": 8,
    }
    mismatches = [
        f"{key} expected {expected_counts[key]} but got {counts[key]}"
        for key in expected_counts
        if counts[key] != expected_counts[key]
    ]
    if mismatches:
        failed = True
        for item in mismatches:
            print(item)

    print_section("legacy_visible_terms")
    legacy_issues = legacy_visible_term_check()
    if legacy_issues:
        failed = True
        for item in legacy_issues:
            print(item)
    else:
        print("ok")

    print_section("unit_structure")
    structure_issues = unit_structure_check()
    if structure_issues:
        failed = True
        for item in structure_issues:
            print(item)
    else:
        print("ok")

    print_section("placeholder_examples")
    placeholder_issues = placeholder_example_check()
    if placeholder_issues:
        failed = True
        for item in placeholder_issues:
            print(item)
    else:
        print("ok")

    print_section("tracker_layout")
    tracker_issues = tracker_layout_check()
    if tracker_issues:
        failed = True
        for item in tracker_issues:
            print(item)
    else:
        print("ok")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
