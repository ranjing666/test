# Troubleshooting

## 1. 运行后直接报找不到模块

常见原因：

- 你没有在当前项目目录运行

正确方式：

```bash
cd stage2_growth/project_packs/unit_020_cli_learning_manager
python main.py
```

## 2. 新增任务后，下次打开又没了

常见原因：

- 程序没有正常退出
- 你运行的是别的目录下的同名文件

检查方法：

- 看终端最开始打印的 `Data file`
- 确认是不是当前目录里的 `learning_tasks.json`

## 3. 输入编号后提示越界

原因：

- 你输入的任务编号不存在

处理方式：

- 先列出任务
- 再输入 1 到当前任务数之间的数字

## 4. 中文显示乱码

常见原因：

- 终端编码和文件编码不一致

处理方式：

- 优先用 VS Code 终端或 Windows Terminal
- 确认文件保存为 UTF-8
