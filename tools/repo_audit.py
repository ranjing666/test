from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent

START_GUIDE_FILE = "从这里开始.md"
MASTER_PLAN_FILE = "100天学习总计划.md"
TRACKER_FILE = "学习进度总看板.md"
PROJECT_GUIDE_FILE = "项目包使用指南.md"
PROJECT_TRACKER_FILE = "项目包进度看板.md"
GITHUB_TUTORIAL_FILE = "GitHub上传教程.md"
ENGLISH_TRACK_DIR = "编程英语同步学习"
ENGLISH_ROUTE_FILE = "100天编程英语路线.md"
ENGLISH_README_FILE = "README.md"
LEARNING_NAV_FILE = "学习顺序总导航.md"


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
        "stage1_01_daily_guides": len(list((ROOT / "stage1_foundation" / "01_daily_guides").glob("day_*.md"))),
        "stage2_01_daily_guides": len(list((ROOT / "stage2_growth" / "01_daily_guides").glob("day_*.md"))),
        "stage3_01_daily_guides": len(list((ROOT / "stage3_advanced" / "01_daily_guides").glob("day_*.md"))),
        "stage4_01_daily_guides": len(list((ROOT / "stage4_expert" / "01_daily_guides").glob("day_*.md"))),
        "stage5_01_daily_guides": len(list((ROOT / "stage5_master" / "01_daily_guides").glob("day_*.md"))),
        "study_logs": len(list((ROOT / "study_logs").glob("day*.md"))),
        "unit_files": len(list(ROOT.glob("stage*_*/02_units/unit_*.md"))),
        "project_pack_roots": sum(
            1
            for stage in ["stage2_growth", "stage3_advanced", "stage4_expert", "stage5_master"]
            for child in (ROOT / stage / "07_project_packs").iterdir()
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
    for path in ROOT.glob("stage*_*/02_units/unit_*.md"):
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
    path = ROOT / TRACKER_FILE
    if not path.exists():
        return [f"{TRACKER_FILE} is missing"]
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if "| 完成 | 学习日 | 主题 | 完成 | 学习日 | 主题 |" not in text:
        issues.append(f"{TRACKER_FILE} missing compact progress table")
    if "- [ ] Day " in text:
        issues.append(f"{TRACKER_FILE} still contains old long checklist layout")
    return issues


def entry_filename_check() -> list[str]:
    required = [
        START_GUIDE_FILE,
        MASTER_PLAN_FILE,
        TRACKER_FILE,
        LEARNING_NAV_FILE,
        PROJECT_GUIDE_FILE,
        PROJECT_TRACKER_FILE,
        GITHUB_TUTORIAL_FILE,
    ]
    legacy = [
        "START_HERE.md",
        "100_DAYS_MASTER_PLAN.md",
        "LEARNING_PROGRESS_TRACKER.md",
        "学习顺序导航.md",
        "PROJECT_PACKS_GUIDE.md",
        "PROJECT_PACKS_PROGRESS_TRACKER.md",
        "GITHUB_UPLOAD_TUTORIAL.md",
    ]
    issues: list[str] = []
    for name in required:
        if not (ROOT / name).exists():
            issues.append(f"missing entry file: {name}")
    for name in legacy:
        if (ROOT / name).exists():
            issues.append(f"legacy entry file still exists: {name}")
    return issues


def english_track_check() -> list[str]:
    track_dir = ROOT / ENGLISH_TRACK_DIR
    required = [
        track_dir / ENGLISH_README_FILE,
        track_dir / ENGLISH_ROUTE_FILE,
        track_dir / "高频编程英语词块.md",
        track_dir / "每日英语练习模板.md",
        track_dir / "英语输出句型模板.md",
        track_dir / "阶段1_基础操作英语.md",
        track_dir / "阶段2_项目起步英语.md",
        track_dir / "阶段3_后端算法英语.md",
        track_dir / "阶段4_工程化英语.md",
        track_dir / "阶段5_表达求职英语.md",
    ]
    issues: list[str] = []
    for path in required:
        if not path.exists():
            issues.append(f"missing english track file: {path.relative_to(ROOT)}")
    return issues


def navigation_check() -> list[str]:
    issues: list[str] = []
    nav_file = ROOT / LEARNING_NAV_FILE
    if not nav_file.exists():
        issues.append(f"missing navigation file: {LEARNING_NAV_FILE}")
    for path in ROOT.glob("stage*_*/01_daily_guides/day_*.md"):
        text = path.read_text(encoding="utf-8")
        if "## 导航" not in text:
            issues.append(f"{path.relative_to(ROOT)} missing navigation section")
        if "上一天：" not in text or "下一天：" not in text:
            issues.append(f"{path.relative_to(ROOT)} missing previous/next links")
    return issues


def core_sequence_check() -> list[str]:
    ordered_tokens = [
        "stage1_foundation/01_daily_guides/day_001.md",
        "stage1_foundation/02_units/unit_001.md",
        "stage1_foundation/03_workbooks/unit_001_workbook.md",
        "stage1_foundation/04_code_templates/unit_001_template.py",
        "stage1_foundation/05_code_solutions/unit_001_solution.py",
        "stage1_foundation/06_quizzes/unit_001_quiz.md",
        "study_logs/day001.md",
        TRACKER_FILE,
    ]
    files_to_check = [
        (ROOT / "README.md", "## 从哪里开始", "## 现在的仓库结构"),
        (ROOT / START_GUIDE_FILE, "## 你现在只走这一条线", "## 如果你不想一下子看 100 天"),
        (ROOT / LEARNING_NAV_FILE, "## 零基础默认顺序", "## 每天固定顺序"),
        (ROOT / "stage1_foundation" / "README.md", "## 这一阶段怎么学", "## 这一阶段的结构"),
        (ROOT / "stage1_foundation" / "01_daily_guides" / "day_001.md", "## 今天要打开的资料", "## 同步补充"),
    ]
    issues: list[str] = []
    for path, start_marker, end_marker in files_to_check:
        if not path.exists():
            issues.append(f"missing core sequence file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        start = text.find(start_marker)
        end = text.find(end_marker, start + len(start_marker))
        if start == -1 or end == -1:
            issues.append(f"{path.relative_to(ROOT)} missing core sequence section markers")
            continue
        section_text = text[start:end]
        positions: list[int] = []
        for token in ordered_tokens:
            position = section_text.find(token)
            if position == -1:
                issues.append(f"{path.relative_to(ROOT)} missing core sequence token: {token}")
                break
            positions.append(position)
        else:
            if positions != sorted(positions):
                issues.append(f"{path.relative_to(ROOT)} has incorrect core sequence order")
    return issues


def placeholder_example_check() -> list[str]:
    generic_patterns = [
        "print('Unit ",
        "print(\"Unit ",
        "Keep going,",
    ]
    targeted_rules = {
        "stage2_growth/02_units/unit_020.md": ["## Project summary", "## Resume bullets"],
        "stage3_advanced/02_units/unit_033.md": ["import pandas as pd", "import matplotlib.pyplot as plt"],
        "stage3_advanced/02_units/unit_034.md": ["def find_max(", "def is_valid("],
        "stage3_advanced/02_units/unit_040.md": ["## Project summary", "## Resume bullets"],
        "stage3_advanced/02_units/unit_050.md": ["## Project summary", "## Resume bullets"],
        "stage4_expert/02_units/unit_070.md": ["import pandas as pd", "import matplotlib.pyplot as plt"],
        "stage4_expert/02_units/unit_079.md": ["CREATE TABLE students", "SELECT name, score"],
        "stage4_expert/02_units/unit_080.md": ["def find_max(", "def is_valid("],
        "stage4_expert/02_units/unit_085.md": ["def find_max(", "def is_valid("],
        "stage5_master/02_units/unit_090.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/02_units/unit_091.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/02_units/unit_092.md": ["requests.get(", '"status": "ok"'],
        "stage5_master/02_units/unit_093.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/02_units/unit_094.md": ["## Project log", "git status"],
        "stage5_master/02_units/unit_095.md": ["CREATE TABLE students", "SELECT name, score"],
        "stage5_master/02_units/unit_096.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/02_units/unit_098.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/02_units/unit_099.md": ["## Project summary", "## Resume bullets"],
        "stage5_master/02_units/unit_086.md": ["def find_max(", "def is_valid("],
        "stage5_master/02_units/unit_097.md": ["import pandas as pd", "import matplotlib.pyplot as plt"],
        "stage5_master/02_units/unit_100.md": ["def find_max(", "def is_valid("],
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
        for path in (ROOT / stage / "02_units").glob("unit_*.md"):
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
        stage_dir = stage_dir_for_unit(unit_number) / "01_daily_guides"
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
        "stage1_01_daily_guides": 10,
        "stage2_01_daily_guides": 20,
        "stage3_01_daily_guides": 30,
        "stage4_01_daily_guides": 25,
        "stage5_01_daily_guides": 15,
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

    print_section("entry_filenames")
    entry_issues = entry_filename_check()
    if entry_issues:
        failed = True
        for item in entry_issues:
            print(item)
    else:
        print("ok")

    print_section("legacy_visible_terms")
    legacy_issues = legacy_visible_term_check()
    if legacy_issues:
        failed = True
        for item in legacy_issues:
            print(item)
    else:
        print("ok")

    print_section("english_track")
    english_issues = english_track_check()
    if english_issues:
        failed = True
        for item in english_issues:
            print(item)
    else:
        print("ok")

    print_section("navigation")
    navigation_issues = navigation_check()
    if navigation_issues:
        failed = True
        for item in navigation_issues:
            print(item)
    else:
        print("ok")

    print_section("core_sequence")
    core_sequence_issues = core_sequence_check()
    if core_sequence_issues:
        failed = True
        for item in core_sequence_issues:
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



