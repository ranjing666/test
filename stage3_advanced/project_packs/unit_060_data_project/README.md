# Unit 060 Project Pack: Data Project

这个项目包对应 [../../units/unit_060.md](../../units/unit_060.md) 的里程碑产出：`完成一个完整数据分析项目`。

## 你会做出什么

你会得到一个最小的数据项目流程：

- 读取 CSV 数据
- 汇总每天学习时长
- 统计最常见科目
- 生成 Markdown 报告

## 文件说明

- `data/sample_learning_minutes.csv`：示例数据集
- `analyze.py`：分析脚本
- `report_template.md`：报告结构模板
- `output/report.md`：分析脚本运行后生成

## 如何运行

在这个目录打开终端后执行：

```bash
python analyze.py
```

运行后你会看到：

- 终端打印分析摘要
- `output/report.md` 被自动生成或更新

## 建议练习顺序

1. 先运行一次脚本。
2. 打开生成的报告。
3. 自己改几行 CSV 数据再重跑。
4. 观察统计结果怎么变化。

## 你下一步可以扩展什么

- 改成你自己的学习数据
- 增加每周趋势图
- 增加异常值检查
- 后续迁移到 pandas 和 matplotlib

## 英语词汇

- `dataset`：数据集
- `summary`：汇总
- `average`：平均值
- `report`：报告
- `insight`：洞察
