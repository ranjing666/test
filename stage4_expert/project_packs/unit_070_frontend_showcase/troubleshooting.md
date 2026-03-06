# Troubleshooting

## 1. 双击打开后页面空白

检查点：

- `app.js` 是否和 `index.html` 在同一目录
- 浏览器控制台是否有语法报错

## 2. 点击筛选按钮没反应

常见原因：

- `app.js` 没有正确加载

处理方式：

- 打开浏览器开发者工具
- 看 `Console` 有没有报错
- 看 `Network` 是否成功加载 `app.js`

## 3. 样式没有生效

检查点：

- `styles.css` 文件名是否改错
- `index.html` 里的 `<link rel="stylesheet" href="styles.css">` 是否还在

## 4. 手机上布局很挤

处理方式：

- 先检查有没有 `meta viewport`
- 再检查 CSS 里的媒体查询是否被改坏
