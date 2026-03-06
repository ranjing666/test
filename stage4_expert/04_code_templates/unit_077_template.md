# 单元 077 起步模板：Linux 与服务器基本功

这一份不是最终答案，而是一个可以继续补、继续改的起步包。

## 文件：`Dockerfile`

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]
```

## 文件：`workflow.yml`

```yaml
name: basic-check

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 077 starter pack"
git push
```
