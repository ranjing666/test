# 单元 030 参考答案：Flask 入门与路由

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`app.py`

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask 入门与路由"

@app.route("/api/status")
def status():
    return jsonify({"status": "ok", "unit": "030"})

if __name__ == "__main__":
    app.run(debug=True)
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 030 starter pack"
git push
```
