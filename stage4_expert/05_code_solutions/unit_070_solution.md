# 单元 070 参考答案：前端项目实战

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`main.py`

```python
import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Li Hua", "Amy", "David"],
        "score": [95, 88, 91],
    }
)

print(df)
print("Average:", df["score"].mean())
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 070 starter pack"
git push
```
