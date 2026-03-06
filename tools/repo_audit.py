from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent


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
        "plan_batches": len(list((ROOT / "plan_1000_days").glob("day_*.md"))),
        "unit_files": len(list(ROOT.glob("stage*_*/units/unit_*.md"))),
        "project_pack_roots": sum(
            1
            for stage in ["stage2_growth", "stage3_advanced", "stage4_expert", "stage5_master"]
            for child in (ROOT / stage / "project_packs").iterdir()
            if child.is_dir()
        ),
    }


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
    for key, value in count_check().items():
        print(f"{key}={value}")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
