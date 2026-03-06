from pathlib import Path


UNITS = [
    {
        "unit": 1,
        "title": "认识电脑与开发环境",
        "days": "Day 001-010",
        "goals": [
            "知道什么是文件、文件夹、路径和 `.py` 文件。",
            "会打开编辑器、保存文件、运行第一个 Python 脚本。",
            "知道“改一处、运行一次、看一次结果”的最基本学习方法。",
        ],
        "warmup": [
            "你现在能不能说出“文件”和“文件夹”的区别？",
            "你能不能找到一个 `.py` 文件并说出它是什么？",
            "你知不知道运行程序以后，屏幕上会发生什么？",
        ],
        "guided": [
            "打开编辑器，新建一个 `unit_001_practice.py` 文件。",
            "输入一行 `print(\"Hello\")`，保存并运行它。",
            "把输出文字改成你自己的名字，再运行一遍。",
        ],
        "basic": [
            "写 3 行 `print()`，分别输出：你的名字、你的城市、你的学习目标。",
            "让程序再问你一个问题：`What is your name?`",
            "把程序输出改成中英各一行。",
        ],
        "advanced": [
            "把你的程序做成一个“学习启动画面”，加上分隔线。",
            "尝试自己新建一个不同名字的 `.py` 文件并运行。",
        ],
        "vocab": ["file", "folder", "open", "save", "run", "code"],
        "sentence": "I can open and run a Python file.",
        "project": "完成一个个人学习启动脚本",
        "project_steps": [
            "打印欢迎语。",
            "询问你的名字。",
            "询问你今天要学什么。",
            "输出一句鼓励自己的话。",
        ],
        "checklist": [
            "我会保存 `.py` 文件。",
            "我会运行 Python 文件。",
            "我知道改代码后要重新运行。",
            "我能解释 `print()` 的作用。",
        ],
        "answer_tips": [
            "一开始不需要做复杂功能，只要能运行成功就是进步。",
            "问用户问题时可以先记住 `input()` 这个名字，不要求立刻理解很深。",
        ],
        "template": """# Unit 001 template
# 目标：认识文件、运行脚本、输出和输入

print("=" * 40)
print("My first study launcher")
print("我的第一个学习启动脚本")
print("=" * 40)

name = input("What is your name? ")
goal = input("What do you want to learn today? ")

print()
print("Hello,", name)
print("Today's goal:", goal)
print("Keep going!")
""",
        "solution": """# Unit 001 solution

print("=" * 40)
print("Study Launcher / 学习启动器")
print("=" * 40)

name = input("What is your name? ")
goal = input("What do you want to learn today? ")

print()
print("Hello,", name)
print("Today you will learn:", goal)
print("Step by step, you will improve.")
print("一步一步，你会越来越强。")
""",
    },
    {
        "unit": 2,
        "title": "print 与注释",
        "days": "Day 011-020",
        "goals": [
            "会用 `print()` 输出多行内容。",
            "知道注释是给人看的，不是给电脑看的。",
            "能把程序写得更整齐、更容易读。",
        ],
        "warmup": [
            "你还记得 `print()` 最基本的作用吗？",
            "你知道代码里为什么要写注释吗？",
            "你能看出下面哪一行是注释吗？",
        ],
        "guided": [
            "写一个三行欢迎程序。",
            "在关键位置加中文注释。",
            "再加 1 行英文注释。",
        ],
        "basic": [
            "输出一个标题和两行正文。",
            "写 2 条注释解释你的程序在做什么。",
            "尝试输出一个空行，让版面更清楚。",
        ],
        "advanced": [
            "做一个中英双语欢迎卡片。",
            "自己设计一个 5 行以内的小海报输出。",
        ],
        "vocab": ["print", "text", "string", "comment", "line", "title"],
        "sentence": "This program prints text on the screen.",
        "project": "完成一个带中英文注释的欢迎卡片程序",
        "project_steps": [
            "先打印标题。",
            "再打印中文欢迎语。",
            "再打印英文欢迎语。",
            "用注释解释每一块代码。",
        ],
        "checklist": [
            "我会写单行注释。",
            "我知道注释不会被程序执行。",
            "我会让输出版面更整齐。",
            "我会用 `print()` 输出多行内容。",
        ],
        "answer_tips": [
            "注释不需要写得很花哨，只要能帮助你自己看懂就够了。",
            "版面整齐本身就是一种编程习惯。",
        ],
        "template": """# Unit 002 template
# 请给下面的程序补上合适的输出和注释

# 这里打印标题
print("Welcome Card")

# 这里打印中文欢迎语
print("欢迎来到 Python 世界")

# 这里打印英文欢迎语
print("Welcome to the world of Python")
""",
        "solution": """# Unit 002 solution
# 这个程序用来输出一张简单的欢迎卡片

print("=" * 32)
print("Welcome Card / 欢迎卡片")
print("=" * 32)

# 中文欢迎语
print("欢迎来到 Python 世界")

# 英文欢迎语
print("Welcome to the world of Python")
""",
    },
    {
        "unit": 3,
        "title": "变量与 input",
        "days": "Day 021-030",
        "goals": [
            "知道变量像“带名字的小盒子”。",
            "会用 `input()` 接收名字、城市、兴趣等信息。",
            "会把输入和输出连起来形成一个简单交互程序。",
        ],
        "warmup": [
            "变量为什么要有名字？",
            "输入以后，程序是怎么“记住”你输入的内容的？",
            "变量和字符串有什么区别？",
        ],
        "guided": [
            "让程序问名字。",
            "把名字保存到变量里。",
            "再把变量里的内容输出出来。",
        ],
        "basic": [
            "问用户姓名、城市、兴趣。",
            "分别存到不同变量里。",
            "用 3 行输出这些信息。",
        ],
        "advanced": [
            "做一个自我介绍问答程序。",
            "让程序最后输出一句完整的介绍句子。",
        ],
        "vocab": ["variable", "value", "input", "output", "ask", "answer"],
        "sentence": "My program can ask and answer simple questions.",
        "project": "完成一个交互式自我介绍程序",
        "project_steps": [
            "提问姓名。",
            "提问城市。",
            "提问兴趣。",
            "整合输出一段自我介绍。",
        ],
        "checklist": [
            "我知道 `=` 是赋值，不是数学里的相等。",
            "我会用多个变量保存不同内容。",
            "我会把输入和输出连接起来。",
            "我能说出变量存在的意义。",
        ],
        "answer_tips": [
            "变量名尽量见名知意，例如 `name`、`city`、`hobby`。",
            "输入得到的通常是文本，先不用急着做复杂转换。",
        ],
        "template": """# Unit 003 template

name = input("What is your name? ")
city = input("Which city do you live in? ")
hobby = input("What do you like? ")

print()
print("Name:", name)
print("City:", city)
print("Hobby:", hobby)
""",
        "solution": """# Unit 003 solution

name = input("What is your name? ")
city = input("Which city do you live in? ")
hobby = input("What do you like? ")

print()
print("Hello,", name)
print("You live in", city)
print("You like", hobby)
print("Nice to meet you!")
""",
    },
    {
        "unit": 4,
        "title": "数字与四则运算",
        "days": "Day 031-040",
        "goals": [
            "理解整数、小数和简单运算。",
            "会做加减乘除。",
            "会做一个最基础的两数计算器。",
        ],
        "warmup": [
            "你知道 `+ - * /` 分别代表什么吗？",
            "为什么有时候输入的数字需要转换？",
            "你能预测一个简单表达式的结果吗？",
        ],
        "guided": [
            "先直接输出 2 + 3 的结果。",
            "再让用户输入两个数字。",
            "最后输出加法结果。",
        ],
        "basic": [
            "实现加法和减法。",
            "再补上乘法和除法。",
            "让程序输出清楚的结果标签。",
        ],
        "advanced": [
            "做一个小计算器。",
            "加入一句提醒：除数不能为 0。",
        ],
        "vocab": ["number", "result", "add", "subtract", "multiply", "divide"],
        "sentence": "The result is shown on the screen.",
        "project": "完成一个基础四则运算计算器",
        "project_steps": [
            "输入两个数字。",
            "计算四种结果。",
            "整齐输出。",
            "检查除数是否为 0。",
        ],
        "checklist": [
            "我会使用 `+ - * /`。",
            "我会把输入转成数字。",
            "我知道除法要特别注意 0。",
            "我会输出带标签的结果。",
        ],
        "answer_tips": [
            "这时需要开始认识 `int()` 或 `float()`。",
            "先做正确，再追求漂亮。",
        ],
        "template": """# Unit 004 template

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print()
print("Add:", first_number + second_number)
print("Subtract:", first_number - second_number)
print("Multiply:", first_number * second_number)

if second_number != 0:
    print("Divide:", first_number / second_number)
else:
    print("Divide: cannot divide by zero")
""",
        "solution": """# Unit 004 solution

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

add_result = first_number + second_number
subtract_result = first_number - second_number
multiply_result = first_number * second_number

print()
print("Add:", add_result)
print("Subtract:", subtract_result)
print("Multiply:", multiply_result)

if second_number != 0:
    divide_result = first_number / second_number
    print("Divide:", divide_result)
else:
    print("Divide: cannot divide by zero")
""",
    },
    {
        "unit": 5,
        "title": "字符串与格式化",
        "days": "Day 041-050",
        "goals": [
            "知道字符串就是被引号包起来的文本。",
            "会拼接字符串，知道空格和格式的重要性。",
            "会用更清楚的方式输出一句完整信息。",
        ],
        "warmup": [
            "字符串和数字有什么不同？",
            "为什么拼接文本时有时要自己补空格？",
            "你能读懂一条格式化输出吗？",
        ],
        "guided": [
            "让程序输出 `Hello, Tom` 这样的句子。",
            "把名字改成变量。",
            "再加入城市或目标。",
        ],
        "basic": [
            "做一个欢迎卡片。",
            "输出姓名、城市、目标。",
            "让版面更整齐。",
        ],
        "advanced": [
            "做一个学习信息摘要卡。",
            "用统一风格输出 5 行内容。",
        ],
        "vocab": ["word", "sentence", "message", "format", "length", "space"],
        "sentence": "I can format a short message.",
        "project": "完成一个格式化学习信息卡片",
        "project_steps": [
            "输入姓名。",
            "输入城市。",
            "输入学习目标。",
            "输出整齐卡片。",
        ],
        "checklist": [
            "我知道字符串和数字不是一回事。",
            "我会输出一句完整的格式化信息。",
            "我会让字符串输出更整齐。",
            "我知道空格本身也很重要。",
        ],
        "answer_tips": [
            "新手最容易忽略空格和排版，但它们很影响可读性。",
            "别急着追求复杂格式，先把一条信息说清楚。",
        ],
        "template": """# Unit 005 template

name = input("Your name: ")
city = input("Your city: ")
goal = input("Your goal: ")

print()
print("=" * 30)
print("Study Card")
print("=" * 30)
print(f"Name: {name}")
print(f"City: {city}")
print(f"Goal: {goal}")
""",
        "solution": """# Unit 005 solution

name = input("Your name: ")
city = input("Your city: ")
goal = input("Your goal: ")

print()
print("=" * 30)
print("Study Card / 学习卡片")
print("=" * 30)
print(f"Name: {name}")
print(f"City: {city}")
print(f"Goal: {goal}")
print("=" * 30)
""",
    },
    {
        "unit": 6,
        "title": "比较运算与布尔值",
        "days": "Day 051-060",
        "goals": [
            "知道 True 和 False 是什么。",
            "会做 `==`、`>`、`<` 等基本比较。",
            "会写出“是否通过”“是否成年”这种判断逻辑。",
        ],
        "warmup": [
            "什么时候程序需要回答“是或不是”？",
            "你能区分 `=` 和 `==` 吗？",
            "比较的结果为什么只有两种？",
        ],
        "guided": [
            "让程序判断 5 > 3 的结果。",
            "再让程序比较两个分数。",
            "最后输出是否通过。",
        ],
        "basic": [
            "判断年龄是否成年。",
            "判断分数是否及格。",
            "把判断结果输出成一句完整的话。",
        ],
        "advanced": [
            "同时判断年龄和分数。",
            "输出多个比较结果。",
        ],
        "vocab": ["true", "false", "equal", "greater", "less", "check"],
        "sentence": "I can check whether two values are the same.",
        "project": "完成一个年龄与分数检查器",
        "project_steps": [
            "输入年龄。",
            "输入分数。",
            "判断是否成年。",
            "判断是否及格。",
        ],
        "checklist": [
            "我会写 `==`。",
            "我会做大小比较。",
            "我知道比较结果会变成 True 或 False。",
            "我会把判断结果输出成自然语言。",
        ],
        "answer_tips": [
            "`=` 是赋值，`==` 是比较，这是特别容易混的点。",
            "先直接打印比较结果，再慢慢把它写进更完整的句子里。",
        ],
        "template": """# Unit 006 template

age = int(input("Enter your age: "))
score = int(input("Enter your score: "))

is_adult = age >= 18
is_pass = score >= 60

print()
print("Adult:", is_adult)
print("Pass:", is_pass)
""",
        "solution": """# Unit 006 solution

age = int(input("Enter your age: "))
score = int(input("Enter your score: "))

is_adult = age >= 18
is_pass = score >= 60

print()
print("Adult:", is_adult)
print("Pass:", is_pass)
print("Can move to next step:", is_adult and is_pass)
""",
    },
    {
        "unit": 7,
        "title": "if / elif / else",
        "days": "Day 061-070",
        "goals": [
            "会根据条件执行不同分支。",
            "知道 `if`、`elif`、`else` 的基本结构。",
            "会写一个简单的选择建议程序。",
        ],
        "warmup": [
            "如果天气不同，建议是不是也应该不同？",
            "为什么程序需要“分支”这种能力？",
            "你能看懂三种不同情况的处理逻辑吗？",
        ],
        "guided": [
            "根据分数输出“优秀 / 及格 / 继续努力”。",
            "根据天气输出穿衣建议。",
            "观察缩进位置。",
        ],
        "basic": [
            "根据温度给建议。",
            "根据分数给反馈。",
            "根据时间段输出问候语。",
        ],
        "advanced": [
            "做一个天气建议程序。",
            "做一个简单菜单选择程序。",
        ],
        "vocab": ["if", "else", "choice", "option", "menu", "decide"],
        "sentence": "Please choose one option.",
        "project": "完成一个天气和学习建议程序",
        "project_steps": [
            "输入天气。",
            "输入分数。",
            "分别给出建议。",
            "让输出更清楚。",
        ],
        "checklist": [
            "我知道分支语句为什么存在。",
            "我会写 `if` 和 `else`。",
            "我知道什么时候要用 `elif`。",
            "我知道缩进在 Python 里很重要。",
        ],
        "answer_tips": [
            "先只写两种情况，通了以后再加第三种。",
            "分支很多时，先在纸上列条件再写代码。",
        ],
        "template": """# Unit 007 template

weather = input("Enter weather (sunny/rainy/cold): ")
score = int(input("Enter your score: "))

if weather == "sunny":
    print("Go outside for a short walk.")
elif weather == "rainy":
    print("Stay inside and study.")
else:
    print("Prepare well and keep warm.")

if score >= 90:
    print("Excellent!")
elif score >= 60:
    print("Good job, keep going.")
else:
    print("Review more and try again.")
""",
        "solution": """# Unit 007 solution

weather = input("Enter weather (sunny/rainy/cold): ")
score = int(input("Enter your score: "))

if weather == "sunny":
    print("Weather advice: Go outside for a short walk.")
elif weather == "rainy":
    print("Weather advice: Stay inside and study.")
else:
    print("Weather advice: Prepare well and keep warm.")

if score >= 90:
    print("Study advice: Excellent!")
elif score >= 60:
    print("Study advice: Good job, keep going.")
else:
    print("Study advice: Review more and try again.")
""",
    },
    {
        "unit": 8,
        "title": "while 循环",
        "days": "Day 071-080",
        "goals": [
            "理解“重复直到满足条件”为止。",
            "会写最基本的 `while` 循环。",
            "会做一个简单的重试程序。",
        ],
        "warmup": [
            "什么时候需要让程序重复做一件事？",
            "什么叫结束条件？",
            "如果没有结束条件会发生什么？",
        ],
        "guided": [
            "让程序从 1 打印到 3。",
            "再让程序重复问一个问题。",
            "输入正确答案后结束。",
        ],
        "basic": [
            "写一个密码重试程序。",
            "限制最多重试 3 次。",
            "输出剩余次数。",
        ],
        "advanced": [
            "做一个小型猜词程序。",
            "加入成功和失败两种结束提示。",
        ],
        "vocab": ["repeat", "again", "count", "stop", "continue", "until"],
        "sentence": "Repeat the task until the answer is correct.",
        "project": "完成一个密码重试和倒计数程序",
        "project_steps": [
            "设置正确密码。",
            "设置初始次数。",
            "循环询问。",
            "在成功或次数用完时结束。",
        ],
        "checklist": [
            "我知道 `while` 是“条件满足就继续”。",
            "我会设置计数器。",
            "我会让循环正确结束。",
            "我知道无限循环为什么危险。",
        ],
        "answer_tips": [
            "写循环前先写结束条件。",
            "计数器是新手最需要掌握的循环工具。",
        ],
        "template": """# Unit 008 template

secret = "python"
tries = 3

while tries > 0:
    answer = input("Enter the password: ")

    if answer == secret:
        print("Correct!")
        break

    tries = tries - 1
    print("Wrong password. Tries left:", tries)

print("Program finished.")
""",
        "solution": """# Unit 008 solution

secret = "python"
tries = 3

while tries > 0:
    answer = input("Enter the password: ")

    if answer == secret:
        print("Correct!")
        print("You may continue learning.")
        break

    tries = tries - 1
    print("Wrong password. Tries left:", tries)

if tries == 0:
    print("No tries left.")

print("Program finished.")
""",
    },
    {
        "unit": 9,
        "title": "for 循环与 range",
        "days": "Day 081-090",
        "goals": [
            "理解 `for` 循环是按顺序做很多次。",
            "会用 `range()` 生成数字序列。",
            "会做求和、乘法表、重复输出等基本任务。",
        ],
        "warmup": [
            "如果一件事要做 10 次，你想不想一行一行手写？",
            "为什么 `for` 和 `while` 都是循环，但感觉不一样？",
            "你能猜出 `range(1, 6)` 会包含哪些数字吗？",
        ],
        "guided": [
            "用 `for` 打印 1 到 5。",
            "再计算 1 到 5 的总和。",
            "再输出一个简单乘法表。",
        ],
        "basic": [
            "打印 1 到 10。",
            "计算 1 到 10 的和。",
            "打印 3 的乘法表。",
        ],
        "advanced": [
            "自己做一个 1 到 9 的乘法表。",
            "让程序输出学习天数清单。",
        ],
        "vocab": ["for", "range", "each", "total", "sum", "times"],
        "sentence": "For each number, I do one step.",
        "project": "完成一个求和和乘法表练习程序",
        "project_steps": [
            "打印数字。",
            "累加总和。",
            "输出乘法表。",
            "让版面更清楚。",
        ],
        "checklist": [
            "我会写 `for`。",
            "我会使用 `range()`。",
            "我会做简单累加。",
            "我知道循环变量每轮都会变化。",
        ],
        "answer_tips": [
            "先从很小的范围开始，比如 1 到 3。",
            "求和时别忘了先准备一个初始值。",
        ],
        "template": """# Unit 009 template

total = 0

for number in range(1, 11):
    print("Number:", number)
    total = total + number

print("Total:", total)

print()
for number in range(1, 6):
    print("3 x", number, "=", 3 * number)
""",
        "solution": """# Unit 009 solution

total = 0

for number in range(1, 11):
    print("Number:", number)
    total = total + number

print("Total:", total)

print("=" * 20)
for number in range(1, 10):
    print("3 x", number, "=", 3 * number)
""",
    },
    {
        "unit": 10,
        "title": "函数入门",
        "days": "Day 091-100",
        "goals": [
            "知道函数是“把重复逻辑打包”。",
            "会定义最基础的函数。",
            "会传参数、会返回结果。",
        ],
        "warmup": [
            "如果一段代码要重复写 5 次，怎样更省力？",
            "函数为什么比复制粘贴更好？",
            "参数和返回值分别在干什么？",
        ],
        "guided": [
            "写一个 `say_hello()` 函数。",
            "写一个 `add_numbers()` 函数。",
            "调用这两个函数看结果。",
        ],
        "basic": [
            "定义一个欢迎函数。",
            "定义一个求和函数。",
            "定义一个判断是否及格的函数。",
        ],
        "advanced": [
            "把前面的小逻辑拆成多个函数。",
            "做一个“个人工具箱”程序。",
        ],
        "vocab": ["function", "call", "parameter", "return", "reuse", "useful"],
        "sentence": "This function returns a useful result.",
        "project": "完成一个由多个函数组成的小工具箱",
        "project_steps": [
            "写欢迎函数。",
            "写加法函数。",
            "写判断函数。",
            "在主程序里调用它们。",
        ],
        "checklist": [
            "我知道函数存在的意义。",
            "我会定义函数。",
            "我会传参数。",
            "我会用 `return` 返回结果。",
        ],
        "answer_tips": [
            "不要一开始就写很复杂的函数，先从 2 到 5 行的小函数开始。",
            "把函数想成“有名字的小机器”，输入东西，输出结果。",
        ],
        "template": """# Unit 010 template

def say_hello(name):
    print("Hello,", name)


def add_numbers(first_number, second_number):
    return first_number + second_number


def is_pass(score):
    return score >= 60


say_hello("Student")
print("Add result:", add_numbers(10, 20))
print("Pass result:", is_pass(75))
""",
        "solution": """# Unit 010 solution

def say_hello(name):
    print("Hello,", name)
    print("Keep learning!")


def add_numbers(first_number, second_number):
    return first_number + second_number


def is_pass(score):
    return score >= 60


say_hello("Student")
print("Add result:", add_numbers(10, 20))
print("Pass result:", is_pass(75))
""",
    },
]


def workbook_text(unit):
    vocab = ", ".join(f"`{word}`" for word in unit["vocab"])
    lines = [
        f"# 单元 {unit['unit']:03d} 工作簿：{unit['title']}",
        "",
        f"- 对应范围：{unit['days']}",
        f"- 配套单元讲义：`stage1_foundation/02_units/unit_{unit['unit']:03d}.md`",
        f"- 本工作簿目标：围绕“{unit['project']}”把这一单元真正练起来。",
        "",
        "## 这份工作簿怎么用",
        "",
        "建议顺序：",
        "1. 先看单元讲义。",
        "2. 再做这份工作簿里的练习。",
        "3. 然后打开代码模板自己敲一遍。",
        "4. 最后对照参考答案，但不要一开始就抄答案。",
        "",
        "## 学完这一单元后你要会什么",
        "",
    ]
    lines.extend([f"- {goal}" for goal in unit["goals"]])
    lines.extend(
        [
            "",
            "## 热身复习",
            "",
        ]
    )
    lines.extend([f"{index}. {question}" for index, question in enumerate(unit["warmup"], start=1)])
    lines.extend(
        [
            "",
            "## 跟着做",
            "",
        ]
    )
    lines.extend([f"{index}. {task}" for index, task in enumerate(unit["guided"], start=1)])
    lines.extend(
        [
            "",
            "## 基础练习",
            "",
        ]
    )
    lines.extend([f"{index}. {task}" for index, task in enumerate(unit["basic"], start=1)])
    lines.extend(
        [
            "",
            "## 提升练习",
            "",
        ]
    )
    lines.extend([f"{index}. {task}" for index, task in enumerate(unit["advanced"], start=1)])
    lines.extend(
        [
            "",
            "## 英语小练习",
            "",
            f"- 本单元词汇：{vocab}",
            f"- 本单元句子：`{unit['sentence']}`",
            "- 请把句子读 3 遍，再用中文说出大意。",
            "- 请任选 3 个词，自己造 3 个非常短的技术句子。",
            "",
            "## 小项目作业",
            "",
            f"本单元最终小项目：`{unit['project']}`",
            "",
        ]
    )
    lines.extend([f"{index}. {step}" for index, step in enumerate(unit["project_steps"], start=1)])
    lines.extend(
        [
            "",
            "## 自查清单",
            "",
        ]
    )
    lines.extend([f"- [ ] {item}" for item in unit["checklist"]])
    lines.extend(
        [
            "",
            "## 参考答案方向",
            "",
        ]
    )
    lines.extend([f"- {item}" for item in unit["answer_tips"]])
    lines.extend(
        [
            "",
            "## GitHub 提交建议",
            "",
            "```bash",
            "git add .",
            f'git commit -m "Finish unit {unit["unit"]:03d} workbook practice"',
            "git push",
            "```",
            "",
            "## 学完后请做的最后一件事",
            "",
            "去 `study_logs/` 里写一份学习记录，至少写这 3 句：",
            "- 今天我真正会了什么。",
            "- 今天我最容易错在哪里。",
            "- 明天我要继续做什么。",
        ]
    )
    return "\n".join(lines) + "\n"


def readme_text(title, kind):
    if kind == "03_workbooks":
        intro = "这个目录保存第 1 阶段前 10 个单元的工作簿。每份工作簿都包含练习、英语、小项目和自查清单。"
        suffix = "workbook"
    elif kind == "templates":
        intro = "这个目录保存第 1 阶段前 10 个单元的代码模板。建议先自己补、自己改，再运行。"
        suffix = "template"
    elif kind == "06_quizzes":
        intro = "这个目录保存第 1 阶段前 10 个单元的小测。建议学完一个单元后先独立回答，再对照讲义和代码。"
        suffix = "quiz"
    else:
        intro = "这个目录保存第 1 阶段前 10 个单元的参考答案。建议最后再看。"
        suffix = "solution"
    lines = [f"# {title}", "", intro, "", "## 文件列表", ""]
    for unit in UNITS:
        lines.append(f"- `unit_{unit['unit']:03d}_{suffix}.{'md' if kind == '03_workbooks' else 'py'}` - {unit['title']}")
    return "\n".join(lines) + "\n"


def quiz_text(unit):
    lines = [
        f"# 单元 {unit['unit']:03d} 小测：{unit['title']}",
        "",
        "## 问题",
        "",
        f"1. 请用自己的话解释：`{unit['goals'][0]}`",
        f"2. 请说出这个单元最终小项目：`{unit['project']}` 的最小版本至少要包含什么。",
        f"3. 请把这句英文翻成中文：`{unit['sentence']}`",
        f"4. 请从这些词里任选 3 个，自己写 3 句很短的话：{', '.join(unit['vocab'][:4])}",
        "5. 请写一句：你在这个单元最容易出错的地方是什么？",
        "",
        "## 参考答案方向",
        "",
        "- 第 1 题不要求背标准定义，只要能说出它是干什么的就行。",
        "- 第 2 题重点是先说出最小可运行版，不用一开始就追求复杂。",
        "- 第 3 题大意对就行。",
        "- 第 4 题句子很短也可以，只要体现词义。",
        "- 第 5 题写真实情况，不要写空话。",
        "",
        "## 通过标准",
        "",
        "- 你能不用看资料回答至少 3 题。",
        "- 你知道这个单元自己哪里还不稳。",
        "- 你知道明天该继续补什么。",
    ]
    return "\n".join(lines) + "\n"


def main():
    repo_root = Path(__file__).resolve().parents[1]
    stage_root = repo_root / "stage1_foundation"
    workbook_dir = stage_root / "03_workbooks"
    template_dir = stage_root / "04_code_templates"
    solution_dir = stage_root / "05_code_solutions"
    quiz_dir = stage_root / "06_quizzes"

    workbook_dir.mkdir(parents=True, exist_ok=True)
    template_dir.mkdir(parents=True, exist_ok=True)
    solution_dir.mkdir(parents=True, exist_ok=True)
    quiz_dir.mkdir(parents=True, exist_ok=True)

    (workbook_dir / "README.md").write_text(readme_text("第 1 阶段工作簿目录", "03_workbooks"), encoding="utf-8")
    (template_dir / "README.md").write_text(readme_text("第 1 阶段代码模板目录", "templates"), encoding="utf-8")
    (solution_dir / "README.md").write_text(readme_text("第 1 阶段参考答案目录", "solutions"), encoding="utf-8")
    (quiz_dir / "README.md").write_text(readme_text("第 1 阶段小测目录", "06_quizzes"), encoding="utf-8")

    for unit in UNITS:
        number = unit["unit"]
        (workbook_dir / f"unit_{number:03d}_workbook.md").write_text(workbook_text(unit), encoding="utf-8")
        (template_dir / f"unit_{number:03d}_template.py").write_text(unit["template"], encoding="utf-8")
        (solution_dir / f"unit_{number:03d}_solution.py").write_text(unit["solution"], encoding="utf-8")
        (quiz_dir / f"unit_{number:03d}_quiz.md").write_text(quiz_text(unit), encoding="utf-8")


if __name__ == "__main__":
    main()



