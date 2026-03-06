# Unit 040 Project Pack: Blog System

这个项目包对应 [../../02_units/unit_040.md](../../02_units/unit_040.md) 的里程碑产出：`完成一个可注册登录的博客系统`。

## 你会做出什么

这是一个最小博客系统，包含：

- 用户注册
- 用户登录和退出
- 发布文章
- 首页展示全部文章
- SQLite 数据库存储

## 文件说明

- `app.py`：Flask 应用主文件
- `blog.db`：程序第一次运行后自动生成
- `templates/`：页面模板
- `static/style.css`：页面样式
- `manual_test_checklist.md`：手动测试清单
- `troubleshooting.md`：常见问题排查
- `acceptance_rubric.md`：当前单元完成标准
- `extension_roadmap.md`：后续升级路线

## 如何运行

先安装依赖：

```bash
pip install -r requirements.txt
```

再启动程序：

```bash
python app.py
```

浏览器打开：

```text
http://127.0.0.1:5000
```

## 建议练习顺序

1. 先注册一个账号。
2. 再登录并发布 2 篇文章。
3. 退出登录，再重新登录。
4. 打开 `blog.db`，理解数据已经落盘。

## 你下一步可以扩展什么

- 给文章增加编辑和删除
- 给用户增加个人主页
- 增加评论功能
- 把 SQLite 换成更完整的数据库方案

## 英语词汇

- `register`：注册
- `login`：登录
- `post`：文章
- `author`：作者
- `database`：数据库

