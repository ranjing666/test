# Troubleshooting

## 1. 前端提示 `Failed to fetch`

常见原因：

- FastAPI 后端没有启动
- 接口地址不是 `http://127.0.0.1:8000`

先检查：

```bash
uvicorn main:app --reload
```

## 2. 打开前端后没有任务列表

检查点：

- 后端 `/api/todos` 是否能打开
- 浏览器控制台是否报错
- `frontend/app.js` 里的 `API_BASE` 是否被改坏

## 3. 跨域报错

检查点：

- 后端是否保留了 `CORSMiddleware`
- 是否是从别的端口在请求

## 4. 添加任务后没有刷新

常见原因：

- 请求失败
- 提交后 `loadTodos()` 没执行

排查方式：

- 打开浏览器控制台
- 查看 `Network` 请求状态码
- 查看后端终端有没有报错
