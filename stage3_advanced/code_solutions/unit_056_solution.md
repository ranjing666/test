# 单元 056 参考答案：API 数据采集

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`main.py`

```python
import requests

response = requests.get("https://api.github.com")
data = response.json()

print("Status:", response.status_code)
print("Current user URL:", data.get("current_user_url"))
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 056 starter pack"
git push
```
