# 英语 + 编程零基础学习仓库

这个仓库现在统一按 `100` 个学习日来组织。

规则很简单：

- `1 个单元 = 1 个学习日`
- 详细的学习步骤仍然保留在对应 `units/unit_XXX.md` 里

## 从哪里开始

如果你现在是零基础，直接按这个顺序走：

1. `START_HERE.md`
2. `100_DAYS_MASTER_PLAN.md`
3. `stage1_foundation/daily_guides/day_001.md`
4. `stage1_foundation/units/unit_001.md`
5. `stage1_foundation/workbooks/unit_001_workbook.md`
6. `stage1_foundation/code_templates/unit_001_template.py`
7. `stage1_foundation/code_solutions/unit_001_solution.py`
8. `stage1_foundation/quizzes/unit_001_quiz.md`
9. `study_logs/day001.md`
10. `LEARNING_PROGRESS_TRACKER.md`

## 现在的仓库结构

```text
.
├── README.md
├── START_HERE.md
├── 100_DAYS_MASTER_PLAN.md
├── PROJECT_PACKS_GUIDE.md
├── PROJECT_PACKS_PROGRESS_TRACKER.md
├── LEARNING_PROGRESS_TRACKER.md
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
8. 在 `LEARNING_PROGRESS_TRACKER.md` 打勾

## 100 天学习路线

- 第 1 阶段：Day 001-010
- 第 2 阶段：Day 011-030
- 第 3 阶段：Day 031-060
- 第 4 阶段：Day 061-085
- 第 5 阶段：Day 086-100

如果你想看完整导航，打开：

- `100_DAYS_MASTER_PLAN.md`

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
