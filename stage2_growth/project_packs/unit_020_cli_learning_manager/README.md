# Unit 020 Project Pack: CLI Learning Manager

这个项目包对应 [../../units/unit_020.md](../../units/unit_020.md) 的里程碑产出：`完成一个命令行学习管理器`。

## 你会做出什么

你会得到一个命令行程序，它可以：

- 查看当前学习任务
- 添加学习任务
- 标记任务已完成
- 删除任务
- 查看完成统计

## 文件说明

- `main.py`：主程序入口，负责菜单和交互
- `storage.py`：读写 JSON 数据
- `sample_data.json`：第一份示例数据
- `learning_tasks.json`：程序第一次保存后自动生成
- `manual_test_checklist.md`：手动测试清单
- `troubleshooting.md`：常见问题排查

## 如何运行

在这个目录打开终端后执行：

```bash
python main.py
```

## 建议你按这个顺序练

1. 先直接运行，理解菜单。
2. 自己添加 2 条任务。
3. 标记 1 条任务为完成。
4. 删掉 1 条任务。
5. 打开 `learning_tasks.json` 看真实保存结果。

## 你下一步可以扩展什么

- 增加优先级字段
- 增加截止日期字段
- 增加“只看未完成任务”
- 增加按关键词搜索

## 英语词汇

- `task`：任务
- `complete`：完成
- `storage`：存储
- `save`：保存
- `delete`：删除
