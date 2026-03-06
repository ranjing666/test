# Unit 030 Project Pack: Minimal Flask Site

这个项目包对应 [../../units/unit_030.md](../../units/unit_030.md) 的里程碑产出：`完成一个最小 Flask 网站`。

## 你会做出什么

你会得到一个最小但完整的网站，包含：

- 首页
- 关于页
- 一个简单的 JSON 状态接口
- 模板文件
- 静态样式文件

## 文件说明

- `app.py`：Flask 应用入口
- `requirements.txt`：依赖说明
- `templates/`：页面模板
- `static/style.css`：样式文件
- `manual_test_checklist.md`：手动测试清单
- `troubleshooting.md`：常见问题排查

## 如何运行

先安装依赖：

```bash
pip install -r requirements.txt
```

再启动程序：

```bash
python app.py
```

然后浏览器打开：

```text
http://127.0.0.1:5000
```

## 推荐你怎么练

1. 先打开首页和关于页。
2. 再访问 `/api/status` 看返回的 JSON。
3. 把网页标题改成你自己的名字。
4. 给首页再加一个学习目标列表。

## 你下一步可以扩展什么

- 新增联系页
- 用表单接收留言
- 把内容改成从 Python 变量传给模板
- 接数据库

## 英语词汇

- `route`：路由
- `template`：模板
- `static`：静态文件
- `server`：服务器
- `response`：响应
