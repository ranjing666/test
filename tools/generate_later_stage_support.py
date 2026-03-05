from pathlib import Path

from generate_1000_day_plan import UNITS


STAGES = [
    ("stage2_growth", "第 2 阶段：成长进阶", 11, 30),
    ("stage3_advanced", "第 3 阶段：高级进阶", 31, 60),
    ("stage4_expert", "第 4 阶段：专家深化", 61, 85),
    ("stage5_master", "第 5 阶段：大师输出", 86, 100),
]


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
    if any(word in text for word in ["作品集", "写作", "演示", "简历", "面试", "毕业", "复盘"]):
        return "career"
    return "python"


def starter_pack(unit_number, unit):
    mode = mode_of(unit)
    title = unit["title"]
    topics = unit["prog"]

    if mode == "html":
        return [
            ("index.html", "html", f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
  </head>
  <body>
    <header>
      <h1>{title}</h1>
    </header>
    <main>
      <p>把这里改成你自己的内容。</p>
    </main>
  </body>
</html>"""),
        ]

    if mode == "css":
        return [
            ("index.html", "html", f"""<section class="card">
  <h1>{title}</h1>
  <p>请继续补充页面内容。</p>
</section>"""),
            ("style.css", "css", """body {
  margin: 0;
  padding: 24px;
  background: #f4f6fb;
  font-family: "Microsoft YaHei", sans-serif;
}

.card {
  max-width: 560px;
  margin: 0 auto;
  padding: 24px;
  background: white;
  border-radius: 16px;
}"""),
        ]

    if mode == "javascript":
        return [
            ("package.json", "json", """{
  "name": "study-starter",
  "private": true,
  "scripts": {
    "dev": "vite"
  }
}"""),
            ("main.js", "javascript", """const message = "Please continue the task.";
console.log(message);"""),
        ]

    if mode == "react":
        return [
            ("App.tsx", "tsx", f"""import "./styles.css";

export default function App() {{
  return (
    <main className="app">
      <h1>{title}</h1>
      <p>从这里继续补充你的组件。</p>
    </main>
  );
}}"""),
            ("styles.css", "css", """.app {
  padding: 24px;
  font-family: "Microsoft YaHei", sans-serif;
}"""),
        ]

    if mode == "typescript":
        return [
            ("main.ts", "ts", f"""type StudyTask = {{
  title: string;
  done: boolean;
}};

const currentTask: StudyTask = {{
  title: "{title}",
  done: false,
}};

console.log(currentTask);"""),
        ]

    if mode == "flask":
        return [
            ("app.py", "python", f"""from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "{title}"

if __name__ == "__main__":
    app.run(debug=True)"""),
        ]

    if mode == "fastapi":
        return [
            ("app.py", "python", """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "starter"}"""),
        ]

    if mode == "sql":
        return [
            ("schema.sql", "sql", """CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT
);"""),
            ("query.sql", "sql", """SELECT id, name
FROM items
ORDER BY id DESC;"""),
        ]

    if mode == "api":
        return [
            ("main.py", "python", """import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())"""),
        ]

    if mode == "data":
        return [
            ("main.py", "python", """import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Li Hua", "Amy", "David"],
        "score": [95, 88, 91],
    }
)

print(df)"""),
        ]

    if mode == "ops":
        return [
            ("Dockerfile", "dockerfile", """FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]"""),
            ("workflow.yml", "yaml", """name: basic-check

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4"""),
        ]

    if mode == "git":
        return [
            ("commands.md", "markdown", """## Git starter

```bash
git status
git add .
git commit -m "study progress"
git push
```"""),
        ]

    if mode == "algo":
        return [
            ("main.py", "python", """def solve(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(solve([1, 2, 3]))"""),
        ]

    if mode == "engineering":
        return [
            ("notes.md", "markdown", f"""## {title}

- Current problem:
- Current design:
- Current risk:
- Next improvement:
"""),
        ]

    if mode == "career":
        return [
            ("outline.md", "markdown", f"""## {title}

- Goal:
- Audience:
- Main points:
- Example:
- Result:
"""),
        ]

    return [
        ("main.py", "python", f"""print("Unit {unit_number:03d}: {title}")
print("Topic 1: {topics[0]}")
print("Topic 2: {topics[1]}")"""),
    ]


def solution_pack(unit_number, unit):
    mode = mode_of(unit)
    title = unit["title"]

    if mode == "html":
        return [
            ("index.html", "html", f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
  </head>
  <body>
    <header>
      <h1>{title}</h1>
      <p>这是一个完整的最小页面示例。</p>
    </header>
    <main>
      <section>
        <h2>Today's focus</h2>
        <p>{unit["prog"][0]}</p>
      </section>
    </main>
  </body>
</html>"""),
        ]

    if mode == "css":
        return [
            ("index.html", "html", f"""<section class="card">
  <h1>{title}</h1>
  <p>这个页面已经有基础结构和样式。</p>
</section>"""),
            ("style.css", "css", """body {
  margin: 0;
  padding: 32px;
  background: linear-gradient(180deg, #f4f6fb, #e9eef8);
  font-family: "Microsoft YaHei", sans-serif;
}

.card {
  max-width: 560px;
  margin: 0 auto;
  padding: 24px;
  background: white;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
}"""),
        ]

    if mode == "javascript":
        return [
            ("package.json", "json", """{
  "name": "study-finished-example",
  "private": true,
  "scripts": {
    "dev": "vite"
  }
}"""),
            ("main.js", "javascript", """const currentTime = new Date().toLocaleTimeString();
console.log(`Task finished at ${currentTime}`);"""),
        ]

    if mode == "react":
        return [
            ("App.tsx", "tsx", f"""import {{ useState }} from "react";
import "./styles.css";

export default function App() {{
  const [done, setDone] = useState(false);

  return (
    <main className="app">
      <h1>{title}</h1>
      <p>Status: {{done ? "done" : "in progress"}}</p>
      <button onClick={{() => setDone(!done)}}>Toggle</button>
    </main>
  );
}}"""),
            ("styles.css", "css", """.app {
  padding: 24px;
  font-family: "Microsoft YaHei", sans-serif;
}"""),
        ]

    if mode == "typescript":
        return [
            ("main.ts", "ts", f"""type StudyTask = {{
  title: string;
  done: boolean;
}};

const currentTask: StudyTask = {{
  title: "{title}",
  done: true,
}};

function formatTask(task: StudyTask): string {{
  return `${{task.title}} - ${{task.done ? "done" : "not done"}}`;
}}

console.log(formatTask(currentTask));"""),
        ]

    if mode == "flask":
        return [
            ("app.py", "python", f"""from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "{title}"

@app.route("/api/status")
def status():
    return jsonify({{"status": "ok", "unit": "{unit_number:03d}"}})

if __name__ == "__main__":
    app.run(debug=True)"""),
        ]

    if mode == "fastapi":
        return [
            ("app.py", "python", f"""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {{"message": "{title}"}}

@app.get("/health")
def health():
    return {{"status": "ok", "unit": "{unit_number:03d}"}}"""),
        ]

    if mode == "sql":
        return [
            ("schema.sql", "sql", """CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT
);

INSERT INTO items (name, description)
VALUES ('Notebook', 'study notes'), ('Task', 'daily work');"""),
            ("query.sql", "sql", """SELECT id, name
FROM items
WHERE name IS NOT NULL
ORDER BY id DESC;"""),
        ]

    if mode == "api":
        return [
            ("main.py", "python", """import requests

response = requests.get("https://api.github.com")
data = response.json()

print("Status:", response.status_code)
print("Current user URL:", data.get("current_user_url"))"""),
        ]

    if mode == "data":
        return [
            ("main.py", "python", """import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Li Hua", "Amy", "David"],
        "score": [95, 88, 91],
    }
)

print(df)
print("Average:", df["score"].mean())"""),
        ]

    if mode == "ops":
        return [
            ("Dockerfile", "dockerfile", """FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]"""),
            ("workflow.yml", "yaml", """name: basic-check

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: pytest"""),
        ]

    if mode == "git":
        return [
            ("commands.md", "markdown", """## Git finished example

```bash
git status
git add .
git commit -m "finish the current unit"
git push
```

## Daily log

- I finished one unit.
- I fixed problems.
- I prepared the next step.
"""),
        ]

    if mode == "algo":
        return [
            ("main.py", "python", """def solve(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print("Answer:", solve([1, 2, 3, 4]))"""),
        ]

    if mode == "engineering":
        return [
            ("notes.md", "markdown", f"""## {title}

- Current problem: keep the code clean and stable
- Current design: break work into smaller parts
- Current risk: make changes without testing
- Next improvement: add checks and better documentation
"""),
        ]

    if mode == "career":
        return [
            ("outline.md", "markdown", f"""## {title}

- Goal: explain the work clearly
- Audience: learners, interviewers, or users
- Main points: problem, solution, result
- Example: use one real project
- Result: a clear and strong presentation
"""),
        ]

    return [
        ("main.py", "python", f"""print("Unit {unit_number:03d}: {title}")
print("Output:", "{unit['output']}")"""),
    ]


def workbook_text(unit_number, unit):
    words = ", ".join(f"`{word}`" for word in words_of(unit))
    lines = [
        f"# 单元 {unit_number:03d} 工作簿：{unit['title']}",
        "",
        f"- 最终产出：{unit['output']}",
        f"- 配套单元讲义：`units/unit_{unit_number:03d}.md`",
        f"- 配套模板：`code_templates/unit_{unit_number:03d}_template.md`",
        f"- 配套答案：`code_solutions/unit_{unit_number:03d}_solution.md`",
        f"- 配套小测：`quizzes/unit_{unit_number:03d}_quiz.md`",
        "",
        "## 本单元先做什么",
        "",
        "1. 先看单元讲义，知道为什么学。",
        "2. 再看模板，照着补一个最小版本。",
        "3. 做下面的练习，不要求一步到位。",
        "4. 最后再对照参考答案和小测。",
        "",
        "## 本单元目标",
        "",
    ]
    for topic in unit["prog"]:
        lines.append(f"- 知道 `{topic}` 在当前单元里负责什么。")
    lines.extend(
        [
            f"- 最后做出：`{unit['output']}`",
            "",
            "## 热身问题",
            "",
            f"1. 你能不能用一句大白话解释 `{unit['prog'][0]}`？",
            f"2. 你知不知道 `{unit['prog'][1]}` 和前面内容的关系？",
            f"3. 你能不能说出最终产出 `{unit['output']}` 的最小版本应该长什么样？",
            "",
            "## 跟着做",
            "",
            f"1. 先把模板里的第一段内容手敲一遍，感受 `{unit['prog'][0]}`。",
            f"2. 再补上第二块内容，感受 `{unit['prog'][1]}`。",
            f"3. 再用你自己的话改一个小地方，把它和 `{unit['prog'][2]}` 接起来。",
            "",
            "## 基础练习",
            "",
            f"1. 做一个最小版本，只要能体现 `{unit['prog'][0]}` 和 `{unit['prog'][1]}` 就行。",
            f"2. 再补上 `{unit['prog'][2]}`，让结果更完整。",
            f"3. 最后补上 `{unit['prog'][3]}`，让它更接近 `{unit['output']}`。",
            "",
            "## 提升练习",
            "",
            "1. 把命名改得更清楚。",
            "2. 补一句英文说明，解释这个单元的产出在做什么。",
            "3. 如果这是网页或接口，就让它多一块可见结果；如果这是算法或数据题，就多做一组输入输出。",
            "",
            "## 英语练习",
            "",
            f"- 本单元词汇：{words}",
            f"- 本单元句子：`{unit['sentence']}`",
            "- 先大声读 3 遍，再用中文讲出大意。",
            "- 任选 3 个词，写 3 个很短的技术句子。",
            "",
            "## 小项目推进建议",
            "",
            f"- 第一步：先完成 `{unit['output']}` 的最小可运行版。",
            f"- 第二步：再让 `{unit['prog'][2]}` 和 `{unit['prog'][3]}` 进入成果里。",
            "- 第三步：最后再整理命名、注释、说明文字。",
            "",
            "## 自查清单",
            "",
            f"- [ ] 我知道 `{unit['prog'][0]}` 是干什么的。",
            f"- [ ] 我知道 `{unit['prog'][1]}` 和前面的关系。",
            f"- [ ] 我动手补过模板，而不是只看。",
            f"- [ ] 我已经开始做 `{unit['output']}`。",
            "",
            "## GitHub 提交建议",
            "",
            "```bash",
            "git add .",
            f'git commit -m "Finish unit {unit_number:03d} support pack practice"',
            "git push",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def pack_markdown(title, intro, blocks, unit_number):
    lines = [f"# {title}", "", intro, ""]
    for filename, lang, code in blocks:
        lines.extend(
            [
                f"## 文件：`{filename}`",
                "",
                f"```{lang}",
                code,
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "## 使用说明",
            "",
            "1. 先手敲一遍，不要直接复制。",
            "2. 跑起来或读一遍输出，再改一个小地方。",
            "3. 卡住时回到单元讲义和工作簿。",
            "",
            "## 建议提交",
            "",
            "```bash",
            "git add .",
            f'git commit -m "Work on unit {unit_number:03d} starter pack"',
            "git push",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def quiz_text(unit_number, unit):
    words = words_of(unit)
    lines = [
        f"# 单元 {unit_number:03d} 小测：{unit['title']}",
        "",
        "## 选择或简答题",
        "",
        f"1. 请用一句自己的话解释：`{unit['prog'][0]}` 是干什么的？",
        f"2. `{unit['prog'][1]}` 为什么不是孤立存在的？它要和什么配合？",
        f"3. 如果你要做出 `{unit['output']}` 的最小版本，你会先保留哪两块能力？",
        f"4. 请把这句英文翻成中文：`{unit['sentence']}`",
        f"5. 请从这些词里任选 3 个做短句：{', '.join(words[:4])}",
        "",
        "## 参考答案方向",
        "",
        f"- 第 1 题：重点不是背标准定义，而是说出 `{unit['prog'][0]}` 在当前单元里的作用。",
        f"- 第 2 题：要能说出 `{unit['prog'][1]}` 需要和前面的内容一起工作。",
        f"- 第 3 题：通常先保留 `{unit['prog'][0]}` 和 `{unit['prog'][1]}`，再慢慢补完整。",
        f"- 第 4 题：大意说对就行，不要求字字死记。",
        "- 第 5 题：句子很短也可以，只要能体现词义。",
        "",
        "## 通过标准",
        "",
        "- 你能不用看资料说出至少 3 题。",
        "- 你能把英文句子的大意说清楚。",
        "- 你知道自己哪里还不稳，准备回去补哪一段。",
    ]
    return "\n".join(lines) + "\n"


def readme_text(title, suffix, start, end):
    lines = [f"# {title}", "", "## 文件列表", ""]
    for unit_number in range(start, end + 1):
        unit = UNITS[unit_number - 1]
        lines.append(f"- `unit_{unit_number:03d}_{suffix}.md` - {unit['title']}")
    return "\n".join(lines) + "\n"


def ensure_stage_readme(stage_root):
    readme = stage_root / "README.md"
    marker = "## 练习支持包入口"
    text = readme.read_text(encoding="utf-8") if readme.exists() else ""
    if marker not in text:
        text = text.rstrip() + "\n\n" + "\n".join(
            [
                marker,
                "",
                "这一阶段现在也补上了练习支持包。",
                "- `workbooks/`：工作簿",
                "- `code_templates/`：起步模板",
                "- `code_solutions/`：参考答案",
                "- `quizzes/`：单元小测",
                "",
            ]
        )
        readme.write_text(text.rstrip() + "\n", encoding="utf-8")


def main():
    repo_root = Path(__file__).resolve().parents[1]

    for stage_dir, stage_label, start, end in STAGES:
        stage_root = repo_root / stage_dir
        workbook_dir = stage_root / "workbooks"
        template_dir = stage_root / "code_templates"
        solution_dir = stage_root / "code_solutions"
        quiz_dir = stage_root / "quizzes"

        for current_dir in [workbook_dir, template_dir, solution_dir, quiz_dir]:
            current_dir.mkdir(parents=True, exist_ok=True)

        (workbook_dir / "README.md").write_text(readme_text(f"{stage_label} 工作簿目录", "workbook", start, end), encoding="utf-8")
        (template_dir / "README.md").write_text(readme_text(f"{stage_label} 起步模板目录", "template", start, end), encoding="utf-8")
        (solution_dir / "README.md").write_text(readme_text(f"{stage_label} 参考答案目录", "solution", start, end), encoding="utf-8")
        (quiz_dir / "README.md").write_text(readme_text(f"{stage_label} 小测目录", "quiz", start, end), encoding="utf-8")

        for unit_number in range(start, end + 1):
            unit = UNITS[unit_number - 1]
            (workbook_dir / f"unit_{unit_number:03d}_workbook.md").write_text(workbook_text(unit_number, unit), encoding="utf-8")
            (template_dir / f"unit_{unit_number:03d}_template.md").write_text(
                pack_markdown(
                    f"单元 {unit_number:03d} 起步模板：{unit['title']}",
                    "这一份不是最终答案，而是一个可以继续补、继续改的起步包。",
                    starter_pack(unit_number, unit),
                    unit_number,
                ),
                encoding="utf-8",
            )
            (solution_dir / f"unit_{unit_number:03d}_solution.md").write_text(
                pack_markdown(
                    f"单元 {unit_number:03d} 参考答案：{unit['title']}",
                    "这一份用来对照思路和结构。建议先自己做，再回来比对。",
                    solution_pack(unit_number, unit),
                    unit_number,
                ),
                encoding="utf-8",
            )
            (quiz_dir / f"unit_{unit_number:03d}_quiz.md").write_text(quiz_text(unit_number, unit), encoding="utf-8")

        ensure_stage_readme(stage_root)


if __name__ == "__main__":
    main()
