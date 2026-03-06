from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


STAGES = [
    ("stage1_foundation", "第 1 阶段：入门基础", 1, 10),
    ("stage2_growth", "第 2 阶段：成长进阶", 11, 30),
    ("stage3_advanced", "第 3 阶段：高级进阶", 31, 60),
    ("stage4_expert", "第 4 阶段：专家深化", 61, 85),
    ("stage5_master", "第 5 阶段：大师输出", 86, 100),
]


def load_units():
    tool_path = Path(__file__).resolve().parent / "generate_1000_day_plan.py"
    spec = spec_from_file_location("generate_1000_day_plan", tool_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.UNITS


def stage_for_unit(unit_number):
    for stage_dir, stage_label, start, end in STAGES:
        if start <= unit_number <= end:
            return stage_dir, stage_label
    raise ValueError(unit_number)


def words_of(unit):
    return [word.strip() for word in unit["words"].split(",") if word.strip()]


def day_info(day_number, units):
    unit_number = (day_number - 1) // 10 + 1
    local_day = (day_number - 1) % 10 + 1
    unit = units[unit_number - 1]
    stage_dir, stage_label = stage_for_unit(unit_number)
    return {
        "day_number": day_number,
        "unit_number": unit_number,
        "local_day": local_day,
        "unit": unit,
        "stage_dir": stage_dir,
        "stage_label": stage_label,
    }


def file_refs(info):
    day_number = info["day_number"]
    unit_number = info["unit_number"]
    stage_dir = info["stage_dir"]
    return {
        "daily_guide": f"{stage_dir}/daily_guides/day_{day_number:03d}.md",
        "unit": f"{stage_dir}/units/unit_{unit_number:03d}.md",
        "workbook": f"{stage_dir}/workbooks/unit_{unit_number:03d}_workbook.md",
        "template": f"{stage_dir}/code_templates/unit_{unit_number:03d}_template{' .py' if stage_dir == 'stage1_foundation' else '.md'}",
        "solution": f"{stage_dir}/code_solutions/unit_{unit_number:03d}_solution{' .py' if stage_dir == 'stage1_foundation' else '.md'}",
        "quiz": f"{stage_dir}/quizzes/unit_{unit_number:03d}_quiz.md",
    }


def normalized_refs(info):
    refs = file_refs(info)
    refs["template"] = refs["template"].replace(" ", "")
    refs["solution"] = refs["solution"].replace(" ", "")
    return refs


def next_step(info, units):
    day_number = info["day_number"]
    unit_number = info["unit_number"]
    local_day = info["local_day"]
    if day_number == 1000:
        return [
            "回看整套 1000 天资料，整理长期保留的作品和笔记。",
            "写下一份下一阶段计划：继续深入哪个方向。",
        ]
    if local_day < 10:
        next_day = day_number + 1
        next_info = day_info(next_day, units)
        return [
            f"直接去对应逐日指南：`{next_info['stage_dir']}/daily_guides/day_{next_day:03d}.md`。",
            "先复习今天最容易错的 1 个点，再继续下一天。",
        ]
    next_unit = unit_number + 1
    next_stage_dir, _ = stage_for_unit(next_unit)
    return [
        f"明天进入下一个单元：`{next_stage_dir}/daily_guides/day_{day_number + 1:03d}.md`。",
        "先把这一单元的最终产出和错点回看 5 分钟，再开新单元。",
    ]


def log_text(info, units):
    day_number = info["day_number"]
    unit_number = info["unit_number"]
    local_day = info["local_day"]
    unit = info["unit"]
    refs = normalized_refs(info)
    vocab = words_of(unit)[:5]
    tomorrow = next_step(info, units)

    lines = [
        f"# Day {day_number:03d} 学习记录",
        "",
        "## 基本信息",
        "",
        "- 日期：",
        f"- 第几天：Day {day_number:03d}",
        f"- 所属阶段：{info['stage_label']}",
        f"- 所属单元：unit_{unit_number:03d} - {unit['title']}",
        f"- 单元内第几天：第 {local_day} / 10 天",
        "- 学习时长：",
        "",
        "## 今天建议先打开的文件",
        "",
        f"- 逐日指南：`{refs['daily_guide']}`",
        f"- 单元讲义：`{refs['unit']}`",
        f"- 工作簿：`{refs['workbook']}`",
        f"- 代码模板：`{refs['template']}`",
        f"- 参考答案：`{refs['solution']}`",
        f"- 小测：`{refs['quiz']}`",
        "",
        "## 今天我学了什么",
        "",
        f"- 单元主题：{unit['title']}",
        f"- 单元最终产出：{unit['output']}",
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
    ]
    for word in vocab:
        lines.append(f"- {word}")
    lines.extend(
        [
            "",
            "## 今天我运行了什么代码或看了什么关键片段",
            "",
            "```text",
            "把你今天练习过的关键代码、命令、页面结构或查询语句放在这里",
            "```",
            "",
            "## 今天我做出的最小成果",
            "",
            "- ",
            "",
            "## 今天我遇到的问题",
            "",
            "- ",
            "",
            "## 我现在还不懂的地方",
            "",
            "- ",
            "",
            "## 明天我要做什么",
            "",
        ]
    )
    for item in tomorrow:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 给老师的话",
            "",
            "- ",
            "",
        ]
    )
    return "\n".join(lines)


def range_index_text(start_day, end_day, units):
    lines = [
        f"# Day {start_day:03d}-{end_day:03d} 学习日志目录",
        "",
        "这个文件用来快速跳转到这一段的每日学习日志。",
        "",
    ]
    current = start_day
    while current <= end_day:
        info = day_info(current, units)
        unit_number = info["unit_number"]
        unit = info["unit"]
        unit_end = min(end_day, current + 9)
        lines.append(f"## 单元 {unit_number:03d}：{unit['title']}（Day {current:03d}-{unit_end:03d}）")
        lines.append("")
        for day in range(current, unit_end + 1):
            lines.append(f"- [day{day:03d}.md](day{day:03d}.md)")
        lines.append("")
        current += 10
    return "\n".join(lines)


def readme_text():
    return """# 学习记录说明

这个目录用来保存你的学习轨迹。

现在已经预生成了 `Day 001` 到 `Day 1000` 的每日学习日志文件，你可以直接打开对应 `dayNNN.md` 填写，不需要再手工复制模板。

## 目录结构

- `day001.md` 到 `day1000.md`：每天对应一份学习记录
- `index_001_100.md` 到 `index_901_1000.md`：按 100 天分段的日志导航
- `daily_log_template.md`：通用空白模板
- `weekly_review_template.md`：每周复盘模板
- `monthly_review_template.md`：每月复盘模板

## 使用方式

1. 先打开当天的逐日指南。
2. 学完后直接填写当天对应的 `dayNNN.md`。
3. 每周结束时填写 `weekly_review_template.md`。
4. 每月结束时填写 `monthly_review_template.md`。

## 为什么一定要写学习记录

因为零基础最容易出现两个问题：

1. 学了以后很快忘。
2. 不知道自己到底进步了什么。

每天写几分钟记录，可以帮你做到：

- 看见自己真正完成了什么
- 复习当天最重要的内容
- 积累以后复盘要用的材料
- 在 GitHub 上留下连续学习痕迹

## 日志导航

- `index_001_100.md`
- `index_101_200.md`
- `index_201_300.md`
- `index_301_400.md`
- `index_401_500.md`
- `index_501_600.md`
- `index_601_700.md`
- `index_701_800.md`
- `index_801_900.md`
- `index_901_1000.md`
"""


def main():
    repo_root = Path(__file__).resolve().parents[1]
    study_logs = repo_root / "study_logs"
    study_logs.mkdir(parents=True, exist_ok=True)
    units = load_units()

    for day_number in range(1, 1001):
        path = study_logs / f"day{day_number:03d}.md"
        if path.exists():
            continue
        path.write_text(log_text(day_info(day_number, units), units), encoding="utf-8")

    for start_day in range(1, 1000, 100):
        end_day = start_day + 99
        index_path = study_logs / f"index_{start_day:03d}_{end_day:03d}.md"
        index_path.write_text(range_index_text(start_day, end_day, units), encoding="utf-8")

    (study_logs / "README.md").write_text(readme_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
