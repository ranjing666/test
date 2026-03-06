# Troubleshooting

## 1. 提示找不到 CSV 文件

原因：

- 你没有在当前项目目录运行

正确方式：

```bash
cd stage3_advanced/07_project_packs/unit_060_data_project
python analyze.py
```

## 2. 提示某一行不能转成数字

原因：

- `minutes` 列里出现了空值或非数字

处理方式：

- 打开 CSV
- 检查 `minutes` 是否全是整数

## 3. 报告没有更新

常见原因：

- 你改了数据但没保存
- 你看的不是当前目录下的 `output/report.md`

## 4. 我想换成自己的数据

做法：

- 保持列名不变：`date,subject,minutes,mood`
- 再把示例行替换成你自己的内容

