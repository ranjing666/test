# 项目包总指南

这个文件专门讲一件事：怎么使用仓库里的 `project_packs/`。

如果你已经学到某个里程碑单元，不要只看单元讲义，也要看对应项目包。项目包的作用是把“学过的知识点”收束成“一个能做出来的东西”。

## 项目包和普通模板有什么区别

`code_templates/` 更像局部练习。

`project_packs/` 更像完整小项目。

项目包会更强调：

- 目录结构
- 运行方式
- 自测方式
- 常见报错排查
- 可以继续扩展的方向

## 当前项目包地图

### 第 2 阶段

- `stage2_growth/project_packs/unit_020_cli_learning_manager/`
- `stage2_growth/project_packs/unit_030_min_flask_site/`

### 第 3 阶段

- `stage3_advanced/project_packs/unit_040_blog_system/`
- `stage3_advanced/project_packs/unit_060_data_project/`

### 第 4 阶段

- `stage4_expert/project_packs/unit_070_frontend_showcase/`
- `stage4_expert/project_packs/unit_080_fullstack_demo/`

### 第 5 阶段

- `stage5_master/project_packs/unit_090_specialization_kit/`
- `stage5_master/project_packs/unit_100_reflection_kit/`

## 每次怎么用一个项目包

固定按这个顺序，不容易乱：

1. 先看对应单元讲义。
2. 再打开项目包里的 `README.md`。
3. 按运行步骤先跑通最小版本。
4. 再看 `manual_test_checklist.md`，确认核心功能都通了。
5. 如果卡住，再查 `troubleshooting.md`。
6. 最后才开始自己扩展功能。

## 如果你是零基础，最重要的原则

- 一次只改一小步。
- 每改一步就运行一次。
- 先确认“能跑”，再追求“好看”。
- 不要一上来就自己改太多结构。

## 各类项目包的目标差异

### 命令行项目

重点是：

- 输入输出
- 数据保存
- 菜单流程

### Web 项目

重点是：

- 路由
- 模板
- 表单
- 静态资源

### 数据项目

重点是：

- 数据输入
- 统计逻辑
- 结果输出
- 报告表达

### 前端项目

重点是：

- 页面结构
- 数据渲染
- 交互逻辑
- 展示表达

### 全栈项目

重点是：

- 前后端接口对齐
- 请求和响应
- 调试顺序
- 数据结构稳定

### 高阶规划包

重点是：

- 方向选择
- 里程碑
- 交付物
- 复盘和路线

## 什么时候算“真的做完”

至少满足这 4 条：

- 你能跑通它
- 你能解释它每一层在干什么
- 你能改 1 到 2 个小地方而不崩
- 你能写一段自己的总结

## 学完后要做什么

1. 把改动保存。
2. 更新 `study_logs/dayNNN.md`。
3. 在 `LEARNING_PROGRESS_TRACKER.md` 标记进度。
4. 提交到 GitHub。
