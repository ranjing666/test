# 单元 085 参考答案：稳定性、消息队列与重试

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`main.py`

```python
def solve(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print("Answer:", solve([1, 2, 3, 4]))
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 085 starter pack"
git push
```
