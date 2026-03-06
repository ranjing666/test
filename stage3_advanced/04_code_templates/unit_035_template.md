# 单元 035 起步模板：API 与 JSON

这一份不是最终答案，而是一个可以继续补、继续改的起步包。

## 文件：`main.py`

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 035 starter pack"
git push
```
