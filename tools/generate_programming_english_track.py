from pathlib import Path

from generate_1000_day_plan import UNITS


ROOT = Path(__file__).resolve().parents[1]
TRACK_DIR = ROOT / "编程英语同步学习"
ROUTE_FILE = TRACK_DIR / "100天编程英语路线.md"
VOCAB_FILE = TRACK_DIR / "高频编程英语词块.md"
TEMPLATE_FILE = TRACK_DIR / "每日英语练习模板.md"
OUTPUT_FILE = TRACK_DIR / "英语输出句型模板.md"
README_FILE = TRACK_DIR / "README.md"


STAGES = [
    ("阶段1_基础操作英语.md", "第 1 阶段：基础操作英语", 1, 10, "先把最基础的文件、运行、输入、输出看懂，会读、会抄、会说最短句。"),
    ("阶段2_项目起步英语.md", "第 2 阶段：项目起步英语", 11, 30, "开始会描述列表、文件、Git、网页和表单，能用短句解释自己写的程序。"),
    ("阶段3_后端算法英语.md", "第 3 阶段：后端算法英语", 31, 60, "能读懂 API、数据库、测试、部署、数据分析这些常见英文表达。"),
    ("阶段4_工程化英语.md", "第 4 阶段：工程化英语", 61, 85, "开始掌握 React、FastAPI、部署、测试、性能这些工程化英语。"),
    ("阶段5_表达求职英语.md", "第 5 阶段：表达与求职英语", 86, 100, "重点转向文档、演示、作品集、面试和长期表达能力。"),
]


CORE_VOCAB_GROUPS = [
    (
        "基础动作",
        [
            ("open", "打开"),
            ("save", "保存"),
            ("run", "运行"),
            ("read", "读取"),
            ("write", "写入"),
            ("check", "检查"),
            ("fix", "修复"),
            ("build", "构建"),
            ("finish", "完成"),
            ("repeat", "重复"),
            ("choose", "选择"),
            ("explain", "解释"),
        ],
    ),
    (
        "文件与代码",
        [
            ("file", "文件"),
            ("folder", "文件夹"),
            ("path", "路径"),
            ("line", "行"),
            ("code", "代码"),
            ("comment", "注释"),
            ("module", "模块"),
            ("library", "库"),
            ("function", "函数"),
            ("parameter", "参数"),
            ("return", "返回"),
            ("variable", "变量"),
        ],
    ),
    (
        "数据与逻辑",
        [
            ("list", "列表"),
            ("item", "项目"),
            ("key", "键"),
            ("value", "值"),
            ("data", "数据"),
            ("count", "计数"),
            ("sort", "排序"),
            ("result", "结果"),
            ("error", "错误"),
            ("debug", "调试"),
            ("test", "测试"),
            ("expected", "预期的"),
        ],
    ),
    (
        "网页前端",
        [
            ("page", "页面"),
            ("form", "表单"),
            ("input", "输入框/输入"),
            ("button", "按钮"),
            ("click", "点击"),
            ("browser", "浏览器"),
            ("style", "样式"),
            ("layout", "布局"),
            ("component", "组件"),
            ("state", "状态"),
            ("route", "路由"),
            ("render", "渲染"),
        ],
    ),
    (
        "后端接口",
        [
            ("server", "服务器"),
            ("request", "请求"),
            ("response", "响应"),
            ("api", "接口"),
            ("json", "JSON 数据"),
            ("endpoint", "接口地址"),
            ("database", "数据库"),
            ("query", "查询"),
            ("model", "模型"),
            ("token", "令牌"),
            ("auth", "鉴权"),
            ("session", "会话"),
        ],
    ),
    (
        "数据分析与自动化",
        [
            ("csv", "CSV 文件"),
            ("column", "列"),
            ("row", "行"),
            ("clean", "清洗"),
            ("group", "分组"),
            ("chart", "图表"),
            ("analysis", "分析"),
            ("report", "报告"),
            ("extract", "提取"),
            ("transform", "转换"),
            ("pipeline", "管道"),
            ("automation", "自动化"),
        ],
    ),
    (
        "工程化与部署",
        [
            ("deploy", "部署"),
            ("config", "配置"),
            ("env", "环境变量"),
            ("log", "日志"),
            ("monitor", "监控"),
            ("cloud", "云"),
            ("docker", "Docker"),
            ("container", "容器"),
            ("workflow", "工作流"),
            ("coverage", "覆盖率"),
            ("performance", "性能"),
            ("retry", "重试"),
        ],
    ),
    (
        "表达与求职",
        [
            ("document", "文档"),
            ("tutorial", "教程"),
            ("present", "展示/演示"),
            ("demo", "演示"),
            ("slide", "幻灯片"),
            ("portfolio", "作品集"),
            ("resume", "简历"),
            ("interview", "面试"),
            ("review", "复盘/评审"),
            ("highlight", "亮点"),
            ("audience", "受众"),
            ("future", "未来"),
        ],
    ),
]


def words_of(unit: dict[str, str]) -> list[str]:
    return [word.strip() for word in unit["words"].split(",") if word.strip()]


def route_task(unit: dict[str, str]) -> list[str]:
    words = words_of(unit)
    return [
        f"朗读句子 `{unit['sentence']}` 3 遍，先保证嘴巴能顺下来。",
        f"手写 6 个词：`{', '.join(words)}`，每个词旁边写一个中文提示。",
        f"从这 6 个词里任选 3 个，造 3 个最短英文短句。",
        f"用中文解释这句话和这 6 个词跟 `{unit['title']}` 有什么关系。",
    ]


def build_readme() -> str:
    lines = [
        "# 编程英语同步学习",
        "",
        "这个目录是一条独立的英语学习线，但它和主课程完全对齐。",
        "规则很简单：每天跟着当天的编程内容，再补 15 到 25 分钟英语。",
        "",
        "总导航在：`../学习顺序总导航.md`。",
        "",
        "## 这里有什么",
        "",
        "- `100天编程英语路线.md`：按 Day 001 到 Day 100 展开的英语主线",
        "- `阶段1_基础操作英语.md` 到 `阶段5_表达求职英语.md`：按阶段讲重点",
        "- `高频编程英语词块.md`：最值得先记住的一批词",
        "- `每日英语练习模板.md`：每天照着练",
        "- `英语输出句型模板.md`：以后写文档、做演示、面试都能直接套",
        "",
        "## 每天怎么用",
        "",
        "1. 先完成当天的编程主线。",
        "2. 再打开 `100天编程英语路线.md` 找到对应 Day。",
        "3. 朗读句子、抄词、做最短输出。",
        "4. 最后把今天的英语收获写进 `study_logs/dayXXX.md`。",
        "",
        "## 不要怎么学",
        "",
        "- 不要一上来背一大堆孤立单词。",
        "- 不要追求复杂长句。",
        "- 不要只看不读，只读不写。",
        "",
        "## 你的目标",
        "",
        "- 前期：看见常见词不陌生",
        "- 中期：能读懂常见编程句子",
        "- 后期：能写短英文说明、README、演示稿",
        "",
    ]
    return "\n".join(lines) + "\n"


def build_route() -> str:
    lines = [
        "# 100 天编程英语路线",
        "",
        "这份文件和主课程完全同步。",
        "你每天只要找到当天 Day，照着做英语部分即可。",
        "",
    ]
    for stage_name, stage_label, start, end, goal in STAGES:
        lines.extend(
            [
                f"## {stage_label}",
                "",
                f"- 范围：`Day {start:03d}-{end:03d}`",
                f"- 本阶段英语目标：{goal}",
                "",
            ]
        )
        for unit_number in range(start, end + 1):
            unit = UNITS[unit_number - 1]
            words = ", ".join(words_of(unit))
            tasks = route_task(unit)
            lines.extend(
                [
                    f"### Day {unit_number:03d}：{unit['title']}",
                    f"- 核心句子：`{unit['sentence']}`",
                    f"- 高频词：`{words}`",
                    f"- 最小英语任务 1：{tasks[0]}",
                    f"- 最小英语任务 2：{tasks[1]}",
                    f"- 最小英语任务 3：{tasks[2]}",
                    f"- 理解检查：{tasks[3]}",
                    "",
                ]
            )
    return "\n".join(lines) + "\n"


def build_stage_file(stage_label: str, start: int, end: int, goal: str) -> str:
    units = UNITS[start - 1 : end]
    sentences = [unit["sentence"] for unit in units]
    all_words: list[str] = []
    for unit in units:
        for word in words_of(unit):
            if word not in all_words:
                all_words.append(word)

    key_patterns = [
        "I can ...",
        "This program ...",
        "The app ...",
        "Users can ...",
        "I can explain ...",
    ]

    lines = [
        f"# {stage_label}",
        "",
        f"- 范围：`Day {start:03d}-{end:03d}`",
        f"- 核心目标：{goal}",
        "",
        "## 这一阶段英语到底练什么",
        "",
        "- 先做到看见词不陌生。",
        "- 再做到能读懂简单技术句子。",
        "- 最后做到能写 1 到 3 句自己的说明。",
        "",
        "## 这一阶段每天固定动作",
        "",
        "1. 朗读当天句子 3 遍。",
        "2. 抄写当天 6 个词。",
        "3. 用 3 个词写 3 个短句。",
        "4. 用中文解释一句话的技术意思。",
        "",
        "## 这一阶段重点句子",
        "",
    ]
    for sentence in sentences:
        lines.append(f"- `{sentence}`")
    lines.extend(
        [
            "",
            "## 这一阶段最常用的表达开头",
            "",
        ]
    )
    for pattern in key_patterns:
        lines.append(f"- `{pattern}`")
    lines.extend(
        [
            "",
            "## 这一阶段高频词",
            "",
            f"- `{'`, `'.join(all_words[:30])}`",
            "",
            "## 这一阶段收尾输出",
            "",
            "- 能用 2 到 4 句英文说清自己今天写了什么。",
            "- 能用 1 到 2 句英文写出程序作用。",
            "- 能看懂当天句子的主要意思，不要求每个词都精确翻译。",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def build_vocab_file() -> str:
    lines = [
        "# 高频编程英语词块",
        "",
        "这不是全量词典，而是最值得先掌握的一批核心词。",
        "先把这些词练熟，再去吃更大的英文材料。",
        "",
    ]
    for group_name, items in CORE_VOCAB_GROUPS:
        lines.extend([f"## {group_name}", ""])
        for english, chinese in items:
            lines.append(f"- `{english}`：{chinese}")
        lines.append("")
    return "\n".join(lines) + "\n"


def build_template_file() -> str:
    lines = [
        "# 每日英语练习模板",
        "",
        "## 基本信息",
        "",
        "- Day：",
        "- 对应单元：",
        "- 今天的英语句子：",
        "",
        "## 今天先读",
        "",
        "- 我朗读了几遍：",
        "- 哪个词最拗口：",
        "",
        "## 今天要写",
        "",
        "1. 关键词 1：",
        "2. 关键词 2：",
        "3. 关键词 3：",
        "",
        "## 我自己的 3 个英文短句",
        "",
        "1. ",
        "2. ",
        "3. ",
        "",
        "## 中文解释",
        "",
        "- 这句话大意是：",
        "- 这几个词在代码里的意思是：",
        "",
        "## 明天复习什么",
        "",
        "- ",
        "- ",
        "",
    ]
    return "\n".join(lines) + "\n"


def build_output_file() -> str:
    lines = [
        "# 英语输出句型模板",
        "",
        "后面写 README、做演示、做英文说明时，先用这些短句型，不要强行写复杂句。",
        "",
        "## 介绍程序",
        "",
        "- `This program helps users ...`",
        "- `The app can ...`",
        "- `This page shows ...`",
        "",
        "## 介绍功能",
        "",
        "- `Users can add, edit, and delete ...`",
        "- `The API returns JSON data.`",
        "- `The form collects user input.`",
        "",
        "## 介绍问题和修复",
        "",
        "- `The error says ...`",
        "- `I fixed the problem by ...`",
        "- `I tested the result again.`",
        "",
        "## 介绍学习收获",
        "",
        "- `I learned how to ...`",
        "- `Now I can ...`",
        "- `Next I want to improve ...`",
        "",
        "## 介绍项目展示",
        "",
        "- `I built this project for ...`",
        "- `The main flow is simple.`",
        "- `First, the user ... Then, the system ...`",
        "",
        "## 面试和作品集常用句",
        "",
        "- `My role was to build ...`",
        "- `The biggest challenge was ...`",
        "- `I improved the project by ...`",
        "",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    TRACK_DIR.mkdir(parents=True, exist_ok=True)
    README_FILE.write_text(build_readme(), encoding="utf-8")
    ROUTE_FILE.write_text(build_route(), encoding="utf-8")
    VOCAB_FILE.write_text(build_vocab_file(), encoding="utf-8")
    TEMPLATE_FILE.write_text(build_template_file(), encoding="utf-8")
    OUTPUT_FILE.write_text(build_output_file(), encoding="utf-8")
    for filename, stage_label, start, end, goal in STAGES:
        (TRACK_DIR / filename).write_text(build_stage_file(stage_label, start, end, goal), encoding="utf-8")


if __name__ == "__main__":
    main()
