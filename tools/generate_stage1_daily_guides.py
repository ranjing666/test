from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


DAY_PATTERNS = [
    {
        "name": "开场定位",
        "goal": "先把单元主题、关键词和最终小项目连起来，不追求一次学很多。",
        "coach": "今天是开场日。你只需要知道这一单元在解决什么问题，以及最后要做出什么。",
    },
    {
        "name": "跑通模板",
        "goal": "先把现成模板跑起来，确认你会保存、运行、观察结果。",
        "coach": "零基础最重要的不是背定义，而是先让代码真的跑起来。",
    },
    {
        "name": "第一次改代码",
        "goal": "把模板改成自己的版本，建立“改一处、跑一次”的习惯。",
        "coach": "只有你自己动手改过，知识点才会开始变成自己的东西。",
    },
    {
        "name": "解释代码",
        "goal": "把今天看到的代码拆开，用中文说明每一部分在做什么。",
        "coach": "你现在不需要写复杂程序，但要开始训练“我知道它为什么这样写”。",
    },
    {
        "name": "跟练任务",
        "goal": "按讲义和工作簿完成一轮跟练，把核心动作做熟。",
        "coach": "今天的重点不是快，而是按照步骤把一个最小练习做完整。",
    },
    {
        "name": "基础练习 A",
        "goal": "开始脱离模板，自己完成第一轮基础练习。",
        "coach": "你会发现从“照着写”变成“自己写一点”时最容易卡住，这很正常。",
    },
    {
        "name": "基础练习 B",
        "goal": "继续完成基础练习，并把英语词汇塞回代码场景里。",
        "coach": "今天要把编程和英语绑在一起学，避免两个方向各学各的。",
    },
    {
        "name": "提升挑战",
        "goal": "尝试单元里的提升练习，允许慢，但要亲手试。",
        "coach": "今天不是为了做得多高级，而是为了建立“我敢试”的动作。",
    },
    {
        "name": "组装小项目",
        "goal": "把这一单元的零散知识拼起来，做出一个最小可运行成果。",
        "coach": "今天要从散点练习切换到完整成果，重点是能跑、能解释、能保存。",
    },
    {
        "name": "复盘与提交",
        "goal": "通过小测、日志和 Git 提交，把这个单元收口。",
        "coach": "如果只学不复盘，过几天就会糊。今天的任务是把这 10 天真正关掉。",
    },
]


UNIT_HINTS = {
    1: {
        "demo": """print("Hello")
name = input("What is your name? ")
print("Hello,", name)""",
        "mistakes": [
            "改完代码忘记保存，结果运行出来还是旧内容。",
            "把文件保存成了 `.txt`，不是 `.py`。",
            "修改后没有重新运行，就以为程序没变化。",
        ],
    },
    2: {
        "demo": """# 这是标题
print("Welcome")
print("欢迎来到 Python")""",
        "mistakes": [
            "把注释写成普通文本，忘了前面的 `#`。",
            "输出文字漏了引号。",
            "版面太乱，自己回头看不懂。",
        ],
    },
    3: {
        "demo": """name = input("What is your name? ")
city = input("Which city do you live in? ")
print("Hello,", name)
print("City:", city)""",
        "mistakes": [
            "把变量名和字符串混为一谈。",
            "输入后没有保存到变量里。",
            "以为 `=` 是数学里的相等，而不是赋值。",
        ],
    },
    4: {
        "demo": """a = 8
b = 3
print(a + b)
print(a * b)""",
        "mistakes": [
            "把文本数字和真正数字混用。",
            "忘了除法结果可能带小数。",
            "运算顺序没有加括号，结果和预期不一样。",
        ],
    },
    5: {
        "demo": """name = "Li Hua"
goal = "learn Python"
print("Hello, " + name)
print(f"My goal is to {goal}.")""",
        "mistakes": [
            "字符串拼接时漏了空格。",
            "把变量名写进引号里，导致显示成字面文本。",
            "格式化时大括号或引号没配对。",
        ],
    },
    6: {
        "demo": """score = 85
print(score >= 60)
print(score == 100)""",
        "mistakes": [
            "把 `=` 和 `==` 搞混。",
            "以为布尔值是普通字符串。",
            "比较数字时左右顺序写反却没察觉。",
        ],
    },
    7: {
        "demo": """score = 72
if score >= 60:
    print("Pass")
else:
    print("Try again")""",
        "mistakes": [
            "缩进不一致导致语法错误。",
            "条件判断写完后忘了冒号。",
            "`if`、`elif`、`else` 的顺序混乱。",
        ],
    },
    8: {
        "demo": """count = 1
while count <= 3:
    print(count)
    count += 1""",
        "mistakes": [
            "忘记更新计数器，导致死循环。",
            "循环条件写错，次数不对。",
            "缩进位置错，更新代码没有放进循环体里。",
        ],
    },
    9: {
        "demo": """total = 0
for number in range(1, 6):
    total += number
print(total)""",
        "mistakes": [
            "没搞清楚 `range` 的结束位置不包含最后一个数。",
            "循环变量名字写错，后面用不了。",
            "累加语句缩进错，结果不对。",
        ],
    },
    10: {
        "demo": """def say_hello(name):
    print("Hello,", name)

say_hello("Li Hua")""",
        "mistakes": [
            "定义函数后忘了调用，所以程序没有输出。",
            "参数名字和传入值对应不上。",
            "把函数体缩进丢了，导致语法错误。",
        ],
    },
}


def load_units():
    tool_path = Path(__file__).resolve().parent / "generate_stage1_support.py"
    spec = spec_from_file_location("generate_stage1_support", tool_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.UNITS


def day_number(unit_number, offset):
    return (unit_number - 1) * 10 + offset + 1


def unit_files(unit_number):
    return {
        "unit": f"stage1_foundation/units/unit_{unit_number:03d}.md",
        "workbook": f"stage1_foundation/workbooks/unit_{unit_number:03d}_workbook.md",
        "template": f"stage1_foundation/code_templates/unit_{unit_number:03d}_template.py",
        "solution": f"stage1_foundation/code_solutions/unit_{unit_number:03d}_solution.py",
        "quiz": f"stage1_foundation/quizzes/unit_{unit_number:03d}_quiz.md",
    }


def snippet_for_day(unit_number, day_index):
    demo = UNIT_HINTS[unit_number]["demo"]
    if day_index in {0, 1, 2, 3}:
        return demo
    if day_index in {4, 5, 6, 7}:
        return demo + "\n# 修改一处，再运行一遍"
    return demo + "\n# 把它扩展成你自己的小项目版本"


def today_tasks(unit, unit_number, day_index):
    files = unit_files(unit_number)
    guided = unit["guided"]
    basic = unit["basic"]
    advanced = unit["advanced"]
    project_steps = unit["project_steps"]

    if day_index == 0:
        return [
            f"打开 `{files['unit']}`，先读本单元目标和 10 天安排。",
            f"把本单元 6 个词 `{', '.join(unit['vocab'])}` 抄到自己的笔记里。",
            f"写一句中文：这个单元最后要完成 `{unit['project']}`。",
        ]
    if day_index == 1:
        return [
            f"打开 `{files['template']}`，直接运行一次，确认能看到结果。",
            "把运行后的输出截图或用文字记录下来。",
            "如果报错，不要跳过，先把报错内容保存到学习日志里。",
        ]
    if day_index == 2:
        return [
            f"在 `{files['template']}` 里至少改 3 处内容。",
            "每改一处就运行一次，观察哪里变了。",
            "把你最满意的一版保存下来。",
        ]
    if day_index == 3:
        return [
            "把今天看到的代码逐行解释成中文。",
            "至少挑 3 行代码，写出“这一行为什么存在”。",
            "记下你现在最不理解的 1 个地方。",
        ]
    if day_index == 4:
        return [f"完成跟练：{guided[0]}", f"继续：{guided[1]}", f"最后：{guided[2]}"]
    if day_index == 5:
        return [f"完成基础练习：{basic[0]}", f"继续：{basic[1]}", "做完后运行并检查结果。"]
    if day_index == 6:
        return [f"完成基础练习：{basic[2]}", "把程序里的文字尽量改成你自己的真实信息。", "把今天出现的英文词再读 3 遍。"]
    if day_index == 7:
        return [f"尝试提升练习：{advanced[0]}", f"如果还有精力，再做：{advanced[1]}", "做不完也没关系，但必须自己先试。"]
    if day_index == 8:
        steps = [f"{idx + 1}. {step}" for idx, step in enumerate(project_steps)]
        return [
            f"今天把单元小项目 `{unit['project']}` 组装起来。",
            "按下面顺序做：" + " ".join(steps),
            f"卡住时再对照 `{files['solution']}`，不要一开始就看答案。",
        ]
    return [
        f"完成 `{files['quiz']}` 里的小测。",
        "把这 10 天最容易错的 3 个点写进学习日志。",
        "执行一次 Git 提交，把这个单元真正收口。",
    ]


def output_for_day(unit, unit_number, day_index):
    if day_index == 0:
        return "写出一段 3 句以内的中文目标说明。"
    if day_index == 1:
        return "成功运行模板，并能说出屏幕上出现了什么。"
    if day_index == 2:
        return "保存一份属于你自己的第一个改写版本。"
    if day_index == 3:
        return "写出一份逐行解释笔记。"
    if day_index in {4, 5, 6}:
        return "完成今天练习，并且至少独立改对一次。"
    if day_index == 7:
        return "完成至少 1 个提升练习尝试版。"
    if day_index == 8:
        return f"完成单元小项目：`{unit['project']}` 的最小可运行版。"
    return "完成小测、日志和一次提交记录。"


def review_questions(unit, unit_number, day_index):
    questions = [
        f"今天的主题 `{unit['title']}` 在程序里到底是干什么的？",
        "如果我明天忘了，今天这份文件能不能帮我重新捡起来？",
        "我今天是只看懂了，还是亲手改过并运行过？",
    ]
    if day_index >= 8:
        questions[1] = f"我现在能不能把 `{unit['project']}` 的最小版本从头讲给别人听？"
    return questions


def completion_checks(unit, unit_number, day_index):
    checks = [
        "我今天至少亲手运行过 1 次。",
        "我今天至少亲手修改过 1 次。",
        "我今天写下了一个真实的卡点或错点。",
    ]
    if day_index >= 8:
        checks.append("我今天把零散知识拼成了一个完整小成果。")
    return checks


def daily_text(unit, unit_number, day_index):
    day_no = day_number(unit_number, day_index)
    files = unit_files(unit_number)
    pattern = DAY_PATTERNS[day_index]
    hints = UNIT_HINTS[unit_number]
    vocab = ", ".join(unit["vocab"][:3]) if day_index < 5 else ", ".join(unit["vocab"][3:])
    tasks = "\n".join([f"{idx + 1}. {task}" for idx, task in enumerate(today_tasks(unit, unit_number, day_index))])
    mistakes = "\n".join([f"- {item}" for item in hints["mistakes"]])
    review = "\n".join([f"- {item}" for item in review_questions(unit, unit_number, day_index)])
    checks = "\n".join([f"- [ ] {item}" for item in completion_checks(unit, unit_number, day_index)])
    code_block = snippet_for_day(unit_number, day_index)

    lines = [
        f"# Day {day_no:03d}：{unit['title']} - {pattern['name']}",
        "",
        f"- 所属单元：`unit_{unit_number:03d}`",
        f"- 单元主题：{unit['title']}",
        f"- 单元最终产出：{unit['project']}",
        "- 建议时长：60 到 90 分钟",
        "",
        "## 今天只要先完成这件事",
        "",
        f"{pattern['goal']}",
        "",
        "## 今天先这样理解",
        "",
        f"{pattern['coach']} {unit['answer_tips'][0]}",
        "",
        "## 今日示例",
        "",
        "```python",
        code_block,
        "```",
        "",
        "## 今天要做什么",
        "",
        tasks,
        "",
        "## 今天要打开哪些文件",
        "",
        f"- `{files['unit']}`",
        f"- `{files['workbook']}`",
        f"- `{files['template']}`",
        f"- `{files['quiz']}`" if day_index == 9 else f"- `{files['solution']}` 只在真的卡住时再看",
        "",
        "## 今日英语",
        "",
        f"- 今日句子：`{unit['sentence']}`",
        f"- 今天先重点看：`{vocab}`",
        "- 先读 3 遍，再用中文说一遍大意。",
        "",
        "## 常见错误",
        "",
        mistakes,
        "",
        "## 今天最小产出",
        "",
        f"- {output_for_day(unit, unit_number, day_index)}",
        "",
        "## 完成后检查",
        "",
        checks,
        "",
        "## 复盘问题",
        "",
        review,
        "",
        "## 学完后顺手做",
        "",
        f"- 去 `study_logs/day{day_no:03d}.md` 记录今天做了什么。如果还没有这个文件，就先复制 `study_logs/daily_log_template.md`。",
        "- 如果今天是第 10 天，做完小测后执行一次 Git 提交。",
        "",
    ]
    return "\n".join(lines)


def readme_text(units):
    lines = [
        "# 第 1 阶段逐日学习指南",
        "",
        "这个目录把第 1 阶段 Day 001-100 拆成真正可以每天打开就学的文件。",
        "",
        "建议顺序：",
        "1. 先看对应单元讲义。",
        "2. 再打开当天的逐日指南。",
        "3. 然后做工作簿和代码模板。",
        "4. 最后做小测和学习日志。",
        "",
        "## 单元导航",
        "",
    ]
    for unit in units:
        unit_number = unit["unit"]
        start = day_number(unit_number, 0)
        end = day_number(unit_number, 9)
        lines.append(f"### 单元 {unit_number:03d}：{unit['title']}（Day {start:03d}-{end:03d}）")
        lines.append("")
        for offset in range(10):
            day_no = day_number(unit_number, offset)
            lines.append(f"- [Day {day_no:03d}](day_{day_no:03d}.md)")
        lines.append("")
    return "\n".join(lines)


def main():
    repo_root = Path(__file__).resolve().parents[1]
    daily_dir = repo_root / "stage1_foundation" / "daily_guides"
    daily_dir.mkdir(parents=True, exist_ok=True)

    units = load_units()
    (daily_dir / "README.md").write_text(readme_text(units), encoding="utf-8")

    for unit in units:
        unit_number = unit["unit"]
        for offset in range(10):
            day_no = day_number(unit_number, offset)
            text = daily_text(unit, unit_number, offset)
            (daily_dir / f"day_{day_no:03d}.md").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
