# 英语 + 编程零基础学习仓库

这个仓库现在统一按 `100` 个学习日来组织。

规则很简单：

- `1 个单元 = 1 个学习日`
- 详细的学习步骤仍然保留在对应 `units/unit_XXX.md` 里

## 从哪里开始

如果你现在就开始学，主线按这个顺序走：

1. `stage1_foundation/daily_guides/day_001.md`
2. `stage1_foundation/units/unit_001.md`
3. `stage1_foundation/workbooks/unit_001_workbook.md`
4. `stage1_foundation/code_templates/unit_001_template.py`
5. `stage1_foundation/code_solutions/unit_001_solution.py`
6. `stage1_foundation/quizzes/unit_001_quiz.md`
7. `study_logs/day001.md`
8. `学习进度总看板.md`

补充导航和总览放在这里：

- `从这里开始.md`
- `学习顺序总导航.md`
- `100天学习总计划.md`
- `编程英语同步学习/100天编程英语路线.md`

## 现在的仓库结构

```text
.
├── README.md
├── 从这里开始.md
├── 学习顺序总导航.md
├── 100天学习总计划.md
├── 项目包使用指南.md
├── 项目包进度看板.md
├── 学习进度总看板.md
├── 编程英语同步学习/
├── stage1_foundation/
│   ├── daily_guides/      # Day 001-010，学习日入口
│   ├── units/             # 单元讲义，保留单元内 10 个学习步骤
│   ├── workbooks/
│   ├── code_templates/
│   ├── code_solutions/
│   └── quizzes/
├── stage2_growth/         # Day 011-030
├── stage3_advanced/       # Day 031-060
├── stage4_expert/         # Day 061-085
├── stage5_master/         # Day 086-100
├── study_logs/            # Day 001-100 的学习日志
└── tools/
```

## 现在怎么学

以后统一按这一条主线：

1. 先开 `daily_guides/day_XXX.md`
2. 再看 `units/unit_XXX.md`
3. 再做 `workbooks/unit_XXX_workbook.md`
4. 然后完成 `code_templates/`
5. 卡住时再看 `code_solutions/`
6. 最后做 `quizzes/`
7. 写 `study_logs/dayXXX.md`
8. 在 `学习进度总看板.md` 打勾

主线完成后，再补 `编程英语同步学习/100天编程英语路线.md` 里的当天英语任务。

## 100 天学习路线

- 第 1 阶段：Day 001-010
- 第 2 阶段：Day 011-030
- 第 3 阶段：Day 031-060
- 第 4 阶段：Day 061-085
- 第 5 阶段：Day 086-100

如果你想看完整导航，打开：

- `学习顺序总导航.md`
- `100天学习总计划.md`
- `编程英语同步学习/100天编程英语路线.md`

如果你今天只想开始，不想看太远，直接打开：

- `stage1_foundation/daily_guides/day_001.md`

## 同步到 GitHub

```bash
git add .
git commit -m "Update learning materials"
git push
```

## 仓库自检

```bash
python tools/repo_audit.py
```
