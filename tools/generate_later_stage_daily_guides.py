from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


STAGES = [
    ("stage2_growth", "第 2 阶段：成长进阶", 11, 30),
    ("stage3_advanced", "第 3 阶段：高级进阶", 31, 60),
    ("stage4_expert", "第 4 阶段：专家深化", 61, 85),
    ("stage5_master", "第 5 阶段：大师输出", 86, 100),
]


DAY_PATTERNS = [
    ("开场定位", "先把单元主题、四个核心点和最终产出连起来。"),
    ("跑通起步包", "先把起步模板或起步包读通、跑通、看懂结构。"),
    ("改第一版", "在起步包基础上改第一版，建立自己的版本。"),
    ("解释结构", "用中文解释文件结构、主流程和关键部件。"),
    ("核心主题 A", "聚焦第一个核心点，做最小练习。"),
    ("核心主题 B", "继续推进第二个核心点，和前面的内容连起来。"),
    ("核心主题 C", "把第三个核心点放进真实任务里，不只停在概念。"),
    ("核心主题 D / 挑战", "尝试第四个核心点或小挑战，允许慢，但必须动手。"),
    ("整合输出", "围绕单元产出拼成一个最小可运行成果。"),
    ("复盘提交", "做小测、写复盘、提交版本，让这个单元真正收口。"),
]


MODE_HINTS = {
    "python": {
        "snippet": """data = ["step1", "step2", "step3"]
for item in data:
    print(item)""",
        "mistakes": [
            "只看不跑，结果以为自己会了。",
            "改了变量名，后面的引用却没一起改。",
            "把报错直接跳过，没有先读最后一行。",
        ],
    },
    "git": {
        "snippet": """git status
git add .
git commit -m "study progress"
git push""",
        "mistakes": [
            "改完文件却忘了 `git add`。",
            "提交信息太空，不知道这次改了什么。",
            "只会 push，不会先看 `git status`。",
        ],
    },
    "html": {
        "snippet": """<!doctype html>
<html lang="zh-CN">
  <body>
    <h1>Hello HTML</h1>
  </body>
</html>""",
        "mistakes": [
            "标签开了却没关，结构乱掉。",
            "只看页面效果，不看 HTML 结构本身。",
            "语义标签和普通标签混着用但自己说不清区别。",
        ],
    },
    "css": {
        "snippet": """body {
  margin: 0;
  padding: 24px;
}

.card {
  background: white;
}""",
        "mistakes": [
            "样式改了却没刷新页面。",
            "类名写错，导致样式没生效。",
            "一开始就堆很多样式，结果自己也看不懂。",
        ],
    },
    "javascript": {
        "snippet": """const button = document.querySelector("#btn");
button.addEventListener("click", () => {
  console.log("clicked");
});""",
        "mistakes": [
            "脚本先于元素执行，选择器拿不到节点。",
            "事件绑定了，但没确认有没有真的触发。",
            "变量、函数、节点名字混着写，自己后来分不清。",
        ],
    },
    "react": {
        "snippet": """import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}""",
        "mistakes": [
            "组件拆太多，但自己说不清数据从哪来。",
            "状态更新了，却没理解为什么界面会重新渲染。",
            "只会复制组件，不会先做最小可运行版本。",
        ],
    },
    "typescript": {
        "snippet": """type Task = {
  title: string;
  done: boolean;
};

const currentTask: Task = { title: "study", done: false };""",
        "mistakes": [
            "类型和真实值对不上。",
            "只顾着消灭报错，不理解类型在保护什么。",
            "接口、类型、变量命名太乱。",
        ],
    },
    "flask": {
        "snippet": """from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
""",
        "mistakes": [
            "路由能跑，但自己说不清请求是怎么进来的。",
            "只关注结果页面，不理解函数和返回值。",
            "一改动就报错，但没有先看终端输出。",
        ],
    },
    "fastapi": {
        "snippet": """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ok"}""",
        "mistakes": [
            "接口能返回数据，但不知道参数校验在哪里发生。",
            "路径、方法、返回结构混着记。",
            "只会照抄，不会自己改一个字段试试。",
        ],
    },
    "sql": {
        "snippet": """SELECT name, score
FROM students
WHERE score >= 90
ORDER BY score DESC;""",
        "mistakes": [
            "查数据前没想清楚要哪几列。",
            "条件和排序一起用时容易写乱。",
            "只看结果，不解释查询语句每一段在做什么。",
        ],
    },
    "api": {
        "snippet": """import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())""",
        "mistakes": [
            "拿到 JSON 就慌，不先观察结构。",
            "状态码和数据内容混为一谈。",
            "接口出错时只看页面，不看错误信息。",
        ],
    },
    "data": {
        "snippet": """import pandas as pd

df = pd.DataFrame({"name": ["Li Hua", "Amy"], "score": [95, 88]})
print(df)
print(df["score"].mean())""",
        "mistakes": [
            "没有先看数据长什么样，就急着分析。",
            "列名拼错导致结果不对。",
            "图画出来了，但说不清结论是什么。",
        ],
    },
    "ops": {
        "snippet": """FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]""",
        "mistakes": [
            "环境没跑通就开始改复杂配置。",
            "把部署问题误以为是代码逻辑问题。",
            "看到工具链复杂就不肯先做最小版本。",
        ],
    },
    "algo": {
        "snippet": """def solve(numbers):
    total = 0
    for number in numbers:
        total += number
    return total""",
        "mistakes": [
            "一上来就追求最优解，最小可运行版都没做出来。",
            "没有先手写样例就开始写代码。",
            "代码写完了，但不会自己验证边界情况。",
        ],
    },
    "engineering": {
        "snippet": """## Review notes

- Current problem:
- Refactor target:
- Next small step:""",
        "mistakes": [
            "只会加代码，不愿意删乱代码。",
            "看到“重构、模式、性能”就觉得抽象，其实要先抓一个具体例子。",
            "写完功能后，不复盘为什么现在结构更好或更差。",
        ],
    },
    "career": {
        "snippet": """## Project summary

- Problem
- Solution
- Result""",
        "mistakes": [
            "以为写作和表达不是技术能力。",
            "只写做了什么，不写为什么有价值。",
            "作品很多，但没有整理成别人看得懂的材料。",
        ],
    },
}


def load_units():
    tool_path = Path(__file__).resolve().parent / "generate_1000_day_plan.py"
    spec = spec_from_file_location("generate_1000_day_plan", tool_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.UNITS


def stage_for_unit(unit_number):
    for stage_dir, stage_label, start, end in STAGES:
        if start <= unit_number <= end:
            return stage_dir, stage_label, start, end
    raise ValueError(unit_number)


def words_of(unit):
    return [word.strip() for word in unit["words"].split(",") if word.strip()]


def mode_of(unit):
    text = " ".join([unit["title"], *unit["prog"]])
    if "Node" in text or "npm" in text or "Vite" in text or "package.json" in text:
        return "javascript"
    if "HTML" in text:
        return "html"
    if "CSS" in text or "布局" in text:
        return "css"
    if "JavaScript" in text or "DOM" in text or "事件" in text:
        return "javascript"
    if "React" in text or "Hooks" in text or "JSX" in text or "Context" in text:
        return "react"
    if "TypeScript" in text:
        return "typescript"
    if "Flask" in text:
        return "flask"
    if "FastAPI" in text or "Pydantic" in text or "JWT" in text or "SQLAlchemy" in text:
        return "fastapi"
    if any(word in text for word in ["作品集", "写作", "演示", "简历", "面试", "毕业", "复盘"]):
        return "career"
    if "SQL" in text or "数据库" in text or "SQLite" in text:
        return "sql"
    if "API" in text or "JSON" in text or "requests" in text:
        return "api"
    if "Pandas" in text or "数据" in text or "Excel" in text or "ETL" in text or "抓取" in text:
        return "data"
    if "Docker" in text or "Linux" in text or "CI/CD" in text or "云" in text:
        return "ops"
    if "Git" in text:
        return "git"
    if any(word in text for word in ["数组", "哈希", "栈", "队列", "递归", "回溯", "排序", "树", "图", "堆", "贪心", "复杂度", "伪代码"]):
        return "algo"
    if any(word in text for word in ["重构", "设计模式", "性能", "消息队列", "系统设计", "日志", "监控", "安全", "开源"]):
        return "engineering"
    return "python"


def day_number(unit_number, offset):
    return (unit_number - 1) * 10 + offset + 1


def file_paths(stage_dir, unit_number):
    return {
        "unit": f"{stage_dir}/units/unit_{unit_number:03d}.md",
        "workbook": f"{stage_dir}/workbooks/unit_{unit_number:03d}_workbook.md",
        "template": f"{stage_dir}/code_templates/unit_{unit_number:03d}_template.md",
        "solution": f"{stage_dir}/code_solutions/unit_{unit_number:03d}_solution.md",
        "quiz": f"{stage_dir}/quizzes/unit_{unit_number:03d}_quiz.md",
    }


def tasks_for_day(unit, stage_dir, unit_number, day_index):
    files = file_paths(stage_dir, unit_number)
    topics = unit["prog"]
    output = unit["output"]
    if day_index == 0:
        return [
            f"打开 `{files['unit']}`，先读完单元目标、四个核心点和 10 天安排。",
            f"把本单元最终产出 `{output}` 抄到学习笔记里。",
            f"圈出今天最陌生的 3 个词：`{', '.join(words_of(unit)[:3])}`。",
        ]
    if day_index == 1:
        return [
            f"打开 `{files['template']}`，先完整读一遍。",
            "如果能运行，就跑起来；如果只是模板说明，就把文件结构讲一遍。",
            "用一句中文写下：这个起步包最重要的入口是什么。",
        ]
    if day_index == 2:
        return [
            f"在 `{files['template']}` 的思路上改第一版，至少改 3 处。",
            "每改一次就运行、刷新、验证或读输出。",
            "把今天最像自己版本的一份保留下来。",
        ]
    if day_index == 3:
        return [
            "解释文件结构：哪些文件负责入口，哪些负责样式、逻辑或数据。",
            "至少挑 3 段代码或说明，写出“为什么要有它”。",
            "把你最不理解的一个点写进学习日志。",
        ]
    if day_index == 4:
        return [
            f"围绕 `{topics[0]}` 做一个最小练习。",
            "先做最小版本，再说复杂版本。",
            "练完后用一句中文总结：它到底解决了什么问题。",
        ]
    if day_index == 5:
        return [
            f"围绕 `{topics[1]}` 做第二个最小练习。",
            f"把 `{topics[0]}` 和 `{topics[1]}` 连在一起试一次。",
            "记录连接这两块内容时最卡的地方。",
        ]
    if day_index == 6:
        return [
            f"围绕 `{topics[2]}` 做实际改动，不要只停在阅读。",
            "把今天学到的词汇尽量放回代码、注释或页面文字里。",
            "做完后回头看：今天的代码哪里最能体现这个主题。",
        ]
    if day_index == 7:
        return [
            f"围绕 `{topics[3]}` 做一个小挑战，先追求可运行。",
            "如果卡住，先缩小问题，不要直接放弃。",
            f"卡到走不下去时，再对照 `{files['solution']}`。",
        ]
    if day_index == 8:
        return [
            f"今天把单元产出 `{output}` 拼成最小完整版本。",
            "先保证主流程通，再慢慢补细节和美化。",
            "从头到尾演示一次，确认自己知道输入、处理、输出在哪里。",
        ]
    return [
        f"完成 `{files['quiz']}` 小测。",
        "写 3 条复盘：我会了什么、我最容易错什么、下个单元我要先抓什么。",
        "执行一次 Git 提交，把这个单元真正收口。",
    ]


def output_for_day(unit, day_index):
    if day_index == 0:
        return "写出本单元目标和最终产出的中文说明。"
    if day_index == 1:
        return "说清起步包或起步模板的入口文件和作用。"
    if day_index == 2:
        return "得到自己的第一版改写结果。"
    if day_index == 3:
        return "写出一份结构说明或逐段解释笔记。"
    if day_index in {4, 5, 6, 7}:
        return "完成一个围绕今天主题的最小练习。"
    if day_index == 8:
        return f"完成 `{unit['output']}` 的最小可运行版本。"
    return "完成小测、日志和一次提交记录。"


def review_questions(unit, day_index):
    if day_index < 8:
        return [
            f"今天的主题 `{unit['title']}` 在真实项目里到底是干什么的？",
            "我今天是看懂了一点，还是亲手跑通和改过了？",
            "如果明天忘了，我今天的笔记和文件能不能把我拉回来？",
        ]
    return [
        f"我现在能不能把 `{unit['output']}` 的最小版本从头讲给别人听？",
        "这一单元最值得保留的代码、页面、结果或笔记是哪一个？",
        "下一个单元开始前，我最该先补稳的薄弱点是什么？",
    ]


def daily_text(unit, stage_dir, stage_label, unit_number, day_index):
    day_no = day_number(unit_number, day_index)
    files = file_paths(stage_dir, unit_number)
    mode = mode_of(unit)
    hint = MODE_HINTS[mode]
    pattern_name, pattern_goal = DAY_PATTERNS[day_index]
    tasks = "\n".join([f"{idx + 1}. {item}" for idx, item in enumerate(tasks_for_day(unit, stage_dir, unit_number, day_index))])
    mistakes = "\n".join([f"- {item}" for item in hint["mistakes"]])
    review = "\n".join([f"- {item}" for item in review_questions(unit, day_index)])
    words = words_of(unit)
    vocab_slice = words[:3] if day_index < 5 else words[3:6]
    vocab_text = ", ".join(vocab_slice) if vocab_slice else ", ".join(words[:3])
    checks = [
        "- [ ] 我今天至少亲手运行、验证或解释过 1 次。",
        "- [ ] 我今天至少亲手改过 1 处。",
        "- [ ] 我今天留下了一条真实的卡点记录。",
    ]
    if day_index >= 8:
        checks.append("- [ ] 我今天把零散知识拼成了一个更完整的成果。")

    lines = [
        f"# Day {day_no:03d}：{unit['title']} - {pattern_name}",
        "",
        f"- 所属阶段：{stage_label}",
        f"- 所属单元：`unit_{unit_number:03d}`",
        f"- 单元最终产出：{unit['output']}",
        "- 建议时长：70 到 110 分钟",
        "",
        "## 今天只要先抓这一件事",
        "",
        pattern_goal,
        "",
        "## 今天先这样理解",
        "",
        f"这一单元的主线一直是 `{unit['output']}`。今天不是追求学完全部，而是围绕当前焦点往前推进一小步，并且留下能回看的结果。",
        "",
        "## 今日示例",
        "",
        "```",
        hint["snippet"],
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
        f"- 今天重点词：`{vocab_text}`",
        "- 先读 3 遍，再用中文说出大意。",
        "",
        "## 常见错误",
        "",
        mistakes,
        "",
        "## 今天最小产出",
        "",
        f"- {output_for_day(unit, day_index)}",
        "",
        "## 完成后检查",
        "",
        *checks,
        "",
        "## 复盘问题",
        "",
        review,
        "",
        "## 学完后顺手做",
        "",
        f"- 去 `study_logs/day{day_no:03d}.md` 写今天的记录；如果还没有，就先复制 `study_logs/daily_log_template.md`。",
        "- 如果今天是这个单元的第 10 天，做完小测后执行一次 Git 提交。",
        "",
    ]
    return "\n".join(lines)


def stage_readme_text(stage_dir, stage_label, start_unit, end_unit, units):
    lines = [
        f"# {stage_label} 逐日学习指南",
        "",
        f"这个目录把 `{stage_label}` 对应的所有内容拆成了可以每天直接打开学习的文件。",
        "",
        "建议顺序：",
        "1. 先看当天的逐日指南。",
        "2. 再看对应单元讲义。",
        "3. 再做工作簿和起步模板。",
        "4. 最后做小测和学习日志。",
        "",
        "## 单元导航",
        "",
    ]
    for unit_number in range(start_unit, end_unit + 1):
        unit = units[unit_number - 1]
        start_day = day_number(unit_number, 0)
        end_day = day_number(unit_number, 9)
        lines.append(f"### 单元 {unit_number:03d}：{unit['title']}（Day {start_day:03d}-{end_day:03d}）")
        lines.append("")
        for offset in range(10):
            day_no = day_number(unit_number, offset)
            lines.append(f"- [Day {day_no:03d}](day_{day_no:03d}.md)")
        lines.append("")
    return "\n".join(lines)


def main():
    repo_root = Path(__file__).resolve().parents[1]
    units = load_units()

    for stage_dir, stage_label, start_unit, end_unit in STAGES:
        daily_dir = repo_root / stage_dir / "daily_guides"
        daily_dir.mkdir(parents=True, exist_ok=True)
        (daily_dir / "README.md").write_text(
            stage_readme_text(stage_dir, stage_label, start_unit, end_unit, units),
            encoding="utf-8",
        )

        for unit_number in range(start_unit, end_unit + 1):
            unit = units[unit_number - 1]
            for offset in range(10):
                day_no = day_number(unit_number, offset)
                text = daily_text(unit, stage_dir, stage_label, unit_number, offset)
                (daily_dir / f"day_{day_no:03d}.md").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
