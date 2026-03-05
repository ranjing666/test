# Python 学习笔记 - 第一周
# Python Learning Notes - Week 01

---

## 📚 第1天：认识Python

### 什么是Python？
Python是一种编程语言，就像中文、英文是人类的语言一样，Python是计算机的语言。

**特点：**
- 简单易学 (Easy to learn)
- 功能强大 (Powerful)
- 应用广泛 (Widely used)

### Python能做什么？
- 网站开发 (Web development)
- 数据分析 (Data analysis)
- 人工智能 (Artificial Intelligence)
- 游戏开发 (Game development)
- 自动化脚本 (Automation)

---

## 💻 第2天：安装和运行

### 检查Python版本
打开终端，输入：
```bash
python --version
```

你应该看到类似：`Python 3.14.2`

### 运行Python程序的两种方式

#### 方式1：运行文件
```bash
python hello.py
```

#### 方式2：交互模式
```bash
python
>>> print("Hello")
Hello
>>> exit()
```

---

## 📝 第3天：print() 函数详解

### 基本用法
```python
print("Hello, World!")
```

### 打印多个内容
```python
print("Hello", "World")
# 输出：Hello World
```

### 打印数字
```python
print(100)
print(3.14)
```

### 打印空行
```python
print()
```

### 完整示例
```python
# 打印文字
print("我在学Python")
print("I am learning Python")

# 打印数字
print(2024)

# 打印多个内容
print("我的年龄是", 20)

# 打印空行
print()
print("上面有一个空行")
```

---

## 💡 第4天：注释的使用

### 什么是注释？
注释是给人看的说明，计算机会忽略它。

### 单行注释
```python
# 这是一个注释
print("Hello")  # 这也是注释
```

### 为什么要写注释？
1. **解释代码**：告诉别人（或未来的自己）这段代码做什么
2. **临时禁用代码**：不想删除，但暂时不用
3. **标记待办事项**：提醒自己还有什么要做

### 好的注释示例
```python
# 计算两个数的和
result = 10 + 20

# 显示结果
print(result)
```

### 不好的注释示例
```python
# 打印Hello
print("Hello")  # 这个注释是多余的，代码已经很清楚了
```

---

## 🎯 第5天：字符串 (String)

### 什么是字符串？
字符串就是文字，用引号包起来。

### 三种引号
```python
# 单引号
print('Hello')

# 双引号
print("Hello")

# 三引号（可以多行）
print("""这是
多行
文字""")
```

### 字符串拼接
```python
# 使用 + 号
print("Hello" + "World")  # HelloWorld
print("Hello" + " " + "World")  # Hello World

# 使用逗号（自动加空格）
print("Hello", "World")  # Hello World
```

### 字符串重复
```python
print("Ha" * 3)  # HaHaHa
print("=" * 20)  # ====================
```

### 实用示例
```python
# 制作分隔线
print("=" * 30)
print("欢迎来到Python世界")
print("Welcome to Python World")
print("=" * 30)
```

---

## 🔧 第6天：常见错误和解决

### 错误1：忘记引号
```python
# ❌ 错误
print(Hello)

# ✅ 正确
print("Hello")
```

### 错误2：引号不匹配
```python
# ❌ 错误
print("Hello')

# ✅ 正确
print("Hello")
```

### 错误3：拼写错误
```python
# ❌ 错误
prnit("Hello")

# ✅ 正确
print("Hello")
```

### 错误4：中文括号
```python
# ❌ 错误（中文括号）
print（"Hello"）

# ✅ 正确（英文括号）
print("Hello")
```

### 如何看懂错误信息
```python
>>> print("Hello
  File "<stdin>", line 1
    print("Hello
          ^
SyntaxError: unterminated string literal
```

- `SyntaxError`：语法错误
- `unterminated string literal`：字符串没有结束（忘记关闭引号）

---

## 🎨 第7天：实战练习

### 练习1：自我介绍程序
创建 `about_me.py`：
```python
# 自我介绍程序
# Self Introduction Program

print("=" * 40)
print("自我介绍 / Self Introduction")
print("=" * 40)
print()

# 基本信息
print("姓名 / Name: 张三")
print("年龄 / Age: 20")
print("城市 / City: 北京 Beijing")
print()

# 兴趣爱好
print("我喜欢 / I like:")
print("- 编程 Programming")
print("- 音乐 Music")
print("- 运动 Sports")
print()

print("=" * 40)
print("谢谢！/ Thank you!")
print("=" * 40)
```

### 练习2：制作ASCII艺术
```python
# ASCII艺术
print("  *  ")
print(" *** ")
print("*****")
print(" *** ")
print("  *  ")
```

### 练习3：打印乘法表（预览）
```python
# 简单的乘法表
print("2 x 1 =", 2 * 1)
print("2 x 2 =", 2 * 2)
print("2 x 3 =", 2 * 3)
print("2 x 4 =", 2 * 4)
print("2 x 5 =", 2 * 5)
```

---

## 📊 第8天：本周总结

### 你学会了什么？

#### 1. Python基础概念
- ✅ 什么是编程
- ✅ 什么是Python
- ✅ 如何运行Python程序

#### 2. print() 函数
- ✅ 打印文字
- ✅ 打印数字
- ✅ 打印多个内容
- ✅ 打印空行

#### 3. 注释
- ✅ 单行注释 `#`
- ✅ 注释的作用
- ✅ 何时使用注释

#### 4. 字符串
- ✅ 什么是字符串
- ✅ 单引号和双引号
- ✅ 字符串拼接
- ✅ 字符串重复

#### 5. 调试技能
- ✅ 识别常见错误
- ✅ 读懂错误信息
- ✅ 修复简单bug

### 本周代码统计
```
总行数：约50行
程序数：3个
注释数：约20行
```

---

## 🎯 下周预告

下周我们将学习：
1. **变量 (Variables)**：如何存储数据
2. **输入 (Input)**：如何获取用户输入
3. **数据类型 (Data Types)**：数字、文字的区别
4. **简单计算**：用Python做数学题

### 预习任务
思考这些问题：
- 如何让程序记住一个数字？
- 如何让用户输入自己的名字？
- 如何用Python计算 100 + 200？

---

## 📖 学习资源

### 在线资源
- [Python官方教程](https://docs.python.org/3/tutorial/)
- [菜鸟教程](https://www.runoob.com/python3/)
- [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

### 练习平台
- [Python Tutor](http://pythontutor.com/) - 可视化代码执行
- [Replit](https://replit.com/) - 在线编程环境

### 视频教程
- [B站Python入门](https://www.bilibili.com/video/BV1ex411x7Em/)
- [YouTube Python Tutorial](https://www.youtube.com/watch?v=_uQrJ0TkZlc)

---

## ✅ 本周检查清单

完成后打勾：
- [ ] 成功安装Python
- [ ] 运行了第一个程序
- [ ] 理解print()函数
- [ ] 会写注释
- [ ] 理解字符串
- [ ] 完成3个练习程序
- [ ] 学习了150个英语单词
- [ ] 能用英文介绍自己

---

## 💪 给自己的话

**中文：**
恭喜你完成了第一周的学习！编程的世界很大，但每个高手都是从 `print("Hello")` 开始的。不要着急，慢慢来，每天进步一点点。遇到问题很正常，解决问题的过程就是学习的过程。加油！

**English:**
Congratulations on completing Week 1! The world of programming is vast, but every expert started with `print("Hello")`. Don't rush, take it slow, and make a little progress every day. It's normal to encounter problems - solving them is part of learning. Keep going!

---

**下周见！See you next week!** 🚀
