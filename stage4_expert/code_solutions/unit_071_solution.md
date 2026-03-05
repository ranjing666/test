# 单元 071 参考答案：FastAPI 基础

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`app.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI 基础"}

@app.get("/health")
def health():
    return {"status": "ok", "unit": "071"}
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 071 starter pack"
git push
```
