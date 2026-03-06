from pathlib import Path


def u(title, p1, p2, p3, p4, words, sentence, output):
    return {
        "title": title,
        "prog": [p1, p2, p3, p4],
        "words": words,
        "sentence": sentence,
        "output": output,
    }


PHASES = [
    "基础入门",
    "Python 进阶与小项目",
    "前端与网页基础",
    "后端与数据库基础",
    "算法与问题解决",
    "数据分析与自动化",
    "现代前端开发",
    "现代后端与部署",
    "工程质量与系统能力",
    "作品集、求职与毕业大项目",
]


UNITS = [
    u("认识电脑与开发环境", "文件和文件夹", "扩展名与路径", "编辑器基本操作", "运行 Python 文件", "file, folder, open, save, run, code", "I can open and run a Python file.", "写一份环境认识笔记并运行第一个脚本"),
    u("print 与注释", "print() 输出文本", "字符串和引号", "注释解释代码", "多行输出排版", "print, text, string, comment, line, title", "This program prints text on the screen.", "完成一个带中英文输出的欢迎脚本"),
    u("变量与 input", "变量保存数据", "赋值符号 =", "input() 接收输入", "把输入和输出组合", "variable, value, input, output, ask, answer", "My program can ask and answer simple questions.", "完成一个自我介绍交互程序"),
    u("数字与四则运算", "整数和小数", "加减乘除", "表达式计算", "做一个简单计算器", "number, result, add, subtract, multiply, divide", "The result is shown on the screen.", "完成一个两数计算器"),
    u("字符串与格式化", "字符串拼接", "字符串重复", "基础格式化输出", "len() 与文本长度", "word, sentence, message, format, length, space", "I can format a short message.", "完成一个格式化问候语程序"),
    u("比较运算与布尔值", "True 和 False", "比较运算符", "条件表达式", "if 的第一印象", "true, false, equal, greater, less, check", "I can check whether two values are the same.", "完成一个分数是否及格判断器"),
    u("if / elif / else", "单分支判断", "多分支判断", "缩进规则", "根据输入给出不同结果", "if, else, choice, option, menu, decide", "Please choose one option.", "完成一个天气建议小程序"),
    u("while 循环", "重复执行同一任务", "计数器思维", "结束条件", "break 基础", "repeat, again, count, stop, continue, until", "Repeat the task until the answer is correct.", "完成一个密码重试程序"),
    u("for 循环与 range", "for 遍历数字", "range() 的用法", "累加与计数", "简单嵌套循环", "for, range, each, total, sum, times", "For each number, I do one step.", "完成一个乘法表程序"),
    u("函数入门", "定义函数", "参数", "返回值", "复用代码", "function, call, parameter, return, reuse, useful", "This function returns a useful result.", "完成一个由多个函数组成的小工具箱"),
    u("列表基础", "创建列表", "索引和取值", "append 和 remove", "列表与循环配合", "list, item, first, last, add, remove", "I can keep many items in one list.", "完成一个待办清单基础版"),
    u("列表进阶与清单程序", "切片与遍历", "排序与计数", "列表修改", "列表驱动菜单程序", "order, sort, count, change, task, item", "I can sort and update my task list.", "完成一个可增删改查的清单程序"),
    u("字典基础", "键和值", "读取与修改字典", "遍历字典", "用字典保存信息", "key, value, pair, data, detail, record", "A dictionary stores data with keys and values.", "完成一个学生信息记录器"),
    u("字符串常用方法", "lower upper strip", "split 和 join", "find 和 replace", "文本清洗思维", "clean, split, join, find, replace, text", "I can clean and split text data.", "完成一个文本整理小程序"),
    u("文件读写", "打开文本文件", "读取内容", "写入内容", "with open 语法", "read, write, file, path, save, content", "I can read from and write to a file.", "完成一个记事本保存程序"),
    u("报错与调试", "常见语法错误", "定位报错行", "try except 基础", "调试步骤", "error, fix, debug, problem, trace, check", "I can read an error and try to fix it.", "完成一个报错记录与修复清单"),
    u("模块与 import", "import 标准库", "拆分自己的模块", "模块中的函数", "重复代码抽离", "module, import, library, reuse, organize, share", "I can import code from another file.", "把前面的工具函数拆成多个模块"),
    u("类与对象入门", "类是什么", "对象和属性", "方法", "简单建模", "class, object, attribute, method, model, create", "An object has data and behavior.", "完成一个图书或学生对象练习"),
    u("常用标准库", "random", "datetime", "pathlib", "collections 初步", "random, date, path, time, useful, library", "Python has useful libraries for daily tasks.", "完成一个随机抽签和日期提示工具"),
    u("第一阶段综合项目", "需求拆解", "功能列表", "逐步编码", "测试与复盘", "project, step, feature, test, improve, finish", "I can finish a small project step by step.", "完成一个命令行学习管理器"),
    u("Git 与 GitHub 基础", "仓库概念", "git status add commit", "远程仓库 push pull", "写清晰提交信息", "git, commit, push, pull, branch, repo", "I can save my work with Git.", "把前面的小项目整理并推送到 GitHub"),
    u("HTML 页面骨架", "html head body", "标题段落链接", "图片和列表", "页面结构意识", "html, page, title, link, image, list", "This HTML page has a clear structure.", "完成一个个人介绍网页"),
    u("HTML 表单与语义标签", "form input button", "table 和 list", "header main footer", "语义化标签", "form, input, button, header, footer, table", "This form collects user information.", "完成一个带表单的个人主页"),
    u("CSS 选择器与盒模型", "选择器", "颜色与字体", "margin padding border", "盒模型理解", "style, color, font, border, margin, padding", "I can style a page with CSS.", "完成一个好看的简介页面"),
    u("CSS 布局与响应式", "display 和 position", "flex 基础", "网格布局初步", "移动端适配意识", "layout, flex, grid, mobile, resize, align", "My page can adapt to different screens.", "完成一个响应式着陆页"),
    u("JavaScript 入门", "变量与数据类型", "console.log", "运算和字符串", "浏览器中的脚本", "javascript, browser, value, log, script, type", "I can run simple JavaScript in the browser.", "完成一个网页中的问候脚本"),
    u("JavaScript 控制流", "if 判断", "for 和 while", "函数", "数组和对象初步", "loop, array, object, function, condition, value", "I can control logic in JavaScript.", "完成一个简单网页计算器"),
    u("DOM 与事件", "选择页面元素", "点击事件", "输入事件", "动态修改页面", "dom, event, click, input, update, element", "I can update a page when the user clicks.", "完成一个交互式计数器网页"),
    u("前端小项目练习", "拆解页面需求", "多文件组织", "调试前端问题", "做一个可交互页面", "frontend, page, style, bug, click, project", "I can build a small interactive frontend project.", "完成一个待办网页或问答网页"),
    u("Flask 入门与路由", "安装 Flask", "hello flask", "路由函数", "返回页面内容", "flask, route, server, request, page, run", "A route connects a URL to Python code.", "完成一个最小 Flask 网站"),
    u("Flask 模板与表单", "Jinja 模板", "变量传给页面", "GET 和 POST", "静态资源", "template, form, post, get, render, static", "I can render data into an HTML template.", "完成一个表单提交并显示结果的网站"),
    u("SQL 与 SQLite 基础", "表 行 列", "CREATE INSERT", "SELECT WHERE", "SQLite 文件数据库", "table, row, column, select, insert, query", "SQL helps me read and change data.", "完成一个数据库练习脚本"),
    u("CRUD 应用", "新增数据", "读取数据", "更新数据", "删除数据", "create, read, update, delete, record, database", "A CRUD app can add and change records.", "完成一个待办或记账 CRUD 网站"),
    u("登录注册与会话", "用户模型", "密码哈希概念", "session 基础", "登录状态保护", "user, login, logout, password, session, secure", "Users can log in and keep a session.", "完成一个带登录功能的小网站"),
    u("API 与 JSON", "什么是 API", "JSON 结构", "请求和响应", "设计一个简单接口", "api, json, request, response, data, endpoint", "An API sends and receives JSON data.", "完成一个返回 JSON 的接口"),
    u("requests 与第三方接口", "requests.get", "处理接口数据", "参数与异常", "展示接口结果", "request, data, fetch, parse, result, network", "I can fetch data from a public API.", "完成一个天气或名言查询脚本"),
    u("pytest 测试入门", "assert 断言", "测试函数", "测试异常", "组织测试文件", "test, assert, expected, actual, case, pass", "A test checks whether code works as expected.", "为前面的小程序补上基础测试"),
    u("部署与环境变量", "环境变量", "部署平台认识", "查看日志", "修复线上问题", "deploy, env, log, online, config, error", "I can deploy an app and read logs.", "把一个小项目部署到线上"),
    u("文档与协作流程", "README 结构", "Issue 和分支", "Pull Request 概念", "代码审查意识", "readme, issue, branch, review, document, team", "Good documentation helps teamwork.", "为一个项目写完整 README 和使用说明"),
    u("博客项目实战", "需求拆解", "页面和模型设计", "开发核心功能", "上线与复盘", "blog, post, page, feature, polish, deploy", "I can ship a small but complete blog project.", "完成一个可注册登录的博客系统"),
    u("问题拆解与伪代码", "读题与提炼输入输出", "伪代码", "流程图思维", "小题分步解决", "problem, input, output, step, plan, solve", "I can break a problem into smaller steps.", "完成一组入门算法题并写思路"),
    u("复杂度与性能直觉", "时间复杂度", "空间复杂度", "Big O 直觉", "简单性能对比", "time, space, fast, slow, cost, compare", "Some solutions are faster than others.", "为同一题写两个版本并比较性能"),
    u("数组与字符串题型", "双指针", "计数统计", "滑动窗口初步", "常见数组字符串套路", "array, string, count, window, index, scan", "I can scan an array and keep useful information.", "完成一组数组和字符串练习题"),
    u("哈希表与集合题型", "频次统计", "查重", "映射关系", "集合判断", "hash, set, map, unique, lookup, count", "A hash map can speed up lookups.", "完成一组哈希表题并总结模板"),
    u("栈与队列题型", "后进先出", "先进先出", "用列表和 deque", "模拟真实流程", "stack, queue, push, pop, front, back", "A stack and a queue solve different problems.", "完成一组栈队列练习"),
    u("递归与回溯入门", "递归函数", "递归出口", "调用栈", "回溯尝试与撤销", "recursion, base, call, path, try, backtrack", "Recursion solves a problem by solving smaller ones.", "完成递归和回溯基础题"),
    u("排序与查找", "冒泡和选择排序思想", "Python sort", "二分查找", "查找与排序的关系", "sort, search, binary, order, compare, position", "Sorting can make searching easier.", "完成排序和查找练习集"),
    u("链表与二叉树", "链表节点", "指针思维初步", "树和根节点", "深度和广度遍历直觉", "node, tree, root, next, left, right", "A tree is made of connected nodes.", "完成链表和树的基础题"),
    u("图、堆与贪心初步", "图和边", "BFS 和 DFS 印象", "heapq", "贪心直觉", "graph, edge, heap, greedy, path, priority", "Some problems need a graph or a heap.", "完成图和堆的入门题"),
    u("算法阶段总结项目", "做题复盘", "错题分类", "限时练习", "英文解释思路", "review, pattern, mistake, explain, solution, improve", "I can explain why a solution works.", "整理一份算法错题本和思路手册"),
    u("Pandas 基础", "Series 和 DataFrame", "读取 CSV", "选择行列", "describe 和 info", "dataframe, column, row, csv, summary, table", "I can read a CSV file into pandas.", "完成一个基础数据读取分析脚本"),
    u("数据清洗", "缺失值处理", "去重", "类型转换", "清洗字符串列", "clean, missing, duplicate, type, convert, column", "Clean data is easier to analyze.", "完成一个脏数据清洗脚本"),
    u("数据分析与聚合", "filter 和 sort", "groupby", "merge 基础", "透视表直觉", "group, merge, filter, sort, summary, metric", "I can summarize data by groups.", "完成一个销售或成绩分析脚本"),
    u("数据可视化", "折线图", "柱状图", "标题与标签", "讲故事式展示", "chart, plot, axis, label, compare, trend", "A chart should tell a clear story.", "完成一个图表分析报告"),
    u("网页抓取", "requests 获取网页", "BeautifulSoup 解析", "提取标签内容", "保存抓取结果", "scrape, html, tag, parse, page, extract", "I can extract useful data from a web page.", "完成一个简单网页信息抓取器"),
    u("API 数据采集", "调用公开 API", "参数与分页", "JSON 转表格", "失败重试意识", "api, json, page, token, field, retry", "I can collect data from an API.", "完成一个 API 数据采集脚本"),
    u("文件自动化", "pathlib 遍历文件", "批量改名", "批量整理文件", "生成汇总文件", "path, rename, folder, batch, organize, file", "I can automate boring file tasks.", "完成一个批量整理文件工具"),
    u("Excel 与邮件自动化", "读写 Excel", "格式化表格", "生成通知内容", "自动发送流程概念", "excel, sheet, email, report, send, format", "Automation can save time on repeated office work.", "完成一个日报表自动生成器"),
    u("ETL 管道入门", "抽取数据", "转换数据", "加载到目标文件", "管道脚本结构", "extract, transform, load, pipeline, source, target", "An ETL pipeline moves and cleans data.", "完成一个小型 ETL 管道"),
    u("数据项目实战", "选题和目标", "清洗分析可视化", "写结论", "发布到 GitHub", "dataset, analysis, report, insight, result, publish", "I can finish a complete data project.", "完成一个完整数据分析项目"),
    u("Node、npm 与前端工具链", "Node 作用", "npm install", "package.json", "Vite 开发环境", "node, npm, package, install, script, dev", "I can manage frontend tools with npm.", "搭建一个现代前端开发环境"),
    u("React 组件与 JSX", "组件概念", "JSX 语法", "props 传值", "组件拆分", "react, component, jsx, props, render, ui", "A component helps me build reusable UI.", "完成一个由多个组件组成的页面"),
    u("React 状态与事件", "useState", "事件处理", "列表渲染", "父子组件传值", "state, event, click, list, update, render", "State changes make the UI update.", "完成一个 React 版计数器和清单"),
    u("React Hooks 与表单", "useEffect", "受控输入", "表单校验", "副作用理解", "hook, effect, form, validate, input, submit", "I can manage form state in React.", "完成一个表单收集页面"),
    u("React 路由与 Context", "react-router", "多页面导航", "Context 共享状态", "基础项目结构", "route, page, context, share, navigate, layout", "Context lets components share data.", "完成一个多页面 React 小站"),
    u("React 样式与可访问性", "CSS Modules 或普通 CSS", "响应式组件", "语义化按钮和表单", "键盘可访问性", "style, accessible, button, label, mobile, focus", "Good UI should also be accessible.", "完善前端项目的样式与可访问性"),
    u("React 获取接口数据", "fetch 或 axios", "loading 和 error", "渲染远程数据", "简单缓存思维", "fetch, loading, error, data, remote, api", "I can show API data in a React page.", "完成一个读取接口数据的页面"),
    u("TypeScript 入门", "基础类型", "对象类型", "函数类型", "接口 interface", "type, interface, safe, check, define, object", "TypeScript helps me catch mistakes earlier.", "把一个小组件改写为 TypeScript"),
    u("React + TypeScript", "props 类型标注", "state 类型标注", "接口数据类型", "通用组件意识", "typed, props, state, model, reusable, safe", "I can build React components with clear types.", "完成一个 React + TS 小应用"),
    u("前端项目实战", "项目选题", "页面拆分", "接口联调或假数据", "部署上线", "frontend, project, page, polish, deploy, demo", "I can ship a frontend project for users.", "完成一个可展示的前端作品"),
    u("FastAPI 基础", "FastAPI 项目结构", "路径参数", "查询参数", "自动文档", "fastapi, path, query, endpoint, docs, app", "FastAPI can generate API docs automatically.", "完成一个最小 FastAPI 服务"),
    u("Pydantic 与参数校验", "请求模型", "字段校验", "错误提示", "配置项管理", "model, validate, field, error, setting, schema", "Validation keeps bad data out of my app.", "为接口加入完整参数校验"),
    u("SQLAlchemy 与数据层", "定义模型", "数据库会话", "CRUD 服务层", "迁移意识", "orm, model, session, database, record, service", "The ORM maps Python objects to database tables.", "完成一个带数据库的 FastAPI 服务"),
    u("JWT 鉴权", "注册登录接口", "密码哈希", "JWT 令牌", "权限控制", "token, auth, login, secure, password, access", "A token lets the server know who I am.", "为接口加入登录和权限功能"),
    u("异步、后台任务与限流", "async await", "后台任务", "任务拆分", "限流与保护意识", "async, await, task, queue, rate, limit", "Async code can handle waiting more efficiently.", "完成一个带后台任务的接口"),
    u("Docker 入门", "镜像和容器", "Dockerfile", "docker compose", "本地容器化运行", "docker, image, container, build, run, compose", "Docker helps me run apps in a stable environment.", "把一个 Web 项目容器化"),
    u("Linux 与服务器基本功", "目录和权限", "进程和端口", "日志查看", "服务部署习惯", "linux, server, process, log, port, permission", "I can use basic Linux commands on a server.", "完成一份服务器常用命令清单"),
    u("CI/CD 与 GitHub Actions", "自动测试工作流", "自动构建", "自动部署思路", "失败排查", "workflow, action, build, test, deploy, pipeline", "Automation can run tests after every push.", "为项目加入 GitHub Actions"),
    u("云部署与运维基础", "云平台概览", "环境变量和密钥", "数据库托管", "线上问题排查", "cloud, service, secret, monitor, env, deploy", "A deployed app needs monitoring and care.", "把前后端项目部署到云端"),
    u("全栈集成项目", "前后端联调", "CORS", "接口文档对齐", "上线与运维清单", "fullstack, integrate, cors, api, frontend, backend", "Frontend and backend must agree on data shape.", "完成一个可访问的全栈项目"),
    u("可读代码与重构", "命名规则", "函数拆分", "删除重复代码", "读代码和改代码", "readable, name, refactor, clean, duplicate, improve", "Clean code is easier to read and change.", "重构一个旧项目并写改进说明"),
    u("常见设计模式", "工厂模式", "策略模式", "适配器模式", "事件和观察者思维", "pattern, strategy, factory, adapter, event, design", "A pattern is a reusable design idea.", "在一个小项目中应用 1 到 2 个设计模式"),
    u("测试进阶", "fixture", "mock", "集成测试", "覆盖率", "fixture, mock, integration, coverage, reliable, test", "Better tests make software more reliable.", "为一个项目补全中级测试方案"),
    u("性能优化", "性能分析", "慢查询意识", "缓存基础", "前后端性能检查", "performance, profile, cache, slow, optimize, measure", "I should measure before I optimize.", "完成一个性能优化前后对比报告"),
    u("稳定性、消息队列与重试", "失败重试", "幂等性直觉", "消息队列概念", "任务解耦", "retry, queue, message, stable, fail, recover", "Good systems recover from failures.", "完成一个带重试和队列思路的任务设计"),
    u("系统设计基础", "需求估算", "高层架构图", "读写分离直觉", "可扩展性基础", "system, scale, traffic, database, service, design", "A system design starts from requirements.", "完成一个中小型系统设计说明"),
    u("日志、监控与告警", "结构化日志", "关键指标", "基础监控", "告警和 runbook", "log, metric, monitor, alert, health, trace", "Monitoring helps me find problems earlier.", "为一个项目补齐日志和监控方案"),
    u("安全基础", "输入校验", "权限边界", "常见 Web 风险", "密钥管理", "secure, validate, secret, attack, auth, protect", "Security starts with careful input handling.", "完成一个项目的安全检查清单"),
    u("开源贡献流程", "读 issue", "fork 和分支", "提交 PR", "接受 review", "open source, fork, pull request, review, issue, patch", "I can contribute small improvements to open source.", "完成一次真实或模拟的开源贡献"),
    u("专项方向项目", "选择方向", "制定里程碑", "集中开发", "复盘与展示", "specialize, focus, milestone, deliver, review, improve", "Focused practice helps me go deeper.", "完成一个你主攻方向的专项项目"),
    u("作品集网站与案例包装", "作品集结构", "项目卡片", "案例说明", "个人故事表达", "portfolio, project, story, showcase, profile, demo", "My portfolio should show what I can build.", "完成一个正式作品集网站"),
    u("技术写作与英文文档", "README 重写", "英文教程文章", "API 使用说明", "把复杂内容写清楚", "document, tutorial, explain, example, clear, audience", "Good writing makes technical work easier to learn.", "完成一篇中英结合的技术文章"),
    u("技术表达与英文演示", "口头讲解代码", "录制演示视频", "做简单幻灯片", "回答常见问题", "present, explain, demo, slide, question, answer", "I can explain my project in English.", "完成一次项目英文演示"),
    u("简历、GitHub 与求职材料", "简历结构", "项目描述", "GitHub 主页整理", "投递材料统一", "resume, profile, highlight, skill, project, apply", "My materials should show real work clearly.", "完成一套可投递的求职材料"),
    u("面试总复习", "Python 总复习", "Web 总复习", "SQL 和算法回看", "项目问答模拟", "interview, review, answer, practice, explain, improve", "Practice makes interview answers clearer.", "完成一轮综合模拟面试"),
    u("毕业大项目规划", "问题定义", "用户故事", "功能优先级", "技术架构和里程碑", "capstone, user, feature, milestone, plan, architecture", "A strong project starts with a clear plan.", "完成毕业大项目方案书"),
    u("毕业大项目开发 Sprint 1", "项目骨架", "核心数据模型", "主要接口或页面", "第一个可运行版本", "build, sprint, backend, frontend, model, version", "I can turn a plan into a working first version.", "完成毕业项目第一阶段开发"),
    u("毕业大项目开发 Sprint 2", "核心流程完善", "测试和修复", "体验优化", "部署准备", "feature, test, polish, deploy, refine, improve", "I can improve the project based on testing.", "完成毕业项目第二阶段开发"),
    u("毕业大项目发布与打磨", "上线部署", "使用文档", "演示视频", "Bug 修复和细节打磨", "release, guide, demo, bug, polish, launch", "A finished project needs docs and polishing.", "完成毕业项目发布版"),
    u("最终复盘与以教促学", "知识地图", "教别人解释概念", "长期学习机制", "下一阶段路线", "reflect, teach, habit, roadmap, summary, future", "Teaching is a strong way to learn deeply.", "完成一份总复盘和下一阶段计划"),
]


def build_unit_header(unit_index, day_start, unit):
    unit_number = unit_index + 1
    day_end = day_start + 9
    prog_text = "；".join(unit["prog"])
    return "\n".join(
        [
            f"## 单元 {unit_number:03d}：{unit['title']}（Day {day_start:03d}-{day_end:03d}）",
            f"- 编程焦点：{prog_text}",
            f"- 英语词汇：{unit['words']}",
            f"- 英语句型：`{unit['sentence']}`",
            f"- 本单元产出：{unit['output']}",
            "",
        ]
    )


def build_day_entry(day_number, unit, local_day):
    prog = unit["prog"]
    output = unit["output"]
    start_day = day_number - local_day + 1
    review_range = f"Day {start_day:03d}-{day_number:03d}"

    if local_day == 1:
        coding = f"先理解 `{prog[0]}`，只求知道它是什么、为什么要学。"
        english = f"朗读并认识这些词：{unit['words']}。"
        task = f"读 3 个最小例子；手敲 1 遍；再用中文写出对“{unit['title']}”的第一理解。"
        deliver = f"在学习日志中整理 5 个关键词，并说明 `{prog[0]}` 的作用。"
        check = f"能用自己的话解释 `{prog[0]}` 是什么。"
    elif local_day == 2:
        coding = f"围绕 `{prog[0]}` 做跟练，把昨天看到的内容变成自己能敲出来的代码。"
        english = f"熟悉句型：`{unit['sentence']}`，并尝试自己读 3 遍。"
        task = "重写昨天的例子，主动改 3 个小地方，例如文字、数字、顺序或变量名。"
        deliver = f"得到一个能运行的练习版本，作为“{output}”的第 1 个小部件。"
        check = f"能独立写出一个包含 `{prog[0]}` 的最小例子。"
    elif local_day == 3:
        coding = f"开始学习 `{prog[1]}`，注意它和前一个知识点的关系。"
        english = "把今天遇到的高频词写成一个小词表，并给出中文解释。"
        task = f"先看例子，再自己模仿 2 次，重点观察 `{prog[1]}` 在代码中的位置。"
        deliver = f"补一段学习笔记，说明 `{prog[0]}` 和 `{prog[1]}` 分别负责什么。"
        check = f"能指出一段代码里哪部分属于 `{prog[1]}`。"
    elif local_day == 4:
        coding = f"把 `{prog[0]}` 和 `{prog[1]}` 放在一起练，开始做小题或小改造。"
        english = "把一个英文句子拆开理解，至少认出主语、动词和关键技术词。"
        task = "完成 3 个小练习，每个练习只改一处核心逻辑，避免一次改太多。"
        deliver = "整理一页错题或疑问记录，写出哪里容易混淆。"
        check = f"能自己找出 `{prog[0]}` 和 `{prog[1]}` 的配合方式。"
    elif local_day == 5:
        coding = f"学习 `{prog[2]}`，开始接触更接近真实程序的写法。"
        english = "围绕今天的主题写 3 句很短的英文说明，不追求复杂，只求准确。"
        task = f"看示例、仿写、运行，再自己解释为什么要用 `{prog[2]}`。"
        deliver = f"写一段 80 到 120 字的中文总结，主题是 `{prog[2]}`。"
        check = f"能说明 `{prog[2]}` 解决了什么问题。"
    elif local_day == 6:
        coding = f"把 `{prog[2]}` 和前面的内容结合，完成一组更完整的练习。"
        english = "复习本单元词汇，并把其中 5 个词写进代码注释或学习记录。"
        task = "做 2 到 3 个组合练习，重点是先预测结果，再运行验证。"
        deliver = f"形成“{output}”的练习版雏形。"
        check = "能在不看答案的情况下完成一次跟练。"
    elif local_day == 7:
        coding = f"学习 `{prog[3]}`，为本单元小项目补上最后一块核心能力。"
        english = "听读一句英文描述，再用中文解释这句话的意思和关键词。"
        task = f"先写一个最小例子，再把 `{prog[3]}` 放进正在做的小项目中。"
        deliver = f"列出“{output}”还差哪些功能，形成一个很小的待办清单。"
        check = f"能说清 `{prog[3]}` 在项目里负责哪部分。"
    elif local_day == 8:
        coding = f"进入本单元项目开发日，把 `{prog[0]}`、`{prog[1]}`、`{prog[2]}`、`{prog[3]}` 串起来。"
        english = "把本单元句型和词汇复述一遍，并尝试口头讲解今天写的代码。"
        task = f"围绕“{output}”完成输入、处理、输出三部分，先求能运行，再求美观。"
        deliver = f"得到“{output}”的第 1 个完整可运行版本。"
        check = "能从头到尾演示一次程序运行流程。"
    elif local_day == 9:
        coding = "进入调试和完善日，重点是修 Bug、改命名、补注释、删重复。"
        english = "用简单英文写 3 到 5 句项目说明，例如程序做什么、怎么运行、输入什么。"
        task = "回放报错过程，记录 3 个今天修掉的问题，并写下修复方法。"
        deliver = f"得到“{output}”的优化版，并配一段中英结合说明。"
        check = "能说出至少 3 个自己今天修掉或避免的问题。"
    else:
        coding = f"做 `{review_range}` 总复习，把本单元知识点串成一张小地图。"
        english = "把本单元高频词再读一遍，并复述句型，力求看见就懂大意。"
        task = "整理笔记、运行最终版、提交 GitHub、写周报式总结，并预热下一单元。"
        deliver = f"提交“{output}”最终版，外加一份阶段复盘。"
        check = "能口头复述本单元 5 到 10 个关键点。"

    return "\n".join(
        [
            f"### Day {day_number:03d}",
            f"- 编程：{coding}",
            f"- 英语：{english}",
            f"- 任务：{task}",
            f"- 产出：{deliver}",
            f"- 检查：{check}",
            "",
        ]
    )


def build_master_index():
    lines = [
        "# 1000 天详细学习计划",
        "",
        "这不是一个只有标题的概览，而是一套按天执行的长期学习路线。",
        "",
        "适合对象：",
        "- 中文母语",
        "- 编程零基础或基础很弱",
        "- 英语基础弱但愿意长期积累",
        "- 希望把学习内容持续同步到 GitHub",
        "",
        "## 计划怎么用",
        "",
        "每天建议 90 到 150 分钟：",
        "- 20 分钟：英语词汇和句型",
        "- 45 到 80 分钟：编程主线学习和敲代码",
        "- 15 到 30 分钟：练习、复盘、写学习日志",
        "- 10 分钟：提交代码或整理笔记",
        "",
        "如果当天很忙，不要完全停掉，至少完成这 3 件事：",
        "- 看当天计划",
        "- 敲 10 分钟代码",
        "- 在日志里写 3 句话",
        "",
        "## 阶段总览",
        "",
        "| 阶段 | 天数 | 重点 | 明细文件 |",
        "|------|------|------|----------|",
    ]

    for phase_index, phase_name in enumerate(PHASES):
        start = phase_index * 100 + 1
        end = start + 99
        filename = f"plan_1000_days/day_{start:03d}_{end:03d}.md"
        lines.append(f"| 第 {phase_index + 1} 阶段 | Day {start:03d}-{end:03d} | {phase_name} | [{filename}]({filename}) |")

    lines.extend(
        [
            "",
            "## 学习原则",
            "",
            "1. 先理解最小例子，再自己改例子。",
            "2. 报错不是失败，是学习材料。",
            "3. 每 10 天做一个小项目或整合练习。",
            "4. 编程和英语同时推进，但每次只抓少量重点。",
            "5. 只要不断更，就能逐渐形成自己的 GitHub 学习档案。",
            "",
            "## 和仓库其他资料的关系",
            "",
            "- `从这里开始.md`：适合刚开始时先看。",
            "- `stage1_foundation/`：当前已经有的第一阶段讲义和示例代码。",
            "- `study_logs/`：每日记录、反思、错题和问题统一放这里。",
            "- `plan_1000_days/`：本次生成的按天详细计划。",
            "",
            "## 现在立刻该做什么",
            "",
            "1. 看 `plan_1000_days/day_001_100.md`。",
            "2. 只执行 `Day 001`，不要急着看很远。",
            "3. 完成后填写 `study_logs/day001.md`。",
            "4. 学完几天后，再回头看整体节奏。",
            "",
            "## 说明",
            "",
            "这份计划已经尽量做到：",
            "- 逐级渐进",
            "- 每天有明确任务",
            "- 每 10 天有产出",
            "- 适合长期坚持",
            "",
            "后面如果你要我继续做，我可以基于这套 1000 天计划继续补：",
            "- 每一天的详细讲义",
            "- 每一课的配套代码",
            "- 每周测验",
            "- 每月复盘",
        ]
    )

    return "\n".join(lines) + "\n"


def build_plan_readme():
    lines = [
        "# 1000 天计划目录",
        "",
        "这个目录保存按天展开的 1000 天学习计划。",
        "",
        "使用建议：",
        "- 一次只看今天，不要一次性试图读完 1000 天。",
        "- 每学完 1 天，就去 `study_logs/` 写一份记录。",
        "- 每 10 天至少做一次 Git 提交，把学习痕迹保存到 GitHub。",
        "",
        "## 明细文件",
        "",
    ]

    for block in range(10):
        start = block * 100 + 1
        end = start + 99
        lines.append(f"- [Day {start:03d}-{end:03d}](day_{start:03d}_{end:03d}.md)")

    return "\n".join(lines) + "\n"


def build_block_file(block_index):
    start = block_index * 100 + 1
    end = start + 99
    phase_name = PHASES[block_index]
    lines = [
        f"# Day {start:03d}-{end:03d}",
        "",
        f"阶段主题：{phase_name}",
        "",
        "阅读方式：",
        "- 只执行当前这一天。",
        "- 每 10 天做一个小整合。",
        "- 看不懂时，先跑例子，再回头读解释。",
        "",
    ]

    unit_start = block_index * 10
    for unit_index in range(unit_start, unit_start + 10):
        unit = UNITS[unit_index]
        day_start = unit_index * 10 + 1
        lines.append(build_unit_header(unit_index, day_start, unit))
        for local_day in range(1, 11):
            day_number = day_start + local_day - 1
            lines.append(build_day_entry(day_number, unit, local_day))

    return "\n".join(lines).rstrip() + "\n"


def main():
    if len(UNITS) != 100:
        raise ValueError(f"Expected 100 units, got {len(UNITS)}")

    repo_root = Path(__file__).resolve().parents[1]
    plan_dir = repo_root / "plan_1000_days"
    plan_dir.mkdir(parents=True, exist_ok=True)

    (repo_root / "1000_DAYS_MASTER_PLAN.md").write_text(build_master_index(), encoding="utf-8")
    (plan_dir / "README.md").write_text(build_plan_readme(), encoding="utf-8")

    for block_index in range(10):
        start = block_index * 100 + 1
        end = start + 99
        filename = plan_dir / f"day_{start:03d}_{end:03d}.md"
        filename.write_text(build_block_file(block_index), encoding="utf-8")


if __name__ == "__main__":
    main()
