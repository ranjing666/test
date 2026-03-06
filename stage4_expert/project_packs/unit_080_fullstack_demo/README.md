# Unit 080 Project Pack: Fullstack Demo

这个项目包对应 [../../units/unit_080.md](../../units/unit_080.md) 的里程碑产出：`完成一个可访问的全栈项目`。

## 你会做出什么

这是一个最小全栈待办项目，包含：

- FastAPI 后端
- CORS 配置
- 前端页面读取接口
- 新增任务
- 切换任务完成状态

## 目录结构

- `backend/main.py`：接口服务
- `backend/requirements.txt`：后端依赖
- `frontend/index.html`：前端入口
- `frontend/app.js`：前端请求和渲染逻辑
- `frontend/styles.css`：前端样式
- `manual_test_checklist.md`：手动测试清单
- `troubleshooting.md`：常见问题排查

## 如何运行

先启动后端：

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

再打开前端：

- 直接双击 `frontend/index.html`
- 或用静态服务器打开 `frontend/`

接口默认地址：

```text
http://127.0.0.1:8000
```

## 你会练到什么

- 什么是前后端数据约定
- 为什么需要 CORS
- 前端如何用 `fetch()` 调接口
- 后端如何返回统一 JSON

## 下一步怎么升级

- 把数据改为数据库存储
- 加用户体系
- 加任务删除接口
- 部署到线上环境

## 英语词汇

- `frontend`：前端
- `backend`：后端
- `cors`：跨域资源共享
- `endpoint`：接口端点
- `payload`：请求数据
