# 英语 + 编程零基础学习仓库

这个仓库现在按“长期教学资料库”来使用。

目标很明确：
- 我负责把后续课程、讲义、练习、词汇、复盘模板持续写进仓库。
- 你负责按顺序学习、练习、提交到 GitHub。
- 所有资料默认用中文讲解，并保留必要的英文原词，帮助你同时提升编程和英语。

## 从哪里开始

如果你现在是零基础，请按这个顺序看：

1. `START_HERE.md`
2. `1000_DAYS_MASTER_PLAN.md`
3. `stage1_foundation/daily_guides/day_001.md`
4. `stage1_foundation/units/README.md`
5. `stage1_foundation/units/unit_001.md`
6. `stage1_foundation/workbooks/unit_001_workbook.md`
7. `stage1_foundation/code_templates/unit_001_template.py`
8. `stage1_foundation/code_solutions/unit_001_solution.py`
9. `stage1_foundation/quizzes/unit_001_quiz.md`
10. `plan_1000_days/day_001_100.md`
11. `stage1_foundation/README.md`
12. `study_logs/day001.md`
13. `LEARNING_PROGRESS_TRACKER.md`

## 现在的仓库结构

```text
.
├── README.md
├── START_HERE.md
├── 1000_DAYS_MASTER_PLAN.md
├── LEARNING_PROGRESS_TRACKER.md    # 1000 天总进度看板
├── plan_1000_days/                 # 按天展开的一千天详细计划
├── stage1_foundation/              # 当前正式使用的入门阶段资料
│   ├── README.md
│   ├── daily_guides/              # Day 001-100 的逐日执行指南
│   ├── units/                     # Day 001-100 的详细单元讲义
│   ├── workbooks/                 # 第 1 阶段前 10 个单元练习包
│   ├── code_templates/            # 第 1 阶段前 10 个单元代码模板
│   ├── code_solutions/            # 第 1 阶段前 10 个单元参考答案
│   └── quizzes/                   # 第 1 阶段前 10 个单元小测
├── stage2_growth/                 # Day 101-300 的详细单元讲义
├── stage3_advanced/               # Day 301-600 的详细单元讲义
├── stage4_expert/                 # Day 601-850 的详细单元讲义
├── stage5_master/                 # Day 851-1000 的详细单元讲义
├── study_logs/                    # 每日记录、每周复盘模板
└── tools/                         # 课程维护脚本，学习时可以忽略
```

## 资料存放规则

以后新的教学资料，统一按下面的规则保存：

- 阶段总览放在 `stageX_xxx/README.md`
- 逐日执行指南放在 `stageX_xxx/daily_guides/day_NNN.md`
- 单元讲义放在 `stageX_xxx/units/unit_NNN.md`
- 练习工作簿放在 `stageX_xxx/workbooks/`
- 配套代码模板和参考答案放在 `stageX_xxx/code_templates/` 与 `stageX_xxx/code_solutions/`
- 小测放在 `stageX_xxx/quizzes/`
- 里程碑项目包放在 `stageX_xxx/project_packs/`
- 学习日志放在 `study_logs/dayNNN.md`
- 每周复盘或总结放在 `study_logs/`

这样做的好处是：

- 你以后打开仓库就知道先学什么
- GitHub 提交历史会留下完整学习轨迹
- 每节课的讲义、词汇、代码、作业都能对应起来

## 长期计划入口

如果你想看完整的一千天路线：

- 先看 `1000_DAYS_MASTER_PLAN.md`
- 再看 `plan_1000_days/day_001_100.md`
- 后面按 `day_101_200.md`、`day_201_300.md` 这样的顺序继续

如果你想直接看“真正能学的详细教材”：

- Day 001-100：先看 `stage1_foundation/daily_guides/README.md`，再配合 `units/`、`workbooks/`、`code_templates/`、`code_solutions/`、`quizzes/`
- Day 101-300：先看 `stage2_growth/daily_guides/README.md`，再配合 `units/`、`workbooks/`、`code_templates/`、`code_solutions/`、`quizzes/`、`project_packs/`
- Day 301-600：先看 `stage3_advanced/daily_guides/README.md`，再配合 `units/`、`workbooks/`、`code_templates/`、`code_solutions/`、`quizzes/`、`project_packs/`
- Day 601-850：先看 `stage4_expert/daily_guides/README.md`，再配合 `units/`、`workbooks/`、`code_templates/`、`code_solutions/`、`quizzes/`、`project_packs/`
- Day 851-1000：先看 `stage5_master/daily_guides/README.md`，再配合 `units/`、`workbooks/`、`code_templates/`、`code_solutions/`、`quizzes/`、`project_packs/`

如果你今天只想开始，不想看太远：

- 先打开 `stage1_foundation/daily_guides/day_001.md`
- 直接打开 `stage1_foundation/units/unit_001.md`
- 再打开 `stage1_foundation/workbooks/unit_001_workbook.md`
- 然后完成 `stage1_foundation/code_templates/unit_001_template.py`
- 卡住时再看 `stage1_foundation/code_solutions/unit_001_solution.py`
- 最后做 `stage1_foundation/quizzes/unit_001_quiz.md`
- 然后执行里面的 `Day 001`
- 然后填写 `study_logs/day001.md`
- 然后在 `LEARNING_PROGRESS_TRACKER.md` 里记录当前位置

### 阶段1：入门基础
- 认识电脑、程序、Python、终端、文件
- 学会 `print()`、变量、`input()`、基本数据类型
- 能写简单的交互式小程序

### 阶段2：继续生长
- 列表、字典、文件、调试、模块、类、标准库
- Git / GitHub、HTML、CSS、JavaScript、DOM、Flask 路由入口
- 从命令行程序过渡到网页和基础 Web 开发

### 阶段3及以后
- 阶段3：Flask、数据库、API、测试、部署、算法、数据分析与自动化
- 阶段4：Node、React、TypeScript、FastAPI、Docker、CI/CD、工程质量
- 阶段5：系统设计、开源、作品集、写作表达、简历面试、毕业大项目

## 如何同步到 GitHub

每次学完并确认文件已经更新后，可以执行：

```bash
git add .
git commit -m "Add lesson materials and study notes"
git push
```

## 已有资料说明

为了避免一套仓库里同时存在多套旧路径，已经清理掉以下旧版重复资料：

- 旧周计划目录 `week01/`
- 旧版总规划 `training_camp_plan.md`
- 旧版综合说明 `programming_guide.md`
- 顶层零散练习脚本

后续正式教学只沿着 `stage1_foundation/` 到 `stage5_master/`、`plan_1000_days/`、`study_logs/` 继续维护。
