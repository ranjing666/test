from pathlib import Path

from generate_1000_day_plan import PHASES, UNITS


STAGES = [
    ("stage1_foundation", "第 1 阶段：入门基础", 1, 10),
    ("stage2_growth", "第 2 阶段：成长进阶", 11, 30),
    ("stage3_advanced", "第 3 阶段：高级进阶", 31, 60),
    ("stage4_expert", "第 4 阶段：专家深化", 61, 85),
    ("stage5_master", "第 5 阶段：大师输出", 86, 100),
]


EXAMPLE_OVERRIDES = {
    33: [
        ("python", "from flask import Flask, request, redirect, url_for\n\napp = Flask(__name__)\nTASKS = []\n\n@app.post('/tasks')\ndef create_task():\n    TASKS.append(request.form['title'])\n    return redirect(url_for('list_tasks'))"),
        ("python", "@app.get('/tasks')\ndef list_tasks():\n    return {'items': TASKS}\n\n@app.post('/tasks/<int:index>/delete')\ndef delete_task(index):\n    TASKS.pop(index)\n    return {'ok': True}"),
    ],
    34: [
        ("python", "from werkzeug.security import generate_password_hash, check_password_hash\n\npassword_hash = generate_password_hash('study123')\nprint(check_password_hash(password_hash, 'study123'))"),
        ("python", "from flask import session\n\nsession['user_id'] = 1\nif 'user_id' in session:\n    print('logged in')"),
    ],
    37: [
        ("python", "def add(a, b):\n    return a + b\n\ndef test_add():\n    assert add(2, 3) == 5"),
        ("python", "import pytest\n\n@pytest.mark.parametrize('text, expected', [('hello', 5), ('', 0)])\ndef test_length(text, expected):\n    assert len(text) == expected"),
    ],
    38: [
        ("python", "import os\n\napp_env = os.getenv('APP_ENV', 'development')\ndatabase_url = os.getenv('DATABASE_URL', 'sqlite:///local.db')\nprint(app_env)\nprint(database_url)"),
        ("yaml", "services:\n  web:\n    build: .\n    environment:\n      APP_ENV: production\n      DATABASE_URL: ${DATABASE_URL}"),
    ],
    39: [
        ("markdown", "## README\n\n- What this project does\n- How to run it\n- Example input and output\n- Common problems"),
        ("markdown", "## Issue template\n\n- Problem\n- Expected result\n- Actual result\n- Steps to reproduce"),
    ],
    20: [
        ("markdown", "## Learning Task\n\n- Title: Review Python lists\n- Priority: High\n- Status: Todo\n- Notes: Rewrite 3 examples by hand"),
        ("markdown", "## Feature list\n\n- Add task\n- Mark task done\n- Delete task\n- Save tasks to JSON"),
    ],
    40: [
        ("markdown", "## Blog page plan\n\n- Home page\n- Register page\n- Login page\n- New post page"),
        ("markdown", "## Post model\n\n- title\n- content\n- author_id\n- created_at"),
    ],
    50: [
        ("markdown", "## Wrong answer review\n\n- Topic:\n- Mistake:\n- Fix:\n- Takeaway:"),
        ("markdown", "## English explanation\n\n- Problem:\n- Idea:\n- Why it works:"),
    ],
    57: [
        ("python", "from pathlib import Path\n\nfor path in Path('downloads').glob('*.txt'):\n    print(path.name)"),
        ("python", "from pathlib import Path\n\nsource = Path('report draft.txt')\nsource.rename('report_draft.txt')"),
    ],
    61: [
        ("json", "{\n  \"name\": \"frontend-demo\",\n  \"scripts\": {\n    \"dev\": \"vite\",\n    \"build\": \"vite build\"\n  }\n}"),
        ("bash", "npm install\nnpm run dev\nnpm run build"),
    ],
    70: [
        ("html", "<section class=\"app\">\n  <header>\n    <h1>Focus Board</h1>\n    <button>Add Card</button>\n  </header>\n  <main id=\"cards\"></main>\n</section>"),
        ("javascript", "const cards = [{ title: 'Math' }, { title: 'English' }];\nconst root = document.querySelector('#cards');\nroot.innerHTML = cards.map(card => `<article>${card.title}</article>`).join('');"),
    ],
    75: [
        ("python", "import asyncio\n\nasync def send_email():\n    await asyncio.sleep(1)\n    return 'sent'"),
        ("python", "def should_retry(attempt, status_code):\n    return attempt < 3 and status_code >= 500"),
    ],
    79: [
        ("markdown", "## Deploy checklist\n\n- Set `APP_ENV=production`\n- Add database URL\n- Add secret key\n- Confirm `/health` works"),
        ("yaml", "services:\n  web:\n    image: study-app:latest\n    env:\n      APP_ENV: production\n      DATABASE_URL: ${DATABASE_URL}"),
    ],
    80: [
        ("python", "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/api/tasks')\ndef list_tasks():\n    return {'items': [{'id': 1, 'title': 'Read docs'}]}"),
        ("javascript", "async function loadTasks() {\n  const response = await fetch('http://localhost:8000/api/tasks');\n  const data = await response.json();\n  console.log(data.items);\n}"),
    ],
    81: [
        ("python", "def calculate_total(prices):\n    total = 0\n    for price in prices:\n        total += price\n    return total"),
        ("python", "def format_student_report(name, score):\n    status = 'pass' if score >= 60 else 'fail'\n    return f'{name}: {score} ({status})'"),
    ],
    83: [
        ("python", "import pytest\n\n@pytest.fixture\ndef sample_user():\n    return {'name': 'Li Hua', 'role': 'student'}"),
        ("python", "def test_profile_name(sample_user):\n    assert sample_user['name'] == 'Li Hua'"),
    ],
    84: [
        ("python", "from time import perf_counter\n\nstart = perf_counter()\n_ = sum(i * i for i in range(5000))\nend = perf_counter()\nprint(end - start)"),
        ("python", "from functools import lru_cache\n\n@lru_cache\ndef slow_square(number):\n    return number * number"),
    ],
    85: [
        ("python", "def retryable_send(attempt, status_code):\n    if attempt >= 3:\n        return 'stop'\n    if status_code >= 500:\n        return 'retry'\n    return 'success'"),
        ("json", "{\n  \"job\": \"send_report\",\n  \"retry\": 2,\n  \"payload\": {\"user_id\": 1}\n}"),
    ],
    86: [
        ("markdown", "## System sketch\n\n- Users send requests through an API gateway\n- App service handles business logic\n- Database stores core records\n- Cache speeds up hot queries"),
        ("markdown", "## Capacity note\n\n- Daily users: 1000\n- Peak requests per second: 30\n- Main bottleneck: database reads"),
    ],
    87: [
        ("json", "{\n  \"level\": \"info\",\n  \"event\": \"login_success\",\n  \"user_id\": 1,\n  \"request_id\": \"req-123\"\n}"),
        ("python", "def should_alert(error_rate, latency_ms):\n    return error_rate > 0.05 or latency_ms > 800"),
    ],
    88: [
        ("python", "def validate_username(username):\n    return username.isalnum() and 3 <= len(username) <= 20"),
        ("python", "def can_access(user_role, resource_owner):\n    return user_role == 'admin' or resource_owner"),
    ],
    89: [
        ("markdown", "## Contribution flow\n\n1. Read the issue\n2. Fork the repository\n3. Create a branch\n4. Open a pull request"),
        ("bash", "git checkout -b fix/readme-link\ngit add README.md\ngit commit -m \"Fix broken README link\"\ngit push origin fix/readme-link"),
    ],
    90: [
        ("markdown", "## Specialization choice\n\n- Direction:\n- User:\n- Core problem:\n- Reason:"),
        ("markdown", "## Milestone plan\n\n- Week 1: define scope\n- Week 2: build core flow\n- Week 3: test and improve\n- Week 4: demo and publish"),
    ],
    91: [
        ("markdown", "## Portfolio case card\n\n- Project:\n- Problem:\n- Solution:\n- Result:"),
        ("markdown", "## About section\n\n- I started from zero.\n- Now I can build small web apps.\n- I focus on clear structure and steady progress."),
    ],
    92: [
        ("markdown", "## README structure\n\n- What this project does\n- How to run it\n- Example input and output\n- Common problems"),
        ("markdown", "## API usage note\n\n- Endpoint: `/api/tasks`\n- Method: `GET`\n- Response: `{\"items\": []}`\n- Error case: `401 unauthorized`"),
    ],
    93: [
        ("markdown", "## Demo opening\n\n- Hello, I built a study tracker for beginners.\n- It helps users record coding and English practice.\n- I will show the main flow first."),
        ("markdown", "## Slide outline\n\n- Problem\n- Solution\n- Demo\n- Lessons learned"),
    ],
    94: [
        ("markdown", "## Resume bullets\n\n- Built a study tracker with Python and GitHub.\n- Shipped a small blog system and wrote clear docs.\n- Improved features after manual testing and feedback."),
        ("markdown", "## GitHub profile note\n\n- Pinned projects: Study Tracker, Blog System, Data Report\n- Short bio: learner who turns notes into working projects\n- Focus: Python, web, steady improvement"),
    ],
    95: [
        ("markdown", "## Interview answer\n\n- Question:\n- Answer:\n- Result:"),
        ("markdown", "## Follow-up question\n\n- Challenge:\n- Fix:\n- Lesson:"),
    ],
    96: [
        ("markdown", "## Capstone problem\n\n- User:\n- Problem:\n- Product idea:"),
        ("markdown", "## Capstone milestones\n\n- Week 1: define scope\n- Week 2: build first version\n- Week 3: test and improve\n- Week 4: publish and demo"),
    ],
    97: [
        ("markdown", "## Sprint 1 checklist\n\n- Build project skeleton\n- Define key data model\n- Finish one main API or page\n- Run the first end-to-end flow"),
        ("markdown", "## First version notes\n\n- Main user flow works\n- Known bugs are listed\n- Next sprint target is clear"),
    ],
    98: [
        ("markdown", "## Sprint 2 checklist\n\n- Improve main user flow\n- Fix top 3 bugs\n- Add one missing feature\n- Rewrite unclear labels"),
        ("markdown", "## Testing notes\n\n- What failed:\n- Why it failed:\n- How I fixed it:\n- What I should retest:"),
    ],
    99: [
        ("markdown", "## Release checklist\n\n- App runs in production\n- README is updated\n- Demo link works\n- Known bugs are listed"),
        ("markdown", "## Demo video outline\n\n- 10s intro\n- 30s flow\n- 20s technical choice\n- 10s close"),
    ],
    100: [
        ("markdown", "## My Learning Summary\n\n- Start point: complete beginner\n- Biggest progress: I can build and explain small projects\n- Next goal: ship one stronger specialization project"),
        ("markdown", "## Teach One Concept\n\n- Concept: API\n- Plain explanation: an API is a rule for how two programs talk\n- Small example: the frontend asks for JSON, the backend sends JSON back"),
    ],
}


def stage_for_unit(unit_number):
    for stage_dir, stage_label, start, end in STAGES:
        if start <= unit_number <= end:
            return stage_dir, stage_label
    raise ValueError(unit_number)


def phase_for_unit(unit_number):
    return PHASES[(unit_number - 1) // 10]


def words_of(unit):
    return [word.strip() for word in unit["words"].split(",") if word.strip()]


def mode_of(unit):
    text = " ".join([unit["title"], *unit["prog"]])
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
    if any(word in text for word in ["作品集", "写作", "演示", "简历", "面试", "毕业", "复盘"]):
        return "career"
    return "python"


def explain(topic, output):
    return (
        f"`{topic}` 你现在先把它理解成当前单元必须会用的一小块能力。"
        f"它不是孤立存在的，最后会服务于“{output}”这个成果。"
        "你不用先把定义背下来，而是通过例子、跟练、组合和复盘慢慢吃透。"
    )


def examples(unit_number, unit):
    if unit_number in EXAMPLE_OVERRIDES:
        return EXAMPLE_OVERRIDES[unit_number]

    mode = mode_of(unit)
    title = unit["title"]
    if mode == "html":
        return [
            ("html", f"<!doctype html>\n<html lang=\"zh-CN\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <title>{title}</title>\n  </head>\n  <body>\n    <h1>{title}</h1>\n    <p>先练最小页面结构。</p>\n  </body>\n</html>"),
            ("html", "<form>\n  <label>Name</label>\n  <input />\n  <button>Submit</button>\n</form>"),
        ]
    if mode == "css":
        return [
            ("css", "body {\n  margin: 0;\n  padding: 24px;\n  background: #f5f7fb;\n}\n\n.card {\n  padding: 24px;\n  border-radius: 16px;\n  background: white;\n}"),
            ("html", "<section class=\"card\">\n  <h1>Hello CSS</h1>\n  <p>先把布局摆清楚。</p>\n</section>"),
        ]
    if mode == "javascript":
        return [
            ("javascript", "const button = document.querySelector('#btn');\nconst output = document.querySelector('#output');\n\nbutton.addEventListener('click', () => {\n  output.textContent = 'Clicked';\n});"),
            ("html", "<button id=\"btn\">Click</button>\n<p id=\"output\">Waiting...</p>"),
        ]
    if mode == "react":
        return [
            ("tsx", "import { useState } from 'react';\n\nexport default function Counter() {\n  const [count, setCount] = useState(0);\n  return (\n    <section>\n      <p>Count: {count}</p>\n      <button onClick={() => setCount(count + 1)}>Add</button>\n    </section>\n  );\n}"),
            ("tsx", "type TaskProps = { title: string };\n\nexport function TaskItem({ title }: TaskProps) {\n  return <li>{title}</li>;\n}"),
        ]
    if mode == "typescript":
        return [
            ("ts", "type Student = {\n  name: string;\n  score: number;\n};\n\nfunction showStudent(student: Student): string {\n  return `${student.name}: ${student.score}`;\n}"),
            ("ts", "const numbers: number[] = [1, 2, 3];\nconst total = numbers.reduce((sum, item) => sum + item, 0);\nconsole.log(total);"),
        ]
    if mode == "flask":
        return [
            ("python", "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello, Flask!'\n\nif __name__ == '__main__':\n    app.run(debug=True)"),
            ("python", "from flask import jsonify\n\n@app.route('/api/status')\ndef status():\n    return jsonify({'status': 'ok'})"),
        ]
    if mode == "fastapi":
        return [
            ("python", "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass Item(BaseModel):\n    name: str\n    price: float\n\n@app.post('/items')\ndef create_item(item: Item):\n    return item"),
            ("python", "from fastapi import HTTPException\n\ndef get_token(token: str = ''):\n    if not token:\n        raise HTTPException(status_code=401, detail='missing token')"),
        ]
    if mode == "sql":
        return [
            ("sql", "CREATE TABLE students (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  score INTEGER NOT NULL\n);"),
            ("sql", "SELECT name, score\nFROM students\nWHERE score >= 90\nORDER BY score DESC;"),
        ]
    if mode == "api":
        return [
            ("python", "import requests\n\nresponse = requests.get('https://api.github.com')\nprint(response.status_code)\nprint(response.json())"),
            ("json", "{\n  \"status\": \"ok\",\n  \"items\": [\n    {\"id\": 1, \"name\": \"demo\"}\n  ]\n}"),
        ]
    if mode == "data":
        return [
            ("python", "import pandas as pd\n\ndf = pd.DataFrame({'name': ['Li Hua', 'Amy'], 'score': [95, 88]})\nprint(df)\nprint(df['score'].mean())"),
            ("python", "import matplotlib.pyplot as plt\n\nplt.bar(['A', 'B', 'C'], [10, 15, 8])\nplt.title('Simple chart')\nplt.show()"),
        ]
    if mode == "ops":
        return [
            ("dockerfile", "FROM python:3.12-slim\nWORKDIR /app\nCOPY . .\nCMD [\"python\", \"app.py\"]"),
            ("yaml", "name: test\n\non: [push]\n\njobs:\n  check:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4"),
        ]
    if mode == "git":
        return [
            ("bash", "git status\ngit add .\ngit commit -m \"Finish current lesson\"\ngit push"),
            ("markdown", "## Project log\n\n- Today I finished a small feature.\n- I fixed two bugs.\n- Next I will improve the README."),
        ]
    if mode == "algo":
        return [
            ("python", "def find_max(numbers):\n    current_max = numbers[0]\n    for number in numbers[1:]:\n        if number > current_max:\n            current_max = number\n    return current_max"),
            ("python", "def is_valid(items):\n    stack = []\n    pairs = {')': '(', ']': '[', '}': '{'}\n    for item in items:\n        if item in '([{':\n            stack.append(item)\n        elif not stack or stack.pop() != pairs[item]:\n            return False\n    return not stack"),
        ]
    if mode == "career":
        return [
            ("markdown", "## Project summary\n\n- Problem\n- Solution\n- Stack\n- Result"),
            ("markdown", "## Resume bullets\n\n- Built a small full-stack app.\n- Added tests and clear documentation.\n- Improved the product after feedback."),
        ]
    return [
        ("python", f"print('Unit {unit_number:03d}: {unit['title']}')"),
        ("python", "name = input('What is your name? ')\nprint('Keep going,', name)"),
    ]


def day_text(local_day, unit, next_title):
    topics = unit["prog"]
    if local_day == 1:
        focus = topics[0]
        explain_text = f"今天是开场日，只抓 `{topics[0]}`。目标不是学很多，而是第一次把主题、词汇、例子和最终产出串起来。"
        tasks = ["手敲最小例子 1 遍。", "用中文解释例子每一部分在做什么。", "记下今天最陌生的 3 个词。"]
        output = "写出第一份理解笔记。"
    elif local_day == 2:
        focus = topics[0]
        explain_text = f"今天继续练 `{topics[0]}`，但从“看懂”升级到“会改”。只有你自己改过，知识点才算开始真正进入手里。"
        tasks = ["把昨天例子改 3 个地方。", "每改一次都运行或检查结果。", "保留一个最清楚的练习版本。"]
        output = "得到自己的第一个小版本。"
    elif local_day == 3:
        focus = topics[1]
        explain_text = f"今天切到第二个主题 `{topics[1]}`。重点不是孤立背新概念，而是看它怎么接到前两天学过的东西上。"
        tasks = [f"找出例子里哪里体现了 `{topics[1]}`。", "用一句大白话解释它的作用。", "把它补进昨天的练习里。"]
        output = f"形成 `{topics[0]} + {topics[1]}` 的组合练习。"
    elif local_day == 4:
        focus = f"{topics[0]} + {topics[1]}"
        explain_text = "今天不加新概念，只做组合练习。零基础最容易出现的问题就是单独看都懂，一组合就乱，今天就是专门解决这个问题。"
        tasks = ["做 2 到 3 个很小的组合练习。", "每练完一题都说清输入、处理、输出。", "记录最容易混乱的点。"]
        output = "整理一页错点或疑问清单。"
    elif local_day == 5:
        focus = topics[2]
        explain_text = f"今天开始第三个主题 `{topics[2]}`。从今天开始，你会更明显地感觉程序或项目变得更像真正的工具。"
        tasks = [f"先解释 `{topics[2]}` 是干什么的。", "跑通一个最小例子。", "再自己仿写一次。"]
        output = f"写一段关于 `{topics[2]}` 的中文总结。"
    elif local_day == 6:
        focus = f"{topics[0]} + {topics[1]} + {topics[2]}"
        explain_text = "今天是第三个主题的组合练习日。你要开始把前三块知识拼起来，练习从“知道”走向“能独立写一点”。"
        tasks = ["先预测结果，再运行验证。", "改 2 个输入或参数，看结果是否符合预期。", "把一个例子拆成更小步骤后重写。"]
        output = f"得到 `{unit['output']}` 的半成品。"
    elif local_day == 7:
        focus = topics[3]
        explain_text = f"今天学习第四个主题 `{topics[3]}`。它通常是这个单元最后一块关键拼图，作用是把前面的内容真正收束成成果。"
        tasks = [f"写一个只聚焦 `{topics[3]}` 的最小例子。", "把它补进当前项目或练习中。", "写下没有它会少什么。"]
        output = "列出小项目最后的待办清单。"
    elif local_day == 8:
        focus = "小项目整合"
        explain_text = "今天进入整合日。你要把前面四个主题都串起来，先做出最简单但完整可运行的版本，不追求花哨。"
        tasks = [f"围绕 `{unit['output']}` 做最小完整版本。", "先保留主流程，再补细节。", "自己从头到尾演示一次。"]
        output = f"得到 `{unit['output']}` 的第一个完整版本。"
    elif local_day == 9:
        focus = "调试与整理"
        explain_text = "今天是修整日。你要开始像真正做项目那样，主动找 Bug、改命名、补注释、删混乱。"
        tasks = ["找出 3 个可以改进的点。", "补一段简单说明：做什么、怎么运行、输入什么。", "回放一次报错和修复过程。"]
        output = "得到一个更稳定、更像作品的版本。"
    else:
        focus = "复习与衔接"
        explain_text = f"今天是收束日。你要把这 10 天真正串起来，确认自己已经会了什么，然后为下一单元 `{next_title}` 做好过渡。"
        tasks = ["重跑最重要的 1 到 2 个例子。", "写本单元复盘：会了什么、不会什么、最常错什么。", "提交到 GitHub。"]
        output = f"提交 `{unit['output']}` 最终版和本单元总结。"
    return focus, explain_text, tasks, output


def unit_markdown(unit_number):
    unit = UNITS[unit_number - 1]
    next_unit = UNITS[unit_number] if unit_number < len(UNITS) else None
    next_title = next_unit["title"] if next_unit else "下一阶段新主题"
    _, stage_label = stage_for_unit(unit_number)
    lines = [
        f"# 单元 {unit_number:03d}：{unit['title']}",
        "",
        "- 单元结构：10 个学习步骤",
        f"- 所属阶段：{stage_label}",
        f"- 所属 100 天主题：{phase_for_unit(unit_number)}",
        f"- 本单元产出：{unit['output']}",
        "",
        "## 为什么要学这个单元",
        "",
        f"这个单元的目标，不是让你背很多定义，而是把 `{unit['title']}` 变成真正能动手的能力。"
        f"这 10 个学习步骤会始终围绕 `{unit['output']}` 这条线推进，让你知道每一步为什么存在、最后要落到哪里。",
        "",
        "## 核心概念拆解",
        "",
    ]
    for idx, topic in enumerate(unit["prog"], start=1):
        lines.extend([f"### 核心点 {idx}：{topic}", "", explain(topic, unit["output"]), ""])
    words = words_of(unit)
    lines.extend(
        [
            "## 本单元英语",
            "",
            f"核心句型：`{unit['sentence']}`",
            "",
            "本单元高频词：",
        ]
    )
    for word in words:
        lines.append(f"- `{word}`：先做到看见不陌生，能和本单元主题联想起来。")
    lines.extend(["", "## 最小例子", ""])
    for idx, (lang, code) in enumerate(examples(unit_number, unit), start=1):
        lines.extend([f"### 例子 {idx}", "", f"```{lang}", code, "```", "", "先抄一遍，再改一遍，再解释一遍。", ""])
    lines.extend(["## 10 个学习步骤", ""])
    for local_day in range(1, 11):
        focus, explain_text, tasks, output = day_text(local_day, unit, next_title)
        lines.extend(
            [
                f"### 步骤 {local_day}",
                "",
                f"- 当前焦点：`{focus}`",
                f"- 当前连贯性：这一步继续推动“{unit['output']}”这条主线。",
                "",
                "步骤讲解：",
                explain_text,
                "",
                "这一步要做：",
                f"1. {tasks[0]}",
                f"2. {tasks[1]}",
                f"3. {tasks[2]}",
                "",
                "本步英语：",
                f"- 读 3 遍：`{unit['sentence']}`",
                f"- 今天重点看：`{', '.join(words[:3]) if local_day <= 5 else ', '.join(words[3:])}`",
                "- 不会翻也没关系，先做到大概能猜出意思。",
                "",
                "本步产出：",
                f"- {output}",
                "",
                "完成标准：",
                "- 我在这一步亲手改过至少一次内容。",
                "- 我在这一步看过结果，知道程序或页面有没有动起来。",
                "- 我在这一步能用中文说出当前知识点是干什么的。",
                "",
            ]
        )
    lines.extend(
        [
            "## 本单元项目推进法",
            "",
            f"1. 先用 `{unit['prog'][0]}` 和 `{unit['prog'][1]}` 做最小版本。",
            f"2. 再补 `{unit['prog'][2]}`，让结果更完整。",
            f"3. 最后补 `{unit['prog'][3]}`，把它收束成一个可展示的成果。",
            "4. 第 9 步修整，第 10 步复盘并提交。",
            "",
            "## 本单元常见卡点",
            "",
            "- 一次想做太多，结果越写越乱。",
            "- 只看不敲，觉得自己懂了，真正一动手又卡住。",
            "- 只想把功能做完，不愿意解释每一部分在干什么。",
            "- 碰到报错不先看最后一行提示。",
            "",
            "## 单元复盘问题",
            "",
            f"1. 你能不能不用看资料，解释 `{unit['prog'][0]}` 是干什么的？",
            f"2. 你能不能指出 `{unit['prog'][1]}` 在例子或项目里出现在哪里？",
            f"3. 你能不能说明 `{unit['prog'][2]}` 为什么让结果更完整？",
            f"4. 你能不能说清 `{unit['prog'][3]}` 在成果里承担了什么角色？",
            f"5. 你做出来的 `{unit['output']}`，下一步最想改哪里？",
            "",
            "## GitHub 提交建议",
            "",
            "```bash",
            "git add .",
            f"git commit -m \"Finish unit {unit_number:03d}\"",
            "git push",
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def units_readme(stage_label, start, end):
    lines = [
        f"# {stage_label} 单元目录",
        "",
        "这个目录里的每个单元都包含 10 个学习步骤。",
        "每个单元文件里已经包含：讲解、最小例子、逐日任务、英语、产出、复盘。",
        "",
        "## 单元列表",
        "",
    ]
    for unit_number in range(start, end + 1):
        unit = UNITS[unit_number - 1]
        lines.append(f"- [单元 {unit_number:03d}：{unit['title']}](unit_{unit_number:03d}.md) - 10 个学习步骤")
    return "\n".join(lines) + "\n"


def append_stage_entry(repo_root):
    marker = "## 新增详细教材入口"
    for stage_dir, stage_label, start, end in STAGES:
        readme = repo_root / stage_dir / "README.md"
        text = readme.read_text(encoding="utf-8") if readme.exists() else ""
        if marker not in text:
            text = text.rstrip() + "\n\n" + "\n".join(
                [
                    marker,
                    "",
                    "这一阶段现在已经补上了按单元展开的详细讲义。",
                    f"本阶段对应单元范围：`unit_{start:03d}` 到 `unit_{end:03d}`。",
                    "详细目录在：`02_units/README.md`",
                    "",
                ]
            )
            readme.write_text(text.rstrip() + "\n", encoding="utf-8")


def main():
    repo_root = Path(__file__).resolve().parents[1]
    for stage_dir, stage_label, start, end in STAGES:
        units_dir = repo_root / stage_dir / "02_units"
        units_dir.mkdir(parents=True, exist_ok=True)
        (units_dir / "README.md").write_text(units_readme(stage_label, start, end), encoding="utf-8")
        for unit_number in range(start, end + 1):
            (units_dir / f"unit_{unit_number:03d}.md").write_text(unit_markdown(unit_number), encoding="utf-8")
    append_stage_entry(repo_root)


if __name__ == "__main__":
    main()



