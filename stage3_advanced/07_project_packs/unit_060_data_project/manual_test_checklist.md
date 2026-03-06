# Manual Test Checklist

- [ ] 执行 `python analyze.py` 不报错。
- [ ] 终端会打印总学习时长和最常见科目。
- [ ] `output/report.md` 会被生成或更新。
- [ ] 修改 CSV 里的一条 `minutes` 数据后，重新运行结果会变化。
- [ ] 修改 CSV 里的一条 `subject` 数据后，科目汇总会变化。

## 测试通过标准

- 输入数据能被读取
- 汇总逻辑正确
- 报告输出存在且内容同步
