# 单元 072 起步模板：Pydantic 与参数校验

这一份不是最终答案，而是一个可以继续补、继续改的起步包。

## 文件：`app.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "starter"}
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 072 starter pack"
git push
```
