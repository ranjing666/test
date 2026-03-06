from pathlib import Path

from generate_1000_day_plan import PHASES, UNITS

START_GUIDE_FILE = "从这里开始.md"
MASTER_PLAN_FILE = "100天学习总计划.md"
TRACKER_FILE = "学习进度总看板.md"
ENGLISH_TRACK_DIR = "编程英语同步学习"
ENGLISH_ROUTE_FILE = f"{ENGLISH_TRACK_DIR}/100天编程英语路线.md"
LEARNING_NAV_FILE = "学习顺序总导航.md"


STAGES = [
    ("stage1_foundation", "第 1 阶段：入门基础", 1, 10),
    ("stage2_growth", "第 2 阶段：成长进阶", 11, 30),
    ("stage3_advanced", "第 3 阶段：高级进阶", 31, 60),
    ("stage4_expert", "第 4 阶段：专家深化", 61, 85),
    ("stage5_master", "第 5 阶段：大师输出", 86, 100),
]


def words_of(unit):
    return [word.strip() for word in unit["words"].split(",") if word.strip()]


def stage_for_unit(unit_number: int):
    for stage_dir, stage_label, start, end in STAGES:
        if start <= unit_number <= end:
            return stage_dir, stage_label, start, end
    raise ValueError(unit_number)


def phase_for_unit(unit_number: int) -> str:
    return PHASES[(unit_number - 1) // 10]


def existing_file(repo_root: Path, relative_path: str) -> str | None:
    path = repo_root / relative_path
    return relative_path if path.exists() else None


def find_template_path(repo_root: Path, stage_dir: str, unit_number: int, kind: str) -> str | None:
    candidates = [
        f"{stage_dir}/{kind}/unit_{unit_number:03d}_{'template' if kind == 'code_templates' else 'solution'}.py",
        f"{stage_dir}/{kind}/unit_{unit_number:03d}_{'template' if kind == 'code_templates' else 'solution'}.md",
    ]
    for candidate in candidates:
        path = existing_file(repo_root, candidate)
        if path:
            return path
    return None


def find_project_pack(repo_root: Path, stage_dir: str, unit_number: int) -> str | None:
    project_root = repo_root / stage_dir / "project_packs"
    if not project_root.exists():
        return None
    matches = sorted(project_root.glob(f"unit_{unit_number:03d}_*"))
    if not matches:
        return None
    readme = matches[0] / "README.md"
    if readme.exists():
        return readme.relative_to(repo_root).as_posix()
    return None


def material_paths(repo_root: Path, stage_dir: str, unit_number: int) -> dict[str, str | None]:
    return {
        "unit": existing_file(repo_root, f"{stage_dir}/units/unit_{unit_number:03d}.md"),
        "workbook": existing_file(repo_root, f"{stage_dir}/workbooks/unit_{unit_number:03d}_workbook.md"),
        "template": find_template_path(repo_root, stage_dir, unit_number, "code_templates"),
        "solution": find_template_path(repo_root, stage_dir, unit_number, "code_solutions"),
        "quiz": existing_file(repo_root, f"{stage_dir}/quizzes/unit_{unit_number:03d}_quiz.md"),
        "project_pack": find_project_pack(repo_root, stage_dir, unit_number),
    }


def merged_steps(unit: dict[str, str]) -> list[str]:
    topic1, topic2, topic3, topic4 = unit["prog"]
    return [
        "先读单元讲义开头，知道这一天最后要交付什么。",
        f"围绕 `{topic1}` 看最小例子，手敲 1 遍，再改 1 遍。",
        f"用中文解释 `{topic1}`，确保不是只看懂表面。",
        f"围绕 `{topic2}` 做一个最小练习，先追求能跑通。",
        f"把 `{topic1}` 和 `{topic2}` 连起来，形成第一版结果。",
        f"围绕 `{topic3}` 补上第三块能力，开始接近真实成果。",
        f"围绕 `{topic4}` 做最后一块拼接，让结果更完整。",
        "完成工作簿，把卡点和错点写下来。",
        "完成模板或练习代码，卡住时再对照参考答案。",
        "做小测、写学习日志，并提交一次 Git 记录。",
    ]


def day_link(current_stage_dir: str, target_unit_number: int) -> str:
    target_stage_dir = stage_for_unit(target_unit_number)[0]
    filename = f"day_{target_unit_number:03d}.md"
    if target_stage_dir == current_stage_dir:
        return f"`{filename}`"
    return f"`../../{target_stage_dir}/daily_guides/{filename}`"


def navigation_lines(stage_dir: str, unit_number: int) -> list[str]:
    previous_day = day_link(stage_dir, unit_number - 1) if unit_number > 1 else "无，今天就是起点"
    next_day = day_link(stage_dir, unit_number + 1) if unit_number < 100 else "无，今天已经是最后一个学习日"
    return [
        "## 导航",
        "",
        f"- 上一天：{previous_day}",
        f"- 下一天：{next_day}",
        "- 本阶段目录：`README.md`",
        f"- 对应日志：`../../study_logs/day{unit_number:03d}.md`",
        f"- 配套英语：`../../{ENGLISH_ROUTE_FILE}`",
        f"- 总导航：`../../{LEARNING_NAV_FILE}`",
        "",
    ]


def merged_day_text(repo_root: Path, unit_number: int) -> str:
    unit = UNITS[unit_number - 1]
    stage_dir, stage_label, _, _ = stage_for_unit(unit_number)
    files = material_paths(repo_root, stage_dir, unit_number)
    steps = "\n".join(f"{idx}. {step}" for idx, step in enumerate(merged_steps(unit), start=1))
    words = ", ".join(words_of(unit))
    file_lines = [f"- `{files['unit']}`"]
    if files["workbook"]:
        file_lines.append(f"- `{files['workbook']}`")
    if files["template"]:
        file_lines.append(f"- `{files['template']}`")
    if files["solution"]:
        file_lines.append(f"- `{files['solution']}`")
    if files["quiz"]:
        file_lines.append(f"- `{files['quiz']}`")
    if files["project_pack"]:
        file_lines.append(f"- `{files['project_pack']}`")
    files_text = "\n".join(file_lines)
    project_pack_tip = (
        f"- 如果你已经走到项目实现阶段，也打开 `{files['project_pack']}`。"
        if files["project_pack"]
        else "- 这一单元没有额外项目包，先把单元主线做扎实。"
    )

    return "\n".join(
        [
            f"# Day {unit_number:03d}：{unit['title']}",
            "",
            f"- 对应单元：`unit_{unit_number:03d}`",
            f"- 所属阶段：{stage_label}",
            f"- 所属 100 天主题：{phase_for_unit(unit_number)}",
            f"- 最终产出：{unit['output']}",
            "",
            *navigation_lines(stage_dir, unit_number),
            "## 这一天怎么学",
            "",
            "这一份文件就是当前单元的学习入口。",
            "如果一次做不完，可以拆成 2 到 4 次完成。",
            "",
            "## 10 个步骤",
            "",
            steps,
            "",
            "## 今天要打开的资料",
            "",
            files_text,
            f"- `{ENGLISH_ROUTE_FILE}`（找到对应 Day {unit_number:03d}）",
            "",
            "## 今天重点盯住什么",
            "",
            f"- 4 个核心点：`{'`、`'.join(unit['prog'])}`",
            f"- 英语句子：`{unit['sentence']}`",
            f"- 高频词：`{words}`",
            "",
            "## 做到什么算完成",
            "",
            f"- 我能用自己的话解释 `{unit['title']}` 这一单元到底在解决什么问题。",
            f"- 我至少亲手改过 1 次代码、页面、文档或结果文件。",
            f"- 我把 `{unit['output']}` 做到了最小可展示版本。",
            project_pack_tip,
            "",
            "## 收尾动作",
            "",
            f"- 去 `study_logs/day{unit_number:03d}.md` 写今天的学习记录。",
            f"- 在 `{TRACKER_FILE}` 给这一格打勾。",
            "- 执行一次 Git 提交，让学习痕迹留在仓库里。",
            "",
        ]
    )


def stage_daily_readme(stage_label: str, start: int, end: int) -> str:
    lines = [
        f"# {stage_label} 学习日目录",
        "",
        "这个目录按单元整理。",
        "每个 `day_XXX.md` 都是一个完整学习日的入口。",
        "- 阶段主页：`../README.md`",
        f"- 总导航：`../../{LEARNING_NAV_FILE}`",
        f"- 配套英语：`../../{ENGLISH_ROUTE_FILE}`",
        "",
        "建议顺序：",
        "1. 先打开当前 `day_XXX.md`。",
        "2. 再进对应单元讲义 `units/unit_XXX.md`。",
        "3. 再做工作簿、模板、答案和小测。",
        "4. 最后写 `study_logs/dayXXX.md`。",
        "",
        "## 目录",
        "",
    ]
    for unit_number in range(start, end + 1):
        unit = UNITS[unit_number - 1]
        lines.append(f"- [Day {unit_number:03d}](day_{unit_number:03d}.md)：{unit['title']}")
    lines.append("")
    return "\n".join(lines)


def study_log_text(unit_number: int) -> str:
    unit = UNITS[unit_number - 1]
    stage_dir, stage_label, _, _ = stage_for_unit(unit_number)
    return "\n".join(
        [
            f"# Day {unit_number:03d} 学习记录",
            "",
            f"- 对应单元：`unit_{unit_number:03d}`",
            f"- 课程主题：{unit['title']}",
            f"- 所属阶段：{stage_label}",
            f"- 阶段目录：`{stage_dir}`",
            "",
            "## 今天我完成了什么",
            "",
            "- ",
            "- ",
            "- ",
            "",
            "## 今天最关键的 3 个知识点",
            "",
            "1. ",
            "2. ",
            "3. ",
            "",
            "## 今天我打开了哪些资料",
            "",
            "- ",
            "- ",
            "- ",
            "",
            "## 今天新记住的英语词",
            "",
            "- ",
            "- ",
            "- ",
            "",
            "## 今天实际动手了什么",
            "",
            "- 我运行了：",
            "- 我修改了：",
            "- 我验证了：",
            "",
            "## 今天卡住的地方",
            "",
            "- ",
            "",
            "## 下一次我先做什么",
            "",
            "- ",
            "- ",
            "",
        ]
    )


def study_logs_readme() -> str:
    return "\n".join(
        [
            "# 学习记录说明",
            "",
            "这个目录现在保留 `100` 份学习记录。",
            "每一份 `dayXXX.md` 对应 1 个学习日。",
            "",
            "## 现在保留什么",
            "",
            "- `day001.md` 到 `day100.md`：100 份学习记录",
            "- `daily_log_template.md`：空白模板",
            "- `weekly_review_template.md`：每周复盘模板",
            "- `monthly_review_template.md`：每月复盘模板",
            "",
            "## 使用顺序",
            "",
            "1. 先打开阶段目录中的 `daily_guides/day_XXX.md`。",
            "2. 完成这一份学习日里的主要任务。",
            "3. 再填写对应的 `study_logs/dayXXX.md`。",
            "",
            "## 为什么这样改",
            "",
            "- 文件更少，界面更干净。",
            "- 入口和单元编号完全一致，不容易找错。",
            "- 详细的 10 天拆分内容仍然留在 `units/` 里，不会丢。",
            "",
        ]
    )


def daily_log_template() -> str:
    return "\n".join(
        [
            "# 学习日记录模板",
            "",
            "## 基本信息",
            "",
            "- 日期：",
            "- Day：",
            "- 对应单元：",
            "- 学习时长：",
            "",
            "## 今天完成了什么",
            "",
            "- ",
            "- ",
            "- ",
            "",
            "## 今天最重要的 3 个知识点",
            "",
            "1. ",
            "2. ",
            "3. ",
            "",
            "## 今天新认识的英语词汇",
            "",
            "- ",
            "- ",
            "- ",
            "",
            "## 今天我动手了什么",
            "",
            "- 运行：",
            "- 修改：",
            "- 验证：",
            "",
            "## 今天遇到的问题",
            "",
            "- ",
            "",
            "## 下一次先做什么",
            "",
            "- ",
            "- ",
            "",
        ]
    )


def progress_rows(start: int, end: int) -> list[str]:
    lines = [
        "| 完成 | 学习日 | 主题 | 完成 | 学习日 | 主题 |",
        "|------|--------|------|------|--------|------|",
    ]
    entries = [(unit_number, UNITS[unit_number - 1]["title"]) for unit_number in range(start, end + 1)]
    for index in range(0, len(entries), 2):
        left_number, left_title = entries[index]
        if index + 1 < len(entries):
            right_number, right_title = entries[index + 1]
            lines.append(
                f"| [ ] | Day {left_number:03d} | {left_title} | [ ] | Day {right_number:03d} | {right_title} |"
            )
        else:
            lines.append(f"| [ ] | Day {left_number:03d} | {left_title} |  |  |  |")
    return lines


def learning_progress_tracker() -> str:
    lines = [
        "# 学习进度总看板",
        "",
        "这个文件现在按 `100` 个学习日来追踪。",
        "每完成 1 个学习日，就等于完成了 1 个单元。",
        "",
        "## 阶段总进度",
        "",
    ]
    for stage_dir, stage_label, start, end in STAGES:
        lines.append(f"### {stage_label}")
        lines.append("")
        lines.append(f"- 范围：`Day {start:03d}-{end:03d}`")
        lines.append("")
        lines.extend(progress_rows(start, end))
        lines.append("")
    lines.extend(
        [
            "## 当前所处位置",
            "",
            "- 当前日期：",
            "- 当前 Day：",
            "- 当前单元：",
            "- 当前阶段：",
            "",
            "## 本周重点",
            "",
            "- ",
            "- ",
            "- ",
            "",
            "## 本月重点",
            "",
            "- ",
            "- ",
            "- ",
            "",
        ]
    )
    return "\n".join(lines)


def hundred_day_master_plan() -> str:
    lines = [
        "# 100 天学习总计划",
        "",
        "这是一套按 `100` 个学习日展开的总导航。",
        "规则很简单：`1 个单元 = 1 个学习日`。",
        f"学习顺序总导航在：`{LEARNING_NAV_FILE}`。",
        f"配套英语主线在：`{ENGLISH_ROUTE_FILE}`。",
        "",
        "## 这套 100 天怎么用",
        "",
        "1. 每次先打开对应阶段的 `daily_guides/day_XXX.md`。",
        "2. 再进入 `units/unit_XXX.md` 看完整讲义。",
        "3. 再做工作簿、代码模板、参考答案和小测。",
        "4. 最后写 `study_logs/dayXXX.md`。",
        "",
        "## 阶段总览",
        "",
        "| 阶段 | Day 范围 | 重点 |",
        "|------|----------|------|",
        "| 第 1 阶段：入门基础 | Day 001-010 | Python 最基础动作与小程序 |",
        "| 第 2 阶段：成长进阶 | Day 011-030 | Python 进阶、Git、前端基础、Flask 入口 |",
        "| 第 3 阶段：高级进阶 | Day 031-060 | 后端、算法、数据分析与自动化 |",
        "| 第 4 阶段：专家深化 | Day 061-085 | React、FastAPI、部署与工程质量 |",
        "| 第 5 阶段：大师输出 | Day 086-100 | 系统、表达、求职、毕业项目 |",
        "",
    ]
    for stage_dir, stage_label, start, end in STAGES:
        lines.append(f"## {stage_label}")
        lines.append("")
        for unit_number in range(start, end + 1):
            unit = UNITS[unit_number - 1]
            lines.extend(
                [
                    f"### Day {unit_number:03d}：{unit['title']}",
                    f"- 4 个核心点：{'；'.join(unit['prog'])}",
                    f"- 英语句子：`{unit['sentence']}`",
                    f"- 最终产出：{unit['output']}",
                    "",
                ]
            )
    return "\n".join(lines)


def learning_navigation() -> str:
    lines = [
        "# 学习顺序总导航",
        "",
        "这份文件只做一件事：把整套仓库的学习顺序讲清楚。",
        "",
        "## 零基础默认顺序",
        "",
        f"1. 先看 `{START_GUIDE_FILE}`。",
        f"2. 再看 `{MASTER_PLAN_FILE}`。",
        "3. 再打开当天 `daily_guides/day_XXX.md`。",
        "4. 再进当天 `units/unit_XXX.md`。",
        "5. 再做 `workbooks/`、`code_templates/`、`code_solutions/`、`quizzes/`。",
        "6. 写 `study_logs/dayXXX.md`。",
        f"7. 在 `{TRACKER_FILE}` 打勾。",
        f"8. 最后补 `{ENGLISH_ROUTE_FILE}` 对应的当天英语任务。",
        "",
        "## 每天固定顺序",
        "",
        "1. 学习日入口",
        "2. 单元讲义",
        "3. 工作簿",
        "4. 模板代码",
        "5. 参考答案",
        "6. 小测",
        "7. 学习日志",
        "8. 进度打勾",
        "9. 英语同步练习",
        "",
        "## 阶段导航",
        "",
    ]
    for stage_dir, stage_label, start, end in STAGES:
        lines.extend(
            [
                f"### {stage_label}",
                f"- Day 范围：`Day {start:03d}-{end:03d}`",
                f"- 阶段主页：`{stage_dir}/README.md`",
                f"- 学习日目录：`{stage_dir}/daily_guides/README.md`",
                f"- 单元目录：`{stage_dir}/units/README.md`",
                "",
            ]
        )
    lines.extend(
        [
            "## 特殊资料什么时候用",
            "",
            "- `project_packs/`：里程碑项目单元再打开，不是每一天都要先看。",
            f"- `{ENGLISH_ROUTE_FILE}`：每天都用，但只做对应 Day。",
            "- `study_logs/`：每天都写，不要攒着。",
            f"- `{TRACKER_FILE}`：每天完成后再打勾。",
            "",
        ]
    )
    return "\n".join(lines)


def cleanup_daily_guides(repo_root: Path) -> None:
    for stage_dir, _, _, _ in STAGES:
        daily_dir = repo_root / stage_dir / "daily_guides"
        daily_dir.mkdir(parents=True, exist_ok=True)
        for path in daily_dir.glob("day_*.md"):
            path.unlink()


def cleanup_study_logs(repo_root: Path) -> None:
    study_logs = repo_root / "study_logs"
    study_logs.mkdir(parents=True, exist_ok=True)
    for path in study_logs.glob("day*.md"):
        path.unlink()
    for path in study_logs.glob("index_*.md"):
        path.unlink()


def write_stage_daily_guides(repo_root: Path) -> None:
    cleanup_daily_guides(repo_root)
    for stage_dir, stage_label, start, end in STAGES:
        daily_dir = repo_root / stage_dir / "daily_guides"
        (daily_dir / "README.md").write_text(stage_daily_readme(stage_label, start, end), encoding="utf-8")
        for unit_number in range(start, end + 1):
            (daily_dir / f"day_{unit_number:03d}.md").write_text(
                merged_day_text(repo_root, unit_number),
                encoding="utf-8",
            )


def write_study_logs(repo_root: Path) -> None:
    cleanup_study_logs(repo_root)
    study_logs = repo_root / "study_logs"
    (study_logs / "README.md").write_text(study_logs_readme(), encoding="utf-8")
    (study_logs / "daily_log_template.md").write_text(daily_log_template(), encoding="utf-8")
    for unit_number in range(1, 101):
        (study_logs / f"day{unit_number:03d}.md").write_text(study_log_text(unit_number), encoding="utf-8")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    write_stage_daily_guides(repo_root)
    write_study_logs(repo_root)
    (repo_root / MASTER_PLAN_FILE).write_text(hundred_day_master_plan(), encoding="utf-8")
    (repo_root / TRACKER_FILE).write_text(learning_progress_tracker(), encoding="utf-8")
    (repo_root / LEARNING_NAV_FILE).write_text(learning_navigation(), encoding="utf-8")


if __name__ == "__main__":
    main()
